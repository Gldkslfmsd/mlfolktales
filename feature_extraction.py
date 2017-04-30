__author__ = "Dominik"

from keywords_for_features import keywords
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

keywords_set = set(keywords)

train = pd.DataFrame.from_csv("train.csv")
test = pd.DataFrame.from_csv("test.csv")

DIR = "tokenized"

def extract_keywords(df):
	files = [ os.path.join(DIR,"%s.txt" %f) for f in df.id ]
	feature_vectors = []
	for fn,row in zip(files, df.iterrows()):
		row = row[1]
		f_vec = { k:0 for k in keywords }
		f_vec['id'] = row['id']
		f_vec['level_1'] = row.level_1
		with open(fn) as f:
			for line in f:
				ls = line.split()
				for w in ls:
					if w in keywords_set:
						f_vec[w] += 1
		feature_vectors.append(f_vec)
		
	features = ["id"] + keywords + ["level_1"]
	feature_vectors = [ tuple(f[i] for i in features) for f in feature_vectors ]
	return pd.DataFrame.from_records(feature_vectors, columns=features, index="id")
	
train_f = extract_keywords(train)
train_f.to_csv("train_keyword_feats.csv")

test_f = extract_keywords(test)
test_f.to_csv("test_keyword_feats.csv")


# visualize boxplots of features


classes = sorted(list(set(train.level_1)))
pp = PdfPages('keyword_features.pdf')
for kw in keywords:
#        x = train_f.loc[train_f['level_1'] == c][kw]
	sns.boxplot(y=kw, x='level_1', data=train_f)
	#plt.savefig(pp, format="pdf")
	print(kw, "done")
	plt.clf()
	plt.show()
	break

pp.close()

