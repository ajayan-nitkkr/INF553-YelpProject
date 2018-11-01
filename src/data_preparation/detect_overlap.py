"""
Author: Ajay Anand
"""

import pandas as pd
from src.data_preparation.input_data_schema import LasVegasGovtDataSchema
from src.utils.inputOutput_utils import csvWriter


"""
find overlap dataset
"""
def find_overlap(df1, df2, overlap_conditions):
    s1 = pd.merge(df1, df2, how='inner', on=overlap_conditions)
    return s1


if __name__ == '__main__':
    lv_file = '../../resources/dataset/Restaurant_Inspections_LV_Final.csv'
    yelp_challenge_file = '../../resources/dataset/LasVegas_Restaurants_Rimsha_Preprocessed.csv'
    overlapped_file = '../../resources/dataset/Overlapped_Data.csv'

    lv_object = LasVegasGovtDataSchema()
    lv_df = pd.read_csv(lv_file)
    # df = lv_df.drop_duplicates(subset=[lv_object.COL_RESTAURANT_NAME,
    #                                                  lv_object.COL_LOCATION_NAME,
    #                                                  lv_object.COL_CATEGORY_NAME,
    #                                                  lv_object.COL_ADDRESS,
    #                                                  lv_object.COL_CITY,
    #                                                  lv_object.COL_STATE,
    #                                                  lv_object.COL_ZIP])
    # print(len(lv_df))

    yelp_df = pd.read_csv(yelp_challenge_file)

    overlap_conditions = [
        lv_object.COL_RESTAURANT_NAME,
        lv_object.COL_ZIP
    ]
    overlapped_df = find_overlap(lv_df, yelp_df, overlap_conditions)
    # print("overlapped_df:", len(overlapped_df))
    # print(overlapped_df.iloc[0])

    csvWriter(overlapped_file, overlapped_df)