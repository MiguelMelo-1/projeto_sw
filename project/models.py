from project import db
from datetime import datetime
from project import bcrypt

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email_address = db.Column(db.String(50),nullable=False, unique=True)
    password_hash = db.Column(db.String(60),nullable=False)

    # @property
    # def password(self):
    #     return self.password

    # @password.setter
    # def password(self, plain_text_password):
    #     self.password_hash =  bcrypt.generate_password_hash(plain_text_password).decode('utf-8')


class Task(db.Model):
    date_time = datetime.now()
    id = db.Column(db.Integer(), primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable = False)
    state = db.Column(db.Boolean(), default=False)
    date_start = db.Column(db.String(), default=date_time.strftime("%Y-%m-%d"))
    date_end = db.Column(db.String())
    id_user = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=True)