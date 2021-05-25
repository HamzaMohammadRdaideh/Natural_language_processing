from typing import Counter
from matplotlib import image
from wordcloud import WordCloud ,STOPWORDS
import matplotlib.pyplot as plt
import wikipedia
from PIL import Image
import numpy as np
from collections import Counter 

text = '''
500+ Words Essay on Healthy Food

Healthy food refers to food that contains the right amount of nutrients to keep our body fit. We need healthy food to keep ourselves fit.

Furthermore, healthy food is also very delicious as opposed to popular thinking. Nowadays, kids need to eat healthy food more than ever. We must encourage good eating habits so that our future generations will be healthy and fit.

Most importantly, the harmful effects of junk food and the positive impact of healthy food must be stressed upon. People should teach kids from an early age about the same.

Healthy Food Essay

Benefits of Healthy Food

Healthy food does not have merely one but numerous benefits. It helps us in various spheres of life. Healthy food does not only impact our physical health but mental health too.

When we intake healthy fruits and vegetables that are full of nutrients, we reduce the chances of diseases. For instance, green vegetables help us to maintain strength and vigor. In addition, certain healthy food items keep away long-term illnesses like diabetes and blood pressure.
'''

# Create and generate wordclass image
wordcloud = WordCloud().generate(text)

# Display the generate image
plt.imshow(wordcloud ,interpolation = 'bilinear')
plt.axis('off')
# plt.show() # dont forget uncomment 

# To save file
wordcloud.to_file('first_review.png')


# *-------------------------------------*
# a-Delete stop word

stopwords = set(STOPWORDS)
stopwords.add('fit')
stopwords.update(['food'])
clean_text = str([word for word in text.split() if word not in stopwords])

# Generate a word class image
wordcloud = WordCloud(max_words = 20 ,background_color = 'white').generate(clean_text)
plt.figure(figsize=(10 ,7))
plt.imshow(wordcloud ,interpolation = 'bilinear')
plt.axis('off')
# plt.show()

# b-Delete stop word 

stopwords = set(STOPWORDS)
stopwords.add('fit')
stopwords.update(['food' ,'we'])

wordcloud = WordCloud(stopwords = stopwords ,max_words = 20 ,background_color = 'white').generate(clean_text)
plt.figure(figsize=(10 ,7))
plt.imshow(wordcloud ,interpolation = 'bilinear')
plt.axis('off')
# plt.show()


# *-------------------------------------*
# Using Wikipedia

page = wikipedia.page('Manchester United')
text = page.content

cloud = WordCloud(width=800 ,height=800 ,min_font_size=14, background_color='yellow' ,colormap='spring').generate(text)
plt.figure(figsize=(10 ,10) ,facecolor=None)
plt.imshow(cloud ,interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
# plt.show()

# *-------------------------------------*
# Display inside an image
page = wikipedia.page('Manchester United')
text = page.content
image = Image.open('heart.png')
mask = np.array(image)

cloud = WordCloud(mask = mask ,colormap ='Reds').generate(text)
plt.figure(figsize=(10 ,10) ,facecolor=None)
plt.imshow(cloud ,interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()

# *-------------------------------------*
# Color control

def custom_color(*args ,**kwargs):

    word = args[0] # First argumet is the word itself
    if "a" in word:
        return "#FFD700"
    
    return '#CCCCCC'    

page = wikipedia.page('Manchester United')
text = page.content


cloud = WordCloud(color_func=custom_color ,width=800 ,height=800 ,min_font_size=14, background_color='yellow' ,colormap='spring').generate(text)
plt.figure(figsize=(10 ,10) ,facecolor=None)
plt.imshow(cloud ,interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()


# *-------------------------------------*
# Frequencies => priority and number of iterations

page = wikipedia.page('Manchester United')
text = page.content
target = text.split(" ")

# Count the frequency of each word
word_count = Counter(target)
cloud = WordCloud(max_words=2000)
cloud.generate_from_frequencies(word_count)

plt.figure(figsize=(10 ,10) ,facecolor=None)
plt.imshow(cloud ,interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
# plt.show()


# *-------------------------------------*


