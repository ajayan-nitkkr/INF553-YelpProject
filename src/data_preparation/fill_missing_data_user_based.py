import time
from collections import defaultdict, Counter
from INF553_YelpProject.src.utils.inputOutput_utils import csvReader, csvWriter, csvWriter_from_text

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


def print_filled_data_analysis(path, data):
    fout = open(path, "w", encoding = "utf-8")
    
    for key in data.keys():
        fout.write(str(key) +" : ")
        for item in data[key]:
            fout.write("("+ item[0]+", " + str(item[1])+ ")")
        fout.write("\n")
    
    fout.close()
    return

def get_valid_cols(path):
    fin = open(path , "r", encoding = "utf-8")
    cols = []
    for line in fin:
        line = line.strip()
        cols.append(line)
        
    return cols 


def get_user_based_data(data):
    val_counts = Counter(data)
    return val_counts.most_common(1)[0][0]

def fill_missing_data(path):
    
    las_vegas_data = csvReader(path + "v4_with_business_id.csv")
    business_with_sim_data = readText(path+"similar_users_pearson.csv")
    valid_cols = get_valid_cols("../../resources/schema/Final_schema_v4.txt")
    
    business_missing_cols = get_schema(path + "business_with_partial_data_lasVegas.csv", valid_cols)
    
    total_data_len = (len(las_vegas_data))
    print(len(las_vegas_data))
    
    empty_cols = defaultdict(list)
    filled_data_analysis = defaultdict(list)
        
    for _, row in las_vegas_data.iterrows():
        
        bid = row['business_id']    
        
        if bid in business_with_sim_data.keys():
#             print(count, bid)
            similar_users = business_with_sim_data[bid]
            sim_user_count = len(similar_users)
             
            schema = [x.strip() for x in business_missing_cols[bid]]
#             schema = ['accepts_insurance', 'alcohol']
            
            
            for col in schema:
                all_sim_data = []
                final_data = row[col]
                if row[col] != -1:
                    continue
                 
                empty = 0
                for user in similar_users:
                    
                    user = user.strip()
                    
                    sim_data = las_vegas_data.loc[las_vegas_data['business_id'] == user]
                    
                    if (sim_data[col].values[0] != -1):
                        all_sim_data.append(sim_data[col].values[0])
                    
                    else:
                        empty+=1
                         
                if empty ==  sim_user_count:
                    
                    empty_cols[user].append(col)
                    continue
               
                final_data = get_user_based_data(all_sim_data[col])
            
                row[col] = final_data
                filled_data_analysis[bid].append((col,final_data))
            
                     
        else:
            continue
    
    print(len(las_vegas_data))
    if (len(las_vegas_data)==total_data_len):   
        csvWriter(path + "v4_with_filled_data.csv", las_vegas_data)
    
    else:
        print("Missed some data")
        
    csvWriter_from_text(empty_cols, path + "empty_columns.csv")
    
    print_filled_data_analysis(path + "filled_data_analysis.csv", filled_data_analysis)
    
    return

if __name__=='__main__':   
    
    start=time.time()
    path = "../../resources/dataset/"
    
    fill_missing_data(path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  