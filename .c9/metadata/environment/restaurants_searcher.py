{"filter":false,"title":"restaurants_searcher.py","tooltip":"/restaurants_searcher.py","undoManager":{"mark":5,"position":5,"stack":[[{"start":{"row":0,"column":0},"end":{"row":82,"column":32},"action":"remove","lines":["restaurants = \"hogehoge\"","response = \"hugahuga\"","","restaurants = []","response = \"hugahuga\"","","def write_data_to_csv():","    restaurants = []","    response = \"hugahuga\"","    ","    return print(restaurants)","    ","    ","write_data_to_csv()","","{'results': {","    'api_version': '1.26',","    'error': [{'code': 2000, 'message': 'APIキーが正しくありません'}]","    }","}","","{'results': {","    'api_version': '1.26',","    'error': [{'code': 2000, 'message': 'APIキーが正しくありません'}]","    }","}","","def write_data_to_csv():","    restaurants = []","    response = \"hogehoge\"","    if \"error\" in response[\"results\"]:","        return print(\"エラーが発生しました!\")","        ","    return print(restaurants)","    ","write_data_to_csv()","","def write_data_to_csv():","    restaurants = []","    response = \"hogehoge\"","    if \"error\" in response:","        return print(\"エラーが発生しました!\")","    for restaurant in response[\"rest\"]:","        restaurant_name = restaurant[\"name\"]","        restaurants.append(restaurant_name)","        ","    return print(restaurants)","    ","write_data_to_csv()","","# restaurants_searcher.py","","import csv","import json","import requests","","def write_data_to_csv():","    restaurants = []","    response = \"hogehoge\"","    if \"error\" in response:","        return print(\"エラーが発生しました!\")","    for i in response[\"rest\"]:","        restaurants_name = i[\"name\"]","        restaurants.append(restaurants_name)","        ","    return print(restaurants)","    ","write_data_to_csv","","# 初期設定","KEYID = \"c25e3dd16cfba45f\"","COUNT = 100","PREF = \"Z011\"","FREEWORD = \"渋谷駅\"","FORMAT = \"json\"","","PARAMS = {\"key\": KEYID, \"count\":COUNT, \"large_area\":PREF, \"keyword\":FREEWORD, \"format\":FORMAT}","json_res = requests.get(\"http://webservice.recruit.co.jp/hotpepper/gourmet/v1/\", params=params).text","response = json.loads(json_res)","","with open(\"restaurants_list.csv\", \"w\") as f:","    writer = csv.writer(f)","    writer.writerow(restaurants)"],"id":15}],[{"start":{"row":0,"column":0},"end":{"row":29,"column":25},"action":"insert","lines":["# restaurants_searcher.py","","import json","import csv","import requests","","# 初期設定","KEYID = \"メールに記載されていたアクセスキーをここに入力\"","COUNT = 100","PREF = \"Z011\"","FREEWORD = \"渋谷駅\"","FORMAT = \"json\"","","PARAMS = {\"key\": KEYID, \"count\":COUNT, \"large_area\":PREF, \"keyword\":FREEWORD, \"format\":FORMAT}","","def write_data_to_csv(params):","    restaurants = []","    json_res = requests.get(\"http://webservice.recruit.co.jp/hotpepper/gourmet/v1/\", params=params).text","    response = json.loads(json_res)","    if \"error\" in response[\"results\"]:","        return print(\"エラーが発生しました！\")","    for restaurant in response[\"results\"][\"shop\"]:","        restaurant_name = restaurant[\"name\"]","        restaurants.append(restaurant_name)","    with open(\"restaurants_list.csv\", \"w\") as f:","        writer = csv.writer(f)","        writer.writerow(restaurants)","    return print(restaurants)","","write_data_to_csv(PARAMS)"],"id":16}],[{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"remove","lines":["力"],"id":17},{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"remove","lines":["入"]},{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"remove","lines":["に"]},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"remove","lines":["こ"]},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"remove","lines":["こ"]},{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"remove","lines":["を"]},{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"remove","lines":["ー"]},{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"remove","lines":["キ"]},{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"remove","lines":["ス"]},{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"remove","lines":["セ"]},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"remove","lines":["ク"]}],[{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"remove","lines":["ア"],"id":18},{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"remove","lines":["た"]},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"remove","lines":["い"]},{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"remove","lines":["て"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"remove","lines":["れ"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"remove","lines":["さ"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"remove","lines":["載"]},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"remove","lines":["記"]},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"remove","lines":["に"]},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"remove","lines":["ル"]},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"remove","lines":["ー"]},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"remove","lines":["メ"]}],[{"start":{"row":7,"column":9},"end":{"row":7,"column":25},"action":"insert","lines":["c25e3dd16cfba45f"],"id":19}],[{"start":{"row":29,"column":25},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":20},{"start":{"row":30,"column":0},"end":{"row":31,"column":0},"action":"insert","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":29,"column":25},"end":{"row":29,"column":25},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1640260667536,"hash":"fbf99d514c2084a6143c08337609c6c23448d646"}