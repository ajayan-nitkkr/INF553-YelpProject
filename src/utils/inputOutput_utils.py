import json
import pandas as pd

def load_yelp_data_json(file):
    
    with open(file,'rb') as jsonFin:
        data = pd.DataFrame(json.loads(line) for line in jsonFin)    
    
    return data 

def csvWriter(path, data):
    data.to_csv(path, encoding = "utf-8", index=False)
    
def csvReader(path):
    data = pd.read_csv(path, encoding = "utf-8")
    return data


def csvWriter_from_text(data, path):
    fout =  open(path, "w+", encoding = "utf-8")
    
    for key in data.keys():
        fout.write(str(key))
        for col in data[key]: 
            fout.write("," + str(col))
        
        fout.write("\n")
        
    fout.close()
    return