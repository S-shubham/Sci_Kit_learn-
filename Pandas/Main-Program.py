#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[36]:


# To fetch data from the links
import requests


# In[28]:


# Reading the excel file into a dataframe
df=pd.read_excel("abc.xlsx",sheet_name='cik_list_ajay')


# In[29]:


# Print the datafrme
df


# In[31]:


# To check if there is even any missing value in the dataframe
df.isnull().values.any()


# In[32]:


# To check the data type of each column
df.info()


# In[33]:


# Now we want to modify the "SECFNAME" column by adding the prefix "https://www.sec.gov/Archives/"
df.SECFNAME="https://www.sec.gov/Archives/"+df.SECFNAME


# In[34]:


df


# In[38]:


tfile=requests.get(df.SECFNAME[0]).content


# In[39]:


# In the above line we have read the content from the link in the first row.


# In[42]:


# check the type of tfile
type(tfile)


# In[43]:


tfile


# In[ ]:




