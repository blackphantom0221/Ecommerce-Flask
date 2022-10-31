from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    fname = db.Column(db.String(50), nullable=False, unique=True)
    lname = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    day_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    product_id = db.relationship(db.Integer, db.ForeignKey('product.id'), lazy = True )
    my_cart = db.relationship('Product', secondary = 'Cart',
    backref = db.backref("mycart", lazy = 'dynamic'), lazy = 'dynamic')

    def __init__(self, username, email, password, fname, lname):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.fname = fname
        self.lname = lname
    
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
    
    def updateToDB(self):
        db.session.commit()
    
    def addToCart(self, product):
        self.my_cart.appdend(product)
        db.session.commit()
    
    def removeFromCart(self, product):
        db.session.delete(product)
        db.session.commit()
    
    def clearAllCart(self):
        db.session.delete(self)
        db.session.commit()
        
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String)
    user_id = db.relationship(db.Integer, db.ForeignKey('user.id'), lazy = True )


    def __init__(self, name, price, img_url):
        self.name = name
        self.price = price 
        self.img_url = img_url
        
        
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
    
    def updateToDB(self):
        db.session.commit()


# Join Table
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   