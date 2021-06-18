import os
import csv

# Set path to input file
csvpath = os.path.join("Resources", "election_data.csv")

# Open filehandle
with open(csvpath, 'r') as csvfile:
    
    # Convert filehandle to csv.reader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    csv_header = next(csvreader)

    # Initialize target variables
    vote_count = {}
    vote_count2 = {}   # Bonus analysis: tally by candidate and county

    # Read and process each row
    for row in csvreader:

        # Count votes for each candidate
        if row[1] in vote_count.keys():
            vote_count[row[1]] += 1
        else:
            vote_count[row[1]] = 1

print(vote_count)

