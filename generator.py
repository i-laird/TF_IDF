# author: Ian Laird
# file name: generator.py
# class: NLP
# instructor: Dr Lin
# due date: February 11, 2019
# date last modified: February 11, 2019

from nltk.corpus import brown, state_union, shakespeare
from CorpusReader_TFIDF import CorpusReader_TFIDF

def printCorpusStats(corpus):
    tf_idf = CorpusReader_TFIDF(corpus)
    print(tf_idf.tf_idf_dim()[:15])
    for file in corpus.fileids():
        print(file, tf_idf.tf_idf(file)[:15])

    print("Now showing the cosine similarity between each pair of documents")
    for file in corpus.fileids():
        for file2 in corpus.fileids():
            passList = list()
            passList.append(file)
            passList.append(file2)
            print(file, file2, tf_idf.cosine_sim(passList))

   # print(tf_idf.tf_idf_dim())
   # print(len(tf_idf.tf_idf_dim()))


print("This program takes a few minutes to terminate")
# first check it for Brown Corpus
print("Brown")
printCorpusStats(brown)
print("Shakespearean texts")
printCorpusStats(shakespeare)
print("State of the Union")
printCorpusStats(state_union)
exit(0)
