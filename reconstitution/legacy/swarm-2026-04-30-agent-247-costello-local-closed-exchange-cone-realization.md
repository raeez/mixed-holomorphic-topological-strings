# Agent 247 - Costello-Local Closed-Exchange Cone Realization

Status: report-only.  Owned files:

- `reconstitution/costello-local-closed-exchange-cone-realization-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-247-costello-local-closed-exchange-cone-realization.md`

No TeX, script, bibliography, figure, or source-anchor file was edited.

## Stable Core

Agent 241's cone is a valid algebraic source extension:
\[
  \mathcal X^{1,\mathrm{alg}}_{\mathrm{sc},w,M}(I)=\mathbb C[[\hbar]]e_M,
  \qquad d^X_Me_M=0,
\]
\[
  \Xi^{\mathrm{alg},\mathrm{sc}}_M(e_M)
  =
  -\hbar N\bar c_M(f,g)
  \int_Ia(t)b(t)\gamma_{\mathbf 1}(t)\,dt.
\]
With \(W_M=e_M\), \(C_M=0\), and \(\rho^X_{M,N}e_M=e_N\), the algebraic
finite-window and Roos classes vanish in the enlarged central-contact branch.

The same cone is not a Costello-local closed exchange.  A Costello-local
realization must construct a closed source complex, finite-scale graph
propagator, bulk-to-defect restriction, source-face Hom differential,
locality/support and counterterm rules, scalar-contact chain projection, and
compatible finite-window representatives.  The current ordinary branch fails
before secondary Roos classes:
\[
  o_{\sigma,M}^{(1),\mathrm{sc}}=\hbar N[\bar c_M]\neq0,
\]
and, after any externally supplied scalar gate,
\[
  \beta_{M}^{\mathrm{Cost},\mathrm{sc}}
  =
  [\hbar N[\bar c_M]]
  \in
  \operatorname{coker}
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{Cost},\mathrm{sc}}_M).
\]
For the presently constructed genuine Costello-local towers, the scalar image
needed to hit \(-\hbar N[\bar c_M]\) is absent.

## Attack Ledger

