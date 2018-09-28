from flask import render_template
from database import db
from database import app


# 装饰器的作用url与视图函数的映射

note_user = {
    'username': 'monkeyQK',
    'qq': '155392114'
}


posts = [  # fake array of posts
    {
        'author': {'nickname': 'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'nickname': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    }]


@app.route("/")
def hello_flask():
    return "hello flask!"


@app.route("/login")
def login_app():
    page_name = "登录"
    return render_template("login.html", page_name=page_name)


@app.route("/regist")
def reg_app():
    page_name = "注册"
    return render_template("reg.html", page_name=page_name)


@app.route("/index")
def index():
    page_name = "首页"
    return render_template("index.html", page_name=page_name)


@app.route("/list")
def show():
    return render_template("list.html", posts=posts)


@app.route("/init")
def db_init():
    db.create_all()
    return "初始化成功！"


def main():
    app.run(debug=True, host="127.0.0.1")


if __name__ == '__main__':
    main()
