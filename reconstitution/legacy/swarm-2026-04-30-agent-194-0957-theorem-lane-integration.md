# Agent 194 report: 09:57 theorem-lane integration

Date: 2026-04-30  
Owned paths: `theorem-lanes.tex`, `reconstitution/swarm-2026-04-30-agent-194-0957-theorem-lane-integration.md`

## Context read

- `CLAUDE.md` and `AGENTS.md`.
- Attack-heal protocol at `/Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md`.
- Manuscript-proper rectification protocol at `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- 09:57 critique-refresh plan, Agent 190 integration map, and reports/threads 174--189 when present.
- Existing staged `theorem-lanes.tex` edits from Agent 176; these were preserved and extended rather than reverted.

## Stable core

The 09:57 report threads have been routed into `theorem-lanes.tex` as theorem surfaces and exact obligations, not as completed theorems where the analytic or QME data are still open.

Inserted or upgraded lanes:

- `thm:lane-controlled-cxr-reduction` at `theorem-lanes.tex:676`.
- `thm:lane-reduced-dirac-brst-zhu` at `theorem-lanes.tex:864`.
- `thm:lane-equivariant-ce-pv-refined-bracket` at `theorem-lanes.tex:1466`.
- Matlis upgrade references at `theorem-lanes.tex:2145`.
- `thm:lane-omega-weighted-kernel-qme-surface` at `theorem-lanes.tex:2585`.
- `thm:lane-stratified-trace-physical-large-n` at `theorem-lanes.tex:2784`.

## Attack-heal ledger

### A194-01: Curve reduction was too easy to misread as native

Failure mode: a direct replacement of the native \(\mathbb C^2\) holomorphic factorization algebra by a \(\mathbb C\times\mathbb R\) curve vertex algebra would erase the second holomorphic normal direction.

Heal: inserted `thm:lane-controlled-cxr-reduction`, with explicit \(s\)-compact-support contraction, retained \(z_2\)-coefficients/principal parts, two-variable Hamiltonian bracket, matrix pair \(X,Y\), scalar anomaly, Moyal product, and obstruction vector \(\operatorname{Ob}_{\mathbb C\times\mathbb R}\).

Status: theorem surface with analytic pushforward obligations.

### A194-02: Reduced Dirac BRST/Zhu package was not native

Failure mode: using the Dirac BRST/Zhu algebra before controlled reduction falsely transfers a curve construction to the four-dimensional mixed HT theory.

Heal: inserted `thm:lane-reduced-dirac-brst-zhu`, explicitly conditional on `thm:lane-controlled-cxr-reduction`, a retained \(z_2\)-coefficient system, anomaly convention, and a factorization-to-vertex theorem.

Status: conditional theorem surface after reduction only.

### A194-03: Equivariant CE/PV bracket needed the refined weight parameter

Failure mode: the unweighted scalar bracket misses the non-self-dual equivariant bookkeeping and invites an invalid specialization at \(\epsilon_1+\epsilon_2=0\).

Heal: inserted `thm:lane-equivariant-ce-pv-refined-bracket`, with weights on \(c^{a,b}\), \(\theta^{a,b}\), \(u_{a,b}\), \(\mathcal O_{a,b}\), the parameter \(\hbar_\omega\), CE differential formulas, PV bivector, generator map, and self-dual warning.

Status: coordinate dg formula after adjoining \(\hbar_\omega\); kernel/QME/trace upgrades remain obstruction data.

### A194-04: Weighted kernels did not yet prove QME

Failure mode: admissible weighted kernels can be mistaken for a completed equivariant QME theorem.

Heal: inserted `thm:lane-omega-weighted-kernel-qme-surface`, separating finite-window weighted kernel admissibility from the scalar projection defect, non-scalar residual gate, \(H^1\) class, \(\lim^1\) completion issue, and finite-row primitive interface.

Status: finite-window kernel theorem surface plus QME boundary criterion.

### A194-05: Physical large-\(N\) trace was not a mathematical theorem

Failure mode: stable algebraic trace data and physical \(\Omega\)-large-\(N\) expectations can be conflated.

Heal: inserted `thm:lane-stratified-trace-physical-large-n`, with a stratified prefactorization functor surface, finite and stable branches, collar/descent obligations, and a separate physical state criterion with normalization, Ward identities, cumulants, asymptotics, and scalar QME normalization.

Status: theorem surface for exact stratified trace data; physical large-\(N\) remains a criterion/obligation.

### A194-06: Matlis lane needed appendix upgrade anchors

Failure mode: the principal-parts lane lacked the new appendix labels needed for coadjoint action, continuity, residue rigidity, and polynomial-descendant obstruction.

Heal: upgraded the proof-input paragraph of `thm:lane-principal-parts` to cite:

- `prop:app-matlis-coadjoint-action`
- `lem:app-matlis-coadjoint-continuity`
- `thm:app-matlis-residue-rigidity`
- `thm:app-matlis-polynomial-descendant-obstruction`

Status: reference wiring only; no theorem strength increased.

## Remaining obligations

- Construct the analytic \(\pi_!\) theorem for the controlled \(\mathbb C\times\mathbb R\) reduction: \(s\)-orientation sign, \(z_2\)-Dolbeault or residue pushforward, reduced BV pairing degrees, factorization compatibility, and anomaly homotopy.
- Prove the factorization-to-vertex reduction and anomaly convention required by the reduced Dirac BRST/Zhu surface.
- Complete equivariant CE/PV topologies and the corresponding kernel/QME upgrades beyond the coordinate dg formulas.
- Decide the QME obstruction classes: scalar projection, non-scalar residual, \(H^1\), completion \(\lim^1\), and finite-window row limits.
- Supply the physical state, Ward identities, cumulant bounds, and asymptotic expansion required for the physical \(\Omega\)-large-\(N\) criterion.
- Keep external source analogies as vocabulary or hypotheses until a matched-conventions morphism is constructed.

## Verification

- `git diff --check -- theorem-lanes.tex`: clean.
- Duplicate label scan in `theorem-lanes.tex`: no duplicate labels reported.
- Targeted `rg` confirmed all new labels and Matlis anchors.
- Temporary two-pass compile outside the repo:
  `pdflatex -halt-on-error -interaction=nonstopmode -draftmode -output-directory=/tmp/topological-strings-agent194-build main.tex`.
  Both passes exited 0. No undefined-reference warning was reported on the second pass. Remaining warnings are pre-existing overfull/underfull/font warnings, not fatal errors.
