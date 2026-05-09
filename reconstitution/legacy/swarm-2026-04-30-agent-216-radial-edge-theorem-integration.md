# Agent 216: radial edge theorem integration

Date: 2026-04-30.

Owned write paths:

- `appendix-radial-parts-moyal.tex`
- `reconstitution/swarm-2026-04-30-agent-216-radial-edge-theorem-integration.md`

## Integration

`appendix-radial-parts-moyal.tex` already had staged concurrent edits.
Those edits were preserved; this pass adds an unstaged delta on top.

The radial appendix now contains
Proposition `\ref{prop:app-edge-pbw-telescoping}`.  It proves the edge
free normal-diagram identities
\[
  \mathcal N_{\mathrm{free}}
    (E_{2,b,N}-C^{\mathrm{edge}}_{2,b})=0,
  \qquad
  \mathcal N_{\mathrm{free}}
    (E_{a,2,N}-C^{\mathrm{edge}}_{a,2})=0
\]
for all \(b\ge2\) and \(a\ge2\), with
\[
  C^{\mathrm{edge}}_{2,b}
  =
  \sum_{r=0}^{\lfloor(b-2)/2\rfloor}
    (b-1-2r)\operatorname{Tr}(Y^rXY^{b-1-r}M),
\]
and
\[
  C^{\mathrm{edge}}_{a,2}
  =
  \frac3{a+1}
  \sum_{r=0}^{\lfloor(a-2)/2\rfloor}
    (a-1-2r)\operatorname{Tr}(X^{a-1-r}YX^rM).
\]

The proof mechanism is the four-term PBW column identity
\[
  \mathcal N_{\mathrm{free}}\operatorname{Tr}(Y^rXY^{b-1-r}M)
  =
  \Theta_r^{(b)}-\Theta_{r+1}^{(b)}
  -\hbar\Phi_r^{(b)}+\hbar\Phi_{b-1-r}^{(b)}.
\]
The target expansion is the weighted telescoping sum of these columns.
The contraction-degree \(2\) residue is exactly the third Moyal term
\[
  \frac{(b+1)b(b-1)}{12}\hbar^2\operatorname{Tr}(Y^{b-2}),
\]
and cancels with the same sign in \(E_{2,b,N}\).  The \((a,2)\) family is
the same one-moving-letter PBW calculation, scaled by \(3/(a+1)\) from the
first and third Moyal coefficients.

## Boundaries

The finite certificate proposition now treats edge cases as consequences of
the edge theorem, not as finite evidence.  Balanced and interior bidegrees
remain governed by the left-cokernel obstruction
\(\operatorname{coker}\mathcal C_{a,b}\), equivalently the
associated-graded two-colour necklace homotopy problem.  No all-bidegree
radial closure is claimed.

## Commands

```text
python3 -m py_compile scripts/quantum_shear_trace_diagram_normal_form.py \
  scripts/quantum_shear_primitive_search.py \
  scripts/quantum_shear_universal_formula.py
# PASS

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --self-test --self-test-rank 2 --self-test-max-length 6 --max-terms 8
# PASS self-test rank=2 max_length=6 checked=127
# PASS: all requested candidates have zero free trace-diagram residual.

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --family-only --edge-family-max 20 --progress --max-terms 1
# PASS through (2,20) and (20,2); residual_terms=0 in every edge case.

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --family-only --edge-family-max 12 --kernel-correction --progress \
  --max-terms 1
# PASS through (2,12) and (12,2); residual_terms=0, correction_terms=0,
# corrected_residual_terms=0 in every edge case.

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,5 --case 5,3 --solve-free --max-terms 8
# PASS; zero free trace-diagram residual.

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,6 --case 6,3 --kernel-correction --max-terms 4
# PASS; obstruction classes vanish.

python3 scripts/check_moyal_coefficients.py
# ALL CHECKS PASS.

git diff --check
# PASS

git diff --check -- appendix-radial-parts-moyal.tex \
  reconstitution/swarm-2026-04-30-agent-216-radial-edge-theorem-integration.md
# PASS

git diff --cached --check -- appendix-radial-parts-moyal.tex
# PASS

git diff --cached --check
# FAIL on pre-existing staged files outside the owned paths:
# reconstitution/swarm-2026-04-30-agent-194-0957-theorem-lane-integration.md,
# references/primary-sources/gv-hep-th-9809187.tex,
# references/primary-sources/gv-hep-th-9812127.tex,
# references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex,
# references/primary-sources/hkq-compact-cy-hep-th-0612125.txt,
# references/primary-sources/osv-hep-th-0405146.tex.
```
