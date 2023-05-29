from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, BooleanField

class RegistrationForm(FlaskFrom):
    username = StringField('Nome de utilizador', validators=[
        DataRequired(),
        Length(min=2, max=20)
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
    ])
    comfirm_password = PasswordField('Confirmar Password', validators=[
        DataRequired(),
        EqualTo('Password')
    ])
    submit = SubmitField('Registrar')

class LoginForm(FlaskFrom):
    username = StringField('Nome de utilizador', validators=[
        DataRequired(),
        Length(min=2, max=20)
    ])
    password = PasswordField('Password', validators=[
        DataRequired()
    ])
    remember = BooleanField('Lembrar login')
    submit = SubmitField('Login')