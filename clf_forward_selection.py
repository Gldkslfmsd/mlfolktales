__author__ = "Dominik"

from clf_aux import *
import pandas as pd

train = pd.DataFrame.from_csv("train_keyword_feats.csv")
test = pd.DataFrame.from_csv("test_keyword_feats.csv")

classifiers = [
	# (name, classifier, optional limit on size of training data)
	#    ("baseline", DummyClassifier("most_frequent")),
	#    ("3-Nearest Neighbors", KNeighborsClassifier(3)),
	#    ("5-Nearest Neighbors", KNeighborsClassifier(5)),
	#    ("10-Nearest Neighbors", KNeighborsClassifier(10)),
	("Linear SVM", SVC(kernel="linear", C=0.025)),
	("Linear SVM tuned", SVC(kernel="linear", C=0.25)),
	("Decision Tree", DecisionTreeClassifier(max_depth=5, random_state=1)),
	("Random Forest", RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1, random_state=1)),
	("AdaBoost", AdaBoostClassifier()),
	#    ("Naive Bayes", GaussianNB()),
]

DATASET = "%s_keyword_feats.csv"

bestN = 0
best_score = 0
for N in range(1, 200, 1):
	print(N)
	s = test_dataset(DATASET, classifiers, transform="binarize", selectN=N)
	if s > best_score:
		best_score = s
		bestN = N
	print()

print("best")
print(bestN, best_score)
