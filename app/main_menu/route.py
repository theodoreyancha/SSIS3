from flask import Blueprint, render_template, redirect, request

main_menu = Blueprint("mainmenu", __name__,url_prefix="/main" )

@main_menu.route("/")
def main():
    return render_template("mainmenu.html")
