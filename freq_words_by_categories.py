
__author__ = "Dominik"

"""Find the most frequent words in each category and make features from that.

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

def most_freq_words_by_cat(cat):
    files = [ os.path.join(DIR,"%s.txt" %f) for f in train.loc[train['level_1'] == cat].id ]
    words = Counter()
    for fn in files:
        with open(fn) as f:
            for line in f:
                ls = [ w for w in line.split() if w not in stopwords and not is_punctuation(w)]
                words.update(ls)
    return [ a for a,_ in words.most_common()[:20] ]
                

mf = {}
for c in categories:
    mf[c] = most_freq_words_by_cat(c)
    
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

print(has_unique)
print(len(has_unique), len(categories))
for w,_ in unique_freq:
    print(w)

f = open("keywords_for_features.py", "w")
f.write("# file generated automaticaly by freq_words_by_categories.py\n")
f.write("keywords = ")
f.write(str([w for w,_ in unique_freq]))
f.write("\n")
f.close()
