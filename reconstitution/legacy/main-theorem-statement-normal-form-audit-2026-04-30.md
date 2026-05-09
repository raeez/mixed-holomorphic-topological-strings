# Main theorem statement normal-form audit

Date: 2026-04-30.

Agent: 252.

Scope: audit-only.  No TeX, script, bibliography, source, figure, or build
file was edited.  The audited theorem surface is `main.tex` and theorem
statements included from `main.tex:2164` by `\input{theorem-lanes.tex}`.
Appendix and report anchors below are evidence only.

Concurrent-work rule: the checkout is dirty from other agents.  All anchors
refer to the current working tree read by this agent.  No existing edits were
reverted or rewritten.

## Load and method

Loaded `CLAUDE.md`, `AGENTS.md`, the ecosystem attack-heal protocol, and the
Vol II `chriss-ginzburg-rectify` discipline.  Read `main.tex`, `preamble.tex`,
`commands.tex`, `mathmacros.tex`, `notation.tex`, `theorem-lanes.tex`,
`open-obligations.tex`, and the relevant reports from Agents 228-247.  Agent
248's radial Hodge report was read only to sharpen the named radial lane,
because the user explicitly requested the radial necklace Hodge normal form.

Attack criterion: a theorem statement is stale if it leaves a theorem surface
as "conditional", "expected", "problem", or "external input" after the swarm
reports already supplied either a theorem-grade criterion, an exact
obstruction theorem, or a more precise construction target.  Heal criterion:
replace the downgrade by a normal-form statement with exact hypotheses,
branch separation, obstruction vector, and false-transfer exclusions.

## Priority order

P0. Scalar QME / closed exchange.

P1. Costello first-third normalization.

P2. Theta3 finite-row obstruction.

P3. Radial necklace Hodge gate.

P4. Tate bar-cobar / Quillen envelope.

P5. Omega physical trace.

P6. Chiral interface.

This order follows blast radius: false scalar/QME closure corrupts the main
brane-defect theorem first; Costello graph language then risks importing a
universal BV theorem that has not been specialized; theta3 and radial Hodge
are exact algebraic obstruction lanes; Tate, Omega, and chiral interface are
mostly well fenced but still need normal-form wording where theorem summaries
use downgrade language.

## P0. Scalar QME / closed exchange

Current anchors:

- `main.tex:7569-7625`, especially `main.tex:7590-7591`, where the branch
  catalogue still says "proved, or conditional in the exact sense stated".
- `main.tex:8022-8231` for the scalar-contact and finite-window QME setup.
- `theorem-lanes.tex:3178-3348` for the integrated graph/QME branch catalogue.
- Agent reports 232, 241, and 247.

Attack: the ordinary scalar-reduced branch must not be healed by vague closed
exchange.  Agent 241 constructed a finite algebraic central-contact cone.
Agent 247 proved that this is not yet a Costello-local closed exchange.  The
normal theorem surface is a branch theorem plus obstruction sequence.

Proposed normal-form replacement:

```tex
\begin{thm}[Scalar QME obstruction and typed closed-exchange criterion]
Let \(A=\C[z_1,z_2]\), \(\bar A=A/\C\cdot 1\), and
\(\bar c(f,g)=[\{f,g\}]_0\).  In the ordinary scalar-reduced
\(\mathfrak{gl}_N\) branch, the first scalar QME class is
\[
  [\operatorname{Ob}_{\mathrm{sc}}]
    = \hbar_{\mathrm W,N}N[\bar c]
    \in H^2_{\mathrm{Lie}}(\bar A;\C)[[\hbar_{\mathrm W,N}]],
\]
and this class is nonzero.  Hence no internal counterterm in the ordinary
scalar-reduced branch cancels the leading scalar symbol.

The scalar component is cancelled only in the following typed branches.
\begin{enumerate}[label=(\alph*)]
\item Before scalar reduction, the primitive
\(\eta(f)=-[f]_0\) gives \(d_{\mathrm{CE}}\eta=\bar c\), equivalently the
central-character branch \(\chi_N(f)=N[f]_0\) absorbs the scalar source.
\item In the balanced \(\mathfrak{gl}(N|N)\) branch, the scalar representative
vanishes on the balanced scalar-contact habitat.
\item A same-branch closed-exchange solution consists of finite-window
complexes \(\mathcal X^\bullet_{\mathrm{sc},w,M}(I)\), cochain maps
\[
  \Xi^{\mathrm{sc}}_M:
  \mathcal X^\bullet_{\mathrm{sc},w,M}(I)\to
  \mathfrak Q^\bullet_{\mathrm{sc},w,M}(I),
\]
filtered scalar chain projections \(\widehat\sigma_{\mathrm{sc},M}\),
cocycles \(W_M\), and counterterms \(C_M\) such that
\[
  \operatorname{Ob}_{\mathrm{sc},M}
  +\Xi^{\mathrm{sc}}_M(W_M)+d_MC_M=0,
  \qquad
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{sc}}_M)[W_M]
  =-\hbar_{\mathrm W,N}N[\bar c_M],
\]
with compatible truncation and vanishing inverse-limit classes
\[
  \beta^{\mathrm{sc}}_{\mathrm{cl}}=
  \mu^{\mathrm{sc}}_{\mathrm{cl}}=
  \lambda^{\mathrm{sc}}_C=0.
\]
\end{enumerate}
The adjoined one-dimensional central-contact cone proves an enlarged
algebraic source branch.  It is not a Costello-local closed-exchange theorem
until its formal generator is replaced by a closed source complex, finite-scale
propagator, bulk-to-defect graph map, source-face Hom differential, local
counterterm support, scalar chain projection, and compatible finite-window
representatives.  For genuine Costello-local towers the first obstruction is
\[
  o_{\sigma,M}^{(1),\mathrm{sc}}=\hbar_{\mathrm W,N}N[\bar c_M],
\]
and, after an externally supplied scalar gate, the fixed-window image
obstruction is
\[
  \beta_M^{\mathrm{Cost},\mathrm{sc}}
  =
  [\hbar_{\mathrm W,N}N[\bar c_M]]
  \in
  \operatorname{coker}
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{Cost},\mathrm{sc}}_M).
\]
\end{thm}
```

Priority action: replace the loose branch sentence at `main.tex:7590-7591`
with this branch theorem or a compressed version of it.  Preserve the
algebraic cone as a changed source branch, not as Costello-local closure.

## P1. Costello first-third normalization

Current anchors:

- `main.tex:7403-7567` for analytic graph-realization data.
- `main.tex:8384-8412`, whose proposition title still says "conditional".
- `main.tex:8445-8480` for the proved reduced open-line midpoint weights.
- `main.tex:8653-8676`, whose theorem title says "Conditional first/third".
- `main.tex:8721-8772` for the graph-normalization target.
- Agent report 229 and primary-source audit 246.

Attack: the coefficients \(\hbar P\) and \(\hbar^3P^3/24\) are proved in the
formal Weyl algebra and reduced open-line Wick model.  They are not yet a
Costello heat-kernel graph theorem.  The stale word "conditional" should be
replaced by a recognition criterion and obstruction tuple.

Proposed normal-form replacement:

```tex
\begin{thm}[Costello first/third normalization recognition criterion]
The reduced open-line Wick model with midpoint propagator
\(G(t,s)=\frac12\operatorname{sgn}(t-s)\), Weyl-ordered vertices, and only
cross-contractions proves
\[
  W_r^>(f,g)=\frac1{r!}\left(\frac{\hbar}{2}\right)^rP^r(f,g),
  \qquad
  W_r^<(f,g)=\frac1{r!}\left(-\frac{\hbar}{2}\right)^rP^r(f,g).
\]
Thus the odd commutator coefficients in that reduced model are
\[
  \hbar P(f,g),\qquad \frac{\hbar^3}{24}P^3(f,g).
\]

A Costello brane-defect specialization realizes the same first and third
coefficients exactly when it supplies the following datum:
an elliptic mixed HT parent or reduction to the Hamiltonian BF sector,
weighted Tate coefficient convergence of the BV Casimir and propagator,
a brane-restricted propagator with
\[
  P_{\partial,L}|_{\mathrm{Ham}^0}=\frac12P,
\]
a continuous bulk-to-defect kernel into the local QME complex, local
counterterms with RG/support/finite-window compatibility, scalar anomaly
cancellation or a scalar-contact lift, marked finite-window graph row tables,
connected single-trace extraction, and principal-part current compatibility.
For such a datum the normalization defects are
\[
  \mathfrak n_1=
  P_{\partial,L}|_{\mathrm{Ham}^0}-\frac12P,
\]
\[
  \mathfrak n_3=
  \left[
    \operatorname{ObsProd}^{(3)}_{\mathrm{Costello}}(f,g)
    -\frac{\hbar^3}{24}P^3(f,g)
  \right]_{\mathrm{Ham}^0,\mathrm{conn},\mathrm{red}}.
\]
The Costello first/third graph theorem holds precisely on the zero locus of
\[
  \mathfrak O_{\mathrm{Cost}}^{1,3}
  =
  (\mathfrak o_{\mathrm{Cas}},
   \hbar N[\bar c]\ \text{or}\ o_{\sigma,w}^{(r)},
   [\operatorname{Ob}^{\mathrm{red}}_{w,\partial,\hbar}],
   \mathfrak O_{\theta_3},
   \mathfrak n_1,
   \mathfrak n_3).
\]
Absent this datum, the theorem proved here is the reduced open-line Wick
normalization, not a Costello graph realization.
\end{thm}
```

Priority action: retitle `main.tex:8653` away from "Conditional" and fold the
normalization defects into the statement before the problem paragraph.

## P2. Theta3 finite-row obstruction

Current anchors:

- `main.tex:8233-8347`, `prop:theta-three-finite-window-acceptance-gate`.
- `theorem-lanes.tex:3277-3334` in the graph/QME branch catalogue.
- Agent reports 240, 244, and 245.

Attack: the current one-row \(\theta_3\) obstruction is theorem-grade, but
the statement should carry the stronger post-245 pure two-\(u\) obstruction
and the failed eight-face transport, not leave the reader with a vague
"larger package may fix it" downgrade.

Proposed normal-form replacement:

```tex
\begin{prop}[Theta3 row: fixed-window obstruction and enlargement criterion]
For each finite window \(M\), the supplied \(\theta_3\) row is the complex
\[
  \mathcal K^0_{\theta_3,M}=0,\qquad
  \mathcal K^1_{\theta_3,M}=\C\mathsf E_{\theta_3,M},
  \qquad d_{\theta_3,M}=0,
\]
where
\[
  \mathsf E_{\theta_3,M}=-K^M_{\Theta_3}(\zeta_{M,\nu_3}).
\]
The covector
\[
  \ell_{\theta_3}(\mathsf E_{\theta_3,M})=1
\]
is a finite-window \(H^1\)-certificate.  Thus no scalar-zero counterterm
primitive exists inside the supplied one-row complex.

In the ordinary pure two-\(u\) source envelope, in every finite Hamiltonian
degree, the covector
\[
  q_{2u}
  =
  e^*_{((H_{0,1},H_{2,0}),c_{\rho_{2,1}})}
  -\frac12 e^*_{((H_{0,1},H_{0,1}),c_{\rho_{0,2}})}
\]
satisfies
\[
  q_{2u}d_{\mathrm{CE}}=0,\qquad
  q_{2u}(\zeta_{M,\nu_3})=1.
\]
Hence degree enlargement inside that source envelope cannot produce a CE
ancestor for the \(\theta_3\) row.

The tested eight-face companion row has coordinate vector
\[
  (2,-2,3,2,-1,1,-2,-3)
\]
on
\[
  E_{\nu_{02}},E_{\nu_{20}},E_{\nu_{03}},
  E_{\nu_{12}^{(1)}},E_{\nu_{12}^{(2)}},
  E_{\theta_3},E_{\nu_{21}^{(2)}},E_{\nu_{30}},
\]
and diagonal transport to the \(N=2\) window leaves
\[
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}}.
\]

The current controlled enlargements are therefore blocked by the exact tuple
\[
  (\ell_{\theta_3},q_{2u},r_8,V^{M,2}_{\mathrm{diag}}r_8,
   \mathcal C^{(2)}_{\mathrm{missing}}).
\]
A positive enlargement theorem must supply one of:
a scalar-zero CE or local counterterm column
\[
  A^M_{\theta_3,C}=-1,\qquad
  d_MC_{\theta_3,M}=-\mathsf E_{\theta_3,M},
\]
with zero Roos class; a marked source generator outside the ordinary pure
two-\(u\) algebra whose boundary has \(q_{2u}\)-value \(1\) and satisfies
codimension-two closure, Hom-valued Bianchi cancellation, scalar-zero value,
and compatible transport; or a marked companion table proving both
fixed-window and lower-window residuals vanish.
\end{prop}
```

