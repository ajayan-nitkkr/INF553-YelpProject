"""
Author: Ajay Anand
"""

import pandas as pd

from src.data_preparation.input_data_schema import LasVegasGovtDataSchema, YelpBusinessDataSchema
from src.data_schema.feature_names import FeatureNames
from src.utils.inputOutput_utils import csvWriter


def rename_govt_data_features(df):
    lv_object = LasVegasGovtDataSchema()
    schema_object = FeatureNames()
    df.rename(columns={lv_object.COL_RESTAURANT_NAME: schema_object.COL_NAME}, inplace=True)
    df.rename(columns={lv_object.COL_LOCATION_NAME: schema_object.COL_LOCATION_NAME}, inplace=True)
    df.rename(columns={lv_object.COL_CATEGORY_NAME: schema_object.COL_CATEGORY_NAME}, inplace=True)
    df.rename(columns={lv_object.COL_ADDRESS: schema_object.COL_ADDRESS}, inplace=True)
    df.rename(columns={lv_object.COL_CITY: schema_object.COL_CITY}, inplace=True)
    df.rename(columns={lv_object.COL_STATE: schema_object.COL_STATE}, inplace=True)
    df.rename(columns={lv_object.COL_ZIP: schema_object.COL_ZIP}, inplace=True)
    df.rename(columns={lv_object.COL_VIOLATIONS: schema_object.COL_VIOLATIONS}, inplace=True)
    df.rename(columns={lv_object.COL_CURRENT_DEMERITS: schema_object.COL_CURRENT_DEMERITS}, inplace=True)
    df.rename(columns={lv_object.COL_INSPECTION_DEMERITS: schema_object.COL_INSPECTION_DEMERITS}, inplace=True)
    df.rename(columns={lv_object.COL_CURRENT_SCORE: schema_object.COL_CURRENT_SCORE}, inplace=True)
    df.rename(columns={lv_object.COL_INSPECTION_SCORE: schema_object.COL_INSPECTION_SCORE}, inplace=True)
    df.rename(columns={lv_object.COL_CURRENT_GRADE: schema_object.COL_CURRENT_GRADE}, inplace=True)
    df.rename(columns={lv_object.COL_INSPECTION_GRADE: schema_object.COL_INSPECTION_GRADE}, inplace=True)
    return df


