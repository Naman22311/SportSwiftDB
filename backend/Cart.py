from flask import render_template, request, redirect, url_for, flash, session, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import secrets
import pymysql.cursors
from app import mysql

Cart = Blueprint("Cart", __name__, template_folder='../Frontend/HTML', static_folder='../Frontend/static')

def fetch_products(customer_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Product WHERE Product_ID IN (SELECT Product_ID FROM Cart WHERE Customer_ID = %s)", (customer_id,))
    products = cursor.fetchall()
    cursor.close()
    return products

# @Cart.route('/delete_from_cart', methods=['POST'])
# def delete_from_cart():
#     product_id = request.form['product_id']
#     supplier_id = request.form['supplier_id']
    
#     cursor = mysql.connection.cursor()
#     try:
#         cursor.execute("START TRANSACTION")
#         cursor.execute("DELETE FROM cart WHERE Customer_ID = %s AND Product_ID = %s AND Supplier_ID = %s", (session["customer"][0], product_id, supplier_id))
#         cursor.execute("COMMIT")
#         cursor.close()
#         mysql.connection.commit()
#     except Exception as e:
#         mysql.connection.rollback()
#         cursor.close()
#     return redirect(url_for('checkout'))

@Cart.route('/cart', methods=['GET'])
def cart():
    customer_ID = None
    if "customer_ID" in session:
        customer_ID = session["customer_ID"]
        products = fetch_products(customer_ID)
        print(products)
    return render_template('cart.html')
    

    
