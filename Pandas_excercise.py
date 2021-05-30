import pandas as pd
import csv

# What is Pandas?
# Pandas is a Python library used for working with data sets.

# Why Use Pandas?
# Pandas allows us to analyze big data and make conclusions based on statistical theories.
# Pandas can clean messy data sets, and make them readable and relevant.
# Relevant data is very important in data science



# *------------------------------------------------*
# Pandas Series : A Pandas Series is like a column in a table.

my_var = [1,2,3,4,5]
x = pd.Series(my_var)
print(x)

print('-' * 10)
# Create Labels
my_var1 = [1,2,3]
x1 = pd.Series(my_var1 ,index = ['A' ,'B' ,'C'])
print(x1)
print(x1[1])
print(x1['B'])

print('-' * 10)
# Key/Value Objects as Series ,Keys become labels
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)



print('-' * 10)
# *------------------------------------------------*
# DataFrames
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
m = pd.DataFrame(data ,index = ['a','b' ,'c'])
print(m)
print('-' * 10)
print(m.loc['a'])
print('-' * 10)
print(m.loc[['a','b','c']])


print('-' * 10)
# *------------------------------------------------*
# Load File csv
# Use to_string() to print the entire DataFrame.

file = open('D:\Machine_learning\data.csv' ,'r')
my_file = pd.read_csv(file)
print(my_file)
print('-' * 10)
print(my_file.to_string())

print('-' * 10)
# head() method returns the headers and a specified number of rows, starting from the top ,defaulf first 5
print(my_file.head(4))


print('-' * 10)
# tail() method for viewing the last rows of the DataFrame, default last 5
print(my_file.tail())


print('-' * 10)
# info(), that method gives you more information about the data set.
print(my_file.info())