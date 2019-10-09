import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import codecademylib3_seaborn
import glob

files = glob.glob("states*.csv")

files_list = []

# read in each file and add to list
for file in files:
  files_list.append(pd.read_csv(file, index_col=0))
  
# join list of dataframes into one
us_census = pd.concat(files_list)

# sort dataframe by state
us_census = us_census.sort_values('State')

#print(us_census.columns)
#print(us_census.dtypes)
#print(us_census.head())

us_census.Income = us_census['Income'].replace('[\$,]', '', regex=True)
us_census.Income = pd.to_numeric(us_census['Income'])

us_census["Men"] = us_census["GenderPop"].str.split('_', expand=True)[0]
us_census["Women"] = us_census["GenderPop"].str.split('_', expand=True)[1]

us_census.Men = us_census["Men"].replace('M', '', regex=True)
us_census.Women = us_census["Women"].replace('F', '', regex=True)

us_census.Men = pd.to_numeric(us_census['Men'])
us_census.Women = pd.to_numeric(us_census['Women'])

#pyplot.scatter(us_census.Women, us_census.Income)
#pyplot.show()

#print(us_census.Women)

us_census = us_census.fillna(value={'Women':us_census.TotalPop-us_census.Men})

#print(us_census.Women)

#print(us_census.duplicated())

us_census = us_census.drop_duplicates()
us_census = us_census.reset_index(drop=True)

#pyplot.scatter(us_census.Women, us_census.Income)
#pyplot.show()

#print(us_census.columns)

us_census.Asian = us_census['Asian'].replace('[\%,]', '', regex=True)
us_census.Asian = pd.to_numeric(us_census.Asian)

us_census.Black = us_census['Black'].replace('[\%,]', '', regex=True)
us_census.Black = pd.to_numeric(us_census.Black)

us_census.Hispanic = us_census['Hispanic'].replace('[\%,]', '', regex=True)
us_census.Hispanic = pd.to_numeric(us_census.Hispanic)

us_census.Native = us_census['Native'].replace('[\%,]', '', regex=True)
us_census.Native = pd.to_numeric(us_census.Native)

us_census.Pacific = us_census['Pacific'].replace('[\%,]', '', regex=True)
us_census.Pacific = pd.to_numeric(us_census.Pacific)

us_census.White = us_census['White'].replace('[\%,]', '', regex=True)
us_census.White = pd.to_numeric(us_census.White)

us_census = us_census.fillna(value={'Asian': 0, 'Black':0, 'Hispanic':0, 'Native':0, 'Pacific': 0, 'White':0})

print(us_census)

pyplot.hist(us_census.Asian, alpha=0.5)
pyplot.hist(us_census.Black, alpha=0.5)
pyplot.hist(us_census.Hispanic, alpha=0.5)
pyplot.hist(us_census.Native, alpha=0.5)
pyplot.hist(us_census.Pacific, alpha=0.5)
pyplot.hist(us_census.White, alpha=0.5)
pyplot.show()