#coding:utf-8

import sys
import urllib
import urllib.parse
import urllib.request
import json
import collections as cl
import os

def yapi_topics(i):
    url = 'https://shopping.yahooapis.jp/ShoppingWebService/V1/json/categoryRanking'
    appid = 'ID'
    params = urllib.parse.urlencode(
            {'appid': appid,
             'offset':i,
             'period':'weekly',
             'generation':20,
             'gender':'male',})

    #print url + params
    response = urllib.request.urlopen(url + params)
    return response.read()

def do_json(s):
    data = json.loads(s)

    #print(json.dumps(data, sort_keys=True, indent=4)); sys.exit()
    #print(data)

    #空のディクショナリを作る

    ranking = {}
    for  k, v in item_list.items():
        try:
            rank = int(v["_attributes"]["rank"])
            vector = v["_attributes"]["vector"]
            name  = v["Name"]
            ranking[rank] = [vector, name]
        except:
            if k == "RankingInfo":
                StartDate = v["StartDate"]
                EndDate = v["EndDate"]
    '''
    print ('-' * 40)
    print (u"集計開始日:", StartDate)
    print (u"集計終了日:", EndDate)
    print ('-' * 40)
    '''
    ranking_keys = list(ranking.keys())
    ranking_keys.sort()
    '''
    for i in ranking_keys:
        #print (i, ranking[i][0], ranking [i][1])
        print(i, end='')
        print("「", end='')
        print(ranking[i][0], end='')
        print("」", end='')
        print("「", end='')
        print(ranking[i][1], end='')
        print("」")
    '''

    ranking_list = []
    key_list = []
    name_list = []

    for i in ranking_keys:
        ranking_list.append("ranking")
        key_list.append(ranking[i][0])
        name_list.append(ranking[i][1])
    #print(ranking)
    #print(key_list)
    #print(name_list)

    ys = cl.OrderedDict()
    for i in range(len(ranking_list)):
        data1 = cl.OrderedDict()
        data1["Key"] = key_list[i]
        data1["Name"] = name_list[i]

        ys[i] = data1

    #fw = open('ranking.json','w')
    #fw.close()
    fw = open('ranking2.json','a')
    json.dump(ys,fw,ensure_ascii=False)
    fw.close()



if __name__ == '__main__':

    json_str1 = yapi_topics(1)
    do_json(json_str1)
    json_str2 = yapi_topics(20)
    do_json(json_str2)
    json_str3 = yapi_topics(40)
    do_json(json_str3)
    json_str4 = yapi_topics(60)
    do_json(json_str4)
