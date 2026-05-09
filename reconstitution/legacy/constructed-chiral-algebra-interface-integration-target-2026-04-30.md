# Constructed Chiral Algebra Interface Integration Target

Date: 2026-04-30.
Owner: Agent 243.
Writable scope: this report and
`reconstitution/swarm-2026-04-30-agent-243-constructed-chiral-algebra-interface-integration-target.md`.
No TeX or manuscript file is edited here.

## Verdict

The user's constructed chiral algebra can enter the local mixed HT
manuscript only as a reduced interface, not as the native object.  The
native object remains the two-complex-dimensional Hamiltonian
holomorphic factorization algebra
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \bigl(\Omega_c^{0,\bullet}(B)\widehat\otimes
  (\mathfrak h\ltimes\mathcal P[1])\bigr),
  \qquad
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1,
\]
with \(\mathcal P=\operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)\).

The strongest integration target is the tuple
\[
  \mathfrak I_{\mathrm{ch}}
  =
  (\mathcal R_{\mathbb C\times\mathbb R},
   \mathcal F_{\mathrm{red}},
   V_{\mathrm{red}},
   Q_{\mathrm{BRST}},
   \mathbf1,T,Y,
   \operatorname{wt},
   \zeta_{\hbar},
   H_{\mathrm{anom}}),
\]
where \(\mathcal R_{\mathbb C\times\mathbb R}\) is a controlled
pushforward retaining the \(z_2\)-mode or the full two-index
principal-part coefficient system.  The user's chiral algebra is
admissible precisely when it is identified with \(V_{\mathrm{red}}\) in
this tuple and all obstruction components below vanish or are carried as
explicit theorem hypotheses.

## Exact Theorem Target

Let
\[
  X=\mathbb R_t\times\mathbb R_s\times\mathbb C_{z_1}\times\mathbb C_{z_2},
  \qquad
  Y=\mathbb R_t\times\mathbb C_{z_1},
  \qquad
  \pi(t,s;z_1,z_2)=(t;z_1).
\]
A controlled reduction datum is
\[
  \mathcal R_{\mathbb C\times\mathbb R}
  =
  (\pi,\kappa_{\mathrm{top}},\kappa_{\mathrm{hol}},
   B_{z_2},\pi_!,L_{\mathrm{red}},
   \langle-,-\rangle_{\mathrm{red}},
   \{-,-\}_{\mathrm{red}},H_{\mathrm{anom}}).
\]
Its coefficient system is not \(\mathbb C[[z_1]]/\mathbb C\).  It is
\[
  \mathfrak h_{\mathrm{red}}
  =
  \mathbb C[[z_1]][[z_2]]/\mathbb C\cdot1,
  \qquad
  \mathcal P_{\mathrm{red}}
  =
  \operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)
  \subset
  H^2_{(z_1,z_2)}(\mathbb C[[z_1,z_2]])\,dz_1dz_2,
\]
with
\[
  \rho_{a,b}=z_1^{-a-1}z_2^{-b-1}dz_1dz_2,\qquad
  \langle\rho_{a,b},z_1^mz_2^n\rangle_{\mathrm{red}}
  =
  \delta_{a,m}\delta_{b,n}.
\]
The bracket and coadjoint action remain two-variable:
\[
  \{f,g\}_{\mathrm{red}}
  =
  \partial_{z_1}f\,\partial_{z_2}g
  -
  \partial_{z_2}f\,\partial_{z_1}g
  \pmod{\mathbb C},
\]
\[
  z_1^pz_2^q\cdot\rho_{i,j}
  =
  -(pj-qi+p-q)\rho_{i-p+1,j-q+1}.
\]
This is the first obstruction theorem: setting \(z_2=0\) kills the
bracket and the Moyal bivector; keeping only \(b=0\) principal parts is
not stable because \(z_1\cdot\rho_{a,0}=-\rho_{a,1}\).

Under \(\mathcal R_{\mathbb C\times\mathbb R}\), the reduced
factorization target is
\[
  \mathcal F_{\mathrm{red}}(I\times D)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \bigl(\Omega_c^\bullet(I)\widehat\otimes
  \Omega_c^{0,\bullet}(D)\widehat\otimes
  (\mathfrak h_{\mathrm{red}}\ltimes
  \mathcal P_{\mathrm{red}}[1])\bigr),
\]
with brane image
\[
  L_{\mathrm{red}}=\mathbb R_t\times\{z_1=0\}\subset Y
\]
and finite-\(N\) evaluation
\[
  \operatorname{ev}^{\mathrm{red}}_N(f)
  =
  \overline{\operatorname{Tr}f(X,Y)},
  \qquad X=\phi_1,\quad Y=\phi_2.
\]

A factorization-to-vertex theorem must then produce
\[
  (V_{\mathrm{red}},\mathbf1,T,Y),
  \qquad
  Y(a,w)b=\sum_{n\in\mathbb Z}(a_{(n)}b)w^{-n-1},
\]
with finite singular orders, vacuum, translation, and locality.  For the
Dirac branch, the candidate vertex algebra has fields
\[
  Z_1{}^i{}_j(z),\quad Z_2{}^i{}_j(z)
  \quad\mathrm{even},
  \qquad
  c^i{}_j(z),\quad b^i{}_j(z)
  \quad\mathrm{odd},
\]
singular products
\[
  Z_1{}^i{}_j(z)Z_2{}^k{}_\ell(w)
  \sim
  \frac{\hbar\,\delta^i_\ell\delta^k_j}{z-w},
  \qquad
  b^i{}_j(z)c^k{}_\ell(w)
  \sim
  \frac{\delta^i_\ell\delta^k_j}{z-w},
\]
and BRST current
\[
  j_{\mathrm{BRST}}
  =
  \operatorname{Tr}(c[Z_1,Z_2])
  +\frac12\operatorname{Tr}(b[c,c]),
  \qquad
  Q_{\mathrm{BRST}}=\operatorname{Res}j_{\mathrm{BRST}}(z)\,dz.
\]
The square-zero proof is the moment-map equivariance computation
\[
  Q[Z_1,Z_2]=[c,[Z_1,Z_2]]
\]
and the graded Jacobi identity, with the selected scalar anomaly branch
included in \(H_{\mathrm{anom}}\).

The zero-mode/Zhu map is part of the theorem, not notation.  With
\[
  \operatorname{wt}(Z_1)=0,\quad
  \operatorname{wt}(Z_2)=1,\quad
  \operatorname{wt}(c)=0,\quad
  \operatorname{wt}(b)=1,
\]
and \(o(a)=a_{\operatorname{wt}(a)-1}\), set
\[
  X^j{}_i=o(Z_1{}^i{}_j),\quad
  Y^j{}_i=o(Z_2{}^i{}_j),\quad
  C^j{}_i=o(c^i{}_j),\quad
  B^j{}_i=o(b^i{}_j).
\]
The pre-BRST Zhu algebra must be
\[
  W_\hbar(\operatorname{Mat}_N^2)
  \otimes
  \operatorname{Cliff}_{bc}(\mathfrak{gl}_N),
\]
with
\[
  [Y^j{}_i,X^\ell{}_k]=
  \hbar\,\delta^\ell_i\delta^j_k,
  \qquad
  [B^j{}_i,C^\ell{}_k]_{\mathrm{super}}=
  \delta^\ell_i\delta^j_k,
\]
and BRST differential
\[
  QX=[C,X],\qquad QY=[C,Y],\qquad QC=\frac12[C,C],
\]
\[
  QB=YX-XY+\hbar N I+[B,C].
\]
The \(\hbar N I\) term is forced by the manuscript's Capelli/Weyl
normalization.  Omitting it breaks compatibility with the degree-zero
Moyal branch.

The Weyl/Moyal compatibility condition is the continuous algebra map
\[
  \zeta_{\hbar}\colon(\bar A_\hbar,*)\longrightarrow
  \operatorname{Zhu}(V_{\mathrm{red}}),
  \qquad
  f*g=m\circ\exp\left(\frac{\hbar}{2}P\right)(f\otimes g),
\]
with
\[
  P=\partial_{z_1}\otimes\partial_{z_2}
    -\partial_{z_2}\otimes\partial_{z_1},
\]
and zero-mode action on principal parts
\[
  [J_{f,(0)},\Theta_\rho]
  =
  \Theta_{\operatorname{ad}^{\vee}_{f,\hbar}\rho}.
\]
Equivalently,
\[
  \operatorname{ob}_{\mathrm{Zhu}}(f,g)
  =
  \zeta_\hbar(f*g)-\zeta_\hbar(f)\zeta_\hbar(g)
\]
must vanish in the relevant Hochschild two-cocycle complex.

## Obstruction Vector

