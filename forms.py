from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, RadioField, SubmitField
from wtforms import EmailField
from wtforms import validators
from wtforms.validators import NumberRange

class CineForm(Form):
    nombre = StringField('Nombre',[
        validators.DataRequired(message="Este campo es requerido"),
        validators.Length(min=3, max=10, message="Longitud de 3 a 10 caracteres")
    ])
    nCompradores = IntegerField('nCompradores',[
        validators.DataRequired(message="Este campo es requerido"),
        NumberRange(min=1, message="Minimo debe haber un comprador")
    ])
    nBoletos = IntegerField('nBoletos',[
        validators.DataRequired(message="Este campo es requerido"),
        NumberRange(min=1, message="Minimo debe haber un comprador")
    ])
    tCineco = RadioField('tCineco',
        choices=[(1, "Si"), (2, "No")],
        coerce=int,
        validators=[validators.DataRequired(message="Este campo es requerido")]
    )