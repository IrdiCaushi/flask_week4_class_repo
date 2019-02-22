from flask import Flask, render_template
from web.public import course
from api.item import student_user


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello from Irdi"

app.register_blueprint(course,url_prefix="/web/")

app.register_blueprint(student_user,url_prefix="/v1/admin")