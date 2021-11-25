from flask import Blueprint, render_template, redirect, request
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('DB_HOST')
USERNAME = os.getenv('DB_USERNAME')
PASSWORD = os.getenv('DB_PASSWORD')
NAME = os.getenv('DB_NAME')

course = Blueprint("course", __name__,url_prefix="/course" )

@course.route("/",methods=["post","get"])
def index():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME    )
    mycursor = db.cursor(buffered=True)

    mycursor.execute("SELECT* FROM course ")
    db.commit()
    data = mycursor.fetchall()

    return render_template("course_table.html", data=data)

@course.route("/delete",methods=["post","get"])
def delete():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )
    mycursor = db.cursor(buffered=True)

    if request.method == 'POST':
        course_code = request.form['currentRow']
        f = f"DELETE FROM course WHERE Code = '{course_code}'"
        mycursor.execute(f)
        db.commit()


    return course_code

@course.route("/course_add/",methods=["post","get"])
def course_add():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )
    mycursor = db.cursor(buffered=True)

    if request.method == "POST" and "code" in request.form:
        code = request.form["code"]
        cname = request.form["cname"]
        college = request.form["college"]

        mycursor.execute("INSERT INTO course (Code, Name, College) "
                         "VALUES (%s,%s,%s)",
                         (code, cname, college))
        db.commit()

        return redirect("/course")

    return render_template("course_add.html")

@course.route("/update",methods = ["post","get"])
def update():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )
    mycursor = db.cursor(buffered=True)

    if request.method == "POST" and "code" in request.form:
        code = request.form["code"]
        cname = request.form["cname"]
        college = request.form["college"]

        query2 = f"UPDATE course SET Code = '{code}', Name = '{cname}', College = '{college}' WHERE Code = '{code}'"
        mycursor.execute(query2)
        db.commit()
        return redirect("/course")

    return redirect("/course")

@course.route("/back",methods = ["post","get"])
def back():
    return redirect ("/main")