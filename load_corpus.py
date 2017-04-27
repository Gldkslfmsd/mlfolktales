__author__ = 'Simon'

"""
Run 'load_corpus.py' to load 'corpora.txt' and save it by languages and story types so separate directories and textfiles.

'corpora.txt' was created by 'atu_crawler.py'
"""

from corpus_classes import *
from ast import literal_eval


with open('corpora.txt', encoding='utf-8') as f:
    corpus_dict = literal_eval(f.read())
    corpus = Corpus(corpus_dict)

    #corpus.write_specific(corpus.get_corpora_by_language()['English'], 'english_folktales.txt')
    corpus.clean()
    corpus.pretty_write()