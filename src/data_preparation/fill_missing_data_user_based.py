import time
from INF553_YelpProject.src.utils.inputOutput_utils import csvReader, csvWriter_from_text

def readText(path):
    
    fin = open(path, "r", encoding = "utf-8")
    business = dict()
    for line in fin:
        line = line.split(",")
        business[line[0]]=line[1:]
    
    return business

def get_schema(path, valid_cols): 
    fin = open(path , "r", encoding = "utf-8")
    business_missing_cols = dict()
    
    for line in fin:
        line = line.split(",")
        cols = [x for x in line[1:] if x in valid_cols]
        business_missing_cols[line[0]]=cols
    
    return business_missing_cols

def get_valid_cols(path):
    fin = open(path , "r", encoding = "utf-8")
    cols = []
    for line in fin:
        line = line.strip()
        cols.append(line)
        
    return cols 

def fill_missing_data(path):
    
    las_vegas_data = csvReader(path + "final_lasvegas_dataset_v4.csv")
    business_with_sim_data = readText(path+"similar_users_pearson.csv")
    valid_cols = get_valid_cols("../../resources/schema/Final_schema_v4.txt")
    
    business_missing_cols = get_schema(path + "business_with_partial_data_lasVegas.csv", valid_cols)
    
#     total_data_len = len(business_with_missing_data)
    count = 0
    empty_cols = []
        
    for _, row in las_vegas_data.iterrows():
        
        bid = row['business_id']    
        if bid in business_with_sim_data.keys():
#             print(count, bid)
            similar_users = business_with_sim_data[bid]
            sim_user_count = len(similar_users)
             
            schema = [x.strip() for x in business_missing_cols[bid]]
#             schema = ['accepts_insurance', 'alcohol']
            print(schema)
             
            for col in schema:
         
                if row[col]!="Null":
                    continue
                 
                empty = 0
                for user in similar_users:
                    user = user.strip()
                    sim_data = las_vegas_data.loc[las_vegas_data['business_id'] == user]
                     
                    if (sim_data[col].values[0] !="Null"):
                        pass
                    else:
                        empty+=1
                         
                if empty ==  sim_user_count:
                    empty_cols.append((user, col))
                    continue
         
         
        count+=1        
        break    
            

    
    

if __name__=='__main__':   
    
    start=time.time()
    path = "../../resources/dataset/"
    
    fill_missing_data(path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  