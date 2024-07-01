from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import secrets
import pymysql.cursors

app = Flask(__name__, template_folder='../Frontend/HTML', static_folder='../Frontend/static')

app.config['SECRET_KEY'] = secrets.token_hex(16)

user = "root"
pin = ""
host = "localhost"
db_name = "SportSwiftDB"
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{pin}@{host}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'SportSwiftDB'

mysql = MySQL(app)

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='SportSwiftDB',
    cursorclass=pymysql.cursors.DictCursor
)

from login import auth  
from signUp import signUp
from Cart import Cart
from Checkout import Checkout
from product_details import product_details  

app.register_blueprint(auth, url_prefix="/auth")  
app.register_blueprint(signUp, url_prefix="/signUp")  
app.register_blueprint(Cart, url_prefix="/Cart")  
app.register_blueprint(Checkout, url_prefix="/Checkout")
app.register_blueprint(product_details, url_prefix="/product")  

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/explore")
def explore():
    return render_template("explore.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
