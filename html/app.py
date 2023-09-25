import requests
from flask import Flask, render_template, request, send_file

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def handle_data():
    days = request.form["first"]
    response = requests.post("http://localhost:8000/api/predict/", data={"days": int(days)})
    return send_file(response.json()["image_path"])


app.run('0.0.0.0', port=9090)
