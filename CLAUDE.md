# CLAUDE.md — mixed holomorphic-topological strings

## What this manuscript proves

The **formal-Darboux stalk theorem of the Mixed Holomorphic-Topological Deligne conjecture** at $N$ Dirac branes:
\[
A^{\mathrm{cl}}_{\partial, N} = C^\bullet_{\mathrm{CE}}\bigl(\mathfrak{gl}_N,\; \mathrm{Kosz}([\phi_1, \phi_2])\bigr),\qquad
J(f) = \mathrm{Tr}\,f(\phi_1, \phi_2),\qquad
c_f \mapsto \theta_f,\quad u_f \mapsto J(f).
\]
The trace map $J$ is the formal Darboux coordinate expression of the chiral Hochschild cohomology $C^\bullet_{\mathrm{ch}}(A_b, A_b)$, the derived chiral centre at the brane vacuum. The Capelli scalar $\hbar N[\bar c]$ is the projective curvature $\Omega_{\mathrm{central}}$ at the trace generator. The four-curvature taxonomy classifies global obstructions.

The constellation-level master theorem, of which this manuscript is the formal-Darboux stalk:

> Closed sector $= Z^{\mathrm{der}}_{E_d^{\mathrm{ch}}}(\mathcal{C}^{\mathrm{op}}_\partial)$. Modular structure $=$ trace plus clutching. Quantum and global obstructions $=$ curvature in $\mathfrak{K}_T$. Scalar invariants $=$ sections of the modular line bundle on the period domain.

This is the Deligne conjecture in its mixed holomorphic-topological chiral $E_d$ realization.

---

## The voice and the writing standards

The canonical, authoritative writing standards live in
\`MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md\` at the root of this repository. **Read at session start. It binds.**

Voice register: **Witten, Etingof, Polyakov, Dirac, Feynman, Costello, Gaiotto.** Russian research school discipline. Every statement either mathematics or physics. Nothing else survives.

A sentence that does not state mathematics or physics is a defect.

---

## The constellation

| repository | role |
|---|---|
| `~/mixed-holomorphic-topological-strings/` | this manuscript — formal-Darboux stalk |
| `~/chiral-bar-cobar/` (Vol I) | $d = 1$ chiral Koszul; bar / cobar / centre distinction |
| `~/chiral-bar-cobar-vol2/` (Vol II) | $d = 1$ algebraic 3d-gravity HT sector at $A = \mathrm{Vir}_c$ |
| `~/chiral-bar-cobar-vol4/` (Vol IV) | architectural inheritance |
| `~/calabi-yau-quantum-groups/` (Vol III) | $d \geq 2$; two-stage CY-to-chiral; Hall–Drinfeld |
| `~/igusa-cusp-form/` | level-2 modular section of $\Omega_{\mathrm{central}}$ on $K3 \times E$ |
| `~/ecosystem/` | discipline layer; `INVARIANTS.md` binds |

Cross-volume firewall: convention divergence is load-bearing — flag, do not silently reconcile. Every shared symbol matches across volumes; every shared concept has the same definition.

---

## Two principles, seventeen sites

**P1.** Primitive $\neq$ chart.
**P2.** Shadow $\neq$ object.

Seventeen sites where these have been violated; each carries a corrected form.

| # | failed claim | corrected form |
|---|---|---|
| 1 | $A$ is the primitive open object | $\mathcal{C}^{\mathrm{op}}_\partial$ primitive; $A_b = \mathrm{End}(b)$ for chosen $b$ |
| 2 | $\mathrm{Bar}(A) = $ bulk | $\mathrm{Bar}(A) = $ twisting coalgebra; $Z^{\mathrm{der}}_{\mathrm{ch}}(A) \simeq C^\bullet_{\mathrm{ch}}(A, A) = $ bulk |
| 3 | 2d chiral $\Rightarrow $ 3d HT via $E_1$-bar | chiral Deligne–Tamarkin: $A \rightsquigarrow Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ one-up |
| 4 | open sector on bare curve $X$ | open sector on $\partial X^{\mathrm{KN}}$ for Kato–Nakayama log $(X, D, \tau)$ |
| 5 | modularity is property of closed algebra | trace + clutching on the open category |
| 6 | five $\kappa$-numbers $(0, 0, 3, 5, 24)$ are one invariant | five distinct construction layers; spectral-sequence interpretation conjectural |
| 7 | $\mathrm{CY}_d\text{-Cat} \to \mathrm{ChirAlg}$ direct | $\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$ |
| 8 | $Y^+(X) = \mathcal{G}(X)$ | $\mathcal{G}(X) = D(Y^+(X))$ after Hall pairing / completion / integral form / stable-envelope transport / descent |
| 9 | 6d hCS = 3d CS in disguise | 6d hCS realizes $\Phi^{\mathrm{FA}}_3$ on verified loci; one-loop $\int_X \mathrm{Tr}^{\mathrm{ad}}(A(F_A)^3)$ quartic |
| 10 | formal local HT $\Rightarrow $ global compact theory | formal-Darboux + descent + QME + anomaly + locality $\Rightarrow $ candidate |
| 11 | $\Delta_5 = $ compact BPS Hilbert space | $\Delta_5 = $ Borcherds denominator / scalar shadow; operator lift open |
| 12 | scalar $Z_{\mathrm{BPS}} = $ operator algebra | scalar $= $ protected trace of still-to-be-constructed operator package |
| 13 | algebraic holography $= $ 3d gravity construction | identification of HT sector; not construction of dynamical-metric path integral |
| 14 | $W_\infty[\lambda] \Rightarrow E_\infty$ from finite-spin checks | conditional on Prochazka, Creutzig–Kanade–Linshaw, Pope–Romans–Shen/Bakas, Yamada |
| 15 | class M chain-level in ordinary complexes | completed ambient: HS-sewing / coderived BV $= $ bar / weight-completed / pro / $J$-adic |
| 16 | PVA Jacobi $\Rightarrow $ all-loop quantum | classical only; finite-jet PVA all-loop conditional on KZ analytic SDR + Stokes + reflected weights + $T = [Q_{\mathrm{tot}}, G]$ |
| 17 | quadratic chiral duality $\Rightarrow $ Koszul theorem | quadratic dual + MC injection only; chiral Koszul homotopy theorem separate |

When any pattern appears in a draft: replace with the corrected form.

---

## The master architecture

```
                Stage 1 (CY)             Stage 2 (chiral)         Stage 3 (Hall double)
            ┌──────────────┐         ┌────────────────┐         ┌──────────┐
CY_d-Cat ─Φ^FA→│ E_d-HolFA(X) │─∫_Σ───→│ ChirAlg(C)     │──Hall──→│ D(Y^+(X))│
            └──────┬───────┘         └────────┬───────┘         └──────────┘
                   │                          │
                   │ boundary value           │ chosen vacuum b
                   │ on ∂X^KN (Kato–Nakayama) │
                   ▼                          ▼
              ┌───────────┐               ┌──────┐
              │ C^op_∂    │── chart b ──→ │ A_b  │
              └─────┬─────┘               └───┬──┘
                    │                         │
                    │ derived E_d-centre      │ chiral Hochschild
                    └─────────────────────────┘
                                │
                                ▼
              Z^der_{E_d^ch}(C^op_∂) ≃ C^•_ch(A_b, A_b)
                                │
                                ▼
                    modular line bundle
                       = Ω_central
                                │
                                ▼
                  Δ_5 (level-2 modular section
                       on K3 × E)
```

Every constellation volume populates one node. **This manuscript proves the formal-Darboux stalk of $C^\bullet_{\mathrm{ch}}(A_b, A_b)$ at the Dirac brane node.**

---

## The platonic chapter sequence

Eleven chapters; each forced by the previous; each section either constructs the local centre, identifies an obstruction, or computes an example.

1. **The setup.** $\mathbb{R}^2_{\mathrm{top}} \times \mathbb{C}^2_{\mathrm{hol}}$ with brane stacks at holomorphic-symplectic points; the Mixed HT Deligne conjecture; the local stalk question.
2. **The shifted-cotangent BF Lie algebra.** $\mathfrak{h} = \mathbb{C}[[z_1, z_2]] / \mathbb{C}$, $\mathfrak{g} = \mathfrak{h} \ltimes \mathfrak{h}^\vee_{\mathrm{cont}}[1]$; Hamiltonian BF action.
3. **The derived commuting variety stack at $N$ Dirac branes.** $[\mu^{-1}_{\mathrm{der}}(0) / \mathrm{GL}_N]$, $Q\psi = [\phi_1, \phi_2]$.
4. **Boundary algebra and trace map.** $A^{\mathrm{cl}}_{\partial, N}$, $J(f) = \mathrm{Tr}\,f(\phi_1, \phi_2)$.
5. **CE/PV dictionary as Koszul resolution.** $c_f \mapsto \theta_f$, $u_f \mapsto J(f)$ identifies the formal coordinate of $C^\bullet_{\mathrm{ch}}(A_b, A_b)$.
6. **The Capelli scalar.** $\hbar N[\bar c] = \Omega_{\mathrm{central}}|_{J(f)}$, projective curvature, determinant line.
7. **The obstruction calculus.** $\mathfrak{K}_T$, $\Theta_T$, $F_T$, four-curvature taxonomy $\{0,\, d_\Theta\tau,\, \Omega_{\mathrm{central}},\, \notin \mathrm{im}\,d_\Theta\}$. Six named obstructions as coordinates of one curvature.
8. **The pro-Matlis target.** $N$-tower categorical home; Matlis duality at finite presentation.
9. **Examples.** Heisenberg, $\hat{\mathfrak{g}}_k$, $\beta\gamma$, $\mathrm{Vir}_c$ (algebraic HT holographic reading; identification, not construction), $W_N$, $\mathbb{C}^3$, $K3$, $K3 \times E$, generic compact CY3.
10. **The $W_\infty[\lambda] / E_\infty$ admissible endpoint.** Conditional theorem; Prochazka triangular truncation, Creutzig–Kanade–Linshaw parafermion compatibility, Pope–Romans–Shen/Bakas, Yamada weight-window.
11. **The frontier.** MNOP / framing on $S^3$; Hall–Drinfeld–Borcherds compact-CY3 comparison; gravitational lift of $\Phi_{10}$. Three open problems: chiral $E_d$ Deligne at $d \geq 2$; Hall–Drinfeld–Borcherds spectral sequence on compact non-toric CY3; operator-level lift of the modular line.

The opening sentence (Chapter 1):

> *Mixed holomorphic-topological string theory on $\mathbb{R}^2_{\mathrm{top}} \times \mathbb{C}^2_{\mathrm{hol}}$ has, at each formal holomorphic-symplectic brane point, a closed sector that coincides with the chiral Hochschild cohomology of the boundary algebra; this manuscript computes the formal-Darboux coordinate expression of that coincidence at $N$ Dirac branes.*

The closing sentence (Chapter 11):

> *The trace map $J(f) = \mathrm{Tr}\,f(\phi_1, \phi_2)$ is the formal coordinate of the universal closed–open identification at one Dirac brane vacuum; the global identification, the operator-level lift of the modular line, and the chiral $E_d$ Deligne theorem at $d \geq 2$ are the open problems the formal-Darboux stalk has now made well-posed.*

---

## Convention layer (binding)

- $d = \dim_{\mathbb{C}} X$ for target complex dimension.
- Local geometry is $\mathbb{R}^2_{\mathrm{top}} \times \mathbb{C}^2_{\mathrm{hol}}$ at a brane. The only Calabi-Yau datum is the trivial holomorphic volume / symplectic on $\mathbb{C}^2$, used for BV pairing, divergence-free Hamiltonian fields, cyclic trace densities. **Not** a compact CY$_3$ assumption; **not** a BCOV theorem; **not** a license to import quintic / OSV / GV / MNOP / Abel–Jacobi / CoHA / Igusa / BKM into the core local theorem surface.
- Native object: holomorphic $E_2$ / factorization algebra on $\mathbb{C}^2$,
\[
\Omega^{0, \bullet}_c(B) \,\widehat{\otimes}\, \mathfrak{g},\qquad
\mathfrak{g} = \mathfrak{h} \ltimes \mathfrak{h}^\vee_{\mathrm{cont}}[1],\qquad
\mathfrak{h} = \mathbb{C}[[z_1, z_2]] / \mathbb{C}.
\]
Curve vertex algebra / Zhu algebra / Vol II $\mathbb{C} \times \mathbb{R}$ chiral-topological theorems enter only after a controlled reduction with explicit $z_2$-mode or principal-part data, pushed-forward bracket, BV pairing, brane image, anomaly matching.
- Worldsheet $\Sigma$ — complex curve, possibly with boundary or marked points.
- Framing on $S^3$ stated when invoked; deviation flagged.
- BV degree, ghost number, form degree tracked separately. Koszul sign and Gerstenhaber bracket signs fixed in `appendix-sign-conventions.tex`.
- Propagator weight in heat-kernel renormalization explicit.
- $\hbar$ versus $g_s$: distinguish — $\hbar$ for QFT loops, $g_s$ for string genus expansion.
- Holomorphic anomaly sign: BCOV-strict per `appendix-sign-conventions.tex`.
- Negative-cyclic / cyclic / Hochschild homology distinguished.
- $\mathcal{C}^{\mathrm{op}}_\partial = \Phi^{\mathrm{FA}}_d(\mathcal{A})\big|_{\partial X^{\mathrm{KN}}}$ on the Kato–Nakayama log boundary.
- $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}(\mathcal{F}) = \int_{\Sigma_{d-1}} \mathcal{F}\big|_C$ — Lurie–Ayala–Francis factorization homology.
- "Dirac brane stack" $= [\mu^{-1}_{\mathrm{der}}(0) / \mathrm{GL}_N]$ — derived commuting variety stack; the brane reading is the physical realization.
- Capelli scalar $\hbar N[\bar c] = \Omega_{\mathrm{central}}|_{J(f)}$ — the Capelli identification IS the projective curvature evaluation at the trace generator.
- Modular line bundle on $\overline{\mathcal{A}}_g = \Omega_{\mathrm{central}}$ at level $g$. Igusa cusp form $\Phi_{10}$ is its level-2 section; $\Delta_5 = \Phi_{10}^{1/2}$.
- CE/PV dictionary $c_f \mapsto \theta_f$, $u_f \mapsto J(f)$ is the Koszul resolution of $C^\bullet_{\mathrm{ch}}(A_b, A_b)$.

## Theorem-control predicates (binding)

- Native $\mathbb{C}^2$ holomorphic $E_2$ taxonomy retained before any curve-chiral reduction.
- BMK lane: one-pair analytic pro-Matlis retract is **not** strict native all-window support-local current transfer; obstruction $\mathrm{Ob}^\Pi_{\mathrm{BM}}$.
- Larger non-scalar $\theta_3$ row is evidence only with: a CE ancestor, or a scalar-zero Costello local counterterm, or a complete companion-face table; tower compatibility through $\Delta^1_{M, N} = -\pi_{M, N}\mathfrak{b}^M + \mathfrak{b}^N$ plus the secondary $\varprojlim^1 H^0$ primitive class.
- Radial / Weyl theorem surface is $\Omega^{\mathrm{rad}}_{a, b}$, equivalently decorated PBW Stokes for $D^\square_{a, b} = C^+_{a, b} \partial_2$, with failure exactly a signed row in $\ker B^*_{a, b}$.
- Larger non-scalar Costello / QME theorem requires: filtered scalar projection, finite row arrays, primitive matrix $A^M c = -r^M$, transition matrices, Roos compatibility, centrality homotopies, curved bulk-to-defect kernel.
- Brane-preserving $\Omega$-background: normal scaling on $N_L X = \mathbb{R}_s \oplus \mathbb{C}_{z_1} \oplus \mathbb{C}_{z_2}$ with $t$ fixed; $T_\Omega = \mathbb{C}^*_{\varepsilon_s} \times \mathbb{C}^*_{\varepsilon_1} \times \mathbb{C}^*_{\varepsilon_2}$. Literal $(t, s)$-rotation does not preserve the brane line; not native unless a different fixed-locus problem is defined. Theorem surface includes $Q_\Omega = Q + \iota_{V_\Omega}$, $Q_\Omega^2 = L_{V_\Omega}$, inverted normal weights, residue-vs-Euler normalization, stratified factorization data.

---

## The chriss-ginzburg-rectify discipline

For manuscript-proper writing, rewriting, theorem-lane reconstitution: load `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md` before editing.

Five phases:

1. **Global diagnostic** (read-only). Map narrative thread, motivation gaps, define-before-use violations, opening / closing, physical insight calibration, prose, formula red flags.
2. **Platonic restructuring.** Compute layer survey, six platonic-ideal questions, reorder / merge / split / move / delete redundancies / add stubs, structural convergence iteration.
3. **Linear reconstitution loop.** Chunks of 50–100 lines. Six gates simultaneously:
   - **Gate 0** — principle consultation: writing standards, `INVARIANTS.md`, sister catalogues, seventeen-site catalogue.
   - **Gate 1** — mathematical truth: falsification from first principles; every formula recomputed; every proof step checked; every scope qualified; every convention verified.
   - **Gate 2** — define-before-use.
   - **Gate 3** — voice (§V scan).
   - **Gate 4** — motivate-before-introduce.
   - **Gate 5** — chriss-ginzburg architecture: every section answers one question, in service of the climax.
4. **Adversarial re-audit.** Three independent agents (RED / BLUE / GREEN); if any actionable issue: re-enter Phase 3 on affected chunks.
5. **Final convergence.** Build, test, report.

Stop only at convergence or when the exact remaining obstruction is named.

---

## Operational integration

### Build

```bash
cd ~/mixed-holomorphic-topological-strings
make fast        # iterative builds during rectification
make release     # full release; PDFs copied to iCloud
```

Stale processes: `pkill -9 -f pdflatex 2>/dev/null; sleep 2`. Do not rebuild after every edit; build at session end or when verification requires it.

### Compute layer

`scripts/`:
- `check_moyal_coefficients.py` — Moyal star-product coefficients
- `check_one_psi_homology.py` — single-$\psi$ homology bidegree range
- additional sign-rule and homology checks

Lead with content that has compute backing. Flag content with no compute verification. Use compute test names as anchors for the chapter's load-bearing theorems.

### Source layout

- `main.tex` — root.
- `abstract.tex`, `preamble.tex`, `authors.tex`, `commands.tex`, `mathmacros.tex`, `notation.tex`, `nomenclature.tex` — bound parts.
- `appendix-sign-conventions.tex`, `appendix-master-deformation-complex.tex`, `appendix-algorithms.tex`, `appendix-matlis-principal-parts.tex`, `appendix-full-psi-homology.tex`, `appendix-radial-parts-moyal.tex`, `appendix-factorization-current-conventions.tex`, `appendix-unreduced-bv-qme.tex` — appendices.
- `tate-T2-nilpotent-truncation.tex`, `tate-T4-bv-vanishing.tex`, `tate-T5-chain-level-primitive.tex`, `tate-P3-universality.tex` — theorem files.
- `frontier_mnop_framing_volume.tex` — frontier volume.
- `Makefile`, `firstorder.{png,svg}`, `thirdordera.{png,svg}`, `thirdorderb.{png,svg}` — build apparatus and diagrams.
- `scripts/` — computations.

### Memory references

- `~/.claude/projects/-Users-raeez-topological-strings/memory/MEMORY.md` — index.
- `reference_writing_standards.md` — pointer to canonical standards file.
- `feedback_voice.md`, `feedback_writing_discipline.md` — conversation-level distillation.

The canonical writing standards file is the authoritative source.

### Sister catalogues

- `~/calabi-yau-quantum-groups/notes/antipatterns_catalogue.md`, `appendices/first_principles_cache.md`.
- `~/chiral-bar-cobar/notes/antipatterns_catalogue.md`.
- Append a new pattern to `~/mixed-holomorphic-topological-strings/notes/first_principles_cache.md` when a confusion recurs $\geq 2$ times in a session (create the file and `notes/` directory if absent).

---

## Forbidden patterns (catalogue with replacements)

§V of the writing standards is authoritative. Common offenders to delete on sight:

| pattern | replacement |
|---|---|
| matrix microscope, brane microscope, matrix probe | trace measurement, Dirac brane formal-stalk chart |
| platonic ideal (in body prose) | state the structure directly |
| Theorem A / B / C labels in prose | refer by formula or theorem number |
| Wave $N$ / Phase $j$ / round $M$ / session $k$ | delete; state the mathematical content |
| we now turn to, having established, this section sharpens | state next mathematical content directly |
| is closely related to, corresponds to, is the analogue of (when exact) | $=$ or $\simeq$ with the morphism named |
| is wrong, would be, must not, fails to | positive construction; name objects + map |
| certificate, manifest, spec, schema | rational reduction, table, or field-standard term |
| we hope, perhaps, remarkably, crucially, notably | state the result |
| $A$ is the primitive open algebra | $\mathcal{C}^{\mathrm{op}}_\partial$ on $(X, D, \tau)$; chart $b$ gives $A_b = \mathrm{End}(b)$ |
| $\mathrm{Bar}(A)$ is the bulk | $\mathrm{Bar}(A)$ classifies twisting; bulk is $Z^{\mathrm{der}}_{\mathrm{ch}}(A) \simeq C^\bullet_{\mathrm{ch}}(A, A)$ |
| direct $\Phi : \mathrm{CY}_d \to \mathrm{ChirAlg}$ | $\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$ |
| $A$ is modular | $\mathcal{C}^{\mathrm{op}}_\partial$ carries cyclic trace $\mathrm{Tr}_\mathcal{C}$ compatible with clutching; closed shadow has modular consequences |
| $\Delta_5$ = compact BPS Hilbert space | level-2 modular section of $\Omega_{\mathrm{central}}$; operator lift open |
| scalar $Z_{\mathrm{BPS}}$ = operator algebra | scalar = protected trace of still-to-be-constructed operator package |
| $W_\infty[\lambda] \Rightarrow E_\infty$ unconditional | conditional on the four hypotheses |
| formal Darboux $\Rightarrow$ compact target theorem | formal-Darboux + descent + QME + anomaly + locality $\Rightarrow$ candidate |

---

## Define-before-use, motivate-before-introduce

- Every symbol defined at or before first use.
- Every acronym written out at first occurrence: BCOV, BV, QME, VOA, OPE, CoHA, BKM, MNOP, DT, GW, PT, MC, CE, PV, KN.
- Every construction motivated by what came before. Definition forced by the structure preferred over definition by fiat.
- Example before abstract machine when the example carries the structural content.
- Section opens with the first mathematical object; closes by crystallizing what was proved and forcing what comes next.

---

## Supremum discipline

Repair is not demotion. Always take the harder route first: reconstruct the strongest true theorem by adding the missing object, habitat, topology, comparison map, homotopy, kernel, counterterm, computation, verified source, or obstruction class. Do not lower a theorem because the present proof is incomplete. Record a conditional statement only after the stronger formulation has been seriously attacked and the exact missing construction has been named.

A failed theorem surface is reworked until it becomes one of two pristine objects:
1. a proved theorem with all missing data supplied, or
2. a proved obstruction theorem identifying the precise cohomology class, cokernel functional, Roos class, graph row, or finite-window matrix equation that prevents the original statement.

Each attack-and-repair iteration pushes the failed surface upward toward this supremum form.

---

## Agent rules

1. No AI attribution anywhere. Commits by Raeez Lorgat only.
2. No `git stash`.
3. Do not amend commits without explicit instruction.
4. Do not rebuild after every edit.
5. Never guess a BV, Ext, cyclic-homology, OPE, or Feynman-integral formula. Derive from `main.tex`, direct computation, or primary literature.
6. Claim strength matches proof strength. Mark heuristic physics motivation separately from proved algebraic statements.
7. Do not spend proof budget on compact-CY / quintic / OSV / GV / Abel–Jacobi / CoHA / Igusa / BKM fixtures unless the user explicitly reopens the comparison lane.
8. Vol II $\mathbb{C} \times \mathbb{R}$ chiral-topological apparatus is not the native geometry; controlled reduction required.
9. The seventeen-site catalogue is binding before any draft is committed.
10. Prefer small, checkable patches.

---

## Termination criteria

A task is done when:

1. Mathematical content correct (Gate 1).
2. Every symbol defined at or before first use (Gate 2).
3. Voice register passes §V scan (Gate 3).
4. Construction motivated; example placed; opening / closing crystallized (Gate 4).
5. Architecture honors the platonic chapter sequence (Gate 5).
6. Sister catalogues consulted; no constellation antipattern hit; the seventeen-site catalogue clear (Gate 0).

If any gate fails: re-enter the rectification loop.

---

## The structural law

Every section answers one question, forced by what came before, in service of the single climax. Every theorem either constructs the local centre, identifies an obstruction, or computes an example. No sentence that fails to state mathematics or physics survives.
