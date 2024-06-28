from flask import render_template, request, redirect, url_for, flash, session, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import secrets
import pymysql.cursors
from app import mysql

Checkout = Blueprint('Checkout', __name__, template_folder='../Frontend/HTML', static_folder='../Frontend/static')

@Checkout.route('/checkout/clear_cart', methods=['POST'])
def clear_cart():
    customer_id = session["customer_ID"]
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM Cart WHERE Customer_ID = %s", (customer_id,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('/'))

def fetch_products(customer_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Product WHERE Product_ID IN (SELECT Product_ID FROM Cart WHERE Customer_ID = %s)", (customer_id,))
    products = cursor.fetchall()
    cursor.close()
    return products

@Checkout.route('/checkout', methods=['GET'])
def checkout():
    customer_ID = None
    products = []
    if "customer_ID" in session:
        customer_ID = session["customer_ID"]
        products = fetch_products(customer_ID)
    return render_template("checkout.html", products=products)
