
__author__ = "Dominik"

"""Find the most frequent words in each category and make keyword list from that. 
Another script makes dataset from them.

We tried to include
	-- all words including diacritics and stopwords
		-- but most frequent are diacritics and stopwords in all categories, it doesn't make sense
	-- remove diacritics
	-- and stopwords
	
"""

import os
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords as stops
stopwords = set(stops.words('english'))

from unicodedata import category as cat
def is_punctuation(word):
	return any(True for char in word if cat(char).startswith('P'))
	

DIR = "tokenized"

train = pd.DataFrame.from_csv("train.csv")
#categories = set(train.level_1)
categories = ['Animal Tales', 'Tales of Magic', 'Anecdotes and Jokes', 'Formula Tales', 'Religious Tales', 'Realistic Tales',
'Tales of the Stupid Ogre']

class KeywordExtractor():
	
	FILENAME = "gen_keywords_for_features.py"
	def extract(self, only_unique=False, save=False):	
		mf = {}
		for c in categories:
			mf[c] = self.most_freq_words_by_cat(c)
			

		#mf['Tales of Magic'] = self.most_freq_words_by_cat('Tales of Magic')
		self.mf = mf
		if only_unique:
			self.remove_duplicates()
		if save:
			self.save_to_file()
		
	def remove_duplicates(self, mf=None):
		if mf is None:
			mf = self.mf
		unique_freq = []
		has_unique = set()
		new_mf = {}
		for c in categories:
			new_mf[c] = []
			for w in mf[c]:
				skip = False
				for d in categories:
					if d==c: continue
					if w in mf[d]:
						skip = True
						break
				if not skip:
					unique_freq.append((w,c))
					has_unique.add(c)
					new_mf[c].append(w)

		self.mf = new_mf 
		return unique_freq
	
	def debug_print(self):
		mf = self.mf
		unique_freq = []
		has_unique = set()
		for c in categories:
			for w in mf[c]:
				skip = False
				for d in categories:
					if d==c: continue
					if w in mf[d]:
						skip = True
						break
				if not skip:
					unique_freq.append((w,c))
					has_unique.add(c)

		print("classes having unique keyword:", has_unique)
		print(len(has_unique), len(categories))
		for w,_ in unique_freq:
			print(w)

	def save_to_file(self):
		f = open(self.FILENAME, "w")
		f.write("# file generated automaticaly by freq_words_by_categories.py\n")
		f.write("keywords = ")
		agg = []
		for c in categories:
			agg.extend([w[0] for w in self.mf[c]])
		agg = list(set(agg))
		f.write(str(agg))
		f.write("\n")
		f.close()


	def most_freq_words_by_cat(self, cat, n=20):
		"""returns n most frequents words in category cat"""
		files = [ os.path.join(DIR,"%s.txt" %f) for f in train.loc[train['level_1'] == cat].id ]
		words = Counter()
		for fn in files:
			with open(fn) as f:
				for line in f:
					ls = [ w for w in line.split() if w not in stopwords and not is_punctuation(w)]
					words.update(ls)
		return [ a for a,_ in words.most_common()[:n] ]
	
class WeightedMostFreqKeywordsExtractor(KeywordExtractor):
	
	FILENAME = "gen_weighted_keywords_for_features.py"

	def most_freq_words_by_cat(self, cat, n=100):
		"""returns n words by the """
		files = [ os.path.join(DIR,"%s.txt" %f) for f in train.loc[train['level_1'] == cat].id ]
		col_freq = Counter()  # collection frequency: aggregated occurrences in all documents
		doc_freq = Counter()  # number of documents containing word
		for fn in files:
			with open(fn) as f:
				word_bag = set()
				for line in f:
					ls = [ w for w in line.split() if w not in stopwords and not is_punctuation(w)]
					col_freq.update(ls)
					for w in ls:
						word_bag.add(w)
				doc_freq.update(word_bag)
		
		# removing words occurring only once
		for w in list(col_freq.keys()):
			if col_freq[w] == 1:
				del col_freq[w]
		
		most = sorted([(w,col_freq[w]**doc_freq[w], col_freq[w], doc_freq[w]) for w in col_freq.keys()], key=lambda x: -x[1])
		most = most[:n]
		#most = [w[0] for w in most]
		return most
			   

if __name__ == "__main__":
	ext = WeightedMostFreqKeywordsExtractor()	
#	ext = KeywordExtractor()
	ext.extract()
	#ext.remove_duplicates()
	ext.debug_print()
	
	ext.save_to_file()
