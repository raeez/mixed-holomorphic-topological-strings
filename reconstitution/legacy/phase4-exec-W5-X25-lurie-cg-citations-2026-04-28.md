# Phase-4 EXEC W5-X25 — Lurie HA + Costello-Gwilliam Citation Completeness Audit

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Wave.** Wave-5 attack-heal-swarm, attacker X25.
**Mode.** Read-only. No commits. No TeX edits.

**Mandate.** Audit citation completeness to Lurie HA and Costello-
Gwilliam Vol I-II across the topological-strings manuscript proper:
`main.tex`, `theorem-lanes.tex`, `claim-strength-ledger.tex`,
`open-obligations.tex`, `appendix-*.tex`, `tate-*.tex`. Verify the
W5-A1 Heal-3 +3-line Quillen-equivalence remark inscription
preconditions at `rmk:E1-translation`.

---

## §1. Bibliography state (`main.tex` L5970-L6398)

The amsrefs `\bib{...}{...}` bibliography contains the following
entries directly relevant to Lurie HA and Costello / Costello-
Gwilliam:

| Bibkey | Type | Source | Line |
|---|---|---|---|
| `costello-renormalization` | book | Costello, *Renormalization and EFT*, AMS 170, 2011 | 6112 |
| `costello-li-quantum-bcov` | misc | Costello-Li, arXiv:1201.4501, 2012 | 6125 |
| `costello-li-open-closed-bcov` | misc | Costello-Li, arXiv:1505.06703, 2015 | 6134 |
| `costello-gwilliam` | book | Costello-Gwilliam, FAinQFT Vol. 1, CUP NMM 31, 2017 | 6142 |
| `costello-gwilliam-vol2` | book | Costello-Gwilliam, FAinQFT Vol. 2, CUP NMM 41, 2021 | 6154 |
| `costello-twistedM` | article | Costello, twisted M-theory | 6259 |
| `lurie-ha` | book | Lurie, *Higher Algebra*, IAS preprint, 2017 | 6370 |

**Verdict.** The bibliography contains both `lurie-ha` and
`costello-gwilliam-vol2`. **No missing entries** are needed for the
W5-A1 Heal-3 Quillen-equivalence inscription at
`rmk:E1-translation`. Severity-2 risk (missing bibliography entries
blocking inscription): **clean**.

---

## §2. Citation map (manuscript-wide)

`grep` over `main.tex theorem-lanes.tex claim-strength-ledger.tex
open-obligations.tex appendix-*.tex tate-*.tex`:

### §2.1 `lurie-ha` invocations (6 sites; all in `tate-T3`)

| Site | Citation form | Anchored claim |
|---|---|---|
| `tate-T3-quillen-equivalence.tex:136` | `\cite{lurie-ha}*{\S 7.5}` | Spaltenstein semi-model modification (boundedness restriction is harmless rmk) |
| `tate-T3-quillen-equivalence.tex:339` | `\cite{lurie-ha}*{A.3.7.6, A.3.7.10}` | Quillen equivalence => $\infty$-cat equivalence (proof of `cor:tate-bar-cobar-infinity`) |
| `tate-T3-quillen-equivalence.tex:371` | `\cite{lurie-ha}*{\S 5.5}` | Symmetric monoidal $\infty$-cat lift (`cor:tate-lie-bar-cobar`) |
| `tate-T3-quillen-equivalence.tex:454` | `\cite{lurie-ha}*{Th.~7.1.4.6}` | Quillen equivalence of $E_n$-monoidal model cats => module $\infty$-cat equivalence (proof of `thm:open-closed-derived-center-derived`) |
| `tate-T3-quillen-equivalence.tex:473` | `\cite{lurie-ha}*{\S 5.5.5}` | Higher-algebraic Koszul duality (`rmk:lurie-koszul`) |
| `tate-T3-quillen-equivalence.tex:552` | `\cite{lurie-ha}*{\S 5.5.4}` | Locally constant FA on $\R$ <=> $E_1$-algebra (proof of `prop:weiss-cosheaf-residual`) |

**Inline (non-cite) Lurie HA reference.**

* `main.tex:2232` — `rmk:E1-translation`: prose form *"Lurie,
  Higher Algebra, §5.5.4"* (no `\cite{lurie-ha}` invocation; cited
  as inline emphasis).

### §2.2 `costello-gwilliam` (Vol I) invocations (4 sites)

| Site | Citation form | Anchored claim |
|---|---|---|
| `main.tex:2050` | `\cite{costello-gwilliam}*{Vol.~I \S 6.4}` | Locally constant FA vocabulary (preceding `rmk:E1-translation`) |
| `main.tex:2234` | `\cite{costello-gwilliam}*{Vol.~I \S 6.4}` | Locally constant FA vocabulary (inside `rmk:E1-translation`) |
| `main.tex:5180` | `\cites{costello-gwilliam,costello-gwilliam-vol2}` | Quantum observables form a factorization algebra (Costello perturbative BV stmt) |
| `tate-T3-quillen-equivalence.tex:553` | `\cite{costello-gwilliam}*{Vol.~I \S 6.4}` | Same vocabulary parallel to Lurie §5.5.4 (proof of `prop:weiss-cosheaf-residual`) |

### §2.3 `costello-gwilliam-vol2` invocations (1 site, joined)

| Site | Citation form | Anchored claim |
|---|---|---|
| `main.tex:5180` | `\cites{costello-gwilliam,costello-gwilliam-vol2}` | Quantum observables FA |

### §2.4 `costello-renormalization` invocations (10 sites)

`main.tex:5178, 5329`; `tate-P1:23, 31, 68, 92, 131, 202`;
`tate-T1:68, 300, 318, 338, 370, 539`; `tate-T3:518`. Locations
mostly cite *Ch.~5* (heat-kernel parametrix) or *Chs.~5--7*
(regulator package) or *Ch.~6* (RG flow) -- all chapter-level,
which is the appropriate granularity for Costello 2011's chapter
structure.

### §2.5 `costello-li-quantum-bcov` invocations (3 sites)

`main.tex:1664`; `tate-T2:505`; `tate-T4:29, 145`. Cited as
imported BCOV / Costello-Li theorem.

### §2.6 `costello-li-open-closed-bcov` invocations (4 sites)

`main.tex:5190`; `tate-T4:48, 82, 175`. Cited as imported flat
open-closed BCOV theorem.

### §2.7 `costello-twistedM` invocations (3 sites)

`tate-P3:14`; `tate-T4:75, 164`. Cited as physical motivation
for twisted M-theory protected sector.

---

## §3. Theorem-status anchoring audit

**Tate-T3 (Quillen equivalence) Lurie citations.** All six `tate-T3`
Lurie citations are precise to section / theorem level:

| Reference | Precision | Verdict |
|---|---|---|
| `\S 7.5` | section-level (Spaltenstein) | **PRECISE** |
| `A.3.7.6, A.3.7.10` | theorem-level | **PRECISE** |
| `\S 5.5` | section-level (sym monoidal) | acceptable section-level granularity |
| `Th.~7.1.4.6` | theorem-level | **PRECISE** |
| `\S 5.5.5` | subsection-level | **PRECISE** |
| `\S 5.5.4` | subsection-level | **PRECISE** |

**Costello-Gwilliam.** All four citations specify *Vol.~I \S 6.4*
(or both Vol I + Vol II at `main.tex:5180`). Section-level
granularity matches the published volumes. **PRECISE**.

**Costello (renormalization).** Chapter-level (Ch.~5; Chs.~5-7;
Ch.~6) citations match Costello 2011 chapter structure.
**PRECISE** at chapter granularity.

**Severity-1 (imprecise theorem-status anchoring): clean.**

---

## §4. Wave-5 inscription requirement check

**W5-A1 Heal-3 specification.** Per
`reconstitution/phase4-exec-W5-A1-costello-rescan-2026-04-28.md`
L650-660 and L773-775, the proposed inscription is:

> *Quillen equivalence of presentations.* The Lurie HA §5.5.4.10
> equivalence and the Costello-Gwilliam Vol I §6.4 vocabulary are
> related by the standard Quillen equivalence (Lurie HA §A.3.7;
> Costello-Gwilliam Vol II §A.5). Bousfield localisations such as
> $\tau_{\mathfrak h}$ defined in the Lurie HA $\infty$-category
> transfer to the CG combinatorial setting via this equivalence.

This is to be inscribed at `main.tex:2245-2246`, immediately before
the closing `\end{rmk}` of `rmk:E1-translation`. W5-X4 confirmed:

* Lurie HA Theorem **A.3.7.5** (combinatorial / simplicial Quillen
  equivalence; theorem-status);
* Costello-Gwilliam Vol II Corollary **A.5.0.5** (cosheaf-on-Ran
  Quillen equivalence; theorem-status).

**Current state of `rmk:E1-translation` (`main.tex:2229-2246`).**

```latex
\begin{rmk}[Locally constant equivalence and $E_1$-algebra translation]\label{rmk:E1-translation}
  In the locally constant setting on $\R$, factorization algebras are
  equivalent to homotopy associative algebras up to translation
  invariance by Lurie, \emph{Higher Algebra}, \S 5.5.4, in the
  Costello--Gwilliam vocabulary of locally constant factorization
  algebras \cite{costello-gwilliam}*{Vol.~I \S 6.4}. The Hochschild ...
\end{rmk}
```

**Verdict.** The remark currently cites:

* Lurie HA §5.5.4 (inline, prose form, no `\cite{lurie-ha}`) -- the
  $E_1$-algebra equivalence;
* CG Vol I §6.4 (`\cite{costello-gwilliam}`) -- the locally constant
  FA vocabulary.

