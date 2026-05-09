# Phase-4 EXEC W5-X37: Acknowledgements Drafter

**Agent.** W5-X37 = Acknowledgements Drafter, attack-heal-swarm wave 5.
**Mode.** Proposal-only; no TeX file edited; no commit.
**Authorship.** Raeez Lorgat. **Date.** 2026-04-28.
**Predecessors.** W5-X28 (authorship audit, certified sole-author and
clean of LLM byline); W5-X32 (pre-publication preflight, flagged the
absent acknowledgements / funding block as severity-1 closeable).
**Charter.** Draft three acknowledgement-block options for the
156-page sole-author manuscript and recommend one. Each option must
pass the em-dash, AI-tell, agent-language, and LLM-attribution scans.

---

## §1. Setting the landing site

`main.tex` line 5933 opens `\section{Outlook and convention firewalls}`.
Lines 5933-5958 carry two subsections (`ssec:cross-volume-horizon` and
the closing convention-firewall paragraph). Line 5960 is `\appendix`,
followed by five `\input{...}` lines for the appendix and
cross-volume tate file. Line 5968 opens `\begin{biblist}`. Line 6400
closes `\end{biblist}`.

The canonical landing location for an acknowledgements block in
this layout is **immediately before `\appendix` (between line 5958
and line 5960)** as an unnumbered `\section*{Acknowledgements}` at
the same nesting level as the surrounding numbered sections. This is
consistent with AMS / Inventiones / Geom. Topol. / Adv. Math.
conventions for sole-author monographs: acknowledgements close the
main body and precede the appendices.

An alternative landing location places the block after the
bibliography, which is the JHEP convention. The pre-appendix slot
is the safer default for the main-target journal set certified at
W5-X32 §5 (Inventiones / Geom. Topol. / Adv. Math.).

---

## §2. Russian-school discipline considerations

The Russian mathematical school does not personalise acknowledgements
the way Anglo-American papers commonly do. The convention is:

1. Acknowledge a school, a tradition, or a line of work, not an
   accumulation of names with whom the author has had conversations.
2. State funding accurately. If there is none, say so. Do not
   manufacture a sponsor.
3. Do not thank a coauthor where there is none.
4. Do not thank "the anonymous referees" when no referees have yet
   read the manuscript (this would be a counterfactual on a
   pre-submission draft).
5. Cite intellectual debts in the bibliography, not in
   acknowledgements; acknowledgements are a register-of-record, not
   a citation locus.

The W5-X28 audit established that the bibliography (`main.tex`
lines 5970-6395, ~145 entries) carries full named attribution to
BCOV, Witten, Costello, Costello-Gwilliam, Costello-Li,
Beilinson-Drinfeld, Cattaneo-Felder, Kontsevich, Gwilliam-Williams,
Loday-Quillen, Tsygan, Procesi, Razmyslov, Wallach, Levasseur-Stafford,
Beilinson-Feigin-Mazur, Loday-Vallette, Hartshorne, Kunz, Matlis, and
the rest of the cited intellectual lineage. Intellectual debt is
fully discharged by citation.

The acknowledgements block therefore carries only the residual
register-of-record: funding statement, affiliation context, and
optional acknowledgement of the cross-volume programme.

---

## §3. Three drafted options

### Option A (minimal, single sentence, sole-author register)

**LaTeX patch.** Insert between current `main.tex` line 5958 and
line 5960 (after the closing convention-firewall paragraph, before
`\appendix`):

```latex

\section*{Acknowledgements}

This work was conducted as independent research without external
funding.

```

**Word count.** 10 words after `\section*{}` heading.
**Tone.** Maximally minimal; states the funding fact and stops.
**Em-dash scan.** None. **AI-tell scan.** None. **Agent-language
scan.** None. **LLM-attribution scan.** None.

### Option B (moderate, three sentences, lineage-acknowledging)

**LaTeX patch.** Same insertion site as Option A.

```latex

\section*{Acknowledgements}

This work was conducted as independent research without external
funding. The framework owes its central perspective on
Kodaira-Spencer gravity to Bershadsky, Cecotti, Ooguri, and Vafa
(1993), its BV-BRST formulation to Witten (1988) and Costello (2011),
and its factorisation-algebra discipline to Beilinson and Drinfeld
(2004). Errors are the author's.

```

**Word count.** 49 words. **Tone.** Acknowledges the school and the
canonical sources by named lineage, attributes residual error
honestly, no personal-conversation claims. **Em-dash scan.** None.
**AI-tell scan.** None ("framework" is named-construction-bearing
in this register: framework of factorisation algebras, framework
of BV-BRST, etc.; not the marketing buzzword sense). **Agent-language
scan.** None. **LLM-attribution scan.** None.

### Option C (extended, four sentences, cross-volume-aware)

**LaTeX patch.** Same insertion site as Option A.

```latex

\section*{Acknowledgements}

This work was conducted as independent research without external
funding. The framework owes its central perspective on
Kodaira-Spencer gravity to Bershadsky, Cecotti, Ooguri, and Vafa
(1993), its BV-BRST formulation to Witten (1988) and Costello (2011),
and its factorisation-algebra discipline to Beilinson and Drinfeld
(2004). The local Hamiltonian BF analysis on the formal symplectic
disk was sharpened by interface-checking against the cross-volume
programme on Calabi-Yau quantum groups, on the Igusa cusp form, and
on the chiral bar-cobar duality, all of which carry their own
matched-conventions firewalls and contribute no theorem to the local
manuscript. Errors are the author's.

```

**Word count.** 90 words. **Tone.** Acknowledges the cross-volume
research programme without falsely transferring any theorem from one
volume to another (the firewall language is preserved). The phrase
"contribute no theorem to the local manuscript" enforces the
no-cross-volume-leakage discipline already established in the
convention firewalls of `main.tex` line 5933-5958. **Em-dash scan.**
None. **AI-tell scan.** None. **Agent-language scan.** None.
**LLM-attribution scan.** None.

---

## §4. Comparative scan tabulation

| Option | Sentences | Words | Em-dash | AI-tell | Agent-lang | LLM-attr |
|--------|-----------|-------|---------|---------|------------|----------|
| A      | 1         | 10    | 0       | 0       | 0          | 0        |
| B      | 3         | 49    | 0       | 0       | 0          | 0        |
| C      | 4         | 90    | 0       | 0       | 0          | 0        |

All three options are register-clean. The discriminating factors
are length, lineage-acknowledgement load, and cross-volume audibility.

---

## §5. Recommendation

**Recommended option: B (moderate, three sentences).**

**Rationale.**

1. **Funding statement is required.** A 156-page sole-author monograph
   submitted to Inventiones / Geom. Topol. / Adv. Math. without any
   funding statement would be an unusual omission. Option A clears
   this bar at minimum cost.

2. **Lineage acknowledgement is appropriate at this length.** The
   manuscript runs 156 pages and rests structurally on four named
   intellectual lineages: BCOV 1993 for the
   Kodaira-Spencer-gravity perspective, Witten 1988 and Costello 2011
   for the BV-BRST formulation, and Beilinson-Drinfeld 2004 for the
   factorisation-algebra discipline. Naming these in the
   acknowledgements is not redundant with the bibliography; it
   distinguishes the structural pillars from the ~145 incidental
   citations. Option A omits this. Option B makes it explicit
   in 49 words.

3. **Cross-volume reference would be premature in the local
   acknowledgements block.** Option C names the cross-volume
   research programme (Vol III calabi-yau-quantum-groups,
   igusa-cusp-form, chiral bar-cobar) by repository, which is
   atypical for a sole-author paper and risks suggesting a coupling
   that the convention firewalls of `main.tex` line 5933-5958
   explicitly negate. The cross-volume firewall already states
   that no transfer is asserted; repeating this in acknowledgements
   is acceptable but adds 41 words for limited gain. Better to keep
   the firewall in the body and the acknowledgements terse.

4. **Russian-school register matches Option B.** Option B
   acknowledges the school by name (BCOV, Witten, Costello,
   Beilinson-Drinfeld) without overpersonalising and without
   claiming conversations. The phrase "Errors are the author's"
   is canonical sole-author convention.

5. **Length appropriateness.** A 156-page paper with a 10-word
   acknowledgement (Option A) reads slightly under-acknowledged
   at the level of intellectual debt. A 90-word acknowledgement
   (Option C) reads slightly over-padded for a sole-author work
   with no external funding and no human-collaborator conversations
   to record. The 49-word Option B is calibrated.

**Closure cost.** +6 lines in `main.tex` (the `\section*{}` heading
plus three sentences plus blank-line padding).

**No theorem modified, no proof modified, no figure modified, no
bibliography entry modified.** Purely additive.

---

## §6. Sanity firewall

This proposal does not commit any text to the manuscript. The
landing site has been verified by interpretation `main.tex` lines
5933-5970 directly. The bibliography landmark (line 5968,
`\begin{biblist}`) is unchanged. The appendix landmark (line 5960,
`\appendix`) is unchanged. The five appendix `\input{}` lines
(5961-5965) are unchanged.

The `authors.tex` file (3 lines: `\author{Raeez Lorgat}`,
`\email{root@raeez.com}`, `\urladdr{http://math.raeez.com}`) is
unchanged. No second author is added. No LLM byline is added. No
external sponsor is named. No referee is thanked.

---

## §7. Inscription handoff

If user authorises Option B, the W5-X38 (or named follow-up)
inscription agent applies the patch in §3.2 verbatim between
`main.tex` line 5958 and line 5960. No further preflight
modifications are bundled with this patch; the keywords / MSC-2020
patch (W5-X32 X32.2), the `pdfsubject` / `pdfkeywords` patch
(W5-X32 X32.4), and the Makefile `*.idx` cleanup (W5-X32 X32.6)
are independent inscriptions.

End of Phase-4 EXEC W5-X37 acknowledgements drafter.
