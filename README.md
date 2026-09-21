# From Data to Decisions: Machine Learning in Finance and Business

Materials for the bachelor's diploma seminar (course `2400-PL3SL339A`) at the Faculty of Economic
Sciences, University of Warsaw (WNE UW), academic year 2026/27. Supervisor: Michał Woźniak.

Start with the [kick-off slides](slides/01-introduction/seminar-introduction.pdf), continue with
[From Idea to Article](slides/02-research-process/research-process.pdf), then read the documents in
[`docs/`](docs/).

## What is here

| Path | Contents |
| --- | --- |
| [`slides/01-introduction/`](slides/01-introduction/) | Kick-off presentation: how the seminar works, faculty rules, topics. PDF and LaTeX source. |
| [`slides/02-research-process/`](slides/02-research-process/) | How a research paper gets made: finding a question, journals, reading, writing each section, pitfalls, peer review. |
| [`slides/theme/`](slides/theme/) | Shared Beamer theme used by all decks. |
| [`docs/seminar-rules.md`](docs/seminar-rules.md) | How we work: meetings, passing criteria, toolchain, AI tools. |
| [`docs/kanban-workflow.md`](docs/kanban-workflow.md) | Weekly status and the GitHub Projects board, step by step. |
| [`docs/wne-thesis-rules.md`](docs/wne-thesis-rules.md) | Faculty rules in brief, with links to the official sources. |
| [`docs/research-topics.md`](docs/research-topics.md) | Open research projects you can join, with starting literature. |
| [`docs/research-onboarding.md`](docs/research-onboarding.md) | For first-time researchers: reading list on the craft, data sources, tools, glossary. |
| [`docs/resources.md`](docs/resources.md) | Links for LaTeX, git, `uv`, `renv` and the WNE pages. |
| [`templates/thesis/`](templates/thesis/) | LaTeX thesis template: `elsarticle` article plus a WNE-compliant wrapper. |

## Quick start for students

1. Create a GitHub account and send your username to the supervisor.
2. Read the slides and `docs/seminar-rules.md`.
3. Install git, a TeX distribution (or use Overleaf), and `uv` (Python) or `renv` (R).
   Links are in `docs/resources.md`.
4. Copy `templates/thesis/` into your own project repository and run `make` there to check your setup.
5. Send a topic proposal: a working title, two or three sentences on the problem, and confirmation
   that you can get the data.
6. Set up your project board as described in `docs/kanban-workflow.md`.

## Building from source

Requires TeX Live (or MacTeX / MiKTeX) with `latexmk`.

```sh
make slides      # builds every deck in slides/ and copies the PDF next to its source
make template    # builds the example thesis in templates/thesis/
make clean
```

Every push to `main` also builds the slides on GitHub Actions; the PDF is attached to the workflow
run as an artifact.

## Official rules take precedence

The summaries here are a convenience. The binding documents are those published by the faculty at
<https://www.wne.uw.edu.pl/student/prace-dyplomowe> and the course syllabus in
[USOS](https://usosweb.uw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazPrzedmiot&kod=2400-PL3SL339A).
If anything here disagrees with them, they are right; please open an issue.

## Licence

Slides and documents: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). LaTeX theme and
thesis template: MIT. See [`LICENSE.md`](LICENSE.md).
