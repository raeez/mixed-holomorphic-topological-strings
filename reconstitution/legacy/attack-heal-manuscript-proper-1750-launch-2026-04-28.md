# Manuscript-Proper Attack-Heal Launch — 2026-04-28 17:50 Critique

## Control

Canonical critique source:

- `materials/processed/2026-04-28-1750-whitepaper-critical-analysis.txt`
- `materials/raw/2026-04-28-1750-whitepaper-critical-analysis.pdf`

Target artifact:

- `main.tex`
- included TeX fragments, appendices, scripts, and frontmatter where they support claims in `main.tex`

Main-thread integration owner:

- Codex main thread. Agents provide evidence, not authority.

Write policy:

- All six agents are read-only/proposal-only.
- No agent may edit, stage, commit, build, or run write-producing commands in the shared checkout.
- Healing is by exact manuscript-proper repair instructions unless the main thread later assigns isolated worktrees.

Evaluation rule:

- A manuscript claim survives only if the local text supplies definitions, hypotheses, proof/computation, or a correctly imported theorem with verified hypotheses.
- Unsupported overclaims are not healed by deletion alone; the minimal true theorem, proposition, definition, residual problem, or conditional statement must be named.

## Agent Partition

| ID | Agent | Scope | Primary Surfaces |
|---|---|---|---|
| M01 | Herschel | CE/PV/factorization | `Z^{P_0}_{fact}`, CE/PV generator map, brane-line current lift, closed observables |
| M02 | Averroes | Koszul/Matlis/Rees | Koszul duality, PBW, conilpotence, Matlis principal parts, one-psi sector |
| M03 | Wegener | Moyal/radial | Moyal coefficients, normalized commutator, finite-N/radial-parts, script counts |
| M04 | Ptolemy | Costello/QME/graphs | analytic BV package, QME obstruction, reduced Wick vs Costello theorem, anomaly exits |
| M05 | Avicenna | frontmatter/status | abstract, introduction, theorem-status surfaces, reader-visible overclaims |
| M06 | Bernoulli | appendices/scripts/cross-volume | `tate-*.tex`, radial appendix, computation scripts, figures, source firewall |

## Required Return

Each agent must return compact attack ledger entries with:

- claim attacked;
- exact failure mode or proof;
- local file anchors;
- primary-source anchors where needed;
- exact formulas/constants where the attack is computational;
- claim-status recommendation;
- files changed: always `none` in this wave;
- tests or computations run: read-only only, otherwise proposed;
- remaining open questions and deciding evidence.

## First-Pass Fatality List

The current wave is especially asked to attack whether the manuscript proper has fully absorbed these 17:50 casualties:

1. no full `Z^{P_0}_{fact}` theorem yet;
2. no full open BV algebra identification;
3. no full conilpotent Koszul-duality claim for the formal Hamiltonian algebra;
4. no `R`-submodule Matlis wording;
5. no unconditional radial-parts theorem;
6. no normalized-Moyal “no `\hbar^2` correction” claim;
7. no Costello graph theorem from reduced Wick diagrams;
8. no “exactly three” QME classification.
