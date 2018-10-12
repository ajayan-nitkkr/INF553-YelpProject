import time
from INF553_YelpProject.src.utils.inputOutput_utils import load_yelp_data_json, csvWriter

def load_lasVegas_data(data):
    
    data = data[data['city'].map(lambda x: x=="Las Vegas")]
    data = data[data['state'].map(lambda x: x=="NV")]
    return data 
    
def preprocess_yelp_data(path):
    
    filePath = path + "yelp_academic_dataset_business.json"   
    yelp_data = load_yelp_data_json(filePath)
    lasVegasData = load_lasVegas_data(yelp_data)
    csvWriter(path + "lasVegas.csv", lasVegasData)
    
if __name__=='__main__':   
    
    start=time.time()
    path = "../../../data/yelp_dataset/"
    preprocess_yelp_data(path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  
    
    