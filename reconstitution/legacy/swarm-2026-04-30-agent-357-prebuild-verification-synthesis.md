# Prebuild Verification Synthesis

Date: 2026-04-30.

Scope: report-only synthesis of Agents 342, 347, 348, and 353 before the
final root manuscript build.  No manuscript TeX was edited.  No full
`make pdf` build was run here.

## Verdict

Observed status: no root `main.tex` compile blocker is currently known from
the checked static gates.  The remaining whitespace failures live outside the
root manuscript build closure, except for ordinary staged report hygiene.

Run the final build from the repository root after active agents settle:

```bash
ts=$(date +%Y%m%d-%H%M%S)
mkdir -p .build_logs out
git status --short > ".build_logs/prebuild-status-$ts.txt"
make pdf > ".build_logs/make-pdf-$ts.log" 2>&1
```

Do not use `make release` as the build gate unless the integration owner wants
standalone builds and iCloud copying.  `make pdf` is the root manuscript gate;
capture the transcript because `out/main.log` records only the final
`pdflatex` pass.

## Root TeX Compile Blockers

Agent 342 found no fatal package, environment, brace, delimiter, citation,
bibliography, or label blocker in the changed root manuscript surface.  Current
direct checks preserve that conclusion:

- `git diff --check --` restricted to the current root build path set passed.
- `git diff --cached --check --` restricted to the same root build path set
  passed.
- `rg -n -F 'references/primary-sources' main.tex` returned no hits.

Current recursive `main.tex` input closure count is 23.  It includes the
recently relevant root files:

```text
main.tex
mathmacros.tex
authors.tex
abstract.tex
claim-strength-ledger.tex
local-dictionary.tex
principles.tex
theorem-lanes.tex
tate-T3-quillen-equivalence.tex
tate-T4-bv-vanishing.tex
tate-T1-weighted-completion.tex
tate-T2-nilpotent-truncation.tex
tate-T5-chain-level-primitive.tex
tate-P1-hadamard-mittag-leffler.tex
open-obligations.tex
tate-P3-universality.tex
appendix-matlis-principal-parts.tex
appendix-factorization-current-conventions.tex
appendix-sign-conventions.tex
appendix-full-psi-homology.tex
appendix-unreduced-bv-qme.tex
appendix-radial-parts-moyal.tex
tate-P5-cross-volume.tex
```

`preamble.tex` and `frontier_mnop_framing_volume.tex` remain changed outside
the `main.tex` closure.  They are not root build blockers.

## Cite And Label State

Agent 347's manuscript-bound verdict remains clean.  Current direct rescan of
the present tree gives:

```text
MANUSCRIPT_INPUT_CLOSURE_COUNT 23
CHANGED_MANUSCRIPT_TEX_COUNT 15
BIB_KEYS_DEFINED 39
LABELS_DEFINED 559
CITES_IN_CHANGED_MANUSCRIPT 69
REFS_IN_CHANGED_MANUSCRIPT 1335
UNDEFINED_CITES_IN_CHANGED_MANUSCRIPT_COUNT 0
UNDEFINED_REFS_IN_CHANGED_MANUSCRIPT_COUNT 0
DUPLICATE_BIB_KEYS_IN_MAIN_CLOSURE_COUNT 0
DUPLICATE_LABELS_IN_MAIN_CLOSURE_COUNT 0
EMPTY_OR_MALFORMED_COMMANDS_IN_MAIN_CLOSURE_COUNT 0
```

The label count differs by one from Agent 347's recorded 560 because this
rescan was run after concurrent changes and ignores macro-parameter placeholder
labels.  The load-bearing result is unchanged: no undefined manuscript cite,
undefined manuscript reference, duplicate root bibliography key, duplicate
concrete root label, or malformed citation/reference command was found.

External primary-source TeX fixtures retain raw-source internal defects
reported by Agent 347.  They are not input by `main.tex`:

- `references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex` has the
  raw duplicate `\label{quintic}` at lines 828 and 854.
- The same fixture has a raw unresolved `\ref{leadingconifold}` at line 1156;
  the local source defines `\label{leadingconifold.}` at line 1632.
