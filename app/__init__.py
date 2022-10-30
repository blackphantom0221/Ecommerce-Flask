from flask import Flask
from flask_login import LoginManager
from .models import User, db
from config import Config
from flask_migrate import Migrate

from .auth.routes import auth
app = Flask(__name__)
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    
app.config.from_object(Config)


#register Blueprint
app.register_blueprint(auth)

# initialize our database to work with app
db.init_app(app)
migrate = Migrate(app, db)
login.init_app(app)


from . import routes 
from . import models