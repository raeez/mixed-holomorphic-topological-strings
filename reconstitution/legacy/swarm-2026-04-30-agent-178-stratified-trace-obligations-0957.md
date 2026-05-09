# Agent 178 Stratified Trace Obligations

Worktree: `/Users/raeez/topological-strings`
Branch: `master`
Owned files: `open-obligations.tex`, this report.
Status: staged after local verification; no commit.

## Stable Core

The stable core is an obligation surface, not a theorem.  The manuscript
may now name the stronger objects needed for a stratified brane theorem
and a physical trace-state theorem:

- a stratified prefactorization functor on
  \(X=\mathbb R_t\times\mathbb R_s\times\mathbb C^2\) with lower stratum
  \(L=\mathbb R_t\times\{s=z_1=z_2=0\}\);
- a brane module/open algebra branch, either finite
  \(A^q_{N,\Omega}\) or the stable weighted principal-part current
  target;
- product and \(P_{0,\hbar}\)-centrality homotopies against unreduced
  open observables;
- a brane-defect Costello QME kernel and counterterms;
- a continuous trace/state functional, normalization convention, Ward
  identities, cumulant topology, and large-\(N\) asymptotic statement.

No external analogy proves these.  The analogy is admissible only after a
source-primary fixture verifies the source theorem, its hypotheses, and a
matched-conventions morphism to this local mixed HT pair.

## Valid Attacks

```yaml
- id: A1-178-01
  severity: 1
  status: healed
  lens: stratified factorization
  target: open-obligations.tex:514
  claim: The reduced current target already defines a stratified factorization algebra on (X,L).
  broken_step: A reduced interval current prefactorization target does not give values on bulk disks, brane disks, and collars, nor stratified Weiss descent.
  evidence_type: proof_gap
  evidence_ref: open-obligations.tex:514-634; main.tex:7422-7527; appendix-factorization-current-conventions.tex:464-536
  confidence: high
  blast_radius: any protected brane trace or closed-open stratified theorem would lack a typed source category and module values.
  minimal_heal: add the stratified functor, brane branch, collar module, structure maps, first obstruction cochains, and obstruction vector.
  residual: construct the functor and prove descent.
  deciding_evidence: a completed \(\mathcal F^{str}_{\Omega,N}\) on \(\operatorname{Disk}^{str}_{X,L}\) with descent proof.

- id: A1-178-02
  severity: 1
  status: healed
  lens: closed-open centrality
  target: open-obligations.tex:588
  claim: Reduced Moyal current brackets supply the centrality homotopies needed for the unreduced brane.
  broken_step: Strict reduced brackets do not produce product or \(P_0\)-bracket homotopies against arbitrary unreduced open BV observables.
  evidence_type: proof_gap
  evidence_ref: open-obligations.tex:588-615; reconstitution/swarm-2026-04-30-agent-093-bulk-defect-kernel.md
  confidence: high
  blast_radius: the closed-open factorization-centre morphism and stratified trace cannot be formed.
  minimal_heal: add \(H^{prod}_{x,a}\), \(H^{P_0}_{x,a}\), compatibility requirements, and QME curvature obstruction.
  residual: construct the homotopies in the chosen brane-defect local-functional complex.
  deciding_evidence: chain homotopies satisfying the displayed equations and finite-window/weight compatibility.

- id: A1-178-03
  severity: 1
  status: healed
  lens: trace-state and large N
  target: open-obligations.tex:636
  claim: Algebraic stable trace invariants imply the physical large-\(N\) protected trace.
  broken_step: Degreewise stable invariant theory does not choose a state, normalization, topology, cumulant extraction, or Ward identities.
  evidence_type: proof_gap
  evidence_ref: open-obligations.tex:636-733; local-dictionary.tex:831-849; materials/processed/2026-04-30-mixed-holomorphic-topological-strings-critique.txt:100270-100520
  confidence: high
  blast_radius: physical trace asymptotics and protected trace language would overstate the proved algebraic sector.
  minimal_heal: add \(\omega_{N,\Omega}\), \(\nu_{\Omega,N}\), \(\mathcal T_\Omega\), Ward identities, cumulants, and \(\operatorname{Ob}_{tr,\Omega}\).
  residual: construct the state and prove the asymptotic expansion.
  deciding_evidence: a state on the stratified factorization homology with \(d_{QME}\), \(Q_\Omega\), and moment-map Ward identities, plus an expansion in the named topology.

- id: A1-178-04
  severity: 2
  status: healed
  lens: source-primary audit
  target: external CFG/Costello analogy
  claim: CFG or Costello Omega-background results can be cited as proof of the local brane trace theorem.
  broken_step: The primary sources have different hypotheses and targets; none constructs the mixed HT \(R^2\times C^2\) brane module, current target, state, or QME kernel.
  evidence_type: source_conflict
  evidence_ref: arXiv:2602.12412; arXiv:1610.04144; arXiv:1705.02500; arXiv:1409.0848; references/primary-sources/local-costello-bv-kernel-source-anchors-2026-04-30.md
  confidence: high
  blast_radius: imported theorem support would contaminate the local theorem surface.
  minimal_heal: encode \(\operatorname{ob}^{src}_{CFG}\) and \(\operatorname{ob}_{src}\) as source-audit obstructions.
  residual: build a local source fixture if the analogy is to enter the theorem surface.
  deciding_evidence: a primary-source ledger with source theorem, hypotheses, and matched-conventions morphism to \((X,L)\).
```

