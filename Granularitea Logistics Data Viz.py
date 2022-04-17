#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This python script will be to figure how to group data for the excel I am using C:\Users\willi\Documents\GranulariTea Data\US_JP_EU_CH_2015_2019_1.xlsx


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


TeaYear = pd.read_excel(r'C:\Users\willi\Documents\GranulariTea Data\US_JP_EU_CH_2015_2019_1.xlsx', index_col = 0)


# In[5]:


TeaYear_df = pd.DataFrame(data = TeaYear)


# In[6]:


TeaYear_df


# In[7]:


TeaYear_df.columns


# In[8]:


groupedTY_df = TeaYear_df.groupby("Year")


# In[9]:


maxTY_df = groupedTY_df.max()


# In[10]:


maxTY_df = maxTY_df.reset_index()


# In[11]:


print(maxTY_df)


# In[12]:


maxTY_df = maxTY_df.drop(columns = ['Trade Flow','Qty'])


# In[13]:


maxTY_df.rename(columns = {'Trade Value (US$)':'tradeValue_USD'}, inplace = True)


# In[14]:


maxTY_df


# In[21]:


plt.plot(maxTY_df.Year, maxTY_df.tradeValue_USD, linestyle = 'solid')
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.title('Black Tea Imports 2015-2019')
plt.xlabel('Year')
plt.ylabel('Trade Value USD')
plt.savefig('Black_Tea_Imports_2015_2019.png')


# In[ ]:




