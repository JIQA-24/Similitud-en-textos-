import math
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def readFiles():
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

    return docs

def analyzeText():

    # Call the function to read the files
    docs=readFiles()

    # Create a pandas DataFrame with the word counts for each document
    wordCounter = pd.DataFrame(index=list(set(word.lower() 
                                              for doc in docs 
                                              for word in doc.split())), 
                                columns=range(len(docs)), 
                                data=0)
    
    for i, doc in enumerate(docs):
        words = doc.split()
        for word in words:
            wordCounter.loc[word.lower(), i] += 1

    # Calculate the term frequency (TF) for each word in each document
    tf = np.zeros_like(wordCounter.values, dtype=float)
    for i in range(len(docs)):
        tf[:, i] = wordCounter.iloc[:, i].values / np.sum(wordCounter.iloc[:, i].values)

    # Calculate the inverse document frequency (IDF) for each word
    idf = np.zeros_like(wordCounter.values, dtype=float)
    for i in range(len(wordCounter)):
        df = np.count_nonzero(wordCounter.iloc[i].values)
        idf[i] = math.log(len(docs) / df)

    # Calculate the TF-IDF scores for each word in each document
    tf_idf = tf * idf

    # Calculate the cosine similarity for the TF and TF-IDF matrix
    cos_sim = cosine_similarity(tf.T)
    cos_sim_idf = cosine_similarity(tf_idf.T)

    # Print the results
    output_columns = ['P'+str(i+1) for i in range(len(docs))]
    output_df = pd.DataFrame(data=cos_sim, columns=output_columns, index=output_columns)
    print("TF: ")
    print(output_df)
    print("\n")

    output_columns_idf = ['P'+str(i+1) for i in range(len(docs))]
    output_df_idf = pd.DataFrame(data=cos_sim_idf, columns=output_columns_idf, index=output_columns_idf)
    print("TF_IDF: ")
    print(output_df_idf)

