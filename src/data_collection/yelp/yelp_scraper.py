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


def fill_missing_values_As_Null(result_data):
    if YELP_COl_TAKES_RESERVATIONS not in result_data: result_data[YELP_COl_TAKES_RESERVATIONS] = "Null"
    if YELP_COl_DELIVERY not in result_data: result_data[YELP_COl_DELIVERY] = "Null"
    if YELP_COl_TAKE_OUT not in result_data: result_data[YELP_COl_TAKE_OUT] = "Null"
    if YELP_COl_ACCEPTS_CREDIT_CARD not in result_data: result_data[YELP_COl_ACCEPTS_CREDIT_CARD] = "Null"
    if YELP_COl_ACCEPTS_APPLE_PAY not in result_data: result_data[YELP_COl_ACCEPTS_APPLE_PAY] = "Null"
    if YELP_COl_GOOD_FOR not in result_data: result_data[YELP_COl_GOOD_FOR] = "Null"
    if YELP_COl_PARKING not in result_data: result_data[YELP_COl_PARKING] = "Null"
    if YELP_COl_BIKE_PARKING not in result_data: result_data[YELP_COl_BIKE_PARKING] = "Null"
    if YELP_COl_GOOD_FOR_KIDS not in result_data: result_data[YELP_COl_GOOD_FOR_KIDS] = "Null"
    if YELP_COl_GOOD_FOR_GROUPS not in result_data: result_data[YELP_COl_GOOD_FOR_GROUPS] = "Null"
    if YELP_COl_ATTIRE not in result_data: result_data[YELP_COl_ATTIRE] = "Null"
    if YELP_COl_AMBIENCE not in result_data: result_data[YELP_COl_AMBIENCE] = "Null"
    if YELP_COl_NOISE_LEVEL not in result_data: result_data[YELP_COl_NOISE_LEVEL] = "Null"
    if YELP_COl_ALCOHOL not in result_data: result_data[YELP_COl_ALCOHOL] = "Null"
    if YELP_COl_OUTDOOR_SEATING not in result_data: result_data[YELP_COl_OUTDOOR_SEATING] = "Null"
    if YELP_COl_WIFI not in result_data: result_data[YELP_COl_WIFI] = "Null"
    if YELP_COl_HAS_TV not in result_data: result_data[YELP_COl_HAS_TV] = "Null"
    if YELP_COl_CATERS not in result_data: result_data[YELP_COl_CATERS] = "Null"
    if YELP_COl_GOOD_FOR_WORKING not in result_data: result_data[YELP_COl_GOOD_FOR_WORKING] = "Null"
    if YELP_COl_GENDER_NEUTRAL_RESTROOMS not in result_data: result_data[YELP_COl_GENDER_NEUTRAL_RESTROOMS] = "Null"
    if YELP_COl_ACCEPTS_BITCOIN not in result_data: result_data[YELP_COl_ACCEPTS_BITCOIN] = "Null"
    if YELP_COl_ACCEPTS_GOOGLE_PAY not in result_data: result_data[YELP_COl_ACCEPTS_GOOGLE_PAY] = "Null"
    if YELP_COl_BEST_NIGHTS not in result_data: result_data[YELP_COl_BEST_NIGHTS] = "Null"
    if YELP_COl_BY_APPOINTMENT_ONLY not in result_data: result_data[YELP_COl_BY_APPOINTMENT_ONLY] = "Null"
    if YELP_COL_COAT_CHECK not in result_data: result_data[YELP_COL_COAT_CHECK] = "Null"
    if YELP_COL_DOGS_ALLOWED not in result_data: result_data[YELP_COL_DOGS_ALLOWED] = "Null"
    if YELP_COL_DRIVE_THRU not in result_data: result_data[YELP_COL_DRIVE_THRU] = "Null"
    if YELP_COL_GOOD_FOR_DANCING not in result_data: result_data[YELP_COL_GOOD_FOR_DANCING] = "Null"
    if YELP_COL_HAPPY_HOUR not in result_data: result_data[YELP_COL_HAPPY_HOUR] = "Null"
    if YELP_COL_HAS_GLUTEN_FREE_OPTIONS not in result_data: result_data[YELP_COL_HAS_GLUTEN_FREE_OPTIONS] = "Null"
    if YELP_COL_HAS_POOL_TABLE not in result_data: result_data[YELP_COL_HAS_POOL_TABLE] = "Null"
    if YELP_COL_LIKED_BY_VEGANS not in result_data: result_data[YELP_COL_LIKED_BY_VEGANS] = "Null"
    if YELP_COL_LIKED_BY_VEGETARIANS not in result_data: result_data[YELP_COL_LIKED_BY_VEGETARIANS] = "Null"
    if YELP_COL_OFFERS_MILITARY_DISCOUNT not in result_data: result_data[YELP_COL_OFFERS_MILITARY_DISCOUNT] = "Null"
    if YELP_COL_SMOKING not in result_data: result_data[YELP_COL_SMOKING] = "Null"
    if YELP_COL_WAITER_SERVICE not in result_data: result_data[YELP_COL_WAITER_SERVICE] = "Null"
    if YELP_COL_WHEELCHAIR_ACCESSIBLE not in result_data: result_data[YELP_COL_WHEELCHAIR_ACCESSIBLE] = "Null"
    return result_data


"""
Scrap restaurant data from yelp website based on restaurant url
"""
def scrap_yelp_restaurant_data(restaurant_url):
    requests.packages.urllib3.disable_warnings()
    yelp_path = requests.get(restaurant_url, verify=False)
    soup = BeautifulSoup(yelp_path.text, "html.parser")

    result_data = {}

    # basic_data = soup.find('script', type='application/ld+json')
    # basic_data_new = soup.find("dl", {"class": "short-def-list"})
    # if basic_data and basic_data.text:
    #     scrap_basic_info(basic_data.text, result_data)
    # else:
    #     print("Basic data not available for restaurant:", restaurant_url)

    business_info = soup.find("div", {"class": "short-def-list"})
    if business_info:
        scrap_business_info(business_info, result_data)
    else:
        print("Business info not available for restaurant:", restaurant_url)

    fill_missing_values_As_Null(result_data)

    json_data = json.dumps(result_data)
    # print(json_data)
    return json_data
