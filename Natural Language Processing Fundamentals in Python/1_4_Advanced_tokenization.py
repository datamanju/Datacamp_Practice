# 1.Advanced tokenization with NLTK and regex

""" Notes
[A-Za-z]+	upper and lowercase English alphabet
[0-9]	numbers from 0 to 9	9
[A-Za-z\-\.]+	upper and lowercase English alphabet, - and .	'My-Website.com'
(a-z)	a, - and z	'a-z'
(\s+l,)	spaces or a comma	', '
OR is represented using |
You can define a group using ()
You can define explicit character ranges using []
"""
from nltk.tokenize import regexp_tokenize

my_string = "SOLDIER #1: Found them? In Mercea? The coconut's tropical!"
pattern1 = r"(\w+|\?|!)"
pattern2 = r"(\w+|#\d|\?|!)"
pattern3 = r"(#\d\w+\?!)"
pattern4 = r"\s+"

print (regexp_tokenize(my_string, pattern1))
print (regexp_tokenize(my_string, pattern2))
print (regexp_tokenize(my_string, pattern3))
print (regexp_tokenize(my_string, pattern4))

# 2.Regex with NLTK tokenization

# NLTK can be used to match and search tweets with hashtags and mentions
# Import the necessary modules
# Import the necessary modules
# Import the necessary modules
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer

tweets = ['This is the best #nlp exercise ive found online! #python',
 '#NLP is super fun! <3 #learning',
 'Thanks @datacamp :) #nlp #python']

# Define a regex pattern to find hashtags: pattern1
pattern1 = r"#\w+"
# Use the pattern on the first tweet in the tweets list
hashtags = regexp_tokenize(tweets[0], pattern1)
print(hashtags)

# Write a pattern that matches both mentions (@) and hashtags
pattern2 = r"([@|#]\w+)"
# Use the pattern on the last tweet in the tweets list
mentions_hashtags = regexp_tokenize(tweets[-1], pattern2)
print(mentions_hashtags)

# Use the TweetTokenizer to tokenize all tweets into one list
tknzr = TweetTokenizer()
all_tokens = [tknzr.tokenize(t) for t in tweets]
print(all_tokens)

# 3. Non-ascii tokenization
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import word_tokenize
german_text = 'Wann gehen wir Pizza essen? 🍕 Und fährst du mit Über? 🚕'

# Tokenize and print all words in german_text
all_words = word_tokenize(german_text)
print(all_words)

# Tokenize and print only capital words,take note of Ü
capital_words = r"[A-ZÜ]\w+"
print(regexp_tokenize(german_text, capital_words))

# Tokenize and print only emoji
emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"
print(regexp_tokenize(german_text, emoji))