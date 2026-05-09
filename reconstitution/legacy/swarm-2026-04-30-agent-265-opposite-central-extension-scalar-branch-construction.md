# Agent 265 - Opposite Central-Extension Scalar Branch Construction

Agent 265 report.  Worktree: `/Users/raeez/topological-strings`.
Status: report-only.  No manuscript TeX, script, bibliography, source
fixture, figure, or build artifact was edited.

Owned files:

- `reconstitution/opposite-central-extension-scalar-branch-construction-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-265-opposite-central-extension-scalar-branch-construction.md`

## Claim Constructed

There is a theorem-grade scalar repair in the source-replacement category.
It is not a same-branch Costello-local closed exchange.

Let
\[
  A=\mathbb C[z_1,z_2],\qquad
  \bar A=A/\mathbb C\cdot 1,\qquad
  \bar c(f,g)=[\{f,g\}]_0 ,
\]
with
\[
  \{f,g\}=\partial_{z_1}f\,\partial_{z_2}g
  -\partial_{z_2}f\,\partial_{z_1}g .
\]
For \(N>0\), define the opposite scalar central extension
\[
  \bar A^{\mathrm{cl}}_{-\hbar N\bar c}
  =
  \bar A\oplus \mathbb C[[\hbar]]K_{\mathrm{cl}}
\]
by
\[
  [(f,aK_{\mathrm{cl}}),(g,bK_{\mathrm{cl}})]
  =
  \bigl(\{f,g\}_{\bar A},
  -\hbar N\,\bar c(f,g)K_{\mathrm{cl}}\bigr),
  \qquad [K_{\mathrm{cl}},-]=0 .
\]
Let \(k^\vee\) be the central linear cochain
\[
  k^\vee(K_{\mathrm{cl}})=1,\qquad k^\vee(\bar A)=0 .
\]
With the manuscript convention
\[
  (d_{\mathrm{CE}}\lambda)(x,y)=-\lambda([x,y]),
\]
one has
\[
  d_{\mathrm{CE}}k^\vee=\hbar N\,\bar c,\qquad
  d_{\mathrm{CE}}(-k^\vee)=-\hbar N\,\bar c .
\]
Thus the ordinary scalar QME class
\[
  \operatorname{Ob}_{\mathrm{sc}}=\hbar N\bar c
\]
is exact after replacing the source by
\(\bar A^{\mathrm{cl}}_{-\hbar N\bar c}\):
\[
  \operatorname{Ob}_{\mathrm{sc}}+d_{\mathrm{CE}}(-k^\vee)=0 .
\]
Equivalently, the source central character
\[
  J_{\mathrm{op}}=-k^\vee,\qquad J_{\mathrm{op}}(K_{\mathrm{cl}})=-1,
\]
is the one-cochain whose CE differential cancels the scalar class.

This kills the scalar class before scalar reduction because the central line
is kept in the source.  Pushing back to \(\bar A\) or forgetting
\(K_{\mathrm{cl}}\) restores the nonzero class \(\hbar N[\bar c]\).

## Verified Local Anchors

- `main.tex:423-492`: definition of \(\omega=\bar c\), cocycle, and
  non-exactness on \(\bar A\), detected at \(z_1,z_2\).
- `main.tex:7577-7705`: scalar QME obstruction branches, algebraic
  central-contact cone, and same-branch Costello-local criterion.
- `appendix-unreduced-bv-qme.tex:53-133`: formal-local scalar geometry,
  \(\Omega_{\mathrm{loc}}=dz_1\wedge dz_2\), and
  \(\omega(z_1,z_2)=1\).
- `appendix-unreduced-bv-qme.tex:185-305`: scalar-contact chain-lift
  obstruction, with first ordinary branch evaluation
  \(\hbar N\omega(f,g)\gamma_{\mathbf 1}\).
- `appendix-unreduced-bv-qme.tex:560-589`: unreduced primitive
  \(\eta(f)=-[f]_0\), \(d_{\mathrm{CE}}\eta=\omega\), and non-descent to
  \(\bar A\).