Priority action: preserve the current one-row obstruction, but add the
post-245 exact obstruction tuple.  Do not present "larger package" as a loose
expectation.

## P3. Radial necklace Hodge gate

Current anchors:

- `main.tex:6934-7021`, `thm:finite-n-reduced-moyal`.
- `main.tex:7744-7816`, especially `main.tex:7791-7795`, where the all-order
  map still refers to a supplied radial image package or equivalent quantum
  shear primitive.
- `theorem-lanes.tex:2447-2592` and `theorem-lanes.tex:3391-3431`.
- Agent reports 230 and 248.

Attack: "radial input" is too coarse after the necklace formulation.  The
exact replacement is a decorated Hodge obstruction theorem: for each
bidegree, vanishing of a harmonic projection is necessary and sufficient for
the kernel correction.  The all-bidegree theorem remains the potential
identity or first harmonic obstruction, not an external radial-parts appeal.

Proposed normal-form replacement:

```tex
\begin{thm}[Radial necklace Hodge normal form]
The formal Weyl/Moyal coefficients, Capelli triangular normalization, free
indexed normal-ordering formula, stable trace-diagram injectivity, reduced
open-line first/third weights, edge PBW telescoping strips, \(K_{4,4}\), and
the listed finite non-edge certificates are proved on their stated habitats.

For \(a,b\ge1\), let \(G_{a,b}\) be the two-colour necklace graph whose
vertices are cyclic words with \(a\) letters \(X\) and \(b\) letters \(Y\),
and whose oriented edges are
\[
  e_W:[WXY]\to[WYX],
  \qquad W\in\Q\langle X,Y\rangle_{a-1,b-1}.
\]
Then
\[
  \partial_{a,b}W=[WYX]-[WXY],
  \qquad Z_{a,b}=\ker\partial_{a,b}.
\]
Let
\[
  C^+_{a,b}(W)
  =
  \pi_+\mathcal N_{\mathrm{free}}\operatorname{Tr}(W(YX-XY+\hbar NI)),
\]
and put \(A_{a,b}=C^+_{a,b}|_{Z_{a,b}}\).  For the residual
\(R^{\mathrm{free}}_{a,b}\), define
\[
  \Delta^{\mathrm{dec}}_{a,b}=A_{a,b}A_{a,b}^*,
  \qquad
  \mathsf H^{\mathrm{dec}}_{a,b}=\ker A_{a,b}^*,
\]
and let \(\Pi^{\mathrm{harm}}_{a,b}\) be the orthogonal projection to
\(\mathsf H^{\mathrm{dec}}_{a,b}\).

For every bidegree the following are equivalent:
\begin{enumerate}[label=(\alph*)]
\item there exists \(K_{a,b}\in Z_{a,b}\) with
\[
  C^+_{a,b}(K_{a,b})=R^{\mathrm{free}}_{a,b};
\]
\item the cokernel class
\[
  \mathfrak o_{a,b}
  =
  [R^{\mathrm{free}}_{a,b}]
  \in
  \operatorname{coker}(C^+_{a,b}:Z_{a,b}\to\mathsf D^+_{a,b})
\]
vanishes;
\item
\[
  \Pi^{\mathrm{harm}}_{a,b}R^{\mathrm{free}}_{a,b}=0;
\]
\item every stable left-cokernel functional \(\lambda A_{a,b}=0\) satisfies
\[
  \lambda(R^{\mathrm{free}}_{a,b})=0.
\]
\end{enumerate}
When these conditions hold, the Hodge correction is
\[
  K_{a,b}=A_{a,b}^*
  (\Delta^{\mathrm{dec}}_{a,b})^{-1}R^{\mathrm{free}}_{a,b},
\]
with the inverse taken on \(\operatorname{im}A_{a,b}\).  If the harmonic
projection is nonzero, any functional detecting it is the exact obstruction
theorem for the all-bidegree radial/Weyl trace statement.
\end{thm}
```

