from flask_restful import Resource
from flask import jsonify

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


class GetPrices(Resource):

    def get(self):
        # dv = fruits.view('_design/myDesignDoc/_view/prices')
        # prices = []
        # for row in dv:
        #     prices.append(row)
        # print(dv)
        # print(type(dv))
        # print(len(dv))
        prices = [
            {
                "id": "35c87c40c9a5da1d0a13ddc0ef00858a",
                "key": [
                    "apple",
                    0.79
                ],
                "value": "Apples Express"
            },
            {
                "id": "35c87c40c9a5da1d0a13ddc0ef00858a",
                "key": [
                    "apple",
                    1.59
                ],
                "value": "Fresh Mart"
            },
            {
                "id": "35c87c40c9a5da1d0a13ddc0ef00858a",
                "key": [
                    "apple",
                    5.99
                ],
                "value": "Price Max"
            },
            {
                "id": "35c87c40c9a5da1d0a13ddc0ef00b35d",
                "key": [
                    "banana",
                    0.79
                ],
                "value": "Price Max"
            },
            {
                "id": "35c87c40c9a5da1d0a13ddc0ef00b35d",
                "key": [
                    "banana",
                    1.99
                ],
                "value": "Fresh Mart"
            },
            {
                "id": "35c87c40c9a5da1d0a13ddc0ef00b35d",
                "key": [
                    "banana",
                    4.22
                ],
                "value": "Banana Montana"
            },
            {
                "id": "35c87c40c9a5da1d0a13ddc0ef0091ba",
                "key": [
                    "orange",
                    1.09
                ],
                "value": "Citrus Circus"
            },
            {
                "id": "35c87c40c9a5da1d0a13ddc0ef0091ba",
                "key": [
                    "orange",
                    1.99
                ],
                "value": "Fresh Mart"
            },
            {
                "id": "35c87c40c9a5da1d0a13ddc0ef0091ba",
                "key": [
                    "orange",
                    3.19
                ],
                "value": "Price Max"
            }
        ]
        return jsonify(prices)


class MelSentiment(Resource):

    def get(self):
        results = []
        suburbs = set()
        result = {}
        res = {}
        suburb_tweets = {}
        db = couchserver["scenario"]
        total_tweets = db.info()["doc_count"]

        general_mel_view = db.view(
            '_design/melview/_view/gsenti', reduce=True, group=True, group_level=1)

        general_melsenti_view = db.view(
            '_design/melview/_view/gsenti', reduce=True, group=True)
        for row in general_mel_view:
            suburb_name = row.key[0]
            suburb_total = row.value

            suburb_tweets[suburb_name] = suburb_total

            # result[suburb_name] =
        for row in general_melsenti_view:
            suburb_name = row.key[0]
            senti_type = row.key[1]
            senti_num = row.value
            if suburb_name not in suburbs:
                negative = 0
                positive = 0
                neutral = 0
                if senti_type == "neg":
                    negative = senti_num
                elif senti_type == "neu":
                    neutral = senti_num
                elif senti_type == "pos":
                    positive = senti_num

                res[suburb_name] = {
                    "name": suburb_name,
                    "data": {
                        "sentiment": {
                            "neutral": neutral,
                            "negative": negative,
                            "positive": positive
                        },
                        "related_tweets": suburb_tweets[suburb_name],
                        "total_tweets": suburb_tweets[suburb_name]
                    }
                }
                suburbs.add(suburb_name)
            else:
                if senti_type == "neg":
                    negative = senti_num
                    res[suburb_name]['data']['sentiment'].update(
                        {"negative": negative})
                elif senti_type == "neu":
                    neutral = senti_num
                    res[suburb_name]['data']['sentiment'].update(
                        {"neutral": neutral})
                elif senti_type == "pos":
                    positive = senti_num
                    res[suburb_name]['data']['sentiment'].update(
                        {"positive": positive})
            # for data in res.values():
            #     results.append(data)
        return jsonify(res)
