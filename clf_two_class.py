__author__ = "Dominik"

from clf_aux import *
import pandas as pd

train = pd.DataFrame.from_csv("train_keyword_feats.csv")
test = pd.DataFrame.from_csv("test_keyword_feats.csv")

classifiers = [
	# (name, classifier, optional limit on size of training data)
	    ("baseline", DummyClassifier("most_frequent")),
	#    ("3-Nearest Neighbors", KNeighborsClassifier(3)),
	#    ("5-Nearest Neighbors", KNeighborsClassifier(5)),
	#    ("10-Nearest Neighbors", KNeighborsClassifier(10)),
	("Linear SVM", SVC(kernel="linear", C=0.025)),
	("Linear SVM tuned", SVC(kernel="linear", C=0.25)),
	("Decision Tree", DecisionTreeClassifier(max_depth=5, random_state=1)),
	("Random Forest", RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1, random_state=1)),
	("AdaBoost", AdaBoostClassifier()),
	("Naive Bayes", GaussianNB()),
]

DATASET = "%s_keyword_feats.csv"

classes = [#'Tales of the Stupid Ogre', 
		   'Animal Tales', 
		   #'Realistic Tales', 
		   'Anecdotes and Jokes', 
		   'Tales of Magic',
		   #'Formula Tales', 
		   #'Religious Tales'
		 ]

for cl in classes:
	print(cl)
	test_dataset(DATASET, classifiers, transform="binarize", selectN=22, two_class=cl)
	print()
