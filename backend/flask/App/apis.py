from flask_restful import Resource
from flask import jsonify
from App.utils import *
import couchdb

username = "admin"
password = "happy"
ip = "172.26.134.54"
db_address = f'http://{username}:{password}@{ip}:5984'

'''
function (doc) {
  if(doc.pos===1){
    emit([doc.suburb, "pos"], 1);
  } else if (doc.neu === 1) {
    emit([doc.suburb, "neu"], 1);
  } else if (doc.neg === 1) {
    emit([doc.suburb, "neg"], 1);
  }
}
'''

# /generalsenti_all


class AllSentiment(Resource):
    def get(self):
        try:
            couchserver = couchdb.Server(
                db_address)
            db = couchserver["scenario_city"]
        except:
            message = {
                "message": "can't connect to couchdb"
            }
            return(jsonify(message))

        general_all_view = db.view(
            '_design/sentiview/_view/general', reduce=True, group=True, group_level=1)
        general_allsenti_view = db.view(
            '_design/sentiview/_view/general', reduce=True, group=True)
        res = get_general_senti(general_all_view, general_allsenti_view)

        return jsonify(res)


'''
function (doc) {
  if (doc.pos===1) {
    emit([doc.suburb, "pos"], 1);
  } else if (doc.neu===1) {
    emit([doc.suburb, "neu"], 1);
  } else if (doc.neg===1) {
    emit([doc.suburb, "neg"], 1);
  }
}
'''
# /generalsenti_mel


class MelSentiment(Resource):

    def get(self):
        try:
            couchserver = couchdb.Server(
                db_address)
            db = couchserver["scenario_suburb"]
        except:
            message = {
                "message": "can't connect to couchdb"
            }
            return(jsonify(message))

        general_mel_view = db.view(
            '_design/melview/_view/gsenti', reduce=True, group=True, group_level=1)

        general_melsenti_view = db.view(
            '_design/melview/_view/gsenti', reduce=True, group=True)

        res = get_general_senti(general_mel_view, general_melsenti_view)

        return jsonify(res)


'''
function (doc) {
  if(doc.is_china===1) {
    if(doc.pos===1) {
      emit([doc.suburb, "pos", "cn"], 1);
    } else if(doc.neg===1) {
      emit([doc.suburb, "neg", "cn"], 1);
    } else if(doc.neu===1) {
      emit([doc.suburb, "neu", "cn"], 1);
    }
  }
}
'''


class CNSentiment(Resource):

    def get(self):
        try:
            couchserver = couchdb.Server(
                db_address)
            db = couchserver["scenario_may_3rd_au"]
        except:
            message = {
                "message": "can't connect to couchdb"
            }
            return(jsonify(message))
        general_all_view = db.view(
            '_design/sentiview/_view/general', reduce=True, group=True, group_level=1)
        cn_all_view = db.view(
            '_design/sentiview/_view/cn_view', reduce=True, group=True, group_level=2)
        cn_allsenti_view = db.view(
            '_design/sentiview/_view/cn_view', reduce=True, group=True)
        res = get_topic_senti(cn_all_view, cn_allsenti_view, general_all_view)

        return jsonify(res)


'''
function (doc) {
  if(doc.is_covid_19===1) {
    if(doc.pos===1) {
      emit([doc.suburb, "pos", "cn"], 1);
    } else if(doc.neg===1) {
      emit([doc.suburb, "neg", "cn"], 1);
    } else if(doc.neu===1) {
      emit([doc.suburb, "neu", "cn"], 1);
    }
  }
}
'''


class CovidSentiment(Resource):

    def get(self):
        try:
            couchserver = couchdb.Server(
                db_address)
            db = couchserver["scenario_may_3rd_au"]
        except:
            message = {
                "message": "can't connect to couchdb"
            }
            return(jsonify(message))

        general_all_view = db.view(
            '_design/sentiview/_view/general', reduce=True, group=True, group_level=1)
        covid_all_view = db.view(
            '_design/sentiview/_view/covid_view', reduce=True, group=True, group_level=2)
        covid_allsenti_view = db.view(
            '_design/sentiview/_view/covid_view', reduce=True, group=True)
        res = get_topic_senti(
            covid_all_view, covid_allsenti_view, general_all_view)

        return jsonify(res)
