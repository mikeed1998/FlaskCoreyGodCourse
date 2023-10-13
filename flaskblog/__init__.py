import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dc16b97a5546948a8cbfb3dfe414967f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # a donde me manda en caso de fallar login_required
login_manager.login_message_category = 'info'
# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_SERVER'] = 'mail.wozial.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'michael@wozial.com'
app.config['MAIL_PASSWORD'] = 'zCmfxQEz&wTM'
# app.config['MAIL_DEBUG'] = True
mail = Mail(app)

from flaskblog import routes

