from flask import Blueprint, render_template

# user = Blueprint('user', __name__, template_folder='templates')

# @user.route('/')
# def show():
#     return "I am Blueprint :)"

course = Blueprint('course', __name__, template_folder='templates')
courses_list=["COS300","COS310","COS400"]

@course.route('/')
def show():
    return render_template("index.html",course=courses_list)