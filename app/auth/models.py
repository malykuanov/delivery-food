from datetime import datetime

from flask_login import UserMixin

from app import db


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), default="User")
    address = db.Column(db.String(500))
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500))
    role = db.Column(db.String(50))
    date_registration = db.Column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return f"email={self.email}"
