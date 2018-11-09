import time
from collections import defaultdict
from INF553_YelpProject.src.utils.inputOutput_utils import csvReader, csvWriter

def print_data(path, data):
    fout =  open(path, "w+", encoding = "utf-8")
    
    for key in data.keys():
        fout.write(str(key))
        for col in data[key]: 
            fout.write("," + str(col))
        
        fout.write("\n")
        
    fout.close()
    return

def region_wise_mean_score(path):
    las_vegas_data = csvReader(path+"final_lasvegas_dataset.csv")
    postal_code_avg = las_vegas_data.groupby('zip_code', as_index = False)['inspection_score'].mean()
    
    zip_code_mean = defaultdict(float)
    for _, row in postal_code_avg.iterrows():
        zip_code_mean[int(row['zip_code'])]=float(row['inspection_score'])
        
    under_performing_business = defaultdict(list)
    for _, row in las_vegas_data.iterrows():
        zip_code = int(row['zip_code'])
        score = int(row['inspection_score'])
        
        if score < zip_code_mean[zip_code]:
            under_performing_business[zip_code].append(row['business_id'])
    
    under_performing_business_counts = defaultdict(list)
    for key in under_performing_business.keys():
        under_performing_business_counts[key]=[zip_code_mean[key], len(under_performing_business[key])]
    
    csvWriter(path + "postal_code_wise_analysis.csv", postal_code_avg)
    print_data(path + "under_perfermoing_business_lasVegas.csv", under_performing_business)
    print_data(path + "under_perfermoing_business_counts_lasVegas.csv", under_performing_business_counts)    
    return


if __name__=='__main__':   
    
    start=time.time()
    path = "../../resources/dataset/"
    
    region_wise_mean_score(path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  