- `appendix-unreduced-bv-qme.tex:591-685`: scalar contact QME class
  \(\hbar N[\bar c]\) and the no-internal-counterterm result on the
  scalar-reduced source.
- `appendix-unreduced-bv-qme.tex:687-770`: central-character source
  replacement with \(\chi_N(f)=N[f]_0\) and
  \(\hbar N\omega+d_{\mathrm{CE}}(\hbar\chi_N)=0\).
- `appendix-unreduced-bv-qme.tex:2142-2232`: native finite-window
  Costello/QME habitat, Hom differential, source-face term, and scalar
  projection requirement.
- `appendix-unreduced-bv-qme.tex:2387-2485`: current scalar-zero rows and
  the first certified non-scalar \(\theta_3\) obstruction.
- `local-dictionary.tex:83-97`: abstract BV pairing and warning that it is
  not a Costello coefficient coevaluation kernel without convergent Casimir
  data.
- `local-dictionary.tex:829-1050`: scalar-contact projection, non-scalar
  kernel, curvature, finite-window residuals, and \(\theta_3\) dictionary.
- `tate-T1-weighted-completion.tex:66-115`: Costello coefficient kernel
  requirements.
- `tate-T1-weighted-completion.tex:1329-1518`: regular-density
  closed-exchange tower, inclusion map \(\Xi^{\mathrm{reg}}\), and raw
  kernel cochain obstruction.
- `tate-T1-weighted-completion.tex:1526-1741`: fixed-window image
  criterion and inverse-limit \(\beta,\mu,\lambda\) obstruction classes.
- `scripts/finite_window_graph_array.py:1474-1562`: \(\theta_3\) companion
  candidate rejection, scalar-zero check, lower-window transport residual,
  and missing marked Costello incidence table.

## CE Differential And Signs

For \(L=\bar A^{\mathrm{cl}}_{-\hbar N\bar c}\), the CE differential on a
linear cochain \(\lambda\in L^\vee\) is
\[
  (d_{\mathrm{CE}}\lambda)(x,y)=-\lambda([x,y]).
\]
If \(\ell\in\bar A^\vee\) is pulled back to \(L^\vee\), then
\[
  d_L\ell((f,aK),(g,bK))
  =
  -\ell(\{f,g\}_{\bar A})
  =
  d_{\bar A}\ell(f,g).
\]
The central cochain satisfies
\[
  d_L k^\vee((f,aK),(g,bK))
  =
  -k^\vee(\{f,g\}_{\bar A},-\hbar N\bar c(f,g)K)
  =
  \hbar N\bar c(f,g).
\]
Thus
\[
  d_LJ_{\mathrm{op}}=-\hbar N\bar c,\qquad
  J_{\mathrm{op}}=-k^\vee .
\]
On the test pair
\[
  \bar c(z_1,z_2)=1,\qquad
  \{z_1,z_2\}_{\bar A}=0,
\]
hence
\[
  d_LJ_{\mathrm{op}}(z_1,z_2)=-\hbar N .
\]
This cancels
\[
  \operatorname{Ob}_{\mathrm{sc}}(z_1,z_2)=\hbar N .
\]

The same calculation proves why the repair is impossible inside the reduced
source.  If \(\bar c=d_{\mathrm{CE}}\xi\) on \(\bar A\), then
\[
  1=\bar c(z_1,z_2)
  =
  (d_{\mathrm{CE}}\xi)(z_1,z_2)
  =
  -\xi(\{z_1,z_2\}_{\bar A})
  =
  -\xi(0)=0 .
\]
Therefore \([\bar c]\ne0\) on \(\bar A\).  The new primitive is the central
cochain \(J_{\mathrm{op}}\), which does not descend to a cochain on
\(\bar A\).

The Lie bracket on \(L\) satisfies Jacobi precisely because \(\bar c\) is a
CE cocycle:
\[
  \bar c(f,\{g,h\}_{\bar A})
  +\bar c(g,\{h,f\}_{\bar A})
  +\bar c(h,\{f,g\}_{\bar A})=0 .
\]
This is the constant-coefficient projection of the Jacobi identity in
\(A\).

## Relation To The Unreduced Source

