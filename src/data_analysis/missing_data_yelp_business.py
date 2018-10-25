import time
from INF553_YelpProject.src.utils.inputOutput_utils import csvReader, csvWriter

def find_business_with_missing_data(data):
    
    data_schema = ['name', "neighborhood", 'address', 'city', 'state', 'postal_code', 'review_count',
                   'latitude', "longitude", "stars", "is_open", "attributes", "categories", "hours" ]
    
    attribute_schema = ["BikeParking", "BusinessAcceptsCreditCards", "BusinessParking", "GoodForKids",
                        "HasTV", "NoiseLevel", "OutdoorSeating", "RestaurantsAttire", "RestaurantsDelivery",
                        "RestaurantsGoodForGroups", "RestaurantsPriceRange2", "RestaurantsReservations", "RestaurantsTakeOut"]
    
    business_parking_schema = ['garage', "street", "validated", "lot", "valet"]
    
    missing_data = data
    for _, row in missing_data.iterrows():
        for col in data_schema:
            if len(str(row[col]))==0:
                row[col] = 0
            else:
                row[col] = 1
      
    return missing_data


def find_missing_data(path):
    yelp_data = csvReader(path+"preprocessed_lasVegas.csv")
    
    business_with_missing_data = find_business_with_missing_data(yelp_data)
    csvWriter(path+"missing_data_yelp_business.csv", business_with_missing_data)
    
    return 

if __name__=='__main__':   
    
    start=time.time()
    path = "../../resources/dataset/"
    
    find_missing_data(path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  
