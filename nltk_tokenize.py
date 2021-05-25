from nltk import tokenize
from nltk.tokenize import sent_tokenize
from nltk.util import pr # Construct sentences




my_text1 = "Hi my name is Hamza :). I am 24 years old ,nice to meet you.call me later"
print("sent_tooknize : " ,sent_tokenize(my_text1)) # Divide the text into sentences


print('*' * 5)
# *------------------*
my_text2 = "Hi Mr.Hamza . I am Ahmad .call me later"
print("sent_tooknize : " ,sent_tokenize(my_text2))


print('*' * 5)
# *------------------*
my_text3 = 'we can play ,hello . please call me .4.4.44.ggmu,20'
print("sent_tooknize : ",sent_tokenize(my_text3))


print('*' * 5)
# *------------------*

my_text4 ="""
 Get started with Django
Meet Django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

Ridiculously fast.

    Django was designed to help developers take applications from concept to completion as quickly as possible.
Reassuringly secure.

    Django takes security seriously and helps developers avoid many common security mistakes.
Exceedingly scalable.

    Some of the busiest sites on the Web leverage Django’s ability to quickly and flexibly scale.

"""

print("sent _tokenize : " ,sent_tokenize(my_text4))