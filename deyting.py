from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
# from users import User, Person
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///person.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = 'dddd'


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




@app.route('/', methods=['POST', 'GET'])
def form_registration():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        name = request.form['name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        date_birth = request.form['date_birth']
        zodiac_sign = request.form['zodiac_sign']
        height = request.form['height']
        weight = request.form['weight']

        password_hash = generate_password_hash(password)
        new_user = Users(login=login, password_hash=password_hash, name=name, last_name=last_name,
                         gender=gender, date_birth=date_birth, zodiac_sign=zodiac_sign, height=height,
                         weight=weight)
        db.session.add(new_user)
        db.session.commit()
        return render_template('form.html', users=Users.query.all())
    return render_template('form.html')
