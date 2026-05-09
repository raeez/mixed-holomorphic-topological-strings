# Agent 152: kernel contracting homotopy attack-heal

Date: 2026-04-30

Scope owned: `appendix-radial-parts-moyal.tex`,
`scripts/quantum_shear_trace_diagram_normal_form.py`, and this report.
No compact-CY, CoHA, quintic, OSV/GV, Abel-Jacobi, Igusa, or BKM claim
was used or added.

## Claim Attacked

The target after Agent 140 was the remaining all-bidegree radial
quantum-shear theorem: construct, functorially in `(a,b)`, a contracting
homotopy on `ker(partial)` in the free trace-diagram complex producing
kernel corrections `K_{a,b}`.

Result: I did not find a functorial all-bidegree homotopy. The repaired
surface records the exact obstruction class whose vanishing is
equivalent to the missing kernel correction, and it proves additional
free-diagram vanishing certificates beyond `(4,4)`.

## Valid Attacks

```yaml
- id: A152-01
  target: all-bidegree functorial contracting homotopy
  severity: 2
  status: valid-not-closed
  failure_mode: finite-dimensional solves give lifts but no natural
    splitting of the contraction map C_{a,b}
  heal: replaced any closure claim by the obstruction class
    o_{a,b} in coker(C_{a,b}); all-bidegree theorem is now explicitly
    equivalent to o_{a,b}=0 for all bidegrees plus functorial choices

- id: A152-02
  target: uncorrected cyclic lift suffices quantum-mechanically
  severity: 2
  status: valid-healed
  failure_mode: in bidegree (4,4) the classical cyclic lift has a
    four-term free normal-form residual
  heal: retained the Agent 140 K_{4,4} correction and added script
    mode --kernel-correction to solve the residual inside ker(partial)

- id: A152-03
  target: finite-rank trace identities as evidence for universal theorem
  severity: 3
  status: valid-healed
  failure_mode: finite N matrix identities can kill free trace diagrams
    and therefore cannot prove the universal trace-diagram statement
  heal: new solve modes work in the free indexed normal-diagram basis;
    finite-rank checks remain only optional regression self-tests

- id: A152-04
  target: external compact-CY transfer into the local theorem
  severity: 3
  status: non-core-blocked
  failure_mode: external comparison claims would not follow from this
    local R^2_top x C^2_hol computation
  heal: no external comparison statement was added
```

## Repaired Labels

Added:

- `def:app-free-kernel-correction-obstruction`
- `prop:app-free-obstruction-certificates`

Repaired:

- `stmt:app-free-kernel-homotopy-obstruction`

Existing Agent 140 label used but not renamed:

- `prop:app-free-trace-diagram-K44`

## Exact Formulas

Let `W_{a,b}` be the rational span of words with `a-1` letters `X` and
`b-1` letters `Y`. Define

```tex
\partial W=[WYX]-[WXY].
```

The contraction map is

```tex
\mathcal C_{a,b}\left(\sum_W k_W W\right)
=
\mathcal N_{\mathrm{free}}\left(
  \sum_W k_W \operatorname{Tr}(W M)\right),
\qquad M=YX-XY+\hbar N I .
```

For a cyclic solution `c^{cl}` of the classical equation,

```tex
R_{a,b}^{free}
=
\mathcal N_{free}(E_{a,b,N})
-
\mathcal N_{free}\left(
  \sum_W c^{cl}_W \operatorname{Tr}(W M)\right),
\qquad
\mathfrak o_{a,b}=[R_{a,b}^{free}]\in \operatorname{coker}\mathcal C_{a,b}.
```

This class is independent of the cyclic lift because changing `c^{cl}`
by an element of `ker(partial)` changes `R` by an element of
`im(C_{a,b})`. Vanishing of `o_{a,b}` is exactly the existence of a
kernel correction `K_{a,b}`. No functorial all-bidegree splitting was
constructed.

The `(4,4)` kernel correction remains

```tex
K_{4,4}
= \frac{43}{14}\operatorname{Tr}(XXYXYYM)
- \frac{43}{14}\operatorname{Tr}(XYXXYYM)
- \frac{43}{14}\operatorname{Tr}(XYYXYXM)
+ \frac{43}{14}\operatorname{Tr}(XYYYXXM).
```

The new free certificates are

```tex
E_{3,5,N}
= \frac{36}{7}\operatorname{Tr}(XXYYYYM)
+ \frac{24}{7}\operatorname{Tr}(XYXYYYM)
- \frac{6}{7}\operatorname{Tr}(XYYXYYM)
- \frac{6}{7}\operatorname{Tr}(XYYYXYM)
+ \frac{30}{7}\operatorname{Tr}(XYYYYXM)
+ \frac{12}{7}\operatorname{Tr}(YXYXYYM),
```

and

```tex
E_{5,3,N}
= \frac{24}{7}\operatorname{Tr}(XXXXYYM)
- \frac{4}{7}\operatorname{Tr}(XXXYXYM)
+ \frac{20}{7}\operatorname{Tr}(XXXYYXM)
+ \frac{12}{7}\operatorname{Tr}(XXYXXYM)
- \frac{8}{7}\operatorname{Tr}(XXYXYXM)
+ \frac{16}{7}\operatorname{Tr}(XXYYXXM).
```

