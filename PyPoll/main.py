import os
import csv

candidates = []
votes = 0
candidatevotes = []

mypath = os.path.join('.','resources','election_data.csv')
with open(mypath, 'r') as electionresults:
    electiondata = csv.reader(electionresults)
    csvheader = next(electiondata)
    for vote in electiondata:
        votes += 1
        try: #Candidate has already been voted for, increace tally by 1
            myindex = candidates.index(vote[2])
            candidatevotes[myindex] += 1
        except: #Candidate has not been voted for, add candidate to list and set tally to 1
            candidates.append(vote[2])
            candidatevotes.append(1)

Seperator = "-------------------------------\n"

output = "Election Results\n" + Seperator +  f"Total Votes: {votes}\n" + Seperator
maxvotes = 0
maxcandidate = ""
for x in range(0, len(candidates)):
    output += f"{candidates[x]}: {candidatevotes[x]/votes:.3%} ({candidatevotes[x]})\n"
    if candidatevotes[x] > maxvotes:
        maxcandidate = candidates[x]

output += Seperator
output += f"Winner: {maxcandidate}\n"
output += Seperator

print (output)
mypath = os.path.join('.','resources','output.txt')

with open(mypath, 'w', newline="") as txtfile:
    txtfile.write(output)



        