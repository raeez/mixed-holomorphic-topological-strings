# Theta3 Restricted-Habitat Counterterm Theorem Design

Date: 2026-04-30

Lane: theta3 restricted-habitat Bianchi-defect counterterm theorem
design.

Ownership: report only.  No TeX edits.

## Verdict

The missing result is not a general Costello theorem and not a CE source
ancestor.  It is a restricted brane-defect Costello local-functional
construction theorem for a genuine nonscalar degree-zero counterterm
\[
  B^M_{02,20}\in Q^0_{\mathrm{ns},M}
\]
whose differential is exactly the Hom-valued Bianchi defect
\[
  d_{\mathrm{ns},M}B^M_{02,20}=-b^M_{02,20}.
\]

At \(M=2\) this must add a new column
\[
  A^2_B=(0,0,-1)^T
\]
in the basis
\((E^2_{\nu_{02}},E^2_{\nu_{20}},b^2_{02,20})\).  The current habitat
only has the lower-source column
\[
  A^2_D=(-2,2,1)^T,
\]
so the residual \(r_2=(2,-2,0)^T\) is blocked by the covector
\[
  \widetilde\lambda
   =\tfrac12(E^2_{\nu_{02}})^*+(b^2_{02,20})^*.
\]
Thus the theorem must construct \(B^M_{02,20}\) as a real local
functional in a controlled enlarged habitat.  It cannot merely rename
the source exactness of
\[
  d_{\mathrm{CE}}\zeta^0_2=2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]

## Anchors Read

- `main.tex`: current theta3 finite-window gate, lower-source primitive,
  Bianchi defect, cokernel obstruction, and transport/Roos clauses.
- `theorem-lanes.tex`, `open-obligations.tex`,
  `claim-strength-ledger.tex`: duplicated theta3 row surface and claim
  strength.
- `tate-P1-hadamard-mittag-leffler.tex`: finite-row obstruction,
  payload acceptance gate, companion-face obstruction, and source-face
  transport failures.
- `appendix-unreduced-bv-qme.tex`: native finite-window realization
  habitat and constructive nonscalar Costello QME criterion.
- `appendix-factorization-current-conventions.tex`: regular-density and
  wavefront-admissible current habitats.
- `tate-T1-weighted-completion.tex`: nonscalar inverse-limit
  counterterm criterion and Roos obstruction.
- Reconstitution reports on Costello source theorem search, local
  functional habitat, theta3 B-column construction, Bianchi closure,
  matrix integration, companion faces, non-diagonal transport, and Roos
  obstruction.
- Primary-source anchor reports for Costello graph/QME local
  functionals and H\"ormander wavefront operations.

## Exact Theorem Needed

### Theorem: restricted-habitat Bianchi-defect counterterm

Fix a compact interval \(I\), an admissible weight \(w\), and finite
windows \(M\ge 2\).  Let
\[
  (Q^\bullet_{\mathcal G^B,\Lambda,M}(I),d_M)
\]
be a native finite-window brane-defect local-functional Costello habitat
with
\[
  d_M=Q+\{I^w_0,-\},
\]
completed in the same \(\hbar\)-, scalar-contact-, and finite-window
filtration as the theta3 row.  Let
\[
  \sigma_{\mathrm{sc},M}\colon
  Q^\bullet_{\mathcal G^B,\Lambda,M}(I)\to
  Q^\bullet_{\mathrm{sc},M}(I)
\]
be a filtered chain scalar projection, and put
\[
  Q^\bullet_{\mathrm{ns},M}(I)=\ker\sigma_{\mathrm{sc},M}.
\]

Assume the marked finite graph package, restricted coefficient habitat,
renormalized local extension estimates, and transport data listed below.
Then there exists a family of degree-zero local counterterms
\[
  B^M_{02,20}\in Q^0_{\mathrm{ns},M}(I)
\]
such that:

1. Differential:
   \[
     d_{\mathrm{ns},M}B^M_{02,20}=-b^M_{02,20}.
   \]

2. \(M=2\) row coordinate:
   \[
     A^2_B=(0,0,-1)^T
   \]
   in the ordered basis
   \[
     (E^2_{\nu_{02}},E^2_{\nu_{20}},b^2_{02,20}).
   \]
   Equivalently, the corrected lower primitive satisfies
   \[
     d_{\mathrm{ns},2}(D^2_{02,20}+B^2_{02,20})
       =-2E^2_{\nu_{02}}+2E^2_{\nu_{20}}.
   \]

3. No scalar leakage:
   \[
     \sigma_{\mathrm{sc},M}(B^M_{02,20})=0.
   \]
   Since \(\sigma_{\mathrm{sc},M}\) is a chain map, this also forces
   \(\sigma_{\mathrm{sc},M}(b^M_{02,20})=0\); it should be proved, not
   separately assumed, in a constructive theorem.

4. Locality:
   \(B^M_{02,20}\) is a Costello local counterterm supported on the
   allowed collision and source-face strata, with the normal-derivative
   delta form specified in the analytic clause below.

5. Tower compatibility:
   the family satisfies the finite-window, interval, and weight transport
   identities up to the Roos correction clause below.  In the strict
   transport case,
   \[
     \pi_{M,N}B^M_{02,20}=B^N_{02,20}.
   \]

## Nonredundant Hypotheses And Proof Obligations

The theorem should use exactly the following hypotheses/proof
obligations.  Items marked "prove inside" are not independent assumptions
if the theorem is stated as a construction theorem.

### H0. Native finite-window habitat

For every \(M\ge 2\), the complex
\[
  Q^\bullet_{\mathcal G^B,\Lambda,M}(I)
\]
is a completed local-functional habitat for the local mixed
holomorphic-topological theory on
\(\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}\), not a
curve chiral algebra and not a compact Calabi-Yau BCOV complex.

It must contain the theta3 seed graph, the two lower faces
\(\nu_{02},\nu_{20}\), the lower source primitive, and the new
Bianchi-defect counterterm generator.  The differential is
\[
  d_M=Q+\{I^w_0,-\}
\]
and preserves the finite-window filtration, scalar-contact filtration,
and admissible weight filtration.

This is nonredundant: Costello's abstract local functional complex alone
does not identify the brane-defect current habitat or the theta3
finite-window truncations.

### H1. Marked theta3 Bianchi row data

The marked graph package must supply, for every relevant \(M\),

- degree-one rows \(E^M_{\nu_{02}}\), \(E^M_{\nu_{20}}\), and
  \(b^M_{02,20}\);
- the lower source primitive \(\zeta^0_M\) and its source differential;
- the Hom kernel operator \(K^M_{\Theta_3}\) on the marked lower source;
- the lower local functional
  \[
    D^M_{02,20}=K^M_{\Theta_3}(\zeta^0_M)
  \]
  whenever the lower source primitive is used;
- the Bianchi-defect identity
  \[
    b^M_{02,20}
      =d_{\mathrm{ns},M}K^M_{\Theta_3}(\zeta^0_M)
       -K^M_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_M).
  \]

At \(M=2\), the row calculation must be
\[
  d_{\mathrm{ns},2}D^2_{02,20}
    =-2E^2_{\nu_{02}}+2E^2_{\nu_{20}}+b^2_{02,20}.
\]

This hypothesis is nonredundant because the source exactness only
computes the two \(E\)-terms.  The Hom-valued defect \(b\) is the
remaining obstruction.

### H2. Codimension-two closure

The marked theta3 list must be codimension-two closed in the enlarged
package: all faces created by applying \(d_M\), the source differential,
and the Hom kernel differential to the theta3/lower-source data must be
present with their signs and weights.  This gives
\[
  d_M b^M_{02,20}=0
\]
inside \(Q^1_{\mathrm{ns},M}\).

This can be proved from the full marked graph table; it must not be
assumed from an incomplete eight-face table.  Without closure, the target
of \(dB=-b\) is not even known to be a cocycle.

### H3. Restricted coefficient habitat

The theorem must choose one of the following restricted habitats.

1. Regular-density branch:
   every external defect coefficient used by the \(B\)-graphs lies in
   \[
     \mathcal D^{\mathrm{reg}}_c(I)
   \]
   and is represented by a compactly supported smooth density
   \(b(t)\,dt\).

2. Wavefront branch:
   for each marked graph \((\Gamma,M)\), the external coefficients lie
   in a fixed graphwise wavefront-admissible class
   \[
     \mathcal D'_{c,\Lambda,\mathrm{fs}}(I;\Gamma,M),
   \]
   preferably a one-sided sign-conic finite-scaling class so that the
   habitat is linear.

No theorem may quantify over all of \(\mathcal D'_c(I)\).  That stronger
claim is false for the available product/pullback operations.

This hypothesis is nonredundant: it is exactly what makes the
bulk-to-defect graph distributions and counterterms defined.

### H4. Wavefront and locality estimates

For every graph \(\Gamma\), window \(M\), scale pair \(0<\epsilon<L\),
and coefficient tuple occurring in \(B^M_{02,20}\), write
\[
  e_\Gamma\colon X_\Gamma\to I^k
\]
for the incidence map and \(K^M_{\Gamma,\alpha;\epsilon,L}\) for the
finite-scale bulk-to-defect graph distribution.  The theorem must prove
or assume the following estimates for each term.

1. Pullback non-characteristic:
   \[
     N_{e_\Gamma}\cap
     \operatorname{WF}(B_1\boxtimes\cdots\boxtimes B_k)=\varnothing.
   \]
   Hence \(e_\Gamma^*(B_1\boxtimes\cdots\boxtimes B_k)\) is defined with
   the standard wavefront bound.

2. Product transversality:
   \[
     \bigl(
       \operatorname{WF}(K^M_{\Gamma,\alpha;\epsilon,L})
       +\operatorname{WF}(e_\Gamma^*B^{\boxtimes})
     \bigr)\cap 0=\varnothing.
   \]
   Hence the product
   \[
     K^M_{\Gamma,\alpha;\epsilon,L}\cdot e_\Gamma^*B^{\boxtimes}
   \]
   is defined.

3. Finite scaling degree:
   for every collision or source-face diagonal \(\Delta\),
   \[
     \operatorname{sd}_\Delta
     \bigl(K^M_{\Gamma,\alpha;\epsilon,L}\cdot
       e_\Gamma^*B^{\boxtimes}\bigr)<\infty.
   \]
   If \(c_\Delta\) is the real codimension of \(\Delta\), extension
   ambiguities have order
   \[
     N_{\Gamma,\alpha,\Delta}
       =\max\{-1,\lfloor
          \operatorname{sd}_\Delta-c_\Delta\rfloor\}.
   \]

4. Local extension form:
   differences of two allowed extensions are finite sums
   \[
     \sum_{|\beta|\le N_{\Gamma,\alpha,\Delta}}
       \partial_\nu^\beta\delta_\Delta\otimes
       S_{\Gamma,\alpha,\Delta,\beta},
   \]
   supported on
   \[
     \Delta\cap\operatorname{supp}(e_\Gamma^*B^{\boxtimes}).
   \]
   The counterterm \(B^M_{02,20}\) must be one such local extension
   ambiguity, or a finite linear combination of such ambiguities, in
   degree zero.

5. Pushforward wavefront bound:
   after integration along graph configuration fibers, the pushed-forward
   distribution has wavefront contained in the declared brane-defect
   local-functional target.  In particular it remains inside the chosen
   regular-density or wavefront-admissible restricted habitat.

6. Scale asymptotics:
   the small-\(\epsilon\) expansion of the graph weight admits local
   counterterms of the above form, with finite order along each allowed
   stratum and no new nonlocal support.

These are analytic proof obligations.  H\"ormander's pullback/product
theorems justify the operations after the wavefront hypotheses are
verified; they do not verify the graph-specific hypotheses or construct
\(B\).

### H5. Scalar-zero chain projection

The enlarged habitat must carry a filtered chain projection
\[
  \sigma_{\mathrm{sc},M}\colon Q^\bullet_{\mathcal G^B,\Lambda,M}
    \to Q^\bullet_{\mathrm{sc},M}
\]
with
\[
  \sigma_{\mathrm{sc},M}d_M=d_{\mathrm{sc},M}\sigma_{\mathrm{sc},M}.
\]
It must commute with finite-window projection, interval extension by
zero, and weight transport:
\[
  \sigma_{\mathrm{sc},N}\pi_{M,N}
    =\pi^{\mathrm{sc}}_{M,N}\sigma_{\mathrm{sc},M},
\]
and similarly for interval and weight maps.

The counterterm is required to land in
\[
  Q^0_{\mathrm{ns},M}=\ker\sigma_{\mathrm{sc},M}.
\]
Do not state both "\(B\in Q_{\mathrm{ns}}\)" and
"\(\sigma_{\mathrm{sc}}(B)=0\)" as separate assumptions; they are the
same condition.  The theorem should conclude this condition for the
constructed \(B\).  Then \(\sigma_{\mathrm{sc}}(b)=0\) follows from the
differential identity.

### H6. Row-coordinate exactness computation

The proof must compute the \(M=2\) row in the ordered basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},b^2_{02,20})
\]
and show
\[
  d_{\mathrm{ns},2}B^2_{02,20}=-b^2_{02,20}.
\]
Equivalently, the column of \(B\) is
\[
  (0,0,-1)^T.
\]

The zero entries in the two \(E\)-coordinates are load-bearing.  A
counterterm with column \((a,b,-1)^T\) for \(a\ne0\) or \(b\ne0\) does
not repair the stated lower-source residual unless a further compensating
column is also constructed.

This clause is a proof obligation, not an independent hypothesis.

### H7. Window, interval, and weight transport

For \(M\ge N\), let
\[
  \pi_{M,N}\colon Q^\bullet_{\mathcal G^B,\Lambda,M}
     \to Q^\bullet_{\mathcal G^B,\Lambda,N}
\]
be the finite-window projection.  The marked graph data, local
extensions, scalar projection, and counterterms must be compatible with
\(\pi_{M,N}\), interval extension by zero \(j_*\), and weight transport
\(R_{w,w'}\).  At the counterterm level this means identities of the
form
\[
  \pi_{M,N}C^M_{\Gamma,w} = C^N_{\pi\Gamma,w}\pi_{M,N}^{\mathrm{src}},
\]
\[
  j_*C^I_{\Gamma,w}=C^J_{\Gamma,w}j_*,
\]
and
\[
  R_{w,w'}C^M_{\Gamma,w}
     =C^M_{\Gamma,w'}R^{\mathrm{src}}_{w,w'}.
\]

If transport is strict, then
\[
  \pi_{M,N}b^M_{02,20}=b^N_{02,20},
  \qquad
  \pi_{M,N}B^M_{02,20}=B^N_{02,20}.
\]

If transport is not strict, define the degree-one transport defect
\[
  \Delta^1_{M,N}
    =-\pi_{M,N}b^M_{02,20}+b^N_{02,20}.
\]
The theorem must supply a degree-zero correction
\[
  H^{M,N}_{02,20}\in Q^0_{\mathrm{ns},N}
\]
with
\[
  d_{\mathrm{ns},N}H^{M,N}_{02,20}=\Delta^1_{M,N}.
\]
Then
\[
  \Delta^0_{M,N}
   =\pi_{M,N}B^M_{02,20}
     -B^N_{02,20}-H^{M,N}_{02,20}
\]
is a closed degree-zero Roos cochain.  Its class in the Roos
\(\lim^1 H^0(Q^\bullet_{\mathrm{ns},M})\) group must vanish.

This transport/Roos clause is nonredundant unless strict transport and
\[
  H^0(Q^\bullet_{\mathrm{ns},M})=0
\]
are both proved in the enlarged package.  In the minimal free matrix
model with columns \(A_D=(-2,2,1)^T\) and \(A_B=(0,0,-1)^T\), this
amounts to proving the relevant kernel is zero; in the actual graph
habitat it must be checked, not inferred from the toy matrix.

### H8. No alternative-route assumptions

The \(B\)-counterterm theorem must not assume any of the following unless
it is explicitly changing lanes:

- a direct theta3 primitive \(C_{\Theta_3}\) with \(dC_{\Theta_3}=-E\);
- equality \(E_{\nu_{02}}=E_{\nu_{20}}\);
- a full companion-face table with non-diagonal \(v\)-matrices;
- an all-\(\mathcal D'_c(I)\) current theorem;
- a compact Calabi-Yau BCOV comparison theorem;
- Costello-Li open-closed oddness as a replacement for the local
  brane-defect row computation.

These are distinct repair routes or false generalizations.  They are not
hypotheses for the restricted Bianchi-defect counterterm theorem.

## Minimal Statement For Insertion Later

The following is the compact theorem surface the manuscript needs once
the construction data are available.

> Theorem (restricted theta3 Bianchi-defect counterterm).  In the native
> mixed holomorphic-topological finite-window Costello habitat
> \(Q^\bullet_{\mathcal G^B,\Lambda,M}(I)\), assume the marked theta3
> Bianchi package is codimension-two closed, the defect labels lie either
> in the regular-density class or in the declared graphwise
> wavefront-admissible finite-scaling class, the graph kernels satisfy the
> pullback, product, finite-scaling, local-extension, and pushforward
> estimates above, and the scalar projection and counterterm extensions
> commute with finite-window, interval, and weight transport.  Then there
> are local degree-zero counterterms
> \(B^M_{02,20}\in Q^0_{\mathrm{ns},M}(I)\), supported on the allowed
> collision/source-face strata, such that
> \[
>   d_{\mathrm{ns},M}B^M_{02,20}=-b^M_{02,20}.
> \]
> At \(M=2\), the corresponding row column is
> \((0,0,-1)^T\) in the basis
> \((E^2_{\nu_{02}},E^2_{\nu_{20}},b^2_{02,20})\).  The family is
> strictly compatible with finite-window, interval, and weight transport;
> or, in the non-strict case, the degree-one transport defect is killed
> by \(H^{M,N}_{02,20}\) and the resulting degree-zero Roos class in
> \(\lim^1 H^0\) vanishes.

This statement is exact but not yet proved by the current sources or
reports.

## Redundancies Removed

1. Do not require both \(B\in Q_{\mathrm{ns}}\) and
   \(\sigma_{\mathrm{sc}}(B)=0\).  They are identical once
   \(Q_{\mathrm{ns}}\) is defined as the scalar kernel.

2. Do not separately assume \(\sigma_{\mathrm{sc}}(b)=0\) if the theorem
   constructs \(B\in Q_{\mathrm{ns}}\) with \(dB=-b\).  It follows from
   the chain projection.  If the theorem is only an abstract criterion,
   then \(\sigma_{\mathrm{sc}}(b)=0\) must be an input.

3. Do not require both \(dB=-b\) and \(A_B=(0,0,-1)^T\) as independent
   hypotheses.  The latter is the \(M=2\) coordinate verification of the
   former.

4. Do not require \(\lim^1H^0=0\) if strict transport is proved and the
   relevant \(H^0\) vanishes.  Otherwise the Roos vanishing clause is
   mandatory.

5. Do not import the direct theta3 primitive, CE ancestor, or companion
   face table as assumptions.  They are separate repair mechanisms.

6. Do not ask for all compactly supported currents.  Regular densities
   or graphwise wavefront-admissible finite-scaling currents are the
   maximal defensible habitats from the current evidence.

## Missing Data

The theorem design names the following missing inputs.

1. A concrete marked graph/counterterm formula for
   \(B^M_{02,20}\), not just a formal new basis vector.

2. The incidence maps, graph weights, scale kernels, and source-face
   labels for the \(B\)-graphs.

3. The graph-specific wavefront verification:
   pullback non-characteristic condition, product transversality, finite
   scaling degree along every collision/source-face diagonal, and
   pushforward target bound.

4. The local extension order and explicit normal-derivative delta
   counterterm formula for each relevant stratum.

5. The scalar projection on the enlarged \(B\)-habitat and the proof
   that the constructed \(B\) has scalar image zero.

6. The row-coordinate calculation proving no extra
   \(E_{\nu_{02}}\) or \(E_{\nu_{20}}\) terms appear in
   \(dB=-b\).

7. The finite-window transport matrices for \(b\) and \(B\), or the
   correction cochains \(H^{M,N}\).

8. The Roos class computation, unless strict transport plus
   \(H^0=0\) is proved in the actual graph habitat.

9. Primary-source-grade analytic anchors for any H\"ormander
   pushforward or extension theorem cited beyond the standard
   pullback/product criteria.

## Claim Status

Design complete.  Construction not complete.

Current manuscript data prove the obstruction and identify the required
column.  They do not yet construct a local functional
\(B^M_{02,20}\).  The next attack-heal target is the concrete marked
counterterm package satisfying H0-H7 above.
