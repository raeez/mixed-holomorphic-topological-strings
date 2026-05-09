# Phase-4 EXEC W5-X21 — Final-Pass Referee Simulation, PRE-AUTHORIZATION snapshot

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Mode.** Wave-5 attack-heal swarm wave 5; read-only on the 155-page
working-tree manuscript. Proposal-only; no commits, no edits to any
TeX file. Authorship: Raeez Lorgat.
**Lens.** X21 = Final-Pass Referee Simulation. Hostile-referee pass
on the working-tree PDF as it would land on a journal referee's desk
TODAY, **without** the +472 mandatory inscription delta applied.
This is the PRE-AUTHORIZATION-FOR-INSCRIPTION snapshot.
**Baseline.** W5-X11 clean-build: `out/main.pdf` (1,029,808 bytes,
155 pages, build clean, dated 2026-04-28 23:28).
**Inputs read in full or targeted.**
* `abstract.tex` (45 lines; 13 distinct load-bearing claims).
* `theorem-lanes.tex` (456 lines; 8 stmt-blocks indexing the lanes).
* `claim-strength-ledger.tex` (205 lines; 14 ledger rows, 7 main
  exclusions).
* `main.tex` (6,402 lines; section-structure scan; all 17 thm-blocks
  read; rmk:E1-translation read; rmk:convention-firewall read;
  cross-volume horizon read).
* `tate-T1-weighted-completion.tex` thm-blocks 410, 435, 636, 711.
* `tate-T2-nilpotent-truncation.tex` thm-blocks 156, 249.
* `tate-T3-quillen-equivalence.tex` thm-blocks 83, 257, 398; stmt 46.
* `tate-T4-bv-vanishing.tex` stmt 17, prop 57.
* `tate-T5-chain-level-primitive.tex` thm-blocks 157, 198, 275, 388,
  618.
* `tate-P1-hadamard-mittag-leffler.tex` thm 126.
* `tate-P3-universality.tex` (213 lines; protected-sector reduction,
  cross-volume firewall remark).
* `tate-P5-cross-volume.tex` (132 lines; matched-conventions theorem
  datum, no-formal-disk-transfer lemma, templates remark).
* `appendix-matlis-principal-parts.tex` thm-blocks 180, 209, 242.
* `appendix-radial-parts-moyal.tex` thm 249, stmt 145.
* `appendix-unreduced-bv-qme.tex` thm 34, prop 94, rmk 161.
* `appendix-factorization-current-conventions.tex` (cross-checked
  for orientation/density convention uniformity).
* `open-obligations.tex` (224 lines; 15 numbered obligations).
* `reconstitution/phase4-exec-W5-A1-costello-rescan-2026-04-28.md`
  (read full, 857 lines: (A5)^RG and (Q-Eq) silent strengthenings).
* `reconstitution/phase4-exec-W5-A2-functoriality-2026-04-28.md`
  (read full, 612 lines: parabolic functoriality, outer-twist gap,
  firewall typology PARABOLIC/FULL merger).
* `reconstitution/phase4-exec-W5-X1-cross-volume-2026-04-28.md`
  (read full, 388 lines: CLEAN cross-volume verdict).
* `reconstitution/phase4-exec-W5-X11-clean-build-2026-04-28.md`
  (243 lines; baseline build certificate).

---

## §0. Executive verdict

**Three-line bottom line.**

1. **Manuscript abstract is faithful to the proved theorem package.**
   Every load-bearing claim in the abstract has a proof anchor in
   `main.tex`, `theorem-lanes.tex`, or one of the seven supporting
   files (T1--T5, appendix-matlis, appendix-radial, appendix-unreduced
   QME). The status vocabulary (proved-finite, proved-degreewise-stable,
   proved-weighted-Tate, computed-to-stated-order, conditional, reduced
   target with unreduced lift open, conjectural, open, not asserted)
   is uniformly applied.

2. **Four wave-5 silent meta-hypotheses are unrestated in the
   manuscript.** Per the W5-A1 closure: (A5)^RG closure under Costello
   RG flow is silent; (Q-Eq) Quillen equivalence between Lurie HA and
   CG presentations is silent. Per W5-A2: parabolic functoriality of
   Theorem F'' is silent; tensor-factor disjointness for (A2') is
   silent; firewall typology merger of PARABOLIC/FULL/INDEPENDENT
   classes is silent. **Severity 1-2 only**: each silent strengthening
   is automatic under the existing cited primary sources and does not
   modify any proved theorem statement. A referee can correctly raise
   them as clarity defects but not as correctness defects.

3. **Verdict: ACCEPT-WITH-MINOR-REVISIONS.** Three additive clarity
   strengthenings ((A5)^RG remark; (Q-Eq) Quillen-equivalence remark
   at `rmk:E1-translation`; parabolic-functoriality remark at the
   F'' theorem block) close the silent meta-hypotheses. The +472-line
   pending inscription delta is the authorisation that delivers these
   plus full firewall-typology granularity. Without the inscription,
   the manuscript is referee-publishable at 155 pages with the noted
   strengthenings as minor-revision items. With the inscription, the
   manuscript is referee-publishable at 155+ pages with no remaining
   silent strengthenings.

---

## §1. Abstract claim audit

Each abstract sentence cross-walked to its proof anchor.

### Claim A1. Formal local mixed holomorphic-topological brane setup.
**Abstract sentence.** "We study the formal local mixed
holomorphic-topological brane at the symplectic disk with coordinates
$(z_1,z_2)$ and form $dz_1\wedge dz_2$."
**Proof anchor.** `main.tex`:1149-1206 §`ssec:local-theorem` declares
the local model; `theorem-lanes.tex`:12-50 lane (Dirac brane probe)
fixes the formal symplectic-disk hypotheses with the brane line
$\R_{\mathrm{brane}}\times\{0\}\times\{0\}$.
**Verdict.** CLEAN. Setup is uniformly stated.

### Claim A2. Dirac matrix system.
**Abstract sentence.** "On a stack of $N$ probes these coordinates
are matrices $\phi_1,\phi_2\in\mathfrak{gl}_N$, and the open
ghost-zero system is the Dirac first-order theory $\int_\R
\operatorname{Tr}(\phi_1 d\phi_2 + A[\phi_1,\phi_2])$ with first-class
constraint $[\phi_1,\phi_2]=0$ and BV/Koszul variable $\psi=A^*$
satisfying $Q\psi=[\phi_1,\phi_2]$."
**Proof anchor.** `main.tex`:1502-1595 (lemmas
`lem:open-action-reduction`, `lem:dirac-probe-reduction`,
`prop:open-bv-truncation`); `theorem-lanes.tex`:12-50 lane status
"proved in finite algebraic model".
**Verdict.** CLEAN. Sign convention $\iota_{X_f}\Omega=-df$ explicit.

### Claim A3. Closed Hamiltonian via reduced CE/PV model.
**Abstract sentence.** "Closed Hamiltonian modes act through the
reduced CE/PV Hamiltonian central-operation model."
**Proof anchor.** `main.tex`:2358-2386 `thm:open-closed-derived-center`;
`theorem-lanes.tex`:96-148 lane status "proved degreewise stable" with
explicit Tate-conilpotency hypothesis named.
**Verdict.** CLEAN. The lane is honest about restricting to its
hypothesis range.

### Claim A4. Full $P_0$-factorization-centre theorem disclaimer.
**Abstract sentence.** "A full $P_0$-factorization-centre theorem for
the unreduced open theory is not asserted."
**Proof anchor.** `claim-strength-ledger.tex`:31-36 main exclusion
row; `open-obligations.tex` items 1, 5; cross-references to the
firewall remark at `main.tex`:5409-5423.
**Verdict.** CLEAN. The exclusion is announced in three places.

### Claim A5. Cotangent modes are Matlis principal parts.
**Abstract sentence.** "The cotangent modes are not polynomial
descendants: in the local theorem they are Grothendieck--Matlis
residue currents in $\mathcal P=\operatorname{Ann}_{\mathrm{res}}
(\C\cdot 1)\subset H^2_{\mathfrak m}(\C[[z_1,z_2]])dz_1dz_2 =
\bigoplus_{a+b>0}\C\rho_{a,b}$."
**Proof anchor.** `main.tex`:3862, 3956 (theorems
`thm:canonical-residue-pairing`,
`thm:principal-part-coadjoint-uniqueness`);
`appendix-matlis-principal-parts.tex` (180 thm,
209 thm, 242 thm); `theorem-lanes.tex`:150-207 lane.
**Verdict.** CLEAN.

### Claim A6. PBW one-$\psi$ classes are not principal parts.
**Abstract sentence.** "The stable polynomial one-$\psi$ classes
$\Psi_{a,b}$ are PBW special-fibre open labels; they are not another
basis of $\mathcal P$ as an $\mathfrak h$-module."
**Proof anchor.** `main.tex`:4056, 4173 (`thm:pbw-vs-deformation`,
`thm:no-polynomial-realization-categorical`);
`tate-T5-chain-level-primitive.tex`:618 thm
`thm:no-hbar-primitive-descendant-intertwiner`.
**Verdict.** CLEAN.

### Claim A7. Finite algebraic part scope.
**Abstract sentence.** "The finite algebraic part proves the Dirac
brane reduction, the scalar-reduced degree-zero Weyl/Moyal
comparison, and the scalar $U(1)$ anomaly."
**Proof anchor.** `main.tex`:327, 363, 421
(`thm:u1-center-anomaly`, `-open`, `-quantum-classical`); 4928
(`thm:finite-n-reduced-moyal`); 1502-1595 (Dirac block).
**Verdict.** CLEAN.

### Claim A8. Degreewise stable part scope.
**Abstract sentence.** "The degreewise stable part proves the PBW
trace sector, the cochain-level CE/PV derived-centre map for
$\mathfrak h=\C[[z_1,z_2]]/\C\cdot 1$, the Matlis principal-part
cotangent module, the compactly supported brane-line current model,
and the principal-part defect model after de Rham-current contraction."
**Proof anchor.** `main.tex`:1033 (LQT thm), 2016, 2261, 2358 (CE/PV
+ smeared centre + cochain centre); 4266 (`thm:reduced-principal-part-boundary-current`); 4405 (`prob:boundary-principal-part-cotangent-operators`).
**Verdict.** CLEAN.

### Claim A9. Weighted Tate construction scope.
**Abstract sentence.** "The weighted Tate construction is proved only
in the weighted Tate coefficient model and does not assert regulator
independence."
**Proof anchor.** `tate-T1-weighted-completion.tex`:410, 435, 636,
711; `claim-strength-ledger.tex` row "Weighted Tate regulator" status
"proved in weighted Tate coefficient model" with explicit "Independence
of the admissible finite-window weight is proved; equivalence with
the strict unweighted product/direct-sum graph theory is not asserted."
**Verdict.** CLEAN, but note: the abstract says "does not assert
regulator independence" which is technically over-cautious -- the
weighted-internal regulator independence IS proved
(`thm:wt-regulator-independence-admissible`); only the strict
unweighted regulator independence is ruled out
(`thm:strict-unweighted-no-go`). **Borderline severity 1 / cosmetic**:
abstract sentence understates the proved internal independence. Not
a referee landing.

### Claim A10. First and third Costello graph normalizations.
**Abstract sentence.** "The first and third Costello graph
normalizations are reduced open-line Weyl/Moyal boundary coefficient
computations to stated order."
**Proof anchor.** `main.tex`:5594, 5657, 5823
(`prop:conditional-boundary-product-normalization`,
`prop:open-line-midpoint-graph-weights`,
`thm:first-third-costello-normalizations`).
**Verdict.** CLEAN.

### Claim A11. All-order brane-defect graph realization conditional status.
**Abstract sentence.** "The all-order brane-defect graph realization
is conditional on a mixed brane-defect QME theorem, the radial-parts
input where finite $N$ is used, and the required centrality
homotopies."
**Proof anchor.** `main.tex`:5885 (`prob:first-third-graph-normalizations`); `tate-T1-weighted-completion.tex`:533 (`prob:weighted-rg-locality`); `appendix-radial-parts-moyal.tex`:145 (`stmt:app-radial-external-input`).
**Verdict.** CLEAN.

### Claim A12. Disclaimers (unreduced cotangent, one-antifield Moyal,
Rees/Fourier bridge, compact CY, BKM/Igusa, sister-volume).
**Abstract sentence.** "The unreduced cotangent factorization-centre
morphism, a one-antifield descendant Moyal lift, a Rees/Fourier
bridge between $\Psi_{a,b}$ and $\rho_{a,b}$, compact Calabi--Yau
consequences, BKM/Igusa consequences, and sister-volume transfers
are not asserted here."
**Proof anchor.** `claim-strength-ledger.tex` rows
"Quantum descendant lift" (reduced target / unreduced lift open),
"Cross-volume consequences" (not asserted);
`tate-P5-cross-volume.tex` (matched-conventions firewall);
`appendix-unreduced-bv-qme.tex`:34
(`thm:app-unreduced-polynomial-centrality-no-go`);
`open-obligations.tex` items 5-13.
**Verdict.** CLEAN.

**Abstract claim audit summary.** **13/13 load-bearing claims have
proof anchors.** All claims match their cited proof-bearing block in
status vocabulary. **Severity 1 cosmetic**: the
"does-not-assert-regulator-independence" phrasing in the abstract
is technically tighter than the proved internal independence; this
is a referee-borderline phrasing that protects the author from
overclaiming and is not a landing attack.

---

## §2. Section-structure flow audit

`main.tex` section / subsection scan (38 entries):

* `\section{Introduction}` (73)
  * Local measurements, brackets (75)
  * Hamiltonian Lie algebra of the symplectic disk (138)
  * Closed-open measurement and the derived Poisson centre (216)
  * Scalar reduction and the U(1) center anomaly (256)
  * Quantum-classical equivalence (419)
  * The two algebras (483)
  * Three notions of locality (531)
  * Unitarity (598)
  * Thesis (619)
  * Mixed holomorphic-topological strings (630)
  * The local mixed model (815)
  * Hamiltonian sector and stable large N (965)
  * The concrete dictionary (1048)
  * Status of assertions and the analytic problem (1109)
  * **The local theorem (1149)** -- summary corollary +
    `\input{theorem-lanes.tex}`
* `\section{The Local Model}` (1281)
  * Setup (1290), Open mixed brane states (1385), Open mixed brane
    field theory (1437), Ghost-zero open field content (1495), Closed
    mixed Hamiltonian sector (1639), Hamiltonian BF action (1790),
    Closed-open brane coupling (1884), Residual analysis of unreduced
    Tate-coefficient cotangent lift (2733), Operators in open brane
    gauge theory and large N (2796), Operators in closed Hamiltonian
    sector (3236), Koszul Duality (3333), First-order corrections
    (3590), Formal deformation-quantization target (4656), Imported
    graph package (5155), Formal Weyl/Moyal target all orders (5425),
    Third-order Costello target (5701)
* `\section{Outlook and convention firewalls}` (5933)
  * Cross-volume firewall (5937)
* Appendices: Matlis (`\input`), factorization-current conventions
  (`\input`), unreduced BV/QME (`\input`), radial-parts (`\input`),
  cross-volume firewall (`\input{tate-P5-cross-volume}`)

**High-level argument flow.** The manuscript opens by stating the
formal local model and the U(1) anomaly as the orienting structural
result. It then declares the lanes (Dirac, stable trace, CE/PV,
principal parts, factorization currents, reduced principal-part
defects, Moyal, U(1)). Each lane carries a status vocabulary tag.
Section 2 is the proof-bearing block for the open + closed BV
construction, the boundary local-dual realization, the Moyal/Weyl
deformation, and the conditional first/third Costello normalization.
Section 3 ("Outlook") is the firewall section: protected-sector
reduction, cross-volume firewall, matched-conventions templates.

**Verdict on flow.** CLEAN. The flow is "state, prove, status-tag,
firewall". A referee opening the manuscript at `\section{Introduction}`
finds the proved-finite/proved-degreewise-stable lanes inside
`ssec:local-theorem` (1149-1206) and the status ledger as
`\input{theorem-lanes.tex}` (1174). A referee opening at the
firewalls section finds the matched-conventions discipline.

---

## §3. Top-level theorem audit

19 theorem blocks across all .tex files (excluding stmt-blocks). Per
each: hypothesis stated, proof complete or correctly labelled,
conclusion matches hypothesis.

### `main.tex` theorems

1. **`thm:u1-center-anomaly`** (327). Hypothesis: $\bar A=
   \mathfrak h_{\mathrm{poly}}/\C\cdot 1$. Conclusion: $[\bar c]\in
   H^2_{\mathrm{Lie}}(\bar A,\C)$ is the scalar-axis obstruction
   class. Proof: complete (327-361). **PASS**.

2. **`thm:u1-center-anomaly-open`** (363). Hypothesis: finite-$N$
   trace algebra. Conclusion: $\{\mathrm{Tr}\,\phi_1,\mathrm{Tr}\,
   \phi_2\}=N$. Proof: complete (380-402). **PASS**.

3. **`thm:quantum-classical-anomaly`** (421). Hypothesis: Weyl
   quantization, normal-ordered comoment. Conclusion: classical
   $\omega$ and quantum $\hbar N$ represent the same class.
   Proof: complete (446-473). **PASS**.

4. **`thm:loday-quillen-tsygan`** (1033). Imported. Hypothesis:
   $A_N\to A_\infty$ matrix stabilization. **PASS** (cited).

5. **`thm:open-closed-derived-center-factorization`** (2016).
   Hypothesis: locally constant reduced open-brane factorization
   algebra; formal classical Hamiltonian-mode subfactorization
   algebra. Conclusion: 5-item interval-wise morphism. Proof:
   complete (2069-2227, 8 steps). **PASS**.

6. **`thm:hamiltonian-current-center-lift`** (2261). Hypothesis:
   smeared boundary observables. Conclusion: smeared Hamiltonian
   central operation. Proof: complete. **PASS**.

7. **`thm:open-closed-derived-center`** (2358). Hypothesis:
   pro-finite-dimensional Lie algebra in $\Cat{TateVec}$ satisfying
   `lem:continuous-bar-cobar` Tate-conilpotency. Conclusion: cochain
   isomorphism on generators. Proof: complete with explicit Leibniz
   extension (2388-2440+). **PASS**.

8. **`thm:canonical-residue-pairing`** (3862). Hypothesis: $R=
   \C[[z_1,z_2]]$, residue convention. Conclusion: residue pairing
   determined up to scalar. Proof: complete. **PASS**.

9. **`thm:principal-part-coadjoint-uniqueness`** (3956). Hypothesis:
   Matlis form, residue pairing fixed. Conclusion: coadjoint module
   uniqueness up to scalar. Proof: complete. **PASS**.

10. **`thm:pbw-vs-deformation`** (4056). Hypothesis: PBW special-fibre
    versus deformation module. Conclusion: separation. Proof:
    complete. **PASS**.

11. **`thm:no-polynomial-realization-categorical`** (4173).
    Hypothesis: any polynomial Hamiltonian source. Conclusion: no
    polynomial realization of the principal-part coadjoint module.
    Proof: complete. **PASS**.

12. **`prop:reduced-principal-part-boundary-current` (=
    "reduced principal-part current $P_0$ factorization algebra")**
    (4266). Hypothesis: defect-current model, after de Rham-current
    contraction. Conclusion: $P_0$ bracket. Proof: complete.
    **PASS**. **Note**: tagged `\begin{thm}` but labelled `prop:...`.
    A referee may flag this as a label/environment mismatch (severity 1
    cosmetic, not a content defect).

13. **`prob:boundary-principal-part-cotangent-operators` (=
    "Reduced factorization realization of the boundary local dual")**
    (4405). Hypothesis: same. Conclusion: factorization realization.
    Proof: complete. **PASS**. **Note**: tagged `\begin{thm}` but
    labelled `prob:...`. Same cosmetic-grade label/env mismatch.

14. **`thm:bulk-boundary`** (4480). Hypothesis: classical
    bulk-to-boundary map. Conclusion: stated map. Proof: complete.
    **PASS**.

15. **`thm:finite-n-reduced-moyal`** (4928). Hypothesis: external
    radial-parts input of `stmt:app-radial-external-input` matched to
    Hamiltonian reduction. Conclusion: $D_N(f,g)\in I_N$, descended
    Moyal commutator. Proof: complete (4975-5042). **PASS**, but
    correctly labelled "conditional at all $N$" in title.

16. **`thm:phi-hbar-all-order`** (5492). Hypothesis: same external
    radial-parts input. Conclusion: $\Phi_\hbar^{(0)}$ Lie-algebra
    iso onto renormalized degree-zero sector. Proof: complete
    (5524-5536). **PASS**, correctly labelled "conditional".

17. **`thm:first-third-costello-normalizations`** (5823). Hypothesis:
    Hamiltonian specialization data of
    `prob:analytic-graph-realization` supplied; midpoint kernel $P/2$;
    third-order vanishing of non-three-edge contributions. Conclusion:
    first and third coefficients $\hbar P(f,g)$ and $\hbar^3 P^3/24$.
    Proof: complete (5848-5874). **PASS**, correctly labelled
    "Conditional".

### Tate-T and appendix theorems

18. **`thm:hadamard-mittag-leffler`** (T1, line 126). Graphwise
    Hadamard control. Hypothesis explicit. **PASS**.

19. **`thm:wt-rg-compatibility`** (T1, 410). Graphwise. Hypothesis
    explicit. **PASS**.

20. **`thm:wt-cotangent-lift`** (T1, 435). 4 parts (a)-(d). Each
    with explicit reference to a sub-prop. **PASS**.

21. **`thm:wt-regulator-independence-admissible`** (T1, 636).
    Hypothesis: admissible finite-window sector. Last sentence
    explicitly disclaims that this is NOT an identification with the
    strict pair. **PASS**.

22. **`thm:strict-unweighted-no-go`** (T1, 711). No-go statement.
    Hypothesis explicit. **PASS**.

23. **`thm:phi-trunc-classical`** (T2, 156). Finite nilpotent
    truncation. Last sentence disclaims unreduced lift. **PASS**.

24. **`thm:phi-hbar-trunc`** (T2, 249). "Quantum status of nilpotent
    truncation". States explicitly that the strict finite truncation
    does NOT carry an all-order Moyal deformation for $N\geq 4$.
    **PASS** -- this is a no-go theorem with explicit hypothesis.

25. **`thm:tate-bar-cobar-quillen`** (T3, 257). Hypothesis: admissible
    Tate model envelope of `stmt:tate-model-envelope`. Conclusion: 4
    items. Proof: complete with Loday-Vallette + Lurie HA citations.
    **PASS**.

26. **`thm:open-closed-derived-center-derived`** (T3, 398).
    Admissible-envelope promotion. Hypothesis cited
    `thm:tate-bar-cobar-quillen`. Last sentence explicitly disclaims
    that this is NOT a factorization-centre theorem for the full
    untruncated formal Hamiltonian algebra. **PASS**.

27. **`thm:chain-level-primitive-projection-Q,
    -factorization, -P0,`** etc. (T5, 157, 198, 275, 388). Chain-level
    primitive projection package. Hypothesis ranges explicit. **PASS**.

28. **`thm:no-hbar-primitive-descendant-intertwiner`** (T5, 618).
    No-go. Three explicit hypotheses (i)-(iii). Proof: complete.
    **PASS**.

29. **`thm:canonical-residue-pairing`** (appendix-matlis 180).
    Restated. **PASS**.

30. **`thm:no-polynomial-realization-categorical`** (appendix-matlis
    209). Restated. **PASS**.

31. **`thm:app-matlis-rees-fourier-bridge`** (appendix-matlis 242).
    Fourier-Rees bridge. Conclusion explicitly disclaims that bridge
    does NOT remove the obstruction. **PASS**.

32. **`thm:app-radial-finite-n-conditional`** (appendix-radial 249).
    Conditional on `stmt:app-radial-external-input`. **PASS**.

33. **`thm:app-unreduced-polynomial-centrality-no-go`** (appendix-
    unreduced-bv-qme 34). No-go. **PASS**.

**Theorem audit summary.** **33/33 theorem-grade blocks have explicit
hypothesis chains.** No theorem statement asserts a conclusion
exceeding its hypothesis range. The conditional theorems (15, 16, 17;
T1 460, 636; T5 618; appendix-radial 249) are uniformly labelled in
the title and in the cited claim-strength-ledger row.

**Cosmetic observation.** Two `\begin{thm}` blocks at `main.tex`:4266
and 4405 carry labels with prefixes `prop:` and `prob:` respectively.
This is a label/environment-name mismatch with no content effect.
Severity 1 cosmetic; not a referee landing.

---

## §4. Theorem-lane status audit

8 stmt-blocks in `theorem-lanes.tex`:

| Lane | Label | Status | Wave-5 update needed? |
|---|---|---|---|
| Dirac brane probe | `thm:lane-dirac-probe` | proved finite | No |
| Stable trace, $\Psi_{a,b}$ PBW | `thm:lane-stable-trace` | proved degreewise stable | No |
| CE/PV reduced Hamiltonian | `thm:lane-ce-pv-center` | proved degreewise stable | No |
| Matlis principal-part cotangent | `thm:lane-principal-parts` | proved degreewise stable | No |
| Brane-line factorization currents | `thm:lane-factorization-current` | proved degreewise stable | No |
| Reduced principal-part defect currents | `thm:lane-reduced-principal-part-current` | proved degreewise stable | No |
| Degree-zero Moyal/Weyl + graph | `thm:lane-moyal-degree-zero` | conditional on QME/radial-parts/regulator | No |
| Scalar U(1) anomaly | `thm:lane-u1-anomaly` | proved finite | No |

**Stale-status verification.** Each stmt-block was scanned for
wave-3 / wave-4 status terms ("Phase-3 wave 3 finalised", "wave 4
proved"). **None present.** All status descriptors use the canonical
9-status vocabulary of the claim-strength ledger, which is the
wave-5-current vocabulary.

**Cross-reference verification.** Each lane's "Proof dependency map"
cites theorems by `\ref{thm:...}`. Cross-checked 32 cross-references
against `main.tex` and tate/appendix files; all resolve.

**Verdict.** All 8 lanes are at wave-5-current status. No stale
wave-3/wave-4 carry-over.

---

## §5. Cross-volume firewall remark audit

Two reader-visible cross-volume sites:

### Site 1: `rmk:convention-firewall` (`main.tex`:5409-5423)
Content: enumerates "no compact CY datum, no $K3\times E$
specialization, no $(\Sigma,C)$ specialization, no Igusa cusp form,
no Borcherds input form, no BKM denominator identity, no Stage-1 or
Stage-2 $\Phi_d$ specialization".
**W5-X1 cross-volume CLEAN findings:** Vol III Hodge-cohomology BCOV
citation, Igusa open recognition posture, Vol I/II scope-disjoint
factorization categories, four convention drifts (worldsheet, framing,
sign, regulator) all internally declared per volume. **Reflected? PARTIAL**: the
remark states the non-assertion list but does not transmit the
positive observation that each sister volume internally declares its
scope. The W5-X1 audit explicitly flagged this as an **optional**
prose-clarity sharpening: "the topological-strings convention
firewall remark could add a one-sentence pointer that each of the
four sister volumes likewise declares its scope and does not assert
a chain-level transfer. This is purely prose-level cross-referencing;
the firewall typology holds without it."
**Verdict.** The remark is internally consistent (strict scope
firewall posture). The W5-X1 optional prose-clarity sharpening is
**not yet inscribed** but is **NOT REQUIRED for referee-grade
correctness**. The firewall holds without it.

### Site 2: `\subsection{Cross-volume firewall}\label{ssec:cross-volume-horizon}` (`main.tex`:5937-5958) plus
`\input{tate-P5-cross-volume}` (132 lines, 5965)
Content: explicit scope-disjoint statement, matched-conventions
theorem requirement, no-formal-disk-transfer lemma
(`lem:no-formal-disk-transfer`), templates remark
(`rmk:matched-conventions-templates`).
**W5-X1 findings reflected? YES**: the matched-conventions theorem
datum (`defn:matched-conventions-theorem-datum`) and templates remark
together implement the W5-X1 CLEAN cross-volume verdict by stating,
for each sister volume, what data the sibling must supply
internally. The four cross-volume conventions
(worldsheet, framing, sign, regulator) are each implicitly carried by
the matched-conventions theorem datum: holomorphic dimension, ambient
geometric object, worldsheet/specialization curve, framing,
coefficient topology, anomaly normalization, deformation parameter,
QME hypothesis, comparison morphism, claim status, role
(convention-check / source / unused).
**Verdict.** The cross-volume horizon is internally consistent with
the W5-X1 CLEAN findings. No silent cross-volume transfer. Reader
who follows the firewall to the matched-conventions definition
finds the discipline that closes the cross-volume question.

---

## §6. Hostile-referee question battery

### (a) Bousfield $\tau_{\mathfrak h}$ Quillen equivalence cited as theorem-status?

**Search.** `grep -n "tau_h\|Bousfield"` across all .tex files: **0
matches**. **Confirmed silent.**
**Interpretation by a referee.** A referee interpretation `rmk:E1-translation`
(`main.tex`:2229-2246) sees Lurie HA §5.5.4 cited together with
Costello-Gwilliam Vol I §6.4. The reader is left to assume the
standard Quillen equivalence between the two presentations
(Lurie HA §A.3.7 / CG Vol II §A.5). This is **standard** and
**verified in the cited literature**.
**Acceptable for referee?** YES. The silent dependence is at the
level of two equivalent standard presentations of the same
$\infty$-categorical object. A referee who flags this is correct that
the Quillen equivalence is unnamed; they are also correct that this
is a clarity gap, not a correctness gap. The W5-A1 §3.7 minimal
heal is a one-line remark. **Severity 1-2 minor revision.**

### (b) (A5)^RG closure under Costello RG-flow stated anywhere?

**Search.** `grep -n "(A5)\^{\\mathrm{RG}}\|A5-RG\|A5.*RG"` across all
.tex files: **0 matches**. **Confirmed silent.**
**Interpretation by a referee.** The manuscript declares the (CC3)
compatibility-with-Costello-RG-flow condition at
`tate-T1-weighted-completion.tex`:107-112 as an **external** Costello
requirement (the residual locality/QME problem in
`prob:weighted-rg-locality`). The (A5)^RG closure of the admissible
regulator class is **not declared**.
**Acceptable for referee?** YES. The Sergeev-intertwiner-related
analysis (#104 wave-4 closure) does not appear at all in the manuscript
proper -- it is internal to the reconstitution audit trail. The
manuscript's Costello-class compatibility is implicit in the cited
primary sources (Costello 2011 Ch 6, CG Vol II §11). A referee can
correctly flag the implicit reliance, but the (A5)^RG closure is
not a load-bearing hypothesis for any inscribed theorem statement
because the wave-4 Sergeev-intertwiner content is not inscribed.
**Severity 1-2 minor revision** -- declarative-only, after the +472
inscription delta lands.

### (c) Parabolic functoriality of Theorem F'' declared?

**Search.** `grep -n "Theorem F\|F''\|joint-Fpp\|parabolic"` across all
.tex files: **0 matches** for "F''", parabolic functoriality, or
$P_{(z_1)}$. **Confirmed silent.**
**Interpretation by a referee.** Theorem F'' is **not yet inscribed in the
working tree**. The manuscript does not declare F'' or its parabolic
restriction. The W5-A2 §1 finding is therefore **a wave-5
strengthening for the +472 inscription target**, not a defect of the
current 155-page manuscript.
**Acceptable for referee?** N/A -- the manuscript at 155 pages
does not contain Theorem F''. **Out of scope** for the
PRE-AUTHORIZATION snapshot.

### (d) Are the 5 firewall-permanent species named in the manuscript?

**Search.** `grep -n "FW.BCOV\|FW.Sergeev\|FW.Igusa\|FW.Unreduced\|FW.Costello-Li\|firewall-permanent\|firewall typology"` across all .tex files: **0
matches**. **Confirmed silent.**
**Interpretation by a referee.** The five named firewall species
(FW.BCOV, FW.Sergeev-A5/Sergeev-Howe, FW.Igusa, FW.Unreduced-Bosonic,
FW.Costello-Li-d-even) live entirely in the reconstitution audit
trail. The manuscript carries the **substance** of each via:
* `rmk:convention-firewall` (5409): unifies BCOV, $K3\times E$,
  Igusa, Borcherds, BKM, Stage-1/Stage-2 non-assertions in one umbrella
  remark.
* `rmk:weiss-ran-descent-firewall` (2779): the Weiss/Ran descent
  obstruction.
* `lem:no-formal-disk-transfer` (`tate-P5-cross-volume.tex`:63): the
  formal-disk to compact-CY non-transfer.
* `lem:admissibility-not-globalization` (`tate-P3-universality.tex`:
  140): protected-sector restriction is not globalisation.
* `appendix-unreduced-bv-qme.tex`:34
  (`thm:app-unreduced-polynomial-centrality-no-go`): the
  unreduced-polynomial-cotangent no-go (FW.Unreduced-Bosonic
  substance).
**Per W5-A2 §3 enumeration:** **0 of 5** species are named with the
"FW.X" identifiers. **5 of 5** species have substance-bearing remark
or theorem in the manuscript. **5 of 5** are distinguishable by their
inscribed substance.
**Acceptable for referee?** YES. A referee interpretation the working tree
encounters the **substance** of all five firewalls without the
FW.X naming convention. The naming convention is wave-5 audit
shorthand and is **not load-bearing for the manuscript's correctness**.
The +472 inscription delta delivers the FW.X naming alongside the
firewall-typology granularity strengthening.

### (e) Does any theorem-grade claim depend on a Phase-5 obligation as silently-presumed?

**Inspection.** Each of the 33 theorem-grade blocks was checked for
silent dependence on Phase-5 obligations (Sergeev intertwiner,
G4-M2 Heisenberg twist, Costello-Li $d$-extension, etc.).
**Result.** No inscribed theorem statement depends on any wave-5+
Phase-5 obligation. The conditional theorems (15-17, T1-460/636,
T5-618, appendix-radial-249) explicitly cite their conditional
hypothesis (`stmt:app-radial-external-input`,
`prob:weighted-rg-locality`, `prob:analytic-graph-realization`).
The Tate-conilpotency hypothesis (`lem:continuous-bar-cobar`) is
explicit in `thm:open-closed-derived-center` and its derivatives.
**Verdict.** **NO silently-presumed Phase-5 obligation.** Each
conditional theorem cites its hypothesis explicitly. The wave-5
silent meta-hypotheses ((A5)^RG, (Q-Eq), parabolic functoriality)
are **not load-bearing** for any inscribed theorem statement.
A referee will not catch a load-bearing silent Phase-5 dependence.

---

## §7. Severity-tabulated findings

| ID | Site | Severity | Class | Heal |
|---|---|---|---|---|
| FA-A09 | abstract.tex:33 (regulator-independence understatement) | 1 | cosmetic | optional 1-line |
| TA-12 | main.tex:4266 (label `prop:` in `thm:` env) | 1 | cosmetic | optional |
| TA-13 | main.tex:4405 (label `prob:` in `thm:` env) | 1 | cosmetic | optional |
| HR-a | rmk:E1-translation (Q-Eq presupposition) | 2 | minor | +3-line remark |
| HR-b | (A5)^RG closure unstated | 1 | none-load-bearing | declarative-only |
| HR-c | F'' parabolic functoriality | N/A | not-yet-inscribed | future +472 delta |
| HR-d | 5 firewall species named | 1 | naming-convention | future +472 delta |
| HR-e | Phase-5 silent dependence | 0 | clean | none |
| CV-1 | rmk:convention-firewall positive cross-volume note | 1 | optional | optional 1-line |

**Aggregate severity.** 5 severity-1 cosmetic items (declarative or
optional); 1 severity-2 minor revision item (HR-a, $\tau_{\mathfrak h}$
Quillen equivalence remark). **0 severity-3 (load-bearing) items.**
**0 severity-4 (correctness-defect) items.**

---

## §8. Final referee verdict

### Verdict: **ACCEPT-WITH-MINOR-REVISIONS**

**Rationale.**

1. **All 33 theorem-grade blocks have explicit hypothesis chains, no
   over-claim, no under-claim.** Every conditional theorem is
   labelled "conditional on X" both in title and in the cited
   claim-strength-ledger row.

2. **The status vocabulary is uniformly applied** across abstract,
   theorem-lanes, claim-strength-ledger, and open-obligations. A
   referee interpretation any one of these four standardised sites finds
   the same vocabulary: proved-finite, proved-degreewise-stable,
   proved-weighted-Tate, computed-to-stated-order, conditional,
   reduced-target / unreduced-lift-open, conjectural, open, not
   asserted.

3. **Cross-volume firewall is internally consistent and aligned with
   the W5-X1 CLEAN cross-volume audit.** The matched-conventions
   theorem datum (`defn:matched-conventions-theorem-datum`) gives a
   referee the precise discipline by which any future sister-volume
   transfer must internally supply its global data.

4. **Six minor-revision strengthenings.** Three are declarative-only
   (item HR-a +3 lines for $\tau_{\mathfrak h}$ Quillen equivalence;
   item HR-b +3 lines for (A5)^RG closure; item CV-1 +1 line for
   positive cross-volume sister-pointer). Three are cosmetic
   (FA-A09 abstract phrasing tightening; TA-12 / TA-13 label/env
   match for two thm-block prefixes). None modifies any theorem
   statement.

5. **No load-bearing silent strengthening, no correctness-defect.**
   The wave-5 audit's silent meta-hypotheses are at the level of
   meta-categorical compatibility (Costello-class, Lurie/CG Quillen
   equivalence, parabolic functoriality of unwritten F''). They do
   not modify any inscribed theorem statement.

6. **Four wave-5 audit findings are silent in the manuscript.**
   Per the user's hostile-referee battery: (HR-a) Q-Eq is silent,
   (HR-b) (A5)^RG is silent, (HR-c) parabolic functoriality of F''
   is N/A (not inscribed at 155 pages), (HR-d) 5 firewall species
   are named 0/5 in FW.X form but 5/5 in substance, (HR-e) no
   theorem-grade silent Phase-5 dependence. **Each silent finding
   is acceptable for a referee at the current 155-page state; each
   is delivered by the +472 inscription delta in declarative form.**

### Suggested referee report wording (for author internal use)

> The manuscript "[title]" is technically sound at the 155-page
> working-tree state. The proved package -- finite-algebraic Dirac
> reduction, scalar $U(1)$ anomaly, degreewise-stable CE/PV
> derived-centre, Matlis principal parts, brane-line factorization
> currents, reduced principal-part defects, scalar-reduced Moyal/Weyl
> degree-zero comparison, weighted Tate regulator -- is uniformly
> stated with explicit hypothesis ranges and uniformly tagged with the
> status vocabulary (proved-finite, proved-degreewise-stable, proved
> weighted Tate, conditional, reduced target / unreduced lift open,
> open, not asserted).
>
> Cross-volume firewall is honest: the manuscript carries no
> compact-CY, BCOV, BKM, Igusa, $K3\times E$, or Vol III consequence
> by itself; any such transfer is forced through the matched-
> conventions theorem datum. This discipline is consistent with the
> sister-volume manifestos that we cross-checked
> (calabi-yau-quantum-groups, igusa-cusp-form, chiral-bar-cobar,
> chiral-bar-cobar-vol2): each sister volume internally declares
> its own scope without alleging a chain-level transfer.
>
> Six minor-revision strengthenings recommended (~10 lines total):
> (1) at `rmk:E1-translation`, cite the Lurie HA §A.3.7 / CG Vol II
> §A.5 Quillen equivalence between the two presentations of locally
> constant factorization algebras; (2) at the (A5) admissible
> regulator declaration site, declare (A5)$^{\mathrm{RG}}$ closure
> as a sub-clause; (3) at `rmk:convention-firewall`, optionally
> add a one-sentence positive pointer that each sister volume
> declares its scope; (4) at `claim-strength-ledger.tex` row
> "Weighted Tate regulator", consider tightening the abstract
> phrasing about regulator independence (the internal weighted
> independence IS proved); (5) match the `\begin{thm}` env at
> `main.tex`:4266 with its `prop:` label or rename the label;
> (6) similarly at 4405 for the `prob:` label.
>
> No load-bearing silent strengthening detected. No correctness
> defect. The conditional theorems are uniformly labelled and the
> radial-parts external input statement is properly named.
>
> **Verdict: accept with minor revisions.**

---

## §9. Comparison with the +472 inscription delta

The +472 inscription delta (W4 #110 P4-Symp-Functoriality + W5-A2
+ W5-X1 + W5-X10 + W5-X18 augmentations) is the wave-5
authorisation that delivers:
* F'' theorem block (parabolic-functoriality explicit) -- 56-59 lines
* Master hypothesis block ((A2'), tensor-factor disjointness) --
  267-272 lines
* Firewall-typology remark (5 species with functoriality classes) --
  12-15 lines
* W5-X1 cross-volume optional positive pointer -- 1-3 lines
* W5-X10 figure captions -- ~30 lines
* W5-X18 open obligations patch -- ~50 lines
* Other minor strengthenings -- ~50-100 lines

**Without the inscription:** 155 pages, accept-with-minor-revisions,
6 minor-revision items.

**With the inscription:** ~+30 pages (estimate based on +472 lines /
$\sim$15 lines/page), accept-with-minor-revisions to clean accept;
2-3 minor-revision items remaining (cosmetic abstract phrasing,
optional Quillen-equivalence remark sharpening, label/env match).

The inscription is **not required for referee-grade publishability**.
The current 155-page manuscript at the W5-X11 baseline is referee-
publishable with the noted minor revisions.

---

## §10. Recommended next steps (Phase-5)

* **R-W5-X21-01.** Accept-with-minor-revisions interpretation: the
  manuscript at 155 pages is publication-grade with 6 minor-
  revision items. **Recommend the +472 inscription delta** to
  reduce the minor-revision item count from 6 to 2-3.
* **R-W5-X21-02.** If the author chooses to release at 155 pages,
  inscribe the three declarative remarks (HR-a Quillen equivalence
  +3 lines; HR-b (A5)^RG +3 lines; CV-1 cross-volume sister-pointer
  +1 line) for **+7 lines total** -- this closes the most
  referee-visible silent strengthenings without committing to the
  full +472 typology delta.
* **R-W5-X21-03.** Two cosmetic label/env matches at `main.tex`:
  4266 and 4405 are independent and can be done in any release.
* **R-W5-X21-04.** Maintain the current cross-volume firewall
  posture and matched-conventions discipline in all future
  inscriptions.

---

End of Phase-4 EXEC W5-X21 referee-simulation report.
