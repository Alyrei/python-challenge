#modules
import os  
import csv

#import csv
election_data = os.path.join('.', 'Resources', 'election_data.csv')

#declaring variables
total_voters = 0
#candidates/votes stored in list.  Alternates as [candidate1_name, candidate1_votes, candidate2_name, candidate2_votes, ... ]
myList = []
new = True
flip = True
percent = 0.0
winner = 0

#read the csv
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skip header
    csv_header = next(csvfile)

    #for loop to count rows
    for rows in csvreader:
        #increment total_voters for each row
        total_voters += 1
        #check to see if it's a known candidate
        for obj in myList:
            if str(rows[2]) == str(obj):
                new = False
                #found known candidate, increment vote total
                myList[(myList.index(rows[2])+1)] += 1
        #new candidate, add him to list with one vote
        if new:
            myList.append(str(rows[2]))
            myList.append(int(1))
        #set new back to true for next loop
        new = True          

print("Election Results")
print("----------------")
print(f"Total Votes: {total_voters}")
print("----------------")
#uses 'flip' to alternate between printing candidate name and printing voting count
for obj in myList:
    if flip:
        print(f"{str(obj)}:", end=" ")
    else:
        percent = (int(obj) / total_voters) * 100
        #searching for highest number of votes
        if winner < int(obj):
            winner = int(obj)
        print(f"{percent:.2f}% ({int(obj)})")
    #reverse flip for next loop
    flip = not flip
print("----------------")
# #print(max(myList)) 
# Traceback (most recent call last):
#   File "main.py", line 55, in <module>
#     print(max(myList))
# TypeError: '>' not supported between instances of 'int' and 'str'
print(f"Winner: {myList[(myList.index(winner)-1)]}")

#write to file
with open("pypoll.txt", "w") as file:
    file.write("Election Results\n")
    file.write("----------------\n")
    file.write(f"Total Votes: {total_voters}\n")
    file.write("----------------\n")
    for obj in myList:
        if flip:
            file.write(f"{str(obj)} ")
        else:
            percent = (int(obj) / total_voters) * 100
            if winner < int(obj):
                winner = int(obj)
            file.write(f"{percent:.2f}% ({int(obj)})\n")
        flip = not flip
    file.write("----------------\n")
    file.write(f"Winner: {myList[(myList.index(winner)-1)]}")