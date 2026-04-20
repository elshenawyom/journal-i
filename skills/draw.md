# CMJ TikZ Drawing Skill (draw.md)

## Purpose
Turn one abstract into one compile-ready standalone TikZ drawing that communicates exactly one key idea, using CMJ cover style and an implicit square-balanced layout with natural (not perfect) variation.

## Input Contract
- Input is a single abstract paragraph.
- Optional extra input:
  - `focus`: explicit main concept (if omitted, infer one)
  - `density`: `minimal | medium` (default: `minimal`)

## Output Contract
- Output exactly one full `.tex` file using `standalone`.
- No explanation outside the TeX block.
- The output must compile with `pdflatex`.
- The drawing must contain one dominant object/motif only.
- The source must include these two comment lines near the start of the TikZ content:
  - `% Title: ...`
  - `% Figure illustrates ...`

## Non-Negotiable Constraints
1. Single-key-idea rule:
   - Show only one central object/motif.
   - No triptychs, no pipelines, no multi-panel layouts.
   - No second independent object cluster.
2. No top-title rule:
   - Do not render a title above the drawing.
   - Title belongs only in source comments.
3. Approximate square-balance rule:
   - Composition must fit a square frame implicitly.
   - The object should reach outward in all four directions with close (not exact) extents.
   - Small directional deviations are acceptable; do not force perfect geometric alignment.
   - Do not draw the frame itself.
   - Do not draw guide boxes, boundary outlines, or center crosshairs.
4. Anti-logo rule:
   - Do not output a flat emblem/icon look.
   - Include internal structure and progression from center to boundary.
5. No-guide-geometry rule:
   - Do not use dashed or dotted decorative scaffolding.
   - Do not add faint construction layers, helper rings, or background guide shapes.
   - Every visible stroke must belong to the actual object, not to layout guidance.
6. Text-minimal rule:
   - Maximum three short visible labels (1-3 words each).
   - Optional one equation line.
   - No paragraphs, legends, or top headings.

## CMJ Style Rules
1. Use a white background.
2. Use `cmjcrimson` as the main structural color.
3. Use `cmjgold` only as a sparse accent for the key invariant/arrow/vector.
4. Use only semantically meaningful structure strokes; avoid background scaffolding artifacts.
5. Keep motifs geometric and publication-ready (no clip-art).

## Mandatory TeX Skeleton
Use this exact structure unless a strong reason requires extra packages:

```tex
\documentclass[tikz,border=8pt]{standalone}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[sc]{mathpazo}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,fit,backgrounds,decorations.pathmorphing}

\definecolor{cmjcrimson}{RGB}{155,20,30}
\definecolor{cmjgold}{RGB}{186,145,40}
\definecolor{cmjdark}{RGB}{35,35,35}
\definecolor{cmjgray}{RGB}{128,128,128}

\begin{document}
\begin{tikzpicture}[>=Stealth, line cap=round, line join=round, font=\small]
   \path[use as bounding box] (-4,-4) rectangle (4,4); % square canvas only
   % Title: <short title>
   % Figure illustrates <one-sentence statement of the single key idea>.
   % no rendered title at the top
   % no visible frame box, no dashed guide frame, no center crosshair
  % drawing content
\end{tikzpicture}
\end{document}
```

## Workflow
1. Extract the single most important idea from the abstract.
2. Choose one motif that alone can encode that idea.
3. Build a centered square composition with close four-direction reach, allowing natural asymmetry.
4. Keep all supporting marks as variations of the same motif (not separate scenes).
5. Apply strict text budget.

## Quality Checklist
- Exactly one central object/motif is visible.
- No rendered title appears at the top of the figure.
- The figure reads inside an implicit square frame.
- The motif reaches toward all four directions with close (not exact) outer extents.
- No visible frame box appears in the artwork.
- No decorative dashed/dotted guide lines appear.
- No faint helper rings, shells, or construction underlays appear.
- No center crosshair appears.
- The drawing is not a logo-like isolated icon.
- Source comments include `Title` and `Figure illustrates ...`.
- Visible text is minimal and short.
- Crimson dominates; gold appears only as accent.
- Standalone file compiles.

## Reusable Prompt
Copy this prompt and replace `{{ABSTRACT}}`:

```text
You are drawing for the Constructor Mathematical Journal.
Given the abstract below, produce exactly one standalone TikZ .tex file.

Abstract:
{{ABSTRACT}}

Hard constraints:
- Show exactly one key object/idea.
- Do not render a title at the top of the drawing.
- Fit composition into an implicit square frame.
- Make the object's outer reach in left/right/up/down close in length, but not perfectly equal.
- Do not draw frame boxes, dashed guide frames, or center crosshairs.
- Do not draw helper underlays, construction rings, or layout scaffolding.
- Avoid logo-like output; include internal structure from center to boundary.
- Keep visible text minimal: up to three short labels and optional one equation.
- CMJ style: white background, crimson primary, sparse gold accents.
- Add source comments: `% Title: ...` and `% Figure illustrates ...`.
- No multi-panel or pipeline layout.
- Output only TeX code for a standalone document.
```
