
# coding: utf-8

# In[ ]:


#2020 is an unusual year. A kind of novel coronavirus is spreading the whole globe. 
#I collected the raw data from official news about the confirmed cases in the United States. 
#The data is imcompleted and has some missing values due to privacy policy.

#The file has 8 feature columns:
#Case_Id: number ID of confirmed case in US.
#Date: the dates of the confirmed cases.
#City: the city of the confirmed case.
#State: the state of confirmed case. 
#California included the cases from Diamond Princess cruise returnees and Wuhan Chartered-flight returnees.
#Gender: have missing values
#Age: have missing values.
#Details: Spreading information
#Origin: 'Person' means person to person spread case.


# In[29]:


import pandas as pd
import numpy as np 
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
# Plot the Figures Inline
get_ipython().run_line_magic('matplotlib', 'inline')


# In[30]:


data=pd.read_csv(r'C:\Users\ludai\Desktop\Coronavirus_Data_USA.csv')
data.head()


# In[31]:


#check each column's data type
data.dtypes


# In[32]:


#Finding the null values
print(data.isnull().sum())


# In[33]:


data.describe(include='all')


# In[34]:


data.Date.describe()
# the 44 confirmed cases on 2/25 were from Princess cruise. 


# In[35]:


data.columns


# In[36]:


# Cumulative confirmed cases by date
import plotly.express as px
fig = px.line(data, x='Date', y='Case_Id')
fig.show()


# In[37]:


# Daily confirmed cases
plt.figure(figsize=(15,4))
plt.plot(data['Date'].value_counts().sort_index())


# In[38]:


data.Origin.describe() # Summary origin of cases. 44 confirmed cases came from Princess cruise.


# In[39]:


# create a figure and axis 
fig, ax = plt.subplots() 
# count the occurrence of each class 
data = data['Origin'].value_counts()
# get x and y data 
Origin = data.index 
Numbers = data.values 
# create bar chart for origins of confirmed cases
ax.bar(Origin, Numbers) 
# set title and labels 
ax.set_title('Origin of Cases') 
ax.set_xlabel('Origin') 
ax.set_ylabel('Numbers')


# In[40]:


# Confirmed cases by states


# In[41]:


df=pd.read_csv(r'C:\Users\ludai\Desktop\Coronavirus_Data_USA.csv')
df = df['State'].value_counts().rename_axis('States').reset_index(name='Confirmed_Case')
print (df)
fig = px.choropleth(df,locations="States",locationmode="USA-states", color="Confirmed_Case", 
                    color_continuous_scale=px.colors.sequential.Plasma, scope="usa")
fig.show()


# In[ ]:


# Data will be updated.
# Let's pull tegether to defeat the new coronavirus!

