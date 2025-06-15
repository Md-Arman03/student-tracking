# admin_pages/college_view.py

from database import users_collection, attendance_collection, session_collection, feedback_collection
from utils import current_date
import streamlit as st

def load_college_page(college_name):
    st.header(f"🏫 College Details: {college_name}")

    # Students
    st.subheader("👥 Registered Students")
    students = list(users_collection.find({"college": {"$regex": college_name, "$options": "i"}}))
    if students:
        for student in students:
            st.write(f"- {student['username']}")
    else:
        st.warning("No students found for this college.")

    # Attendance
    st.subheader("📅 Attendance Records")
    attendance_logs = list(attendance_collection.find({
        "college": {"$regex": college_name, "$options": "i"}
    }))
    if attendance_logs:
        for a in attendance_logs:
            st.write(f"{a['username']} - {a['date']}")
    else:
        st.info("No attendance data found.")

    # Session Participation
    st.subheader("📘 Session Activities")
    session_logs = list(session_collection.find({
        "username": {"$in": [s['username'] for s in students]}
    }))
    if session_logs:
        for s in session_logs:
            st.write(f"{s['username']} - {s['topic']} ({s['duration']} hr)")
    else:
        st.info("No session data available.")

    # Feedbacks
    st.subheader("📝 Feedbacks")
    feedbacks = list(feedback_collection.find({
        "username": {"$in": [s['username'] for s in students]}
    }))
    if feedbacks:
        for f in feedbacks:
            st.write(f"{f['username']}: {f['feedback']}")
    else:
        st.info("No feedback submitted.")

    # 🔙 Back button
    if st.button("🔙 Back to Dashboard"):
        del st.session_state["view_college"]
        st.experimental_rerun()
