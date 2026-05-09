# Agent 218: main radial/quantum supremum rework

Date: 2026-04-30.

Owned paths:

- `main.tex`
- `reconstitution/swarm-2026-04-30-agent-218-main-radial-quantum-supremum-rework.md`

## Claim Attacked

The main text still treated the radial/Moyal surface as an `external
radial-parts input` or a `conditional all-order` theorem.  That was too weak
after the current certificates:

- Agent 209 proves the one-moving-letter edge PBW telescoping theorem.
- Agent 203 identifies the exact all-interior obstruction as
  \(\mathfrak o_{a,b}\in\operatorname{coker}\mathcal C_{a,b}\), equivalently
  a two-colour necklace homotopy or stable left-cokernel vanishing theorem.
- Agent 191 and the current script evidence certify the balanced diagonal
  through \((6,6)\) and the non-edge total-degree strip through \(12\).

## Repairs Inscribed

- `main.tex:1050`, `main.tex:2058`, `main.tex:2284`: replaced the finite
  edge-window wording by the proved all-edge theorem
  `prop:app-edge-pbw-telescoping`, and named the remaining all-interior
  construction problem.
- `main.tex:6933`: retitled the finite-\(N\) reduced Moyal theorem as a
  radial-input plus obstruction-gate theorem.  It keeps the radial image
  package only where needed and records the exact substitute:
  \(E_{a,b,N}\in\mathcal W_N\widehat\mu(\mathfrak{sl}_N)\), equivalently
  \(\mathfrak o_{a,b}=0\) with functorial \(K_{a,b}\in\ker\partial\).
- `main.tex:7105`: changed the degree-zero corollary from a datum-only
  comparison into a comparison plus radial-normalization obstruction.
- `main.tex:7743`: replaced the old `Conditional all-order` theorem surface
  by `Degree-zero Moyal target and radial-normalization obstruction`.
  The formal Moyal coefficients and Capelli trace target are unconditional;
  the ordinary-trace Lie comparison is conditional only on the radial image
  package or the equivalent solved shear-primitive package.
- `main.tex:7845`: updated the componentwise quantum coefficient theorem so
  its \(T_{\mathrm{Ham},\hbar}\) factor is explicitly radial-gated, with
  all edge strips proved and all-interior closure left as the named
  obstruction.

## Verification

Commands run with `PYTHONDONTWRITEBYTECODE=1`:

```text
python3 scripts/check_moyal_coefficients.py
# PASS: 14641 Moyal pairs through order 11; Capelli round trips;
# N=2,3 radial restrictions; open-line r=1,3 graph weights.

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --self-test --self-test-rank 2 --self-test-max-length 6 --max-terms 8
# PASS self-test rank=2 max_length=6 checked=127.

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --family-only --edge-family-max 12 --kernel-correction --progress --max-terms 1
# PASS through (2,12) and (12,2); all corrected residuals zero.

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --classical-only --max-terms 12
# Expected FAIL: four-term free residual.

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --kernel-correction --max-terms 8
# PASS with the four-term K_{4,4} correction.

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --family-only --balanced-family-max 6 --kernel-correction --progress --max-terms 4
# PASS through (6,6).

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,7 --case 7,3 --case 4,5 --case 5,4 \
  --case 4,6 --case 6,4 --case 3,8 --case 8,3 \
  --case 4,7 --case 7,4 --case 5,6 --case 6,5 \
  --case 3,9 --case 9,3 --case 4,8 --case 8,4 \
  --case 5,7 --case 7,5 --kernel-correction --progress --max-terms 1
# PASS: all requested non-edge total-degree <= 12 strip checks vanish.
```

No TeX build was run because `make pdf` would write build artifacts outside
the two paths assigned for this pass.

## Residual

The full all-interior radial theorem is not claimed.  The exact remaining
construction is:

\[
  \forall a,b\ge3,\qquad
  \mathfrak o_{a,b}=[R^{\mathrm{free}}_{a,b}]
  \in\operatorname{coker}\mathcal C_{a,b}
  \quad\text{vanishes functorially,}
\]

with compatible \(K_{a,b}\in\ker\partial\).  Equivalently, prove the
associated-graded two-colour necklace homotopy or prove that every stable
left-cokernel functional \(\lambda\) with
\(\lambda\mathcal C_{a,b}|_{\ker\partial}=0\) satisfies
\(\lambda(R^{\mathrm{free}}_{a,b})=0\).  A nonzero such \(\lambda\) is the
obstruction theorem blocking the ordinary all-bidegree Weyl-trace comparison.
