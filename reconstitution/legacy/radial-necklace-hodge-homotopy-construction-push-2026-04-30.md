# Radial necklace Hodge homotopy construction push

Date: 2026-04-30.

## Status

No TeX file and no script file was edited.  This note pushes Agent 230's
decorated two-colour necklace formulation to an exact finite-dimensional
Hodge obstruction theorem.

The all-bidegree vanishing theorem is not proved here.  The stable core is
sharper: for every bidegree \((a,b)\) there is a canonical decorated Hodge
projection
\[
  \Pi^{\mathrm{harm}}_{a,b}R^{\mathrm{free}}_{a,b}
\]
whose vanishing is necessary and sufficient for the kernel correction
\(K_{a,b}\).  If this projection is nonzero, it is the exact obstruction
theorem for the all-bidegree radial/Weyl statement.  If it vanishes, the
Green operator of the decorated Laplacian gives the correction.

## Evidence anchors

- `appendix-radial-parts-moyal.tex:559-645`: the free trace-diagram quantum
  lift obstruction and the first \(K_{4,4}\) correction.
- `appendix-radial-parts-moyal.tex:669-722`: free indexed normal diagrams and
  the PBW normal-ordering formula.
- `appendix-radial-parts-moyal.tex:820-895`: the cokernel class
  \(\mathfrak o_{a,b}=[R^{\mathrm{free}}_{a,b}]\) and the remaining
  kernel-homotopy obstruction.
- `theorem-lanes.tex:2392-2529`: the degree-zero Moyal/Weyl theorem lane and
  its radial/Weyl gate.
- `open-obligations.tex:1060-1129`: the current obstruction-complex
  formulation, including the harmonic projection target.
- `claim-strength-ledger.tex:773-818`: ledger status for the finite
  certificates and uniform homotopy obstruction.
- `scripts/quantum_shear_trace_diagram_normal_form.py:276-360`: inversion
  matchings and \(\operatorname{Tr}(WM)\) normal form.
- `scripts/quantum_shear_trace_diagram_normal_form.py:382-412`: Moyal target
  and shear defect.
- `scripts/quantum_shear_trace_diagram_normal_form.py:745-801`: the tagged
  kernel-correction solve.
- `scripts/quantum_shear_primitive_search.py:347-419`: exact rational sparse
  elimination.

## 1. The classical necklace incidence complex

Fix \(a,b\geq1\).  Let
\[
  \mathsf W_{a,b}
  =
  \mathbb Q\langle X,Y\rangle_{a-1,b-1}
\]
be the rational span of linear words with \(a-1\) \(X\)'s and \(b-1\)
\(Y\)'s.  Let \(\mathsf V_{a,b}\) be the rational span of cyclic words with
\(a\) \(X\)'s and \(b\) \(Y\)'s.  Define the multigraph \(G_{a,b}\) by

- vertices \(v=[U]\in\mathsf V_{a,b}\);
- oriented edges \(e_W\), indexed by \(W\in\mathsf W_{a,b}\), with
  \[
    e_W:[WXY]\longrightarrow[WYX].
  \]

The incidence boundary is
\[
  \partial_{a,b}W=[WYX]-[WXY].
\]
Thus
\[
  Z_{a,b}:=\ker\partial_{a,b}=H_1(G_{a,b};\mathbb Q)
\]
as a cycle space.  The graph is connected for \(a,b>0\): adjacent
transpositions move any binary cyclic word to the monotone necklace, and
the displayed edges are exactly the adjacent \(XY\leftrightarrow YX\)
moves modulo cyclic rotation.

