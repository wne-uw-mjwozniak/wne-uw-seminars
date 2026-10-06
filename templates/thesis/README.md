# Thesis template

A LaTeX template for diploma theses at WNE UW, built for the **article form** that this seminar
encourages, with the traditional form available through one switch.

- `article/` is a stand-alone scientific article in Elsevier's `elsarticle` class, the format used
  by the *International Journal of Forecasting* and most Elsevier economics and finance journals.
  You can submit it to a journal as it is.
- `main.tex` is the thesis wrapper required by the faculty: title page, declarations, AI declaration,
  abstract page, contents, the article, the supplement, bibliography and lists, formatted according
  to Załącznik B and D (12 pt Times-like font, 1.5 spacing, 25 mm margins, author-year citations).

## Files

| Path | Purpose |
| --- | --- |
| `metadata.tex` | Title, author, supervisor, abstract, keywords. Edit this first. |
| `main.tex` | Thesis wrapper. Chooses the form and the language. |
| `wne-thesis.sty` | Layout and front-matter macros. You should not need to edit it. |
| `article-thesis.tex`, `wne-article.sty` | Article entry point and metadata export for the thesis build. |
| `article/main.tex`, `article/references.bib` | The article. |
| `supplement/*.tex` | Supplement chapters (article form). Written by the student(s) alone. |
| `chapters/*.tex` | Chapters (traditional form). |
| `references.bib` | Bibliography of the wrapper and supplement. |
| `figures/` | Generated figures. Commit the code that makes them, too. |

## Build

```sh
make            # article-form thesis        -> main.pdf
make article    # stand-alone article        -> article/main.pdf
make clean
```

`make` first compiles `article-thesis.tex` without the article's own page numbers. It produces
`article-thesis.pdf` and `article-thesis.wne` (headings, captions, page locations and counters), then
builds `main.pdf`. The wrapper imports both: pages are numbered continuously, article headings enter
the contents, article captions enter the lists, and supplement counters continue after the article.
Both generated files must come from the same build. Missing either file stops compilation.

### Building from an editor and after cleaning

Run `make` in the template directory. If you are working in this seminar repository, the equivalent
command from the repository root is:

```sh
make -C templates/thesis
```

An editor's **Build** button may compile only `main.tex`, without building the article first.
On a fresh copy or after `make clean`, this causes `Article PDF not found: article-thesis.pdf`
(or a missing `.wne` metadata error). Use `make` for the complete build, including after changes
to the article, so its PDF and metadata stay up to date. If your editor supports custom build
commands, configure it to run `make` with the template directory as its working directory.

If an earlier failed build left `latexmk` reporting an error from a previous invocation, rebuild
from scratch. Run these commands **in the template directory**:

```sh
make clean
make
```

The clean step removes generated files; the second command rebuilds the article and then the thesis.
Warnings about missing contents/list files or undefined citations can occur on the first LaTeX pass;
`latexmk` runs BibTeX and further passes as needed. Check the final build result. A PDF produced
during a failed build may be incomplete and should not be submitted.

### Overleaf

1. Upload the template with its directory structure intact; use pdfLaTeX.
2. Select the root-level **`article-thesis.tex`** as the main document and compile. This entry point
   defines the flag that removes the journal page numbers and footer.
3. Download its PDF as **`article-thesis.pdf`**. Also download the generated **`.wne`** file
   (usually **`output.wne`** on Overleaf) from **Logs and output files → Other logs and files**
   and rename it **`article-thesis.wne`**. Upload both to the template root.
   Do not rename a PDF compiled from `article/main.tex`: it retains the journal page numbers.
4. Select the root-level **`main.tex`** as the main document and compile the complete thesis.
5. After every article edit, repeat steps 2–4 and replace **both** generated files. If switching main
   documents leaves stale output, use **Recompile from scratch**. `make` performs this sequence locally.

See Overleaf's [generated files instructions](https://docs.overleaf.com/navigating-in-the-editor/generated-files)
for access to compilation outputs.

For a separate article project, copy the contents of `article/` and compile its `main.tex` to obtain
the stand-alone version. Article and wrapper bibliographies have separate `.bib` files: update both
exports from your reference manager as needed.

In the article, numbered headings and captions export automatically. After each new starred heading,
add `\addcontentsline{toc}{section}{Heading text}` (use `subsection` for that level). Keep article
pages Arabic and consecutive and table/figure numbers consecutive, including appendices, so the
wrapper can continue their counters. The PDF import does not import article `\label` definitions.

## Switches in `main.tex`

- **Traditional form**: delete `\articleformtrue`. The wrapper then includes `chapters/` instead of
  the article and supplement, and the declarations drop the article-share statements.
- **Thesis in Polish**: change `\usepackage[english]{wne-thesis}` to `[polish]` and set
  `\thesiskind{Praca licencjacka}`.
- **AI declaration**: `\aideclaration{tool}{purpose}`, or `\aideclaration{}{}` if no AI tool was used.

## Two student authors

In `metadata.tex`, set `\secondauthor{Name}{student number}` and fill in
`\authorcontributions{first student's entries}{second student's entries}`. Each entry uses
`\contribution{chapter or section}{percentage}{substantive contribution}`. List every chapter,
including entries with zero contribution. In article form, also fill in `\supervisorcontributions{...}`
for each article section and each supplement chapter (the supervisor's supplement shares are zero).

The template produces one supervisor declaration and one separate declaration per student, identifies
both students on the title page and uses joint authorship wording for the supplement. Each student
declares an overall article share of **at least 40%**, and the supervisor **at most 20%**. Fill in
the actual overall shares before signing, ensure they sum to 100%, and ensure each chapter's shares
also sum to 100%. The supplement belongs entirely to the students. For a traditional thesis,
each student's overall share is **exactly 50%**; omit the supervisor contribution entries.
These are declarations of actual work: the template does not infer or validate the percentages.

## Before you submit

- The single-student Polish declarations follow Załącznik D and the faculty's AI declaration form;
  the two-student wording adapts them to the co-authorship rules. The
  **English wording is an unofficial translation**: confirm the current official forms and title page
  with the Dean's Office, and replace the declarations page with the signed scan (150 dpi, colour)
  in the electronic version.
- Abstract: at most 800 characters with spaces. Keywords: at most 10 words.
- Tables and figures: numbered through the whole thesis, each with a caption and a `\source{...}` line.
- Two student authors: use the dedicated metadata settings above; do not duplicate the single-student page.

## Template regression checks

From the repository root, run `python3 -m unittest discover -s tests -v`. The tests require
`latexmk`, the template's TeX packages and Poppler's `pdftotext`. They build temporary copies
and check imported contents/lists and page references, continuous counters, both authorship modes,
Polish declarations, the Overleaf entry point and failures for missing article files.
