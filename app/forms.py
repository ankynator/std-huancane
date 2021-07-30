from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, Email
from wtforms.widgets.core import TextArea


class SearchFileForm(FlaskForm):
    #create a validation on exists for files
    number_of_file = StringField(label='Numero de expediente:', validators=[Length(min=5, max=5, message='El numero de expediente tiene 5 digitos')])
    submit = SubmitField(label='Buscar')


class RegisterFileForm(FlaskForm):
    file_user_name = StringField(label='Nombres y Apellidos', validators=[DataRequired()])
    file_user_dni = StringField(label='DNI', validators=[Length(min=8, max=8, message='El DNI debe tener 8 digitos'), DataRequired()])
    file_user_phone = StringField(label='Telefono/celular', validators=[Length(min=8, message='El numero de celular es invalido'), DataRequired()])
    file_user_email = StringField(label='Correo electronico', validators=[Email(), DataRequired()])
    file_subject = StringField(label='Asunto', validators=[DataRequired()])
    file_justification = StringField(label='Justificación', widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField(label='Enviar')

    # Nombre: Vander Luis Catti Idme
    # dni: 70298375
    # telefono/celular: 988228877
    # email: idmevander@gmail
    # asunto: Solicito certificado de estudios
    # justificacion: Que por motivos de haber concluido mis estudios y ser este documento requisito de un proceso de postualacion a beca