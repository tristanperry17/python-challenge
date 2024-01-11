#Declariations & imports
import pandas as pd
from pathlib import Path
import numpy as np
import os

#Read in data file and show head, all following print statements are commented below
#relevant code lines for an optional value check 
df = pd.read_csv(r'C:\repositories\python-challenge\PyBank\Resources\budget_data.csv')
print(df.head())

#Calculate and store needed values 
total = df['Profit/Losses'].sum()
months = len(df)
#print(total,months)

#Use shift to create a new column, making it easier to do math to find average difference
df['shift'] = df['Profit/Losses'].shift(1)
df['avg_dif'] = df['Profit/Losses'] - df['shift']
#print(df['avg_dif'])

#Calculates and stores average difference
avgdif = df['avg_dif'].mean()
#print(avgdif)

#Calculate & store greatest increase and decrease
inc = df['avg_dif'].max()
dec = df['avg_dif'].min()

#Find and store the dates where the greatest increase and decrease occured for ease of printing
inci = df.loc[df['avg_dif'] == inc]
#print(inci)

r = inci['Date'].values
rr = r[0]

deci = df.loc[df['avg_dif'] == dec]
d = deci['Date'].values
dd = d[0]
#print(rr, dd)

#Prints analysis output in terminal
print(
'Financial Analysis\n', 
'-----------------------------\n',
'Total Months: ', (months),'\n',
'Total: ', (total), '\n',
'Average Change: ', '$',(avgdif),'\n',
'Greatest Increase In Profits: ',rr, '($',(inc),')','\n',
'Greatest Decrease in Profits: ',dd, '($',(dec),')')

#Prints output into text file
with open(r'C:\repositories\python-challenge\PyBank\analysis\output.txt', "a") as o:
  print(
    'Financial Analysis\n', 
    '-----------------------------\n',
    'Total Months: ', (months),'\n',
    'Total: ', (total), '\n',
    'Average Change: ', '$',(avgdif),'\n',
    'Greatest Increase In Profits: ',rr, '($',(inc),')','\n',
    'Greatest Decrease in Profits: ',dd, '($',(dec),')', file=o)
