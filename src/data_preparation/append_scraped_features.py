"""
Author: Ajay Anand
"""

import pandas as pd
import numpy as np
from src.data_schema.feature_names import FeatureNames
from src.data_preparation.detect_overlap import find_overlap
from src.utils.inputOutput_utils import csvWriter


if __name__ == '__main__':
    # cur_final_dataset = '../../resources/dataset/final_lasvegas_dataset.csv'
    cur_final_dataset = '../../resources/dataset/final_lasvegas_dataset_filled_data.csv'
    scraped_new_features = '../../resources/dataset/scraped_data_shortened.csv'
    # new_final_dataset = '../../resources/dataset/merged_lasvegas_dataset.csv'
    new_final_dataset = '../../resources/dataset/final_lasvegas_dataset_v2.csv'

    schema_object = FeatureNames()
    cur_final_dataset_df = pd.read_csv(cur_final_dataset)
    # print(len(cur_final_dataset_df))
    cur_final_dataset_df = cur_final_dataset_df.drop_duplicates(subset=[schema_object.COL_BUSINESS_ID])
    # print(len(cur_final_dataset_df))
    scraped_new_features_df = pd.read_csv(scraped_new_features)
    # print(len(scraped_new_features_df))
    scraped_new_features_df = scraped_new_features_df.drop_duplicates(subset=[schema_object.COL_BUSINESS_ID])
    # print(len(scraped_new_features_df))
    # schema_object = FeatureNames()
    overlap_conditions = [
        schema_object.COL_BUSINESS_ID
    ]
    overlapped_df = find_overlap(cur_final_dataset_df, scraped_new_features_df, overlap_conditions)
    overlapped_df = overlapped_df.replace(np.nan, 'Null')
    csvWriter(new_final_dataset, overlapped_df)