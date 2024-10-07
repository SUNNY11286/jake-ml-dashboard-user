7# # from flask import Flask, render_template, request, jsonify
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













import subprocess
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory "database" for demonstration
users = {}

# Dummy subscription plans
subscription_plans = ["Free", "Lite", "Pro", "Full"]

# ----- Routes -----

# Home route (login page)
@app.route('/')
def login():
    return render_template('login.html')

# User registration page
@app.route('/register')
def register():
    return render_template('register.html')

# Handle registration
@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    password = request.form.get('password')
    subscription = request.form.get('subscription')

    if email in users:
        flash('Email already registered. Please login.')
        return redirect(url_for('login'))
    
    # Add new user to "database"
    users[email] = {"password": password, "subscription": subscription}
    flash('Registration successful! Please log in.')
    return redirect(url_for('login'))

# Handle login
@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = users.get(email)

    if user and user['password'] == password:
        session['user'] = email  # Save logged-in user's email
        return redirect(url_for('subscription'))
    else:
        flash('Invalid credentials!')
        return redirect(url_for('login'))

# Subscription management page
@app.route('/subscription')
def subscription():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    user_email = session['user']
    current_plan = users[user_email]['subscription']
    return render_template('subscription.html', current_plan=current_plan, plans=subscription_plans)

# Handle subscription update
@app.route('/update_subscription', methods=['POST'])
def update_subscription():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    new_plan = request.form.get('subscription')
    user_email = session['user']
    users[user_email]['subscription'] = new_plan
    flash(f'Subscription updated to {new_plan}!')
    return redirect(url_for('subscription'))

# Trigger Streamlit app on successful subscription
@app.route('/run_mld')
def run_mld():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    subprocess.Popen(["streamlit", "run", "MLD.py"], shell=True)
    return redirect('http://localhost:8501')

if __name__ == '__main__':
    app.run(debug=True)

