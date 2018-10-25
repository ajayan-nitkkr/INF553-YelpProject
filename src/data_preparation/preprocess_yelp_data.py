import time
from INF553_YelpProject.src.utils.inputOutput_utils import load_yelp_data_json, csvWriter

def load_lasVegas_data(data):
    
    data = data[data['city'].map(lambda x: x=="Las Vegas")]
    data = data[data['state'].map(lambda x: x=="NV")]  
    return data 



def clean_yelp_data(data):
    us_states = {"AL" : "01", "AK" : "02", "AZ" : "04", "AR" : "05" ,"CA" : "06", "CO" : "08", "CT" : "09",
                 "DE" : "10", "DC" : "11", "FL" : "12", "GA" : "13", "HI" : "15", "ID" : "16", "IL" : "17",
                 "IN" : "18", "IA" : "19", "KS" : "20", "KY" : "21", "LA" : "22", "ME" : "23", "MD" : "24",
                 "MA" : "25", "MI" : "26", "MN" : "27", "MS" : "28", "MO" : "29", "MT" : "30", "NE" : "31",
                 "NV" : "32", "NH" : "33", "NJ" : "34", "NM" : "35", "NY" : "36", "NC" : "37", "ND" : "38",
                 "OH" : "39", "OK" : "40", "OR" : "41", "PA" : "42", "RI" : "44", "SC" : "45", "SD" : "46",
                 "TN" : "47", "TX" : "48", "UT" : "49", "VT" : "50", "VA" : "51", "WA" : "53", "WV" : "54",
                 "WI" : "55", "WY" : "56"}
    
   
    invalid_data = data[data['state'].map(lambda x: x not in us_states)]
    data = data[data['state'].map(lambda x: (x in us_states.keys()) or (x in us_states.values()))]   
#    print(len(invalid_data), len(data))
    
    return data
     

def groupby_region(data):
    group_counts = data['state'].value_counts()
    
    return group_counts
 
def find_missing_data_count(data):
    pass    


def valid_business(categories_str):
    if categories_str is None:
        return False
    categories = categories_str.split(',')
    fin  = open("../../resources/dataset/business_categories.txt")
    valid_business_list = dict()
    for line in fin:
        line = line.strip()
        valid_business_list[line]=1
    
    for category in categories:
        curr_category = category.strip()
        if curr_category in valid_business_list.keys():
            return True
    return False

def clean_business(data):
    data = data[data['categories'].map(lambda x: valid_business(x)==True)]
    return data
    
def preprocess_yelp_data(path, save_path):
    
    file_path = path + "yelp_academic_dataset_business.json"   
    yelp_data = load_yelp_data_json(file_path)
    
    lasVegasData = load_lasVegas_data(yelp_data)    
    lasVegasData = clean_business(lasVegasData)
    
#     csvWriter(save_path + "preprocessed_lasVegas.csv", lasVegasData)

#     yelp_data = clean_yelp_data(yelp_data)
#     group_count = groupby_region(yelp_data)
#     csvWriter(save_path+"region_wise_counts.csv", group_count)
#     missing_data_count = find_missing_data_count(yelp_data)
        
    return
    
if __name__=='__main__':   
    
    start=time.time()
    path = "../../../data/yelp_dataset/"
    save_path = "../../resources/dataset/"
    
    preprocess_yelp_data(path,save_path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  
    
    