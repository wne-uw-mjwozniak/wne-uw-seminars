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

`make` first compiles the article without its own page numbers, then inserts it into the thesis so
that pages are numbered continuously. On Overleaf, compile `article/main.tex` once, download the PDF
as `article/main-thesis.pdf`, and then compile `main.tex`; or work on the two documents as separate
Overleaf projects.

## Switches in `main.tex`

- **Traditional form**: delete `\articleformtrue`. The wrapper then includes `chapters/` instead of
  the article and supplement, and the declarations drop the article-share statements.
- **Thesis in Polish**: change `\usepackage[english]{wne-thesis}` to `[polish]` and set
  `\thesiskind{Praca licencjacka}`.
- **AI declaration**: `\aideclaration{tool}{purpose}`, or `\aideclaration{}{}` if no AI tool was used.

## Before you submit

- The Polish declarations are quoted from Załącznik D and the faculty's AI declaration form. The
  **English wording is an unofficial translation**: confirm the current official forms and title page
  with the Dean's Office, and replace the declarations page with the signed scan (150 dpi, colour)
  in the electronic version.
- Abstract: at most 800 characters with spaces. Keywords: at most 10 words.
- Tables and figures: numbered through the whole thesis, each with a caption and a `\source{...}` line.
- Two student authors: each author signs a separate declaration and states their contribution per
  chapter. Duplicate the declarations page accordingly.
