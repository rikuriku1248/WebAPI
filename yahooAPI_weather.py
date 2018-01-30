# -*- coding: utf-8 -*-

import json
import requests

url = 'https://map.yahooapis.jp/weather/V1/place'
appid = 'ID'

query = {
        'appid' : appid, #アプリケーションID
        'coordinates' : '136.627205, 36.529954', #経度, 緯度
        'output' : 'json', #出力形式
        #'date' : 'YYYYMMDDHHMI', #日時指定
        #'past' : '0', #過去の香水強度実測値
        #'interval' : '10', #取得間隔
        }

r = requests.get(url, params=query);
print (r)
j = r.json()
print (json.dumps(j, sort_keys=True, indent=2))
