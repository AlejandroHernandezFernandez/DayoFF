import streamlit as st
import datetime 
import calendar


# Use storage for Passwords and Users  
#Do we make this private variables in python????????
Test_User = "user123"
Test_Pass = "password123"
Test_Admin_User = "admin"
Test_Admin_Pass = "adminpass"

today = datetime.date.today()
months = ["January", "February", "March", 
          "April", "May", "June", 
          "July", "August", "September", 
          "October", "November", "December"]

current_month = today.month 
current_year = today.year
num_days = calendar.monthrange(current_year,current_month)[1]
first_weekday = (calendar.monthrange(current_year, current_month)[0] + 1) % 7
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
    st.title("Day oFF Tracker!")
    st.subheader(f"{months[current_month-1]}, {current_year}") # <- Prints the current month as a title based on the months list
    # We can add the rest of the app stuff here
    # Prints the days of the month as buttons
    day = 1
    row = 0
    col1, col2, col3, col4 , col5, col6, col7 = st.columns(7)
    cols = [col1, col2, col3, col4, col5, col6, col7]
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    
    for i in range(7):
        cols[i].markdown(f''':orange[{days[i]}]''')

    while day <= num_days:
        for col in range(7):
            if row == 0 and col < first_weekday:
                with cols[col]:
                    st.write("&nbsp;<br>" * 2, unsafe_allow_html=True)
            else:
                with cols[col]:
                    if day <= num_days:
                        if st.button(f"{day}", key =f"{day}"):
                            st.session_state.selected_day = day
                        day+=1
        row +=1 
    #-> We should later make these buttons be able to open a new screen where the info is displayed
    #->
    #->


    if "selected_day" not in st.session_state:
        st.session_state.selected_day = None

    if st.session_state.selected_day:
        day_screen(st.session_state.selected_day, days)










    # Log out button so we can go back to the login screen
    if st.sidebar.button("Log Out"):
        st.session_state.clear() # Clear all session state variables
        st.rerun() # Rerun to go back to the login screen



#-> Function to display the info for the selected day
def day_screen(selected_day, days):
    date_obj = datetime.date(current_year, current_month, selected_day)
    weekday_name = date_obj.strftime("%a")
    st.subheader(f"Details for {weekday_name}, {selected_day}")

    list_of_names = f"name_list{selected_day}"
    if list_of_names not in st.session_state:
        st.session_state[list_of_names] = []

    name = st.text_input("NAME", key= f"name_input{selected_day}")
    if st.button("Take this day off", key=f"add_button{selected_day}"):
        if name.strip():
            st.session_state[list_of_names].append(name.strip())

    if st.session_state[list_of_names]:
        st.write("People who have taken this day off")
        for person in st.session_state[list_of_names]:
            st.write(f"-{person}")




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