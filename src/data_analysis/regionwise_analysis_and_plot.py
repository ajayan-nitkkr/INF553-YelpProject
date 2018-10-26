import time
from collections import defaultdict
from INF553_YelpProject.src.utils.inputOutput_utils import csvReader, csvWriter


def region_wise_mean_score(path):
    pass

if __name__=='__main__':   
    
    start=time.time()
    path = "../../resources/dataset/"
    
    region_wise_mean_score(path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  
