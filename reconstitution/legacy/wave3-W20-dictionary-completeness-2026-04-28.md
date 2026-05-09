# Wave 3 — W20 — Local-Dictionary Completeness Audit

**Auditor.** W20 of Wave 3.
**Lens.** Beilinson (sheaf-theoretic, exactness, descent, definition coverage) + Definitions (defined-before-use, stability under operations).
**Scope.** Coverage and consistency of `local-dictionary.tex` against the stable-core theorem statements (A, B, C₁, C₂, D, E, F, G) and their proof texts.
**Master-ledger ID prefix.** W3-W20-.
**Status.** Proposal-only. No source files modified.

---

## §0. Evidence base

Files read in full or scanned:

- `/Users/raeez/topological-strings/local-dictionary.tex` (210 lines)
- `/Users/raeez/topological-strings/notation.tex` (267 lines)
- `/Users/raeez/topological-strings/nomenclature.tex` (162 lines)
- `/Users/raeez/topological-strings/mathmacros.tex` (341 lines)
- `/Users/raeez/topological-strings/main.tex` (6358 lines, theorem-bearing windows read)
- `/Users/raeez/topological-strings/principles.tex` (228 lines)
- `/Users/raeez/topological-strings/theorem-lanes.tex` (full)
- `/Users/raeez/topological-strings/reconstitution/attack-heal-platonic-2026-04-28.md` (master ledger §B, §D)
- Selected scans of `tate-T1-weighted-completion.tex`, `tate-T2-nilpotent-truncation.tex`,
  `tate-T3-quillen-equivalence.tex`, `tate-P1-hadamard-mittag-leffler.tex`,
  `tate-P3-universality.tex`, `appendix-matlis-principal-parts.tex`.

**Grep yields, abbreviated.**

| Term | main.tex hits |
|---|---|
| `\bar A_{\mathrm{desc}}` | 8 |
| `\Psi_{a,b}` | 50 |
| `\rho_{a,b}` | 66 |
| `[\bar c]` / `bar c` | 25 |
| `\Theta_\rho` / `\Theta_{a,b}` | 39 |
| `Z^{P_0}_{\mathrm{fact}}` | 23 |
| `Capelli` | 44 |
| `Tate` | 76 |
| `B_f` | 31 |
| `\mathfrak h_I` | 23 |
| `\mathfrak g_I` | 11 |
| `\mathcal P_I` | 5 |
| `A_\partial^{\mathrm{Ham}}` | 23 |
| `A_\partial^{\mathrm{pp}}` | 2 |
| `coadjoint` | 69 |
| `HKR` | 3 |
| `admissible` | 4 (main); >40 in tate-* |
| `q^d` | 0 in main; 5 in tate-T1 |
| `Symp_{\mathrm{form}}` | 0 anywhere |
| `\Phi(c)`, `\Phi(u)` | 7 |
| `\widehat{\mathbf S}_{\mathrm{Tate}}` | 14 |

---

## §1. T1 — Dictionary inventory

`local-dictionary.tex` defines the following 19 terms. Line ranges are
inclusive of the table row (cell start to cell end).

| # | Term | Lines | One-sentence definition | Cross-refs |
|---|---|---|---|---|
| D1 | `R = ℂ[[z₁,z₂]]` | 17–19 | Complete local ring of the formal symplectic disk. | – |
| D2 | `𝔪 = (z₁,z₂)` | 20–22 | Maximal ideal of functions vanishing at the brane point. | – |
| D3 | `𝔥 = R/ℂ·1` | 23–25 | Reduced Hamiltonian Lie algebra of the formal disk; constants killed because they generate the zero Hamiltonian vector field. | – |
| D4 | `Ā = ℂ[z₁,z₂]/ℂ·1` | 27–29 | Polynomial Hamiltonian sector used in explicit trace and Moyal calculations. | – |
| D5 | `Ā_desc` | 31–33 | Abstract polynomial label space for PBW one-ψ descendants; not the Matlis principal-part module. | – |
| D6 | `[c̄]` | 36–39 | Distinguished scalar U(1) anomaly class in `H²_Lie(Ā,ℂ)`, realised by constant Taylor term of Poisson bracket and by Capelli shift. | (implicit) Capelli |
| **Separation rule** | – | 43–54 | Disjoint-blocks declaration for PBW / CE-PV / Matlis labels. | `thm:app-matlis-rees-fourier-bridge` |
| D7 | `H_{a,b} = z₁^a z₂^b` | 63–66 | Polynomial Hamiltonian label in `Ā`, `a+b>0`. | – |
| D8 | `O_{a,b}` | 68–70 | Open ghost-zero trace class `Tr̄(φ₁^a φ₂^b)`. | – |
| D9 | `Ψ_{a,b}` | 72–76 | Primitive one-ψ stable open class, symmetrised trace. | – |
| D10 | `𝖥_Rees` | 78–87 | Fourier–Rees label bridge of `thm:app-matlis-rees-fourier-bridge`; sends `z₁^a z₂^b` to `(-1)^{a+b}ℏ^{a+b}a!b! ρ_{a,b}` after inverting ℏ. | `thm:app-matlis-rees-fourier-bridge` |
| **Disjointness reminder** | – | 92–96 | Indices on `H_{a,b}/Ψ_{a,b}/ρ_{a,b}` are labels, not 𝔥-module identifications. | – |
| D11 | `𝔤 = 𝔥 ⋉ 𝔥^∨_cont[1]` | 105–107 | Shifted cotangent Lie algebra of Hamiltonian canonical transformations. | – |
| D12 | `H_I` | 109–110 | Hamiltonian generator in `𝔥`. | – |
| D13 | `c^I` | 112–114 | CE coordinate dual to a Hamiltonian generator; under `Φ`, `c^I ↦ θ^I`. | – |
| D14 | `u_I` | 116–119 | CE coordinate dual to the shifted cotangent generator; under `Φ`, `u_I ↦ O_I`. | – |
| D15 | `θ^I` | 121–123 | Polyvector coordinate corresponding to `c^I` under the CE/PV derived-centre isomorphism. | – |
| D16 | `O_I` | 125–127 | Hamiltonian observable coordinate corresponding to `u_I` under CE/PV. | – |
| D17 | `Φ` | 129–131 | Cochain-level CE/PV map determined on generators by `c^I↦θ^I`, `u_I↦O_I`. | – |
| D18 | `𝒫` | 143–147 | Reduced principal-part module `Ann(ℂ·1) ⊂ H²_𝔪(R) dz₁dz₂`, identified with `𝔥^∨_cont`. | – |
| D19 | `ρ_{a,b}` | 149–152 | Principal-part residue current `z₁^{-a-1} z₂^{-b-1} dz₁dz₂`, `a+b>0`, with Matlis coadjoint action. | – |
| D20 | `z₁^p z₂^q · ρ_{a,b}` | 154–157 | Coadjoint action `-(pb-qa+p-q)ρ_{a-p+1,b-q+1}`. | – |
| D21 | `𝒫_I` | 159–162 | `𝒫_I = 𝒟'_c(I) ⊗̂ 𝒫`, compactly supported distributional principal-part currents on `I`. | – |
| **Disjointness statement** | – | 167–174 | `Ψ_{a,b} ∈ PBW shadow; ρ_{a,b} ∈ 𝒫 ≅ 𝔥^∨_cont`. | – |
| D22 | `𝔥_I` | 183–187 | `𝔥_I = Ω^•_c(I) ⊗̂ 𝔥`, compactly supported de Rham Hamiltonian currents on `I`. | – |
| D23 | `𝔤_I` | 189–192 | `𝔤_I = 𝔥_I ⋉ 𝒫_I[1]`. | – |
| D24 | `B_f(a)` | 194–197 | Smeared boundary Hamiltonian observable `∫_I a(t) Tr̄ f(φ₁(t),φ₂(t)) dt`. | – |
| D25 | `A^Ham_∂(I)` | 199–201 | Reduced Hamiltonian brane-line `P₀` factorisation algebra `Ŝ(𝔥_I)`. | – |
| D26 | `A^pp_∂(I)` | 203–206 | Reduced post-contraction principal-part defect-current model `Ŝ(𝔥_I) ⊗̂ Ŝ(𝒫_I[1])`. | – |

26 numbered entries plus 3 unnumbered structural paragraphs (Separation
rule, Disjointness reminder, Disjointness statement). Coverage is
oriented around the brane-line `P₀` factorisation algebra and the
PBW / CE-PV / Matlis labelling separation. The dictionary is silent on
quantum / Moyal / Tate / weighted / Capelli-element terms; those flow
from the macro layer or are inscribed inline at theorem statements.

---

## §2. T2 — Theorem-term inventory (stable core)

The stable-core theorems per master ledger §D are:
A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W), C₂(R), D₁, D₂, D₃, E, F, G.
(Plus `lem:tate-mittag-leffler-dictionary`,
`thm:universal-categorical-no-go`.)

**Theorem A — Dirac brane probe** (`thm:lane-dirac-probe`, theorem-lanes.tex; proofs in `lem:dirac-probe-reduction`, `prop:open-bv-truncation`).

Load-bearing terms: `(Ĉ²)₀, dz₁∧dz₂`; `φ₁,φ₂,A ∈ 𝔤𝔩_N`; `S_∂` action; `Q ψ = [φ₁,φ₂]`; moment map `Tr(ε[φ₁,φ₂])`.

**Theorem B — Stable trace + one-ψ PBW shadow** (`thm:lane-stable-trace`).

Load-bearing terms: `Tr̄ f(φ₁,φ₂)`, `Ψ_{a,b}`, `ρ_{a,b}`, PBW special fibre, `𝔥`-coadjoint module, large-N stable connected.

**Theorem C₁ᶠʷ / C₁ᶜᵒᵐᵖ — Open-closed derived centre, cochain level** (`thm:open-closed-derived-center`, main.tex:2322).

Load-bearing terms: `𝔥`, `𝔤 = 𝔥 ⋉ 𝔥^∨_cont[1]`, `Ŝ_Tate(𝔥)`, `C^•_{CE,cont}(𝔤)`, `PV(A_∂)`, `Φ`, generator dictionary `c^I↦θ^I, u_I↦O_I`, `H_I`, `O_I`, Tate-conilpotency hypothesis.

**Theorem C₂(NT/W/R) — Tate-completed/nilpotent-truncated/regulator-independent extensions** (tate-T1, tate-T2, tate-P1).

Load-bearing terms: weight `w(d)=q^d`, `q>1`; `𝔪³`-truncation; admissible Mittag-Leffler envelope; `regulator-admissible-sector` definition; `lem:tate-mittag-leffler-dictionary`.

**Theorem D₁/D₂/D₃ — Matlis principal-part theorems** (`thm:canonical-residue-pairing`, `thm:principal-part-coadjoint-uniqueness`, `thm:no-polynomial-realization-categorical`, main.tex:3838–4187).

Load-bearing terms: `R, 𝔪`; `H²_𝔪(R) dz₁dz₂`; `𝒫 = Ann(ℂ·1)`; `ρ_{a,b}`; residue pairing, `δ_{a,b}`; `coadjoint action z₁^p z₂^q · ρ_{a,b}`; `𝔥^∨_cont`; "T²-Cartan rigidity" (renamed from "Schur"); local-cohomology / Matlis duality.

**Theorem E — Brane-line factorisation-current** (`thm:open-closed-derived-center-factorization`, main.tex:1996; `prop:reduced-principal-part-boundary-current`, main.tex:4240; `thm:hamiltonian-current-center-lift`, main.tex:2225).

Load-bearing terms: `𝔥_I, 𝔤_I, 𝒫_I, A^Ham_∂(I), A^pp_∂(I)`, `B_f(a)`, `u_{a(t)dt⊗f}`, `Z^{P_0}_{\mathrm{fact}}(A^Ham_∂)`, `Φ^Ham_fact`, locally-constant cosheaf, extension by zero, HKR.

**Theorem F — Reduced Moyal commutator at all N (conditional)** (`thm:finite-n-reduced-moyal`, main.tex:4903; `cor:degree-zero-quantum-upgrade`; `thm:phi-hbar-all-order`).

Load-bearing terms: Weyl algebra `𝒲_N`, normal-ordered comoment `μ̂`, `J_N(f)`, `Op_W(f)`, `Δ`, `S_N(f)`, radial-parts input, Capelli/Weyl normalisation, Moyal product `f * g`, Moyal bracket `{f,g}_ℏ`, `∂̄_{bb,ℏ}`, `H⁰_{Ham,conn}`.

**Theorem G — Scalar U(1)/Capelli anomaly** (`thm:u1-center-anomaly`, `thm:u1-center-anomaly-open`, `thm:quantum-classical-anomaly`, main.tex:318–449; `cor:local-bulk-boundary-coupling`).

Load-bearing terms: `[c̄] ∈ H²_Lie(Ā,ℂ)`, `ω` cocycle, `bar A_{[c̄]}`, central extension, Capelli relation `YX − XY + ℏN I ≡ 0`, U(1) centre of `𝔤𝔩_N`, Rees deformation `U_ℏ(Ā_{[c̄]})`, weight bidegree `(0,0)`.

---

## §3. T3 — Cross-map (theorem-term × dictionary status)

Legend.
**D** = defined in `local-dictionary.tex` (or `notation.tex`/`nomenclature.tex`).
**M** = TeX macro in `mathmacros.tex` only (no semantic content).
**U** = used in stable-core theorem without definition; or defined inline only.
**A** = defined but with two distinct usages elsewhere (ambiguity).

| Term | Status | Comment / W3-W20 ID |
|---|---|---|
| `R = ℂ[[z₁,z₂]]` | D (D1) | Clean. |
| `𝔪 = (z₁,z₂)` | D (D2) | Clean. |
| `𝔥 = R/ℂ·1` | D (D3) | Clean. |
| `Ā = ℂ[z₁,z₂]/ℂ·1` | D (D4) | Clean. |
| `Ā_desc` | D (D5) | Clean. Used main.tex:153, 3034, 3038, 3045, 3127, 3300, 3557, 4035, 4086 (8 hits). |
| `[c̄]` | D (D6) | Clean. The Capelli connection is asserted in the entry but not pointed at a labelled lemma; cross-link to `thm:quantum-classical-anomaly` would tighten. |
| `H_{a,b}` | D (D7) | Clean. |
| `O_{a,b}` | D (D8) | Clean. |
| `Ψ_{a,b}` | D (D9) | Clean; 50 main.tex hits all consistent with PBW special-fibre semantics. |
| `𝖥_Rees` | D (D10) | Defined; only 0 hits on `\mathsf F_{\mathrm{Rees}}` outside the dictionary itself. **W3-W20-12** dead-letter (used inline at `appendix-matlis-principal-parts.tex` but the dictionary symbol `𝖥_Rees` is not invoked). |
| `𝔤 = 𝔥 ⋉ 𝔥^∨_cont[1]` | D (D11) | Clean. |
| `H_I, c^I, u_I, θ^I, O_I` | D (D12–D16) | Clean; 7+ main.tex hits each. |
| `Φ` | D (D17) | Clean; 12 main.tex hits as the cochain-level map. |
| `𝒫` | D (D18) | Clean. |
| `ρ_{a,b}` | D (D19) | Clean; 66 main.tex hits. |
| `coadjoint action z₁^p z₂^q · ρ` | D (D20) | Clean. |
| `𝒫_I` | D (D21) | Clean. |
| `𝔥_I, 𝔤_I` | D (D22, D23) | Clean. |
| `B_f(a)` | D (D24) | Clean. |
| `A^Ham_∂(I)` | D (D25) | Clean. |
| `A^pp_∂(I)` | D (D26) | Clean. |
| **Quantum / Moyal terms** | | |
| `Ŝ_Tate(𝔥)` | U | Used 14× in main.tex (e.g. line 2329 "Tate-completed Kirillov–Poisson algebra"); only `Tate filtered envelope` mentioned obliquely in dictionary's separation rule via `thm:app-matlis-rees-fourier-bridge`. **W3-W20-01.** |
| Tate-conilpotency hypothesis | U | Cited from `lem:continuous-bar-cobar`; not in dictionary. The dictionary should at least point to it. **W3-W20-02.** |
| `weight w(d) = q^d`, `q > 1` | U | Defined inline at `tate-T1-weighted-completion.tex:127, 149, 156, 169, 434`; not in `local-dictionary.tex`. C₂(W) statement of master ledger §D depends on it. **W3-W20-03.** |
| `regulator-admissible-sector` | U | Defined inline at `tate-P1-hadamard-mittag-leffler.tex` (`defn:regulator-admissible-sector`); not in `local-dictionary.tex`. C₂(R) depends on it. **W3-W20-04.** |
| `Symp_form(C²,0)` | U | Master ledger M-05/M-28/M-35 "Symp-functoriality" obligation. **`Symp_{\mathrm{form}}` has 0 hits anywhere in the repo**; only `formal symplectomorphism` (main.tex:847, 873) and `tate-P3-universality.tex:55`. The Theorem D₁ claim that `Φ_coad` is `Symp_{\mathrm{form}}`-equivariant has no symbol in the dictionary. **W3-W20-05** (severity 3). |
| Capelli element / Capelli/Weyl normalisation | U | 44 main.tex hits; never defined in `local-dictionary.tex` though it is the engine of Theorems F and G. Inline citations to `\cites{capelli,howe-capelli}`. **W3-W20-06.** |
| Matlis principal-parts / Matlis duality | partial D (D18) | `𝒫` is defined; but the term "Matlis duality" / `injective hull E_R(ℂ)` is referenced in `rmk:residue-pairing-schur` (main.tex:3919) and `appendix-matlis-principal-parts.tex` without a dictionary entry pointing at the underlying duality theorem. **W3-W20-07.** |
| `ρ_{a,b}` as Matlis coordinate | D (D19) | Clean. |
| `Ψ_{a,b}` PBW symbol | D (D9) | Clean. |
| coadjoint action (general 𝔥-module) | D (D20) | Clean for `ρ_{a,b}`; the `Ψ_{a,b}` PBW raising action is *not* in the dictionary, only stated inline at `thm:pbw-vs-deformation`. **W3-W20-08.** |
| `Z^{P_0}_{\mathrm{fact}}` | U | 23 main.tex hits; no dictionary entry. The local convention is stated at main.tex:2212–2220, but the symbol does not appear in `local-dictionary.tex`. Master ledger M-08 confirms this is intentionally a *local* definition; the dictionary should still record it. **W3-W20-09** (severity 3). |
| HKR | U | 3 main.tex hits (Step 1 of `thm:open-closed-derived-center-factorization`); no entry. M-33 W6-02 flags HKR survival in the factorisation theorem. **W3-W20-10.** |
| PV (polyvectors) | U | Heavy use in C₁ statement; no dictionary entry. Defined inline at `lem:linear-poisson-schouten`. **W3-W20-11.** |
| CE (Chevalley–Eilenberg) | U/D-by-context | Spelled out in entries D13–D17 but the abbreviation "CE" itself never expanded in the dictionary. Acceptable, but consider one-line gloss. **W3-W20-13** (low severity). |
| `Tr̄`, scalar-reduced trace | U | Used in D8 (`O_{a,b}` definition) without standalone entry for `Tr̄`. Master ledger M-15 / W6-06 flags the "primitive indecomposable" rename; the bar-trace operator itself is not symbolically isolated in the dictionary. **W3-W20-14.** |
| `\mathfrak{gl}_N`, `Tr`, `(φ₁,φ₂)` matrix probes | U | Used throughout Theorems A, F, G; expected default of mathematical-physics readership. Acceptable absence; could be moved into a "matrix probe" sub-block. **W3-W20-15** (low severity). |
| `T²-Cartan rigidity` | U | Renamed concept (M-06); appears 11× per W2-03 audit. No dictionary entry; only inline near Theorem D₂. **W3-W20-16.** |
| `[\bar c]` ↔ `Tr ψ`-class identification | partial D (D6) | M-31 W3-03 supplies the cohomological identification; the dictionary entry mentions Capelli but not `[Tr ψ]_{BV}`. **W3-W20-17.** |

