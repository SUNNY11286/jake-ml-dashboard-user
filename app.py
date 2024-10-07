77# # from flask import Flask, render_template, request, jsonify
# # from ml_dashboard import MLDashboard
# # import pandas as pd
# # import io

# # app = Flask(__name__)
# # dashboard = MLDashboard()

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/upload', methods=['POST'])
# # def upload():
# #     if 'file' not in request.files:
# #         return jsonify({'error': 'No file part'})
    
# #     file = request.files['file']
# #     if file.filename == '':
# #         return jsonify({'error': 'No selected file'})
    
# #     if file and file.filename.endswith('.csv'):
# #         stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
# #         data = pd.read_csv(stream)
# #         dashboard.data = data
# #         columns = data.columns.tolist()
# #         return jsonify({'columns': columns})
# #     else:
# #         return jsonify({'error': 'Invalid file type'})

# # @app.route('/process', methods=['POST'])
# # def process():
# #     target = request.form.get('target')
# #     model_type = request.form.get('model_type')
    
# #     if dashboard.data is None:
# #         return jsonify({'error': 'No data uploaded'})
    
# #     results = dashboard.run_dashboard(target, model_type)
# #     return jsonify(results)

# # if __name__ == '__main__':
# #     app.run(debug=True)














# from flask import Flask, render_template, request, redirect, url_for, flash

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # Dummy user data for login and subscription validation
# users = {
#     "user@example.com": {"password": "password123", "subscription": True},
#     "test@domain.com": {"password": "testpass", "subscription": False},
# }

# @app.route('/')
# def login():
#     return render_template('login.html')

# @app.route('/login', methods=['POST'])
# def login_post():
#     email = request.form.get('email')
#     password = request.form.get('password')

#     user = users.get(email)

#     if user and user['password'] == password:
#         if user['subscription']:
#             return redirect(url_for('run_mld'))
#         else:
#             flash('Subscription required!')
#             return redirect(url_for('login'))
#     else:
#         flash('Invalid credentials!')
#         return redirect(url_for('login'))

# @app.route('/run_mld')
# def run_mld():
#     return "Running MLD.py logic"


# # @app.route('/')
# # def login():
# #     return render_template('login.html')

# # @app.route('/login', methods=['POST'])
# # def login_post():
# #     email = request.form.get('email')
# #     password = request.form.get('password')

# #     user = users.get(email)

# #     if user and user['password'] == password:
# #         if user['subscription']:
# #             # Redirect to mld.py
# #             return redirect(url_for('run_mld'))
# #         else:
# #             flash('Subscription required!')
# #             return redirect(url_for('login'))
# #     else:
# #         flash('Invalid credentials!')
# #         return redirect(url_for('login'))

# # @app.route('/run_mld')
# # def run_mld():
# #     # Assuming you import or run MLD.py here
# #     # For now, just return a placeholder response
# #     return "Running MLD.py logic"

# if __name__ == '__main__':
#     app.run(debug=True)
    










# import subprocess
# from flask import Flask, render_template, request, redirect, url_for, flash

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # Dummy user data for login and subscription validation
# users = {
#     "user@example.com": {"password": "password123", "subscription": True},
 #    "test@domain.com": {"password": "testpass", "subscription": False},
# }

# @app.route('/')
# def login():
#     return render_template('login.html')

# @app.route('/login', methods=['POST'])
# def login_post():
#     email = request.form.get('email')
 #    password = request.form.get('password')

 #    user = users.get(email)

   #  if user and user['password'] == password:
     #    if user['subscription']:
       #      # Trigger the Streamlit app
        #     #subprocess.Popen(["streamlit", "run", "MLD_orgi.py"], shell=True)
     #        # Redirect to the Streamlit app URL
           #  return redirect('https://share.streamlit.io/sunny11286/ml-dashboard-code/MLD.py')
      #   else:
      #       flash('Subscription required!')
      #       return redirect(url_for('login'))
   #  else:
     #    flash('Invalid credentials!')
      #   return redirect(url_for('login'))

# if __name__ == '__main__':
  #   app.run(debug=True)

















from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for session handling

# Database Setup
def create_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            subscription TEXT DEFAULT 'free'
        )
    ''')
    conn.commit()
    conn.close()

# Database connection helper function
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Index route - login page
@app.route('/')
def login():
    return render_template('login.html')

# Handle login post request
@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
    conn.close()

    if user and check_password_hash(user['password'], password):
        session['user_id'] = user['id']
        session['subscription'] = user['subscription']
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid credentials!')
        return redirect(url_for('login'))

# Registration route - form
@app.route('/register')
def register():
    return render_template('register.html')

# Handle registration post request
@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    password = request.form.get('password')
    subscription = request.form.get('subscription')  # free, lite, pro, full

    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()

    if user:
        flash('Email address already exists')
        return redirect(url_for('register'))

    hashed_password = generate_password_hash(password, method='sha256')

    conn.execute('INSERT INTO users (email, password, subscription) VALUES (?, ?, ?)',
                 (email, hashed_password, subscription))
    conn.commit()
    conn.close()

    flash('Registration successful! Please log in.')
    return redirect(url_for('login'))

# Dashboard route - user is redirected here after successful login
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', subscription=session['subscription'])

if __name__ == '__main__':
    create_db()  # Ensure the database is created
    app.run(debug=True)