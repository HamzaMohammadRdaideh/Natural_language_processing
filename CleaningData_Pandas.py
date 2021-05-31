import pandas as pd

# Pandas - Cleaning Empty Cells : REmove row ,empty cells

df = pd.read_csv('D:\Machine_learning\dirtydata.csv')


print('*' * 50)
# dropna() method returns a new DataFrame, and will not change the original
newdf = df.dropna()
print(newdf)
print(df)


# *---------------------------------------------------------------------------*
print('*' * 50)
# Now, the dropna(inplace = True) will NOT return a new DataFrame, 
# but it will remove all rows containg NULL values from the original DataFrame.

newdf = df.dropna(inplace=True)
print(newdf)
print(df)



# *---------------------------------------------------------------------------*
# Replace Empty Values
# Replace NULL values in the "Calories" columns with the number 130

df['Calories'].fillna(130 ,inplace=True)
print(df.to_string())


# *---------------------------------------------------------------------------*
print('*' * 50)
# Replace Using Mean, Median, or Mode => mean() median() and mode()

x = df['Calories'].mean()
df['Calories'].fillna(x ,inplace=True)
print(df.to_string())



# *---------------------------------------------------------------------------*
print('*' * 50)
# Pandas - Cleaning Data of Wrong Format, row 22 26 ,NaT = (Not a Time)

print(df.to_string)
print(20 * '*')
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())



# *---------------------------------------------------------------------------*
print('*' * 50)
# Removing Rows, row 22 26 
# The result from the converting in the example above gave us a NaT value, 
# which can be handled as a NULL value, and we can remove the row by using the dropna() method

df['Date'] = pd.to_datetime(df['Date'])
df.dropna(subset=['Date'] ,inplace=True)
print(df)


# *---------------------------------------------------------------------------*
print('*' * 50)
# Pandas - Fixing Wrong Data, row 7 

print(df.to_string())
df.loc[7 ,'Duration'] = 45
print(df.to_string())


for x in df.index:
    if df.loc[x,'Duration'] > 120 :
        df.loc[x,'Duration'] = 70

print(df.to_string())


# Remove

print(df.to_string())
print(100 * '*') 
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
print(df.to_string())    



# *---------------------------------------------------------------------------*
print('*' * 50)
# Pandas - Removing Duplicates duplicated(), row 11-12 

print(df.duplicated())
print('*' * 50)
df.drop_duplicates(inplace=True)
print(df.to_string())