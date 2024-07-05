from flask import render_template, request, redirect, url_for, flash, session, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import secrets
import pymysql.cursors
from app import mysql, login_flag

Checkout = Blueprint('Checkout', __name__, template_folder='../Frontend/HTML', static_folder='../Frontend/static')

@Checkout.route('/checkout/clear_cart', methods=['POST'])
def clear_cart():
    customer_id = session.get("customer_ID")
    if customer_id:
        cursor = mysql.connection.cursor()
        try:
            cursor.execute("START TRANSACTION")
            cursor.execute("DELETE FROM Cart WHERE Customer_ID = %s", (customer_id,))
            cursor.execute("COMMIT")
            mysql.connection.commit()
        except Exception as e:
            mysql.connection.rollback()
        
        cursor.close()
    return redirect(url_for('home'))

def fetch_products(customer_id):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT Product.*, Cart.Quantity
        FROM Product
        JOIN Cart ON Product.Product_ID = Cart.Product_ID
        WHERE Cart.Customer_ID = %s
    """, (customer_id,))
    products = cursor.fetchall()
    cursor.close()
    print(products)
    total_amount=0
    total_amount = sum(product[4] * product[7] for product in products)  # Calculate total amount
    return products, total_amount

@Checkout.route('/checkout', methods=['GET'])
def checkout():
    customer_ID = session.get("customer_ID")
    products = []
    total_amount = 0
    if customer_ID:
        products, total_amount = fetch_products(customer_ID)
    return render_template("checkout.html", products=products, total_amount=total_amount)