#!/usr/bin/env python
# coding: utf-8

# In[1]:


#imports
import pandas as pd
import sqlalchemy as sql
import os
import sqlite3


# In[2]:


def read_csv(url):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        print(f"Error extracting data from {url}: {e}")
        return None
    


# In[3]:


def extractblock():
    URLTrainTrips = 'https://urban.jrc.ec.europa.eu/api/udp/v2/en/data/?databrick_id=742&ts=TOURISM&nutslevel=0&nutsversion=-1&nutslevel=9&format=ods'
    URLTourismGHG = 'https://urban.jrc.ec.europa.eu/api/udp/v2/en/data/?databrick_id=740&nutslevel=0&ts=TOURISM&nutsversion=-1&mpx=1&nutslevel=9&format=csv'
    URLNightsSpent ='https://urban.jrc.ec.europa.eu/api/udp/v2/en/data/?databrick_id=764&nutslevel=0&ts=TOURISM&nutsversion=-1&mpx=1&nutslevel=9&format=csv'

    # Read from URLTrainTrips
    train_trips_data = read_csv(URLTrainTrips)
    tourism_ghg_data = read_csv(URLTourismGHG)
    nights_spent_data = read_csv(URLNightsSpent)
    # Describe the data
    return train_trips_data, tourism_ghg_data, nights_spent_data


# In[4]:


train_trips_data, tourism_ghg_data, nights_spent_data = extractblock()
print("Description of train_trips_data:")
print(train_trips_data.describe())


# In[5]:


print(train_trips_data.columns)

print(train_trips_data.info())


# In[6]:


print(tourism_ghg_data.info())


# In[7]:


print(nights_spent_data.info())


# In[162]:


.head()


# In[163]:


def transform_train_trips(train_trips_data):
    # Filter out rows where 'VERSIONS' is 2016
    train_trips_data = train_trips_data[train_trips_data['VERSIONS'] != 2016]
    
    # Filter out rows where 'LEVEL_ID' is not 0
    train_trips_data = train_trips_data[train_trips_data['LEVEL_ID'] == 0]
    
    # Drop unnecessary columns
    train_trips_data.drop(columns=['LEVEL_ID', 'VERSIONS', '2022', 'UNIT'], inplace=True)
    
    transformed_data = []

    for index, row in train_trips_data.iterrows():
        for year_col in ['2019', '2020', '2021']:
            if pd.notna(row[year_col]):
                transformed_data.append({
                    'TERRITORY_ID': row['TERRITORY_ID'],
                    'TERRITORY_NAME': row['NAME_HTML'],
                    'YEAR': year_col,
                    'TRAIN_TRIPS_SHARE': row[year_col]
                })


    train_trips_data_transformed = pd.DataFrame(transformed_data)
                                                
    train_trips_data_transformed['YEAR'] = train_trips_data_transformed['YEAR'].astype(int)

    train_trips_data_transformed['TRAIN_TRIPS_SHARE'] = pd.to_numeric(train_trips_data_transformed['TRAIN_TRIPS_SHARE'])
                                                
    train_trips_data_transformed = train_trips_data_transformed.sort_values(by=['TERRITORY_ID', 'YEAR']).reset_index(drop=True)
    
    return train_trips_data_transformed


# In[164]:


def transform_tourism_ghg(tourism_ghg_data):

    tourism_ghg_transformed = tourism_ghg_data[tourism_ghg_data['VERSIONS'] != 2016]
    
    tourism_ghg_transformed = tourism_ghg_transformed[tourism_ghg_transformed['LEVEL_ID'] == 0]
    
    tourism_ghg_transformed.drop(columns=['LEVEL_ID', 'VERSIONS', 'UNIT', 'DATE', 'NAME_HTML'], inplace=True)

    tourism_ghg_transformed = tourism_ghg_transformed.sort_values(by=['TERRITORY_ID', 'YEAR']).reset_index(drop=True)
    
    tourism_ghg_transformed['YEAR'] = tourism_ghg_transformed['YEAR'].astype(int)
    
    tourism_ghg_transformed.rename(columns={'VALUE': 'GHG_VALUE'}, inplace=True)
    
    return tourism_ghg_transformed


# In[165]:


def transform_nights_spent(nights_spent_data):

    nights_spent_transformed = nights_spent_data[nights_spent_data['VERSIONS'] != 2016]
    
    nights_spent_transformed = nights_spent_transformed[nights_spent_transformed['LEVEL_ID'] == 0]
    
    nights_spent_transformed.drop(columns=['LEVEL_ID', 'VERSIONS', 'UNIT', 'DATE', 'NAME_HTML' ], inplace=True)

    nights_spent_transformed = nights_spent_transformed.sort_values(by=['TERRITORY_ID', 'YEAR']).reset_index(drop=True)
    
    nights_spent_transformed['YEAR'] = nights_spent_transformed['YEAR'].astype(int)
    
    nights_spent_transformed.rename(columns={'VALUE': 'NIGHTS_SPENT_COUNT'}, inplace=True)
    
    return nights_spent_transformed


# In[166]:


def integrate_data(train_trips_data_transformed, tourism_ghg_transformed, nights_spent_transformed):
    
    # Perform inner join on train_trips_data_transformed and tourism_ghg_transformed
    merged_data = pd.merge(train_trips_data_transformed, tourism_ghg_transformed, on=['TERRITORY_ID', 'YEAR'], how='inner')
    
    # Perform inner join on merged_data and nights_spent_transformed
    merged_data = pd.merge(merged_data, nights_spent_transformed, on=['TERRITORY_ID', 'YEAR'], how='inner')
    
    return merged_data


# In[167]:


train_trips_data, tourism_ghg_data, nights_spent_data = extractblock()
train_trips_data_transformed = transform_train_trips(train_trips_data)
tourism_ghg_transformed = transform_tourism_ghg(tourism_ghg_data)
nights_spent_transformed = transform_nights_spent(nights_spent_data)
print(train_trips_data_transformed)


# In[168]:


print(tourism_ghg_transformed)


# In[169]:


print(nights_spent_transformed)


# In[170]:


merged_data = integrate_data(train_trips_data_transformed, tourism_ghg_transformed, nights_spent_transformed)

# Display the merged data
print(merged_data)


# In[171]:


def create_sqlite_database_in_current_dir(file_name):
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, file_name)
    conn = sqlite3.connect(file_path)
    conn.close()  


# In[172]:


def save_to_sqlite(df, table_name , db_url):
    df.to_sql(table_name, db_url, if_exists='replace', index=False) 


# In[173]:


from tabulate import tabulate

def read_from_sqlite(table_name, db_url):
    df = pd.read_sql_table(table_name, db_url)
    print(tabulate(df, headers='keys', tablefmt='pretty'))



# In[174]:


database_file_name = 'DatasSink.sqlite'

create_sqlite_database_in_current_dir(database_file_name)

save_to_sqlite(merged_data, 'Dataset', db_url=f'sqlite:///{database_file_name}')

read_from_sqlite('Dataset', db_url=f'sqlite:///{database_file_name}')


# In[ ]:





# In[ ]:




