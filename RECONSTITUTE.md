# Reconstitution Kickstart — mixed-holomorphic-topological-strings

You are a fresh Claude session at the root of `~/mixed-holomorphic-topological-strings`. Reconstitute this manuscript into its platonic ideal form per the maps and standards on disk.

The manuscript proves the **formal-Darboux trace-sector stalk theorem for the Mixed Holomorphic-Topological Deligne problem** at $N$ Dirac branes:
\[
A^{\mathrm{cl}}_{\partial, N} = C^\bullet_{\mathrm{CE}}\bigl(\mathfrak{gl}_N,\; \mathrm{Kosz}([\phi_1, \phi_2])\bigr),\qquad J(f) = \mathrm{Tr}\,f(\phi_1, \phi_2),\qquad c_f \mapsto \theta_f,\ u_f \mapsto J(f).
\]
The trace map $J$ is the formal Darboux coordinate on the scalar-reduced stable trace sector of the admissible HKR model for the chiral Hochschild cohomology $C^\bullet_{\mathrm{ch}}(A_b, A_b)$. The finite-$N$ Capelli scalar $\hbar N[\bar c]$ is the projective Lie anomaly of the trace representation; determinant-line or modular-line curvature requires the corresponding line, connection, and Atiyah-class pullback.

---

## Phase 0 — bootstrap (one batched parallel read)

In a single message, read in parallel:

- `./CLAUDE.md` — master theorem; two principles (P1 primitive ≠ chart, P2 shadow ≠ object); seventeen-site failure catalogue; master architecture diagram; eleven-chapter platonic sequence; convention layer; theorem-control predicates; six convergence gates; forbidden patterns.
- `./AGENTS.md` — four-part test for new terms; standard terminology by subfield; Codex/GPT-5 harness; self-reflection rubric.
- `./MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md` (symlinked from `~/ecosystem/`) — canonical writing contract (binds).
- `./main.tex`, `./preamble.tex`, `./commands.tex`, `./mathmacros.tex`, `./notation.tex`, `./nomenclature.tex`, `./abstract.tex`.
- All `./appendix-*.tex` and `./tate-*.tex`.
- `./Makefile`.

Internalize before any edit: the seven-voice register (Witten, Etingof, Polyakov, Dirac, Feynman, Costello, Gaiotto); the master theorem; the two principles; the seventeen-site failure catalogue; the master architecture; the platonic chapter sequence; the convention layer; the theorem-control predicates; the four-part test for new terms; the six convergence gates.

---

## Phase 1 — diagnostic (main thread, no edits)

Output a single mapping table from current `main.tex` sections + appendices/tate-* files into the eleven platonic chapters:

1. The setup. ($\mathbb{R}^2_{\mathrm{top}} \times \mathbb{C}^2_{\mathrm{hol}}$; Mixed HT Deligne problem; this manuscript proves the scalar-reduced stable trace-sector formal-Darboux stalk.)
2. The shifted-cotangent BF Lie algebra. ($\mathfrak{h} = \mathbb{C}[[z_1, z_2]]/\mathbb{C}$; $\mathfrak{g} = \mathfrak{h} \ltimes \mathfrak{h}^\vee_{\mathrm{cont}}[1]$; Hamiltonian BF action.)
3. The derived commuting variety stack at $N$ Dirac branes. ($[\mu^{-1}_{\mathrm{der}}(0)/\mathrm{GL}_N]$; $Q\psi = [\phi_1, \phi_2]$.)
4. Boundary algebra and trace map. ($A^{\mathrm{cl}}_{\partial, N}$; $J(f) = \mathrm{Tr}\,f(\phi_1, \phi_2)$.)
5. CE/PV dictionary as Koszul coordinate model. ($c_f \mapsto \theta_f$, $u_f \mapsto J(f)$ identifies the scalar-reduced stable trace-sector coordinate in the admissible HKR model for $C^\bullet_{\mathrm{ch}}(A_b, A_b)$.)
6. The Capelli scalar. ($\hbar N[\bar c]$ as projective Lie anomaly of the trace representation; determinant-line or modular-line curvature after the line, connection, and Atiyah-class pullback are supplied.)
7. The obstruction calculus. ($\mathfrak{K}_{\mathrm{HT}}$; $\Theta_{\mathrm{OCA}}$; \(F_{\mathrm{HT}}\); four obstruction-curvature rows; six native obstructions become projections of one curvature only after the comparison-unifying datum is supplied.)
8. The pro-Matlis target. ($N$-tower categorical home; Matlis duality at finite presentation.)
9. Examples. (Heisenberg, $\hat{\mathfrak{g}}_k$, $\beta\gamma$, $\mathrm{Vir}_c$ identification not construction, $W_N$, $\mathbb{C}^3$, $K3$, $K3 \times E$, generic compact CY3.)
10. The $W_\infty[\lambda]/E_\infty$ admissible endpoint. (Conditional on Prochazka, Creutzig–Kanade–Linshaw, Pope–Romans–Shen/Bakas, Yamada.)
11. The frontier. (MNOP/framing; Hall–Drinfeld–Borcherds; gravitational lift of $\Phi_{10}$; three open problems.)

