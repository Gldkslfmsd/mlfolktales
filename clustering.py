import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import *
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import os.path


train = pd.DataFrame.from_csv("train.csv")

cls = sorted(list(set(train.level_1)))
print(cls)
cls_short = ['Anecdote', 'Animal', 'Formula', 'Realistic', 'Religious', 'Magic',
	   'Ogre'
		]

texts = []
titles = []
labels = []
lab_tit = []
all_words = set()
for _,t in train.iterrows():
	s = open("stemmed/%s.txt" % t.id).read().split()
	for w in s:
		all_words.add(w)
	texts.append(Counter(s))
	labels.append(t.level_1)
	titles.append(t.title)
	lab_tit.append("%s: %s" %(cls_short[cls.index(t.level_1)], t.title))

#all_words = sorted(list(all_words))
#wi = { w:i for i,w in enumerate(all_words)}
#texts_vecs = []
#for t in texts:
#	vec = [0 for _ in range(len(all_words))]
#	for k,w in t.items():
#		vec[wi[k]] = w
#	texts_vecs.append(vec)
	
def norm(A):
	return sum(v**2 for v in A.values())**(1/2)

def cos_similarity(A, B):
	nom = sum(A[i]*B[i] for i in set(A.keys()).union(set(B.keys())))
	return nom/(norm(A)*norm(B))

path = "distances.csv"
if not os.path.exists(path):
	matrix = np.array([ np.array([ cos_similarity(a,b) for a in texts]) for b in texts])
	df = pd.DataFrame(matrix , index=titles, columns=titles)
	df.to_csv(path)
else:
	df = pd.DataFrame.from_csv(path)

plt.figure(num=None, figsize=(5, 18), dpi=80, facecolor='w', edgecolor='k')
a = linkage(df)
d = dendrogram(a, 
		   labels=lab_tit,#titles,
		   leaf_font_size=5,
		orientation="left"
			   )
plt.subplots_adjust(right=0.6, top=0.99, bottom=0.02, left=0.02)
for c,l,t in zip(d['color_list'], labels, titles):
	#print(c,l, t)
	pass
plt.savefig("dendrogram.pdf")
plt.show()

		
