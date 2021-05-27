from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from textblob import Word
from textblob.sentiments import NaiveBayesAnalyzer

# # Tokenization & Part of speech tag
# sen = TextBlob(""" 
# The base class of the class hierarchy.
# When called, it accepts no arguments and returns a new featureless instance that has no instance attributes and cannot be given any.
# """)

# print(f" Words {sen.words}")
# print('*' * 5)

# print(f" Sentences {sen.sentences}")
# print('*' * 5)

# wiki = TextBlob("Python is a high-level, general-purpose programming language.")
# print(wiki.tags)
# print('*' * 5)

# print(wiki.noun_phrases)
# print('*' * 5)

# for word ,pos in sen.tags:
#     print(word + "=>" + pos)
# print('*' * 5)

# # Tokenize in Arabic
# text = TextBlob("مرحبا, لا تؤخر عمل اليوم الى الغد ")
# print(text.words)
# print(text.sentences)

# # Words Inflection and Lemmatization
# from textblob import Word
# sentence = TextBlob('Use 4 spaces per indentation level.')
# print(sentence.words)
# print(sentence.words[2].singularize())
# print(sentence.words[-1].pluralize())

# w = Word('reading')
# w1 = Word('went')
# print(w.lemmatize()  + ' ' + w1.lemmatize())

# print('*' * 5)
# # Noun Phrase Extraction
# for noun in wiki.noun_phrases:
#     print(noun)

# print('*' * 5)
# # Spelling Correction
# b = TextBlob("I havv goood speling! wheree are you goinggg")
# print(b.correct())

# # spellcheck() Word.spellcheck() method that returns a list of (word, confidence) tuples with spelling suggestions.
# w = Word('goingg')
# print(w.spellcheck())

# print('*' * 5)
# # Get Word and Noun Phrase Frequencies
# x = TextBlob(""" We are no longer the Knights who say Ni. 
# "We are now the Knights who say Ekki ekki ekki PTANG.""")
# print(x.word_counts['ekki']) 
# print(x.words.count('ekki'))
# print(x.words.count('ekki' ,case_sensitive=True))                                         

# print('*' * 5)
# # Sentiment Analysis 
# # Polarity[-1 ,1] + Subjectivity = personal opinion

# x1 = TextBlob('Python is amazingly to use . what great fun')
# print(x1.sentiment)
# print(x1.sentiment.polarity)
# print(x1.sentiment.subjectivity)

# print('*' * 5)
# x2 = TextBlob("""You are happy enough I no longer need to dull the pain.
# We all felt sad about his death.
# I'd be happy knowing you're safe.""")
# for sent in x2.sentences:
#     print(sent.sentiment)

# print('*' * 5)
# x3 = TextBlob('I love Jordan' ,analyzer=NaiveBayesAnalyzer())
# x4 = TextBlob('I am crying ' ,analyzer=NaiveBayesAnalyzer())
# print(x3.sentiment)
# print(x4.sentiment)


# print('*' * 5)
# # Parsing
# x4 =TextBlob('Hello, My name iis Hamza')
# print(x4.parse())

# # Ggram like slicing
# print(x4.ngrams(n=2))
# print(x4.ngrams(n=3))
# print(x4.ngrams(n=4))

# print('*' * 5)
# # Definition and Similarity
# print(Word('Jordan').definitions)

# print('*' * 5)
# # Translation and Language Detection
# x5 = TextBlob('سيارة رائعة')
# print(x5.detect_language())
# print(x5.translate(from_lang='ar' ,to ='en'))
# print(x5.translate(to='en'))

# print('*' * 5)
# # Text Classification

train = [
    ('I love this sandwich.', 'pos'),
    ('this is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('this is my best work.', 'pos'),
    ("what an awesome view", 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('he is my sworn enemy!', 'neg'),
    ('my boss is horrible.', 'neg')]
test = [
    ('the beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')]

x7 = NaiveBayesClassifier(train)
print(x7.classify("This is an amazing place!")) 
print(x7.classify('I do not like this match'))   

print('*' * 5)
blob = TextBlob("The beer is good. But the hangover is horrible.", classifier=x7)
print(blob.classify())
for w in blob.sentences:
    print(f"{w} => {w.classify()}")