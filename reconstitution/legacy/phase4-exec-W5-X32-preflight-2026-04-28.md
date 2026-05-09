# Phase-4 EXEC W5-X32 — Pre-Publication Preflight Auditor

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Mode.** Wave-5 attack-heal swarm wave 5; **read-only**;
proposal-only; no commits, no edits to any TeX file.
**Lens.** W5-X32 = pre-publication preflight checklist. Surface
remaining publication-grade gaps for the 155-page manuscript at
ACCEPT-WITH-MINOR-REVISIONS state per W5-X21 referee simulation.
**Baseline.** `out/main.pdf` (1,029,808 bytes, 156 pages by current
build; 155 pages cited at W5-X21 baseline). `main.tex` 6,402 lines.

---

## §0. Executive verdict

**Aggregate severity.** SEVERITY-1 publication improvement opportunities
across four checklist items (no severity-2 publication blocker).
The manuscript is referee-publishable in current form; the items
below are pre-submission recommendations the editor would normally
ask the author to address before galley.

**Severity ledger.**

| ID | Item | Severity | Action class |
|----|------|----------|--------------|
| X32.1 | Abstract length ~ 260 text-words | 0 | CERTIFY (within target) |
| X32.2 | No `\keywords{}`, no MSC-2020 block | 1 | PROPOSE (additive) |
| X32.3 | Title accurately reflects content | 0 | CERTIFY |
| X32.4 | `pdftitle` and `pdfauthor` set; `pdfsubject`, `pdfkeywords` empty | 1 | PROPOSE (additive) |
| X32.5 | 156 pages within Inventiones / GT / JHEP scope | 0 | CERTIFY |
| X32.6 | Stray build artifacts at repo root | 1 | PROPOSE (housekeeping) |
| X32.7 | No acknowledgements / funding section | 1 | PROPOSE (sole author; add as appropriate) |

No severity-2 (publication blocker) items found. Cumulative severity-1
items: four additive improvements, all closeable by a single
preflight inscription pass.

---

## §1. Abstract audit (X32.1)

**File.** `/Users/raeez/topological-strings/abstract.tex` (45 lines,
single environment `\begin{abstract}...\end{abstract}`, no subdivision).

**Word count after LaTeX-stripping.** ~260 text-words counting
prose tokens only (not counting math placeholders or punctuation).
Raw `wc -w` reports 273 words including LaTeX command tokens, 272
after a coarse strip. The reproducible Python tokenizer (strip
display + inline math, replace `\operatorname/\mathcal/\mathfrak`
with their argument, drop residual commands) yields **260 prose
words**.

**Journal-target convention.** Inventiones: typical abstract
≤250 words; tolerated up to ~300. Comm. Math. Phys.: typical
≤200 words. Geom. Topol.: typical ≤300 words. arXiv: ≤1920
characters (~300 words). At 260 prose words, the abstract is:
- within Inventiones tolerance (slightly over the "typical"
  but within editorial tolerance);
- over CMP typical;
- within Geom. Topol. typical;
- within arXiv hard limit.

**Standalone-document discipline.** The abstract reads as standalone:
it states the local model, names the BV/Koszul reduction, names the
$P_0$-factorisation-centre exclusion, names the Matlis residue-current
decomposition $\mathcal P = \bigoplus_{a+b>0}\C\rho_{a,b}$, lists the
proved-to-stated-status sectors, and lists the not-asserted sectors.
A non-specialist reader can extract the precise set of theorems
proved versus open from the abstract alone. No external-document
references, no orphan citation markers.

**Structure.** Single paragraph in source; renders as two paragraphs
in the PDF (the `\[...\]` display breaks). Paragraph 1: setup +
exclusion of unreduced $P_0$-centre + Matlis decomposition.
Paragraph 2: status ledger across the eight proved/conditional/not-asserted
sectors.

**Verdict.** **CERTIFY** (severity-0). Length within target; reads
standalone; status vocabulary uniform with `claim-strength-ledger.tex`.
No revision required for arXiv or Geom. Topol.; if targeting CMP,
consider trimming by ~50 words.

---

## §2. Keywords / MSC-2020 audit (X32.2)

**Direct grep.** `grep -in "MSC\|keyword\|subjclass\|pdfsubject\|pdfkeywords"`
across `main.tex`, `preamble.tex`, `commands.tex`,
`raeez-math-template.sty` returns: **no matches**. The manuscript
has no `\keywords{}` block, no `\subjclass{}` block, no MSC-2020
classification.

**Severity-1 improvement opportunity.** Most journal submission
forms require both. The arXiv submission also benefits from
explicit MSC + keyword tagging for indexing.

**Proposed keywords (Russian-school, named-construction-bearing,
not buzzword-y).**
- BCOV / Kodaira–Spencer gravity
- Hamiltonian BF theory
- Dirac brane probe
- formal symplectic disk
- BV/Koszul reduction
- factorisation-centre / $P_0$-centre
- Chevalley–Eilenberg cohomology
- Grothendieck–Matlis residue currents
- Weyl/Moyal quantisation
- $U(1)$ scalar anomaly
- Capelli shift
- Costello graph normalisation
- mixed holomorphic-topological field theory

**Proposed MSC-2020 codes.**
- **Primary.** 81T20 (Quantum field theory on curved space backgrounds /
  including topological field theory) — Hamiltonian BF on the formal
  symplectic disk.
- **Primary.** 53D55 (Deformation quantization, star products) — Moyal
  quantisation of the symplectic disk and the Capelli/Weyl comparison.
- **Secondary.** 81T70 (Quantization in field theory; cohomological
  methods) — BV/Koszul brane reduction and the $U(1)$ anomaly cocycle.
- **Secondary.** 17B66 (Lie algebras of vector fields and related
  $(super)$ algebras) — Hamiltonian Lie algebra of the formal disk.
- **Secondary.** 17B56 (Cohomology of Lie (super)algebras) —
  Chevalley–Eilenberg cochain calculation $C^\bullet_{\mathrm{CE}}(\mathfrak h)$.
- **Secondary.** 81Q60 (Supersymmetric methods in quantum mechanics) —
  ghost-zero BV / antifield $\psi=A^*$.
- **Secondary.** 81T75 (Noncommutative geometry methods in QFT) —
  matrix probe stack and large-$N$.
- **Secondary.** 14F10 (Differentials and other special sheaves;
  $D$-modules) — Matlis principal-part decomposition.

The two listed in the task brief (17B69, 17B05) are reasonable
secondaries but apply less directly: 17B69 (vertex operator algebras)
is more central in the Vol III CY-to-chiral frontier than here; 17B05
(structure of finite-dimensional Lie superalgebras) is too narrow for
the infinite-dimensional Hamiltonian Lie algebra at issue.

**Inscription site (proposal only).** Insert a `\subjclass[2020]{...}`
+ `\keywords{...}` block in `main.tex` between line 12 (`\date{...}`)
and line 14. amsart `\subjclass` is canonical; for the memoir
documentclass, a custom `\providecommand{\subjclass}[2][2020]{...}`
in `commands.tex` is a one-liner adapter.

**Verdict.** **PROPOSE** (severity-1). Additive, no theorem
modification. Closeable in a single 5-line preflight commit.

---

## §3. Title structure audit (X32.3)

**Title.** "Closed Hamiltonian BF Theory as the Derived Poisson
Center of a Dirac Brane Probe: A formal local mixed
holomorphic-topological model on $\R^2 \times \C^2$".

**Russian-school discipline check.**
- "Closed Hamiltonian BF Theory" — named construction.
- "Derived Poisson Center" — named categorical object.
- "Dirac Brane Probe" — named physics construction (Dirac
  constrained mechanics on a probe stack).
- "Formal local mixed holomorphic-topological model on $\R^2 \times \C^2$" —
  precise geometric setting.

No buzzwords (no "novel", "unified", "framework", "AI",
"machine-learning", "twisted M-theory", "string-theoretic"
abstract-level claims). All four named objects in the title appear
in the abstract: closed Hamiltonian BF action via the Tate Lie
algebra $\mathfrak g = \widehat{\mathfrak h} \ltimes \mathfrak h^\vee[1]$;
Derived Poisson Centre via the reduced CE/PV Hamiltonian
central-operation model; Dirac Brane Probe via the Dirac first-order
action $\int_\R \mathrm{Tr}(\phi_1\,d\phi_2 + A[\phi_1,\phi_2])$;
mixed local model on $\R^2 \times \C^2$ as the geometric setting.

**texorpdfstring split.** The PDF version uses
`R2 x C2` as the ASCII fallback for screen readers and PDF outline
display, with `\R^2\times\C^2` for typeset display. Both renderings
correctly identify the underlying space.

**Verdict.** **CERTIFY** (severity-0). Title is precise,
named-construction-bearing, and accurately summarises the abstract.
No revision recommended.

---

## §4. PDF metadata audit (X32.4)

**Direct check via pdfinfo on `out/main.pdf`.**
- **Title.** "Closed Hamiltonian BF Theory as the Derived Poisson
  Center of a Dirac Brane Probe: A formal local mixed
  holomorphic-topological model on R2 x C2" — CORRECT.
- **Author.** "Raeez Lorgat" — CORRECT.
- **Subject.** *empty* — MISSING.
- **Keywords.** *empty* — MISSING.
- **Creator.** "LaTeX with hyperref".
- **Producer.** "pdfTeX-1.40.27".

**Source.** `main.tex` line 34-37 sets `\hypersetup{pdftitle, pdfauthor}`.
`raeez-math-template.sty` line 665-670 wraps an
`\AtBeginDocument` redundancy that mirrors the same two fields. Neither
sets `pdfsubject` or `pdfkeywords`.

**Severity-1 improvement opportunity.** arXiv and many journal
submission portals harvest `pdfsubject` and `pdfkeywords` for
indexing. ORCID-aware platforms read these fields.

**Proposed inscription.** Extend the `\hypersetup` block in `main.tex`
line 34-37 (or in `raeez-math-template.sty` line 665-670) to:
```
\hypersetup{
  pdftitle={Closed Hamiltonian BF Theory as the Derived Poisson Center of a Dirac Brane Probe},
  pdfauthor={Raeez Lorgat},
  pdfsubject={Mathematical physics; topological string theory; BV-BRST quantisation; Hamiltonian BF on the formal symplectic disk},
  pdfkeywords={BCOV; Kodaira-Spencer gravity; Dirac brane probe; factorisation centre; Moyal quantisation; Matlis residue currents; U(1) anomaly}
}
```

**Verdict.** **PROPOSE** (severity-1). Additive, no functional change.
Closeable in a single 4-line preflight commit.

---

## §5. Page count target (X32.5)

**Current snapshot.** `pdfinfo /Users/raeez/topological-strings/out/main.pdf`
reports **156 pages** (1,029,808 bytes, dated 2026-04-28 23:28).
The W5-X21 referee-simulation baseline cites 155 pages (a 1-page
fluctuation between rebuilds is expected from float placement).
The root-level `main.pdf` is 154 pages, dated 2026-04-28 08:09 — an
older build snapshot; the canonical release is `out/main.pdf`.

**Journal scope assessment.**
- **Inventiones Mathematicae** — tolerates long monographs (50-200pp typical for
  major papers). 156pp within scope.
- **Comm. Math. Phys.** — historically caps at 60-80pp for ordinary
  articles. 156pp would require special-handling negotiation with
  the editor or split into two papers.
- **Geom. Topol.** — tolerates long (100-200pp common). 156pp
  within scope.
- **Adv. Math.** — tolerates long. 156pp within scope.
- **JHEP** — tolerates very long (100-300pp common in mathematical
  physics). 156pp within scope.
- **Selecta Math.** — tolerates long. 156pp within scope.

**Verdict.** **CERTIFY** (severity-0) for Inventiones / Geom. Topol. /
JHEP / Adv. Math. / Selecta. Severity-1 narrative gap for CMP
(would require splitting or editorial negotiation). The repository
voice and content profile match the mathematical-physics
mathematics-monograph register; Inventiones, Geom. Topol., or Adv.
Math. are the natural targets. JHEP is appropriate for a
physics-side companion submission with adjusted prose.

---

## §6. arXiv submission readiness (X32.6)

**Stray build artifacts at repo root.**
```
/Users/raeez/topological-strings/main.aux
/Users/raeez/topological-strings/main.idx
/Users/raeez/topological-strings/main.log
/Users/raeez/topological-strings/main.toc
/Users/raeez/topological-strings/frontier_mnop_framing_volume.aux
/Users/raeez/topological-strings/frontier_mnop_framing_volume.idx
/Users/raeez/topological-strings/frontier_mnop_framing_volume.log
```

Plus the `out/` and `out_test/` build directories. The Makefile
`TEXFLAGS := -output-directory=out` redirects new builds, so these
seven root-level files are residual from a non-redirected build pass
(or the `frontier_*` standalone). They are not committed (per `git
status`); arXiv tarballing would respect `.gitignore` if used.

**Makefile clean target.** Lines 326-328:
```
clean:
    -$(KILL) $(TEXDEBRIS)
    -$(CD) $(OUTDIR); $(KILL) $(TEXDEBRIS)
```
where `TEXDEBRIS := *.toc *.ilg *.log *.nlo *.dvi *.aux *.tar.gz *.nlo *.nls *.nls *.out *.toc *.sta *.gla *.fdb_latexmk *.fls *.synctex.gz`.

This works; `make clean` removes the seven stray root artifacts plus
the `out/` debris. No `*.idx` in the debris list — that explains
the `main.idx` and `frontier_mnop_framing_volume.idx` survival.

**arXiv source upload checklist.**
1. `make clean` to remove `*.aux`, `*.log`, `*.toc`, `*.out`, etc.
2. **NOT** in current `TEXDEBRIS`: `*.idx` files. Add `*.idx` to the
   debris list (severity-1).
3. Tarball the manuscript: `main.tex`, `abstract.tex`,
   `claim-strength-ledger.tex`, `local-dictionary.tex`,
   `principles.tex`, `theorem-lanes.tex`, `open-obligations.tex`,
   `mathmacros.tex`, `commands.tex`, `notation.tex`, `nomenclature.tex`,
   `preamble.tex`, `authors.tex`, `raeez-math-template.sty`, the
   nine appendix and tate-* files, `firstorder.{png,svg}`,
   `thirdorder{a,b}.{png,svg}`.
4. arXiv compiles with `pdflatex` (matches Makefile choice).
5. arXiv requires no `\input` of nonexistent files; verify no
   missing `tate-T*` or `appendix-*` after rename.
6. The `frontier_mnop_framing_volume.tex` is a separate standalone
   not part of `main.tex`; exclude from the tarball.

**Build instructions clarity.** The Makefile `pdf` target runs
`pdflatex` 7 times with `make index` interleaved (matching memoir +
nomencl conventions). arXiv's autobuild typically runs 2-3 passes;
`main.toc` and `main.aux` should converge by pass 3. **Severity-1**:
the README at `/Users/raeez/topological-strings/README.md` is the
generic `amstex-template` README, not specific to this manuscript.
A short `INSTALL.md` or arXiv-specific build note would help.

**Verdict.** **PROPOSE** (severity-1). Two minor cleanups:
add `*.idx` to `TEXDEBRIS` in `Makefile`; provide an arXiv-specific
README or build-note. Closeable in a 5-line preflight commit.

---

## §7. Acknowledgements section audit (X32.7)

**Direct grep.** `grep -in "thank\|acknowledg\|funding\|grant\|gratitude"`
across `main.tex`, `abstract.tex`, `authors.tex` returns **no matches**.

The manuscript has no acknowledgements section, no funding statement,
no thanks, no gratitude. `authors.tex` carries only:
```
\author{Raeez Lorgat}
\email{root@raeez.com}
\urladdr{http://math.raeez.com}
```

**Severity-1 improvement opportunity.** This is a stylistic gap, not
a publication blocker. Most journal submissions ask the author to
indicate any external funding, institutional affiliation, and
intellectual debts. The W5-X28 authorship audit certified no LLM
attribution; that part is clean.

**Russian-school stylistic note.** Bershadsky-Cecotti-Ooguri-Vafa
1993 (the source-convention template), Witten 1988, Costello 2011,
Polyakov 1987, Costello-Gwilliam, Beilinson, Drinfeld, Kazhdan,
Etingof, Gaiotto are all cited in the bibliography with full
attribution; intellectual lineage is acknowledged through citation.
The absence of an explicit acknowledgements section is internally
consistent with the sole-author no-grant register.

**Inscription proposal (sole author, optional but standard).**
Insert at the very end of section "Outlook and convention firewalls"
or as a short un-numbered section before `\appendix`:
```
\section*{Acknowledgements}
The author thanks [list of people who provided technical input
or who read drafts]. Errors are the author's. This work received
no external funding.
```

If no people are appropriate to thank, an explicit single-sentence
funding statement still carries information for the editor: "This
work received no external funding."

**Verdict.** **PROPOSE** (severity-1). Optional but standard;
sole-author convention requires only a brief funding statement at
minimum.

---

## §8. Cross-checklist summary

**Severity ledger (closing).**

| Item | Severity | Closure cost |
|------|----------|--------------|
| X32.1 Abstract length | 0 | None |
| X32.2 MSC-2020 + keywords | 1 | +5 lines `main.tex` |
| X32.3 Title structure | 0 | None |
| X32.4 PDF metadata | 1 | +4 lines `main.tex` |
| X32.5 Page count | 0 | None for IM/GT/AdvMath/JHEP; -50pp for CMP |
| X32.6 Build artifacts | 1 | +1 line `Makefile`; ~10 lines arXiv README |
| X32.7 Acknowledgements | 1 | +5 lines `main.tex` |

**Aggregate.** Four severity-1 items, total inscription footprint
~25 lines. No severity-2 publication blocker.

**Recommendation.** A single preflight inscription pass (W5-X33 or
beyond) closing X32.2, X32.4, X32.6, X32.7 transitions the
manuscript from ACCEPT-WITH-MINOR-REVISIONS (per W5-X21) to a clean
SUBMIT-READY state. The pass is purely additive; no theorem
statement modified, no proof modified, no figure modified.

**Out-of-scope severity-0 acknowledgements.** Title, abstract,
voice, length, body content, citation completeness — all certified
clean.

End of Phase-4 EXEC W5-X32 preflight audit.
