# Phase-4 EXEC W5-X2 — External-Artifact Gate audit on the +452-line inscription target

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** External-Artifact Gate per
`/Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md`
(External Artifact Gate clause), referee-sealed by
`/Users/raeez/ecosystem/INVARIANTS.md` §III (standalone-documents
discipline), §IV (Russian-school voice), and §X (open-source
whitelist).
**Mode.** Proposal-only. No commits. No edits to manuscript TeX
files. No edits to other reconstitution ledger files beyond this
report and the 200-word append to
`reconstitution/attack-heal-platonic-2026-04-28.md`.
**Target.** The +452-line proposed inscription text, distributed
across:
- W5-A2 strengthenings (`reconstitution/phase4-exec-W5-A2-functoriality-2026-04-28.md` §1.6, §2.5, §3.5).
- Decoupling clause LaTeX (`reconstitution/phase4-exec-Decoupling-Proposition-2026-04-28.md` §6.1, §6.2).
- Master hypothesis block (`reconstitution/phase4-exec-Inscription-Readiness-2026-04-28.md` §2.1, the +267-line draft) plus F'' theorem block (§3.1, §3.2) and Theorem G^otr Phase-5 frontier subsection (§4.1).

---

## §0. Executive verdict

**Severity 2 — minimal language cleanup required before
inscription.** The proposed +452-line inscription target carries
**reader-visible scaffolding** (Phase-4 / Phase-5 / inscription
pass / `\texttt{CLAUDE.md}`) that violates the
standalone-documents discipline of `INVARIANTS.md` §III and the
Russian-school voice of §IV. The inscription is **not yet
publication-grade** in its current form. Five distinct violations
identified, all in the master hypothesis block (267-line component)
and the Theorem G^otr Phase-5 frontier subsection (58-line
component); the W5-A2 strengthenings (+11 lines) and the
Decoupling §6.1/§6.2 clauses are clean.

**Closed-source whitelist gate.** PASS. No reader-visible repo
citations to closed-source paths; no hits on the §X kernel /
centcom / moxie / momentum / mass / api-gateway / etc. blocklist.

**Compile gate.** PASS for Decoupling §6.1 clause (verified via
`pdflatex -draftmode` dry pass on a /tmp mirror; baseline build
succeeded; clause-patched build succeeded with only
expected first-pass label warnings; +1 page rendered).

**Em-dash gate.** PASS. Zero en-dashes (U+2013) or em-dashes
(U+2014) in the proposed inscription LaTeX, including the W5-A2
strengthenings and the Decoupling §6.1/§6.2 clauses. The drafts
correctly use `--` (LaTeX en-dash) where en-dashes appear in
rendered output.

**AI-tell / hedging gate.** PASS. No `we believe`, `essentially`,
`basically`, `arguably`, `to our knowledge`, `roughly speaking`,
`great question`, `let me know`, etc. in the reader-visible
inscription text.

---

## §1. Reader-visible scaffolding violations (severity 2)

The five violations are listed in declining severity order.

### V-1. `\texttt{CLAUDE.md}` reader-visible citation

**Location.** Master hypothesis block / Theorem G^otr longtable
entry, third column (proposed inscription at
`phase4-exec-Inscription-Readiness-2026-04-28.md` line 834):

> `cross-volume coupling to the Vol III queer extension of the
> chiral CY\(_3\) algebra (heuristic only at this stage;
> matched-conventions theorem required for transfer per
> \texttt{CLAUDE.md}). Not a Phase-4 chain-level closed theorem.`

**Why it violates.** `CLAUDE.md` is the project's internal-instruction
file. INVARIANTS.md §III's standalone-documents discipline
forbids reader-visible references to internal scaffolding. The
manuscript's referee or external reader, arriving cold at the
claim-strength ledger, has no context for `CLAUDE.md` and would
correctly read this as a leak of the internal-process layer into
publication-grade prose. The phrase "matched-conventions theorem"
is the load-bearing claim; the citation `\texttt{CLAUDE.md}` is
unsupported by an external-facing source.

**Severity.** 2 / minor. The substantive content (matched-conventions
firewall) is correct; only the citation needs repointing.

**Minimal-language cleanup.** Replace
`per \texttt{CLAUDE.md}` with `per the cross-volume firewall
of \texttt{claim-strength-ledger.tex}` or simply drop the
trailing parenthetical citation. The matched-conventions firewall
is already documented in `claim-strength-ledger.tex` under the
"Cross-volume consequences" framing (which this audit verified
exists as the operative reader-visible language in the existing
ledger).

### V-2. `Phase-4 chain-level closed theorem` reader-visible

**Location.** Same line (834) of the Theorem G^otr longtable
entry:

> `Not a Phase-4 chain-level closed theorem.`

**Why it violates.** "Phase-4" is internal-process scaffolding.
`INVARIANTS.md` §III enumerates `Phase L0/L1/L2/L3/L4` as
forbidden in document content. Phase-N labels are admissible
in internal artifacts (this report, the reconstitution ledger,
attack-heal logs); they are not admissible in
`claim-strength-ledger.tex`, which the external reader sees as
manuscript-grade content.

**Severity.** 2 / minor. Substantive content is correct; only
the qualifier `Phase-4` is non-publishable.

**Minimal-language cleanup.** Replace `Not a Phase-4 chain-level
closed theorem` with `Not a chain-level closed theorem in the
present scope` or `Not a closed theorem of this manuscript`.

### V-3. `Phase-5 frontier candidates` subsection title

**Location.** Master hypothesis block §4 (proposed inscription at
lines 779–780):

> `\subsection*{Phase-5 frontier candidates}`
> `\addcontentsline{toc}{subsection}{Phase-5 frontier candidates}`

Plus reader-visible status-vocabulary item (line 790):

> `vocabulary is extended with one item: \emph{Phase-5 frontier
> candidate (parallel-channel non-discharge)}.`

Plus reader-visible row label (line 802):

> `\emph{Phase-5 frontier candidate (parallel-channel non-discharge)} &`

Plus reader-visible body (lines 826–828):

> `Phase-5 work: rigorous formalization of the signed
> parity-equivariance ...`

**Why it violates.** "Phase-5" appears four times reader-visible
in the proposed inscription, including a section heading,
table-of-contents entry, status-vocabulary item, and prose
description of future work. Each instance is internal-process
scaffolding per `INVARIANTS.md` §III. A standalone reader of
`claim-strength-ledger.tex` would parse "Phase-5" as an internal
project-management label without external reference.

**Severity.** 2 / minor. The mathematical classification is
correct; only the label needs repointing.

**Minimal-language cleanup.** Replace `Phase-5` throughout this
section with a publication-grade phrase. Three options:

- `Frontier candidates` (drops the phase qualifier entirely; cleanest).
- `Open-frontier candidates` (parallels the existing
  `open-obligations.tex` register).
- `Cross-volume frontier candidates` (locates the residual
  outside the local manuscript scope, which is the operative
  meaning of the original `Phase-5`).

The status-vocabulary item becomes
`\emph{frontier candidate (parallel-channel non-discharge)}`.
The row label becomes the same. Prose `Phase-5 work` becomes
`Outstanding work` or `Frontier work`.

### V-4. `Phase-4 audit` and `inscription pass` reader-visible

**Location.** Master hypothesis block, status preamble (proposed
inscription at lines 185–186):

> `\emph{proposed} (formally drafted in a Phase-4 audit, recommended`
> `for the next inscription pass),`

**Why it violates.** Both `Phase-4 audit` and `inscription pass`
are internal-process scaffolding. The status vocabulary
(`inscribed / proposed / silent-strengthening / discharged`) is
otherwise publication-grade — only the gloss on `proposed`
leaks the audit machinery to the page.

**Severity.** 2 / minor.

**Minimal-language cleanup.** Replace the gloss with a
publication-grade equivalent:

> `\emph{proposed} (formally drafted as a recommended next
> inscription target),`

or, more cleanly,

> `\emph{proposed} (precise statement on hand; not yet inscribed
> in the canonical definition of the admissible regulator class),`

The latter mirrors the operative meaning of `proposed` without
naming the audit cycle that produced the draft.

### V-5. `P4-EXEC-G3-T-A1`, `P4-EXEC-G3-M2`, `P4-G2-M1`, `W22-T1`, `W22-T2` reader-visible

**Location.** Master hypothesis block, hypothesis dependency table
(proposed inscription at lines 200, 204, 209, 215; theorem
F'' inscription at lines 200, 204, 209, 215, 605–615; the
status-line of `(A2$'$)` at line 241; the discharge-anchor lines
of multiple `\hyp` blocks; F'' theorem block hypotheses (H1)–(H5)).

**Why it violates.** `P4-EXEC-...`, `P4-G2-...`, `P4-G3-...`,
`W22-...`, `W30` are internal worker / wave / phase identifiers.
`INVARIANTS.md` §III explicitly forbids `phase L0/L1/L2/L3/L4,
W8 §..., M16 §..., Z4 §..., R1 re-attack, post-M16,
post-adversarial reconstitution`. The W22 / P4 / G2 / G3 /
W30 family is exactly this register. The existing manuscript
(verified by direct grep on
`/Users/raeez/topological-strings/main.tex`,
`claim-strength-ledger.tex`, `theorem-lanes.tex`,
`open-obligations.tex`, `preamble.tex`) carries **zero** such
identifiers in reader-visible content; the proposed inscription
introduces them.

**Severity.** 2 / minor (volume is high but each instance is a
mechanical relabeling).

**Minimal-language cleanup.** Three options, in increasing depth
of effort:

- **Drop the identifier.** `(W22-T1)` becomes nothing; the
  status line `discharged on three named regulator schemes`
  reads cleanly without naming the worker that did the discharge.
- **Replace with a citation-grade label.** `P4-G3-T-A1
  $\mathrm{osp}(2N|2N)$ discharge` becomes
  `the $\mathrm{osp}(2N|2N)$ discharge of
  Theorem~\ref{thm:osp-classical-discharge}` (or whichever
  inscribed theorem captures the same content; the F''
  inscription would create such a label as part of this
  cleanup).
- **Replace with the operative theorem-or-lemma reference.**
  `P4-G2-M1` becomes `Theorem~\ref{thm:pva-module-lambda-bracket}`
  or whatever inscribed label corresponds.

The author should choose option 2 or 3 throughout; option 1 is
acceptable only where the identifier is decorative rather than
load-bearing.

---

## §2. Whitelist gate (severity 1 — none triggered)

Per `INVARIANTS.md` §X, only `gstore`, `lex`, `op`, `stack` may
be cited in reader-visible content. The audit ran a direct grep
on the proposed inscription LaTeX for `kernel`, `centcom`, `moxie`,
`moxie-whitepaper`, `momentum`, `momentum-dev`, `momentum-docs`,
`mass-webapp`, `mass-bom`, `api-gateway`, `attestation-engine`,
`templating-engine`, `starters`, `organization-info`,
`investment-info`, `treasury-info`, `identity-info`,
`consent-info`, `governance-info`,
`institutional-world-model-whitepaper`,
`programmable-institutions-whitepaper`, `mass-whitepaper`,
`ecosystem`. **Zero hits.** The proposed inscription cites:

- BCOV (`Comm. Math. Phys. 165 (1994), 311--427`) — primary source.
- Costello, *Renormalization* (2011); Costello-Gwilliam Vol. I/II
  (2017/2021) — primary sources.
- Lurie HA — primary source.
- Williams (`arXiv:2007.13985`) — primary source.
- Beilinson-Drinfeld, *Chiral Algebras* (2004) — primary source.
- Drinfeld 1986 / 1989 / 1990 — primary sources.
- Frenkel-Ben-Zvi (2nd ed., 2004); Pressley-Segal (1986);
  Sugawara (1968) — primary sources.
- Kac, *Lie superalgebras* (1977); Cheng-Wang (2012); Sergeev
  (1984) — primary sources.
- DeWitt (1992); Berezin (1966) — primary sources.

All are external publications. **No closed-source repo citations
appear** in the reader-visible inscription text. **PASS.**

---

## §3. Em-dash gate (clean)

Direct grep for U+2013 (en-dash) and U+2014 (em-dash) on the
proposed inscription LaTeX (W5-A2 strengthenings, Decoupling
§6.1/§6.2, master hypothesis block reader-visible content):
**zero hits.** All en-dash-like rendered output uses LaTeX `--`
(double hyphen), which the engine renders as an en-dash without
the codepoint appearing in source.

**PASS.**

---

## §4. Compile gate (clean for Decoupling §6.1)

Per the External-Artifact Gate's optional clean-build clause, the
audit ran `pdflatex -draftmode -interaction=nonstopmode
-halt-on-error main.tex` on a `/tmp/w5x2-build` mirror with the
working tree's `.tex` files copied verbatim plus
`raeez-math-template.sty` resolved from the symlink target.

**Baseline build.** Succeeded with expected first-pass
`LaTeX Warning: Label(s) may have changed` and a small number
of `Underfull \hbox` warnings on existing bibliography lines
(not blocking).

**Patched build (Decoupling §6.1 clause inserted into
`thm:lane-u1-anomaly`).** Succeeded. `\R^2`, `\C^2`, `\bar c`,
`\delta\eta`, `\omega`, `\mathfrak h_I`, `\Omega^\bullet_c`,
`\widehat\otimes`, `\mathbb E_m^{\mathrm{top}}`,
`\mathbb E_n^{\mathrm{hol}}`, `\mathbb E_{m,n}^{\mathrm{mixed}}`,
`\widehat{\C^2}_0` — all macros resolve from existing
`mathmacros.tex` and `commands.tex`. Page count went from 154
to 155 (one extra page rendered for the new clause). Cross-references
`Theorem~\ref{thm:u1-center-anomaly}`,
`Theorem~\ref{thm:lane-factorization-current}`,
`Lemma~\ref{lem:omega-cocycle}` all resolve at the second pass.

**Master hypothesis block compile not run** (per protocol's
"optional — skip if too risky" clause; the +267-line block depends
on a fresh `\newtheorem{hyp}` declaration in `preamble.tex` and
on cross-references whose validity is verified by
`phase4-exec-Inscription-Readiness-2026-04-28.md` §2.1.4
dependency check; running a full clean build of the
267-line patch on the working tree would either require
modifying `preamble.tex` (write action — out of scope for
proposal-only mode) or working in a more elaborate /tmp mirror
with the new `\newtheorem` line patched in, which exceeds the
optional dry-pass scope of this audit).

**PASS for the Decoupling §6.1 clause.** **Deferred for the master
hypothesis block.** The W5-A2 strengthenings (+11 lines, three
sentences plus a comment block) carry no compile risk; their
LaTeX uses only macros (`\mathrm`, `\mathfrak`, standard
math-mode glyphs) that resolve in the base manuscript.

---

## §5. Cross-volume firewall reader-visibility

**Question.** Does the proposed inscription expose internal
scaffolding (`wave-4 ledger`, `W5-A2 finding`, `Phase-4 EXEC`)
to reader-visible LaTeX?

**Answer.** Yes — at five distinct sites enumerated in §1 above.
The internal scaffolding is `Phase-4`, `Phase-5`, `P4-EXEC-G3-T-A1`,
`P4-EXEC-G3-M2`, `P4-G2-M1`, `W22-T1`, `W22-T2`, `W30`,
`Phase-4 audit`, `inscription pass`, and `\texttt{CLAUDE.md}`.

`wave-4 ledger` and `W5-A2 finding` themselves do not appear
reader-visible; their per-violation correlates do. The
firewall reader-visibility violation is therefore **at the
content-label register**, not at the metadata register.

