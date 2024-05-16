#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
plt.show
plt.list


# In[52]:


get_ipython().system('dir mtcars.csv')


# In[53]:


get_ipython().system('dir')


# In[57]:


df=pd.read_csv("mtcars.csv")


# In[50]:


mtcars = pd.read_csv(r"C:\Users\CSD 61\Downloads\mtcars.csv")


# In[42]:


plt.hist(mtcars['mpg'], bins=10, color='pink', edgecolor='black')
plt.xlabel('Miles per gallon (mpg)')
plt.ylabel('Frequency')
plt.title('Histogram of Miles per gallon (mpg)')
plt.show()


# In[38]:


mtcars.head()


# In[60]:


df.columns


# In[39]:


mtcars.tail()


# In[40]:


mtcars.describe()


# In[43]:


mtcars.info()


# In[45]:


mtcars.shape

df.columns
# 
