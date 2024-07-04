#!/usr/bin/env python
# coding: utf-8

# In[1]:


#imports
import pandas as pd
import sqlite3
import os
from sqlalchemy import create_engine
from scipy.stats import linregress
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import matplotlib.dates as mdates
import numpy as np


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


print(tourism_ghg_data.info())


# In[6]:


print(train_trips_data.columns)

print(train_trips_data.info())


# In[7]:


print(nights_spent_data.info())


# In[ ]:





# In[86]:


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
    
    train_trips_data_transformed = train_trips_data_transformed[train_trips_data_transformed['TERRITORY_ID'] != "LU"]
    train_trips_data_transformed = train_trips_data_transformed[train_trips_data_transformed['TERRITORY_ID'] != "SI"]
    
    return train_trips_data_transformed


# In[87]:


def transform_tourism_ghg(tourism_ghg_data):

    tourism_ghg_transformed = tourism_ghg_data[tourism_ghg_data['VERSIONS'] != 2016]
    
    tourism_ghg_transformed = tourism_ghg_transformed[tourism_ghg_transformed['LEVEL_ID'] == 0]
    
    tourism_ghg_transformed.drop(columns=['LEVEL_ID', 'VERSIONS', 'UNIT', 'DATE', 'NAME_HTML'], inplace=True)

    tourism_ghg_transformed = tourism_ghg_transformed.sort_values(by=['TERRITORY_ID', 'YEAR']).reset_index(drop=True)
    
    tourism_ghg_transformed['YEAR'] = tourism_ghg_transformed['YEAR'].astype(int)
    
    tourism_ghg_transformed.rename(columns={'VALUE': 'GHG_VALUE'}, inplace=True)
    
    #data cleaning
    
    countries_with_zero_ghg = tourism_ghg_transformed[tourism_ghg_transformed['GHG_VALUE'] == 0]['TERRITORY_ID'].unique()
    
    tourism_ghg_transformed = tourism_ghg_transformed[~tourism_ghg_transformed['TERRITORY_ID'].isin(countries_with_zero_ghg)]
    
      
    return tourism_ghg_transformed


# In[88]:


def transform_nights_spent(nights_spent_data):

    nights_spent_transformed = nights_spent_data[nights_spent_data['VERSIONS'] != 2016]
    
    nights_spent_transformed = nights_spent_transformed[nights_spent_transformed['LEVEL_ID'] == 0]
    
    nights_spent_transformed.drop(columns=['LEVEL_ID', 'VERSIONS', 'UNIT', 'DATE', 'NAME_HTML' ], inplace=True)

    nights_spent_transformed = nights_spent_transformed.sort_values(by=['TERRITORY_ID', 'YEAR']).reset_index(drop=True)
    
    nights_spent_transformed['YEAR'] = nights_spent_transformed['YEAR'].astype(int)
    
    nights_spent_transformed.rename(columns={'VALUE': 'NIGHTS_SPENT_COUNT'}, inplace=True)
   
    return nights_spent_transformed


# In[89]:


def integrate_data(train_trips_data_transformed, tourism_ghg_transformed, nights_spent_transformed):
    
    merged_data = pd.merge(train_trips_data_transformed, tourism_ghg_transformed, on=['TERRITORY_ID', 'YEAR'], how='inner')
    
    merged_data = pd.merge(merged_data, nights_spent_transformed, on=['TERRITORY_ID', 'YEAR'], how='inner')
    
    merged_data['GHG_NORMALIZED'] = merged_data.apply(
    lambda row: round(row['GHG_VALUE'] / (row['NIGHTS_SPENT_COUNT'] / 1000000), 2) if row['GHG_VALUE'] != 0 else 0, axis=1 )
    
    return merged_data


# In[90]:


train_trips_data, tourism_ghg_data, nights_spent_data = extractblock()
train_trips_data_transformed = transform_train_trips(train_trips_data)
tourism_ghg_transformed = transform_tourism_ghg(tourism_ghg_data)
nights_spent_transformed = transform_nights_spent(nights_spent_data)
print(train_trips_data_transformed)


# In[91]:


print(tourism_ghg_transformed)


# In[92]:


print(nights_spent_transformed)


# In[93]:


merged_data = integrate_data(train_trips_data_transformed, tourism_ghg_transformed, nights_spent_transformed)

print(merged_data)


# In[94]:


def save_to_sqlite(df, table_name, db_url='sqlite:///../data/DataSink.sqlite'):
    engine = create_engine(db_url)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    engine.dispose()


# In[95]:


from tabulate import tabulate

def read_from_sqlite(table_name, db_url):
    df = pd.read_sql_table(table_name, db_url)
    print(tabulate(df, headers='keys', tablefmt='pretty'))



# In[96]:


db_directory = '../data'
if not os.path.exists(db_directory):
    os.makedirs(db_directory)


# In[97]:


database_file_name = 'DataSink.sqlite'

save_to_sqlite(merged_data, 'DataSink', db_url=f'sqlite:///../data/{database_file_name}')

read_from_sqlite('DataSink', db_url=f'sqlite:///../data/{database_file_name}')


# In[98]:


def read_from_sqlite(table_name, db_url):
    conn = sqlite3.connect(db_url)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df


# In[134]:


def perform_analysis(df):
    
    # Correlation
    correlation_coefficient = df['TRAIN_TRIPS_SHARE'].corr(df['GHG_NORMALIZED'])
    print("Correlation Coefficient between TRAIN_TRIPS_SHARE and GHG_NORMALIZED:")
    print(correlation_coefficient)

    # Calculate the slope and intercept using linregress
    slope, intercept, r_value, p_value, std_err = linregress(df['TRAIN_TRIPS_SHARE'], df['GHG_NORMALIZED'])
    # Print slope and intercept
    print(f"Slope: {slope:.2f}")
    print(f"Intercept: {intercept:.2f}")
    
     # Initialize the plot
    sns.set_style('whitegrid')
    plt.figure(figsize=(14, 6))
    g = sns.lmplot(x='TRAIN_TRIPS_SHARE', y='GHG_NORMALIZED', data=df, hue='YEAR', ci=None)
    plt.title('Share of Trips by Train vs Tourism Greenhouse Gas Emissions Intensity (Normalized)')
    plt.xlabel('Share of Trips by Train')
    plt.ylabel('Tourism GHG Intensity (Normalized)')
    
    unique_years = df['YEAR'].unique()
    for year in unique_years:
        year_data = df[df['YEAR'] == year]
        slope, intercept, r_value, p_value, std_err = linregress(year_data['TRAIN_TRIPS_SHARE'], year_data['GHG_NORMALIZED'])
        mean_x = year_data['TRAIN_TRIPS_SHARE'].mean()
        mean_y = year_data['GHG_NORMALIZED'].mean()
        plt.text(mean_x, mean_y, f'{slope:.2f}', fontsize=6, color='black')

    plt.show()
    
    # Create a bar chart for countries and nights spent count
    plt.figure(figsize=(18, 6))
    sns.barplot(x='TERRITORY_NAME', y='NIGHTS_SPENT_COUNT', hue='YEAR', data=df, errorbar=None)
    plt.xlabel('Country')
    plt.ylabel('Nights Spent in destination (100 Mil)')
    plt.title('Tourism demand in destination')
    plt.legend(title='Year')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Create a bar chart for countries and GHG
    plt.figure(figsize=(18, 6))
    sns.barplot(x='TERRITORY_NAME', y='GHG_VALUE', hue='YEAR', data=df, errorbar=None)
    plt.xlabel('Country')
    plt.ylabel('GHG Intensity')
    plt.title('The amount of greenhouse gas (GHG) emissions produced by the tourism ecosystem per Million Euro of Gross Value Added (GVA)')
    plt.legend(title='Year')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Create a bar chart for countries and GHG
    plt.figure(figsize=(18, 6))
    sns.barplot(x='TERRITORY_NAME', y='TRAIN_TRIPS_SHARE', hue='YEAR', data=df, errorbar=None)
    plt.xlabel('Country')
    plt.ylabel('Train Trips Share')
    plt.title('Train Trips Share by Country')
    plt.legend(title='Year')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    
    
    # Scatter plot with regression line
    sns.set_style('whitegrid')
    sns.lmplot(x='TRAIN_TRIPS_SHARE', y='GHG_NORMALIZED', data=df, hue='YEAR', ci=None)
    plt.title('Share of Trips by Train vs Tourism Greenhouse Gas Emissions Intensity (Normalized)')
    plt.xlabel('Share of Trips by Train')
    plt.ylabel('Tourism GHG Intensity (Normalized)')
    plt.show()
    
    avg_data = df.groupby('TERRITORY_NAME').agg({
    'GHG_NORMALIZED': 'mean',
    'TRAIN_TRIPS_SHARE': 'mean'
    }).reset_index()

    avg_data = avg_data.sort_values(by='GHG_NORMALIZED') 
    
    # Bubble plot for countries
    plt.figure(figsize=(18, 6))
    plt.scatter(x=avg_data['TERRITORY_NAME'], 
            y=avg_data['GHG_NORMALIZED'], 
            s=(avg_data['TRAIN_TRIPS_SHARE'] * 200) ** 2,  # Scale bubble size for better visualization
            alpha=0.5, 
            c='b', 
            label='Train Trip%')

    plt.xlabel('Country')
    plt.ylabel('Tourism Average GHG Intensity (Normalized)')
    plt.title('Tourism Average Greenhouse Gas Emissions Intensity (Normalized) vs Train Trip Share per Country')
    plt.xticks(rotation=90)
    plt.show()
    
     # Bubble plot for countries
    avg_data = avg_data.sort_values(by='TRAIN_TRIPS_SHARE') 
    plt.figure(figsize=(18, 8))
    plt.scatter(x=avg_data['TERRITORY_NAME'], 
            y=avg_data['TRAIN_TRIPS_SHARE'], 
            s=(avg_data['GHG_NORMALIZED']) * 100,  # Scale bubble size for better visualization
            label='GHG intensity per country')


    
    for i in range(len(avg_data)):
        plt.annotate(f"{avg_data['GHG_NORMALIZED'].iloc[i]:.2f}", 
                 (avg_data['TERRITORY_NAME'].iloc[i], avg_data['TRAIN_TRIPS_SHARE'].iloc[i]), 
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center', 
                 fontsize=12)
        
    plt.xlabel('Country')
    plt.ylabel('Train Trip Share')
    plt.title('Tourism Average Greenhouse Gas Emissions Intensity (Normalized) vs Train Trip Share per Country')
    plt.xticks(rotation=90)
    plt.show()
            
perform_analysis(merged_data)


# In[135]:


print(merged_data.describe())


# In[137]:


print(merged_data.info())


# In[ ]:

