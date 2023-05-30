from flask_wtf import FlaskForm
from project.models import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

class RegistrationForm(FlaskForm):
    username = StringField('Nome de utilizador', validators=[
        DataRequired(),
        Length(min=2, max=20)
    ])
    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])
    password = PasswordField('Password', validators=[
        DataRequired()
    ])
    confirm_password = PasswordField('Confirmar Password', validators=[
        DataRequired(),
        EqualTo('password')
    ])
    submit = SubmitField('Registrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Este utilizador já existe')

    def validate_email(self, email):
        user = User.query.filter_by(email_address=email.data).first()
        if user:
            raise ValidationError('Este email já existe')

class LoginForm(FlaskForm):
    username = StringField('Nome de utilizador', validators=[
        DataRequired(),
        Length(min=2, max=20)
    ])
    password = PasswordField('Password', validators=[
        DataRequired()
    ])
    remember = BooleanField('Lembrar login')
    submit = SubmitField('Login')