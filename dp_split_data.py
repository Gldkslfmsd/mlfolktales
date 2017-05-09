
__author__ = "Dominik"

"""Splits stories to train and test set in ratio 70:30.

The distribution of level_1 classes remains the same in both sets.
"""

import pandas as pd
import numpy as np

LANGUAGE = "English"

df = pd.DataFrame.from_csv("stories.csv")

df = df.loc[df['language'] == LANGUAGE]
df = df.loc[df['level_1'] != "UNKNOWN"]

levels = set(df.level_1)
train = pd.DataFrame()
test = pd.DataFrame()
for lev in levels:
	if lev == "UNKNOWN": continue
	l = df.loc[df['level_1'] == lev]
	msk = np.random.rand(len(l)) < 0.7
	train = train.append(l[msk])
	test = test.append(l[~msk])
	

# control
x = zip(test['level_1'].value_counts(), train['level_1'].value_counts())
for a,b in x:
	print(a/(a+b))
print()

print("test and train csv files are not overwritten!!!")
# uncomment to generate new split
#test.to_csv("test.csv")
#train.to_csv("train.csv")
