import os
import csv
import copy
import numpy as np
from prettytable import PrettyTable

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

# print(vote_count2)
# print()

test_dict = copy.deepcopy(vote_count2)

del test_dict['Trandee']["O'Tooley"]
del test_dict['Trandee']['Li']
del test_dict['Queen']['Khan']
del test_dict['Bamoo']['Khan']

counties = sorted(test_dict.keys())
# print(counties)

candidates = []
votes_bycounty = {}

for county, candidate_dict in test_dict.items():
    candidates.extend(list(candidate_dict.keys()))
    votes_bycounty[county] = sum(list(candidate_dict.values()))

x = np.array(candidates)
candidates = sorted(np.unique(x))

votes_bycandidate = {key: 0 for key in candidates}

for candidate_dict in test_dict.values():
    for candidate in candidate_dict.keys():
        votes_bycandidate[candidate] += candidate_dict.get(candidate,0)

# Sum total votes
total_votes = sum(votes_bycounty.values())

percent_bycandidate = {}
for candidate in candidates:
    percent_bycandidate[candidate] = votes_bycandidate[candidate] / total_votes

# print(percent_bycandidate)
# print()

output = ["County\tTotal Votes\t" + '\t'.join(candidates)] 
for county in counties:
    percents = []
    for candidate in candidates:
        count = test_dict[county].get(candidate, 0)
        percent = count / votes_bycounty[county]
        percents.append(f"{percent:.2%}")
    output.append(f"{county}\t{votes_bycounty[county]:,}\t" + '\t'.join(percents))
percents = []
for candidate in candidates:
    percent = percent_bycandidate[candidate]
    percents.append(f"{percent:.2%}")
output.append(f"Total\t{total_votes:,}\t" + '\t'.join(percents))


# Print results to console
for row in output:
    print(row)





    