---

## §4. T4 — Unused dictionary entries

For each dictionary entry, count main.tex usages plus apparatus.

| Entry | main.tex hits | Apparatus hits | Status |
|---|---|---|---|
| D1 `R` | many (≥30 inline) | yes | active |
| D2 `𝔪` | many | yes | active |
| D3 `𝔥` | dominant; appears in nearly every theorem | yes | active |
| D4 `Ā` | 113 | yes | active |
| D5 `Ā_desc` | 8 | yes | active |
| D6 `[c̄]` | 25 | yes | active |
| D7 `H_{a,b}` | 4+ | yes | active |
| D8 `O_{a,b}` | several | yes | active |
| D9 `Ψ_{a,b}` | 50 | yes | active |
| D10 `𝖥_Rees` | **0 outside dictionary** | 0 | **dead letter** ⇒ **W3-W20-12.** Used by name only inside the dictionary. The Fourier–Rees bridge theorem (`thm:app-matlis-rees-fourier-bridge`) does not invoke the symbol `\mathsf F_{\mathrm{Rees}}`. Either delete the symbol (replacing with descriptive phrase) or import the symbol into the appendix theorem statement. |
| D11 `𝔤` | many | yes | active |
| D12–D17 generators | each many | yes | active |
| D18 `𝒫` | many | yes | active |
| D19 `ρ_{a,b}` | 66 | yes | active |
| D20 coadjoint formula | 1+ direct (lots inline restatement) | yes | active |
| D21 `𝒫_I` | 5 | yes | active |
| D22 `𝔥_I` | 23 | yes | active |
| D23 `𝔤_I` | 11 | yes | active |
| D24 `B_f(a)` | 31 | yes | active |
| D25 `A^Ham_∂(I)` | 23 | yes | active |
| D26 `A^pp_∂(I)` | 2 | yes | active (sparse) |

**Dead/abandoned entries.** D10 (`𝖥_Rees`) is the only dead letter:
the symbol is unused outside `local-dictionary.tex` itself.

**Sparse-usage flag.** D26 (`A^pp_∂(I)`) appears only at main.tex:1942
and 1960; given how much load this object carries (Theorem E
post-contraction defect-current model), the relative scarcity is
because the model uses
`Obs_{∂,N}^{cl,pp}(I) = Obs_{open,N}^{cl,red}(I) ⊗̂ Ŝ(𝔍_∂^{pp}(I))`
in `prop:reduced-principal-part-boundary-current` (main.tex:4240–4296)
without ever calling it `A^pp_∂(I)`. **W3-W20-18.** Reconcile or drop.

---

## §5. T5 — Convention drift internal

Within `local-dictionary.tex` itself the conventions are internally
consistent on the major points:

- **Shift convention.** `𝔥^∨_cont[1]` (lines 23, 105, 192) consistent
  throughout. Master-ledger M-07 (P-03) flags an external `[+1]/[-1]`
  drift in `main.tex` between 2206 and 3449; the dictionary itself
  uses `[1]` uniformly — no internal drift. **W3-W20-19** for
  external sign-firmware audit (out of scope for this task; flag
  to `wave1` / M-07 owner).

- **Sign of coadjoint formula.** `-(pb − qa + p − q) ρ_{a-p+1,b-q+1}`
  appears in D20 (line 156) consistent with `prop:principal-part-coadjoint`
  and `thm:principal-part-coadjoint-uniqueness` (main.tex:3944–3946).
  Clean.

- **Scalar quotient.** `Ā = ℂ[z₁,z₂]/ℂ·1` and `𝔥 = R/ℂ·1` are split
  between polynomial and completed lines correctly. Dictionary
  D3 says "Reduced Hamiltonian Lie algebra of the formal disk" and
  D4 says "Polynomial Hamiltonian sector"; the inclusion `Ā ⊂ 𝔥`
  (after completion) is not drawn explicitly. Acceptable, but
  `principles.tex:77` (`𝔥 = ℂ[[z₁,z₂]]/ℂ·1`) and
  main.tex:2308 (`𝔥 = (z₁,z₂)ℂ[[z₁,z₂]]`) give two equivalent
  characterizations; the dictionary entry could note the second.
  **W3-W20-20** (low severity).

- **Continuous dual.** `𝔥^∨_cont` is used in D11, D18 with the
  understanding from the Matlis identification. The dictionary
  entry D18 explicitly identifies `𝒫 ≅ 𝔥^∨_cont`; the `[1]` shift
  is split off into D11 (`𝔥^∨_cont[1]`) without contradiction.

- **PBW vs Matlis separation.** The "Separation rule" paragraph
  (lines 43–54) and the disjointness statement (167–174) explicitly
  forbid identifying `Ψ_{a,b}` with `ρ_{a,b}` as 𝔥-modules. This is
  the load-bearing convention M-29 / W4-06; consistent and
  authoritative.

**Minor internal-consistency concern.** D20 lists the coadjoint
action of `z₁^p z₂^q ∈ Ā` (a polynomial Hamiltonian) on `ρ_{a,b}`
without specifying the projection `π_{pp}` for negative-index
results. main.tex:3960 supplies the `π_{pp}` projection convention.
**W3-W20-21** (low severity): add "negative-index target = 0 by
principal-part projection" as a parenthetical.

---

## §6. T6 — Critical-terms audit

The W1–W17 reports cite the following load-bearing terms heavily.
Status against `local-dictionary.tex`:

| Term | Dictionary status | Severity | W3-W20 ID |
|---|---|---|---|
| `Z^{P_0}_{\mathrm{fact}}` (derived Poisson factorisation centre) | **U** | 3 | W3-W20-09 |
| `𝔥` (Hamiltonian Lie algebra) | **D** (D3) | – | clean |
| `𝔥^∨_cont[1]` | **D** (D11, D18) | – | clean (split between two entries; consistent) |
| `PV` (polyvectors) | **U** (only inline at main.tex:2336, 2434) | 2 | W3-W20-11 |
| `CE` (Chevalley–Eilenberg) | **D-by-context** (D13–D17 reference; abbrev never expanded) | 1 | W3-W20-13 |
| `HKR` | **U** (3 inline hits) | 2 | W3-W20-10 |
| `Tate (filtered envelope)` | **U** in dictionary; defined inline at `tate-T3:46 stmt:tate-model-envelope` | 3 | W3-W20-01 |
| `weight w(d) = q^d` | **U** (defined inline at tate-T1:127, 149, 156) | 3 | W3-W20-03 |
| `regulator-admissible-sector` | **U** (`defn:regulator-admissible-sector` in tate-P1) | 2 | W3-W20-04 |
| `Symp_form(C²,0)` | **U** (NO symbol anywhere; "formal symplectomorphism" prose only) | 3 | W3-W20-05 |
| Capelli element | **U** (44 inline hits) | 3 | W3-W20-06 |
| Matlis principal-parts `𝒫` | **D** (D18) | – | clean |
| `ρ_{a,b}` (Matlis coordinate) | **D** (D19) | – | clean |
| `Ψ_{a,b}` (PBW symbol) | **D** (D9) | – | clean |
| coadjoint action (general) | **partial D** (D20 for `ρ`-side only) | 2 | W3-W20-08 |
| "main local theorem" label | – (it is a `\begin{cor}` not a `\begin{thm}`) | – | clean per W17; the dictionary doesn't label the corollary. **W3-W20-22**: optionally add the dictionary line "`thm:main-local` is a *summary corollary*, not a theorem; see `rmk:dirac-thesis`." |

**Scoring.** 7 of 14 critical terms are undefined or under-defined in
the dictionary. None of the seven is a *false* definition; each is
defined inline at the load-bearing theorem. The dictionary is
*incomplete* but not *inconsistent*.

---

## §7. T7 — Proposed heals (one-line dictionary entries)

Each heal proposed as a single dictionary table row, ordered by
severity / blast radius. Proposal-only.

**P-W3-W20-01** (W3-W20-01). Add after D11:
> `Ŝ_Tate(𝔥)` &nbsp; Tate-completed symmetric algebra of `𝔥`, defined
> as the completion in the admissible Tate model envelope of
> `stmt:tate-model-envelope`; coincides with the projective limit
> over the m-adic filtration.

