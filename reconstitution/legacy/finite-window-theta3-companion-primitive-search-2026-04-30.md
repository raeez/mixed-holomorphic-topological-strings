# Finite-Window Theta3 Companion Primitive Search

Scope.  Read-only evidence: `tate-P1-hadamard-mittag-leffler.tex`,
`scripts/finite_window_graph_array.py`, the 09:57 critique plan, and Agent
187's finite-row report.  Writable surface: this note and the Agent 193
report only.

## Object Under Attack

The current one-row order-three package contains the CE-source row
`theta_3=CE(Theta_3,nu_3)`.  In the row notation already present in
`tate-P1-hadamard-mittag-leffler.tex`, its supplied data are:

- graph type `CE`, order `|theta_3|_hbar=3`;
- source coefficient `d_CE zeta_M = + zeta_{M,nu_3} + other faces`;
- row incidence in `-kappa(d_CE zeta_M)` equal to `-1`;
- row value
  \[
    R^{row}_{theta_3,M}
      =
    -K^M_{Theta_3}(zeta_{M,nu_3})
      =: E_{theta_3,M};
  \]
- scalar gate zero in the full-equivariant marked habitat, also supported
  by the displayed Weyl scalar contact `omega(z_1^2,z_2)=0`;
- truncation
  \[
    pi_{M,N}E_{theta_3,M}=E_{theta_3,N}\quad(N>=3),
    \qquad pi_{M,N}E_{theta_3,M}=0\quad(N<3).
  \]

Agent 187's finite row complex is
\[
  K^0_{theta_3,M}=0,\qquad
  K^1_{theta_3,M}=C E_{theta_3,M},\qquad d=0.
\]
That proves a finite-row obstruction only for the displayed one-row
subcomplex.  It does not prove that `E_{theta_3,M}` is non-exact in the
larger local-functional complex.

## Sign Calculation

The residual vector is `r=(1)` in the basis `E_{theta_3}`.  A primitive
candidate `C_{theta_3,M}` must satisfy
\[
  d_{ns,M}C_{theta_3,M}=-E_{theta_3,M}
    =
  K^M_{Theta_3}(zeta_{M,nu_3}).
\]
Equivalently, in the finite primitive-search matrix,
\[
  A^M_{E,C}=-1,\qquad A^M c=-r^M
\]
is solved by `c=1`.

Thus the sign is fixed.  Any proposed companion row with
`d C = +E_{theta_3}` has the wrong sign.  Any proposed row with
`d C = -E_{theta_3} + F` is a valid primitive only after `F` is included in
the degree-one row basis and its residual coefficient is canceled.

## Candidate A: CE-Ancestor Primitive

The most economical Hom-valued construction would add a labelled source
ancestor
\[
  eta_{theta_3,M}
    \in C^\bullet_{CE,lab}(G_M)
\]
with
\[
  d_{CE}eta_{theta_3,M}=zeta_{M,nu_3}
\]
and define
\[
  C^{CE}_{theta_3,M}
    =
  K^M_{Theta_3}(eta_{theta_3,M}).
\]
For a degree-zero kernel,
\[
  d_K K(eta)
    =
  d_MK(eta)-K(d_{CE}eta).
\]
If the Hom-valued Bianchi term `d_K K(eta_{theta_3,M})` is zero on this
ancestor, or if its target-differential and bracket faces are separately
included and canceled, then
\[
  d_M C^{CE}_{theta_3,M}
    =
  K^M_{Theta_3}(zeta_{M,nu_3})
    =
  -E_{theta_3,M}.
\]
This would heal the fixed-window obstruction with the correct sign.

Necessary row labels for this construction:

- primitive label: `C_theta_3^CE = K_Theta_3(eta_theta_3)`;
- graph label: the same genuine marked seed `Theta_3`;
- source label: `eta_theta_3` with `d_CE eta_theta_3 = +zeta_{nu_3}`;
- order: `|Theta_3|_hbar=3`;
- finite degree: `d_max=3`, because the row uses the displayed degree-three
  label `h_{2,1}=z_1^2 z_2`;
