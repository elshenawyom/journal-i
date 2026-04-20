# Maths Society @ Constructor University | Internal Repo

This repository contains the LaTeX sources for the **Constructor Mathematical Journal (CMJ)** and its related **Undergaduate Seminar (UgS)**.

## What’s here

- `cmj/0` - a CMJ template Volume and template-style example files
- `cmj/i` - CMJ Volume I (Spring 2025) (unpublished)
- `ugs/v` - UgS (V) drawing/source files and abstract notes
- `skills/draw.md` - TikZ drawing skill for CMJ covers and UgS posters

## Building the journal

The journal sources use **pdfLaTeX**.

From a volume directory such as `cmj/i`:

```bash
pdflatex main
pdflatex main
```

Or with `latexmk`:

```bash
latexmk -pdf main
```

If you are using Overleaf, upload the volume folder and set `main.tex` as the main document.

## Repository layout

```text
README.md
cmj/
  0/
  i/
ugs/
  v/
skills/
```

## Notes

- Each journal volume has its own `main.tex` and `cmj.sty`.
- Articles are included from the `articles/` folder and front matter from `front/`.
- Supporting paper assets live under `articles/papers/` inside each volume.
- The repository includes generated PDF and auxiliary files from recent builds; those are not required to edit or rebuild the sources.
