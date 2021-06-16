import os
import csv

# Set path to input file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open filehandle
with open(csvpath, 'r') as csvfile:
    
    # Convert filehandle to csv.reader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    csv_header = next(csvreader)

    # Initialize target variables
    month_count = 0.0
    net_pl = 0.0
    # prev_pl = 0.0
    gr_incr = ["mmm-yyyy", 0.0]
    gr_decr = ["mmm-yyyy", 0.0]

    # Read and process each row
    for row in csvreader:

        # Convert current profit/loss to float
        row[1] = float(row[1])

        # Update record count
        month_count += 1

        # Update total profit/loss
        net_pl += row[1]

        # Test and set max increase and max decrease
        if row[1] > gr_incr[1]:
            gr_incr = [row[0], row[1]]
        if row[1] < gr_decr[1]:
            gr_decr = [row[0], row[1]]

        


        





