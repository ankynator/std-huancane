from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/std.db'
app.config['SECRET_KEY'] = '1a32a9360834e7623f6168eb'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import routes