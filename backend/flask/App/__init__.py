from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_router


def create_app(env):
    app = Flask(__name__)


    # Initialization of third-party plugins
    init_ext(app)

    # Initial router
    init_router(app)

    return app
