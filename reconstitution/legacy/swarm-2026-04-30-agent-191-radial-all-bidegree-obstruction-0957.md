# Agent 191: radial all-bidegree obstruction attack-heal

Date: 2026-04-30.

Owned paths:

- `scripts/quantum_shear_trace_diagram_normal_form.py`
- `reconstitution/swarm-2026-04-30-agent-191-radial-all-bidegree-obstruction-0957.md`

Read context: `CLAUDE.md`, `AGENTS.md`, the attack-heal protocol, the
09:57 critique-refresh plan, `appendix-radial-parts-moyal.tex`,
`scripts/quantum_shear_trace_diagram_normal_form.py`, and reports 140,
152, 172, and 183.  `appendix-radial-parts-moyal.tex` was read but not
edited.  No compact-CY, CoHA, quintic, OSV/GV, Abel-Jacobi, Igusa, or
BKM claim was used.

## Claim attacked

The all-bidegree quantum shear primitive would require a functorial
splitting of
\[
  \mathcal C_{a,b}\colon\ker\partial\longrightarrow
  \mathsf{Diag}_{a,b}
\]
which sends the free normal-form residual
\[
  R^{\mathrm{free}}_{a,b}
  =
  \mathcal N_{\mathrm{free}}(E_{a,b,N})
  -
  \mathcal N_{\mathrm{free}}
    \left(\sum_W c^{\mathrm{cl}}_W\operatorname{Tr}(WM)\right)
\]
to a kernel correction \(K_{a,b}\in\ker\partial\).  Equivalently, the
obstruction class
\[
  \mathfrak o_{a,b}=[R^{\mathrm{free}}_{a,b}]
  \in\operatorname{coker}\mathcal C_{a,b}
\]
must vanish in every bidegree, with compatible choices of lifts.  This
report extends finite evidence.  It does not prove the all-bidegree
theorem.

## Script repair

The trace-diagram script had a factorial canonicalization wall on
uncontracted simple-cycle components.  I added a canonical simple-cycle
path before the factorial fallback.  For one-in/one-out directed cycle
components it enumerates roots and the two cyclic label directions,
using the directed colour necklace rather than an \(n!\) vertex
permutation.  The old factorial path remains for all non-cycle
components.

I also added scan controls:

- `--balanced-family-max d` checks diagonal cases `(2,2)` through
  `(d,d)`.
- `--family-only` suppresses the default case list when running family
  scans.
- `--progress` prints a flushed `BEGIN a=... b=...` line before each
  exact solve.

These changes are computational infrastructure only.  They do not alter
the obstruction definition.

## Finite certificates

### Edge families

The existing edge candidates
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
  \frac{3}{a+1}
  \sum_{r=0}^{\lfloor(a-2)/2\rfloor}
  (a-1-2r)\operatorname{Tr}(X^{a-1-r}YX^rM)
\]
now check in kernel-correction mode through
\[
  (2,b),(b,2),\qquad 2\le b\le 12.
\]
Every checked edge case has
`residual_terms=0`, `correction_terms=0`, and
`corrected_residual_terms=0`.  This is strong finite evidence for a
telescoping edge primitive, but no all-edge proof is inscribed here.

### Balanced diagonal

The balanced diagonal through `(6,6)` has zero cokernel obstruction in
the computed free diagram basis:

```text
(2,2): classical_terms=1  residual_terms=0  correction_terms=0
(3,3): classical_terms=3  residual_terms=0  correction_terms=0
(4,4): classical_terms=9  residual_terms=4  correction_terms=4
(5,5): classical_terms=25 residual_terms=22 correction_terms=16
(6,6): classical_terms=79 residual_terms=96 correction_terms=54
```

For `(5,5)`, the cyclic equation has a 25-term lexicographic lift.
Its free residual has 22 terms, and the correction system solves with
rank 29 in 143 rows and 70 columns.  One correction is
\[
\begin{aligned}
  K_{5,5}={}&
  \frac{165}{14}\operatorname{Tr}(XXYXXYYY\,M)
  -\frac{239}{14}\operatorname{Tr}(XXYXYXYY\,M)\\
  &+\frac{505}{21}\operatorname{Tr}(XXYXYYXY\,M)
  -\frac{165}{14}\operatorname{Tr}(XXYYYXYX\,M)\\
  &+\frac{165}{14}\operatorname{Tr}(XXYYYYXX\,M)
  -\frac{165}{14}\operatorname{Tr}(XYXXXYYY\,M)\\
  &+\frac{239}{14}\operatorname{Tr}(XYXXYXYY\,M)
  -\frac{505}{21}\operatorname{Tr}(XYXXYYXY\,M)\\
  &+\frac{457}{21}\operatorname{Tr}(XYXYXYYX\,M)
  -\frac{457}{21}\operatorname{Tr}(XYXYYXXY\,M)\\
  &+\frac{239}{14}\operatorname{Tr}(XYXYYXYX\,M)
  -\frac{239}{14}\operatorname{Tr}(XYXYYYXX\,M)\\
  &-\frac{457}{21}\operatorname{Tr}(XYYXXYYX\,M)
  +\frac{457}{21}\operatorname{Tr}(XYYXYXXY\,M)\\
  &-\frac{505}{21}\operatorname{Tr}(XYYXYXYX\,M)
  +\frac{505}{21}\operatorname{Tr}(XYYXYYXX\,M).
\end{aligned}
\]
The script verifies
\[
  \partial K_{5,5}=0,\qquad
  \mathcal N_{\mathrm{free}}(K_{5,5})=R^{\mathrm{free}}_{5,5}.
\]

