# Radial edge PBW telescoping theorem

Date: 2026-04-30.

## Status

The edge families admit a closed PBW telescoping proof sketch in the free
indexed normal-diagram algebra.  The proof uses the normal-ordering theorem
of `appendix-radial-parts-moyal.tex:693-722`, the obstruction boundary of
`appendix-radial-parts-moyal.tex:820-895`, Agent 191's edge formulas, and
Agent 203's one-moving-letter mechanism.

This note does not prove the balanced or interior all-bidegree theorem.  It
only isolates the edge theorem candidate and the elementary matching counts
needed to promote it to manuscript text.

## Theorem candidate

Let
\[
  M=YX-XY+\hbar NI
\]
and let \(E_{a,b,N}\) be the quantum shear defect of
`appendix-radial-parts-moyal.tex:532-557`.  For every \(b\ge 2\),
\[
  C_{2,b}^{\mathrm{edge}}
  =
  \sum_{r=0}^{\lfloor(b-2)/2\rfloor}
  (b-1-2r)\operatorname{Tr}(Y^rXY^{b-1-r}M).
\]
For every \(a\ge 2\),
\[
  C_{a,2}^{\mathrm{edge}}
  =
  \frac{3}{a+1}
  \sum_{r=0}^{\lfloor(a-2)/2\rfloor}
  (a-1-2r)\operatorname{Tr}(X^{a-1-r}YX^rM).
\]

The candidate theorem is the free normal-diagram identity
\[
  \mathcal N_{\mathrm{free}}(E_{2,b,N})
  =
  \mathcal N_{\mathrm{free}}(C_{2,b}^{\mathrm{edge}}),
  \qquad
  \mathcal N_{\mathrm{free}}(E_{a,2,N})
  =
  \mathcal N_{\mathrm{free}}(C_{a,2}^{\mathrm{edge}}).
\]
Thus the edge obstruction classes vanish with no separate kernel
correction:
\[
  R^{\mathrm{free}}_{2,b}=0,\qquad
  R^{\mathrm{free}}_{a,2}=0,
  \qquad K_{2,b}=K_{a,2}=0
\]
after choosing the displayed edge lift as the cyclic lift.

## Edge diagrams for \((2,b)\)

Let
\[
  \Theta_s^{(b)}=\mathsf D(XY^sXY^{b-s}),
  \qquad 0\le s\le b,
\]
with \(\Theta_s^{(b)}=\Theta_{b-s}^{(b)}\) after canonical cyclic
identification of the two \(X\)-edges.  Let
\[
  \Phi_s^{(b)}=\mathsf D(XY^s)\mid \mathsf D(Y^{b-1-s}),
  \qquad 0\le s\le b-1,
\]
where \(\mathsf D(Y^0)\) means the isolated index loop, hence contributes
the explicit factor \(N\).  Thus
\(\Phi_{b-1}^{(b)}=N\,\mathsf D(XY^{b-1})\).

For
\[
  W_r=Y^rXY^{b-1-r},\qquad 0\le r\le b-1,
\]
the PBW normal-ordering formula gives the four-term column identity
\[
  \mathcal N_{\mathrm{free}}\operatorname{Tr}(W_rM)
  =
  \Theta_r^{(b)}-\Theta_{r+1}^{(b)}
  -\hbar\Phi_r^{(b)}
  +\hbar\Phi_{b-1-r}^{(b)}.       \tag{1}
\]

Proof of (1).  Expand
\[
  \operatorname{Tr}(W_rM)
  =
  \operatorname{Tr}(W_rYX)
  -\operatorname{Tr}(W_rXY)
  +\hbar N\operatorname{Tr}(W_r).
\]
Pair all PBW matchings in the first two trace words which do not see the
adjacent \(YX/XY\) crossing.  The matchings using the adjacent crossing are
cancelled by the scalar term \(\hbar N\operatorname{Tr}(W_r)\), including
their secondary contractions.  Two endpoint families remain.  Contracting
the moving \(X\) against the \(Y\)-block on its left gives
\(-\hbar\Phi_r^{(b)}\); contracting against the reflected block gives
\(+\hbar\Phi_{b-1-r}^{(b)}\).  With no contraction one obtains the
boundary difference \(\Theta_r^{(b)}-\Theta_{r+1}^{(b)}\).  There is no
higher term, since every two-contraction term occurs in one of the paired
families just cancelled.

