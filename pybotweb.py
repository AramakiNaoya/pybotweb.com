from bottle import route, run, template, request
from datetime import datetime
from pybot import pybot

@route("/hello")
def hello():
    return template("pybot_template", input_text="", output_text="")

@route("/hello", method="post")
def do_hello():
    input_text = request.forms.input_text
    output_text = pybot(input_text)
    return template("pybot_template", input_text=input_text, output_text=output_text)

run(host="localhost", port=8080, debug=True)