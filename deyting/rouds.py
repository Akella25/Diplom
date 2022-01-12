from flask import request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from os.path import join, dirname, realpath
from deyting import app, db
from deyting.models import Users, Profile
from deyting.utils.function import piktures


@app.route('/', methods=['POST', 'GET'])
def form_registration():
    login = request.form.get('login')
    password = request.form.get('password')
    if request.method == 'POST':
        if not (login and password):
            flash('Fill in all the fields')
        elif len(password) == 0:
            flash('enter password')
        else:

            password_hash1 = generate_password_hash(password)
            new_user = Users(login=login, password_hash=password_hash1)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('log_user'))
    return render_template('form.html')


@app.route('/login', methods=['POST', 'GET'])
def log_user():
    login = request.form.get('login')
    password = request.form.get('password')
    if request.method == 'POST':
        if login and password:
            user = Users.query.filter_by(login=login).first()

            if user and check_password_hash(user.password_hash, password):
                login_user(user)
                anketa = Profile.query.filter_by(profile=user.id).first()
                if anketa:
                    return redirect(url_for('my_profile'))
                else:
                    return redirect(url_for('anketa'))
            else:
                flash('Неверный логин или пароль')
        else:
            flash('Заполните все поля')
    return render_template('login.html')


@app.route('/logaut', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('form_registration'))


@app.route('/profile', methods=['POST', 'GET'])
@login_required
def anketa():
    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        date_birth = request.form['date_birth']
        zodiac_sign = request.form['zodiac_sign']
        pictures = request.files.get('avatar')

        if name and last_name and gender and date_birth and zodiac_sign and pictures:
            new_user = Profile(name=name, last_name=last_name, gender=gender, date_birth=date_birth,
                        zodiac_sign=zodiac_sign, profile=current_user.id)

            if pictures:
                new_user.add_pictures(pictures.filename)
                path = join(dirname(realpath(__file__)), 'static', pictures.filename)
                piktures(pictures, path)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('my_profile'))
            #db.session.rollback()
        else:
            flash('Заполните все поля')

    return render_template('prof.html')


@app.route('/my_profile', methods=['POST', 'GET'])
@login_required
def my_profile():
    user = Profile.query.filter_by(profile=current_user.id).first()
    return render_template('my_profile.html', user=user, title='profile')


@app.route('/redakt', methods=['POST', 'GET'])
@login_required
def redaktor_prof():
    profile_user = Profile.query.filter_by(profile=current_user.id).first()
    if request.method == 'POST':
        name = request.form.get('name')
        last_name = request.form.get('last_name')
        gender = request.form.get('gender')
        date_birth = request.form.get('date_birth')
        zodiac_sign = request.form.get('zodiac_sign')
        pictures = request.files.get('avatar')

        if name:
            profile_user.name = name

        if last_name:
            profile_user.last_name = last_name
        if gender:
            profile_user.gender = gender
        if date_birth:
            profile_user.date_birth = date_birth
        if zodiac_sign:
            profile_user.zodiac_sign = zodiac_sign

        if pictures:
            profile_user.add_pictures(pictures.filename)
            path = join(dirname(realpath(__file__)), 'static', pictures.filename)
            piktures(pictures, path)
        db.session.add(profile_user)
        db.session.commit()
        return render_template('redakt.html', user=profile_user)


    return render_template('redakt.html', user=profile_user)


@app.route('/delete/<int:id_user>', methods=['POST', 'GET'])
@login_required
def delete_user(id_user):
    delete = Users.query.get(id_user)
    delete_profile = Profile.query.filter_by(profile=id_user).first()

    try:
        db.session.delete(delete)
        db.session.delete(delete_profile)
        db.session.commit()
    except Exception as e:
        raise Exception(str(e))
        #return "error"

    return redirect(url_for('form_registration'))

@app.after_request
def redirect_user(response):
    if response.status == '401 UNAUTHORIZED':
        flash('Неверный логин')
        return redirect(url_for('log_user'))

    return response


