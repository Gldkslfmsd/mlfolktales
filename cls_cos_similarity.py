from collections import Counter
import pandas as pd
from sklearn.metrics import accuracy_score

class CosineSimClassifier:
	
	def fit(self, X, y=None):
		self.targets = sorted(list(set(y)))
		self.groups = { c:[] for c in self.targets }
		for x,c in zip(X, y):
			self.groups[c].append(x)		
		
	def norm(self, A):
		return sum(v**2 for v in A.values())**(1/2)

	def cos_similarity(self, A, B):
		nom = sum(A[i]*B[i] for i in set(A.keys()).union(set(B.keys())))
		return nom/(self.norm(A)*self.norm(B))
	
	def avg_sim_to_class(self, x, cl):
		s = sum(self.cos_similarity(x,c) for c in self.groups[cl])
		return s/len(self.groups[cl])
	
	def avg_sim(self, x):
		return { cl: self.avg_sim_to_class(x, cl) for cl in self.targets }
	
	def predict_one(self, x):
		return max(self.avg_sim(x).items(), key=lambda x: x[1])[0]
	
	def predict(self, X):
		return [ self.predict_one(x) for x in X ]
	
class OneAgainstAllCosSim:
	
	def score(self, X):
		sims = []
		for i in range(len(X)):
			x = X[i]
			all = X[:i] + X[i:]
			clf = CosineSimClassifier()
			clf.fit(all, [0]*len(X))
			s = clf.avg_sim_to_class(x, 0)
			sims.append(s)
		return sims
	
		
	
	def score_all_classes(self, X,y, df):
		targets = sorted(list(set(y)))
		groups = { c:[] for c in targets }
		for x,c in zip(X, y):
			groups[c].append(x)		

		metadata = { c:[] for c in targets }
		for _,t in df.iterrows():
			metadata[t.level_1].append(str(t.id) + " " + t.title)
		
		for cl in targets:
			s = self.score(groups[cl])
			self.analyze_sims(s, metadata[cl], target=cl)
			print()
			print()

	def analyze_sims(self, sims, meta, target=None):
		if target:
			print("%s:" % target)
		z = sorted(list(zip(meta, sims)), key=lambda x: x[1])
		n = len(z)
		median = n//2
		q1 = n//4
		q3 = (3*n)//4
		iqr = z[q3][1] - z[q1][1]
		lower_iqr = z[q1][1] - 1.5*iqr
		upper_iqr = z[q3][1] + 1.5*iqr
		i = 1
		l = False
		u = False
		for a,b in z:
			if not l and b>lower_iqr:
				l = True
				print("--------- IQR lower bound: %2.4f -------- " % lower_iqr)
			print("%2.4f\t%s" % (b,a))
			if i==q1:
				print("==== First quartile ====")
			elif i==median:
				print("==== Median ===")
			elif i==q3:
				print("==== Third quartile ====")
				
			if (not u and b>upper_iqr) or i==n:
				u = True
				print("--------- IQR upper bound: %2.4f -------- " % upper_iqr)
			i += 1
	
	
def load_counters_labels(df):
	counters = []
	y = []
	for _,t in df.iterrows():
		with open("stemmed/%s.txt" % t.id) as f:
			s = f.read().split()
		counters.append(Counter(s))
		y.append(t.level_1)
	return counters, y

def one_vs_all():
	train = pd.DataFrame.from_csv("train.csv")
	train_X, train_y = load_counters_labels(train)	
	ova = OneAgainstAllCosSim()
	ova.score_all_classes(train_X,train_y, train)

# program bodies:
def classify():
	train_X, train_y = load_counters_labels(pd.DataFrame.from_csv("train.csv"))
	test_X, test_y = load_counters_labels(pd.DataFrame.from_csv("test.csv"))
	
	clf = CosineSimClassifier()
	clf.fit(train_X, train_y)
	predicted = clf.predict(test_X)
	
	print(accuracy_score(test_y, predicted))

if __name__ == "__main__":
	classify()

#	one_vs_all()
	