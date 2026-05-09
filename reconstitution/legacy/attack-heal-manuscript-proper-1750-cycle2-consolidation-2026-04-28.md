# Attack-Heal Manuscript Proper 17:50 Cycle 2 Consolidation

Date: 2026-04-28  
Repository: `/Users/raeez/topological-strings`  
Source critique: `materials/processed/2026-04-28-1750-whitepaper-critical-analysis.txt`  
Launch record: `reconstitution/attack-heal-manuscript-proper-1750-cycle2-launch-2026-04-28.md`

## Swarm Status

Six read-only / proposal-only adversarial agents were launched against the manuscript proper after the first 17:50 reconstitution attack-heal pass.

All six returned and were closed. No subagent was write-capable. No TeX repair was inscribed in this cycle. The only command-level computation reported by the swarm was the read-only Moyal script check:

```text
python3 scripts/check_moyal_coefficients.py
N=2: checked 80
N=3: checked 80
```

## Convergence Verdict

No convergence for the manuscript proper as a shippable reconstructed paper.

The cycle confirms the known casualties and adds several manuscript-proper leaks. A smaller dependency-closed core survives only if the paper explicitly excludes or conditions the following from the proved core:

- full `Z^{P_0}_{fact}` theorem;
- full open BV algebra identification;
- conilpotent Koszul duality for the full formal Hamiltonian algebra;
- bare `R`-submodule Matlis annihilator wording;
- unconditional finite-`N` radial-parts theorem;
- normalized-Moyal "no `hbar^2` correction" claim;
- Costello graph theorem from reduced Wick diagrams;
- exhaustive "exactly three" QME classification.

The surviving core is therefore a reduced computational manuscript: direct reduced CE/PV calculations, fenced one-psi PBW/indecomposable primitives, formal Moyal coefficient computations with the actual normalized higher terms, and conditional bridges to unreduced BV, radial parts, Costello graph weights, and cross-volume consequences.

## Stable Core After Cycle 2

The following claims can remain inside the stable core if rewritten with the named fences.

1. Reduced CE/PV computation. The paper may prove a direct reduced Hamiltonian CE/PV statement, for example `Z^{P_0}_{red,Ham}(A) := PV(A)`, provided it is not advertised as the full factorization center and does not rely on unproved open BV centrality homotopies.

2. One-psi primitive. The one-psi theorem is not itself a casualty. It is adequately fenced as a PBW / indecomposable shadow at `main.tex:3033-3052` and in `tate-T5-chain-level-primitive.tex`, provided higher-psi primitives, unreduced centrality, and cotangent-lift claims remain open.

3. Formal Moyal calculation. The normalized bracket must use
   ```tex
   \{f,g\}_{\hbar}=P(f,g)+\frac{\hbar^2}{24}P^3(f,g)+\frac{\hbar^4}{1920}P^5(f,g)+\cdots .
   ```
   Raw even commutator orders may vanish by parity; the normalized bracket generally has an `hbar^2` correction.

4. Scalar quotient bracket. The scalar quotient is adequately fenced in the active manuscript at `main.tex:157-168`, `2236-2237`, `2874-2891`, and `3061-3102`.

5. Rendered figures. The active rendered figures are inline TikZ with labels and weights. Stale SVG sources are debris, not a blocker for the rendered manuscript.

6. Cross-volume consequences. The cross-volume material can remain only as heuristic / convention-checking context unless a local theorem supplies a matched-conventions proof.

## Destroyed Or Non-Core Claims

### A. Full Factorization-Center Identification

Status: valid severity-1 casualty.

Anchors:

- `main.tex:1996-2047`
- `main.tex:2212-2220`
- `main.tex:2322-2348`
- `main.tex:2427-2435`
- `theorem-lanes.tex:96-148`
- `principles.tex:56-71`

Failure mode: the reduced PV algebra is locally named as a factorization center, but the manuscript still lacks a full factorization-center target category, open BV object, centrality homotopies, descent, and product coherence.

Minimal heal: define the reduced direct object explicitly, e.g. `Z^{P_0}_{red,Ham}(A):=PV(A)`, and reserve `Z^{P_0}_{fact}` for the unreduced open-BV factorization-center problem.

### B. Continuous Tate HKR

Status: valid severity-1 proof gap.

Anchors:

- `main.tex:2050-2067`
- `main.tex:2127-2137`
- `main.tex:2193-2209`

Failure mode: ordinary HKR is invoked for a completed Tate algebra without a continuous Hochschild model, finite-window comparison, naturality in the inverse system, and derived-limit control.

Minimal heal: split the direct CE/PV computation from any HKR theorem; any HKR statement must be finite-window or continuous with topology, completed tensors, and limit hypotheses written into the theorem.

### C. Compact-Support Factorization Currents

Status: valid severity-1 proof gap.

