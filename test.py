# Code Here

import pandas
import matplotlib.pyplot as plt
import numpy as np

def heat_cooling_combined(data):
    spring_summer_points = [18019, 18385, 18748]
    fall_points = [17775, 18138, 18505, 18872]
    winter_points = [17897, 18260, 18626]

    fig = plt.figure()
    ax1 = fig.add_subplot(111)


    ax1.plot(data['Date'], data['Heating (kWh)'], color='darkorange')

    ax1.plot([spring_summer_points[0],spring_summer_points[0]], [0,50000], label = 'Spring/Summer Semester Start', color='blue')
    ax1.plot([spring_summer_points[1],spring_summer_points[1]], [0,50000], color='blue')
    ax1.plot([spring_summer_points[2],spring_summer_points[2]], [0,50000], color='blue')
    ax1.plot([fall_points[0],fall_points[0]], [0,50000], label = 'Fall Semester Start', color='red')
    ax1.plot([fall_points[1],fall_points[1]], [0,50000], color='red')
    ax1.plot([fall_points[2],fall_points[2]], [0,50000], color='red')
    ax1.plot([fall_points[3],fall_points[3]], [0,50000], color='red')
    ax1.plot([winter_points[0],winter_points[0]], [0,50000], label = 'Winter Semester Start', color='green')
    ax1.plot([winter_points[1],winter_points[1]], [0,50000], color='green')
    ax1.plot([winter_points[2],winter_points[2]], [0,50000], color='green')

    ax1.set_xlabel('Date')
    ax1.set_ylabel('Heating (kWh)', color='darkorange')
    plt.xticks(rotation = 45)

    ax2 = ax1.twinx()
    ax2.plot(data['Date'], data['Cooling (kWh)'], color='tan')
    ax2.set_ylabel('Cooling (kWh)', color='tan')


    plt.title('Building Heating and Cooling Trends Over Time')
    ax1.legend(loc=1)

    plt.show()
    return

def electricity_gas_combined(data):
    spring_summer_points = [18019, 18385, 18748]
    fall_points = [17775, 18138, 18505, 18872]
    winter_points = [17897, 18260, 18626]

    fig = plt.figure()
    ax1 = fig.add_subplot(111)


    ax1.plot(data['Date'], data['Electricity (kWh)'], color='darkorange')

    ax1.plot([spring_summer_points[0],spring_summer_points[0]], [0,50000], label = 'Spring/Summer Semester Start', color='blue')
    ax1.plot([spring_summer_points[1],spring_summer_points[1]], [0,50000], color='blue')
    ax1.plot([spring_summer_points[2],spring_summer_points[2]], [0,50000], color='blue')
    ax1.plot([fall_points[0],fall_points[0]], [0,50000], label = 'Fall Semester Start', color='red')
    ax1.plot([fall_points[1],fall_points[1]], [0,50000], color='red')
    ax1.plot([fall_points[2],fall_points[2]], [0,50000], color='red')
    ax1.plot([fall_points[3],fall_points[3]], [0,50000], color='red')
    ax1.plot([winter_points[0],winter_points[0]], [0,50000], label = 'Winter Semester Start', color='green')
    ax1.plot([winter_points[1],winter_points[1]], [0,50000], color='green')
    ax1.plot([winter_points[2],winter_points[2]], [0,50000], color='green')

    ax1.set_xlabel('Date')
    ax1.set_ylabel('Electricity (kWh)', color='darkorange')
    plt.xticks(rotation = 45)

    ax2 = ax1.twinx()
    ax2.plot(data['Date'], data['Nat Gas (kWh)'], color='tan')
    ax2.set_ylabel('Natural Gas (kWh)', color='tan')


    plt.title('Electricity and Natural Gas Trends Over Time')
    ax1.legend(loc=1)

    plt.show()
    return

def yearly_all_combined(data):
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
    return

def months_weeks_all(data):
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
    return

