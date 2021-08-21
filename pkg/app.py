# API Github
#
# Essa API foi desenvolvida em python utilizando o micro-framework Flask
#
# Desenvolvido por: Guilherme Lopes
#

from flask import Flask
from pkg.extensions import settings

# Basic Factorie to start the aplication
#
# https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/


def create_app():
    app = Flask(__name__)
    settings.init_app(app)
    settings.load_extensions(app)
    return app
