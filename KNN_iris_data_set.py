#!/usr/bin/env python
# coding: utf-8

# In[103]:


# In scikit we train the model using fit function for different estimators
# and we use the predict function to predict the target variable


# In[104]:


# using KNN to work with the iris data set


# In[105]:


from sklearn import datasets as ds


# In[109]:


from sklearn.svm import SVC
import numpy as np


# In[108]:


iris=ds.load_iris()


# In[110]:


# set the seed to reprodcue the result
np.random.seed(0)


# In[111]:


# generating random permutation of the indices
indices=np.random.permutation(len(iris.data))


# In[113]:


# now split the data into training data and test data


# In[114]:


train_x=iris.data[indices[:-10]]


# In[115]:


train_y=iris.target[indices[:-10]]


# In[116]:


test_x=iris.data[indices[-10:]]


# In[118]:


test_y=iris.target[indices[-10:]]


# In[119]:


# now importing the KNN models to train our data


# In[120]:


from sklearn.neighbors import KNeighborsClassifier


# In[121]:


knn=KNeighborsClassifier()


# In[122]:


knn.fit(train_x,train_y)


# In[123]:


# time to test the model


# In[132]:


res=knn.predict(test_x)
res


# In[126]:


test_y


# In[133]:


# writing a small function to check the accuracy of the model
def check_accuracy(a,b):
    count=0
    for i in range(len(a)):
        if a[i]==b[i]:
            count=count+1
    
    return (count/len(a))*100


# In[134]:


# find the accuracy of the model


# In[135]:


print(check_accuracy(knn.predict(test_x),test_y))


# In[ ]:




