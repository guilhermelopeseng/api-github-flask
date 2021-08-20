from flask import Flask
from pkg.extensions import settings

from pkg.blueprints import restapi

app = Flask(__name__)
settings.init_app(app)


restapi.init_app(app)