#Codigo por: Oscar Emilio Reyes Taboada A01369421
# Jose Israel Quintero Alfaro A0136686

import math
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def tf_idf():
    f1 = open("file1.txt", "r")
    f2 = open("file2.txt", "r")
    f3 = open("file3.txt", "r")
    f4 = open("file4.txt", "r")

    f1r = f1.read()
    f2r = f2.read()
    f3r = f3.read()
    f4r = f4.read()

    # Define a set of documents
    docs = [f1r, f2r, f3r, f4r]

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

    # Calculate the cosine similarity for the TF-IDF matrix
    cos_sim = cosine_similarity(tf_idf.T)

    # Print the results
    output_columns = ['doc'+str(i+1) for i in range(len(docs))]
    output_df = pd.DataFrame(data=cos_sim, columns=output_columns, index=output_columns)
    print(output_df)