#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[22]:


df=pd.DataFrame({"A":[1,5,3,4,2],"B":[3,2,4,3,4],"C":[2,2,7,3,4],"D":[4,3,6,12,7]},index=["A1","A2","A3","A4","A5"])


# In[23]:


sr=pd.Series([12,25,64,18],index=["A","B","C","D"])


# In[24]:


df2=pd.DataFrame({"A":[10,11,7,8,5],"B":[21,5,32,4,6],"C":[11,21,23,7,9],"D":[1,5,3,8,6]},index=["A1","A2","A3","A4","A5"])


# In[6]:


df.rtruediv(sr,axis=1)


# In[7]:


df.rtruediv(df2)


# In[8]:


df=pd.read_csv("nba.csv")


# In[9]:


df


# In[10]:


df.sample(10)


# In[12]:


df.sample(frac=0.05)


# In[14]:


df.sample(frac=0.03,axis=0,replace=False)


# In[16]:


df.select_dtypes(exclude='float64')


# In[17]:


df.sem(axis=0)


# In[21]:


df.sem(axis=1,skipna=False)


# In[25]:


df


# In[34]:


df=pd.DataFrame({"A":[1,5,3,4,2],"B":[3,2,4,3,4],"C":[2,2,7,3,4],"D":[4,3,6,12,7]})


# In[35]:


df


# In[36]:


df.set_value(2,'B',100)


# In[32]:


df.set_value(2,2,100,takeable=True)


# In[33]:


df.set_value(8,8,1000)


# In[37]:


ind=pd.date_range('01/01/2000',periods=5,freq='12H')


# In[43]:


df=pd.DataFrame({"A":[1,2,3,4,5],"B":[10,20,30,40,50],"C":[11,22,33,44,55],"D":[12,24,51,36,2]},index=ind)


# In[44]:


df


# In[49]:


df.shift(-2,axis=0)


# In[50]:


df.shift(-2,axis=1)


# In[51]:


df=pd.read_csv("nba.csv")


# In[52]:


df


# In[54]:


df.skew(axis=1,skipna=True)


# In[55]:


df


# In[56]:


df=pd.DataFrame({"A":[1,2,3,4,5],"B":[10,20,30,40,50],"C":[11,22,33,44,55],"D":[12,24,51,36,2]},index=ind)


# In[57]:


df


# In[67]:


df.slice_shift(-2,axis=1)


# In[68]:


df=pd.read_csv("nba.csv")


# In[69]:


df


# In[70]:


df.sort_index(axis=1)


# In[75]:


df2=df.sample(15)


# In[76]:


df2


# In[78]:


df2.sort_index(axis=1)


# In[80]:


df.sort_index(axis=1)


# In[81]:


df


# In[82]:


df.std(axis=0,skipna=True)


# In[83]:


df.std(axis=1,skipna=True)


# In[87]:


df1=pd.DataFrame({"A":[1,5,3,4,2],"B":[3,2,4,3,4],"C":[2,2,7,3,4],"D":[4,3,6,12,7]},index=["A1","A2","A3","A4","A5"])


# In[88]:


sr=pd.Series([12,25,64,18],index=["A","B","C","D"])


# In[89]:


df2=pd.DataFrame({"A":[10,11,7,8,5],"B":[21,5,32,4,6],"C":[11,21,23,7,9],"D":[1,5,3,8,6]},index=["A1","A2","A3","A4","A5"])


# In[90]:


df1


# In[91]:


df2


# In[96]:


df1.subtract(sr,axis=1)


# In[93]:


df1


# In[94]:


df2


# In[97]:


df1.subtract(df2)


# In[98]:


df


# In[99]:


df.sum(axis=0)


# In[100]:


df=pd.read_csv("nba.csv")


# In[102]:


df.sum(axis=0,skipna=True)


# In[104]:


df.sum(axis=1,skipna=True)


# In[105]:


df2


# In[116]:


df2.swapaxes("index","columns")


# In[120]:


df=pd.DataFrame({"A":[10,11,7,8,5],"B":[21,5,32,4,6],"C":[11,21,23,7,9],"D":[1,5,3,8,6]},index=["A1","A2","A3","A4","A5"])


# In[121]:


df


# In[122]:


df.swapaxes("index","columns")


# In[129]:


df=pd.DataFrame({"A":[1,5+1j,3+.2j,4+1j,None],"B":[3,2,4,3,4],"C":["brook","daniela","samantha","hayden","nathan"],"D":[None,3,6,None,7]},index=["A1","A2","A3","A4","A5"])


# In[131]:


df.swapaxes("index","columns",copy=True)


# In[132]:


df


# In[140]:


df=pd.read_csv("nba.csv")


# In[134]:


df


# In[136]:


df.index=df.index*2


# In[137]:


df


# In[141]:


df.take([0,1,2],axis=1)


# In[142]:


df2


# In[143]:


df2.to_clipboard(sep=',')


# In[151]:


df=pd.DataFrame({"A":[1,5,3,4,2],"B":[3,2,4,3,4],"C":[2,2,7,3,4],"D":[4,3,6,12,7]},index=["A1","A2","A3","A4","A5"])


# In[152]:


df


# In[155]:


df.to_clipboard(excel=True)


# In[156]:


df


# In[165]:


df=pd.DataFrame({"A":[1,5+1j,3+.2j,4+1j,None],"B":[3,2,4,3,4],"C":["brook","daniela","samantha","hayden","nathan"],"D":[None,3,6,None,7]},index=["A1","A2","A3","A4","A5"])


# In[166]:


df


# In[168]:


df.to_dict(orient='series')


# In[ ]:




