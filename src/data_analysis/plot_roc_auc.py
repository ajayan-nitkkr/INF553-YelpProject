import time
from collections import defaultdict
from INF553_YelpProject.src.utils.inputOutput_utils import csvReader
import matplotlib.pyplot as plt

def plot_roc(data):
    pass

def plot_auc(data):
    pass

def plot_graphs(path):
    
    las_vegas_data = csvReader(path + "final_lasvegas_dataset.csv")
    
    plot_roc(las_vegas_data)
    plot_auc(las_vegas_data)

if __name__=='__main__':   
    
    start=time.time()
    path = "../../resources/dataset/"
    
    plot_graphs(path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" ) 