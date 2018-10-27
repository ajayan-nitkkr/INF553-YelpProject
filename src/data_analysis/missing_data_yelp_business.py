import time
from collections import defaultdict
from INF553_YelpProject.src.utils.inputOutput_utils import csvReader, csvWriter

def find_business_with_missing_data(data, data_schema):
    
#     data_schema = ['name', "neighborhood", 'address', 'city', 'state', 'postal_code', 'review_count',
#                    'latitude', "longitude", "stars", "is_open", "attributes", "categories", "hours" ]
#     
#     attribute_schema = ["BikeParking", "BusinessAcceptsCreditCards", "BusinessParking", "GoodForKids",
#                         "HasTV", "NoiseLevel", "OutdoorSeating", "RestaurantsAttire", "RestaurantsDelivery",
#                         "RestaurantsGoodForGroups", "RestaurantsPriceRange2", "RestaurantsReservations", "RestaurantsTakeOut"]
#     
#     business_parking_schema = ['garage', "street", "validated", "lot", "valet"]
    
    data.fillna(value = "Null", inplace = True)

    missing_data = data
#     for col in data_schema:
#         missing_data[col]=data[col].isnull()
    
#     for _,row in missing_data.iterrows():
#         for col in data_schema:
#             if row[col] == "Null":
#                 row[col]=True
#             else:
#                 row[col]=False
    
         
    return missing_data


def missing_data_details(data, data_schema):
    
#     data_schema = ['name', "neighborhood", 'address', 'city', 'state', 'postal_code', 'review_count',
#                    'latitude', "longitude", "stars", "is_open", "attributes", "categories", "hours" ]
    
    full_data_bIds = []
    partial_data_bIds = defaultdict(list)
    
    for _,row in data.iterrows():
        full = True
        b_id = row['BusinessId']
        for col in data_schema:
            if row[col]=="Null":
                partial_data_bIds[b_id].append(col)
                full = False
        if  full:
            full_data_bIds.append(b_id)

    return full_data_bIds, partial_data_bIds

def print_full_data_details(data, path):
    fout =  open(path+"business_with_full_data_lasVegas.txt", "w+", encoding = "utf-8")
    
    for b_id in data:
        fout.write(str(b_id) + "\n")
    
    fout.close()
    return

def print_partial_data_details(data, path):
    fout =  open(path+"business_with_partial_data_lasVegas.csv", "w+", encoding = "utf-8")
    
    for key in data.keys():
        fout.write(str(key))
        for col in data[key]: 
            fout.write("," + str(col))
        
        fout.write("\n")
        
    fout.close()
    return

def print_partial_data_percentage(data, path):
    fout =  open(path+"business_with_percent_partial_data_lasVegas.txt", "w+", encoding = "utf-8")
    
    for key in data.keys():
        fout.write(str(key) +" : " + str(data[key]))
        fout.write("\n")
        
    fout.close()
    return

def print_partial_feature_data_percentage(data, path):
    fout =  open(path+"business_with_percent_partial_feature_data_lasVegas.txt", "w+", encoding = "utf-8")
    
    for key in data.keys():
        fout.write(str(key) +" : " + str(data[key]))
        fout.write("\n")
        
    fout.close()
    return


def get_schema(path):
    fin =  open(path,"r", encoding = "utf-8")
    
    data_schema = [] 
    for line in fin:
        line = line.split()
        col = line[0].strip('"')
        data_schema.append(col)
        
    return data_schema    

def get_partial_data_percentage(data):
    partial_data_analysis_row = {}
    partial_data_analysis_col = defaultdict(int)
    total = len(data)
    
    for key in data.keys():
        partial_data_analysis_row[key]=(float(len(data[key]))/47.0)*100  
        for col in data[key]:
            partial_data_analysis_col[col]+=1
        
    for key in partial_data_analysis_col.keys():
        partial_data_analysis_col[key]/=total
        partial_data_analysis_col[key]*=100
    
    return partial_data_analysis_row, partial_data_analysis_col     
    
def find_missing_data(path):
    yelp_data = csvReader(path+"LasVegas_Restaurants_Rimsha_Preprocessed.csv")
#     yelp_data = csvReader(path+"valid_business_yelp_data.csv")    
      
    data_schema = get_schema("../../resources/schema/Schema_Business_Preprocessed.txt")
    data_schema.remove("BusinessId")
    
    business_with_missing_data = find_business_with_missing_data(yelp_data, data_schema)
    csvWriter(path+"missing_data_yelp_business.csv", business_with_missing_data)
     
     
    full_data_bIds, partial_data_bIds = missing_data_details(business_with_missing_data, data_schema)
    
    partial_data_bId_percent, partial_data_features_percent = get_partial_data_percentage(partial_data_bIds) 
    
    mean_partial_data_row = 0  
    
    print_full_data_details(full_data_bIds, path)
    print_partial_data_details(partial_data_bIds, path)
    print_partial_data_percentage(partial_data_bId_percent, path)
    print_partial_feature_data_percentage(partial_data_features_percent, path)
     
    print(len(partial_data_bIds))
    for key in partial_data_bId_percent.keys():
        mean_partial_data_row+= partial_data_bId_percent[key]  
     
    max_val = -float('inf')
    rareFeature = ""
    
    for key in partial_data_features_percent.keys():
        val = partial_data_features_percent[key]
        if val > max_val:
            max_val = val
            rareFeature = key
    
    commonFeatures = []
    for col in data_schema:
        if col in partial_data_features_percent.keys():
            continue
        commonFeatures.append(col)
        
    print("Mean B_ids Missing Data: "+str(mean_partial_data_row/len(partial_data_bId_percent)))
    print("Most rare feature: " + rareFeature)
    print("Most common features: " + ", ".join(commonFeatures))
    
    return 

if __name__=='__main__':   
    
    start=time.time()
    path = "../../resources/dataset/"
    
    find_missing_data(path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  
