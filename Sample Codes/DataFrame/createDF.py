import pandas as pd
from pandas import Series, DataFrame

# Create DF using Dictionary
inputdata = {'RegNo':[2001, 2002, 2003], 'Name':['ABC', 'DEF', 'GHI'], 'GPA':[8.3, 9.1, 7.98]}
df = pd.DataFrame(data = inputdata)

# Column name and index settings
df = DataFrame(data = inputdata, columns = ['Name', 'GPA', 'RegNo'], index = ['A', 'B', 'C'])
#print (df)

# print column names
#print (df.columns.values)

# Count number of records
#print(df.count().values)
#print(df.shape[0])

# Get column values
#print(df['Name'])

# Print multiple column values
#print(df[ ['Name', 'GPA'] ])

# Get Column sum
#print (df['GPA'].sum())

# Get specified row nad column
#print (df.iloc[0:2,1:2])

#Filter data based on condition
#print(df[df['GPA']>8])

# Get count of number of rows and columns
#print(df.shape)
#print (df.shape[0])

# Count number of records in DF
#print (len(df[df['GPA'] > 8].index))