Priority action: replace the phrase "radial image package supplied, or
equivalent quantum shear primitive package constructed" by this Hodge gate.
Keep the all-bidegree vanishing theorem open unless the potential identity
for all left-cokernel functionals is proved.

## P4. Tate bar-cobar / Quillen envelope

Current anchors:

- `main.tex:2176-2259`, especially the admissible Tate clause inside
  `thm:universal-ce-pv-koszul-criterion`.
- `main.tex:5242-5295`, `lem:continuous-bar-cobar`.
- `main.tex:5411-5461`, `prop:ce-koszul` and its strict endpoint boundary.
- `theorem-lanes.tex:2172-2204`.
- Agent report 239 and primary-source audit 246.

Attack: the theorem should not read as "if an admissible Tate replacement is
later found".  It should state the theorem on the admissible envelope and an
obstruction theorem for the strict full formal disk endpoint.  The source
fixture gap remains for citation support, not for the internal normal form.

Proposed normal-form replacement:

```tex
\begin{thm}[Admissible Tate bar-cobar envelope and strict-endpoint obstruction]
Let
\[
  \mathfrak g_{\mathrm{adm}}
  =
  \mathfrak h_{\mathrm{adm}}\ltimes
  \mathfrak h^{\vee,\mathrm{adm}}_{\mathrm{cont}}[1]
\]
be a lower-central Tate-pronilpotent dg Lie algebra in an admissible
finite-window Mittag-Leffler model envelope.  Assume finite quotient towers,
exact continuous duality, conilpotent CE chains, a PBW-complete enveloping
algebra, a filtered twisting cochain, and exact inverse limits.  Then the
canonical Lie bar-cobar map
\[
  \Omega C_*^{\mathrm{CE}}(\mathfrak g_{\mathrm{adm}})
  \longrightarrow
  \widehat U(\mathfrak g_{\mathrm{adm}})
\]
is a filtered quasi-isomorphism, and exact continuous dualization gives
\[
  C^*_{\mathrm{CE,cont}}(\mathfrak g_{\mathrm{adm}})
  \simeq
  \widehat U(\mathfrak g_{\mathrm{adm}})^!.
\]

For a candidate open trace datum \((\mathfrak h,D,A_{\mathrm{op}},\tau,
B_{\mathrm{cl}})\), promotion to the stronger open/cyclic/Koszul theorem is
accepted exactly when
\[
  O_{\mathrm{AdmTate}}
  =
  O_{\mathrm{win}}+O_{\mathrm{top}}+O_{\mathrm{conilp}}
  +O_{\mathrm{MC}}(\tau)+O_{\mathrm{cobar}}(\tau)
  +O_{\mathrm{PBW}}+O_{P_0}+O_{\mathrm{cyc}}
\]
vanishes.  The cyclic, \(P_0\), kernel, and Costello/QME gates are not
consequences of associative bar-cobar alone.

For the strict product/direct-sum formal disk endpoint, the obstruction is
the non-membership of the diagonal Casimir:
\[
  (C^M_{\mathfrak h})_M
  \notin
  \left(\prod_d H_d\right)\widehat\otimes
  \left(\bigoplus_d H_d^\vee\right),
\]
equivalently the class of the finite-window Casimirs in the quotient
\[
  Q_{\mathrm{Cas}}
  =
  \varprojlim_M(H_{\le M}\otimes H_{\le M}^\vee)/
  \operatorname{im}
  \left(
    (\prod_d H_d)\widehat\otimes(\bigoplus_d H_d^\vee)
  \right)
\]
is nonzero.  Thus the admissible envelope theorem is proved on its habitat,
while the strict endpoint is governed by this exact obstruction tuple.
\end{thm}
```

Priority action: convert "if admissible Tate..." clauses into "the theorem on
the admissible envelope; obstruction theorem for the strict endpoint" and add
the \(P_0\)/cyclic gates explicitly.

## P5. Omega physical trace

Current anchors:

- `theorem-lanes.tex:1544-1713`, equivariant CE/PV refined bracket.
- `theorem-lanes.tex:2763-2975`, normal Omega weighted kernels and QME
  boundary.
- `theorem-lanes.tex:2977-3176`, stratified trace and physical
  Omega-large-\(N\) criterion.
- Agent report 231 and primary-source audit 246.

Attack: the theorem lane is mostly normal-form already, but any main theorem
summary should not say "physical Omega trace" as a consequence of algebraic
stable trace, \(Q_\Omega\) notation, or a finite-window coefficient ring.
It is a stratified state criterion with a named obstruction vector.

Proposed normal-form replacement:

```tex
\begin{stmt}[Omega physical trace: stratified state criterion]
The brane-preserving normal torus acts on
\[
  N_LX=\R_s\oplus\C_{z_1}\oplus\C_{z_2}
\]
with \(t\) fixed, vector field
\[
  V_\Omega=
  \epsilon_s s\partial_s+
  \epsilon_1z_1\partial_{z_1}+
  \epsilon_2z_2\partial_{z_2},
\]
and Cartan differential
\[
  Q_\Omega=Q+\iota_{V_\Omega},\qquad Q_\Omega^2=L_{V_\Omega}.
\]
All dg assertions are made on the invariant/basic complex or keep the
\(L_{V_\Omega}\)-curvature explicitly.

A physical Omega-large-\(N\) trace theorem is the following datum, not a
consequence of stable invariant theory.  One must supply a finite or
\(q\)-moderate all-window coefficient system, a stratified prefactorization
algebra
\[
  \mathcal F^{\mathrm{str}}_{\Omega,N}:
  \operatorname{Disk}^{\mathrm{str}}_{X,L}
  \to
  \operatorname{Ch}_{R_\Omega[[\hbar_{\mathrm{QME}}]]},
\]
a finite or stable brane branch, collar modules and centrality homotopies,
and a continuous cyclic state
\[
  \omega_{N,\Omega}:A^q_{N,\Omega,\lambda}\to R_\Omega
\]
or a state on
\(\int_{L\subset X}\mathcal F^{\mathrm{str}}_{\Omega,N}\) with BRST/BV lift
annihilating the quantum moment ideal.  Its normalization fixes
\[
  \omega_{N,\Omega}(1)=1,\qquad O^{(N)}_{0,0}=N,\qquad
  \lambda=N\hbar_{\mathrm W,N},
\]
and chooses either the residue branch \(\nu_\Omega^{\mathrm{res}}\) or the
Euler branch \(\nu_\Omega^{\mathrm{Eu}}\), including the inverse normal Euler
factor and real orientation sign.

The theorem holds exactly on the common zero locus of
\[
  \operatorname{Ob}_{\Omega,\mathrm{phys}}
  =
  (
    \operatorname{ob}_{\Omega,\mathrm{Cartan}},
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
    \operatorname{ob}_{\mathrm{src}}
  ).
\]
If \(D_{N,\Omega}^2\ne0\), if centrality homotopies fail, or if the cumulant
topology and coefficientwise \(N^{-2}\)-Poincare asymptotics are not supplied,
the result is a trace-state construction target, not a physical protected
trace theorem.
\end{stmt}
```

Priority action: keep the theorem-lane language, but make sure any main
summary uses "state criterion" and not "trace theorem" before the obstruction
vector vanishes.

## P6. Chiral interface

Current anchors:

- `main.tex:1111-1173`, native local Hamiltonian chiral/factorization algebra.
- `main.tex:1242-1420`, finite-window BMK arity-two transfer.
- `main.tex:1454-1508`, native Darboux theorem package.
- `theorem-lanes.tex:381-533`, where the BMK transfer language still contains
  stale "construction obligation" phrasing at `theorem-lanes.tex:381-384` and
  `theorem-lanes.tex:511-514`.
- `theorem-lanes.tex:1027-1080`, constructed chiral algebra interface.
- Agent reports 228 and 243.

Attack: the native object is already the \(\C^2\) holomorphic
\(E_2\)/factorization object.  A curve chiral algebra enters only after a
controlled \(\C\times\R\) reduction and interface datum.  The finite-window
BMK arity-two transfer appears constructed in `main.tex:1242-1420`, so the
included theorem lane should not call that finite-window transfer merely a
construction obligation.

Proposed normal-form replacement:

```tex
\begin{stmt}[Constructed chiral interface normal form]
The native chiral object of the manuscript is
\(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\) on \(\C^2\), equivalently the
local holomorphic \(E_2\)/factorization algebra determined by the Hamiltonian
CE complex and BV pairing.  It is not a curve vertex algebra.

A curve chiral algebra enters only through an interface
\[
  \mathfrak I_{\mathrm{ch}}
  =
  (\mathcal R_{\C\times\R},
   \mathcal F_{\mathrm{red}},
   V_{\mathrm{red}},
   Q_{\mathrm{BRST}},
   \mathbf 1,T,Y,\operatorname{wt},
   \zeta_\hbar,H_{\mathrm{anom}}),
\]
where the reduction keeps
\[
  \mathfrak h_{\mathrm{red}}
  =
  \C[[z_1]][[z_2]]/\C\cdot1
\]
and the two-index principal-part module, with the original two-variable
Hamiltonian bracket and reduced brane image retained.

The finite-window BMK arity-two transfer is theorem-grade on the stated
finite-window/collar habitat.  The strict all-window BMK and full
curve-vertex conclusion require the obstruction vector
\[
  \operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}
  =
  (\operatorname{Ob}_{\mathrm{red}},
   \operatorname{Ob}_{\mathrm{vert}},
   \operatorname{Ob}_{\mathrm{Zhu}},
   \operatorname{Ob}_{\mathrm{nat}})
\]
to vanish.  Its components record the \(s,z_2\) pushforward, BV pairing,
factorization, brane image, anomaly and Moyal compatibility; finite Laurent
OPEs, vacuum, translation, locality, conformal weights, and
\(Q_{\mathrm{BRST}}^2=0\); zero-mode/Zhu multiplicativity, Capelli shift,
HKR/completed stable comparison, and principal-part coadjoint zero modes; and
comparison back to the native \(\C^2\) factorization source.

Vanishing of this vector is the admission theorem for \(V_{\mathrm{red}}\) as
a reduced curve chiral interface.  Without it, no VOA or Zhu conclusion is a
native theorem of the \(\C^2\) local model.
\end{stmt}
```

Priority action: update only the theorem-statement language: finite-window
arity-two BMK transfer should be stated as proved, strict all-window and
VOA/Zhu as the interface admission theorem.

## Final audit verdict

No TeX edits are authorized or needed in this pass.  The theorem statements
above are the exact normal forms to inscribe in a later TeX integration pass.
The highest-risk stale downgrades are the scalar branch catalogue and the
Costello first/third "conditional" title.  The strongest true theorem surface
is not weaker than the current text: it is more exact, because each lane has a
named habitat, branch separation, obstruction vector, and a precise criterion
for promotion.
