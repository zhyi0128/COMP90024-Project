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


api.add_resource(GetPrices, '/getprices/')
api.add_resource(DataAPI1, "/dataapi1/")
api.add_resource(MelSentiment, "/melsentiment")
