#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[47]:


df=pd.read_csv("nba.csv")


# In[18]:


ind=pd.date_range('01/01/2000',periods=8,freq='30T')


# In[19]:


df=pd.DataFrame({"A":[1,2,3,4,5,6,7,8],"B":[10,20,30,40,50,60,70,80]},index=ind)


# In[20]:


df


# In[28]:


df.between_time('02:00','03:30',include_start=False,include_end=False)


# In[27]:


df.between_time('01:00','06:00')


# In[42]:


df=pd.DataFrame({"A":[None,1,2,3,None,None],"B":[11,5,None,None,None,8],"C":[None,5,10,11,None,8]})


# In[43]:


df


# In[44]:


df.bfill(axis='columns')


# In[45]:


df.bfill(axis='rows')


# In[46]:


df


# In[48]:


df


# In[76]:


df=pd.DataFrame({"A":[5,8,12,9,5,3],"B":[1,4,6,4,11,3],"C":[11,4,8,7,3,2]})


# In[50]:


df


# In[51]:


df.clip(-4,9)


# In[57]:


lower_limit=pd.Series([1,-3,2,3,-2,-1])


# In[55]:


df.clip(limit,limit+5,axis=0)


# In[56]:


df.clip(limit,limit+5,axis=1)


# In[58]:


upper_limit=lower_limit+5


# In[59]:


upper_limit


# In[60]:


lower_limit


# In[61]:


df.clip(lower_limit,upper_limit,axis=0)


# In[63]:


df2=df.copy()


# In[64]:


df2


# In[65]:


df=df.abs()


# In[66]:


df


# In[69]:


df.clip_lower(100)


# In[75]:


df.clip_lower(np.array([[1,2,3],[10,12,3],[1,4,3],[1,2,3],[1,2,3],[1,2,3]]))


# In[74]:


df


# In[106]:


df=pd.DataFrame({"A":[-5,8,12,-9,5,3],"B":[-1,-4,6,4,11,3],"C":[11,4,-8,7,3,-2]})


# In[86]:


df


# In[87]:


df.clip_upper(8)


# In[83]:


limit=np.array([[10,2,8],[3,5,3],[2,4,6],[11,2,3],[5,2,3],[4,5,3]])


# In[89]:


df.clip_upper(limit)


# In[88]:


limit


# In[91]:


df.compound(axis=1)


# In[93]:


df.index=df.index*3


# In[94]:


df


# In[99]:


dk=df.copy(deep=True)


# In[100]:


dk


# In[101]:


dk=dk*2


# In[102]:


df


# In[103]:


dk


# In[117]:


df


# In[118]:


dk=df.copy(deep=False)


# In[119]:


dk


# In[120]:


dk=dk*2


# In[121]:


dk


# In[122]:


df


# In[130]:


df[:3]=df[:3]/6


# In[124]:


df


# In[125]:


dk


# In[127]:


df is dk


# In[128]:


dk is df


# In[131]:


df


# In[132]:


df is dk


# In[133]:


dk=df.copy(deep=True)


# In[134]:


dk is df


# In[135]:


df is dk


# In[136]:


a=pd.Series([1,2,3])


# In[137]:


a


# In[138]:


aa=a.copy(deep=False)


# In[139]:


aa is a


# In[140]:


a is aa


# In[141]:


dc=df


# In[142]:


df


# In[144]:


dc=dc*2


# In[145]:


df


# In[146]:


dc


# In[147]:


df


# In[150]:


dc=df.copy(deep=False)


# In[151]:


dc.values is df.values


# In[152]:


a=pd.DataFrame({"A":[1,2,3],"C":[4,5,6]})


# In[153]:


a


# In[154]:


b=a


# In[155]:


a=a*5


# In[156]:


a


# In[157]:


b


# In[ ]:




