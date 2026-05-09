# Radial/Weyl uniform homotopy mechanism

Date: 2026-04-30.

## Evidence surface

The exact obstruction is already the right object.  The manuscript defines
\(\mathcal C_{a,b}\colon\ker\partial\to\mathsf{Diag}_{a,b}\) and
\(\mathfrak o_{a,b}=[R^{\mathrm{free}}_{a,b}]\) in
`appendix-radial-parts-moyal.tex:820-866`; it states that all-bidegree
closure is equivalent to vanishing of these classes plus functorial lifts
in `appendix-radial-parts-moyal.tex:868-895`.  The free PBW normal-ordering
formula is `appendix-radial-parts-moyal.tex:693-722`, and stable free
diagram injectivity is `appendix-radial-parts-moyal.tex:741-764`.

The script implements the same complex.  Normal diagrams and matchings are
formed in `scripts/quantum_shear_trace_diagram_normal_form.py:276-352`;
\(\operatorname{Tr}(WM)\) is expanded in
`scripts/quantum_shear_trace_diagram_normal_form.py:355-360`; the Moyal
target is `scripts/quantum_shear_trace_diagram_normal_form.py:382-412`; and
the kernel-correction solve is
`scripts/quantum_shear_trace_diagram_normal_form.py:745-801`.  The sparse
solver is pivot-gauge Gaussian elimination, not a canonical homotopy
(`scripts/quantum_shear_primitive_search.py:347-419`).

Agent 191 extended the finite certificates: edge formulas through
\((2,12),(12,2)\) in
`reconstitution/swarm-2026-04-30-agent-191-radial-all-bidegree-obstruction-0957.md:68-92`;
balanced diagonal through \((6,6)\) in
`reconstitution/swarm-2026-04-30-agent-191-radial-all-bidegree-obstruction-0957.md:94-141`;
and the non-edge total-degree strip through degree \(12\) in
`reconstitution/swarm-2026-04-30-agent-191-radial-all-bidegree-obstruction-0957.md:143-157`.

## Mechanism found

Status: theorem candidate, not proved here.  The edge family has a visible
PBW telescoping mechanism.  In bidegree \((2,b)\), every word in
\(\mathsf W_{2,b}\) has one free \(X\).  Write
\[
  W_r=Y^rXY^{b-1-r},\qquad
  0\le r\le \lfloor(b-2)/2\rfloor .
\]
The candidate
\[
  C^{\mathrm{edge}}_{2,b}
  =
  \sum_r(b-1-2r)\operatorname{Tr}(W_rM)
\]
is a discrete divergence on the \(Y\)-string.  The proposed proof expands
\(\mathcal N_{\mathrm{free}}\operatorname{Tr}(W_rM)\), pairs each
non-boundary PBW matching with its adjacent translate in the \(r\)-sum, and
checks that the unpaired boundary matchings are exactly the odd Weyl/Moyal
terms in \(\{z_1^3/3,z_2^{b+1}\}_\hbar\), including the \(\hbar^2\)
pure-power term.  The scalar \(\hbar N\operatorname{Tr}(W_r)\) part should
cancel the isolated-loop diagrams.  The \((a,2)\) family is the same
argument after swapping \(X,Y\), with the Capelli/Weyl normalization factor
\(3/(a+1)\).

The interior and balanced cases show a different mechanism.  The residual
after the lexicographic cyclic lift is supported in positive contraction
degree.  For example, current runs give
\[
\begin{array}{c|c|c|c|c}
(a,b)&\text{classical terms}&\text{residual terms}&
\text{correction terms}&(\text{rank};\text{rows};\text{cols})\\
\hline
(4,4)&9&4&4&(10;49;20)\\
(5,5)&25&22&16&(29;143;70)\\
(6,6)&79&96&54&(93;446;252).
\end{array}
\]
The first correction \(K_{4,4}\) is a four-term shuffle square
(`appendix-radial-parts-moyal.tex:629-638`).  The \((5,5)\) and \((6,6)\)
corrections are larger combinations of the same adjacent-interchange
geometry, but the pivot coefficients are not canonical.  They should be
read as evidence for a cellular homotopy on two-colour cyclic words, not as
a closed formula.

The simple-cycle canonicalization in
`scripts/quantum_shear_trace_diagram_normal_form.py:169-238` is therefore
computational infrastructure.  It says that the uncontracted components are
directed colour necklaces and prevents factorial relabelling.  It does not
prove the homotopy.

## Theorem Candidate A: Edge Telescoping

