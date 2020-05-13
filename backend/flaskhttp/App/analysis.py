from flask_restful import Resource
from flask import jsonify
from App.utils import *
import couchdb

couchserver = couchdb.Server('http://admin:happy@172.26.132.133:5984')

# apr_28_db_name = "apr_28_melbourne"
# apr_28_db = couchserver[apr_28_db_name]
# print(apr_28_db["1252751225889546241"]["doc"])

return_json = {

    "name": "Melbourne",
    "value": {
        "positive": 10,
        "negative": 10,
        "neutral": 20,
    }

}


class DataAPI1(Resource):
    def get(self):
        return jsonify({
            "type": "API",
            "TODO": "True"
        })


class AllSentiment(Resource):
    def get(self):
        db = couchserver["scenario_may_3rd_au"]
        general_all_view = db.view(
            '_design/sentiview/_view/general', reduce=True, group=True, group_level=1)
        general_allsenti_view = db.view(
            '_design/sentiview/_view/general', reduce=True, group=True)
        res = get_general_senti(general_all_view, general_allsenti_view)
        return jsonify(res)


class MelSentiment(Resource):

    def get(self):
        db = couchserver["scenario"]
        total_tweets = db.info()["doc_count"]

        general_mel_view = db.view(
            '_design/melview/_view/gsenti', reduce=True, group=True, group_level=1)

        general_melsenti_view = db.view(
            '_design/melview/_view/gsenti', reduce=True, group=True)
        res = get_general_senti(general_mel_view, general_melsenti_view)
        return jsonify(res)