The exact obstruction vector for the interface is
\[
  \operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}
  =
  (\operatorname{Ob}_{\mathrm{red}},
   \operatorname{Ob}_{\mathrm{vert}},
   \operatorname{Ob}_{\mathrm{Zhu}},
   \operatorname{Ob}_{\mathrm{nat}}).
\]

The reduction part is
\[
  \operatorname{Ob}_{\mathrm{red}}
  =
  (\operatorname{ob}_{s,\mathrm{or}},
   \operatorname{ob}_{z_2,\mathrm{fib}},
   \operatorname{ob}_{K,\infty},
   \operatorname{ob}_{\mathrm{pair}},
   \operatorname{ob}_{\mathrm{fac},2},
   \operatorname{ob}_{\mathrm{fac},3},
   \operatorname{ob}_{\mathrm{brane}},
   \operatorname{ob}_{\mathrm{anom}},
   \operatorname{ob}_{\mathrm{Moyal}}).
\]
Here \(\operatorname{ob}_{K,\infty}\) is the compatible finite-window
failure of \(d_FK+Kd_F=\operatorname{id}-i\pi_!\), and
\(\operatorname{ob}_{\mathrm{anom}}\) contains the scalar class
\[
  \hbar N[\bar c]\in H^2_{\mathrm{Lie}}(\bar A;\mathbb C)[[\hbar]]
\]
unless the theorem chooses the central-character branch, the balanced
supertrace branch, or a closed-exchange/brane-defect contribution whose
leading class is \(-\hbar N[\bar c]\).

The vertex part is
\[
  \operatorname{Ob}_{\mathrm{vert}}
  =
  (\operatorname{ob}_{\mathrm{FV}},
   \operatorname{ob}_{\mathrm{Laurent}},
   \operatorname{ob}_{\mathrm{loc}},
   \operatorname{ob}_{\mathrm{wt}},
   \operatorname{ob}_{\mathrm{BRST}}).
\]
It vanishes only after the reduced factorization product gives finite
Laurent OPEs, a vacuum, translation, locality, conformal weights, and
\(Q_{\mathrm{BRST}}^2=0\).

The Zhu part is
\[
  \operatorname{Ob}_{\mathrm{Zhu}}
  =
  (\operatorname{ob}_{\mathrm{zero}},
   \operatorname{ob}_{\mathrm{Zhu}}^{\mathrm{mult}},
   \operatorname{ob}_{\mathrm{Capelli}},
   \operatorname{ob}_{\mathrm{HKR}}).
\]
It measures zero-mode convention, multiplicativity of \(\zeta_\hbar\),
the Capelli shift, and any Hochschild/HKR/CE-PV comparison.  Vol II's
Zhu bridge applies only after a graded vertex algebra with conformal
vector has been constructed, and its quasi-isomorphism claims require
the stated finiteness hypotheses.

The native relation is
\[
  \operatorname{Ob}_{\mathrm{nat}}
  =
  (\operatorname{ob}_{\pi_!\mathrm{-source}},
   \operatorname{Ob}^{\infty}_{\mathrm{BM}},
   \operatorname{ob}_{\mathrm{false-native}}).
\]
This records that the curve algebra is a reduced shadow of
\(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\), not the native
\(\mathbb C^2\) object.  The Bochner-Martinelli all-window transfer is a
separate native \(E_2\) problem; it is not solved by the curve VOA.

## Attack Ledger

