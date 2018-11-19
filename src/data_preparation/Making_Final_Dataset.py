
# coding: utf-8

# <h2>Making Final Dataset

# <h4>Import Statements

# In[246]:


import pandas as pd
import json
import numpy as np
import ast
from tqdm import tqdm_notebook


# <h4>Reading data with strings into Pandas Dataframe df

# In[247]:


df=pd.read_csv('/home/rim/INF-Project/final_lasvegas_dataset_v2.csv')
df.shape


# In[248]:


df.columns.values


# In[249]:


new_df=df[['zip_code', 'violations', 'current_demerits', 'inspection_demerits','inspection_grade',
       'current_score', 'inspection_score', 'rating',
       'review_count', 'accepts_insurance', 'ages_allowed', 'alcohol',
       'ambience', 'byob', 'byob_corkage', 'best_nights', 'bike_parking',
       'business_accepts_bitcoin', 'business_accepts_creditcards',
       'business_parking', 'byappointmentonly', 'caters', 'coat_check',
       'corkage', 'dietary_restrictions', 'dogs_allowed', 'drive_thru',
       'good_for_dancing', 'good_for_kids', 'good_for_meal',
       'hair_specializes_in', 'happy_hour', 'has_tv', 'music',
       'noise_level', 'open_24_hours', 'outdoor_seating',
       'restaurants_attire', 'restaurants_counter_service',
       'restaurants_delivery', 'restaurants_good_for_groups',
       'restaurants_price_range2', 'restaurants_reservations',
       'restaurants_table_service', 'restaurants_takeout', 'smoking',
       'wheelchair_accessible', 'wifi', 'accepts_apple_pay',
       'accepts_google_pay', 'gender_neutral_restrooms', 'good_for',
       'good_for_working', 'has_gluten_free_options', 'has_pool_table',
       'liked_by_vegans', 'liked_by_vegetarians',
       'offers_military_discount', 'waiter_service']]


# In[250]:


COL_ACCEPTS_APPLE_PAY = "accepts_apple_pay"
COL_ACCEPTS_GOOGLE_PAY = "accepts_google_pay"
COL_GENDER_NEUTRAL_RESTROOMS = "gender_neutral_restrooms"
COL_GOOD_FOR = "good_for"
COL_GOOD_FOR_WORKING = "good_for_working"
COL_HAS_GLUTEN_FREE_OPTIONS = "has_gluten_free_options"
COL_HAS_POOL_TABLE = "has_pool_table"
COL_LIKED_BY_VEGANS = "liked_by_vegans"
COL_LIKED_BY_VEGETARIANS = "liked_by_vegetarians"
COL_OFFERS_MILITARY_DISCOUNT = "offers_military_discount"
COL_WAITER_SERVICE = "waiter_service"


# In[251]:


new_df.accepts_apple_pay.unique()
#Mapping : No=0, Yes=1
new_df.accepts_apple_pay.replace('No',0,inplace=True)
new_df.accepts_apple_pay.replace('Yes',1,inplace=True)
new_df.accepts_apple_pay.unique()


# In[252]:


new_df.accepts_google_pay.unique()
#Mapping : No=0, Yes=1
new_df.accepts_google_pay.replace('No',0,inplace=True)
new_df.accepts_google_pay.replace('Yes',1,inplace=True)
new_df.accepts_google_pay.unique()


# In[254]:


new_df.gender_neutral_restrooms.unique()
#Mapping : Yes=1
new_df.gender_neutral_restrooms.replace('Yes',1,inplace=True)
new_df.gender_neutral_restrooms.replace('-1',-1,inplace=True)
new_df.gender_neutral_restrooms.unique()


# In[255]:


unique_strings=new_df.good_for.unique()
unique_strings


# In[256]:


def change_good_for(String_value):
    final_val=0
    hmap={'Breakfast':1, 'Brunch':1, 'Lunch':1, 'Dinner':1, 'Dessert':1, 'Late Night':1}
    arr_values=String_value.split(',')
    for elem in arr_values:
        final_val+=hmap[elem.lstrip()]
    return final_val


# In[259]:


final_hmap={}
for each_string in unique_strings:
    if each_string!='-1':
        final_hmap[each_string]=change_good_for(each_string)
final_hmap


# In[260]:


for key in final_hmap:
    new_df.good_for.replace(key,final_hmap[key],inplace=True)


