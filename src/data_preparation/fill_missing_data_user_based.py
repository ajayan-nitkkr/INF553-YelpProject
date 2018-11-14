import time
from collections import defaultdict
from INF553_YelpProject.src.utils.inputOutput_utils import csvReader, csvWriter_from_text

def readText(path):
    
    fin = open(path, "r", encoding = "utf-8")
    business = dict()
    for line in fin:
        line = line.split(",")
        business[line[0]]=line[1:]
    
    return business

def get_schema(path): 
    fin = open(path , "r", encoding = "utf-8")
    business_missing_cols = dict()
    for line in fin:
        line = line.split(",")
        business_missing_cols[line[0]]=line[1:]
    
    return business_missing_cols

def fill_missing_data(path):
    
    las_vegas_data = csvReader(path + "final_lasvegas_dataset.csv")
    business_with_missing_data = readText(path+"similar_users_pearson.csv")
    business_missing_cols = get_schema(path + "business_with_partial_data_lasVegas.csv")
    
    #     schema = ['category_name', 'violations', 'current_demerits', 'inspection_demerits', 
#               'current_score', 'inspection_score', 'current_grade', 'inspection_grade', 
#               'rating', 'review_count', 'accepts_insurance', 'alcohol', 'ambience', 'byob', 
#               'byob_corkage', 'best_nights', 'bike_parking', 'business_accepts_bitcoin', 
#               'business_accepts_creditcards', 'business_parking', 'byappointmentonly', 
#               'caters', 'coat_check', 'corkage', 'dietary_restrictions', 'dogs_allowed', 
#               'drive_thru', 'good_for_dancing', 'good_for_kids', 'good_for_meal', 
#                'happy_hour', 'has_tv', 'music', 'open_24_hours', 'outdoor_seating', 'restaurants_attire', 
#                'restaurants_counter_service', 'restaurants_delivery', 'restaurants_good_for_groups', 
#                'restaurants_price_range2', 'restaurants_reservations', 'restaurants_table_service', 
#                'restaurants_takeout', 'smoking', 'wheelchair_accessible', 'wifi']
    
#     schema = ['violations', 'current_demerits', 'inspection_demerits', 
#               'current_score', 'inspection_score', 'rating', 'review_count']
    
#     total_data_len = len(business_with_missing_data)
    count = 0
    for _, row in las_vegas_data.iterrows():
        bid = row['business_id']   
        
        if bid in business_with_missing_data.keys():
#             print(count, bid)
            similar_users = business_with_missing_data[bid]
            sim_user_count = len(similar_users)
            
            schema = [x.strip() for x in business_missing_cols[bid]]
            schema = ['accepts_insurance']
            
            for col in schema:
                
                if row[col]!="Null":
                    continue
                empty = 0
                for user in similar_users:
                    sim_data = las_vegas_data.loc[las_vegas_data['business_id'] == user]
                    
                        
                    if ((sim_data[col]!="Null")):
                        pass
                    else:
                        empty+=1
                        
                if empty ==  sim_user_count:
                    print("---------------------------------here")
                    print(col)
                    continue
        
        
        count+=1        
        break    
            

    
    

if __name__=='__main__':   
    
    start=time.time()
    path = "../../resources/dataset/"
    
    fill_missing_data(path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  