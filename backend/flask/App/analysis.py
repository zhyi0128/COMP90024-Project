from flask_restful import Resource
from flask import jsonify


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


class DataAPI2(Resource):
    def post(self):
        pass

    def get(self):
        pass