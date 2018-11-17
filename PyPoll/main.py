import os
import csv
# establish  path
csvpath=os.path.join("Resources","election_data.csv")

votes=0
count=[]
novotes=0
candidate=[]
candidate_list=[]
candidate_vote=[]
vote_percent=[]
# open csv file
with open(csvpath,'r') as csvfile:
    # read csv file
    csvreader=csv.reader(csvfile,delimiter=',')
    csvheader=next(csvreader)
    # iterate through rows in csv file
    for row in csvreader:
        votes+=1
        candidate.append(row[2])
    # create a set of candidates names
    for a in set(candidate):
        candidate_list.append(a)
        # count votes for each candidate & append in a list
        b=candidate.count(a)
        candidate_vote.append(b)
        # calculate the vote percentage & append ina list
        c=round(((b/votes)*100),0)
        vote_percent.append(c)
        # finding the winner
        winner = max(candidate_vote)
        winner_name = candidate_list[candidate_vote.index(winner)]
        # zipping all the lists
        ss=list(zip(candidate_list,candidate_vote,vote_percent,))
    # printing the outputs
    print(f"Total Votes = {votes}")
    print(ss)
    # in other way
    for i in range(len(candidate_list)):
        print(f"{candidate_list[i]}: {vote_percent[i]}%  ({candidate_vote[i]})")
    print(f"Winner: {winner_name}")

# Create a new file & output the values
file=open("output.txt",'w')
file.write(f"Total Votes = {votes}\n")
file.write(f"{ss}\n")
for i in range(len(candidate_list)):
    file.write(f"{candidate_list[i]}: {vote_percent[i]}%  ({candidate_vote[i]})\n")
file.write(f"Winner: {winner_name}\n")
file.close()









