# Agent 121 D'_c Wavefront Extension

Status: arbitrary \(\mathcal D'_c(I)\) graph labels attacked.  A
wavefront-admissible distributional graph layer is inscribed, including a
one-sided conormal class strictly beyond smooth compact densities.  The
full \(\mathcal D'_c(I)\) extension is false for the current Costello
graph products without extra renormalization data.

## Owned Paths

- `appendix-factorization-current-conventions.tex`
- `reconstitution/swarm-2026-04-30-agent-121-Dc-wavefront-extension.md`

## Stable Construction

Added `def:app-wavefront-admissible-defect-labels` and
`prop:app-wavefront-admissible-costello-graph-kernel`.

The definition is graphwise and finite-windowed.  For a graph
\(\Gamma\), window \(M\), and label tuple \(B_\bullet\), the admissible
relation
\[
  \mathcal D'_{c,\mathrm{WF}}(I;\Gamma,M)
  \subset(\mathcal D'_c(I))^r
\]
requires:

- non-characteristic incidence pullbacks/pushforwards and proper support;
- H\"ormander product transversality between graph Hadamard coefficients
  and the pushed-forward current \(B_\Gamma\);
- finite scaling degree along graph collision diagonals and local
  extension ambiguity supported on
  \(\Delta\cap\operatorname{supp}(B_\Gamma)\);
- final graph pushforward inside the brane-defect local-functional
  wavefront class.

The non-smooth positive class is
\[
  \mathcal D'_{c,\Lambda,\mathrm{fs}}(I)
  =
  \{B:\mathrm{WF}(B)\subset\Lambda,\ B
  \text{ has finite scaling degree along its singular support}\},
\]
where \(\Lambda\subset T^*I\setminus0\) is diagonal-admissible:
no finite nonempty sum of covectors in \(\Lambda\) is zero.  On an
oriented interval the half-cones \(\xi>0\) and \(\xi<0\) are
diagonal-admissible, so compactly supported one-sided conormal boundary
values give genuine distributional labels beyond regular densities.

## Attack Ledger

```yaml
id: A1-121-01
severity: 2
status: healed
lens: arbitrary distribution obstruction
target: appendix-factorization-current-conventions.tex residual D'_c theorem
claim: Agent 116's regular-density graph kernel can extend to every compactly supported distribution label.
broken_step: The graph product can require multiplication of a singular boundary propagator with coincident point-supported currents.
evidence_type: counterexample
evidence_ref: appendix-factorization-current-conventions.tex:1031-1043
files_read: [appendix-factorization-current-conventions.tex, reconstitution/swarm-2026-04-30-agent-116-regular-density-graph-kernel.md, references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md]
tools_used: [sed, rg, nl]
confidence: high
blast_radius: Would falsely promote a coefficient-current formalism into a full distributional Costello graph theorem.
minimal_heal: State the delta-on-diagonal obstruction and restrict graph products to a wavefront-admissible relation.
residual: A larger extension would need new renormalization choices for failed products, not just Costello's existing graph package.
deciding_evidence: H\"ormander product criterion for the one-edge graph with \(B_1=B_2=\delta_{t_0}\).
```

```yaml
id: A1-121-02
severity: 2
status: healed
lens: CE-source closure
target: proposed distributional source class
claim: A useful singular extension can be stated as all conormal distributions without tuple-level restrictions.
broken_step: Wavefront transversality is not a property of a single label alone; it depends on the graph, incidence maps, collision diagonals, and finite tuple. Repeating a singular label can destroy admissibility.
evidence_type: proof_gap
evidence_ref: appendix-factorization-current-conventions.tex:832-889
files_read: [appendix-factorization-current-conventions.tex, tate-P1-hadamard-mittag-leffler.tex]
tools_used: [sed, rg, nl]
confidence: high
blast_radius: Would define a source CE algebra whose symmetric powers are not graphwise defined.
minimal_heal: Define \(\mathcal D'_{c,\mathrm{WF}}(I;\Gamma,M)\) as a finite-tuple relation and state when a linear subspace gives an honest restricted CE source.
residual: Classifying all maximal linear subspaces is not needed for the graphwise theorem.
deciding_evidence: Tuple-level H\"ormander condition and the coincident delta counterexample.
```

```yaml
id: A1-121-03
severity: 3
status: healed
lens: nontrivial positive class
target: distributions beyond regular densities
claim: The only safe theorem-grade extension is the smooth-density class.
broken_step: One-sided wavefront cones cannot cancel conormals to collision diagonals, so their compact finite-scaling distributions satisfy the product criterion.
evidence_type: proof
evidence_ref: appendix-factorization-current-conventions.tex:892-913, 1019-1029
files_read: [appendix-factorization-current-conventions.tex, tate-P1-hadamard-mittag-leffler.tex, main.tex]
tools_used: [sed, rg, nl]
confidence: high
blast_radius: Would leave a real microlocal enlargement uninscribed.
minimal_heal: Add diagonal-admissible cones and the class \(\mathcal D'_{c,\Lambda,\mathrm{fs}}(I)\).
residual: The theorem still assumes the graph singularities are the ordinary conormals supplied by the finite-window Hadamard package.
deciding_evidence: Sum-zero conormal calculation for graph collision diagonals.
```

```yaml
id: A1-121-04
severity: 3
status: healed
lens: counterterm support
target: wavefront extension proof
claim: Product transversality alone proves the Costello counterterm extension.
broken_step: The graph product also needs finite scaling degree along each collision diagonal and a support statement for extension ambiguity.
evidence_type: proof_gap
evidence_ref: appendix-factorization-current-conventions.tex:868-874, 937-959, 997-1009
files_read: [appendix-factorization-current-conventions.tex, references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md, tate-P1-hadamard-mittag-leffler.tex]
tools_used: [sed, rg, nl]
confidence: high
blast_radius: Would produce products but not renormalized local counterterms.
minimal_heal: Add finite-scaling and counterterm support to the definition and proposition.
residual: Numerical scaling-degree bounds for each specific Hamiltonian brane graph remain part of the chosen regulator-admissible graph calculus.
deciding_evidence: Costello graph locality and the local support of extension ambiguities.
```

## Repairs Made

- Added a graphwise wavefront-admissible relation for distributional
  cotangent labels.
- Added the one-sided finite-scaling cone class
  \(\mathcal D'_{c,\Lambda,\mathrm{fs}}(I)\), including interval
  half-cone examples.
- Proved finite-scale well-definedness, small-\(\epsilon\)
  counterterm support, finite-window/weight compatibility, and the
  delta-on-diagonal obstruction to all of \(\mathcal D'_c(I)\).
- Kept the theorem graphwise.  It becomes a CE source only for subspaces
  whose every finite tuple satisfies the relation.

## Verification

Context and source reads:

- `sed -n` on `CLAUDE.md`, `AGENTS.md`, the attack-heal protocols, the
  Vol II rectification skill, and Vol III `FRONTIER.md`.
- `sed -n` / `nl -ba` on
  `appendix-factorization-current-conventions.tex`,
  `reconstitution/swarm-2026-04-30-agent-108-bulk-defect-kernel-construction.md`,
  `reconstitution/swarm-2026-04-30-agent-116-regular-density-graph-kernel.md`,
  `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md`,
  `main.tex`, `tate-P1-hadamard-mittag-leffler.tex`,
  `tate-T1-weighted-completion.tex`, `commands.tex`, `mathmacros.tex`,
  `notation.tex`, and `preamble.tex`.
- `rg -n` for `D'_c`, `wavefront`, `H\"ormander`, `conormal`,
  `costello-renormalization`, and `hormander-vol1`.

Post-patch checks:

- `git diff --check -- appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-121-Dc-wavefront-extension.md`
  passed.
- `grep -n '[[:blank:]]$' appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-121-Dc-wavefront-extension.md`
  returned no hits.
- Label scans found `def:app-wavefront-admissible-defect-labels` at
  `appendix-factorization-current-conventions.tex:833` and
  `prop:app-wavefront-admissible-costello-graph-kernel` at
  `appendix-factorization-current-conventions.tex:917`.
- Manuscript process-language scan over the appendix found no `Agent`,
  `swarm`, `phase`, `draft`, or `prior draft` hits.  It did find ordinary
  mathematical uses of `version`.
- Citation scans found the inserted `hormander-vol1` and
  `costello-renormalization` citations in the appendix.
- After staging exactly the two owned paths,
  `git diff --cached --check -- appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-121-Dc-wavefront-extension.md`
  passed.
- `git diff -- appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-121-Dc-wavefront-extension.md`
  returned empty after staging.
- `git diff --cached --name-only -- appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-121-Dc-wavefront-extension.md`
  listed exactly the two owned paths.

No full `make pdf` was run because the checkout has concurrent staged
manuscript edits and the build writes `out/main.pdf`, outside this
agent's writable surface.

## Residual Theorem Obligations

- No full \(\mathcal D'_c(I)\) theorem.  Coincident singular labels on a
  graph diagonal require new renormalization data.
- No all-graph summability theorem and no non-scalar QME vanishing.
- No filtered scalar projection extension beyond the already named
  habitats.
- The wavefront theorem assumes the finite-window Costello graph kernels
  have the ordinary collision-diagonal conormal singularities supplied by
  the existing Hadamard/Mittag-Leffler package.
