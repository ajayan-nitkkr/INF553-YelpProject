
import pandas as pd
import json
import numpy as np
import ast
from tqdm import tqdm_notebook


#Reading lasVegas.csv into Pandas Dataframe df

df=pd.DataFrame.from_csv('/home/rim/INF-Project/preprocessed_lasVegas.csv')
df.shape

#Select required columns and rename columns to standard names

df=df[['business_id','name','neighborhood','address','city','state','postal_code','stars','review_count','attributes']]
df.columns=['BusinessId',"RestaurantName",'Neighborhood',"Address",'City','State','Zip','Stars','ReviewCount','attributes']
df.columns.values


#Divide df into 2 parts - attributes and the rest


df_1=df[['BusinessId',"RestaurantName",'Neighborhood',"Address",'City','State','Zip','Stars','ReviewCount']]
df_2=df[['attributes']]


# Replace blank with ''


df_1.fillna('', inplace=True)
df_1


# Replace None or NA attributes with {}


df_2.replace('None','{}', inplace=True)
df_2.fillna('{}', inplace=True)
df_2


# Making a new dataframe out of attributes dictionary


cols=['BikeParking','BusinessAcceptsCreditCards','BusinessParking','GoodForKids','HasTV','NoiseLevel','OutdoorSeating','RestaurantsAttire','RestaurantsDelivery','RestaurantsGoodForGroups','RestaurantsPriceRange2','RestaurantsReservations','RestaurantsTakeOut']

df_3=pd.DataFrame(columns=cols)

for index, row in tqdm_notebook(df_2.iterrows()):
    string=ast.literal_eval(row.attributes)
    df_4=pd.DataFrame.from_dict([string])
    df_3=pd.concat([df_3,df_4], axis=0)
df_3


#  Concatenate New Attributes Columns and older remaining columns

df_1.reset_index(drop=True, inplace=True)
df_3.reset_index(drop=True, inplace=True)
dat1 = pd.concat([df_1, df_3], axis=1)
df_1.shape,df_3.shape,dat1.shape
dat1


#  Mapping Values

# All True=1, False=0

dat1.replace('True',1,inplace=True)
dat1.replace('False',0,inplace=True)
dat1


dat1.columns.values

dat1.HasTV.unique()
dat1.WheelchairAccessible.unique()
dat1.HappyHour.unique()
dat1.GoodForDancing.unique()
dat1.DriveThru.unique()
dat1.DogsAllowed.unique()
dat1.Corkage.unique()
dat1.RestaurantsReservations.unique()
dat1.RestaurantsTableService.unique()
dat1.RestaurantsTakeOut.unique()
dat1.RestaurantsCounterService.unique()
dat1.RestaurantsDelivery.unique()
dat1.RestaurantsGoodForGroups.unique()
dat1.CoatCheck.unique()
dat1.Caters.unique()
dat1.ByAppointmentOnly.unique()
dat1.BusinessAcceptsCreditCards.unique()
dat1.BusinessAcceptsBitcoin.unique()
dat1.BikeParking.unique()
dat1.BYOB.unique()
dat1.GoodForKids.unique()
dat1.Open24Hours.unique()
dat1.OutdoorSeating.unique()
dat1.AcceptsInsurance.unique()


dat1.WiFi.unique()
#Mapping : no=0,free=1, paid=2
dat1.WiFi.replace('no',0,inplace=True)
dat1.WiFi.replace('free',1,inplace=True)
dat1.WiFi.replace('paid',2,inplace=True)
dat1.WiFi.unique()



dat1.Smoking.unique()
#Mapping : no=0, yes=1, outdoor=2
dat1.Smoking.replace('no',0,inplace=True)
dat1.Smoking.replace('yes',1,inplace=True)
dat1.Smoking.replace('outdoor',2,inplace=True)
dat1.Smoking.unique()



#Dont Know what they represent
dat1.RestaurantsPriceRange2.unique()


dat1.RestaurantsAttire.unique()
#Mapping : casual=0, dressy=1, formal=2
dat1.RestaurantsAttire.replace('casual',0,inplace=True)
dat1.RestaurantsAttire.replace('dressy',1,inplace=True)
dat1.RestaurantsAttire.replace('formal',2,inplace=True)
dat1.RestaurantsAttire.unique()


dat1.NoiseLevel.unique()
#Mapping : quiet=0,average=1, loud=2, very_loud=3
dat1.NoiseLevel.replace('quiet',0,inplace=True)
dat1.NoiseLevel.replace('average',1,inplace=True)
dat1.NoiseLevel.replace('loud',2,inplace=True)
dat1.NoiseLevel.replace('very_loud',3,inplace=True)
dat1.NoiseLevel.unique()



