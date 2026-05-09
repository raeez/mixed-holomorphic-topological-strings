# Phase-4 EXEC W5-X11: Clean-Build Verifier

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Role.** Attacker W5-X11, attack-heal-swarm wave 5.
**Mode.** Read-only on the working tree; write-allowed only inside
`/tmp/w5x11-build/` plus the two reconstitution/ files mentioned.
**Target.** Verify that the current manuscript at
`/Users/raeez/topological-strings` compiles cleanly and produces a
referee-grade PDF; report any overfull / underfull hboxes, missing
references, or compilation warnings.

---

## 1. Build harness

### 1.1 Source inventory

The clean-build directory `/tmp/w5x11-build/` was populated with the
following sources from the working tree:

- Root and bound parts: `main.tex`, `abstract.tex`, `preamble.tex`,
  `authors.tex`, `commands.tex`, `mathmacros.tex`, `notation.tex`,
  `nomenclature.tex`.
- Stand-alone documents: `principles.tex`, `local-dictionary.tex`,
  `theorem-lanes.tex`, `claim-strength-ledger.tex`,
  `open-obligations.tex`.
- Tate package: `tate-T1-weighted-completion.tex`,
  `tate-T2-nilpotent-truncation.tex`,
  `tate-T3-quillen-equivalence.tex`, `tate-T4-bv-vanishing.tex`,
  `tate-T5-chain-level-primitive.tex`,
  `tate-P1-hadamard-mittag-leffler.tex`,
  `tate-P3-universality.tex`, `tate-P5-cross-volume.tex`.
- Appendix package: `appendix-factorization-current-conventions.tex`,
  `appendix-matlis-principal-parts.tex`,
  `appendix-radial-parts-moyal.tex`,
  `appendix-unreduced-bv-qme.tex`.
- Image assets: `firstorder.{png,svg}`, `thirdordera.{png,svg}`,
  `thirdorderb.{png,svg}`.
- Build infrastructure: `Makefile`, `main.tex.latexmain`.

Excluded (per task spec): `out/`, `out_test/`, `.agents/`, `.claude/`,
`.git/`, `materials/`, `scripts/`, `references/`, `reconstitution/`.

### 1.2 Compilation harness

Engine: `pdflatex` (TeX Live 2025, pdfTeX 3.141592653-2.6-1.40.27).
Search path: `TEXINPUTS=/tmp/w5x11-build/:/Users/raeez/latex-template::`.
Flags: `-interaction=nonstopmode -file-line-error`.
Passes run: 5 (3 mandatory + 1 to converge label warnings + 1 stability
verification).

### 1.3 Pass-by-pass page counts

| Pass | Pages | Bytes  | Label warning | Status     |
|------|-------|--------|---------------|------------|
| 1    | 154   | 1009646| yes           | exit 0     |
| 2    | 155   | 1029770| yes           | exit 0     |
| 3    | 155   | 1027066| yes           | exit 0     |
| 4    | 155   | 1027072| no            | exit 0     |
| 5    | 155   | 1027072| no            | exit 0     |

Build is converged at pass 4 (label cross-references stable). Pass 5
confirms idempotency: identical PDF byte count.

---

## 2. Final-build certification

### 2.1 PDF metadata (pdfinfo)

- **Title.** Closed Hamiltonian BF Theory as the Derived Poisson Center
  of a Dirac Brane Probe: A formal local mixed
  holomorphic-topological model on R2 x C2.
- **Pages.** 155.
- **Producer.** pdfTeX-1.40.27.
- **File.** `/tmp/w5x11-build/main.pdf`, 1027072 bytes.

### 2.2 LaTeX warnings, errors, missing references

| Class                  | Count | Notes                                    |
|------------------------|-------|------------------------------------------|
| Compilation errors `!` |   0   | Build converged exit 0 on every pass.    |
| LaTeX Warnings         |   0   | After pass 4 (label closure).            |
| Undefined references   |   0   | Zero `?` placeholders on final pass.     |
| Undefined citations    |   0   | All 36 cited keys resolve to numbered    |
|                        |       | entries in the `biblist`.                |
| Overfull \hbox         |   0   | None.                                    |
| Underfull \hbox        |  19   | All low-severity stretchy-space          |
|                        |       | warnings; line-by-line list in 2.3.      |

### 2.3 Underfull \hbox inventory (with file mapping)

The 19 underfull warnings are typographic (the line ends short of the
text-block right margin; usually because a math display is wrapped on a
line of its own), not bad-box rendering errors. They are listed below
in order of appearance, mapped to the originating source file by
cross-referencing the page-mark stream in `pass4.log`.

| Loc | Lines     | Badness | File                                       | Region                       |
|-----|-----------|---------|--------------------------------------------|------------------------------|
|  1  | 306--309  | 4013    | `main.tex`                                 | antisymmetry display         |
|  2  | 1592--1597| 3250    | `main.tex`                                 | $\bar{\partial}$ variation   |
|  3  | 2039--2046| 4168    | `main.tex`                                 | Costello--Gwilliam citation  |
|  4  | 2551--2560| 2951    | `main.tex`                                 | index-triple parenthetical   |
|  5  | 2551--2560| 5954    | `main.tex`                                 | C u c term continuation      |
|  6  | 242--252  | 7558    | `tate-T1-weighted-completion.tex`          | Casimir Tate-window display  |
|  7  | 242--252  | 10000   | `tate-T1-weighted-completion.tex`          | $w_d e_n$ continuation       |
|  8  | 440--446  | 2698    | `tate-T1-weighted-completion.tex`          | Casimir convergence display  |
|  9  | 83--99    | 6396    | `tate-T5-chain-level-primitive.tex`        | open-bracket preserves $F$   |
| 10  | 138--142  | 10000   | `tate-P1-hadamard-mittag-leffler.tex`      | Hadamard parametrix limit    |
| 11  | 3879--3896| 10000   | `main.tex`                                 | diagonal weight constraint   |
| 12  | 3879--3896| 5970    | `main.tex`                                 | Poisson bracket continuation |
| 13  | 3897--3915| 6575    | `main.tex`                                 | direct Poisson computation   |
| 14  | 4943--4950| 10000   | `main.tex`                                 | connected single-trace proj. |
| 15  | 5105--5118| 3088    | `main.tex`                                 | Remark 3.172 opener          |
| 16  | 5105--5118| 4242    | `main.tex`                                 | Weyl/Moyal continuation      |
| 17  | 5815--5818| 10000   | `main.tex`                                 | brane-defect ribbon graph    |
| 18  | 83--90    | 10000   | `tate-P3-universality.tex`                 | Proposition 5.4 opener       |
| 19  | 6244--6244| 3601    | `main.tex` bibliography                    | Costello [2016] author line  |

All 19 are well-known TeX line-stretching artifacts arising from
math-display lines that the paragraph builder cannot fully balance to
the right margin. None render as visible text overrun. Wave-3 referee
report explicitly tolerates this class as "release polish, not a
mathematical blocker"; the count remains within publication tolerance.

---

## 3. Comparison to wave-3 referee baseline

Wave-3 baseline
(`reconstitution/wave3-referee-report-2026-04-28.md`):
- 137 pages.
- 1 overfull hbox at `tate-T3-quillen-equivalence.tex:84-92`.

Current build (wave-5 closing):
- 155 pages (delta +18 pages, +13.1%).
- 0 overfull hbox; the wave-3 single overfull is closed.

The +18-page expansion reflects the wave-4 / wave-5 inscriptions:
- Reduced unreduced cotangent factorization-current discussion
  (`appendix-factorization-current-conventions.tex` is now in scope).
- Matlis principal-part appendix
  (`appendix-matlis-principal-parts.tex`).
- Unreduced BV / QME appendix
  (`appendix-unreduced-bv-qme.tex`).
- Radial-parts Moyal appendix
  (`appendix-radial-parts-moyal.tex`).
- Principles / open-obligations / claim-strength-ledger /
  local-dictionary stand-alones now bound into `main.tex`.
- Cross-volume firewall (`tate-P5-cross-volume.tex`).

