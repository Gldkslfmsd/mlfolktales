
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from pandas.tools.plotting import table

df = pd.DataFrame.from_csv("stories.csv")

pp = PdfPages('pies.pdf')

def pie_table(df, title):
	df.plot.pie(title=title)
	
	plt.savefig(pp, format="pdf")
	_, ax = plt.subplots()#111, frame_on=False)  # no visible frame
	ax.xaxis.set_visible(False)  # hide the x axis
	ax.yaxis.set_visible(False)  # hide the y axis
	ax.set_frame_on(False)  # no visible frame, uncomment if size is ok
	
	plt.title(title)
	print(title)
	print("==================")
	print(df)
	print()
	
	table(ax,df,loc='center', colWidths=[0.17] * len(df))  # where df is your data frame

	plt.savefig(pp, format="pdf")
	plt.clf()
	
pie_table(df.language.value_counts(), "Number of stories by language")

f = df.loc[df['level_1'] != "UNKNOWN"]

pie_table(f.language.value_counts(),"Number of stories with known atu_level_1 by language")

#df.language.plot.pie()


langs = ['Hungarian', 
		 'Czech', 
		 'Russian', 
		 'Spanish', 
		 'French', 
		 'German', 
		 'Danish', 
		 'Dutch', 
		 'Polish', 
		 'Italian',
		 'English'
		 ]

for lan in set(df.language):
	f = df.loc[df['language'] == lan]
	f = f.loc[f['level_1'] != "UNKNOWN"]
	f = f.level_1.value_counts()
	print()
	pie_table(f, lan + " known atu_labels_1")
	print()
	
	

pp.close()
