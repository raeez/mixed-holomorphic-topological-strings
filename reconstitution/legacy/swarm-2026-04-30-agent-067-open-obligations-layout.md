# Agent 067 open-obligations layout repair

## Warnings attacked

- Fresh `pdflatex` showed no overfull warning inside the current
  `open-obligations.tex`; the older `out/main.log` context was from a longer
  line-number regime and no longer locates an owned-file warning.
- Attacked the owned high-risk display classes anyway: coordinate obstruction
  terms, the \(\mathcal D_\hbar\) quotient, the mixed brane-defect scalar
  bracket, the Weyl normalization display, the Weyl/Moyal exponential, and the
  global target datum / admissibility vector.
- Post-patch temporary build still reports overfull boxes only outside this
  lane: `local-dictionary.tex`, `tate-T3-quillen-equivalence.tex`, and
  `appendix-radial-parts-moyal.tex`.

## Exact edits

- `open-obligations.tex` lines 60--72: wrapped
  \(\mathfrak o^{\mathrm{br}}_{M,N}\) and
  \(\mathfrak o^{\mathrm{coad}}_{M,N}\) in `aligned`; inserted an actual row
  break before the coadjoint subtraction.
- `open-obligations.tex` lines 177--185: wrapped the
  \(\mathcal D_\hbar\) presentation in `aligned`; placed the quotient slash on
  its own aligned row.
- `open-obligations.tex` lines 257--272: wrapped the open scalar bracket and
  Weyl normalization in `aligned`; broke before the central term and before the
  modulus clause.
- `open-obligations.tex` lines 336--343: wrapped the Weyl/Moyal convention in
  `aligned`; replaced the unbreakable exponential row by a two-row display.
- `open-obligations.tex` lines 360--381: wrapped
  \(\mathfrak C_{\mathrm{tar}}\) and
  \(\operatorname{Ob}_{\mathfrak C_{\mathrm{tar}}}\) in `aligned`; broke the
  long tuples across explicit rows.

## Content-preservation checks

- No obligation prose, obstruction name, target datum entry, admissibility
  vector entry, or theorem-unlocking criterion was changed.
- `git diff --word-diff=plain -- open-obligations.tex` shows only `aligned`
  wrappers, alignment markers, display row breaks, and delimiter sizing in the
  Moyal exponential. The mathematical tokens remain the same.
- Agent 051 layout triage report was searched for and not found; the only
  matching current layout report was Agent 062 cross-volume layout.

## Commands run

- `sed -n '1,220p' CLAUDE.md`
- `rg --files reconstitution | rg "agent-051|051|layout"`
- `nl -ba open-obligations.tex`
- `rg -n "Overfull|open-obligations|obligation" out/main.log`
- `pdflatex -output-directory=out -interaction=nonstopmode main.tex`
- `pdflatex -draftmode -output-directory=/tmp/topological-strings-agent067.71NxTF -interaction=nonstopmode main.tex`
- `rg -n "Overfull|Undefined control sequence|Fatal error|Emergency stop|No pages of output" /tmp/topological-strings-agent067.71NxTF/main.log`
- `git diff --word-diff=plain -- open-obligations.tex`
- `git diff --check` reported an unowned pre-existing whitespace error at
  `frontier_mnop_framing_volume.tex:569`; not touched.
- `git diff --check -- open-obligations.tex reconstitution/swarm-2026-04-30-agent-067-open-obligations-layout.md`
  passed.
- `git restore --worktree out/main.pdf`
- `git add -- open-obligations.tex reconstitution/swarm-2026-04-30-agent-067-open-obligations-layout.md`
- `git diff --cached --check`

## Files changed

- `open-obligations.tex`
- `reconstitution/swarm-2026-04-30-agent-067-open-obligations-layout.md`

Both owned paths are staged. Other staged and unstaged swarm work was present
before this lane's staging and was left untouched.

## Residual layout risk

No residual overfull warning is attached to `open-obligations.tex` in the
post-patch temporary build. Residual project warnings outside the lane remain
unchanged, including the 85.42854pt display warning in
`appendix-radial-parts-moyal.tex`.
