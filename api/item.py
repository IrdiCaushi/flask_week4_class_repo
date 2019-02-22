from flask import Blueprint

student_user = Blueprint('student_user', __name__, template_folder='templates')

@student_user.route('/')
def show():
    return "I am Student Blueprint :)"
    