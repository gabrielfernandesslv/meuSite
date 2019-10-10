from flask import Flask, render_template

app = Flask (__name__)

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