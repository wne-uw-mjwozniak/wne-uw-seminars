# Build the thesis. Requires a TeX distribution with latexmk (TeX Live, MacTeX, MiKTeX).
#
#   make            article-form thesis (article + WNE wrapper)  -> main.pdf
#   make article    stand-alone article for journal submission   -> article/main.pdf
#   make clean      remove build files

LATEXMK = latexmk -pdf -interaction=nonstopmode -halt-on-error

.PHONY: all thesis article article-thesis clean

all: thesis

# Stand-alone preprint, exactly as you would submit it to a journal.
article:
	cd article && $(LATEXMK) main.tex

# Same article without its own page numbers, so the thesis can number the pages continuously.
article-thesis:
	cd article && $(LATEXMK) -jobname=main-thesis -usepretex='\def\thesisbuild{1}' main.tex

thesis: article-thesis
	$(LATEXMK) main.tex

clean:
	cd article && latexmk -C main.tex && latexmk -C -jobname=main-thesis main.tex
	latexmk -C main.tex
