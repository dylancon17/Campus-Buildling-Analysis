# Code Here

import pandas
import matplotlib.pyplot as plt
import numpy as np

def heat_cooling_combined(data):

    #Gives the x coordinates for the start of each semester.
    spring_summer_points = [18019, 18385, 18748]
    fall_points = [17775, 18138, 18505, 18872]
    winter_points = [17897, 18260, 18626]

    #Sets up a graph, creates a subplot to plot multiple y-axis scales on the same graph
    fig = plt.figure()
    ax1 = fig.add_subplot(111)


    ax1.plot(data['Date'], data['Heating (kWh)'], color='darkorange')

    #Plots a vertical line for the start of each semester
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

    #Organizes the axes
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Heating (kWh)', color='darkorange')
    plt.xticks(rotation = 45)

    #Sets up a second set of data that has it's own independent scale
    ax2 = ax1.twinx()
    ax2.plot(data['Date'], data['Cooling (kWh)'], color='tan')
    ax2.set_ylabel('Cooling (kWh)', color='tan')

    #Title and legend
    plt.title('Figure 1: Building Heating and Cooling Trends Over Time')
    ax1.legend(loc=1)

    plt.show()
    return

def electricity_gas_combined(data):
    
    #Gives the x coordinates for the start of each semester.
    spring_summer_points = [18019, 18385, 18748]
    fall_points = [17775, 18138, 18505, 18872]
    winter_points = [17897, 18260, 18626]

    #Sets up a graph, creates a subplot to plot multiple y-axis scales on the same graph
    fig = plt.figure()
    ax1 = fig.add_subplot(111)


    ax1.plot(data['Date'], data['Electricity (kWh)'], color='darkorange')

    #Plots a vertical line for the start of each semester
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

    #Organizes the axes
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Electricity (kWh)', color='darkorange')
    plt.xticks(rotation = 45)

    #Sets up a second set of data that has it's own independent scale
    ax2 = ax1.twinx()
    ax2.plot(data['Date'], data['Nat Gas (kWh)'], color='tan')
    ax2.set_ylabel('Natural Gas (kWh)', color='tan')

    #Title and legend
    plt.title('Figure 2: Electricity and Natural Gas Trends Over Time')
    ax1.legend(loc=1)

    plt.show()
    return

def yearly_all_combined(data):
    # helper variables to specify the years of interest and the columns.
    years = [2018, 2019, 2020, 2021]
    cols = ['Heating (kWh)', 'Cooling (kWh)', 'Electricity (kWh)', 'Nat Gas (kWh)', 'Domestic Water (m3)']

    # Create a new figure with the number of subplots equal to the number of cols
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
    
    #Creates a title at the top of the page
    plt.suptitle('Figure 3: Annual Energy Usage Patterns')

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

    #Creates a title centered above and between the two subplots
    plt.suptitle('Figure 4: Weekly Electricity and Monthly Heating/Cooling Trends')

    # Show the plot
    plt.show()
    return

