"""
Author: Ajay Anand
"""

import pandas as pd
import numpy as np
from src.data_preparation.input_data_schema import LosAngelesGovtDataSchema
from src.data_schema.feature_names import FeatureNames
from src.utils.inputOutput_utils import csvWriter


"""
rename the column feature names as per schema,
drop the columns not in schema,
create new columns in schema with Null values
"""
def prepare_la_data_features(df):
    la_object = LosAngelesGovtDataSchema()
    schema_object = FeatureNames()
    df.rename(columns={la_object.COL_NAME: schema_object.COL_NAME}, inplace=True)
    df[schema_object.COL_LOCATION_NAME] = "Null"
    df[schema_object.COL_CATEGORY_NAME] = "Null"
    df.rename(columns={la_object.COL_SITE_ADDRESS: schema_object.COL_ADDRESS}, inplace=True)
    df.rename(columns={la_object.COL_SITE_CITY: schema_object.COL_CITY}, inplace=True)
    df.rename(columns={la_object.COL_SITE_STATE: schema_object.COL_STATE}, inplace=True)
    df.rename(columns={la_object.COL_SITE_ZIP: schema_object.COL_ZIP}, inplace=True)
    df[schema_object.COL_VIOLATIONS] = "Null"
    df[schema_object.COL_CURRENT_DEMERITS] = "Null"
    df[schema_object.COL_INSPECTION_DEMERITS] = "Null"
    df.rename(columns={la_object.COl_SCORE: schema_object.COL_CURRENT_SCORE}, inplace=True)
    df[schema_object.COL_INSPECTION_SCORE] = "Null"
    df.rename(columns={la_object.COL_GRADE: schema_object.COL_CURRENT_GRADE}, inplace=True)
    df[schema_object.COL_INSPECTION_GRADE] = "Null"
    df[schema_object.COL_BUSINESS_ID] = "Null"
    df[schema_object.COL_NEIGHBORHOOD] = "Null"
    df.rename(columns={la_object.COl_RATING: schema_object.COL_RATING}, inplace=True)
    df.rename(columns={la_object.COL_REVIEW: schema_object.COL_REVIEW_COUNT}, inplace=True)
    df[schema_object.COL_ACCEPTS_INSURANCE] = "Null"
    df[schema_object.COL_AGES_ALLOWED] = "Null"
    df.rename(columns={la_object.COl_ALCOHOL: schema_object.COL_ALCOHOL}, inplace=True)
    df.rename(columns={la_object.COl_AMBIENCE: schema_object.COL_AMBIENCE}, inplace=True)
    df[schema_object.COL_BYOB] = "Null"
    df[schema_object.COL_BYOB_Corkage] = "Null"
    df[schema_object.COL_BEST_NIGHTS] = "Null"
    df.rename(columns={la_object.COl_BIKE_PARKING: schema_object.COL_BIKE_PARKING}, inplace=True)
    df[schema_object.COL_BUSINESS_ACCEPTS_BITCOIN] = "Null"
    df.rename(columns={la_object.COl_ACCEPT_CREDIT_CARD: schema_object.COL_BUSINESS_ACCEPTS_CREDITCARDS}, inplace=True)
    df[schema_object.COL_BUSINESS_PARKING] = "Null"
    df[schema_object.COL_BYAPPOINTMENTONLY] = "Null"
    df.rename(columns={la_object.COL_CATERS: schema_object.COL_CATERS}, inplace=True)
    df[schema_object.COL_COAT_CHECK] = "Null"
    df[schema_object.COL_CORKAGE] = "Null"
    df[schema_object.COL_DIETARY_RESTRICTIONS] = "Null"
    df[schema_object.COL_DOGS_ALLOWED] = "Null"
    df[schema_object.COL_DRIVE_THRU] = "Null"
    df[schema_object.COL_GOOD_FOR_DANCING] = "Null"
    df.rename(columns={la_object.COL_GOOD_FOR_KIDS: schema_object.COL_GOOD_FOR_KIDS}, inplace=True)
    df[schema_object.COL_GOOD_FOR_MEAL] = "Null"
    df[schema_object.COL_HAIR_SPECIALIZES_IN] = "Null"
    df[schema_object.COL_HAPPY_HOUR] = "Null"
    df.rename(columns={la_object.COL_HAS_TV: schema_object.COL_HAS_TV}, inplace=True)
    df[schema_object.COL_MUSIC] = "Null"
    df.rename(columns={la_object.COl_NOISE_LEVEL: schema_object.COL_NOISE_LEVEL}, inplace=True)
    df[schema_object.COL_OPEN_24_HOURS] = "Null"
    df.rename(columns={la_object.COL_OUTDOOR_SEATING: schema_object.COL_OUTDOOR_SEATING}, inplace=True)
    df.rename(columns={la_object.COL_ATTIRE: schema_object.COL_RESTAURANTS_ATTIRE}, inplace=True)
    df[schema_object.COL_RESTAURANTS_COUNTER_SERVICE] = "Null"
    df.rename(columns={la_object.COl_DELIVERY: schema_object.COL_RESTAURANTS_DELIVERY}, inplace=True)
    df.rename(columns={la_object.COL_GOOD_FOR_GROUPS: schema_object.COL_RESTAURANTS_GOOD_FOR_GROUPS}, inplace=True)
    df.rename(columns={la_object.COl_PRICE: schema_object.COL_RESTAURANTS_PRICE_RANGE2}, inplace=True)
    df.rename(columns={la_object.COl_TAKES_RESERVATIONS: schema_object.COL_RESTAURANTS_RESERVATIONS}, inplace=True)
    df[schema_object.COL_RESTAURANTS_TABLE_SERVICE] = "Null"
    df.rename(columns={la_object.COl_TAKEOUT: schema_object.COL_RESTAURANTS_TAKEOUT}, inplace=True)
    df[schema_object.COL_SMOKING] = "Null"
    df[schema_object.COL_WHEELCHAIR_ACCESSIBLE] = "Null"
    df.rename(columns={la_object.COL_WIFI: schema_object.COL_WIFI}, inplace=True)
    df.rename(columns={la_object.COl_ACCEPT_APPLE_PAY: schema_object.COL_ACCEPTS_APPLE_PAY}, inplace=True)
    df[schema_object.COL_ACCEPTS_GOOGLE_PAY] = "Null"
    df.rename(columns={la_object.COL_GENDER_NEUTRAL_RESTROOMS: schema_object.COL_GENDER_NEUTRAL_RESTROOMS}, inplace=True)
    df.rename(columns={la_object.COl_GOOD_FOR: schema_object.COL_GOOD_FOR}, inplace=True)
    df.rename(columns={la_object.COL_GOOD_FOR_WORKING: schema_object.COL_GOOD_FOR_WORKING}, inplace=True)
    df[schema_object.COL_HAS_GLUTEN_FREE_OPTIONS] = "Null"
    df[schema_object.COL_HAS_POOL_TABLE] = "Null"
    df[schema_object.COL_LIKED_BY_VEGANS] = "Null"
    df[schema_object.COL_LIKED_BY_VEGETARIANS] = "Null"
    df[schema_object.COL_OFFERS_MILITARY_DISCOUNT] = "Null"
    df[schema_object.COL_WAITER_SERVICE] = "Null"

    df.drop([la_object.COL_ACTIVITY_DATE], axis=1, inplace=True)
    df.drop([la_object.COL_RECORD_ID], axis=1, inplace=True)
    df.drop([la_object.COL_ADDRESS], axis=1, inplace=True)
    df.drop([la_object.COL_PROGRAM_ELEMENT_CODE], axis=1, inplace=True)
    df.drop([la_object.COL_PROGRAM_ELEMENT_CODE_DESCRIPTION], axis=1, inplace=True)
    df.drop([la_object.COL_SERVICE_DESCRIPTION], axis=1, inplace=True)
    df.drop([la_object.COL_ROW_ID], axis=1, inplace=True)
    df.drop([la_object.COL_VIOLATION_CODE], axis=1, inplace=True)
    df.drop([la_object.COL_VIOLATION_CODE_DESCRIPTION], axis=1, inplace=True)
    df.drop([la_object.COl_POINTS], axis=1, inplace=True)
    df.drop([la_object.COl_COUNT], axis=1, inplace=True)
    df.drop([la_object.COl_PHONE], axis=1, inplace=True)
    df.drop([la_object.COl_PARKING], axis=1, inplace=True)

    return df


if __name__ == '__main__':

    input_la_dataset_file = '../../resources/dataset/LA_dataset_v1.csv'
    output_dataset_file = '../../resources/dataset/LA_dataset_v2.csv'
    input_df = pd.read_csv(input_la_dataset_file)

    # prepare features
    input_df = prepare_la_data_features(input_df)

    # fill empty values as Null
    input_df = input_df.replace(np.nan, 'Null')

    csvWriter(output_dataset_file, input_df)
