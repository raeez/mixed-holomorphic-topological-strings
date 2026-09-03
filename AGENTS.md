# AGENTS.md — mixed holomorphic-topological strings

## Golden rule: no project management at any scale whatsoever in the manuscript

Reader-facing book and paper sources contain mathematics or physics only.
This is absolute at every scale: volume, part, chapter, section, theorem,
proof, remark, example, footnote, caption, table, front matter, back matter,
bibliography annotation, and PDF metadata.
Never insert agent/task instructions, audit or repair workflow, worktree or
commit details, review/packet status, test dashboards, TODO queues, progress
reports, ownership assignments, or references to models, agents, prompts, and
critiques. Keep such material outside the manuscript. Mathematical status is
different and must remain explicit: theorem, conditional consequence,
heuristic, conjecture, and open problem. State missing data as mathematics,
without narrating who found the gap. The objective is correct, rigorous,
complete mathematics; builds and prose polish do not replace proof. Pass this
rule to every subagent and check its returned prose.

> **Mirrors `./CLAUDE.md` on substance.** Both files encode the same wisdom; AGENTS.md emphasizes generative discipline, the four-part test for terminology, the standard-name catalogue, and Codex / GPT-5-family harness calibration.
>
> **Inherits `~/ecosystem/INVARIANTS.md`** — destructive-git forbidden list, no-LLM-commit-attribution, deep semantic merges, intelligence propagation, voice.
> **Inherits `~/ecosystem/AGENTS-HARNESS.md`** when present — Codex / GPT-5-family harness calibration: reasoning effort, agentic eagerness, tool-use discipline, persistence, verbosity, uncertainty handling, long-context outlining, self-reflection rubric, scope discipline.
>
> **Model target.** Deepest host-exposed GPT-5.5 / GPT-5-Codex-family model. `reasoning_effort = xhigh` for any non-trivial mathematical work; never lower than `high`.
>
> **Authoritative writing standards.** `./MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md` at this repository root binds. Read at session start.

---

## What this manuscript proves

The **formal-Darboux trace-sector stalk theorem for the Mixed Holomorphic-Topological Deligne problem** at $N$ Dirac branes:
\[
A^{\mathrm{cl}}_{\partial, N} = C^\bullet_{\mathrm{CE}}\bigl(\mathfrak{gl}_N,\; \mathrm{Kosz}([\phi_1, \phi_2])\bigr),\qquad
J(f) = \mathrm{Tr}\,f(\phi_1, \phi_2),\qquad
c_f \mapsto \theta_f,\quad u_f \mapsto J(f).
\]
The trace map $J$ is the formal Darboux coordinate on the scalar-reduced stable trace sector of the admissible HKR model for the chiral Hochschild cohomology $C^\bullet_{\mathrm{ch}}(A_b, A_b)$. The finite-$N$ Capelli scalar $\hbar N[\bar c]$ is the projective Lie anomaly of the trace representation; it is determinant-line or modular-line curvature only after the corresponding line, connection, and Atiyah-class pullback have been supplied. The obstruction-curvature taxonomy classifies the global comparison problem.

The constellation-level master theorem, of which this manuscript proves the scalar-reduced stable trace-sector formal-Darboux stalk:

> Closed sector $= Z^{\mathrm{der}}_{E_d^{\mathrm{ch}}}(\mathcal{C}^{\mathrm{op}}_\partial)$. Modular structure $=$ trace plus clutching. Quantum and global obstructions $=$ curvature in the supplied comparison complex. Scalar invariants $=$ sections of the modular line bundle on the period domain after the line datum is constructed.

This manuscript supplies the local trace-sector input to the mixed holomorphic-topological chiral $E_d$ Deligne problem.

---

## Voice

Combined voice: **Witten, Etingof, Polyakov, Dirac, Feynman, Costello, Gaiotto.** Russian research school discipline. Every statement either mathematics or physics. Nothing else survives.

A sentence that does not state mathematics or physics is a defect.

The canonical writing standards file at the root of this repository binds.

---

## The four-part test for new terms

Before introducing any new term, run the four-part test of §III of the writing standards. **All four must hold.**

1. **Scope.** No accepted term in algebra, geometry, number theory, homotopy theory, or mathematical physics covers the construction, even when those fields are searched together. *Most coinings fail here.*
2. **Material.** The object is a precise mathematical object — category, complex, sheaf, operad, algebra, functor, morphism, class, characteristic, integral, structure constant. Not an attitude, methodology, or slogan.
3. **Subject.** Etymology and form match the mathematical register: Greek/Latin roots, named after discoverer or operative property, or composition with accepted prefixes (chiral-, derived-, factorization-, modular-, shifted-, twisted-, completed-, filtered-, perfect-, virtual-).
4. **Inner yearning.** The mathematical structure itself yearns for the name; no other name fits as well. The strictest criterion. If a paragraph of standard prose describes the object cleanly, the structure does not yearn for a new name.

A term failing any of (1)–(4) is **branding**, deleted on sight.

### Examples passing all four
- *factorization algebra* — forced by locality structure (Beilinson–Drinfeld).
- *Maurer–Cartan element* — named after discoverer; forced by integrability.
- *shifted symplectic structure* — accepted prefix; forced by degree shift.
- *Borcherds product* — named after discoverer; forced by multiplicative lift.
- *chiral Hochschild cochain* — accepted prefixes; forced by chiral OPE.
- *derived chiral centre* — accepted prefixes; forced by open-closed centre construction.

### Examples failing
- *matrix microscope, brane microscope, matrix probe* — fail (1): "trace measurement" suffices; fail (2): name a methodology, not an object; fail (3): evocative metaphor; fail (4): structure yearns for "trace measurement on the derived zero fibre," not "microscope." Replace with "trace measurement" or "$J(f) = \mathrm{Tr}\,f(\phi_1, \phi_2)$" or "Dirac brane formal-stalk chart."
- *magic identity* — every identity has a name; cite WDVV, Bianchi, Jacobi, holomorphic anomaly, residue.
- *inner music, X spine, secret weapon* — fail all four; delete and state the structure.

When generating prose, theorem statements, or replacement abstracts, run the four-part test before any candidate term is inscribed.

---

## Standard terminology by subfield

The default; deviation requires the four-part test.

### Algebra and homological algebra

Lie / dg Lie / $L_\infty$-algebra. **Maurer–Cartan element**, MC equation, MC space, deformation functor. Hochschild cochain complex $C^\bullet(A, A)$ with **Gerstenhaber bracket** and **cup product**; Hochschild cohomology $HH^\bullet$; Hochschild homology $HH_\bullet$; **negative-cyclic** $HC^-_\bullet$; **periodic cyclic** $HP_\bullet$. **Chevalley–Eilenberg** complex $C^\bullet_{\mathrm{CE}}(\mathfrak{g}, M)$ — write out at first use. Koszul duality, complex, resolution. Bar construction $B$, cobar $\Omega$, twisting morphism. **Batalin–Vilkovisky (BV)**, classical / quantum master equation (CME / QME), BV bracket $\{-,-\}$, BV Laplacian $\Delta$. **Operad**, cooperad, $E_n$-operad, little $n$-disks, framed little disks, **Swiss-cheese operad** (Voronov; topological). **Factorization algebra** (Beilinson–Drinfeld, Costello–Gwilliam) — *not* a synonym for vertex algebra or chiral algebra. **Vertex algebra**, **vertex operator algebra (VOA)**, **chiral algebra** — distinguish: vertex algebra carries OPE on a formal disk; chiral algebra carries the right $\mathcal{D}$-module on a curve $C$. Drinfeld centre $Z(\mathcal{C})$, derived centre $Z^{\mathrm{der}}$, chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}$ — distinguish.

The bar complex is *not* a centre. Bar/cobar classifies twisting morphisms. The acting bulk is the derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(A) \simeq C^\bullet_{\mathrm{ch}}(A, A)$.

### Geometry

**Calabi–Yau** (always with diaeresis on the second i). Distinguish *$d$-Calabi–Yau category* (Kontsevich–Soibelman; non-degenerate negative-cyclic trace $HC^-_d(\mathcal{A}) \to k$) from *Calabi–Yau $d$-fold* ($K_X$ trivial). **Holomorphic symplectic** ($\omega \in \Omega^2$ closed, non-degenerate) versus **holomorphic volume form** (section of $K_X$) — not interchangeable. Hodge structure, mixed Hodge structure, variation of Hodge structure (VHS), period map. Moduli stack, derived moduli stack, derived intersection, derived zero locus $\mu^{-1}_{\mathrm{der}}(0)$. Kodaira–Spencer map, Tian–Todorov lemma, **BCOV theory** (Bershadsky–Cecotti–Ooguri–Vafa, 1993–94 — spell out at first use). Holomorphic anomaly equation: precise sign convention is binding. Threefold, fourfold, $n$-fold for complex dimension $n$. Perfect obstruction theory, virtual fundamental class $[X]^{\mathrm{vir}}$, virtual structure sheaf. **Donaldson–Thomas (DT)**, **Pandharipande–Thomas (PT)**, **Gromov–Witten (GW)**, **Maulik–Nekrasov–Okounkov–Pandharipande (MNOP)**.

The Dirac brane stack at $N$ branes is the derived commuting variety $[\mu^{-1}_{\mathrm{der}}(0) / \mathrm{GL}_N]$.

### Number theory and modular forms