def covid_shutdown(data):

    data2019_extended= data[data['Date'].dt.year == 2019]
    data2020_extended= data[data['Date'].dt.year == 2020]
    data2021_extended= data[data['Date'].dt.year == 2021]

    data2019 = data2019_extended.head(150)
    data2020 = data2020_extended.head(150)
    data2021 = data2021_extended.head(150)

    array_2019 = data2019.values
    array_2021 = data2021.values
    list_heat_avg, list_cool_avg, list_electricity_avg, list_gas_avg, list_water_avg = [], [], [], [], []
    row_number = 0
    for row in array_2019:
        heating_2019, cooling_2019, electricity_2019, nat_gas_2019, water_2019 = row[1], row[2], row[3], row[4], row[5]
        heating_2021, cooling_2021, electricity_2021, nat_gas_2021, water_2021 = array_2021[row_number][1], array_2021[row_number][2], array_2021[row_number][3], array_2021[row_number][4], array_2021[row_number][5]
        list_heat_avg.append((heating_2019 + heating_2021)//2)
        list_cool_avg.append((cooling_2019 + cooling_2021)//2)
        list_electricity_avg.append((electricity_2019 + electricity_2021)//2)
        list_gas_avg.append((nat_gas_2019 + nat_gas_2021)//2)
        list_water_avg.append((water_2019 + water_2021)//2)
        row_number =+ 1

    dates = data2020['Date']
    averages = pandas.DataFrame()
    averages['Date'] = dates
    averages['Heating'] = list_heat_avg
    averages['Cooling'] = list_cool_avg
    averages['Electricity'] = list_electricity_avg
    averages['Nat Gas'] = list_gas_avg
    averages['Water'] = list_water_avg


    ax1 = plt.subplot(511)
    ax2 = plt.subplot(512)
    ax3 = plt.subplot(513)
    ax4 = plt.subplot(514)
    ax5 = plt.subplot(515)

    covid_closure = [18335,18335]

    ax1.plot(averages['Date'], averages['Heating'], color='darkorange', label = 'Heating Average', linewidth = 1)
    ax1.plot(data2020['Date'], data2020['Heating (kWh)'], color='darkorange', linewidth = 2 , label = 'Heating 2020')
    ax1.plot(covid_closure, [0,50000], label = 'March 13 2020 - Classes Moved Online', color='blue', linewidth = 3)


    ax2.plot(averages['Date'], averages['Cooling'], color='red', label = 'Cooling Average', linewidth = 1)
    ax2.plot(data2020['Date'], data2020['Cooling (kWh)'], color='red', linewidth = 2 , label = 'Cooling 2020')
    ax2.plot(covid_closure, [0,50000], label = 'March 13 2020 - Classes Moved Online', color='blue', linewidth = 3)

    ax3.plot(averages['Date'], averages['Electricity'], color='gold', label = 'Electricity Average', linewidth = 1)
    ax3.plot(data2020['Date'], data2020['Electricity (kWh)'], color='gold', linewidth = 2 , label = 'Electricity 2020')
    ax3.plot(covid_closure, [0,50000], label = 'March 13 2020 - Classes Moved Online', color='blue', linewidth = 3)

    ax4.plot(averages['Date'], averages['Nat Gas'], color='tan', label = 'Natural Gas Average', linewidth = 1)
    ax4.plot(data2020['Date'], data2020['Nat Gas (kWh)'], color='tan', linewidth = 2 , label = 'Natural Gas 2020')
    ax4.plot(covid_closure, [0,50000], label = 'March 13 2020 - Classes Moved Online', color='blue', linewidth = 3)

    ax5.plot(averages['Date'], averages['Water'], color='lightcoral', label = 'Domestic Water Average', linewidth = 1)
    ax5.plot(data2020['Date'], data2020['Domestic Water (m3)'], color='lightcoral', linewidth = 2 , label = 'Domestic Water 2020')
    ax5.plot(covid_closure, [0,50000], label = 'March 13 2020 - Classes Moved Online', color='blue', linewidth = 3)

    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()
    ax5.legend()

    ax1.set_ylim([0,30000])
    ax2.set_ylim([2500,10000])
    ax3.set_ylim([8000,14000])
    ax4.set_ylim([4000,13000])
    ax5.set_ylim([0,25])

    plt.show()
    return


data = pandas.read_csv('building1.csv', sep=',', header=0)
data.head()

data['Date'] = pandas.to_datetime(data['Date'])

heat_cooling_combined(data)
electricity_gas_combined(data)
yearly_all_combined(data)
months_weeks_all(data)
covid_shutdown(data)

