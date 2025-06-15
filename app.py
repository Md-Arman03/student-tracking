import streamlit as st
from auth import register_user, login_user
from student_pages import attendance, session, feedback
from admin_pages import dashboard

st.set_page_config(page_title="Student Portal")

# Initialize session key
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "username" not in st.session_state:
    st.session_state["username"] = ""

# App title
st.title("📚 Student Management Portal")

# If not logged in: show login/register
if not st.session_state["logged_in"]:
    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Register":
        st.subheader("Create New Account")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Register"):
            if register_user(username, password):
                st.success("Registered Successfully!")
            else:
                st.warning("User already exists.")

    elif choice == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login_user(username, password):
                st.success(f"Welcome {username}")
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.rerun()  # ✅ updated here
            else:
                st.error("Invalid credentials")

else:
    # When logged in
    st.sidebar.success(f"Logged in as: {st.session_state['username']}")
    page = st.sidebar.radio("Go to", ["Attendance", "Session", "Feedback", "Dashboard", "Logout"])

    if page == "Attendance":
        attendance.load_page(st.session_state["username"])

    elif page == "Session":
        session.load_page(st.session_state["username"])

    elif page == "Feedback":
        feedback.load_page(st.session_state["username"])

    elif page == "Dashboard":
        dashboard.load_page()

    elif page == "Logout":
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""
        st.rerun()  # ✅ updated here too
