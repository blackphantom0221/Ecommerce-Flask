from itertools import product
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from app.models import Cart, Product, User, db
from app.routes import homePage

cart = Blueprint('cart', __name__, template_folder='cart_templates')

@cart.route('/add')
@login_required
def addCart(product_id):
    product = Product.query.get(product_id)
    if product: 
        current_user.addToCart(product) 
    else:
        print('Product does not exist!')

    return redirect(url_for('products'))


@cart.route('/remove')
@login_required
def removeFromCart(product_id):
    product = Product.query.get(product_id)
    if product:
        current_user.removeFromCart(product)
    else:
        print('product not in cart')
    return redirect(url_for('products'))

@cart.route('/remove/all')
@login_required
def removeall(product_id):
    product = Product.query.get(product_id)
    if current_user.id == product.user_id:
        product.clearAllCart()
    else:
        print('cart already empty!')
    return redirect(url_for('homePage'))


@cart.route('/view/Cart')
@login_required
def viewCart(cart_id):
    cart = User.query.get(cart_id)
    if cart:
        return render_template('checkout.html', cart = cart)
    else:
        return redirect(url_for('homePage'))