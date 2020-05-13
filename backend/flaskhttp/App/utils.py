def get_general_senti(allview, sentiview):
    results = []
    suburbs = set()
    res = {}
    suburb_tweets = {}
    for row in allview:
        suburb_name = row.key[0]
        suburb_total = row.value
        suburb_tweets[suburb_name] = suburb_total

    for row in sentiview:
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
    return res


def get_topic_senti(allview, sentiview, alltweetview):
    results = []
    suburbs = set()
    res = {}
    suburb_tweets = {}
    suburb_all_tweets = {}
    for row in allview:
        suburb_name = row.key[0]
        suburb_total = row.value
        suburb_tweets[suburb_name] = suburb_total

    for row in alltweetview:
        suburb_name = row.key[0]
        suburb_total = row.value
        suburb_all_tweets[suburb_name] = suburb_total

    for row in sentiview:
        suburb_name = row.key[0]
        senti_type = row.key[2]
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
                    "total_tweets": suburb_all_tweets[suburb_name]
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
    return res