dat1.BYOBCorkage.unique()
#Mapping : no->0, yes_free->1, yes_corkage->2
dat1.BYOBCorkage.replace('no',0,inplace=True)
dat1.BYOBCorkage.replace('yes_free',1,inplace=True)
dat1.BYOBCorkage.replace('yes_corkage',2,inplace=True)
dat1.BYOBCorkage.unique()



#Range of Ages Allowed
dat1.AgesAllowed.unique()
#Mapping : allages->0,18plus->1,21plus->2
dat1.AgesAllowed.replace('allages',0,inplace=True)
dat1.AgesAllowed.replace('18plus',1,inplace=True)
dat1.AgesAllowed.replace('21plus',2,inplace=True)
dat1.AgesAllowed.unique()


#Range of Alcohol
dat1.Alcohol.unique()
#Mapping : none->0, beer_and_wine->1,full_bar->2
dat1.Alcohol.replace('none',0,inplace=True)
dat1.Alcohol.replace('beer_and_wine',1,inplace=True)
dat1.Alcohol.replace('full_bar',2,inplace=True)
dat1.Alcohol.unique()


#Mapping - count number of True Values - number of best nights in a week
for row in tqdm_notebook(dat1.BestNights):
    if type(row)==type(''):
        dat1.BestNights.replace(row,row.count('True'),inplace=True)   
dat1.BestNights.unique()


#Mapping - count number of True Values - number of types of ambiences it offers
for row in tqdm_notebook(dat1.Ambience):
    if type(row)==type(''):
        dat1.Ambience.replace(row,row.count('True'),inplace=True)   
dat1.Ambience.unique()



#Mapping - count number of True Values - number of types of parkings available
#eg- {'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False} has 1 type of parking
# and "{'garage': True, 'street': True, 'validated': False, 'lot': False, 'valet': True}" has 3
for row in tqdm_notebook(dat1.BusinessParking):
    if type(row)==type(''):
        dat1.BusinessParking.replace(row,row.count('True'),inplace=True)   
dat1.BusinessParking.unique()


for row in tqdm_notebook(dat1.GoodForMeal):
    if type(row)==type(''):
        dat1.GoodForMeal.replace(row,row.count('True'),inplace=True)   
dat1.GoodForMeal.unique()


for row in tqdm_notebook(dat1.HairSpecializesIn):
    if type(row)==type(''):
        dat1.HairSpecializesIn.replace(row,row.count('True'),inplace=True)   
dat1.HairSpecializesIn.unique()



for row in tqdm_notebook(dat1.Music):
    if type(row)==type(''):
        dat1.Music.replace(row,row.count('True'),inplace=True)   
dat1.Music.unique()



#dat1.DietaryRestrictions.unique()
#7 types/combos of dietry restrictions. These are as follows -
dat1.DietaryRestrictions.replace("{'dairy-free': True, 'gluten-free': False, 'vegan': True, 'kosher': False, 'halal': False, 'soy-free': False, 'vegetarian': True}",0,inplace=True)
dat1.DietaryRestrictions.replace("{'dairy-free': False, 'gluten-free': False, 'vegan': False, 'kosher': False, 'halal': False, 'soy-free': False, 'vegetarian': True}",1,inplace=True)
dat1.DietaryRestrictions.replace("{'dairy-free': True, 'gluten-free': False, 'vegan': True, 'kosher': False, 'halal': False, 'soy-free': True, 'vegetarian': True}",2,inplace=True)
dat1.DietaryRestrictions.replace("{'dairy-free': False, 'gluten-free': False, 'vegan': True, 'kosher': False, 'halal': False, 'soy-free': False, 'vegetarian': True}",3,inplace=True)
dat1.DietaryRestrictions.replace("{'dairy-free': False, 'gluten-free': False, 'vegan': True, 'kosher': False, 'halal': False, 'soy-free': False, 'vegetarian': False}",4,inplace=True)
dat1.DietaryRestrictions.replace("{'dairy-free': True, 'gluten-free': False, 'vegan': False, 'kosher': False, 'halal': False, 'soy-free': False, 'vegetarian': True}",5,inplace=True)
dat1.DietaryRestrictions.replace("{'dairy-free': False, 'gluten-free': True, 'vegan': False, 'kosher': False, 'halal': False, 'soy-free': False, 'vegetarian': False}",6,inplace=True)
dat1.DietaryRestrictions.unique()



dat1.fillna('Null', inplace=True)



dat1.to_csv('LasVegas_Restaurants_Temp.csv',',',index=False)

