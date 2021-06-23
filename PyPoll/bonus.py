import os
import csv
import copy
from prettytable import PrettyTable

# ====================================================
# Bonus analysis: Tally votes by county and candidate
# ====================================================

# Input file has columns: Voter ID, County, Candidate
# Each record represents one vote for the identified candidate
# Set path to input file
csvpath = os.path.join("Resources", "election_data.csv")

# Open filehandle
with open(csvpath, 'r') as csvfile:
    
    # Convert filehandle to csv.reader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    next(csvreader)

    # Initialize target variables
    vote_count2 = {}

    # Read and process each row
    for row in csvreader:

        # Count votes for each county by candidate
        if row[1] not in vote_count2.keys():           # Check if county is in the keys
            vote_count2[row[1]] = {}                   # Add new county to keys
        if row[2] not in vote_count2[row[1]].keys():   # Check if candidate is in subkeys for county
            vote_count2[row[1]][row[2]] = 1            # Add new candidate to county subkeys and count first vote
        else:                                          # County key and candidate subkey exist
            vote_count2[row[1]][row[2]] += 1           # Tally vote

# Create independent copy of dictionary
test_dict = copy.deepcopy(vote_count2)

# Throw a wrench in the works. Delete some items so a few county-candidate 
#    combinations are undefined. This forces the analysis to deal with 
#    undefined combinations of county/candidte.
del test_dict['Trandee']["O'Tooley"]
del test_dict['Trandee']['Li']
del test_dict['Queen']['Khan']
del test_dict['Bamoo']['Khan']

# List of unique counties
counties = sorted(test_dict.keys())

# Make list of unique candidates and tally total votes by county
candidate_set = set()
votes_bycounty = {}
# Note that 'candidate_dict' is a dictionary, not a value
for county, candidate_dict in test_dict.items():
    # Add only unique items to set 'candidates_set'
    candidate_set.update(candidate_dict.keys())
    # candidate_dict.values converted to list to allowing summing values
    votes_bycounty[county] = sum(list(candidate_dict.values()))

# Convert 'candidate_set' to sorted list
candidates = sorted(candidate_set)

# Tally total votes for each candidate
#    Initialize dictionary with count=0 for each candidate
votes_bycandidate = {key: 0 for key in candidates}
# Note that 'candidate_dict' is a dictionary, not a value
for candidate_dict in test_dict.values():
    for candidate in candidate_dict.keys():
        votes_bycandidate[candidate] += candidate_dict[candidate]

# Sum total votes in election
total_votes = sum(votes_bycounty.values())

# PrettyTable - "A simple Python library for easily displaying tabular data 
#    in a visually appealing ASCII table format"
PTab = PrettyTable()

# Set field names 
fields = ['County', 'Total Votes']
fields.extend(candidates)
PTab.field_names = fields

# Add row for each county with results by candidate
for county in counties:
    row = [f"{county}", f"{votes_bycounty[county]:,}"]
    results = []
    for candidate in candidates:
        # use dict.get to trap cases where vote=0 for county-candidate 
        count = test_dict[county].get(candidate, 0)
        percent = count / votes_bycounty[county]
        results.append(f"{count:,} ({percent:.1%})")
    row.extend(results)
    PTab.add_row(row)

# Add row with totals
row = ['Total', f"{total_votes:,}"]
results = []
for candidate in candidates:
    count = votes_bycandidate[candidate]
    percent = count / total_votes
    results.append(f"{count:,} ({percent:.1%})")
row.extend(results)
PTab.add_row(row)

# Right align all fields, then left align 'County' column
PTab.align = 'r'
PTab.align['County'] = 'l'

# Modify PrettyTable output string to separate Total row and show winner
# ----------------------------------------------------------------------
text_table = PTab.get_string()
# convert 'text_table' to list of lines
rows = text_table.split("\n")
# Extract a "border" row of dashes to use for separating sections of output
dashrow = rows[0]
# Insert 'dashrow' to separate Total row from previous results by county
rows.insert(len(rows) - 2, dashrow)
# Identify winner name and winner percent of total votes
winner_name = max(votes_bycandidate, key=votes_bycandidate.get)
winner_pcnt = f"{(votes_bycandidate[winner_name] / total_votes):.1%}"
# Start building winner string for insertion
winner_str = f"| The winner is {winner_name} with {winner_pcnt} of the total vote"
# Count spaces needed for padding
spaces = len(dashrow) - len(winner_str) - 1
# Finish building winner row
winner_str = winner_str + " "*spaces + "|"
# Insert winner row and another 'dashrow" at the end
rows.extend([winner_str, dashrow])

# Print output to console
for row in rows:
    print(row)








