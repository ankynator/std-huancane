from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length


class SearchFileForm(FlaskForm):
    #create a validation on exists for files
    number_of_file = StringField(label='Numero de expediente:', validators=[Length(min=5, max=5, message='El numero de expediente tiene 5 digitos')])
    submit = SubmitField(label='Buscar')


class RegisterFileForm(FlaskForm):
    number_of_file = StringField(label='Numero de expediente', validators=[Length(min=5, max=5, message='El numero de expediente tiene 5 digitos')])
    name_of_file = StringField(label='Titulo de expediente:', validators=[Length(min=10, max=30, message='Nombre demasiado largo')])
    submit = SubmitField(label='Registrar')