def covid_shutdown(data):

    #Break the data into each year, only 2019, 2020 and 2021 are used as 2018 does not have spring data
    data2019_extended= data[data['Date'].dt.year == 2019]
    data2020_extended= data[data['Date'].dt.year == 2020]
    data2021_extended= data[data['Date'].dt.year == 2021]

    #Keeps only the first 150 days of each year. This is to help focus in on March rather than the whole year
    data2019 = data2019_extended.head(150)
    data2020 = data2020_extended.head(150)
    data2021 = data2021_extended.head(150)

    #Converts to an array for easier data manipulation
    array_2019 = data2019.values
    array_2021 = data2021.values

    list_heat_avg, list_cool_avg, list_electricity_avg, list_gas_avg, list_water_avg = [], [], [], [], []
    row_number = 0

    #Iterates through the first 150 days in a year
    for row in array_2019:
        #Pulls the values for each column in 2019 and 2021
        heating_2019, cooling_2019, electricity_2019, nat_gas_2019, water_2019 = row[1], row[2], row[3], row[4], row[5]
        heating_2021, cooling_2021, electricity_2021, nat_gas_2021, water_2021 = array_2021[row_number][1], array_2021[row_number][2], array_2021[row_number][3], array_2021[row_number][4], array_2021[row_number][5]
        #Averages those values to create an daily average for comparison to 2020
        list_heat_avg.append((heating_2019 + heating_2021)//2)
        list_cool_avg.append((cooling_2019 + cooling_2021)//2)
        list_electricity_avg.append((electricity_2019 + electricity_2021)//2)
        list_gas_avg.append((nat_gas_2019 + nat_gas_2021)//2)
        list_water_avg.append((water_2019 + water_2021)//2)

        row_number =+ 1

    #Pulls just the dates from 2020
    dates = data2020['Date']

    #Creates an empty data frame and then fills it with the 2019/2021 averages 
    averages = pandas.DataFrame()
    averages['Date'] = dates
    averages['Heating'] = list_heat_avg
    averages['Cooling'] = list_cool_avg
    averages['Electricity'] = list_electricity_avg
    averages['Nat Gas'] = list_gas_avg
    averages['Water'] = list_water_avg

    #Sets up 5 graphs aligned vertically
    ax1 = plt.subplot(511)
    ax2 = plt.subplot(512)
    ax3 = plt.subplot(513)
    ax4 = plt.subplot(514)
    ax5 = plt.subplot(515)

    #The x coordinate for the middle of March 2020
    covid_closure = [18335,18335]

    #Plots heating average, heating 2020 and a vertical line for the campus closure
    ax1.plot(averages['Date'], averages['Heating'], color='darkorange', label = 'Heating Average', linewidth = 1)
    ax1.plot(data2020['Date'], data2020['Heating (kWh)'], color='darkorange', linewidth = 2 , label = 'Heating 2020')
    ax1.plot(covid_closure, [0,50000], label = 'Classes Moved Online', color='blue', linewidth = 3)

    #Plots cooling average, cooling 2020 and a vertical line for the campus closure
    ax2.plot(averages['Date'], averages['Cooling'], color='red', label = 'Cooling Average', linewidth = 1)
    ax2.plot(data2020['Date'], data2020['Cooling (kWh)'], color='red', linewidth = 2 , label = 'Cooling 2020')
    ax2.plot(covid_closure, [0,50000], label = 'Classes Moved Online', color='blue', linewidth = 3)

    #Plots electricity average, electricity 2020 and a vertical line for the campus closure
    ax3.plot(averages['Date'], averages['Electricity'], color='gold', label = 'Electricity Average', linewidth = 1)
    ax3.plot(data2020['Date'], data2020['Electricity (kWh)'], color='gold', linewidth = 2 , label = 'Electricity 2020')
    ax3.plot(covid_closure, [0,50000], label = 'Classes Moved Online', color='blue', linewidth = 3)

    #Plots nat gas average, nat gas 2020 and a vertical line for the campus closure
    ax4.plot(averages['Date'], averages['Nat Gas'], color='tan', label = 'Natural Gas Average', linewidth = 1)
    ax4.plot(data2020['Date'], data2020['Nat Gas (kWh)'], color='tan', linewidth = 2 , label = 'Natural Gas 2020')
    ax4.plot(covid_closure, [0,50000], label = 'Classes Moved Online', color='blue', linewidth = 3)

    #Plots water average, water 2020 and a vertical line for the campus closure
    ax5.plot(averages['Date'], averages['Water'], color='lightcoral', label = 'Domestic Water Average', linewidth = 1)
    ax5.plot(data2020['Date'], data2020['Domestic Water (m3)'], color='lightcoral', linewidth = 2 , label = 'Domestic Water 2020')
    ax5.plot(covid_closure, [0,50000], label = 'Classes Moved Online', color='blue', linewidth = 3)

    #Adds a legend to each graph
    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()
    ax5.legend()

    #Sets the upper and lower y-bounds for each graph to increase the readability
    ax1.set_ylim([0,30000])
    ax2.set_ylim([2500,10000])
    ax3.set_ylim([8000,14000])
    ax4.set_ylim([4000,13000])
    ax5.set_ylim([0,25])

    #Title and x-label
    plt.suptitle('Figure 5: A Comparison between Energy Use in the 2020 Campus Closure and Other Years')
    ax5.set_xlabel('Date')

    plt.show()
    return

def comparing_buildings(data1, data2):
    
    #Sets up 5 vertically aligned graphs
    fig = plt.figure()
    ax1 = fig.add_subplot(511)
    ax2 = fig.add_subplot(512)
    ax3 = fig.add_subplot(513)
    ax4 = fig.add_subplot(514)
    ax5 = fig.add_subplot(515)

    #Plots buildling 1 and buildling 2 stats for each category into a differnt graph
    ax1.plot(data1['Date'], data1['Heating (kWh)'], color='orange', label = 'Building 1')
    ax1.plot(data1['Date'], data2['Heating (kWh)'], color='red', label = 'Building 2')
    ax2.plot(data1['Date'], data1['Cooling (kWh)'], color='orange')
    ax2.plot(data1['Date'], data2['Cooling (kWh)'], color='red')
    ax3.plot(data1['Date'], data1['Electricity (kWh)'], color='orange')
    ax3.plot(data1['Date'], data2['Electricity (kWh)'], color='red')
    ax4.plot(data1['Date'], data1['Nat Gas (kWh)'], color='orange')
    ax4.plot(data1['Date'], data2['Nat Gas (kWh)'], color='red')
    ax5.plot(data1['Date'], data1['Domestic Water (m3)'], color='orange')
    ax5.plot(data1['Date'], data2['Domestic Water (m3)'], color='red')
    
    #Adds y-labels
    ax1.set_ylabel('Heating(kwh)')
    ax2.set_ylabel('Cooling(kwh)')
    ax3.set_ylabel('Electricity(kwh)')
    ax4.set_ylabel('Natural Gas(kWh)')
    ax5.set_ylabel('Domestic Water(m3)')

    #Adds a legend to only one graph as it applies to all
    ax1.legend()

    #Title and x-label
    ax5.set_xlabel('Date')
    ax1.set_title('Figure 6: A Comparison of Building 1 and Building 2')
    
    plt.show()
    return

#Imports buildling 1
data1 = pandas.read_csv('building1.csv', sep=',', header=0)
data1.head()
data1['Date'] = pandas.to_datetime(data1['Date'])

#Imports building 2
data2 = pandas.read_csv('building2.csv', sep=',', header=0)
data2.head()
data2['Date'] = pandas.to_datetime(data2['Date'])

heat_cooling_combined(data1) #For Q1
electricity_gas_combined(data1) #For Q1
yearly_all_combined(data1) #For Q1
months_weeks_all(data1) #For Q1
covid_shutdown(data1) #For Q2
comparing_buildings(data1, data2) #For Q3