The unreduced polynomial source
\[
  0\to \mathbb C\cdot1\to A\to\bar A\to0
\]
is the central extension of \(\bar A\) with class \(+\bar c\).  The opposite
source \(L\) is the pushout of this extension along
\[
  \mathbb C[[\hbar]]\cdot1\longrightarrow
  \mathbb C[[\hbar]]K_{\mathrm{cl}},
  \qquad
  1\longmapsto -\hbar N K_{\mathrm{cl}} .
\]
Explicitly,
\[
  \Phi:A[[\hbar]]\longrightarrow L,\qquad
  \Phi(f)=(\bar f,-\hbar N[f]_0K_{\mathrm{cl}})
\]
is a Lie homomorphism:
\[
  [\Phi(f),\Phi(g)]_L
  =
  \Phi(\{f,g\}).
\]
Indeed the central component is
\[
  -\hbar N\,\bar c(f,g)K_{\mathrm{cl}}
  =
  -\hbar N[\{f,g\}]_0K_{\mathrm{cl}} .
\]
The one-cochain \(J_{\mathrm{op}}\) pulls back to the usual unreduced
central-character primitive:
\[
  J_{\mathrm{op}}\Phi(f)=\hbar N[f]_0=\hbar\chi_N(f),
  \qquad \chi_N(f)=N[f]_0 .
\]
Therefore
\[
  d_{\mathrm{CE}}(J_{\mathrm{op}}\Phi)
  =
  d_{\mathrm{CE}}(\hbar\chi_N)
  =
  -\hbar N\omega ,
\]
which is the appendix central-character formula
\[
  \hbar N\omega+d_{\mathrm{CE}}(\hbar\chi_N)=0 .
\]
Over \(\mathbb C((\hbar))\) and \(N\ne0\), \(L\) is isomorphic to the
unreduced extension after rescaling \(K_{\mathrm{cl}}\).  Over
\(\mathbb C[[\hbar]]\) this rescaling uses \((\hbar N)^{-1}\), so it is not
an allowed identification in the formal \(\hbar\)-adic branch.  The correct
formal relation is the pushout above.

## Finite-Window Transport

Let \(\bar A_M\) be an admissible finite Hamiltonian window containing the
linear monomials \(z_1,z_2\), and let
\[
  \pi_{M,N}:\bar A_M\to\bar A_N,\qquad M\ge N\ge1,
\]
be the finite-window projection.  Put
\[
  L_M=\bar A_M\oplus \mathbb C[[\hbar]]K_{\mathrm{cl}},
\]
with truncated bracket
\[
  [(f,aK),(g,bK)]_M
  =
  \bigl(\pi_M\{f,g\}_{\bar A},
  -\hbar N\,\bar c_M(f,g)K\bigr).
\]
The transport map is
\[
  \rho^L_{M,N}(f+aK)=\pi_{M,N}f+aK .
\]
It is compatible with the central term because \(\bar c\) only sees the
linear coefficients of its two inputs:
\[
  \bar c_N(\pi_{M,N}f,\pi_{M,N}g)=\bar c_M(f,g)
\]
whenever the two inputs survive to the lower window.  Equivalently, the
central term is supported on the pair \(z_1,z_2\), which every admissible
scalar window retains.

For central cochains
\[
  J_{\mathrm{op},M}(K)=-1,\qquad J_{\mathrm{op},M}(\bar A_M)=0,
\]
one has
\[
  (\rho^L_{M,N})^*J_{\mathrm{op},N}=J_{\mathrm{op},M},
  \qquad
  (\rho^L_{M,N})^*dJ_{\mathrm{op},N}=dJ_{\mathrm{op},M}.
\]
Thus
\[
  \operatorname{Ob}_{\mathrm{sc},M}+dJ_{\mathrm{op},M}=0
\]
is compatible in the finite-window inverse system.  The CE-source analogues
of the inverse-limit obstruction classes \(\beta,\mu,\lambda_C\) vanish in
this scalar source-replacement system for the elementary reason that the same
compatible primitive \((J_{\mathrm{op},M})_M\) is present in every window.  No
Mittag-Leffler claim about a Costello closed-exchange tower is used.