Let
\[
  T_{a,b}
  =
  \sum_{j=0}^{b}[Y^jX^aY^{b-j}]
  -
  {b+1\over\binom{a+b}{a}}
  \sum_{U\in\operatorname{Sh}(a,b)}[U].
\]
The total coefficient of \(T_{a,b}\) is zero, hence
\[
  T_{a,b}\in\operatorname{im}\partial_{a,b}.
\]
With the cyclic-word basis orthonormal, let
\[
  \Delta^0_{a,b}=\partial_{a,b}\partial_{a,b}^{*}
\]
on the zero-mean vertex subspace.  The classical Hodge lift
\[
  c^{\mathrm{cl}}_{a,b}
  =
  \partial_{a,b}^{*}(\Delta^0_{a,b})^{-1}T_{a,b}
\]
solves
\[
  \partial_{a,b}c^{\mathrm{cl}}_{a,b}=T_{a,b}.
\]
This is a canonical replacement for the pivot-gauge cyclic lift used by the
script.  Changing the classical lift changes the later residual by an
element of the cycle correction image, so it does not change the obstruction
class.

## 2. Decorated PBW cochains

Let \(\mathsf D_{a,b}\) be the rational span of the free indexed normal
diagrams in bidegree \((a,b)\), with the hbar and \(N\) powers included as
part of the basis key.  Let \(\mathsf D^+_{a,b}\) be the complement to the
uncontracted \(\hbar^0\) cyclic component.  Equivalently, \(\mathsf D^+\)
is the positive normal-ordering sector left after the cyclic incidence
equation has been solved.  It includes the \(\hbar N\operatorname{Tr}(W)\)
Capelli term, because that term is invisible to the classical incidence
boundary but visible in the free indexed diagram algebra.

For \(W\in\mathsf W_{a,b}\), define
\[
  C^+_{a,b}(W)
  =
  \pi_+
  \mathcal N_{\mathrm{free}}\operatorname{Tr}(WM),
  \qquad
  M=YX-XY+\hbar NI,
\]
where \(\pi_+\) removes the uncontracted cyclic component.  Explicitly,
using the PBW matching formula,
\[
\begin{aligned}
  C^+_{a,b}(W)
  =
  \pi_+\bigg(
    &\sum_{\Gamma\in\operatorname{Match}(WYX)}
      (-\hbar)^{|\Gamma|}N^{e(WYX,\Gamma)}
      \mathsf D(WYX,\Gamma)\\
    &-
    \sum_{\Gamma\in\operatorname{Match}(WXY)}
      (-\hbar)^{|\Gamma|}N^{e(WXY,\Gamma)}
      \mathsf D(WXY,\Gamma)\\
    &+
    \hbar N
    \sum_{\Gamma\in\operatorname{Match}(W)}
      (-\hbar)^{|\Gamma|}N^{e(W,\Gamma)}
      \mathsf D(W,\Gamma)
  \bigg).
\end{aligned}
\]
This is the decorated edge cochain map.  It decomposes into component
functionals indexed by PBW contraction diagrams; each component is an edge
cochain on \(G_{a,b}\).

Put
\[
  A_{a,b}:=C^+_{a,b}|_{Z_{a,b}}:
  Z_{a,b}\longrightarrow\mathsf D^+_{a,b}.
\]
For a chosen classical lift \(c^{\mathrm{cl}}\), put
\[
  E^+_{a,b}
  =
  \pi_+\mathcal N_{\mathrm{free}}(E_{a,b,N})
\]
and
\[
  R^{\mathrm{free}}_{a,b}
  =
  E^+_{a,b}-C^+_{a,b}(c^{\mathrm{cl}}_{a,b}).
\]
Then the desired correction is exactly
\[
  A_{a,b}K_{a,b}=R^{\mathrm{free}}_{a,b},
  \qquad K_{a,b}\in Z_{a,b}.
\]
This is the relative form of the tagged script solve: the script uses the
matrix
\[
  B_{a,b}:\mathsf W_{a,b}\to
  \mathsf V_{a,b}\oplus\mathsf D^+_{a,b},
  \qquad
  W\mapsto(\partial W,C^+(W)),
\]
and solves
\[
  B_{a,b}K=(0,R^{\mathrm{free}}_{a,b}).
\]

## 3. Decorated Hodge obstruction theorem

Give \(Z_{a,b}\) and \(\mathsf D^+_{a,b}\) the inner products for which the
chosen word-cycle and diagram bases are orthonormal.  Let
\[
  A=A_{a,b},\qquad A^*:\mathsf D^+_{a,b}\to Z_{a,b}
\]
be the adjoint.  Define the decorated Laplacian on diagram cochains by
\[
  \Delta^{\mathrm{dec}}_{a,b}=AA^*.
\]
Its harmonic subspace is
\[
  \mathsf H^{\mathrm{dec}}_{a,b}
  =
  \ker A^*
  =
  (\operatorname{im}A)^\perp.
\]
Let
\[
  \Pi^{\mathrm{harm}}_{a,b}:
  \mathsf D^+_{a,b}\to \mathsf H^{\mathrm{dec}}_{a,b}
\]
be the orthogonal projection.

**Theorem.**  For every \(a,b\geq1\), the following are equivalent.

1. There exists \(K_{a,b}\in\ker\partial_{a,b}\) such that
   \[
     C^+_{a,b}(K_{a,b})=R^{\mathrm{free}}_{a,b}.
   \]
2. The cokernel obstruction class
   \[
     \mathfrak o_{a,b}
     =
     [R^{\mathrm{free}}_{a,b}]
     \in\operatorname{coker}
     (C^+_{a,b}:\ker\partial_{a,b}\to\mathsf D^+_{a,b})
   \]
   vanishes.
3. The decorated harmonic projection vanishes:
   \[
     \Pi^{\mathrm{harm}}_{a,b}R^{\mathrm{free}}_{a,b}=0.
   \]
4. Every diagram functional
   \(\lambda\in(\mathsf D^+_{a,b})^*\) satisfying
   \[
     \lambda C^+_{a,b}(K)=0\qquad(K\in\ker\partial_{a,b})
   \]
   also satisfies
   \[
     \lambda(R^{\mathrm{free}}_{a,b})=0.
   \]

When these equivalent conditions hold, the Hodge correction is
\[
  K_{a,b}
  =
  A^*(\Delta^{\mathrm{dec}}_{a,b})^{-1}
  R^{\mathrm{free}}_{a,b},
\]
where the inverse is taken on \(\operatorname{im}A\).  If the harmonic
projection is nonzero, any functional detecting it is an exact left-cokernel
obstruction to the all-bidegree radial/Weyl theorem.

**Proof.**  The finite-dimensional Hodge decomposition for \(A\) gives
\[
  \mathsf D^+_{a,b}
  =
  \operatorname{im}A
  \oplus
  \ker A^*.
\]
Thus \(R^{\mathrm{free}}_{a,b}\in\operatorname{im}A\) if and only if its
projection to \(\ker A^*\) is zero.  This proves the equivalence of (1),
(2), and (3).  The dual statement (4) is the usual annihilator criterion
for membership in a finite-dimensional image:
\[
  R\in\operatorname{im}A
  \quad\Longleftrightarrow\quad
  \lambda(R)=0\text{ for every }\lambda\in\ker A^*.
\]
If \(R\in\operatorname{im}A\), then
\[
  AA^*(AA^*)^{-1}R=R,
\]
so \(K=A^*(AA^*)^{-1}R\) is a correction.  Conversely, a correction makes
the harmonic projection vanish.  This proves the theorem.

## 4. Potential formulation