The remark **does NOT yet cite Lurie HA A.3.7.5 or CG Vol II A.5.0.5**.
The Heal-3 +3-line Quillen-equivalence inscription is **proposed but
not inscribed**. Bibliography preconditions are met (`lurie-ha` and
`costello-gwilliam-vol2` are both already in the bibliography); the
inscription itself remains a Phase-5 task per
`reconstitution/phase4-exec-W5-A1-costello-rescan-2026-04-28.md`
R-P4-W5-A1-02.

**Severity-2 (missing bibliography entries blocking inscription):
clean.** The bibkeys `lurie-ha` and `costello-gwilliam-vol2` exist;
the inscription needs only prose, not new bibitems.

---

## §5. Cross-volume citation hygiene

### §5.1 Vol III (`~/calabi-yau-quantum-groups`)

Vol III bibliography (`bibliography/references.tex`) uses bibkey
`LurieHA` (line 179) and several Costello-Gwilliam aliases:
`CostelloGwilliam` (L93), `CostelloGwilliam2017` (L426),
`CostelloGwilliam2` (L860). Vol III citations consistently
specify theorem / section number:

* `\cite[HA~5.5.3]{LurieHA}` (cy_to_chiral.tex:1668)
* `\cite[Theorem~5.1.2.2]{LurieHA}` (cy_to_chiral.tex:5348;
  hochschild_calculus.tex:692)
* `\cite[Section~7.3]{LurieHA}` (cy_to_chiral.tex:5385)
* `\cite[Theorem~5.3.1.30]{LurieHA}` (quantum_chiral_algebras.tex:2589, 2599)
* `\cite[\S 6.1.1--6.1.2]{CostelloGwilliam}` (toric_cy3_coha.tex:921)

**Cross-volume note.** Vol III uses different bibkey conventions
(`LurieHA` vs. topological-strings's `lurie-ha`; `CostelloGwilliam`
vs. `costello-gwilliam`). This is bibkey-style divergence, not a
content firewall violation. Vol III's citation precision (named
theorem / proposition / section numbers) matches topological-
strings's `tate-T3` precision.

### §5.2 Chiral-bar-cobar (`~/chiral-bar-cobar`)

Bibliography contains `costello-renormalization` (L344) and
`gwilliam-thesis` (L721); no `lurie-ha` / `LurieHA` bibitem found.
Not relevant to the topological-strings citation hygiene firewall.

---

## §6. Convergence verdict

| Audit dimension | Verdict |
|---|---|
| §1 Bibliography state | clean (`lurie-ha`, `costello-gwilliam-vol2` present) |
| §2 Citation map | 30+ sites recorded across 7 file families |
| §3 Theorem-status precision | **PRECISE** (clean) |
| §4 W5-A1 Heal-3 preconditions | **bibliography clean**, inscription pending Phase-5 |
| §5 Cross-volume comparison | Vol III precision matches; bibkey divergence noted |

**Severity-1 (imprecise theorem-status anchoring): clean.**
**Severity-2 (missing bibliography entries blocking inscription): clean.**

**Certify.** The topological-strings manuscript's Lurie HA / Costello
/ Costello-Gwilliam citation hygiene is at the precision level
expected for the W5-A1 Heal-3 +3-line Quillen-equivalence
inscription at `rmk:E1-translation`. The inscription itself is the
remaining Phase-5 task; this report is read-only and does not
inscribe.

---

## §7. Inputs read

* `main.tex` (full bibliography L5970-L6398; targeted
  `rmk:E1-translation` L2229-2246; targeted Costello stmts
  L5170-5194; line 642, 1664, 2050).
* `tate-T3-quillen-equivalence.tex` (full Lurie citation contexts
  L120-590).
* `tate-T1, T2, T4, P1, P3` (citation-site context only).
* `claim-strength-ledger.tex`, `open-obligations.tex`,
  `theorem-lanes.tex` (named references; no `\cite{lurie-ha}` /
  `\cite{costello-gwilliam}` invocations found).
* `reconstitution/phase4-exec-W5-A1-costello-rescan-2026-04-28.md`
  (Heal-3 specification; R-P4-W5-A1-02 inscription queue).
* `reconstitution/phase4-exec-W5-X4-second-order-A1-2026-04-28.md`
  (W5-X4 confirmation of A.3.7.5 + A.5.0.5 as theorem-status).
* `~/calabi-yau-quantum-groups/bibliography/references.tex`
  (sister-volume bibkey hygiene).
* `~/calabi-yau-quantum-groups/chapters/theory/hochschild_calculus.tex`,
  `cy_to_chiral.tex`, `quantum_chiral_algebras.tex` (sample of
  Vol III citation precision).
* `~/chiral-bar-cobar/bibliography/references.tex` (negative
  result -- no `lurie-ha`).

No commits. No TeX edits. Read-only audit.
