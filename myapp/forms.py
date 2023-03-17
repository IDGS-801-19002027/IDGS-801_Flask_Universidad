from wtforms import Form
from wtforms import StringField, IntegerField, BooleanField, EmailField, validators

class UserForm(Form):
    id = IntegerField('id')
    nombres = StringField('Nombre')
    apellidos = StringField('Apellidos')
    email = EmailField('Correo')

class MaestroForm(Form):
    id = IntegerField('id')
    nombres = StringField('Nombres')
    apellidos = StringField('Apellidos')
    email = EmailField('Correo')
    estatus = BooleanField('Estatus')