```yaml
- id: A243-01
  severity: 1
  status: healed
  lens: native geometry
  claim: The user's constructed chiral algebra can be imported as the native object of the manuscript.
  broken_step: The native object is a holomorphic factorization algebra on polydisks in C^2; a vertex algebra lives on a complex curve with finite Laurent OPEs.
  evidence_ref: "main.tex:1111-1240; theorem-lanes.tex:227-696; local-dictionary.tex:170-374"
  minimal_heal: Make the chiral algebra a reduced V_red after R_{C x R}, not a replacement for F_Ham^hol.
  residual: Construct the reduction and factorization-to-vertex package.

- id: A243-02
  severity: 1
  status: healed
  lens: transverse mode
  claim: The C x R reduction sets z2=0.
  broken_step: Setting z2=0 kills partial_{z2}, hence the Hamiltonian bracket, Moyal bivector, scalar cocycle, and second matrix in the brane Weyl algebra.
  evidence_ref: "theorem-lanes.tex:746-854; reconstitution/native-cxr-voa-zhu-reduction-construction-target-2026-04-30.md:119-192"
  minimal_heal: Retain h_red=C[[z1]][[z2]]/C and the full two-index principal-part module.
  residual: None for the algebraic retained-mode target.

- id: A243-03
  severity: 1
  status: healed
  lens: principal parts
  claim: A one-variable residue line b=0 suffices.
  broken_step: The b=0 line is not stable under the coadjoint action.
  evidence_ref: "z1.rho_{a,0}=-rho_{a,1}; theorem-lanes.tex:850-854; open-obligations.tex:161-180"
  minimal_heal: Keep the full Matlis principal-part coefficient system.
  residual: None for the cotangent coefficient target.

- id: A243-04
  severity: 1
  status: valid
  lens: factorization-to-vertex
  claim: Reduced factorization automatically gives a vertex algebra.
  broken_step: A vertex algebra requires finite Laurent singularity, vacuum, translation, locality, and a conformal/weight convention.
  evidence_ref: "theorem-lanes.tex:638-676; theorem-lanes.tex:893-1024; Vol II hocheschild.tex:687-717"
  minimal_heal: Add Ob_vert and require the full factorization-to-vertex package before using V_red.
  residual: ob_FV, ob_Laurent, ob_loc, ob_wt.

- id: A243-05
  severity: 1
  status: valid
  lens: anomaly and BRST
  claim: The Dirac BRST current is automatically square-zero in the reduced theory.
  broken_step: Algebraic Jacobi gives the formal square-zero calculation only after the scalar anomaly branch and normal-ordering convention are fixed.
  evidence_ref: "theorem-lanes.tex:929-948; theorem-lanes.tex:1019-1024; main.tex:588-610"
  minimal_heal: Carry H_anom and prove Q_BRST^2=0 with the selected scalar branch.
  residual: ob_anom and ob_BRST.

- id: A243-06
  severity: 1
  status: valid
  lens: Zhu and zero modes
  claim: The Zhu algebra automatically realizes the Weyl/Moyal brane algebra.
  broken_step: Zhu requires weights and zero-mode conventions; multiplicativity of zeta_hbar and the Capelli shift must be checked.
  evidence_ref: "theorem-lanes.tex:950-995; Vol II hocheschild.tex:674-752"
  minimal_heal: Require zeta_hbar and the Hochschild obstruction ob_Zhu(f,g).
  residual: ob_zero, ob_Zhu^mult, ob_Capelli.

- id: A243-07
  severity: 2
  status: valid
  lens: Vol II control
  claim: Vol II SC^{ch,top}, chiral Hochschild, or Zhu technology constructs the interface by itself.
  broken_step: Vol II supplies the operadic and Hochschild grammar after the reduced vertex algebra exists; it does not construct pi_!, the retained z2 system, anomaly transport, or the local C^2 source morphism.
  evidence_ref: "Vol II concordance.tex:12-19; sc_chtop_heptagon.tex:218-265; hocheschild.tex:392-410, 674-752; notes/first_principles_cache.md:98-106"
  minimal_heal: Use Vol II as a control consistency target after R_{C x R} and V_red, not as theorem evidence for reduction.
  residual: source fixtures and finite hypotheses for any Vol II bridge.
```

## File Anchors

- `CLAUDE.md:44-66`: native \(\mathbb C^2\) factorization object and
  controlled-reduction firewall.
- `AGENTS.md:87-101`: no direct import of Volume II curve chiral algebra;
  reduction must retain \(z_2\) or principal-part data.
- `main.tex:1111-1240`: constructed local Hamiltonian
  CE/factorization object and no one-dimensional OPE claim.
- `main.tex:1242-1452`: finite-window Bochner-Martinelli transfer, genuine
  two-variable principal-part face, and native \(E_2\) obstruction vector.
- `main.tex:1454-1528`: native Darboux theorem package and curve/compact
  firewall.
- `main.tex:530-610`: open \(U(1)\) center anomaly and Capelli/Rees
  quantum-classical scalar class.
- `main.tex:6179-6265`: support-local principal-part current
  prefactorization datum.
- `main.tex:6934-6987`: finite-\(N\) reduced Moyal commutator and stable
  connected Hamiltonian trace target.
- `main.tex:7744-8020`: degree-zero Moyal target and componentwise quantum
  coefficient surface.
- `theorem-lanes.tex:227-379`: local chiral/factorization taxonomy.
- `theorem-lanes.tex:381-533`: native holomorphic \(E_2\) collision lane and
  Bochner-Martinelli obligation.
