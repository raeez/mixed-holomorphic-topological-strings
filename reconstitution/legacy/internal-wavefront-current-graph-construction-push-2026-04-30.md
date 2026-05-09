# Internal wavefront/current graph construction push

Date: 2026-04-30.
Agent: 267.
Repo: `/Users/raeez/topological-strings`.

## Claim Attacked

Claim attacked: the manuscript's current graph theorem can be promoted
from regular densities and finite graphwise wavefront-admissible tuples
to arbitrary compactly supported currents
\(\mathcal D'_c(I)\), using H\"ormander as the analytic input.

Verdict: false in the present operation grammar.  H\"ormander supplies
criteria for pullback, product, and pushforward.  It does not supply a
canonical product when the criteria fail.  The strongest true theorem is
the graphwise relation described below, plus two maximal sign-conic
linear habitats for ordinary collision-conormal graph kernels.  The full
space \(\mathcal D'_c(I)\) is blocked by a no-canonical-product
obstruction before the scalar-contact or Roos complexes are reached.

Local anchors:

- `appendix-factorization-current-conventions.tex:1394-1480` defines the
  current wavefront-admissible relation, presently with schematic
  \(X_\Gamma(I)\).
- `appendix-factorization-current-conventions.tex:1482-1612` proves the
  finite wavefront graph layer and the coincident-delta obstruction.
- `appendix-factorization-current-conventions.tex:1614-1782` records the
  current-compatible \(D'_c\) theorem surface, product/pushforward
  estimates, counterterm support, and compatibility formulas.
- `tate-T1-weighted-completion.tex:2398-2582` defines
  \(\eta^{\mathrm{reg}}_{n_0,M}\).
- `tate-T1-weighted-completion.tex:2584-2754` constructs the formal
  primitive cone and states explicitly that it is not an original-complex
  smoothing theorem.
- `references/primary-sources/hormander-wavefront-source-anchors-2026-04-30.md`
  confines H\"ormander to operation criteria.

## Construction Attempted

Fix a finite Hamiltonian window \(M\), a connected Costello graph
\(\Gamma\), and external cotangent-current labels
\(B_\bullet=(B_1,\ldots,B_r)\), \(B_j\in\mathcal D'_c(I)\).
Write
\[
  X=\mathbb R^2_{\mathrm{top}}\times\widehat{\mathbb C^2}_{0,\mathrm{hol}},
  \qquad
  L_I=I\times\{0\}\times\{p\}\subset X .
\]
For graph bookkeeping let \(V_{\mathrm{bulk}}(\Gamma)\) be the bulk
vertices, \(V_{\partial}(\Gamma)\) the defect vertices, and let
\(\ell:\{1,\ldots,r\}\to V_{\partial}(\Gamma)\) attach the external
current labels to defect slots.  Choose a small coordinate chart in the
formal local model and set
\[
  X_\Gamma^0(I)=
  X^{V_{\mathrm{bulk}}(\Gamma)}
  \times L_I^{V_{\partial}(\Gamma)}
  \times E_{\Gamma,M},
\]
where \(E_{\Gamma,M}\) is the finite-dimensional coefficient/edge
parameter space in window \(M\).  The coefficient factor is smooth and has
zero wavefront contribution.

The incidence map for current labels is
\[
  e_\Gamma:X_\Gamma^0(I)\longrightarrow I^r,\qquad
  e_{\Gamma,j}(x)=t_{\ell(j)} .
\]
Repeated labels at one defect vertex are encoded by a diagonal component
of \(e_\Gamma\).  Put
\[
  B^\boxtimes=B_1\boxtimes\cdots\boxtimes B_r .
\]
The pushed current label is not a formal symbol.  It is the distribution
\[
  B_\Gamma=e_\Gamma^*B^\boxtimes
\]
when the non-characteristic condition holds:
\[
  N_{e_\Gamma}\cap\mathrm{WF}(B^\boxtimes)=\emptyset,\qquad
  N_{e_\Gamma}
  =
  \{(e_\Gamma(x),\xi)\mid de_{\Gamma,x}^{\,t}\xi=0\}.
\]
Then
\[
  \mathrm{WF}(B_\Gamma)
  \subset
  e_\Gamma^\#\mathrm{WF}(B^\boxtimes)
  =
  \{(x,de_{\Gamma,x}^{\,t}\xi)\mid
    (e_\Gamma(x),\xi)\in\mathrm{WF}(B^\boxtimes)\}.
\]
The tensor-product bound used for \(B^\boxtimes\) is the standard
H\"ormander bound:
\[
  \mathrm{WF}(B^\boxtimes)
  \subset
  \left(
  \prod_{j=1}^r(\mathrm{WF}(B_j)\cup 0_{I})
  \right)\setminus 0_{I^r}.
\]

For each Hadamard coefficient \(K^M_{\Gamma,\alpha}\) on
\(X_\Gamma^0(I)\setminus\operatorname{Diag}(\Gamma)\), set
\[
  \Lambda^M_{\Gamma,\alpha}
  =
  \mathrm{WF}(K^M_{\Gamma,\alpha}),\qquad
  \Lambda_{B,\Gamma}=\mathrm{WF}(B_\Gamma).
\]
The product exists exactly under the conic transversality condition
\[
  \bigl(\Lambda^M_{\Gamma,\alpha}
       +\Lambda_{B,\Gamma}\bigr)
  \cap 0_{X_\Gamma^0(I)}=\emptyset .
\]
In that case
\[
  T^M_{\Gamma,\alpha}(B_\bullet)
  =
  K^M_{\Gamma,\alpha}B_\Gamma
\]
is canonical and
\[
\begin{aligned}
  \mathrm{WF}(T^M_{\Gamma,\alpha})
  \subset&
  \Lambda^M_{\Gamma,\alpha}
  \cup\Lambda_{B,\Gamma}
  \cup
  \bigl(\Lambda^M_{\Gamma,\alpha}+\Lambda_{B,\Gamma}\bigr).
\end{aligned}
\]

Let \(\Delta\in\operatorname{Diag}(\Gamma)\) be a collision diagonal of
codimension \(c_\Delta\).  The diagonal extension datum is finite exactly
when
\[
  s_{\Gamma,\alpha,\Delta}
  =
  \operatorname{sd}_\Delta
  \bigl(T^M_{\Gamma,\alpha}(B_\bullet)\bigr)<\infty .
\]
Then two local extensions differ by
\[
  \widetilde T'-\widetilde T
  =
  \sum_{|\beta|\le N_{\Gamma,\alpha,\Delta}}
  \partial_\nu^\beta\delta_\Delta\otimes S_{\Delta,\beta},
  \qquad
  N_{\Gamma,\alpha,\Delta}
  =
  \max\{-1,\lfloor s_{\Gamma,\alpha,\Delta}-c_\Delta\rfloor\}.
\]
The coefficient distributions satisfy
\[
  \operatorname{supp}S_{\Delta,\beta}
  \subset
  \Delta\cap\operatorname{supp}(B_\Gamma),
\]
and carry the same finite-window Hamiltonian coefficient label.  Hence
the counterterm support is
\[
  \bigcup_{\Delta\in\operatorname{Diag}(\Gamma)}
  \Delta\cap\operatorname{supp}(B_\Gamma),
\]
with finite normal-derivative order bounded by the displayed
\(N_{\Gamma,\alpha,\Delta}\).

Let \(p_\Gamma:X_\Gamma^0(I)\to Y_\Gamma(I)\) be the final graph
projection to the local-functional variables.  Assume it is proper on
the support of the chosen extension.  Then
\[
  \mathrm{WF}(p_{\Gamma,*}T^M_{\Gamma,\alpha})
  \subset
  \{(y,\eta)\mid
  \exists x\in p_\Gamma^{-1}(y),\
  (x,dp_{\Gamma,x}^{\,t}\eta)\in
  \mathrm{WF}(T^M_{\Gamma,\alpha})\}.
\]

Thus the maximal operation-defined relation is
\[
  \mathcal D'_{c,\mathrm{WF}}(I;\Gamma,M)
  =
  \{B_\bullet\in(\mathcal D'_c(I))^r
  \mid
  \text{all four operations above are defined}\}.
\]
This is a finite tuple relation.  It is not automatically a CE source.
A linear subspace \(\mathcal V\subset\mathcal D'_c(I)\) gives a
restricted CE source only when
\[
  \mathcal V^r\subset
  \mathcal D'_{c,\mathrm{WF}}(I;\Gamma,M)
\]
for every graph, window, and finite input under consideration.

## Closed Subhabitat

The regular-density habitat closes:
\[
  \mathcal D^{\mathrm{reg}}_c(I)=C_c^\infty(I)dt .
\]
It is stable under multiplication by smooth test functions, extension by
zero, finite-window truncation, and weight transport.  Smooth densities
do not enlarge the graph wavefront sets, and the counterterms remain
regular-density coefficients under the regular-density graph package.

For non-regular labels, the clean linear habitats for ordinary
collision-conormal kernels are the two sign-conic finite-scaling
subspaces
\[
  \mathcal D'_{c,\Lambda_\pm,\mathrm{fs}}(I)
  =
  \{B\in\mathcal D'_c(I)\mid
    \mathrm{WF}(B)\subset\Lambda_\pm,
    B\text{ has finite scaling degree along its singular support}\},
\]
where
\[
  \Lambda_+=\{(t,\xi)\mid \xi>0\},\qquad
  \Lambda_-=\{(t,\xi)\mid \xi<0\}.
\]
These are maximal among sign-conic diagonal-admissible linear habitats on
an oriented interval: any conic set containing both a positive and a
negative covector admits a finite nonempty sum equal to zero after
rescaling.  A conormal covector to an \(n\)-fold collision block has
components \((\eta_1,\ldots,\eta_n)\) with
\(\sum_i\eta_i=0\).  If every label covector lies in one open half-cone,
it cannot cancel such a conormal vector.  The product criterion therefore
holds for ordinary collision-conormal graph kernels; finite scaling
degree supplies the extension/counterterm step.

The full maximal object for arbitrary graph packages is still the
tuplewise relation \(\mathcal D'_{c,\mathrm{WF}}(I;\Gamma,M)\), not a
unique linear subspace.  The two sign-conic classes are the largest
uniform one-dimensional conic linear subspaces available without adding
new renormalization rules.

## Obstruction Theorem If Blocked

There is no canonical graph product on all of \(\mathcal D'_c(I)\) in
the present operation grammar.

Take the one-edge boundary graph whose singular boundary coefficient has
\[
  \mathrm{WF}(K)\supset
  \{(t_0,t_0;\tau,-\tau)\mid \tau\ne0\}
  \subset N^*\{t=s\}.
\]
Let
\[
  B_1=B_2=\delta_{t_0}.
\]
Then
\[
  \mathrm{WF}(B_1\boxtimes B_2)
  \supset
  \{(t_0,t_0;-\tau,\tau)\mid \tau\ne0\}.
\]
Hence
\[
  \bigl(\mathrm{WF}(K)+
  \mathrm{WF}(B_1\boxtimes B_2)\bigr)\cap0\ne\emptyset .
\]
The product \(K(B_1\boxtimes B_2)\) is therefore not defined by the
H\"ormander product operation.  Equivalently, the graph asks for the
singular boundary value of \(K\) on the diagonal at \((t_0,t_0)\), i.e.
for a restriction whose normal set meets \(\mathrm{WF}(K)\).  Different
finite-part choices differ by distributions supported on the collision
stratum.  Such a choice is extra renormalization data; it is not
canonical and is not supplied by Costello's general finite-scale package
or by Costello--Gwilliam vocabulary.

The cohomological shadow, once a wavefront graph package exists, is the
regular-density quotient obstruction
\[
  \eta^{\mathrm{reg}}_{n_0,M}
  =
  [\mathfrak s^{\mathrm{WF}}_{n_0,M}]
  \in
  H^1(\mathcal Q^\bullet_{w,M}(I)/
      \mathcal X^{\bullet,\mathrm{reg}}_{w,M}(I)).
\]
It is killed in the original complex exactly when a degree-zero
distributional counterterm \(C^{\mathrm{sing}}_{n_0,M}\) satisfies
\[
  \bar d_Mq_M(C^{\mathrm{sing}}_{n_0,M})
  =
  -\mathfrak s^{\mathrm{WF}}_{n_0,M}.
\]
Adjoining \(p^{\mathrm{WF}}_{n_0,M}\) with
\(\widetilde d p^{\mathrm{WF}}_{n_0,M}
=-\widehat{\mathfrak s}^{\mathrm{WF}}_{n_0,M}\) closes the extended
cone, but it is an extension of the complex, not a canonical product on
all currents.

## Scalar-Contact And Roos Compatibility

Let \(\mathcal Q^\bullet_{w,M}(I)\) be the finite-window current
local-functional target and
\(\mathcal X^{\bullet,\mathrm{reg}}_{w,M}(I)\) the regular-density
closed-exchange subcomplex.  The singular quotient is
\[
  \mathcal C^{\bullet,\mathrm{reg}}_{w,M}(I)
  =
  \mathcal Q^\bullet_{w,M}(I)/
  \mathcal X^{\bullet,\mathrm{reg}}_{w,M}(I).
\]
For a wavefront package the first non-regular residual component is
\[
\begin{aligned}
  \mathfrak s^{\mathrm{WF}}_{n_0,M}
  =
  q_M[\hbar^{n_0}]\Bigl(
    &\operatorname{Ob}^{\mathrm{red},\neg\mathrm{rd}}_{w,\partial,\hbar,M}
    +d_MC^{\neg\mathrm{rd}}_{<n_0,M}  \\
    &+\{C^{\mathrm{reg}}_{<n_0,M},
         C^{\neg\mathrm{rd}}_{<n_0,M}\}_{\hbar,M}
    +\frac12
      \{C^{\neg\mathrm{rd}}_{<n_0,M},
        C^{\neg\mathrm{rd}}_{<n_0,M}\}_{\hbar,M}
  \Bigr).
\end{aligned}
\]
The scalar-contact gate must be passed before this is used as a
non-scalar class:
\[
  \widehat\sigma_{\mathrm{sc}}
  \left(d_{\mathrm{QME}}\kappa+\frac12[\kappa,\kappa]_\hbar\right)=0.
\]

Counterterms in the wavefront branch must obey
\[
  j_*C_{\Gamma,I}^{\mathrm{WF},M}(\epsilon;B_\bullet)
  =
  C_{\Gamma,J}^{\mathrm{WF},M}(\epsilon;j_*B_\bullet),
\]
\[
  \pi_{M,N}C_{\Gamma,w}^{\mathrm{WF},M}(\epsilon;B_\bullet)
  =
  C_{\Gamma,w}^{\mathrm{WF},N}(\epsilon;B_\bullet)\pi^{\mathrm{CE}}_{M,N},
\]
\[
  R^M_{w,w'}C_{\Gamma,w}^{\mathrm{WF},M}(\epsilon;B_\bullet)
  =
  C_{\Gamma,w'}^{\mathrm{WF},M}(\epsilon;B_\bullet)
  R^{M,\mathrm{CE}}_{w,w'} .
\]
Failure of the first identity is a factorization-current residual.
Failure of finite-window compatibility gives the Roos cocycle
\[
  \delta_M=
  \pi_{M+1,M}C^{\mathrm{WF},M+1}_{\Gamma,w}
  -
  C^{\mathrm{WF},M}_{\Gamma,w}
  \in Z^0(\mathcal Q^\bullet_{w,M}(I)),
\]
whose class in
\[
  \varprojlim\nolimits^1_MH^0(\mathcal Q^\bullet_{w,M}(I))
\]
is the primitive-compatibility obstruction.  Weight transport has the
same form with \(R^M_{w,w'}\) replacing \(\pi_{M,N}\).

## TeX-Ready Insertion

The following insertion is justified as a strengthening of
`def:app-wavefront-admissible-defect-labels`; it should replace only the
schematic \(X_\Gamma(I)\) paragraph if the integration owner elects to
edit the appendix.

```tex
\begin{defn}[Graphwise wavefront-admissible current package]
\label{def:app-graphwise-wavefront-current-package}
  Fix a finite Hamiltonian window \(M\), a connected Costello graph
  \(\Gamma\), and external cotangent-current labels
  \(B_\bullet=(B_1,\ldots,B_r)\), \(B_j\in\mathcal D'_c(I)\).  Let
  \(V_{\mathrm{bulk}}(\Gamma)\) be the bulk vertices,
  \(V_\partial(\Gamma)\) the defect vertices, and
  \(\ell:\{1,\ldots,r\}\to V_\partial(\Gamma)\) the attachment map for
  the external current labels.  In a fixed local chart set
  \[
    X_\Gamma^0(I)=
    X^{V_{\mathrm{bulk}}(\Gamma)}
    \times L_I^{V_\partial(\Gamma)}
    \times E_{\Gamma,M},
  \]
  where
  \(X=\mathbb R^2_{\mathrm{top}}\times
  \widehat{\mathbb C^2}_{0,\mathrm{hol}}\),
  \(L_I=I\times\{0\}\times\{p\}\), and \(E_{\Gamma,M}\) is the finite
  coefficient/edge-parameter space of the window.  The incidence map is
  \[
    e_\Gamma:X_\Gamma^0(I)\to I^r,\qquad
    e_{\Gamma,j}(x)=t_{\ell(j)} .
  \]
  For \(B^\boxtimes=B_1\boxtimes\cdots\boxtimes B_r\), define
  \(B_\Gamma=e_\Gamma^*B^\boxtimes\) only when
  \(N_{e_\Gamma}\cap\mathrm{WF}(B^\boxtimes)=\emptyset\).  Then
  \[
    \mathrm{WF}(B_\Gamma)\subset
    e_\Gamma^\#\mathrm{WF}(B^\boxtimes).
  \]
  The tuple \(B_\bullet\) is \((\Gamma,M)\)-admissible when, for every
  Hadamard coefficient \(K^M_{\Gamma,\alpha}\), the product condition
  \[
    \bigl(\mathrm{WF}(K^M_{\Gamma,\alpha})
    +\mathrm{WF}(B_\Gamma)\bigr)\cap0_{X_\Gamma^0(I)}=\emptyset
  \]
  holds, the products have finite scaling degree along every
  \(\Delta\in\operatorname{Diag}(\Gamma)\), and the final graph
  projection \(p_\Gamma:X_\Gamma^0(I)\to Y_\Gamma(I)\) is proper on
  support with pushed-forward wavefront inside the chosen
  brane-defect local-functional cone.
\end{defn}
```

## Verification Commands

Commands run:

```bash
sed -n '1,240p' AGENTS.md
sed -n '1,240p' CLAUDE.md
sed -n '1,240p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,220p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,260p' references/primary-sources/hormander-wavefront-source-anchors-2026-04-30.md
nl -ba appendix-factorization-current-conventions.tex | sed -n '1190,1788p'
nl -ba tate-T1-weighted-completion.tex | sed -n '2398,2754p'
nl -ba tate-P1-hadamard-mittag-leffler.tex | sed -n '100,190p'
sed -n '1,260p' reconstitution/regular-density-wavefront-current-graph-branch-construction-target-2026-04-30.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-237-regular-density-wavefront-current-graph-branch-construction-target.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-121-Dc-wavefront-extension.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-154-current-compatible-Dc-theorem.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-139-wavefront-counterterm-eta-kill.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-144-distributional-primitive-for-wavefront-eta.md
python3 scripts/finite_window_graph_array.py
rg -n -e 'X_\\Gamma|incidence|Hadamard|eta\\^\\{\\mathrm\\{reg\\}\\}|Roos|varprojlim' \
  appendix-factorization-current-conventions.tex tate-T1-weighted-completion.tex \
  tate-P1-hadamard-mittag-leffler.tex theorem-lanes.tex claim-strength-ledger.tex
```

No PDF build was run.

## Files Changed

Changed and intended to stage:

- `reconstitution/internal-wavefront-current-graph-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-267-internal-wavefront-current-graph-construction-push.md`

No manuscript TeX, scripts, source fixtures, bibliography, or build
artifacts were edited.
