import pandas as pd
import glob
from pathlib import Path
from openpyxl import Workbook

#Pandas settings for troubleshooting/testing
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)


##Inport logic section begins##
##Current issues: 2


# Find all schedule files
excelFiles = glob.glob('schedules/*.xlsx', recursive = True)
csvFiles = glob.glob('schedules/*.csv', recursive = True)


#This currently only reads the courses section of the Excel file; The logic can be repeated for further
#usage with modified values, it just hasn't been done yet
schedules = []
for file in excelFiles:
    #print(file)
    df = pd.read_excel(file, 
                           skiprows=5,  # Skip to "CS 100" row
                           nrows=9,     # Read 8 rows of courses
                           header=None, # No column headers
                           engine='openpyxl')  # Parse offered courses
    df = df.replace('\t', '', regex=True)
    
    schedules.append(df)

#combined = pd.concat(schedules, ignore_index=True)
#print(combined)

#This logic concatnates the two dataframes together, which leaves a lot of unused space for probably no reason.
#(Could possibly combine the two sets?)
#Also the colNames is only here for formatting, remove when possible.
for file in csvFiles:
    #print(file)
    colNames = ['col1', 'col2', 'col3', 'col4', 'col5']
    df = pd.read_csv(file, names=colNames)
    df = df.replace('\t', '', regex=True)
    
    schedules.append(df)

combined = pd.concat(schedules, ignore_index=True)

print(combined)
##Import logic section ends##


##Export logic section begins##
##Current issues: 1

#Pandas Excel output
df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]}) #Fix the values in this line (these are here for stand-in)
df.to_excel('output.xlsx', index=False)

#Pandas CSV output
df.to_csv('output.csv', index=False)