## Relation To The Algebraic Central-Contact Cone

The algebraic central-contact cone is
\[
  \mathcal X^{1,\mathrm{alg}}_{\mathrm{sc},w,M}(I)
  =
  \mathbb C[[\hbar]]e_M,\qquad d^X_Me_M=0,
\]
with declared scalar image
\[
  \Xi^{\mathrm{alg},\mathrm{sc}}_M(e_M)
  =
  -\hbar N\bar c_M .
\]
The opposite central extension is the CE origin of the same scalar contact:
\[
  d_{\mathrm{CE}}J_{\mathrm{op},M}
  =
  -\hbar N\bar c_M .
\]
The two constructions are not identical.  In the central-extension branch
\(J_{\mathrm{op},M}\) is not a closed degree-one source cocycle:
\[
  d_{\mathrm{CE}}J_{\mathrm{op},M}\ne0 .
\]
The algebraic cone instead adjoins a closed source generator and declares
its image to be the contact cocycle.  The cone is the contact shadow of the
central-extension calculation, not a Costello-local graph realization and
not the original scalar-reduced branch.

## Proof Of Scalar Repair

In the ordinary scalar-reduced branch, the scalar QME representative is
\[
  \operatorname{Ob}_{\mathrm{sc},M}(\gamma_{\mathbf 1};a,f;b,g)
  =
  \hbar N\,\bar c_M(f,g)
  \int_Ia(t)b(t)\gamma_{\mathbf 1}(t)\,dt .
\]
In the opposite source-replacement branch, add the central source cochain
\[
  J_{\mathrm{op},M}=-k^\vee_M
\]
with the same brane-local density factor.  Then
\[
  d_{\mathrm{CE}}J_{\mathrm{op},M}
  =
  -\hbar N\bar c_M ,
\]
and therefore
\[
  \operatorname{Ob}_{\mathrm{sc},M}
  +
  d_{\mathrm{CE}}J_{\mathrm{op},M}
  =
  0 .
\]
At \((f,g)=(z_1,z_2)\), this reads
\[
  \hbar N-\hbar N=0 .
\]
The repair is finite-window compatible by the transport calculation above.
It kills exactly the scalar CE class pulled back to the central extension:
\[
  \pi^*(\hbar N[\bar c_M])=0
  \quad\text{in}\quad
  H^2_{\mathrm{Lie}}(L_M;\mathbb C[[\hbar]]) .
\]
It does not assert that \(\hbar N[\bar c_M]\) vanishes in
\(H^2_{\mathrm{Lie}}(\bar A_M;\mathbb C[[\hbar]])\).

## Attack Ledger

```yaml
- id: A1-265-01
  severity: 1
  status: healed
  lens: CE sign and central character
  target: opposite central extension L=bar A^{cl}_{-hbar N cbar}
  claim: The central extension supplies a primitive of the opposite scalar class.
  broken_step: The sign depends on the CE convention d lambda(x,y)=-lambda([x,y]).
  evidence_type: proof
  evidence_ref: appendix-unreduced-bv-qme.tex:560-589; python CE check through bidegree<6
  files_read:
    - main.tex
    - appendix-unreduced-bv-qme.tex
  tools_used: [nl, sed, python3]
  confidence: high
  blast_radius: wrong sign would double the scalar obstruction instead of cancelling it
  minimal_heal: choose J_op=-k^vee, so d_CE J_op=-hbar N cbar
  residual: none inside the scalar CE source-replacement branch
  deciding_evidence: d_CE J_op(z1,z2)=-hbar N and Ob_sc(z1,z2)=+hbar N

- id: A1-265-02
  severity: 1
  status: valid
  lens: branch type
  target: ordinary scalar-reduced Costello-local closed-exchange branch
  claim: The opposite central extension is a same-branch Costello-local closed exchange.
  broken_step: J_op is a source one-cochain with nonzero CE differential, not a closed Costello source cocycle W_M. No closed field, propagator, source-face graph table, bulk-to-defect kernel, or local counterterm has been constructed.
  evidence_type: proof_gap
  evidence_ref: main.tex:7655-7705; appendix-unreduced-bv-qme.tex:2142-2232; tate-T1-weighted-completion.tex:1526-1741
  files_read:
    - main.tex
    - appendix-unreduced-bv-qme.tex
    - tate-T1-weighted-completion.tex
  tools_used: [nl, sed, rg]
  confidence: high
  blast_radius: false closure of the ordinary scalar QME branch
  minimal_heal: classify the construction as source replacement, not Costello-local closed exchange
  residual: same-branch beta_M^{Cost,sc} remains unless a genuine Costello source maps to -hbar N[cbar_M]
  deciding_evidence: x_M in Z^1(X_M^{Cost,sc}) with H^1(sigma Xi)[x_M]=-hbar N[cbar_M]

- id: A1-265-03
  severity: 1
  status: valid
  lens: scalar-contact filtration
  target: widehat sigma_sc,M in the original brane-defect QME complex
  claim: Killing the source CE class automatically constructs the original filtered scalar-contact projection.
  broken_step: The source replacement makes the scalar class exact in C^*(L_M), but it does not build a continuous filtered chain projection from the original local-functional complex to C^*(bar A).
  evidence_type: line_reference
  evidence_ref: appendix-unreduced-bv-qme.tex:185-305; local-dictionary.tex:829-923; main.tex:8084-8132
  files_read:
    - appendix-unreduced-bv-qme.tex
    - local-dictionary.tex
    - main.tex
  tools_used: [nl, sed, rg]
  confidence: high
  blast_radius: forms ker widehat sigma_sc before the filtration lift exists
  minimal_heal: use a new source complex C^*(L_M) for the scalar branch; do not reuse the original reduced projection
  residual: construct a filtered target projection only if the branch is to be compared inside the original QME target
  deciding_evidence: explicit filtered cochain map widehat sigma_sc,M commuting with d_M

- id: A1-265-04
  severity: 1
  status: valid
  lens: BV pairing
  target: K_cl as a physical closed field
  claim: The central line K_cl is already part of the Costello BV field theory.
  broken_step: The manuscript BV pairing is on h[1] plus h^vee_cont[2]; K_cl is only a source central line. A Costello field would require a degree-complementary dual, coevaluation kernel, propagator, and interaction/source-face rules.
  evidence_type: line_reference
  evidence_ref: local-dictionary.tex:83-97; tate-T1-weighted-completion.tex:66-115; main.tex:7380-7409
  files_read:
    - local-dictionary.tex
    - tate-T1-weighted-completion.tex
    - main.tex
  tools_used: [nl, sed, rg]
  confidence: high
  blast_radius: imports an algebraic central source into the analytic BV graph package
  minimal_heal: keep K_cl as source data unless a K_cl/K_cl^vee BV pair and propagator are constructed
  residual: physical closed-field realization of K_cl is open
  deciding_evidence: BV field extension with degree -1 pairing, heat kernel, and RG-compatible counterterms

- id: A1-265-05
  severity: 2
  status: valid
  lens: brane-defect locality
  target: defect-supported scalar contact
  claim: The central character proves the Costello brane-defect locality theorem.
  broken_step: The scalar density is local on the brane line as an algebraic contact, but no bulk-to-defect kernel or D'_c wavefront/counterterm theorem is supplied.
  evidence_type: line_reference
  evidence_ref: main.tex:7444-7518; references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:156-232
  files_read:
    - main.tex
    - references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md
  tools_used: [nl, sed, rg]
  confidence: high
  blast_radius: turns a central character into an analytic graph theorem
  minimal_heal: state brane locality only for the displayed scalar CE contact; require separate bulk-to-defect and wavefront data for Costello locality
  residual: D'_c/current-valued graph theorem remains open
  deciding_evidence: local Costello kernel with wavefront, counterterm, finite-window, and RG compatibility

- id: A1-265-06
  severity: 2
  status: healed
  lens: finite-window transport
  target: L_M inverse system
  claim: Windowwise scalar primitives may fail Roos compatibility.
  broken_step: The primitive J_op,M is the same central cochain in every admissible window and rho^*J_op,N=J_op,M.
  evidence_type: computation
  evidence_ref: python finite-window central transport check, no failures for surviving pairs through M<6
  files_read:
    - tate-T1-weighted-completion.tex
  tools_used: [python3, nl, sed]
  confidence: high
  blast_radius: false inverse-limit obstruction in the source-replacement scalar branch
  minimal_heal: require scalar windows to retain z1,z2 and set rho^L(K)=K
  residual: none for the scalar source branch; Costello towers have separate Roos classes
  deciding_evidence: rho^*dJ_N=dJ_M for all admissible M>=N

- id: A1-265-07
  severity: 1
  status: valid
  lens: non-scalar rows
  target: theta_3 and regular-density non-scalar tower
  claim: The scalar source replacement solves the non-scalar QME rows.
  broken_step: K_cl is central and can be ignored by scalar-zero pulled-back rows, but it supplies no theta_3 primitive, companion-face table, or marked Costello incidence weights.
  evidence_type: computation
  evidence_ref: appendix-unreduced-bv-qme.tex:2387-2485; scripts/finite_window_graph_array.py:1474-1562; python theta3 check
  files_read:
    - appendix-unreduced-bv-qme.tex
    - scripts/finite_window_graph_array.py
  tools_used: [nl, sed, python3]
  confidence: high
  blast_radius: conflates scalar repair with full QME closure
  minimal_heal: pull scalar-zero non-scalar rows back along L_M->bar A_M, but keep their obstruction ledger unchanged
  residual: theta_3 marked Costello table and lower-window transport identity remain missing
  deciding_evidence: C_theta3,M or companion rows with d_M C=-E_theta3,M and compatible finite-window transport
```

