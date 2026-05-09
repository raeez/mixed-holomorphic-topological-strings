# PDF visual QA report, 2026-04-28

Worktree: `/private/tmp/topological-strings-rearch-wave4-20260428-0520/visual`

Branch: `agent/topological-strings-rearch4-visual-20260428`

## Build

Built `out/main.pdf` in the isolated worktree with:

```bash
TEXINPUTS=.:/Users/raeez/latex-template//: make pdf
```

The resulting PDF has 137 pages on letter paper. `pdfinfo` reports
creation on Tue Apr 28 05:19:50 2026 SAST.

Direct `make pdf` in this worktree did not find
`raeez-math-template.sty`, because the local symlink points to a missing
relative `../latex-template` directory. The successful build therefore
used the canonical template directory through `TEXINPUTS`, with `.` kept
first so TeX resolves the worktree's `main.tex` rather than the template
repository's `main.tex`.

The final log scan found no overfull boxes and no unresolved references
or citations. It found underfull hbox diagnostics only. The build also
emitted repeated font checksum/width warnings for `ntxebgmia.vf`; no
visible glyph corruption was seen on the inspected rendered pages.

## Tools used

- `make pdf`
- `pdfinfo`
- `pdftoppm`
- `pdfjam`
- `pdftotext -layout`
- `rg`
- manual image inspection of rendered PNGs

Representative pages were rendered at 160 dpi with `pdftoppm`. Contact
sheets were produced with `pdfjam` and rendered back to PNG for a broad
pass before inspecting individual pages.

## Pages inspected

Inspected pages:

`1-8, 24-28, 46-51, 106, 122, 128, 130, 132, 136-137`

This is 27 unique pages, covering:

- title, abstract, claim-strength ledger, local dictionary, table of
  contents, and first body pages;
- theorem-lane pages;
- the Tate-T3/Quillen-equivalence region;
- the first-order figure page;
- the third-order figure page;
- appendix openings;
- final bibliography pages.

## Findings

No release-blocking visual layout failure was found in the inspected
sample.

The claim-strength ledger and local dictionary tables are tight but
readable, with no visible clipping or overlapping text. The table of
contents is stable; its continuation into the first body section is
visually coherent. The theorem-lane pages are dense but readable, and
the displayed equations and theorem blocks in the Tate-T3 lane do not
overlap or clip.

Figure 0.1 and Figure 0.2 are present, centered, and captioned. The
rendered figure assets are not missing or visibly clipped.

The appendix openings and final bibliography pages render cleanly. The
bibliography begins on the same page as the closing appendix material,
but the transition is readable and not a layout defect.

## Fixes

No TeX layout fixes were applied. No directly verified visual failure
required a scoped edit to `main.tex`, `theorem-lanes.tex`,
`claim-strength-ledger.tex`, `local-dictionary.tex`, or
`tate-T3-quillen-equivalence.tex`.

## Residuals

This was a representative page-level visual audit, not a page-by-page
inspection of all 137 pages.

Future plain `make pdf` runs in this worktree will still need either the
same `TEXINPUTS=.:/Users/raeez/latex-template//:` prefix or a separate
repair of the local `raeez-math-template.sty` symlink. The symlink repair
was outside this task's writable scope and was not performed.
