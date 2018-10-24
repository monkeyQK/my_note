# 导入模块
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


# 创建flask对象
app = Flask(__name__)

# 配置flask配置对象中键：SQLALCHEMY_DATABASE_URI

# dialect+driver://username:password@host:port/database

dialect = "mysql"
driver = "mysqlconnector"
username = "root"
password = "password"
host = "192.168.3.11"
port = '3306'
database = "my_notes"
conn_url = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
    dialect, driver, username, password, host, port, database)


app.config['SQLALCHEMY_DATABASE_URI'] = conn_url

# 配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动

app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'asdfasd'
# 获取SQLAlchemy实例对象，接下来就可以使用对象调用数据

db = SQLAlchemy(app)
