#Declarations & imports
import pandas as pd
from pathlib import Path
import numpy as np
import os
cv = 0
dv = 0
rv = 0

#Read in data file and show head, all following print statements are commented below
#relevant code lines for an optional value check
df = pd.read_csv(r'C:\repositories\python-challenge\PyPoll\Resources\election_data.csv')
#print(df)

#Store length for total votes
tv = len(df)

#Look through the Candidates in csv, counting and storing how many votes each recieved
for i in df['Candidate']:
    if i == 'Charles Casper Stockham':
        cv = cv + 1
    elif i == 'Diana DeGette':
        dv = dv + 1
    else:
        rv = rv + 1

#print(tv, cv, dv, rv)

#Calculate and store percentage of votes out of total votes for each candidate
cvp = 100 * float(cv)/float(tv)
dvp = 100 * float(dv)/float(tv)
rvp = 100 * float(rv)/float(tv)
#print(cvp, dvp, rvp)

#Store percentages for each candidate with their names, in order to call the name
#of the winning candidate
cand = {'Charles Casper Stockham': cvp, 'Diana DeGette': dvp, 'Raymon Anthony Doane': rvp}
winner = max(cand, key=cand.get)
#print(winner)

#Print results in terminal
print(
'Election Results\n', 
'-----------------------------\n',
'Total Votes: ', (tv),'\n',
'-----------------------------\n',
'Charles Casper Stockham: ',(round(cvp,3)),'%', '(',(cv),')', '\n',
'Diana DeGette: ',(round(dvp,3)),'%', '(',(dv),')', '\n',
'Raymon Anthony Doane: ',(round(rvp,3)),'%', '(',(rv),')', '\n',
'-----------------------------\n',
'Winner: ',(winner), '\n',
'-----------------------------')

#Print results in an output text file
with open(r'C:\repositories\python-challenge\PyPoll\analysis\output.txt', "a") as o:
  print(
    'Election Results\n', 
    '-----------------------------\n',
    'Total Votes: ', (tv),'\n',
    '-----------------------------\n',
    'Charles Casper Stockham: ',(round(cvp,3)),'%', '(',(cv),')', '\n',
    'Diana DeGette: ',(round(dvp,3)),'%', '(',(dv),')', '\n',
    'Raymon Anthony Doane: ',(round(rvp,3)),'%', '(',(rv),')', '\n',
    '-----------------------------\n',
    'Winner: ',(winner), '\n',
    '-----------------------------', file=o)