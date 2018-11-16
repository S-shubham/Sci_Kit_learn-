#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[17]:


df=pd.DataFrame({"A":[-5,8,12,None,5,3],"B":[-1,None,6,4,None,3],"C":["sam","haris","alex",np.nan,"peter","nathan"]})


# In[18]:


df


# In[19]:


df.count(axis=0)


# In[20]:


df.count(axis=1)


# In[23]:


dfa=df[['A','B']]


# In[24]:


dfa


# In[26]:


dfa.corr(method='pearson')


# In[27]:


dfa.corr(method='spearman')


# In[28]:


dfa.corr(method='kendall')


# In[29]:


ok=pd.read_csv("nba.csv")


# In[32]:


ok.corr(method='pearson')


# In[33]:


ok.corr(method='kendall')


# In[34]:


ok.corr(method='spearman')


# In[35]:


df1=pd.DataFrame({"A":[1,5,7,8],"B":[5,8,4,3],"C":[10,4,9,3]})


# In[36]:


df2=pd.DataFrame({"A":[5,3,6,4],"B":[11,2,4,3],"C":[4,3,8,5]})


# In[37]:


df1


# In[38]:


df2


# In[39]:


df1.corrwith(df2,axis=0)


# In[40]:


df1.corrwith(df2,axis=1)


# In[87]:


dff=pd.DataFrame({"A":[5,3,None,4],"B":[None,2,4,3],"C":[4,3,8,5],"D":[5,4,2,None]})


# In[51]:


df


# In[52]:


df.cov()


# In[53]:


df


# In[54]:


df3


# In[57]:


d


# In[56]:


df3


# In[58]:


df


# In[67]:


df.cummin(skipna=True)


# In[64]:


df3


# In[66]:


df3.cummin(axis=1)


# In[69]:


df3


# In[73]:


df3.cumprod()


# In[74]:


df3.cumprod(axis=1)


# In[75]:


df.cumprod(axis=0,skipna=True)


# In[76]:


df3


# In[83]:


df3.diff(axis=0)


# In[79]:


df3.diff(periods=2)


# In[80]:


df3


# In[84]:


df3.diff(axis=1,periods=1)


# In[85]:


df=df3


# In[86]:


df.div(2)


# In[88]:


dff=pd.DataFrame({"A":[5,3,None,4],"B":[None,2,4,3],"C":[4,3,8,5],"D":[5,4,2,None]})


# In[90]:


df.div([2,3,4,1.5],axis=1)


# In[91]:


dff


# In[92]:


dff.div(2,fill_value=50)


# In[93]:


series_object=pd.Series([2,3,1.5,4])


# In[94]:


series_object


# In[102]:


df.div(series_object,axis=0)


# In[97]:


dff


# In[101]:


df


# In[100]:


df=pd.DataFrame({"A":[5,3,6,4],"B":[11,2,4,3],"C":[4,3,8,5],"D":[5,4,2,8]})


# In[103]:


a=pd.DataFrame({"A":[1,2],"B":[2,3]})


# In[104]:


a


# In[107]:


b=pd.DataFrame({"A":[2,4],"B":[1,3]})


# In[108]:


a.dot(b)


# In[109]:


b


# In[110]:


a.shape


# In[111]:


b.shape


# In[113]:


a.eq(b)


# In[114]:


a


# In[115]:


b


# In[117]:


df


# In[118]:


ck=pd.Series([11,3,4,8])


# In[128]:


df.eq(ck,axis=0)


# In[123]:


a.iloc[1,1]=3


# In[124]:


a


# In[125]:


a.eq(b)


# In[129]:


b.eq(3)


# In[136]:


dff.eq(ck,axis=0)


# In[134]:


ck


# In[137]:


a


# In[148]:


b.iloc[1,0]=np.nan


# In[149]:


b


# In[150]:


a.equals(b)


# In[151]:


a.iloc[0,0]=2


# In[152]:


a.iloc[0,1]=1


# In[153]:


a


# In[154]:


b


# In[155]:


a.equals(b)


# In[156]:


pd.Series([1,2]).equals(pd.Series([1,2]))


# In[161]:


a=pd.DataFrame({"A":[1,2,3],"B":[4,5,None],"C":[7,8,9]})


# In[160]:


b=pd.DataFrame({"A":[1,2,3],"B":[4,5,None],"C":[7,8,9]})


# In[162]:


a.equals(b)


# In[163]:


df1


# In[164]:


df2


# In[165]:


df1.equals(df2)


# In[166]:


a


# In[167]:


b


# In[168]:


a.equals(b)


# In[170]:


from numpy.random import randn


# In[171]:


from pandas import DataFrame


# In[174]:


np.random.seed(10)


# In[175]:


df = DataFrame(randn(10, 2), columns=list('ab'))


# In[176]:


df


# In[177]:


df.eval('a + b')


# In[180]:


df.eval('c = a + b')


# In[179]:


df.iloc[2,1]=None


# In[183]:


df1.eval('D=A+B+C',inplace=True)


# In[184]:


df1


# In[185]:


a


# In[186]:


a.eval('D = B+C',inplace=True)


# In[187]:


a


# In[191]:


dff


# In[193]:


dff.ffill(axis=1)


# In[194]:


df=pd.read_csv("nba.csv")


# In[195]:


df


# In[196]:


df.filter(["Name","College","Salary"])


# In[200]:


df.filter(regex='[aA]')


# In[201]:


dff


# In[203]:


dff.first_valid_index()


# In[204]:


a


# In[205]:


a.first_valid_index()


# In[206]:


aa=pd.Series([None,None,1,2,5])


# In[207]:


aa.first_valid_index()


# In[211]:


bkk=dff[["B","C"]]


# In[212]:


bkk


# In[213]:


bkk.first_valid_index()


# In[214]:


bkk.iloc[0,1]=None


# In[215]:


bkk.first_valid_index()


# In[232]:


df=pd.DataFrame({"A":[None,None,2,4,5],"B":[None,None,None,44,2],"C":[None,None,None,1,5]})


# In[233]:


df


# In[234]:


df.first_valid_index()


# In[235]:


df=pd.Series([None,None,"sam","alex","sophia",None])


# In[236]:


df


# In[237]:


df.first_valid_index()


# In[239]:


df1


# In[240]:


df1.floordiv(2)


# In[246]:


sr=pd.Series([2,1,3,1])


# In[247]:


sr


# In[248]:


df1.floordiv(sr,axis=0)


# In[249]:


df=pd.DataFrame({"A":[5,3,6,4],"B":[11,None,4,3],"C":[4,3,8,None],"D":[5,4,2,8]})


# In[250]:


df


# In[252]:


df.floordiv(sr,fill_value=50)


# In[253]:


df1


# In[254]:


df=pd.DataFrame({"A":[5,3,6,4],"B":[11,2,4,3],"C":[4,3,8,5],"D":[5,4,2,8]})


# In[255]:


df


# In[257]:


df.floordiv(sr,axis=0)


# In[ ]:




