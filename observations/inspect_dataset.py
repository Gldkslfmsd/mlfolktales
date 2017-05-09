
__author__ = "Dominik"

import seaborn as sns
import matplotlib.pyplot as plt
from clf_aux import *

DATASET="%s_keyword_feats.csv"

tr_X, tr_y = load_dataset(DATASET % "train")
te_X, te_y = load_dataset(DATASET % "test")

tr_Xs, tr_y, te_X, te_y = scale_datasets(tr_X, tr_y, te_X, te_y)

tr_X = pd.DataFrame(tr_Xs, columns=tr_X.columns)


def correlation(tr_X):
	corrmat = tr_X.corr()
	print(tr_X.corr())

	# Set up the matplotlib figure
	f, ax = plt.subplots(figsize=(12, 9))

	# Draw the heatmap using seaborn
	sns.heatmap(corrmat, vmax=.8, square=True)

	plt.savefig("corr.pdf")


from sklearn.ensemble import ExtraTreesClassifier

# http://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html
def feature_importance(X, y):
	keywords = list(X.columns)
	print(keywords)
	
	# Build a forest and compute the feature importances
	forest = ExtraTreesClassifier(n_estimators=250,
								  random_state=0)
	forest.fit(X, y)
	importances = forest.feature_importances_
	std = np.std([tree.feature_importances_ for tree in forest.estimators_],
				 axis=0)
	indices = np.argsort(importances)[::-1]

	# Print the feature ranking
	print("Feature ranking:")

	rank = []
	for f in range(X.shape[1]):
		print("%d.\t%s\t%f" % (f + 1, keywords[indices[f]], importances[indices[f]]))
		rank.append(keywords[indices[f]])
		
	def make_plot(N):
		# Plot the feature importances of the forest
		plt.figure()
		plt.title("Feature importances")
		plt.bar(range(N), importances[indices][:N],
				color="r", #yerr=std[indices][:N], 
				align="center")
		plt.xticks(range(N), keywords[:N])
		plt.xlim([-1, N])
		plt.savefig("forest_feature_importance.pdf")
	make_plot(X.shape[1])
	#make_plot(20)
	
	return rank

rank = feature_importance(tr_X, tr_y)
print(rank)
	


	
	