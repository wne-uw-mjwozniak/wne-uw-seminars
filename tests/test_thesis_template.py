"""Build-level regressions. Run: python3 -m unittest discover -s tests -v.

Requires latexmk, a complete TeX distribution and pdftotext. Builds isolated
copies, including the same article entry point used on Overleaf.
"""
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

TEMPLATE = Path(__file__).resolve().parents[1] / "templates" / "thesis"
LATEXMK = ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error"]


class ThesisTemplateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="wne-template-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for source in TEMPLATE.rglob("*"):
            if source.is_file() and (source.suffix in {".tex", ".sty", ".bib"}
                                     or source.name == "Makefile"):
                target = self.root / source.relative_to(TEMPLATE)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)

    def command(self, *args, success=True, cwd=None):
        result = subprocess.run(args, cwd=cwd or self.root, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if success:
            self.assertEqual(result.returncode, 0, result.stdout[-7000:])
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout[-1000:])
        return result.stdout

    def edit(self, name, old, new):
        path = self.root / name
        text = path.read_text()
        self.assertIn(old, text)
        path.write_text(text.replace(old, new))

    def pdftext(self, path="main.pdf"):
        return self.command("pdftotext", "-layout", path, "-")

    def pair(self):
        with (self.root / "metadata.tex").open("a") as out:
            out.write(r"""
\secondauthor{Anna Nowak}{654321}
\authorcontributions{\contribution{Test chapter}{40}{First contribution.}}{
  \contribution{Test chapter}{40}{Second contribution.}}
\supervisorcontributions{\contribution{Test chapter}{20}{Supervisor contribution.}}
""")

    def test_article_lists_counters_and_page_offsets(self):
        # An additional author changes front matter length. A float-only page
        # verifies metadata uses the float's output page, not its input page.
        self.pair()
        self.edit("article/main.tex", r"\section{Conclusions}", r"""
\subsection{Integration subsection}
\begin{equation}x=1\end{equation}
\begin{figure}[p]\centering Test figure one.
\caption{First exported figure}\end{figure}
\begin{figure}[p]\centering Test figure two.
\caption{Second exported figure}\end{figure}
\begin{table}[p]\centering Test table.
\caption{Deferred exported table}\end{table}
\clearpage
\section{Conclusions}
""")
        with (self.root / "supplement/results.tex").open("a") as out:
            out.write(r"""
\begin{table}[H]\caption{Supplement regression table}Test.
\source{Test data.}\end{table}
\begin{figure}[H]\caption{Supplement regression figure}Test.
\source{Test data.}\end{figure}
\begin{equation}x=2\label{eq:regression}\end{equation}
""")
        self.command("make")
        metadata = (self.root / "article-thesis.wne").read_text()
        self.assertIn(r"\WNEArticleCounters{2}{2}{2}{0}", metadata)
        toc = (self.root / "main.toc").read_text()
        lot = (self.root / "main.lot").read_text()
        lof = (self.root / "main.lof").read_text()
        self.assertIn("Integration subsection", toc)
        self.assertRegex(lot, r"numberline\s*\{3\}.*Supplement regression table")
        self.assertRegex(lof, r"numberline\s*\{3\}.*Supplement regression figure")
        self.assertRegex((self.root / "main.aux").read_text(),
                         r"newlabel\{eq:regression\}\{\{3\}")
        # Page references and hyperlink destinations must agree with actual
        # thesis pages. Skip contents/lists where the same text also appears.
        pages = self.pdftext().split("\f")
        for title, contents in [("Integration subsection", toc),
                                ("Deferred exported table", lot),
                                ("First exported figure", lof),
                                ("Second exported figure", lof)]:
            line = next(line for line in contents.splitlines() if title in line)
            match = re.search(r"\}\{(\d+)\}\{page\.(\d+)\}", line)
            self.assertIsNotNone(match, line)
            page, anchor = map(int, match.groups())
            self.assertEqual(page, anchor)
            self.assertIn(title, pages[page])  # title sheet is page zero
        warnings = [line for line in (self.root / "main.log").read_text().splitlines()
                    if "destination with the same identifier" in line]
        self.assertEqual(warnings, [])

    def test_pair_polish(self):
        self.pair()
        self.edit("main.tex", "[english]", "[polish]")
        self.command("make")
        text = self.pdftext()
        self.assertEqual(text.count("nie mniej niż 40%"), 2)
        self.assertIn("nie więcej niż 20%", text)
        self.assertNotIn("60%", text)
        self.assertIn("Anna Nowak", text.split("\f")[0])

    def test_traditional_pair(self):
        self.pair()
        self.edit("main.tex", r"\articleformtrue", r"\articleformfalse")
        self.command(*LATEXMK, "main.tex")
        text = self.pdftext()
        self.assertEqual(text.count("My share in the thesis is 50%."), 2)
        self.assertNotIn("not less than 40%", text)
        self.assertNotIn("Scientific article", text)

    def test_overleaf_entry_and_single_author(self):
        self.command(*LATEXMK, "-jobname=output", "article-thesis.tex")
        for extension in ("pdf", "wne"):
            (self.root / f"output.{extension}").rename(self.root / f"article-thesis.{extension}")
        article_pages = self.pdftext("article-thesis.pdf").split("\f")
        for page in article_pages:
            lines = page.strip().splitlines()
            if lines:
                self.assertFalse(re.fullmatch(r"\s*\d+\s*", lines[-1]), lines[-1])
        self.assertNotIn("Preprint submitted", "".join(article_pages))
        self.command(*LATEXMK, "main.tex")
        self.assertIn("not less than 60%", " ".join(self.pdftext().split()))
        self.assertIn("Out-of-sample forecast accuracy", (self.root / "main.lot").read_text())
        self.command(*LATEXMK, "main.tex", cwd=self.root / "article")
        self.assertIn("Preprint submitted", self.pdftext("article/main.pdf"))

    def test_missing_article_files_fail(self):
        output = self.command(*LATEXMK, "main.tex", success=False)
        self.assertIn("Article PDF not found", output)
        self.command(*LATEXMK, "article-thesis.tex")
        (self.root / "article-thesis.wne").unlink()
        output = self.command(*LATEXMK, "-g", "main.tex", success=False)
        self.assertIn("Article metadata not found", output)

    def test_pair_requires_contribution_descriptions(self):
        with (self.root / "metadata.tex").open("a") as out:
            out.write(r"\secondauthor{Anna Nowak}{654321}")
        output = self.command(*LATEXMK, "main.tex", success=False)
        self.assertIn("Missing first author's chapter contributions", output)


if __name__ == "__main__":
    unittest.main()
