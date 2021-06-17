#!/usr/bin/env python
# coding: utf-8

# <h1>Project 1: Performing Analysis of Meteorological Data<h1>
#    ~ <b>Ankita Komal</b>
#     

# <h2>Problem Statement: To transform the raw data into information and then convert it into knowledge.<h2>

# The dataset has hourly temperature recorded for last 10 years starting from 2006-04-01
# 00:00:00.000 +0200 to 2016-09-09 23:00:00.000 +0200. It corresponds to Finland, a country in
# the Northern Europe. 

# <b>Importing all python libraries</b>

# In[30]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


# <b>Importing weatherhistory dataset</b>

# In[13]:


data=pd.read_csv('C:/Users/Ankita/Desktop/weatherHistory.csv')


# In[14]:


data.shape


# In[15]:


data.head() #used to get the 1st n rows


# <b>For analysing we are using correlation heatmap as it is ideal for data analysis since it makes patterns easily readable and highlights the differece and vaiation in the data.
# for mor information about correlation heatmap check https://www.geeksforgeeks.org/how-to-create-a-seaborn-correlation-heatmap-in-python/#:~:text=The%20data%20here%20has%20to,kaggle.com%20is%20being%20used.</b>

# In[28]:


sns.heatmap(data.corr())


# In[18]:


plt.figure(figsize=(10,10))
plt.plot(data['Temperature (C)'])
plt.plot(data['Humidity'])
plt.legend(['Temperature (C)','Humidity'])


# In[19]:


plt.figure()
plt.plot(data['Humidity'])


# In[20]:


cols_plot = ['Apparent Temperature (C)', 'Humidity']

axes = data[cols_plot].plot(marker='.', alpha=0.5, linestyle='None', figsize=(15, 16), subplots=True)
for ax in axes:
    ax.set_ylabel('Hourly Totals')


# In[21]:


import matplotlib.dates as mdates
fig, ax = plt.subplots(figsize=(10,8))
# ax.plot(weather_monthly_mean['Temperature (C)'], color='black', label='Temperature')

ax.plot(data['Apparent Temperature (C)'], color='red', label='Apparent Temperature')

ax.plot(data['Humidity'], color='blue', label='Humidity')

#data[['Apparent Temperature (C)', 'Humidity']].plot.area(ax=ax, linewidth=0)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.legend()
ax.set_ylabel('Monthly Total Temperature');


# In[22]:


data_columns = ['Temperature (C)', 'Apparent Temperature (C)', 'Humidity']


# Resample to weekly frequency, aggregating with mean
weather_monthly_mean = data[data_columns].mean()
weather_monthly_mean.tail(20)


# In[23]:


data.describe()


# In[24]:


data[data_columns].head()


# In[25]:


y = data['Formatted Date'][:80]
x1 = data['Temperature (C)'][:80]
x2 = data['Humidity'][:80]
fig = plt.figure(figsize=(10,10))
ax = fig.add_axes([0,0,1,1])
l1 = ax.plot(y,x1,'ys-') # solid line with yellow colour and square marker
l2 = ax.plot(y,x2,'go--') # dash line with green colour and circle marker
ax.legend(labels = ('Temp', 'Humidity'), loc = 'lower right') # legend placed at lower right
ax.set_title("DataStatus")
ax.set_ylabel('Monthly temp total')
ax.set_xlabel('Date')
ax.axis('off')


# In[26]:


y = data['Formatted Date'][96400:]
x1 = data['Temperature (C)'][96400:]
x2 = data['Humidity'][96400:]
fig = plt.figure(figsize=(10,10))
ax = fig.add_axes([0,0,1,1])
l1 = ax.plot(y,x1,'ys-') # solid line with yellow colour and square marker
l2 = ax.plot(y,x2,'go--') # dash line with green colour and circle marker
ax.legend(labels = ('Temp', 'Humidity'), loc = 'lower right') # legend placed at lower right
ax.set_title("DataStatus")
ax.set_ylabel('Monthly temp total')
ax.set_xlabel('Date')
ax.axis('off')

