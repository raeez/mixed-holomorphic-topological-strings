# Radial all-interior necklace homotopy push

Date: 2026-04-30.

## Status

No manuscript or script file was edited.  This note pushes the radial/Weyl
interior theorem surface beyond the proved edge strip by formulating the
associated-graded two-colour necklace theorem which would close all
interior bidegrees.

The strongest honest statement is a left-cokernel vanishing theorem.  It is
equivalent to an associated-graded necklace homotopy.  No stable
left-cokernel functional was found.  New exact finite checks extend the
non-edge certificate window through total degree \(13\), prove by
computation that the first interior strips \(a=3\) and \(b=3\) need no
kernel correction through \(12\), and verify the \(a=4\) strip through
\((4,11)\).  The unfinished \((4,12)\) run is not evidence.

## Evidence anchors

The manuscript already has the right obstruction object.

- `appendix-radial-parts-moyal.tex:559-645`: free trace-diagram quantum-lift obstruction and the first nonzero \((4,4)\) correction.
- `appendix-radial-parts-moyal.tex:669-722`: free indexed normal diagrams and PBW normal-ordering.
- `appendix-radial-parts-moyal.tex:741-764`: stable injectivity for free normal diagrams.
- `appendix-radial-parts-moyal.tex:820-895`: obstruction class
  \[
    \mathfrak o_{a,b}=[R^{\mathrm{free}}_{a,b}]
    \in\operatorname{coker}\mathcal C_{a,b}.
  \]
- `appendix-radial-parts-moyal.tex:898-1044`: proved edge PBW telescoping theorem.
- `appendix-radial-parts-moyal.tex:1046-1145`: finite non-edge free certificates.
- `appendix-radial-parts-moyal.tex:1442-1495`: script verification status and its limits.

The script implements the same chain problem.

- `scripts/quantum_shear_trace_diagram_normal_form.py:1-18`: the basis is free indexed normal diagrams, not finite-rank trace identities.
- `scripts/quantum_shear_trace_diagram_normal_form.py:276-360`: PBW matchings and \(\operatorname{Tr}(WM)\).
- `scripts/quantum_shear_trace_diagram_normal_form.py:382-412`: Moyal target and shear defect.
- `scripts/quantum_shear_trace_diagram_normal_form.py:745-801`: kernel-correction solve in the tagged cyclic plus diagram system.
- `scripts/quantum_shear_primitive_search.py:347-419`: rational sparse elimination.  This is a pivot-gauge solver, not a functorial homotopy.

## Stage 1: the graph behind \(\partial\)

For \(a,b\geq 1\), define a graph \(G_{a,b}\).  Its vertices are cyclic
words with \(a\) letters \(X\) and \(b\) letters \(Y\).  Its oriented edges
are words \(W\) with \(a-1\) letters \(X\) and \(b-1\) letters \(Y\):
\[
  e_W\colon [WXY]\longrightarrow [WYX].
\]
Then the manuscript boundary
\[
  \partial W=[WYX]-[WXY]
\]
is exactly the incidence map \(C_1(G_{a,b})\to C_0(G_{a,b})\), and
\(\ker\partial=H_1(G_{a,b})\).  The first correction
\[
  XXYXYY-XYXXYY-XYYXYX+XYYYXX
\]
is a square cycle in this graph.  The larger \((5,5)\) and \((6,6)\)
corrections computed by earlier agents are weighted sums of the same
cellular square geometry.

This graph interpretation is the clean associated-graded habitat.  The
edge theorem is the one-dimensional case of this incidence complex.  The
all-interior theorem is a statement about the cycle space of \(G_{a,b}\),
with PBW contraction decorations.

## Stage 2: strongest theorem candidate

Let
\[
  \mathcal C_{a,b}\colon \ker\partial\to\mathsf{Diag}_{a,b}
\]
be the manuscript contraction map
\[
  K=\sum_W k_WW\longmapsto
  \mathcal N_{\mathrm{free}}\left(
    \sum_W k_W\operatorname{Tr}(WM)\right),
  \qquad M=YX-XY+\hbar NI.
\]
Filter \(\mathsf{Diag}_{a,b}\) by PBW contraction degree.  Since
\(\partial K=0\), the degree-zero part of \(\mathcal C_{a,b}(K)\) vanishes;
only positive contraction degrees remain.

