

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sea
```


```python
#read csv files
ride_data = pd.read_csv("raw_data/ride_data.csv")
city_data = pd.read_csv("raw_data/city_data.csv")
```


```python
#merge data
merged_df = pd.merge(ride_data, city_data, on="city", how="outer")
merged_df = merged_df.sort_values('city', ascending=True)
grouped_df = merged_df.groupby("city")
merged_df.head(20)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1489</th>
      <td>Alvarezhaven</td>
      <td>2016-07-04 04:28:22</td>
      <td>33.31</td>
      <td>306054352684</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1475</th>
      <td>Alvarezhaven</td>
      <td>2016-06-11 23:45:52</td>
      <td>43.34</td>
      <td>3938173695105</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1476</th>
      <td>Alvarezhaven</td>
      <td>2016-02-07 02:46:18</td>
      <td>35.22</td>
      <td>5405756761666</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1477</th>
      <td>Alvarezhaven</td>
      <td>2016-01-21 07:25:48</td>
      <td>22.83</td>
      <td>3565582370530</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1479</th>
      <td>Alvarezhaven</td>
      <td>2016-05-20 12:26:56</td>
      <td>42.00</td>
      <td>7852567608457</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1480</th>
      <td>Alvarezhaven</td>
      <td>2016-08-03 06:45:57</td>
      <td>4.07</td>
      <td>6100187302721</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1481</th>
      <td>Alvarezhaven</td>
      <td>2016-01-25 06:02:25</td>
      <td>5.16</td>
      <td>2233026076010</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1482</th>
      <td>Alvarezhaven</td>
      <td>2016-11-19 02:00:34</td>
      <td>5.34</td>
      <td>1108172306544</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1483</th>
      <td>Alvarezhaven</td>
      <td>2016-02-15 11:14:12</td>
      <td>31.74</td>
      <td>5487020911007</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1484</th>
      <td>Alvarezhaven</td>
      <td>2016-06-16 18:29:05</td>
      <td>32.46</td>
      <td>858631473935</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1485</th>
      <td>Alvarezhaven</td>
      <td>2016-03-16 02:01:15</td>
      <td>33.62</td>
      <td>8974645194719</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1486</th>
      <td>Alvarezhaven</td>
      <td>2016-09-19 16:01:49</td>
      <td>27.51</td>
      <td>6282665852239</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1487</th>
      <td>Alvarezhaven</td>
      <td>2016-05-16 15:33:14</td>
      <td>6.45</td>
      <td>8939751998750</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1488</th>
      <td>Alvarezhaven</td>
      <td>2016-01-27 10:38:40</td>
      <td>6.72</td>
      <td>6152998520191</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>Alvarezhaven</td>
      <td>2016-04-18 20:51:29</td>
      <td>31.93</td>
      <td>4267015736324</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1460</th>
      <td>Alvarezhaven</td>
      <td>2016-08-01 00:39:48</td>
      <td>6.42</td>
      <td>8394540350728</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1474</th>
      <td>Alvarezhaven</td>
      <td>2016-05-15 20:43:44</td>
      <td>40.04</td>
      <td>1806812593131</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1473</th>
      <td>Alvarezhaven</td>
      <td>2016-09-23 21:51:59</td>
      <td>17.67</td>
      <td>3829336915201</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1478</th>
      <td>Alvarezhaven</td>
      <td>2016-05-01 14:35:12</td>
      <td>22.54</td>
      <td>6435260355302</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1462</th>
      <td>Alvarezhaven</td>
      <td>2016-08-18 07:12:06</td>
      <td>20.74</td>
      <td>357421158941</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
#calculations
city_df = merged_df.drop_duplicates(["city"])
city_df = city_df.sort_values('city', ascending =True)
city_list = city_df['city'].tolist()
city_avg_fare_list = grouped_df['fare'].mean().tolist()
city_total_rides_list = grouped_df['ride_id'].count().tolist()
city_total_drivers_list = city_df['driver_count'].tolist()
city_type_list = city_df['type'].tolist()
```


```python
#dataframe with only relevant data, formatted for ease of use
clean_df = pd.DataFrame(list(zip(city_list,
                                 city_avg_fare_list,
                                 city_total_rides_list,
                                 city_total_drivers_list,
                                 city_type_list)),
                       columns=['City', 'AvgFare', 'TotalRides','Total Drivers','Type'])

clean_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>AvgFare</th>
      <th>TotalRides</th>
      <th>Total Drivers</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alvarezhaven</td>
      <td>23.928710</td>
      <td>31</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alyssaberg</td>
      <td>20.609615</td>
      <td>26</td>
      <td>67</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anitamouth</td>
      <td>37.315556</td>
      <td>9</td>
      <td>16</td>
      <td>Suburban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Antoniomouth</td>
      <td>23.625000</td>
      <td>22</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Aprilchester</td>
      <td>21.981579</td>
      <td>19</td>
      <td>49</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
clean_df['Total Fare'] = clean_df.AvgFare * clean_df.TotalRides
clean_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>AvgFare</th>
      <th>TotalRides</th>
      <th>Total Drivers</th>
      <th>Type</th>
      <th>Total Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alvarezhaven</td>
      <td>23.928710</td>
      <td>31</td>
      <td>21</td>
      <td>Urban</td>
      <td>741.79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alyssaberg</td>
      <td>20.609615</td>
      <td>26</td>
      <td>67</td>
      <td>Urban</td>
      <td>535.85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anitamouth</td>
      <td>37.315556</td>
      <td>9</td>
      <td>16</td>
      <td>Suburban</td>
      <td>335.84</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Antoniomouth</td>
      <td>23.625000</td>
      <td>22</td>
      <td>21</td>
      <td>Urban</td>
      <td>519.75</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Aprilchester</td>
      <td>21.981579</td>
      <td>19</td>
      <td>49</td>
      <td>Urban</td>
      <td>417.65</td>
    </tr>
  </tbody>
</table>
</div>




```python
#scatter plot here
```


```python
total_fares = merged_df['fare'].sum()
total_rides = merged_df['ride_id'].count()
total_drivers = clean_df['Total Drivers'].sum()
```


```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percent of Total Drivers</th>
      <th>Percent of Total Fares</th>
      <th>Percent of Total Rides</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rural</th>
      <td>3.108189</td>
      <td>6.579786</td>
      <td>5.193187</td>
    </tr>
    <tr>
      <th>Suburban</th>
      <td>18.977884</td>
      <td>31.445750</td>
      <td>27.295388</td>
    </tr>
    <tr>
      <th>Urban</th>
      <td>77.913927</td>
      <td>61.974463</td>
      <td>67.511425</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
