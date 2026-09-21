# Build everything in this repository. Requires TeX Live / MacTeX / MiKTeX with latexmk.

SLIDES_DIR := slides/01-introduction
SLIDES_PDF := $(SLIDES_DIR)/seminar-introduction.pdf

.PHONY: all slides template clean

all: slides template

slides:
	cd $(SLIDES_DIR) && latexmk -interaction=nonstopmode -halt-on-error
	cp $(SLIDES_DIR)/build/main.pdf $(SLIDES_PDF)

template:
	$(MAKE) -C templates/thesis

clean:
	cd $(SLIDES_DIR) && latexmk -C && rm -rf build
	$(MAKE) -C templates/thesis clean
