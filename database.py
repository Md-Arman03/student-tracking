from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["student_app"]

users_collection = db["users"]
attendance_collection = db["attendance"]
session_collection = db["sessions"]
feedback_collection = db["feedbacks"]
