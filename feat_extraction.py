__author__ = "Dominik"


"""Create a feature vectors for all stories in test and train set by given keywords.


Keywords are given this way:"""
#from keywords_for_features import keywords
from gen_weighted_keywords_for_features import keywords 

"""and are generated by feat_design.py"""

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

keywords_set = set(keywords)

DIR = "tokenized"

def extract_keywords(df, keywords_set=keywords_set, DIR=DIR):
	"""df: DataFrame from train.csv or test.csv, contains lists of fairytales 
	and their atu, id etc.
	keywords_set: set of keywords for features
	
	returns: DataFrame containing feature value matrix"""
	files = [ os.path.join(DIR,"%s.txt" %f) for f in df.id ]
	feature_vectors = []
	for fn,row in zip(files, df.iterrows()):
		row = row[1]
		f_vec = { k:0 for k in keywords_set }
		f_vec['id'] = row['id']
		f_vec['level_1'] = row.level_1
		with open(fn) as f:
			num_words = 0
			for line in f:
				ls = line.split()
				for w in ls:
					if w in keywords_set:
						f_vec[w] += 1
				num_words += len(ls)
			for w in keywords_set:
				f_vec[w] /= num_words
		feature_vectors.append(f_vec)
		
	features = ["id"] + list(keywords_set) + ["level_1"]
	feature_vectors = [ tuple(f[i] for i in features) for f in feature_vectors ]
	return pd.DataFrame.from_records(feature_vectors, columns=features, index="id")

def launch_extraction(keywords_set=keywords_set):
	train = pd.DataFrame.from_csv("train.csv")
	test = pd.DataFrame.from_csv("test.csv")
		
	train_f = extract_keywords(train, keywords_set=keywords_set)
	train_f.to_csv("train_keyword_feats.csv")

	test_f = extract_keywords(test, keywords_set=keywords_set)
	test_f.to_csv("test_keyword_feats.csv")


if __name__ == "__main__":
	launch_extraction()

