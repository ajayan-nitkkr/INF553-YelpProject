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

def fill_missing_data(path):
    
    las_vegas_data = csvReader(path + "final_lasvegas_dataset.csv")
    business_with_missing_data = readText(path+"similar_users_pearson.csv")
    
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
    
    schema = ['violations', 'current_demerits', 'inspection_demerits', 
              'current_score', 'inspection_score', 'rating', 'review_count']

    
    

if __name__=='__main__':   
    
    start=time.time()
    path = "../../resources/dataset/"
    
    fill_missing_data(path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  