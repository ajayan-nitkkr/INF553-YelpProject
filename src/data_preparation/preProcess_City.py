import json
import time
import pandas as pd
from collections import defaultdict

############################################################### File Operations

def jsonReader(path):
    file = []
    if (path):
        jsonFin = open(path, "r", encoding = "utf-8")
        jsonData = {}
        index = 0
        statesData = defaultdict(list)
        statesCount = defaultdict(int)
        inValidData = defaultdict(list)
        cityCount = defaultdict(int)
        lasVegasData = []
        for line in jsonFin:
            record = json.loads(line)
            
            cityCount[(record['city'],record['state'])]+=1
            
            #Removing ON from states
            
            if len(record['state'])<2 or len(record['state'])>2 or record['state'].isdigit():
                
                if record['state']=='C':
                    record['state']="CA"
                    statesData[record['state']].append(record)

                else:
                    inValidData[record['business_id']] = [record['state'], record['city'],record['postal_code']] 
                
            elif len(record['state']) == 2:
                statesData[record['state']].append(record)
                statesCount[record['state']]+=1
                
            if record['state']=="NV" and record['city']=="Las Vegas":
                lasVegasData.append(record)
    
#     for key in inValidData.keys():
#         print(key, inValidData[key])
        
    #print(len(statesData), len(inValidData))

#     for key in sorted(statesCount, key = statesCount.get, reverse  = True):
#         print(key, statesCount[key])
#     for key in sorted(cityCount, key = cityCount.get, reverse  = True):
#         print(key, cityCount[key])


#     for key in sorted(statesData):
#         print(key+" : "+ ", ".join(statesData[key]))
    
    return lasVegasData 


def load_yelp_challenge_data(file):
    
    with open(file,'rb') as jsonFin:
        data = pd.DataFrame(json.loads(line) for line in jsonFin)
    
    data = data[data['city'].map(lambda x: x=="Las Vegas")]
    data = data[data['state'].map(lambda x: x=="NV")]
    
    print("Yelp Data: "+str(len(data))) 
    return data 

def csvWriter(path, data):
    data.to_csv(path, encoding = "utf-8")

def jsonWriter(path,lasVegasData):
    jsonFout = open(path+file, "w",encoding ="utf-8")
    for element in lasVegasData:
        jsonFout.write(str(element)+"\n")
    jsonFout.close()
    
    return
    
def preprocessJson(path):
    
    filePath = path + "yelp_academic_dataset_business.json"
    #filePath = path + "temp_business.json"
    
    #lasVegasData = jsonReader(filePath)
    lasVegasData = load_yelp_challenge_data(filePath)
    csvWriter(path+"lasVegas.csv", lasVegasData)
    
    data = pd.read_csv(path+"lasVegas.csv")
    
    #jsonWriter(path+"lasVegas.json", lasVegasData)
    
    
     

if __name__=='__main__':   
    
    start=time.time()
    
    path = "../../../data/yelp_dataset/"
    preprocessJson(path) 
    
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  
    
    