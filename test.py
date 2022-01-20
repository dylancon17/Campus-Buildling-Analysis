# Code Here

import pandas
import matplotlib.pyplot as plt
import numpy as np

data = pandas.read_csv('building1.csv', sep=',', header=0)
data.head()

data['Date'] = pandas.to_datetime(data['Date'])

plt.plot(data['Date'], data['Heating (kWh)'])
plt.xlabel('Date')
plt.ylabel('Heating (kWh)')
plt.show()


# helper variables to specify the years of interest and the columns.
years = [2018, 2019, 2020, 2021]
cols = ['Heating (kWh)', 'Cooling (kWh)', 'Electricity (kWh)', 'Nat Gas (kWh)', 'Domestic Water (m3)']

# Create a new figure with the number of subplots equal to the number of cols
# figsize specifies the figure size in [width, height] format
fig, ax = plt.subplots(nrows=len(cols), ncols=1, figsize=[20,14])

# Loop through the years to plot
for year in years:
    # Select the data from that year
    dat = data[data['Date'].dt.year == year]
    
    # Loop through the columns and plot the data in the appropriate subplot
    for idx in range(len(cols)):
        ax[idx].plot(dat['Date'].dt.dayofyear, dat[cols[idx]])
        
# Set the same xlabel for all subplots
plt.setp(ax, xlabel = 'Day of year')

# Loop through the subplots and set the appropriate ylabel
for idx in range(len(cols)):
    plt.setp(ax[idx], ylabel = cols[idx])
    
    # Add a legend to each subplot
    ax[idx].legend(years)
    
# Show the plot
plt.show()

# Create a new figure
fig = plt.figure(figsize=[14,4])

# Create a new subplot.  '121' means 1 row, 2 columns, 1st subplot
axes1 = plt.subplot(121)

# Bin the data by day of the week
binned_data_by_day_of_week = data.groupby(data['Date'].dt.dayofweek)

# Plot the min, max and mean of the Electricity data
binned_data_by_day_of_week ['Electricity (kWh)'].max().plot(ax=axes1)
binned_data_by_day_of_week ['Electricity (kWh)'].mean().plot(ax=axes1)
binned_data_by_day_of_week ['Electricity (kWh)'].min().plot(ax=axes1)

# Create labels
plt.xlabel('Day of Week')

# dayofweek by default starts with Monday as index 0.  xticks() allows
# for custom tick labels
plt.xticks(range(7),['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'])
plt.ylabel('Electricity (kWh)')

# Add a legend
plt.legend(['Max', 'Mean', 'Min'])


# Create a new subplot.  '121' means 1 row, 2 columns, 2nd subplot
axes2 = plt.subplot(122)

# Bin the data by month
binned_data_by_month = data.groupby(data['Date'].dt.month)

# Plot the average monthly heating and cooling use
binned_data_by_month ['Heating (kWh)'].mean().plot(ax=axes2)
binned_data_by_month ['Cooling (kWh)'].mean().plot(ax=axes2)

# Add labels and a legend
plt.xlabel('Month')
plt.legend(['Mean Heating (kWh)', 'Mean Cooling (kWh)'])
plt.ylabel('Daily kWh')

# Show the plot
plt.show()
