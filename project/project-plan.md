# Project Plan

## Title
<!-- Give your project a short title. -->
The Relationship Between Train Usage and Greenhouse Gas Emissions in EU Tourism Ecosystems

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
Do EU regions with higher train usage exhibit lower the amount of greenhouse gas (GHG) emissions produced by the tourism ecosystem in relation to the total GHG emissions reported by that region? 

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Analyzing the correlation between the use of public railway in tourrist activities and greenhouse gas emissions in EU regions' tourism ecosystems is essential for understanding the potential impact of sustainable transportation on environmental sustainability. 
This project employs Javyee datapiplines and open data sources and implementing robust data pipelines to gather and process information on train usage, tourism statistics, and GHG emissions. 
The results of this analysis can provide insights into the effectiveness of sustainable transit solutions in reducing the carbon footprint of tourism activities. 
## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Greenhouse gas emissions by source sector
* Metadata URL: [https://ec.europa.eu/eurostat/cache/metadata/en/env_air_gge_esms.htm]
* Data URL: [https://ec.europa.eu/eurostat/databrowser/view/ENV_AIR_GGE__custom_1313758/bookmark/table?lang=en&bookmarkId=1188f0ad-38e0-46c7-b2ce-5159b0ddfc8e]
* Data Type:Spreadsheets XLSX

This dataset provides indicator of the measured man-made greenhouse gas (GHG) emissions as well as GHG removals, The net GHG emissions include international aviation. The data are submitted annually by Member States to the EU and the United Nations Framework Convention on Climate Change (UNFCCC). The European Environment Agency (EEA) compiles the EU aggregate data and publishes data for the EU and all Member States. 

### Datasource2: Tourism GHG intensity
* Metadata URL: [https://ec.europa.eu/eurostat/cache/metadata/en/env_ac_ainah_r2_sims.htm]
* Data URL: [https://ec.europa.eu/eurostat/web/products-datasets/-/env_ac_ainah_r2]
* Data Type: CSV

This dataset provides indicator of the measured amount of greenhouse gas (GHG) emissions produced by the tourism ecosystem per Million Euro of Gross Value Added (GVA) in the tourism sector

### Datasource3: Share of trips by train
* Metadata URL: [https://ec.europa.eu/eurostat/cache/metadata/en/tour_dem_esms.htm]
* Data URL: [(https://urban.jrc.ec.europa.eu/api/udp/v2/en/data/?databrick_id=742&ts=TOURISM&nutslevel=0&nutsversion=-1&nutslevel=9&format=ods)]
* Data Type: CSV
The dataset describes the share of trips taken by train within a tourism destination in the EU. The indicator is obtained dividing the number of trips by train by the number of trips done using all means of transport, i.e.: Air, land, railways, buses, coahes, motor vehicles, waterway, other. Higher values indicate a more widespread use of the train for domestic travel compared to other modes of transport with a higher environmental impact. 

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Collection of data sources and evaluating data quality
2. Extraction of data into Jayvee pipeline
3. Cleaning and transfroming the data
4. Analyzing





1. Example Issue [#1][i1]
2. ...

[i1]: https://github.com/jvalue/made-template/issues/1
