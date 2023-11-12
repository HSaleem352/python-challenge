# This is the main script to analyze the CSV file for the PyPoll Challenge 
# 1 - https://docs.python.org/3/tutorial/datastructures.html


# Import the modules to work on the csv file and to navigate in the OS
import os
import csv

# Create the file path to read the pyPoll CSV file
csv_path = os.path.join(r"Resources\election_data.csv")

# create empty lists and variables to store data
ballot_id = []
county = []
candidate = []

# open the file provided by the filepath
with open(csv_path) as pollcsv:
    # Read the CSV file with , as the delimiter 
    pollreader = csv.reader(pollcsv) 
    header = next(pollreader)

    for row in pollreader:
        # Add ballot ID
        ballot_id.append(row[0])

        # Add county
        county.append(row[1])

        # Add candidate 
        candidate.append(row[2])

    # Getting the number of votes casted
    total_votes = len(ballot_id)
    
    # Counting the candidates 
    candidate_list = []

    for item in candidate:
        if item not in candidate_list:
            candidate_list.append(item)

    # Counting votes for each candidate 
    votes = []
    # https://docs.python.org/3/tutorial/datastructures.html
    # count() is a method for lists that returns the number of times the parameter appears in that list
    for items in candidate_list:
        votes.append(candidate.count(items))
    
    # Getting the percentage for each candidate  
    percent_vote = []
    for items in votes:
        percent_vote.append(round((items / total_votes)*100,3))

    # Getting the winner 
    winner_vote = votes[0]
    for items in votes:
        if items > winner_vote:
            winner_vote = items
    winner = candidate_list[votes.index(winner_vote)]
    
# Printing Analysis in Terminal 
print("Election Results \n")
print("---------------------------------------\n")
print(f"Total Votes: {total_votes} \n")
print("---------------------------------------\n")
for i in range(0,len(candidate_list)):
    print(f"{candidate_list[i]}: {percent_vote[i]}% ({votes[i]}) \n")
print("---------------------------------------\n")
print(f"Winner: {winner} \n")
print("---------------------------------------\n")

# Create a new folder called analysis in the Working Directory if it does not already exist

if (not os.path.isdir("Analysis")):
    os.mkdir("Analysis") # https://note.nkmk.me/en/python-os-mkdir-makedirs/#create-a-directory-osmkdir

# Create a filepath for the Analysis
output_filepath = os.path.join(r"Analysis\election_data_analysis.txt")

# Create and write to the new text file 
# https://www.freecodecamp.org/news/file-handling-in-python/
with open(output_filepath, "w") as writer:
    writer.writelines("Election Results \n")
    writer.writelines("---------------------------------------\n")
    writer.writelines(f"Total Votes: {total_votes} \n")
    writer.writelines("---------------------------------------\n")
    for i in range(0,len(candidate_list)):
        writer.writelines(f"{candidate_list[i]}: {percent_vote[i]}% ({votes[i]}) \n")
    writer.writelines("---------------------------------------\n")
    writer.writelines(f"Winner: {winner} \n")
    writer.writelines("---------------------------------------\n")







