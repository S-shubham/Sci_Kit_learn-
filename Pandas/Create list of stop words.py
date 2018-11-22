#!/usr/bin/env python
# coding: utf-8

# In[32]:


fread=open("StopWords_Generic.txt","r")


# In[33]:


# Create a list to store the stop words
li=[]


# In[34]:


for line in fread:
    line=line.rstrip('\n')
    li.append(line)


# In[36]:


li


# In[37]:


fread1=open("StopWords_Geographic.txt","r")


# In[38]:


li1=[]


# In[39]:


for line in fread1:
    line=line.rstrip('\n')
    li1.append(line)


# In[40]:


li1


# In[41]:


# REAding another set of stopwords


# In[42]:


fread2=open("StopWords_GenericLong.txt","r")


# In[43]:


li2=[]


# In[44]:


for line in fread2:
    line=line.rstrip('\n')
    li2.append(line)


# In[45]:


li2


# In[46]:


fread3=open("StopWords_DatesandNumbers.txt","r")


# In[47]:


li3=[]


# In[48]:


for line in fread3:
    line=line.rstrip('\n')
    li3.append(line)


# In[49]:


li3


# In[50]:


fread4=open("StopWords_Currencies.txt","r")


# In[51]:


li4=[]


# In[52]:


for line in fread4:
    line=line.rstrip('\n')
    li4.append(line)


# In[53]:


li4


# In[54]:


fread5=open("StopWords_Auditor.txt","r")


# In[55]:


li5=[]


# In[56]:


for line in fread5:
    line=line.rstrip('\n')
    li5.append(line)


# In[57]:


li5


# In[67]:


# All the stopwords has been succesffully read now
# Combine all the stop words into a single list
stop_words=li+li1+li2+li3+li4+li5


# In[68]:


if len(stop_words) == len(li)+len(li1)+len(li2)+len(li3)+len(li4)+len(li5):
    print("Successfully Merged")


# In[70]:


# Now we have successfully created the list of stop words.


# In[ ]:




