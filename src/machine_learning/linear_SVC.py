
# coding: utf-8

# In[18]:


import numpy as np
from sklearn.svm import SVC
import pandas as pd
import math
from INF553_YelpProject.src.machine_learning.model_save_and_load import *
from INF553_YelpProject.src.machine_learning.split_data_train_test_validation import *
from INF553_YelpProject.src.machine_learning.evaluation_metrics import *


# In[5]:


def read_dataset(filename):
    df=pd.DataFrame.from_csv(filename)
    return df


# In[12]:


def get_training_val_test_set(filename):
    #print(df.columns.values)
    X_train,X_val,X_test,y_train,y_val,y_test=splitData(filename)
    return X_train,X_val,X_test,y_train,y_val,y_test


# In[13]:


def train_LinearSVC(X_train,Y_train):
    '''
    Similar to SVC with parameter kernel=’linear’, but implemented in terms of liblinear rather than libsvm, so it has more flexibility in the choice of penalties and loss functions and should scale better to large numbers of samples.
    This class supports both dense and sparse input and the multiclass support is handled according to a one-vs-the-rest scheme.
    '''
    clf = LinearSVC(random_state=0, tol=1e-5)
    #hinge loss, L2 penalty, do dual=False when n_samples>n_features
    model = clf.fit(X_train, Y_train) 
    save_model(model,'svc_model.sav')


# In[14]:


def predict_health_score(X_test):
    Y_pred=clf.predict([X_test])
    return Y_pred


# In[15]:


def get_eval_metrics(Y_test,Y_pred):
    #Use Ajay's API
    eval_obj=EvaluationMetric()
    eval_dict=eval_obj.get_evaluation_metrics(Y_test, Y_pred)
    return eval_dict


# In[16]:


df=read_dataset('../../resources/dataset/final_lasvegas_dataset.csv')
X_train,X_val,X_test,y_train,y_val,y_test=get_training_val_test_set(df)
train_SVC(X_train,Y_train)
Y_pred=predict_health_score(X_test)
eval_dict=get_eval_metrics(Y_test,Y_pred)

