from deyting import db, manager
from datetime import datetime
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String(100))
    date_registration = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.relationship('Profile', backref='users')


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    last_name = db.Column(db.String)
    gender = db.Column(db.String)
    date_birth = db.Column(db.Integer)
    zodiac_sign = db.Column(db.String)
    profile = db.Column(db.Integer, db.ForeignKey('users.id'))
    pictures = db.Column(db.String)


@manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)