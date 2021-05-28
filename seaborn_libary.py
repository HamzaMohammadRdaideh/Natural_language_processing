import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Load iris data
iris = sns.load_dataset('iris')

# Construct iris plot
sns.swarmplot(x = "species" ,y = "petal_length" ,data = iris)
plt.show()

# *-------------------------------------------------*

# Load tips data
tips = sns.load_dataset('tips')

# Construct tips plot
sns.violinplot(x = "total_bill" ,data = tips)
plt.show()

# *-------------------------------------------------*
# Pairwise relationship in dataset
iris = sns.load_dataset('iris')
sns.pairplot(iris)
plt.show()


# *-------------------------------------------------*
# Scatter plots & Hexbin plots
m ,x = [0 , 1],[(1, .5) ,(.5 ,1)]
data = np.random.multivariate_normal(m ,x ,200)
df = pd.DataFrame(data ,columns = ['x' ,'y'])
sns.jointplot(x = 'x' ,y = 'y' ,data = df)
plt.show()