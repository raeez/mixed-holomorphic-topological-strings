# Agent 172: radial obstruction family attack-heal

Date: 2026-04-30

Scope owned: `appendix-radial-parts-moyal.tex`,
`scripts/quantum_shear_trace_diagram_normal_form.py`, and this report.
Reports 140 and 152 were read.  No compact-CY, CoHA, quintic, OSV/GV,
Abel-Jacobi, Igusa, or BKM claim was used.

## Claim Attacked

After Agent 152, the all-bidegree problem was reduced to the free
cokernel class
\[
  \mathfrak o_{a,b}=[R^{\mathrm{free}}_{a,b}]
  \in\operatorname{coker}\mathcal C_{a,b}.
\]
I attacked the next finite total-degree strip beyond the recorded
certificates and computed the cases \((3,6)\) and \((6,3)\).

Result: in both cases the lexicographic cyclic lift already has zero
free normal-form residual.  Thus
\[
  \mathfrak o_{3,6}=\mathfrak o_{6,3}=0,\qquad
  K_{3,6}=K_{6,3}=0
\]
in this pivot gauge.  This is a finite certificate, not an all-bidegree
homotopy.

## Valid Attacks

```yaml
- id: A172-01
  target: all-bidegree closure after finite certificates
  severity: 2
  status: valid-not-closed
  failure_mode: vanishing in (3,6) and (6,3) gives no functorial
    splitting of C_{a,b}
  heal: inscribed only the finite total-degree-9 certificates and left
    stmt:app-free-kernel-homotopy-obstruction unchanged

- id: A172-02
  target: reproducibility of finite lift formulas
  severity: 3
  status: healed
  failure_mode: --kernel-correction reports only the kernel correction,
    so zero-correction cases do not print the cyclic lift coefficients
  heal: added --solve-classical, which solves only the cyclic boundary
    equation and prints the rational lift support

- id: A172-03
  target: edge-family and balanced extrapolation
  severity: 3
  status: valid-residual
  failure_mode: high-degree exploratory exact runs for edge sweeps and
    (5,5) were not completed inside a bounded certificate window
  heal: no edge-all or balanced-family theorem was stated
```

## Repaired Labels

Repaired:

- `prop:app-free-obstruction-certificates`
- `rmk:app-radial-finite-verification`

Script additions:

- built-in candidates for `(3,6)` and `(6,3)`
- `--solve-classical`

No label was added for an all-bidegree theorem.

## Exact Formulas

For \((3,6)\), the cyclic lift is
\[
\begin{aligned}
  C_{3,6}
  &=
    \frac{25}{4}\operatorname{Tr}(XXYYYYY\,M)
    +\frac{19}{4}\operatorname{Tr}(XYXYYYY\,M)\\
  &\quad
    -\frac{3}{4}\operatorname{Tr}(XYYXYYY\,M)
    -\frac{3}{4}\operatorname{Tr}(XYYYXYY\,M)\\
  &\quad
    -\frac{3}{4}\operatorname{Tr}(XYYYYXY\,M)
    +\frac{11}{2}\operatorname{Tr}(XYYYYYX\,M)\\
  &\quad
    +\frac{13}{4}\operatorname{Tr}(YXYXYYY\,M)
    +\frac{1}{4}\operatorname{Tr}(YXYYXYY\,M)
    +\frac{7}{4}\operatorname{Tr}(YXYYYXY\,M).
\end{aligned}
\]

For \((6,3)\), the cyclic lift is
\[
\begin{aligned}
  C_{6,3}
  &=
    \frac{25}{7}\operatorname{Tr}(XXXXXYY\,M)
    -\frac{3}{7}\operatorname{Tr}(XXXXYXY\,M)
    +\frac{22}{7}\operatorname{Tr}(XXXXYYX\,M)\\
  &\quad
    -\frac{3}{7}\operatorname{Tr}(XXXYXXY\,M)
    -\frac{6}{7}\operatorname{Tr}(XXXYXYX\,M)
    +\frac{19}{7}\operatorname{Tr}(XXXYYXX\,M)\\
  &\quad
    +\frac{16}{7}\operatorname{Tr}(XXYXXXY\,M)
    +\frac{1}{7}\operatorname{Tr}(XXYXXYX\,M)
    +\operatorname{Tr}(XXYXYXX\,M).
\end{aligned}
\]

The free normal-form computation gives
\[
  \mathcal N_{\mathrm{free}}(E_{3,6,N}-C_{3,6})=0,\qquad
  \mathcal N_{\mathrm{free}}(E_{6,3,N}-C_{6,3})=0.
\]
Therefore the kernel corrections are zero in these two cases.

## Script Outputs

Classical lift extraction:

```text
python3 scripts/quantum_shear_trace_diagram_normal_form.py --case 3,6 --case 6,3 --solve-classical --max-terms 20
PASS a=3 b=6 mode=classical-solve support=9 rank=9 rows=10 cols=21
PASS a=6 b=3 mode=classical-solve support=9 rank=9 rows=10 cols=21
PASS: all requested cyclic boundary equations have rational lifts.
```

Free obstruction checks:

```text
python3 scripts/quantum_shear_trace_diagram_normal_form.py --case 3,6 --kernel-correction --max-terms 12
PASS a=3 b=6 mode=kernel-correction classical=ok classical_terms=9 residual_terms=0 correction=ok correction_terms=0 rank=9 rows=44 cols=21 corrected_residual_terms=0
PASS: all requested kernel-correction obstruction classes vanish.

python3 scripts/quantum_shear_trace_diagram_normal_form.py --case 6,3 --kernel-correction --max-terms 12
PASS a=6 b=3 mode=kernel-correction classical=ok classical_terms=9 residual_terms=0 correction=ok correction_terms=0 rank=9 rows=44 cols=21 corrected_residual_terms=0
PASS: all requested kernel-correction obstruction classes vanish.
```

Regression:

```text
python3 -m py_compile scripts/quantum_shear_trace_diagram_normal_form.py scripts/quantum_shear_primitive_search.py scripts/quantum_shear_universal_formula.py
# pass

python3 scripts/quantum_shear_trace_diagram_normal_form.py --self-test --self-test-rank 2 --self-test-max-length 5 --max-terms 8
# PASS self-test rank=2 max_length=5 checked=63
# PASS: all requested candidates have zero free trace-diagram residual.

python3 scripts/quantum_shear_trace_diagram_normal_form.py --max-terms 8
# PASS: all requested candidates have zero free trace-diagram residual.
```

`make pdf` was not run.  The assigned write scope excludes build
artifacts such as `out/main.pdf`, and Agent 152 already recorded an
out-of-scope bibliography failure on an extra rerun.

## Files Changed / Staged

Changed and staged by this agent:

- `appendix-radial-parts-moyal.tex`
- `scripts/quantum_shear_trace_diagram_normal_form.py`
- `reconstitution/swarm-2026-04-30-agent-172-radial-obstruction-family.md`

Observed scoped status after staging:

```text
M  appendix-radial-parts-moyal.tex
A  reconstitution/swarm-2026-04-30-agent-172-radial-obstruction-family.md
A  scripts/quantum_shear_trace_diagram_normal_form.py
```

Pre-existing scoped/context status not touched by this agent:

```text
A  reconstitution/swarm-2026-04-30-agent-140-trace-diagram-normal-form.md
?? reconstitution/swarm-2026-04-30-agent-152-kernel-contracting-homotopy.md
```

## Remaining Theorem Obligations

1. Construct a functorial all-bidegree splitting of
   \(\mathcal C_{a,b}\colon\ker\partial\to\mathsf{Diag}_{a,b}\), or
   produce a first nonzero cokernel certificate.
2. Prove or refute the infinite edge-family pattern.  The current
   script has a parametric candidate, but this report does not prove it.
3. Decide the next balanced obstruction case, beginning with \((5,5)\),
   after improving the free-diagram canonicalization enough to make the
   exact solve bounded.
4. Do not use these finite certificates as unconditional radial-parts
   input outside the stated bidegrees.
