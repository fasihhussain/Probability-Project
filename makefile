file = project

thesis: $(file).pdf

all : thesis

$(file).pdf: *.tex
	pdflatex $(file)
	bibtex $(file).aux
	pdflatex $(file)
	pdflatex $(file)

clean:
	rm -f *.aux $(file).log $(file).lof $(file).toc $(file).bbl $(file).blg $(file).brf $(file).out $(file).pdf *.snm *.nav *.gz *.fdb_latexmk *.fls

