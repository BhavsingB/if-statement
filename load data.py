import pandas as pd

# How to Load the Different type of data into a Python
'''
# df = pd.read_csv('app_list.csv') # csv format
# df = pd.read_csv('crops.csv') # csv format
# df = pd.read_csv('student-mat.csv',delimiter=";") # csv format
# df = pd.read_csv('iris data') # txt format
# dataframe = pd.read_csv("XYZCorp_LendingData (1).txt",delimiter="\t") # txt format
# df = pd.read_excel('sampleexcel.xlsx') # Old xlsx format
# df = pd.read_excel('sampleexcel.xlsx',sheet_name='sreekar') # Old xlsx format a particaler sheet
'''


# Exploring Data frames
'''
print(df)
print(df.head()) # give the details of crops data of first 5 rows
print(df.head(10)) # give the details of crops data of first 10 rows
print(df.tail()) # give the details of crops data of last 5 rows
print(df['crop']) # a particular columns
print(df[['crop','area','msp']]) #  give 3 columns - crop,year,area
'''
# Pandas Attributes
'''
print(df.dtyps) # gives data types of entire file which is having 5 columns.
print(df['area'].dtypes) # gives data types of specific column.
print(df.columns) # gives the column names
print(df.axes) # give the rows and columns name
print(df.ndim) # no of Dimentions
print(df.size) # total tuples in the file i.e 100 ^ 5 = 500
print(df.shape) # give the number of rows and columns
print(df.values) # Numpy representation of data
'''

# Pandas Methods
'''
print(df.describe()) # give the description if crops data
print(df.max()) # give max value for entire data set
print(df['area'].max()) # give max value for particular columns
print(df.mean()) # give mean values of numarical data
print(df['area'].mean()) # mean for particular columns
print(df.sample(n=10)) # gives random rows

print(df.head(15))
print(df.dropna()) # gives the data by deleting NaN

print(df.loc[5:15,['crop','year','area']]) # gives records from 5 -15 for 3 column
print(df.iloc[10:20,[1,3]]) # give data based on the index number
print(df.iloc[5]) # give the data of 10th row
print(df.iloc[10:20])
print(df.iloc[:20])
print(df['area'])
'''



