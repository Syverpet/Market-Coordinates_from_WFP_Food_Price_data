# Market-Coordinates_from_WFP_Food_Price_data
## This Python script automatically extracts (geocodes) the coordinates of markets from open access WFP food price data sets. 
#### example of data set: https://data.humdata.org/dataset/wfp-food-prices-for-mali


## Inputs are WFP food price data csv files, and outputs are two new csv files, locations that were found, locations not found:
![image](https://user-images.githubusercontent.com/78020605/118402909-e1b9cd80-b663-11eb-9b4f-c1c017e49798.png)


### The geocoder uses the OpenStreetMap(OSM) based  tool "Nominatim" to extract the coordinates from a list of location names. 
### Dependencies: geopy, pandas

#### Author: Syver Petersen
#### Contact: syverpet@gmail.com