For \(\lambda\in(\mathsf D^+_{a,b})^*\), define an edge cochain
\[
  \alpha_\lambda(W)=\lambda(C^+_{a,b}(W)).
\]
The condition
\[
  \lambda C^+_{a,b}|_{Z_{a,b}}=0
\]
means that \(\alpha_\lambda\) has zero period on every cycle of
\(G_{a,b}\).  Since \(G_{a,b}\) is connected, this is equivalent to the
existence of a vertex potential
\[
  \phi_\lambda\in\mathsf V_{a,b}^*
\]
with
\[
  \lambda C^+_{a,b}(W)
  =
  \phi_\lambda([WYX])-\phi_\lambda([WXY])
  =
  \phi_\lambda(\partial W)
  \qquad(W\in\mathsf W_{a,b}).
\]
The potential is unique up to an additive constant, and the value
\(\phi_\lambda(T_{a,b})\) is independent of that constant because
\(T_{a,b}\) has total coefficient zero.

For such a potential,
\[
\begin{aligned}
  \lambda(R^{\mathrm{free}}_{a,b})
  &=
  \lambda(E^+_{a,b})
  -
  \lambda C^+_{a,b}(c^{\mathrm{cl}}_{a,b})\\
  &=
  \lambda(E^+_{a,b})
  -
  \phi_\lambda(\partial c^{\mathrm{cl}}_{a,b})\\
  &=
  \lambda(E^+_{a,b})-\phi_\lambda(T_{a,b}).
\end{aligned}
\]
Therefore
\[
  \Pi^{\mathrm{harm}}_{a,b}R^{\mathrm{free}}_{a,b}=0
\]
if and only if every decorated edge cochain with zero cycle periods satisfies
the Moyal potential identity
\[
  \boxed{\lambda(E^+_{a,b})=\phi_\lambda(T_{a,b}).}
\]
This is the exact all-bidegree condition.  It is stronger than any finite
table and weaker than a closed formula for \(K_{a,b}\).  Proving this
identity for all diagram functionals \(\lambda\) would close the
all-bidegree homotopy.  Producing one \(\lambda\) for which it fails would
prove the obstruction theorem in that bidegree.

## 5. Attack on the naive Agent 230 homotopy

Agent 230 proposed
\[
  H^{\mathrm{neck}}_{a,b,q}
  =
  \iota_{a,b}\Delta^{-1}_{a,b,q}d^*_{a,b,q}\pi_{a,b,q}.
\]
This is the right shape but not yet a constructed homotopy.  The attack is
load-bearing:

1. The bare graph Laplacian \(dd^*+d^*d\) inverts the incidence boundary
   \(\partial\).  The quantum correction problem in the manuscript is not
   \(\partial K=R\); it is
   \[
     C^+_{a,b}(K)=R,\qquad K\in\ker\partial.
   \]
   The correct Laplacian for this relative problem is \(AA^*\), or
   equivalently the tagged Laplacian \(BB^*\) on
   \(\mathsf V\oplus\mathsf D^+\).
2. A projection
   \[
     \pi_{a,b,q}:\mathsf D^+_{a,b}\to C^1(G_{a,b})
   \]
   is not canonical from the present data.  Each diagram functional gives an
   edge cochain by pullback along \(C^+\), but there is no proved inverse
   sending an arbitrary diagram residual to a unique decorated edge cochain
   whose graph Hodge primitive is the desired \(K\).
3. The required missing theorem is exactly the potential identity above.
   The edge PBW theorem proves it in the one-moving-letter strip.  The
   \(K_{4,4}\), \(K_{5,5}\), and \(K_{6,6}\) corrections show that interior
   bidegrees require genuine cycle-space corrections, not a bare incidence
   inverse.

Thus the healed statement is not the naive graph Green operator.  It is the
relative decorated Hodge theorem for \(A=C^+|_{\ker\partial}\), with the
potential identity as the all-bidegree vanishing condition.

## 6. Small exact checks used only as calibration

All commands were run with `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`.
No script, TeX, PDF, or bytecode output file was intentionally written.

PBW free-normal-form self-test and \(K_{4,4}\) control:

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --self-test --self-test-rank 2 --self-test-max-length 5 \
  --case 4,4 --max-terms 0

