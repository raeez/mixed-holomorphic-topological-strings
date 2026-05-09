# Agent 108 Bulk-to-Defect Kernel Construction

Status: coefficient-current kernel layer constructed; Costello graph/QME
kernel remains an explicit analytic obstruction problem.

## Stable Construction

The proved layer is the completed convolution habitat
\[
  \mathbf K^\bullet_{w,\partial,\hbar}(I)
  =
  \operatorname{Hom}_{\mathrm{cont}}\!\left(
    C^\bullet_{\mathrm{CE},\mathrm{cont}}
    (\mathfrak g^{w,\mathrm{cur}}_{\hbar,I}),
    \mathfrak Q^\bullet_{w,\partial,\hbar}(I)\right),
\]
with
\[
  d_{\mathbf K}T=d_{\mathrm{QME}}T-(-1)^{|T|}T\,d_{\mathrm{CE}},
  \qquad
  \operatorname{Curv}_{\mathbf K}(\kappa)
  =d_{\mathbf K}\kappa+\frac12[\kappa,\kappa]_{\mathbf K}.
\]

The canonical coefficient-current kernel is
\[
  \kappa^{\mathrm{coef}}_{\hbar,w,I}
  (u_{a(t)dt\otimes f})=\iota_I(B^w_f(a)),
  \qquad
  \kappa^{\mathrm{coef}}_{\hbar,w,I}(c_{B,\rho})
    =\iota_I(\Theta^w_\rho(B)).
\]
It is degree zero, continuous in the hbar-adic, scalar-contact, and
finite-window Mittag-Leffler topology, compatible with truncation
\(\pi_{M,N}\) and weight transport \(R^M_{w,w'}\), and reduces at
\(\hbar=0\) to the reduced current interface
\(\Phi_I^{\mathrm{cur}}\).

Inside the freely adjoined coefficient-current target, the generator
brackets are strict:
\[
  \{B^w_f(a),B^w_g(b)\}_{\hbar}=B^w_{\{f,g\}_{\hbar}}(ab),
\]
\[
  \{B^w_f(a),\Theta^w_\rho(B)\}_{\hbar}
    =\Theta^w_{\operatorname{ad}^{\vee}_{f,\hbar}\rho}(aB),
  \qquad
  \{\Theta^w_\rho(B),\Theta^w_\sigma(C)\}_{\hbar}=0.
\]

## Attack Ledger

```yaml
id: A1-108-01
severity: 2
status: healed
lens: Costello source admissibility
target: non-scalar Costello graph/QME realization
claim: Costello's BV/RG formalism supplies the current-valued target and bulk-to-defect kernel automatically.
broken_step: The Costello source fixture supports heat kernels, BV Laplacian, RG/QME, locality/counterterms, graph asymptotics, and obstruction calculus, but not the current-valued target, D'_c wavefront theorem, or bulk-to-defect kernel.
evidence_type: source_conflict
evidence_ref: references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:13-21, 160-196, 221-241
files_read: [references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md, reconstitution/swarm-2026-04-30-agent-102-costello-graph-qme-source.md]
tools_used: [sed, rg, nl]
confidence: high
blast_radius: Would promote an unsupported graph theorem.
minimal_heal: Construct only the coefficient-current kernel and name the analytic residual.
residual: D'_c graph wavefront/counterterm theorem and non-scalar QME vanishing.
deciding_evidence: A finite-window distributional graph theorem with compatible counterterms.
```

```yaml
id: A1-108-02
severity: 2
status: healed
lens: convolution/MC precision
target: appendix-factorization-current-conventions.tex non-scalar lift datum
claim: A map \(d_{\mathrm{QME}}\kappa+\frac12[\kappa,\kappa]\) is a precise MC curvature for the CE source.
broken_step: The CE differential contribution must be present in the convolution differential; on generators it is the source-bracket subtraction in the defect formulas.
evidence_type: proof_gap
evidence_ref: appendix-factorization-current-conventions.tex:441-478, 636-704
files_read: [appendix-factorization-current-conventions.tex, main.tex, tate-T1-weighted-completion.tex]
tools_used: [nl, rg]
confidence: high
blast_radius: Curvature classes would be attached to the wrong complex.
minimal_heal: Add \(\mathbf K\), \(d_{\mathbf K}\), and \(\operatorname{Curv}_{\mathbf K}\); replace the obstruction formulas by convolution curvature and evaluation on finite CE inputs.
residual: None for the coefficient-current layer.
deciding_evidence: Local TeX diff plus generator-level proof.
```

```yaml
id: A1-108-03
severity: 2
status: healed
lens: distributional defect analysis
target: arbitrary \(B\in\mathcal D'_c(I)\) in Costello graph weights
claim: The coefficient-current map for \(B\in\mathcal D'_c(I)\) is already a Costello graph kernel.
broken_step: The coefficient algebra accepts compactly supported distributions, but graph products with finite-scale propagators require wavefront transversality, small-diagonal extension, and compatible counterterms.
evidence_type: unsupported
evidence_ref: main.tex:6823-6832, 6875-6890; references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:177-196
files_read: [main.tex, references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md]
tools_used: [nl, rg]
confidence: high
blast_radius: Would confuse a formal current coefficient with a renormalized local functional.
minimal_heal: State the exact analytic theorem; permit graph-level proof only for regular density restriction until that theorem exists.
residual: The named D'_c wavefront/counterterm theorem.
deciding_evidence: A proof that all defect-current-labelled finite-window graph distributions renormalize compatibly.
```

## Repairs Made

- Added `def:app-bulk-defect-convolution-habitat`.
- Added `prop:app-bulk-defect-kernel-layer`.
- Replaced the appendix obstruction curvature displays with
  \(\operatorname{Curv}_{\mathbf K}(\kappa_{\hbar,w,I})\) and made the
  residual class evaluation-based on fixed finite CE inputs.

## Proof Status

Proved:

- source and target habitat, including topology and filtration;
- degree-zero coefficient-current kernel by the completed symmetric
  algebra universal property;
- finite-window truncation and admissible weight-transport compatibility;
- reduction to the already proved algebraic current interface;
- strict coefficient-current bracket identities;
- orderwise obstruction class and finite-window counterterm criterion
  after lower orders have been solved.

Not proved:

- genuine Costello graph lift for arbitrary compactly supported
  distribution labels \(B\);
- wavefront/counterterm/RG compatibility for \(\mathcal D'_c\)-valued
  defect coefficients;
- vanishing of the scalar-lift tower \(o_{\sigma,w}^{(r)}(I)\);
- vanishing of the reduced non-scalar class in
  \(H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})\);
- realization of \(\Theta^w_\rho(B)\) inside finite polynomial open BV
  observables.

## Residual Theorem

For every finite window \(M\), every Costello graph \(\Gamma\), and every
defect-current label \(B_j\in\mathcal D'_c(I)\), prove that the
distribution obtained from the finite-scale propagators
\(P_{\epsilon,L}^{w,M}\) and the pushed-forward currents \(i_*B_j\)
satisfies wavefront transversality, admits a local extension across the
small diagonals, and has counterterms
\[
  C_{\Gamma,w}^{M}(\epsilon;B_\bullet)
\]
compatible with interval extension by zero, finite-window truncation, and
admissible weight transport.  This is the missing analytic/construction
theorem.  Without it, the graph-level theorem must restrict \(B\) to
regular compactly supported densities.

## Verification

Commands run before patching:

- `git status --short`
- `sed -n` on the attack-heal protocol, repo instructions, prior reports,
  Costello source fixture, and Vol III frontier file
- `rg -n` and `nl -ba` over the target appendix, unreduced QME appendix,
  `main.tex`, `tate-T1-weighted-completion.tex`,
  `tate-P1-hadamard-mittag-leffler.tex`, `theorem-lanes.tex`, and
  `open-obligations.tex`

Post-patch checks:

- `git diff --check -- appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-108-bulk-defect-kernel-construction.md`
  passed.
- `grep -n '[[:blank:]]$' reconstitution/swarm-2026-04-30-agent-108-bulk-defect-kernel-construction.md appendix-factorization-current-conventions.tex`
  returned no hits.
- Label and curvature scans found
  `def:app-bulk-defect-convolution-habitat`,
  `prop:app-bulk-defect-kernel-layer`, and
  `\operatorname{Curv}_{\mathbf K}` in the target appendix.

No full `make pdf` was run because the checkout has concurrent edits and
the build writes `out/main.pdf`, outside this agent's writable surface.
