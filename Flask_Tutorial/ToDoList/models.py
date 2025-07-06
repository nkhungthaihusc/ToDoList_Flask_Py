from sqlalchemy import Column
from ToDoList import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime
from zoneinfo import ZoneInfo

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default=False, nullable=False)
    date_created = db.Column(db.DateTime(timezone = True), default=datetime.now(ZoneInfo("Asia/Ho_Chi_Minh")))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer , primary_key = True)
    email = db.Column(db.String(150) , unique = True)
    user_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    notes = db.relationship("Note")

    def __init__(self , email , user_name , password):
        self.email = email
        self.user_name = user_name
        self.password = password
