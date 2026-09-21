# Build everything in this repository. Requires TeX Live / MacTeX / MiKTeX with latexmk.

# deck directory : name of the PDF committed next to the source
DECKS := 01-introduction:seminar-introduction 02-research-process:research-process

.PHONY: all slides template clean

all: slides template

slides:
	@for d in $(DECKS); do \
	  dir=slides/$${d%%:*}; pdf=$${d##*:}.pdf; \
	  echo "Building $$dir -> $$pdf"; \
	  (cd $$dir && latexmk -interaction=nonstopmode -halt-on-error) || exit 1; \
	  cp $$dir/build/main.pdf $$dir/$$pdf; \
	done

template:
	$(MAKE) -C templates/thesis

clean:
	@for d in $(DECKS); do (cd slides/$${d%%:*} && latexmk -C && rm -rf build); done
	$(MAKE) -C templates/thesis clean