This is the local PBW telescoping identity.  The coefficient
\(b-1-2r\) is the discrete harmonic weight on the interval of possible
positions of the unique \(X\).

## Target expansion

For \((2,b)\), the Moyal bracket has only the first and third odd terms:
\[
  J_N\!\left(
    \{z_1^3/3,z_2^{b+1}\}_\hbar
  \right)
  =
  (b+1)\operatorname{WeylTr}(X^2Y^b)
  +
  \frac{(b+1)b(b-1)}{12}\hbar^2\operatorname{Tr}(Y^{b-2}).
\]
Counting PBW matchings in the shear sum and in the Weyl average gives
\[
  \mathcal N_{\mathrm{free}}(E_{2,b,N})
  =
  \sum_{r=0}^{\lfloor(b-2)/2\rfloor}
  (b-1-2r)
  \left(
    \Theta_r^{(b)}-\Theta_{r+1}^{(b)}
    -\hbar\Phi_r^{(b)}
    +\hbar\Phi_{b-1-r}^{(b)}
  \right).                         \tag{2}
\]

The count is elementary.

- In contraction degree \(0\), the shear sum contributes \(b+1\) copies
  of \(\Theta_0^{(b)}\).  The Weyl average contributes \(2\) copies of
  each non-middle two-\(X\) cyclic separation and \(1\) copy of the middle
  separation when \(b\) is even.  This gives the coefficients
  \(b-1,-2,\ldots,-2\) and the terminal \(-1\) in the even middle case.
- In contraction degree \(1\), the shear sum contributes
  \(-(b+1)\Phi_s^{(b)}\) for each \(0\le s\le b-1\).  The first Moyal
  Weyl average contributes \(-2(s+1)\Phi_s^{(b)}\) before subtraction.
  Hence the defect coefficient is
  \[
    -(b+1)+2(s+1)=2s-(b-1),
  \]
  which is exactly the antisymmetric half-sum in (2).
- In contraction degree \(2\), the difference between the shear
  double-contraction count and the first Moyal Weyl double-contraction
  count is
  \[
    \frac{(b+1)b(b-1)}{12}\,
    \mathcal N_{\mathrm{free}}\operatorname{Tr}(Y^{b-2}).
  \]
  This is precisely the third Moyal term above, with the same sign after
  subtracting the Moyal bracket.  Thus no \(\hbar^2\) free diagram remains.

Combining (1) and (2) proves the \((2,b)\) edge formula.

The same argument can be written as an induction: subtract the
\((b-1)\)-weighted \(r=0\) column.  It removes the two endpoint diagrams
\(\Theta_0^{(b)}\), \(\Phi_0^{(b)}\), and \(\Phi_{b-1}^{(b)}\), lowers
the remaining linear weight by \(2\), and leaves the same problem with the
next \(Y\)-position.  The process stops when the middle coefficient is
zero for odd \(b\), or when the self-reflected middle column has coefficient
\(1\) for even \(b\).

## The \((a,2)\) edge

The \((a,2)\) calculation is the same one-moving-letter calculation with
the unique \(Y\) moving through an \(X\)-string.  Put
\[
  \widetilde\Theta_s^{(a)}=\mathsf D(X^{a-s}YX^sY),
  \qquad 0\le s\le a,
\]
and
\[
  \widetilde\Phi_s^{(a)}
  =
  \mathsf D(X^{a-1-s})\mid \mathsf D(X^sY),
  \qquad 0\le s\le a-1,
\]
with \(\mathsf D(X^0)=N\).  For
\[
  V_r=X^{a-1-r}YX^r,\qquad 0\le r\le a-1,
\]
the same matching involution gives
\[
  \mathcal N_{\mathrm{free}}\operatorname{Tr}(V_rM)
  =
  \widetilde\Theta_r^{(a)}-\widetilde\Theta_{r+1}^{(a)}
  -\hbar\widetilde\Phi_r^{(a)}
  +\hbar\widetilde\Phi_{a-1-r}^{(a)}.       \tag{3}
\]

