# Agent 262 Weiss/Ran Stratified Descent Source Fixture

Worktree: `/Users/raeez/topological-strings`.

Owned files:

- `references/primary-sources/weiss-ran-stratified-descent-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-262-weiss-ran-stratified-descent-source-fixture.md`

No manuscript TeX or bibliography files were edited.  No PDF build was
run.

## Verdict

The source fixture is built.  The verified external sources support only
the descent and factorization grammar needed to state the manuscript's
obligations:

- Costello--Gwilliam Vol. I: Weiss covers, factorization algebras as
  Weiss homotopy cosheaves, local dg Lie algebra examples, and extension
  from factorizing bases under hypotheses.
- Boavida de Brito--Weiss: \(J_k\) finite-point covers, homotopy
  sheafification in manifold calculus, and configuration-category
  descent/product analogues.
- Ayala--Francis--Tanaka: stratified factorization homology,
  `Disk`-algebra coefficient grammar, bounded Ran topology, excision,
  and continuity.
- Existing Omega/stratified source ledger: related-model boundaries for
  AFT, Costello Omega, Costello M2/Koszul, and CFG Chern--Simons trace.

None of these sources proves the local mixed HT stratified brane
construction, brane-defect QME, unreduced centrality homotopies,
\(\Omega\)-basic normal contraction, trace-state functional, or
large-\(N\) cumulant theorem.

## Attack-Heal Results

`A262-01` -- Weiss descent import.

- Claim attacked: Costello--Gwilliam's Weiss cosheaf theorem can be
  cited as the manuscript's stratified Weiss descent proof.
- Failure: the source theorems require a factorization algebra or local
  dg Lie algebra satisfying their hypotheses; the manuscript still has
  to construct \(\mathcal F^{str}_{\Omega,N}\) on bulk disks, brane
  intervals, and collars.
- Heal: fixture records CG Vol. I anchors for Weiss cover/descent and
  marks the local descent defect as an internal obstruction.

`A262-02` -- Ran/configuration transfer.

- Claim attacked: Boavida--Weiss configuration-category descent/product
  results prove the product or Ran descent needed for the observable
  cosheaf.
- Failure: those sources concern manifold-calculus functors and
  configuration categories, not mixed HT factorization algebras of
  observables.
- Heal: fixture restricts them to finite-point \(J_k\), homotopy
  sheafification, and configuration product grammar.

`A262-03` -- Stratified factorization homology import.

- Claim attacked: AFT stratified factorization homology proves the
  brane trace theorem.
- Failure: AFT requires a `Disk`-algebra coefficient datum; it does not
  construct the present brane algebra, central-action map, QME package,
  or trace state.
- Heal: fixture maps AFT to the exact coefficient/excision obligations
  and records non-support for the Omega trace-state surface.

`A262-04` -- Existing Omega/CFG analogy.

- Claim attacked: Costello Omega, Costello M2/Koszul, or CFG
  Chern--Simons trace sources can be imported as theorem support.
- Failure: all are different models or trace mechanisms with different
  hypotheses.
- Heal: fixture cites the existing internal ledger and preserves its
  boundary: analogy/template only until matched-conventions data are
  constructed.

## Fixture Output

Primary source ledger written:

- `references/primary-sources/weiss-ran-stratified-descent-source-anchors-2026-04-30.md`

It contains:

- local manuscript obligation anchors;
- metadata and verified anchors for Costello--Gwilliam Vol. I/II,
  Boavida de Brito--Weiss homotopy sheaves, Boavida--Weiss
  configuration categories, Boavida--Weiss configuration product, AFT
  stratified factorization homology, and the existing Omega/stratified
  source fixture;
- a support matrix from each source theorem to the manuscript's Weiss
  descent, factorization algebra, stratified brane, and Omega
  trace-state obligations;
- explicit non-support firewall entries;
- verification commands, files read, and remaining gaps.

## Verification Commands

Representative local commands:

```bash
sed -n '1,220p' AGENTS.md
sed -n '1,220p' CLAUDE.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,220p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '4118,4265p' main.tex
sed -n '890,1080p' open-obligations.tex
sed -n '630,718p' local-dictionary.tex
sed -n '1,260p' references/primary-sources/omega-stratified-source-anchors-2026-04-30.md
rg -n -F -e "Weiss" -e "Ran" -e "stratified" -e "factorization" main.tex open-obligations.tex local-dictionary.tex references reconstitution
```

Representative source extraction commands:

```bash
mkdir -p /tmp/agent262-sources
curl -L -o /tmp/agent262-sources/cg-nlab.pdf https://ncatlab.org/nlab/files/CostelloGwilliam-FactorizationAlgebras.pdf
pdftotext /tmp/agent262-sources/cg-nlab.pdf /tmp/agent262-sources/cg-nlab.txt
curl -L -o /tmp/agent262-sources/bdw-hha.pdf https://www.intlpress.com/site/pub/files/_fulltext/journals/hha/2013/0015/0002/HHA-2013-0015-0002-a020.pdf
pdftotext /tmp/agent262-sources/bdw-hha.pdf /tmp/agent262-sources/bdw-hha.txt
curl -L -o /tmp/agent262-sources/bdw-config-embeddings.pdf https://arxiv.org/pdf/1502.01640
pdftotext /tmp/agent262-sources/bdw-config-embeddings.pdf /tmp/agent262-sources/bdw-config-embeddings.txt
curl -L -o /tmp/agent262-sources/bdw-config-product.pdf https://arxiv.org/pdf/1701.06987
pdftotext /tmp/agent262-sources/bdw-config-product.pdf /tmp/agent262-sources/bdw-config-product.txt
curl -L -o /tmp/agent262-sources/aft-arxiv.pdf https://arxiv.org/pdf/1409.0848
pdftotext /tmp/agent262-sources/aft-arxiv.pdf /tmp/agent262-sources/aft-arxiv.txt
```

Metadata checks used Cambridge Core, arXiv, Springer, International
Press/HHA, and the University of Lisbon research portal.

## Files Read

- `AGENTS.md`
- `CLAUDE.md`
- `/Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md`
- `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `main.tex`
- `open-obligations.tex`
- `local-dictionary.tex`
- `reconstitution/missing-primary-source-fixture-plan-2026-04-30.md`
- `reconstitution/global-weiss-ran-descent-firewall-construction-target-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-238-global-weiss-ran-descent-firewall-construction-target.md`
- `reconstitution/swarm-2026-04-30-agent-178-stratified-trace-obligations-0957.md`
- `reconstitution/swarm-2026-04-30-agent-186-omega-stratified-source-audit-0957.md`
- `reconstitution/physical-omega-largeN-trace-state-thread-2026-04-30.md`
- `reconstitution/omega-physical-largeN-state-construction-target-2026-04-30.md`
- `references/primary-sources/omega-stratified-source-anchors-2026-04-30.md`
- `references/primary-sources/costello-gwilliam-vol1-cambridge.html`
- `references/primary-sources/costello-gwilliam-vol2-cambridge.html`
- `references/primary-sources/costello-cg-source-anchors-2026-04-28.md`
- `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md`
- source text extracts under `/tmp/agent262-sources`

## Remaining Gaps

- Exact CUP published-book theorem/page anchors for
  Costello--Gwilliam Vol. I and Vol. II remain unverified.  The detailed
  anchors in the fixture are to the author/preprint PDF and existing
  local section fixtures.
- A matched-conventions comparison from the manuscript's stratified
  mixed HT pair \((X,L)\) to AFT's conically smooth `Disk` framework is
  still absent.
- The product-disk-to-arbitrary-stratified-Weiss cofinality theorem for
  the manuscript's observables remains to be proved.
- The brane-defect QME kernel, centrality homotopies,
  \(Q_\Omega\)-basic contraction, residue/Euler normalization, and
  trace state remain construction targets.
