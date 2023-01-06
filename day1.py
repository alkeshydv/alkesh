#!/usr/bin/env python
# coding: utf-8

# In[2]:


q=[[[1,2,3,4],[5,6,7,8],[7,8,9,0],[1,2,4,5]]]
print(q)


# In[4]:


type(q)


# In[8]:


w=np.array(q)


# In[10]:


import numpy as np


# In[13]:


w=np.array(q)
print(w)


# In[15]:


type(w)


# In[17]:


w.size


# In[19]:


w.ndim


# In[21]:


w.itemsize


# In[23]:


e=np.zeros((2,4))
print(e)


# In[25]:


r=np.zeros((5,7))
print(r)


# In[27]:


t=np.zeros((5,7))
print(r.ndim)


# In[31]:


t=np.full((4,5),69)
t


# In[34]:


y=np.random.rand(5,6)
y


# In[36]:


u=np.ones((5,6))
u


# In[38]:


i=np.eye(5)
i


# In[42]:


w.size


# In[44]:


w.shape


# In[46]:


w.dtype


# In[48]:


np.copy(w)


# In[54]:


w.sort()
w


# In[56]:


w.sort(axis=1)
w


# In[59]:


w.shape


# In[61]:


r=w.reshape(4,4,1)
r


# In[ ]:




