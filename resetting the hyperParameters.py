#!/usr/bin/env python
# coding: utf-8

# In[56]:


import numpy as np


# In[57]:


from sklearn.svm import SVC


# In[58]:


rng=np.random.RandomState(0)


# In[67]:


x=rng.rand(100,10)


# In[68]:


y=rng.binomial(1,0.5,100)


# In[69]:


X_test=rng.rand(5,10)


# In[70]:


# now we will not set the hyperparameter to clf as of now


# In[71]:


clf=SVC()


# In[72]:


clf.set_params(kernel='linear').fit(x,y)


# In[74]:


clf.predict(X_test)


# In[75]:


# again re-setting the parameters for clf


# In[76]:


clf.set_params(kernel='rbf',gamma='scale').fit(x,y)


# In[77]:


clf.predict(X_test)


# In[ ]:




