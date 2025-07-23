import streamlit as st


# Use storage for Passwords and Users  
#Do we make this private variables in python????????
Test_User = "user123"
Test_Pass = "password123"
Test_Admin_User = "admin"
Test_Admin_Pass = "adminpass"

# Function to display the Login Screen 
def login_screen():
    st.title("Day oFF")
    st.subheader("Login to your account")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Log In")

        if login_button:
            if username == Test_User and password == Test_Pass:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.session_state["role"] = "user" 
                st.success(f"Welcome, {username}!")
                st.rerun() 
            elif username == Test_Admin_User and password == Test_Admin_Pass:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.session_state["role"] = "admin" 
                st.success(f"Welcome, Admin {username}! ")
                st.rerun() 
            else:
                st.error("Invalid username or password.")

#  Function to display the Main Application Screen 
def main_app_screen():
    st.title("Main Screen")
    # We can add the rest of the app stuff here
    #->
    #->
    #->










    # Log out button so we can go back to the login screen
    if st.sidebar.button("Log Out"):
        st.session_state.clear() # Clear all session state variables
        st.rerun() # Rerun to go back to the login screen

# --- Main Application Logic ---
if __name__ == "__main__":
    # Remaking the variables here to avoid error of there not beign variables
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = None
    if "role" not in st.session_state:
        st.session_state["role"] = None

    if st.session_state["logged_in"]:
        main_app_screen()
    else:
        login_screen()