## Exact Branch Boundary

Stable theorem-grade statement:

1. In the CE source category, the extension
   \(\bar A^{\mathrm{cl}}_{-\hbar N\bar c}\) is a Lie algebra.
2. The scalar class \(\hbar N[\bar c]\) pulls back to zero in
   \(H^2_{\mathrm{Lie}}(\bar A^{\mathrm{cl}}_{-\hbar N\bar c})\).
3. The compatible primitive is \(J_{\mathrm{op}}=-k^\vee\).
4. The construction is compatible with finite windows retaining \(z_1,z_2\).
5. It is the formal pushout of the unreduced source \(A\) along
   \(1\mapsto-\hbar N K_{\mathrm{cl}}\), and pulls back to the central
   character \(\hbar\chi_N\) on \(A\).

Non-claims:

1. It is not a Costello-local closed-exchange theorem.
2. It does not construct a scalar-contact chain projection on the original
   ordinary scalar-reduced QME target.
3. It does not add a BV field, BV dual, propagator, or coevaluation kernel
   for \(K_{\mathrm{cl}}\).
4. It does not prove current-valued brane-defect locality or a
   \(\mathcal D'_c\) wavefront/counterterm theorem.
5. It does not solve any non-scalar finite-row obstruction.

If one insists on the original same-branch Costello-local scalar theorem,
the exact obstruction remains
\[
  \beta_M^{\mathrm{Cost},\mathrm{sc}}
  =
  [\hbar N[\bar c_M]]
  \in
  \operatorname{coker}
  H^1(\widehat\sigma_{\mathrm{sc},M}
  \Xi^{\mathrm{Cost},\mathrm{sc}}_M),
\]
after the still-prior scalar-contact projection obstruction
\[
  o_{\sigma,M}^{(1),\mathrm{sc}}=\hbar N[\bar c_M]\ne0 .
\]
The central-extension primitive is not an element of
\(Z^1(\mathcal X^{\bullet,\mathrm{Cost},\mathrm{sc}}_{w,M}(I))\); it has
nonzero differential
\[
  d_{\mathrm{CE}}J_{\mathrm{op},M}=-\hbar N\bar c_M .
\]
This is the precise obstruction to reclassifying the branch as a
same-branch closed exchange.

## TeX-Ready Insertion Draft

```tex
\paragraph{Opposite central source for the scalar branch.}
Let
\[
  \bar A^{\mathrm{cl}}_{-\hbar N\bar c}
  =
  \bar A\oplus\mathbb C[[\hbar]]K_{\mathrm{cl}},
  \qquad
  [(f,aK),(g,bK)]
  =
  (\{f,g\}_{\bar A},-\hbar N\bar c(f,g)K).
\]
If \(k^\vee(K_{\mathrm{cl}})=1\) and \(k^\vee(\bar A)=0\), then, with
\((d_{\mathrm{CE}}\lambda)(x,y)=-\lambda([x,y])\),
\[
  d_{\mathrm{CE}}k^\vee=\hbar N\bar c,\qquad
  d_{\mathrm{CE}}(-k^\vee)=-\hbar N\bar c .
\]
Hence the scalar QME representative
\(\operatorname{Ob}_{\mathrm{sc},M}=\hbar N\bar c_M\) satisfies
\[
  \operatorname{Ob}_{\mathrm{sc},M}+d_{\mathrm{CE}}(-k^\vee_M)=0
\]
after replacing the scalar-reduced source by
\(\bar A^{\mathrm{cl}}_{-\hbar N\bar c}\).  This is a source replacement
before scalar reduction.  It is the pushout of the unreduced extension
\(0\to\mathbb C\cdot1\to A\to\bar A\to0\) along
\(1\mapsto-\hbar N K_{\mathrm{cl}}\), and the primitive pulls back to
\(\hbar\chi_N\), \(\chi_N(f)=N[f]_0\), on \(A\).  The construction is
compatible with finite-window truncation by sending \(K_{\mathrm{cl}}\) to
\(K_{\mathrm{cl}}\).

This does not prove a same-branch Costello-local closed exchange.  The
cochain \(-k^\vee_M\) is not closed; its differential is exactly the scalar
contact being killed.  A Costello-local repair would still have to construct
a closed source complex, propagator, bulk-to-defect graph map, source-face
Hom differential, scalar-contact chain projection, and compatible
counterterms whose scalar image is \(-\hbar N[\bar c_M]\).
```

## Commands Run

```bash
sed -n '1,260p' AGENTS.md
sed -n '1,260p' CLAUDE.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '129,168p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '143,160p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
git status --short
rg --files reconstitution | rg '241|247|259|scalar|QME|qme|central|extension|contact|window'
sed -n '1,420p' reconstitution/swarm-2026-04-30-agent-241-finite-window-closed-exchange-realization-construction-push.md
sed -n '1,320p' reconstitution/swarm-2026-04-30-agent-247-costello-local-closed-exchange-cone-realization.md
sed -n '1,520p' reconstitution/swarm-2026-04-30-agent-259-costello-local-scalar-source-repair-push.md
nl -ba main.tex | sed -n '423,520p'
nl -ba main.tex | sed -n '7380,7725p'
nl -ba main.tex | sed -n '8000,8255p'
nl -ba appendix-unreduced-bv-qme.tex | sed -n '45,320p'
nl -ba appendix-unreduced-bv-qme.tex | sed -n '555,790p'
nl -ba appendix-unreduced-bv-qme.tex | sed -n '2140,2245p'
nl -ba appendix-unreduced-bv-qme.tex | sed -n '2380,2495p'
nl -ba local-dictionary.tex | sed -n '72,155p'
nl -ba local-dictionary.tex | sed -n '820,1060p'
nl -ba tate-T1-weighted-completion.tex | sed -n '66,115p'
nl -ba tate-T1-weighted-completion.tex | sed -n '349,370p'
nl -ba tate-T1-weighted-completion.tex | sed -n '1329,1518p'
nl -ba tate-T1-weighted-completion.tex | sed -n '1520,1745p'
nl -ba scripts/finite_window_graph_array.py | sed -n '1460,1565p'
nl -ba references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md | sed -n '1,250p'
nl -ba references/primary-sources/local-costello-bv-kernel-source-anchors-2026-04-30.md | sed -n '1,300p'
rg -n -F -e "current-valued" -e "D'_c" -e "bulk-to-defect" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from itertools import product
def bracket_bar(x, y):
    a,b=x; c,d=y
    coeff=a*d-b*c
    exp=(a+c-1,b+d-1)
    if coeff == 0 or exp[0] < 0 or exp[1] < 0:
        return []
    if exp == (0,0):
        return []
    return [(coeff, exp)]
def cbar(x, y):
    a,b=x; c,d=y
    return (a*d-b*c) if (a+c,b+d)==(1,1) else 0
def ce_cocycle_delta(x,y,z):
    s = 0
    for coeff,e in bracket_bar(y,z): s += coeff*cbar(x,e)
    for coeff,e in bracket_bar(z,x): s += coeff*cbar(y,e)
    for coeff,e in bracket_bar(x,y): s += coeff*cbar(z,e)
    return s
monos=[(a,b) for a in range(6) for b in range(6) if (a,b)!=(0,0)]
fail=[]
for x,y,z in product(monos, repeat=3):
    val=ce_cocycle_delta(x,y,z)
    if val:
        fail.append((x,y,z,val)); break
print('CE cocycle failures through bidegree<6:', len(fail))
print('cbar(z1,z2)=', cbar((1,0),(0,1)))
print('bar bracket {z1,z2}_bar has terms:', bracket_bar((1,0),(0,1)))
print('For any eta on bar A, d eta(z1,z2)=-eta(0)=0; cbar is non-exact since cbar(z1,z2)=1.')
print('In L_- with [z1,z2]=-hbar*N*K, d kvee(z1,z2)=+hbar*N and d(-kvee)(z1,z2)=-hbar*N.')
def trunc(m, N):
    return m if 1 <= m[0]+m[1] <= N else None
bad=[]
for M in range(1,6):
  for N in range(1,M+1):
    for x,y in product([(a,b) for a in range(M+1) for b in range(M+1) if 1 <= a+b <= M], repeat=2):
        tx, ty = trunc(x,N), trunc(y,N)
        lhs = cbar(x,y) if tx is not None and ty is not None else 0
        rhs = cbar(tx,ty) if tx is not None and ty is not None else 0
        if lhs != rhs:
            bad.append((M,N,x,y,lhs,rhs)); break
    if bad: break
  if bad: break
print('surviving-pair finite-window central transport failures:', len(bad))
PY
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import importlib.util, sys
spec = importlib.util.spec_from_file_location('fw', 'scripts/finite_window_graph_array.py')
fw = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = fw
spec.loader.exec_module(fw)
check = fw.theta3_eight_face_candidate_obstruction_check()
print('theta3 accepted:', check.accepted)
print('theta3 scalar_zero_verified:', check.scalar_zero_verified)
print('theta3 exact_obstruction:', check.exact_obstruction)
print('theta3 status:', check.status)
PY
```

Two diagnostic commands failed and were corrected:

- An initial `rg` regex used unescaped braces in `K_{cl}` and failed with a
  regex parse error.  It was rerun with fixed-string `rg -F` searches.
- An initial direct `importlib` load of `scripts/finite_window_graph_array.py`
  failed because the dataclass module was not registered in `sys.modules`.
  The corrected import registered `sys.modules[spec.name]` before execution.

Observed outputs:

```text
CE cocycle failures through bidegree<6: 0
cbar(z1,z2)= 1
bar bracket {z1,z2}_bar has terms: []
For any eta on bar A, d eta(z1,z2)=-eta(0)=0; cbar is non-exact since cbar(z1,z2)=1.
In L_- with [z1,z2]=-hbar*N*K, d kvee(z1,z2)=+hbar*N and d(-kvee)(z1,z2)=-hbar*N.
surviving-pair finite-window central transport failures: 0
theta3 accepted: False
theta3 scalar_zero_verified: True
theta3 exact_obstruction: R_cand=2E_nu02-2E_nu20+3E_nu03+2E_nu12_1-E_nu12_2+E_theta_3-2E_nu21_2-3E_nu30; diagonal v sends it at N=2 to 2E_nu02-2E_nu20; the marked Costello incidence/weight table is absent
theta3 status: rejected as theorem-grade companion cancellation; it is an explicit obstruction datum until the marked Costello table and lower-window transport identity are supplied
```

No PDF build was run.

## Files Changed

- `reconstitution/opposite-central-extension-scalar-branch-construction-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-265-opposite-central-extension-scalar-branch-construction.md`