## Repairs Made

`open-obligations.tex` now contains two new obligation entries.

- `Stratified brane prefactorization and module datum` names
  \(\mathcal F^{str}_{\Omega,N}\), \(\operatorname{Disk}^{str}_{X,L}\),
  the finite and stable brane branches, the collar module, descent
  defects, centrality homotopies, QME curvature, and
  \(\operatorname{Ob}_{str,\Omega,N}\).
- `Trace-state functional and physical large-\(N\) surface` names
  \(\omega_{N,\Omega}\), \(\mathfrak T_{\Omega,N}\),
  residue/Euler normalization, Ward identities, connected cumulants,
  the large-\(N\) asymptotic topology, and
  \(\operatorname{Ob}_{tr,\Omega}\).

## Source-Primary Audit

- Ayala--Francis--Tanaka, `arXiv:1409.0848`, supports the framework of
  factorization homology for stratified spaces.  It does not construct
  this mixed HT brane module or its trace.
- Costello, `arXiv:1610.04144`, supports the methodology that an
  Omega-background can identify a protected sector and lower-dimensional
  gauge theory with branes tracked as defects.  It does not prove the
  local \(R^2\times C^2\) Hamiltonian brane theorem.
- Costello, `arXiv:1705.02500`, supports a separate large-\(K\)
  Koszul-duality result for M2 branes in an Omega-background.  It does
  not choose the state or cumulant topology for this brane trace.
- Costello--Francis--Gwilliam, `arXiv:2602.12412`, supports the pattern
  of a BV-quantized Chern-Simons \(E_3\)-algebra, perfect modules, and a
  factorization-homology trace computing link invariants.  It is a
  Chern-Simons/link theorem, not a theorem for the present mixed HT
  model.
- The local Costello source fixtures support finite-scale BV/RG/QME
  vocabulary and obstruction-complex grammar.  They explicitly do not
  supply an automatic \(\mathcal D'_c\)-valued current target,
  bulk-to-defect kernel, or brane-defect graph theorem.

## Verification

Commands run:

```bash
sed -n '1,220p' CLAUDE.md
sed -n '1,220p' AGENTS.md
sed -n '1,260p' reconstitution/critique-refresh-2026-04-30-0957-ingestion-and-swarm-plan.md
sed -n '1,980p' open-obligations.tex
sed -n '1,260p' /Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/references/protocol.md
sed -n '1,220p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
rg -n -F -e "stratified" -e "trace" -e "Costello" -e "QME" main.tex open-obligations.tex theorem-lanes.tex local-dictionary.tex appendix-factorization-current-conventions.tex
git diff --check -- open-obligations.tex
```

Result: `git diff --check -- open-obligations.tex` returned cleanly.
No full `make pdf` was run because it writes build artifacts outside the
owned path while concurrent agents are editing.

## Remaining Obligations

The next agent or integration owner must decide the theorem surface by
constructing:

- the stratified disk category and \(\mathcal F^{str}_{\Omega,N}\);
- the collar module \(\mathcal M_{\Omega,N}\);
- unreduced centrality homotopies in the brane-defect QME complex;
- the Costello brane-defect kernel and counterterms;
- a state \(\omega_{N,\Omega}\), normalization \(\nu_{\Omega,N}\), and
  topology \(\mathcal T_\Omega\);
- Ward identities and large-\(N\) cumulant asymptotics;
- a primary-source fixture before CFG/Costello analogies are used as
  theorem support.
