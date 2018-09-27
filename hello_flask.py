from flask import render_template
from database import db
from database import app


# 装饰器的作用url与视图函数的映射


@app.route("/")
def hello_flask():
    return "hello flask!"


@app.route("/login")
def login_app():
    return render_template("login.html", username="monkeyQK")


@app.route("/init")
def db_init():
    db.create_all()
    return "初始化成功！"


def main():
    app.run(debug=True, host="127.0.0.1")


if __name__ == '__main__':
    main()
