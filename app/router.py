from flask import Flask, request, render_template
from . import config


app = Flask(__name__)
app.config.from_object('config')


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('index')
    elif request.method == 'POST':
        return render_template('index')