#Sentiment Analysis

from nltk.util import pr
import pandas as pd
import numbers as np
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt

reviews_dataset = pd.read_csv('Reviews.csv')
reviews_dataset = reviews_dataset.head(20000)
reviews_dataset.dropna()
print(reviews_dataset.head())

sns.distplot(reviews_dataset['Score'])
# plt.show()

sns.countplot(x='Score' ,data=reviews_dataset)
# plt.show()


# *------------------------------------------*
print('*' * 10)
print(reviews_dataset['Text'][350])
text_blob_object = TextBlob(reviews_dataset['Text'][350])
# print(text_blob_object.sentiment)

print('*' * 10)
def find_pol(review):
    return TextBlob(review).sentiment.polarity

reviews_dataset['Sentiment_Polarity'] = reviews_dataset['Text'].apply(find_pol)
print(reviews_dataset.head())

sns.displot(reviews_dataset['Sentiment_Polarity'])
# plt.show()

# *------------------------------------------*
print('*' * 10)
sns.barplot(x='Score' ,y='Sentiment_Polarity' ,data=reviews_dataset)
plt.show()

# *------------------------------------------*
print('*' * 10)

most_negative = reviews_dataset[reviews_dataset.Sentiment_Polarity == -1].Text.head()
print(most_negative)

print(reviews_dataset['Text'][545])
most_positive = reviews_dataset[reviews_dataset.Sentiment_Polarity == 1].Text.head()
print(most_positive)

print(reviews_dataset['Text'][106])
print(reviews_dataset['Text'][223])