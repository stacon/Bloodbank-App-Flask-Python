from flask import Flask, request, render_template
from . import models

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template('index.html')
    # if request.method == 'GET':
    #     return render_template('index')
    # elif request.method == 'POST':
    #     return render_template('index')