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