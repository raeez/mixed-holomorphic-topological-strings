# Agent 217: radial theorem-lane supremum rework

Date: 2026-04-30.

Owned write paths:

- `theorem-lanes.tex`
- `reconstitution/swarm-2026-04-30-agent-217-radial-theorem-lane-supremum-rework.md`

## Claims attacked

1. `theorem-lanes.tex:370-371`: the local taxonomy still described the
   Weyl/Moyal trace realization as merely conditional.  Repaired to the
   radial/Weyl finite-certificate trace gate.
2. `theorem-lanes.tex:2355-2499`: the degree-zero Moyal/Weyl lane treated
   the stable trace comparison as a generic radial-parts input.  Reworked
   it into the strongest available theorem surface: proved formal
   Moyal/Capelli/open-line data, proved edge PBW telescoping, proved
   \(K_{4,4}\), finite non-edge certificates, and the exact
   \(\operatorname{coker}\mathcal C_{a,b}\) obstruction target.
3. `theorem-lanes.tex:2524-2580`: the componentwise quantum coefficient
   surface carried a conditional degree-zero Moyal trace factor.  Repaired
   to reference the same radial/Weyl finite-certificate gate.
4. `theorem-lanes.tex:3251-3338`: the graph/QME branch catalogue named
   only the moment-ideal defect \(E_{a,b,N}\).  Reworked it to include the
   free normal-diagram obstruction class, edge theorem, \(K_{4,4}\),
   finite certificates, and the exact left-cokernel theorem alternative.

## Repairs made

- Inscribed the Agent 209 edge result as theorem-lane data:
  \[
    \mathfrak o_{2,b}=0,\qquad \mathfrak o_{a,2}=0
  \]
  by Proposition `prop:app-edge-pbw-telescoping`.
- Promoted Agent 203's interior analysis from table evidence to the exact
  construction target:
  \[
    \mathfrak o_{a,b}
    =[R^{\mathrm{free}}_{a,b}]
    \in \operatorname{coker}(\mathcal C_{a,b}\colon
    \ker\partial\to\mathsf{Diag}_{a,b}),
  \]
  together with functorial lifts \(K_{a,b}\).
- Added the obstruction-theorem alternative: a stable left functional
  \(\lambda\mathcal C_{a,b}|_{\ker\partial}=0\) with
  \(\lambda(R^{\mathrm{free}}_{a,b})\ne0\) is the exact obstruction to the
  original all-bidegree radial/Weyl statement.
- Removed lazy conditional wording from the relevant Moyal/Zhu theorem-lane
  prose; remaining `conditional` / `external` scan hits are label names
  already present in referenced theorem labels.

## Commands and checks

```text
git diff --check -- theorem-lanes.tex
# PASS

rg -n "conditional|expected|external" theorem-lanes.tex
# Only label-name hits:
# stmt:app-radial-external-input
# prop:conditional-boundary-product-normalization

rg -n "prop:app-edge-pbw-telescoping|prop:app-free-trace-diagram-K44|prop:app-free-obstruction-certificates|stmt:app-free-kernel-homotopy-obstruction|def:app-free-kernel-correction-obstruction" appendix-radial-parts-moyal.tex theorem-lanes.tex
# PASS: every new theorem-lane reference has a source label in the appendix.

PYTHONDONTWRITEBYTECODE=1 python3 scripts/quantum_shear_trace_diagram_normal_form.py --family-only --edge-family-max 6 --progress --max-terms 1
# PASS: edge candidates through (2,6) and (6,2) have zero free trace-diagram residual.

PYTHONDONTWRITEBYTECODE=1 python3 scripts/quantum_shear_trace_diagram_normal_form.py --case 4,4 --kernel-correction --max-terms 8
# PASS: K_{4,4} correction kills the four-term free residual.
```

## Remaining construction targets

- Construct the associated-graded positive-contraction two-colour necklace
  homotopy \(H\) producing functorial \(K_{a,b}\) in every interior
  bidegree.
- Equivalently, prove the left-cokernel vanishing theorem for
  \(\mathcal C_{a,b}|_{\ker\partial}\) on the Moyal shear residual
  subspace.
- If the vanishing theorem fails, exhibit the first stable left-cokernel
  functional and record the resulting obstruction theorem.
- After the invariant is formulated, decide the \((7,7)\) and non-edge
  total-degree \(13\) finite windows as checks, not as substitutes for the
  homotopy.

Files changed: `theorem-lanes.tex` and this report.
