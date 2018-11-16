#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


df=pd.read_csv("nba.csv")


# In[11]:


df.get_value(4,0,takeable=True)


# In[8]:


df.get_value(10,'Salary')


# In[9]:


df


# In[13]:


dd=df.groupby('Team')


# In[15]:


print(dd)


# In[16]:


df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                     'B' : ['one', 'one', 'two', 'three',
                           'two', 'two', 'one', 'three'],
                       'C' : np.random.randn(8),
                       'D' : np.random.randn(8)})


# In[17]:


df


# In[20]:


grouped = df.groupby(['A','B'])


# In[21]:


grouped


# In[22]:


df


# In[23]:


grouped.first()


# In[25]:


grouped.last()


# In[26]:


daf=pd.read_csv("nba.csv")


# In[31]:


gk=daf.groupby('Team')


# In[ ]:





# In[30]:


gk.get_group('Boston Celtics')


# In[29]:


gk.last()


# In[32]:


gk.first()


# In[33]:


gkk=daf.groupby(['Team','Position'])


# In[34]:


gkk.first()


# In[36]:


df=daf


# In[38]:


df.hist('Salary')


# In[49]:


tp=pd.DataFrame({"A":[4,5,2,6],"B":[11,2,5,8],"C":[1,8,66,4]})


# In[51]:


tp


# In[50]:


tp.idxmin(axis=0)


# In[44]:


tp


# In[45]:


df=pd.DataFrame({"A":[4,5,2,None],"B":[11,2,None,8],"C":[1,8,66,4]})


# In[46]:


df


# In[52]:


df.idxmin(axis=1,skipna=True)


# In[54]:


df=pd.DataFrame({"A":[4+2j,5,2,6],"B":[11,2,5,8],"C":[1,8,66,4]})


# In[55]:


df


# In[67]:


df=pd.DataFrame({"A":["sofia",5,8,11,100],"B":[2+2j,8,77,4,11],"C":["amy",11,4,6,9]})


# In[68]:


df


# In[69]:


df.info()


# In[70]:


df_new=df[1:]


# In[71]:


df_new


# In[72]:


df_new.info()


# In[78]:


df_new=df_new.infer_objects()


# In[79]:


df_new.info()


# In[80]:


df_new


# In[81]:


df=pd.read_csv("nba.csv")


# In[82]:


df.info()


# In[85]:


df.info(verbose=False)


# In[89]:


df.info(max_cols=8)


# In[92]:


df.info()


# In[93]:


df.info(null_counts=False)


# In[ ]:




