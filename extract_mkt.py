from functools import partial
from geopy.geocoders import Nominatim
import pandas as pd

# Set up geocoder:
geolocator = Nominatim(user_agent="Write any name")
geocode = partial(geolocator.geocode, language="es")

# Load your WFP food price data set (in csv format):
markets_df = pd.read_csv("Mali_FoodP.csv")
# Convert dataframe to a dictionary:
markets_list = markets_df['mktname'].to_list()
markets_dict = dict.fromkeys(markets_list)

# Find coordinates of market names in markets_dict (Geocode):
for i in markets_dict:
  geomarket = geocode(i)
  if geomarket != None:
    markets_dict[i] = [geomarket.latitude, geomarket.longitude]

# Remove not found markets names from markets_dict:
markets_dict2 = {}
for key, value in markets_dict.items():
    if value != None:
        markets_dict2[key] = value

# Create a dictionary of names that were not found by the geolocator:
Not_found_dict = {}
for key, value in markets_dict.items():
    if value == None:
        Not_found_dict[key] = value

# Make a dataframe of the geolocated markets dictionary:
markets_df = pd.DataFrame.from_dict(markets_dict2, orient='index')
markets_df.columns = ['lat', 'long']
print(markets_df)

# Make a dataframe of the Not_found_dict:
Not_found_df = pd.DataFrame.from_dict(Not_found_dict, orient='index')
Not_found_df.columns = ['NOT FOUND MARKETS:']
print(Not_found_df)

# Export dataframes to csv files: 
markets_df.to_csv("name_of_file1.csv")
Not_found_df.to_csv("name_of_file2.csv")
