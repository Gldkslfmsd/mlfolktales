"""Runs feature_extraction.py and then creates boxplots"""

from feat_extraction import *

# visualize boxplots of features


classes = sorted(list(set(train.level_1)))
pp = PdfPages('keyword_features.pdf')
for kw in keywords:
#        x = train_f.loc[train_f['level_1'] == c][kw]
	sns.boxplot(y=kw, x='level_1', data=train_f)
	plt.savefig(pp, format="pdf")
	print(kw, "done")
	plt.clf()
	plt.show()
	#break

pp.close()
