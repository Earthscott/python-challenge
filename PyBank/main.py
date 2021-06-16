import os
import csv

# Set path to input file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Open filehandle
with open(csvpath, 'r') as csvfile:
    
    # Convert filehandle to csv.reader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    csv_header = next(csvreader)

    # Initialize target variables
    month_count = 0.0
    net_pl = 0
    prev_pl = 0
    gr_incr = ["mmm-yyyy", 0.0]
    gr_decr = ["mmm-yyyy", 0.0]

    # Read and process each row
    for row in csvreader:

        # Update record count
        month_count += 1

        # Update total profit/loss
        net_pl += row[1]

        





