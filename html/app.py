from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template("index.html")


@app.route('/data', methods=['POST'])
def handle_data():
    first, second = request.form['first'], request.form['second']
    response = requests.get("http://host.docker.internal:8000/pretty/{}/{}".format(first, second))
    return response.text


app.run('0.0.0.0', port=9090)