# Imports
from gensim import matutils, models
import scipy.sparse


import pandas as pd

vec_df = pd.read_csv('saves/3.stopwords_vectorized_df.csv', index_col = 0).transpose()
vec_df


sparse_counts = scipy.sparse.csr_matrix(vec_df)
corpus = matutils.Sparse2Corpus(sparse_counts)


import pickle

vectorizer = pickle.load(open("saves/3.vectorizer.pkl", "rb"))
id2word = dict((v, k) for k, v in vectorizer.vocabulary_.items())


lda = models.LdaModel(corpus = corpus, id2word = id2word, num_topics = 2, passes = 10)
lda.print_topics()


lda = models.LdaModel(corpus = corpus, id2word = id2word, num_topics = 3, passes = 10)
lda.print_topics()


lda = models.LdaModel(corpus = corpus, id2word = id2word, num_topics = 4, passes = 10)
lda.print_topics()


lda = models.LdaModel(corpus = corpus, id2word = id2word, num_topics = 5, passes = 10)
lda.print_topics()


import spacy
nlp = spacy.load('en_core_web_sm')











