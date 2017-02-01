__author__ = 'Simon'
from corpus_classes import *
from ast import literal_eval

with open('corpora.txt', encoding='utf-8') as f:
    corpus_dict = literal_eval(f.read())
    corpus = Corpus(corpus_dict)

    #corpus.write_specific(corpus.get_corpora_by_language()['English'], 'english_folktales.txt')
    corpus.clean()
    corpus.pretty_write()