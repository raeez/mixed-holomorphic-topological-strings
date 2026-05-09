# Agent 116 Regular-Density Graph Kernel

Status: regular-density Costello graph kernel layer inscribed.  The
arbitrary \(\mathcal D'_c\)-label extension remains an analytic theorem
obligation, not a claimed result.

## Owned Paths

- `appendix-factorization-current-conventions.tex`
- `reconstitution/swarm-2026-04-30-agent-116-regular-density-graph-kernel.md`

## Stable Construction

The new proposition is
`appendix-factorization-current-conventions.tex:642`,
`prop:app-regular-density-costello-graph-kernel`.

It replaces the arbitrary compactly supported distributional cotangent
labels by the regular-density subspace
\[
  \mathcal D^{\mathrm{reg}}_c(I)
  =
  \{b(t)dt: b\in C_c^\infty(I)\}
  \subset \mathcal D'_c(I)
\]
and restricts the current source to
\[
  \mathfrak g^{w,\mathrm{reg}}_{\hbar,I}
  =
  (\Omega^\bullet_c(I)\widehat\otimes\mathfrak h_{w,\hbar})
  \ltimes
  (\mathcal D^{\mathrm{reg}}_c(I)\widehat\otimes
   \mathfrak h^{\vee,w}_{\hbar,\mathrm{cont}})[1].
\]

Under the already named regulator-admissible finite-scale Costello
brane-defect calculus, every fixed finite-window graph with regular
external cotangent labels has a smooth finite-scale graph weight, a local
Costello counterterm expansion, and a renormalized regular-density
brane-defect local functional.  The graph weights commute with interval
extension by zero, finite-window truncation, and admissible weight
transport.

This is a graphwise analytic lift of Agent 108's coefficient-current
kernel.  It is not a proof of the non-scalar QME.  The curvature still
lands in the finite-window obstruction tower of
`thm:wt-nonscalar-counterterm-criterion` once a filtered scalar projection
has been constructed on the chosen graph/counterterm habitat.

## Attack Ledger

```yaml
id: A1-116-01
severity: 2
status: healed
lens: distributional overclaim
target: appendix-factorization-current-conventions.tex prop:app-bulk-defect-kernel-layer residual
claim: Agent 108's coefficient-current kernel gives the Costello graph kernel for all \(B\in\mathcal D'_c(I)\).
broken_step: Costello's source package supplies finite-scale heat kernels, graph locality, counterterms, and obstruction calculus, but not a theorem multiplying arbitrary compactly supported defect distributions with graph propagators and extending across graph diagonals.
evidence_type: source_conflict
evidence_ref: references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:177-196; reconstitution/swarm-2026-04-30-agent-108-bulk-defect-kernel-construction.md:88-106
files_read: [appendix-factorization-current-conventions.tex, references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md, reconstitution/swarm-2026-04-30-agent-108-bulk-defect-kernel-construction.md]
tools_used: [rg, sed, nl]
confidence: high
blast_radius: Would promote an unsupported \(\mathcal D'_c\) wavefront/counterterm theorem.
minimal_heal: Restrict the graph theorem to \(C_c^\infty(I)dt\) labels and state the exact \(\mathcal D'_c\) extension theorem.
residual: Arbitrary compactly supported distributional labels.
deciding_evidence: A Hormander transversality, small-diagonal extension, and compatible counterterm theorem for \(\mathcal D'_c(I)\)-labelled defect graphs.
```

```yaml
id: A1-116-02
severity: 2
status: healed
lens: regular-density analytic sufficiency
target: regular compactly supported density labels
claim: Even regular compactly supported density labels must remain analytic debt.
broken_step: At positive heat-kernel scale the propagator is smooth; multiplication by compactly supported smooth densities produces smooth compact graph integrands. As \(\epsilon\to0\), smooth multipliers do not enlarge wavefront sets, so Costello/Hadamard locality supplies the same local counterterm expansion graph by graph.
evidence_type: proof
evidence_ref: references/primary-sources/costello-renormalisation-bv-0706.1533.txt:77-90, 1746-1807, 3544-3569, 3660-3685; tate-P1-hadamard-mittag-leffler.tex:135-187, 240-273
files_read: [references/primary-sources/costello-renormalisation-bv-0706.1533.txt, tate-P1-hadamard-mittag-leffler.tex, tate-T1-weighted-completion.tex]
tools_used: [nl, rg]
confidence: high
blast_radius: Would leave a provable regular-density theorem uninscribed.
minimal_heal: Add `prop:app-regular-density-costello-graph-kernel` with source/target, finite-scale smoothness, renormalized counterterms, and compatibility.
residual: Summability and QME vanishing remain exactly the existing obstruction tower.
deciding_evidence: The finite-scale smoothness proof plus Costello/Hadamard graphwise counterterm theorem.
```

```yaml
id: A1-116-03
severity: 2
status: healed
lens: QME overclosure
target: new regular-density graph proposition
claim: A regular-density graph lift solves the non-scalar Costello QME.
broken_step: The regular-density argument removes the extra cotangent-label wavefront problem only. It does not construct a filtered scalar projection on the full graph/counterterm habitat and does not kill the residual class in \(H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})\).
evidence_type: proof_gap
evidence_ref: main.tex:7364-7573; tate-T1-weighted-completion.tex:980-1086; appendix-unreduced-bv-qme.tex:937-1075
files_read: [main.tex, tate-T1-weighted-completion.tex, appendix-unreduced-bv-qme.tex, theorem-lanes.tex]
tools_used: [nl, rg]
confidence: high
blast_radius: Would turn a graph-kernel existence statement into a false QME theorem.
minimal_heal: State the curvature consequence conditionally on an available filtered scalar projection and point it back to `thm:wt-nonscalar-counterterm-criterion`.
residual: Scalar-projection lift and non-scalar \(H^1/\varprojlim^1\) vanishing.
deciding_evidence: Compatible finite-window counterterms killing the curvature class after scalar projection exists.
```

```yaml
id: A1-116-04
severity: 3
status: healed
lens: finite-window compatibility
target: graph-level lift across weighted windows
claim: A regular-density graph lift can be stated without finite-window and weight-transport equations.
broken_step: The target obstruction tower is a strict finite-window Mittag-Leffler system. A graph kernel that does not commute with \(\pi_{M,N}\) and \(R^M_{w,w'}\) would not define an element of the completed convolution habitat.
evidence_type: line_reference
evidence_ref: appendix-factorization-current-conventions.tex:441-478, 510-532; tate-T1-weighted-completion.tex:604-760, 932-978
files_read: [appendix-factorization-current-conventions.tex, tate-T1-weighted-completion.tex]
tools_used: [nl, rg]
confidence: high
blast_radius: Would make the theorem unusable by the existing counterterm criterion.
minimal_heal: Add explicit \(\pi_{M,N}\) and \(R^M_{w,w'}\) compatibility equations in the proposition.
residual: None for regular-density finite-window compatibility.
deciding_evidence: Scoped TeX diff and label scan.
```

## Repairs Made

- Added `prop:app-regular-density-costello-graph-kernel`.
- Defined the regular source
  \(\mathfrak g^{w,\mathrm{reg}}_{\hbar,I}\) and the restricted
  convolution habitat.
- Proved finite-scale smoothness for regular density labels and graphwise
  renormalized local counterterms under the existing regulator-admissible
  Costello brane-defect calculus.
- Added finite-window truncation and admissible weight-transport
  compatibility equations.
- Stated the theorem boundary: no scalar-projection lift, no residual
  non-scalar QME vanishing, and no arbitrary \(\mathcal D'_c\) extension.

## Verification

Commands run before inscription:

- `git status --short`
- `sed -n` on `CLAUDE.md`, `AGENTS.md`, the attack-heal protocols, and
  the Vol II rectification skill.
- `nl -ba` / `sed -n` on `appendix-factorization-current-conventions.tex`,
  `main.tex`, `tate-T1-weighted-completion.tex`,
  `tate-P1-hadamard-mittag-leffler.tex`,
  `appendix-unreduced-bv-qme.tex`, `theorem-lanes.tex`,
  `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md`,
  and the reports for Agents 102 and 108.
- `nl -ba` on the Costello local mirror anchors for heat kernels,
  regularized BV, counterterms, graph asymptotics, and local graph
  locality.

Post-patch checks:

- `git diff --check -- appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-116-regular-density-graph-kernel.md`
  passed.
- `grep -n '[[:blank:]]$' appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-116-regular-density-graph-kernel.md`
  returned no hits.
- Label scan found `prop:app-regular-density-costello-graph-kernel` at
  `appendix-factorization-current-conventions.tex:643`.
- Scoped `git status --short -- appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-116-regular-density-graph-kernel.md`
  showed only the assigned appendix and this new report before staging.
- After `git add appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-116-regular-density-graph-kernel.md`,
  `git diff --cached --check -- appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-116-regular-density-graph-kernel.md`
  passed.
- `git diff -- appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-116-regular-density-graph-kernel.md`
  returned empty after staging.
- `git diff --cached --name-only -- appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-116-regular-density-graph-kernel.md`
  listed exactly the two owned paths.

No full `make pdf` is planned: it writes `out/main.pdf`, outside the
assigned writable surface, and this checkout has concurrent staged
manuscript edits.

## Residual Theorem

For every finite window \(M\), every Costello graph \(\Gamma\), and every
compactly supported distributional defect label \(B_j\in\mathcal D'_c(I)\),
prove that the product of the finite-scale brane-defect propagator kernels
with the pushed-forward current labels satisfies Hormander wavefront
transversality, admits local extensions across all graph small diagonals,
and has counterterms
\[
  C_{\Gamma,w}^{M}(\epsilon;B_\bullet)
\]
compatible with interval extension by zero, finite-window truncation, and
admissible weight transport.  Only after this theorem is proved may the
regular-density graph kernel be extended to arbitrary
\(\mathcal D'_c(I)\)-labels.
