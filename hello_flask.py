from flask import render_template
from note import db
from note import app
from model import User
from model import Note_info
from flask import request
from flask import session
from flask import redirect
from flask import url_for
import json
from functools import wraps
# 装饰器的作用url与视图函数的映射

note_user = {
    'username': 'monkeyQK',
    'qq': '145678916'
}

my_note_type = {
    "01": "服务器登录",
    "02": "阿里云用户",
    "03": "淘宝",
    "04": "学习网站",
    "05": "医院网络配置",
    "06": "重要配置",
    "07": "其他"}


@app.route('/insert_user')
def insert_user():
    user_new = User(user_id='monkeyQK', user_name="管理员",
                    user_password="123456")

    # 单条插入
    db.session.add(user_new)
    db.session.commit()
    return '插入成功！'


def log_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(session.get("user_id"))
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for("login_app"))

    return wrapper


@app.route("/login")
def login_app():
    page_name = "登录"
    return render_template("login.html", page_name=page_name)


@app.route('/check_login', methods=['POST'])
def check_login():
    user_id = request.form.get('user_id')
    # user_id = eval(user_id)
    user_pwd = request.form.get('user_password')
    # user_pwd = eval(user_pwd)
    user = User.query.filter_by(user_id=user_id,
                                user_password=user_pwd).first()
    print(user)
    if user:
        session.permanent = True
        session['user_id'] = user_id
        return redirect(url_for('show'))
    else:
        return "用户名或密码错误！"


@app.route('/regist_user', methods=['POST'])
def regist():
    user_id = request.form.get('user_id')
    # user_id = eval(user_id)
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        return "用户名已存在"
    else:
        pass
    user_name = request.form.get('user_name')
    user_pwd = request.form.get('user_password')
    # user_pwd = eval(user_pwd)
    user_new = User(user_id=user_id, user_name=user_name,
                    user_password=user_pwd)
    # 单条插入
    db.session.add(user_new)
    db.session.commit()
    return redirect(url_for('login_app'))


@app.route('/note_save', methods=['POST'])
def note_save():
    note_name = request.form.get('note_name')
    note_type = request.form.get('note_type')
    my_note_type_r = {v: k for k, v in my_note_type.items()}
    note_type = my_note_type_r[note_type]
    note_addr = request.form.get('note_addr')
    note_username = request.form.get('note_username')
    note_password = request.form.get('note_password')
    note_mark = request.form.get('note_mark')
    note_info = Note_info(
        note_name=note_name,
        note_type=note_type,
        note_addr=note_addr,
        note_username=note_username,
        note_password=note_password,
        note_mark=note_mark)
    # 单条插入
    db.session.add(note_info)
    db.session.commit()
    return redirect(url_for('show'))


@app.route('/note_show', methods=['POST', 'GET'])
def note_show():
    page_name = "查看记录"
    note_id = request.args.get('note_id')
    note_info = Note_info.query.filter_by(note_id=note_id).first()
    print(note_info)
    return render_template("note_s.html", page_name=page_name, posts=note_info)


@app.route('/note_del', methods=['POST', 'GET'])
def note_del():
    note_id = request.args.get('note_id')
    try:
        note_info = Note_info.query.filter_by(note_id=note_id).first()
        db.session.delete(note_info)
        db.session.commit()
        return redirect(url_for('show'))
    except Exception as e:
        return '删除失败！'


@app.route('/update_list', methods=['POST', 'GET'])
def update_list():
    page_name = "修改记录"
    note_id = request.args.get('note_id')
    note_info = Note_info.query.filter_by(note_id=note_id).first()
    print(note_info)
    return render_template("note_u.html", page_name=page_name, posts=note_info)


@app.route('/note_update', methods=['POST', 'GET'])
def note_update():
    note_id = request.form.get('note_id')
    note_info = Note_info.query.filter_by(note_id=note_id).first()
    note_info.note_name = request.form.get('note_name')
    note_info.note_type = request.form.get('note_type')
    note_info.note_addr = request.form.get('note_addr')
    note_info.note_username = request.form.get('note_username')
    note_info.note_password = request.form.get('note_password')
    note_info.note_mark = request.form.get('note_mark')
    # 单条插入
    db.session.add(note_info)
    db.session.commit()
    return redirect(url_for('show'))


def findType_id(note_id):
    return my_note_type[note_id]


def ifSelected(note_id_list):
    if note_id_list[0] == note_id_list[1]:
        return "selected"
    else:
        return ""


@app.route("/logo_out")
def logo_out():
    session.clear()
    return redirect(url_for('index'))


@app.route("/regist")
def reg_app():
    page_name = "注册"
    return render_template("reg.html", page_name=page_name)


@app.route("/")
def index():
    page_name = "首页"
    if db_init():
        return render_template("index.html", page_name=page_name)
    else:
        return "系统异常，请联系管理员！"


@app.route("/note")
@log_required
def note():
    page_name = "记录"
    return render_template("note.html", page_name=page_name)


@app.route("/list")
@log_required
def show():
    note_info = Note_info.query.all()
    note_dict = json.dumps(
        note_info,
        default=Note_info.obj_to_json,
        ensure_ascii=False)
    posts = json.loads(note_dict)
    return render_template("list.html", posts=posts)


@app.route('/note_query', methods=['POST'])
def note_queryByName():
    keywords = request.form.get('key_words')
    print(request.form.get('key_words'))
    note_list = Note_info.query.filter(
        Note_info.note_name.like(
            '%' + keywords + '%')).all()
    note_dict = json.dumps(
        note_list,
        default=Note_info.obj_to_json,
        ensure_ascii=False)
    posts = json.loads(note_dict)
    return render_template('list.html', posts=posts)



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
    env = app.jinja_env
    env.filters['findType_id'] = findType_id
    env.filters['ifSelected'] = ifSelected
    app.run(debug=True, host="192.168.33.11", port=8080)


if __name__ == '__main__':
    main()