Modular form, Siegel modular form, Hilbert modular form, automorphic form, Maass form. Borcherds product, theta lift, Saito–Kurokawa, Ikeda, Yoshida, Gritsenko lifts. **Igusa cusp form** $\Phi_{10} = \chi_{10}$ — *not* "$\Delta_5$" without prior definition; "$\Delta_5$" is a working handle for $\Phi_{10}^{1/2}$ or the level-five BKM denominator depending on convention; specify. **Borcherds–Kac–Moody (BKM) algebra**, denominator formula, Weyl–Kac character formula. Eisenstein series $E_k$, cusp form, CM point, Hecke operator, L-function. **CHL (Chaudhuri–Hockney–Lykken) model**, CHL point, dyonic invariant.

### Homotopical and $\infty$-categorical

$\infty$-category — always with the $\infty$ symbol; never spelled "infinity-category" inconsistently. Stable $\infty$-category, dg category, $A_\infty$-category, cyclic $A_\infty$-category. Homotopy colimit / limit, derived functor, (co)fibration, mapping space, adjunction. $\infty$-operad, dendroidal $\infty$-category, coloured operad. **Factorization homology** $\int_M \mathcal{A}$ (Lurie; Ayala–Francis). Pro-object, ind-object, **pro-Matlis**.

### Physics

Topological string, A-model, B-model, mirror symmetry. **Worldsheet $\Sigma$** (always Greek $\Sigma$; never "WS"). Target $X$. Mapping space $\mathrm{Map}(\Sigma, X)$. Moduli of curves $\overline{\mathcal{M}}_{g, n}$. Brane, D-brane, boundary condition, boundary state, boundary vacuum. BPS state, BPS index, BPS spectrum. Genus expansion $\sum_{g \geq 0} g_s^{2g - 2} F_g$; string coupling $g_s$; $\hbar$ for the QFT loop expansion. **Distinguish $g_s$ and $\hbar$.** Large-$N$, 't Hooft expansion, 't Hooft coupling $\lambda = g_{\mathrm{YM}}^2 N$. Open–closed, bulk–boundary, open-closed map, bulk-boundary OPE. **Chern–Simons** (3d, 3d holomorphic, 6d holomorphic), Witten genus, elliptic genus. **OPE** (operator product expansion), stress tensor $T(z)$, central charge $c$ or $\kappa$. Anomaly: distinguish gauge / global / 't Hooft / mixed / parity; specify the anomaly polynomial. Holomorphic twist, topological twist, $\Omega$-background, Nekrasov partition function.

---

## Two principles, seventeen sites

**P1.** Primitive $\neq$ chart.
**P2.** Shadow $\neq$ object.

Front-loaded for synthesis: the seventeen sites are the standard places where these principles have been violated. Every replacement abstract, master sentence, or theorem statement runs the seventeen-site check before inscription.

| # | failed claim | corrected form |
|---|---|---|
| 1 | $A$ primitive open object | $\mathcal{C}^{\mathrm{op}}_\partial$ primitive; $A_b = \mathrm{End}(b)$ for chosen $b$ |
| 2 | $\mathrm{Bar}(A) = $ bulk | $\mathrm{Bar}(A) = $ twisting coalgebra; $Z^{\mathrm{der}}_{\mathrm{ch}}(A) \simeq C^\bullet_{\mathrm{ch}}(A, A) = $ bulk |
| 3 | 2d chiral $\Rightarrow $ 3d HT via $E_1$-bar | chiral Deligne–Tamarkin: $A \rightsquigarrow Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ one-up |
| 4 | open sector on bare curve $X$ | open sector on $\partial X^{\mathrm{KN}}$ for Kato–Nakayama log $(X, D, \tau)$ |
| 5 | modularity is property of closed algebra | trace + clutching on the open category |
| 6 | five $\kappa$-numbers $(0, 0, 3, 5, 24)$ as one invariant | five distinct construction layers; spectral-sequence interpretation conjectural |
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
| 17 | quadratic chiral duality $\Rightarrow $ Koszul theorem | quadratic dual + MC injection; chiral Koszul homotopy theorem separate |

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

Every constellation volume populates one node. **This manuscript proves the scalar-reduced stable trace-sector formal-Darboux stalk of the admissible HKR model for $C^\bullet_{\mathrm{ch}}(A_b, A_b)$ at the Dirac brane node.**

When generating any synthesis, replacement abstract, or master sentence: anchor in this diagram. The diagram is the structural ground; do not claim a position outside it.

---

## The platonic chapter sequence

Eleven chapters; each forced by the previous.

