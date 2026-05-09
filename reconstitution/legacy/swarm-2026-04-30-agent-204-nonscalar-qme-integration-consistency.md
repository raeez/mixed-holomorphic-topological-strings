# Agent 204 - Non-scalar QME integration consistency

Status: report-only audit complete.  No TeX edits.

Canonical report:
`reconstitution/nonscalar-qme-integration-consistency-2026-04-30.md`.

## Findings

1. Agent 198's appendix block is sound as a finite-window criterion:
   `def:app-native-finite-window-realization-habitat`,
   `thm:app-constructive-nonscalar-costello-qme-realization`, and
   `prop:app-closed-rows-and-theta-three-source-face` prove the habitat,
   primitive criterion, closed \(\alpha_{\mathrm{sc}}\)/\(\alpha_{11}\) rows,
   and finite-row \(\theta_3\) obstruction.  They do not prove all-graph QME.
2. The new labels are cited only inside `appendix-unreduced-bv-qme.tex`.
   `main.tex`, `theorem-lanes.tex`, and `claim-strength-ledger.tex` should
   cite the new definition/theorem/proposition where they describe the
   non-scalar QME lane.
3. The primitive formula \(A^M c=-r^M\), its left-cokernel certificate
   \(\ell A^M=0,\ell(r^M)\ne0\), and the Roos compatibility class should be
   displayed in `main.tex`, `local-dictionary.tex`, and
   `open-obligations.tex`.
4. The \(\theta_3\) source face is written as \(\zeta_{M,\nu_3}\) in the
   appendix and source reports, but as \(\zeta_{\nu_3,M}\) in
   `abstract.tex`, `claim-strength-ledger.tex`, and `open-obligations.tex`.
   Standardize to \(\zeta_{M,\nu_3}\).
5. `abstract.tex` and `local-dictionary.tex` blur the companion-face branch:
   a companion-face table changes the row residual; it is not a degree-zero
   primitive.  The report gives replacement text.
6. No compact Calabi--Yau or CoHA false transfer was found.  The firewall
   language is intact.

## Commands run

```bash
rg --files
rg -n 'finite[- ]window|primitive|QME|theta_3|alpha|all-graph|compact Calabi|CoHA' abstract.tex theorem-lanes.tex main.tex claim-strength-ledger.tex local-dictionary.tex open-obligations.tex appendix-unreduced-bv-qme.tex
rg -n '\\zeta_{\\nu_3,M}|\\zeta_{M,\\nu_3}' abstract.tex claim-strength-ledger.tex open-obligations.tex local-dictionary.tex theorem-lanes.tex main.tex appendix-unreduced-bv-qme.tex reconstitution/*.md
git diff --check -- abstract.tex theorem-lanes.tex main.tex claim-strength-ledger.tex local-dictionary.tex open-obligations.tex appendix-unreduced-bv-qme.tex
chktex -q abstract.tex theorem-lanes.tex main.tex claim-strength-ledger.tex local-dictionary.tex open-obligations.tex appendix-unreduced-bv-qme.tex
pdflatex -draftmode -interaction=nonstopmode -halt-on-error -output-directory=/tmp/topological-strings-agent204-tex main.tex
PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite_window_graph_array.py > /tmp/agent204-finite-window-graph-array.json
```

Results: `git diff --check` passed; `chktex` produced style warnings only;
`pdflatex -draftmode` exited `0` with first-pass undefined-reference warnings;
the finite-window script reproduced the zero minimal branch and the obstructed
\(\theta_3\) one-row subcomplex.

## Files changed

- `reconstitution/nonscalar-qme-integration-consistency-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-204-nonscalar-qme-integration-consistency.md`
