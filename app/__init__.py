from flask import Flask
from flask_login import LoginManager


app = Flask(__name__)
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    
# Register Blueprint(AKA If we create another folder for login and stuff)


from . import routes 