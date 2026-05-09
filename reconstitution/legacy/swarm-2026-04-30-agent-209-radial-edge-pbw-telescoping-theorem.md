# Agent 209: radial edge PBW telescoping theorem

Date: 2026-04-30.

Owned paths:

- `reconstitution/radial-edge-pbw-telescoping-theorem-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-209-radial-edge-pbw-telescoping-theorem.md`

No TeX or script file was edited.

## Claim attacked

Agent 191 found edge formulas
\[
  C_{2,b}^{\mathrm{edge}}
  =
  \sum_{r=0}^{\lfloor(b-2)/2\rfloor}
  (b-1-2r)\operatorname{Tr}(Y^rXY^{b-1-r}M)
\]
and
\[
  C_{a,2}^{\mathrm{edge}}
  =
  \frac3{a+1}
  \sum_{r=0}^{\lfloor(a-2)/2\rfloor}
  (a-1-2r)\operatorname{Tr}(X^{a-1-r}YX^rM),
\]
checked through \(12\).  Agent 203 identified them as a one-moving-letter
PBW telescoping candidate.  The attack was whether this is only finite
evidence or a manuscript-ready all-edge mechanism.

## Result

Status: theorem candidate with a closed proof sketch.  In the free indexed
normal-diagram algebra,
\[
  \mathcal N_{\mathrm{free}}(E_{2,b,N}-C_{2,b}^{\mathrm{edge}})=0,
  \qquad
  \mathcal N_{\mathrm{free}}(E_{a,2,N}-C_{a,2}^{\mathrm{edge}})=0.
\]
The proof is the four-term PBW column identity
\[
  \mathcal N_{\mathrm{free}}\operatorname{Tr}(Y^rXY^{b-1-r}M)
  =
  \Theta_r-\Theta_{r+1}-\hbar\Phi_r+\hbar\Phi_{b-1-r},
\]
together with the target expansion
\[
  \mathcal N_{\mathrm{free}}(E_{2,b,N})
  =
  \sum_{r=0}^{\lfloor(b-2)/2\rfloor}
  (b-1-2r)
  (\Theta_r-\Theta_{r+1}-\hbar\Phi_r+\hbar\Phi_{b-1-r}).
\]
The \((a,2)\) family is the transposed calculation scaled by
\(3/(a+1)\), exactly the ratio of the first and third Moyal coefficients.

Detailed proof sketch is in
`reconstitution/radial-edge-pbw-telescoping-theorem-2026-04-30.md`.

## Attacks

- Finite-table attack: healed for edge families.  The edge coefficients
  are the linear discrete-divergence weights, not pivot-gauge artifacts.
- Boundary attack: healed.  The \(\hbar N\) scalar term in \(M\) cancels
  the adjacent-crossing endpoint family and gives the isolated-loop
  normalization.
- Third-order attack: healed as a target-count lemma.  The remaining
  double-contraction count is exactly the third Moyal term, hence cancels
  in \(E_{2,b,N}\) and in the scaled transposed \((a,2)\) family.
- Interior attack: still valid.  Balanced and non-edge bidegrees need the
  associated-graded two-colour necklace homotopy, or an equivalent
  left-cokernel vanishing theorem for
  \(\mathcal C_{a,b}|_{\ker\partial}\).  The edge proof does not supply it.

## Residuals

For TeX inscription, write the elementary matching-count lemma in the
manuscript notation: contraction degree \(0\), contraction degree \(1\),
and the degree \(2\) cancellation against the third Moyal coefficient.
No mathematical obstruction remains in the edge proof sketch.  No claim is
made for balanced/interior bidegrees.

## Commands run

```text
python3 -m py_compile scripts/quantum_shear_trace_diagram_normal_form.py \
  scripts/quantum_shear_primitive_search.py \
  scripts/quantum_shear_universal_formula.py
# PASS

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --self-test --self-test-rank 2 --self-test-max-length 6 --max-terms 8
# PASS self-test rank=2 max_length=6 checked=127

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --family-only --edge-family-max 12 --kernel-correction --progress \
  --max-terms 1
# PASS through (2,12) and (12,2); residual_terms=0,
# correction_terms=0, corrected_residual_terms=0 in every edge case.

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --family-only --edge-family-max 20 --progress --max-terms 1
# PASS through (2,20) and (20,2) in direct candidate mode.

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 2,6 --case 6,2 --max-terms 40
# PASS.
```

Exploratory read-only Python imports printed the \((2,5)\), \((2,6)\), and
\((6,2)\) column normal forms.  They wrote no files.

Files changed: the two owned markdown reports above.
