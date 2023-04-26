import nltk 
import gensim
import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

file_docs = []

with open('prueba.c-') as f:
    tokens = sent_tokenize(f.read())
    for line in tokens:
        file_docs.append(line)
        
print("Number of documents:",len(file_docs))

#Tokenize the words and create dictionary

gen_docs = [[w.lower() for w in word_tokenize(text)]
            for text in file_docs]

dictionary = gensim.corpora.Dictionary(gen_docs)
print(dictionary.token2id)

#Create a bag of words

corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]

#TFIDF

tf_idf = gensim.models.TfidfModel(corpus)
for doc in tf_idf[corpus]:
    print([[dictionary[id], np.around(freq, decimals=2)] for id, freq in doc])
    

sims = gensim.similarities.Similarity('workdir/',tf_idf[corpus],
                                    num_features=len(dictionary))


# Create query document

file_docs2 = []

with open('prueba2.c-') as f:
    tokens = sent_tokenize(f.read())
    for line in tokens:
        file2_docs.append(line)
        
for line in file2_docs:
    query_doc = [w.lower() for w in word_tokenize(line)]
    query_doc_bow = dictionary.doc2bow(query_doc)
    
query_doc_tf_idf = tf_idf[query_doc_bow]
print('Comparing Result:', sims[query_doc_tf_idf])