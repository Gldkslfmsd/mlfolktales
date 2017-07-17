all: main.pdf

bars.tex: figures.sh
	bash figures.sh

# LaTeX must be run multiple times to get references right
pdf main.pdf: main.tex $(wildcard *.tex) bibliography.bib bars.tex
	pdflatex $<
	bibtex main 
	pdflatex $<
	pdflatex $<
	cp main.pdf report.pdf

clean:
	rm -f *.log *.dvi *.aux *.toc *.lof *.lot *.out *.bbl *.blg
	rm -f main.pdf