The table has columns: chapter # · platonic content · current source files · structural delta (missing / redundant / misplaced / weak-motivation / loitering). No prose, no recap. Output the table and proceed.

---

## Phase 2 — parallel reconstitution swarm (one batch of 15 Agent calls)

In a single message, dispatch 15 agents in parallel. Each Agent call uses the **general-purpose** subagent type with `isolation: "worktree"`. Each agent receives a self-contained brief built from the **shared context block** below plus its **specific task**. Each runs the full chriss-ginzburg-rectify Phase 3 six-gate loop on its assigned target.

### Shared context block (same for every agent)

> You are reconstituting one chapter (or one cross-cutting axis) of the mixed-holomorphic-topological-strings manuscript. The manuscript proves the scalar-reduced stable trace-sector formal-Darboux stalk for the Mixed HT Deligne problem: the global closed-sector target is $Z^{\mathrm{der}}_{E_d^{\mathrm{ch}}}(\mathcal{C}^{\mathrm{op}}_\partial)$, while this manuscript computes the local trace-sector coordinate at a Dirac brane: $A^{\mathrm{cl}}_{\partial, N} = C^\bullet_{\mathrm{CE}}(\mathfrak{gl}_N, \mathrm{Kosz}([\phi_1, \phi_2]))$, $J(f) = \mathrm{Tr}\,f(\phi_1, \phi_2)$, $c_f \mapsto \theta_f$, $u_f \mapsto J(f)$.
>
> **Mandatory reads before editing:** `~/mixed-holomorphic-topological-strings/CLAUDE.md`, `AGENTS.md`, `MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md`, `preamble.tex`, `commands.tex`, `mathmacros.tex`, `notation.tex`, `appendix-sign-conventions.tex`, plus the specific files for your task.
>
> **Voice (binding):** Witten, Etingof, Polyakov, Dirac, Feynman, Costello, Gaiotto. Russian research school discipline. Every statement either mathematics or physics. Nothing else survives.
>
> **Two principles (binding):** P1 primitive $\neq$ chart; P2 shadow $\neq$ object. Seventeen-site failure catalogue applies — corrected forms in CLAUDE.md.
>
> **Convention layer (binding):** $\mathcal{C}^{\mathrm{op}}_\partial = \Phi^{\mathrm{FA}}_d(\mathcal{A})|_{\partial X^{\mathrm{KN}}}$; $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}(\mathcal{F}) = \int_{\Sigma_{d-1}} \mathcal{F}|_C$ (factorization homology); Dirac brane stack $= [\mu^{-1}_{\mathrm{der}}(0)/\mathrm{GL}_N]$ (derived commuting variety); Capelli scalar $\hbar N[\bar c]$ is the projective Lie anomaly of the trace representation; modular-line curvature requires the corresponding line, connection, and Atiyah-class pullback; Igusa $\Phi_{10}$ is a level-2 section only after that modular-line datum is supplied. CE/PV dictionary is the Koszul coordinate model for the scalar-reduced stable trace sector of $C^\bullet_{\mathrm{ch}}(A_b, A_b)$.
>
> **Six gates (all must pass simultaneously):** Gate 0 principle consultation (writing standards, INVARIANTS, sister catalogues, seventeen sites). Gate 1 mathematical truth (recompute every formula, verify every proof step, qualify every scope). Gate 2 define-before-use (every symbol defined at or before first use; every acronym written out at first occurrence). Gate 3 voice (§V scan: no meta-narration, no bookkeeping, no catalogue IDs, no branding, no hedging, no negative framing, no CS jargon, no approximation language for exact identifications). Gate 4 motivate-before-introduce (every construction motivated by what came before). Gate 5 chriss-ginzburg architecture (every section answers one question, in service of the climax).
>
> **Forbidden patterns (delete on sight):** matrix microscope, brane microscope, magic identity, inner music, X spine, secret weapon; Theorem A/B/C labels in body prose; Wave $N$ / Phase $j$ / round $M$; "we now turn to", "having established", "this section sharpens"; "is closely related to", "corresponds to" when exact; "is wrong", "would be", "must not"; "certificate", "manifest", "spec", "schema"; "we hope", "perhaps", "remarkably", "crucially", "notably". Replacements in CLAUDE.md.
>
> **Four-part test for new terms (Scope, Material, Subject, Inner Yearning):** if a term you are about to inscribe fails any of the four, replace with the field's standard term. Most coinings fail Scope. List of accepted terms by subfield in AGENTS.md §IV.
>
> **Theorem-control predicates (binding):** native $\mathbb{C}^2$ holomorphic $E_2$ taxonomy retained before any curve-chiral reduction; BMK pro-Matlis retract is not strict native all-window support-local current transfer (obstruction $\mathrm{Ob}^\Pi_{\mathrm{BM}}$); $\theta_3$ requires CE ancestor or scalar-zero Costello local counterterm or complete companion-face table plus $\Delta^1_{M, N}$ + $\varprojlim^1 H^0$ secondary; radial/Weyl is $\Omega^{\mathrm{rad}}_{a, b}$, decorated PBW Stokes for $D^\square_{a, b} = C^+_{a, b}\partial_2$, failure exactly a signed row in $\ker B^*_{a, b}$; non-scalar Costello/QME requires filtered scalar projection + finite row arrays + $A^M c = -r^M$ + transition matrices + Roos compatibility + centrality homotopies + curved bulk-to-defect kernel; brane-preserving $\Omega$-background is normal scaling on $N_L X = \mathbb{R}_s \oplus \mathbb{C}_{z_1} \oplus \mathbb{C}_{z_2}$ with $t$ fixed.
>
> **Compute layer:** `scripts/check_moyal_coefficients.py`, `scripts/check_one_psi_homology.py`. Lead with content that has compute backing.
>
> **Output contract:** edits inscribed; residual obstruction (if any) named precisely; frontier items uncovered (with file references). Report under 300 words.

### Per-agent specific tasks

Dispatch 15 agents in parallel with these specific assignments.

**C1 — Chapter 1 setup.** Read `main.tex` opening sections + `abstract.tex`. Reconstitute Chapter 1 to state the Mixed HT Deligne problem as the global object and this manuscript as its scalar-reduced stable trace-sector formal-Darboux stalk. Replace any "main theorem of the whole subject" framing with "formal-Darboux trace-sector stalk theorem." Opening sentence must be the platonic opener in CLAUDE.md. No globalization claim survives without "+ descent + QME + anomaly + locality $\Rightarrow$ candidate."

**C2 — Chapter 2 BF Lie algebra.** Read main.tex sections on $\mathfrak{h}, \mathfrak{g}$, BF action; `appendix-master-deformation-complex.tex`. Reconstitute as the unique compatible local action on the shifted cotangent of $\mathfrak{h}$. State $\mathfrak{g} = \mathfrak{h} \ltimes \mathfrak{h}^\vee_{\mathrm{cont}}[1]$ as forced by the holomorphic-symplectic Darboux normal form.

**C3 — Chapter 3 derived commuting variety.** Read main.tex sections on $(\phi_1, \phi_2)$, moment map $\mu$, derived zero locus. Name the stack as $[\mu^{-1}_{\mathrm{der}}(0) / \mathrm{GL}_N]$ — the derived commuting variety stack (standard name). Physical reading: $N$ Dirac branes. Cite Costello / Pantev–Toën–Vaquié–Vezzosi / Calaque for the derived stack.

**C4 — Chapter 4 boundary algebra and trace.** Read main.tex sections on $A^{\mathrm{cl}}_{\partial, N}$ and $J$. Surface that $J: \mathcal{O}(\mathfrak{g}) \to A^{\mathrm{cl}}_{\partial, N}$ is the trace map (not a "measurement"). Distinguish $A_b$ (chart at chosen vacuum $b$) from $\mathcal{C}^{\mathrm{op}}_\partial$ (primitive open object — primitive lives in the constellation, this manuscript uses the chart).

**C5 — Chapter 5 CE/PV dictionary as Koszul coordinate model.** Read `tate-P3-universality.tex`, `tate-T2-nilpotent-truncation.tex`, `tate-T5-chain-level-primitive.tex`. The dictionary $c_f \mapsto \theta_f$, $u_f \mapsto J(f)$ is the Koszul coordinate model for the scalar-reduced stable trace sector of the admissible HKR model for $C^\bullet_{\mathrm{ch}}(A_b, A_b)$. State exactly which cohomology is identified; the universality theorem (P3) is then a corollary only in that sector.

**C6 — Chapter 6 Capelli scalar.** Read `tate-T4-bv-vanishing.tex`, `appendix-unreduced-bv-qme.tex`. The Capelli scalar is the projective Lie anomaly of the trace representation. State determinant-line or modular-line curvature only after the line, connection, and Atiyah-class pullback are supplied. Scheme dependence per `appendix-factorization-current-conventions.tex`.

**C7 — Chapter 7 obstruction calculus.** Read `appendix-master-deformation-complex.tex` + main.tex sections on $\mathfrak{K}_{\mathrm{HT}}, \Theta_{\mathrm{OCA}}, F_{\mathrm{HT}}$. State the four obstruction-curvature rows as a criterion in the common comparison complex. Six native obstructions (radial Stokes, pro-Matlis, Capelli, modular clutching, BCOV/GV/DT compact comparison, Hall–Drinfeld–Borcherds) become coordinates of one \(F_{\mathrm{HT}}\) only after the comparison-unifying datum and projection maps are supplied.

**C8 — Chapter 8 pro-Matlis.** Read `appendix-matlis-principal-parts.tex`. Motivate pro-Matlis as the categorical home of bulk-boundary duality along the $N$-tower. Pro-Matlis controls the finite-window leakage row; the full obstruction-curvature taxonomy appears only after the common comparison complex is supplied.

**C9 — Chapter 9 examples.** Read main.tex example sections. Reconstitute as the test of the local theorem: Heisenberg, $\hat{\mathfrak{g}}_k$, $\beta\gamma$, $\mathrm{Vir}_c$ (algebraic HT holographic reading; identification, not construction), $W_N$, $\mathbb{C}^3$, $K3$, $K3 \times E$ (cross-link to `~/calabi-yau-quantum-groups` for five-layer $\kappa$ structure; cross-link to `~/igusa-cusp-form` for level-2 modular section), generic compact CY3. Each example is a falsifying test, not a decoration.

**C10 — Chapter 10 $W_\infty[\lambda] / E_\infty$ admissible endpoint.** Read main.tex sections on $W_\infty$. Conditional theorem; admissible locus stated. Hypotheses: Prochazka triangular truncation, Creutzig–Kanade–Linshaw parafermion compatibility, Pope–Romans–Shen/Bakas, Yamada weight-window. Spin-$\leq 8$ checks are evidence within the locus.

**C11 — Chapter 11 frontier.** Read `frontier_mnop_framing_volume.tex`. State three open problems: (i) chiral $E_d$ Deligne conjecture at $d \geq 2$; (ii) Hall–Drinfeld–Borcherds comparison spectral sequence on compact non-toric CY3 (with the five-layer $\kappa$ structure as $E_2$ page); (iii) operator-level lift of the modular line bundle on $K3 \times E$ (the candidate: bulk module $C^\bullet_{\mathrm{ch}}(A_b, A_b)$ at $K3 \times E$ HT theory's brane vacuum, twisted by $\Omega_{\mathrm{central}}$ at level 2). Closing sentence per CLAUDE.md.

**X-V — voice + seventeen-site cross-cutting scan.** Run §V of the writing standards across the entire reconstituted manuscript. Hits: meta-narration, bookkeeping, catalogue IDs, branding, hedging, negative framing, CS jargon, approximation language. Run the seventeen-site catalogue. Replace per CLAUDE.md table.

**X-D — define-before-use + acronym audit.** Verify every symbol is defined at or before first use. Verify BCOV, BV, QME, VOA, OPE, CoHA, BKM, MNOP, DT, GW, PT, MC, CE, PV, KN are written out at first occurrence. Verify motivate-before-introduce for every construction.

**X-S — convention layer + theorem-control predicates.** Verify $d = \dim_{\mathbb{C}} X$; worldsheet $\Sigma$ named; framing; BV/ghost/form degree separation; Koszul/Gerstenhaber signs per `appendix-sign-conventions.tex`; $\hbar$ vs $g_s$; BCOV-strict holomorphic anomaly sign; $\mathrm{Sp}^{\mathrm{ch}} = \int$; pro-Matlis $N$-tower home; Capelli scalar $= \hbar N[\bar c]$ as projective Lie anomaly; determinant-line or modular-line curvature only after line data; native $\mathbb{C}^2$ taxonomy retained; BMK obstruction $\mathrm{Ob}^\Pi_{\mathrm{BM}}$; $\theta_3$ requirements; radial/Weyl $\Omega^{\mathrm{rad}}_{a, b}$; non-scalar Costello/QME data; brane-preserving $\Omega$-background.

**X-O — opening / closing crystallization + cross-chapter inevitability.** Verify each chapter's opening starts with the first mathematical object (no summary dump) and each chapter's closing crystallizes what was proved and forces the next. Verify the inter-chapter transitions are mathematical observations, not connective tissue. Confirm the platonic structural law: every section answers one question, forced by what came before, in service of the single climax.

---

## Phase 3 — integration (main thread, deep semantic merge)

Receive all 15 reports. Deep semantic merge per `~/ecosystem/INVARIANTS.md §VII` — no `-s ours`, no `-s theirs`, every conflict resolved by examining both sides in context.

Run the cross-cutting scans X-V, X-D, X-S, X-O against the integrated manuscript one more time. If any gate fails: re-spawn the affected per-chapter agent on the affected chunk.

Run compute layer:
```bash
cd ~/mixed-holomorphic-topological-strings
python3 scripts/check_moyal_coefficients.py
python3 scripts/check_one_psi_homology.py
```

Build:
```bash
pkill -9 -f pdflatex 2>/dev/null; sleep 2
make fast
```

If build fails: name the LaTeX error precisely and re-spawn the affected agent.

---

## Phase 4 — final convergence

```bash
make release
```

Verify: `out/main.pdf` and `out/frontier_mnop_framing_volume.pdf` exist; clean log; zero undefined references; no new overfull boxes versus the prior release.

Final report (under 500 words):
- Chapters reconstituted (one line each).
- Identifications surfaced (Capelli $= \hbar N[\bar c]$ as projective Lie anomaly; determinant/modular curvature only after line data; pro-Matlis $= N$-tower categorical home; CE/PV $=$ scalar-reduced stable trace-sector Koszul coordinate model; chiral specialization $=$ factorization homology; Dirac brane stack $=$ derived commuting variety).
- Residual obstructions named (precisely, with file references).
- Frontier open problems updated (the three named in Chapter 11).
- Build status (`out/main.pdf` page count; clean / errors).

---

## Termination

Done when:

1. Mathematical content correct (Gate 1) across every chunk.
2. Every symbol defined at or before first use (Gate 2).
3. Voice register passes §V scan (Gate 3) — no hits in body prose.
4. Construction motivated; example placed; opening / closing crystallized (Gate 4).
5. Architecture honors the platonic chapter sequence (Gate 5).
6. Sister catalogues consulted; seventeen-site catalogue clear; four-part test passed for every coined term (Gate 0).
7. `make release` succeeds; PDFs clean.

If any gate fails: re-enter Phase 2 on the affected chunks. Stop only at convergence or when the exact remaining obstruction is named.

---

## Open problems anchoring Chapter 11

1. **Chiral $E_d$ Deligne conjecture at $d \geq 2$.** The centre identification is proved at $d = 1$ (Beilinson–Drinfeld, Costello–Gwilliam); $d \geq 2$ requires a chiral $E_d$ operad and a centre-of-module-category construction in the chiral setting.

2. **Hall–Drinfeld–Borcherds comparison spectral sequence on compact non-toric CY3.** The five-layer $K3 \times E$ structure $\kappa_{\mathrm{cat}} = 0$, $\kappa^{\mathrm{Hodge}}_{\mathrm{ch}} = 0$, $\kappa^{\mathrm{Heis}}_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$, $\kappa_{\mathrm{fiber}} = 24$ as the $E_2$ page; Hall–Borcherds comparison residuals as differentials; convergence to a single $\kappa$-invariant.

3. **Operator-level lift of the Igusa cusp form $\Phi_{10}$.** The candidate is the bulk module $C^\bullet_{\mathrm{ch}}(A_b, A_b)$ at the $K3 \times E$ HT theory's brane vacuum, twisted by the modular line bundle whose level-2 section is $\Delta_5 = \Phi_{10}^{1/2}$. The Hall–Borcherds comparison residual is the obstruction to this lift.

---

## The structural law

Every section answers one question, forced by what came before, in service of the single climax. Every theorem either constructs the local centre, identifies an obstruction, or computes an example. No sentence that fails to state mathematics or physics survives.

Begin.
