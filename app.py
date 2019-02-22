from flask import Flask, render_template
from web.public import course
from api.item import student_user
from extensions import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test21.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db.init_app(app)

# db.create_all()

@app.before_first_request
def create():
    db.create_all()

@app.route('/')
def hello():
    return "Hello from Irdi"
