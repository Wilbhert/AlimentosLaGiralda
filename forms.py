from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import PasswordField, TextField, SubmitField, DateField
from wtforms.validators import InputRequired     #validores

# crea una clase que extiende de Flaskform y se llama Login()
class LogIn(FlaskForm):     
    
    usr = TextField('Usuario', validators=[InputRequired(message='El campo usuario es requerido')])
    pwd = PasswordField('Contraseña', validators=[InputRequired(message='El campo usuario es requerido')])
    btn = SubmitField('Ingresar')


class Search(FlaskForm):
    
    name = TextField('name')
    btn = SubmitField('Buscar')

class Form(FlaskForm):
    nombre = TextField('Nombre')
    apellido = TextField('Apellido')
    documento = TextField('Documento')
    cargo = TextField('Cargo')
    fecIngreso = DateField('Fecha de Ingreso')
    tipoContrato = TextField('Tipo de Contrato')
    terminacion = DateField('Terminacion')
    area = TextField('Area')
    salario = TextField('Salario')
    retro = TextField('Retroalimentacion')
    puntaje = TextField('Puntaje')
    tipoUsuario = TextField('Tipo de Usuario')
    btn = SubmitField('Crear')

