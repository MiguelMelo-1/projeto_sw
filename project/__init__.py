from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from project.forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'e6e7367df57e95a4788360c842521e3e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)


from project import routes