import time
from collections import defaultdict
from INF553_YelpProject.src.utils.inputOutput_utils import csvReader, csvWriter_from_text


def get_pearson_similarity(b1, b2, data):
    
    b1_data = data[b1]
    b2_data = data[b2]
     
    b1_avg = sum(b1_data)/len(b1_data)
    b2_avg = sum(b2_data)/len(b2_data)
    
    b1_new = [(x-b1_avg) for x in b1_data]
    b2_new = [(x-b2_avg) for x in b2_data]
    
    if len(b1_new)!=len(b2_new):
        return 0
    num = sum([b1_new[i]*b2_new[i] for i in range(len(b1_new))])
    denom1 = (sum([(x)**2 for x in b1_new]))**0.5
    denom2 = (sum([(x)**2 for x in b2_new]))**0.5
    
    denom =  denom1*denom2
    
    pearson_corr = 0 if denom == 0 else num/denom 
    
    return pearson_corr
    

def get_cosine_similarity(b1, b2, data):
    
    b1_data = data[b1]
    b2_data = data[b2]

    if len(b1_data)!=len(b2_data):
        return 0
    sum_x = 0
    sum_y = 0
    sum_xy = 0     
    for i in range(len(b1_data)):
        x = b1_data[i] 
        y = b2_data[i]
        sum_x += x*x
        sum_y += y*y
        sum_xy += x*y
    
    return sum_xy/((sum_x*sum_y)**0.5)



def find_best_similarity_metrics(path):
    
    las_vegas_data = csvReader(path + "final_lasvegas_dataset.csv")
    
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
    
    business_data = defaultdict(list)
    for _, row in las_vegas_data.iterrows():
        bid = row['business_id']
        
        if bid in business_data.keys():
            continue
        
        business_data_details = []
        for col in schema:
            business_data_details.append(row[col])
        business_data[bid] = business_data_details    
    
    similar_business_pearson = defaultdict(list)
    similar_business_cosine = defaultdict(list)
    
    count  = 0
    for curr_bid in business_data.keys():
        for new_bid in business_data.keys():
             
            if new_bid == curr_bid:
                continue
            sim_score_p = get_pearson_similarity(curr_bid, new_bid, business_data)              
            sim_score_c = get_cosine_similarity(curr_bid, new_bid, business_data)
            
#             print(sim_score_p, sim_score_c)
            
            if sim_score_p>=0.917 :   ##For Pearson Corr
                similar_business_pearson[curr_bid].append(new_bid)
                
            if sim_score_c>=0.962 :   ##For Cosine Sim
                similar_business_cosine[curr_bid].append(new_bid)


    csvWriter_from_text(similar_business_pearson, path+"similar_users_pearson.csv")
    csvWriter_from_text(similar_business_cosine, path+"similar_users_cosine.csv")
    
    
if __name__=='__main__':   
    
    start=time.time()
    path = "../../resources/dataset/"
    
    find_best_similarity_metrics(path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  