**Severity.** 2 / minor. Cleanup is mechanical relabeling (replace
identifiers with theorem references or drop them); no
mathematical content changes. The five sites in §1 enumerate the
exhaustive cleanup list.

---

## §6. Aggregate verdict and proposed minimal-language cleanup

**Verdict.** **The +452-line inscription target does NOT pass the
External-Artifact Gate as currently drafted.** Five reader-visible
scaffolding violations (V-1 through V-5) require minimal-language
cleanup before the inscription is publication-grade. The
underlying mathematical content is correct; only the surface
prose and labels need repointing.

**Severity.** 2 / minor (load-bearing cleanup, not a logical or
mathematical defect).

**Estimated cleanup line-delta.** Each violation is a mechanical
local edit:
- V-1 (`\texttt{CLAUDE.md}` citation): -1 line (drop) or 0 lines
  (replace inline).
- V-2 (`Phase-4 chain-level closed theorem`): 0 lines (replace
  inline).
- V-3 (`Phase-5 frontier candidates` ×4 instances): 0 lines
  (replace inline; possibly -2 if section title is shortened).
- V-4 (`Phase-4 audit`, `inscription pass`): 0 lines (replace
  gloss inline).
- V-5 (`P4-EXEC-...`, `W22-...`, `W30` ×~30 instances across the
  master hypothesis block, F'' theorem block, and Theorem G^otr
  longtable): 0 lines net (each identifier replaced with a
  theorem reference of similar length, or dropped if decorative).

**Total cleanup line-delta.** Estimated **-2 to 0 lines net**.
The cleanup does not inflate the inscription footprint; it only
reroutes labels.

**Heal status.** The cleanup is **mandatory before inscription**.
After cleanup, the inscription target is publication-grade
(External-Artifact Gate certification). The W5-A2 strengthenings
and the Decoupling §6.1/§6.2 clauses pass cleanly already.

**Strategic implication for the inscription target.** Authorize
the +452-line target *contingent* on the V-1 through V-5 cleanup.
The cleanup is a one-pass mechanical edit; the user can perform
it together with the inscription itself, or the next attack-heal
cycle (W5-X3 or W6) can produce a clean draft.

**Inscription gate status.** **NOT YET PASSING** until V-1
through V-5 are healed. After healing (estimated effort: one
editorial pass on
`phase4-exec-Inscription-Readiness-2026-04-28.md` §2.1, §3.2, §4.1,
yielding a clean +452-line draft): **PASSING**.

---

## §7. Citations

- `/Users/raeez/ecosystem/INVARIANTS.md` §III (standalone-documents
  discipline; forbidden version / draft / phase / wave / process
  language; pre-ship grep), §IV (Russian-school voice; named
  attribution; honest epistemic status), §X (open-source whitelist;
  the four `gstore`, `lex`, `op`, `stack` repositories).
- `/Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md`
  External Artifact Gate clause (run standalone scan; remove
  process language; run whitelist scan; cite only the four
  whitelisted public repositories; treat any hit as blocking
  convergence).
- `/Users/raeez/topological-strings/CLAUDE.md` Repo-local clause
  (Russian mathematical-physics voice; named attribution; physical
  intuition + formal rigor coexist; honest epistemic status on
  every load-bearing claim).
- `/Users/raeez/topological-strings/reconstitution/phase4-exec-W5-A2-functoriality-2026-04-28.md`
  §1.6, §2.5, §3.5 (the +11-line W5-A2 strengthenings audited
  here).
- `/Users/raeez/topological-strings/reconstitution/phase4-exec-Decoupling-Proposition-2026-04-28.md`
  §6.1, §6.2, §6.3 (the Decoupling clause LaTeX audited here).
- `/Users/raeez/topological-strings/reconstitution/phase4-exec-Inscription-Readiness-2026-04-28.md`
  §2.1, §3.1, §3.2, §4.1 (the master hypothesis block, the F''
  theorem block, the Theorem G^otr Phase-5 frontier subsection
  audited here).

---

End of Phase-4 EXEC W5-X2 (External-Artifact Gate audit) report.
