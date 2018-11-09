import time
from collections import defaultdict
from INF553_YelpProject.src.utils.inputOutput_utils import csvReader, csvWriter
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def get_pearson_similarity(b1, b2):
    pass

def find_best_similarity_metrics(path):
    
    las_vegas_data = csvReader(path)
    schema = ['name','location_name','category_name','address','city','state','zip_code','violations','current_demerits','inspection_demerits','neighborhood','rating','review_count','accepts_insurance','ages_allowed','alcohol','ambience','byob','byob_corkage','best_nights','bike_parking','business_accepts_bitcoin','business_accepts_creditcards','business_parking','byappointmentonly','caters','coat_check','corkage','dietary_restrictions','dogs_allowed','drive_thru','good_for_dancing','good_for_kids','good_for_meal','hair_specializes_in','happy_hour','has_tv','music','noise_level','open_24_hours','outdoor_seating','restaurants_attire','restaurants_counter_service','restaurants_delivery','restaurants_good_for_groups','restaurants_price_range2','restaurants_reservations','restaurants_table_service','restaurants_takeout','smoking','wheelchair_accessible','wifi']
    
    business = defaultdict(list)
    for _, row in las_vegas_data.iterrows():
        pass
    
if __name__=='__main__':   
    
    start=time.time()
    path = "../../resources/dataset/"
    
    find_best_similarity_metrics(path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  