- external labels: `u_{a(t)dt tensor z_1^2}`,
  `u_{b(t)dt tensor z_2}`, and `c_{B_theta,rho_{2,1}}`;
- edge labels inherited from the theta row:
  `P^{w,M}_{epsilon,L}` with `(h_{2,1},rho_{2,1})`,
  `Delta^{w,M}_{epsilon,L}` with `(h_{1,1},rho_{1,1})`, and the boundary
  Weyl edge with `(z_1^2,z_2)`;
- marker: the same full `gl(N|N)`-equivariant signed Brauer marker
  `m_{theta_3}` with cyclic supertrace zero;
- scalar condition: `sigma_sc(C_theta_3^CE)=0`, not merely
  `sigma_sc(dC_theta_3^CE)=0`;
- boundary matrix entry: `A_{E_theta_3,C_theta_3^CE}=-1`;
- all additional `d_MK(eta)` or bracket faces either vanish, are absent by
  a proved Bianchi identity on the ancestor, or appear as explicit
  companion degree-one rows with matching residual coefficients.

Attack.  The current data do not supply `eta_{theta_3,M}`.  They also do
not supply the target-differential and bracket faces needed to verify
`d_K K(eta)=0`.  Therefore this is a valid healing shape, not a current
construction.

## Candidate B: Local Counterterm Primitive

A direct Costello counterterm heal would add a degree-zero local functional
\[
  C^{ct}_{theta_3,M}\in K^0_{ns,M}(I)
\]
with the same external labels and marker habitat as the theta row and with
\[
  d_{ns,M}C^{ct}_{theta_3,M}
    =
  K^M_{Theta_3}(zeta_{M,nu_3})
    =
  -E_{theta_3,M}.
\]
In row-array language this is a primitive candidate row, not another
degree-one residual row.  It becomes an order-three lower-counterterm
entry in the next QME residual after it is chosen.

Necessary data:

- primitive basis label: `C_theta_3^ct`;
- local counterterm vertex label:
  `C^M_{Theta_3,nu_3,w}(epsilon;B^Theta_bullet)`;
- hbar order: `3`;
- coefficient window: `d_max=3`, killed below windows `N<3`;
- target differential expansion:
  \[
    d_{ns,M}C^ct_{theta_3,M}
      =
    -E_{theta_3,M}
  \]
  with no undeclared degree-one summands;
- scalar condition:
  \[
    sigma_sc(C^ct_{theta_3,M})=0.
  \]
  In the full-equivariant branch this follows only if the counterterm
  itself is placed in the same full marked habitat.  Otherwise its scalar
  projection must be computed;
- primitive transport:
  \[
    P^{M,N}_{C,C}=1\quad(N>=3),\qquad P^{M,N}_{C,C}=0\quad(N<3),
  \]
  and all off-diagonal primitive transport entries zero unless a larger
  primitive basis is declared.

Attack.  The present finite-window package names positive graph weights and
formal local counterterm vertices as possible labels, but it does not give
this particular counterterm functional or its differential.  A symbolic
name `C_theta_3` alone is not admissible evidence.

## Candidate C: Companion CE Faces Changing The Residual

The source decomposition in the theta row is written
\[
  d_{CE}zeta_M=+zeta_{M,nu_3}+other faces.
\]
Instead of finding a degree-zero primitive, one could restore the complete
CE-source face table.  If the omitted faces `nu` are supplied with signs
`epsilon^{CE}_{Theta_3,nu}` and their row values satisfy
\[
  \sum_\nu
    -epsilon^{CE}_{Theta_3,nu}
      K^M_{Theta_3}(zeta_{M,nu})
    =
  0,
\]
then the residual changes from the one-row vector `E_theta_3` to zero.

This is a real heal only when the finite source table is complete.  It is
not a degree-zero primitive.  It is a replacement of the one-row complex by
a larger degree-one row presentation.

Necessary data:

- all source faces in `d_CE zeta_M`, not just `nu_3`;
- CE signs and Koszul coefficients;
- coordinate expressions of every
  `K^M_{Theta_3}(zeta_{M,nu})` in the lower-window row basis;
- scalar gates for every companion face;
- source-face truncation matrix `v^{M,N}`;
- proof that the total source-face row sum is closed and scalar-zero.

Attack.  The current one-row package intentionally omits the other faces.
No equality with `-E_theta_3` is available.  This route is open but not
constructed.

## Truncation And Roos Gate For A Genuine Primitive

If either Candidate A or Candidate B supplies a single primitive
`C_{theta_3,M}` with `dC=-E`, the fixed-window and tower checks are:
\[
  A_M=(-1),\qquad r_M=(1),\qquad c_M=(1).
\]
For `M>=N>=3`,
\[
  T^{M,N}_{E,E}=1,\qquad P^{M,N}_{C,C}=1,
\]
so
\[
  T^{M,N}A^M=A^NP^{M,N}.
\]
For `N<3`, both the theta row and the primitive row are absent; all
entries are zero.  The chosen solutions satisfy
\[
  P^{M,N}c_M-c_N=0.
\]
Hence the Roos `lim^1` class is zero.

If instead
\[
  pi_{M,N}C_{theta_3,M}=C_{theta_3,N}+h_{M,N},
\]
with `h_{M,N}` closed of degree zero, then the fixed-window obstruction is
healed but the remaining obstruction is the Roos class
\[
  [h_{M,N}]\in H^0(K^\bullet_{ns,N}(I)).
\]
The script must report this as a tower failure, not as a fixed-window
failure.

## Verdict

No construction is possible from the current data.  The one-row obstruction
stands exactly as Agent 187 stated: it is a nonzero class in the displayed
finite row subcomplex.  Supremum discipline improves the residual by naming
the minimal missing object:

1. either a CE-source ancestor `eta_{theta_3}` for which
   `K_Theta_3(eta_{theta_3})` has boundary `-E_theta_3`, with all Bianchi
   companion faces supplied;
2. or a local counterterm primitive `C^ct_{theta_3}` with explicit
   differential `dC=-E`;
3. or a complete CE companion-face table whose total degree-one residual
   is zero.

The current manuscript and script contain only the hypothetical interface
case `theta_3_with_supplied_candidate_C_theta_3`; they do not supply any of
these mathematical data.

## Executable Script Spec

Future edits to `scripts/finite_window_graph_array.py` should add no
numerical claim until the row data above exist.  The next executable layer
should be:

1. Add a `PrimitiveCandidateRow` record with fields:
   `row_label`, `source`, `hbar_order`, `coefficient_window_degree`,
   `external_labels`, `edge_labels`, `marker_tensor`, `scalar_projection`,
   `differential_entries`, `primitive_transport`, and `status`.
2. Add a CE-ancestor case guarded by booleans:
   `source_ancestor_verified`, `extra_faces_closed`, `scalar_zero`,
   `truncation_verified`.
   When all are true, feed
   `degree_zero_basis=("C_theta_3_CE",)`,
   `degree_one_basis=("E_theta_3",)`,
   `differential_entries=(("C_theta_3_CE","E_theta_3",-1),)`,
   `residual_entries=(("E_theta_3",1),)`.
3. Add a counterterm case with the same matrix entries but require an
   explicit string or coordinate payload for
   `d_ns C_theta_3_ct = -E_theta_3`.
4. Add a companion-face cancellation case with degree-zero basis empty and
   degree-one basis all CE faces.  It passes only if the residual coordinate
   vector is zero after summing supplied signs.
5. Add a transport check:
   `T*r_M == r_N` and `T*A_M == A_N*P`.
6. Add a Roos check on a chosen solution family:
   report zero when `P*c_M-c_N=0`; otherwise emit the closed degree-zero
   difference as the `lim^1` representative.
7. Add negative tests:
   missing source ancestor, undeclared extra Bianchi face, scalar projection
   not zero, and truncation mismatch.  These must return `invalid primitive
   datum`, not `primitive_exists=true`.

No script edit was made in this pass.
