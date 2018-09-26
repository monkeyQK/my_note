from flask import Flask
from flask import render_template


app = Flask(__name__)

# 装饰器的作用url与视图函数的映射


@app.route("/")
def hello_flask():
    return "hello flask!"


@app.route("/login")
def login_app():
    return render_template("login.html", username="monkeyQK")


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