**Theorem candidate, all-interior necklace left-cokernel vanishing.**  For
all \(a,b\geq3\), every stable free-diagram functional
\[
  \lambda\colon\mathsf{Diag}_{a,b}^{+}\to\mathbb Q[\hbar,N]
\]
such that
\[
  \lambda\mathcal C_{a,b}(K)=0
  \qquad\text{for all }K\in\ker\partial
\]
satisfies
\[
  \lambda(R^{\mathrm{free}}_{a,b})=0.
\]
Equivalently,
\[
  R^{\mathrm{free}}_{a,b}\in
  \operatorname{im}\left(
    \mathcal C_{a,b}\colon\ker\partial\to\mathsf{Diag}_{a,b}
  \right)
\]
for all \(a,b\geq3\).  Thus \(\mathfrak o_{a,b}=0\) in every interior
bidegree.

This is stronger than bounded certificates and weaker than a displayed
closed formula for every \(K_{a,b}\).  It is the exact theorem needed by
Statement `stmt:app-free-kernel-homotopy-obstruction`.

## Stage 3: equivalent homotopy

Let \(\mathsf{Diag}_{a,b}^{(q)}\) be contraction degree \(q\).  Write
\[
  \mathcal C_{a,b}=\partial+\sum_{q\geq1}\hbar^q C^{(q)}_{a,b}.
\]
The candidate homotopy is the cellular Green homotopy of the decorated
necklace graph:
\[
  H^{\mathrm{neck}}_{a,b,q}
  =
  \iota_{a,b}\,\Delta_{a,b,q}^{-1}\,d^{*}_{a,b,q}\,\pi_{a,b,q}.
\]
Here \(d\) is the incidence differential on the graph \(G_{a,b}\) with the
PBW matching decoration fixed, \(\Delta=dd^*+d^*d\) is the finite necklace
Laplacian on the zero-mean subspace, \(\pi\) projects a positive
contraction diagram to its decorated edge cochain, and \(\iota\) sends the
resulting cycle back into \(\ker\partial\).  The inverse is taken after
removing harmonic vectors.  The left-cokernel theorem above is precisely
the assertion that the residual has no harmonic projection.

With this \(H\), construct \(K_{a,b}\) recursively by contraction degree:
\[
  K^{(q)}_{a,b}
  =
  H^{\mathrm{neck}}_{a,b,q}\left(
    R^{(q)}_{a,b}
    -\sum_{0<i<q} C^{(q-i)}_{a,b}K^{(i)}_{a,b}
  \right).
\]
Then \(K_{a,b}=\sum_q K^{(q)}_{a,b}\) gives
\[
  \mathcal N_{\mathrm{free}}\left(
    \sum_W (K_{a,b})_W\operatorname{Tr}(WM)\right)
  =
  R^{\mathrm{free}}_{a,b}.
\]

Proof skeleton:

1. Identify \(\ker\partial\) with \(H_1(G_{a,b})\).  This is immediate from
   the incidence description of \(\partial\).
2. For a fixed PBW matching \(\Gamma\), prove that
   \(\operatorname{Tr}(WM)\) gives a decorated edge cochain.  The local
   relation is the PBW matching formula of
   `appendix-radial-parts-moyal.tex:693-722`; the scalar
   \(\hbar N\operatorname{Tr}(W)\) cancels the isolated-loop faces.
3. Prove harmonic vanishing.  Equivalently, if
   \(\lambda\mathcal C_{a,b}\) has zero period on every cycle of
   \(G_{a,b}\), then \(\lambda\mathcal C_{a,b}=\delta\phi_\lambda\) for a
   vertex potential \(\phi_\lambda\), and the Moyal shear target satisfies
   \[
     \lambda\mathcal N_{\mathrm{free}}(E_{a,b,N})
     =
     \phi_\lambda\left(
       \sum_{j=0}^b[Y^jX^aY^{b-j}]
       -\frac{b+1}{\binom{a+b}{a}}
        \sum_{U\in\operatorname{Sh}(a,b)}[U]
     \right).
   \]
   This is the left-cokernel vanishing theorem in potential form.
4. Apply the recursive formula for \(K^{(q)}_{a,b}\).  The stable
   injectivity lemma then promotes the free diagram identity to the
   all-\(N\) universal indexed statement.

The hard point is Step 3.  It should be attacked as a finite-dimensional
Hodge theorem for decorated two-colour necklaces, not as another
lexicographic sparse solve.

## Stage 4: exact obstruction if the theorem fails

