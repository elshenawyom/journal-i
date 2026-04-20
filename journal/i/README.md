# Constructor Mathematical Journal — Volume I

**Spring 2025 · Constructor University Mathematics Society**

This repository contains the full source for the inaugural issue of the
*Constructor Mathematical Journal* (CMJ), a student expository journal of the
Constructor University Mathematics Society.

---

## Compilation

The project uses **pdfLaTeX** only — no BibTeX/Biber required.
Run two passes so that page references in the Table of Contents resolve:

```
pdflatex main
pdflatex main
```

Or with latexmk (auto-reruns as needed):

```
latexmk -pdf main
```

**Overleaf:** upload the full project folder and set `main.tex` as the main
document.

---

## Project Structure

```
journal-i/
├── main.tex                          Root document
├── cmj.sty                           Journal style package
│
├── front/
│   ├── cover.tex                     Cover page (TikZ artwork)
│   ├── info.tex                      About this volume / cover art note
│   ├── thisvolume.tex                "On this volume" editorial note
│   ├── editorial.tex                 Editor's address
│   └── staff.tex                     Editorial staff list
│
├── articles/
│   ├── 01-shannon.tex                Aly Assaf — Shannon's Theorem & Polar Codes
│   ├── 02-shor.tex                   Ahmed Maghri — The Qubit and Shor's Algorithm
│   └── 03-bragg.tex                  Loredana-Maria Iacob — Bragg's Law & Protein Structure
│
├── assets/
│   └── papers/
│       ├── shannon-polar-codes/      Original paper files, section .tex files, images
│       ├── qubit-shor/               Original paper files, section .tex files
│       └── bragg-x-ray/              Original paper files, images (bragg-fig*.png)
│
└── template/
    ├── article-template.tex          Flat single-file template (quickstart)
    └── article/
        ├── article.tex               Multi-file template (recommended for longer papers)
        └── sections/
            ├── section-1.tex         Example: Introduction + Preliminaries
            └── section-2.tex         Example: Main Results
```

---

## Adding a New Article

### Quick method (single file)

1. Copy `template/article-template.tex` and rename it, e.g.:
   ```
   articles/04-yourname.tex
   ```
2. Fill in the four arguments of `\articleheader` and write your content.
3. In `main.tex`, add `\input{articles/04-yourname}` in the Articles section.
4. Add a `\contentsentry` in the Table of Contents block of `main.tex`.

### Multi-file method (for longer papers)

1. Copy `template/article/` into `articles/papers/your-topic/`.
2. Create a thin wrapper `articles/04-yourname.tex` that calls `\articleheader`
   and `\input{}`s your section files.
3. If you have images, add `{articles/papers/your-topic/}` to `\graphicspath`
   in `cmj.sty`.
4. Register in `main.tex` as above.

### `\articleheader` signature

```latex
\articleheader
  {Title of the Article}
  {Author Name}
  {Department, Class of 20XX\\Constructor University Bremen}
  {Abstract text — one short paragraph.}
```

The article label for the ToC must match the `\label` at the top of the file
and the third argument of `\contentsentry` in `main.tex`:

```latex
\label{art:yourlabel}               % top of your article file
\contentsentry{Title}{Author}{art:yourlabel}  % in main.tex
```

---

## Available Environments

Defined in `cmj.sty`:

| Environment      | Purpose          | Frame colour      |
|------------------|------------------|-------------------|
| `definitionbox`  | Definitions      | Deep crimson      |
| `theorembox`     | Theorems         | Deep burgundy     |
| `notebox`        | Remarks / notes  | Lavender          |
| `theorem` (amsthm) | Inline theorems | Standard         |

Colour constants: `cmjcrimson` (deep crimson), `cmjgold`, `cmjdark`, `cmjgray`.

---

## Style Notes

- Section/figure/equation counters reset per article automatically.
- Running headers use the article title set in `\articleheader`.
  Avoid `\\` in the title argument to keep the header single-line.
- References are manual numbered lists — no BibTeX keys needed.
- Images go in `articles/papers/<topic>/` and `\graphicspath` is updated in
  `cmj.sty` to point there.
