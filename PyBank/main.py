#Modules
import os
import sys
import csv
import statistics
csvpath = os.path.join('budget_data_2.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)
    row_count = sum(1 for row in csvreader)
    print("Financial Analysis")
    print ("==================================")
    print("Total Months: ", row_count)
    print("Total Revenue: ")
    print("Average Revenue Change: ")
    print("reatest Increase in Revenue: ")
    print("Greatest Decrease in Revenue: ")


f= open("PyBank_main.txt","w+")
f.write("Financial Analysis")
f.write('\r\n')
f.write("==================================")
f.write('\r\n')
f.write("Total Months: ")
f.write(str(row_count))
f.write('\r\n')
f.write("Total Revenue ")
f.write('\r\n')
f.write("Greatest Increase in Revenue ")
f.write('\r\n')
f.write("Greatest Decrease in Revenue ")
f.write('\r\n')
f.close() 

print('\r\n')
print('\r\n')
print("The operation has been completed.")