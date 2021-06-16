import os
import csv

# Format currency with negative sign in front of dollar sign
def format_currency(value):
    curr_str = f"${abs(value):,.2f}"
    if value < 0:
        curr_str = "-" + curr_str
    return curr_str


# Set path to input file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open filehandle
with open(csvpath, 'r') as csvfile:
    
    # Convert filehandle to csv.reader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    csv_header = next(csvreader)

    # Initialize target variables
    month_count = 0
    net_pl = 0.00
    gr_incr = ["mmm-yyyy", 0.00]
    gr_decr = ["mmm-yyyy", 0.00]

    # Read and process each row
    for row in csvreader:

        # Convert current monthly profit/loss to float
        row[1] = float(row[1])

        # Update record count
        month_count += 1

        # Update total profit/loss
        net_pl += row[1]

        # Test and set max monthly increase and max decrease
        if row[1] > gr_incr[1]:
            gr_incr = [row[0], row[1]]
        if row[1] < gr_decr[1]:
            gr_decr = [row[0], row[1]]

# Calculate mean monthly profit/loss
mean_change = net_pl / month_count

# List to hold analysis output text
output = ["Financial Analysis",
    "--------------------------------------------------------------",
    f"Total months: {month_count}",
    f"Net profit/loss: {format_currency(net_pl)}",
    f"Average monthly profit/loss: {format_currency(mean_change)}",
    f"Greatest monthly profit {format_currency(gr_incr[1])} occurred during {gr_incr[0]}",
    f"Greatest monthly loss {format_currency(gr_decr[1])} occurred during {gr_decr[0]}",
    ]


# Print results to console
for row in output:
    print(row)

# Output results to text file
outfile = os.path.join('Analysis', "PyBank_output.txt")
with open(outfile, 'w') as file1:
    for row in output:
        file1.write(f"{row}\n")





