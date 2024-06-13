#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytest
import pandas as pd
from Pipeline import (
    read_csv,
    extractblock,
    transform_train_trips,
    transform_tourism_ghg,
    transform_nights_spent,
    integrate_data,
    save_to_sqlite,
    read_from_sqlite,
)


# In[2]:


DATABASE_FILE_NAME = 'DataSink.sqlite'
OUTPUT_FILE_PATH = 'sqlite:///../data/DataSink.sqlite'


# In[3]:


def test_outputfile():
    assert os.path.exists(OUTPUT_FILE_PATH), "SQLite database file was not created.."
   


# In[4]:


def test_read_csv():
#mock link to test reading csv files
    url = 'https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv'  # mock link
    df = read_csv(url)
    assert df is not None, "Failed to read CSV from URL"
    


# In[ ]:




