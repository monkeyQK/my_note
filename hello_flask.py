from flask import render_template
from database import db
from database import app
from model import User
from flask import request
from flask import session
from flask import redirect
from flask import url_for
# 装饰器的作用url与视图函数的映射

note_user = {
    'username': 'monkeyQK',
    'qq': '145678916'
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


@app.route('/insert_user')
def insert_user():
    user_new = User(user_id='monkeyQK', user_name="管理员",
                    user_password="123456")

    # 单条插入
    db.session.add(user_new)
    db.session.commit()
    return '插入成功！'


@app.route("/login")
def login_app():
    page_name = "登录"
    return render_template("login.html", page_name=page_name)


@app.route('/check_login', methods=['POST'])
def check_login():
    user_id = request.form.get('user_id')
    # user_id = eval(user_id)
    print(request.form.get('user_id'))
    user_pwd = request.form.get('user_password')
    # user_pwd = eval(user_pwd)
    print(user_pwd)
    user = User.query.filter_by(user_id=user_id,
                                user_password=user_pwd).first()
    if user:
        session['user_id'] = user_id
        session.permanent = True
        return redirect(url_for('show', posts=posts))
    else:
        return "用户名或密码错误！"


@app.route('/regist_user', methods=['POST'])
def regist():
    user_id = request.form.get('user_id')
    # user_id = eval(user_id)
    print(request.form.get('user_id'))
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        return "用户名已存在"
    else:
        pass
    user_name = request.form.get('user_name')
    print(request.form.get('user_name'))
    user_pwd = request.form.get('user_password')
    # user_pwd = eval(user_pwd)
    print(user_pwd)
    user_new = User(user_id=user_id, user_name=user_name,
                    user_password=user_pwd)
    # 单条插入
    db.session.add(user_new)
    db.session.commit()
    return '注册成功！'


@app.route('/content', methods=['POST'])
def content():
    user_id = request.form.get('user_id')
    # user_id = eval(user_id)
    print(request.form.get('user_id'))
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        return "用户名已存在"
    else:
        pass
    user_name = request.form.get('user_name')
    print(request.form.get('user_name'))
    user_pwd = request.form.get('user_password')
    # user_pwd = eval(user_pwd)
    print(user_pwd)
    user_new = User(user_id=user_id, user_name=user_name,
                    user_password=user_pwd)
    # 单条插入
    db.session.add(user_new)
    db.session.commit()
    return '注册成功！'


@app.route("/logo_out")
def logo_out():
    session.clear()
    return redirect(url_for('login_app', posts=posts))


@app.route("/regist")
def reg_app():
    page_name = "注册"
    return render_template("reg.html", page_name=page_name)


@app.route("/index")
def index():
    page_name = "首页"
    return render_template("index.html", page_name=page_name)


@app.route("/note")
def note():
    page_name = "记录"
    return render_template("note.html", page_name=page_name)


@app.route("/list")
def show():
    return render_template("list.html", posts=posts)


@app.route("/init")
def db_init():
    db.create_all()
    return "初始化成功！"


@app.route("/drop_")
def db_drop():
    db.drop_all()
    return "清空成功！"


@app.context_processor
def my_context_processor():
    user_id = session.get("user_id")
    if user_id:
        user = User.query.filter_by(user_id=user_id).first()
        if user:
            return {'user': user}
    return {}


def main():
    app.run(debug=True, host="127.0.0.1")


if __name__ == '__main__':
    main()
