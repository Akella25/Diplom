from flask import request, render_template
from werkzeug.security import generate_password_hash, check_password_hash

from deyting import app, db
from deyting.models import Users


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
