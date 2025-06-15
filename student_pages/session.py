from database import session_collection
import streamlit as st

def load_page(username):
    st.header("🕐 Add Session Activity")
    topic = st.text_input("Topic Covered")
    duration = st.number_input("Duration (in hours)", min_value=0.5, step=0.5)
    if st.button("Submit Session"):
        session_collection.insert_one({
            "username": username,
            "topic": topic,
            "duration": duration
        })
        st.success("Session added.")
