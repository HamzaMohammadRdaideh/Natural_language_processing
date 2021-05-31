import pandas as pd
import matplotlib.pyplot as plt
# Data Correlations

df = pd.read_csv('D:\Machine_learning\data_correlations.csv')
print(df.to_string())
print('*' * 100)
print(df.corr())


# *------------------------------------------------------------*
# Pandas Plotting

df.plot()
plt.show()

# Scatter
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show() 

# Hist
df.plot(kind = 'hist', x = 'Duration', y = 'Calories')
plt.show()