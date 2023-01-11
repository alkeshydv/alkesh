#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[3,5,8]])


# In[6]:


#horizontal
c=np.hstack((a,b))
c


# In[9]:


#vertical
d=np.vstack((a,b))
d


# In[12]:


#range
e=np.arange(1,13)
e


# In[15]:


r=np.arange(13,140,13)
r


# In[19]:


#linspace
t=np.linspace(0,5,num=20)
t


# In[21]:


#indexing and slicing
u=np.array([[1,2,3],[4,5,6]])
u


# In[24]:


u.size


# In[26]:


#to slice first row
u[0]


# In[30]:


#to slice second row
u[1]


# In[33]:


u[0:1]


# In[35]:


u[:,0]


# In[37]:


u[:,2]


# In[39]:


u[1][2]


# In[42]:


i=np.ones((4,4))
i


# In[44]:


i=np.eye(5)
i


# In[47]:


u=+2
u


# In[49]:


k=np.array([[1,2,3],[4,5,6]])
k


# In[53]:


k += 2
k


# In[55]:


k.min()


# In[58]:


p=np.random.randint(11,545,size=(3,4))
p


# In[60]:


p.max()


# In[62]:


p.reshape(6,2)


# In[64]:


l=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
l


# In[66]:


l[0:2]


# In[ ]:




