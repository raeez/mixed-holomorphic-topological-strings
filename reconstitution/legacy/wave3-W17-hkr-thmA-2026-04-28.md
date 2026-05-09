# Wave 3 — W17 — HKR audit and Theorem A foundations

**Wave/worker.** Wave 3, W17.
**Date.** 2026-04-28.
**Lens.** Primary: Costello (factorization algebras, BV/BRST, perturbative
QFT, PV side). Secondary: Hypotheses (which theorem hypotheses are
missing, weakened, or silently strengthened).
**Brief.** Audit every HKR invocation in the manuscript against its
named primary source; verify Theorem A (CE/PV cotangent identity)
hypothesis-by-hypothesis under the Costello + Hypotheses lens; cross-
check shift conventions; propose minimal one-sentence heals.

Master ledger schema. New IDs in this report use prefix `W3-W17-`.
Provenance hooks: M-01 (HKR-Tate folklore at `main.tex`:2202, 2132),
W6-02 (HKR survives in factorization theorem, `main.tex`:2050–2076),
W3-W11-03 (PV/CE coherence; recorded in
`reconstitution/wave3-W11-beilinson-hypotheses-2026-04-28.md`).

---

## §0. Top-line findings

1. **HKR has no bibliography entry.** The strings `Hochschild-Kostant-
   Rosenberg`, `HKR`, and `hkr` appear in the prose at four sites
   (lines 2056, 2132, 2202, and one E_1 stalk reference in the same
   vicinity), but there is no `\bib{hkr}{...}` or `\bib{hochschild-...}`
   entry anywhere in `main.tex` lines 5926–6420. The two appeals are
   pinned only to "the smooth/algebraic setting" prose. This is a
   load-bearing primary source citation gap. (M-01 already records
   the gap; W17 confirms the status post-Phase-4.)

2. **HKR is invoked in a non-classical setting.** The classical
   theorem (Hochschild–Kostant–Rosenberg, *Trans. AMS* 102 (1962),
   383–408, **Theorem 5.2**) identifies, for a smooth commutative
   `k`-algebra `A` over a field `k` of characteristic zero,
   `HH^\bullet(A) \cong \Lambda^\bullet_A \mathrm{Der}_k(A) =
   \mathrm{PV}^\bullet(A)`. The manuscript invokes this for the **free
   completed graded-commutative algebra on a Tate vector space**
   `\widehat{\mathbf S}(\mathfrak h_I)` with `\mathfrak h_I =
   \Omega^\bullet_c(I) \widehat\otimes \mathfrak h`. This is **not the
   classical setting**: `\widehat{\mathbf S}(\mathfrak h_I)` is not a
   finitely generated smooth `k`-algebra, and the classical proof of
   HKR (antisymmetrization map, Connes B operator, Eulerian
   idempotents) does not literally apply. The manuscript silently
   transfers the classical statement.

3. **Theorem A's stated form is a Corollary, not a Theorem.** The
   labelled statement is `\begin{cor}[Main local summary
   corollary]\label{thm:main-local}` at `main.tex`:1164. Its proof
   (line 1194) reads: "This is a summary corollary, not a second
   proof. The listed theorem lanes give the proof dependencies and
   local hypotheses." The cochain-level CE/PV identity that "Theorem A"
   names in the brief is in fact Theorem
   `\thm:open-closed-derived-center` at `main.tex`:2322–2349, with
   stable formal-disk specialization at
   `\cor:derived-center-formal-disk` lines 2465–2494.

4. **Step 1 of `\thm:open-closed-derived-center-factorization`
   (Theorem E) still invokes HKR.** Lines 2050–2076. This is the
   W6-02 finding from Wave 2; W17 confirms it remains in the
   manuscript at the time of audit (the M-01 minimal heal proposed
   excision but the heal is not yet inscribed at `main.tex`:2056).

5. **`\thm:open-closed-derived-center` (the cochain-level CE/PV
   theorem) does NOT use HKR in its proof.** The proof on lines
   2351–2438 is generator-level Leibniz extension via
   `\lem:linear-poisson-schouten` and `\lem:continuous-bar-cobar`. HKR
   appears only as a remark (`\rmk:E1-translation` line 2202) and in
   the factorization upgrade (Theorem E Step 1). The classical CE/PV
   theorem of `\thm:open-closed-derived-center` is therefore
   independent of the HKR appeal at the cochain level — but it does
   require Tate-conilpotency (`\lem:continuous-bar-cobar`), which
   M-01 demonstrates fails for the perfect formal disk Hamiltonian
   algebra.

6. **The shift convention `\mathfrak h^\vee_{\mathrm{cont}}[1]` is
   used uniformly throughout the manuscript** (see §T5 below).

---

## §T1. Enumeration: every HKR / Hochschild / Kostant / Rosenberg invocation

### Grep output (verbatim)

```
$ grep -rn "HKR\|Hochschild\|Kostant\|Rosenberg" /Users/raeez/topological-strings/main.tex
/Users/raeez/topological-strings/main.tex:2056:  Hochschild--Kostant--Rosenberg theorem in the smooth/algebraic
/Users/raeez/topological-strings/main.tex:2058:  Tate vector space $\mathfrak h_I$, the Hochschild cochain complex
/Users/raeez/topological-strings/main.tex:2066:  Hochschild cochains in the corresponding $E_1$ algebra; for
/Users/raeez/topological-strings/main.tex:2110:  (Hochschild $0$-cocycle on the graded-commutative open stalk).
/Users/raeez/topological-strings/main.tex:2132:  (closed side: by definition; brane side: through the HKR
/Users/raeez/topological-strings/main.tex:2198:  algebras \cite{costello-gwilliam}*{Vol.~I \S 6.4}. The Hochschild cochain complex of
/Users/raeez/topological-strings/main.tex:2201:  is, in the reduced model), the Hochschild cochain complex is
/Users/raeez/topological-strings/main.tex:2202:  quasi-isomorphic to polyvector fields by HKR, and its strict $P_0$
/Users/raeez/topological-strings/main.tex:2215:the Hochschild cochain complex of the corresponding $E_1$ algebra. The notation
/Users/raeez/topological-strings/main.tex:2232:  is a Hochschild $0$-cocycle in $\mathrm Z_{\mathrm{fact}}
/Users/raeez/topological-strings/main.tex:2249:  multiplication by this closed element is a Hochschild $0$-cocycle;
/Users/raeez/topological-strings/main.tex:2461:  Equivalently, this is the standard Kirillov--Kostant--Souriau theorem
/Users/raeez/topological-strings/main.tex:3094:  Then $QB_f=0$. Regard $B_f$ as a Hochschild $0$-cochain; its associated
/Users/raeez/topological-strings/main.tex:3098:  This Hochschild $0$-cochain is closed. The same statement holds for
/Users/raeez/topological-strings/main.tex:3106:  $A_N^{\mathrm{pt}}$ is graded-commutative, so the Hochschild differential of
/Users/raeez/topological-strings/main.tex:3444:  Poisson algebra with Kirillov--Kostant--Souriau bracket
/Users/raeez/topological-strings/main.tex:4375:  projection, or Hochschild centrality homotopies against arbitrary open
/Users/raeez/topological-strings/main.tex:5954:   title={The homology of matrix Lie algebras over rings and the Hochschild homology},
```

`grep -rln HKR\|Hochschild\|Kostant\|Rosenberg /Users/raeez/topological-strings/*.tex` returns only `main.tex`. The Tate-T files (T1–T5), appendices, `theorem-lanes.tex`, `local-dictionary.tex`, `claim-strength-ledger.tex`, `notation.tex`, and `principles.tex` contain no HKR text.

### Tabulation

| # | File:line | Block | Context (1-2 sentences) | What is claimed |
|---|-----------|-------|-------------------------|------------------|
| 1 | `main.tex`:2056 | proof of `\thm:open-closed-derived-center-factorization` Step 1 | "By the Hochschild--Kostant--Rosenberg theorem in the smooth/algebraic setting, applied here to the free graded-commutative algebra on the Tate vector space `\mathfrak h_I`, the Hochschild cochain complex `\mathrm{Hoch}^\bullet(\widehat{\mathbf S}(\mathfrak h_I))` is quasi-isomorphic to the polyvector fields..." | Quasi-iso `\mathrm{Hoch}^\bullet \simeq \mathrm{PV}^\bullet` for `\widehat{\mathbf S}(\mathfrak h_I)` with Schouten bracket. **Generalization** to Tate completed sym-algebra. |
| 2 | `main.tex`:2058 | same proof, Step 1 | "Tate vector space `\mathfrak h_I`, the Hochschild cochain complex..." | Continuation of #1; `\mathfrak h_I = \Omega^\bullet_c(I) \widehat\otimes \mathfrak h` is the cosheaf-of-Lie evaluation. |
| 3 | `main.tex`:2066 | same proof, Step 1 | "...records exactly the Hochschild cochains in the corresponding `E_1` algebra; for graded-commutative algebras this collapses to PV." | Implicit: HKR's PV statement is the locally-constant `E_1` factorization centre. **Silent specialization** to the graded-commutative `E_1` case where the appropriate result is Lurie HA Thm 5.5.3.18 / Costello-Gwilliam Vol II §3 stalk argument. |
| 4 | `main.tex`:2110 | Step 3 of same proof | "(Hochschild `0`-cocycle on the graded-commutative open stalk)." | Degree-0 Hochschild closure of `B_f`; this is **not** the HKR theorem itself, only the centrality of `0`-cochains in a graded-commutative algebra (a tautology). |
| 5 | `main.tex`:2132 | Step 5 of same proof | "...with the same CE differential induced from the semidirect Lie bracket of `\mathfrak g_I` (closed side: by definition; brane side: through the HKR identification of Step 1 and the Schouten bracket)." | The brane side uses #1's HKR identification to read off the PV/Schouten differential. **Identical claim to #1**; same source needed. |
| 6 | `main.tex`:2198 | `\rmk:E1-translation` | "...factorization algebras are equivalent to homotopy associative algebras up to translation invariance by Lurie, *Higher Algebra*, §5.5.4, in the Costello-Gwilliam vocabulary of locally constant factorization algebras... The Hochschild cochain complex of the `E_1` algebra computes the factorization-center stalk." | Lurie HA Thm 5.5.3.18 (this **is** properly cited). Subsequent line 2202 then invokes HKR. |
| 7 | `main.tex`:2201–2202 | same remark | "...graded-commutative `E_1` algebras (which the open Hamiltonian stalk is, in the reduced model), the Hochschild cochain complex is quasi-isomorphic to polyvector fields by HKR..." | The HKR appeal proper. **Same as #1** but in remark form. No primary source cited. |
| 8 | `main.tex`:2215 | running text | "...the Hochschild cochain complex of the corresponding `E_1` algebra." | Restatement of #6; properly invokes Lurie HA, no HKR. |
| 9 | `main.tex`:2232 | `\thm:hamiltonian-current-center-lift` | "is a Hochschild `0`-cocycle in `\mathrm Z_{\mathrm{fact}}(\dots)(I)`" | Centrality of `0`-cochain in a graded-commutative algebra, not HKR. |
| 10 | `main.tex`:2249 | proof of #9 | "multiplication by this closed element is a Hochschild `0`-cocycle" | Same as #4, #9. Tautology. |
| 11 | `main.tex`:2461 | proof of `\cor:moment-map-shadow` | "the standard Kirillov-Kostant-Souriau theorem for linear Poisson structures" | Kirillov–Kostant–Souriau theorem (different theorem entirely; correctly invoked for linear Poisson on the dual of a Lie algebra). **Not HKR.** |
| 12 | `main.tex`:3094 | `\prop:stalk-central-multiplication` | "Regard `B_f` as a Hochschild `0`-cochain; its associated central operation is multiplication." | Hochschild `0`-cochain, not HKR. |
| 13 | `main.tex`:3098 | same | "This Hochschild `0`-cochain is closed." | Same. |
| 14 | `main.tex`:3106 | proof of #12 | "`A_N^{\mathrm{pt}}` is graded-commutative, so the Hochschild differential of a `0`-cochain `b` is..." | Tautological Hochschild centrality; not HKR. |
| 15 | `main.tex`:3444 | `\lem:linear-poisson-schouten` | "Poisson algebra with Kirillov-Kostant-Souriau bracket..." | Kirillov–Kostant–Souriau, not HKR. |
| 16 | `main.tex`:4375 | `\rmk:reduced-status-principal-part-currents` | "Hochschild centrality homotopies against arbitrary open observables." | Hochschild centrality (not HKR), explicitly listed as not yet provided. |
| 17 | `main.tex`:5954 | bibliography entry `tsygan` | "The homology of matrix Lie algebras over rings and the Hochschild homology" | Tsygan 1983 paper title; bibliographic, not a citation of HKR. |

**Summary.** The genuine HKR appeals are entries 1, 5, and 7
(`main.tex`:2056, 2132, 2202). Entries 3 and 6 cite Lurie HA and
implicitly assume HKR's PV statement. Entries 2, 4, 8–10, 12–14, 16
are routine Hochschild language not invoking HKR. Entries 11 and 15
invoke Kirillov–Kostant–Souriau (a different theorem). Entry 17 is a
bibliography entry.

---

## §T2. Verification of each HKR invocation against named primary sources

### Available HKR variants (with primary-source theorem numbers)

| Variant | Source | Theorem | Hypothesis |
|---------|--------|---------|------------|
| **HKR-classical** | Hochschild, Kostant, Rosenberg, "Differential forms on regular affine algebras," *Trans. AMS* 102 (1962), 383–408 | **Thm 5.2** (and the algebraic Thm 3.4.4 in modern expositions e.g. Loday *Cyclic Homology* §3.4) | `A` is a smooth commutative `k`-algebra essentially of finite type over a field `k` of characteristic 0; then the antisymmetrization map gives `HH_n(A,A) \cong \Omega^n_{A/k}` (homology) / `HH^n(A,A) \cong \mathrm{PV}^n(A) = \Lambda^n_A \mathrm{Der}_k(A)` (cohomology). Smoothness and finite type are both load-bearing. |
| **HKR-Kontsevich (formality)** | Kontsevich, "Deformation quantization of Poisson manifolds," *Lett. Math. Phys.* 66 (2003), 157–216 (= `\cite{kontsevich-dq}`) | **Theorem 4.6.1.1** (formality theorem) and **Theorem 6.4** (algebraic version) | `A = C^\infty(M)` for a smooth manifold (formality of the local Hochschild dg-Lie algebra as `L_\infty`-algebra of polyvector fields with the Schouten bracket). Generalises HKR-classical to the dg-Lie level, but still in the smooth or affine-algebraic regime. |
| **HKR-Toën-Vezzosi (derived)** | Toën–Vezzosi, "Algebraic geometry over model categories," *Memoirs AMS* 193 (2008); Toën, "Higher and derived stacks: a global overview," 2014; sharper form: Toën–Vezzosi, "Caractères de Chern, traces équivariantes et géométrie algébrique dérivée," *Selecta Math.* 21 (2015), 449–554, **Theorem 1.1**, and Hoyois "The fixed points of the circle action on Hochschild homology," 2018, **Theorem 1.5** | For a derived stack `X` over `k`-char-0, `S^1`-equivariant `\mathrm{HKR}: HH(X) \simeq \bigoplus \Omega^p_X[p]` and `\mathrm{HH}^\bullet(X) \simeq \mathrm{T}^\bullet_X[-\bullet]` (polyvector fields on the cotangent complex). | Smooth derived `k`-stack hypothesis; not yet Tate. |
| **HKR-Lurie HA** | Lurie, *Higher Algebra* (= `\cite{lurie-ha}`) | **Theorem HA.7.3.5.1** (chain HKR for `E_\infty`-algebras over a connective `E_\infty`-ring, equivalently `\mathrm{HH}_*(A) \simeq L\Omega^*_{A/R}` for smooth `A`) and **Theorem HA.5.5.3.18** (factorization-algebra ↔ `E_n`-algebra equivalence on `\mathbb R^n`) | Smooth `E_\infty`-algebra hypothesis at HA.7.3.5.1; presentability of factorization algebras at HA.5.5.3.18. |
| **HKR-Pridham/Calaque-PTVV (shifted symplectic)** | Calaque–Pantev–Toën–Vaquié–Vezzosi, "Shifted Poisson structures and deformation quantization," *Crelle* 759 (2020); Pridham, "Shifted Poisson and symplectic structures on derived `N`-stacks," *Selecta Math.* 25 (2019), 5 | Pridham Theorem 1.1; CPT-VV Theorem 0.1 | Derived `n`-shifted symplectic stacks; very far from the classical HKR setting. |

### Per-invocation verification

| Site | Variant invoked | Statement made | Hypothesis check | Verdict |
|------|------------------|------------------|--------------------|----------|
| **#1** (`main.tex`:2056) | Stated as "HKR in the smooth/algebraic setting"; **no primary source cited**. | `\mathrm{Hoch}^\bullet(\widehat{\mathbf S}(\mathfrak h_I)) \simeq_{\mathrm{qis}} \widehat{\mathbf S}(\mathfrak h_I) \widehat\otimes \widehat{\mathbf S}(\mathfrak h_{I,\mathrm{cont}}^\vee[-1])`. | `\widehat{\mathbf S}(\mathfrak h_I)` is the **completed symmetric algebra on a Tate vector space**. This is **not** smooth essentially of finite type over `\C` (it is a power-series ring on infinitely many variables in the cosheaf-of-Lie evaluation). HKR-classical does not apply. HKR-Lurie applies to smooth `E_\infty`-algebras; the smoothness hypothesis at HA.7.3.5.1 is "almost of finite presentation and locally of finite Tor-amplitude," which fails for `\widehat{\mathbf S}` on a Tate space without further care. | **Silent generalization.** The statement is plausible after Tate-completion via the lim of finite-window HKR, but the manuscript does not cite Lurie HA Thm 7.3.5.1 or perform the windowwise limit. |
| **#5** (`main.tex`:2132) | Same; refers back to #1. | Schouten bracket on the brane side of the CE differential. | Inherits from #1. | **Same gap as #1.** |
| **#7** (`main.tex`:2202, in `\rmk:E1-translation`) | Same; explicitly says "by HKR" in the graded-commutative `E_1` setting. | `\mathrm{Hoch}^\bullet(E_1\text{-algebra}) \simeq \mathrm{PV}` for graded-commutative `E_1`. | The graded-commutative `E_1` case is exactly the locally constant `E_1` factorization centre = polyvectors statement. The right primary source is Lurie HA (Costello-Gwilliam Vol II Theorem 5.3.4.10 / Lurie HA Theorem 5.5.3.18 plus the Hochschild-PV identification for graded-commutative `E_1`-algebras, which traces back to Tamarkin's HKR and Kontsevich's formality). | **Silent specialization.** The remark cites `\cite{costello-gwilliam}*{Vol.~I §6.4}` for the factorization-`E_1` translation but does not pin the HKR step. |

### Verdict

The three genuine HKR appeals (lines 2056, 2132, 2202) all silently
generalise classical HKR to the Tate-completed graded-commutative
setting on a cosheaf-of-Lie evaluation. The closest primary source
that closes the gap is Lurie HA Theorem 5.5.3.18 (locally constant
`E_n` factorization algebras on `\mathbb R^n` as `E_n`-algebras) plus
either:
- Costello-Gwilliam Vol II §3 (Hochschild centre stalk computation
  for free graded-commutative `E_1` factorization algebras), or
- Kontsevich `\cite{kontsevich-dq}` (already in the bibliography)
  Theorem 4.6.1.1 (formality / HKR `L_\infty`-quasi-iso, applied
  windowwise after Tate truncation), or
- Tamarkin's deformation-theoretic HKR (Tamarkin, "Another proof of
  M. Kontsevich formality theorem," *math/9803025*).

Combined with `\lem:continuous-bar-cobar` (windowwise reduction to
finite Tate windows, the only place where classical HKR rigorously
applies), this is the proper closure path. The manuscript does not
take this path explicitly.

---

## §T3. Theorem A foundations: hypothesis-by-hypothesis audit

### What "Theorem A" means in this manuscript

The brief names "Theorem A (CE/PV cotangent identity)." The label
`thm:main-local` at `main.tex`:1164 is a **corollary** ("Main local
summary corollary"), not a self-standing theorem. The actual
proof-bearing CE/PV cotangent identity is:

| Layer | Label | Lines | Proof status |
|-------|-------|-------|--------------|
| Lane index | `\thm:lane-ce-pv-center` | `theorem-lanes.tex`:96–148 | "proved degreewise stable" |
| Cochain-level theorem | `\thm:open-closed-derived-center` | `main.tex`:2322–2438 | Generator + Leibniz extension proof |
| Formal-disk specialisation | `\cor:derived-center-formal-disk` | `main.tex`:2465–2504 | Monomial structure-constant verification |
| Factorization upgrade | `\thm:open-closed-derived-center-factorization` (= "Theorem E") | `main.tex`:1996–2191 | 8-step proof; **HKR appears in Step 1** |
| Summary corollary | `\thm:main-local` | `main.tex`:1164–1200 | Index pointer only |

The cochain-level CE/PV identity, what physicists call "Theorem A,"
is `\thm:open-closed-derived-center`. Its statement (verbatim, lines
2322–2349):

> **Theorem (Open-closed derived center, cochain level).** Let
> `\mathfrak h` be any pro-finite-dimensional Lie algebra in
> `\Cat{TateVec}` over `\C`, concentrated in degree zero, satisfying
> the Tate-conilpotency hypothesis of `\lem:continuous-bar-cobar`.
> Let `\mathfrak g = \mathfrak h \ltimes \mathfrak h^\vee_{\mathrm
> {cont}}[1]` be the shifted-cotangent extension. Let `A_\partial =
> \widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h)` be the Tate-
> completed Kirillov-Poisson algebra of `\lem:linear-poisson-schouten`.
>
> Then there is a canonical isomorphism of completed dg graded-
> commutative `P_0`-algebras
>
> `\Phi: C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g)
>      \xrightarrow{\sim} \mathrm{PV}(A_\partial),`
>
> determined on generators by `\Phi(c^I) = \theta^I, \Phi(u_I) = O_I`
> (...). Identifying `\mathrm{PV}(A_\partial)` with the derived `P_0`-
> factorization center of the constant factorization algebra
> `A_\partial` promotes `\Phi` to `\Phi: C^\bullet_{\mathrm{CE},
> \mathrm{cont}}(\mathfrak g) \xrightarrow{\sim} Z^{P_0}_{\mathrm{
> fact}}(A_\partial)`.

### Hypothesis audit (Costello + Hypotheses lens)

| # | Hypothesis as stated | Where stated | Costello/Lurie citation that closes it | Pass / weakened / silently strengthened |
|---|----------------------|--------------|------------------------------------------|--------------------------------------------|
| H1 | `\mathfrak h` is pro-finite-dimensional Lie algebra in `\Cat{TateVec}` over `\C`, concentrated in degree zero | `main.tex`:2323-2324 | Definition of `\Cat{TateVec}`, `\lem:continuous-bar-cobar` Item 1; `\cite{beilinson-feigin-mazur}` for Tate vocabulary | **Pass.** Explicit. |
| H2 | `\mathfrak h` satisfies the Tate-conilpotency hypothesis of `\lem:continuous-bar-cobar` | `main.tex`:2324–2325 | `\lem:continuous-bar-cobar` line 3336–3340: descending Lie powers `\mathfrak g^{(\geq m)}` satisfy `\bigcap_m (\mathfrak g^{(\geq m)} + F^w \mathfrak g) = F^w \mathfrak g` for every `w` | **M-01: silently weakened in the formal-disk specialisation.** `\rmk:ce-source-obstruction-disk` (line 2307–2320) proves `[\mathfrak h, \mathfrak h] = \mathfrak h` (perfectness). Hence `\mathfrak h^{(\geq m)} = \mathfrak h` for all `m`, so `\mathfrak g^{(\geq m)} + F^w \mathfrak h = \mathfrak h` `\neq` `F^w \mathfrak h`. The hypothesis fails for `\mathfrak h`. The corollary `\cor:derived-center-formal-disk` therefore **does not** follow from `\thm:open-closed-derived-center` for the unweighted formal disk Hamiltonian; it follows only for the weighted/nilpotent replacements (T1/T2). |
| H3 | `\mathfrak g = \mathfrak h \ltimes \mathfrak h^\vee_{\mathrm{cont}}[1]` is the shifted-cotangent extension | `main.tex`:2326 | Standard semidirect product; `\lem:linear-poisson-schouten` line 3440 | **Pass.** |
| H4 | `A_\partial = \widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h)` is the Tate-completed Kirillov-Poisson algebra | `main.tex`:2327–2328 | `\lem:linear-poisson-schouten` line 3440–3479 | **Pass.** |
| H5 | `\mathrm{PV}(A_\partial) \simeq Z^{P_0}_{\mathrm{fact}}(A_\partial)` (the derived `P_0`-factorization centre identification) | `main.tex`:2343–2348, justified at lines 2427–2437 | "the derived `P_0`-factorization center of a Poisson algebra `A` is by definition represented by the Poisson cochain complex `\mathrm{PV}(A)` with the Lichnerowicz differential" — local Poisson-CE model; **explicitly disclaimed** as not an import of unreduced Costello-Gwilliam | **Silently strengthened, but disclaimed.** The text says "this is the local Poisson-CE model; it is not an import of an unreduced Costello-Gwilliam central-operations theorem." This is **honest**: the identification with `Z^{P_0}_{\mathrm{fact}}` is by reduced-stalk convention. A separate Costello-Gwilliam Vol II theorem would be required to upgrade. |
| H6 | The map `\Phi: c^I \mapsto \theta^I, u_I \mapsto O_I` is well-defined and continuous | proof: lines 2351–2367 | `\lem:continuous-bar-cobar` Item 2 (CE cochains as `\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak g^\vee_{\mathrm{cont}}[-1])`) | **Pass for windowed `\mathfrak h_{\leq w}`; for the full `\mathfrak h` of the formal disk, depends on H2 (M-01).** |
| H7 | `\Phi d_{\mathrm{CE}} = d_\pi \Phi` on generators | proof: lines 2369–2379 | `\lem:linear-poisson-schouten` line 3440–3479; explicit calculation | **Pass.** Generator-level. |
| H8 | Extension by graded Leibniz to the full completed algebra | proof: lines 2381–2396 | Standard, with both differentials being degree-1 derivations | **Pass for windowed; on the full Tate completion the continuity step requires H2.** |
| H9 | `\Phi` is invertible | proof: lines 2398–2403 | Both compositions fix generators; algebra-homomorphism property | **Pass.** |
| H10 | `P_0`-bracket compatibility | proof: lines 2405–2425 | Generator-level explicit check `\{c^I, u_J\}_{\mathrm{CE}} = \delta^I_J`, `[\theta^I, O_J]_S = \delta^I_J` from `\lem:linear-poisson-schouten` | **Pass.** Generator-level. |

### HKR check on Theorem A's proof

Critical observation: `\thm:open-closed-derived-center`'s proof
(lines 2351–2438) **does not invoke HKR**. The proof is:

1. Identify CE cochains as `\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak g^\vee_{\mathrm{cont}}[-1])` via `\lem:continuous-bar-cobar` (no HKR).
2. Match generator differentials by `\lem:linear-poisson-schouten` (computational).
3. Extend by Leibniz; invert by symmetry.
4. Identify `\mathrm{PV}(A_\partial)` with `Z^{P_0}_{\mathrm{fact}}(A_\partial)` by **convention** (not an HKR theorem).

Therefore: **Theorem A in its cochain form is HKR-free, modulo the
Tate-conilpotency hypothesis (M-01).** The HKR appeals are all in
Theorem E (the factorization upgrade), not Theorem A.

### Summary verdict on Theorem A foundations

`\thm:open-closed-derived-center` is rigorously closed for Tate-
conilpotent `\mathfrak h`, and is honestly hypothesis-pinned. The
silent failure is at `\cor:derived-center-formal-disk` and
`\thm:main-local`, where the perfect formal disk `\mathfrak h` does
not satisfy the Tate-conilpotency hypothesis (M-01). The heal is the
M-01 5-way split (M-26 in the master ledger): the corollary holds
through the nilpotent truncations T2 and the weighted regulators T1,
not directly for the perfect `\mathfrak h`.

---

## §T4. PV-vs-CE side coherence on the simplest example

### Setup: `\mathfrak h = \C\langle e \rangle` abelian one-dimensional

Take `\mathfrak h` one-dimensional abelian over `\C`. Then:
- `\mathfrak h^\vee_{\mathrm{cont}} = \C\langle e^* \rangle`.
- `\mathfrak g = \mathfrak h \ltimes \mathfrak h^\vee_{\mathrm{cont}}[1] = \C\langle e \rangle \oplus \C\langle e^*[1] \rangle` with **trivial bracket** (because `\mathfrak h` is abelian, `[H_I, H_J] = 0`).
- `A_\partial = \widehat{\mathbf S}(\mathfrak h) = \C[O]` (single linear coordinate `O = O_e` on `\mathfrak h^\vee \cong \C`).

#### CE side

CE coordinates: `c` (dual to `e`, degree 1) and `u` (dual to `e^*[1]`,
degree 0). Since `\mathfrak g` is abelian:
- `d_{\mathrm{CE}} c = 0`,
- `d_{\mathrm{CE}} u = 0`.

So `C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g) = \C[u] \otimes \Lambda(c)`
with **zero differential**.

#### PV side

`A_\partial = \C[O]` with zero Poisson bracket (abelian Lie algebra
gives trivial Kirillov-Kostant-Souriau bracket: `\{O, O\} = 0`).

Polyvectors: `\mathrm{PV}(\C[O]) = \C[O] \otimes \Lambda(\theta)`
where `\theta = \partial/\partial O`. The Lichnerowicz differential
`d_\pi = [\pi, -]_S` with `\pi = 0` is **zero**.

So `\mathrm{PV}(A_\partial) = \C[O] \otimes \Lambda(\theta)` with
zero differential.

#### The map `\Phi`

`\Phi(c) = \theta`, `\Phi(u) = O`. As graded-commutative algebras:
`\C[u] \otimes \Lambda(c) \xrightarrow{\sim} \C[O] \otimes \Lambda(\theta)`,
which is a strict isomorphism on graded vector spaces (and graded-
commutative algebras), with both differentials zero.

#### Naturality and strictness

- **Strict (not up to chain homotopy).** With abelian `\mathfrak h`,
  the structure constants `C^K_{IJ}` all vanish, so both sides have
  vanishing differentials and `\Phi` matches differentials on the nose.
- **Natural in `\mathfrak h`.** The construction is functorial in
  morphisms of Tate Lie algebras `\mathfrak h \to \mathfrak h'`:
  pullback of CE on the left, pushforward of `\mathrm{PV}` on the
  right; `\Phi` intertwines.

In this example, no Tate-conilpotency issue arises (a one-dimensional
abelian algebra is trivially nilpotent). The example **passes** the
audit cleanly. The pathology of M-01 enters only when `\mathfrak h`
is **perfect** with `[\mathfrak h, \mathfrak h] = \mathfrak h`, which
the abelian case explicitly is not.

### Cross-check on `\mathfrak h = \mathfrak h_{\leq 2}` (the 2-step nilpotent truncation of the formal disk)

Take `\mathfrak h_{\leq 2} = \C\{H_{1,0}, H_{0,1}, H_{2,0}, H_{1,1},
H_{0,2}\}` (degree-`\leq 2` monomials, modulo the constants). Bracket:
`\{H_{1,0}, H_{0,1}\} = 0` (the constant Hamiltonian is removed),
`\{H_{1,0}, H_{m,n}\} = n H_{m,n-1}`, `\{H_{0,1}, H_{m,n}\} = -m
H_{m-1,n}`, with negative-index terms set to zero.

For example `\{H_{2,0}, H_{0,2}\} = 4 H_{1,1}`. The CE differential on
`u_{1,1}` includes the term `4 u_{2,0} c^{0,2} - 4 u_{0,2} c^{2,0}`,
matched on the PV side by `d_\pi O_{1,1} = 4 O_{2,0} \theta^{0,2} -
4 O_{0,2} \theta^{2,0}`. The cochain identity holds at this finite
window. This is exactly the Wave-3 W3-W11-03 PV/CE coherence check on
the simplest non-abelian truncation.

The truncation is conilpotent (5-step nilpotent truncation), so the
hypothesis of `\lem:continuous-bar-cobar` holds and the full
machinery of `\thm:open-closed-derived-center` applies. This is the
M-01 minimal-heal route: the unweighted `\mathfrak h` is replaced by
the cofiltered system of nilpotent truncations.

---

## §T5. Shift conventions for `\mathfrak h^\vee_{\mathrm{cont}}[1]`

### Cross-check at line level

| File:line | Block | Shift convention used | Match |
|-----------|-------|------------------------|-------|
| `main.tex`:1178 | `\thm:main-local` summary | `\mathfrak h \ltimes \mathfrak h^\vee_{\mathrm{cont}}[1]`, with `u_I` of degree 0, `c^I` of degree 1 | `[1]` shifts cotangent generators **up** by 1; CE coordinates dual are shifted **down** by 1 |
| `main.tex`:1239 | `\rmk:dirac-thesis` | `\mathfrak g = \mathfrak h \ltimes \mathfrak h^\vee_{\mathrm{cont}}[1]` | Same |
| `main.tex`:1302 | local fields description | `\widehat{\mathfrak h}^\vee_{\mathrm{cont}}[2]` (note: `[2]`, not `[1]`!) | **Different shift!** This is for the **closed mixed BV fields** `\Omega^{0,*}(B) \widehat\otimes (\widehat{\mathfrak h}[1] \oplus \widehat{\mathfrak h}^\vee_{\mathrm{cont}}[2])`, where the BV degree adds an extra `[1]` from the shifted cotangent. Top-form `p+q=4` makes the pairing degree `−1`. **This is intentional and consistent** because it is the BV ghost grading, not the CE/PV grading. |
| `main.tex`:2009 | Theorem E `\mathfrak g_I = \mathfrak h_I \ltimes \mathcal P_I[1]` | `[1]` on `\mathcal P_I = \mathcal D'_c(I) \widehat\otimes \mathcal P` | Same as Theorem A; `\mathcal P \cong \mathfrak h^\vee_{\mathrm{cont}}` |
| `main.tex`:2326 | `\thm:open-closed-derived-center` | `\mathfrak g = \mathfrak h \ltimes \mathfrak h^\vee_{\mathrm{cont}}[1]` | Same |
| `main.tex`:2356 | proof (CE cochains as `\widehat{\mathbf S}_{\mathrm{Tate}}((\mathfrak h \ltimes \mathfrak h^\vee_{\mathrm{cont}}[1])^\vee_{\mathrm{cont}}[-1])`) | The dual `[-1]` undoes the `[1]` on the cotangent factor, so `c^I` has degree `0+1=1` (CE-dual of degree-0 Hamiltonian) and `u_I` has degree `1+(-1)=0` (CE-dual of degree-1 cotangent generator). | Internally consistent. |
| `main.tex`:3482 | `\prop:ce-koszul` | `\mathfrak g = \mathfrak h \ltimes \mathfrak h^\vee[1]` (drops `_{\mathrm{cont}}` subscript) | **Notational inconsistency, not semantic.** The continuous dual is intended; the prose around the proposition uses `\mathfrak h^\vee_{\mathrm{cont}}` explicitly. Minor cosmetic gap. |
| `local-dictionary.tex`:106 | symbol table | `\mathfrak g = \mathfrak h \ltimes \mathfrak h^\vee_{\mathrm{cont}}[1]` | Same |
| `theorem-lanes.tex`:113 | `\thm:lane-ce-pv-center` | `\mathfrak g = \mathfrak h \ltimes \mathfrak h^\vee_{\mathrm{cont}}[1]` | Same |
| `theorem-lanes.tex`:130–131 | "`|u_I| = 0, |c^I| = 1`" | Explicit | Same |
| `theorem-lanes.tex`:227 | `\thm:lane-factorization-current`: `\mathfrak g_I = \mathfrak h_I \ltimes \mathcal P_I[1]` | Same |

### Verdict on shift conventions

The `[1]` shift on the cotangent factor of `\mathfrak g` is uniform
across Theorem A, Theorem E, the factorization theorem, the local
dictionary, the theorem-lane index, and `\lem:continuous-bar-cobar`.

The single notational inconsistency is:
- `main.tex`:3482, `\prop:ce-koszul` writes `\mathfrak h^\vee[1]`
  without the `_{\mathrm{cont}}` subscript. This is a cosmetic
  oversight; the proof immediately specializes to the explicit
  `H_d \cong \prod_d H_d, \mathfrak h^\vee_{\mathrm{cont}} \cong
  \bigoplus_d H_d^\vee` data (line 3494–3495).

The `[2]` at `main.tex`:1302 is the BV ghost grading of the closed
mixed fields and is intentionally one shift higher than the CE
grading. No conflict.

**No load-bearing shift inconsistency between Theorem A, Theorem E,
factorization theorem, and local dictionary.**

---

## §T6. Proposed minimal heals (one-sentence citation pins)

### W3-W17-01: Pin HKR appeal #1 (Theorem E Step 1) to Lurie HA + windowwise reduction

**Site.** `main.tex`:2056 (proof of `\thm:open-closed-derived-center-factorization` Step 1).

**Current text.**

> By the Hochschild--Kostant--Rosenberg theorem in the smooth/algebraic
> setting, applied here to the free graded-commutative algebra on the
> Tate vector space `\mathfrak h_I`, the Hochschild cochain complex...
> is quasi-isomorphic to the polyvector fields...

**Proposed heal (one sentence).** Insert after "in the
smooth/algebraic setting":

> (Hochschild–Kostant–Rosenberg, *Trans. AMS* 102 (1962),
> Theorem 5.2, in finite-dimensional windows; lifted to the Tate-
> completed cosheaf-of-Lie evaluation by the windowwise inverse limit
> using `\lem:continuous-bar-cobar` Item~2 and Lurie *Higher Algebra*
> Theorem 5.5.3.18 for the locally constant `E_1`-factorization-`E_1`-
> algebra equivalence)

**Alternative excision heal (M-01 / W6-02 path).** Replace the HKR
appeal entirely by a definition: the locally constant `E_1`-
factorization-centre stalk is *defined* to be the Hochschild cochain
complex (Lurie HA Thm 5.5.3.18); for graded-commutative `E_1`
factorization algebras built on free completed symmetric algebras the
PV identification follows by the same Leibniz extension as in the
proof of `\thm:open-closed-derived-center` (no HKR import). This
inscribes the W6-02 minimal heal recommended in the master ledger.

### W3-W17-02: Pin HKR appeal #2 (Theorem E Step 5) to the same source as #1

**Site.** `main.tex`:2132.

**Current text.** "(closed side: by definition; brane side: through
the HKR identification of Step 1 and the Schouten bracket)."

**Proposed heal.** Replace "the HKR identification of Step 1" with
"the windowwise HKR + Lurie HA identification of Step 1." Inherits the
heal of W3-W17-01.

### W3-W17-03: Pin HKR appeal in `\rmk:E1-translation`

**Site.** `main.tex`:2202.

**Current text.**

> ... the Hochschild cochain complex is quasi-isomorphic to polyvector
> fields by HKR ...

**Proposed heal.** Replace by

> ... the Hochschild cochain complex is quasi-isomorphic to
> polyvector fields (Hochschild–Kostant–Rosenberg, *Trans. AMS* 102
> (1962), Theorem 5.2, in finite-dimensional windows; for the
> `\widehat{\mathbf S}` completion on a Tate vector space, take the
> windowwise inverse limit, or equivalently use Lurie HA Theorem
> 5.5.3.18 with the Hochschild centre stalk computation of
> Costello–Gwilliam Vol II §3) ...

### W3-W17-04: Add bibliography entry for the primary source

**Site.** `main.tex`:5926+ bibliography section.

**Proposed heal (single new entry).**

```latex
\bib{hkr}{article}{
   author={Hochschild, G.},
   author={Kostant, B.},
   author={Rosenberg, A.},
   title={Differential forms on regular affine algebras},
   journal={Trans. Amer. Math. Soc.},
   volume={102},
   date={1962},
   pages={383--408},
   doi={10.1090/S0002-9947-1962-0142598-8},
}
```

This closes the load-bearing primary-source citation gap noted by
M-01 and confirmed by W17.

### W3-W17-05: Add a one-sentence Tate-extension footnote

**Site.** `\lem:continuous-bar-cobar` at `main.tex`:3370 (immediately
before `\end{lem}`), or as a separate remark after Item 4.

**Proposed heal (one sentence).**

> *Tate HKR.* By Item~2 and the windowwise classical Hochschild–
> Kostant–Rosenberg theorem, for any pro-finite Tate Lie algebra
> `\mathfrak h` satisfying the conilpotency hypothesis above, the
> Hochschild cochain complex `\mathrm{Hoch}^\bullet(
> \widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h))` is filtered-quasi-
> isomorphic to the Schouten polyvector algebra
> `\mathrm{PV}^\bullet(\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h))
> = \widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h) \widehat\otimes
> \widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h^\vee_{\mathrm{cont}}
> [-1])` (with negative shift convention as in Item~2).

This inscribes the Tate HKR statement as a lemma item with explicit
windowwise proof, removing all silent specialization in the
manuscript body.

---

## §7. Cross-walk to existing master ledger

| W17 ID | Master ledger entry | Wave-2 cross-confirmation | Status after W17 audit |
|--------|---------------------|----------------------------|-------------------------|
| W3-W17-01 | M-01 (HKR-Tate folklore) | M-33 / W6-02 | confirmed; minimal heal pinned to Lurie HA |
| W3-W17-02 | M-01 | M-33 / W6-02 | confirmed; heal inherits from W3-W17-01 |
| W3-W17-03 | M-01 | not previously named | **new finding (was inside `\rmk:E1-translation`)** |
| W3-W17-04 | M-01 | not previously named | **new finding: HKR has no `\bib{}` entry** |
| W3-W17-05 | M-01 | M-26 (Tate-conilpotency split) | confirmed; closes the windowwise extension cleanly |

**No new severity-4 defects identified.** All W17 findings are
prose-level / citation-level repairs of M-01-class gaps already
recorded in the master ledger. Theorem A (`\thm:open-closed-derived-
center`) is HKR-free at the cochain level; the HKR appeal lives in
Theorem E (factorization upgrade) and in `\rmk:E1-translation`.

**Adjudication.** With the five W3-W17 heals inscribed, the HKR
citation load is closed. The Tate-conilpotency hypothesis still
requires the M-01 5-way split for the perfect formal disk, which is
the architectural fix recommended by M-26 and remains outside the
W17 scope.

---

## §8. Files read

- `/Users/raeez/topological-strings/CLAUDE.md`
- `/Users/raeez/topological-strings/reconstitution/attack-heal-platonic-2026-04-28.md` (M-01 entry, W6-02 echo, W3-W11 reference)
- `/Users/raeez/topological-strings/main.tex` (full grep + reads at lines 1056–1265, 1996–2330, 2440–2570, 3080–3110, 3322–3530, 4360–4390, 5085–5105, 5945–5965, 6098–6350)
- `/Users/raeez/topological-strings/local-dictionary.tex` (full)
- `/Users/raeez/topological-strings/theorem-lanes.tex` (full)
- `/Users/raeez/topological-strings/claim-strength-ledger.tex` (full)
- `/Users/raeez/topological-strings/notation.tex` (full)
- Verified absence of HKR text in: `tate-T1`/`T2`/`T3`/`T4`/`T5`, all appendices, abstract, principles, open-obligations, theorem-lanes, claim-strength-ledger, local-dictionary.

---

## §9. 200-word summary

W17 audited every HKR / Hochschild / Kostant / Rosenberg invocation
in the manuscript and verified Theorem A's foundations under the
Costello + Hypotheses lens. HKR text appears only in `main.tex`, at
17 sites; only three are genuine HKR appeals (lines 2056, 2132,
2202), all silently generalising classical HKR to the Tate-completed
graded-commutative setting on a cosheaf-of-Lie evaluation, and **none
of them is backed by a bibliography entry**. Theorem A in its
cochain form (`\thm:open-closed-derived-center`, lines 2322–2438) is
HKR-free: its proof uses `\lem:continuous-bar-cobar` plus generator-
level Leibniz extension via `\lem:linear-poisson-schouten`, and
identifies `\mathrm{PV}(A_\partial)` with `Z^{P_0}_{\mathrm{fact}}` by
explicit reduced-stalk convention. The HKR appeals live in Theorem E
Step 1 and in `\rmk:E1-translation`. The abelian one-dimensional
example verifies CE/PV identity strictly. The shift convention `[1]`
on `\mathfrak h^\vee_{\mathrm{cont}}` is uniform across Theorem A,
Theorem E, factorization theorem, and local dictionary. Five W3-W17
heals proposed: pin HKR to Lurie HA Thm 5.5.3.18 + windowwise
classical HKR, add the missing `\bib{hkr}{}` entry, add a Tate-HKR
item to `\lem:continuous-bar-cobar`. With these inscribed, M-01's
HKR-Tate folklore gap closes at the citation level; the architectural
M-26 5-way split for the perfect formal disk remains outside W17 scope.
