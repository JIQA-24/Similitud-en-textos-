from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Similitud de coseno
cos_sim = cosine_similarity(X)

#print(vectorizer.vocabulary_)
#print(X.toarray())

# Print la matrix de similitud
print(cos_sim)
