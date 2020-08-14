from bottle import route, run, template, request
from pybot import pybot

@route("/hello")
def hello():
    return template("index.html", input_text="", output_text="")

@route("/hello", method="post")
def do_hello():
    input_text = request.forms.input_text
    output_text = pybot(input_text)
    return template("index.html", input_text=input_text, output_text=output_text)

run(host="localhost", port=8080, debug=True, reloader=True)