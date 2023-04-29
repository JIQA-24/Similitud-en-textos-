import math
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def getTF():

    f1 = open("programa1.c-", "r")
    f2 = open("programa2.c-", "r")
    f3 = open("programa3.c-", "r")
    f4 = open("programa4.c-", "r")

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

    # Calculate the cosine similarity for the TF matrix
    cos_sim = cosine_similarity(tf.T)

    # Print the results
    output_columns = ['Programa'+str(i+1) for i in range(len(docs))]
    output_df = pd.DataFrame(data=cos_sim, columns=output_columns, index=output_columns)
    print(output_df)