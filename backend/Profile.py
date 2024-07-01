from itertools import product
from flask import render_template, request, redirect, url_for, flash, session, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import secrets
import pymysql.cursors
from app import mysql

Profile = Blueprint('Profile', __name__, template_folder='../Frontend/HTML', static_folder='../Frontend/static')

@Profile.route('/profile/update', methods=['POST'])
def update_profile():
    if 'customer_ID' not in session:
        return redirect(url_for('auth.login'))
    
    customer_id = session['customer_ID']
    new_email = request.form['email']
    new_password = request.form['password']
    
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE Customer 
        SET email_ID = %s, Password = %s 
        WHERE Customer_ID = %s
    """, (new_email, new_password, customer_id))
    mysql.connection.commit()
    cursor.close()
    
    flash('Profile updated successfully', 'success')
    return redirect(url_for('Profile.profile'))

def get_customer_details(customer_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT Name, Address, email_ID FROM Customer WHERE Customer_ID = %s", (customer_id,))
    customer = cursor.fetchone()
    cursor.close()
    return customer

def fetch_products(customer_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Product WHERE Product_ID IN (SELECT Product_ID FROM Orders WHERE Customer_ID = %s)", (customer_id,))
    products = cursor.fetchall()
    cursor.close()
    return products

@Profile.route('/profile', methods=['GET'])
def profile():
    if 'customer_ID' not in session:
        return redirect(url_for('auth.login'))
    
    products = []
    customer_id = session["customer_ID"]
    products = fetch_products(customer_id)

    customer = get_customer_details(customer_id)
    customer_data = {
        'name': customer[0],
        'address': customer[1],
        'email': customer[2]
    }

    return render_template('profile.html', customer=customer_data, products = products)
