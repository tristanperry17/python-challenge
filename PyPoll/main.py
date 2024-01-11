import pandas as pd
from pathlib import Path
import numpy as np
import os
cv = 0
dv = 0
rv = 0


df = pd.read_csv(r'C:\repositories\python-challenge\PyPoll\Resources\election_data.csv')
#print(df)

tv = len(df)

for i in df['Candidate']:
    if i == 'Charles Casper Stockham':
        cv = cv + 1
    elif i == 'Diana DeGette':
        dv = dv + 1
    else:
        rv = rv + 1

#print(tv, cv, dv, rv)

cvp = 100 * float(cv)/float(tv)
dvp = 100 * float(dv)/float(tv)
rvp = 100 * float(rv)/float(tv)
#print(cvp, dvp, rvp)

cand = {'Charles Casper Stockham': cvp, 'Diana DeGette': dvp, 'Raymon Anthony Doane': rvp}
winner = max(cand, key=cand.get)
#print(winner)

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