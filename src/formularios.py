from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import PasswordField, TextField, SubmitField
from wtforms.validators import InputRequired     #validores

# crea una clase que extiende de Flaskform y se llama Login()
class LogIn(FlaskForm):     # 
    
    usr = TextField('Username', validators=[InputRequired(message='El campo usuario es requerido')])
    
    pwd = PasswordField('Password', validators=[InputRequired(message='El campo usuario es requerido')])

    btn = SubmitField('login')