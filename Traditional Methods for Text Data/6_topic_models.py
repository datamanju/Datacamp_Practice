# Notes:  summarization techniques to extract topic or concept based features from text documents;
# methods: Latent Semantic Indexing (LSI), Latent Dirichlet Allocation (LDA)
https://miro.medium.com/max/625/1*Wa5tvzIPAfcJj3bV6RW7xg.png

from sklearn.decomposition import LatentDirichletAllocation


# Generate a document-topic matrix, which would be the feature matrix we are looking for.
lda = LatentDirichletAllocation(n_components=3, max_iter=10000, random_state=0)
dt_matrix = lda.fit_transform(cv_matrix)
features = pd.DataFrame(dt_matrix, columns=['T1', 'T2', 'T3'])
features

# Generate a topic-term matrix, which helps us in looking at potential topics in the corpus.
tt_matrix = lda.components_
for topic_weights in tt_matrix:
    topic = [(token, weight) for token, weight in zip(vocab, topic_weights)]
    topic = sorted(topic, key=lambda x: -x[1])
    topic = [item for item in topic if item[1] > 0.6]
    print(topic)
    print()

# Document Clustering with Topic Model Features
from sklearn.cluster import KMeans

km = KMeans(n_clusters=3, random_state=0)
km.fit_transform(features)
cluster_labels = km.labels_
cluster_labels = pd.DataFrame(cluster_labels, columns=['ClusterLabel'])
pd.concat([corpus_df, cluster_labels], axis=1)