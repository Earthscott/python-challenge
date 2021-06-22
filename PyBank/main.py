import os
import csv

# Format float as currency with negative sign in front of dollar sign
def format_currency(value):
    curr_str = f"${abs(value):,.2f}"
    if value < 0:
        curr_str = "-" + curr_str
    return curr_str

# Input file has columns: Date, Profit/Losses
    # Date format "MMM-YYYY"
    # 'Profit/Losses' represents profit or loss during that month
    
# Set path to input file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open filehandle
with open(csvpath, 'r') as csvfile:
    
    # Convert filehandle to csv.reader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    next(csvreader)

    # Initialize target variables
    month_count = 0
    net_pl = 0.0
    prev_pl = 0.0
    delta_list = []
    gr_incr = ["mmm-yyyy", 0.00]
    gr_decr = ["mmm-yyyy", 0.00]

    # Read and process each row
    for row in csvreader:

        # Convert current monthly profit/loss to float
        pl = float(row[1])

        # Update record count
        month_count += 1

        # Update total profit/loss
        net_pl += pl

        # Calculate month-to-month difference in profit/loss
        if month_count > 1:                   # Skip first record
            delta = pl - prev_pl              # Calculate difference
            delta_list.append(delta)          # Add difference to list for mean calculation
            if delta > gr_incr[1]:            # Identify greatest increase and store mo/yr
                gr_incr = [row[0], delta]
            if delta < gr_decr[1]:            # Identify greatest decrease and store mo/yr
                gr_decr = [row[0], delta]
        
        # Store previous profit/loss for difference calculation
        prev_pl = pl

# Calculate mean of the month-to-month profit/loss differences
delta_mean = sum(delta_list) / len(delta_list)

# List to hold analysis output text
output = ["Financial Analysis",
    "-------------------------------------------------------------------------",
    f"Months in analysis: {month_count}",
    f"Net profit/loss: {format_currency(net_pl)}",
    f"Mean of month-to-month profit/loss differences: {format_currency(delta_mean)}",
    f"Greatest month-to-month profit/loss increase: {format_currency(gr_incr[1])}, {gr_incr[0]}",
    f"Greatest month-to-month profit/loss decrease: {format_currency(gr_decr[1])}, {gr_decr[0]}",]

# Print results to console
for row in output:
    print(row)

# Output results to text file
outfile = os.path.join('Analysis', "PyBank_output.txt")
with open(outfile, 'w') as file1:
    for row in output:
        file1.write(f"{row}\n")
