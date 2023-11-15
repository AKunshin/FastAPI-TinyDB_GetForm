"""
Script for filling the database
"""
from tinydb import TinyDB


db = TinyDB("templates.json")

db.truncate()

db.insert(
    {
        "name": "OrderForm",
        "client_name": "text",
        "client_email": "email",
        "client_phone": "phone",
        "order_date": "date",
    }
)
db.insert(
    {
        "name": "RegistrationForm",
        "user_name": "text",
        "user_email": "email",
        "user_password": "text",
        "registration_date": "date",
    }
)
db.insert(
    {
        "name": "CommentForm",
        "author_name": "text",
        "author_phone": "phone",
        "text_comment": "text",
    }
)
