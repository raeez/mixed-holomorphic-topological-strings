# Agent 267 attack-heal report: internal wavefront/current graph construction

Date: 2026-04-30.
Worktree: `/Users/raeez/topological-strings`.
Owned write files:

- `reconstitution/internal-wavefront-current-graph-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-267-internal-wavefront-current-graph-construction-push.md`

No TeX manuscript files, scripts, source fixtures, bibliography files, or
build artifacts were edited.

## Claim Attacked

The attacked claim was:

> The wavefront/current graph theorem can be made canonical for every
> \(B\in\mathcal D'_c(I)\) by citing H\"ormander.

Attack result: valid.  H\"ormander gives operation criteria only.  The
manuscript must construct the graph spaces, incidence maps, label cones,
product, extension, counterterm, scalar quotient, and Roos compatibility
internally.  When the product criterion fails, H\"ormander supplies no
canonical product.

## Construction Attempted

I constructed the finite graph package as follows.

For a graph \(\Gamma\), finite window \(M\), and labels
\(B_\bullet=(B_1,\ldots,B_r)\), use
\[
  X_\Gamma^0(I)=
  X^{V_{\mathrm{bulk}}(\Gamma)}
  \times L_I^{V_\partial(\Gamma)}
  \times E_{\Gamma,M},
  \qquad
  X=\mathbb R^2_{\mathrm{top}}\times\widehat{\mathbb C^2}_{0,\mathrm{hol}}.
\]
Here \(L_I=I\times\{0\}\times\{p\}\), and \(E_{\Gamma,M}\) is the finite
coefficient/edge-parameter factor.  The current-label incidence map is
\[
  e_\Gamma:X_\Gamma^0(I)\to I^r,\qquad
  e_{\Gamma,j}(x)=t_{\ell(j)} .
\]
Repeated labels at one defect vertex become diagonal pullbacks.  For
\(B^\boxtimes=B_1\boxtimes\cdots\boxtimes B_r\), define
\[
  B_\Gamma=e_\Gamma^*B^\boxtimes
\]
only if
\[
  N_{e_\Gamma}\cap\mathrm{WF}(B^\boxtimes)=\emptyset.
\]
Then
\[
  \mathrm{WF}(B_\Gamma)\subset
  e_\Gamma^\#\mathrm{WF}(B^\boxtimes).
\]

For each Hadamard coefficient \(K^M_{\Gamma,\alpha}\), the product
\[
  T^M_{\Gamma,\alpha}(B_\bullet)=
  K^M_{\Gamma,\alpha}B_\Gamma
\]
is canonical exactly when
\[
  \bigl(\mathrm{WF}(K^M_{\Gamma,\alpha})
  +\mathrm{WF}(B_\Gamma)\bigr)\cap0_{X_\Gamma^0(I)}=\emptyset.
\]
The product wavefront is bounded by
\[
\begin{aligned}
  \mathrm{WF}(T^M_{\Gamma,\alpha})
  \subset&
  \mathrm{WF}(K^M_{\Gamma,\alpha})
  \cup\mathrm{WF}(B_\Gamma)\\
  &\cup
  \bigl(\mathrm{WF}(K^M_{\Gamma,\alpha})
  +\mathrm{WF}(B_\Gamma)\bigr).
\end{aligned}
\]

For each collision diagonal \(\Delta\), require
\[
  \operatorname{sd}_\Delta
  \bigl(T^M_{\Gamma,\alpha}(B_\bullet)\bigr)<\infty .
\]
If \(c_\Delta=\operatorname{codim}\Delta\), the extension ambiguity is
\[
  \widetilde T'-\widetilde T
  =
  \sum_{|\beta|\le N_{\Gamma,\alpha,\Delta}}
  \partial_\nu^\beta\delta_\Delta\otimes S_{\Delta,\beta},
  \qquad
  N_{\Gamma,\alpha,\Delta}
  =
  \max\{-1,\lfloor
    \operatorname{sd}_\Delta(T^M_{\Gamma,\alpha})-c_\Delta\rfloor\}.
\]
The support is contained in
\[
  \Delta\cap\operatorname{supp}(B_\Gamma).
\]

The final graph projection \(p_\Gamma:X_\Gamma^0(I)\to Y_\Gamma(I)\)
must be proper on support, and then
\[
  \mathrm{WF}(p_{\Gamma,*}T^M_{\Gamma,\alpha})
  \subset
  \{(y,\eta)\mid
  \exists x\in p_\Gamma^{-1}(y),\
  (x,dp_{\Gamma,x}^{\,t}\eta)\in
  \mathrm{WF}(T^M_{\Gamma,\alpha})\}.
\]

This gives the maximal operation-defined relation
\[
  \mathcal D'_{c,\mathrm{WF}}(I;\Gamma,M)
  \subset(\mathcal D'_c(I))^r.
\]
It is maximal for the present operations: outside it, at least one
pullback, product, finite scaling-degree extension, or pushforward is not
defined by the allowed calculus.

## Closed Subhabitat

The theorem closes on:

1. Regular densities
\[
  \mathcal D^{\mathrm{reg}}_c(I)=C_c^\infty(I)dt.
\]

2. Finite graphwise admissible tuples
\[
  B_\bullet\in\mathcal D'_{c,\mathrm{WF}}(I;\Gamma,M).
\]

3. For ordinary collision-conormal graph kernels on an oriented interval,
the two maximal sign-conic finite-scaling linear habitats
\[
  \mathcal D'_{c,\Lambda_\pm,\mathrm{fs}}(I)
  =
  \{B\in\mathcal D'_c(I)\mid
  \mathrm{WF}(B)\subset\Lambda_\pm,
  B\text{ has finite scaling degree along its singular support}\},
\]
\[
  \Lambda_+=\{(t,\xi)\mid\xi>0\},\qquad
  \Lambda_-=\{(t,\xi)\mid\xi<0\}.
\]
These are maximal in the sign-conic sense: any cone containing both signs
admits rescaled covectors with finite sum zero, and so can cancel a
collision conormal.

A linear CE current source is available only after choosing
\(\mathcal V\subset\mathcal D'_c(I)\) such that every finite tuple from
\(\mathcal V\) lies in the corresponding graph/window admissible
relation.  The relation itself is the intrinsic object.

## Obstruction Theorem

No theorem exists for all of \(\mathcal D'_c(I)\) without extra
renormalization data.

Take a one-edge boundary graph with singular coefficient \(K\) satisfying
\[
  \mathrm{WF}(K)\supset
  \{(t_0,t_0;\tau,-\tau)\mid\tau\ne0\}.
\]
Set \(B_1=B_2=\delta_{t_0}\).  Since
\[
  \mathrm{WF}(\delta_{t_0}\boxtimes\delta_{t_0})
  \supset
  \{(t_0,t_0;-\tau,\tau)\mid\tau\ne0\},
\]
one has
\[
  (\mathrm{WF}(K)+
  \mathrm{WF}(\delta_{t_0}\boxtimes\delta_{t_0}))\cap0\ne\emptyset.
\]
The product is not canonical.  Any finite-part value is a new
renormalization prescription supported on the collision stratum.

The cohomological obstruction after a wavefront graph package exists is
\[
  \eta^{\mathrm{reg}}_{n_0,M}
  =
  [\mathfrak s^{\mathrm{WF}}_{n_0,M}]
  \in
  H^1(\mathcal Q^\bullet_{w,M}(I)/
      \mathcal X^{\bullet,\mathrm{reg}}_{w,M}(I)).
\]
The original complex kills it exactly when
\[
  \bar d_Mq_M(C^{\mathrm{sing}}_{n_0,M})
  =
  -\mathfrak s^{\mathrm{WF}}_{n_0,M}.
\]
The primitive cone of
`tate-T1-weighted-completion.tex:2584-2754` is a valid extension theorem,
not a proof of a canonical all-current graph product.

## Scalar-Contact And Roos Compatibility

The scalar-contact gate is
\[
  \widehat\sigma_{\mathrm{sc}}
  \left(d_{\mathrm{QME}}\kappa+\frac12[\kappa,\kappa]_\hbar\right)=0.
\]
Only after this gate does the residual live in the non-scalar kernel.

The finite-window current counterterms must satisfy:
\[
  j_*C_{\Gamma,I}^{\mathrm{WF},M}
  =
  C_{\Gamma,J}^{\mathrm{WF},M}(j_*B_\bullet),
\]
\[
  \pi_{M,N}C_{\Gamma,w}^{\mathrm{WF},M}
  =
  C_{\Gamma,w}^{\mathrm{WF},N}\pi^{\mathrm{CE}}_{M,N},
\]
\[
  R^M_{w,w'}C_{\Gamma,w}^{\mathrm{WF},M}
  =
  C_{\Gamma,w'}^{\mathrm{WF},M}R^{M,\mathrm{CE}}_{w,w'} .
\]
The Roos class is represented by
\[
  \delta_M=
  \pi_{M+1,M}C_{\Gamma,w}^{\mathrm{WF},M+1}
  -
  C_{\Gamma,w}^{\mathrm{WF},M}
  \in Z^0(\mathcal Q^\bullet_{w,M}(I)),
\]
with class in
\[
  \varprojlim\nolimits^1_MH^0(\mathcal Q^\bullet_{w,M}(I)).
\]
Vanishing is equivalent to compatible primitive choices.  Failure of
interval extension is a factorization-current failure, not a Roos
finite-window primitive failure.

## Attack Ledger

```yaml
- id: A267-01
  severity: 1
  status: valid
  lens: arbitrary-current product
  target: arbitrary D'_c(I) graph theorem
  claim: Every compactly supported current can label every graph.
  broken_step: Coincident delta labels cancel the conormal wavefront of a
    singular boundary propagator, so the graph product is undefined.
  evidence_type: counterexample
  evidence_ref: appendix-factorization-current-conventions.tex:1599-1611;
    appendix-factorization-current-conventions.tex:1729-1737
  minimal_heal: Keep arbitrary D'_c(I) outside the graph theorem unless
    extra renormalization data define failed products.

- id: A267-02
  severity: 2
  status: healed
  lens: graph configuration space
  target: def:app-wavefront-admissible-defect-labels
  claim: The schematic X_Gamma(I) description is enough for theorem-grade
    pullback/product/pushforward bookkeeping.
  broken_step: The incidence map e_Gamma and its normal set decide whether
    B_Gamma exists, especially with repeated labels.
  evidence_type: proof_gap
  evidence_ref: appendix-factorization-current-conventions.tex:1399-1409
  minimal_heal: Insert the explicit X_Gamma^0(I), e_Gamma, N_e, and
    e_Gamma^# WF formulas from this report.

- id: A267-03
  severity: 2
  status: healed
  lens: maximal habitat
  target: wavefront admissible source
  claim: There is one maximal linear distributional source for all graph
    products.
  broken_step: The intrinsic maximal object is tuplewise and graphwise.
    Linear CE sources require every finite tuple to satisfy the relation.
  evidence_type: proof
  evidence_ref: appendix-factorization-current-conventions.tex:1451-1456
  minimal_heal: State the tuple relation as maximal for the allowed
    operations; isolate Lambda_+ and Lambda_- as maximal sign-conic
    finite-scaling linear habitats for ordinary collision-conormal kernels.

- id: A267-04
  severity: 2
  status: healed
  lens: scalar-contact/Roos boundary
  target: wavefront current counterterms
  claim: Product and extension criteria alone close the non-scalar theorem.
  broken_step: Counterterms must pass scalar-contact projection and
    finite-window/weight Roos compatibility.
  evidence_type: proof_gap
  evidence_ref: tate-T1-weighted-completion.tex:2398-2582;
    appendix-factorization-current-conventions.tex:1703-1728
  minimal_heal: Carry the sigma_sc gate, eta^reg quotient, and Roos
    cocycle formulas with the graph theorem.

- id: A267-05
  severity: 3
  status: healed
  lens: source support
  target: Hormander citation boundary
  claim: Hormander proves the manuscript's wavefront current graph theorem.
  broken_step: The source fixture says Hormander supports only operation
    criteria, with primary page anchors still partly unverified.
  evidence_type: source_boundary
  evidence_ref: references/primary-sources/hormander-wavefront-source-anchors-2026-04-30.md
  minimal_heal: Cite Hormander only for operation criteria; keep graph
    spaces, kernels, counterterms, scalar quotient, eta, and Roos internal.
```

## TeX-Ready Insertion

The insertion below is justified but not inscribed because Agent 267's
writable surface is report-only.

```tex
\begin{prop}[Graphwise current product criterion]
\label{prop:app-graphwise-current-product-criterion}
  Let \(B_\bullet\), \(X_\Gamma^0(I)\), and
  \(e_\Gamma:X_\Gamma^0(I)\to I^r\) be as in
  Definition~\ref{def:app-graphwise-wavefront-current-package}.  If
  \(N_{e_\Gamma}\cap\mathrm{WF}(B^\boxtimes)=\emptyset\), then
  \(B_\Gamma=e_\Gamma^*B^\boxtimes\) is defined and
  \[
    \mathrm{WF}(B_\Gamma)\subset
    e_\Gamma^\#\mathrm{WF}(B^\boxtimes).
  \]
  If moreover, for every Hadamard coefficient
  \(K^M_{\Gamma,\alpha}\),
  \[
    (\mathrm{WF}(K^M_{\Gamma,\alpha})
    +\mathrm{WF}(B_\Gamma))\cap0=\emptyset,
  \]
  then \(K^M_{\Gamma,\alpha}B_\Gamma\) is canonical.  Finite scaling
  degree along every graph collision diagonal gives extensions whose
  ambiguity is supported on
  \(\Delta\cap\operatorname{supp}(B_\Gamma)\) and is a finite sum of
  normal derivatives of \(\delta_\Delta\) of order at most
  \(\max\{-1,\lfloor\operatorname{sd}_\Delta-c_\Delta\rfloor\}\).  Proper
  support for the final projection gives the displayed pushforward
  wavefront bound.
\end{prop}
```

## Verification Commands

Commands run:

```bash
sed -n '1,240p' AGENTS.md
sed -n '1,240p' CLAUDE.md
sed -n '1,240p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,220p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,260p' references/primary-sources/hormander-wavefront-source-anchors-2026-04-30.md
sed -n '1,330p' references/primary-sources/local-costello-bv-kernel-source-anchors-2026-04-30.md
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

Changed and staged:

- `reconstitution/internal-wavefront-current-graph-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-267-internal-wavefront-current-graph-construction-push.md`

No other files were changed by Agent 267.
