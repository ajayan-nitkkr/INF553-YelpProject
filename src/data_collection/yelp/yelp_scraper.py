"""
Author: Ajay Anand
"""

import requests
import json

import requests
from bs4 import BeautifulSoup

from src.data_collection.yelp.yelp_feature_names import *
from src.data_schema.feature_names import FeatureNames


"""
add any basic information present for restaurant
"""
def scrap_basic_info(info, result_data):
    schema_obj = FeatureNames()
    basic_data_json = json.loads(info)
    result_data['Price'] = basic_data_json.get(YELP_COl_PRICE)


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


"""
Scrap restaurant data from yelp website based on restaurant url
"""
def scrap_yelp_restaurant_data(restaurant_url):
    requests.packages.urllib3.disable_warnings()
    yelp_path = requests.get(restaurant_url, verify=False)
    soup = BeautifulSoup(yelp_path.text, "html.parser")

    result_data = {}

    basic_data = soup.find('script', type='application/ld+json')
    if basic_data and basic_data.text:
        scrap_basic_info(basic_data.text, result_data)
    else:
        print("Basic data not available for restaurant:", restaurant_url)

    business_info = soup.find("div", {"class": "short-def-list"})
    if business_info:
        scrap_business_info(business_info, result_data)
    else:
        print("Business info not available for restaurant:", restaurant_url)

    # fill_missing_values_As_None()

    json_data = json.dumps(result_data)
    # print(json_data)
    return json_data
