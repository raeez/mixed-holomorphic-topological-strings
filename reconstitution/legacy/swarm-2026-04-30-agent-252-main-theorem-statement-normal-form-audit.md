# Agent 252 - Main theorem statement normal-form audit

Date: 2026-04-30.

Status: report-only.  No TeX, source, script, bibliography, figure, or build
file was edited.  Owned write paths:

- `reconstitution/main-theorem-statement-normal-form-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-252-main-theorem-statement-normal-form-audit.md`

## Claim attacked

The attacked claim was that the current `main.tex` theorem statements already
reflect the post-Agents-228-247 theorem strength.  Several lanes are close,
but some statements still carry stale downgrade language:

- scalar QME branches still read as loose alternatives;
- Costello first/third graph language still says "conditional";
- theta3 needs the post-245 pure two-`u` and eight-face obstruction tuple;
- radial/Weyl needs the decorated necklace Hodge obstruction theorem, not a
  generic radial input;
- Tate bar-cobar needs theorem-on-admissible-envelope plus strict-endpoint
  obstruction wording;
- Omega physical trace and chiral interface need admission/criterion language
  wherever theorem summaries overstate stable trace or curve-VOA transfer.

## Evidence read

- `CLAUDE.md`
- `AGENTS.md`
- ecosystem attack-heal protocol
- Vol II `chriss-ginzburg-rectify` skill
- `main.tex`, `preamble.tex`, `commands.tex`, `mathmacros.tex`,
  `notation.tex`
- `theorem-lanes.tex`, `open-obligations.tex`, `claim-strength-ledger.tex`,
  `local-dictionary.tex`
- Agent reports 228, 229, 230, 231, 232, 239, 240, 241, 242, 243, 244, 245,
  246, and 247
- Agent 248 radial Hodge report as supplementary evidence for the explicitly
  requested radial necklace Hodge lane

## Priority order

1. Scalar QME / closed exchange.
2. Costello first-third normalization.
3. Theta3 finite-row obstruction.
4. Radial necklace Hodge gate.
5. Tate bar-cobar / Quillen envelope.
6. Omega physical trace.
7. Chiral interface.

## Normal-form ledger

### 1. Scalar QME / closed exchange

Anchors: `main.tex:7569-7625`, `main.tex:8022-8231`,
`theorem-lanes.tex:3178-3348`; Agents 232, 241, 247.

Finding: ordinary scalar-reduced \(\mathfrak{gl}_N\) has nonzero class
\[
  \hbar_{\mathrm W,N}N[\bar c]\in H^2_{\mathrm{Lie}}(\bar A;\C)[[\hbar]].
\]
The algebraic cone is a defect-supported central-contact source replacement,
not a Costello-local closed exchange.

Replacement statement: state a scalar branch theorem.  The allowed branches
are unreduced central character, balanced supertrace, or a same-branch
closed-exchange tower \((\mathcal X_M,\Xi_M,W_M,C_M)\) with scalar image
\(-\hbar_{\mathrm W,N}N[\bar c_M]\) and zero
\[
  \beta^{\mathrm{sc}}_{\mathrm{cl}},\quad
  \mu^{\mathrm{sc}}_{\mathrm{cl}},\quad
  \lambda^{\mathrm{sc}}_C.
\]
For genuine Costello-local towers the current first obstructions are
\[
  o_{\sigma,M}^{(1),\mathrm{sc}}=\hbar_{\mathrm W,N}N[\bar c_M],
  \qquad
  \beta_M^{\mathrm{Cost},\mathrm{sc}}
  =
  [\hbar_{\mathrm W,N}N[\bar c_M]]
  \in
  \operatorname{coker}
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi_M^{\mathrm{Cost},\mathrm{sc}}).
\]

### 2. Costello first-third normalization

Anchors: `main.tex:7403-7567`, `main.tex:8384-8412`,
`main.tex:8445-8480`, `main.tex:8653-8676`, `main.tex:8721-8772`;
Agent 229.

Finding: \(\hbar P\) and \(\hbar^3P^3/24\) are proved in the formal
Weyl/Moyal and reduced open-line Wick models.  They are not yet a Costello
heat-kernel graph theorem.

Replacement statement: retitle as a recognition criterion.  A Costello
specialization must supply the elliptic parent/reduction, weighted Tate
coefficient convergence, brane-restricted propagator with
\[
  P_{\partial,L}|_{\mathrm{Ham}^0}=P/2,
\]
bulk-to-defect kernel, counterterms, scalar lift, marked graph rows,
connected extraction, and current compatibility.  The exact obstruction is
\[
  \mathfrak O_{\mathrm{Cost}}^{1,3}
  =
  (\mathfrak o_{\mathrm{Cas}},
   \hbar N[\bar c]\ \text{or}\ o_{\sigma,w}^{(r)},
   [\operatorname{Ob}^{\mathrm{red}}_{w,\partial,\hbar}],
   \mathfrak O_{\theta_3},
   \mathfrak n_1,
   \mathfrak n_3),
\]
with
\[
  \mathfrak n_1=P_{\partial,L}|_{\mathrm{Ham}^0}-P/2,
\]
\[
  \mathfrak n_3=
  [\operatorname{ObsProd}^{(3)}_{\mathrm{Costello}}-\hbar^3P^3/24]
  _{\mathrm{Ham}^0,\mathrm{conn},\mathrm{red}}.
\]

### 3. Theta3 finite-row obstruction

Anchors: `main.tex:8233-8347`, `theorem-lanes.tex:3277-3334`; Agents 240,
244, 245.

Finding: the row complex
\[
  \mathcal K^0_{\theta_3,M}=0,\qquad
  \mathcal K^1_{\theta_3,M}=\C\mathsf E_{\theta_3,M}
\]
has the finite-row certificate
\(\ell_{\theta_3}(\mathsf E_{\theta_3,M})=1\).  The pure two-`u` source
envelope is obstructed in every finite Hamiltonian degree by
\[
  q_{2u}d_{\mathrm{CE}}=0,\qquad
  q_{2u}(\zeta_{M,\nu_3})=1.
\]
The tested eight-face vector
\[
  (2,-2,3,2,-1,1,-2,-3)
\]
has lower \(N=2\) residual \(2E^2_{\nu_{02}}-2E^2_{\nu_{20}}\).

Replacement statement: the exact current obstruction tuple is
\[
  (\ell_{\theta_3},q_{2u},r_8,V^{M,2}_{\mathrm{diag}}r_8,
  \mathcal C^{(2)}_{\mathrm{missing}}).
\]
It is killed only by a scalar-zero counterterm/CE column
\[
  A^M_{\theta_3,C}=-1,\qquad d_MC_{\theta_3,M}=-\mathsf E_{\theta_3,M},
\]
a marked source generator defeating \(q_{2u}\), or a marked companion table
with zero fixed-window and lower-window residuals.

### 4. Radial necklace Hodge gate

Anchors: `main.tex:6934-7021`, `main.tex:7744-7816`,
`theorem-lanes.tex:2447-2592`, `theorem-lanes.tex:3391-3431`; Agents 230,
248.

Finding: the all-interior radial theorem is not a generic radial-parts input.
It is the decorated necklace Hodge problem.

Replacement statement: for the two-colour necklace graph \(G_{a,b}\), set
\[
  Z_{a,b}=\ker\partial_{a,b},\qquad
  C^+_{a,b}(W)=
  \pi_+\mathcal N_{\mathrm{free}}\operatorname{Tr}(W(YX-XY+\hbar NI)),
\]
and \(A_{a,b}=C^+_{a,b}|_{Z_{a,b}}\).  With
\[
  \Delta^{\mathrm{dec}}_{a,b}=A_{a,b}A_{a,b}^*,
  \qquad
  \mathsf H^{\mathrm{dec}}_{a,b}=\ker A_{a,b}^*,
\]
the kernel correction exists iff
\[
  \Pi^{\mathrm{harm}}_{a,b}R^{\mathrm{free}}_{a,b}=0,
\]
equivalently every left-cokernel functional \(\lambda A_{a,b}=0\) satisfies
\[
  \lambda(R^{\mathrm{free}}_{a,b})=0.
\]
Failure is the exact obstruction theorem; success gives
\[
  K_{a,b}=
  A_{a,b}^*(\Delta^{\mathrm{dec}}_{a,b})^{-1}
  R^{\mathrm{free}}_{a,b}.
\]

### 5. Tate bar-cobar / Quillen envelope

Anchors: `main.tex:2176-2259`, `main.tex:5242-5295`,
`main.tex:5411-5461`, `theorem-lanes.tex:2172-2204`; Agent 239 and audit
246.

Finding: the theorem is valid on an admissible lower-central
Tate-pronilpotent finite-window ML envelope.  The strict product/direct-sum
formal disk endpoint has a Casimir obstruction.

