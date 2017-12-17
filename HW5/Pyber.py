
# coding: utf-8

# In[2]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sea


# In[4]:

#read csv files
ride_data = pd.read_csv("raw_data/ride_data.csv")
city_data = pd.read_csv("raw_data/city_data.csv")


# In[36]:

#merge data
merged_df = pd.merge(ride_data, city_data, on="city", how="outer")
merged_df = merged_df.sort_values('city', ascending=True)
grouped_df = merged_df.groupby("city")
merged_df.head(20)


# In[53]:

#calculations
city_df = merged_df.drop_duplicates(["city"])
city_df = city_df.sort_values('city', ascending =True)
city_list = city_df['city'].tolist()
city_avg_fare_list = grouped_df['fare'].mean().tolist()
city_total_rides_list = grouped_df['ride_id'].count().tolist()
city_total_drivers_list = city_df['driver_count'].tolist()
city_type_list = city_df['type'].tolist()


# In[85]:

#dataframe with only relevant data, formatted for ease of use
clean_df = pd.DataFrame(list(zip(city_list,
                                 city_avg_fare_list,
                                 city_total_rides_list,
                                 city_total_drivers_list,
                                 city_type_list)),
                       columns=['City', 'AvgFare', 'TotalRides','Total Drivers','Type'])

clean_df.head()


# In[97]:

clean_df['Total Fare'] = clean_df.AvgFare * clean_df.TotalRides
clean_df.head()


# In[ ]:

#scatter plot here


# In[98]:

total_fares = merged_df['fare'].sum()
total_rides = merged_df['ride_id'].count()
total_drivers = clean_df['Total Drivers'].sum()


# In[106]:

#data for pies
type_df = clean_df.groupby('Type')
drivers_by_type = type_df['Total Drivers'].sum().tolist()
rides_by_type = type_df['TotalRides'].sum().tolist()
fares_by_type = type_df['Total Fare'].sum().tolist()

drivers_perc = [x/total_drivers*100 for x in drivers_by_type]
rides_perc = [x/total_rides*100 for x in rides_by_type]
fares_perc = [x/total_fares*100 for x in fares_by_type]
pie_df = pd.DataFrame({"Percent of Total Fares":fares_perc,
                      "Percent of Total Rides":rides_perc,
                      "Percent of Total Drivers":drivers_perc,}, index=['Rural', 'Suburban', 'Urban'])
pie_df.head()


# In[ ]:



