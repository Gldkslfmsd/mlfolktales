__author__ = "Dominik"

"""This experiment can be expanded. 
"""

from clf_aux import *
import pandas as pd
import numpy as np

train = pd.DataFrame.from_csv("train_keyword_feats.csv")
test = pd.DataFrame.from_csv("test_keyword_feats.csv")

classifiers = [
	# (name, classifier, optional limit on size of training data)
	("Linear SVM", SVC(kernel="linear", C=0.025)),
	# currently best parameters
	("Linear SVM tuned", SVC(kernel="linear", C=0.25)),
]


for deg in range(1,3):
	for coef in np.arange(0.01, 1, 0.1):
		for c in np.arange(0.01, 1, 0.01):
			t = (str(c)+"-"+str(deg), SVC(kernel="poly", degree=deg, C=c, coef0=coef))
			#classifiers.append(t)

DATASET = "%s_keyword_feats.csv"

best = test_dataset(DATASET, classifiers, transform="binarize", selectN=16)

print("best score:")
print(best)
