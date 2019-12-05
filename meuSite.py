from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import registratioform

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meuSite.db'
app.config['SECRET_KEY'] = 'akjdshsagdgajdgmnxmch'
db = SQLAlchemy(app)

class Usuario(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    cartaosus = db.Column(db.Integer, unique=True, nullable=False)
    endereco = db.Column(db.String(200), unique=True, nullable=False)
    telefone = db.Column(db.String(14), unique=True, nullable=False)
    cidade_estado = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template("login.html")

@app.route('/objetivo')
def objetivo():
    return render_template("objetivo.html")

@app.route('/form', methods=['POST', 'GET'])
def form():

    form = registratioform()

    if form.validate_on_submit:
        novo_user = Usuario(nome=form.nome.data, idade=form.idade.data, 
        cartaosus=form.cartaosus.data, endereco=form.endereco.data, telefone=form.telefone.data, cidade_estado=form.cidade_estado.data, 
        email=form.email.data, password=form.password.data)
        db.session.add(novo_user)
        db.session.commit
    return render_template("form.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)