PASS self-test rank=2 max_length=5 checked=63
PASS a=4 b=4 mode=candidate target_terms=39 candidate_terms=10 residual_terms=0
PASS: all requested candidates have zero free trace-diagram residual.
```

Relative kernel-correction calibration:

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --case 5,5 --kernel-correction --max-terms 0

PASS a=4 b=4 mode=kernel-correction classical=ok classical_terms=9
  residual_terms=4 correction=ok correction_terms=4 rank=10 rows=49
  cols=20 corrected_residual_terms=0

PASS a=5 b=5 mode=kernel-correction classical=ok classical_terms=25
  residual_terms=22 correction=ok correction_terms=16 rank=29 rows=143
  cols=70 corrected_residual_terms=0

PASS: all requested kernel-correction obstruction classes vanish.
```

Rank calibration from a read-only Python import:

```text
(3,3) words=6 vertices=4 rank_partial=3 cycle_dim=3
  diagram_keys=12 tagged_rank=3 rank_A=0 residual_terms=0
  correction_terms=0 corrected=True

(4,4) words=20 vertices=10 rank_partial=9 cycle_dim=11
  diagram_keys=39 tagged_rank=10 rank_A=1 residual_terms=4
  correction_terms=4 corrected=True

(5,5) words=70 vertices=26 rank_partial=25 cycle_dim=45
  diagram_keys=117 tagged_rank=29 rank_A=4 residual_terms=22
  correction_terms=16 corrected=True
```

These checks support the theorem surface but do not prove all-bidegree
vanishing.  They show why the decorated Laplacian must be \(AA^*\): in
\((4,4)\), the cycle space has dimension \(11\), while the positive
correction image detected in the tagged solve has rank \(1\).

## 7. Proposed insertion

Insert after Statement `stmt:app-free-kernel-homotopy-obstruction`, before
the finite certificate propositions.

```tex
\begin{defn}[Decorated necklace Hodge obstruction]
  Fix \(a,b\geq1\).  Let \(G_{a,b}\) be the two-colour necklace
  multigraph whose vertices are cyclic words with \(a\) \(X\)'s and
  \(b\) \(Y\)'s and whose oriented edges are words \(W\) with
  \(a-1\) \(X\)'s and \(b-1\) \(Y\)'s,
  \[
    e_W:[WXY]\to[WYX].
  \]
  Thus \(\partial W=[WYX]-[WXY]\) is the incidence map and
  \(Z_{a,b}=\ker\partial\) is the cycle space.  Let
  \[
    C^+_{a,b}(W)
    =
    \pi_+\mathcal N_{\mathrm{free}}\operatorname{Tr}(WM)
  \]
  be the positive free normal-diagram part, with
  \(M=YX-XY+\hbar NI\), and set
  \[
    A_{a,b}=C^+_{a,b}|_{Z_{a,b}}.
  \]
  With the word-cycle and free-diagram bases orthonormal, define
  \[
    \Delta^{\mathrm{dec}}_{a,b}=A_{a,b}A_{a,b}^{*},\qquad
    \mathsf H^{\mathrm{dec}}_{a,b}=\ker A_{a,b}^{*}.
  \]
  Let \(\Pi^{\mathrm{harm}}_{a,b}\) be the orthogonal projection to
  \(\mathsf H^{\mathrm{dec}}_{a,b}\).
\end{defn}

\begin{prop}[Decorated Hodge obstruction criterion]
  For any classical cyclic lift \(c^{\mathrm{cl}}_{a,b}\), let
  \[
    R^{\mathrm{free}}_{a,b}
    =
    \pi_+\mathcal N_{\mathrm{free}}(E_{a,b,N})
    -
    C^+_{a,b}(c^{\mathrm{cl}}_{a,b}).
  \]
  Then \(R^{\mathrm{free}}_{a,b}\) is in
  \(\operatorname{im}(C^+_{a,b}:\ker\partial\to\mathsf D^+_{a,b})\)
  if and only if
  \[
    \Pi^{\mathrm{harm}}_{a,b}R^{\mathrm{free}}_{a,b}=0.
  \]
  When this holds, the Hodge correction is
  \[
    K_{a,b}
    =
    A_{a,b}^{*}(\Delta^{\mathrm{dec}}_{a,b})^{-1}
    R^{\mathrm{free}}_{a,b},
  \]
  with the inverse on \(\operatorname{im}A_{a,b}\).  If the projection is
  nonzero, any functional detecting it is the exact left-cokernel
  obstruction to the all-bidegree radial/Weyl statement.
\end{prop}

\begin{rmk}[Potential form]
  A functional \(\lambda\) on \(\mathsf D^+_{a,b}\) lies in the left
  cokernel precisely when the edge cochain
  \(W\mapsto\lambda C^+_{a,b}(W)\) has zero periods on \(G_{a,b}\).  Since
  \(G_{a,b}\) is connected, this is equivalent to a potential
  \(\phi_\lambda\) with
  \[
    \lambda C^+_{a,b}(W)=\phi_\lambda([WYX])-\phi_\lambda([WXY]).
  \]
  Hence the all-bidegree theorem is the identity
  \[
    \lambda\pi_+\mathcal N_{\mathrm{free}}(E_{a,b,N})
    =
    \phi_\lambda(T_{a,b})
  \]
  for every such \(\lambda\).  A failure of this equality is the first
  harmonic obstruction.
\end{rmk}
```

