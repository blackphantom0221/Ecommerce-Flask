from re import L
from flask import render_template, redirect, url_for
# We don't need request because we are just pulling from the table we made
from app import app 
from .models import User, Product



@app.route('/')
def homePage():
    
    return render_template('index.html')

@app.route('/products')
def products():
    product = Product.query.all()
    return render_template('viewProducts.html', product = product )

@app.route('/products/<int: product_id>')
def singleProduct(product_id):
    product = Product.query.get(product_id)
    if product:
        return render_template('single_Product.html', product = product)
    else:
        return redirect(url_for('products'))