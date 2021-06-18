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
    vote_count2 = {}   # Bonus analysis: tally by candidate and county

    # Read and process each row
    for row in csvreader:

        # Count votes for each candidate
        if row[1] in vote_count.keys():   # Check if candidate is in vote_count
            vote_count[row[1]] += 1
        else:                             # Add new candidate to vote_count
            vote_count[row[1]] = 1

print(vote_count)
print()

# Initialize results variables
total_count = 0

# Find max value in vote_count
max_votes = max(vote_count.values())

# Tabulate all votes and identify winner
for candidate in vote_count.keys():
    total_count += vote_count[candidate]
    if vote_count[candidate] == max_votes:
        winner = candidate

# List to hold analysis output text
ndash = 30
output = ["Election Results",
        "-" * ndash,
        "Total votes: " + f"{total_count:,}",
        "-" * ndash]
for candidate in sorted(vote_count.keys()):
    pcnt_vote = vote_count[candidate] / total_count
    output.append(f"{candidate}: " + f"{pcnt_vote:.3%} (" + f"{vote_count[candidate]:,})")
output.append("-" * ndash)
output.append(f"Winner: {winner}")
output.append("-" * ndash)

# Print results to console
for row in output:
    print(row)





    

