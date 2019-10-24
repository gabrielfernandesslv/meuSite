from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meuSite.db'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)

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
    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)