#import modules
import os
import csv

#file path for csv
pyPoll_csv = os.path.join("Resources", "election_data.csv")

#print(pyPoll_csv)

#output file for voter results
outputFile = os.path.join("election_survey_analysis.txt")

#create lists and variables to store data
candidates = []
candidate_vote = {} #dictionary that will hold votes of each candidate
vote_percent = []
winning_candidate = ""
total_votes = 0
winner_count = 0

#read csv file
with open(pyPoll_csv, "r", encoding = "utf-8") as poll_data:

    #split data by commas
    csvReader = csv.reader(poll_data, delimiter=",")
    
    #read and print header
    header = next(csvReader)
    #print(f"Header: {header}")

    #rows as lists (index 0 is id, index 1 is county, and index 2 is candidate)
    #for loop to go through each row of data after header
    for row in csvReader:
        total_votes += 1 #same as total_votes = total_votes + 1

        #check to see if the candidate is in list
        if row[2] not in candidates:
        
            #append candidate list row[2] if candidate is not in list
            candidates.append(row[2])

            #add value to dictionary and start count at 1 for votes
            candidate_vote[row[2]] = 1
        
        else:
            #add vote to vote list if applicable
            candidate_vote[row[2]] += 1

print(candidate_vote)
vote_output = ""

for candidate in candidate_vote:
    #get vote count and percentagle of the votes
    votes = candidate_vote.get(candidate)
    vote_percent = (float(votes) / float(total_votes)) * 100
    vote_output += f"\n{candidate}: {vote_percent:.2f}% ({votes})\n"
    
    #print(vote_output)
    
    #compare votes to winning count
    if votes > winner_count:
        #update votes to be the new winning count
        winner_count = votes
        #update winning candidate
        winning_candidate = candidate
    
winner = f"Winner: {winning_candidate} \n"

#create an ouput variable to hold output
output = (
    f"\n Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:}\n"
    f"-------------------------\n"
    f"{vote_output}\n"
    f"-------------------------\n"
    f"{winner}\n"
    f"-------------------------\n"
)

# print output
print(output)

#print results and export data to text file
with open(outputFile, "w") as textFile:
    #write output to text file
    textFile.write(output)
