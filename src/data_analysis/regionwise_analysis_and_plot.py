import time
from collections import defaultdict
from INF553_YelpProject.src.utils.inputOutput_utils import csvReader, csvWriter


def region_wise_mean_score(path):
    las_vegas_data = csvReader(path+"final_lasvegas_dataset.csv")
    postal_code_avg = las_vegas_data.groupby('zip_code', as_index = False)['current_score'].mean()
    
    
    csvWriter(path + "postal_code_wise_analysis.csv", postal_code_avg)
    
    return


if __name__=='__main__':   
    
    start=time.time()
    path = "../../resources/dataset/"
    
    region_wise_mean_score(path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  
