import requests
import json

import requests
from bs4 import BeautifulSoup

from src.data_collection.yelp.yelp_feature_names import *
from src.data_schema.feature_names import *

"""
Scrap restaurant data from yelp website based on restaurant url
"""
def scrap_yelp_restaurant_data(restaurant_url):
    yelp_path = requests.get(restaurant_url, verify=False)
    soup = BeautifulSoup(yelp_path.text, "html.parser")

    result_data = {}

    basic_data = soup.find('script', type='application/ld+json')
    if basic_data and basic_data.text:
        scrap_basic_info(basic_data.text, result_data)

    business_info = soup.find("div", {"class": "short-def-list"})
    if business_info:
        scrap_business_info(business_info, result_data)

    json_data = json.dumps(result_data)
    print(json_data)


"""
add any basic information present for restaurant
"""
def scrap_basic_info(info, result_data):
    basic_data_json = json.loads(info)
    result_data[COl_PRICE] = basic_data_json.get(YELP_COl_PRICE)


"""
add any business information present for restaurant
"""
def scrap_business_info(info, result_data):
    key_list = info.find_all("dt")
    value_list = info.find_all("dd")
    if key_list and value_list:
        for i in range(len(key_list)):
            if key_list[i] and value_list[i]:
                key = key_list[i].text.strip()
                value = value_list[i].text.strip()
                result_data[key] = value