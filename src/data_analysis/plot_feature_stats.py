import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.data_schema.feature_names import FeatureNames
from src.data_preparation.input_data_schema import LasVegasGovtDataSchema


def plot_feature_stat(df, feature_xaxis, feature_yaxis, output_file):
    ##### construct list of mean, standard deviation, max values,###
    # min values, used for graph datapoints #####
    groups_df = df.groupby([feature_xaxis])
    # mean_df = df.groupby(feature_xaxis, as_index=False)[feature_yaxis].mean()
    mean_df = groups_df.mean()
    mean_list = mean_df[feature_yaxis]
    feature_list = df.groupby([feature_xaxis])[feature_xaxis]

    # sd_df = df.groupby(feature_xaxis, as_index=False)[feature_yaxis].std()
    sd_df = groups_df.std()
    # df.groupby([feature_xaxis]).std()
    sd_list = sd_df[feature_yaxis]

    # min_df = df.groupby(feature_xaxis, as_index=False)[feature_yaxis].min()
    min_df = groups_df.min()
    min_list = min_df[feature_yaxis]

    # max_df = df.groupby(feature_xaxis, as_index=False)[feature_yaxis].max()
    max_df = groups_df.max()
    max_list = max_df[feature_yaxis]

    #### plot the mean, standard deviation, max value, min value in graph #####
    plt.errorbar(np.arange(len(feature_list)), mean_list.values, sd_list.values, fmt='ok', ecolor='blue', lw=3)
    plt.errorbar(np.arange(len(feature_list)), mean_list.values,
                 [mean_list.values - min_list.values, max_list.values - mean_list.values],
                 fmt='.k', ecolor='gray', lw=1)

    #### Round off the score to two decimal places to be displayed in the graph #####
    for i in range(len(mean_list)):
        mean_list[i] = round(mean_list[i],2)
    for i in range(len(min_list)):
        min_list[i] = round(min_list[i],2)
    for i in range(len(max_list)):
        max_list[i] = round(max_list[i],2)

    #### annonate the values of datapoint labels in the graph ######
    for xy in zip(np.arange(len(feature_list)), mean_list.values):
        plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
    for xy in zip(np.arange(len(feature_list)), min_list.values):
        plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
    for xy in zip(np.arange(len(feature_list)), max_list.values):
        plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')

    #### display/save the label on x and y axis #####
    plt.xlabel(feature_xaxis)
    plt.ylabel(feature_yaxis)
    # plt.show()
    plt.savefig(output_file)


if __name__ == '__main__':
    file = '../../resources/dataset/final_lasvegas_dataset.csv'
    output_file = '../../resources/images/graphs/price.png'

    df = pd.read_csv(file)
    schema_obj = FeatureNames()
    df = df[[schema_obj.COL_RESTAURANTS_PRICE_RANGE2, schema_obj.COL_INSPECTION_SCORE]]
    plot_feature_stat(df, schema_obj.COL_RESTAURANTS_PRICE_RANGE2, schema_obj.COL_INSPECTION_SCORE, output_file)