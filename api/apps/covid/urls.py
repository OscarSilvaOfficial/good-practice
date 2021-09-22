from flask_restful import Api as RestfulApi
from . import views

def urls(app):
    app.add_resource(views.CovidResource, '/covid')