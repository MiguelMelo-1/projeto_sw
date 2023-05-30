from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
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

<<<<<<< Updated upstream
class LoginForm(FlaskForm):
=======



class LoginForm(FlaskForm):
>>>>>>> Stashed changes
    username = StringField('Nome de utilizador', validators=[
        DataRequired(),
        Length(min=2, max=20)
    ])
    password = PasswordField('Password', validators=[
        DataRequired()
    ])
    remember = BooleanField('Lembrar login')
    submit = SubmitField('Login')