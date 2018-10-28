#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import svm


# In[2]:


from sklearn import datasets


# In[3]:


clf=svm.SVC(gamma='scale')


# In[4]:


iris=datasets.load_iris()


# In[5]:


X=iris.data


# In[6]:


Y=iris.target


# In[7]:


clf.fit(X,Y)


# In[8]:


# now we are going to save the model


# In[9]:


import pickle


# In[10]:


s=pickle.dumps(clf)


# In[12]:


clf2=pickle.loads(s)


# In[14]:


clf2.predict(X[0:1])


# In[15]:


Y[0]


# In[16]:


# trying to predict the last element in the data sets
clf2.predict(X[-1:])


# In[17]:


Y[-1]


# In[ ]:




