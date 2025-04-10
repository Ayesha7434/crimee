
# # import streamlit as st
# # from auth import Authentication
# # from crime_report import CrimeReporting

# # def login_page():
# #     """Login page interface with enhanced styling."""
# #     st.markdown("""
# #     <style>
# #     .login-title {
# #         color: #2c3e50;
# #         text-align: center;
# #         margin-bottom: 30px;
# #     }
# #     .stButton>button {
# #         width: 100%;
# #         background-color: #3498db;
# #         color: white;
# #         border: none;
# #         padding: 10px;
# #         border-radius: 5px;
# #         transition: background-color 0.3s ease;
# #     }
# #     .stButton>button:hover {
# #         background-color: #2980b9;
# #     }
# #     .stTextInput>div>div>input {
# #         border-radius: 5px;
# #         border: 1px solid #bdc3c7;
# #         padding: 10px;
# #     }
# #     </style>
# #     """, unsafe_allow_html=True)
    
# #     st.markdown("<h1 class='login-title'>🚨 Crime Reporting System - Login</h1>", unsafe_allow_html=True)
    
# #     username = st.text_input("Username", placeholder="Enter your username")
# #     password = st.text_input("Password", type="password", placeholder="Enter your password")
    
# #     col1, col2 = st.columns(2)
    
# #     with col1:
# #         if st.button("Login"):
# #             if Authentication.login_user(username, password):
# #                 st.session_state.logged_in = True
# #                 st.session_state.username = username
# #                 st.rerun()
    
# #     with col2:
# #         if st.button("Register New Account"):
# #             st.session_state.show_registration = True
# #             st.rerun()

# # def registration_page():
# #     """User registration interface with enhanced styling."""
# #     st.markdown("""
# #     <style>
# #     .registration-title {
# #         color: #2c3e50;
# #         text-align: center;
# #         margin-bottom: 30px;
# #     }
# #     .stButton>button {
# #         width: 100%;
# #         background-color: #2ecc71;
# #         color: white;
# #         border: none;
# #         padding: 10px;
# #         border-radius: 5px;
# #         transition: background-color 0.3s ease;
# #     }
# #     .stButton>button:hover {
# #         background-color: #27ae60;
# #     }
# #     .stTextInput>div>div>input {
# #         border-radius: 5px;
# #         border: 1px solid #bdc3c7;
# #         padding: 10px;
# #     }
# #     </style>
# #     """, unsafe_allow_html=True)
    
# #     st.markdown("<h1 class='registration-title'>🔐 Crime Reporting System - Registration</h1>", unsafe_allow_html=True)
    
# #     new_username = st.text_input("Choose a Username", placeholder="Enter a unique username")
# #     new_password = st.text_input("Create a Password", type="password", placeholder="Enter a strong password")
# #     confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
    
# #     col1, col2 = st.columns(2)
    
# #     with col1:
# #         if st.button("Create Account"):
# #             if new_password != confirm_password:
# #                 st.error("Passwords do not match!")
# #             elif not new_username or not new_password:
# #                 st.error("Username and password cannot be empty!")
# #             else:
# #                 if Authentication.register_user(new_username, new_password):
# #                     st.session_state.show_registration = False
# #                     st.rerun()
    
# #     with col2:
# #         if st.button("Back to Login"):
# #             st.session_state.show_registration = False
# #             st.rerun()

# # def crime_reporting_page():
# #     """Enhanced crime reporting interface with additional resources."""
# #     st.markdown(f"<h1 style='color: #2c3e50;'>🚨 Crime Reporting - Welcome, {st.session_state.username}</h1>", unsafe_allow_html=True)
    
# #     # Government Reporting Resources
# #     st.markdown("### 🏛️ Official Crime Reporting Resources")
# #     col1, col2 = st.columns(2)
    
# #     with col1:
# #         st.markdown("#### Federal Investigation Agency (FIA)")
# #         st.markdown("[Report to FIA Online](https://www.fia.gov.pk/complaints_dept)", unsafe_allow_html=True)
# #         st.info("Official portal for reporting federal-level crimes")
    
# #     with col2:
# #         st.markdown("#### Bahawalnagar Police District")
# #         st.markdown("""
# #         **Contact Details:**
# #         - Phone: 063-9240053
# #         - Fax: 063-9240077
# #         - E-mail: dpo.bwn@punjabpolice.gov.pk
# #         """)
    
# #     st.divider()
    
# #     # Crime reporting form
# #     with st.form("crime_report_form"):
# #         st.markdown("## 📝 Submit Crime Report")
        
# #         crime_type = st.selectbox("Type of Crime", [
# #             "Theft", "Assault", "Burglary", "Fraud", 
# #             "Cybercrime", "Other"
# #         ])
        
# #         location = st.text_input("Location of Incident")
# #         incident_date = st.date_input("Date of Incident")
# #         description = st.text_area("Detailed Description")
        
# #         # Optional: Severity rating
# #         severity = st.slider("Incident Severity", 1, 10, 5, help="1 being least severe, 10 being most severe")
        
# #         submitted = st.form_submit_button("Submit Report")
        
# #         if submitted:
# #             # Prepare report dictionary with severity
# #             report = {
# #                 "crime_type": crime_type,
# #                 "location": location,
# #                 "incident_date": str(incident_date),
# #                 "description": description,
# #                 "severity": severity
# #             }
            
# #             # Save the report
# #             CrimeReporting.save_report(report)

# # def view_reports_page():
# #     """Enhanced page to view existing crime reports."""
# #     st.markdown("<h1 style='color: #2c3e50;'>📋 Existing Crime Reports</h1>", unsafe_allow_html=True)
    
# #     CrimeReporting.view_reports()
    
# #     # Optional: Filter or search functionality can be added here
# #     st.sidebar.header("Filter Reports")
# #     filter_type = st.sidebar.selectbox("Filter by Crime Type", 
# #         ["All", "Theft", "Assault", "Burglary", "Fraud", "Cybercrime", "Other"]
# #     )

# # def main():
# #     """Main application controller."""
# #     # Initialize session state variables
# #     if 'logged_in' not in st.session_state:
# #         st.session_state.logged_in = False
# #     if 'show_registration' not in st.session_state:
# #         st.session_state.show_registration = False
    
# #     # Sidebar styling
# #     st.markdown("""
# #     <style>
# #     .sidebar .sidebar-content {
# #         background-color: #f1f2f6;
# #     }
# #     .sidebar .sidebar-content .stRadio>div {
# #         background-color: white;
# #         padding: 10px;
# #         border-radius: 5px;
# #     }
# #     </style>
# #     """, unsafe_allow_html=True)
    
# #     # Sidebar for navigation when logged in
# #     if st.session_state.logged_in:
# #         menu = st.sidebar.radio("Navigation", 
# #             ["Report Crime", "View Reports", "Logout"]
# #         )
        
# #         if menu == "Report Crime":
# #             crime_reporting_page()
# #         elif menu == "View Reports":
# #             view_reports_page()
# #         elif menu == "Logout":
# #             st.session_state.logged_in = False
# #             st.rerun()
# #     else:
# #         # Show login or registration page
# #         if st.session_state.show_registration:
# #             registration_page()
# #         else:
# #             login_page()

# # if __name__ == "__main__":
# #     # Page configuration with enhanced styling
# #     st.set_page_config(
# #         page_title="Crime Reporting System", 
# #         page_icon="🚨",
# #         layout="wide"
# #     )
    
# #     main()







# import streamlit as st
# from auth import Authentication
# from crime_report import CrimeReporting
# import time

# def show_popup(message, type="success"):
#     """Show a popup message."""
#     if type == "success":
#         st.success(message)
#     elif type == "error":
#         st.error(message)
#     elif type == "info":
#         st.info(message)
#     elif type == "warning":
#         st.warning(message)
    
#     # Add a progress bar for visual feedback
#     progress_bar = st.progress(0)
#     for percent_complete in range(100):
#         time.sleep(0.01)  # Small delay
#         progress_bar.progress(percent_complete + 1)
    
#     # Remove the progress bar
#     progress_bar.empty()

# def login_page():
#     """Login page interface."""
#     st.title("Crime Reporting System - Login")
    
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         if st.button("Login"):
#             if Authentication.login_user(username, password):
#                 st.session_state.logged_in = True
#                 st.session_state.username = username
#                 st.rerun()
    
#     with col2:
#         if st.button("Register New Account"):
#             st.session_state.show_registration = True
#             st.rerun()

# def registration_page():
#     """User registration interface with email and phone number."""
#     st.title("Crime Reporting System - Registration")
    
#     new_username = st.text_input("Choose a Username")
#     new_password = st.text_input("Create a Password", type="password")
#     confirm_password = st.text_input("Confirm Password", type="password")
#     email = st.text_input("Email Address")
#     phone = st.text_input("Phone Number")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         if st.button("Create Account"):
#             if new_password != confirm_password:
#                 st.error("Passwords do not match!")
#             elif not new_username or not new_password:
#                 st.error("Username and password cannot be empty!")
#             elif not email or not phone:
#                 st.error("Email and phone number are required!")
#             else:
#                 if Authentication.register_user(new_username, new_password, email, phone):
#                     st.session_state.show_registration = False
#                     st.rerun()
    
#     with col2:
#         if st.button("Back to Login"):
#             st.session_state.show_registration = False
#             st.rerun()

# def crime_reporting_page():
#     """Crime reporting interface with popup confirmation."""
#     st.markdown(f"<h1 style='color: #2c3e50;'>🚨 Crime Reporting - Welcome, {st.session_state.username}</h1>", unsafe_allow_html=True)
    
#     # Government Reporting Resources
#     st.markdown("### 🏛️ Official Crime Reporting Resources")
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("#### Federal Investigation Agency (FIA)")
#         st.markdown("[Report to FIA Online](https://www.fia.gov.pk/complaints_dept)", unsafe_allow_html=True)
#         st.info("Official portal for reporting federal-level crimes")
    
#     with col2:
#         st.markdown("#### Bahawalnagar Police District")
#         st.markdown("""
#         **Contact Details:**
#         - Phone: 063-9240053
#         - Fax: 063-9240077
#         - E-mail: dpo.bwn@punjabpolice.gov.pk
#         """)
    
#     # Emergency section
#     st.markdown("### 🚓 Emergency Contacts")
#     emergency_col1, emergency_col2 = st.columns(2)
    
#     with emergency_col1:
#         st.markdown("#### Police Emergency")
#         st.markdown("""
#         **Emergency Numbers:**
#         - National Emergency: 15
#         - Highway Patrol: 130
#         - Rescue Services: 1122
#         """)
#         st.warning("For immediate assistance in life-threatening situations")
    
#     with emergency_col2:
#         st.markdown("#### Women's Helpline")
#         st.markdown("""
#         **Protection Services:**
#         - Women's Helpline: 1043
#         - Child Protection: 1121
#         - Cyber Crime Wing: 9288888
#         """)
    
#     st.divider()
    
#     # Crime reporting form
#     with st.form("crime_report_form"):
#         crime_type = st.selectbox("Type of Crime", [
#             "Theft", "Assault", "Burglary", "Fraud", 
#             "Cybercrime", "Other"
#         ])
        
#         location = st.text_input("Location of Incident")
#         incident_date = st.date_input("Date of Incident")
#         description = st.text_area("Detailed Description")
        
#         # Severity rating
#         severity = st.slider("Incident Severity", 1, 10, 5, help="1 being least severe, 10 being most severe")
        
#         submitted = st.form_submit_button("Submit Report")
        
#         if submitted:
#             # Prepare report dictionary
#             report = {
#                 "crime_type": crime_type,
#                 "location": location,
#                 "incident_date": str(incident_date),
#                 "description": description,
#                 "severity": severity
#             }
            
#             # Save the report
#             report_id = CrimeReporting.save_report(report, st.session_state.username)
            
#             # Show popup
#             show_popup(f"Crime report #{report_id} submitted successfully!")
            
#             # Display notification that they'll be notified on status changes
#             st.info("You will be notified when there are updates to your report status.")

# def view_reports_page():
#     """Page to view existing crime reports with search and filter."""
#     st.markdown("<h1 style='color: #2c3e50;'>📋 Existing Crime Reports</h1>", unsafe_allow_html=True)
    
#     # Search and filter options
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         search_term = st.text_input("Search Reports", placeholder="Search by keywords...")
    
#     with col2:
#         filter_type = st.selectbox("Filter By", 
#             ["None", "Category", "Status", "Date"]
#         )
    
#     with col3:
#         filter_value = None
#         if filter_type == "Category":
#             filter_value = st.selectbox("Select Category", 
#                 ["All", "Theft", "Assault", "Burglary", "Fraud", "Cybercrime", "Other"]
#             )
#             filter_type = "crime_type" if filter_value != "All" else None
#         elif filter_type == "Status":
#             filter_value = st.selectbox("Select Status", 
#                 ["All", "Submitted", "Under Investigation", "Resolved", "Closed"]
#             )
#             filter_type = "status" if filter_value != "All" else None
#         elif filter_type == "Date":
#             filter_value = str(st.date_input("Select Date"))
#             filter_type = "date"
#         else:
#             filter_type = None
    
#     # Clear filters button
#     if st.button("Clear Filters"):
#         search_term = ""
#         filter_type = None
#         filter_value = None
    
#     # View reports with filters
#     CrimeReporting.view_reports(filter_type, filter_value, search_term, st.session_state.username)
    
# def notifications_page():
#     """Page to view notifications."""
#     st.markdown("<h1 style='color: #2c3e50;'>🔔 Your Notifications</h1>", unsafe_allow_html=True)
    
#     reports = CrimeReporting.load_reports()
#     user_reports = [r for r in reports if r.get('reported_by') == st.session_state.username]
    
#     if not user_reports:
#         st.info("You don't have any reports yet.")
#         return
    
#     notifications_found = False
    
#     for report in user_reports:
#         if 'notifications' in report and report['notifications']:
#             notifications_found = True
#             with st.expander(f"Notifications for Report #{report['id']} - {report.get('crime_type')}"):
#                 for notif in report['notifications']:
#                     st.info(f"{notif['message']} - {notif['timestamp']}")
    
#     if not notifications_found:
#         st.info("No notifications yet. You'll be notified when your report status changes.")

# def main():
#     """Main application controller."""
#     # Initialize session state variables
#     if 'logged_in' not in st.session_state:
#         st.session_state.logged_in = False
#     if 'show_registration' not in st.session_state:
#         st.session_state.show_registration = False
#     if 'username' not in st.session_state:
#         st.session_state.username = None
    
#     # Sidebar for navigation when logged in
#     if st.session_state.logged_in:
#         menu = st.sidebar.radio("Navigation", 
#             ["Report Crime", "View Reports", "Notifications", "Logout"]
#         )
        
#         if menu == "Report Crime":
#             crime_reporting_page()
#         elif menu == "View Reports":
#             view_reports_page()
#         elif menu == "Notifications":
#             notifications_page()
#         elif menu == "Logout":
#             st.session_state.logged_in = False
#             st.session_state.username = None
#             st.rerun()
#     else:
#         # Show login or registration page
#         if st.session_state.show_registration:
#             registration_page()
#         else:
#             login_page()

# if __name__ == "__main__":
#     # Page configuration
#     st.set_page_config(
#         page_title="Crime Reporting System", 
#         page_icon="🚨",
#         layout="wide"
#     )
    
#     main()






import streamlit as st
from auth import Authentication
from crime_report import CrimeReporting
import time

def show_popup(message, type="success"):
    """Show a popup message."""
    if type == "success":
        st.success(message)
    elif type == "error":
        st.error(message)
    elif type == "info":
        st.info(message)
    elif type == "warning":
        st.warning(message)
    
    # Add a progress bar for visual feedback
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)  # Small delay
        progress_bar.progress(percent_complete + 1)
    
    # Remove the progress bar
    progress_bar.empty()

