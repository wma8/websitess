from flask import render_template, session, redirect, url_for, flash, request, Flask, jsonify, Markup
from werkzeug.security import generate_password_hash, check_password_hash

from .forms import UserForm, LoginForm
from ..models import User
from . import main
from app import db


@main.route('/', methods=['GET', 'POST'])
def signup():
    # session.clear()
    form = UserForm()
    if form is None:
        flash('Should input username and password')
    elif form.validate_on_submit():
        data = form.data
        user = User(
            username=data["username"],
            password=generate_password_hash(data["password"])
        )
        db.session.add(user)
        try:
            db.session.commit()
            flash('User created!')
        except:
            db.session.rollback()
            flash('User create failed')
    return render_template('index.html', form=form)


@main.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form is None:
        flash('Should input username and password!')
    elif form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # print(user.password)
        if user is None:
            flash("Not flash")
        elif not user.check_password(form.password.data):
            flash("Wrong password")
        else:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.signup'))
            # return redirect(url_for('main.post2channel'))
    return render_template('login.html', **locals())


@main.route('/logout/')
def logout():
    session.pop("user_id", None)
    # session.clear()
    return redirect(url_for('main.login'))


@main.route('/my_page/')
def mypage():
    return render_template('my_page.html')
