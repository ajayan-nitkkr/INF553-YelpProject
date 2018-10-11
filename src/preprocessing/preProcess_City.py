import json
import time
from collections import defaultdict

############################################################### File Operations

def jsonReader(path):
    file = []
    if (path):
        jsonFin = open(path, "r", encoding = "utf-8")
        jsonData = {}
        index = 0
        statesData = defaultdict(int)
        inValidData = defaultdict(list)
        for line in jsonFin:
            record = json.loads(line)
            
            if len(record['state'])<2 or len(record['state'])>2 or record['state'].isdigit():
                inValidData[record['business_id']] = [record['state'], record['city'],record['postal_code']] 
            
            elif len(record['state']) == 2:
                statesData[record['state']]+=1
    
    for key in inValidData.keys():
        print(key, inValidData[key])
    #print(len(statesData), len(inValidStatesData))
#     for key in sorted(statesData, key=statesData.get, reverse = True):
#         print(key+" : "+ str(statesData[key]))
    
    return statesData 


def csvWriter(path):
    pass

def preprocessJson(path):
    
    filePath = path + "yelp_academic_dataset_business.json"
    #filePath = path + "temp_business.json"
    
    fileData = jsonReader(filePath)
     




if __name__=='__main__':   
    
    start=time.time()
    
    path = "../../../data/yelp_dataset/"
    preprocessJson(path) 
    
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  
    
    