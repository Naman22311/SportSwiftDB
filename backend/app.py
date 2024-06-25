from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import secrets
import pymysql.cursors

app = Flask(__name__, template_folder='../Frontend/HTML', static_folder='../Frontend/static')

app.config['SECRET_KEY'] = secrets.token_hex(16)

user = "root"
pin = "Shrutya1%"
host = "localhost"
db_name = "SportSwiftDB"
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{pin}@{host}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Shrutya1%'
app.config['MYSQL_DB'] = 'SportSwiftDB'

mysql = MySQL(app)

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Shrutya1%',
    database='SportSwiftDB',
    cursorclass=pymysql.cursors.DictCursor
)

from login import auth  

app.register_blueprint(auth, url_prefix="/auth")  

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/explore")
def explore():
    return render_template("explore.html")

if __name__ == "__main__":
    app.run()
