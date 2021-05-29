# Series : one dimensional labeleed array-like object
# DataFrame : multi coulmns

import numpy as np
import pandas as pd

data = [100 ,200 ,300 ,400 ,500]
s = pd.Series(data)

print(s.describe())
s.plot(kind = 'line')

print('*' * 10)

print(s)
s.index = ['a' ,'b' ,'c' ,'d' ,'e']
print(s)

print('*' * 10)
print('Mean :' , s.mean())
print('Max :' , s.mad())
print('Min :' , s.min())


# *--------------------*
print('*' * 10)

dict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "area" : [2.5 ,1.1 ,3.5 ,2.5 ,101.5],
  "population" : [1 ,2 ,7 ,11 ,15]
}

my_data = pd.DataFrame(dict)
print('Mean', my_data.mean())
print('*' * 10)
print(my_data.describe())
print('*' * 10)
my_data.index = ['a' ,'b' ,'c' ,'d' ,'e']
print(my_data)


# *--------------------*
print('*' * 10)

x = {
    'one' : [1,2,3,4,5],
    'two' : [1,1,1,1,1],
    'letter' :['a','a','a','a','a']
}

data_x = pd.DataFrame(x)
for index ,row in data_x.iterrows():
    print(row['two']+3 ,row['letter'])

# *--------------------*
print('*' * 10)

names = ['hamza' ,'mohammad' ,'mahmoud' ,'sami']
year_of_birthday = [1990,1998,1997,1989]

in_one_list = list(zip(names ,year_of_birthday))
print(in_one_list)

in_one_list_pandas = pd.DataFrame(data = in_one_list ,columns=['names' ,'year_of_birthday'])
print(in_one_list_pandas)

print('*' * 10)
# Sort

in_one_list_pandas = in_one_list_pandas.sort_values(['year_of_birthday'] ,ascending=False)
print(in_one_list_pandas)


print('*' * 10)
# *--------------------*
# Head() Return first value

print('Head 1 : ' , in_one_list_pandas.head(1))
print('Head 2 :' ,in_one_list_pandas.head(2))


print('*' * 10)
print('Max birth' , in_one_list_pandas['year_of_birthday'].max())
print('Sum birth' , in_one_list_pandas['year_of_birthday'].sum())


print('*' * 10)
# *--------------------*
# Applying function on data

y = {
    'one' : [1,2,3,4,5],
    'two' : [1,1,1,1,1],
    'letter' :['a','a','a','a','a']
}

y = pd.DataFrame(y)
print(y)

print('*' * 10)
print(y['one'].apply(np.sqrt))

print('*' * 10)
print(y['letter'].map(lambda x : 'Map_' + x))

print('*' * 10)
# *--------------------*
# Add / Delete coulmns

h = [1,2,3,5,6,7,8,9]
h = pd.DataFrame(h)

print(h)
h.columns = ['Priority']
print(h)
h['New'] = 0
print(h)
del h['New']
print(h)


print('*' * 10)
# *--------------------*
# Group By

r = {
    'one' : [1,2,3,4,5],
    'two' : [1,1,1,1,1],
    'letter' :['a','b','b','c','c']
}

r = pd.DataFrame(r)
print(r)

print('rg')
rg = r.groupby('letter')
print(rg.first())


print('*' * 10)
l = r.groupby(['letter' ,'one']).sum()
print