**P-W3-W20-02** (W3-W20-02). Add as a footnote after D11:
> *Tate-conilpotency hypothesis.* All bar-cobar appeals run through
> `lem:continuous-bar-cobar`. The hypothesis is `𝔤 ∈ TateVec` is
> conilpotent in the admissible envelope.

**P-W3-W20-03** (W3-W20-03). Add new block after Matlis labels:
> **Weighted Tate envelope.** `w(d)=q^d`, `q>1`: exponential
> degree weight defining Theorem C₂(W); ledger `tate-T1`.

**P-W3-W20-04** (W3-W20-04). Same block:
> `regulator-admissible-sector`: the open subset of admissible
> exponential weights and Hadamard regulators on which Theorem C₂(R)
> is regulator-independent; defined at
> `defn:regulator-admissible-sector`.

**P-W3-W20-05** (W3-W20-05). Add after D11:
> `Symp_form(C²,0)`: formal-symplectomorphism group of the formal
> disk; acts on 𝔥 by the natural action and on `𝒫 ≅ 𝔥^∨_cont`
> through the residue pairing.  Theorem D₁ is `Symp_form`-equivariant
> (M-28, M-35).

**P-W3-W20-06** (W3-W20-06). New "Quantum reduction labels" block:
> *Capelli element.* `c_C := YX − XY + ℏN I ∈ 𝒲_N`. Vanishes in
> the degree-zero quantum Hamiltonian reduction; its leading
> ℏ-coefficient is the U(1) anomaly class `[c̄]` (Theorems G,
> `thm:quantum-classical-anomaly`).

**P-W3-W20-07** (W3-W20-07). One-liner:
> *Matlis duality.* The duality `R ↔ E_R(ℂ) = H²_𝔪(R) dz₁dz₂`
> of `\cite{matlis-injective}`; restricted to `𝒫` after annihilating
> the scalar Hamiltonian.

**P-W3-W20-08** (W3-W20-08). Append a row after D9:
> *PBW raising action.* `F_{p,q} : Ψ̃_{a,b} ↦ (pb-qa) Ψ̃_{a+p-1,b+q-1}`.
> This is the `Ā`-action on `Ā_desc`, distinct from the coadjoint
> lowering D20.

**P-W3-W20-09** (W3-W20-09). New block "Factorisation centre":
> `Z^{P_0}_{\mathrm{fact}}(A)` *(local convention).* For a
> graded-commutative `P_0` factorisation algebra `A`, the
> factorisation algebra of `E_1` central operations equipped with
> the Poisson/BV homotopies; in the locally constant 1-d case its
> stalk is the Hochschild cochain complex. See main.tex:2212–2220.
> **No** unrestricted Costello–Gwilliam centrality is imported.

**P-W3-W20-10** (W3-W20-10). Append to factorisation block:
> *HKR (Hochschild–Kostant–Rosenberg).* For free graded-commutative
> algebras on a Tate vector space, the HKR identification
> `Hoch^•(Ŝ(𝔥_I)) ≃ PV^•(Ŝ(𝔥_I))` of main.tex:2056–2064
> (Step 1 of `thm:open-closed-derived-center-factorization`).

**P-W3-W20-11** (W3-W20-11). Append:
> `PV(A_∂)` := `Ŝ(𝔥) ⊗̂ Ŝ(𝔥^∨_cont[-1])` with Schouten bracket.
> This is the polyvector-fields complex on the formal symplectic
> disk used in Theorem C₁.

**P-W3-W20-12** (W3-W20-12). Either remove the `𝖥_Rees` symbol from
D10 (replacing with descriptive prose) or import `\mathsf F_{Rees}`
into `appendix-matlis-principal-parts.tex` so the symbol earns its
keep.

**P-W3-W20-13** (W3-W20-13). Optional gloss in section header:
> *CE = Chevalley–Eilenberg; PV = polyvector fields; HKR =
> Hochschild–Kostant–Rosenberg; BV = Batalin–Vilkovisky.*

**P-W3-W20-14** (W3-W20-14). Add to PBW block:
> `Tr̄ f(φ₁,φ₂) := Tr(f) mod ℂ·Tr(1)`: scalar-reduced trace,
> primitive-connected single-trace projection.

**P-W3-W20-16** (W3-W20-16). Add after D19:
> *T²-Cartan rigidity.* The bigraded total-degree-zero
> 𝔥-equivariance constraint forcing the residue pairing to be
> unique up to a scalar; see Theorem D₂ and `rmk:residue-pairing-schur`.
> Replaces the deprecated "Schur rigidity" interpretation (master ledger
> M-06).

**P-W3-W20-17** (W3-W20-17). Extend D6:
> Cohomologically equal to `[Tr ψ]_BV` under the chain-level
> identification of M-31 / W3-03.

**P-W3-W20-18** (W3-W20-18). Either retire D26 in favour of
`Obs_{∂,N}^{cl,pp}(I)` (used at main.tex:4251) or harmonise.

**P-W3-W20-21** (W3-W20-21). Append a `*` to D20:
> *Negative-index targets are zero, by principal-part projection
> `π_{pp}`* (main.tex:3960).

**P-W3-W20-22** (W3-W20-22). Optional terminal line:
> `thm:main-local` is a summary *corollary* (`\begin{cor}`),
> not a primary theorem; see `rmk:dirac-thesis`.

---

## §8. Verdict and convergence note

`local-dictionary.tex` is *internally consistent and authoritative*
on the PBW / CE-PV / Matlis label separation that drives Theorems
B, C₁, D₁, D₂, D₃, E. Its principal **incompleteness** is in three
domains:

1. **Tate / weighted / admissible** vocabulary used by C₂(NT),
   C₂(W), C₂(R) is defined entirely outside the dictionary. Heals
   P-W3-W20-01 through -04.
2. **Quantum / Moyal / Capelli** vocabulary used by Theorems F, G
   is defined inline; the dictionary is silent. Heals P-W3-W20-06.
3. **Factorisation-centre / HKR / PV** used by Theorem E and C₁ are
   inline-only. Heals P-W3-W20-09, -10, -11.

**Dead letter.** D10 (`𝖥_Rees`) is the only entry without external
usage. Either retire or wire into the appendix.

**Symp_form gap** (P-W3-W20-05) is the highest-severity finding:
the symbol is invoked nowhere in the manuscript even though
master ledger §D claims Theorem D₁ is `Symp_form`-canonical and
Theorems A, B, G are `Symp_form`-equivariant. This is *consistent
with* the master ledger only if one accepts "formal symplectomorphism"
in prose as the operational meaning. Proposal-grade fix is to
inscribe the symbol once in the dictionary and once at Theorem D₁.

**No fatal incompleteness found.** All gaps are `definition-not-yet-
imported` items, not contradictions. The dictionary as it stands
*does* support the stable-core proofs once readers chase inline
definitions; the dictionary's job per Beilinson lens
(definition-coverage, sheafy descent of conventions across
theorems) is partially fulfilled.

---

## §9. Inscription guidance for downstream waves

For Phase-1 dictionary expansion, the proposed ordering by minimal
edit cost is:

- **Tier-A (single-row table additions).** P-W3-W20-01, -02, -03,
  -04, -06, -09, -10, -11, -16. Each is a one-line entry; total
  edit budget ≈ 9 rows.
- **Tier-B (single-line modifiers).** P-W3-W20-08, -14, -17, -21,
  -22. Budget ≈ 5 lines.
- **Tier-C (decisions).** P-W3-W20-05 requires deciding whether to
  inscribe `Symp_form` as a symbol; P-W3-W20-12 requires deciding
  whether `𝖥_Rees` stays.

After Tier-A inscription, the dictionary covers all stable-core
theorems' load-bearing vocabulary. Tier-B sharpens existing entries;
Tier-C resolves the two structural decisions (Symp symbol; F_Rees
fate).

**Cross-attacker confirmations expected.**
- W2 (Drinfeld functoriality) cross-confirms Symp_form gap (M-28, M-35).
- W4 (Etingof / categorical no-go) cross-confirms PBW/Matlis
  separation as authoritative (D9 + D19 + master ledger M-29).
- W6 (Beilinson composition) cross-confirms HKR usage in Theorem E
  Step 1 (master ledger M-33 W6-02).

End of W3-W20 dictionary-completeness audit.

---

## §10. 200-word summary

`local-dictionary.tex` defines 26 numbered terms organised into
six blocks: local rings, PBW special-fibre labels, CE/PV labels,
Matlis principal-part labels, interval-current labels, and two
disjointness statements protecting the PBW / Matlis separation.
The dictionary is **internally consistent**: signs, shifts, and
the 𝒫-vs-Ψ separation are uniform; no convention drift detected.
Coverage of stable-core theorems A, B, D₁, D₂, D₃, E is **complete**
modulo seven inline-only critical terms that should migrate into
the dictionary: `Ŝ_Tate(𝔥)`, `Z^{P_0}_{\mathrm{fact}}`, `PV`, `HKR`,
Capelli element, weight `w(d)=q^d`, and `regulator-admissible-sector`
(severities 2–3). One symbol, `𝖥_Rees`, is a **dead letter** —
defined in the dictionary but never invoked outside it. One term,
`Symp_form(C²,0)`, has **zero symbol presence** in the entire
manuscript despite master-ledger claims of `Symp_form`-equivariance
on Theorems A, B, D, G. Theorems C₂(NT/W/R), F, G depend on
quantum/Tate/weighted vocabulary that is not in the dictionary;
heals P-W3-W20-01 through -11 supply nine single-row additions
that close the gaps without rewriting any proof. No fatal
incompleteness. Proposal-only; no source files modified. ID prefix
W3-W20-.
