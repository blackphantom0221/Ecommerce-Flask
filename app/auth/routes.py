from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from app.models import Product, User, db
from auth.forms import Login, SignUp
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
auth = Blueprint('auth', __name__, template_folder='auth_templates')
@auth.route('/SignUp', methods = ["GET","POST"])
def signMeUp():
    form = SignUp()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            fname = form.fname.data
            lname = form.lname.data
            email = form.email.data
            password = form.password.data
            my_user = User(username, fname, lname, email, password)
            my_user.saveToDB()
            return redirect(url_for('logMeIn'))
    return render_template('SignUp.html', form=form)
@auth.route('/Login', methods = ["GET", "POST"])
def logMeIn():
    form = Login()
    if request.method == "POST":
        print('post method made')
        if form.validate():
            username = form.username.data
            password = form.password.data
            print(username, password)
            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    print('successfully logged in')
                    login_user(user)
                    return redirect(url_for('realHomePage'))
                else:
                    print('incorrect password')
            else:
                print('user does not exist')
    return render_template('Login.html', form=form)
@auth.route('/logout')
@login_required
def logMeOut():
    logout_user()
    return redirect(url_for('logMeIn'))