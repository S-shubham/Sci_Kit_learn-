#!/usr/bin/env python
# coding: utf-8

# In[38]:


# In sci-kit learn input is alwasy type_Casted to float64


# In[39]:


# for regression problem sci_kit casts the target to float64
# but it leaves the classification problem as it is 


# In[40]:


from sklearn import datasets


# In[42]:


from sklearn.svm import SVC


# In[43]:


iris=datasets.load_iris()


# In[45]:


clf=SVC(gamma='scale')


# In[46]:


clf.fit(iris.data,iris.target)


# In[51]:


a=list(clf.predict(iris.data[:3]))


# In[54]:


a[0].dtype


# In[48]:


# now an example of strig


# In[49]:


clf.fit(iris.data,iris.target_names[iris.target])


# In[53]:


b=list(clf.predict(iris.data[:3]))


# In[55]:


b


# In[ ]:


# it can be clearly seen that 

