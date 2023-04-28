import math
import pandas as pd
import numpy as np

# Define a set of documents
docs = ['This is the first document', 'This document is the second document', 'And this is the third one', 'Is this the first document']

# Create a pandas DataFrame with the word counts for each document
word_counts = pd.DataFrame(index=list(set(word.lower() for doc in docs for word in doc.split())), columns=range(len(docs)), data=0)
for i, doc in enumerate(docs):
    words = doc.split()
    for word in words:
        word_counts.loc[word.lower(), i] += 1

# Calculate the term frequency (TF) for each word in each document
tf = np.zeros_like(word_counts.values, dtype=float)
for i in range(len(docs)):
    tf[:, i] = word_counts.iloc[:, i].values / np.sum(word_counts.iloc[:, i].values)

# Calculate the inverse document frequency (IDF) for each word
idf = np.zeros_like(word_counts.values, dtype=float)
for i in range(len(word_counts)):
    df = np.count_nonzero(word_counts.iloc[i].values)
    idf[i] = math.log(len(docs) / df)

# Calculate the TF-IDF scores for each word in each document
tf_idf = tf * idf

# Calculate the cosine similarity between each pair of documents
similarity_matrix = np.zeros((len(docs), len(docs)))
for i in range(len(docs)):
    for j in range(len(docs)):
        if i == j:
            similarity_matrix[i, j] = 1.0
        else:
            similarity_matrix[i, j] = np.dot(tf_idf[:, i], tf_idf[:, j]) / (np.linalg.norm(tf_idf[:, i]) * np.linalg.norm(tf_idf[:, j]))

# Create a DataFrame to display the results
output_columns = [f"Document {i+1}" for i in range(len(docs))]
output_df = pd.DataFrame(data=similarity_matrix, columns=output_columns, index=output_columns)
print(output_df)