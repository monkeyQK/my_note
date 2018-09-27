from database import db


# 定义模型 Flask-SQLALchemy使用继承至db.Model的类来定义模型,如:

class Note_info(db.Model):
    __tablename__ = 'note_info'
    note_id = db.Column(db.String(64), primary_key=True)
    note_name = db.Column(db.String(30), default="")
    note_type = db.Column(db.String(30), default="")
    note_addr = db.Column(db.String(20), default="")
    note_username = db.Column(db.String(20), default="")
    note_password = db.Column(db.String(20), default="")
    note_mark = db.Column(db.String(100), default="")

    def __repr__(self):
        return '<Note_info %r>' % self.note_name

    def obj_to_json(self):
        return{
            "note_id": self.note_id,
            "note_name": self.note_name,
            "note_addr": self.note_addr,
            "note_username": self.note_username,
            "note_password": self.note_password

        }


class User(db.Model):
    __tablename__ = 'user_info'
    user_id = db.Column(db.String(64), primary_key=True)
    user_name = db.Column(db.String(30), default="")
    user_password = db.Column(db.String(20), default="")

    def __repr__(self):
        return '<User %r>' % self.user_name

    def obj_to_json(self):
        return{
            "user_id": self.user_id,
            "user_name": self.user_name,
            "user_password": self.user_password

        }
