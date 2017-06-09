__author__ = "Dominik"

from feat_extraction import *

path = os.path.join("martin", "keywords", "text", "keywordstext.txt")

keywords_set = set()

with open(path, "r") as f:
	for line in f:
		w, *_ = line.split()
		keywords_set.add(w)

launch_extraction(keywords_set=keywords_set)

