from deyting import db
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String(100))
    name = db.Column(db.String)
    last_name = db.Column(db.String)
    gender = db.Column(db.String)
    date_birth = db.Column(db.Integer)
    zodiac_sign = db.Column(db.String)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    date_registration = db.Column(db.DateTime, default=datetime.utcnow)