#1. Why Use Spacy for NER?
# Easy pipeline creation
# Different entity types compared to nltk
# Informal language corpora
# Easily find entities in Tweets and chat messages

# Import spacy
import spacy

# Instantiate the English model: nlp
nlp = spacy.load('en', tagger=False, parser=False, matcher=False)

# Create a new document: doc
doc = nlp(article)

# Print all of the found entities and their labels
for ent in doc.ents:
    print(ent.label_, ent.text)
    
# Which are the extra categories that spacy uses compared to nltk in its named-entity recognition?
# NORP, CARDINAL, MONEY, WORKOFART, LANGUAGE, EVENT