- `theorem-lanes.tex:535-696`: constructed local chiral/factorization
  algebra and vertex/OPE boundary.
- `theorem-lanes.tex:698-884`: controlled \(\mathbb C\times\mathbb R\)
  reduction with retained \(z_2\)-coefficients.
- `theorem-lanes.tex:886-1025`: reduced Dirac BRST curve algebra and Zhu
  bridge theorem surface.
- `local-dictionary.tex:170-374`: local taxonomy, vertex/OPE restriction
  boundary, and Weyl/Moyal compatibility requirements.
- `claim-strength-ledger.tex:502-570`: native \(E_2\), controlled
  \(\mathbb C\times\mathbb R\), and reduced Dirac BRST/Zhu classifications.
- `open-obligations.tex:323-328`: current failed-surface ledger for
  \(\mathbb C\times\mathbb R\), VOA, BRST, and Zhu gates.
- `open-obligations.tex:1076-1097`: Weyl/Moyal graph normalization
  coefficients \(1\) and \(1/24\).
- `reconstitution/chiral-algebra-construction-thread-2026-04-30.md:8-24`:
  stable local construction and one-dimensional boundary.
- `reconstitution/controlled-CxR-reduction-thread-2026-04-30.md:7-50`:
  retained-mode verdict.
- `reconstitution/reduced-dirac-brst-zhu-thread-2026-04-30.md:42-100`:
  controlled reduction hypotheses for Dirac BRST/Zhu.
- `reconstitution/native-cxr-voa-zhu-reduction-construction-target-2026-04-30.md:659-713`:
  prior manuscript integration target and obstruction theorem.
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:12-19`:
  status words are mathematical data.
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/sc_chtop_heptagon.tex:218-265`:
  \(\mathsf{SC}^{\mathrm{ch,top}}\) closed/open colours and no open-to-closed
  direction.
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:392-410`:
  bulk equals chiral Hochschild only under physical prefactorization
  hypotheses.
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:687-752`:
  Zhu bridge requires a graded vertex algebra with conformal vector and has
  separate quasi-isomorphism criteria.
- `/Users/raeez/chiral-bar-cobar-vol2/notes/first_principles_cache.md:98-106`:
  Vol II control warnings on \(\mathsf{SC}^{\mathrm{ch,top}}\), strictness,
  associator dependence, and chain-level overclaim.

## Proposed Manuscript Insertion Points

1. `theorem-lanes.tex` after `thm:lane-reduced-dirac-brst-zhu`
   (`theorem-lanes.tex:1025`): add a statement named "constructed chiral
   algebra interface target".  It should display
   \(\mathfrak I_{\mathrm{ch}}\), the retained-mode reduction, the
   BRST/Zhu package, and the obstruction vector above.

2. `local-dictionary.tex` after the Weyl/Moyal compatibility row
   (`local-dictionary.tex:346-374`): add a dictionary row saying that an
   externally constructed chiral algebra may enter only as
   \(V_{\mathrm{red}}\) in \(\mathfrak I_{\mathrm{ch}}\).

3. `claim-strength-ledger.tex` after the reduced Dirac BRST/Zhu row
   (`claim-strength-ledger.tex:552-570`): classify the interface as
   "theorem-surface-with-missing-construction after controlled reduction;
   false transfer before it".

4. `open-obligations.tex` inside the failed-surface ledger after the
   \(\mathbb C\times\mathbb R\), VOA, BRST, and Zhu gate
   (`open-obligations.tex:323-328`): replace the current single sentence
   by the obstruction vector
   \(\operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}\).

5. `main.tex` only if the paper wants the interface in the body: insert
   after `prop:native-darboux-theorem-package` (`main.tex:1454-1528`) a
   theorem-target paragraph, not a proved theorem, unless all components of
   \(\operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}\) are supplied.

## Stable Core

The stable core is nonempty and strict:

1. The native object is \(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\) on
   \(\mathbb C^2\).
2. A constructed curve chiral algebra may enter only after a retained-mode
   \(\mathbb C\times\mathbb R\) reduction.
3. The reduced coefficient system keeps \(z_2\) and the full Matlis
   principal-part module.
4. The reduced Dirac BRST/Zhu package must prove its OPE, weights,
   nilpotence, zero-mode convention, Capelli shift, and Moyal
   multiplicativity.
5. Vol II supplies grammar and bridge targets after these data exist.  It
   supplies no shortcut around the reduction, anomaly, and native-source
   compatibility problems.
