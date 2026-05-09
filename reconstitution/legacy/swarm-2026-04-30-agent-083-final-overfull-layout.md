# Agent 083 Final Overfull Layout Repair

Lane: final overfull layout repair after Agent 077 clean build.

## Warnings found

- `local-dictionary.tex`: overfull `\vbox`, `61.49878pt` too high, while
  outputting the first local-dictionary page.  Source anchor:
  `local-dictionary.tex:13--120`, the non-breakable canonical maps table.
- `local-dictionary.tex:284--285`: overfull `\hbox`, `17.2633pt` too wide,
  caused by `cofactorization/opposite-interval` in the source--target
  status longtable.
- `appendix-radial-parts-moyal.tex:711`: overfull `\hbox`, `85.42854pt` too
  wide, caused by the final text line in the finite arithmetic checklist
  display.

## Ownership check

`reconstitution/swarm-live-launch-log-2026-04-30.md` marks Agents 058 and 059
closed.  The remaining live agents 079--082 own source-provenance, source
fixtures, abstract/frontmatter, and CoHA-provenance lanes, not the two
overfull source files.  Pre-edit `git diff` showed no local unstaged or staged
delta in `local-dictionary.tex` or `appendix-radial-parts-moyal.tex`.

## Edits

- Converted the first local-dictionary table from `tabular` inside `center`
  to a breakable `longtable`, preserving columns, headers, row order, and
  mathematical content.
- Inserted `\allowbreak{}` after the slash in
  `cofactorization/opposite-interval`.
- Split the final radial-Moyal checklist text into three display lines.

No theorem, claim strength, formula, coefficient, sign, or citation was
changed.

## Checks run

- `git diff --check`: clean.
- `make pdf`: pass, exit code `0`; final `out/main.pdf` has 255 pages and
  size 1,502,615 bytes.
- `rg -n "Overfull \\\\[hv]box|Overfull" out/main.log`: no hits.
- Reference/fatal scan for undefined controls, fatal errors, emergency stops,
  undefined references/citations, and label-change rerun warnings: no hits.

## Files changed

- `local-dictionary.tex`
- `appendix-radial-parts-moyal.tex`
- `reconstitution/swarm-2026-04-30-agent-083-final-overfull-layout.md`

The build touched the already-unstaged generated artifact `out/main.pdf`; it
is not part of this lane's staged ownership.

## Residual layout status

- Overfull `\hbox`: `0`.
- Overfull `\vbox`: `0`.
- Underfull `\hbox`: `25`.
- Underfull `\vbox`: `0`.

The three Agent 077 overfull warnings are cleared.  Remaining underfull hboxes
were outside this lane and were not chased.
