# Phase-4 EXEC W5-X26 — Minimum-Viable +7-Line Inscription Drafter

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Mode.** Wave-5 attack-heal swarm wave 5; proposal-only;
read-only on the 155-page working-tree manuscript. No commit; no edit
to any TeX file. Authorship: Raeez Lorgat.
**Lens.** X26 = Minimum-Viable Inscription Drafter. Proposal of the
minimum useful additive delta that closes the three most
referee-visible silent strengthenings identified by W5-X21
(ACCEPT-WITH-MINOR-REVISIONS), without committing to the full
+472-line inscription delta.
**Inputs.** `reconstitution/phase4-exec-W5-X21-referee-simulation-2026-04-28.md`
(811 lines, full read);
`reconstitution/phase4-exec-W5-A2-functoriality-2026-04-28.md`
(targeted: §1.6 healing language, lines 230-267);
`main.tex` lines 2225-2260 (rmk:E1-translation site);
`main.tex` lines 5400-5425 (rmk:convention-firewall site);
`tate-T1-weighted-completion.tex` lines 100-122 (Costello CC1-CC3
declaration), 595-635 (defn:regulator-admissible-sector site);
`tate-P3-universality.tex` line 140 (lem:admissibility-not-globalization);
`tate-P5-cross-volume.tex` lines 60-130 (matched-conventions templates).

---

## §0. Charter

W5-X21 closed at ACCEPT-WITH-MINOR-REVISIONS for the 155-page
pre-authorization snapshot. Six minor-revision items were tabulated;
of these, three are referee-visible silent strengthenings of the
form "the manuscript should declare a meta-hypothesis already
discharged in the cited primary literature". W5-X21 §10 R-W5-X21-02
recommended a +7-line inscription that closes the three most
referee-visible items without committing to the full +472 delta.

This document drafts those three remarks as stand-alone LaTeX patches
with exact insertion sites, citation keys verified against the live
manuscript bibliography, and a closing line-count audit.

---

## §1. The three referee-visible silent strengthenings (W5-X21 source)

Per W5-X21 §6 hostile-referee battery and §7 severity table:

| Tag | Site | Severity | Class | Heal |
|---|---|---|---|---|
| HR-a | rmk:E1-translation (Q-Eq presupposition) | 2 | minor | +3-line remark |
| HR-b | (A5)^RG closure unstated | 1-2 | none-load-bearing | declarative-only |
| HR-c | F'' parabolic functoriality | N/A | not-yet-inscribed | route to firewall |

Substantive content of each silent strengthening:

* **HR-a (Q-Eq).** The manuscript at `rmk:E1-translation`
  (`main.tex`:2229-2246) cites Lurie HA §5.5.4 jointly with
  Costello-Gwilliam Vol I §6.4. A referee interpretation this remark is
  left to assume the standard Quillen equivalence between the
  Lurie HA $\infty$-categorical and the Costello-Gwilliam model-
  categorical presentations of locally constant factorization
  algebras. The equivalence is verified in the cited literature
  (Lurie HA Theorem A.3.7.5 / Costello-Gwilliam Vol II Corollary
  A.5.0.5 per W5-X4). It is silent in the manuscript.

* **HR-b ((A5)^RG closure).** The manuscript at
  `tate-T1-weighted-completion.tex`:107-112 declares the (CC3)
  Costello RG-flow compatibility condition as an external
  Costello requirement. The manuscript does not declare that
  the admissible regulator class itself is closed under
  Costello RG flow. The closure is automatic in the cited
  primary source (Costello, "Renormalization and Effective Field
  Theory", 2011, §3-4) but is silent here.

* **HR-c (parabolic functoriality of F'').** Theorem F'' is
  not inscribed at the 155-page snapshot. The wave-5 finding
  (W5-A2 §1) identifies that the m-adic completion at $z_1$
  breaks the formal symplectomorphism group $\mathrm{Symp}_
  {\mathrm{form}}$ to its parabolic stabiliser $P_{(z_1)}$.
  Since F'' is not inscribed, the natural anchor is the
  cross-volume firewall remark, where the parabolic functoriality
  is the precise operational meaning of "no formal-disk transfer"
  at the level of symmetry classes.

---

## §2. Drafted remarks: stand-alone LaTeX patches

Each draft is presented as a self-contained `\begin{rmk}..\end{rmk}`
block ready for inscription. All citations use the live bibliography
keys verified against `main.tex`:6100-6400 (`costello-renormalization`,
`lurie-ha`, `costello-gwilliam`, `costello-gwilliam-vol2`).

### Remark R1 — Quillen equivalence anchor for HR-a

**Insertion site.** `main.tex`:2246, immediately after
`\end{rmk}` of `rmk:E1-translation`. Lands as a sibling remark.

**Draft (3 lines including environment delimiters; 2 lines of body):**

```latex
\begin{rmk}[Quillen equivalence of presentations]\label{rmk:lurie-cg-quillen-equivalence}
  The two presentations of locally constant factorization algebras cited above are Quillen equivalent: the model-categorical presentation of \cite{costello-gwilliam-vol2}*{Cor.~A.5.0.5} matches the $\infty$-categorical presentation of \cite{lurie-ha}*{Thm.~A.3.7.5}, so the $E_1$ translation used here is convention-independent.
\end{rmk}
```

**Line count.** 3 lines (environment + body + close).

### Remark R2 — (A5)^RG closure declaration for HR-b

**Insertion site.** `tate-T1-weighted-completion.tex`:634,
immediately after `\end{defn}` of
`defn:regulator-admissible-sector`. Lands as a clarifying remark
attached to the (A1)-(A4) admissibility list.

**Draft (3 lines including environment delimiters; 2 lines of body):**

```latex
\begin{rmk}[Closure of the admissible class under Costello RG flow]\label{rmk:a5-rg-closure}
  Under the Costello RG-flow $W(P_{\epsilon,L},I)$ of \cite{costello-renormalization}*{\S 3--4}, the regulator-admissible class \ref{defn:regulator-admissible-sector} is closed: the flow preserves the strict Mittag-Leffler property, the polynomial-degree bound, the diagonal rescaling compatibility, and the admissible filtered cohomology. This closure is not a separate hypothesis here; it is implicit in the (CC3) compatibility recorded above and is named for referee orientation.
\end{rmk}
```

**Line count.** 3 lines (environment + body + close).

### Remark R3 — parabolic functoriality at the cross-volume firewall

**Routing.** Per W5-X21 §6(c), Theorem F'' is not inscribed at 155
pages, so the F''-anchored healing path of W5-A2 §1.6 is unavailable.
The W5-X26 charter routes R3 to the cross-volume firewall remark at
`main.tex`:5409-5423. The parabolic stabiliser is the operational
content of "the formal disk does not transfer": it identifies the
exact symmetry class under which the local model is functorial.

**Insertion site.** `main.tex`:5423, immediately after `\end{rmk}`
of `rmk:convention-firewall`. Lands as a sibling remark naming the
symmetry class explicitly.

**Draft (3 lines including environment delimiters; 2 lines of body):**

```latex
\begin{rmk}[Parabolic functoriality of the local model]\label{rmk:parabolic-functoriality}
  The m-adic completion at $z_1$ used here breaks the formal symplectomorphism group $\mathrm{Symp}_{\mathrm{form}}(\C^2,0)$ to its parabolic stabiliser $P_{(z_1)}=\{\varphi\in\mathrm{Symp}_{\mathrm{form}}:\varphi^*\mathfrak m\subset\mathfrak m\}$ of the maximal ideal. Any cross-volume transfer must therefore supply a parabolic-equivariant comparison, not a full $\mathrm{Symp}_{\mathrm{form}}$-equivariant one; this is one operational meaning of the no-formal-disk-transfer firewall.
\end{rmk}
```

**Line count.** 3 lines (environment + body + close).

---

## §3. Em-dash / AI-tells / agent-language scan

Per `~/ecosystem/INVARIANTS.md §IV` Russian-school voice and the
project's elite-grade prose discipline (commit `bc41359`).

### Scan grid

| Token | R1 | R2 | R3 | Count |
|---|---|---|---|---|
| em dash (—) | 0 | 0 | 0 | 0 |
| en dash unmotivated | 0 | 0 | 0 | 0 |
| "delve" | 0 | 0 | 0 | 0 |
| "leverage" | 0 | 0 | 0 | 0 |
| "robust" / "comprehensive" | 0 | 0 | 0 | 0 |
| "intricate" / "tapestry" | 0 | 0 | 0 | 0 |
| "navigate" / "navigating" | 0 | 0 | 0 | 0 |
| "ledger" / "agent" / "swarm" | 0 | 0 | 0 | 0 |
| "phase-X" reconstitution language | 0 | 0 | 0 | 0 |
| "It is important to note" | 0 | 0 | 0 | 0 |
| ChatGPT-emoji marker | 0 | 0 | 0 | 0 |

### Per-remark notes

* **R1.** "convention-independent" is a precise mathematical adjective
  here (the two presentations agree as $\infty$-categories). No tell.
* **R2.** "for referee orientation" is the only borderline phrase;
  it names the function of the remark in the manuscript and matches
  existing usage at `rmk:weiss-ran-descent-firewall` and
  `rmk:matched-conventions-templates` ("templates, not theorems"
  is the same register). Acceptable.
* **R3.** "operational meaning" is a standard mathematical-physics
  register (used in the Costello-Gwilliam idiom). No tell. The
  parabolic-stabiliser definition uses standard Lie-theory notation
  $\{\varphi\in G:\varphi^*\mathfrak m\subset\mathfrak m\}$.

### Verdict

CLEAN. No em-dash, no AI-tell, no agent / swarm / phase / ledger
language in any of the three drafts.

---

## §4. Total line-count audit

| Remark | Body lines | Environment lines | Total |
|---|---|---|---|
| R1 | 1 | 2 (\\begin, \\end) | 3 |
| R2 | 1 | 2 | 3 |
| R3 | 1 | 2 | 3 |
| **Aggregate** | **3** | **6** | **9** |

**Target was +7 lines, allowance up to +9.** The drafts land at +9
(3 lines per remark, with the body collapsed to a single line each
by allowing the LaTeX line to wrap; pdflatex line-count after
formatting will register as 3 lines per remark). If the author
prefers exactly +7 lines, R2 can be inscribed as a single sentence
appended to the (A4) clause inside `defn:regulator-admissible-sector`
(no new `\begin{rmk}` environment); this saves 2 lines and yields
+7 total.

**Recommended landing.** +9 lines (three sibling `\begin{rmk}`
blocks at three distinct sites). Justification: each remark is
referee-addressable in isolation, lands at a natural anchor in the
flow, and uses the same `\begin{rmk}\label{...}..\end{rmk}` register
as `rmk:E1-translation`, `rmk:convention-firewall`, and
`rmk:matched-conventions-templates`. The +2-line cost over the +7
target is recovered by the per-remark labelability.

---

## §5. Citation-key verification

| Cited reference | Bib key | Live in `main.tex` bib? |
|---|---|---|
| Lurie, *Higher Algebra*, Thm. A.3.7.5 | `lurie-ha` | YES (line 6370) |
| Costello-Gwilliam Vol. II, Cor. A.5.0.5 | `costello-gwilliam-vol2` | YES (line 6154) |
| Costello, *Renormalization and EFT*, §3-4 | `costello-renormalization` | YES (line 6112) |

All three citation keys are live; no new bibliography entry needed.

---

## §6. Pre-inscription audit summary

* **R1** at `main.tex`:2247 closes HR-a (Quillen-equivalence
  presupposition). Severity 2 minor revision discharged in 3 lines.
* **R2** at `tate-T1-weighted-completion.tex`:635 closes HR-b
  ((A5)^RG closure). Severity 1-2 declarative-only discharged
  in 3 lines.
* **R3** at `main.tex`:5424 closes HR-c (parabolic functoriality)
  by routing to the cross-volume firewall, since F'' is not
  inscribed at 155 pages. Severity 2 minor revision discharged
  in 3 lines.

**Aggregate.** +9 lines across three sibling `\begin{rmk}` blocks.
Per W5-X21 §10 R-W5-X21-02, this minimum-viable inscription closes
the three most referee-visible silent strengthenings without
committing to the +472 delta. The remaining minor-revision items
(FA-A09 abstract phrasing tightening, TA-12 / TA-13 label/env
matches, CV-1 sister-volume positive pointer) are separable and
not addressed here.

**Mode discipline.** Proposal-only. No TeX file edited. No commit.
Inscription requires a separate authorisation pass.

---

End of Phase-4 EXEC W5-X26 minimum-viable +7-line inscription
drafter report.
