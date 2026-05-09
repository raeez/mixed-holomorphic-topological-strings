# Agent 203: radial/Weyl uniform homotopy mechanism

Date: 2026-04-30.

Owned paths:

- `reconstitution/radial-weyl-uniform-homotopy-mechanism-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-203-radial-weyl-uniform-homotopy-mechanism.md`

No script or TeX file was edited.

## Claim attacked

Finite vanishing certificates from Agent 191 might already contain the
uniform all-bidegree quantum shear primitive.  The exact obstruction is the
free normal-diagram class
\[
  \mathfrak o_{a,b}=[R^{\mathrm{free}}_{a,b}]
  \in\operatorname{coker}\mathcal C_{a,b},
\]
defined in `appendix-radial-parts-moyal.tex:820-866`; vanishing plus
functorial lifts is the manuscript boundary in
`appendix-radial-parts-moyal.tex:868-895`.

## Result

The edge mechanism is visible as a theorem candidate.  The formulas in Agent 191,
`reconstitution/swarm-2026-04-30-agent-191-radial-all-bidegree-obstruction-0957.md:70-84`,
should be attacked as an all-edge theorem: the coefficient
\((b-1-2r)\), respectively \(3(a-1-2r)/(a+1)\), is a PBW telescoping
weight along the one-moving-letter string.  The proof should pair interior
normal-ordering matchings and leave only the Moyal boundary terms plus the
\(\hbar N\) isolated-loop cancellation.

The balanced/interior mechanism is not yet a theorem.  The corrections are
certificates in a positive-contraction two-colour necklace complex.  The
missing invariant is associated-graded acyclicity of that complex on the
Moyal shear residual subspace, or equivalently a natural left-cokernel
theorem for \(\mathcal C_{a,b}|_{\ker\partial}\).  The detailed theorem
candidates and proof strategy are recorded in
`reconstitution/radial-weyl-uniform-homotopy-mechanism-2026-04-30.md`.

## Verified evidence

Current code reproduces Agent 191's certificates.

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
  --family-only --edge-family-max 12 --kernel-correction --progress \
  --max-terms 1
# PASS through (2,12) and (12,2); every case has residual_terms=0,
# correction_terms=0, corrected_residual_terms=0.

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --family-only --balanced-family-max 6 --kernel-correction --progress \
  --max-terms 4
# PASS through (6,6).  The diagonal data are:
# (4,4): residual_terms=4, correction_terms=4
# (5,5): residual_terms=22, correction_terms=16
# (6,6): residual_terms=96, correction_terms=54

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,7 --case 7,3 --case 4,5 --case 5,4 \
  --case 4,6 --case 6,4 --kernel-correction --progress --max-terms 1
# PASS

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,8 --case 8,3 --case 4,7 --case 7,4 \
  --case 5,6 --case 6,5 --kernel-correction --progress --max-terms 1
# PASS

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,9 --case 9,3 --case 4,8 --case 8,4 \
  --case 5,7 --case 7,5 --kernel-correction --progress --max-terms 1
# PASS
```

The control failure and heal remain:

```text
python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --classical-only --max-terms 12
# expected FAIL: four-term free residual

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --kernel-correction --max-terms 8
# PASS with the four-term K_{4,4} correction
```

## Valid attacks

```yaml
- id: A203-01
  severity: 2
  status: healed-to-theorem-candidate
  lens: edge-family telescoping
  target: (2,b) and (a,2)
  claim: finite edge checks are only a table
  finding: the one-moving-letter PBW expansion has a visible discrete
    divergence; this should be stated as an all-edge theorem candidate
  residual: write the matching-pair involution and endpoint calculation

- id: A203-02
  severity: 2
  status: valid-not-closed
  lens: balanced/interior homotopy
  target: all bidegrees
  claim: finite certificates through total degree 12 imply all-bidegree
    radial/Weyl closure
  broken_step: the sparse solver gives pivot-gauge lifts, not a natural
    splitting of C_{a,b}
  residual: prove associated-graded acyclicity of the positive-contraction
    two-colour necklace complex, or exhibit a left-cokernel functional

- id: A203-03
  severity: 3
  status: valid
  lens: canonicalization
  target: simple-cycle normal forms
  claim: cycle canonicalization is the structural homotopy
  broken_step: `canonical_simple_directed_cycle` at
    scripts/quantum_shear_trace_diagram_normal_form.py:189-238 is an exact
    speedup for colour necklaces; it does not kill cokernels
```

## Residual open cases

- Prove the all-edge PBW telescoping theorem.
- Construct the associated-graded necklace homotopy \(H\), or a natural
  left-cokernel vanishing theorem, for interior bidegrees.
- Decide \((7,7)\) and the non-edge total-degree \(13\) strip after the
  invariant is formulated; further tables alone will not close the theorem.
- Preserve the manuscript's current conditional status for the all-\(N\)
  radial/Weyl trace input until the homotopy is proved.

Files changed: the two owned reports above.  `make pdf` was not run because
no manuscript file changed.
