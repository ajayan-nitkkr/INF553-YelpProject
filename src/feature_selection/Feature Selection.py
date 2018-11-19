
# coding: utf-8

# In[1]:


from sklearn.feature_selection import VarianceThreshold


# In[2]:


X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
sel.fit_transform(X)


# In[3]:


from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif, mutual_info_classif


# In[4]:


X_new = SelectKBest(chi2, k=10).fit_transform(X_train, Y_train)

#not for sparse data
X_new = SelectKBest(f_classif, k=10).fit_transform(X_train, Y_train)

X_new = SelectKBest(mutual_info_classif, k=10).fit_transform(X_train, Y_train)

