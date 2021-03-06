"""
Author: Ajay Anand
"""

import json
import pandas as pd
import time
from src.data_collection.yelp.yelp_api_adapter import search_yelp_restaurant
from src.data_collection.yelp.yelp_scraper import scrap_yelp_restaurant_data
from src.data_schema.feature_names import FeatureNames
# from src.data_preparation.input_data_schema import YelpBusinessDataSchema
# from src.data_collection.yelp.yelp_feature_names import *


def traverse_business_data(yelp_df):
    schema_obj = FeatureNames()
    restaurant_list = []
    for index, row in yelp_df.iterrows():
        print("index:",index)
        # if index >= 10:
        #     break
        business_id = row[schema_obj.COL_BUSINESS_ID]
        if business_id:
            business_data = search_yelp_restaurant(business_id)
            if not(business_data and type(business_data) is dict):
                print("Not able to search for business id:",business_id)
            elif 'url' not in business_data or business_data['url'] == "":
                print("Url not found for business id:", business_id)
            else:
                scraped_data = scrap_yelp_restaurant_data(business_data['url'])
                scraped_data = json.loads(scraped_data)
                scraped_data['business_id'] = business_id
                restaurant_list.append(scraped_data)

    # result = json.dumps(restaurant_list)[0]
    print(restaurant_list)
    return restaurant_list


if __name__ == '__main__':
    program_start_time = round(time.time() * 1000)
    # business_id = 'hTzcHtk4-0QJnFUbkKpd5Q'
    # name = 'Citi Trends'
    # latitude = '36.1783477'
    # longitude = '-115.1769162'
    # business_data = search_yelp_restaurant(business_id)
    # scraped_data = scrap_yelp_restaurant_data(business_data['url'])
    # print(scraped_data)
    # yelp_business_file = '../../../resources/dataset/LasVegas_Restaurants_Rimsha_Preprocessed.csv'
    dataset_file = '../../../resources/dataset/final_lasvegas_dataset.csv'
    yelp_output_file = '../../../resources/dataset/scraped_data.csv'
    df = pd.read_csv(dataset_file)
    # df = df[100:200]
    result = traverse_business_data(df)
    # yelp_df = create_yelp_data_frame_new_format(result)
    yelp_df = pd.DataFrame.from_dict(result, orient='columns')
    yelp_df.to_csv(yelp_output_file, encoding='utf-8', index=False, mode='a', header=True)
    print("finished...")
    program_end_time = round(time.time() * 1000)
    print("\nProgram run time:", (program_end_time - program_start_time)/1000, "s")

