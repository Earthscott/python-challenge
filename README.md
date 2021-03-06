# PyBank and PyPoll

## PyBank

The objective is to perform a financial analysis of monthly profit or loss over a certain time period. Given an input file with the following fields:

1. Date (format Mmm-yyyy).
2. Profit or loss during that month.

Find the following:

* The total number of months represented in the dataset.
* The cumulative sum of monthly profit/loss values for the entire dataset.
* The mean of the month-to-month profit/loss differences (i.e., `PL(i) - PL(i-1)` where _PL_ is the profit/loss and _i_ is the current index of the month.
* The greatest increase in month-to-month difference in profit/loss, and the corresponding date.
* The greatest decrease in month-to-month difference in profit/loss, and the corresponding date.

Print the results to the terminal and save the results in a text file.

The input file is located in the `PyBank/Resources` folder, and the output is saved in the `PyBank/Analysis` folder. The script `main.pl` is executed from the `PyBank` folder.

## PyPoll

The objectives are to tally the votes in an election and report on the results. Each record in the input file represents a single vote, and has the following fields:

1. Voter ID, a unique number representing the voter.
2. County, the name of the county in which the vote was cast.
3. Candidate, the name of the ccandidate receiving the vote.

Tabulate the votes for each candidate and report the following:

* The total number of votes cast in the election.
* For each candidate,
  * Name.
  * The percentage of votes received.
  * The number of votes received.
* The winner of the election.

Note that the Voter ID and the County are not needed for this analysis. Print the results to the terminal and save the results in a text file.

The input file is located in the `PyPoll/Resources` folder, and the output is saved in the `PyPoll/Analysis` folder. The script `main.pl` is executed from the `PyPoll` folder. The python script iterates over the input file and stores the vote count in a dictionary with candidate names as keys and vote counts as values.

### Bonus Analysis

The original PyPoll objectives are modified to present the results by county and candidate in a tabular form. The following modifications were made:

* A nested dictionay was used to store the ressults with county as the primary key, candidate name as the nested key, and votes counts by county-candidate combination as values.
* The original PyPoll dataset was used, but some of the county-candidate combinations were deleted from the dictionary. This was done as a proof-of-concept to address the possibility that a candidate did not receive any votes in a particular county.
* The python library PrettyTable was used to display results in a visually appealing ASCII table format. PrettyTable has limited options for custimizing the output, so the ASCII table was modified to include additional elements.

The script `bonus.pl` is executed from the `PyPoll` folder, and output is sent to the console only.

