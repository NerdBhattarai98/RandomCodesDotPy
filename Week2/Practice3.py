from sklearn.feature_extraction.text import CountVectorizer
from DocumentSimilarity import documents
import numpy as np

vectorizer = CountVectorizer()

vectors = vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())
print(vectors.toarray())