def rename_yelp_challenge_features(df):
    yelp_obj = YelpBusinessDataSchema()
    schema_obj = FeatureNames()
    df.rename(columns={yelp_obj.COL_BUSINESS_ID: schema_obj.COL_BUSINESS_ID}, inplace=True)
    df.rename(columns={yelp_obj.COL_RESTAURANT_NAME: schema_obj.COL_NAME}, inplace=True)
    df.rename(columns={yelp_obj.COL_NEIGHBORHOOD: schema_obj.COL_NEIGHBORHOOD}, inplace=True)
    df.rename(columns={yelp_obj.COL_ADDRESS: schema_obj.COL_ADDRESS}, inplace=True)
    df.rename(columns={yelp_obj.COL_CITY: schema_obj.COL_CITY}, inplace=True)
    df.rename(columns={yelp_obj.COL_STATE: schema_obj.COL_STATE}, inplace=True)
    df.rename(columns={yelp_obj.COL_ZIP: schema_obj.COL_ZIP}, inplace=True)
    df.rename(columns={yelp_obj.COL_STARS: schema_obj.COL_RATING}, inplace=True)
    df.rename(columns={yelp_obj.COL_REVIEW_COUNT: schema_obj.COL_REVIEW_COUNT}, inplace=True)
    df.rename(columns={yelp_obj.COL_ACCEPTS_INSURANCE: schema_obj.COL_ACCEPTS_INSURANCE}, inplace=True)
    df.rename(columns={yelp_obj.COL_AGES_ALLOWED: schema_obj.COL_AGES_ALLOWED}, inplace=True)
    df.rename(columns={yelp_obj.COL_ALCOHOL: schema_obj.COL_ALCOHOL}, inplace=True)
    df.rename(columns={yelp_obj.COL_AMBIENCE: schema_obj.COL_AMBIENCE}, inplace=True)
    df.rename(columns={yelp_obj.COL_BYOB: schema_obj.COL_BYOB}, inplace=True)
    df.rename(columns={yelp_obj.COL_BYOB_Corkage: schema_obj.COL_BYOB_Corkage}, inplace=True)
    df.rename(columns={yelp_obj.COL_BEST_NIGHTS: schema_obj.COL_BEST_NIGHTS}, inplace=True)
    df.rename(columns={yelp_obj.COL_BIKE_PARKING: schema_obj.COL_BIKE_PARKING}, inplace=True)
    df.rename(columns={yelp_obj.COL_BUSINESS_ACCEPTS_BITCOIN: schema_obj.COL_BUSINESS_ACCEPTS_BITCOIN}, inplace=True)
    df.rename(columns={yelp_obj.COL_BUSINESS_ACCEPTS_CREDITCARDS: schema_obj.COL_BUSINESS_ACCEPTS_CREDITCARDS}, inplace=True)
    df.rename(columns={yelp_obj.COL_BUSINESS_PARKING: schema_obj.COL_BUSINESS_PARKING}, inplace=True)
    df.rename(columns={yelp_obj.COL_BYAPPOINTMENTONLY: schema_obj.COL_BYAPPOINTMENTONLY}, inplace=True)
    df.rename(columns={yelp_obj.COL_CATERS: schema_obj.COL_CATERS}, inplace=True)
    df.rename(columns={yelp_obj.COL_COAT_CHECK: schema_obj.COL_COAT_CHECK}, inplace=True)
    df.rename(columns={yelp_obj.COL_CORKAGE: schema_obj.COL_CORKAGE}, inplace=True)
    df.rename(columns={yelp_obj.COL_DIETARY_RESTRICTIONS: schema_obj.COL_DIETARY_RESTRICTIONS}, inplace=True)
    df.rename(columns={yelp_obj.COL_DOGS_ALLOWED: schema_obj.COL_DOGS_ALLOWED}, inplace=True)
    df.rename(columns={yelp_obj.COL_DRIVE_THRU: schema_obj.COL_DRIVE_THRU}, inplace=True)
    df.rename(columns={yelp_obj.COL_GOOD_FOR_DANCING: schema_obj.COL_GOOD_FOR_DANCING}, inplace=True)
    df.rename(columns={yelp_obj.COL_GOOD_FOR_KIDS: schema_obj.COL_GOOD_FOR_KIDS}, inplace=True)
    df.rename(columns={yelp_obj.COL_GOOD_FOR_MEAL: schema_obj.COL_GOOD_FOR_MEAL}, inplace=True)
    df.rename(columns={yelp_obj.COL_HAIR_SPECIALIZES_IN: schema_obj.COL_HAIR_SPECIALIZES_IN}, inplace=True)
    df.rename(columns={yelp_obj.COL_HAPPY_HOUR: schema_obj.COL_HAPPY_HOUR}, inplace=True)
    df.rename(columns={yelp_obj.COL_HAS_TV: schema_obj.COL_HAS_TV}, inplace=True)
    df.rename(columns={yelp_obj.COL_MUSIC: schema_obj.COL_MUSIC}, inplace=True)
    df.rename(columns={yelp_obj.COL_NOISE_LEVEL: schema_obj.COL_NOISE_LEVEL}, inplace=True)
    df.rename(columns={yelp_obj.COL_OPEN_24_HOURS: schema_obj.COL_OPEN_24_HOURS}, inplace=True)
    df.rename(columns={yelp_obj.COL_OUTDOOR_SEATING: schema_obj.COL_OUTDOOR_SEATING}, inplace=True)
    df.rename(columns={yelp_obj.COL_RESTAURANTS_ATTIRE: schema_obj.COL_RESTAURANTS_ATTIRE}, inplace=True)
    df.rename(columns={yelp_obj.COL_RESTAURANTS_COUNTER_SERVICE: schema_obj.COL_RESTAURANTS_COUNTER_SERVICE}, inplace=True)
    df.rename(columns={yelp_obj.COL_RESTAURANTS_DELIVERY: schema_obj.COL_RESTAURANTS_DELIVERY}, inplace=True)
    df.rename(columns={yelp_obj.COL_RESTAURANTS_GOOD_FOR_GROUPS: schema_obj.COL_RESTAURANTS_GOOD_FOR_GROUPS}, inplace=True)
    df.rename(columns={yelp_obj.COL_RESTAURANTS_PRICE_RANGE2: schema_obj.COL_RESTAURANTS_PRICE_RANGE2}, inplace=True)
    df.rename(columns={yelp_obj.COL_RESTAURANTS_RESERVATIONS: schema_obj.COL_RESTAURANTS_RESERVATIONS}, inplace=True)
    df.rename(columns={yelp_obj.COL_RESTAURANTS_TABLE_SERVICE: schema_obj.COL_RESTAURANTS_TABLE_SERVICE}, inplace=True)
    df.rename(columns={yelp_obj.COL_RESTAURANTS_TAKEOUT: schema_obj.COL_RESTAURANTS_TAKEOUT}, inplace=True)
    df.rename(columns={yelp_obj.COL_SMOKING: schema_obj.COL_SMOKING}, inplace=True)
    df.rename(columns={yelp_obj.CoL_WHEELCHAIR_ACCESSIBLE: schema_obj.COL_WHEELCHAIR_ACCESSIBLE}, inplace=True)
    df.rename(columns={yelp_obj.COL_WIFI: schema_obj.COL_WIFI}, inplace=True)
    return df


if __name__ == '__main__':

    input_dataset_file = '../../resources/dataset/Overlapped_Data.csv'
    output_dataset_file = '../../resources/dataset/final_lasvegas_dataset.csv'

    input_df = pd.read_csv(input_dataset_file)
    input_df = rename_govt_data_features(input_df)
    input_df = rename_yelp_challenge_features(input_df)
    csvWriter(output_dataset_file, input_df)