```yaml
- id: A1-247-01
  severity: 1
  status: valid
  lens: Costello locality
  target: Agent 241 algebraic cone
  claim: The generator e_M is a genuine closed bulk exchange.
  broken_step: e_M is a defect-supported central contact generator with declared image; it is not produced by a closed field, finite-scale propagator, bulk-to-defect graph, or local counterterm calculus.
  evidence_type: proof_gap
  evidence_ref: reconstitution/swarm-2026-04-30-agent-241-finite-window-closed-exchange-realization-construction-push.md:27-69; appendix-unreduced-bv-qme.tex:2142-2232; references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:40-130
  files_read:
    - reconstitution/swarm-2026-04-30-agent-241-finite-window-closed-exchange-realization-construction-push.md
    - appendix-unreduced-bv-qme.tex
    - references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md
  confidence: high
  blast_radius: false closure of the ordinary scalar QME branch
  minimal_heal: classify the cone as a changed algebraic central-contact source branch
  residual: construct a Costello-local closed source whose scalar image is -hbar N[bar c_M]
  deciding_evidence: finite-scale graph kernel with d_K Xi=0 and scalar image -hbar N[bar c_M]

- id: A1-247-02
  severity: 1
  status: valid
  lens: scalar-contact chain projection
  target: original ordinary scalar-reduced complex
  claim: The scalar symbol extractor can be used after adding the cone without proving a chain projection.
  broken_step: The original ordinary branch has first chain-lift obstruction hbar N[bar c_M], nonzero on z_1,z_2.
  evidence_type: line_reference
  evidence_ref: appendix-unreduced-bv-qme.tex:236-305; local-dictionary.tex:840-874; main.tex:8022-8070
  files_read:
    - appendix-unreduced-bv-qme.tex
    - local-dictionary.tex
    - main.tex
  confidence: high
  blast_radius: forms ker widehat sigma_sc before the gate exists
  minimal_heal: put o_sigma first in the obstruction sequence
  residual: kill o_sigma by a true source/model replacement or by a Costello-local opposite scalar class
  deciding_evidence: continuous filtered chain map widehat sigma_sc,M commuting with d_M

- id: A1-247-03
  severity: 1
  status: valid
  lens: source-face Bianchi identity
  target: candidate Xi_M^Cost
  claim: A scalar contact cocycle is enough to define a closed-exchange cochain map.
  broken_step: A Costello Hom kernel must satisfy d_K Xi=d_M Xi-Xi d_X=0, including CE source faces, BV-edge faces, collision faces, and counterterm faces.
  evidence_type: line_reference
  evidence_ref: appendix-unreduced-bv-qme.tex:2174-2197; open-obligations.tex:397-438; reconstitution/swarm-2026-04-30-agent-198-nonscalar-costello-qme-realization.md:41-63
  files_read:
    - appendix-unreduced-bv-qme.tex
    - open-obligations.tex
    - reconstitution/swarm-2026-04-30-agent-198-nonscalar-costello-qme-realization.md
  confidence: high
  blast_radius: treats a prescribed contact as a graph-theoretic closed source
  minimal_heal: demand the Hom-valued source-face equation and curvature equation
  residual: construct the finite graph table producing the central source line
  deciding_evidence: closed marked row table with source-face signs and d_K Xi=0

- id: A1-247-04
  severity: 1
  status: valid
  lens: finite-window image criterion
  target: beta_M^Cost,sc
  claim: Vanishing in the algebraic cone proves vanishing for Costello-local towers.
  broken_step: The algebraic cone enlarges the source so H^1(sigma Xi) contains -hbar N[bar c_M]; the current genuine towers have scalar-zero image.
  evidence_type: line_reference
  evidence_ref: reconstitution/swarm-2026-04-30-agent-118-construct-X-Xi-closed-exchange.md:5-53; reconstitution/scalar-qme-closed-exchange-construction-target-2026-04-30.md:156-200; tate-T1-weighted-completion.tex:1526-1587
  files_read:
    - reconstitution/swarm-2026-04-30-agent-118-construct-X-Xi-closed-exchange.md
    - reconstitution/scalar-qme-closed-exchange-construction-target-2026-04-30.md
    - tate-T1-weighted-completion.tex
  confidence: high
  blast_radius: imports an enlarged-source result into the original branch
  minimal_heal: define beta_M^Cost,sc as the coker of H^1(widehat sigma Xi^Cost)
  residual: compute or construct an admissible Costello-local scalar-image class
  deciding_evidence: W_M in X^Cost with H^1(widehat sigma Xi^Cost)[W_M] = -hbar N[bar c_M]

- id: A1-247-05
  severity: 1
  status: valid
  lens: support and wavefront
  target: defect current / bulk-to-defect support
  claim: Costello source anchors already supply the current-valued defect target and bulk-to-defect kernel.
  broken_step: Local mirrors support general finite-scale BV/RG locality but contain no current-valued, D'_c, or bulk-to-defect theorem for this Hamiltonian defect target.
  evidence_type: missing_source
  evidence_ref: references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:156-232; references/primary-sources/local-costello-bv-kernel-source-anchors-2026-04-30.md:242-260
  files_read:
    - references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md
    - references/primary-sources/local-costello-bv-kernel-source-anchors-2026-04-30.md
  confidence: high
  blast_radius: cites universal BV formalism as a specific Hamiltonian kernel
  minimal_heal: require a current-compatible kernel theorem or restrict to regular densities
  residual: prove wavefront transversality, small-diagonal extension, counterterm support, RG, and finite-window compatibility
  deciding_evidence: a Costello-local D'_c or regular-density theorem producing the displayed scalar contact

- id: A1-247-06
  severity: 2
  status: non_core
  lens: Roos compatibility
  target: mu_cl^sc and lambda_C^sc
  claim: The algebraic zero Roos classes decide the Costello-local branch.
  broken_step: They decide only the one-dimensional source line with rho e=e and C=0; Costello-local representatives carry independent H^0 tower compatibility classes.
  evidence_type: line_reference
  evidence_ref: tate-T1-weighted-completion.tex:1576-1740; reconstitution/swarm-2026-04-30-agent-111-closed-exchange-ml-tower.md:46-79
  files_read:
    - tate-T1-weighted-completion.tex
    - reconstitution/swarm-2026-04-30-agent-111-closed-exchange-ml-tower.md
  confidence: high
  blast_radius: would falsely promote windowwise data to inverse-limit data
  minimal_heal: record mu and lambda_C after beta vanishes
  residual: not reached for the current Costello-local branch because beta_M^Cost,sc is nonzero
  deciding_evidence: compatible W_M and C_M, or ML H^0 towers, for the actual Costello-local X and Q
```

## Healed Obstruction Package

The algebraic source map is
\[
  \Xi^{\mathrm{alg},\mathrm{sc}}_M(e_M)
    =
  -\hbar N\,\bar c_M(f,g)
  \int_Ia(t)b(t)\gamma_{\mathbf 1}(t)\,dt .
\]

The Costello-local source map, if it exists, must be a graph sum
\[
  \Xi^{\mathrm{Cost},\mathrm{sc}}_M(x)
  =
  \sum_{\Gamma\in\mathcal G^{\mathrm{cl}\to\mathrm{bd}}_M}
  {1\over|\operatorname{Aut}\Gamma|}
  W^{R,M}_{\Gamma,L,w}(x;-)
\]
inside the completed scalar-contact QME complex, with
\[
  d_{\mathbf K,M}\Xi_M=0,\qquad
  \pi_{M,N}\Xi_M=\Xi_N\rho^X_{M,N}.
\]

The exact obstruction sequence is:
\[
  o_{\sigma,M}^{(1),\mathrm{sc}},
  \quad
  \beta_{M}^{\mathrm{Cost},\mathrm{sc}},
  \quad
  \beta_{\mathrm{cl}}^{\mathrm{Cost},\mathrm{sc}},
  \quad
  \mu_{\mathrm{cl}}^{\mathrm{Cost},\mathrm{sc}},
  \quad
  \lambda_C^{\mathrm{Cost},\mathrm{sc}}.
\]
The current branch stops at the first two terms.  The algebraic cone makes all
terms zero only by changing the source to include \(e_M\).

## Proposed Insertion

Add to the scalar QME obligation lane:

```tex
The minimal central-contact cone proves only the enlarged algebraic branch.
A Costello-local closed exchange must replace the formal generator \(e_M\)
by a closed source complex, finite-scale propagator, bulk-to-defect graph
kernel, source-face Bianchi identity, local counterterm support, filtered
scalar chain projection, and compatible finite-window representatives.  The
first Costello-local scalar image obstruction is
\[
  \beta_{M}^{\mathrm{Cost},\mathrm{sc}}
  =
  [\hbar N[\bar c_M]]
  \in
  \operatorname{coker}
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{Cost},\mathrm{sc}}_M).
\]
For the current genuine Costello-local towers this image is scalar-zero, so
the ordinary scalar-reduced branch remains blocked unless a new local source
class with image \(-\hbar N[\bar c_M]\) is constructed; if it is supplied, the
remaining obstructions are the inverse-limit \(\beta\) and the Roos classes
\(\mu,\lambda_C\).
```

## Verification

Read:

- `CLAUDE.md`
- `AGENTS.md`
- `~/ecosystem/INVARIANTS.md`
- `~/ecosystem/AGENTS-HARNESS.md`
- `~/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md`
- `~/ecosystem/skills/shared/attack-heal-swarm/protocol.md`
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `main.tex`
- `appendix-unreduced-bv-qme.tex`
- `open-obligations.tex`
- `claim-strength-ledger.tex`
- `local-dictionary.tex`
- `tate-T1-weighted-completion.tex`
- `reconstitution/scalar-qme-closed-exchange-construction-target-2026-04-30.md`
- `reconstitution/finite-window-closed-exchange-realization-construction-push-2026-04-30.md`
- Agent reports 111, 118, 147, 198, 220, 232, and 241
- Costello source fixtures under `references/primary-sources/`

Commands run included targeted `rg`, `nl -ba`, and `sed` reads over the files
above; negative source searches for `bulk-to-defect`, `current-valued`, and
`D'_c`; and the finite scalar CE check:

```text
CE cocycle failures through bidegree<6: 0
omega(z1,z2)= 1
reduced exactness test: d eta(z1,z2) = -eta({z1,z2} mod C) = 0, so omega is not exact on A/C
```

No build was run.  This lane is report-only, and the shared checkout already
contains concurrent manuscript and PDF changes outside this agent's ownership.
