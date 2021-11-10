from flask import Blueprint, render_template, request, flash
from werkzeug.wrappers import request

auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    # if request.method == "POST":
    #     email = request.form.get("email")
    #     password = request.form.get("password")
    #     print(email, password)

    #     if len(email) < 4:
    #         flash("your email is too short", category="error")
    #     elif len(password) < 5:
    #         flash(
    #             "Your Password is too short please use one with 5 or more characters", category="error")

    return render_template("signup.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    # if request.method == "POST":
    #     email = request.form.get("email")
    #     password = request.form.get("password")
    #     print(email, password)
    return render_template("login.html")