The next balanced stress test `(7,7)` was attempted in the same mode.
It did not return after the computation crossed from 252 columns in
`(6,6)` to 924 columns in `(7,7)`.  I stopped it without using it as
evidence.  The first unresolved balanced case in this run is therefore
`(7,7)`, not a nonzero obstruction.

### Non-edge finite strip

Kernel-correction mode gives zero obstruction for the following
additional non-edge cases:

```text
(3,7), (7,3), (4,5), (5,4), (4,6), (6,4)
(3,8), (8,3), (4,7), (7,4), (5,6), (6,5)
(3,9), (9,3), (4,8), (8,4), (5,7), (7,5)
(6,6)
```

Together with the previous reports, this covers all non-edge bidegrees
with total degree at most 12, and edge bidegrees through `(2,12)` and
`(12,2)`.  The first untested non-edge total degree is 13.

## Valid attacks

```yaml
- id: A191-01
  severity: 2
  status: valid-not-closed
  lens: all-bidegree homotopy
  target: stmt:app-free-kernel-homotopy-obstruction
  claim: finite vanishing certificates imply the all-bidegree radial
    quantum shear theorem
  broken_step: the finite solves produce pivot-gauge lifts but no
    functorial splitting of C_{a,b}
  evidence_type: proof_gap
  evidence_ref: finite scans above; no formula for a natural section of
    C_{a,b}
  blast_radius: the degree-zero Moyal comparison remains conditional on
    the radial-parts input outside certified windows
  minimal_heal: keep the obstruction class
    o_{a,b}=[R^{free}_{a,b}] in coker(C_{a,b}) as the exact theorem
    boundary
  residual: construct a functorial splitting, or exhibit a left-cokernel
    functional lambda with lambda C_{a,b}=0 and lambda(R^{free}_{a,b})
    nonzero
  deciding_evidence: closed formula for K_{a,b}; or a first nonzero
    cokernel certificate

- id: A191-02
  severity: 3
  status: healed-finite
  lens: balanced diagonal
  target: balanced case (5,5)
  claim: balanced bidegrees may fail immediately after K_{4,4}
  broken_step: direct free normal-form solve gives a 16-term kernel
    correction for (5,5)
  evidence_type: computation
  evidence_ref: python3 scripts/quantum_shear_trace_diagram_normal_form.py
    --case 5,5 --kernel-correction --progress --max-terms 30
  residual: no closed diagonal formula; (7,7) is computationally open

- id: A191-03
  severity: 3
  status: valid-residual
  lens: edge-family telescoping
  target: (2,b) and (b,2)
  claim: the displayed edge formulas prove the all-edge family
  broken_step: exact checks through b=12 show zero correction, but no
    telescoping proof in the trace-diagram complex was written
  evidence_type: bounded_computation
  evidence_ref: python3 scripts/quantum_shear_trace_diagram_normal_form.py
    --family-only --edge-family-max 12 --kernel-correction --progress
    --max-terms 1
  residual: prove the edge telescoping identity from the PBW
    normal-ordering theorem
```

## Commands

Regression and canonicalization:

```text
python3 -m py_compile scripts/quantum_shear_trace_diagram_normal_form.py \
  scripts/quantum_shear_primitive_search.py \
  scripts/quantum_shear_universal_formula.py
# PASS

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --self-test --self-test-rank 2 --self-test-max-length 6 --max-terms 8
# PASS self-test rank=2 max_length=6 checked=127
# PASS: all requested candidates have zero free trace-diagram residual.
```

Family and strip scans:

```text
python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --family-only --edge-family-max 12 --kernel-correction --progress \
  --max-terms 1
# PASS through (2,12) and (12,2); all residual_terms=0 and
# correction_terms=0.

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --family-only --balanced-family-max 6 --kernel-correction --progress \
  --max-terms 4
# PASS through (6,6).

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,9 --case 9,3 --case 4,8 --case 8,4 \
  --case 5,7 --case 7,5 --kernel-correction --progress --max-terms 1
# PASS for the total-degree-12 non-edge strip.
```

Stopped exploratory run:

```text
python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 7,7 --kernel-correction --progress --max-terms 1
# printed BEGIN a=7 b=7 and was stopped after no certificate returned.
```

`make pdf` was not run.  No manuscript file was edited.

## Remaining obligations

1. Prove the edge telescoping primitive for all \(b\), or find the first
   edge cokernel functional.  The finite evidence through \(b=12\) is
   not a theorem.
2. Construct a functorial splitting of \(\mathcal C_{a,b}\) on the
   residuals \(R^{\mathrm{free}}_{a,b}\), at least for the diagonal
   family, or produce the first nonzero left-cokernel certificate.
3. Improve the exact solver for `(7,7)` and the total-degree-13 strip.
   The current obstruction is computational size, not a mathematical
   nonvanishing result.
