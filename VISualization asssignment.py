#!/usr/bin/env python
# coding: utf-8

# ## ASSIGNMENT- 04
# 
# ## DATA VISUALIZATION

# In[1]:


#Load Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# ## LOADING DATA

# In[7]:


investementdata = pd.read_csv('India Investments.csv')
investementdata.head()


# ## CHECKING DATATYPES

# In[11]:


investementdata.info()


# ## CHECKING DATA SIZE

# In[12]:


investementdata.shape


# In[13]:


investementdata.isnull().sum()


# In[16]:


round(100*(investementdata.isnull().sum()/len(investementdata.index)),2)


# ## DROPPING MAXIMUM NULL VALUES

# In[17]:


investementdata.drop(['State Investment/Variety Notes','Partnership'],axis =1 ,inplace= True)


# ## DATA STASTICS

# In[18]:


investementdata.describe()


# ## DOWNLOADING CLEAN DATASET

# In[21]:


investementdata.to_csv('IndiaInvestments.csv')


# In[ ]:




