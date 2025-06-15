from database import users_collection, attendance_collection, session_collection, feedback_collection
from utils import current_date
from admin_pages.college_view import load_college_page  # ✅ Import the college view page
import streamlit as st

def load_page():
    st.header("📊 Admin Dashboard")

    # ✅ College-wise search for registered users
    st.subheader("🎓 College-wise Student Strength")
    college_query = st.text_input("Enter college name:")
    if college_query:
        matched_users = users_collection.find({"college": {"$regex": college_query, "$options": "i"}})
        user_list = [u["username"] for u in matched_users]

        st.write(f"### Students from '{college_query}':")
        for u in user_list:
            st.write(f"👤 {u}")

        total_count = users_collection.count_documents({"college": {"$regex": college_query, "$options": "i"}})
        st.info(f"Total registered students in {college_query}: **{total_count}**")

        # ✅ Attendance count from that college
        total_present = attendance_collection.count_documents({
            "college": {"$regex": college_query, "$options": "i"},
            "date": current_date()
        })
        st.success(f"📅 Students present today from {college_query}: **{total_present}**")

        # ✅ Button to view full college data
        if st.button("🔍 View College Details"):
            st.session_state["view_college"] = college_query
            st.experimental_rerun()

    # Redirect to detailed college page
    if "view_college" in st.session_state:
        load_college_page(st.session_state["view_college"])
        return

    # Other Sections
    st.subheader("🗓️ Attendance Logs")
    for log in attendance_collection.find():
        st.text(f"{log['username']} - {log['date']} - {log.get('college', 'Unknown')}")

    st.subheader("📘 Session Activities")
    for s in session_collection.find():
        st.text(f"{s['username']} - {s['topic']} ({s['duration']} hr)")

    st.subheader("📝 Feedbacks")
    for f in feedback_collection.find():
        st.text(f"{f['username']} - {f['feedback']}")
