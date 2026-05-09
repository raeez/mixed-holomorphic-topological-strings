# Agent 253 Report: Missing Primary Source Fixture Plan

Date: 2026-04-30

Owned writable files:

- `reconstitution/missing-primary-source-fixture-plan-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-253-missing-primary-source-fixture-plan.md`

No TeX, bibliography, source fixture, script, PDF, or cross-repo file was
edited.  No browsing was used.

## Stable Core

Agent 246's source-support audit is stable.  The current manuscript has the
right source-boundary grammar: Costello, LQT, Tate bar-cobar, Hormander,
Weiss/Ran, and BMK sources may support standard external theorems or
calculus, but they do not prove the local mixed
`R^2_top x C^2_hol` Hamiltonian brane-defect theorem surfaces.

The healed deliverable is the companion plan:

```text
reconstitution/missing-primary-source-fixture-plan-2026-04-30.md
```

It names the five source fixtures to build, the likely primary references,
the theorem each source can support, and the exact boundary where the
manuscript must derive rather than cite.

## Attack-Heal Ledger

```yaml
- id: A253-01
  severity: 2
  status: healed
  lens: source fixture construction
  target: Agent 246 source-support audit
  claim: The audit can remain a source-gap list.
  broken_step: A list of gaps does not tell the next source worker which
    primary references to fetch, which theorem to anchor, or where citation
    must stop.
  evidence_type: missing_source
  evidence_ref:
    - reconstitution/primary-source-theorem-support-audit-2026-04-30.md
    - reconstitution/swarm-2026-04-30-agent-246-primary-source-theorem-support-audit.md
  minimal_heal: Write a fixture-by-fixture work order with source rows,
    theorem support, cite/derive boundary, and acceptance schema.
  residual: Exact page/theorem anchors still require the future fixture pass.

- id: A253-02
  severity: 1
  status: healed
  lens: false theorem transfer
  target: LQT/Tsygan, Tate, Hormander, Weiss/Ran, BMK lanes
  claim: Adding citations could close the local theorem surfaces.
  broken_step: The cited traditions support external templates or analytic
    criteria, not the manuscript's local Hamiltonian current graph, Tate
    envelope, BMK all-window transfer, or stratified brane QME.
  evidence_type: line_reference
  evidence_ref:
    - main.tex:1242
    - main.tex:1756
    - main.tex:5200
    - theorem-lanes.tex:3372
    - open-obligations.tex:890
  minimal_heal: Each fixture row now contains an explicit non-support boundary
    and an internal derivation obligation.
  residual: Future TeX passes must preserve this boundary when citations are
    inserted.

- id: A253-03
  severity: 2
  status: healed
  lens: bibliographic precision
  target: likely primary references
  claim: The plan can name exact theorem anchors from memory.
  broken_step: Invented theorem numbers would create a false source fixture.
  evidence_type: unsupported
  evidence_ref: ecosystem attack-heal evidence standard for research claims
  minimal_heal: The plan names exact source works and stable local
    identifiers where available, but marks page/theorem anchors as fixture
    verification tasks unless locally checked.
  residual: Future source worker must use primary/official sources only and
    record checksums and exact anchors.

- id: A253-04
  severity: 2
  status: healed
  lens: concurrent worktree discipline
  target: shared checkout
  claim: A report-only agent can safely edit adjacent source/provenance files.
  broken_step: User ownership is exactly two report files; TeX, bibliography,
    source fixture, and provenance edits are out of scope.
  evidence_type: scope
  evidence_ref: user instruction in current turn
  minimal_heal: Write only the two assigned report files and stage only those
    paths.
  residual: None for this agent.
```

## Repairs Made

- Wrote `reconstitution/missing-primary-source-fixture-plan-2026-04-30.md`.
- Wrote this agent report.
- Converted Agent 246's missing-source priorities into five fixture work
  packages:
  `LQT/Tsygan`, `Tate bar-cobar/Quillen`, `Hormander wavefront`,
  `Weiss/Ran/stratified descent`, and `BMK/Koppelman`.
- For each package, recorded likely primary references, the theorem each
  source may support, and whether the manuscript should cite or internally
  derive.

## Source Decisions

| Lane | Cite external source for | Derive internally |
|---|---|---|
| LQT/Tsygan | Stable `gl_infty(A)` CE homology and cyclic homology template. | Dirac/Koszul stable trace, one-psi primitive homology, finite-window completed LQT map. |
| Tate bar-cobar/Quillen | Standard Koszul, bar-cobar, PBW, model-category, monoidal transfer, and localization grammar. | Admissible Tate envelope, lower-central Tate-pronilpotence, exact continuous dualization, ML/Roos gates, strict endpoint obstruction. |
| Hormander | Wavefront product, pullback/restriction, pushforward criteria. | Kernel wavefronts, graph products, diagonal extensions, counterterms, arbitrary-current obstruction. |
| Weiss/Ran/stratified | Factorization/Weiss descent, Ran/chiral language where invoked, stratified factorization homology grammar. | Mixed product-disk site, stratified pair `(X,L)`, collar modules, centrality homotopies, QME curvature, trace state. |
| BMK/Koppelman | Classical BMK kernel, Koppelman `bar partial` homotopy identity, normalization after verification. | Finite-window moment projection, cutoff collar estimates, arity-two Hamiltonian/Matlis transfer, all-window obstruction vector. |

## Verification

Commands used:

```bash
sed -n '1,220p' CLAUDE.md
sed -n '1,220p' /Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md
sed -n '1,220p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-246-primary-source-theorem-support-audit.md
sed -n '1,520p' reconstitution/primary-source-theorem-support-audit-2026-04-30.md
sed -n '8848,8874p' main.tex
sed -n '9100,9270p' main.tex
nl -ba main.tex | sed -n '1240,1505p'
nl -ba main.tex | sed -n '1738,1788p'
nl -ba main.tex | sed -n '5200,5468p'
nl -ba theorem-lanes.tex | sed -n '3350,3485p'
nl -ba open-obligations.tex | sed -n '880,1025p'
rg -n "Loday|Tsygan|Quillen|Priddy|Hinich|Hovey|Lefevre|Hormander|Weiss|Ran|Ayala|Francis|Tanaka|Bochner|Martinelli|Koppelman|BMK" main.tex theorem-lanes.tex claim-strength-ledger.tex open-obligations.tex local-dictionary.tex references/source-provenance.md references/primary-sources
```

Post-write checks and staging are recorded in the final session response.

## Residual Obligations

- Future source agents must build the five actual fixtures under
  `references/primary-sources/`.
- Exact page/theorem anchors for BMK/Koppelman and Hormander Chapter 8 remain
  to be verified from primary/official sources.
- Bibliography/provenance integration is intentionally left untouched by this
  report-only agent.
