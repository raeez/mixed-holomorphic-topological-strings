# Agent 179 - Equivariant QME Kernel Attack

Status: patched owned appendix surface.  No commit.

## Stable Core

The normal \(\Omega\)-background is a localization datum, not a QME
solution.  It supplies
\[
  V_\Omega=
  \varepsilon_s s\partial_s
  +\varepsilon_1z_1\partial_{z_1}
  +\varepsilon_2z_2\partial_{z_2},
  \qquad
  Q_\Omega=Q+\iota_{V_\Omega},
  \qquad
  Q_\Omega^2=L_{V_\Omega}.
\]
All obstruction complexes must therefore be taken on the
\(T_\Omega\)-invariant/basic subcomplex, or else the first obstruction is
already \(L_{V_\Omega}\).

The appendix now requires a normal \(\Omega\)-equivariant finite-window
Costello kernel datum before any equivariant QME claim can be formed.  The
datum includes:

- the brane-preserving normal torus on
  \(N_LX=\R_s\oplus\C_{z_1}\oplus\C_{z_2}\), with \(t\) fixed;
- the localized coefficient ring
  \[
    R_\Omega=
    \C[\varepsilon_s,\varepsilon_1,\varepsilon_2,\hbar_\omega]
      [(\varepsilon_s\varepsilon_1\varepsilon_2)^{-1}],
    \qquad
    \operatorname{wt}(\hbar_\omega)=\varepsilon_1+\varepsilon_2;
  \]
- the off-self-dual weighted Hamiltonian bracket
  \[
    \{f,g\}_\Omega=
    \hbar_\omega(\partial_{z_1}f\,\partial_{z_2}g
    -\partial_{z_2}f\,\partial_{z_1}g);
  \]
- normal contractions
  \[
    Q_\Omega h_\chi+h_\chi Q_\Omega
    =
    \operatorname{id}-\operatorname{pr}_{\chi=0}
  \]
  on nonzero normal-weight summands;
- an equivariant propagator satisfying
  \[
    [Q_\Omega,P^{w,M}_{\epsilon,L,\Omega}]
    =
    K^{w,M}_{\epsilon,\Omega}-K^{w,M}_{L,\Omega},
    \qquad
    [L_{V_\Omega},P^{w,M}_{\epsilon,L,\Omega}]=0;
  \]
- a named normal-localization normalization \(\nu_\Omega\), with Euler and
  residue conventions not silently identified;
- equivariant local counterterms, a filtered scalar projection, and a
  Hom-valued graph kernel.

## Obstruction Formulas

Scalar projection is controlled by the relative Hom defects
\[
  \delta^{(0)}_{\Omega,\sigma,M}
  =
  d_{\mathrm{CE},\Omega}\sigma_{\mathrm{sc},\Omega,M}
  -\sigma_{\mathrm{sc},\Omega,M}d_{\operatorname{gr},\Omega},
\]
and, after choosing a filtered lift \(s_{\Omega,M}\),
\[
  \mathfrak o^{(r)}_{\Omega,\sigma,M}
  \in
  H^1\!\left(
    \operatorname{Hom}_{T_\Omega,-r}
    (\operatorname{gr}_{F}\mathfrak Q^\bullet_{\mathcal G,\Omega,M},
     S^\bullet_{\Omega,M})
  \right).
\]
These must vanish successively before the non-scalar kernel complex
\[
  \mathcal K^\bullet_{\mathrm{ns},\Omega,M}
  =
  \ker\widehat\sigma_{\mathrm{sc},\Omega,M}
\]
is defined as a \(d_{M,\Omega}\)-complex.

The order-\(n\) non-scalar residual is
\[
\begin{aligned}
  R^{\mathrm{ns}}_{n,\Omega,M}
    =
  [\hbar^n]\bigl(
    &\operatorname{Curv}_{\mathbf K,\Omega,M}
      (\kappa^M_{\mathcal G,\Omega,w,I})
    +d_{M,\Omega}C_{<n,\Omega,M} \\
    &+\frac12\{C_{<n,\Omega,M},C_{<n,\Omega,M}\}_{\hbar,M,\Omega}
  \bigr).
\end{aligned}
\]
The scalar gate is
\[
  \mathfrak s_{n,\Omega,M}
  =
  \widehat\sigma_{\mathrm{sc},\Omega,M}
  (R^{\mathrm{ns}}_{n,\Omega,M}).
\]
Only after \(\mathfrak s_{n,\Omega,M}=0\) does the class
\[
  \mathfrak o^{\mathrm{ns}}_{n,\Omega,M}
  =
  [R^{\mathrm{ns}}_{n,\Omega,M}]
  \in
  H^1(\mathcal K^\bullet_{\mathrm{ns},\Omega,M})
\]
exist.  Counterterms require this inverse-limit \(H^1\) class and the
Milnor \(\varprojlim^1H^0\) primitive-compatibility class
\(\lambda_{n,\Omega}\) to vanish.

For centrality, the new equivariant row is
\[
  R^{\mathrm{cent}}_{x,y,\Omega,M}
  =
  \operatorname{Curv}_{\mathbf K,\Omega,M}
  (\kappa^M_{\mathcal G,\Omega,w,I})(x\wedge y).
\]
A \(Q_\Omega\)-centrality homotopy is an invariant primitive
\[
  R^{\mathrm{cent}}_{x,y,\Omega,M}
  +d_{M,\Omega}H^\Omega_{x,y,M}=0,
  \qquad
  L_{V_\Omega}H^\Omega_{x,y,M}=0.
\]
Before passing to invariants, the secondary obstruction is
\[
  \ell^{\mathrm{cent}}_{x,y,\Omega,M}
  =
  [L_{V_\Omega}H_{x,y,\Omega,M}].
\]

## Valid Attacks

```yaml
- id: A1-179-01
  severity: 1
  status: healed
  lens: Omega/QME separation
  target: equivariant Costello brane-defect kernel claim
  claim: The normal Omega layer solves the brane-defect QME.
  broken_step: Q_Omega gives weights and contractions, while graph curvature still needs an equivariant propagator, counterterms, scalar projection, and non-scalar obstruction vanishing.
  evidence_type: proof_gap
  evidence_ref: def:app-normal-omega-costello-kernel-datum; thm:app-equivariant-brane-defect-qme-criterion
  confidence: high
  blast_radius: A false QME theorem would erase all graph/counterterm obstruction classes.
  minimal_heal: Add the full equivariant finite-window datum and state the H^1/lim^1 criterion for QME closure.
  residual: Construct the actual equivariant graph package and compute the classes.

- id: A1-179-02
  severity: 1
  status: healed
  lens: Cartan differential
  target: Q_Omega obstruction complex
  claim: Q_Omega is a differential on all fields.
  broken_step: Q_Omega^2=L_{V_Omega}; cohomology requires invariant/basic fields or a separate homotopy killing L_V.
  evidence_type: algebraic_identity
  evidence_ref: def:app-normal-omega-costello-kernel-datum; prop:app-qomega-centrality-homotopy-criterion
  confidence: high
  blast_radius: Non-invariant primitives would not define Q_Omega-homotopies.
  minimal_heal: Restrict complexes to invariant/basic subcomplexes and add the secondary L_V centrality obstruction.
  residual: If a future package works non-basic, it must construct the corresponding L_V-homotopy.

- id: A1-179-03
  severity: 1
  status: healed
  lens: scalar projection
  target: equivariant scalar gate
  claim: Scalar-shadow vanishing in the balanced branch automatically extends to the Omega graph habitat.
  broken_step: The scalar projection must be a filtered chain map after the Omega differential, localization normalization, and graph counterterms are inserted.
  evidence_type: proof_gap
  evidence_ref: thm:app-equivariant-brane-defect-qme-criterion
  confidence: high
  blast_radius: Kernel H^1 classes would be formed before the kernel is a complex.
  minimal_heal: Add delta^(0) and higher Hom obstruction classes for the equivariant scalar projection.
  residual: Compute these Hom classes for any concrete equivariant graph/counterterm habitat.

- id: A1-179-04
  severity: 2
  status: healed
  lens: normalization
  target: residue/Euler localization convention
  claim: The residue and Euler conventions can be interchanged silently.
  broken_step: Scalar-contact coefficients and trace normalizations depend on the chosen normal localization factor.
  evidence_type: missing_hypothesis
  evidence_ref: def:app-normal-omega-costello-kernel-datum
  confidence: high
  blast_radius: Wrong normal factor changes scalar gates and obstruction representatives.
  minimal_heal: Require a named normalization nu_Omega and a comparison map before using a residue convention as Euler localization.
  residual: Supply the comparison theorem if the manuscript uses residue normalization.
```

## Files Changed

- `appendix-unreduced-bv-qme.tex`
- `reconstitution/swarm-2026-04-30-agent-179-equivariant-qme-kernel-0957.md`

## Checks

Commands run:

```bash
git diff --check -- appendix-unreduced-bv-qme.tex
rg -n "app-normal-omega-costello-kernel-datum|app-equivariant-brane-defect-qme-criterion|app-qomega-centrality-homotopy-criterion|app-qomega-centrality-homotopy-equation|app-omega" appendix-unreduced-bv-qme.tex
rg -n "label\\{([^}]*)\\}" appendix-unreduced-bv-qme.tex | sed 's/.*label{//; s/}.*//' | sort | uniq -d
rg -n "Omega.*(solves|proves).*QME|QME.*(solved|automatic|automatically)|normal .*automatic" appendix-unreduced-bv-qme.tex
chktex -q appendix-unreduced-bv-qme.tex
lacheck appendix-unreduced-bv-qme.tex
```

Results:

- `git diff --check` passed for the appendix.
- Label scan found the new labels and no duplicate labels.
- The automatic-QME wording scan returned no hits.
- `chktex` and `lacheck` still report the existing appendix warning class.
  Filtered checks on the new warning lines show no remaining new lacheck
  warning after the normalization punctuation repair.  `chktex` still emits
  standard formula-style warnings on the new displayed bracket expressions
  and label-placement warnings already present throughout the file.
- `make pdf` was not run because the assigned writable surface excludes the
  tracked build artifact.

## Residual Obligations

- Construct the actual \(T_\Omega\)-equivariant finite-scale propagator and
  prove the displayed homotopy identity in the weighted Tate category.
- Choose Euler or residue normalization and prove any comparison map used.
- Populate the equivariant graph/counterterm table with row values, signs,
  marker transports, scalar gates, and truncation coefficients.
- Kill the scalar-projection Hom obstruction tower.
- Compute the non-scalar \(H^1\) classes and the Milnor
  \(\varprojlim^1H^0\) primitive-compatibility classes.
- Supply invariant \(Q_\Omega\)-centrality primitives, or compute the
  secondary \(L_{V_\Omega}\) obstruction.
