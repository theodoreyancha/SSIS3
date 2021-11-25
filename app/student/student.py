from flask import Blueprint, render_template, redirect, request
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('DB_HOST')
USERNAME = os.getenv('DB_USERNAME')
PASSWORD = os.getenv('DB_PASSWORD')
NAME = os.getenv('DB_NAME')


student = Blueprint("student", __name__,url_prefix="/student" )

@student.route("/",methods=["post","get"])
def index():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )
    mycursor = db.cursor(buffered=True)

    mycursor.execute("SELECT* FROM student ")
    db.commit()
    data = mycursor.fetchall()

    return render_template("student_table.html", data=data)

@student.route("/delete",methods=["post","get"])
def delete():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )
    mycursor = db.cursor(buffered=True)

    if request.method == 'POST':
        student_id = request.form['currentRow']
        f = f"DELETE FROM student WHERE ID = '{student_id}'"
        mycursor.execute(f)
        db.commit()


    return student_id

@student.route("/student_add/",methods=["post","get"])
def student_add():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )
    mycursor = db.cursor(buffered=True)

    if request.method == "POST" and "id" in request.form:
        id = request.form["id"]
        fname = request.form["fname"]
        lname = request.form["lname"]
        course = request.form["course"]
        year = request.form["year"]
        gender = request.form["gender"]

        mycursor.execute("INSERT INTO student (ID, FirstName, LastName, Course, Year, Gender) "
                         "VALUES (%s,%s,%s,%s,%s,%s)",
                         (id, fname, lname, course, year, gender))
        db.commit()
        return redirect("/student")
    else:
        pass

    return render_template("student_add.html")

@student.route("/update",methods = ["post","get"])
def update():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )
    mycursor = db.cursor(buffered=True)

    if request.method == "POST" and "id" in request.form:
        oldid = request.form["oldid"]
        id = request.form["id"]
        fname = request.form["fname"]
        lname = request.form["lname"]
        course = request.form["course"]
        year = request.form["year"]
        gender = request.form["gender"]

        query2 = f"UPDATE student SET ID = '{id}', FirstName = '{fname}', LastName = '{lname}', Course = '{course}', Year = '{year}', Gender ='{gender}' WHERE ID = '{oldid}'"
        mycursor.execute(query2)
        db.commit()
        return redirect("/student")

    return redirect("/student")

@student.route("/back",methods = ["post","get"])
def back():
    return redirect ("/main")