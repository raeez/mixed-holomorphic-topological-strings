# Phase-4 EXEC W5-X16: Standalone Apparatus Build Auditor

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Role.** Attacker W5-X16, attack-heal-swarm wave 5 (relaunch after
usage-cap interruption).
**Mode.** Read-only on the working tree; write-allowed only inside
`/tmp/w5x16r-build/` and the two reconstitution/ files mentioned in the
task spec.
**Target.** Verify per `INVARIANTS.md §III` that each apparatus file in
the manuscript root compiles standalone via `pdflatex` and produces a
non-empty PDF, document the apparatus dependency graph, and scan for
em-dashes, AI tells, and agent-language leaks.

Scope: `principles.tex`, `claim-strength-ledger.tex`,
`open-obligations.tex`, `theorem-lanes.tex`, `local-dictionary.tex`,
`abstract.tex`, four `appendix-*.tex`, and eight `tate-*.tex` files.
Total: 18 apparatus targets.

---

## 1. Build harness

### 1.1 Working directory and source inventory

`/tmp/w5x16r-build/` was populated with these sources copied from the
working tree:

- Apparatus targets (18): `principles.tex`,
  `claim-strength-ledger.tex`, `open-obligations.tex`,
  `theorem-lanes.tex`, `local-dictionary.tex`, `abstract.tex`,
  `appendix-factorization-current-conventions.tex`,
  `appendix-matlis-principal-parts.tex`,
  `appendix-radial-parts-moyal.tex`,
  `appendix-unreduced-bv-qme.tex`,
  `tate-P1-hadamard-mittag-leffler.tex`, `tate-P3-universality.tex`,
  `tate-P5-cross-volume.tex`, `tate-T1-weighted-completion.tex`,
  `tate-T2-nilpotent-truncation.tex`,
  `tate-T3-quillen-equivalence.tex`, `tate-T4-bv-vanishing.tex`,
  `tate-T5-chain-level-primitive.tex`.
- Shared prelude: `preamble.tex`, `commands.tex`, `mathmacros.tex`,
  `notation.tex`, `nomenclature.tex`, `authors.tex`,
  `raeez-math-template.sty`.
- Image assets: `firstorder.{png,svg}`, `thirdordera.{png,svg}`,
  `thirdorderb.{png,svg}`.

Excluded per task spec: `out/`, `out_test/`, `.agents/`, `.claude/`,
`.git/`, `materials/`, `scripts/`, `references/`, `reconstitution/`.

### 1.2 Driver template

Each apparatus file is wrapped in a per-target driver
`driver-<TARGET>.tex`. The driver mirrors `main.tex`'s actual
configuration (memoir 11pt, `raeez-math-template`,
`mathmacros.tex` + `authors.tex`, manuscript-section depth, appendix
counter rebinder, `tikz` libraries, and the two `\providecommand`
fallbacks `\alpharef` and `\Op`):

```latex
\documentclass[11pt]{memoir}
\usepackage{raeez-math-template}
\input{mathmacros.tex}
\input{authors.tex}
\title{Standalone build harness}
\date{April 28, 2026}
\renewcommand{\thesection}{\arabic{section}}
\renewcommand{\thesubsection}{\thesection.\arabic{subsection}}
\renewcommand{\thesubsubsection}{\thesubsection.\arabic{subsubsection}}
\setsecnumdepth{subsubsection}
\settocdepth{subsubsection}
\makeatletter
\let\ts@originalappendix\appendix
\renewcommand{\appendix}{ ... }
\makeatother
\hypersetup{ ... }
\usepackage{tikz}
\usetikzlibrary{arrows.meta, decorations.markings,
                positioning, calc, decorations.pathmorphing}
\providecommand{\alpharef}{\ref{lem:continuous-bar-cobar}}
\providecommand{\Op}{\mathcal{O}}
\begin{document}
\maketitle
\input{TARGET}
\end{document}
```

### 1.3 Compilation procedure

Engine: `pdflatex` (TeX Live 2025, pdfTeX 3.141592653-2.6-1.40.27).
Flags: `-interaction=nonstopmode -file-line-error`.
Passes per target: 3 (per task spec).
Per-target log files: `logs/<TARGET>-pass{1,2,3}.log`.

---

## 2. Per-target build certification

| Target                                              | Status                  | Pass1 | Pass2 | Pass3 | Pages | Bytes  |
|-----------------------------------------------------|-------------------------|-------|-------|-------|-------|--------|
| `principles.tex`                                    | PASS-WITH-WARNINGS      | 0     | 0     | 0     | 3     | 160140 |
| `claim-strength-ledger.tex`                         | PASS-WITH-WARNINGS      | 0     | 0     | 0     | 4     | 139915 |
| `open-obligations.tex`                              | PASS-WITH-WARNINGS      | 0     | 0     | 0     | 3     | 145235 |
| `theorem-lanes.tex`                                 | PASS-WITH-WARNINGS      | 0     | 0     | 0     | 6     | 168333 |
| `local-dictionary.tex`                              | PASS-WITH-WARNINGS      | 0     | 0     | 0     | 3     | 159556 |
| `abstract.tex`                                      | PASS                    | 0     | 0     | 0     | 1     | 100881 |
| `appendix-factorization-current-conventions.tex`    | PASS-WITH-WARNINGS      | 0     | 0     | 0     | 3     | 139997 |
| `appendix-matlis-principal-parts.tex`               | PASS-WITH-WARNINGS      | 0     | 0     | 0     | 6     | 164914 |
| `appendix-radial-parts-moyal.tex`                   | PASS-WITH-WARNINGS      | 0     | 0     | 0     | 5     | 149502 |
| `appendix-unreduced-bv-qme.tex`                     | PASS-WITH-WARNINGS      | 0     | 0     | 0     | 3     | 145742 |
| `tate-P1-hadamard-mittag-leffler.tex`               | PASS-WITH-WARNINGS      | 0     | 0     | 0     | 4     | 164304 |
| `tate-P3-universality.tex`                          | PASS-WITH-WARNINGS      | 0     | 0     | 0     | 3     | 154574 |
| `tate-P5-cross-volume.tex`                          | PASS                    | 0     | 0     | 0     | 2     | 114209 |
| `tate-T1-weighted-completion.tex`                   | PASS-WITH-WARNINGS      | 0     | 0     | 0     | 10    | 209976 |
| `tate-T2-nilpotent-truncation.tex`                  | PASS-WITH-WARNINGS      | 0     | 0     | 0     | 7     | 201249 |
| `tate-T3-quillen-equivalence.tex`                   | PASS-WITH-WARNINGS      | 0     | 0     | 0     | 7     | 198716 |
| `tate-T4-bv-vanishing.tex`                          | PASS-WITH-WARNINGS      | 0     | 0     | 0     | 3     | 139257 |
| `tate-T5-chain-level-primitive.tex`                 | PASS-WITH-WARNINGS      | 0     | 0     | 0     | 9     | 207617 |

**18/18 standalone-buildable.** No FAILs. No `! ` LaTeX errors in any
log. All exit codes 0 across all three passes. Authoritative page
counts verified via `pdfinfo`. Total 82 pages of standalone-rendered
apparatus.

### 2.1 Warning classification

Every warning falls into one of two non-load-bearing categories:

1. **Cross-fragment undefined references / citations.** The fragments
   are designed to be `\input{}`-ed into `main.tex`, where they share a
   common label namespace. Compiled standalone, each fragment can only
   resolve labels defined inside itself; references to labels living
   in `main.tex` body, in other apparatus fragments, or in the BibTeX
   bibliography raise "Reference ... undefined" / "Citation ...
   undefined" warnings. These are expected by the task spec and are
   not source defects. Spot-check verification: every undefined label
   sampled (`lem:dirac-probe-reduction`, `prop:open-bv-truncation`,
   `prop:one-psi-homology`, `thm:chain-level-primitive-projection`,
   `thm:pbw-vs-deformation`, `thm:no-polynomial-realization-categorical`,
   `thm:app-matlis-rees-fourier-bridge`, `prop:grav-ops`,
   `lem:linear-poisson-schouten`, `thm:open-closed-derived-center`,
   `lem:continuous-bar-cobar`) is present in `main.tex`,
   `appendix-matlis-principal-parts.tex`, or
   `tate-T5-chain-level-primitive.tex`.

2. **Minor underfull `\hbox` boxes.** `tate-T5-chain-level-primitive`
   shows two underfull boxes (lines 83--99 and 718--726, both
   typographic, badness 10000 and 2875). `tate-P3-universality`,
   `tate-P1-hadamard-mittag-leffler`,
   `appendix-radial-parts-moyal`, `tate-T1-weighted-completion`,
   `tate-T2-nilpotent-truncation`, `tate-T3-quillen-equivalence`, and
   `tate-T4-bv-vanishing` each show 1--3 underfull boxes. None are
   overfull beyond the normal ledger threshold; none affect content
   rendering. These are normal for a paragraph-flow document compiled
   without surrounding contextual material (e.g. without preceding
   sections feeding hyphenation breaks).

### 2.2 No-FAIL certification

Every apparatus file compiled in 3 passes with `pdflatex` exit code 0
and produced a non-empty PDF. No `! Undefined control sequence`, no
`! Missing $`, no `! LaTeX Error`, no `Runaway argument`, no
`! Emergency stop`. The apparatus is standalone-build clean.

---

## 3. Apparatus dependency graph

The driver reproduces the prelude `main.tex` actually loads:
`\usepackage{raeez-math-template}` then `\input{mathmacros.tex}` then
`\input{authors.tex}`. **No apparatus file requires `commands.tex`,
`notation.tex`, or `nomenclature.tex`** for its own command resolution
- those are legacy support files used inside the bibliographic body
of `main.tex` and not by any standalone apparatus file. The apparatus
loads only `mathmacros.tex` plus the `raeez-math-template` package
plus `tikz`+libraries plus the `\alpharef` and `\Op` `\providecommand`
fallbacks declared in `main.tex`.

Cross-reference graph (label definitions vs. external references):

| File                                            | Local label defs | Refs to others | Local cites |
|-------------------------------------------------|------------------|----------------|-------------|
| `principles.tex`                                | 1                | 3              | 0           |
| `claim-strength-ledger.tex`                     | 0                | 5              | 0           |
| `open-obligations.tex`                          | 1                | 10             | 0           |
| `theorem-lanes.tex`                             | 9                | 46             | 0           |
| `local-dictionary.tex`                          | 0                | 1              | 0           |
| `abstract.tex`                                  | 0                | 0              | 0           |
| `appendix-factorization-current-conventions.tex`| 7                | 5              | 0           |
| `appendix-matlis-principal-parts.tex`           | 11               | 5              | 3           |
| `appendix-radial-parts-moyal.tex`               | 12               | 7              | 0           |
| `appendix-unreduced-bv-qme.tex`                 | 5                | 2              | 0           |
| `tate-P1-hadamard-mittag-leffler.tex`           | 8                | 15             | 2           |
| `tate-P3-universality.tex`                      | 3                | 4              | 2           |
| `tate-P5-cross-volume.tex`                      | 4                | 0              | 0           |
| `tate-T1-weighted-completion.tex`               | 39               | 31             | 1           |
| `tate-T2-nilpotent-truncation.tex`              | 16               | 13             | 2           |
| `tate-T3-quillen-equivalence.tex`               | 14               | 14             | 11          |
| `tate-T4-bv-vanishing.tex`                      | 5                | 10             | 3           |
| `tate-T5-chain-level-primitive.tex`             | 19               | 31             | 0           |

**Hub fragments.** `theorem-lanes.tex` is the largest reference hub
(46 cross-fragment references): it acts as the proof-dependency index
for every theorem lane. `tate-T5-chain-level-primitive.tex` is the
second hub (31 references). `tate-T1-weighted-completion.tex` and
`tate-T5-chain-level-primitive.tex` are the largest definition hubs
(39 and 19 labels respectively).

**Self-contained fragments.** `abstract.tex` defines no labels, makes
no external references, and uses no citations - the only fully
self-sealed leaf. `tate-P5-cross-volume.tex` defines four labels and
makes no external references; it is also clean PASS.
`local-dictionary.tex` makes a single external reference (to
`thm:app-matlis-rees-fourier-bridge` in
`appendix-matlis-principal-parts.tex`).

**Dependency directionality.** The dominant direction is
*apparatus -> (`main.tex` body + Tate fragments + appendices)*. No
apparatus file is a forward target of `main.tex` body labels (every
apparatus reference points at a label defined in a fragment of equal
or higher depth, or in the manuscript body itself).

---

## 4. Em-dash, AI-tells, and agent-language scan

### 4.1 Em-dash scan (`---` and U+2014)

All 18 files: **0 em-dashes in prose**. Two ASCII `---` matches
appear, both inside LaTeX comments (`% --- End of fragment.` in
`tate-P3-universality.tex` line 212; `% --- End of appendix.` in
`tate-P5-cross-volume.tex` line 131). These are not rendered. No
Unicode U+2014 anywhere. **Em-dash invariant: clean.**

### 4.2 Agent-language scan

Pattern: `\b(agent|swarm|attack-heal|wave[0-9]|phase[0-9]|reconstitution|claude|codex|harness|adversarial|subagent|worktree)\b`.

All 18 files: **0 hits.** No agent infrastructure terminology bleeds
into apparatus prose.

The word `ledger` appears in `claim-strength-ledger.tex` (4 times,
all references to the published apparatus name "claim-strength
ledger"), in `open-obligations.tex` (2 times, same usage), and in
`theorem-lanes.tex` (1 time, "the claim-strength ledger"). These are
the formal apparatus name; this is the published Russian-school voice
referring to its own apparatus, not an LLM `ledger` artifact. **Voice
clean.**

### 4.3 AI-tell phrase scan

Pattern: `delve into|in summary|to summarize|in conclusion|firstly|secondly|furthermore,|moreover,|in essence|crucially,|importantly,|notably,|overall,|specifically,|let us recall`.

Two hits, both in normal mathematical-prose connector usage:
- `tate-T1-weighted-completion.tex:730` "Moreover, for any admissible
  weight w, the inclusion ..." (mathematical paragraph connector,
  attaching a quantifier-bound corollary).
- `tate-T5-chain-level-primitive.tex:782` "... not through any
  analytic propagator. Specifically, $H^\bullet(\Omega^\bullet_c(I)) =
  H^\bullet_c(I;\C)$ is one-dimensional ..." (introducing a specific
  computation).

Both are conventional Russian-school connector usage in mathematical
prose, not AI-generated cliche. **No remediation needed.**

---

## 5. Repair proposal

**None required.** All 18 apparatus files PASS or PASS-WITH-WARNINGS
(non-load-bearing warnings only). The build is standalone-clean per
`INVARIANTS.md §III`.

If a future cycle wants to suppress the cross-fragment undefined
warnings entirely, the driver template could be extended with
`\providecommand` no-op stubs for every label class. That is purely
cosmetic; it would not change the rendered PDFs and is not needed
for correctness or for INVARIANTS compliance.

---

## 6. Certification

**Severity.** Zero. No FAILs, no source defects, no voice violations,
no apparatus convention drift.

**Verdict.** All 18 apparatus files certified standalone-buildable
under the convention used by `main.tex` (memoir +
`raeez-math-template` + `mathmacros.tex` + `authors.tex` + tikz
libraries + the two `\providecommand` fallbacks). Total 82 pages of
PDF output.

**Artifacts.** Build directory `/tmp/w5x16r-build/` retains all
drivers, all per-pass logs in `logs/`, all 18 PDFs, the build script
`build_all.sh`, and the warning-scan script `scan_warnings.sh`. The
working tree at `/Users/raeez/topological-strings/` was not modified.
