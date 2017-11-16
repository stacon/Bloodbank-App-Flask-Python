from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template('master/layout.html')
    # if request.method == 'GET':
    #     return render_template('index')
    # elif request.method == 'POST':
    #     return render_template('index')