The wave-3 overfull at `tate-T3-quillen-equivalence.tex:84-92`
(Theorem `thm:tate-model-structure`, "Existence inside the admissible
envelope") has been **closed**. The theorem statement remains at the
same line range (lines 83-94 in the current build), so the heal was
local paragraph-spacing or discretionary-break adjustment, not a
relocation or restructure. No overfull migrated elsewhere in the
manuscript.

**Verdict.** The wave-3 single severity-3 layout-polish escalation is
healed. Build hygiene is at or above the wave-3 referee bar.

---

## 4. Reader-visible PDF text scan

Methodology: `pdftotext /tmp/w5x11-build/main.pdf
/tmp/w5x11-build/main.txt` followed by Perl-regex character-class scans
on the rendered text. (This catches reader-visible glyphs even when the
TeX source uses a macro or comment.)

### 4.1 Em-dash (U+2014) and en-dash (U+2013)

- **Em-dash U+2014.** Zero occurrences in the rendered PDF.
- **En-dash U+2013.** 161 occurrences, all in compound proper names
  (e.g. "Calabi--Yau", "Bershadsky--Cecotti--Ooguri--Vafa",
  "Fourier--Rees", "Costello--Gwilliam", "Harish-Chandra--Wallach",
  etc.) and in number ranges. None are used as a sentence break.

  Spot-checks confirm proper Russian-school typographic convention:
  no instance of `[a-z]–\s` (en-dash followed by space, the AI
  tell pattern). All en-dashes are tightly bound between proper-name
  tokens or between range endpoints.

### 4.2 AI-tell vocabulary

Zero occurrences in the rendered PDF for the standard AI-prose tells:
`delve`, `tapestry`, `nuanced`, `leverage`, `pivotal`, `elevate`,
`crucial`, `unwavering`, `robust`, `in conclusion`, `in summary`,
`to conclude`, `overall`, `notably`, `importantly`,
`it should be noted`, `it's worth`. PASS.

### 4.3 Agent / swarm / ledger / draft / workflow language

- `agent`: 0 occurrences.
- `swarm`: 0 occurrences.
- `draft`: 0 occurrences (no manuscript-stage stigmata leak).
- `wave`, `attack-heal`, `phase 4`, `harness`, `workflow`, `claude`,
  `anthropic`, `llm`, `gpt`, `sonnet`, `opus`: 0 occurrences each.
- `ledger`: 14 occurrences, **all** of which name the load-bearing
  manuscript artifact "claim-strength ledger" (i.e. the document
  `claim-strength-ledger.tex`). This is the sanctioned mathematical
  vocabulary for the status-tracking apparatus introduced into the
  manuscript itself; not a process / workflow leak. PASS.
- `attack`: 1 occurrence -- "the finite exact-arithmetic attack
  verifies the same obstruction through exponents $\le 5$ and Moyal".
  This is mathematical English ("an attack on a problem"), not
  attack-heal workflow language. Acceptable.
- `phase`: 32 occurrences, all in the physics sense ("phase space",
  "constrained phase space", "reduced phase space"). PASS.

### 4.4 Reader-visible violation count

**Zero.** No em-dashes, no AI-tells, no workflow / agent / swarm
leakage in the rendered PDF.

---

## 5. Verdict

**Severity 0.** Clean certification.

- **PDF page count.** 155.
- **Overfull \hbox count.** 0 (closed from wave-3 baseline of 1).
- **Underfull \hbox count.** 19, all low-severity stretchy-space
  warnings on math-display lines; below the publication-blocker
  threshold.
- **Undefined references / citations.** 0.
- **LaTeX errors.** 0.
- **Reader-visible em-dash / AI-tell / agent-language violations
  in the rendered PDF.** 0.

The manuscript passes the wave-3 referee bar on every dimension that
report scoped, and improves it on the layout-polish dimension.

No commit. No edit outside `/tmp/w5x11-build/` and the two
reconstitution/ files mentioned in the task spec.

**Build artefact location.** `/tmp/w5x11-build/main.pdf` (1027072 bytes,
155 pages). Pass logs: `/tmp/w5x11-build/pass{1,2,3,4,5}.log`. Full
TeX transcript: `/tmp/w5x11-build/main.log`.
