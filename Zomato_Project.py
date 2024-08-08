#!/usr/bin/env python
# coding: utf-8

# # ZOMATO DATA ANLYSIS PROJECT

# In[ ]:


pandas is used for data manupulation and analysis
numpy is used for numerical operations
matplotlib.pyplot and seaborn are used for data visulization


# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Step-2 CREATE THE DATA-FRAME

# In[2]:


dataframe = pd.read_csv('Zomato data .csv') #read the csv file 


# In[3]:


print(dataframe)


# In[4]:


dataframe


# # CONVERT THE DATA TYPE OF COLOUMN-RATE

# In[5]:


def handleRate(value): #user defien funtion(handle-rate) in which we pass the ftn
    value = str(value).split('/') # data type is a sting it split the rate column
    value = value[0]; #we get the value on 0
    return float(value)

dataframe['rate'] = dataframe['rate'].apply(handleRate) # data frame coloumn "rate" and we apply the handle rate ftn
print(dataframe.head())


# In[8]:


dataframe.info()


# # 1) What type of resturant do the majority of customers order from?

# In[9]:


dataframe.head()


# In[10]:


sns.countplot(x = dataframe['listed_in(type)'])  # 100 (tell us the count) .list in type coloumn is the name of coloumn
plt.xlabel('type of resturant') # label type of resturant on x - axis


# # concluison - majority of the resturant falls in the dining catogary

# # 2) How many votes has each type of resturant have recieved?

# In[11]:


dataframe.head()


# In[12]:


grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum() # group data (varaible). group 2 coloumn which are listed_in(type) and votes and add themem
result = pd.DataFrame({'votes': grouped_data}) # insert group-data in pd=frame
plt.plot(result, c = 'black' , marker = 'o') # make plot and gave color 
plt.xlabel ('types of resturant' , c = 'red' , size = 20)
plt.ylabel('votes' , c = 'red' , size = 20) 


# # conclusion - dining resturant has recieved maximum votes

# # 3) What are the ratings that the majority of resturant have received?

# In[13]:


dataframe.head()


# In[15]:


plt.hist(dataframe['rate'],bins = 2) # bin show nbr of coloumn in histogram
plt.title('ratings distribution')
plt.show()


# # conclusion - the majority resturant received ratings from 3.4 to 4

# # 4) Zomato has observed that the most couples order most of their food online. What is their average
# spending on each order?
# 

# In[16]:


dataframe.head()


# In[17]:


couple_data = dataframe['approx_cost(for two people)']
sns.countplot(x = couple_data)


# # conclusion - the majority of couples prefer resturants with an approximate cost of 300 rupess

# # 5) Which mode (online or offline) has that maximum rating?

# In[18]:


plt.figure(figsize = (6,6)) # set the figure size
sns.boxplot(x = 'online_order' , y = 'rate' , data = dataframe) 


# # conclusion - offline order recieve lower rating in comprasion to online rating

# In[ ]:




