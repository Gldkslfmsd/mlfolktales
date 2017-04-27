__author__ = "Dominik"

'''reads 'corpora.txt' created by atu_crawler.py and creates 
-- 'stories.csv' -- stories description
-- corpus_(txt|xml) -- flat directory with all stories

'''

from ast import literal_eval

from crawler.corpus_classes import *

with open('corpora.txt', encoding='utf-8') as f:
    corpus_dict = literal_eval(f.read())
#    corpus = XmlFlatCorpus(corpus_dict)
    corpus = TxtFlatCorpus(corpus_dict)

    #corpus.write_specific(corpus.get_corpora_by_language()['English'], 'english_folktales.txt')
    corpus.clean()
    corpus.pretty_write()
