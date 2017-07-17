

figures() {
	BEG='\begin{figure}
	\centering'
	echo $BEG

	DIR=$1
	FIG=$2
	SUF=$4
	col() {
		echo '\begin{subfigure}{.5\textwidth}'
		echo '\centering'
		for R in $@; do
			echo "\\includegraphics[width=0.9\\linewidth]{$DIR/$FIG$R""$SUF"".pdf}"
#			echo "\\caption{rank=$R""}"
#			echo "\\label{fig:ccols$R""}"
		done
		echo '\end{subfigure}%'
	}
	col 10 4 6 7 #9  11
	col 8 9  11
#	col 4 7

	echo "\\caption{$3}"
	echo "\\label{fig:$2}"
	echo '\end{figure}'

} 

CAP="Distribution of English stories by ATU level 2."

figures plots bars "$CAP" > bars.tex


