# Agent 150 Local Build / Reference Audit

Scope: report-only audit after the local-geometry correction wave.  Writable
surface was restricted to this report, except for a possible direct trivial
TeX build blocker.  No source patch was needed.

Principal correction enforced: the core paper is the formal-local mixed
HT SFT on `R^2_top x C^2_hol`.  Compact Calabi-Yau, CoHA, quintic,
OSV/GV, Abel-Jacobi, MNOP, Vol III, Igusa, Borcherds, and BKM material
is external comparison only.

## Build Status

Status: PASS for an isolated draft build.

I did not run `make pdf` and did not touch `out/main.pdf`.  The tracked
`out/main.pdf` was already dirty in the shared checkout and remained outside
this agent's surface.

Clean isolated build protocol:

```bash
mkdir -p /tmp/topological-strings-agent150-clean
# copied main.tex into /tmp and supplied empty /tmp main.aux/main.toc
cd /tmp/topological-strings-agent150-clean
TEXINPUTS=.:/Users/raeez/topological-strings//: \
  pdflatex -halt-on-error -interaction=nonstopmode \
  -draftmode -file-line-error main.tex
```

Result after repeated isolated passes: exit 0.  The final `/tmp` log has
no fatal TeX error, no undefined-reference warning, and no multiply-defined
label warning.  Remaining nonfatal warnings found by log scan:

```text
Overfull hbox at tate-T1-weighted-completion.tex line 1531
Overfull hbox at tate-T1-weighted-completion.tex line 1839
Overfull hbox at appendix-radial-parts-moyal.tex line 584
```

The third pass had one transient undefined reference:
`prop:universal-scalar-contact-bracket-rows` at
`tate-P1-hadamard-mittag-leffler.tex:1202`.  Static scan and aux inspection
showed the label exists at `tate-P1-hadamard-mittag-leffler.tex:1011`; the
later isolated pass cleared the warning.  This was cross-reference churn,
not a source defect.

## Valid Attacks

`A150-01` Stale root auxiliary-file hazard.

Non-isolated draft builds that read the repo-root ignored `main.aux` can stop
at `main.aux:690` with `Missing number, treated as zero`.  The offending stale
entry is a bookmark row for `Igusa: Delta5, BKM superalgebra,
Mukai-Heisenberg centre`.  This is generated aux state, not manuscript source.
The clean `/tmp` build with empty aux/toc files does not reproduce the fatal
error.

Recommendation: do not treat this as a TeX source blocker.  Build from a clean
aux state when checking the current manuscript.

`A150-02` Reference scan after Agents 136-149.

Reports for Agents 136 through 149 are present.  Agent 136 recorded an older
`\drop:open-descendant-action` / `main.tex:5103` build blocker; later reports
and the present clean build show it is no longer fatal.  Agent 144 recorded a
repair for the `tate-T1-weighted-completion.tex:2211` fatal equation/label
issue.  Agent 146 recorded a one-pass `/tmp` build with ordinary undefined
references only.  Agents 147-149 added source-fixture, appendix, dictionary,
and theorem-lane material; the present static and LaTeX checks found no
undefined label introduced by those reports.

Static checks:

```bash
perl -0ne '...' main.tex abstract.tex claim-strength-ledger.tex \
  local-dictionary.tex principles.tex theorem-lanes.tex open-obligations.tex \
  appendix-*.tex tate-*.tex frontier_mnop_framing_volume.tex
```

Results: no duplicate labels, and no `\ref`/`\eqref` target absent from the
source label set.

`A150-03` Compact/global leakage scan.

Targeted `rg` scan for compact/global terms across core TeX files found
quarantine and matched-conventions language, not an unguarded import into the
local theorem surface.

Representative guarded hits:

- `abstract.tex:102-104`: no global BCOV, compact Calabi-Yau, CoHA, quintic,
  HKQ/CDGP/GV/OSV, Abel-Jacobi, MNOP/chiral-volume, Vol III, Igusa,
  Borcherds/BKM consequence follows here.
