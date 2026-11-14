# Paper Submission

Research manuscript documenting the Taylor-cone solver development and validation.

## Contents

- `main.tex` — main LaTeX document
- `sections/` — modular paper sections; `revision_style.tex` defines tracked-change markup
- `references.bib` — bibliography
- `figures/` — generated figures
- `data/` — result tables quoted in the text
- `tables/` — exported table sources
- `main.pdf` — compiled output

## Compile Locally

A full LaTeX distribution is required (`latexmk`, `pdflatex`, `bibtex`):

```bash
cd paper_submission
rm -f main.out          # clear bookmarks cache if needed
latexmk -pdf main.tex
```

Alternatively, use `pdflatex` plus `bibtex` with three `pdflatex` passes.

## Compile Using Overleaf

Upload the contents of `paper_submission/` to Overleaf and compile `main.tex`.

## Regenerating Figures and Data Tables

Figures and data tables are produced by scripts in the solver examples directory. All results are reproducible from the source code.

## Paper Status

The manuscript includes:
- Complete theoretical derivations
- Solver architecture and implementation details
- Numerical verification results
- Validation against published experimental images
- Discussion of limitations and future work

No physical experiments were conducted by the authors; experimental validation uses published literature data.
