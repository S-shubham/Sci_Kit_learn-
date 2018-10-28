#!/usr/bin/env python
# coding: utf-8

# In[18]:


# In sci-kit learn input is alwasy type_Casted to float64


# In[19]:


import numpy as np


# In[21]:


from sklearn import random_projection


# In[22]:


rng=np.random.RandomState(0)


# In[27]:


x=rng.rand(10,2000)


# In[28]:


x.dtype


# In[29]:


x=np.array(x,dtype='float32')


# In[32]:


# now we have explicitly upcasted the data type of 'x' to float32


# In[33]:


x.dtype


# In[35]:


transformer=random_projection.GaussianRandomProjection()


# In[36]:


X=transformer.fit_transform(x)


# In[37]:


X.dtype


# In[ ]:




