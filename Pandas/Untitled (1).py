#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[26]:


df=pd.read_csv("apple.csv" , parse_dates=["date"],index_col="date")


# In[27]:


df


# In[28]:


df.info()


# In[29]:


df.close.resample('M').mean()


# In[33]:


df.close.resample('M').mean()


# In[34]:


df


# In[37]:


df.open.resample('Q').mean()


# In[38]:


df


# In[45]:


df.close.rolling(3).mean()


# In[46]:


df=pd.read_csv("nba.csv")


# In[50]:


df.Team.replace(to_replace='Boston Celtics',value='shubhi')


# In[51]:


ok=pd.DataFrame([1,5,11,4,8,np.nan,10,16])


# In[52]:


ok


# In[53]:


ok.replace(to_replace=np.nan, value=100)


# In[55]:



dk=pd.DataFrame({"Brand":['A','B','ABC','D','AB'],"Spec":['H','I','J','K','L']})


# In[56]:


dk


# In[59]:


dk.Brand.replace(to_replace=['ABC','AB'],value='LOL')


# In[ ]:




