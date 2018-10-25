"""
Author: Ajay Anand
"""

import pandas as pd
import json

from src.data_preparation.input_data_schema import LasVegasGovtDataSchema
# from src.utils.inputOutput_utils import

"""
load the government data from csv file into dataframe
"""
def load_lv_govt_data(file):
    df = pd.read_csv(file)
    # print(len(df))
    # df = df.loc[df['City'] == 'LOS ANGELES']
    # df = df.rename(columns={'Zip': 'zip'})
    # df = df.rename(columns={'Facility': 'name'})
    # df = df['name'].str.lower().to_frame()
    # print("Las Angeles Health Data: "+str(len(df)))
#     print(len(df))
    return df

"""
load the yelp challenge data from json file into dataframe
"""
def load_yelp_challenge_data(file):
    with open(file,'rb') as f:
        data = pd.DataFrame(json.loads(line) for line in f)
    print("Yelp Data: "+str(len(data)))
    data = data['name'].str.lower().to_frame()
    data = data.rename(columns={'postal_code': 'zip'})
    # df = data.loc[data['City'] == 'Calgary']
    return data

"""
find overlap dataset
"""
def find_overlap(df1, df2, overlap_conditions):
    print("finding overlap...")
    # https: // stackoverflow.com / questions / 26921943 / pandas - intersection - of - two - data - frames - based - on - column - entries / 26921975
    # s1 = pd.merge(la_govt_df, yelp_df, how='inner', on=['name'])
    s1 = pd.merge(df1, df2, how='inner', on=overlap_conditions)
    # print(len(s1))
    return s1


if __name__ == '__main__':
    # lv_govt_data_path1 = '../../../../data/LA_govt_2016-18_dataset.csv'
    lv_current_grade_file = '../../resources/dataset/Restaurant_Inspections_CurrentGrade.csv'
    lv_inspection_grade_file = '../../resources/dataset/Restaurant_Inspections_InspectionGrade.csv'
    lv_violation_file = '../../resources/dataset/Restaurant_Inspections_Violation_Demerits.csv'
    yelp_challenge_data_path = '../../../../data/yelp_dataset/yelp_dataset~/yelp_academic_dataset_business.json'

    # merge multiple files of government data into single dataframe
    lv_object = LasVegasGovtDataSchema()
    lv_current_grade_df = load_lv_govt_data(lv_current_grade_file)
    print("lv_govt_df1:",len(lv_current_grade_df), len(lv_current_grade_df[lv_object.COL_RESTAURANT_NAME].unique()))
    lv_inspection_grade_df = load_lv_govt_data(lv_inspection_grade_file)
    print("lv_govt_df2:", len(lv_inspection_grade_df), len(lv_inspection_grade_df[lv_object.COL_RESTAURANT_NAME].unique()))
    overlap_conditions = lv_object.COL_RESTAURANT_NAME
    df = find_overlap(lv_current_grade_df, lv_inspection_grade_df, overlap_conditions)
    print("df:",len(df))
    print (len(df[lv_object.COL_RESTAURANT_NAME].unique()))
    lv_violation_df = load_lv_govt_data(lv_violation_file)
    print("lv_govt_df2:", len(lv_violation_df), len(lv_violation_df[lv_object.COL_RESTAURANT_NAME].unique()))
    overlap_conditions = lv_object.COL_RESTAURANT_NAME
    df = find_overlap(df, lv_violation_df, overlap_conditions)
    print("df:", len(df))


    # yelp_df = load_yelp_challenge_data(yelp_challenge_data_path)
    # find_overlap(lv_govt_df1, yelp_df)