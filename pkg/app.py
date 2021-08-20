from flask import Flask
from pkg.extensions import settings

def create_app():
    app = Flask(__name__)
    settings.init_app(app)
    settings.load_extensions(app)
    return app
