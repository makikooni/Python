import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob


files = glob.glob("states*.csv")

df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)

us_census = pd.concat(df_list)

#print(us_census)
#print(us_census.columns)
#print(us_census.dtypes)
us_census['Income'] = us_census['Income'].str[1:]
us_census.Income =pd.to_numeric(us_census.Income)

string_split =us_census['GenderPop'].str.split('_')
us_census['Men'] =string_split.str.get(0)
us_census['Women'] =string_split.str.get(1)
us_census['Men'] = us_census['Men'].str[:-1]
us_census['Women'] = us_census['Women'].str[:-1]
us_census['Men'] =pd.to_numeric(us_census['Men'])
us_census['Women'] =pd.to_numeric(us_census['Women'])

us_census.Women = us_census.Women.fillna(us_census.TotalPop-us_census.Men)

#print(us_census.State.duplicated())
us_census =us_census.drop_duplicates(subset=['State'])

plt.scatter(us_census['Women'], us_census['Income'])
plt.title("Scatter Plot of Income vs. Number of Women per State")
plt.xlabel("Population of Women per State")
plt.ylabel("Income (in US Dollars)")
plt.show()
plt.clf()

us_census['Hispanic'] = us_census['Hispanic'].str[:-1]
us_census.Hispanic =pd.to_numeric(us_census.Hispanic)
us_census['White'] = us_census['White'].str[:-1]
us_census.White =pd.to_numeric(us_census.White)
us_census['Black'] = us_census['Black'].str[:-1]
us_census.Black =pd.to_numeric(us_census.Black)
us_census['Native'] = us_census['Native'].str[:-1]
us_census.Native =pd.to_numeric(us_census.Native)
us_census['Asian'] = us_census['Asian'].str[:-1]
us_census.Asian =pd.to_numeric(us_census.Asian)
us_census['Pacific'] = us_census['Pacific'].str[:-1]
us_census.Pacific =pd.to_numeric(us_census.Pacific)
print(us_census)

for race in ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']:
    plt.hist(us_census[race])
    plt.title("Histogram of the Percentage of {} People per State".format(race))
    plt.xlabel("Percentage")
    plt.ylabel("Frequency")
    plt.show()
    plt.clf()
