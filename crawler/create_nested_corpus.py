__author__ = 'Simon'

"""
Run this script to load 'corpora.txt' and save it by languages and story types to separate directories and textfiles.
Intended working directory is 'crawler/'.

'corpora.txt' was created by 'atu_crawler.py'
"""

from ast import literal_eval

from crawler.corpus_classes import *

with open('corpora.txt', encoding='utf-8') as f:
    corpus_dict = literal_eval(f.read())
    corpus = Corpus(corpus_dict)

    #corpus.write_specific(corpus.get_corpora_by_language()['English'], 'english_folktales.txt')
    corpus.clean()
    corpus.pretty_write()