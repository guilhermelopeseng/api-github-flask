from flask import Blueprint

from .views import index, user

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/user", methods=["POST"], view_func=user)

def init_app(app):
    app.register_blueprint(bp)