import time
from INF553_YelpProject.src.utils.inputOutput_utils import csvReader, csvWriter

def find_business_with_missing_data(data):
    pass



def find_missing_data(path):
    yelp_data = csvReader(path+"valid_business_yelp_data.csv")
    
    business_with_missing_data = find_business_with_missing_data(yelp_data)
    


if __name__=='__main__':   
    
    start=time.time()
    path = "../../resources/dataset/"
    
    find_missing_data(path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  