Anchors:

- `main.tex:2174-2188`
- `main.tex:2788-2801`
- `tate-T5-chain-level-primitive.tex:778-787`

Failure mode: an open interval has `H_c^1(I)=C`, not degree-zero point values. The manuscript still treats compact-support contraction too much like ordinary point evaluation.

Minimal heal: write the density contraction explicitly: choose `lambda_I dt`, define `p`, `i`, and `K`, prove `dK+Kd=id-ip`, and record the degree and sign conventions.

### D. Conilpotent Koszul Duality For Full Formal Hamiltonians

Status: valid severity-1 casualty.

Anchors:

- `main.tex:187-194`
- `main.tex:3295`
- `main.tex:3336-3340`
- `main.tex:3428-3433`
- `main.tex:3481-3542`
- `main.tex:3544-3569`
- `theorem-lanes.tex:96-147`
- `tate-T2-nilpotent-truncation.tex:484-499`
- `tate-T3-quillen-equivalence.tex:398-468`

Failure mode: the manuscript still lets the reader infer that full closed CE cochains have Koszul dual `\widehat U(\mathfrak g)` as a theorem. But the available bar-cobar theorem needs conilpotence, and the full formal Hamiltonian algebra is not conilpotent in the required sense.

Minimal heal: split the material into layers:

- direct CE/PV theorem for the reduced algebra;
- Tate-conilpotent / nilpotent / admissible envelope theorem for bar-cobar;
- PBW/Rees special-fibre label comparison;
- conjectural or conditional full brane-closed deformation-level duality.

The introduction must say this before the reader reaches the technical section.

### E. Matlis Principal-Parts Wording

Status: valid severity-1 wording/proof mismatch.

Anchors:

- `abstract.tex:18-20`
- `claim-strength-ledger.tex:48-53`
- `local-dictionary.tex:143-147`
- `theorem-lanes.tex:164-174`
- `principles.tex:171-190`
- `main.tex:3760-3765`
- `main.tex:3840-3846`
- `main.tex:3908-3924`
- `main.tex:4212-4222`
- `main.tex:4425-4433`
- `appendix-matlis-principal-parts.tex:90-120`

Failure mode: the manuscript still speaks of an `R`-submodule annihilator or bare `Ann(C\cdot 1)`. The object constructed by the residue pairing is not an `R`-submodule in that naive sense.

Minimal heal: define `\operatorname{Ann}_{res}(\mathbb C\cdot 1)` as a `\mathbb C`-linear residue annihilator and replace every bare annihilator phrasing accordingly.

### F. Rees/Fourier Bridge Status Conflict

Status: valid severity-2 reader-confusion issue.

Anchors:

- `abstract.tex:38-40`
- `main.tex:1081-1088`
- `main.tex:4058-4072`
- `main.tex:4111-4112`

Failure mode: the text says the Rees/Fourier bridge does not exist, while appendices construct a limited Fourier-delta Rees label bridge.

Minimal heal: distinguish the forbidden same-action / deformation-level `\mathfrak h`-module bridge from the limited label bridge that is actually constructed.

### G. Unconditional Radial-Parts / Finite-`N` Comparison

Status: valid severity-1 casualty.

Anchors:

- `main.tex:4917-4923`
- `main.tex:5459-5498`
- `main.tex:5533-5543`
- `tate-T2-nilpotent-truncation.tex:263-268`

Failure mode: the proof of the all-order degree-zero comparison cites a conditional radial-parts input but the surrounding prose still reads as an unconditional theorem or as "no remaining obstruction."

Minimal heal: split the formal coefficient theorem from the finite-`N` stable trace theorem, and attach the external radial-parts hypothesis everywhere the finite-`N` comparison is invoked.

### H. Normalized-Moyal `hbar^2` Claim

Status: valid severity-1 counterexample.

Anchors:

- `main.tex:5011-5056`
- `main.tex:5396-5435`

Counterexample:

```tex
f=z_1^3z_2,\qquad g=z_1z_2^3.
```

Then

```tex
P(f,g)=8z_1^3z_2^3,\qquad P^3(f,g)=-72z_1z_2,
```

so the normalized bracket contains

```tex
8z_1^3z_2^3-3\hbar^2 z_1z_2+O(\hbar^4).
```

Minimal heal: rewrite the theorem and all prose to say that raw even commutator orders vanish by parity, while normalized Moyal brackets generally have `hbar^2`, `hbar^4`, ... terms.

### I. Script Evidence Mismatch

Status: valid severity-2 source/evidence mismatch.

Anchors:

- `main.tex:4981-4984`
- `scripts/check_moyal_coefficients.py:48-55`
- `scripts/check_moyal_coefficients.py:737-743`
- `scripts/check_moyal_coefficients.py:921-930`

Failure mode: the manuscript reports a count inconsistent with the script output. The script reports 80 checked pairs for `N=2` and 80 for `N=3`, not 36. Its connected cumulant projection also only verifies `P^1` in the primary cases where higher odd powers vanish.

Minimal heal: update the count and either weaken the script-prose claim or add higher-order connected-cumulant tests using examples with nonzero `P^3`, such as the Moyal counterexample above.

### J. Costello Graph Theorem From Reduced Wick Diagrams

Status: valid severity-1 casualty.

Anchors:

- `abstract.tex:34-36`
- `claim-strength-ledger.tex:103-106`
- `open-obligations.tex:153-157`
- `main.tex:5648-5655`
- `main.tex:5780-5803`
- `main.tex:5842-5875`

Failure mode: reduced open-line Weyl/Moyal boundary coefficients do not by themselves prove a Costello graph theorem. The analytic Costello object needs locality, renormalization, counterterms, propagator data, BV integration, and QME control.

Minimal heal: say the paper computes first and third reduced open-line Weyl/Moyal boundary coefficients. Costello graph realization remains conditional on the analytic graph/RG construction.

### K. Exhaustive QME Classification

Status: valid severity-1 casualty.

Anchors:

- `principles.tex:131-154`
- `open-obligations.tex:123-151`
- `appendix-unreduced-bv-qme.tex:160-178`
- `main.tex:5339-5345`

Failure mode: the manuscript names three candidate mechanisms as though they are exhaustive, but no obstruction-complex computation proves exhaustiveness.

Minimal heal: replace "must either" / "exactly three" classification language with "known candidate mechanisms include." Exhaustiveness requires an `H^1` obstruction-complex theorem.

## New Valid Attacks Found In Cycle 2

### L. Finite-Window Factorization-Center Overclaim

Status: valid severity-2 leak.

Anchors:

- `tate-T2-nilpotent-truncation.tex:157-181`
- `tate-T2-nilpotent-truncation.tex:199-222`
- `tate-T2-nilpotent-truncation.tex:376-397`

Failure mode: finite-dimensional nilpotent truncation removes one analytic difficulty but inherits the broken interval `Z^{P_0}_{fact}` and compact-support proof.

Minimal heal: describe the finite truncation as a finite nilpotent CE/PV cotangent shadow or finite-truncation free-center model, not as an unreduced open-BV factorization-center morphism.

### M. Quillen Equivalence Promotion

Status: valid severity-2 leak.

Anchors:

- `tate-T3-quillen-equivalence.tex:398-424`
- `tate-T3-quillen-equivalence.tex:443-467`
- `tate-T3-quillen-equivalence.tex:495-528`

Failure mode: a Lie bar-cobar Quillen equivalence does not construct a completed dg `P_0` model structure, factorization algebra, or local centrality theorem for the full object.

Minimal heal: make every T3 use an admissible-envelope theorem or a finite nilpotent theorem; do not use it as independent evidence for the full manuscript theorem.

### N. Reduced Principal-Part Current Center

Status: valid severity-2 leak.

Anchors:

- `main.tex:4240-4296`
- `main.tex:4298-4367`
- `main.tex:4369-4377`
- `appendix-factorization-current-conventions.tex:107-148`

Failure mode: a reduced semidirect `P_0` current algebra is called a center sector without Hochschild or `P_0` centrality homotopies.

Minimal heal: call it a reduced current model or reduced principal-part sector; keep "center" reserved for a proved central object.

### O. Weighted Completion Versus Conilpotence

Status: valid severity-2 leak.

Anchors:

- `tate-T1-weighted-completion.tex:433-490`
- `tate-T1-weighted-completion.tex:493-528`

Failure mode: the weighted Casimir and weighted QME/locality arguments are allowed to imply conilpotent bar-cobar or factorization-center conclusions. They do not.

Minimal heal: use weighted completion only for generator-level CE/PV identity or conditional cochain-level target maps, unless a separate weighted factorization-center object and centrality-homotopy theorem is proved.

### P. Weighted Locality / RG Overclaim

Status: valid severity-2 leak.

Anchors:

- `tate-P1-hadamard-mittag-leffler.tex:126-168`
- `tate-P1-hadamard-mittag-leffler.tex:216-244`

Failure mode: graphwise finite-window wave-front support is treated as full Costello locality for the inverse-limit field theory. The manuscript has not proved topology, jet-density continuity, summability, or counterterm compatibility for the full inverse limit.

Minimal heal: state graphwise finite-window Hadamard control only. Do not call it a full Costello locality or QME theorem.

### Q. Frontmatter Geometry Error

Status: valid severity-2 concrete error.

Anchor:

- `main.tex:77-84`

Failure mode: `\mathbb R^2\times\mathbb C^2` is described as "1+4-real-dimensional." It is real dimension six.

Minimal heal: write the geometry as `\mathbb R_{brane}\times\mathbb R_{top,normal}\times\mathbb C^2_{hol}`, total real dimension six, with the brane line specified separately.

### R. Cross-Volume Firewall Geometry Mismatch

Status: valid severity-2 reader-confusion issue.

Anchors:

- `main.tex:8-11`
- `main.tex:1881-1885`
- `main.tex:5896-5914`
- `tate-P5-cross-volume.tex:11-16`
- `tate-P5-cross-volume.tex:56-61`

Failure mode: the firewall says the model is local at `\mathbb R\times\widehat{\mathbb C^2}_0`, while the active geometry is `\mathbb R^2_{top}\times\mathbb C^2_{hol}` with a brane line `\mathbb R\times\{0\}\times\{p\}`.

Minimal heal: use one geometry convention throughout the firewall and frontmatter.

### S. Source Hygiene / Local-Path Evidence

Status: valid severity-2 external-facing manuscript issue.

Anchors:

- `theorem-lanes.tex:391-396`
- `main.tex:2537-2541`
- `main.tex:4981-4989`
- `main.tex:5668-5672`
- `main.tex:5812-5817`
- `appendix-radial-parts-moyal.tex:340-365`

Failure mode: rendered TeX cites local scripts and local paths as theorem evidence. That is not a standalone public-source presentation.

Minimal heal: move computations into an appendix table, cite public/archived artifacts if needed, or phrase local scripts as internal verification outside the theorem proof.

### T. Eight-Casualty Standalone Table Missing

Status: valid severity-2 manuscript-architecture issue.

Anchors:

- `main.tex:1164-1191`
- `theorem-lanes.tex:96-148`
- `theorem-lanes.tex:209-265`
- `theorem-lanes.tex:344-418`
- `claim-strength-ledger.tex:73-123`

Failure mode: a cold reader can still infer stronger theorems than the manuscript proves. The eight main casualties are not all stated in one reader-visible theorem-status table.

Minimal heal: insert a single eight-row status table in the front matter or theorem-lane section, using the 17:50 casualty formulation and exact proved/open/conditional labels.

### U. Route / Process Code Leakage

Status: valid severity-3 style and standalone issue.

Anchors:

- `main.tex:2685-2710`
- `tate-T4-bv-vanishing.tex:13`
- `tate-T2-nilpotent-truncation.tex:20-24`
- `tate-T3-quillen-equivalence.tex:545-585`

Failure mode: route codes such as `R0-R3`, `T3`, and `T4` read like internal process scaffolding rather than mathematical structure.

Minimal heal: replace route labels with mathematical names in the reader-facing paper.

## Invalid Or Overturned Attacks

1. The one-psi primitive is not destroyed as stated. It survives as a PBW / indecomposable shadow, with higher-psi and unreduced centrality still open.

2. No active Layer-7 theorem overclaim was found. Layer 7 is marked conjectural at `main.tex:490-504` and `claim-strength-ledger.tex:125-128`.

3. The scalar quotient bracket is adequately fenced in the active manuscript.

4. The rendered figure attack is not fatal: current figures are inline TikZ; stale SVGs are unused source debris.

## Repair Order For The Next Manuscript Wave

1. Frontmatter truth table. Add the eight-casualty theorem-status table before the reader meets the theorem lanes.

2. Vocabulary pass. Replace `Z^{P_0}_{fact}` / "center" / "open BV algebra" wording with reduced-object names unless the local proof supplies the full centrality data.

3. Koszul layer pass. Add the Layer 0-7 ledger and separate direct CE/PV, admissible conilpotent, PBW/Rees, and conjectural deformation-level claims.

4. Matlis pass. Define `\operatorname{Ann}_{res}` and remove bare `R`-submodule annihilator language.

5. Moyal pass. Correct the normalized expansion, insert the counterexample, update script-count prose, and condition finite-`N` radial claims.

6. Costello/QME pass. Replace graph-theorem and exhaustive-QME language with conditional analytic obligations.

7. Geometry/firewall/source-hygiene pass. Fix the six-real-dimensional geometry, cross-volume firewall convention, local-path citations, and process-code leakage.

## Verification Still Needed

Before declaring the next wave healed, run targeted scans rather than a full rebuild after each edit:

```text
rg -n "Z\\^\\{P_0\\}_\\{fact\\}|factorization center|open BV algebra|Ann\\(|annihilator submodule|no.*hbar\\^2|hbar\\^2 correction|exactly three|must either|Costello graph theorem|radial-parts|R0|R1|R2|R3|local script|/Users/" .
```

Then run a session-end build when the TeX repair wave is complete:

```text
make pdf
```

Convergence criterion for the next wave: every severity-1 and severity-2 item above is either healed by explicit manuscript text and proof/data, invalidated by a local check, or moved outside the manuscript's stable core with a visible open-obligation label.
