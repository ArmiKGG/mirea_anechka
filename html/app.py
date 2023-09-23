from flask import Flask, render_template, request, Response
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template("index.html")


@app.route('/films/', methods=['POST'])
def handle_data():
    file = request.files["file"]
    file.save(file.filename)
    response = requests.post("http://localhost:8000/api/file/", files={"file": open(file.filename, "rb")})
    string = ""
    for r in response.json():
        string += f"<div><p><span><h1>Название: </h1></span><span><h3>{r['title']}</h3></span></p>" \
                  f"<p><span><h1>Информация: </h1></span><span><h3>{r['extra']}</h3></span></p>" \
                  f"<p><span><h1>Рейтинг: </h1></span><span><h3>{r['details']}</h3></span></p></div><hr>"
    return string


app.run('0.0.0.0', port=9090)