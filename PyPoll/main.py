import os
import csv

# Input file has columns: Voter ID, County, Candidate
# Each record represents one vote for the identified candidate
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

    # Read and process each row
    for row in csvreader:

        # Count votes for each candidate
        if row[2] in vote_count.keys():   # Check if candidate is in the keys vote_count
            vote_count[row[2]] += 1
        else:                             # Add new candidate to vote_count
            vote_count[row[2]] = 1

# Sum total votes
total_count = sum(vote_count.values())

# Find max value in vote_count and identify winner
max_votes = max(vote_count.values())
for candidate in vote_count.keys():
    if vote_count[candidate] == max_votes:
        winner = candidate

# List to hold analysis output text
ndash = 30    # Number of dashes to print horizontal line
output = ["Election Results",
        "-" * ndash,
        "Total votes: " + f"{total_count:,}",
        "-" * ndash]
for candidate in sorted(vote_count.keys()):  # Output results for each candidate
    pcnt_vote = vote_count[candidate] / total_count   # Calculate percentage of total votes
    output.append(f"{candidate}: " + f"{pcnt_vote:.3%} (" + f"{vote_count[candidate]:,})")
output.append("-" * ndash)
output.append(f"Winner: {winner}")
output.append("-" * ndash)

# Print results to console
for row in output:
    print(row)

# Output results to text file
outfile = os.path.join('Analysis', "PyPoll_output.txt")
with open(outfile, 'w') as file1:
    for row in output:
        file1.write(f"{row}\n")




    

