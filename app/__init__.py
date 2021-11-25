from flask import Flask, redirect
from .main_menu.route import main_menu
from .student.student import student
from .course.course import course
from .college.college import college

app = Flask(__name__)

app.register_blueprint(student)
app.register_blueprint(course)
app.register_blueprint(college)
app.register_blueprint(main_menu)

@app.route("/")
def main():
    return redirect("/main")
