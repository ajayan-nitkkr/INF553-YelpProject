import pandas
import pickle

#Logistic Regression as Sample model
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression

class ModelUtils:
	def __init__(self):
		pass

	def sample_training(self):
		#Reading sample dataset, Training of Logistic Regression model
		url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
		names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
		#dataframe = pandas.read_csv(filename, names=column_names)
		dataframe = pandas.read_csv(url, names=names)
		array = dataframe.values
		X = array[:,0:8]
		Y = array[:,8]
		test_size = 0.33
		seed = 7
		X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
		# Fit the model on 33%
		model = LogisticRegression()
		model.fit(X_train, Y_train)
		return model
		#return X_test,Y_test,model
		

	def save_model(self,model,filename):
		# save the model to disk
		#filename = 'finalized_model.sav'
		pickle.dump(model, open(filename, 'wb'))
		return filename

	#def load_model(self,X_test,Y_test,filename): 
	def load_model(self,filename): 
		# load the model from disk
		loaded_model = pickle.load(open(filename, 'rb'))
		return loaded_model		
		#result = loaded_model.score(X_test, Y_test)
		#print(result)

if __name__=='__main__':
	obj=ModelUtils()
	#X_test,Y_test,model=obj.sample_training()
	model=obj.sample_training()
	obj.save_model(model,'finalized_model.sav')
	obj.load_model('finalized_model.sav')
	#obj.load_model(X_test,Y_test,'finalized_model.sav')