- `claim-strength-ledger.tex:58-59`, `585-590`: external-only source routing;
  not theorem support for compact-CY consequences.
- `local-dictionary.tex:152-157`: explicit do-not-import row for compact CY,
  GV, MNOP, quintic, OSV/GV, Abel-Jacobi, CoHA, Igusa/BKM, and Vol III.
- `theorem-lanes.tex:320-346`, `1905-1946`: explicit exclusions from local
  theorem lanes.
- `main.tex:7053-7061` and `main.tex:8050-8068`: firewall language requiring
  separate matched-conventions data for any external target.
- `tate-T4-bv-vanishing.tex:18-37`: restates Costello-Li compact BCOV
  hypotheses only to separate them from the local `R^2 x C^2` brane-defect
  coefficient problem.
- `tate-P3-universality.tex:553-590` and `tate-P5-cross-volume.tex:678-700`:
  external-target obstruction language, not a local theorem import.
- `frontier_mnop_framing_volume.tex`: standalone frontier note.  It is not
  `\input` or `\include`d by `main.tex`.

Conclusion: no valid compact-CY/CoHA/quintic/OSV/GV/Abel-Jacobi/Igusa/BKM
leakage attack survived this local scan.

## Fixes Made

No manuscript or source-reference patch was made.  Only this audit report was
created.

## Commands / Results

```bash
ls reconstitution/swarm-2026-04-30-agent-13[6-9]*.md \
   reconstitution/swarm-2026-04-30-agent-14[0-9]*.md
```

Result: reports for Agents 136 through 149 exist.

```bash
rg -n -i "(compact[ -]?(cy|calabi)|calabi[- ]?yau|CY_?3|threefold|quintic|\
\bcoha\b|\bosv\b|gopakumar|\bgv\b|\bmnop\b|abel[- ]?jacobi|igusa|\
\bbkm\b|borcherds|vol iii|hkq|cdgp|compactification|worldsheet|\
instanton|mirror|global bcov|global moduli|global theorem|compact hodge)" \
  main.tex abstract.tex claim-strength-ledger.tex local-dictionary.tex \
  principles.tex theorem-lanes.tex open-obligations.tex appendix-*.tex \
  tate-*.tex frontier_mnop_framing_volume.tex
```

Result: guarded/firewall/external-comparison hits only, as classified above.

```bash
rg -n "include\{frontier_mnop|input\{frontier_mnop|frontier_mnop" main.tex *.tex
```

Result: no `main.tex` inclusion of `frontier_mnop_framing_volume.tex`.

```bash
rg -n "undefined|Undefined|Label\(s\)|Fatal|LaTeX Error|multiply defined|\
Foreign command|Overfull" /tmp/topological-strings-agent150-clean/main.log
```

Result: only the three overfull boxes listed above in the final isolated log.

```bash
git status --short -- main.aux main.log main.toc out/main.pdf \
  reconstitution/swarm-2026-04-30-agent-150-local-build-reference-audit.md
```

Result before this report was written: only `M out/main.pdf` appeared; root
aux/log/toc were not modified by this audit.

## Remaining Obligations

- Keep all compact-CY/CoHA/quintic/OSV/GV/Abel-Jacobi/MNOP/Vol III/Igusa/BKM
  rows as external comparison or matched-conventions targets only.
- For local theorem strength, the remaining mathematical obligations are the
  ones already named in the manuscript and recent reports: non-scalar
  Costello kernel/QME construction, regular-density versus wavefront-current
  restrictions, finite-window-to-limit compatibility, and the residual scalar
  projection obstruction.
- Build hygiene: a clean aux state is required before diagnosing source TeX.
  The stale root `main.aux` can produce a false fatal error.
- Typography: the three overfull boxes above remain nonfatal cleanup items.
