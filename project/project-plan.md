# Project Plan

## Title
<!-- Give your project a short title. -->
The Relationship Between Train Usage and Greenhouse Gas Emissions in EU Tourism Ecosystems

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
How does the utilization of trains as mode of transportation within a tourism destination
can influence the overall greenhouse gas intensity of the tourism sector within EU countries?


## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Analyzing the correlation between the use of public railway in tourrist activities and greenhouse gas emissions in EU regions' tourism ecosystems is essential for understanding the potential impact of sustainable transportation on environmental sustainability. 
This project employs Javyee datapiplines and open data sources and implementing robust data pipelines to gather and process information on train usage, tourism statistics, and GHG emissions. 
The results of this analysis can provide insights into the effectiveness of sustainable transit solutions in reducing the carbon footprint of tourism activities. 
## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Tourism GHG intensity
* Metadata URL: [https://ec.europa.eu/eurostat/cache/metadata/en/env_ac_ainah_r2_sims.htm]
* Data URL: [https://ec.europa.eu/eurostat/web/products-datasets/-/env_ac_ainah_r2]
* Data Type: CSV

This dataset contains data on the greenhouse gas (GHG) intensity of the tourism sector, measured as GHG emissions per Million Euro of Gross Value Added (GVA) in the tourism sector. It helps in understanding the environmental impact of tourism activities within European Union countries. 

### Datasource2: Share of trips by train
* Metadata URL: [https://ec.europa.eu/eurostat/cache/metadata/en/tour_dem_esms.htm]
* Data URL: [(https://urban.jrc.ec.europa.eu/api/udp/v2/en/data/?databrick_id=742&ts=TOURISM&nutslevel=0&nutsversion=-1&nutslevel=9&format=ods)]
* Data Type: CSV
The dataset describes the share of trips taken by train within a tourism destination in the EU. The indicator is obtained dividing the number of trips by train by the number of trips done using all means of transport, i.e.: Air, land, railways, buses, coahes, motor vehicles, waterway, other. Higher values indicate a more widespread use of the train for domestic travel compared to other modes of transport with a higher environmental impact. 
### Datasource3: Tourism Demand expressed by the number of nights spent in tourism destination
* Metadata URL: [https://ec.europa.eu/eurostat/cache/metadata/en/tour_dem_esms.htm]
* Data URL: [https://urban.jrc.ec.europa.eu/api/udp/v2/en/data/?databrick_id=764&nutslevel=0&ts=TOURISM&nutsversion=-1&mpx=1&nutslevel=9&format=csv]
* Data Type: CSV
This dataset provides information on the total number of nights spent at tourist accommodation establishments in a destination (country or region) by both domestic and foreign tourists. It is provided by EU Tourism as a basic tourism descriptor to provide further context and characterization of the tourism activity of countries as it offers insights into the overall demand for tourism services in a particular destination. This measurement will help to assess the environmental impact of tourism activities within EU countries while accounting for the scale of tourism demand in each destination. Given that the high variance in tourism demand between destination countries can distort the GHG value. 
## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Collection of data sources and evaluating data quality [https://github.com/hendhussienfau/MADE-HH/issues/1]
2. Extraction of data into Jayvee pipeline [https://github.com/hendhussienfau/MADE-HH/issues/2]
3. Cleaning and transfroming the data [https://github.com/hendhussienfau/MADE-HH/issues/3]
4. Integrating data and creating derived data [https://github.com/hendhussienfau/MADE-HH/issues/4]
5. saving the pipeline output to database [https://github.com/hendhussienfau/MADE-HH/issues/5]
6. Analyzing the output data [https://github.com/hendhussienfau/MADE-HH/issues/6]

