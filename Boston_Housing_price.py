#!/usr/bin/env python
# coding: utf-8

# In[20]:


import os
import tarfile


# In[21]:


from six.moves import urllib


# In[22]:


DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"


# In[23]:


HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


# In[26]:


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


# In[34]:


import pandas as pd
fetch_housing_data()


# In[28]:


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


# In[35]:


df=load_housing_data()


# In[37]:


df.head


# In[38]:


df.columns


# In[39]:


df.shape


# In[42]:


df.info()


# In[45]:


df['ocean_proximity'].value_counts()


# In[47]:


# for categorical or similar attribute we can actually count the frequency of each type using value_counts() function


# In[48]:


df.describe()


# In[49]:


# plotting the numerical attributes on histogram


# In[50]:


import matplotlib.pyplot as plt


# In[54]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[55]:


df.hist(bins=50,figsize=(20,15))


# In[53]:


df['total_bedrooms'].describe()


# In[56]:


df['median_income']


# In[61]:


def split_train_test(data,test_ratio):
    shuffled_index=np.random.permutation(len(data))
    test_set_size=int(len(data)*test_ratio)
    test_set=shuffled_index[:test_set_size]
    train_set=shuffled_index[test_set_size:]
    return data.iloc[train_set],data.iloc[test_set]


# In[63]:


train_data,test_data=split_train_test(df,0.2)


# In[64]:


len(train_data)+len(test_data)


# In[65]:


len(df)


# In[66]:


from sklearn.model_selection import train_test_split


# In[68]:


train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)


# In[ ]:




