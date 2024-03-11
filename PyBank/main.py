#Importing the necessary modules/libraries
import os
import csv

#Creating an object out of the CSV file
budget_data = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_amt = 0
value = 0
change = 0

dates = []
profits_losses = []

#Opening and reading the CSV file
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Reading the header row
    csv_header = next(csvfile)

    #Reading the first row 
    first_row = next(csvreader)
    total_months += 1
    net_amt += int(first_row[1])
    value = int(first_row[1])
    
    # For each row after header and first row
    for row in csvreader:
        # Dates list
        dates.append(row[0])
        
        # Calculate the change and then add to list of profits_losses
        change = int(row[1])-value
        profits_losses.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months += 1

        #Total net amount of "Profit/Losses over entire period"
        net_amt = net_amt + int(row[1])

    #Greatest increase in profits
    # Amount
    greatest_increase = max(profits_losses)
    # Date
    increase_index = profits_losses.index(greatest_increase)
    increase_date = dates[increase_index]

    #Greatest decrease in profits 
    # Amount
    greatest_decrease = min(profits_losses)
    # Date
    decrease_index = profits_losses.index(greatest_decrease)
    decrease_date = dates[decrease_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits_losses)/len(profits_losses)
    

#Displaying information
print("Financial Analysis")
print("\n------------------------------\n")

print(f"Total Months: {total_months}")

print(f"\nTotal: ${net_amt}")

print(f"\nAverage Change: ${round(avg_change,2)}")

print(f"\nGreatest Increase in Profits: {increase_date} (${greatest_increase})")

print(f"\nGreatest Decrease in Profits: {decrease_date} (${greatest_decrease})")


# Export results to text file
output = os.path.join("..", "analysis", "results.txt")

# Open and write results to text file
with open(output, 'w') as txtfile:
    print("Financial Analysis", file=txtfile)
    print("\n------------------------------\n", file=txtfile)

    print(f"Total Months: {total_months}", file=txtfile)

    print(f"\nTotal: ${net_amt}", file=txtfile)

    print(f"\nAverage Change: ${round(avg_change,2)}", file=txtfile)

    print(f"\nGreatest Increase in Profits: {increase_date} (${greatest_increase})", file=txtfile)

    print(f"\nGreatest Decrease in Profits: {decrease_date} (${greatest_decrease})", file=txtfile)

