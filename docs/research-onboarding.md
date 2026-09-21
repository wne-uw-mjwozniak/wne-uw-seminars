# Research onboarding: for people doing this for the first time

Companion to the deck [From Idea to Article](../slides/02-research-process/research-process.pdf).
All references below were checked against Crossref or the original page in September 2026.

## The first month, concretely

1. Install [Zotero](https://www.zotero.org/) with the [Better BibTeX](https://retorque.re/zotero-better-bibtex/)
   plug-in, and export your library to `paper/references.bib`.
2. Pick one target journal and skim its last two years: titles and abstracts only. Note the five
   papers closest to your interests.
3. Read three of them to the second pass and one to the third pass (see "How to read a paper").
4. Start a **literature matrix**: one row per paper; columns for question, data, method, main
   result, limitation, relation to your work. A spreadsheet or a markdown table is fine.
5. Start a **research log** (`LOG.md` in your repository): date, what you tried, what happened,
   what you concluded, what is next.
6. Draft the two-page concept note and put it on your board as the first card.

Before the first experiment: write down the evaluation protocol and freeze the test period;
implement and tune the baselines first; reproduce one published number; sketch the tables and
figures you expect to need.

## Reading list on the craft

**Reading and writing**

- Keshav, S. (2007). How to read a paper. *ACM SIGCOMM Computer Communication Review*, 37(3), 83-84. https://doi.org/10.1145/1273445.1273458
- Head, K. The introduction formula. https://blogs.ubc.ca/khead/research/research-advice/formula
- Cochrane, J. H. Writing tips for Ph.D. students. https://www.johnhcochrane.com/writing-group
  (written for PhD students in economics and finance; nearly all of it applies to a bachelor's thesis)

**Doing empirical ML properly**

- Kapoor, S., & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-based science. *Patterns*, 4(9), 100804. https://doi.org/10.1016/j.patter.2023.100804
- Lones, M. A. (2024). Avoiding common machine learning pitfalls. *Patterns*, 5(10), 101046. https://doi.org/10.1016/j.patter.2024.101046
- Bergmeir, C., & Benítez, J. M. (2012). On the use of cross-validation for time series predictor evaluation. *Information Sciences*, 191, 192-213. https://doi.org/10.1016/j.ins.2011.12.028
- Bailey, D. H., Borwein, J. M., López de Prado, M., & Zhu, Q. J. (2014). Pseudo-mathematics and financial charlatanism: The effects of backtest overfitting on out-of-sample performance. *Notices of the American Mathematical Society*, 61(5), 458-471. https://doi.org/10.1090/noti1105
- Diebold, F. X., & Mariano, R. S. (1995). Comparing predictive accuracy. *Journal of Business & Economic Statistics*, 13(3), 253-263. https://doi.org/10.1080/07350015.1995.10524599

**The field**

- Petropoulos, F., et al. (2022). Forecasting: theory and practice. *International Journal of Forecasting*, 38(3), 705-871. https://doi.org/10.1016/j.ijforecast.2021.11.001
  (an encyclopaedic, open-access review; use it to find the literature on almost any forecasting topic)
- Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and practice* (3rd ed.). OTexts. https://otexts.com/fpp3/

## Finding papers and judging journals

| Tool | Use it for |
| --- | --- |
| [Google Scholar](https://scholar.google.com/) | First search; "Cited by" and "Related articles"; BibTeX export (always check the fields) |
| Scopus, Web of Science | Systematic searches; available through the [University Library (BUW)](https://www.buw.uw.edu.pl/), also off campus |
| [Semantic Scholar](https://www.semanticscholar.org/), [Connected Papers](https://www.connectedpapers.com/) | Citation graphs around a key paper |
| [arXiv](https://arxiv.org/), [SSRN](https://www.ssrn.com/), [IDEAS/RePEc](https://ideas.repec.org/) | Preprints and working papers: the newest work, not yet peer reviewed |
| [Scimago Journal Rank](https://www.scimagojr.com/) | Journal quartiles by field |
| Polish ministerial list of journals | Points used in the Polish evaluation system |

Close to home: the [Central European Economic Journal](https://ceej.wne.uw.edu.pl/) is the open-access,
peer-reviewed journal of our faculty.

Warning signs of a predatory journal: unsolicited e-mail invitations, publication fees with review
in days, an implausibly broad scope, an editorial board you cannot verify.

## Data sources to start from

- Financial markets: [Stooq](https://stooq.com/) (Polish and global quotes), Yahoo Finance via the
  `yfinance` package, [FRED](https://fred.stlouisfed.org/)
- Macroeconomic and official statistics: [Eurostat](https://ec.europa.eu/eurostat),
  [Statistics Poland (GUS)](https://stat.gov.pl/), [NBP](https://nbp.pl/), [OECD](https://data.oecd.org/),
  [World Bank](https://data.worldbank.org/)
- Forecasting benchmarks: M4 and M5 competition data, the
  [Monash Time Series Forecasting Repository](https://forecastingdata.org/)
- General ML datasets: [OpenML](https://www.openml.org/), [UCI Machine Learning Repository](https://archive.ics.uci.edu/),
  [Kaggle](https://www.kaggle.com/datasets), [Hugging Face Datasets](https://huggingface.co/datasets)

Check the licence and terms of use before you build a thesis on a dataset, and record the download
date. Company data needs written permission that covers publication of results.

## Glossary of the publication process

| Term | Meaning |
| --- | --- |
| Preprint / working paper | A public version not yet peer reviewed (arXiv, SSRN, RePEc) |
| Desk reject | The editor declines the paper without sending it to referees, usually for fit or quality |
| Referee report | A reviewer's written assessment with requests for changes |
| R&R (revise and resubmit) | The journal invites a revised version; the best realistic first outcome |
| Response letter | Your point-by-point answer to every comment, submitted with the revision |
| Corresponding author | The author who handles communication with the journal |
| CRediT statement | Standard taxonomy describing who did what |
| Replication package | Code and data that reproduce every number in the paper |
| DOI | Permanent identifier of a publication; use it to verify that a reference exists |
| Impact factor, SJR, quartile (Q1-Q4) | Citation-based journal metrics; rough signals, not measures of a paper's quality |
| Open access, APC | Free to read; sometimes funded by an article processing charge paid by authors |
