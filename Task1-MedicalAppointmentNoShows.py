#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Loading Datastet
df = pd.read_csv("medicalappointment.csv")
df.head()


# In[3]:


df.isnull()


# In[4]:


df.drop_duplicates()


# In[5]:


import string, unicodedata


# In[6]:


def standardize_text(text):
    text = str(text).lower()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return ' '.join(text.split())


# In[7]:


df['Gender'] = df['Gender'].apply(standardize_text)
df['Gender']


# In[8]:


df['Neighbourhood']=df['Neighbourhood'].apply(standardize_text)
df['Neighbourhood']


# In[9]:


df['No-show']=df['No-show'].apply(standardize_text)
df['No-show']


# In[12]:


df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['ScheduledDay'] = df['ScheduledDay'].dt.strftime('%d-%m-%Y')


# In[18]:


df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])
df['AppointmentDay'] = df['AppointmentDay'].dt.strftime('%d-%m-%Y')


# In[20]:


df.head(15)


# In[21]:


df.columns = (
    df.columns
    .str.strip()                      # remove leading/trailing spaces
    .str.lower()                     # convert to lowercase
    .str.replace(' ', '_')           # replace spaces with underscores
)


# In[22]:


df


# In[24]:


df.dtypes


# In[31]:


df['scheduledday'] = pd.to_datetime(df['scheduledday'], dayfirst=True)
df['scheduledday']


# In[30]:


df['appointmentday'] = pd.to_datetime(df['appointmentday'], dayfirst=True)
df['appointmentday']

