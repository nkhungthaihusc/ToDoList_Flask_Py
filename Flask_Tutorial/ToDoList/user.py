from flask import Blueprint , render_template, request , flash, session , redirect , url_for
import os
import re
from flask_login import login_user, login_required , logout_user , current_user
from .models import User, Note
from ToDoList import db
from werkzeug.security import generate_password_hash , check_password_hash
user = Blueprint("user" , __name__)

def is_valid_password(password):
    # Kiểm tra độ dài
    if len(password) < 8 or len(password) > 16:
        return False

    # Kiểm tra có ít nhất 1 chữ in hoa
    if not re.search(r"[A-Z]", password):
        return False

    # Kiểm tra có ít nhất 1 ký tự đặc biệt
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True


@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("pass")
        user = User.query.filter_by(email = email).first()
        if not user:
            flash("User doesn't exist","error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters" , "error")
        elif not is_valid_password(password):
            flash("Password must be have special characters , capital letters , and 8 - 16 characters" , "warning")
        else:
            if not check_password_hash(user.password , password):
                flash("Wrong password")
            else:
                session.permanent = True
                session["user_name"] = user.user_name
                login_user(user , remember=True)
                flash("Logged in success!" , "success")
                return redirect(url_for("view.home"))
    return render_template("login.html" , user=current_user , icon_path="login.png")





@user.route('/signup' , methods=['GET','POST'])


def signup():
    if request.method == "POST":
        email = request.form.get("email")
        user_name = request.form.get("name")
        password = request.form.get("pass")
        confirm = request.form.get("password")
        user = User.query.filter_by(email = email).first()
        if user:
            print(user.email)
            flash("Existed this email!!! Please try again other email" , category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters" , "error")
        elif not is_valid_password(password):
            flash("Password must be have special characters , capital letters , and 8 - 16 characters" , "warning")
        elif password != confirm:
            flash("Password doesn't not match" , "error")
        else:
            password = generate_password_hash(password , method = "pbkdf2:sha256")
            new_user = User(email , user_name , password)
            try:
                db.session.add(new_user)
                db.session.commit()
                flash("Created user successful" , "success")
                login_user(new_user , remember=True)
                return redirect(url_for("view.home"))
            except:
                "error"
    return render_template("signup.html" , icon_path="signup.png")


@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("user.login"))
