import pandas as pd
alpha_column_file="../feature_selection/columns_vs_alpha.txt"
f=open(alpha_column_file)
for i in range(0,6):
    line=f.readline().strip('\n').strip('\t').split(",")
    column_names=line[2:]
    #print(column_names)
    alpha_val=line[1]
    #print(alpha_val)
    v4_data = pd.read_csv("../../resources/dataset/final_lasvegas_dataset_v4.csv")
    X = v4_data[column_names]
    op_file=open("../../resources/dataset/dataset_alpha_"+str(alpha_val)+".csv","w")
    X.to_csv(op_file,',',index=False)

