#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np


# In[2]:


from sklearn import datasets


# In[3]:


from sklearn import svm


# In[4]:


digit=datasets.load_digits()


# In[7]:


type(digit)


# In[15]:


len(digit.data)


# In[9]:


# now divide the datasets into test and training set


# In[16]:


# generate random indices
indices=np.random.permutation(len(digit.data))


# In[17]:


indices


# In[21]:


train_x=digit.data[indices[:1348]]


# In[23]:


train_y=digit.target[indices[:1348]]


# In[26]:


test_x=digit.data[indices[1348:]]


# In[27]:


test_y=digit.target[indices[1348:]]


# In[28]:


# now we have randomly taken a train and test sample of the data
# time to apply the macine learnin model


# In[30]:


predictor=svm.SVC(gamma=0.0001,C=100)


# In[31]:


predictor.fit(train_x,train_y)


# In[32]:


res=predictor.predict(test_x)


# In[33]:


count=0;
for i in range(len(res)):
    if res[i]==test_y[i]:
        count=count+1


# In[35]:


count/len(res)*100


# In[ ]:


# the model has 98.9 % accuracy

