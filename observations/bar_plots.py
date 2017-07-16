__author__ = "Dominik"

'''reads 'stories.csv' and creates 'pies.pdf' with some pie plots'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from pandas.tools.plotting import table

df = pd.DataFrame.from_csv("stories.csv")

pp = PdfPages('bars.pdf')

BARS = 1

def bar_plot(df, title, single_files=True):
	ni = []
	m = 15
	for i in df.index:
		if len(i)>m:
			ni.append(i[:m]+"...")
		else:
			ni.append(i)
	if ni:
		ml = max(map(len, ni))
	else:
		ml = 0
	df.index = pd.Series(ni)
	
	a = df.plot.bar(title=title, rot=30)
	fig = a.figure
	fig.tight_layout()

	for p in a.patches:
		a.annotate("%d" % p.get_height(), (p.get_x() * 1.005, p.get_height() * 1.005))
	print(ml)
#	fig.subplots_adjust(top=0.1, bottom=0.1)

	global BARS
	if not single_files:
		plt.savefig(pp, format="pdf")
	else:
		plt.savefig("bars%d.pdf" % BARS, format="pdf")
		BARS += 1
	_, ax = plt.subplots()  # 111, frame_on=False)  # no visible frame
	ax.xaxis.set_visible(False)  # hide the x axis
	ax.yaxis.set_visible(False)  # hide the y axis
	ax.set_frame_on(False)  # no visible frame, uncomment if size is ok

	plt.title(title+ " "+str(ml))
	print(title)
	print("==================")
	print(df)
	print()

	#table(ax, df, loc='center right', colWidths=[0.17] * len(df))  # where df is your data frame

	#plt.savefig(pp, format="pdf")
	plt.clf()


bar_plot(df.language.value_counts(), "Number of stories by language")

f = df.loc[df['level_1'] != "UNKNOWN"]

bar_plot(f.language.value_counts(), "Number of stories with known atu_level_1 by language")

# df.language.plot.pie()


langs = [  # 'Hungarian', 
	# 'Czech', 
	# 'Russian', 
	# 'Spanish', 
	# 'French', 
	# 'German', 
	# 'Danish', 
	# 'Dutch', 
	# 'Polish', 
	# 'Italian',
	'English'
]

levs = set(df['level_1'])

for lan in langs:
	f = df.loc[df['language'] == lan]
	f = f.loc[f['level_1'] != "UNKNOWN"]
	e = f.level_1.value_counts()
#	print(e)
	print()
	bar_plot(e, lan + " known atu_labels_1")
	
	print()

	print(f)

	for lev in levs:
		f = df.loc[df['language'] == lan]
		f = f.loc[f['level_1'] == lev]
		try:
			f = f.level_2.value_counts()
			bar_plot(f, lan + " -- " + lev + " atu_labels_2")
		except TypeError:
			print("no data")
			
			

pp.close()