# 1.Word Counts
# note bag of words distinguishes between uppercase and lowercase characters
#sample data
article = "'\'\'\'Debugging\'\'\' is the process of finding and resolving of defects that prevent correct operation " \
          "of computer software or a system.  \n\nNumerous books have been written about debugging (see below: #Further " \
          "reading|Further reading),"

# Import Counter
from collections import Counter
from nltk.tokenize import word_tokenize

# Tokenize the article: tokens
tokens = word_tokenize(article)

# Convert the tokens into lowercase: lower_tokens
lower_tokens = [t.lower() for t in tokens]

# Create a Counter with the lowercase tokens: bow_simple
bow_simple = Counter(lower_tokens)

# Print the 10 most common tokens
print(bow_simple.most_common(10))

#2. Simple text preprocessing
"""
Helps make for better input data when performing machine learning or other statistical methods
Examples:
Tokenization to create a bag of words
Lowercasing words
Lemmatization/Stemming
Shorten words to their root stems
Removing stop words, punctuation, or unwanted tokens
"""

# Import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter

# Retain alphabetic words: alpha_only
alpha_only = [t for t in lower_tokens if t.isalpha()]

# Remove all stop words: no_stops
english_stops = set(stopwords.words('english'))
no_stops = [t for t in alpha_only if t not in english_stops]

# Instantiate the WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

# Lemmatize all tokens into a new list: lemmatized
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

# Create the bag-of-words: bow
bow = Counter(lemmatized)

# Print the 10 most common tokens
print(bow.most_common(10))