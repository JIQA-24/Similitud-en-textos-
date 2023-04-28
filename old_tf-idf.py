from sklearn.feature_extraction.text import TfidfVectorizer

corpus = ['This is the first document.',
          'This is the second document.',
          'And this is the third one.',
          'Is this the first document?']

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.vocabulary_)
print(X.toarray())