"""
Author: Ajay Anand
"""

import pandas as pd
import numpy as np
from src.data_schema.feature_names import FeatureNames
from src.utils.inputOutput_utils import csvWriter
from src.data_collection.yelp.yelp_feature_names import *


def rename_scraped_features(df):
    schema_obj = FeatureNames()
    df.rename(columns={YELP_COl_ALCOHOL: schema_obj.COL_ALCOHOL}, inplace=True)
    df.rename(columns={YELP_COl_AMBIENCE: schema_obj.COL_AMBIENCE}, inplace=True)
    df.rename(columns={YELP_COl_BEST_NIGHTS: schema_obj.COL_BEST_NIGHTS}, inplace=True)
    df.rename(columns={YELP_COl_BIKE_PARKING: schema_obj.COL_BIKE_PARKING}, inplace=True)
    df.rename(columns={YELP_COl_ACCEPTS_BITCOIN: schema_obj.COL_BUSINESS_ACCEPTS_BITCOIN}, inplace=True)
    df.rename(columns={YELP_COl_ACCEPTS_CREDIT_CARD: schema_obj.COL_BUSINESS_ACCEPTS_CREDITCARDS}, inplace=True)
    df.rename(columns={YELP_COl_PARKING: schema_obj.COL_BUSINESS_PARKING}, inplace=True)
    df.rename(columns={YELP_COl_BY_APPOINTMENT_ONLY: schema_obj.COL_BYAPPOINTMENTONLY}, inplace=True)
    df.rename(columns={YELP_COl_CATERS: schema_obj.COL_CATERS}, inplace=True)
    df.rename(columns={YELP_COL_COAT_CHECK: schema_obj.COL_COAT_CHECK}, inplace=True)
    df.rename(columns={YELP_COL_DOGS_ALLOWED: schema_obj.COL_DOGS_ALLOWED}, inplace=True)
    df.rename(columns={YELP_COL_DRIVE_THRU: schema_obj.COL_DRIVE_THRU}, inplace=True)
    df.rename(columns={YELP_COL_GOOD_FOR_DANCING: schema_obj.COL_GOOD_FOR_DANCING}, inplace=True)
    df.rename(columns={YELP_COl_GOOD_FOR_KIDS: schema_obj.COL_GOOD_FOR_KIDS}, inplace=True)
    df.rename(columns={YELP_COL_HAPPY_HOUR: schema_obj.COL_HAPPY_HOUR}, inplace=True)
    df.rename(columns={YELP_COl_HAS_TV: schema_obj.COL_HAS_TV}, inplace=True)
    df.rename(columns={YELP_COl_NOISE_LEVEL: schema_obj.COL_NOISE_LEVEL}, inplace=True)
    df.rename(columns={YELP_COl_OUTDOOR_SEATING: schema_obj.COL_OUTDOOR_SEATING}, inplace=True)
    df.rename(columns={YELP_COl_ATTIRE: schema_obj.COL_RESTAURANTS_ATTIRE}, inplace=True)
    df.rename(columns={YELP_COl_DELIVERY: schema_obj.COL_RESTAURANTS_DELIVERY}, inplace=True)
    df.rename(columns={YELP_COl_GOOD_FOR_GROUPS: schema_obj.COL_RESTAURANTS_GOOD_FOR_GROUPS}, inplace=True)
    df.rename(columns={YELP_COl_TAKES_RESERVATIONS: schema_obj.COL_RESTAURANTS_RESERVATIONS}, inplace=True)
    df.rename(columns={YELP_COl_TAKE_OUT: schema_obj.COL_RESTAURANTS_TAKEOUT}, inplace=True)
    df.rename(columns={YELP_COL_SMOKING: schema_obj.COL_SMOKING}, inplace=True)
    df.rename(columns={YELP_COL_WHEELCHAIR_ACCESSIBLE: schema_obj.CoL_WHEELCHAIR_ACCESSIBLE}, inplace=True)
    df.rename(columns={YELP_COl_WIFI: schema_obj.COL_WIFI}, inplace=True)


if __name__ == '__main__':
    dataset_file = '../../resources/dataset/final_lasvegas_dataset.csv'
    scraped_file = '../../resources/dataset/scraped_data.csv'
    output_nan_file = '../../resources/dataset/final_lasvegas_dataset_nan.csv'
    output_scraped_rename_file = '../../resources/dataset/scraped_data_renamed.csv'
    output_fill_data_file = '../../resources/dataset/final_lasvegas_dataset_filled_data.csv'

    dataset_df = pd.read_csv(dataset_file)
    scraped_df = pd.read_csv(scraped_file)

    # replace "Null" values with nan
    nan_df = dataset_df.replace('Null', np.nan)
    csvWriter(output_nan_file, nan_df)

    # rename columns of scraped data to match with dataset file
    rename_scraped_features(scraped_df)
    csvWriter(output_scraped_rename_file, scraped_df)

    # fill nan values in dataset with scraped values
    nan_dataset_df = pd.read_csv(output_nan_file)
    scraped_renamed_df = pd.read_csv(output_scraped_rename_file)
    scraped_renamed_df = scraped_renamed_df.replace('Null', np.nan)
    # nan_df[nan_df.isnull()] = d2
    filled_df = nan_dataset_df.fillna(scraped_renamed_df)
    csvWriter(output_fill_data_file, filled_df)