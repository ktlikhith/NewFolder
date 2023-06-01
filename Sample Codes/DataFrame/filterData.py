import pandas as pd
from pandas import Series, DataFrame

students = [('Mark',  'Apples', 44),
            ('Aadi',  'Mangos', 31),
            ('Shaun', 'Grapes', 30),
            ('Simi',  'Apples', 32),
            ('Luka',  'Mangos', 43),
            ('Mike',  'Apples', 45),
            ('Arun',  'Mangos', 35),
            ('Riti',  'Grapes', 37), ]

df = pd.DataFrame(  students, columns = ['Name' , 'Product', 'Sale'])

## Display the DataFrame
#print(df)

# Select only rows with 'Apples'
#print(df['Product'] == 'Apples')
#print (df[df['Product'] == 'Apples'])

# Select only those rows where sale value is between 30 and 40
#print(df[(df['Sale'] > 30) & (df['Sale'] < 40)])

# Find record with max Sale 
#print(df[df['Sale'] == df['Sale'].max()])
#print(df[df['Sale'] == df['Sale'].max()].values[0,2])

# Find records whose Sale is more than average Sale


# Count records whose Sale is less than average Sale

#print (df.sort_values(by=['Sale'], ascending = False))
#print (df)
