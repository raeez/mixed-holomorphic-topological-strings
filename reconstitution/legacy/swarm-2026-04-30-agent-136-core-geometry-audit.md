# Agent 136 Core Geometry Audit

Date: 2026-04-30.

Owned writable surface: `main.tex`, `abstract.tex`, `theorem-lanes.tex`,
and this report. No subagents were launched.

Staged by Agent 136: `abstract.tex`, `main.tex`, `theorem-lanes.tex`, and
`reconstitution/swarm-2026-04-30-agent-136-core-geometry-audit.md`. The
index already contained other active-swarm staged files; Agent 136 did
not unstage or modify those paths.

## Stable Core

The theorem surface is the formal-local mixed holomorphic-topological SFT
on
\[
  \mathbb R^2_{\mathrm{top}}\times
  \widehat{\mathbb C^2}_{0,\mathrm{hol}},
\]
with brane line
\(\mathbb R_{\mathrm{brane}}\times\{0\}\times\{0\}\), Hamiltonian BF
closed sector for the formal symplectic disk
\((\operatorname{Spf}\mathbb C[[z_1,z_2]],dz_1\wedge dz_2)\), and the
Dirac/Koszul matrix brane probe. The preserved Calabi-Yau datum is local
unimodularity: \(dz_1dz_2\), the BV pairing, divergence, residue/cyclic
trace density, and Hamiltonian divergence-free fields modulo constants.

## Valid Attacks

`A136-01` Severity 2. The abstract opened on the symplectic disk without
first naming the ambient mixed geometry, and its exclusion list omitted
CoHA, quintic, HKQ/CDGP/GV/OSV, and Abel--Jacobi comparison lanes.
Healed in `abstract.tex:2` and `abstract.tex:102`.

`A136-02` Severity 2. BCOV/Kodaira-Spencer source-convention language in
the local-sector definitions could still be read as compact CY3 input.
Healed by naming
\(\mathbb R^2_{\mathrm{top}}\times\widehat{\mathbb C^2}_{0,\mathrm{hol}}\)
as the active geometry and isolating BCOV as source convention only.
Anchors: `main.tex:180`, `main.tex:933`, `main.tex:1049`.

`A136-03` Severity 2. The global Hamiltonian restriction proposition sat
inside the local model as though it were part of the theorem input.
Healed as an external formal-stalk firewall, not a hypothesis of
Theorem~\ref{thm:main-local}. Anchors: `main.tex:1078`,
`main.tex:1091`, `main.tex:1153`.

`A136-04` Severity 2. The cyclic Calabi-Yau open-field convention and the
point-brane residue remark could be mistaken for a compact/global
Calabi-Yau assumption. Healed by identifying the only used datum as the
local two-dimensional residue/cyclic pairing on the skyscraper Ext
algebra. Anchors: `main.tex:1200`, `main.tex:2314`.

`A136-05` Severity 2. Analytic graph-realization paragraphs allowed
Costello--Li BCOV/HCS and compactification language to appear as
mechanisms for the local theorem. Healed by marking these as external
analytic or negative source-comparison data. Anchors: `main.tex:1632`,
`main.tex:2578`, `main.tex:3649`, `main.tex:6685`.

`A136-06` Severity 3. The matched-conventions firewall did not enumerate
all quarantined lanes named by the principal. Healed by adding CoHA,
quintic, HKQ/CDGP/GV/OSV, Abel--Jacobi, Igusa, Borcherds/BKM, and
sister-volume exclusions. Anchors: `main.tex:7053`, `main.tex:8046`,
`theorem-lanes.tex:1668`.

`A136-07` Severity 4. The necklace proof used "Abel map" terminology for
an elementary circle-sum map. This was not Abel--Jacobi theory, but it
was ambiguous in the present audit. Healed by renaming it throughout the
local proof. Anchors: `main.tex:3965`, `main.tex:4567`.

## Build-Hygiene Addendum

