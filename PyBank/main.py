#modules
import os  
import csv

#import csv
budget_data = os.path.join('.', 'Resources', 'budget_data.csv')

#declaring variables
months_total = 0
net_total = 0
last_value = 0
change_total = 0
change_average = 0
greatest_increase = 0
greatest_decrease = 0
first = True
greatest_increase_month = ""
greatest_decrease_month = ""

#read the csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skip header
    csv_header = next(csvfile)

    #for loop to count rows and add net total
    for rows in csvreader:
        months_total += 1
        net_total += int(rows[1])
        
        #checking for first value
        if first: 
            first = False

        #calculating change compared to last
        else:
            change_total+=int(rows[1]) - last_value
            #check if greatest increase found
            if((int(rows[1]) - last_value) > greatest_increase):
                #if so, store as greatest increase value
                greatest_increase = int(rows[1]) - last_value
                greatest_increase_month = rows[0]
            #check if greatest decrease found
            if((int(rows[1]) - last_value) < greatest_decrease):
                #if so, store as greatest decrease value
                greatest_decrease = int(rows[1]) - last_value
                greatest_decrease_month = rows[0]
        #capture last value
        last_value = int(rows[1])

#calculating average change    
change_average = change_total / (months_total-1) 

#print statements
print("Financial Analysis")
print("----------------")
print(f"Total Months:{months_total}")
print(f"Net Total: ${net_total}")    
print(f"Average Change: ${round(change_average, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

#write to file
with open("pybank.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------\n")
    file.write(f"Total Months:{months_total}\n")
    file.write(f"Net Total: ${net_total}\n")    
    file.write(f"Average Change: ${round(change_average, 2)}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
    