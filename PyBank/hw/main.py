import os
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")
total_months = 0
total_profit = []
monthly_profit_change = []
min=0
max=0

# Open csv
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header labels
    csvheader = next(csvreader)

    # Iterate through the rows in the stored file contents
    for row in csvreader:
        # Calculate total months
        total_months+=1
        # create a list total profit
        total_profit.append(int(row[1]))

    # Iterate through the profits
    for i in range(len(total_profit) - 1):

        # difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i + 1] - total_profit[i])
        change = total_profit[i + 1] - total_profit[i]
        # Calculate max profit
        if change > 0:
            if max<change:
                max = change
                m=row[0]
        # Calculate the Max loss
        if(change<0):
            if(min>change):
                min=change
                n=row[0]

    total_average=round(sum(monthly_profit_change)/len(monthly_profit_change),2)
    print(f" Total Months = {total_months}")
    print(f" Total Amount = ${sum(total_profit)}")
    print(f" Average  Change: ${total_average}")
    print(f"Greatest Increase in Profits: {m} (${max})")
    print(f"Greatest decrease in Profits: {n} (${min})")


file = open("output.txt","w")
file.write("Financial Analysis" + "\n")
file.write("...................................................................................." + "\n")
file.write(f" Total Months = {total_months}\n")
file.write(f" Total Amount = ${sum(total_profit)}\n")
file.write(f" Average  Change: ${total_average}\n")
file.write(f"Greatest Increase in Profits: {m} (${max})\n")
file.write(f"Greatest decrease in Profits: {n} (${min})\n")
file.close()

