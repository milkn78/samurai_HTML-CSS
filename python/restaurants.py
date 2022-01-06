restaurants = "hogehoge"
response = "hugahuga"

restaurants = []
response = "hugahuga"

def write_data_to_csv():
    restaurants = []
    response = "hugahuga"
    
    return print(restaurants)
    
    
write_data_to_csv()

{'results': {
    'api_version': '1.26',
    'error': [{'code': 2000, 'message': 'APIキーが正しくありません'}]
    }
}

{'results': {
    'api_version': '1.26',
    'error': [{'code': 2000, 'message': 'APIキーが正しくありません'}]
    }
}

def write_data_to_csv():
    restaurants = []
    response = "hogehoge"
    if "error" in response["results"]:
        return print("エラーが発生しました!")
        
    return print(restaurants)
    
write_data_to_csv()

def write_data_to_csv():
    restaurants = []
    response = "hogehoge"
    if "error" in response:
        return print("エラーが発生しました!")
    for restaurant in response["rest"]:
        restaurant_name = restaurant["name"]
        restaurants.append(restaurant_name)
        
    return print(restaurants)
    
write_data_to_csv()

# restaurants_searcher.py

import csv
import json
import requests

def write_data_to_csv():
    restaurants = []
    response = "hogehoge"
    if "error" in response:
        return print("エラーが発生しました!")
    for i in response["rest"]:
        restaurants_name = i["name"]
        restaurants.append(restaurants_name)
        
    return print(restaurants)
    
write_data_to_csv

# 初期設定
KEYID = "c25e3dd16cfba45f"
COUNT = 100
PREF = "Z011"
FREEWORD = "渋谷駅"
FORMAT = "json"

PARAMS = {"key": KEYID, "count":COUNT, "large_area":PREF, "keyword":FREEWORD, "format":FORMAT}
json_res = requests.get("http://webservice.recruit.co.jp/hotpepper/gourmet/v1/", params=params).text
response = json.loads(json_res)

with open("restaurants_list.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(restaurants)