# Local Build Gate Report

Date: 2026-04-30.

Scope: report-only build/reference/firewall gate for the current
`topological-strings` checkout after the chiral/QME integration and
bibliography repair.  Shared checkout source files were read only.  The only
repository write is this report.

## Commands and Results

Control files read:

```bash
sed -n '1,220p' CLAUDE.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md
sed -n '1,300p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '129,170p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '143,170p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
```

Build isolation:

```bash
mktemp -d /tmp/topological-strings-agent173.XXXXXX
rsync -a --exclude=.git --exclude=out --exclude=out_test --exclude=.build_logs \
  --exclude='*.aux' --exclude='*.log' --exclude='*.toc' --exclude='*.idx' \
  --exclude='*.ilg' --exclude='*.ind' --exclude='*.nlo' --exclude='*.nls' \
  --exclude='*.bbl' --exclude='*.blg' ./ /tmp/topological-strings-agent173.7BMtwt/
mkdir -p out
```

Result: isolated build root
`/tmp/topological-strings-agent173.7BMtwt`.  No in-repository `make pdf` was
run.  No shared-checkout `out/main.pdf` write was performed.

TeX passes:

```bash
pdflatex -output-directory=out -interaction=nonstopmode -file-line-error main.tex
for pass in 2 3 4 5 6 7; do
  pdflatex -output-directory=out -interaction=nonstopmode -file-line-error main.tex \
    > "agent173-pass${pass}.stdout" 2>&1
  cp out/main.log "agent173-pass${pass}.main.log"
done
```

Result: passes 1--7 returned `0`.  Final product:

```text
out/main.pdf: 352 pages, 1956253 bytes
out/main.log: 1.8M
out/main.aux: 190K
out/main.toc: 8.9K
```

Fatal/error scan on the final log:

```bash
rg -n -e '^! ' -e 'Emergency stop' -e 'Runaway argument' \
  -e 'Fatal error' -e 'Undefined control sequence' \
  -e 'File ended while scanning' -e 'No pages of output' \
  -e 'LaTeX Warning: (Reference|Citation).*undefined' \
  -e 'There were undefined references' \
  -e 'Rerun to get cross-references right' \
  -e 'Label\(s\) may have changed' out/main.log
```

Result: no matches.  No fatal TeX errors.  No undefined references or
citations after reruns.  No rerun request remained.

Focused label/citation scan over bound manuscript inputs:

```text
labels=512
refs=345
cites=24
bibkeys=37
duplicate_labels=0
missing_refs=0
missing_cites=0
```

The scan covered `main.tex`, frontmatter inputs, theorem lanes, Tate
fragments, open obligations, and the bound appendices.  Raw primary-source
TeX mirrors under `references/primary-sources/` were excluded from this
label/citation gate because they are source fixtures, not bound manuscript
inputs.

Layout diagnostics in the final log:

```text
box warnings=56
overfull warnings=4
```

The overfull entries are nonfatal:

```text
Overfull \vbox (96.60744pt too high) while \output is active
Overfull \hbox (1.29213pt too wide) detected at line 1531
Overfull \hbox (15.05399pt too wide) detected at line 1839
Overfull \hbox (9.61589pt too wide) detected at line 584
```

## Firewall Scan

Command form:

```bash
rg -n -i -e 'compact Calabi|compact CY|compact threefold|Calabi--Yau|Calabi-Yau|quintic|OSV|GV|Gopakumar|MNOP|CoHA|BKM|Igusa|Borcherds|holomorphic anomaly|worldsheet instanton|mirror quintic|Abel--Jacobi|Abel-Jacobi|global BCOV|Vol III' \
  abstract.tex main.tex claim-strength-ledger.tex local-dictionary.tex theorem-lanes.tex \
  open-obligations.tex appendix-factorization-current-conventions.tex \
  appendix-unreduced-bv-qme.tex appendix-radial-parts-moyal.tex \
  tate-P3-universality.tex tate-P5-cross-volume.tex
```

Hit counts:

```text
abstract.tex:3
main.tex:25
claim-strength-ledger.tex:9
local-dictionary.tex:15
theorem-lanes.tex:12
open-obligations.tex:4
appendix-factorization-current-conventions.tex:7
appendix-unreduced-bv-qme.tex:3
tate-P3-universality.tex:9
tate-P5-cross-volume.tex:22
```

Adjudication: no fatal compact/global leakage found in the bound core theorem
surface.  The hits fall into three accepted classes:

1. Local unimodularity/source-convention language: the only Calabi--Yau datum
   in the core is the formal local holomorphic volume/residue/cyclic pairing.
2. Explicit exclusion language: "not used", "not a consequence", "no compact
   CY3 BCOV theorem", "no CoHA", "requires its own matched-conventions
   theorem".
3. Matched-conventions appendices: global, Vol III, Igusa/BKM, compact BCOV,
   MNOP/chiral-volume, and related targets appear as external obstruction
   data, not as inputs to the local theorem.

The abstract and local dictionary correctly foreground the constructed object:
the formal Hamiltonian holomorphic factorization algebra
`\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}`, with mixed/current/Weyl-Moyal/defect
avatars and a separate firewall against one-dimensional VOA/OPE and compact
target overclaims.

The standalone file `frontier_mnop_framing_volume.tex` was also inspected as a
non-bound surface.  It is not input by `main.tex`; its compact-CY, MNOP, CoHA,
quintic, GV, OSV, and BKM language is explicitly framed as standalone frontier
or source-obligation material, not as evidence for the local
`\R^2_{\mathrm{top}}\times\C^2_{\mathrm{hol}}` theorem.

## Attack Ledger

`A173-01` TeX fatal build blocker.  Status: invalid.  Evidence: seven isolated
`pdflatex` passes returned `0`; final log has no fatal-error patterns.

`A173-02` Undefined references or citations after reruns.  Status: invalid.
Evidence: final log has no undefined-reference or undefined-citation warnings;
independent source scan reports `missing_refs=0`, `missing_cites=0`.

`A173-03` Duplicate label instability.  Status: invalid.  Evidence:
independent label scan reports `duplicate_labels=0`; final log has no
multiply-defined-label warning.

`A173-04` Compact/global theorem leakage into the local core.  Status: invalid
for the current gate.  Evidence: focused scan found only local
unimodularity/source-convention uses, explicit exclusion language, and external
matched-conventions obstruction data.

`A173-05` Layout warnings.  Status: valid non-core.  Evidence: final log has
56 box warnings, including 4 overfull warnings.  These do not block the stated
fatal-error/reference gate.

## Fixes

None.  No trivial inactive-file build blocker occurred.  No source file was
modified.

## Remaining Build Obligations

1. Layout pass if a typography gate is opened: resolve or consciously accept
   the 56 box warnings, especially the 96.60744pt overfull vbox and the
   15.05399pt overfull hbox.
2. A normal in-repository release build remains the integration owner's task.
   This report deliberately did not run `make pdf` and did not update
   `out/main.pdf`.
3. Mathematical obligations remain exactly those named in the manuscript:
   weighted RG/locality, non-scalar QME operation realization, one-antifield
   lift, and matched-conventions external target data.  The build gate neither
   proves nor weakens those claims.
