# pip install spacy
# python -m spacy download en
# python -m spacy download en_core_web_sm
import spacy
nlp = spacy.load("en_core_web_sm")


# Token words :
text = nlp('Hello    World!')
for token in text:
    print(' " ' + token.text + ' " ')



print('*------------------------------------*')
# # Token sentence
text1 =nlp("Hello my name is Hamza . I am 24 year ,I live in amman")

token_list = []
for token in text1:
    token_list.append(token.text) 
print(token_list)    

print('*------------------------------------*')
# Stop word

spacy_stop_words = spacy.lang.en.stop_words.STOP_WORDS
print('Number of stop words ' + str(len(spacy_stop_words)))
print('First 30 stop words : ' + str(list(spacy_stop_words)[:30]) )


for word in text1:
        print(f'{word} | {word.is_stop}')



print('*------------------------------------*')


sen = nlp(u'Manchester United is looking to sign a forward for $90 million')

for word in sen:
    print(f" {word.text + ' => ' + word.pos_ + ' => ' + word.lemma_ + ' => ' + word.tag_ + ' => ' + word.dep_ + ' => ' + word.shape_} | {word.is_alpha , word.is_stop} ")


print('*------------------------------------*')
# Remove stop words
sen1 =nlp("""
After tokenization, spaCy can parse and tag a given Doc. This is where the trained pipeline and its statistical models come in, 
which enable spaCy to make predictions of which tag or label most likely applies in this context. 
A trained component includes binary data that is produced by showing a system enough examples for it to make predictions 
that generalize across the language – for example, a word following “the” in English is most likely a noun.
""")

filter_word = []

for word in sen1:

    if word.is_stop == False:
        filter_word.append(word)
print('Filtered sentences : ' + str(filter_word))


print('*------------------------------------*')
# Detecting nouns
sen3 = nlp(u'Manchester United is looking to sign a forward for $90 million , likt harry kean and Halland and Hamza')
for chunk in sen3.noun_chunks:
    print(chunk)

print('*------------------------------------*')
# Named Entity Recognation NER
# Return an important element and categories

doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

print('*------------------------------------*')
# Word vector representation

word = nlp('tree')
print(word.vector.shape)
print(word.vector)

print('*------------------------------------*')
# Computing Similarity

target = nlp('Cats are beatifull animals')

s1 = nlp('Dogs are awsome')
s2 = nlp('Cars are speedest')
s3 = nlp('Apple is looking at buying U.K. startup for $1 billion')

print(target.similarity(s1))
print(target.similarity(s2))
print(target.similarity(s3))

print('*------------------------------------*')
# Get word frequency
from collections import Counter

text5 = nlp("""
Jordan (Arabic: الأردن‎; tr. Al-ʾUrdunn [al.ʔur.dunː]), officially the Hashemite Kingdom of Jordan,[a] is a country in Western Asia. It is situated at the crossroads of Asia, Africa and Europe,[8] within the levant region, on the East Bank of the Jordan River. Jordan is bordered by Saudi Arabia, Iraq, Syria, Israel and the West Bank of Palestine. The Dead Sea is located along its western borders, and the country has a 26-kilometre (16 mi) coastline on the Red Sea in its extreme south-west.[9] Amman is the nation's capital and largest city, as well as the economic, political and cultural centre.[10]

Modern-day Jordan has been inhabited by humans since the Paleolithic period. Three stable kingdoms emerged there at the end of the Bronze Age: Ammon, Moab and Edom. Later rulers include the Nabataean Kingdom, the Persian Empire, the Roman Empire, the Rashidun, Umayyad, and Abbasid Caliphates, and the Ottoman Empire. After the Great Arab Revolt against the Ottomans in 1916 during World War I, the Ottoman Empire was partitioned by Britain and France. The Emirate of Transjordan was established in 1921 by the Hashemite, then Emir, Abdullah I, and the emirate became a British protectorate. In 1946, Jordan became an independent state officially known as the Hashemite Kingdom of Transjordan, but was renamed in 1949 to the Hashemite Kingdom of Jordan after the country captured the West Bank during the 1948 Arab–Israeli War and annexed it until it was lost to Israel in 1967. Jordan renounced its claim to the territory in 1988, and became the second Arab state to sign a peace treaty with Israel in 1994.[11] Jordan is a founding member of the Arab League and the Organisation of Islamic Co-operation. The sovereign state is a constitutional monarchy, but the king holds wide executive and legislative powers.

Jordan is a semi-arid country, covering an area of 89,342 km2 (34,495 sq mi), with a population of 10 million, making it the eleventh-most populous Arab country. The dominant majority, or around 95% of the country's population, is Sunni Muslim, with an indigenous Christian minority. Jordan has been repeatedly referred to as an "oasis of stability" in the turbulent region of the Middle East. It has been mostly unscathed by the violence that swept the region following the Arab Spring in 2010.[12] From as early as 1948, Jordan has accepted refugees from multiple neighbouring countries in conflict. An estimated 2.1 million Palestinian and 1.4 million Syrian refugees are present in Jordan as of a 2015 census.[4] The kingdom is also a refuge to thousands of Iraqi Christians fleeing persecution by ISIL.[13] While Jordan continues to accept refugees, the recent large influx from Syria placed substantial strain on national resources and infrastructure.[14]

Jordan ranks high in the Human Development Index, and has an upper middle income economy. The Jordanian economy, one of the smallest economies in the region, is attractive to foreign investors based upon a skilled workforce.[15] The country is a major tourist destination, also attracting medical tourism due to its well developed health sector.[16] Nonetheless, a lack of natural resources, large flow of refugees and regional turmoil have hampered economic growth.
""")

words = [token.text for token in text5 if token.is_stop != True and token.is_punct != True]
word_freq = Counter(words)
common_word = word_freq.most_common(5)
print(common_word)


print('*------------------------------------*')
#Information extraction using NER and Dependency Parsing

my_text = nlp("""
My name is Hamza Mohammad Rdaideh , I live in
Amman , Jordan. 
""")


name_chunk = []
for name in my_text.noun_chunks:
    name_chunk.append(name)
print(f" 'name : ' + {name_chunk} ")

print(5 * '*')

for name in my_text.noun_chunks:
    print(name.text, name.root.text, name.root.dep_,
            name.root.head.text)