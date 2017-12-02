import csv
import os

#Pathing to Data files
datafile1 = os.path.join('budget_data_1.csv')


months = []
revenue_change = []

#Populate lists
#first data file
with open(datafile1, newline="") as data1:
	reader = csv.reader(data1, delimiter=",")
	next(reader) #skips header
	for row in reader:
		#grab month
		months.append(row[0])

		#revenue change
		revenue_change.append(row[1])


revenue_change = [int(x) for x in revenue_change]

print("Financial Analysis" + "\n" + "------------------" + "\n")
#Total number of months included in the dataset
print("Total months in data set: ", str(len(months)))
#Total amount of revenue gained over period
print("Total revenue over period: $", sum(revenue_change) )
#Avg change in revenue between months
rcl= len(revenue_change)
difflist = [revenue_change[i+1]-revenue_change[i] for i in range(rcl-1)]
avgchange = sum(difflist)/len(difflist)
print("Average change in revenue between months: $" +str(avgchange))
#Greatest increase
greatest_increase_date = months[revenue_change.index(max(revenue_change))]
print("Greatest increase in revenue: " + greatest_increase_date + " " + str(max(revenue_change)))
#Greatest decrease
greatest_decrease_date = months[revenue_change.index(min(revenue_change))]
print("Greatest decreasse in revenue: " + greatest_decrease_date + " " +str(min(revenue_change)))

#set path for output
output_file = os.path.join("output.txt")
#open and write output file
file = open("output1.txt", "w")
file.write("Financial Analysis" + "\n" + "------------------" + "\n")
file.write("Total months in data set: " +str(len(months))+ "\n")
file.write("Total revenue over period: $" +str(sum(revenue_change))+ "\n")
file.write("Average change in revenue between months: $" +str(avgchange)+ "\n")
file.write("Greatest increase in revenue: $" + str(max(revenue_change))+"\n")
file.write("Greatest decreasse in revenue: $" + str(min(revenue_change))+ "\n")
file.close()
