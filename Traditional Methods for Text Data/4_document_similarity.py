# Note: Document similarity is the process of using a distance or similarity based metric 
# that can be used to identify how similar a text document is with any other document(s) 
# based on features extracted from the documents like bag of words or tf-idf.

# it uses cosine as a score, when files are similar, the angle between vectors are small, which is expressed by cosine = 1,
# whereas if files are opposite, 180'unrelated, then cosine = -1, if 90' then similarity score is cosine = 0.

from sklearn.metrics.pairwise import cosine_similarity

similarity_matrix = cosine_similarity(tv_matrix)
similarity_df = pd.DataFrame(similarity_matrix)
similarity_df