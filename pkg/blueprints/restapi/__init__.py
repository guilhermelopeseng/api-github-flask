from flask import Blueprint
from flask_restful import Api

from .resources import UserInfoResource

# Use Bluprint
#
# https://flask.palletsprojects.com/en/2.0.x/tutorial/views/

bp = Blueprint("restapi", __name__, url_prefix='/api/v1')
api = Api(bp)

api.add_resource(UserInfoResource, '/user')


def init_app(app):
    app.register_blueprint(bp)
