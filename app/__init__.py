from flask import Flask
from flask_login import LoginManager
from .models import Cart, User, db
from config import Config
from flask_migrate import Migrate

# from .auth.routes import auth
from .cart.routes import cart


app = Flask(__name__)
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    
app.config.from_object(Config)


#register Blueprint
# app.register_blueprint(auth)
app.register_blueprint(cart)

# initialize our database to work with app
db.init_app(app)
migrate = Migrate(app, db)
login.init_app(app)


from . import routes 
from . import models