Replacement statement: for
\[
  \mathfrak g_{\mathrm{adm}}
  =
  \mathfrak h_{\mathrm{adm}}\ltimes
  \mathfrak h^{\vee,\mathrm{adm}}_{\mathrm{cont}}[1],
\]
state
\[
  \Omega C_*^{\mathrm{CE}}(\mathfrak g_{\mathrm{adm}})
  \to \widehat U(\mathfrak g_{\mathrm{adm}})
\]
as a filtered quasi-isomorphism and
\[
  C^*_{\mathrm{CE,cont}}(\mathfrak g_{\mathrm{adm}})
  \simeq
  \widehat U(\mathfrak g_{\mathrm{adm}})^!.
\]
The stronger open/cyclic/Koszul promotion is governed by
\[
  O_{\mathrm{AdmTate}}
  =
  O_{\mathrm{win}}+O_{\mathrm{top}}+O_{\mathrm{conilp}}
  +O_{\mathrm{MC}}(\tau)+O_{\mathrm{cobar}}(\tau)
  +O_{\mathrm{PBW}}+O_{P_0}+O_{\mathrm{cyc}}.
\]
The strict endpoint obstruction is
\[
  (C^M_{\mathfrak h})_M
  \notin
  \left(\prod_d H_d\right)\widehat\otimes
  \left(\bigoplus_d H_d^\vee\right).
\]

### 6. Omega physical trace

Anchors: `theorem-lanes.tex:1544-1713`, `theorem-lanes.tex:2763-2975`,
`theorem-lanes.tex:2977-3176`; Agent 231 and audit 246.

Finding: the physical Omega trace is not implied by stable trace labels,
\(Q_\Omega\) notation, or finite-window localization.  The lane is a
stratified state criterion.

Replacement statement: fix the normal torus on
\[
  N_LX=\R_s\oplus\C_{z_1}\oplus\C_{z_2},
  \qquad
  Q_\Omega=Q+\iota_{V_\Omega},\quad Q_\Omega^2=L_{V_\Omega}.
\]
Require a stratified prefactorization algebra on \((X,L)\), finite/stable
brane branch, collar modules, centrality homotopies, continuous cyclic state
\(\omega_{N,\Omega}\), BRST/BV lift killing the moment ideal, normalization
\[
  \omega(1)=1,\quad O^{(N)}_{0,0}=N,\quad
  \lambda=N\hbar_{\mathrm W,N},
\]
residue or Euler branch, Ward identities, cumulant topology, and
coefficientwise \(N^{-2}\)-Poincare asymptotics.  The theorem is the zero
locus of
\[
  \operatorname{Ob}_{\Omega,\mathrm{phys}}
  =
  (\operatorname{ob}_{\Omega,\mathrm{Cartan}},
   \operatorname{ob}_{\Omega,\mathrm{contr}},
   \operatorname{ob}_{\Omega,\mathrm{coeff}},
   \operatorname{ob}_{\mathrm{str}},
   \operatorname{ob}_{\mathrm{red}},
   \operatorname{ob}_{\mathrm{branch}},
   \operatorname{ob}_{\mathrm{state}},
   \operatorname{ob}_{\mathrm{norm}},
   \operatorname{ob}^{\mathrm{sc}}_{\mathrm{QME}},
   \operatorname{ob}^{\mathrm{ns}}_{\mathrm{QME}},
   \operatorname{ob}_{\mathrm{cent}},
   \operatorname{ob}_{\mathrm{Ward}},
   \operatorname{ob}_{\mathrm{cum}},
   \operatorname{ob}_{\mathrm{asymp}},
   \operatorname{ob}_{\mathrm{src}}).
\]

### 7. Chiral interface

Anchors: `main.tex:1111-1173`, `main.tex:1242-1420`,
`main.tex:1454-1508`, `theorem-lanes.tex:381-533`,
`theorem-lanes.tex:1027-1080`; Agents 228 and 243.

Finding: finite-window BMK arity-two transfer is now theorem-grade on its
finite habitat, but strict all-window and curve-VOA/Zhu claims require the
constructed interface.  The native object remains the \(\C^2\) holomorphic
\(E_2\)/factorization algebra.

Replacement statement: a curve chiral algebra enters only via
\[
  \mathfrak I_{\mathrm{ch}}
  =
  (\mathcal R_{\C\times\R},
   \mathcal F_{\mathrm{red}},
   V_{\mathrm{red}},
   Q_{\mathrm{BRST}},
   \mathbf1,T,Y,\operatorname{wt},
   \zeta_\hbar,H_{\mathrm{anom}}).
\]
Admission is exactly
\[
  \operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}
  =
  (\operatorname{Ob}_{\mathrm{red}},
   \operatorname{Ob}_{\mathrm{vert}},
   \operatorname{Ob}_{\mathrm{Zhu}},
   \operatorname{Ob}_{\mathrm{nat}})
  =0.
\]
Without this vanishing, no VOA/Zhu conclusion is native to the \(\C^2\)
local model.

## Files changed

- Added `reconstitution/main-theorem-statement-normal-form-audit-2026-04-30.md`.
- Added `reconstitution/swarm-2026-04-30-agent-252-main-theorem-statement-normal-form-audit.md`.

## Verification

This pass used targeted `rg`, `sed`, and `nl -ba` reads only.  No PDF build
was run because the task is report-only and the shared checkout has active
concurrent TeX edits outside this agent's ownership.