def login_page():
    """Login page interface."""
    st.title("Crime Reporting System - Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Login"):
            if Authentication.login_user(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
    
    with col2:
        if st.button("Register New Account"):
            st.session_state.show_registration = True
            st.rerun()

def registration_page():
    """User registration interface with email and phone number."""
    st.title("Crime Reporting System - Registration")
    
    new_username = st.text_input("Choose a Username")
    new_password = st.text_input("Create a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Create Account"):
            if new_password != confirm_password:
                st.error("Passwords do not match!")
            elif not new_username or not new_password:
                st.error("Username and password cannot be empty!")
            elif not email or not phone:
                st.error("Email and phone number are required!")
            else:
                if Authentication.register_user(new_username, new_password, email, phone):
                    st.session_state.show_registration = False
                    st.rerun()
    
    with col2:
        if st.button("Back to Login"):
            st.session_state.show_registration = False
            st.rerun()

def crime_reporting_page():
    """Crime reporting interface with popup confirmation."""
    st.markdown(f"<h1 style='color: #2c3e50;'>🚨 Crime Reporting - Welcome, {st.session_state.username}</h1>", unsafe_allow_html=True)
    
    # Government Reporting Resources
    st.markdown("### 🏛️ Official Crime Reporting Resources")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Federal Investigation Agency (FIA)")
        st.markdown("[Report to FIA Online](https://www.fia.gov.pk/complaints_dept)", unsafe_allow_html=True)
        st.info("Official portal for reporting federal-level crimes")
    
    with col2:
        st.markdown("#### Bahawalnagar Police District")
        st.markdown("""
        **Contact Details:**
        - Phone: 063-9240053
        - Fax: 063-9240077
        - E-mail: dpo.bwn@punjabpolice.gov.pk
        """)
    
    # Emergency section
    st.markdown("### 🚓 Emergency Contacts")
    emergency_col1, emergency_col2 = st.columns(2)
    
    with emergency_col1:
        st.markdown("#### Police Emergency")
        st.markdown("""
        **Emergency Numbers:**
        - National Emergency: 15
        - Highway Patrol: 130
        - Rescue Services: 1122
        """)
        st.warning("For immediate assistance in life-threatening situations")
    
    with emergency_col2:
        st.markdown("#### Women's Helpline")
        st.markdown("""
        **Protection Services:**
        - Women's Helpline: 1043
        - Child Protection: 1121
        - Cyber Crime Wing: 9288888
        """)
    
    st.divider()
    
    # Crime reporting form
    with st.form("crime_report_form"):
        crime_type = st.selectbox("Type of Crime", [
            "Theft", "Assault", "Burglary", "Fraud", 
            "Cybercrime", "Other"
        ])
        
        location = st.text_input("Location of Incident")
        incident_date = st.date_input("Date of Incident")
        description = st.text_area("Detailed Description")
        
        # Severity rating
        severity = st.slider("Incident Severity", 1, 10, 5, help="1 being least severe, 10 being most severe")
        
        submitted = st.form_submit_button("Submit Report")
        
        if submitted:
            # Prepare report dictionary
            report = {
                "crime_type": crime_type,
                "location": location,
                "incident_date": str(incident_date),
                "description": description,
                "severity": severity
            }
            
            # Save the report
            report_id = CrimeReporting.save_report(report, st.session_state.username)
            
            # Show popup
            show_popup(f"Crime report #{report_id} submitted successfully!")
            
            # Display notification that they'll be notified on status changes
            st.info("You will be notified when there are updates to your report status.")

def view_reports_page():
    """Page to view existing crime reports with search and filter."""
    st.markdown("<h1 style='color: #2c3e50;'>📋 Existing Crime Reports</h1>", unsafe_allow_html=True)
    
    # Search and filter options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        search_term = st.text_input("Search Reports", placeholder="Search by keywords...")
    
    with col2:
        filter_type = st.selectbox("Filter By", 
            ["None", "Category", "Status", "Date"]
        )
    
    with col3:
        filter_value = None
        if filter_type == "Category":
            filter_value = st.selectbox("Select Category", 
                ["All", "Theft", "Assault", "Burglary", "Fraud", "Cybercrime", "Other"]
            )
            filter_type = "crime_type" if filter_value != "All" else None
        elif filter_type == "Status":
            filter_value = st.selectbox("Select Status", 
                ["All", "Submitted", "Under Investigation", "Resolved", "Closed"]
            )
            filter_type = "status" if filter_value != "All" else None
        elif filter_type == "Date":
            filter_value = str(st.date_input("Select Date"))
            filter_type = "date"
        else:
            filter_type = None
    
    # Clear filters button
    if st.button("Clear Filters"):
        search_term = ""
        filter_type = None
        filter_value = None
        st.rerun()
    
    # View reports with filters
    CrimeReporting.view_reports(filter_type, filter_value, search_term, st.session_state.username)
    
def notifications_page():
    """Page to view notifications."""
    st.markdown("<h1 style='color: #2c3e50;'>🔔 Your Notifications</h1>", unsafe_allow_html=True)
    
    reports = CrimeReporting.load_reports()
    
    # Filter for user's reports
    user_reports = [r for r in reports if r.get('reported_by') == st.session_state.username]
    
    if not user_reports:
        st.info("You don't have any reports yet.")
        return
    
    # Notification counter
    total_notifications = sum(1 for r in user_reports if 'notifications' in r for _ in r['notifications'])
    st.caption(f"You have {total_notifications} total notifications")
    
    notifications_found = False
    
    for report in user_reports:
        if 'notifications' in report and report['notifications']:
            notifications_found = True
            with st.expander(f"Notifications for Report #{report['id']} - {report.get('crime_type')}"):
                for notif in report['notifications']:
                    st.info(f"{notif['message']} - {notif['timestamp']}")
                
                # Add link to view the full report
                if st.button(f"View Full Report #{report['id']}", key=f"view_from_notif_{report['id']}"):
                    st.session_state.view_report_id = report['id']
                    st.session_state.active_tab = "View Reports"
                    st.rerun()
    
    if not notifications_found:
        st.info("No notifications yet. You'll be notified when your report status changes.")

def account_page():
    """User account page to view and update personal information."""
    st.markdown(f"<h1 style='color: #2c3e50;'>👤 Your Account</h1>", unsafe_allow_html=True)
    
    # Get user information from session state
    if 'user_info' in st.session_state:
        user_info = st.session_state.user_info
        
        st.write(f"**Username:** {user_info.get('username', '')}")
        st.write(f"**Email:** {user_info.get('email', '')}")
        st.write(f"**Phone:** {user_info.get('phone', '')}")
        
        # Show user's report statistics
        reports = CrimeReporting.load_reports()
        user_reports = [r for r in reports if r.get('reported_by') == st.session_state.username]
        
        st.write(f"**Total Reports:** {len(user_reports)}")
        
        # Count reports by status
        status_counts = {}
        for report in user_reports:
            status = report.get('status', 'Submitted')
            if status in status_counts:
                status_counts[status] += 1
            else:
                status_counts[status] = 1
        
        # Display status counts
        if status_counts:
            st.write("**Reports by Status:**")
            for status, count in status_counts.items():
                st.write(f"- {status}: {count}")
    else:
        st.error("User information not available.")

def main():
    """Main application controller."""
    # Initialize session state variables
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'show_registration' not in st.session_state:
        st.session_state.show_registration = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'active_tab' not in st.session_state:
        st.session_state.active_tab = "Report Crime"
    if 'report_to_update' not in st.session_state:
        st.session_state.report_to_update = None
    
    # Sidebar for navigation when logged in
    if st.session_state.logged_in:
        menu = st.sidebar.radio("Navigation", 
            ["Report Crime", "View Reports", "Notifications", "Account", "Logout"],
            index=["Report Crime", "View Reports", "Notifications", "Account", "Logout"].index(st.session_state.active_tab) 
                  if st.session_state.active_tab in ["Report Crime", "View Reports", "Notifications", "Account", "Logout"] else 0
        )
        
        # Update active tab
        st.session_state.active_tab = menu
        
        if menu == "Report Crime":
            crime_reporting_page()
        elif menu == "View Reports":
            view_reports_page()
        elif menu == "Notifications":
            notifications_page()
        elif menu == "Account":
            account_page()
        elif menu == "Logout":
            # Clear session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.session_state.logged_in = False
            st.session_state.username = None
            st.rerun()
    else:
        # Show login or registration page
        if st.session_state.show_registration:
            registration_page()
        else:
            login_page()

if __name__ == "__main__":
    # Page configuration
    st.set_page_config(
        page_title="Crime Reporting System", 
        page_icon="🚨",
        layout="wide"
    )
    
    main()