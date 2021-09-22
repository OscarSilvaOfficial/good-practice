from operator import imod
from flask_restful import Api as RestfulApi
from api.apps.covid.urls import urls as covid_urls
from api.sqlalchemy import db, migrate
from flask import Flask

def flask_sqlalchemy(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:123456@127.0.0.1/db"

def create_urls(api):
    covid_urls(api)

def flask_restful(app: Flask):
    api=RestfulApi(app)
    api.prefix = '/api'
    create_urls(api)

def create_api():
    app = Flask(__name__)

    flask_sqlalchemy(app)
    flask_restful(app)

    return app