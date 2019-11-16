# Note: 
# Feature engineering is the process of using domain knowledge of the data to create features that make machine learning algorithms work. 
# For unstructured, textual data, we need to convert free flowing text into some numeric representations which can then be understood 
# by machine learning algorithms.

import pandas as pd
import numpy as np
import re
import nltk
import matplotlib.pyplot as plt
pd.options.display.max_colwidth = 200
%matplotlib inline


# 1.Feature Engineering
# A corpus is typically a collection of text documents usually belonging to one or more subjects.
corpus = ['The sky is blue and beautiful.',
          'Love this blue and beautiful sky!',
          'The quick brown fox jumps over the lazy dog.',
          "A king's breakfast has sausages, ham, bacon, eggs, toast and beans",
          'I love green eggs, ham, sausages and bacon!',
          'The brown fox is quick and the blue dog is lazy!',
          'The sky is very blue and the sky is very beautiful today',
          'The dog is lazy but the brown fox is quick!']

labels = ['weather', 'weather', 'animals', 'food', 'food', 'animals', 'weather', 'animals']

corpus = np.array(corpus)
corpus_df = pd.DataFrame({'Document': corpus, 
                          'Category': labels})
corpus_df

# 2.Text pre-processing
# remove tags, accented characters, expanding contractions, special characters, stopwords;
# do Stemming and lemmatization.

wpt = nltk.WordPunctTokenizer()
stop_words = nltk.corpus.stopwords.words('english')

def normalize_document(doc):
    # lower case and remove special characters\whitespaces
    doc = re.sub(r'[^a-zA-Z\s]', '', doc, re.I|re.A)
    doc = doc.lower()
    doc = doc.strip()
    # tokenize document
    tokens = wpt.tokenize(doc)
    # filter stopwords out of document
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # re-create document from filtered tokens
    doc = ' '.join(filtered_tokens)
    return doc

# turn the function into a pipeline and plug in the corpus to process line by line
normalize_corpus = np.vectorize(normalize_document)
norm_corpus = normalize_corpus(corpus)

