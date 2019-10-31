from flask_wtf import FlaskForm
from wtforms import(
stringfield,
passwordfield,
submitfield,
booleanfield
)
from wtforms.validators import datarequired, lenght, email,equalto  

class registratioform(FlaskForm):
    username = stringfield(
        'usuario',
        validators=[datarequired(),lenght(min=2,max=80)]
    )
    email = stringfield('email', validators=[datarequired(),email()])
    password = passwordfield('senha', validators=[datarequired()])
    confirm_password = passwordfield('repete senha', validators=[datarequired(),equalto('password')])