If all-interior vanishing fails, the precise obstruction is the harmonic
projection
\[
  \Pi^{\mathrm{harm}}_{a,b}
  R^{\mathrm{free}}_{a,b}\neq0
\]
in the decorated necklace Laplacian above.

Equivalently, the obstruction is a stable functional \(\lambda\) with
\[
  \lambda\mathcal C_{a,b}(K)=0
  \quad\text{for all }K\in\ker\partial,
  \qquad
  \lambda(R^{\mathrm{free}}_{a,b})\neq0.
\]
In script terms, it is a left null vector of the tagged matrix assembled
in `solve_kernel_correction_case`, with nonzero pairing against the tagged
target.  This is not a heuristic obstruction.  It is the exact
left-cokernel row which would block the all-bidegree radial/Weyl statement.

No such row appeared in the finite windows below.

## Stage 5: new finite checks

All commands were run with `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`.
No bytecode, TeX, PDF, or script output file was intentionally written.

### Total degree 13 interior strip

Command:

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,10 --case 10,3 --case 4,9 --case 9,4 \
  --case 5,8 --case 8,5 --case 6,7 --case 7,6 \
  --kernel-correction --progress --max-terms 1
```

Result:

```text
(3,10): residual_terms=0   correction_terms=0   rank=21  rows=104 cols=55
(10,3): residual_terms=0   correction_terms=0   rank=21  rows=104 cols=55
(4,9):  residual_terms=10  correction_terms=12  rank=57  rows=285 cols=165
(9,4):  residual_terms=10  correction_terms=12  rank=57  rows=285 cols=165
(5,8):  residual_terms=78  correction_terms=46  rank=111 rows=542 cols=330
(8,5):  residual_terms=90  correction_terms=49  rank=111 rows=542 cols=330
(6,7):  residual_terms=165 correction_terms=83  rank=154 rows=744 cols=462
(7,6):  residual_terms=170 correction_terms=79  rank=154 rows=744 cols=462
```

Every corrected residual is zero.  This extends the recorded non-edge
window from total degree \(12\) to total degree \(13\).

### Width-one interior strips

Commands:

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,3 --case 3,4 --case 3,5 --case 3,6 --case 3,7 \
  --case 3,8 --case 3,9 --case 3,10 --case 3,11 --case 3,12 \
  --kernel-correction --progress --max-terms 1

python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,3 --case 5,3 --case 6,3 --case 7,3 --case 8,3 \
  --case 9,3 --case 10,3 --case 11,3 --case 12,3 \
  --kernel-correction --progress --max-terms 1
```

Result: every checked case has

```text
residual_terms=0, correction_terms=0, corrected_residual_terms=0.
```

This supports a separate width-one interior theorem:
the lexicographic cyclic lift should already be a full free
normal-diagram lift for \(a=3\) or \(b=3\).  The proof should be a
two-moving-letter PBW telescoping argument.  It is not yet inscribed as a
closed formula.

### Width-two \(a=4\) strip

Command:

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --case 4,5 --case 4,6 --case 4,7 --case 4,8 \
  --case 4,9 --case 4,10 --case 4,11 --case 4,12 \
  --kernel-correction --progress --max-terms 1
```

Completed rows:

```text
(4,4):  residual_terms=4  correction_terms=4
(4,5):  residual_terms=4  correction_terms=4
(4,6):  residual_terms=7  correction_terms=7
(4,7):  residual_terms=7  correction_terms=8
(4,8):  residual_terms=10 correction_terms=12
(4,9):  residual_terms=10 correction_terms=12
(4,10): residual_terms=13 correction_terms=16
(4,11): residual_terms=13 correction_terms=16
```

Every completed corrected residual is zero.  The \((4,12)\) row did not
return after several polling windows and was stopped.  It is not counted.

## Attack-heal conclusion

The edge theorem is no longer the frontier.  The interior problem has a
precise associated-graded form:

\[
  \text{prove } \Pi^{\mathrm{harm}}_{a,b}R^{\mathrm{free}}_{a,b}=0
  \text{ for every }a,b\geq3,
\]
or exhibit the first stable harmonic functional with nonzero residual
pairing.  Finite certificates now support the vanishing theorem through
all non-edge bidegrees of total degree \(13\), plus width-one strips through
\(12\), but they remain checks.  The next proof move is to build the
decorated-necklace Hodge homotopy and prove the potential identity in
Stage 3.
