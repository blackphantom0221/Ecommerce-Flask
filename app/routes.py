from re import L
from flask import render_template, redirect, url_for
# We don't need request because we are just pulling from the table we made
from app import app 
from flask_login import login_required


@app.route('/')
def homePage():
    
    return render_template('index.html')

@app.route('/rec')
def items():
    pass
    return render_template('')