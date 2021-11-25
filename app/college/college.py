from flask import Blueprint, render_template, redirect, request
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('DB_HOST')
USERNAME = os.getenv('DB_USERNAME')
PASSWORD = os.getenv('DB_PASSWORD')
NAME = os.getenv('DB_NAME')

college = Blueprint("college", __name__,url_prefix="/college" )

@college.route("/",methods=["post","get"])
def index():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )
    mycursor = db.cursor(buffered=True)

    mycursor.execute("SELECT* FROM college ")
    db.commit()
    data = mycursor.fetchall()

    return render_template("college_table.html", data=data)

@college.route("/delete",methods=["post","get"])
def delete():
    db = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        passwd=PASSWORD,
        database=NAME
    )
    mycursor = db.cursor(buffered=True)

    if request.method == 'POST':
        college_code = request.form['currentRow']
        f = f"DELETE FROM college WHERE Code = '{college_code}'"
        mycursor.execute(f)
        db.commit()


    return college_code

@college.route("/college_add/",methods=["post","get"])
def college_add():
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


        mycursor.execute("INSERT INTO college (Code, Name) "
                         "VALUES (%s,%s)",
                         (code, cname))
        db.commit()

        return redirect("/college")

    return render_template("college_add.html")

@college.route("/update",methods = ["post","get"])
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

        query2 = f"UPDATE college SET Code = '{code}', Name = '{cname}' WHERE Code = '{code}'"
        mycursor.execute(query2)
        db.commit()
        return redirect("/college")

    return redirect("/college")

@college.route("/back",methods = ["post","get"])
def back():
    return redirect ("/main")