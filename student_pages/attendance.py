from database import attendance_collection
from utils import current_date
import streamlit as st

def load_page(username):
    st.header("📅 Mark Your Attendance")

    # ✅ Ask college manually
    college = st.text_input("Enter your college name")

    # Check if already marked
    existing = attendance_collection.find_one({
        "username": username,
        "date": current_date()
    })

    if existing:
        st.success("✅ Attendance already marked for today.")
    else:
        if st.button("Mark Present"):
            attendance_collection.insert_one({
                "username": username,
                "date": current_date(),
                "college": college  # ✅ save college entered manually
            })
            st.success("✅ Attendance marked.")

    # 🔢 Show total present today
    total_today = attendance_collection.count_documents({
        "date": current_date()
    })
    st.info(f"📊 Total students present today: **{total_today}**")
