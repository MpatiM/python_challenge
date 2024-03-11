#Importing the necessary modules/libraries
import os
import csv

#Creating an object out of the CSV file
election_data = os.path.join("Resources", "election_data.csv")

# Initialize Variables
total_votes = 0
candidate_list = {}

#Opening and reading the CSV file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)

    # For each row after header and first row
    for row in csvreader:
        
        # Total Votes
        total_votes += 1
        
        # Append new values to dictionary and add to voter count
        if str(row[2]) not in candidate_list.keys():
            candidate_list[str(row[2])] = 1
            
        else:
            candidate_list[str(row[2])] += 1

    # Calculate percentage
    perc = []
    
    for vote in candidate_list.values():
        val = round((vote/total_votes)*100, 3)
        perc.append(val)
    
    # Candidate Winner
    popular = max(candidate_list.values())
    
    for key, value in candidate_list.items():
        if value == popular:
            winner = key


# Displaying Information
print("Election Results")
print("\n--------------------\n")

print(f"Total Votes: {total_votes}")
print("\n--------------------\n")    

for i in range(len(candidate_list)):
    print("{}: {}% ({})\n".format(list(candidate_list.keys())[i], perc[i], list(candidate_list.values())[i]))

print("\n--------------------\n") 

print("Winner: {}".format(winner))
print("\n--------------------\n") 


# Export results to text file
output = os.path.join("analysis", "results.txt")

# Open and write results to text file
with open(output, 'w') as txtfile:
    print("Election Results", file=txtfile)
    print("\n--------------------\n", file=txtfile)

    print(f"Total Votes: {total_votes}", file=txtfile)
    print("\n--------------------\n", file=txtfile)    

    for i in range(len(candidate_list)):
        print("{}: {}% ({})\n".format(list(candidate_list.keys())[i], perc[i], list(candidate_list.values())[i]), file=txtfile)

    print("\n--------------------\n", file=txtfile) 

    print("Winner: {}".format(winner), file=txtfile)
    print("\n--------------------\n", file=txtfile) 