1. **The setup.** $\mathbb{R}^2_{\mathrm{top}} \times \mathbb{C}^2_{\mathrm{hol}}$; brane stacks at holomorphic-symplectic points; the Mixed HT Deligne conjecture; the local stalk question.
2. **The shifted-cotangent BF Lie algebra.** $\mathfrak{h} = \mathbb{C}[[z_1, z_2]] / \mathbb{C}$, $\mathfrak{g} = \mathfrak{h} \ltimes \mathfrak{h}^\vee_{\mathrm{cont}}[1]$; Hamiltonian BF action.
3. **The derived commuting variety stack at $N$ Dirac branes.** $[\mu^{-1}_{\mathrm{der}}(0) / \mathrm{GL}_N]$, $Q\psi = [\phi_1, \phi_2]$.
4. **Boundary algebra and trace map.** $A^{\mathrm{cl}}_{\partial, N}$, $J(f) = \mathrm{Tr}\,f(\phi_1, \phi_2)$.
5. **CE/PV dictionary as Koszul coordinate model.** $c_f \mapsto \theta_f$, $u_f \mapsto J(f)$; identification with the scalar-reduced stable trace-sector coordinate in the admissible HKR model for $C^\bullet_{\mathrm{ch}}(A_b, A_b)$.
6. **The Capelli scalar.** $\hbar N[\bar c]$ as projective Lie anomaly of the trace representation; determinant-line or modular-line curvature only after the line, connection, and Atiyah-class pullback are supplied.
7. **The obstruction calculus.** $\mathfrak{K}_{\mathrm{HT}}$, $\Theta_{\mathrm{OCA}}$, \(F_{\mathrm{HT}}\), and the four obstruction-curvature rows. Six native obstructions become projections of one curvature only after the comparison-unifying datum is supplied.
8. **The pro-Matlis target.** $N$-tower categorical home; Matlis duality at finite presentation.
9. **Examples.** Heisenberg, $\hat{\mathfrak{g}}_k$, $\beta\gamma$, $\mathrm{Vir}_c$ (algebraic HT holographic reading; identification, not construction), $W_N$, $\mathbb{C}^3$, $K3$, $K3 \times E$, generic compact CY3.
10. **The $W_\infty[\lambda] / E_\infty$ admissible endpoint.** Conditional theorem.
11. **The frontier.** MNOP / framing; Hall–Drinfeld–Borcherds; gravitational lift of $\Phi_{10}$. Three open problems: chiral $E_d$ Deligne at $d \geq 2$; Hall–Drinfeld–Borcherds spectral sequence on compact non-toric CY3; operator-level lift of the modular line.

---

## Convention layer (binding)

- $d = \dim_{\mathbb{C}} X$ for target complex dimension.
- Local geometry is $\mathbb{R}^2_{\mathrm{top}} \times \mathbb{C}^2_{\mathrm{hol}}$ at a brane. Only Calabi-Yau datum is the trivial holomorphic volume / symplectic on $\mathbb{C}^2$, used for BV pairing, divergence-free Hamiltonian fields, cyclic trace densities. **Not** a compact CY$_3$ assumption; **not** a BCOV theorem; **not** a license to import quintic / OSV / GV / MNOP / Abel–Jacobi / CoHA / Igusa / BKM into the core local theorem surface.
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
- $\hbar$ versus $g_s$: distinguish.
- Holomorphic anomaly sign: BCOV-strict per `appendix-sign-conventions.tex`.
- Negative-cyclic / cyclic / Hochschild homology distinguished.
- $\mathcal{C}^{\mathrm{op}}_\partial = \Phi^{\mathrm{FA}}_d(\mathcal{A})\big|_{\partial X^{\mathrm{KN}}}$ on the Kato–Nakayama log boundary.
- $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}(\mathcal{F}) = \int_{\Sigma_{d-1}} \mathcal{F}\big|_C$ — Lurie–Ayala–Francis factorization homology.
- "Dirac brane stack" $= [\mu^{-1}_{\mathrm{der}}(0) / \mathrm{GL}_N]$, the derived commuting variety.
- Capelli scalar $\hbar N[\bar c]$ is the projective Lie anomaly of the trace representation; determinant-line or modular-line curvature requires the corresponding line, connection, and Atiyah-class pullback.
- Modular line bundle on $\overline{\mathcal{A}}_g = \Omega_{\mathrm{central}}$ at level $g$. Igusa $\Phi_{10}$ is its level-2 section; $\Delta_5 = \Phi_{10}^{1/2}$.
- CE/PV dictionary $c_f \mapsto \theta_f$, $u_f \mapsto J(f)$ is the Koszul coordinate model for the scalar-reduced stable trace sector of the admissible HKR model for $C^\bullet_{\mathrm{ch}}(A_b, A_b)$.

## Theorem-control predicates (binding)

