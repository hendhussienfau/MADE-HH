# The Relationship Between Train Usage and Greenhouse Gas Emissions in EU Tourism Ecosystems
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
## Research Question
How does the utilization of trains as mode of transportation within a tourism destination
can influence the overall greenhouse gas intensity of the tourism sector within EU countries?

## Motivation
Tourism is a major economic driver in the European Union countries, contributing approximately 11% to employment, encompassing direct, indirect, and induced jobs in 2019 according to the estimates of the European Commission. However, the influx of tourism poses significant environmental challenges, particularly in terms of greenhouse gas (GHG) emissions which was estimated be the European Commission to be as high as 48 Tons of GHG emissions per Million Euro of Gross Value Added on average across the EU countries. As global awareness of climate change increases, the need for sustainable tourism practices has become more urgent. One critical aspect of this is the mode of transportation used by tourists within their destinations. Trains as a mode of transport, are known for their lower environmental impact compared to cars and airplanes. As part of the efforts the necessity to accelerate green transition in EU Tourism, the Council of the European defined the share of trips by train as one of the green pillars for this green transition, as it measures the relative importance of sustainable means of transportation within a tourism destination, approximated by the share of trips taken by train. Higher values indicate a more widespread use of the train compared to other modes of transport with a higher environmental impact. This report aims to address the research question: How does the utilization of trains as a mode of transportation within a tourism destination influence the overall greenhouse gas intensity of the tourism sector within EU countries? By doing so, it is examining the potential of train travel to reduce GHG emissions. 

## Data Sources
The chosen datasets are developed by European Commission Joint Research Centre. They provide tourism-relevant data and indicators collected from available, trusted sources concerning the tourism ecosystem on EU27 Member States aiming to characterize the tourism ecosystem at destination level (i.e., country), and track progress towards lower environmental impacts. The data sets can be described as follows: 
1. Share of trips by train: This dataset provides information on the share of trips within a tourism destination that utilize trains as the mode of transportation. It gives insights into the preference for train travel which is relevant for understanding the transportation choices made by tourists. It is listed as one of the green pillars by EU Tourism Dashboard.
Source: [Joint Research Centre Data Catalogue - UDP - Share of trips by train - European Commission (europa.eu)](https://data.jrc.ec.europa.eu/dataset/fdfc3d62-86dd-4104-853f-2c89e676561f)
2. Tourism GHG intensity: This dataset contains data on the greenhouse gas (GHG) intensity of the tourism sector, measured as GHG emissions per Million Euro of Gross Value Added (GVA) in the tourism sector. It helps in understanding the environmental impact of tourism activities within European Union countries. 
Source: [Joint Research Centre Data Catalogue - UDP - Tourism GHG intensity - European Commission (europa.eu)](https://data.jrc.ec.europa.eu/dataset/1c837ec8-9d2e-4f6e-be91-bafc812a1c7b)
3. Tourism Demand expressed by the number of nights spent in tourism destination: This dataset provides information on the total number of nights spent at tourist accommodation establishments in a destination (country or region) by both domestic and foreign tourists. It is provided by EU Tourism as a basic tourism descriptor to provide further context and characterization of the tourism activity of countries as it offers insights into the overall demand for tourism services in a particular destination. This measurement will help to assess the environmental impact of tourism activities within EU countries while accounting for the scale of tourism demand in each destination. Given that the high variance in tourism demand between destination countries can distort the GHG value. 
Source: [Joint Research Centre Data Catalogue - UDP - Nights spent - European Commission (europa.eu)]
(https://data.jrc.ec.europa.eu/dataset/4c16628c-1e56-45b3-af40-70dd82df5408)
## Data Pipeline
![Pipeline Graph](https://github.com/hendhussienfau/MADE-HH/assets/104495535/dc2d30e7-4ce5-4912-b268-d266a81e1c26)
Python was the primary technology used to implement this pipeline using data processing functions from Panda library, while the SQLite database management system was used for loading into the data sink . The stages used in the pipeline are listed below: 
•Data Collection: Data was collected from three CSV files using http links from the Joint Research Centre Data Catalogue. These sources included information on train trips, tourism greenhouse gas intensity, and nights spent at tourist accommodations.
•Data Transformation: the data underwent transformation steps to prepare it for analysis. It included filtering out specific rows based on criteria and transposing some data columns to fit the next pipeline blocks. 
•Integration: the transformed datasets were combined using inner joins based on common keys such as territory ID and year. This integration allowed for the creation of a unified dataset for further analysis.
•Loading: Finally, the integrated dataset was loaded into an SQLite table to as a final sink which allows for retrieval and sharing of the dataset for future usage.
## License
Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

