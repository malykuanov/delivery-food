import json

from flask import Blueprint, flash, redirect, url_for, g, request, render_template, session, jsonify
from flask_login import login_user, current_user
from werkzeug.security import generate_password_hash

from app import login_manager, db
from app.auth.models import Users, get_user
from app.auth.forms import LoginForm, RegisterForm
from app.products.models import ProductCategory

auth = Blueprint('auth',
                 __name__,
                 template_folder="templates",
                 static_folder="static",
                 static_url_path='/home-static')


@login_manager.user_loader
def load_user(user_id):
    print("user logged >>", user_id)
    print(get_user(user_id))
    g.user = get_user(user_id)
    return g.user


@auth.route('/login', methods=["POST", "GET"])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home.index'))

    categories = ProductCategory.query.order_by(ProductCategory.id).all()
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = Users.query.filter_by(email=form.email.data).first()
            if user and user.psw == form.psw.data:
                session['userLogged'] = user.email
                if form.remember.data:
                    login_user(user)
                    session.permanent = True
                else:
                    login_user(user)
                return redirect(url_for('home.index'))
            else:
                flash("User not found", category="error")
        else:
            for error in form.errors.items():
                flash(message=error, category="error")
    return render_template("auth/login.html", categories=categories, form=form)


@auth.route('/register', methods=["POST", "GET"])
def register():
    categories = ProductCategory.query.order_by(ProductCategory.id).all()

    form = RegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            if form.email.data in [user.email for user in Users.query.all()]:
                flash("Пользователь с таким email зарегистрирован", category="error")
                return render_template("auth/register.html", title="Register", form=form)
            try:
                hash_psw = generate_password_hash(form.psw1.data)
                u = Users(email=form.email.data, psw=hash_psw,
                          name=form.name.data, address=form.address.data)
                db.session.add(u)
                db.session.commit()
                flash("Success", category="success")
            except Exception as e:
                db.session.rollback()
                print("Ошибка добавления в БД", e)
        else:
            for error in form.errors.items():
                flash(message=error, category="error")

    return render_template("auth/register.html", categories=categories, form=form)