The normalization is forced by the Moyal coefficients.  For \((2,a)\), the
first and third Moyal coefficients are
\[
  a+1,\qquad \frac{(a+1)a(a-1)}{12}.
\]
For \((a,2)\), they are
\[
  3,\qquad \frac{a(a-1)}4.
\]
Both are obtained from the \((2,a)\) coefficients by multiplication by
\(3/(a+1)\).  Therefore the target expansion is \(3/(a+1)\) times the
weighted sum of the columns (3), namely
\[
  \mathcal N_{\mathrm{free}}(E_{a,2,N})
  =
  \frac3{a+1}
  \sum_{r=0}^{\lfloor(a-2)/2\rfloor}
  (a-1-2r)
  \mathcal N_{\mathrm{free}}
  \operatorname{Tr}(X^{a-1-r}YX^rM).
\]

## Relation to the script

The script is an exact implementation of the proof objects, not a finite
rank substitute.

- `scripts/quantum_shear_trace_diagram_normal_form.py:276-303` enumerates
  the PBW contraction matchings.
- `scripts/quantum_shear_trace_diagram_normal_form.py:306-339` imposes
  the two Kronecker identifications for each contracted \(Y,X\) pair.
- `scripts/quantum_shear_trace_diagram_normal_form.py:355-360` is exactly
  the column \(\mathcal N_{\mathrm{free}}\operatorname{Tr}(WM)\).
- `scripts/quantum_shear_trace_diagram_normal_form.py:382-396` constructs
  the first and third Moyal terms used in the target expansion.
- `scripts/quantum_shear_trace_diagram_normal_form.py:445-458` implements
  the two edge formulas above.
- `scripts/quantum_shear_trace_diagram_normal_form.py:745-801` checks the
  kernel-correction formulation and verifies that the edge residual and
  correction are both zero in the checked windows.

Agent 191 verified the edge formulas through \(12\) in kernel-correction
mode.  The present pass additionally checked the direct candidate identity
through \(20\).  These computations reflect (1) and (2): each column has
the four-term normal form, and the weighted sum is the target expansion.

## Attacks and residuals

- Edge finite-table attack: healed to a theorem candidate.  The formula is
  no longer just a table; it is the discrete PBW divergence (1) plus the
  target count (2).
- Endpoint attack: healed in the proof sketch.  The scalar
  \(\hbar N\operatorname{Tr}(W_r)\) cancels the adjacent-crossing
  endpoint family and supplies the \(Y^0\) or \(X^0\) isolated-loop
  normalization.
- Third-Moyal attack: healed as a named count.  The only possible
  two-contraction residue equals the order-three Moyal term and cancels.
- Balanced/interior attack: not healed here.  The balanced diagonal and
  non-edge strips still require the associated-graded necklace homotopy or
  a natural left-cokernel vanishing theorem for
  \(\mathcal C_{a,b}|_{\ker\partial}\).  The edge theorem does not imply
  that interior theorem.

Residual before TeX inscription: write the matching-count lemma for the
three target coefficients in the manuscript's notation.  No new
mathematical obstruction appeared for the edge families.

## Commands run

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
# PASS through (2,12) and (12,2); residual_terms=0,
# correction_terms=0, corrected_residual_terms=0 in every edge case.

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --family-only --edge-family-max 20 --progress --max-terms 1
# PASS through (2,20) and (20,2) in direct candidate mode.

python3 scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 2,6 --case 6,2 --max-terms 40
# PASS, representative edge check with three edge columns.
```

Exploratory Python imports of
`scripts/quantum_shear_trace_diagram_normal_form.py` were used to print the
\((2,5)\), \((2,6)\), and \((6,2)\) column normal forms and identify the
four-term identity (1).  They wrote no files.
