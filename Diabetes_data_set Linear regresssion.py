#!/usr/bin/env python
# coding: utf-8

# In[136]:


# working with diabetese data set
# using linear model to predict 


# In[139]:


from sklearn import datasets as ds
import numpy as np


# In[138]:


diabetes=ds.load_diabetes()


# In[141]:


np.random.seed(0)


# In[142]:


indices=np.random.permutation(len(diabetes.data))


# In[144]:


train_x=diabetes.data[indices[:-20]]


# In[145]:


train_y=diabetes.target[indices[:-20]]


# In[146]:


test_x=diabetes.data[indices[-20:]]


# In[147]:


test_y=diabetes.target[indices[-20:]]


# In[148]:


from sklearn import linear_model


# In[149]:


regr=linear_model.LinearRegression()


# In[151]:


regr.fit(train_x,train_y)


# In[154]:


a=regr.predict(test_x)


# In[176]:


def find_accuracy(a,b):
    count=0
    for i in range(len(a)):
        count=count+(a[i]-b[i])**2
    return math.sqrt(count/len(a))


# In[188]:


print("the accuracy of our model is : ",find_accuracy(a,test_y))


# In[189]:


# finding out the value of the coefficients


# In[190]:


print(regr.coef_)


# In[191]:


# the mean squared error is


# In[193]:


np.mean((a-test_y)**2)


# In[194]:


# finding the variance score for this data set
# 1 being perfect predictions 
# 0 being there is no relation among the data
regr.score(test_x,test_y)


# In[ ]:




