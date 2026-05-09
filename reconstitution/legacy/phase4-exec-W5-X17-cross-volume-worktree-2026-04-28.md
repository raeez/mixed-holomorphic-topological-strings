# Phase-4 EXEC W5-X17 Cross-Volume Worktree Integration Probe (RELAUNCH)

**Author.** Raeez Lorgat. Mode: read-only on all worktrees, no commits, no
modifications. Date: 2026-04-28.

**Lens.** X17 = Cross-Volume Worktree Integration. Wave-5 follow-on to
W5-X1 (which audited declarative firewall consistency by interpretation
`CLAUDE.md` and `main.tex` of each sister volume). X17 probes the
*worktree state* (uncommitted work, branches, active worktrees) to
detect cross-volume merge debt that X1's source-of-truth lens cannot
see. This is the **RELAUNCH** after a usage cap interrupted the prior
X17 invocation; the original X17 report has been preserved as the
source of the §1 dossiers and the relaunch confirms / sharpens them.

**Scope.** Four sister volumes:

1. `~/calabi-yau-quantum-groups` (Vol III, CY-to-chiral functor),
2. `~/igusa-cusp-form` ($\Delta_5$ Borcherds determinant),
3. `~/chiral-bar-cobar` (Vol I, ordered bar / five-theorem core),
4. `~/chiral-bar-cobar-vol2` (Vol II, $A_\infty$ chiral / 3D HT QFT).

**Result. CERTIFY MERGE-CLEAN with one structural caveat.** No sister
volume has wave-4/wave-5 *content* destined for topological-strings.
None of the uncommitted work or branches asserts a chain-level claim
about $\R^2 \times \widehat{\C^2}_0$ Hamiltonian BF, brane-defect BV,
or doubled-brane $q(N)$. The firewall typology (FW.BCOV, FW.Sergeev-A5,
FW.Igusa, FW.Unreduced-Bosonic, FW.Costello-Li-d-even) is preserved.
The structural caveat is large in-flight per-volume work that will
publish independently. The relaunch sharpens the count audit and
exposes the in-place-rewrite vs new-file split inside Vol III's
14-agent swarm, plus the staged-vs-untracked split inside Igusa.

---

## §1. Per-volume worktree status

### §1.1 `calabi-yau-quantum-groups` (Vol III)

**HEAD.** `main` at `7634eef` "14-agent swarm against perturbative
$E_3$ hCS gaps on $K3\times E$".

**Uncommitted (`git status --short`).** 30 entries. 21 tracked
modifications:
- 4 manuscript chapters: `chapters/examples/k3e_cy3_programme.tex`,
  `chapters/theory/{cy3_chain_level_bridge, hochschild_calculus,
  quantum_groups_foundations}.tex`.
- 14 swarm-blocker6 v2 working notes
  `notes/swarm_blocker6_v2_agent01..14_*.tex`.
- 1 register `working_notes.tex`.
- 7 PDF / index re-renders in `out/` and at top level.
- 1 untracked `main.idx`.

**`git diff --stat HEAD` magnitude.** 2988 insertions, 3073 deletions
across 29 tracked files; net **-85 lines** with $\sim$6000-line
in-place rewrite churn (e.g. agent09 BCOV one-loop note: 232-line
diff / 117-line net delta; agent10 BCOV higher-genus note:
414-line diff / 50-line net delta).

**Origin commit `7634eef`.** Introduced 8207 insertions across the
14 swarm-blocker6 notes in one shot. The current uncommitted state
is in-place healing of those 14 notes (agent01: 1015 lines / agent02:
884 / agent03: 471 / agent04: 248 / agent05: 493 / agent06: 739 /
agent07: 495 / agent08: 562 / agent09: 592 / agent10: 538 /
agent11: 373 / agent12: 714 / agent13: 341 / agent14: 742) plus a
+275-line `def:framed-hcs-hochschild-target` definition and Hochschild
target machinery added to `chapters/theory/cy3_chain_level_bridge.tex`.
Vol III is consolidating the swarm output, not adding new files.

**Recent commits (last 10).** All wave-4 content stays in Vol III
($K3\times E$ inscription, 6D hCS Costello-Li construction, Weiss
descent, Gritsenko-Clery, Vol III determinant artifact, K3 Hall-
Drinfeld stratification). HEAD is `7634eef` (14-agent swarm head).

**Branches.** `main` (current) and `w2-k3xk3xe-bialgebra-associator-chl`
(legacy wave-2 inscription branch) plus seven worktree-agent branches
`worktree-agent-{a05f7797, a3aa38ba, aaf9dd75, ac0fc1ac, ae1c7771,
aee16e88, afa53e22}`. The 14-agent swarm head `7634eef` lives on `main`
only (`git branch --contains 7634eef` returns `* main`).

**Active worktrees.** 7 entries in `.git/worktrees/agent-*`, each
pinned to its own `worktree-agent-*` branch and resolving to
`.claude/worktrees/agent-*`. All mtimes 2026-04-25 15:08 (parked
since wave-4 swarm landing).

**Cross-volume reference test.**
- Working-tree grep on the 20 uncommitted-or-recent notes for
  `BCOV|Hamiltonian.BF|brane.defect.BV|q\(N\)` returns 20 hits, all
  in Vol III internal convention-checking surface
  (`physics_topological_strings.tex`, `physics_bv_brst_cy.tex`,
  `physics_celestial_cy.tex`, etc., plus the BCOV-tagged
  swarm-blocker6 agents 09 and 10 — Hodge-cohomology level only).
- Specific topological-strings lexicon scan
  (`topological string|Kodaira-Spencer`):
  agent09 BCOV one-loop: **0 hits**;
  agent10 BCOV higher-genus: **3 hits** (mention of "BCOV moduli",
  "BCOV holomorphic anomaly equation", "complete variation of BCOV"
  as **citations** / heuristic comparisons, not load-bearing
  cross-volume claims).
- Commit-log scan since 2026-04-25 with regex
  `BCOV|Hamiltonian BF|brane-defect|q(N)|topological-string|Kodaira-Spencer`
  returns 0 commits.
- Agent09 BCOV one-loop note diff confirms FW.BCOV-preserving
  retraction language: title healed from "Explicit one-loop BCOV
  partition function" to "One-loop BCOV torsion witness", abstract
  restated as "scalar one-loop BCOV torsion witness", with explicit
  flag "This is weaker than a proof that the whole non-zero-spectrum
  determinant is metric-independent."

**Verdict.** No topological-strings merge debt. Vol III work is
internally bounded. The +275-line chain-level-bridge inscription is
Vol III's framed Hochschild target apparatus, bound to Vol III's
$E_3$ / CY3 / DWR-Ran factorization spine.

### §1.2 `igusa-cusp-form`

**HEAD.** `master` at `b7c7a2b` "Rectify cross-references and close
opening loop".

**Uncommitted (`git status --short`).** 81 entries.
- **9 staged-`A`** (new files already in index):
  `materials/processed/2026-04-28-090346-attack-whitepaper-analysis.txt`,
  `materials/raw/2026-04-28-090346-attack-whitepaper-analysis.pdf`,
  `notes/attack_whitepaper_analysis_20260428_090346_guide.md`,
  `notes/{eighth,ninth,tenth,eleventh,twelfth,thirteenth}_reconstitution_*.md`,
  `refs/source-provenance.md`.
- **5 modified** tracked files: `compute/verify_square_root.py`,
  `main.tex`, `out/main.pdf`, `proj.bib`,
  `raeez.lorgat.automorphic-corrections.pdf`.
- **~60 untracked `??`**: `.agents/`,
  `.claude/commands/chriss-ginzburg-rectify.md`,
  `compute/__pycache__/`, two extra whitepaper-analysis materials,
  the full taxonomy of fourteenth/fifth/fourth/third/seventh/sixth/
  next attack-heal reports across chain, d0, hybrid, koszul,
  orientation, recognition, weyl-pfaffian, o2-walls, primitive-
  recognition, integration-map.

**`git diff --stat HEAD` magnitude (tracked diffs).**
- `main.tex`: **+9262 / -2109 = net +7153 lines** (largest
  manuscript expansion in any sister volume).
- `compute/verify_square_root.py`: 348 lines.
- Untracked notes (~60 markdown files at 200-500 lines typical) add
  an estimated **+15,000 to +30,000 lines** of swarm reports.

**Recent commits (last 10).** All Igusa-internal: cross-reference
rectification, Phase-3 PDF release at 111 pages 768K, Phase-3 honest
tightening, AI-tell sweep, $cgr/2A2$-deep-scrub merge with 2079
lines net deleted, $A_\infty$ rectification of hypothesis (P).

**Branches.** **80+** branches. Taxonomy:
- 38 `agent/igusa-*-20260428` swarm sandboxes (wave-3/4/5/6/7).
- 28 `close-*-{1887a7d, 2c0bec4, feb4161}` close-out branches
  (P3-{a,b}, P4, P5, P6, F-{a,b}, O-{a,b}, bmu2-{a,b,c,d,e},
  bottnorm, imag-walls, paired-block, S1equiv, strictrect,
  w2-vs-aut, wstrict, R-Step4 / R-Step4-actual / R-Step4-attack-actual
  / R-Step4-b, R-O2 / R-O2-b, RBib).
- 5 `heal/{dirac-automorphic-dt, gn-anchors, lattice-factorization-bv,
  lemma1-theorem2, theorem3-orientation}` heal branches.
- 2 `cgr/{2A-bookkeeping-scrub, 2A2-deep-scrub}` Chriss-Ginzburg
  rectification branches; both already merged into master.
- 2 `preserve/{master-base-20260427, w2-chiral-upgrade-20260427}`
  preservation branches.
- `master` (current).

**Active worktrees.** **76 entries** in `.git/worktrees/`:
`heal-H{1-5}-{96f6acc, efc2583}`, `igusa-agent-{chain, d0, hybrid,
orient, recognition, weyl}`, `igusa-c{6,7,8}-*` (15 c-cycle worktrees),
`igusa-cgr-{2A, 2A2}`, `igusa-{third, fourth, fifth, sixth, seventh,
next}-*` (~40 swarm-cycle worktrees).

**Cross-volume reference test.**
- `git diff HEAD -- main.tex` filtered for
  `bcov|hamiltonian.bf|brane.defect|moyal|topological.string|q\(N\)|kodaira.spencer`
  returns **0 matches**.
- The 60+ untracked `notes/*attack_heal*.md` markdown files: zero
  hits for the same regex (grep on `notes/*.md` and `notes/*/*.md`).
- Commit-log scan since 2026-04-25 returns 0 cross-firewall hits.

**Verdict.** No topological-strings merge debt. Igusa wave-5 work is
massive and active but firewalled to its own modular-form frontier
(P3-P6, F-a/b, O-a/b, bmu2 small-orbit gerbe vanishing, b-cocycle
central extension, Sym_3 cyclic invariance, Borcherds f(0,2)=0
paired block, imaginary-wall orientation extension, weyl-equivariant
orientation cocycle, S^1-equivariance Goodwillie remark). The
Borcherds / BKM heuristic bridge to topological-strings is
charter-permitted and convention-only.

### §1.3 `chiral-bar-cobar` (Vol I)

**HEAD.** `master` at `7c57322` "release pdf".

**Uncommitted (`git status --short`).** 7 entries, all `D` (deletions)
of standalone PDFs in `standalone/`: `N2_mc3_all_types.pdf`,
`N3_e1_primacy.pdf`, `N6_shadow_formality.pdf`,
`cy_quantum_groups_6d_hcs.pdf`, `introduction_full_survey.pdf`,
`programme_summary.pdf`, `programme_summary_sections2_4.pdf`. Zero
TeX modifications.

**`git diff --stat HEAD` magnitude.** 7 PDF deletions, 0 insertions.
Trivial — these are byproduct artifacts.

**Recent commits (last 10).** Vol I-internal: standalone refinements
(Vol I determinant: line-bundle analogy, canonical operator
exposition), 4-volume LaTeX prose audit ledger, KZ/BV analytic-SDR
scope propagation into 5-theorem comparison spine, Vol I compact
PDF artifacts.

**Branches.** Only 3: `main` (current), `agent-w2-cplus-load`,
`agent-w2-phi25`. 5 commits since 2026-04-25.

**Active worktrees.** 2 entries: `agent-w2-cplus-load`,
`agent-w2-phi25` (parked since 2026-04-26 02:34).

**Cross-volume reference test.** No diff content; commit-log scan
since 2026-04-25 returns 0 hits. The `cy_quantum_groups_6d_hcs.pdf`
deletion is a Vol I housekeeping artifact for a deprecated
standalone, not a cross-volume edit.

**Verdict.** No topological-strings merge debt. Vol I is in
publication-stable state.

### §1.4 `chiral-bar-cobar-vol2` (Vol II)

**HEAD.** `main` at `2b9d966` "release pdf".

**Uncommitted (`git status --short`).** Empty.

**`git diff --stat HEAD`.** Empty.

**Recent commits (last 10).** Vol II-internal: standalone survey
refinement, manuscript prose fortification, KZ side Makefile parity,
KZ analytic-SDR constructive branch merge, BV/PVA topologisation
scope repair, Vol II standalone TeX failure classifier (and its
back-port to main).

**Branches.** 3: `main` (current), `codex/kz-bv-constructive-20260424`,
`w2-heptagon-coherence`. 1 commit on `main` since 2026-04-25
(the release PDF).

**Active worktrees.** 1 entry: `chiral-bar-cobar-vol2-kz-bv-20260424`
pinned to `refs/heads/codex/kz-bv-constructive-20260424` (parked
since 2026-04-25 15:08).

**Cross-volume reference test.** No diff content; commit-log scan
since 2026-04-25 returns 0 hits.

**Verdict.** No topological-strings merge debt. Vol II is in
publication-stable state.

---

## §2. Cross-volume merge-debt audit

### §2.1 Wave-4 / Wave-5 work matrix

| Volume | Status size | Wave-4/5 commits since 04-25 | Active worktrees | Tracked diff into ts-primitives? |
|---|---|---|---|---|
| Vol III | 30 entries; ~6k churn / -85 net | $\approx 5$ on `main` (+legacy) | 7 swarm worktrees | NO (BCOV refs are Hodge-cohomology on compact CY$_3$, not chain-level on $\R^2\times\widehat{\C^2}_0$) |
| Igusa | 81 entries; +7153 main.tex / +25k+ notes | $\approx 10$ on `master` since 04-26 | 76 swarm worktrees | NO ($\Delta_5$ Borcherds determinant internal) |
| Vol I | 7 PDF deletes | $\approx 9$ since 04-25 | 2 (parked) | NO (deletions only) |
| Vol II | empty | 1 since 04-25 | 1 KZ-BV worktree | NO (KZ-BV branch is Vol II internal) |

### §2.2 Reconstitution-directory check

Only topological-strings has a `reconstitution/` tree (the
`attack-heal-platonic-2026-04-28.md` ledger and 100+ wave-3/4/5/6
exec reports). None of the four sister volumes has a
`reconstitution/` directory — confirming that the reconstitution
discipline is currently localised to topological-strings.

### §2.3 Firewall preservation under uncommitted work

For every sister-volume diff that referenced BCOV, the reference is
at one of the following levels:

- **Vol III:** $\alpha_{\BCOV} = \chi_{\mathrm{top}}(X)/24 \cdot
  [\Omega_X]^{0,1} \in H^{0,1}(K3\times E)$ (Hodge cohomology on a
  compact CY$_3$, Costello-Li 2016 Prop 5.2). Same level as W5-X1
  §1's verdict: **not chain-level** in
  $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$. The agent09 BCOV
  one-loop note is currently being healed *to weaken its claim* —
  current uncommitted state retracts "explicit one-loop BCOV
  partition function" to "one-loop BCOV torsion witness", explicitly
  flagging metric-dependence beyond the Euler-class anomaly.
- **Igusa:** No BCOV/Hamiltonian-BF/Moyal references in uncommitted
  diff. The 2026-04-28 whitepaper analysis is an Igusa-internal
  critical analysis ingestion; no cross-volume claim.
- **Vol I, Vol II:** No relevant content.

**FW.BCOV firewall preserved across all four uncommitted sister
worktrees.** No chain-level isomorphism is alleged on either side
of any sister-volume firewall.

---

## §3. Cross-volume integration scope estimate

### §3.1 Per-volume line-delta into topological-strings

| Volume | Estimated delta into topological-strings |
|---|---|
| Vol III | 0 lines. All Vol III work belongs in Vol III. The W5-X1 declarative cross-volume audit and X17's worktree audit agree: BCOV references are intentionally one-way (Vol III consumes BCOV physics motivation, topological-strings does not consume Vol III chain-level claims). |
| Igusa | 0 lines. Igusa wave-5 reconstitution targets the $\Delta_5$ determinant internal architecture; the topological-strings $K3\times E$ heuristic bridge is one-way (topological-strings consumes Igusa's Borcherds bridge as motivation, Igusa does not consume topological-strings primitives). |
| Vol I | 0 lines. PDF deletions only. |
| Vol II | 0 lines. Empty status. |

**Total cross-volume merge debt to topological-strings: 0 lines.**

### §3.2 Publication-blocking dependencies

None. Topological-strings can publish without waiting on:

- Vol III's 14-agent perturbative $E_3$ hCS swarm to land
  ($\alpha_{\BCOV}$ vanishing on $K3\times E$ is a Vol III internal
  question for the CY-to-chiral functor at $d=3$; topological-strings
  uses BCOV as physics motivation only).
- Igusa's Phase-3 to Phase-4 reconstitution sweep (the topological
  string $\to$ Igusa modular-form bridge is heuristic and
  convention-checking, not load-bearing for the local Hamiltonian BF
  / Moyal calculation).
- Vol I's standalone-PDF housekeeping or Vol II's KZ-BV constructive
  branch.

The reverse implication (do these volumes block on topological-strings?)
is also negative: each sister volume is publishing on its own
schedule with its own firewall typology.

### §3.3 Convention-anchors to monitor on next cycle

Passive observation (no inscription pending):

- **`d = dim_C X`** convention: topological-strings `notation.tex`
  vs Vol III `chapters/theory/cy3_chain_level_bridge.tex` (the
  in-flight +275-line `def:framed-hcs-hochschild-target` adds
  $X$-CY$_3$ machinery and Hochschild-target conventions adjacent to
  topological-strings factorization conventions in
  `appendix-factorization-current-conventions.tex`).
- **Worldsheet $\Sigma$ vs DWR/Ran-nerve simplex**:
  topological-strings `mathmacros.tex` vs Vol III's
  $\PhiFA^{\HH,\mathrm{fr}}_{3,N}(\Perf(X))$ definition.
- **Framing datum on $S^3$**: topological-strings `tate-P*` vs Vol III
  swarm-blocker6 agent03 spectral-gap note (parked, mtime
  2026-04-25 15:08).

These are convention anchors, not pending repairs. They would
become merge debt only if a Vol III statement asserted a
load-bearing isomorphism with a topological-strings primitive.

---

## §4. Verdict

**MERGE-CLEAN.** All four sister volumes have firewall-preserving
worktree state with respect to topological-strings. No deep-semantic
merge into topological-strings is required to clear cross-volume
debt before publication.

**Caveat.** The volume of in-flight work in Vol III (~6000-line
in-place rewrite churn across the 14-agent swarm-blocker6 v2 fleet,
+275-line chain-level-bridge chapter inscription, 7 active
worktrees) and Igusa (+7153-line `main.tex` expansion, 60+ untracked
attack-heal reports, 80+ branches, 76 active worktrees) is large.
Both volumes are in mid-wave-5 swarm cycles. This is not merge debt
for topological-strings; it is the current state of the four-volume
constellation, where each volume drives its own attack-heal cadence.

**Cross-validation with W5-X1.** X1 (declarative firewall consistency
via `CLAUDE.md` + `main.tex`) and X17 (worktree-state probe) reach
the same verdict: all five firewalls (BCOV, Sergeev-A5, Igusa,
Unreduced-Bosonic, Costello-Li-d-even) hold across the constellation,
both in the published source-of-truth (X1) and in the active
in-flight worktrees (X17). The two-lens audit closes.

**Open monitor item.** If Vol III's 14-agent swarm lands a chain-level
$E_3$ identification on $K3\times E$ that propagates to a global
BCOV statement requiring topological-strings local Hamiltonian BF
input, that would be a future merge-debt event. The current Vol III
in-place healing of the agent09 / agent10 BCOV notes is *retreating*
from such a claim (title weakened, abstract scope reduced to scalar
torsion witness, explicit metric-dependence flag inscribed). As of
2026-04-28 23:40 PT, no such cross-volume inscription has landed.

**RELAUNCH delta vs prior X17.** Substantively identical conclusions.
The relaunch sharpens (i) the staged-vs-untracked split inside Igusa
(9 staged + 60 untracked, vs the prior X17's "12 modified or added,
70+ untracked"), (ii) the per-agent line counts inside the
swarm-blocker6 origin commit `7634eef` (8207 lines across 14 files,
not estimated), (iii) the in-place-vs-new-file confirmation that
Vol III is healing its swarm output rather than adding new
inscriptions, and (iv) the agent09 BCOV one-loop note retraction
language confirming firewall-preserving healing direction.

**Report.** This file
(`reconstitution/phase4-exec-W5-X17-cross-volume-worktree-2026-04-28.md`).

End of W5-X17 RELAUNCH.
