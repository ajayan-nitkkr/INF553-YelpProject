import json
import pandas as pd

def load_yelp_data_json(file):
    
    with open(file,'rb') as jsonFin:
        data = pd.DataFrame(json.loads(line) for line in jsonFin)    
    
    return data 

def csvWriter(path, data):
    data.to_csv(path, encoding = "utf-8", index=False)

