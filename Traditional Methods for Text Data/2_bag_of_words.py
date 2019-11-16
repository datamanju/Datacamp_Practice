# 1. Bag of Words
# note: A vector space model is simply a mathematical model to represent unstructured text 
# (or any other data) as numeric vectors, such that each dimension of the vector is a specific 
# feature\attribute.

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(min_df=0., max_df=1.)
cv_matrix = cv.fit_transform(norm_corpus)
cv_matrix = cv_matrix.toarray()

# get all unique words in the corpus
vocab = cv.get_feature_names()
# show document feature vectors
pd.DataFrame(cv_matrix, columns=vocab)

# If a corpus of documents consists of N unique words across all the documents, 
# we would have an N-dimensional vector for each of the documents.

# 2. Bag of N-Grams Model
# An N-gram is basically a collection of word tokens from a text document such that these tokens 
# are contiguous and occur in a sequence. It is different from bag of words, as it considers 2, 3 or more 
# combination of words in a bag. Hence 2-gram or 3-gram models.

# you can set the n-gram range to 1,2 to get unigrams as well as bigrams
bv = CountVectorizer(ngram_range=(2,2))
bv_matrix = bv.fit_transform(norm_corpus)

bv_matrix = bv_matrix.toarray()
vocab = bv.get_feature_names()
pd.DataFrame(bv_matrix, columns=vocab)
