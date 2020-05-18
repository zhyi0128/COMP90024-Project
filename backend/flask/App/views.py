from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from App.analysis import *

api_blueprint = Blueprint('service', __name__, url_prefix='/api')
api = Api(api_blueprint)


def init_router(app):
    app.register_blueprint(api_blueprint)


@api_blueprint.route("/")
def index():
    return "API index"


api.add_resource(MelSentiment, "/generalsenti_mel")
api.add_resource(AllSentiment, "/generalsenti_all")
api.add_resource(CNSentiment, "/cn_all")
api.add_resource(CovidSentiment, "/covid19_all")
