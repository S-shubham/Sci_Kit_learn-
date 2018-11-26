#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


df=pd.read_csv("nba.csv")


# In[4]:


df


# In[5]:


df.xs(0)


# In[7]:


df.xs("Salary",axis=1)


# In[ ]:




