"""
Author: Ajay Anand
"""

import pandas as pd

from src.data_preparation.input_data_schema import LasVegasGovtDataSchema
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
    df.rename(columns={lv_object.COL_CURRENT_GRADE: schema_object.COL_CURRENT_GRADE}, inplace=True)
    # df.rename(columns={lv_object.COL_INSPECTION_GRADE: schema_object.COL_INSPECTION_GRADE}, inplace=True)
    # df.rename(columns={lv_object.COL_VIOLATIONS: schema_object.COL_VIOLATIONS}, inplace=True)
    # df.rename(columns={lv_object.COL_CURRENT_DEMERITS: schema_object.COL_CURRENT_DEMERITS}, inplace=True)
    # df.rename(columns={lv_object.COL_INSPECTION_DEMERITS: schema_object.COL_INSPECTION_DEMERITS}, inplace=True)
    return df


if __name__ == '__main__':
    govt_input_file = '../../resources/dataset/Restaurant_Inspections_CurrentGrade.csv'
    govt_output_file = '../../resources/dataset/Restaurant_Inspections_CurrentGrade_new.csv'
    govt_df = pd.read_csv(govt_input_file)
    govt_df = rename_govt_data_features(govt_df)
    csvWriter(govt_output_file, govt_df)