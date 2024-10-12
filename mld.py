# import streamlit as st

# # Simulated user database (in practice, fetch from your actual user database)
# users = {
#     "user1": "password1",
#     "user2": "password2",
#     "premium_user": "premium_pass"
# }

# def authenticate(username, password):
#     """Authenticate the user against the simulated user database."""
#     return users.get(username) == password

# # Check if user is logged in
# if 'authenticated' not in st.session_state:
#     st.session_state.authenticated = False

# # User authentication form
# if not st.session_state.authenticated:
#     st.subheader("Please Log In")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type='password')
    
#     if st.button("Login"):
#         if authenticate(username, password):
#             st.session_state.authenticated = True
#             st.session_state.username = username  # Store username in session state
#             st.success(f"Welcome, {username}!")
#         else:
#             st.error("Invalid username or password")

# # If the user is authenticated, show the dashboard
# if st.session_state.authenticated:
#     st.title("Dashboard")
#     st.write(f"Hello, {st.session_state.username}! Here is your dashboard.")

#     # Add your dashboard content here
#     st.write("Dashboard content goes here.")
    
#     # Example content for premium users
#     if username == "premium_user":
#         st.subheader("Premium Features")
#         st.write("Access to premium features is granted.")

#     # Logout option
#     if st.button("Logout"):
#         st.session_state.authenticated = False
#         st.experimental_rerun()  # Refresh the app to show login form again



import streamlit as st
import os

# Simulated user database (replace with your actual database connection)
users = {
    "user1": "password1",
    "user2": "password2",
    "premium_user": "premium_pass"
}

def authenticate(username, password):
    return users.get(username) == password

# Check if user is logged in
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# User authentication form
if not st.session_state.authenticated:
    st.subheader("Please Log In")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid username or password")

# If the user is authenticated, show the dashboard
if st.session_state.authenticated:
    st.title("Dashboard")
    st.write(f"Hello, {st.session_state.username}! Here is your dashboard.")

    # Dashboard content
    st.write("Dashboard content goes here.")
    
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.experimental_rerun()
