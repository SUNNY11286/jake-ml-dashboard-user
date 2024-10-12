# from flask import Flask, render_template, redirect, url_for, request, session
# from datetime import timedelta, datetime
# import sqlite3

# app = Flask(__name__)
# app.secret_key = "your_secret_key"
# app.permanent_session_lifetime = timedelta(days=10)

# # Database connection
# def get_db_connection():
#     conn = sqlite3.connect('database.db')
#     conn.row_factory = sqlite3.Row
#     return conn

# # Home route
# @app.route("/")
# def home():
#     if "user" in session:
#         return redirect(url_for("dashboard"))
#     return redirect(url_for("login"))

# # Login route
# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         session.permanent = True
#         user = request.form["username"]
#         password = request.form["password"]

#         conn = get_db_connection()
#         user_data = conn.execute("SELECT * FROM users WHERE username = ?", (user,)).fetchone()
#         conn.close()

#         if user_data and user_data["password"] == password:
#             session["user"] = user
#             session["subscription"] = user_data["subscription"]
#             return redirect(url_for("dashboard"))
#         else:
#             return render_template("login.html", error="Invalid Credentials")
#     return render_template("login.html")

# # Registration route
# @app.route("/register", methods=["POST", "GET"])
# def register():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]
#         subscription = request.form["subscription"]

#         conn = get_db_connection()
#         conn.execute("INSERT INTO users (username, password, subscription, created_at) VALUES (?, ?, ?, ?)",
#                      (username, password, subscription, datetime.now()))
#         conn.commit()
#         conn.close()
#         return redirect(url_for("login"))
#     return render_template("register.html")



# import hashlib


# def hash_url(url):
#     return hashlib.sha256(url.encode()).hexdigest()

# @app.route('/streamlit')
# def streamlit_access():
#     if 'user' not in session:
#         return redirect(url_for('login'))  # Redirect to login page if not logged in
#     actual_url = "https://share.streamlit.io/sunny11286/ml-dashboard-code/MLD.py"
#     hashed_url = hash_url(actual_url)
#     return redirect(f"/redirected/{hashed_url}")

# @app.route('/redirected/<hashed_url>')
# def redirected(hashed_url):
#     # Here you can also add logic to validate the hashed URL if needed
#     actual_url = "https://share.streamlit.io/sunny11286/ml-dashboard-code/MLD.py"
#     if hash_url(actual_url) == hashed_url:
#         return redirect(actual_url)
#     return "Invalid Access", 403




# # Dashboard route
# # @app.route("/dashboard")
# # def dashboard():
# #     if "user" in session:
# #         subscription = session["subscription"]
# #         if subscription == "premium" or subscription == "on-demand":
# #             return redirect("https://share.streamlit.io/sunny11286/ml-dashboard-code/MLD.py")
# #         else:
# #             return render_template("subscription.html", subscription=subscription)
# #     else:
# #         return redirect(url_for("login"))
# @app.route("/dashboard")
# def dashboard():
#     if "user" in session:
#         subscription = session["subscription"]
#         if subscription in ["premium", "on-demand"]:
#             return render_template("redirect.html")
#         return render_template("dashboard.html", subscription=subscription)
#     else:
#         return redirect(url_for("login"))
    

# # Subscription options route
# @app.route("/subscription", methods=["POST"])
# def subscription():
#     if "user" in session:
#         subscription = request.form["subscription"]
#         conn = get_db_connection()
#         conn.execute("UPDATE users SET subscription = ? WHERE username = ?", (subscription, session["user"]))
#         conn.commit()
#         conn.close()
#         session["subscription"] = subscription
#         return redirect(url_for("dashboard"))
#     return redirect(url_for("login"))

# # Logout route
# @app.route("/logout")
# def logout():
#     session.pop("user", None)
#     return redirect(url_for("login"))

# if __name__ == "__main__":
#     app.run(debug=True)



