For every \(b\ge2\), in the free indexed normal-diagram algebra,
\[
  \mathcal N_{\mathrm{free}}(E_{2,b,N})
  =
  \mathcal N_{\mathrm{free}}\!\left(
  \sum_{r=0}^{\lfloor(b-2)/2\rfloor}
  (b-1-2r)\operatorname{Tr}(Y^rXY^{b-1-r}M)\right).
\]
For every \(a\ge2\),
\[
  \mathcal N_{\mathrm{free}}(E_{a,2,N})
  =
  \mathcal N_{\mathrm{free}}\!\left(
  \frac3{a+1}\sum_{r=0}^{\lfloor(a-2)/2\rfloor}
  (a-1-2r)\operatorname{Tr}(X^{a-1-r}YX^rM)\right).
\]

Hypotheses: the Weyl convention of
`appendix-radial-parts-moyal.tex:16-37`; the matrix moment element
\(M=YX-XY+\hbar NI\); and the free normal-ordering theorem
`appendix-radial-parts-moyal.tex:693-722`.  No finite-rank trace identity
is used.

Proof strategy: filter matchings by the contracted position adjacent to the
unique free \(X\) (or \(Y\)).  Pair all translated interior matchings in the
weighted \(r\)-sum.  The two unpaired boundary faces reproduce the Moyal
target from `scripts/quantum_shear_trace_diagram_normal_form.py:383-396`.
The \(M\)-scalar term supplies precisely the isolated-loop contribution
created by the endpoint contraction.  This is a direct PBW telescoping
identity and should be inscribed before any further table extension.

## Theorem Candidate B: Uniform Interior Homotopy

Define the contraction filtration \(F^q\mathsf{Diag}_{a,b}\) by PBW
matching number.  Write
\[
  \mathcal C_{a,b}
  =
  \partial+\sum_{q\ge1}\hbar^qD_q
\]
on \(\mathsf W_{a,b}\), where the \(\hbar^0\) associated graded is the
cyclic boundary \(\partial W=[WYX]-[WXY]\).  Let
\[
  \mathsf K^{+}_{a,b}
  =
  \left(\ker\partial,\;D_1,D_2,\ldots\right)
\]
be the positive-contraction two-colour necklace complex obtained from the
free normal-ordering theorem.

Conditional theorem: if \(\mathsf K^{+}_{a,b}\) is acyclic on the residual
subspace generated by the Moyal shear defect, with a homotopy natural under
cyclic rotation, \(X\leftrightarrow Y\), and deletion of a paired
contraction, then \(\mathfrak o_{a,b}=0\) for all \(a,b\).  The lift is
constructed recursively by contraction degree:
\[
  K^{(q)}_{a,b}
  =
  -H\left(R^{(q)}_{a,b}
    -\sum_{i<q}D_{q-i}K^{(i)}_{a,b}\right).
\]
This would give a functorial splitting of \(\mathcal C_{a,b}\) and hence
the all-bidegree quantum shear primitive.

The missing invariant is exactly this associated-graded acyclicity, or
equivalently a natural left-cokernel theorem:
every cyclic, stable normal-diagram functional \(\lambda\) with
\(\lambda\mathcal C_{a,b}|_{\ker\partial}=0\) must satisfy
\(\lambda(R^{\mathrm{free}}_{a,b})=0\), compatibly in \((a,b)\).  The finite
certificates verify this invariant only in bounded windows.

## Attacks

- Pivot-gauge attack.  The displayed \(K_{5,5}\) and \(K_{6,6}\) supports
  come from the lexicographic sparse solver.  They are certificates, not
  formulas for a natural homotopy.
- Finite-table attack.  Edge checks through \(12\), balanced checks through
  \(6\), and total-degree checks through \(12\) do not imply the
  associated-graded left-cokernel theorem.
- Canonicalization attack.  Directed-cycle canonicalization removes the
  factorial wall for simple cycles, but it does not identify the cokernel.
- Finite-rank attack.  The optional PBW self-test specializes to rank \(2\);
  theorem status still comes only from the free normal-diagram basis and
  stable injectivity.

## Reproduction commands

```text
python3 -m py_compile scripts/quantum_shear_trace_diagram_normal_form.py \
  scripts/quantum_shear_primitive_search.py \
  scripts/quantum_shear_universal_formula.py

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --self-test --self-test-rank 2 --self-test-max-length 6 --max-terms 8

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --classical-only --max-terms 12

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --kernel-correction --max-terms 8

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --family-only --edge-family-max 12 --kernel-correction --progress \
  --max-terms 1

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --family-only --balanced-family-max 6 --kernel-correction --progress \
  --max-terms 4

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,7 --case 7,3 --case 4,5 --case 5,4 \
  --case 4,6 --case 6,4 --kernel-correction --progress --max-terms 1

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,8 --case 8,3 --case 4,7 --case 7,4 \
  --case 5,6 --case 6,5 --kernel-correction --progress --max-terms 1

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,9 --case 9,3 --case 4,8 --case 8,4 \
  --case 5,7 --case 7,5 --kernel-correction --progress --max-terms 1
```

The unresolved computational frontier from this pass remains \((7,7)\) and
the non-edge total-degree \(13\) strip.  No manuscript or script file was
edited.
