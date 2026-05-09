# Agent 142 Local Kernel Geometry Audit

Status: repaired the owned appendix surface for local-geometry leakage.
No compact Calabi-Yau, CoHA, quintic, OSV/GV, Abel-Jacobi, Igusa, BKM,
or global BCOV statement enters the local theorem surface.

## Scope

Owned writable paths:

- `appendix-factorization-current-conventions.tex`
- `reconstitution/swarm-2026-04-30-agent-142-local-kernel-geometry-audit.md`

Read-only context used:

- `CLAUDE.md`
- ecosystem attack-heal protocol files
- Vol II `chriss-ginzburg-rectify` skill
- `local-dictionary.tex`
- `main.tex`
- `appendix-unreduced-bv-qme.tex`
- `tate-T1-weighted-completion.tex`
- reports 108, 116, 121, 134, 137

## Valid Attacks

```yaml
id: A1-142-01
severity: 2
status: healed
lens: local-geometry habitat
target: appendix-factorization-current-conventions.tex, opening and current definitions
claim: The factorization-current interface is visibly local without restating the base geometry.
broken_step: The appendix named interval currents and Hamiltonian labels, but did not explicitly bind the whole layer to \(\R^2_{\mathrm{top}}\times\widehat{\C^2}_{0,\mathrm{hol}}\), the brane interval, and the formal symplectic disk.
evidence_type: line_reference
evidence_ref: appendix-factorization-current-conventions.tex:23-34, 37-50
minimal_heal: Add the local mixed HT geometry, interval/current direction, \(\mathfrak h=\C[[z_1,z_2]]/\C\cdot1\), \(\Omega_{\mathrm{loc}}\), and the Poisson bracket at the start of the appendix and in the source definition.
residual: None for the reduced current source.
```

```yaml
id: A1-142-02
severity: 2
status: healed
lens: local Calabi-Yau/unimodularity
target: kernel definitions and principal-part duality
claim: The word Calabi-Yau cannot leak compact target meaning into the kernel layer.
broken_step: The current dual used \(\operatorname{Res}(\rho f)\) and Matlis coadjoint action without a theorem-grade statement of where the local volume/symplectic datum enters.
evidence_type: proof_gap
evidence_ref: appendix-factorization-current-conventions.tex:97-187
minimal_heal: Add `prop:app-local-unimodular-current-kernel-input`, proving that the only Calabi-Yau input is \((\widehat{\C^2}_0,dz_1\wedge dz_2)\).
residual: None for the coefficient-current layer.
```

```yaml
id: A1-142-03
severity: 2
status: healed
lens: Costello graph locality
target: bulk-to-defect, regular-density, and wavefront graph propositions
claim: Finite-window kernels and wavefront labels are automatically understood as local.
broken_step: The graph statements referred to Costello finite-window packages and \(X_\Gamma(I)\), but did not explicitly say the windows are formal holomorphic Hamiltonian windows and that wavefront admissibility is local on the brane interval and formal disk coefficient sector.
evidence_type: unsupported
evidence_ref: appendix-factorization-current-conventions.tex:577-684, 774-866, 945-1101
minimal_heal: Add local mixed HT hypotheses, finite-window Hamiltonian-degree wording, and local microlocal boundary statements.
residual: Full \(\mathcal D'_c(I)\) graph theorem remains false without additional wavefront/counterterm data.
```

```yaml
id: A1-142-04
severity: 2
status: healed
lens: external-comparison firewall
target: obstruction proposition
claim: A non-scalar graph/QME theorem could be read as a compact/global comparison theorem.
broken_step: The obstruction theorem did not explicitly quarantine compact Calabi-Yau, CoHA, global BCOV, and cross-volume consequences.
evidence_type: unsupported
evidence_ref: appendix-factorization-current-conventions.tex:1164-1241
minimal_heal: State that the conditions are only for the local mixed HT brane-defect model and do not assert compact Calabi-Yau, CoHA, global BCOV, or cross-volume comparison theorems.
residual: Matched-conventions transfer remains only in the firewall section of `main.tex`.
```

## Repaired Propositions and Labels

- Added `prop:app-local-unimodular-current-kernel-input`.
- Strengthened `def:app-factorization-current-source`.
- Strengthened `def:app-factorization-current-dual`.
- Strengthened `def:app-unreduced-nonscalar-current-lift-datum`.
- Strengthened `def:app-bulk-defect-convolution-habitat`.
- Strengthened `prop:app-bulk-defect-kernel-layer`.
- Strengthened `prop:app-regular-density-costello-graph-kernel`.
- Strengthened `def:app-wavefront-admissible-defect-labels`.
- Strengthened `prop:app-wavefront-admissible-costello-graph-kernel`.
- Strengthened `prop:app-nonscalar-current-lift-obstructions`.

## Exact Local Formulas

Local formal datum:
\[
  \left(\widehat{\C^2}_0,\Omega_{\mathrm{loc}}\right),
  \qquad
  \Omega_{\mathrm{loc}}=dz_1\wedge dz_2 .
\]

Hamiltonian algebra and bracket:
\[
  \mathfrak h=\C[[z_1,z_2]]/\C\cdot1,
  \qquad
  \{f,g\}
  =
  \partial_{z_1}f\,\partial_{z_2}g
  -\partial_{z_2}f\,\partial_{z_1}g .
\]

Hamiltonian vector field:
\[
  \iota_{X_f}\Omega_{\mathrm{loc}}=-df,
  \qquad
  X_f=(\partial_{z_1}f)\partial_{z_2}
      -(\partial_{z_2}f)\partial_{z_1}.
\]

Unimodularity:
\[
  \operatorname{div}_{\Omega_{\mathrm{loc}}}X_f
  =
  -\partial_{z_1}\partial_{z_2}f
  +\partial_{z_2}\partial_{z_1}f
  =0 .
\]

Residue pairing:
\[
  \operatorname{Res}_0
  \left(z_1^{-i-1}z_2^{-j-1}dz_1dz_2\,z_1^mz_2^n\right)
  =
  \delta_{i,m}\delta_{j,n}.
\]

Current source:
\[
  \mathfrak h_I=\Omega^\bullet_c(I)\widehat\otimes\mathfrak h,
  \qquad
  \mathfrak g_I=\mathfrak h_I\ltimes
  (\mathcal D'_c(I)\widehat\otimes\mathcal P)[1].
\]

Weighted current source:
\[
  \mathfrak g^{w,\mathrm{cur}}_{\hbar,I}
  =
  (\Omega^\bullet_c(I)\widehat\otimes\mathfrak h_{w,\hbar})
  \ltimes
  (\mathcal D'_c(I)\widehat\otimes
  \mathfrak h^{\vee,w}_{\hbar,\mathrm{cont}})[1].
\]

Coefficient-current kernel:
\[
  \kappa^{\mathrm{coef}}_{\hbar,w,I}
  (u_{a(t)dt\otimes f})=\iota_I(B_f^w(a)),
  \qquad
  \kappa^{\mathrm{coef}}_{\hbar,w,I}(c_{B,\rho})
  =\iota_I(\Theta_\rho^w(B)).
\]

Wavefront relation:
\[
  \mathcal D'_{c,\mathrm{WF}}(I;\Gamma,M)
  \subset(\mathcal D'_c(I))^r,
\]
defined by non-characteristic incidence maps, proper support,
Hormander product transversality, finite scaling degree on graph
collision diagonals, and final pushforward into the brane-defect
local-functional wavefront class.

## Verification Commands

```bash
git diff --check -- appendix-factorization-current-conventions.tex
grep -n '[[:blank:]]$' appendix-factorization-current-conventions.tex
rg -n "label\\{([^}]*)\\}" appendix-factorization-current-conventions.tex | sed 's/.*label{//; s/}.*//' | sort | uniq -d
rg -n -e 'local mixed' -e 'formal-local' -e 'Omega_' -e 'compact Calabi' -e 'global BCOV' -e 'CoHA' -e 'quintic' -e 'OSV' -e 'Abel' -e 'Igusa' -e 'BKM' -e 'wavefront-admissible' -e 'finite Hamiltonian window' appendix-factorization-current-conventions.tex
rg -n "Agent|swarm|prior draft|previous draft|phase|version" appendix-factorization-current-conventions.tex
chktex -q appendix-factorization-current-conventions.tex
```

Results:

- `git diff --check` passed.
- trailing-whitespace grep returned no hits.
- duplicate-label scan returned no hits.
- compact/global scan found only explicit quarantine language.
- process-language scan found only ordinary mathematical uses of
  "versions"; no manuscript process language was introduced.
- `chktex` returned style warnings already typical for this appendix
  class: label placement, dash length, math-spacing, and citation
  non-breaking-space warnings.  No fatal TeX error was reported.

No full `make pdf` was run because the checkout has concurrent staged
manuscript edits and the build writes generated output outside this
agent's assigned writable surface.

## Files Changed and Staged

- `appendix-factorization-current-conventions.tex`
- `reconstitution/swarm-2026-04-30-agent-142-local-kernel-geometry-audit.md`

Both owned paths were staged after scoped verification.  No other paths
were staged by Agent 142.

## Remaining Theorem Obligations

- Prove or continue to restrict the full \(\mathcal D'_c(I)\) graph
  extension.  Coincident singular labels still require additional
  renormalization data.
- Construct the filtered scalar projection on any enlarged
  graph/counterterm habitat before claiming a reduced non-scalar
  obstruction class.
- Prove vanishing of the residual
  \(H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})\) class and
  the compatible \(\varprojlim^1H^0\) primitive obstruction.
- A concrete finite-window Costello package must still supply its actual
  graph table, counterterms, incidence coefficients, and weight-transport
  compatibilities.
