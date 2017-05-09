__author__ = "Dominik"

"""takes files mentioned in test.csv and train.csv from corpus_txt, tokenize them and store them 
to a newly created directory "tokenized"
"""

import nltk.data
from nltk.tokenize import WordPunctTokenizer
from sys import argv, stderr, stdin, stdout


sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
wptokenizer = WordPunctTokenizer()

def process_file(f, out=stdout):
#	try:
#	f = open(name, "r")
	text = f.read()
	f.close()
#	except UnicodeDecodeError:
#		print(name, file=open("errors", "a"))
#		return

	sent_tokenized = sent_detector.tokenize(text)
	Nsent = len(sent_tokenized)

	Ntoks = 0
	for s in sent_tokenized:
		tok = wptokenizer.tokenize(s)
		Ntoks += len(tok)
		# let's lowercase it in this point because maybe the case is
		# important for tokenizers
		o = " ".join(map(lambda s: s.lower(), tok))
		out.write(o+"\n")
	out.close()

	#print("file:",name, "sentences:", Nsent, "tokens:", Ntoks)
	
if __name__ == "__main__":
	import pandas as pd
	import os
	train = pd.DataFrame.from_csv("train.csv")
	test = pd.DataFrame.from_csv("test.csv")

	filenames = [ "%s.txt" %s for s in train.id.append(test.id) ]

	OUTDIR = "tokenized"

	os.makedirs(OUTDIR, exist_ok=True)
	for fn in filenames:
		print(fn)
		f = open(os.path.join("corpus_txt", fn), "r")
		p = os.path.join(OUTDIR, fn)
		out = open(p, "w")
		process_file(f, out=out)