- Native $\mathbb{C}^2$ holomorphic $E_2$ taxonomy retained before any curve-chiral reduction.
- BMK lane: one-pair analytic pro-Matlis retract is **not** strict native all-window support-local current transfer; obstruction $\mathrm{Ob}^\Pi_{\mathrm{BM}}$.
- Larger non-scalar $\theta_3$ row: evidence only with a CE ancestor, or a scalar-zero Costello local counterterm, or a complete companion-face table; tower compatibility through $\Delta^1_{M, N} = -\pi_{M, N}\mathfrak{b}^M + \mathfrak{b}^N$ plus the secondary $\varprojlim^1 H^0$ primitive class.
- Radial / Weyl theorem surface is $\Omega^{\mathrm{rad}}_{a, b}$, equivalently decorated PBW Stokes for $D^\square_{a, b} = C^+_{a, b} \partial_2$, with failure exactly a signed row in $\ker B^*_{a, b}$.
- Larger non-scalar Costello / QME theorem requires: filtered scalar projection, finite row arrays, primitive matrix $A^M c = -r^M$, transition matrices, Roos compatibility, centrality homotopies, curved bulk-to-defect kernel.
- Brane-preserving $\Omega$-background: normal scaling on $N_L X = \mathbb{R}_s \oplus \mathbb{C}_{z_1} \oplus \mathbb{C}_{z_2}$ with $t$ fixed; $T_\Omega = \mathbb{C}^*_{\varepsilon_s} \times \mathbb{C}^*_{\varepsilon_1} \times \mathbb{C}^*_{\varepsilon_2}$. Theorem surface includes $Q_\Omega = Q + \iota_{V_\Omega}$, $Q_\Omega^2 = L_{V_\Omega}$, inverted normal weights, residue-vs-Euler normalization, stratified factorization data.

---

## Codex / GPT-5-family harness

| parameter | setting | rationale |
|---|---|---|
| `reasoning_effort` | **`xhigh`** always; never below `high` | Mixed HT SFT / Kodaira-Spencer-type local BV / Costello graph-QME / $L_\infty$-renormalization is frontier mathematical physics; no downgrade. |
| `model` | **deepest host-exposed**: GPT-5.5 Pro / Heavy in ChatGPT when available; GPT-5.5 / latest GPT-5-Codex-family in Codex; API fallback latest GPT-5.4 / GPT-5-Codex with `xhigh` where supported | Pro-class mathematics + physics. |
| `verbosity` | as the argument requires | No abridgment of load-bearing expansions, anomaly terms, or Feynman sums. |
| token budget | unbounded for research | If context fills, compact side work. Never elide a propagator term, a Feynman graph, or a named anomaly. |
| tool use | parallel `read_file` for TeX + `scripts/` + figures | Batch reads before writing. |
| persistence | absolute | Do not yield on a partial computation. Either close the calculation or name the open term precisely. |
| self-reflection rubric | required before any inscription | See below. |

### Long-form proof harness

Public OpenAI material describes GPT-5.5 Pro as the ChatGPT research-grade option for hardest long-running workflows; GPT-5.5 in Codex as 400K-context agentic coding model. The private ChatGPT Pro harness is not public. The open analogue:

1. **Deliberation budget.** For theorem repair, cross-volume synthesis, adversarial review, or primary-source reconstruction, a 30–60 minute agent run is normal. Do not stop because the first plan is plausible. Stop only when the proof closes, a computation decides the point, or the exact open obligation is named.
2. **Private scratch, public proof trace.** Use private reasoning for search and synthesis; never expose raw scratchpad as an answer. Deliverable is the checked proof path: definitions, reductions, cited theorems, computations, remaining obstruction.
3. **Context before invention.** Load CLAUDE.md, this file, the canonical writing standards file, `main.tex`, preamble / macros / notation, diagram sources, compute scripts, cited local BV / Costello / Hamiltonian / Witten sources before the first mathematical edit. Load Vol III or compact-CY anchors only for an explicit comparison or firewall audit. Build an internal outline; do not write from memory.
4. **Multiple routes.** For any load-bearing identity, seek independent derivations: low-order amplitude, BV-degree check, graph computation, primary literature, local script, cross-repo consistency. Agreement is evidence; disagreement is the deliverable.
5. **Adversarial loop.** After a proposed repair, attack the strongest failure mode: sign, measure, propagator, anomaly term, BV degree, large-$N$ limit, false transfer into Vol III. Heal, then attack again until no fatal objection survives.
6. **Agent topology.** Large swarms partitioned by disjoint proof obligations or files. Subagents provide evidence, not authority. The main thread integrates by deep semantic merge and heals the proof, statement, or construction rather than voting truth into existence.
7. **Progress reports.** Long runs emit compact `commentary` checkpoints: what has been read, what has been ruled out, what proof obligation remains. Final answer is short unless the proof itself is the requested artifact.

### Self-reflection rubric (before any revision, inscription, or merge)

| category | top-marks test |
|---|---|
| correctness | every expansion term, sign, measure, BV degree verified |
| rigor | every load-bearing claim carries *proved / conjectured / expected / heuristic / computed / folklore* |
| attribution | every prior result cited by author + year + equation when available (BCOV 1993, Costello 2011, Costello–Li 2012, Witten 1988, local BV / Hamiltonian sources, Beilinson–Drinfeld 2004, Lurie HA, Ayala–Francis, etc.) |
| concrete-before-abstract | a worked example precedes the general claim |
| voice | per the canonical writing standards file (Witten / Etingof / Polyakov / Dirac / Feynman / Costello / Gaiotto) |
| four-part test | every coined term passes §III; otherwise replace with the field's standard term |
| seventeen sites | none of the seventeen failure patterns appears in the inscription |
| convention agreement | local conventions agree with `appendix-sign-conventions.tex` and Vol II; Vol III compact-CY conventions checked only in scope of an explicit comparison |

If any category falls short — restart that category. Do not patch.

### Long-context handling

`main.tex` + preamble / commands / macros + bibliography + figures routinely exceed 10K tokens.

1. Outline internally before responding. Do not show the outline.
2. Parallel-`read_file` every cited source and every relevant script.
3. When quoting a numerical coefficient, sign, or normalization, cite the TeX line or the script that produced it.

---

## The chriss-ginzburg-rectify discipline

For manuscript-proper writing, rewriting, theorem-lane reconstitution: load `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md` before editing.

Five phases:

1. **Global diagnostic** (read-only). Map narrative thread, motivation gaps, define-before-use violations, opening / closing, physical insight calibration, prose, formula red flags.
2. **Platonic restructuring.** Compute layer survey, six platonic-ideal questions, structural edits, structural convergence iteration.
3. **Linear reconstitution loop.** Chunks of 50–100 lines. Six gates simultaneously:
   - **Gate 0** — principle consultation: writing standards, INVARIANTS.md, sister catalogues, four-part test, seventeen-site catalogue.
   - **Gate 1** — mathematical truth.
   - **Gate 2** — define-before-use.
   - **Gate 3** — voice (§V scan).
   - **Gate 4** — motivate-before-introduce.
   - **Gate 5** — chriss-ginzburg architecture.
4. **Adversarial re-audit** — three independent agents (RED / BLUE / GREEN); if any actionable issue, re-enter Phase 3.
5. **Final convergence.** Build, test, report.

Stop only at convergence or when the exact remaining obstruction is named.

---

## Constellation paths

- `~/chiral-bar-cobar/` (Vol I) — chiral Koszul; bar / cobar / centre distinction.
- `~/chiral-bar-cobar-vol2/` (Vol II) — $A_\infty$ chiral algebras + 3D HT QFT; algebraic 3d-gravity HT sector.
- `~/chiral-bar-cobar-vol4/` (Vol IV) — architectural inheritance.
- `~/calabi-yau-quantum-groups/` (Vol III) — CY-to-chiral frontier; two-stage functor; Hall–Drinfeld realization. **External comparison only.** No compact-CY$_3$ / Vol III / global BCOV theorem follows from this repository without a separate matched-conventions theorem.
- `~/igusa-cusp-form/` — Borcherds + BKM + $\Delta_5$. **External comparison only.** No BKM consequence follows from the local Hamiltonian BF / Moyal calculation alone.
- `~/ecosystem/` — discipline layer.

Cross-volume firewall: convention divergence is load-bearing — flag, do not silently reconcile.

---

## Build and source

### Build

```bash
cd ~/mixed-holomorphic-topological-strings
make pdf         # default
make fast        # iterative builds during rectification
make release     # full release; PDFs copied to iCloud
```

Stale processes: `pkill -9 -f pdflatex 2>/dev/null; sleep 2`. Do not rebuild after every edit; build at session end or when verification requires it.

### Source layout

`main.tex` (root), `abstract.tex`, `preamble.tex`, `authors.tex`, `commands.tex`, `mathmacros.tex`, `notation.tex`, `nomenclature.tex`. Appendices `appendix-*.tex`. Theorem files `tate-T*-*.tex`, `tate-P*-*.tex`. `frontier_mnop_framing_volume.tex`. `Makefile`, `firstorder.{png,svg}`, `thirdordera.{png,svg}`, `thirdorderb.{png,svg}`. `scripts/`.

### Compute layer

`scripts/check_moyal_coefficients.py`, `check_one_psi_homology.py`, additional sign-rule and homology checks. Lead with content that has compute backing. Flag content with no compute verification.

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

## Codex load order

1. `./CLAUDE.md` — repo briefing.
2. `./MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md` — canonical writing standards.
3. `~/ecosystem/INVARIANTS.md` — ecosystem rules.
4. `~/ecosystem/AGENTS-HARNESS.md` (when present) — Codex / GPT-5 harness.
5. `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md` — rectification discipline.
6. `main.tex` (root) + `preamble.tex` + `commands.tex` + `mathmacros.tex` + `notation.tex` + `nomenclature.tex`.
7. Figure sources (`firstorder.svg`, `thirdordera.svg`, `thirdorderb.svg`) and `scripts/` for any quoted computation.
8. Cross-repo Vol III / Igusa / compact-CY sources only when an explicit comparison or firewall task requires them.

---

## Agent rules

1. **No AI attribution anywhere.** Commits by Raeez Lorgat only.
2. **No `git stash`.**
3. **Do not amend commits without explicit instruction.**
4. **Do not rebuild after every edit.** Build at session end when useful.
5. **Never guess** a BV, Ext, cyclic-homology, OPE, Feynman-integral formula. Derive from `main.tex`, direct computation, or primary literature.
6. **Claim strength matches proof strength.** Mark heuristic physics motivation separately from proved algebraic statements.
7. **User-authorized large swarms** are permitted. Disjoint scopes. Explicit integration ownership. Deep semantic merge across `~/chiral-bar-cobar`, `~/chiral-bar-cobar-vol2`, `~/mixed-holomorphic-topological-strings` for cross-cutting claims; `~/calabi-yau-quantum-groups`, `~/igusa-cusp-form`, compact-CY sources only on assigned matched-conventions or firewall tasks.
8. **Do not spend proof budget** on compact-CY / quintic / OSV / GV / Abel–Jacobi / CoHA / Igusa / BKM fixtures unless the user explicitly reopens the comparison lane.
9. **Vol II $\mathbb{C} \times \mathbb{R}$** chiral-topological apparatus is not the native geometry of this paper. Curve chiral algebras, Zhu algebras, and $SC^{\mathrm{ch,top}}$ comparisons require a controlled reduction with $z_2$-mode or principal-part data, pushed-forward bracket, BV pairing, brane image, anomaly matching.
10. **$\Omega$-background** uses the brane-preserving normal scaling torus on $N_L X = \mathbb{R}_s \oplus \mathbb{C}_{z_1} \oplus \mathbb{C}_{z_2}$ with $t$ fixed.
11. **The seventeen-site catalogue** is binding before any draft is committed.
12. **Prefer small, checkable patches.** If changing a formula, record the verification path in nearby prose only when it helps future checking.

---

## User-authorized max-effort swarm protocol

When the user explicitly asks for an adversarial, rescue, review, or cross-volume swarm: treat as authorization to use the largest useful swarm the runtime supports. Do not downshift to old 3-agent / 5-agent / 30-agent cautionary numbers. Request the strongest model and the highest reasoning budget; when the host does not expose those controls, encode the requirement in the agent prompt: proof-grade, first-principles, max-effort.

Swarm design before launch: partition agents by disjoint mathematical axes, files, or proof obligations; name the integration owner; forbid agents from reverting work they did not make; require deep semantic merge across `~/chiral-bar-cobar`, `~/chiral-bar-cobar-vol2`, and `~/mixed-holomorphic-topological-strings` only when the claim genuinely crosses those repos.

Every attack-heal agent returns: claim attacked, failure mode or proof, local file anchors, primary source anchors, exact formulas / constants, claim-status recommendation, files changed, computations run, remaining open questions. For theorem-level work, attack/heal cycles repeat until convergence: no new fatal attack survives, and at least one real mathematical improvement is inscribed. If the attack breaks a theorem surface, the heal step does not stop at demotion — it builds the missing data or proves the exact obstruction theorem and queues the next construction target.

The main thread integrates; agents do not vote truth into existence. Preserve all mathematically substantive content; resolve conflicts by examining both sides in context; verify with targeted `rg`, local computations, and session-end builds when appropriate.

---

## Supremum discipline

Repair is not demotion. Always take the harder route first: reconstruct the strongest true theorem by adding the missing object, habitat, topology, comparison map, homotopy, kernel, counterterm, computation, verified source, or obstruction class. Do not lower a theorem because the present proof is incomplete. Record a conditional statement only after the stronger formulation has been seriously attacked and the exact missing construction has been named.

A failed theorem surface is reworked until it becomes one of two pristine objects:
1. a proved theorem with all missing data supplied, or
2. a proved obstruction theorem identifying the precise cohomology class, cokernel functional, Roos class, graph row, or finite-window matrix equation that prevents the original statement.

Each attack-and-repair iteration pushes the failed surface upward toward this supremum form.

---

## Output norms

- For research synthesis: lapidary, dense, declarative; no decoration.
- For replacement abstracts: anchor in the master architecture; verify each claim against the seventeen-site catalogue; run the four-part test on every coined term.
- For commit messages: state the mathematical content of the change; no LLM attribution.
- For PR descriptions: same; cite theorem numbers, formula numbers, and the changed gates.
- For long-form proof traces: definitions, reductions, cited theorems, computations, remaining obstruction; private reasoning stays private.

---

## Termination criteria

A task is done when:

1. Mathematical content correct (Gate 1).
2. Every symbol defined at or before first use (Gate 2).
3. Voice register passes §V scan (Gate 3).
4. Construction motivated; example placed; opening / closing crystallized (Gate 4).
5. Architecture honors the platonic chapter sequence (Gate 5).
6. Sister catalogues consulted; no constellation antipattern hit; the seventeen-site catalogue clear; the four-part test passed for every coined term (Gate 0).

If any gate fails: re-enter the rectification loop.

---

## Escalation triggers (additional to harness defaults)

- A computation cannot be closed with honest rigor → the open term, named precisely, **is** the deliverable.
- A compact-CY, Vol III, CoHA, Igusa, or BKM claim appears inside the core local theorem surface → stop, report, quarantine unless the user explicitly assigns a comparison theorem.
- A figure's contents disagree with the prose narrative → stop, report; the figure is usually the computation; overwrite only under user direction.
- Any term enters the manuscript that has not passed the four-part test → stop, replace with the field's standard term.
- Any of the seventeen failure-site patterns appears in a draft → stop, replace with the corrected form.

---

## The structural law

Every section answers one question, forced by what came before, in service of the single climax. Every theorem either constructs the local centre, identifies an obstruction, or computes an example. No sentence that fails to state mathematics or physics survives.

---

## Code-writing discipline — repo application

Per `~/ecosystem/INVARIANTS.md §XIII`. Twelve rules instantiated for mixed-holomorphic-topological-strings (mixed holomorphic–topological SFT on $\mathbb{R}^2_{\mathrm{top}} \times \mathbb{C}^2_{\mathrm{hol}}$; BCOV / Kodaira–Spencer / holomorphic-anomaly / $L_\infty$ renormalization; seventeen-site catalogue):

1. **Think Before Coding.** Every $L_\infty$-renormalization-edit names the affected BCOV / Kodaira–Spencer / holomorphic-anomaly equation, the mixed-signature factor (topological vs holomorphic), and the claim-status macro. Every new term passes the four-part coining test.
2. **Simplicity First.** Mixed-signature is the scope; no speculative pure-holomorphic or pure-topological digressions outside the named split. No new objects beyond what the seventeen-site catalogue authorises. Do not spend proof budget on compact-CY / quintic / OSV / GV / Abel–Jacobi / CoHA / Igusa / BKM fixtures without explicit reopening.
3. **Surgical Changes.** A holomorphic-anomaly equation edit does not opportunistically rewrite the Kodaira–Spencer setup. A $L_\infty$ renormalization step is local to its diagrammatic level. The five-gate termination criteria bound the rectification loop — do not exceed.
4. **Goal-Driven Execution.** Success = `pdflatex main.tex` clean, theorem ledger consistent, all five Termination Gates pass (mathematical content, define-before-use, voice register, motivation + example + crystallisation, platonic architecture, sister catalogues clear, four-part test passed). Build session-end only.
5. **Use the model only for judgment calls.** Cross-references and bibliography deterministic. Renormalization counterterm-bookkeeping is deterministic — verify, do not LLM-approximate.
6. **Token budgets are not advisory.** Monograph; checkpoint between renormalization levels and between chapters. Supremum discipline: take the harder route first — reconstruct the strongest true theorem rather than lowering one.
7. **Surface conflicts, don't average them.** Cross-volume vertical equivalences with the chiral-bar-cobar constellation are canonical at the chiral side where shared; flag drift here. A figure disagreeing with prose halts and reports — figure usually wins (the computation).
8. **Read before you write.** Read the affected BCOV / KS / holomorphic-anomaly setup before editing a renormalization step. Cross-reference primary literature for any BV / Ext / cyclic-homology / OPE / Feynman-integral formula.
9. **Tests verify intent.** Claim-status macros honest; mixed-signature calculation checks verify computed counterterms, not just symbolic shapes. The five-gate termination criteria are the load-bearing tests. Heuristic physics motivation is marked separately from proved algebraic statements.
10. **Checkpoint after every significant step.** Between renormalization levels, summarize counterterm-bookkeeping delta. Between rectification iterations, restate which of the five gates remain open.
11. **Match the codebase's conventions, even if you disagree.** raeez-math-template per `INVARIANTS.md §XII`. The `thm` environment guard per `repo-roster.sh::MATH_TEMPLATE_CONSUMERS`. Vol II $\mathbb{C} \times \mathbb{R}$ chiral-topological apparatus is not the native geometry — controlled reduction required.
12. **Fail loud.** Surface every failed counterterm-cancellation; never silently substitute heuristic for verified. Any seventeen-site failure pattern in a draft halts and replaces. Any new term that has not passed the four-part test halts and replaces. Repair upward to a proved theorem or a proved obstruction — never demote.
