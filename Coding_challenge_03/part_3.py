# 3. Working with CSV
# Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions from quasi-continuous daily measurements at Mauna Loa, Hawaii dataset, obtained from here (https://github.com/datasets/co2-ppm-daily/tree/master/data).
#
# Using Python (csv) calculate the following:
#
# Annual average for each year in the dataset.
# Minimum, maximum and average for the entire dataset.
# Seasonal average if Spring (March, April, May), Summer (June, July, August), Autumn (September, October, November) and Winter (December, January, February).
# Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.

import csv
import os

#1st I'll create a list called years containing a single entry for each year in the CSV file.
years = []
with open("co2__ppm_daily.csv") as co2_csv:
    next(co2_csv) #skip first line
    for row in csv.reader(co2_csv):
        year = row[0].split('-')[0]
        if year not in years:
            years.append(year)
    print(years)
    print(type(row[1]))


#In the code chunk below, for every year in my years list, I open the csv file, then add all the values from that year
#to a variable called total_co2. Each time I add the ppm to the total I also add a count to the 'days' variable.
#Once all the rows have been tested, I take the average of the year's ppm by dividing the total_co2 by the number of days.
#Finaly, for each iteration of the loop the average co2 ppm is appened to the list called avg_ppm_per_year.
avg_ppm_per_year= []
for year in years:
    total_co2 = 0
    days=0
    with open("co2__ppm_daily.csv") as co2_csv:
        next(co2_csv)  # skip first line
        for row in csv.reader(co2_csv):
            if year == row[0].split('-')[0]:
                total_co2 += float(row[1])
                days += 1
    avg_co2 = total_co2/days
    avg_ppm_per_year.append(avg_co2)
print(avg_ppm_per_year)

#To print the min, max, and mean co2 values in the entire CSV file:
all_values = []
with open("co2__ppm_daily.csv") as co2_csv:
    next(co2_csv) #skip first line
    for row in csv.reader(co2_csv):
        all_values.append(float(row[1]))

print('Min value: ' + str(min(all_values)))
print('Max value: ' + str(max(all_values)))
avg_all_ppm = sum(all_values)/len(all_values)
print('Total mean: ' + str(avg_all_ppm))

# To print the seasonal averages
# First I create a blank list for each season
spring = []
summer = []
fall = []
winter = []

#I then test the month values of each row to determine which season it is in, then add the ppm values of that row
#to the list for that season
with open("co2__ppm_daily.csv") as co2_csv:
    next(co2_csv) #skip first line
    for row in csv.reader(co2_csv):
        if float(row[0].split('-')[1]) == 3.0 or float(row[0].split('-')[1]) == 4.0 or float(row[0].split('-')[1]) == 5.0:
            spring.append(float(row[1]))
        elif float(row[0].split('-')[1]) == 6.0 or float(row[0].split('-')[1]) == 7.0 or float(row[0].split('-')[1]) == 8.0:
            summer.append(float(row[1]))
        elif float(row[0].split('-')[1]) == 9.0 or float(row[0].split('-')[1]) == 10.0 or float(row[0].split('-')[1]) == 11.0:
            fall.append(float(row[1]))
        elif float(row[0].split('-')[1]) == 12.0 or float(row[0].split('-')[1]) == 1.0 or float(row[0].split('-')[1]) == 2.0:
            winter.append(float(row[1]))

#Once I have the complete list for each season I calcualte the mean of each list and print the values.
    avg_spring = sum(spring)/len(spring)
    avg_summer = sum(summer) / len(summer)
    avg_fall = sum(fall) / len(fall)
    avg_winter = sum(winter) / len(winter)
print('Spring average: ' + str(avg_spring))
print('Summer average: ' + str(avg_summer))
print('Fall average: ' + str(avg_fall))
print('Winter average: ' + str(avg_winter))

#Below I subtact the total mean of all ppm values from the ppm value of each row, then add each of those diffrences
# to a list called 'anomaly'. I then print the list of all anomalies from the mean.
anomaly = []
with open("co2__ppm_daily.csv") as co2_csv:
    next(co2_csv) #skip first line
    for row in csv.reader(co2_csv):
        item_anomaly = float(row[1]) - avg_all_ppm
        anomaly.append(item_anomaly)
print(anomaly)
