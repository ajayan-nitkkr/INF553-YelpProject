import time
from collections import defaultdict
import pandas as pd
import numpy as np
from INF553_YelpProject.src.utils.inputOutput_utils import csvReader, csvWriter

def find_business_with_missing_data(data):
    
    data_schema = ['name', "neighborhood", 'address', 'city', 'state', 'postal_code', 'review_count',
                   'latitude', "longitude", "stars", "is_open", "attributes", "categories", "hours" ]
    
    attribute_schema = ["BikeParking", "BusinessAcceptsCreditCards", "BusinessParking", "GoodForKids",
                        "HasTV", "NoiseLevel", "OutdoorSeating", "RestaurantsAttire", "RestaurantsDelivery",
                        "RestaurantsGoodForGroups", "RestaurantsPriceRange2", "RestaurantsReservations", "RestaurantsTakeOut"]
    
    business_parking_schema = ['garage', "street", "validated", "lot", "valet"]
    
    missing_data = data
    for col in data_schema:
        missing_data[col]=data[col].isnull()
       
    return missing_data


def missing_data_details(data):
    
    data_schema = ['name', "neighborhood", 'address', 'city', 'state', 'postal_code', 'review_count',
                   'latitude', "longitude", "stars", "is_open", "attributes", "categories", "hours" ]
    
    full_data_bIds = []
    partial_data_bIds = defaultdict(list)
    
    for _,row in data.iterrows():
        full = True
        b_id = row['business_id']
        for col in data_schema:
            if row[col]==True:
                partial_data_bIds[b_id].append(col)
                full = False
        if  full:
            full_data_bIds.append(b_id)

    return full_data_bIds, partial_data_bIds

def print_full_data_details(data, path):
    fout =  open(path+"business_with_full_data_All_Yelp_Data.txt", "w+", encoding = "utf-8")
    
    for b_id in data:
        fout.write(str(b_id) + "\n")
    
    fout.close()
    return

def print_partial_data_details(data, path):
    fout =  open(path+"business_with_partial_data_All_Yelp_Data.csv", "w+", encoding = "utf-8")
    
    for key in data.keys():
        fout.write(str(key))
        for col in data[key]: 
            fout.write("," + str(col))
        
        fout.write("\n")
        
    fout.close()
    return
    
def find_missing_data(path):
#     yelp_data = csvReader(path+"preprocessed_lasVegas.csv")
    yelp_data = csvReader(path+"valid_business_yelp_data.csv")    
    business_with_missing_data = find_business_with_missing_data(yelp_data)
#     csvWriter(path+"missing_data_yelp_business_All_Yelp_Data.csv", business_with_missing_data)
    
    full_data_bIds, partial_data_bIds = missing_data_details(business_with_missing_data)
    
    print(len(full_data_bIds), len(partial_data_bIds))

#     print_full_data_details(full_data_bIds, path)
#     print_partial_data_details(partial_data_bIds, path)
    
    return 

if __name__=='__main__':   
    
    start=time.time()
    path = "../../resources/dataset/"
    
    find_missing_data(path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  
