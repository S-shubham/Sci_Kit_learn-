#!/usr/bin/env python
# coding: utf-8

# In[1]:


2+3


# In[3]:


from sklearn import datasets as ds


# In[5]:


digit=ds.load_digits()


# In[6]:


from sklearn import svm


# In[7]:


clf=svm.SVC(gamma=0.001,C=100.)


# In[10]:


clf.fit(digit.data[:-1],digit.target[:-1])


# In[12]:


clf.predict(digit.data[-1:])


# In[14]:


digit.target[-1:]


# In[ ]:




