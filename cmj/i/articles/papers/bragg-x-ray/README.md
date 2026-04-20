# Pepadun Journal Template

**Electronic Publication for the Development of Digital Applications for the Nation**  
Official LaTeX template for academic articles in Pepadun Journal. This template meets all journal formatting requirements and is ready to use on Overleaf or local LaTeX systems.

![Pepadun Journal Banner](https://pepadun.fmipa.unila.ac.id/public/site/images/jmanajer/header-pepadun-new.jpg)

## Key Features
✅ Standard academic journal format  
✅ Professional header/footer with journal info  
✅ Automatic reference management (IEEE style)  
✅ Optimized figure & table environments  
✅ Automatic equation numbering  
✅ Multi-author support with affiliations  
✅ Custom abstract & keywords format  
✅ Overleaf & local LaTeX compatible  

## File Structure
```
pepadun-template/
├── main.tex             # Main document file
├── pepadun.sty          # Custom style file
├── pepadun.bib          # Reference database
├── unila-logo.png       # Sample image
└── README.md            # This documentation
```

## Using on Overleaf

1. **Create a new project** at [overleaf.com](https://www.overleaf.com/)
2. **Upload files**:
   - Click "New Project" → "Upload Project"
   - Select all template files (`main.tex`, `pepadun.sty`, `pepadun.bib`)
3. **Compile**:
   - Set compiler to **LaTeX** (Top-right menu)
   - Click "Recompile"
4. **Start Writing**:
   - Edit `main.tex` for article content
   - Add references in `pepadun.bib`

## Local Compilation
```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

## Content Guide

### 1. Article Metadata
```latex
\title{Your Article Title}
\author{
    \textsuperscript{1}First Author Name,
    \textsuperscript{2}Second Author Name and
    \textsuperscript{3}Last Author Name \\[6pt]
    \textsuperscript{1,2}Affiliation of Authors 1 & 2 \\
    \textsuperscript{3}Affiliation of Author 3 \\ 
    Institution Address, City, Country \\[6pt]
    e-mail: \textsuperscript{1} email1@institution.edu,
    \textsuperscript{2} \href{mailto:email2@institution.edu}{\uline{email2@institution.edu}}
}
```

### 2. Abstract & Keywords
```latex
\begin{abstract}
Abstract text (200-300 words)...
\end{abstract}

\keywords{keywords; separated; by semicolons; maximum five}
```

### 3. Figures & Tables
**Figure:**
```latex
\begin{pepadunfigure}{Figure Title}
    \includegraphics[width=0.5\textwidth]{filename.png}
\end{pepadunfigure}
```

**Table:**
```latex
\begin{pepaduntable}{Table Title}
    \begin{tabular}{@{}l c r@{}}
        \toprule
        Header 1 & Header 2 & Header 3 \\
        \midrule
        Data 1 & Data 2 & Data 3 \\
        \bottomrule
    \end{tabular}
\end{pepaduntable}
```

### 4. References
1. Add new entries in `pepadun.bib`
2. Cite in text: `\cite{reference_key}`
3. References automatically format to IEEE standards

## Format Specifications
- **Paper Size**: A4
- **Margins**: Top 3.25cm, Others 2cm
- **Font**: Times New Roman 11pt
- **Spacing**: 1.15 (one-and-half spaced)
- **Header**: Journal name & volume
- **Footer**: Center-aligned page numbers

## Customization Tips
1. **Journal Volume**:
   - Edit in `pepadun.sty`:
     ```latex
     \fancyhead[R]{\textit{Vol. 5, No. 2, Year 2024}} % Update with current issue
     ```

2. **Institution Logo**:
   - Replace `unila-logo.png` with your logo
   - Adjust size in `width=0.3\textwidth`

3. **References**:
   - Export references from Mendeley/Zotero in BibTeX format
   - Paste into `pepadun.bib`

## Troubleshooting
- If compilation fails:
  1. Set compiler to **LaTeX** (not pdfLaTeX)
  2. Ensure Biber runs as part of compilation process
  3. Check Overleaf logs for specific error messages

## Contribution
This template is developed by Pepadun Journal Development Team. Technical issues can be reported through:
- [Overleaf Issues](https://www.overleaf.com/project)
- Email: jurnalpepadun@fmipa.unila.ac.id

## License
Template licensed under [MIT License](LICENSE). Users are free to:
- Use for article preparation
- Modify for specific needs
- Redistribute with attribution

---

**Pepadun Journal**  
Faculty of Mathematics and Natural Sciences  
University of Lampung  
[pepadun.fmipa.unila.ac.id](https://pepadun.fmipa.unila.ac.id)


## Key Information for Overleaf Users

1. **Reference Management**:
   - Use BibTeX format for all references
   - DOI links automatically appear instead of URLs

2. **Language Support**:
   - Template uses English as primary language

3. **Special Features**:
   - Automatic header with journal info on every page
   - Clean reference formatting with DOI prioritization
   - Optimized spacing for academic readability

This template is production-ready for Pepadun Journal submissions. The clean IEEE-compliant formatting ensures your research meets publication standards while focusing on content quality. Happy writing!