#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("D:/Data Visulatiation/Covi19.csv")


# In[8]:


df


# In[9]:


df.head()


# In[10]:


df


# In[13]:


print(df.shape)


# In[14]:


print(df.columns)


# In[15]:


print(df.dtypes)


# In[16]:


print(df.info())


# In[17]:


print(df.columns)


# In[20]:


Country_df = df['Country']
Country_df


# In[21]:


print(Country_df.head())


# In[23]:


Confirmed_df = df['Confirmed']
Confirmed_df


# In[24]:


print(Confirmed_df.head())


# In[28]:


print(Country_df.tail())


# In[29]:


df.columns


# In[34]:


subset = df[['Date','Country','Confirmed','Recovered']]
print(subset.head())


# In[36]:


subset2 = df[['Date','Confirmed','Recovered','Deaths']]
print(subset2.head())


# In[37]:


print(subset2.tail())


# In[38]:


print(df.loc[0])


# In[40]:


print(df.loc[1])


# In[41]:


print(df.loc[99])


# In[42]:


print(df.loc[1613])


# In[48]:


print(df.tail(n=1))


# In[49]:


print(df.loc[[0,99,999]])


# In[50]:


print(df.iloc[1])


# In[51]:


print(df.iloc[[0,99,999]])


# In[52]:


print(df.iloc[-1])


# In[53]:


print(df.iloc[0:10])


# In[54]:


subset2 = df.loc[:,['Country','Confirmed']]
print(subset2.head())


# In[61]:


subset3 = df.iloc[:,[2,4,-1]]
subset3


# In[71]:


small_range = list(range(0,5))
print(small_range)


# In[72]:


subset4 = df.iloc[:,small_range]
print(subset4.head())


# In[73]:


print(df.loc[42,'Country'])


# In[75]:


print(df.iloc[42,0])


# In[78]:


print(df.iloc[[0,99,999],[0,3,4]])


# In[81]:


#if we use the columns names directly,
#it makes the code a bit easier to read
#note now we haev to use loc,instead of iloc

print(df.loc[[0,99,999],['Recovered','Deaths','Confirmed']])


# In[82]:


print(df.loc[10:13],['Country','Deaths','Confirmed'])


# In[83]:


print(df.head(n=10))


# In[89]:


print(df.groupby('Country')['Confirmed'].mean())
#Expectancey


# In[96]:


multi_group_var = df.groupby(['Date','Confirmed'])[['Deaths','Recovered']].mean()
multi_group_var


# In[99]:


#if you need to "flatten" the dataframe,you can use the
#reset_index method.
flat = multi_group_var.reset_index()
flat.head(n=16)


# In[100]:


#Grouped Frequencey Counts
#use the nunique to get counts of unique values on a Pandas Series

print(df.groupby('Country')['Recovered'].nunique())


# In[103]:


#Basic plot
global_covid19_data = df.groupby('Country')['Confirmed'].mean()
print(global_covid19_data)


# In[107]:


#just plot it into simple graph by
#the use of matplotlib.pyplots packages

global_covid19_data.plot()


# # Methods of visual presentation of data
# #Visual Representation of the Data
# #1. Histogram -- vertical bar chart frequencies
# #2. frequencey polygon-- line graph of frequencies
# #3. Ogive -- line graph of cumulative frequencies
# #4. Pie Chart -- proportion representation for categories of a whole
# #5. Stem and Leaf Plot
# #6.Pareto Chart
# #7. Scatter plot
# 

# # Priciples of Excellent Graphs
# 
# #The graph should not disort the data
# #The graph should not contain unnecessary adornments (sometimes refferd to as chart junk)
# #The scale on the verticle axis should begin at zero
# #All axes should be properly labeled
# #the graph contain a title
# #The simplest possible graph should be used for a given set of data
# 

# # Measure of Central Tendency
# """
# Measure of Centrak tendency yield information about "particular places or 
# locations in as group of numbers."
# A single number to describe the Chacteristics of a set of data
# """
# # Central tendency of measure of location
# #1. Arithmetic mean
# #2. Weighted mean
# #3. Median
# #4. Percentile
# 
# # Dispersion
# 
# #1. Skewness
# #2. Kurtosis
# #3. Range
# #4. Interquartile range
# #5. Variance
# #6. Stadard score
# #7. Coefficient of variation
# 
# 
# 
# 
# 

# In[ ]:




