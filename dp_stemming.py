"""Loads all 'tokenized' textfiles from test.csv and train.csv. 
Performs stemming, removes stopwords and punctuation, and saves results to 'stemmed' directory.
"""


import pandas as pd
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords as stw
import string
import os.path


stopwords = set(stw.words('english'))
st = LancasterStemmer()

def stem(word):
	return st.stem(word)


def read_file(filename):
	with open(filename, "r") as f:
		tokens = f.read().split()
	nonsw = ( t for t in tokens if t not in stopwords )
	nonpunct = ( t for t in nonsw if all(map(lambda c: c not in string.punctuation, t)) )
	stemmed = [ stem(w) for w in nonpunct ]
	return stemmed

DIR = "stemmed"

def stemm_save_files(filenames, DIR=DIR):
	if not os.path.exists(DIR):
		os.makedirs(DIR)
	for fid in filenames:
		s = read_file("tokenized/%s.txt" % fid)
		with open("%s/%s.txt" %(DIR, fid), "w") as f:
			f.write(" ".join(s))

def stem_df(df, DIR=DIR):
	trids = [ f.id for _,f in df.iterrows() ]
	stemm_save_files(trids, DIR=DIR)


train = pd.DataFrame.from_csv("train.csv")
stem_df(train)
test = pd.DataFrame.from_csv("test.csv")
stem_df(test)
