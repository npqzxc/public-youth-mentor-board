from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    from app.routes_web import web
    from app.routes_api import api

    app.register_blueprint(web)
    app.register_blueprint(api, url_prefix="/api")
    return app
