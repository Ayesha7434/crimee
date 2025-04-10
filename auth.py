# import json
# import streamlit as st
# from passlib.hash import pbkdf2_sha256

# class Authentication:
#     @staticmethod
#     def hash_password(password):
#         """Hash the password using PBKDF2."""
#         return pbkdf2_sha256.hash(password)
    
#     @staticmethod
#     def verify_password(stored_password, provided_password):
#         """Verify the provided password against the stored hash."""
#         return pbkdf2_sha256.verify(provided_password, stored_password)
    
#     @staticmethod
#     def load_users():
#         """Load users from JSON file."""
#         try:
#             with open('users.json', 'r') as f:
#                 content = f.read().strip()
#                 # If file is empty, return an empty dictionary
#                 if not content:
#                     return {}
#                 return json.loads(content)
#         except (FileNotFoundError, json.JSONDecodeError):
#             # Create an empty file if it doesn't exist or is invalid
#             with open('users.json', 'w') as f:
#                 json.dump({}, f)
#             return {}
    
#     @staticmethod
#     def save_users(users):
#         """Save users to JSON file."""
#         with open('users.json', 'w') as f:
#             json.dump(users, f, indent=4)
    
#     @staticmethod
#     def register_user(username, password):
#         """Register a new user."""
#         users = Authentication.load_users()
        
#         # Check if username already exists
#         if username in users:
#             st.error("Username already exists!")
#             return False
        
#         # Hash the password and save
#         hashed_password = Authentication.hash_password(password)
#         users[username] = {
#             "password": hashed_password
#         }
        
#         Authentication.save_users(users)
#         st.success("Registration successful!")
#         return True
    
#     @staticmethod
#     def login_user(username, password):
#         """Authenticate a user."""
#         users = Authentication.load_users()
        
#         # Check if user exists
#         if username not in users:
#             st.error("User not found!")
#             return False
        
#         # Verify password
#         if Authentication.verify_password(users[username]["password"], password):
#             st.success("Login successful!")
#             return True
        
#         st.error("Incorrect password!")
#         return False



import json
import streamlit as st
from passlib.hash import pbkdf2_sha256

class Authentication:
    @staticmethod
    def hash_password(password):
        """Hash the password using PBKDF2."""
        return pbkdf2_sha256.hash(password)
    
    @staticmethod
    def verify_password(stored_password, provided_password):
        """Verify the provided password against the stored hash."""
        return pbkdf2_sha256.verify(provided_password, stored_password)
    
    @staticmethod
    def load_users():
        """Load users from JSON file."""
        try:
            with open('users.json', 'r') as f:
                content = f.read().strip()
                # If file is empty, return an empty dictionary
                if not content:
                    return {}
                return json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            # Create an empty file if it doesn't exist or is invalid
            with open('users.json', 'w') as f:
                json.dump({}, f)
            return {}
    
    @staticmethod
    def save_users(users):
        """Save users to JSON file."""
        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)
    
    @staticmethod
    def register_user(username, password, email, phone):
        """Register a new user with email and phone."""
        users = Authentication.load_users()
        
        # Check if username already exists
        if username in users:
            st.error("Username already exists!")
            return False
        
        # Hash the password and save with email and phone
        hashed_password = Authentication.hash_password(password)
        users[username] = {
            "password": hashed_password,
            "email": email,
            "phone": phone
        }
        
        Authentication.save_users(users)
        st.success("Registration successful!")
        return True
    
    @staticmethod
    def login_user(username, password):
        """Authenticate a user."""
        users = Authentication.load_users()
        
        # Check if user exists
        if username not in users:
            st.error("User not found!")
            return False
        
        # Verify password
        if Authentication.verify_password(users[username]["password"], password):
            st.success("Login successful!")
            # Save user info in session state for access across pages
            st.session_state.user_info = {
                "username": username,
                "email": users[username].get("email", ""),
                "phone": users[username].get("phone", "")
            }
            return True
        
        st.error("Incorrect password!")
        return False