## 8. Attack-heal ledger

```yaml
- id: A248-01
  severity: 2
  status: healed
  lens: decorated Hodge formulation
  target: Agent 230 graph Green homotopy
  claim: the bare necklace graph Laplacian constructs the quantum kernel
    correction
  broken_step: the correction equation is C^+(K)=R with K in ker(partial),
    not partial(K)=R
  evidence_type: proof_gap
  evidence_ref: appendix-radial-parts-moyal.tex:820-895;
    scripts/quantum_shear_trace_diagram_normal_form.py:745-801
  minimal_heal: replace the bare incidence Laplacian by the decorated
    relative Laplacian A A^* for A=C^+|_{ker partial}
  residual: prove Pi_harm R=0 uniformly, or exhibit a nonzero harmonic row

- id: A248-02
  severity: 2
  status: valid-not-closed
  lens: all-bidegree vanishing
  target: Pi_harm R_free=0 for all a,b
  claim: finite certificates imply the all-bidegree radial/Weyl theorem
  broken_step: finite sparse solves give pivot-gauge corrections, not the
    potential identity for every decorated left-cokernel functional
  evidence_type: proof_gap
  evidence_ref: open-obligations.tex:1060-1129; finite checks in this report
  minimal_heal: state the potential identity
    lambda(E^+)=phi_lambda(T) as the exact theorem target
  residual: prove the identity for all decorated PBW functionals

- id: A248-03
  severity: 3
  status: healed
  lens: obstruction theorem
  target: all-bidegree failure mode
  claim: failure of the all-bidegree theorem is vague residual evidence
  broken_step: the failure mode is an exact finite-dimensional harmonic
    projection, not a heuristic
  evidence_type: derivation
  evidence_ref: Hodge theorem in this report
  minimal_heal: record Pi_harm R_free as the exact obstruction class
  residual: none for the obstruction theorem; only the vanishing remains open
```

## Conclusion

The all-bidegree radial/Weyl theorem is now reduced to one exact identity:
for every decorated PBW functional whose edge cochain has zero graph periods,
the Moyal positive diagram target must equal the value of its vertex
potential on the classical shear target.  This is the theorem to prove.
Until it is proved, the manuscript should not claim an all-bidegree homotopy.
If the identity fails, the first failing functional is precisely
\(\Pi^{\mathrm{harm}}_{a,b}R^{\mathrm{free}}_{a,b}\) and gives the
obstruction theorem.
