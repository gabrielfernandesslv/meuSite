from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, SelectField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length 

class registratioform(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(),Length(min=2,max=80)])

    idade = IntegerField ('Idade', validators=[DataRequired()])

    cartaosus = IntegerField ('Cartão de SUS', validators=[DataRequired()])

    endereco = StringField ('Endereço', validators=[DataRequired()])

    telefone = IntegerField ('Telefone', validators=[DataRequired()])

    cidade_estado = StringField ('Cidade-Estado', validators=[DataRequired()])

    email = StringField('Email', validators=[DataRequired(),Email()])

    password = PasswordField('Senha', validators=[DataRequired()])

    confirm_password = PasswordField('Repete Senha', validators=[DataRequired(), EqualTo('password')])
    
    botao = SubmitField('Enviar')