The edge-family certificates tested here use

```tex
\sum_{r=0}^{2}(6-2r)\operatorname{Tr}(Y^rXY^{6-r}M),
\qquad
\frac{3}{8}\sum_{r=0}^{2}(6-2r)\operatorname{Tr}(X^{6-r}YX^rM).
```

They have zero kernel correction in bidegrees `(2,7)` and `(7,2)`.

## Script Extension

`scripts/quantum_shear_trace_diagram_normal_form.py` now has:

- `--solve-free`: directly solves for a free indexed trace-diagram
  primitive in the chosen bidegree.
- `--kernel-correction`: solves the cyclic equation, computes the free
  residual, and solves for a correction constrained by `partial K=0`.
- `--edge-family-max`: optional edge-family batch driver.

The kernel-correction system tags cyclic rows and diagram rows in one
rational sparse linear system. It does not use finite-rank trace
identities.

## Script Outputs

Expected attack failure for the uncorrected `(4,4)` lift:

```text
FAIL a=4 b=4 mode=classical-only target_terms=39 candidate_terms=9 residual_terms=4
terms=4
      43/7 * hbar^2 D[(X0>1,X1>2,Y2>3,Y3>0)]
     -43/7 * hbar^2 D[(X0>1,X2>3,Y1>2,Y3>0)]
     -43/7 * hbar^3 D[(X0>0) (Y0>0)]
      43/7 * hbar^3 N D[(X0>1,Y1>0)]
```

Kernel correction for `(4,4)`:

```text
PASS a=4 b=4 mode=kernel-correction classical=ok classical_terms=9 residual_terms=4 correction=ok correction_terms=4 rank=10 rows=49 cols=20 corrected_residual_terms=0
     43/14 * Tr(XXYXYY M)
    -43/14 * Tr(XYXXYY M)
    -43/14 * Tr(XYYXYX M)
     43/14 * Tr(XYYYXX M)
```

Free solves beyond `(4,4)`:

```text
PASS a=3 b=5 mode=free-solve target_terms=23 support=6 rank=6 rows=24 cols=15 residual_terms=0
PASS a=5 b=3 mode=free-solve target_terms=23 support=6 rank=6 rows=24 cols=15 residual_terms=0
PASS: all requested free solves have zero free trace-diagram residual.
```

Edge-family obstruction checks:

```text
PASS a=2 b=7 mode=kernel-correction classical=ok classical_terms=3 residual_terms=0 correction=ok correction_terms=0 rank=3 rows=14 cols=7 corrected_residual_terms=0
PASS a=7 b=2 mode=kernel-correction classical=ok classical_terms=3 residual_terms=0 correction=ok correction_terms=0 rank=3 rows=14 cols=7 corrected_residual_terms=0
PASS: all requested kernel-correction obstruction classes vanish.
```

Regression checks:

```text
python3 -m py_compile scripts/quantum_shear_trace_diagram_normal_form.py scripts/quantum_shear_primitive_search.py scripts/quantum_shear_universal_formula.py
# pass

python3 scripts/quantum_shear_trace_diagram_normal_form.py --self-test --self-test-rank 2 --self-test-max-length 5 --max-terms 8
# PASS self-test rank=2 max_length=5 checked=63
# PASS: all requested candidates have zero free trace-diagram residual.

python3 scripts/quantum_shear_trace_diagram_normal_form.py --max-terms 8
# PASS: all requested candidates have zero free trace-diagram residual.
```

## Build Status

`make pdf` succeeded once after the appendix reflow and wrote
`out/main.pdf`. It still reported the pre-existing appendix overfull at
line 584 from the Agent 140 `(4,4)` display.

A later extra cross-reference rerun failed outside my scope in
`main.tex` bibliography lines 8266--8279:

```text
! Package rkeyval Error: Invalid key name character.
l.8275    },
```

I did not edit `main.tex`; this is not part of Agent 152 ownership.

## Files Changed / Staged

Files changed by this agent:

- `appendix-radial-parts-moyal.tex`
- `scripts/quantum_shear_trace_diagram_normal_form.py`
- `reconstitution/swarm-2026-04-30-agent-152-kernel-contracting-homotopy.md`

I did not run `git add`. Before this report was added, observed scoped
status was `MM appendix-radial-parts-moyal.tex` and
`AM scripts/quantum_shear_trace_diagram_normal_form.py`, so the index
already contained staged entries not created by a staging command in
this session. `main.tex` and `out/main.pdf` were also modified in the
shared worktree/build surface, outside the Agent 152 edit scope.

## Remaining Theorem Obligations

1. Construct a functorial all-bidegree splitting of
   `C_{a,b}: ker(partial) -> Diag_{a,b}`, or prove it cannot exist.
2. Decide whether `o_{a,b}=0` for all bidegrees; a first nonzero
   obstruction would be a computable cokernel class.
3. Prove an infinite edge-family theorem if the edge pattern is to be
   promoted beyond the tested `(2,7)` and `(7,2)` cases.
4. Improve high-degree free-diagram canonicalization before pushing much
   past total bidegree eight; current canonicalization becomes expensive.