# from flask import Flask, render_template, request, redirect, url_for, session
# from datetime import timedelta, datetime
# import hashlib
# import sqlite3

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# def hash_url(url):
#     return hashlib.sha256(url.encode()).hexdigest()

# # Database connection
# def get_db_connection():
#     conn = sqlite3.connect('database.db')
#     conn.row_factory = sqlite3.Row
#     return conn

# @app.route('/')
# def home():
#     return render_template('login.html')  # Render your login page here

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         conn = get_db_connection()
#         user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
#         conn.close()

#         if user:
#             session['user'] = username
#             session['subscription'] = user['subscription']  # Assuming you have a subscription field
#             return redirect(url_for('dashboard'))

#         return 'Invalid credentials', 403

#     return render_template('login.html')

# # Registration route
# @app.route("/register", methods=["POST", "GET"])
# def register():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]
#         subscription = request.form["subscription"]

#         conn = get_db_connection()
#         conn.execute("INSERT INTO users (username, password, subscription, created_at) VALUES (?, ?, ?, ?)",
#                      (username, password, subscription, datetime.now()))
#         conn.commit()
#         conn.close()
#         return redirect(url_for("login"))
#     return render_template("register.html")


# @app.route('/dashboard')
# def dashboard():
#     if 'user' not in session:
#         return redirect(url_for('login'))

#     return render_template('redirect.html')

# @app.route('/streamlit')
# def streamlit_access():
#     if 'user' not in session:
#         return redirect(url_for('login'))
#     # Check subscription level
#     if session.get('subscription') not in ['pro', 'premium']:
#         return "Access denied. This feature is available for Pro and Premium users only.", 403
    
#     actual_url = "https://share.streamlit.io/sunny11286/ml-dashboard-code/MLD.py"
#     hashed_url = hash_url(actual_url)
#     return redirect(f"/redirected/{hashed_url}")

# @app.route('/redirected/<hashed_url>')
# def redirected(hashed_url):
#     actual_url = "https://share.streamlit.io/sunny11286/ml-dashboard-code/MLD.py"
#     if hash_url(actual_url) == hashed_url:
#         return redirect(actual_url)
#     return "Invalid Access", 403

# @app.route('/logout')
# def logout():
#     session.pop('user', None)
#     session.pop('subscription', None)
#     return redirect(url_for('home'))

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, session
import hashlib
from datetime import timedelta, datetime
import sqlite3
import subprocess
import threading
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Function to start Streamlit app
def run_streamlit():
    subprocess.run(["streamlit", "run", "MLD.py"])

def hash_url(url):
    return hashlib.sha256(url.encode()).hexdigest()

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()

        if user:
            session['user'] = username
            session['subscription'] = user['subscription']  # Assuming you have a subscription field
            return redirect(url_for('dashboard'))

        return 'Invalid credentials', 403

    return render_template('login.html')


# Registration route
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        subscription = request.form["subscription"]

        conn = get_db_connection()
        conn.execute("INSERT INTO users (username, password, subscription, created_at) VALUES (?, ?, ?, ?)",
                     (username, password, subscription, datetime.now()))
        conn.commit()
        conn.close()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    # Determine which action to take based on subscription level
    if session.get('subscription') in ['free', 'on demand']:
        # Run Streamlit app directly
        thread = threading.Thread(target=run_streamlit)
        thread.start()
        time.sleep(2)  # Give it a moment to start
        return render_template('streamlit_running.html')  # Show a message that Streamlit is running
    else:
        return render_template('redirect.html')

@app.route('/streamlit')
def streamlit_access():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    # Check subscription level
    if session.get('subscription') not in ['pro', 'premium']:
        return redirect(url_for('dashboard'))  # Direct to dashboard for free or on-demand users
    
    actual_url = "https://share.streamlit.io/sunny11286/ml-dashboard-code/MLD.py"
    return redirect(actual_url)

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('subscription', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Start the Streamlit app in a separate thread
    thread = threading.Thread(target=run_streamlit)
    thread.start()
    
    # Run the Flask app
    app.run(debug=True)
