from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:1234567890@izen.cxppaurfujpc.ap-northeast-2.rds.amazonaws.com:3306/project1?charset=utf8"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
