from database import feedback_collection
import streamlit as st

def load_page(username):
    st.header("💬 Submit Feedback")
    feedback_text = st.text_area("Your Feedback")
    if st.button("Submit"):
        feedback_collection.insert_one({
            "username": username,
            "feedback": feedback_text
        })
        st.success("Feedback submitted.")
