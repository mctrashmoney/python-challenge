import csv
import os


# Define paths
csv_file_path = os.path.join('Resources', 'election_data.csv')
output_file_path = os.path.join('analysis', 'election_analysis.txt')


# Set variables
total_votes = 0
candidate_votes = {}


# Read csv file
with open(csv_file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    skipheader = next(csv_reader) 


    # Looping through the rows in csv
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the winner
winner = max(candidate_votes, key=candidate_votes.get)


# Write results to a text file
with open(output_file_path, mode='w') as file:
    file.write('Election Results\n')
    file.write('_________________________________________\n')
    file.write(f'Total Votes: {total_votes}\n')
    file.write('_________________________________________\n')
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f'{candidate}: {percentage:.3f}% ({votes})\n')
    file.write('_________________________________________\n')
    file.write(f'Winner: {winner}\n')
    file.write('_________________________________________\n')


# Prints the txt onto the terminal
txtfile = 'analysis\election_analysis.txt'
with open(txtfile, 'r') as terminaldata:
    print(terminaldata)
    summary = terminaldata.read()
    print(summary)