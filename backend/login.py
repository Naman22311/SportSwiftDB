from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_mysqldb import MySQL
from sqlalchemy.exc import IntegrityError
import secrets
import pymysql.cursors

login = Blueprint("login", __name__, template_folder='../Frontend/HTML', static_folder = '../Frontend/static')
login.config['SECRET_KEY'] = secrets.token_hex(16)

user = "root"
pin = ""
host = "localhost"
db_name = "SportSwiftDB"
login.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{pin}@{host}/{db_name}"
login.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login.config['MYSQL_HOST'] = 'localhost'  
login.config['MYSQL_USER'] = 'root'
login.config['MYSQL_PASSWORD'] = ''
login.config['MYSQL_DB'] = 'SportSwiftDB'

mysql = MySQL(login)

MAX_LOGIN_ATTEMPTS=3
def update_failed_attempts(username):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE email NATURAL JOIN customer SET failed_attempts = failed_attempts + 1 WHERE em = %s;", (username,))
    mysql.connection.commit()
    cursor.close()

def reset_failed_attempts(username):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE email NATURAL JOIN customer SET failed_attempts = 0 WHERE em = %s;", (username,))
    mysql.connection.commit()
    cursor.close()

def validate_customer(username, password):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT Customer_ID FROM email NATURAL JOIN customer where em=%s and Password=%s;", (username, password))
    user = cursor.fetchone()
    cursor.close()
    return user 

def get_blocked(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT blocked FROM email NATURAL JOIN customer NATURAL JOIN check_blocked  where em=%s;", (username,))
    failed_attempts = cursor.fetchone()
    cursor.close()
    if failed_attempts == None: 
        return 0
    return failed_attempts[0]

def DropTriggerLogin(username):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE email NATURAL JOIN customer SET failed_attempts = failed_attempts + 1 WHERE em = %s;", (username,))
    mysql.connection.commit()
    cursor.close()

@login.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    failed_attempts = get_blocked(email)
    
    if failed_attempts:
        flash('Your account is locked due to too many failed login attempts. Please contact support.','error')
        return redirect(url_for('login'))

    customer = validate_customer(email, password)
    if customer:
        session["customer"] = customer
        reset_failed_attempts(email)  
        return redirect(url_for('customer_dashboard'))
    else:
        DropTriggerLogin(email) 
        flash('Invalid username or password')
        return redirect(url_for('login'))
    