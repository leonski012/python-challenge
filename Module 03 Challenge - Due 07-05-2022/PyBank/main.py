#import modules
import os
import csv

#file path for csv 
pyBank_csv = os.path.join("Resources", "budget_data.csv")

#file to hold output of PyBank analysis
output_file = os.path.join("budget_analysis.txt")

#print(pyBank_csv)

#create lists to store data
month = []
net_total = []

#define running totals
month_count = 0
total_profit_loss = 0


#read in csv file
with open(pyBank_csv, 'r', encoding="utf-8") as csvFile:

    #split data by commas
    csvReader = csv.reader(csvFile, delimiter=",")

    #print(csvReader)
    
    #read and print header
    header = next(csvReader)
    #print(f"Header: {header}")

    #for loop to go through each row of data after header
    for row in csvReader:
        
        #append each month to month and profit/loss to profit/loss
        month.append(row[0])
        net_total.append(int(row[1]))
    
    #the total number of months and net profit/loss included in the dataset
    month_count = len(month)
    total = sum(net_total)
    #print(month_count)
    #print(sum(net_total))

    #variables for loops
    x = 1
    y = 0

    #Average change
    average_change = (net_total[1] - net_total[0])
    
    monthly_changes = []
    
    #The changes in "Profit/Losses" over the entire period
    for months in range(month_count - 1):
        average_change = (net_total[x] - net_total[y])
        monthly_changes.append(int(average_change))
        x += 1
        y += 1

        #The average of those changes
        average_monthly_change = round(sum(monthly_changes)/(month_count - 1),2)
        
        #find max and min change
        max_change = max(monthly_changes)
        min_change = min(monthly_changes)

         #finding max and min months from index
        max_month = monthly_changes.index(max_change)
        min_month = monthly_changes.index(min_change)

        #The greatest increase and decrease in profits (date and amount) over the entire period
        max_change_month = month[max_month + 1]
        min_change_month = month[min_month + 1]

 # print out output to terminal
output = (
    f"\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Month: {month_count}\n"
    f"Total: ${total}\n"
    f"Average Change: ${average_monthly_change}\n"
    f"Greatest Increase in Profits: {max_change_month} (${max_change})\n"
    f"Greatest Decrease in Profits: {min_change_month} (${min_change})\n"
)
print(output)

#export output file to text file
with open(output_file, "w") as text_file:
    text_file.write(output)