#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # DATA

# In[25]:


df=pd.read_excel('TRANSPORT_DATA.xlsx')
df.head()


# # DATA PREPARATION AND CLEANING 

# In[26]:


df.info()


# In[28]:


df.columns


# In[14]:


df.dtypes


# In[29]:


print('columns with missing value :',df.columns[df.isnull().any()].tolist())
print()
missing=df.isnull().sum() 

print(f'{missing.idxmax()} column has maximum missing value with {missing.max()} missing value')


# # CATEGORICAL COLUMNS

# In[30]:


df.select_dtypes(include="object").columns


# # NUMERICAL COLUMNS

# In[31]:


df.select_dtypes(exclude="object").columns


# In[32]:


df.describe()


# In[34]:


df.isnull().sum()


# In[35]:


df.county_name.fillna('Not Mentioned',inplace=True)
# dropping other nulls
df.dropna(inplace=True)


# # FILLING NULL VALUES

# In[36]:


df.isnull().sum()


# # STORING INTO SQL FOR FUTURE REFERENCES:
# 

# In[22]:


from sqlalchemy import create_engine


# In[23]:


lot_3=create_engine('mysql+pymysql://root:yuvaraj143@localhost/Hotel')
df.to_sql('Public_transport_data',lot_3,index=False)


# #                    EXPLORATORY DATA ANALYSIS & VISUALIZATION:
# 

# In[53]:


df.head()


# In[38]:


df['county_name'].value_counts(normalize = True)[:10]


# In[42]:


plt.figure(figsize=(12,6), dpi=110)

sns.countplot(data=df, x='county_name',order=pd.value_counts(df['county_name']).iloc[:10].index,
              palette='colorblind')

plt.title('Top 10 Countries of Origin ', weight='bold')
plt.xlabel('Country Names')
plt.ylabel('Transportation')


# In[54]:


trans_released = df.groupby('geotypevalue')[['geoname']].count()
trans_released


# In[60]:


plt.figure(figsize=(16,8))

plt.plot(trans_released.geoname, 'o--g')


plt.xlabel('Year')
plt.ylabel('Number of Games Released')
plt.title('Total Number of Games Released per year');


# In[65]:


plt.figure(figsize=(18,5))

sns.boxplot(x='pop_total',y='percent_se',hue='county_name',data=df)


# In[61]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




