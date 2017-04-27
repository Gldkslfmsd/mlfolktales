__author__ = "Dominik"


from corpus_classes import *
from ast import literal_eval


with open('corpora.txt', encoding='utf-8') as f:
    corpus_dict = literal_eval(f.read())
#    corpus = XmlFlatCorpus(corpus_dict)
    corpus = TxtFlatCorpus(corpus_dict)

    #corpus.write_specific(corpus.get_corpora_by_language()['English'], 'english_folktales.txt')
    corpus.clean()
    corpus.pretty_write()
