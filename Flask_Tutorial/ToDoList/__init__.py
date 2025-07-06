from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_login import LoginManager
load_dotenv()
from datetime import timedelta


db = SQLAlchemy()
SECRET_KEY = os.getenv('SECRET_KEY')
DB_NAME = os.getenv('DB_NAME')
# print(SECRET_KEY, DB_NAME)

def create_database(app):
    if not os.path.exists("todolist/" + DB_NAME):
        with app.app_context():
            db.create_all()
            print("created db")

def create_app():
    app = Flask(__name__)


    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


    from .models import Note , User
    create_database(app)


    from ToDoList.user import user
    from ToDoList.view import view


    app.register_blueprint(user)
    app.register_blueprint(view)


    login_manager = LoginManager()
    login_manager.login_view = "user.login"
    login_manager.init_app(app)

    app.permanent_session_lifetime = timedelta(minutes=1)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app
