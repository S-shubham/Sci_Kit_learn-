#!/usr/bin/env python
# coding: utf-8

# In[1]:


# write a function to remove '@sth' form each string


# In[2]:


def remove_handle(st):
    for i in range(len(st)):
        if st[i]==' ':
            st=st[i+1:]
            break
    return st
        


# In[3]:


a= '@mindi heya! all it was a blast at the party'
b= '@niki_24your I gotch u girl keep shaking those booty :)'


# In[4]:


print(remove_handle(a))


# In[5]:


print(remove_handle(b))


# In[ ]:




