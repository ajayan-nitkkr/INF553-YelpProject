import pandas as pd
df_v2=pd.read_csv('/home/rim/INF553-YelpProject/resources/dataset/final_lasvegas_dataset_v2.csv')
df_v3=pd.read_csv('/home/rim/INF553-YelpProject/resources/dataset/final_lasvegas_dataset_v3.csv')
df_v4=pd.read_csv('/home/rim/INF553-YelpProject/resources/dataset/final_lasvegas_dataset_v4.csv')
print(df_v2.shape,df_v3.shape,df_v4.shape)
business_id=df_v2[['business_id']]
business_id.reset_index(drop=True, inplace=True)
df_v3.reset_index(drop=True, inplace=True)
v3_with_bid = pd.concat([business_id, df_v3], axis=1)
v3_with_bid.to_csv('v3_with_business_id.csv',',',index=False)
business_id.reset_index(drop=True, inplace=True)
df_v4.reset_index(drop=True, inplace=True)
v4_with_bid = pd.concat([business_id, df_v4], axis=1)
v4_with_bid.shape
v4_with_bid.to_csv('v4_with_business_id.csv',',',index=False)