`B136-01` Status: stale or already repaired before Agent 136 inspection.
Agent 137 reported a TeX blocker at `main.tex:5103`, with
`\drop:open-descendant-action` parsed as an undefined control sequence.
Current `main.tex` has no such token. The relevant source has the valid
label `\label{prop:open-descendant-action}` at `main.tex:5042` and valid
references at `main.tex:751`, `main.tex:3994`, `main.tex:5111`,
`main.tex:5428`, and `main.tex:5492`. No source edit was required for
this token.

Verification: repo-wide search found no `\drop:open-descendant-action`
or `\drop` token in source. A one-pass `pdflatex` run into
`/tmp/topological-strings-agent136-build` passed the reported
`main.tex:5103` region and stopped later at
`tate-T1-weighted-completion.tex:2211` with `Missing $ inserted`, outside
Agent 136's writable surface.

## Repairs Made

- `abstract.tex`: front-loaded the active
  \(\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}\)
  geometry and expanded the no-consequence firewall.
- `main.tex`: strengthened BCOV/CY source-convention language, converted
  global Hamiltonian material to a formal-stalk firewall, localized the
  cyclic Ext pairing, quarantined analytic BCOV/HCS input, renamed the
  local Abel terminology, and expanded matched-conventions exclusions.
- `theorem-lanes.tex`: expanded the scalar-anomaly lane exclusions to
  cover compact CY, CoHA, quintic, OSV/GV, Abel--Jacobi, Igusa, and
  Borcherds/BKM.

## Theorem Labels Touched

- `prop:formal-local-global-restriction`
- `def:local-th-string`
- `thm:main-local`
- `prop:skyscraper-ext`
- `prob:analytic-graph-realization`
- `prob:formal-factorization-center`
- `stmt:costello-li-flat-bcov`
- `thm:matched-conventions-transfer`
- `thm:lane-u1-anomaly` by theorem-lane scope text

## Verification

- `rg -n "Calabi|CY|CY3|compact Calabi|compact CY|BCOV|CoHA|quintic|OSV|GV|Gopakumar|Vafa|Abel|Jacobi|Igusa|BKM|Borcherds|MNOP|CDGP|HKQ|Vol III|sister-volume|global" main.tex abstract.tex theorem-lanes.tex`
- `rg -n -F -e "BCOV Hamiltonian" -e "Abel-map" -e "Abel coordinate" -e "global CY-to-chiral input" -e "maximal global statement" -e "compactified avatar" -e "global BV/gauge-fixing" -e "Global local-Hamiltonian restriction" abstract.tex main.tex theorem-lanes.tex`
- `git diff --check -- abstract.tex main.tex theorem-lanes.tex`
- `rg -n "\\\\drop:open-descendant-action|drop:open-descendant-action|\\\\drop" main.tex abstract.tex theorem-lanes.tex`
- `pdflatex -halt-on-error -interaction=nonstopmode -file-line-error -output-directory=/tmp/topological-strings-agent136-build main.tex`
- `rg -n "drop:open-descendant-action|Undefined control sequence|Fatal error" /tmp/topological-strings-agent136-build/main.log`

The forbidden-phrase scan returned no stale hits for the repaired
phrases. The remaining BCOV/CY/global hits are source-convention,
negative applicability, local-unimodularity, bibliography, or explicit
matched-conventions firewall text. The `\drop` blocker did not reproduce
from current `main.tex`. `git diff --check` passed.

I did not run `make pdf`; the checkout has a large active swarm state and
the requested ownership surface excludes build artifacts. The `/tmp`
`pdflatex` run was used only to verify the reported `main.tex` blocker
without writing `out/main.pdf`.

## Remaining Obligations

The non-scalar graph/QME vanishing, finite-window counterterms,
bulk-to-defect kernel, and any genuine compact/global comparison remain
outside the stable core. Any future use of compact Calabi-Yau, CoHA,
quintic, HKQ/CDGP/GV/OSV, Abel--Jacobi, Igusa, or BKM material requires a
separate matched-conventions theorem and obstruction-class vanishing.
