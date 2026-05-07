# Cross-reference and interweaving audit (agent L)
## topological-strings, main.tex + included parts, 2026-05-07

This is a read-only audit of the manuscript's interweaving health: cross-references, bibliography, decorative transitions, false-strength claims, and the §1 + §2 dependency graph. No `.tex` files were modified.

Files audited as **included** by `main.tex` (build root):

- `abstract.tex`
- `tate-T1-weighted-completion.tex`, `tate-T2-nilpotent-truncation.tex`, `tate-T3-quillen-equivalence.tex`, `tate-T4-bv-vanishing.tex`, `tate-T5-chain-level-primitive.tex`, `tate-P1-hadamard-mittag-leffler.tex`
- `appendix-matlis-principal-parts.tex`, `appendix-factorization-current-conventions.tex`, `appendix-sign-conventions.tex`, `appendix-full-psi-homology.tex`, `appendix-unreduced-bv-qme.tex`, `appendix-radial-parts-moyal.tex`

Files audited as **dead / not included** (no `\input` from `main.tex`, no entry in `Makefile`, empty `standalone/` directory):

- `tate-P3-universality.tex` (15 theorems/lemmas/defs, 8 labels, fully developed obstruction theorem on universality)
- `tate-P5-cross-volume.tex` (14 statements, 11 labels, cross-volume firewall)
- `principles.tex` (`sec:three-principles`)
- `reader-route.tex` (proof status board)
- `claim-strength-ledger.tex` (claim-status table)
- `local-dictionary.tex` (terminology bridge)
- `open-obligations.tex` (`sec:open-obligations`)
- `frontier_mnop_framing_volume.tex` (separately compiled standalone)

This is a **load-bearing, structural finding**: the dead files contain substantial material (33 labels, 33+ theorems/lemmas/defs/cors/props) that is inaccessible from the compiled manuscript. They are referenced **into** by the included files in 22 distinct cross-references (see §1, item "Decorative-transition map" and §6 below).

---

## 1. Cross-reference health

| Quantity                                 | Count |
| ---------------------------------------- | ----: |
| `\label{...}` declarations (included)    |   512 |
| `\label{...}` declarations (unincluded)  |    33 |
| `\ref` / `\eqref` / `\cref` / `\autoref` (included files), unique targets |  380 |
| Duplicate labels                         |     0 |
| Unresolved references (after pdflatex stabilization) | **1 (silent `??`)** |
| First-pass forward warnings (clear after stabilization) | many (normal LaTeX behavior) |

### Unresolved reference (silent `??` in PDF)

- `main.tex:954` — `\S\ref{ssec:scalar-anomaly}` references a label that does not exist. The actual label, declared at `main.tex:689`, is `\label{subsec:scalar-anomaly}`. The mismatch is **silent**: pdflatex emits no `Reference undefined` warning for this case (verified by `out_test/main.log`), but `pdftotext main.pdf | grep '??'` shows the result rendered as `§??–§1.3` near "the open factorization algebra ... of §??–§1.3".  
  - **The same label is used correctly** at `main.tex:1002` as `\S\ref{subsec:scalar-anomaly}`. So this is a one-letter typo (`ssec:` vs `subsec:`).
  - **Suggested fix**: rename the label at line 689 to `ssec:scalar-anomaly` (matching the `ssec:` prefix used by *every other* `\subsection` label in main.tex: `ssec:intro-notation-index`, `ssec:two-algebras`, `ssec:local-theorem`, `ssec:tate-residual-resolution`, etc.) and update the single correct reference at line 1002.

### Orphan labels (declared, never referenced)

133 orphan labels in included files. Distribution by prefix:

| prefix | count | comment |
|--------|------:|---------|
| `rmk:` | 47    | most are remark labels added defensively; can stay |
| `prop:`| 11    | nine of these are propositions never cited (false weight: a proposition that is not used is dead structure) |
| `eq:`  | 11    | unused display labels |
| `def:` | 11    | unused (mostly old-style `def:` rather than `defn:`); see notation drift below |
| `cor:` | 10    | unused corollaries |
| `thm:` |  9    | major theorems no downstream theorem cites — see list below |
| `lem:` |  9    | unused lemma anchors |
| `lost:`|  5    | item-level anchors inside `prop:trunc-lost-sectors`; the parent prop is also orphan |
| `sec:` |  4    | unused section anchors |
| `defn:`|  4    | unused (mostly newer-style `defn:`) |
| `ssec:`|  3    | unused subsection anchors |
| `ex:`  |  3    | example anchors |
| `stmt:`|  2    | external-input statement anchors |
| `constr:` | 2  | construction anchors |
| `prob:`|  1    | one orphan problem |
| `app:` |  1    | unused appendix anchor |

#### Notation drift inside included files

- `def:` versus `defn:`: 14 of 15 inputs use `defn:`, but 11 use the older `def:` prefix (e.g. `def:hamiltonian-cyclic-koszul-lie-model`, `def:local-topological-string-sector`, `def:local-th-string`, `def:tate-model`, `def:wt-omega-normal-window`, `def:hamiltonian-cyclic-koszul-lie-model`, etc.). Either standardize on `defn:` or the inverse.
- `subsec:` versus `ssec:`: only one outlier (`subsec:scalar-anomaly`); see fix above.

#### Orphan major-theorem labels (9 `thm:*`, in §1 / §2 / appendices)

| label | location | severity |
|-------|----------|----------|
| `thm:bv-replacement-unitarity` | `main.tex:1218` (§1.7 Unitarity) | high — a §1 theorem with no downstream citation |
| `thm:reduced-moyal-commutator` | `main.tex:8430` | high — referenced by name in adjacent prose but no `\ref` |
| `thm:gauge-brst-cyclic-obstruction` | `main.tex:6091` | medium |
| `thm:primitive-cyclic-koszul-p0-model` | `main.tex` | medium |
| `thm:weighted-rg-locality-reduced` | `tate-T1` | medium |
| `thm:wt-ce-pv-qtoone-stabilization` | `tate-T1` | medium |
| `thm:wt-finite-degree-observables` | `tate-T1` (line 1082) | medium |
| `thm:wt-wavefront-distributional-primitive-cone` | `tate-T1` | medium |
| `thm:T5-universal-primitive-descendant-envelope` | `tate-T5` | medium |

#### Orphan proposition labels (11 `prop:*`)

`prop:app-factorization-principal-part-bracket`, `prop:app-factorization-source-of-B`, `prop:app-marked-bst0-equivariant-differential`, `prop:coordinate-coupling-equations`, `prop:genuine-order-two-graph-weight-rows`, `prop:native-darboux-disk-constructions`, `prop:no-universal-strict-kernel-habitat`, `prop:theta-three-finite-window-criterion`, `prop:theta-three-primitive-entry-criterion`, `prop:trunc-lost-sectors`, `prop:wt-raw-kappa-cochain-obstruction`.

#### Orphan `lost:*` enumeration anchors

Inside `prop:trunc-lost-sectors` (in `tate-T2-nilpotent-truncation.tex` lines 343–386), five `lost:translations`, `lost:sl2`, `lost:constants`, `lost:u1-anomaly`, `lost:colim` are item anchors but the prose around them does not `\ref` to them. They are functional decoration; harmless but dead.

---

## 2. Bibliography health

