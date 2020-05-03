from flask import Flask

from App.views import init_router


def create_app():
    app = Flask(__name__)

    # Initial router
    init_router(app)

    return app