# In[261]:


new_df.good_for.unique()


# In[262]:


new_df.good_for_working.unique()
#Mapping : Yes=1
new_df.good_for_working.replace('Yes',1,inplace=True)
new_df.good_for_working.unique()


# In[263]:


new_df.has_gluten_free_options.unique()
#Mapping : Yes=1
new_df.has_gluten_free_options.replace('Yes',1,inplace=True)
new_df.has_gluten_free_options.unique()


# In[264]:


new_df.has_pool_table.unique()
#Mapping : Yes=1 No=0
new_df.has_pool_table.replace('Yes',1,inplace=True)
new_df.has_pool_table.replace('No',0,inplace=True)
new_df.has_pool_table.unique()


# In[265]:


new_df.liked_by_vegans.unique()
#Mapping : Yes=1
new_df.liked_by_vegans.replace('Yes',1,inplace=True)
new_df.liked_by_vegans.unique()


# In[266]:


new_df.liked_by_vegetarians.unique()
#Mapping : Yes=1
new_df.liked_by_vegetarians.replace('Yes',1,inplace=True)
new_df.liked_by_vegetarians.unique()


# In[267]:


new_df.offers_military_discount.unique()#Mapping : Yes=1
new_df.offers_military_discount.replace('Yes',1,inplace=True)
new_df.offers_military_discount.unique()


# In[268]:


new_df.waiter_service.unique()
#Mapping : Yes=1 No=0
new_df.waiter_service.replace('Yes',1,inplace=True)
new_df.waiter_service.replace('No',0,inplace=True)
new_df.waiter_service.unique()


# In[270]:


new_df.replace('Null',-1,inplace=True)
new_df.replace('-1',-1,inplace=True)


# In[271]:


new_df.alcohol.unique()
#Mapping : none->0, beer_and_wine->1,full_bar->2
new_df.alcohol.replace('No',0,inplace=True)
new_df.alcohol.replace('Beer & Wine Only',1,inplace=True)
new_df.alcohol.replace('Full Bar',2,inplace=True)
new_df.alcohol.replace('0',0,inplace=True)
new_df.alcohol.replace('1',1,inplace=True)
new_df.alcohol.replace('2',2,inplace=True)
new_df.alcohol.unique()


# In[272]:


new_df.ambience.unique()
new_df.ambience.replace('0',0,inplace=True)
new_df.ambience.replace('1',1,inplace=True)
new_df.ambience.replace('2',2,inplace=True)
new_df.ambience.replace('3',3,inplace=True)
new_df.ambience.replace('Null',-1,inplace=True)
new_df.ambience.unique()


# In[273]:


new_df.ambience.replace('Casual',1,inplace=True)
new_df.ambience.replace('Casual, Trendy, Classy',3,inplace=True)
new_df.ambience.replace('Divey, Casual',2,inplace=True)
new_df.ambience.replace('Romantic',1,inplace=True)
new_df.ambience.replace('Romantic, Classy',2,inplace=True)
new_df.ambience.unique()


# In[274]:


new_df.best_nights.unique()
new_df.best_nights.replace('Null',-1,inplace=True)
new_df.best_nights.replace('0',0,inplace=True)
new_df.best_nights.replace('1',1,inplace=True)
new_df.best_nights.replace('2',2,inplace=True)
new_df.best_nights.replace('3',3,inplace=True)
new_df.best_nights.replace('Sun',1,inplace=True)
new_df.best_nights.replace('Thu, Fri, Sat',3,inplace=True)
new_df.best_nights.replace('Fri, Sat, Sun',3,inplace=True)
new_df.best_nights.replace('Mon, Fri, Sat',3,inplace=True)
new_df.best_nights.replace('Mon, Thu, Sun',3,inplace=True)
new_df.best_nights.unique()


# In[275]:


new_df.bike_parking.unique()
new_df.bike_parking.replace('Null',-1,inplace=True)
new_df.bike_parking.replace('1',1,inplace=True)
new_df.bike_parking.replace('0',0,inplace=True)
new_df.bike_parking.replace('Yes',1,inplace=True)
new_df.bike_parking.replace('No',0,inplace=True)
new_df.bike_parking.unique()


# In[276]:


new_df.business_accepts_bitcoin.unique()
new_df.business_accepts_bitcoin.replace('Null',-1,inplace=True)
new_df.business_accepts_bitcoin.replace('0',0,inplace=True)
new_df.business_accepts_bitcoin.replace('1',1,inplace=True)
new_df.business_accepts_bitcoin.replace('No',0,inplace=True)
new_df.business_accepts_bitcoin.replace('Yes',1,inplace=True)
new_df.business_accepts_bitcoin.unique()


# In[277]:


new_df.business_accepts_creditcards.unique()
new_df.business_accepts_creditcards.replace('1',1,inplace=True)
new_df.business_accepts_creditcards.replace('0',0,inplace=True)
new_df.business_accepts_creditcards.replace('Null',-1,inplace=True)
new_df.business_accepts_creditcards.replace('Yes',1,inplace=True)
new_df.business_accepts_creditcards.unique()


# In[278]:


new_df.business_parking.unique()
new_df.business_parking.replace('0',0,inplace=True)
new_df.business_parking.replace('1',1,inplace=True)
new_df.business_parking.replace('2',2,inplace=True)
new_df.business_parking.replace('3',3,inplace=True)
new_df.business_parking.replace('4',4,inplace=True)
new_df.business_parking.replace('5',5,inplace=True)
new_df.business_parking.replace('Null',-1,inplace=True)
new_df.business_parking.replace('Private Lot',1,inplace=True)
new_df.business_parking.replace('Valet, Street, Private Lot',3,inplace=True)
new_df.business_parking.unique()


# In[279]:


new_df.byappointmentonly.unique()
new_df.byappointmentonly.replace('Null',-1,inplace=True)
new_df.byappointmentonly.replace('0',0,inplace=True)
new_df.byappointmentonly.replace('No',0,inplace=True)
new_df.byappointmentonly.unique()


# In[280]:


new_df.replace('Null',-1,inplace=True)


# In[281]:


new_df.caters.unique()
new_df.caters.replace('1',1,inplace=True)
new_df.caters.replace('0',0,inplace=True)
new_df.caters.replace('Yes',1,inplace=True)
new_df.caters.replace('No',0,inplace=True)
new_df.caters.unique()


# In[282]:


new_df.coat_check.unique()
new_df.coat_check.replace('0',0,inplace=True)
new_df.coat_check.replace('1',1,inplace=True)
new_df.coat_check.replace('No',0,inplace=True)
new_df.coat_check.unique()


# In[283]:


new_df.dogs_allowed.unique()
new_df.dogs_allowed.replace('0',0,inplace=True)
new_df.dogs_allowed.replace('1',1,inplace=True)
new_df.dogs_allowed.replace('Yes',1,inplace=True)
new_df.dogs_allowed.replace('No',0,inplace=True)
new_df.dogs_allowed.unique()


# In[284]:


new_df.drive_thru.unique()
new_df.drive_thru.replace('0',0,inplace=True)
new_df.drive_thru.replace('1',1,inplace=True)
new_df.drive_thru.replace('No',0,inplace=True)
new_df.drive_thru.replace('Yes',1,inplace=True)
new_df.drive_thru.unique()


# In[285]:


new_df.good_for_dancing.unique()
new_df.good_for_dancing.replace('0',0,inplace=True)
new_df.good_for_dancing.replace('1',1,inplace=True)
new_df.good_for_dancing.replace('No',0,inplace=True)
new_df.good_for_dancing.replace('Yes',1,inplace=True)
new_df.good_for_dancing.unique()


# In[286]:


new_df.good_for_kids.unique()
new_df.good_for_kids.replace('0',0,inplace=True)
new_df.good_for_kids.replace('1',1,inplace=True)
new_df.good_for_kids.replace('No',0,inplace=True)
new_df.good_for_kids.replace('Yes',1,inplace=True)
new_df.good_for_kids.unique()


# In[287]:


new_df.good_for_working.unique()
new_df.good_for_working.replace('Yes',1,inplace=True)
new_df.good_for_working.unique()


# In[288]:


new_df.happy_hour.unique()

new_df.happy_hour.replace('0',0,inplace=True)
new_df.happy_hour.replace('1',1,inplace=True)
new_df.happy_hour.replace('No',0,inplace=True)
new_df.happy_hour.replace('Yes',1,inplace=True)
new_df.happy_hour.unique()


# In[289]:


new_df.has_tv.unique()
new_df.has_tv.replace('0',0,inplace=True)
new_df.has_tv.replace('1',1,inplace=True)
new_df.has_tv.replace('No',0,inplace=True)
new_df.has_tv.replace('Yes',1,inplace=True)
new_df.has_tv.unique()


# In[290]:


new_df.noise_level.unique()
#Mapping : quiet=0,average=1, loud=2, very_loud=3
new_df.noise_level.replace('Quiet',0,inplace=True)
new_df.noise_level.replace('Average',1,inplace=True)
new_df.noise_level.replace('Loud',2,inplace=True)
new_df.noise_level.replace('Very Loud',3,inplace=True)
new_df.noise_level.replace('0',0,inplace=True)
new_df.noise_level.replace('1',1,inplace=True)
new_df.noise_level.replace('2',2,inplace=True)
new_df.noise_level.replace('3',3,inplace=True)
new_df.noise_level.unique()


# In[291]:


new_df.outdoor_seating.unique()
new_df.outdoor_seating.replace('0',0,inplace=True)
new_df.outdoor_seating.replace('1',1,inplace=True)
new_df.outdoor_seating.replace('No',0,inplace=True)
new_df.outdoor_seating.replace('Yes',1,inplace=True)
new_df.outdoor_seating.unique()


# In[292]:


new_df.restaurants_good_for_groups.unique()
new_df.restaurants_good_for_groups.replace('0',0,inplace=True)
new_df.restaurants_good_for_groups.replace('1',1,inplace=True)
new_df.restaurants_good_for_groups.replace('No',0,inplace=True)
new_df.restaurants_good_for_groups.replace('Yes',1,inplace=True)
new_df.restaurants_good_for_groups.unique()


# In[293]:


new_df.restaurants_delivery.unique()
new_df.restaurants_delivery.replace('0',0,inplace=True)
new_df.restaurants_delivery.replace('1',1,inplace=True)
new_df.restaurants_delivery.replace('No',0,inplace=True)
new_df.restaurants_delivery.replace('Yes',1,inplace=True)
new_df.restaurants_delivery.unique()


# In[294]:


new_df.restaurants_attire.unique()
#Mapping : casual=0, dressy=1, formal=2
new_df.restaurants_attire.replace('Casual',0,inplace=True)
new_df.restaurants_attire.replace('0',0,inplace=True)
new_df.restaurants_attire.replace('1',1,inplace=True)
new_df.restaurants_attire.unique()


# In[295]:


new_df.restaurants_reservations.unique()
new_df.restaurants_reservations.replace('0',0,inplace=True)
new_df.restaurants_reservations.replace('1',1,inplace=True)
new_df.restaurants_reservations.replace('No',0,inplace=True)
new_df.restaurants_reservations.replace('Yes',1,inplace=True)
new_df.restaurants_reservations.unique()


# In[296]:


new_df.restaurants_takeout.unique()
new_df.restaurants_takeout.replace('0',0,inplace=True)
new_df.restaurants_takeout.replace('1',1,inplace=True)
new_df.restaurants_takeout.replace('No',0,inplace=True)
new_df.restaurants_takeout.replace('Yes',1,inplace=True)
new_df.restaurants_takeout.unique()


# In[297]:


new_df.smoking.unique()
#Mapping : no=0, yes=1, outdoor=2
new_df.smoking.replace('Yes',1,inplace=True)
new_df.smoking.replace('0',0,inplace=True)
new_df.smoking.replace('1',1,inplace=True)
new_df.smoking.replace('2',2,inplace=True)
new_df.smoking.unique()


# In[298]:


new_df.wheelchair_accessible.unique()
new_df.wheelchair_accessible.replace('0',0,inplace=True)
new_df.wheelchair_accessible.replace('1',1,inplace=True)
new_df.wheelchair_accessible.replace('No',0,inplace=True)
new_df.wheelchair_accessible.replace('Yes',1,inplace=True)
new_df.wheelchair_accessible.unique()


# In[299]:


new_df.wifi.unique()
#Mapping : no=0,free=1, paid=2
new_df.wifi.replace('No',0,inplace=True)
new_df.wifi.replace('Free',1,inplace=True)
new_df.wifi.replace('0',0,inplace=True)
new_df.wifi.replace('1',1,inplace=True)
new_df.wifi.unique()


# In[300]:


new_df.to_csv('final_lasvegas_dataset_v3.csv',',',index=False)

