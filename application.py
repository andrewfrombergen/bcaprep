import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from flask_talisman import Talisman
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, is_complex

# Configure application and database
app = Flask(__name__)
Talisman(app, content_security_policy=None)
db = SQL(os.getenv("DATABASE_URL"))

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template("index.html")

    # Attempt to register user
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 400)
        if not request.form.get("password"):
            return apology("must provide password", 400)
        elif not is_complex(request.form.get("password")):
            return apology("password does not meet complexity requirements")
        if not request.form.get("confirmation"):
            return apology("must confirm password", 400)
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must match", 400)
        if {"username": request.form.get("username")} in db.execute("SELECT username FROM users"):
            return apology("username already taken", 400)

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), generate_password_hash(request.form.get("password")))
        session.clear()
        return redirect("/entrancetest", registered=True)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/tips")
def tips():
    return render_template("tips.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/entrancetest", methods=["GET", "POST"])
@login_required
def entrancetest():
    # Save functionality
    if request.method == "POST":
        db.execute("UPDATE users SET entrancetest = ? WHERE id = ?", request.form.get("entrancetest"), session["user_id"])

    # Retrieve and render with previous study plan and username
    username = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0]["username"]
    entrancetest = db.execute("SELECT entrancetest FROM users WHERE username = ?", username)[0]["entrancetest"]
    return render_template("test.html", entrancetest=entrancetest, username=username)

@app.route("/login", methods=["GET", "POST"])
def login():

    # Forget any user_id
    session.clear()

    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        # Ensure username and password were submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]
        return redirect("/entrancetest")

@app.route("/logout")
def logout():
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/entrancetest")

def errorhandler(e):
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)