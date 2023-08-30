#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("mckinsey.csv")


# In[3]:


df.shape


# In[4]:


type(df)


# In[5]:


df["country"]


# In[6]:


df.head()


# In[7]:


df.tail()


# In[8]:


df.describe()


# In[9]:


df.describe(include="object")

# basic operation 0f column
# In[10]:


df[["country","life_exp"]]


# In[11]:


df["country"].unique()


# In[12]:


df["country"].value_counts()


# In[13]:


df["total_gdp"]=df["population"]*df["gdp_cap"]
df


# In[14]:


df["custom"]=[i for i in range(1704)]


# In[15]:


df


# In[16]:


df.drop(["custom"],axis=1,inplace=True)
df

#working with rows 
# In[17]:


ser=df["country"]
ser


# In[18]:


ser[5]

# how to select record 30 th to 40 th rows for the last 3columns using iloc??
# In[19]:


df.iloc[29:41,-3:]


# In[20]:


df.sort_values(["year"])


# In[21]:


movies=pd.read_csv("movies.csv")
movies


# In[22]:


directors=pd.read_csv("directors.csv")
directors.head()


# In[23]:


movies=pd.read_csv("movies.csv",index_col=0)
movies


# In[24]:


directors=pd.read_csv("directors.csv",index_col=0)
directors.head()


# In[25]:


movies.shape


# In[26]:


directors.shape

# movies directors left outer join
# In[27]:


(movies["director_id"].nunique())


# In[28]:


directors["id"].isin(directors["id"])


# In[29]:


data=movies.merge(directors,how="left",left_on="director_id",right_on="id")
data.head()


# In[30]:


data.drop(["director_id","id_y"],axis=1,inplace=True)


# In[31]:


data.head()


# In[32]:


data.info()


# In[33]:


df.describe()


# In[34]:


data.describe(include=object)


# In[35]:


data["revenue"]=data["revenue"]/1000000


# In[36]:


data["budget"]=data["budget"]/1000000

# quering dataframe to data fatch the data
# In[37]:


data.loc[data["vote_average"]>=8,["title","vote_average"]].head()


# In[38]:


data["vote_average"]>=8 # show always use loc and iloc


# In[39]:


data.loc[data["title"]=="Batman"]


# In[40]:


data.loc[data["title"].str.contains("Batman")]


# In[41]:


data.sort_values("popularity",ascending=False).head(5)


# In[42]:


data.groupby("director_name")["budget"].max()


# In[43]:


weather=pd.read_csv("weather.csv")


# In[44]:


weather


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[45]:


weather.shape


# In[46]:


weather_melt = pd.melt(weather, id_vars=["year", "month", "element"],
        var_name="day",value_name="temp")


# In[47]:


weather_tidy = weather_melt.pivot_table(index=["year", "month", "day"], columns="element", values="temp")


# In[48]:


weather_tidy

# uber case how to handle time stamp data 
# In[49]:


data =pd.read_csv("UberDrives.csv")


# In[50]:


data


# In[51]:


data.info()


# In[52]:


data.drop(1155, axis=0, inplace=True)


# In[53]:


data.drop_duplicates(inplace=True)


# In[54]:


data.columns = [col_name[:-1] for col_name in data.columns]


# In[55]:


data["START_DATE"] = pd.to_datetime(data["START_DATE"])


# In[56]:


data.head()


# In[57]:


data["END_DATE"] = pd.to_datetime(data["END_DATE"])


# In[58]:


data


# In[59]:


ts = data['START_DATE'][0]
ts

# What is the shortest journey made? - miles
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




