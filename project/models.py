from project import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
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
    # def __repr__(self):
    #     return '{id = %r, title = %r, desc = %r, category = %r, state = %r, date_start = %r, date_end = %r, id_user = %r}' % self.id % self.title % self.desc % self.category % self.state % self.date_start % self.date_end % self.id_user