import pandas as pd
import matplotlib.pyplot as plt

def plot_grade_vs_rest(filename):
	df=pd.DataFrame.from_csv(filename)
	print(df.shape)
	print(df.columns.values)
	print(df.InspectionGrade.unique())
	df_count=df.groupby('InspectionGrade').InspectionGrade.count()
	print(df_count)
	df_percentage=100 * df.InspectionGrade.value_counts() / len(df.InspectionGrade)
	print(df_percentage)
	df_count.plot.bar()
	ax = df_count.plot(kind='bar',  title='InspectionGrade')
	for p in ax.patches:
		ax.annotate(str(p.get_height()), xy=(p.get_x(), p.get_height()))
	df_count.to_csv('Grade_vs_Restaurants.csv',',')

if __name__=="__main__":
	filename='/home/rim/INF-Project/Restaurant_Inspections_InspectionGrade.csv'
	plot_grade_vs_rest(filename)