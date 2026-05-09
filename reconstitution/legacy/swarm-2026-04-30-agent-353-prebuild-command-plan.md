# Agent 353 pre-build command plan

Date: 2026-04-30.

Scope: report-only final pre-build command plan.  No manuscript TeX was
edited.  This report reads Agent 342 and Agent 348 as controlling evidence.

## Verdict

Run the root manuscript build with `make pdf` after the active agents settle.
Capture the full make transcript because `out/main.log` records only the
final `pdflatex` pass.  Do not run `make release` for the build gate unless
the integration owner explicitly wants iCloud copying and release packaging.

Preserve raw primary-source fixture whitespace.  Agent 348 verified that the
staged whitespace/EOF findings in the four imported arXiv TeX fixtures match
recorded source-stream hashes.  They are not root manuscript build blockers.
Normalizing them would be a deliberate fixture-regeneration patch requiring
checksum-ledger updates, not a pre-build cleanup.

## Commands

Run from the repository root after current agents stop writing:

```bash
ts=$(date +%Y%m%d-%H%M%S)
mkdir -p .build_logs out
git status --short > ".build_logs/prebuild-status-$ts.txt"
```

Strict whitespace gate for the root build closure and local style file:

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
```

Diagnostic global staged check, non-blocking if it reports only the known raw
fixture whitespace from Agent 342/348:

```bash
git diff --cached --check -- > ".build_logs/prebuild-global-cached-diff-check-$ts.log" 2>&1
```

Root build:

```bash
make pdf > ".build_logs/make-pdf-$ts.log" 2>&1
```

Post-build freshness check:

```bash
find "${root_build_paths[@]}" -newer out/main.log -print > ".build_logs/postbuild-sources-newer-than-log-$ts.txt"
```

That freshness file should be empty.  If not, another agent edited a build
input during or after the build; rerun the build after the new edits settle.

## Diagnostics to inspect

Inspect the command logs in this order:

1. `.build_logs/prebuild-root-diff-check-$ts.log`
2. `.build_logs/prebuild-root-cached-diff-check-$ts.log`
3. `.build_logs/prebuild-global-cached-diff-check-$ts.log`
4. `.build_logs/make-pdf-$ts.log`
5. `out/main.log`
6. `out/main.ilg`
7. `.build_logs/postbuild-sources-newer-than-log-$ts.txt`

The two root diff-check logs should be empty.  The global cached diff-check
log may contain only the raw fixture whitespace/EOF findings for:

- `references/primary-sources/gv-hep-th-9809187.tex`
- `references/primary-sources/gv-hep-th-9812127.tex`
- `references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex`
- `references/primary-sources/osv-hep-th-0405146.tex`

Any manuscript path in the global diff-check log is a real pre-build blocker.

Run these scans after `make pdf`:

```bash
grep -aEn '^! |Emergency stop|Fatal error|Undefined control sequence|Runaway argument|File ended while scanning|No pages of output|LaTeX Error|Package .* Error' ".build_logs/make-pdf-$ts.log" out/main.log
grep -aEn 'Citation .*undefined|Reference .*undefined|There were undefined references|There were undefined citations|multiply-defined|Label\(s\) may have changed|Rerun to get cross-references right' out/main.log
grep -aEn 'Overfull \\[hv]box|Underfull \\[hv]box' out/main.log
grep -aEn 'nomencl\.ist|lethead_prefix|lethead_suffix|lethead_flag|Input style error' out/main.ilg
wc -c out/main.nlo out/main.nls
ls -l out/main.pdf out/main.log out/main.aux out/main.toc
```

Expected fatal/reference/bibliography result: no matches in the first two
greps.  Expected nomenclature result, if unchanged from Agent 327, is the
known `nomencl.ist` support-surface noise with empty `out/main.nlo` and
`out/main.nls`; it is not a manuscript theorem blocker.

For layout, compare new `out/main.log` against Agent 327's stale warning
surface.  The old semantically meaningful targets were:

- `claim-strength-ledger.tex:236-248`
- `local-dictionary.tex:699-711`
- `tate-T1-weighted-completion.tex:1758-1772`
- `tate-T1-weighted-completion.tex:2065-2080`
- `open-obligations.tex:1221-1236`
- `appendix-radial-parts-moyal.tex:629-638`

If these warnings persist after the fresh build, treat them as layout repair
targets, not as proof failures.  If new overfull boxes appear on theorem
statements, displayed obstruction vectors, or coefficient identities, inspect
the source before accepting the build.

## Source fixture whitespace decision

Preserve it.  Exempt the four raw primary-source TeX fixtures from the
ordinary whitespace gate unless the integration owner starts a separate
normalization patch.  A normalization patch must update checksum ledgers and
state that the mirrors are normalized local copies rather than byte-for-byte
source streams.

## Checks run by Agent 353

- Read `CLAUDE.md`, ecosystem voice and self-reflection excerpts, and the
  Vol II rectification skill.
- Read
  `reconstitution/swarm-2026-04-30-agent-342-final-build-readiness-audit.md`.
- Read
  `reconstitution/swarm-2026-04-30-agent-348-primary-fixture-whitespace-triage.md`.
- Inspected `Makefile` build targets and the current stale build-log audit
  reports.
