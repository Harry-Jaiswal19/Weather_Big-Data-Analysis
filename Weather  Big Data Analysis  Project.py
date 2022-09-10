#!/usr/bin/env python
# coding: utf-8

# # # # WEATHER DATASET BIG DATA ANALYSIS # # #
# 
# This dataset is in CSV format and we will solve this dataset using pandas dataFrame.
# 

# In[3]:


import pandas as pd


# In[4]:


#reading the CSV file through the pandas read command.
df = pd.read_csv(r"E:\MY  Data analytics project\Weather Data.csv")


# In[5]:


#printing the  imported dataset. 
df


# In[6]:


#show the first 10 rows in the data frame.
df.head(10)


# In[7]:


#printing the shape of the dataframe.
df.shape


# In[8]:


#Printing the index of the dataframe.
df.index


# In[12]:


#showing all the columns name which is present in the dataframe.
df.columns


# In[13]:


#Printing the data type of the dataframe.
df.dtypes


# In[14]:


#printing Unique value in the data frame
df["Weather"].unique()


# In[15]:


df.nunique()


# In[16]:


df.count()


# In[17]:


df.count


# In[18]:


df["Weather"].value_counts()


# In[19]:


df.info()


# In[20]:



df["Wind Speed_km/h"].nunique()


# In[21]:


df["Wind Speed_km/h"].unique()


# In[22]:


df.head(2)


# In[23]:


df.Weather.value_counts()


# In[24]:


df[df.Weather=="Clear"]


# In[25]:


df.groupby("Weather").get_group("Clear").head(10)


# In[26]:


df[df["Wind Speed_km/h"]==4].head(10)


# In[29]:


df[(df["Wind Speed_km/h"]==4)& (df["Weather"]=="Snow")]


# In[30]:


df[(df["Visibility_km"]>24) |(df["Weather"]=="Snow")]


# In[ ]:




