from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_mysqldb import MySQL
from sqlalchemy.exc import IntegrityError
import secrets
import pymysql.cursors
# from login import login

app = Flask(__name__, template_folder='../Frontend/HTML', static_folder = '../Frontend/static')

# app.register_blueprint(login, url_prefix = "/")

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/explore")
def explore():
    return render_template("explore.html")
if __name__ == "__main__":
    app.run()