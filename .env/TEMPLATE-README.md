# How to Add a New Article to *The Constructor Mathematics Review*

## Quick Start

1. **Copy the template.**
   Copy `article-template.tex` and rename it following the convention:

   ```
   article-NN-short-name.tex
   ```

   where `NN` is the next two-digit number (e.g. `04`).

2. **Fill in the header.**
   Open your new file and update the five arguments of `\articleheader`:

   ```latex
   \articleheader
     {Your Article Title}
     {Your Name}
     {Constructor University Bremen}
     {Your abstract text here.}
   ```

3. **Write your content.**
   Add sections directly or use `\input{}` to include separate `.tex` files.
   Available environments:

   | Environment      | Use for          | Colour       |
   |------------------|------------------|--------------|
   | `definitionbox`  | Definitions      | Red frame    |
   | `theorembox`     | Theorems         | Blue frame   |
   | `notebox`        | Side notes       | Lavender     |
   | `theorem` (amsthm) | Inline theorems | Standard  |

4. **Add references.**
   Use the `\articlereferences` command followed by a numbered list:

   ```latex
   \articlereferences
   \begin{enumerate}[label={[\arabic*]}, leftmargin=2em, itemsep=0.25em]
     \item A.~Author, ``Title,'' \textit{Journal}, 2025.
   \end{enumerate}
   ```

5. **Register in `main.tex`.**
   Add two lines:

   ```latex
   % In the Articles section:
   \input{article-NN-short-name}

   % In the Table of Contents block:
   \contentsentry
     {Your Article Title}
     {Your Name}
     {art:yourlabel}
   ```

   Make sure the label in `\contentsentry` matches the `\label{art:yourlabel}`
   in your article file.

## Compilation

This project uses **pdfLaTeX** (no BibTeX/Biber required):

```
pdflatex main
pdflatex main
```

Two passes are needed so that page references in the Table of Contents
resolve correctly.

On **Overleaf**, simply upload the full project folder and set `main.tex`
as the main document.

## Project Structure

```
journal-i/
├── main.tex                     Root document
├── cumsj.sty                    Journal style package
├── journal-cover.tex            Cover page (TikZ artwork)
├── journal-editorial.tex        Editorial / letter from editors
├── article-01-shannon.tex       Paper 1 wrapper
├── article-02-shor.tex          Paper 2 wrapper
├── article-03-placeholder.tex   Paper 3 placeholder
├── article-template.tex         ← copy this to add articles
├── TEMPLATE-README.md           This file
├── Shannon_s_Theorem_and_Polar_Codes/   Original paper 1
└── The_Qubit_and_Shor_s_Algorithm/      Original paper 2
```

## Tips

- **Images:** Place images in a subfolder and add it to `\graphicspath`
  in `cumsj.sty`, or use a full relative path in `\includegraphics`.
- **Custom commands:** If your article needs new commands, define them
  locally inside your article file (not in `cumsj.sty`) to avoid
  conflicts.
- **Section numbering** resets automatically with each `\articleheader`.
- **Colours:** Use `cujblue`, `cujgold`, `cujdark`, `cujgray` for
  consistency with the journal theme.