- The untracked normal-function TeX fixtures carry many raw internal
  unresolved references.  They are external source mirrors, not manuscript
  cite/label failures.

## Raw Fixture Whitespace

Agent 348 verified Agent 342's fixture whitespace finding and classified it as
raw source fixture integrity, not root build failure.  Current direct
verification agrees:

- `git diff --cached --check --` on the four staged TeX fixtures fails.
- `git diff --check --` on those four paths passes, so the failures are staged
  additions rather than unstaged follow-up edits.
- Their SHA-256 hashes match Agent 348's recorded source-stream hashes.

Known staged TeX fixture failures:

- `references/primary-sources/gv-hep-th-9809187.tex`: blank line at EOF.
- `references/primary-sources/gv-hep-th-9812127.tex`: blank line at EOF.
- `references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex`: 114
  trailing-whitespace diagnostics.
- `references/primary-sources/osv-hep-th-0405146.tex`: 6 trailing-whitespace
  diagnostics.

Current global staged `git diff --cached --check --` is broader than Agent
353's non-blocking diagnostic expectation.  It also reports staged markdown
report whitespace and 114 trailing-whitespace diagnostics in
`references/primary-sources/hkq-compact-cy-hep-th-0612125.txt`.  These are
global commit-hygiene issues, not root `main.tex` build blockers.

Preserve the raw fixtures for the final manuscript build.  Normalization is a
separate fixture-regeneration decision and must update checksum ledgers while
stating that the local mirrors are normalized copies rather than byte-for-byte
source streams.

## Build Gate

Recommended prebuild checks from Agent 353, with the current root closure
separation preserved:

```bash
root_build_paths=(
  main.tex
  raeez-math-template.sty
  mathmacros.tex
  authors.tex
  abstract.tex
  claim-strength-ledger.tex
  local-dictionary.tex
  principles.tex
  theorem-lanes.tex
  tate-T3-quillen-equivalence.tex
  tate-T1-weighted-completion.tex
  tate-P1-hadamard-mittag-leffler.tex
  open-obligations.tex
  appendix-matlis-principal-parts.tex
  appendix-factorization-current-conventions.tex
  appendix-unreduced-bv-qme.tex
  appendix-radial-parts-moyal.tex
  tate-P5-cross-volume.tex
)
git diff --check -- "${root_build_paths[@]}" > ".build_logs/prebuild-root-diff-check-$ts.log" 2>&1
git diff --cached --check -- "${root_build_paths[@]}" > ".build_logs/prebuild-root-cached-diff-check-$ts.log" 2>&1
git diff --cached --check -- > ".build_logs/prebuild-global-cached-diff-check-$ts.log" 2>&1
make pdf > ".build_logs/make-pdf-$ts.log" 2>&1
find "${root_build_paths[@]}" -newer out/main.log -print > ".build_logs/postbuild-sources-newer-than-log-$ts.txt"
```

The two root diff-check logs should be empty.  The global cached diff-check
log is diagnostic under the current raw-fixture policy; any manuscript path
there is a blocker.

After the build, inspect:

```bash
grep -aEn '^! |Emergency stop|Fatal error|Undefined control sequence|Runaway argument|File ended while scanning|No pages of output|LaTeX Error|Package .* Error' ".build_logs/make-pdf-$ts.log" out/main.log
grep -aEn 'Citation .*undefined|Reference .*undefined|There were undefined references|There were undefined citations|multiply-defined|Label\(s\) may have changed|Rerun to get cross-references right' out/main.log
grep -aEn 'Overfull \\[hv]box|Underfull \\[hv]box' out/main.log
grep -aEn 'nomencl\.ist|lethead_prefix|lethead_suffix|lethead_flag|Input style error' out/main.ilg
wc -c out/main.nlo out/main.nls
ls -l out/main.pdf out/main.log out/main.aux out/main.toc
```

Expected fatal/cite/reference result: no matches in the first two greps.
Known nomenclature support-surface noise may persist if unchanged from Agent
327; it is not a theorem blocker.  Persistent layout warnings on theorem
statements, obstruction vectors, or coefficient identities should be treated
as layout repair targets after the build.