- Total bibliography entries (`\bib{}`): **39** (lines 10477–10930 of `main.tex`, `\begin{biblist}` ... `\end{biblist}`).
- No `.bib` file: bibliography is inline `amsrefs` style.
- Unique cited keys (across all included files): **35**.
- **Unused bib entries** (declared, never `\cite`'d in included or unincluded source): **3**:
  - `aksz` — `\bib{aksz}{article}` at `main.tex:10548` — the words "AKSZ" and "AKSZ language" appear at `main.tex:3557` and `main.tex:6998` but **without** a `\cite{aksz}`.
  - `cattaneo-felder-bv` — `\bib{cattaneo-felder-bv}{article}` at `main.tex:10821` — the names Cattaneo–Felder are not cited anywhere by key.
  - `witten-cs` — `\bib{witten-cs}{article}` at `main.tex:10516` — the manuscript does cite Witten verbally ("Witten 1988", "Witten centrality") but no `\cite{witten-cs}` exists.
- **Missing bib entries** (cited keys without bibliography entry): **0**.
- Citation frequency — top 10:

| key | times |
|-----|------:|
| `costello-renormalization` | 19 |
| `loday-vallette` | 9 |
| `lurie-ha` | 7 |
| `costello-li-open-closed-bcov` | 6 |
| `hormander-vol1` | 5 |
| `costello-li-quantum-bcov` | 5 |
| `costello-gwilliam` | 5 |
| `ruppenthal-bmk` | 4 |
| `procesi`, `razmyslov`, `kontsevich-dq` | 4 each |

- Recommended action for the 3 unused entries: either `\cite{aksz}` at the AKSZ paragraphs (`main.tex:3557`, `6998`) where it is named in prose, `\cite{witten-cs}` at the "Witten centrality" / "Witten 1988" paragraphs (e.g. `main.tex:633` "Witten's centrality computation", or `main.tex:2527` `loday-quillen,tsygan` discussion), and `\cite{cattaneo-felder-bv}` at the brane-action / BV-line paragraph in §2 (e.g. `main.tex:3722` Hamiltonian BF action, where Cattaneo–Felder is the canonical attribution). Otherwise, **delete** the three orphan `\bib{...}` entries to keep the bibliography tight.

### `cites` style discipline

`amsrefs` warns once: `Package amsrefs Warning: Use of \cites is recommended instead of \cite`. There are 27 single-key `\cite{...}` calls and 7 `\cites{...,...}` calls. Not load-bearing, but an `amsrefs` lint suggests changing every multi-key usage to `\cites`.

---

## 3. Decorative-transition map

The Russian-school discipline is **largely intact**. Searches for the standard pre/post-section transition phrases return essentially nothing across `main.tex`, the six included `tate-*.tex`, and the six included `appendix-*.tex`:

| pattern | hits |
|---------|-----:|
| "In this section / subsection (we will / we) " | 0 |
| "We now turn to / We turn to" | 0 |
| "Before we (proceed / continue / begin)" | 0 |
| "In what follows" | 0 |
| "Note that" / "Recall that" | 0 |
| "We have just" / "We will now" / "We have now" | 0 |
| "Throughout / Below we / Below," | 0 |
| "We begin / We start / We conclude / We close / Finally," | 0 |
| "Next, " | 0 |

The three matches for the verb "this subsection" (`main.tex:2259`, `6343`, `6574`) are **closure** sentences ("the close of this subsection", "this subsection closes with") and read as named obstructions, not pure narration; they pass the discipline.

Three `\paragraph*{Organizing question.}` markers exist (`tate-P1-hadamard-mittag-leffler.tex:11`, `tate-P3-universality.tex:13`, `tate-P5-cross-volume.tex:12`). These are headed sub-paragraph anchors, not orphan transitional sentences; they pass the discipline.

**No decorative-transition findings to fix.**

---

## 4. False-strength map

The rectify-discipline rule is: every assertion must have either a proof in place, an admissibility flag (clearly named external input), or an obstruction theorem. Sweep across all included files:

### 4a. `\paragraph{Conjectural ...}` block in `abstract.tex` (lines 188–254)

Four conjectures are **clearly flagged** under the heading `\noindent\textbf{Conjectural, with precise statement.}`:

- (C1) all-bidegree radial/Weyl normal-form vanishing — points to `prop:app-radial-dual-potential-obstruction` (resolves into `appendix-radial-parts-moyal.tex`),
- (C2) reduced non-scalar Costello QME — points to `prob:quantum-p0-operation-realization`,
- (C3) unreduced Tate-coefficient cotangent lift — points to `prob:formal-factorization-center` (38 cross-references — the manuscript's most central open obstruction),
- (C4) strict native all-window Bochner–Martinelli current transfer — points to `\operatorname{Ob}^{\Pi}_{\mathrm{BM}}`.

Each conjecture has a named obstruction class or problem statement. **No false strength here**: the abstract correctly demarcates `\textbf{Proved}` from `\textbf{Conjectural, with precise statement}`.

### 4b. "external" inputs in main body and appendix

| line | claim | epistemic flag |
|------|-------|----------------|
| `main.tex:1721` | "The external several-complex-variables sources are used here only for ..." | flagged correctly |
| `main.tex:2010` | "The external Koppelman identity for $K_{\mathrm{BM}}$ supplies only ..." | flagged correctly |
| `appendix-radial-parts-moyal.tex:323` | `\begin{stmt}[Radial-parts input data] \label{stmt:app-radial-external-input}` | external-input statement, used 11 times via `\ref{stmt:app-radial-external-input}`. Excellent admissibility-flag discipline. |
| `appendix-radial-parts-moyal.tex:344` | "It is not supplied by the cited radial-parts sources in this exact Weyl/Capelli convention." | this is the right voice |

### 4c. `should be / will be` hedging

Single match: `main.tex:8941` "the obstruction should be represented as a local functional class in the chosen bulk-defect local-functional complex." This is inside `\begin{prob}[Hamiltonian specialization datum for Costello perturbative BV]` (a problem statement), so "should be" is structurally correct (problems describe what their data look like).

### 4d. "missing" / "not addressed"

The phrase "missing" appears 4 times, all inside the body of named obstruction theorems or problems where the missing object is precisely the **named** datum (centrality homotopies, marked source column, etc.). This is supremum-discipline-correct.

### 4e. Suspect `lost:*` items in `tate-T2`

`prop:trunc-lost-sectors` (line 343 in `tate-T2-nilpotent-truncation.tex`) lists **what is removed by the m^3 truncation**. The five `\item\label{lost:*}` anchors are never `\ref`'d back, so the proposition is functioning as a **prose checklist** rather than an obstruction theorem. The proof "What remains classically: ... The all-order Moyal descendant lift is excluded by `\ref{thm:phi-hbar-trunc}` unless extra quantum truncation data are added" is good obstruction-naming but the labels are decorative. Either drop the `\label{lost:*}`s, or `\ref` to them in the prose where each lost sector is discussed downstream.

### 4f. Theorem 1.7 (`thm:bv-replacement-unitarity`)

Stated `main.tex:1218`. Proved in place. **Never referenced** by any downstream lemma, theorem, or remark, in any included file. Either it is a synthesis statement that summarizes downstream content (in which case wire its summary into the proof of `thm:main-local`), or the unitarity / BV-replacement story has decoupled from the main lane. Currently sits as a theorem floating in §1.7.

**No structurally false-strength claims found in §1 or §2.** All conjectural language is segregated into the abstract's "Conjectural, with precise statement" block, all "external" inputs are flagged with admissibility / `stmt:` anchors, and all "missing" objects are named.

---

## 5. Dependency graph for §1 and §2 major theorems

§1 = `\section{Introduction}` (`main.tex:254` to `main.tex:3172`); §2 = `\section{The Local Model}` (`main.tex:3173` onward). I tabulate the major load-bearing theorems and problems in §1 + §2, with their direct dependencies and downstream supports. "Cited count" is the number of `\ref` / `\eqref` to that label across all included files.

| Label                                     | Section / Line | Title (short)                                     | Direct deps                                                              | Supports / cited from                     | Cited count |
|-------------------------------------------|---------------:|---------------------------------------------------|--------------------------------------------------------------------------|-------------------------------------------|------------:|
| `lem:probe-trace-microscope`              | §1.1 / 336     | Procesi–Razmyslov microscope                      | `\cites{procesi,razmyslov}`                                              | §1.1, §1.4, `thm:main-local` proof        |  several   |
| `thm:witten-centrality-local-form`        | §1.4 / 640     | Reduced Hamiltonian central-operation criterion   | `prob:formal-factorization-center` (open obstruction)                    | unitarity statements, §1.5                |    1*      |
| `thm:u1-center-anomaly`                   | §1.5 / 779     | U(1) center anomaly: closed side                  | `lem:omega-cocycle`                                                       | §1.5, abstract, principles                |     5      |
| `thm:u1-center-anomaly-open`              | §1.5 / 815     | U(1) center anomaly: open side                    | (matrix calc)                                                             | §1.5, abstract, principles                |     5      |
| `thm:quantum-classical-anomaly`           | §1.5 / 873     | Quantum-classical equivalence of U(1) center class| `\cites{capelli,howe-capelli}`                                            | §1.5, abstract                            |     5      |
| `prop:three-localities` (cite by name)    | §1.6 / 1157    | Locality forced by three differentials            | (de Rham + Q + delta(t-s))                                                | §1.6 only                                 |     1      |
| `thm:bv-replacement-unitarity`            | §1.7 / 1218    | BV replacement for unitarity                      | `\cite{costello-renormalization}`                                         | **no downstream citation**                |     0      |
| `prop:local-hamiltonian-factorization-observables` | §1.10 / 1612 | Constructed Hamiltonian CE/factorization observables | T1 weighted Tate, BMK appendix                                       | §1.10, T1, T5                              |  several   |
| `prop:finite-window-bm-native-e2-transfer`| §1.10 / 1678   | BMK current data + finite-window obstruction      | `\cites{laurent-thiebaut-bmk,ruppenthal-bmk}`, `\cite{hormander-vol1}`     | abstract (C4), `thm:main-local`           |  several   |
| `prop:native-darboux-disk-constructions`  | §1.10 / 2088   | Native Darboux disk                               | (formal Darboux)                                                           | **no downstream citation**                |     0      |
| `prop:formal-local-global-restriction`    | §1.10 / 2170   | Formal-stalk Hamiltonian restriction              | (Taylor-stalk)                                                             | tate-P3, tate-P5 (dead files)             |     0 in live |
| `thm:loday-quillen-tsygan`                | §1.11 / 2369   | Loday–Quillen–Tsygan stable trace                 | `\cites{loday-quillen,tsygan}`                                            | §1.11, §1.13                              |  several   |
| `thm:stable-eulerian-lqt-window`          | §1.11 / 2385   | Stable Eulerian finite-window LQT projection      | `thm:loday-quillen-tsygan`                                                | §1.11, §1.13                              |  several   |
| `thm:coordinate-free-cotangent-ce-pv`     | §1.13 / 2646   | Coordinate-free cotangent CE/PV identity          | (finite-dim CE/PV)                                                        | proof of `thm:universal-ce-pv-koszul-criterion` |  3   |
| `thm:reduced-ce-pv-central-operation`     | §1.13 (proof of T-univ) | Coordinate formal-disk identity            | `thm:formal-disk-completed-ce-pv`, `thm:principal-part-coadjoint-uniqueness` | many                                  |    25   |
| `thm:formal-disk-completed-ce-pv`         | §1.13 / 2716   | Formal-disk source-to-boundary CE/PV reconstruction | `thm:reduced-ce-pv-central-operation`                                  | `thm:universal-ce-pv-koszul-criterion`    |     2      |
| `thm:universal-ce-pv-koszul-criterion`    | §1.14 / 2867   | **Coordinate CE/PV theorem and admissible Koszul criterion** | finite-dim CE/PV; `thm:principal-part-coadjoint-uniqueness`; `thm:wt-omega-kernel-admissibility` (T1); `thm:relative-filtered-koszul-lift`; `lem:filtered-cobar-qiso-criterion`; `lem:continuous-bar-cobar`; `prop:low-degree-pronilpotent-obstruction`; `defn:stable-ainfty-koszul-acceptance-datum`; `thm:stable-ainfty-koszul-under-hypotheses`; `rmk:colim-does-not-recover-full`; `rmk:conilpotency-essential`; `prob:weighted-rg-locality` | abstract, `thm:main-local`, `principles` (dead) |    16   |
| `thm:main-local`                          | §1.15 / 2990   | **Formal local Hamiltonian BF/Dirac-brane comparison** | `thm:universal-ce-pv-koszul-criterion`; `thm:reduced-principal-part-boundary-current`; `thm:componentwise-quantum-coefficient-comparison`; `thm:phi-hbar-all-order`; `prop:app-edge-pbw-telescoping`; `prop:app-radial-dual-potential-obstruction`; `prob:formal-factorization-center` | tate-T2, tate-T4, tate-P3 (dead), §1, §2  |    19   |
| `prop:local-model-mixed-definition`       | §2.1 / 3198    | Local mixed model                                 | (target spec)                                                             | §2.2, §2.3                                |     few    |
| `prop:skyscraper-ext`                     | §2.2 / 3318    | Affine skyscraper self-Ext                        | (algebraic)                                                                | §2.2, §2.3                                 |     few    |
| `lem:open-action-reduction`               | §2.3 / 3425    | Open-action reduction                             | `eq:open-action-derived`                                                   | §1.1, §2.3, §3                             |    several |
| `lem:dirac-probe-reduction`               | §2.3 / 3457    | Dirac reduction of probe phase space              | (constraint algebra)                                                       | §1.1, principles, §2.3                    |    several |
| `prop:open-bv-truncation`                 | §2.3 / 3495    | Classical BV truncation                           | `lem:dirac-probe-reduction`                                                | §1.1, principles, §2.3                    |    several |
| `lem:polynomial-poincare`                 | §2.4 / 3640    | Polynomial Poincaré primitive                     | (de Rham polynomial)                                                       | §2.4, §2.6                                 |     1      |
| `prop:hamiltonian-polyvector-reduction`   | §2.4 / 3670    | Hamiltonian polyvector reduction                  | `lem:polynomial-poincare`                                                  | §2.4–§2.6                                  |     few    |
| `prop:brane-bracket-locality`             | §2.6 / 3989    | Locality of brane $P_0$ bracket                   | matrix algebra                                                             | §1.4, §2.6                                 |     2      |
| `thm:hamiltonian-current-center-lift`     | §2.6 / 4293    | Hamiltonian-current central operation, smeared    | `prop:brane-bracket-locality`                                              | named in `main.tex:863` only               |     1      |
| `thm:reduced-ce-pv-cochain` (4443)        | §2.6 / 4443    | Admissible reduced cochain CE/PV                  | dictionary, signs                                                          | proof of `thm:universal-ce-pv-koszul-criterion` |  several  |
| `prop:ce-source-obstruction`              | §2.6 / 4345    | CE-source obstruction                             | (perfect-Lie obstruction)                                                  | §1.13–§1.14                                |     1      |
| `thm:relative-filtered-koszul-lift`       | §2.6 / 4771    | Relative filtered CE/PV reconstruction criterion  | `lem:filtered-cobar-qiso-criterion`                                       | proof of `thm:universal-ce-pv-koszul-criterion` |  1      |
| `thm:stable-ainfty-koszul-under-hypotheses` | §2.6 / 4987   | Admissible open-side filtered $A_\infty$-Koszul acceptance | `defn:stable-ainfty-koszul-acceptance-datum`                       | proof of `thm:universal-ce-pv-koszul-criterion` |  2      |
| `prob:pbw-p0-center-action`               | §2.7 / 5216    | PBW-source $P_0$-center action criterion          | named obstruction                                                           | §2.7                                       |   small    |
| `prob:formal-factorization-center`        | §2.7 / 5255    | **Unreduced Tate-coefficient cotangent lift datum** | `lem:tate-casimir-obstruction`, weighted Tate (T1), nilpotent (T2)         | abstract (C3), §1, §2, T2, T3, T4, T5     |    38      |

`*` for `thm:witten-centrality-local-form`: the cited count is approximate; the theorem is referenced by name without explicit `\ref`.

### Cycle / dead-end analysis

- **No cycles** detected among `\ref`-edges.
- **Dead ends** (theorems / propositions with **0 downstream `\ref`** in included files):
  - `thm:bv-replacement-unitarity` (§1.7 / line 1218) — synthesis statement floating
  - `prop:native-darboux-disk-constructions` (§1.10 / line 2088) — references neither downstream
  - `prop:formal-local-global-restriction` (§1.10 / line 2170) — only referenced from dead files (`tate-P3`, `tate-P5`); inside the live build it is dangling
  - `prop:trunc-lost-sectors` (`tate-T2:343`) — five `lost:*` items hang off it
- **Orphan major-theorem labels** (the 9 listed in §1 above).

### Most-load-bearing nodes (ranking by inbound `\ref` count)

1. `prob:formal-factorization-center` (38) — primary open obstruction, the spine of the manuscript.
2. `thm:principal-part-coadjoint-uniqueness` (26)
3. `thm:reduced-ce-pv-central-operation` (25)
4. `thm:reduced-principal-part-boundary-current` (23)
5. `thm:main-local` (19) — the §1.15 main theorem.
6. `thm:bulk-boundary` (17)
7. `thm:universal-ce-pv-koszul-criterion` (16)
8. `prob:quantum-p0-operation-realization` (13)
9. `thm:phi-hbar-all-order` (12)
10. `thm:componentwise-quantum-coefficient-comparison` (9)

The core is well-interwoven. The proof of `thm:main-local` in §1.15 is supported through `thm:universal-ce-pv-koszul-criterion`, which factors through `thm:reduced-ce-pv-central-operation`, `thm:relative-filtered-koszul-lift`, `lem:filtered-cobar-qiso-criterion`, and `thm:stable-ainfty-koszul-under-hypotheses`; the open-side leg flows through `lem:dirac-probe-reduction`, `prop:open-bv-truncation`, and `lem:open-action-reduction`. The Koszul/Tate completion lane is in `tate-T1` (38 statements, 39 labels), the nilpotent truncation in `tate-T2` (11 statements), the bar-cobar/Quillen rectification in `tate-T3` (22 statements), the BV vanishing in `tate-T4` (6 statements), the chain-level primitive in `tate-T5` (20 statements), and the Hadamard regulator in `tate-P1` (20 statements). Each is wired into `thm:main-local` and `prob:formal-factorization-center` through finite-window obstruction classes.

### What is **not** in the live build

- `tate-P3-universality.tex` — universality theorem with named `\operatorname{Ob}^{\mathrm{univ}}_{p,X}` and `cor:protected-formal-uniformity`. Referenced into by `principles.tex` only (also dead). Refers **out** to `thm:main-local`, `ssec:local-theorem`, `thm:componentwise-quantum-coefficient-comparison`, etc., across 22 distinct labels in included material.
- `tate-P5-cross-volume.tex` — matched-conventions firewall. Refers out to `thm:main-local`.

If these were re-`\input` into `main.tex`, the manuscript would acquire a universality story (P3) and a cross-volume firewall (P5) that match exactly the `Ob^univ_{p,X}` / `Ob_{UKD}` discipline named in `CLAUDE.md`. With them dead, the manuscript currently has **no live universality theorem** and **no live cross-volume firewall**, even though the `principles.tex` discipline assumes both.

---

## 6. Top 5 highest-leverage interweaving fixes

Ranked by structural impact on the manuscript's interweaving health:

### 6.1 Re-include the dead `\input`s (P3, P5, principles, reader-route, ledger, dictionary, open-obligations)

**Highest leverage.** Eight stand-alone files of substantial mathematics (60+ theorems / props / defs / cors / problems, 33 labels) are present in the repo, written, but never compiled into `main.pdf`. The Makefile compiles only `main.tex`, the `standalone/` directory is empty, and `main.tex` does not `\input` them. Either:

  - (a) **add explicit `\input` lines** in `main.tex` between §2 and the appendices (after line 5263 / before line 10469) for `principles.tex`, `reader-route.tex`, `claim-strength-ledger.tex`, `local-dictionary.tex`, `open-obligations.tex`, `tate-P3-universality.tex`, `tate-P5-cross-volume.tex`; or
  - (b) **state explicitly** in `CLAUDE.md` and the manuscript that these are quarantined-conditional / in-flight files; or
  - (c) **delete** them from the repository if they are obsolete.

The current state — present-but-dead — is the worst of all worlds: it makes references like `\ref{thm:main-local}` from `tate-P3:755` invisible to the reader, while consuming proof budget and review surface.

### 6.2 Fix `subsec:scalar-anomaly` ↔ `ssec:scalar-anomaly` typo

`main.tex:954` produces a silent `??` in the compiled PDF (`§??–§1.3` near "the open factorization algebra ..."). Standardize on `ssec:` (matching every other subsection label in `main.tex`). Concrete fix:

  - `main.tex:689`: `\label{subsec:scalar-anomaly}` → `\label{ssec:scalar-anomaly}`.
  - `main.tex:1002`: `\S\ref{subsec:scalar-anomaly}` → `\S\ref{ssec:scalar-anomaly}`.

(Total: 2 line edits; eliminates the only PDF-visible silent reference failure.)

### 6.3 Audit and route the 9 orphan major-theorem labels

In particular, `thm:bv-replacement-unitarity` (§1.7) is a §1 theorem that no downstream theorem cites. Either route it into the proof of `thm:main-local` (Mechanism Principle 4 / 6 currently mentions unitarity once but does not `\ref`), or absorb its content into the introduction discussion. The same audit applies to `prop:native-darboux-disk-constructions` (§1.10), `prop:trunc-lost-sectors` (`tate-T2`), and the 7 other orphan theorems / props listed in §1 above. Per the discipline, each isolated theorem must either (i) supply data into a downstream theorem, (ii) be the source of an obstruction class, or (iii) be merged into prose.

### 6.4 Either cite or delete the 3 unused bib entries

  - `\cite{aksz}` at `main.tex:3557` ("In AKSZ language ...") and `main.tex:6998` ("the AKSZ remark above") — currently AKSZ is named verbally without citation key.
  - `\cite{witten-cs}` at `main.tex:633` ("Witten's centrality computation") or `main.tex:6448` (Koszul/cyclic discussion) — currently Witten is named without citation key.
  - `\cite{cattaneo-felder-bv}` at the Hamiltonian BF action / open BV paragraph (§2.5, around `main.tex:3722`) — Cattaneo–Felder is canonical attribution for the BF construction this paper builds on.

If the references are not supposed to anchor here, **delete** the three `\bib{...}` entries (lines 10548–10561, 10516–10529, 10821–10832) to keep the bibliography lean.

### 6.5 Standardize `def:` versus `defn:` label-prefix discipline

11 `def:`-prefixed labels coexist with 14 `defn:`-prefixed labels. Pick one. Recommended: `defn:` (matches the `\begin{defn}` environment name in the manuscript). After standardization, the 11 `def:`-labels (`def:hamiltonian-cyclic-koszul-lie-model`, `def:local-topological-string-sector`, `def:local-th-string`, `def:tate-model`, `def:wt-omega-normal-window`, `def:app-factorization-current-coordinates`, `def:app-factorization-enlarged-current-target`, `def:app-matlis-principal-parts`, `def:app-matlis-topology`, `def:app-radial-stable-primitive-extraction`, `def:app-radial-vandermonde-gauge-variables`, `def:app-sign-hamiltonian-cyclic`, `def:app-square-cell-pbw-stokes-complex`, `def:app-unreduced-bv-degrees`) become `defn:*`, and any in-flight `\ref` from dead files like `tate-P3` / `tate-P5` to them needs updating consistently. (Many of the 11 `def:` labels are orphan — see §1 — so the migration is light.)

---

## Appendix: counts at a glance

| metric | value |
|--------|------:|
| `main.tex` total lines | 10,936 |
| Total live `.tex` lines (included files) | ~32,815 |
| Sections in `main.tex` | 2 (§1 Introduction, §2 The Local Model), plus §3-§4 in `tate-T*` and appendices |
| Bibliography entries | 39 |
| Unique cited keys (live) | 35 |
| Unused bib entries | 3 |
| Missing bib entries | 0 |
| Unique labels (included) | 512 |
| Unique labels (dead files) | 33 |
| Total `\ref`/`\eqref`/... unique targets (live) | 380 |
| Unresolved references (after pdflatex stabilization) | 1 silent (`subsec:scalar-anomaly` ↔ `ssec:scalar-anomaly`) |
| Duplicate labels | 0 |
| Orphan labels (unused) | 133 |
| Decorative-transition findings | 0 |
| False-strength findings (in §1 or §2) | 0 (all conjectural language gated into abstract) |
| Dead-end major theorems (orphan `thm:*`) | 9 |
| Dead-end major propositions (orphan `prop:*`) | 11 |
| Dead `\input`-able files in repo | 7 (tate-P3, tate-P5, principles, reader-route, claim-strength-ledger, local-dictionary, open-obligations) |
| Inbound `\ref` from dead files into live labels | 22 |
| pdflatex stable build | yes (3 pass-through warnings; 0 reference errors) |

---

*End of audit. No `.tex` files were modified by this agent. Audit report staged at `_audit/cross-reference-and-interweaving.md`.*
