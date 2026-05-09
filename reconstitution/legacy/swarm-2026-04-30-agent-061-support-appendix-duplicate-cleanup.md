# Agent 061 support-appendix duplicate-line cleanup

## Defects checked

- `tate-T1-weighted-completion.tex`, proof of
  `thm:wt-cotangent-lift`: checked the reported fragment
  `descends to the weighted symmetric algebra by \ref{w:W2}, subject to the`.
  It occurs once in the current working tree, once in the staged index,
  and once in `HEAD`.
- `appendix-factorization-current-conventions.tex`, proof of
  `cor:app-factorization-principal-part-current-brackets`: checked the
  reported line `z_1^p z_2^q\cdot\rho_{i,j}`.  It occurs once in the
  current working tree, once in the staged index, and once in `HEAD`.
- A consecutive-line scan over both owned TeX files found no nonblank
  duplicated adjacent lines.

## Exact edits

- No TeX edit was made.  The suspected duplicate text was not present in
  the current file contents, the staged index, or `HEAD`.
- Added this report file.

## Theorem-content preservation rationale

The checked passages each contain a single necessary proof line:

- In `thm:wt-cotangent-lift`, the line records that the target Schouten
  bracket descends by `\ref{w:W2}` under the same
  bracket-admissibility reading.
- In `cor:app-factorization-principal-part-current-brackets`, the line
  starts the Matlis coadjoint-action formula used to derive the displayed
  current bracket.

Removing either surviving line would delete proof content.  Since no
adjacent duplicate remained, preserving theorem content required no TeX
change.

## Commands run

- `pwd`
- `git status --short`
- `sed -n '1,220p' CLAUDE.md`
- `sed -n '1,220p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `rg -n "..." /Users/raeez/ecosystem/INVARIANTS.md /Users/raeez/ecosystem/AGENTS-HARNESS.md`
- `git diff -- tate-T1-weighted-completion.tex appendix-factorization-current-conventions.tex`
- `git diff --cached -- tate-T1-weighted-completion.tex appendix-factorization-current-conventions.tex`
- `rg -n -F "descends to the weighted symmetric algebra" tate-T1-weighted-completion.tex`
- `rg -n -F "z_1^p z_2^q\\cdot\\rho_{i,j}" appendix-factorization-current-conventions.tex`
- `rg -n -F "thm:wt-cotangent-lift" tate-T1-weighted-completion.tex`
- `rg -n -F "cor:app-factorization-principal-part-current-brackets" appendix-factorization-current-conventions.tex`
- `nl -ba tate-T1-weighted-completion.tex | sed -n '430,510p'`
- `nl -ba appendix-factorization-current-conventions.tex | sed -n '276,318p'`
- `git show :tate-T1-weighted-completion.tex | nl -ba | sed -n '430,510p'`
- `git show :appendix-factorization-current-conventions.tex | nl -ba | sed -n '276,318p'`
- `git show HEAD:tate-T1-weighted-completion.tex | rg -n -F "descends to the weighted symmetric algebra"`
- `git show HEAD:appendix-factorization-current-conventions.tex | rg -n -F "z_1^p z_2^q\\cdot\\rho_{i,j}"`
- `awk 'prev==$0 && $0 !~ /^[[:space:]]*$/ {print FILENAME ":" NR-1 ":" prev; print FILENAME ":" NR ":" $0} {prev=$0}' tate-T1-weighted-completion.tex appendix-factorization-current-conventions.tex`
- `git diff --cached --check -- tate-T1-weighted-completion.tex appendix-factorization-current-conventions.tex`
- `sed -n '1,160p' Makefile`
- `command -v chktex`
- `command -v pdflatex`
- `git diff --check`
- `chktex -q tate-T1-weighted-completion.tex appendix-factorization-current-conventions.tex`
- `sed -n '1,220p' reconstitution/swarm-2026-04-30-agent-061-support-appendix-duplicate-cleanup.md`
- `git status --short -- tate-T1-weighted-completion.tex appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-061-support-appendix-duplicate-cleanup.md`
- `git status --short -- appendix-factorization-current-conventions.tex`
- `git status --short -- tate-T1-weighted-completion.tex`
- `git diff --cached --name-status -- tate-T1-weighted-completion.tex appendix-factorization-current-conventions.tex`
- `git diff --name-status -- tate-T1-weighted-completion.tex appendix-factorization-current-conventions.tex`
- `git status --short`
- `git diff --check`
- `git add -- reconstitution/swarm-2026-04-30-agent-061-support-appendix-duplicate-cleanup.md`
- `git diff --cached --check -- reconstitution/swarm-2026-04-30-agent-061-support-appendix-duplicate-cleanup.md tate-T1-weighted-completion.tex appendix-factorization-current-conventions.tex`
- `git status --short -- reconstitution/swarm-2026-04-30-agent-061-support-appendix-duplicate-cleanup.md tate-T1-weighted-completion.tex appendix-factorization-current-conventions.tex`

## Check results

- `git diff --check`: passed.
- `git diff --cached --check -- tate-T1-weighted-completion.tex appendix-factorization-current-conventions.tex`: passed.
- Final `git diff --check` after report creation: passed.
- Final staged-path `git diff --cached --check` after staging the
  report: passed.
- `chktex -q tate-T1-weighted-completion.tex appendix-factorization-current-conventions.tex`: completed with pre-existing style warnings and exit code 2; no warning indicated the reported duplicate-line defects.

## Files changed

- `reconstitution/swarm-2026-04-30-agent-061-support-appendix-duplicate-cleanup.md`

## Residual risk

The report verifies the current working tree, staged index, and `HEAD`
for the two exact reported duplicate sites.  It does not audit unrelated
duplicate prose outside the two owned TeX files.  The targeted TeX check
was lint-only; no full PDF build was run because no TeX content changed
and the worktree contains substantial unrelated concurrent changes.
