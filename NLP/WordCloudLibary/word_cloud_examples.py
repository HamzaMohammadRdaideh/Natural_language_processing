from wordcloud import WordCloud
import matplotlib.pyplot as plt

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
plt.show()

# To save file
wordcloud.to_file('first_review.png')