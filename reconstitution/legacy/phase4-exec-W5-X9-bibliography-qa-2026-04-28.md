# Phase-4 EXEC W5-X9 -- Bibliography QA Drafter

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Attacker.** W5-X9 (Bibliography QA Drafter), attack-heal-swarm wave 5.
**Mode.** Proposal-only. No edits to `main.tex` or any manuscript TeX file.
**Target.** W5-X6 escalated severity-2 objection #16: malformed citation
labels in the bibliography, specifically `[13]razmyslov`, `[2]tsygan`,
and `[16]loday-vallette` (with [16] alleged to be Priddy and [17] alleged
to be Loday-Vallette).

---

## §0. Method

The manuscript bibliography uses `amsrefs` (`\bib{key}{type}{...}` blocks
inside a `biblist` environment), not raw `\bibitem`. The `amsrefs`
machinery auto-numbers the printed reference list in source-order, and
`\cite{key}` resolves to the auto-assigned label via the `bibcite`
records in `main.aux`. Three steps were executed.

1. Enumerate every `\bib{key}{type}` entry in `main.tex`.
2. Enumerate every `\cite{key}` and `\cites{key1,key2,\dots}`
   invocation in the manuscript apparatus
   (`main.tex`, `theorem-lanes.tex`, `claim-strength-ledger.tex`,
   `open-obligations.tex`, `principles.tex`, `notation.tex`,
   `nomenclature.tex`, `local-dictionary.tex`,
   `abstract.tex`, the four `appendix-*.tex` files, and the five
   `tate-*.tex` files).
3. Cross-check the actual rendered numbers in the canonical build
   `out/main.aux` against the W5-X6 specific allegations
   `[13]razmyslov`, `[2]tsygan`, `[16]loday-vallette` and against the
   alleged Priddy / Loday-Vallette confusion.

A separate `main.aux` exists at the top level alongside an
`out/main.aux` inside the build directory. The top-level `main.aux` is
**stale** (pre-appendix-input) and does not reflect current rendering.
All numerics below are taken from `out/main.aux` (timestamp
`2026-04-28 23:14`, matching `out/main.pdf`), which is the canonical
build.

---

## §1. Bibliography enumeration

Thirty-seven `\bib{key}{type}{...}` entries were located in
`main.tex`, lines 5949--6378. Every entry is well-formed:
`amsrefs` syntax, single closing brace per entry, valid type
(`article`, `book`, `misc`, `thesis`), unique key, no duplicate label.
Keys (alphabetical):

```
aksz                                          loday-quillen
bcov                                          loday-vallette
beilinson-drinfeld-chiral                     lurie-ha
beilinson-feigin-mazur                        matlis-injective
berger-moerdijk-axiomatic                     priddy
capelli                                       procesi
cattaneo-felder-bv                            quillen-htpy
costello-gwilliam                             razmyslov
costello-gwilliam-vol2                        schwede-shipley-monoid
costello-li-open-closed-bcov                  tsygan
costello-li-quantum-bcov                      wallach-reductive-invariant-differential
costello-renormalization                      witten-cs
costello-twistedM
gwilliam-williams-holomorphic-bosonic-string
harish-chandra-invariant-differential-operators
hartshorne-local-cohomology
hinich-htpy-alg
hormander-vol1
hovey
howe-capelli
kontsevich-dq
kunz-residues-duality
lefevre-hasegawa
levasseur-stafford-harish-chandra
levasseur-stafford-kernel-harish-chandra
```

Each key is uniquely defined; no collisions were found.

---

## §2. Current rendered numbering (canonical `out/main.aux`)

The current build assigns auto-numbers in source order:

```
[1]  bcov                                        [20] hartshorne-local-cohomology
[2]  loday-quillen                               [21] kunz-residues-duality
[3]  tsygan                                      [22] beilinson-feigin-mazur
[4]  witten-cs                                   [23] priddy
[5]  gwilliam-williams-holomorphic-bosonic-string [24] loday-vallette
[6]  aksz                                        [25] costello-twistedM
[7]  kontsevich-dq                               [26] capelli
[8]  harish-chandra-invariant-differential-operators [27] howe-capelli
[9]  wallach-reductive-invariant-differential    [28] beilinson-drinfeld-chiral
[10] levasseur-stafford-harish-chandra            [29] berger-moerdijk-axiomatic
[11] levasseur-stafford-kernel-harish-chandra     [30] cattaneo-felder-bv
[12] costello-renormalization                     [31] hinich-htpy-alg
[13] costello-li-quantum-bcov                     [32] hormander-vol1
[14] costello-li-open-closed-bcov                 [33] hovey
[15] costello-gwilliam                            [34] lefevre-hasegawa
[16] costello-gwilliam-vol2                       [35] lurie-ha
[17] procesi                                      [36] quillen-htpy
[18] razmyslov                                    [37] schwede-shipley-monoid
[19] matlis-injective
```

In particular: `tsygan` is `[3]`, `razmyslov` is `[18]`, `priddy` is
`[23]`, `loday-vallette` is `[24]`. There is no Priddy / Loday-Vallette
swap: `\cite{priddy}` resolves to `[23] = Priddy 1970, "Koszul
resolutions"`, and `\cite{loday-vallette}` resolves to `[24] = Loday-
Vallette 2012, "Algebraic Operads"`. The W5-X6 alleged numbering
`[13]razmyslov, [2]tsygan, [16]loday-vallette with [16]=Priddy /
[17]=Loday-Vallette` does not match the current build at any position,
and reflects an earlier draft. The malformed `[N]name` glyph form
itself does not appear in any current `*.tex` source file (verified by
`grep -rE '\[[0-9]+\][a-z]+' *.tex`, which returns empty).

---

## §3. Citation enumeration and orphan check

Thirty-six unique citation keys are invoked across the manuscript
apparatus. All thirty-six resolve to `\bib{}` entries:

| key | bibliography no. | citation count |
|-----|------------------|----------------|
| `costello-renormalization` | 12 | 15 |
| `loday-vallette` | 24 | 9 |
| `lurie-ha` | 35 | 6 |
| `costello-li-quantum-bcov` | 13 | 6 |
| `costello-li-open-closed-bcov` | 14 | 6 |
| `costello-gwilliam` | 15 | 4 |
| `bcov` | 1 | 4 |
| `razmyslov` | 18 | 3 |
| `procesi` | 17 | 3 |
| `kontsevich-dq` | 7 | 3 |
| `costello-twistedM` | 25 | 3 |
| (single- and double-cite keys, 24 entries) | various | 1--2 each |

Zero orphan citations. Every `\cite{key}` and every key inside every
`\cites{key1, key2, ...}` resolves to a bibliography entry.

One bibliography entry is **never cited**: `beilinson-drinfeld-chiral`.
It nevertheless appears at position `[28]` in the printed bibliography
because `amsrefs` includes every `\bib{}` block by default, with no
`\nocite{*}` filter. This is not malformed; it is an unused-but-listed
reference. Two options:
1. Remove the entry to avoid an unreferenced bibliography line.
2. Add a justified `\cite{beilinson-drinfeld-chiral}` at the
   factorization / chiral-algebra discussion, where it is contextually
   appropriate (the manuscript discusses chiral algebra structures
   without explicitly citing Beilinson--Drinfeld 2004).

---

## §4. Proposed bibliography QA patch (NOT applied)

### §4.1 Malformed `\bibitem` entries

None to repair. All thirty-seven `\bib{key}{type}{...}` blocks are
syntactically well-formed: balanced braces, single key, valid type,
unique label, no duplicate. The W5-X6 list of malformed labels
(`[13]razmyslov`, `[2]tsygan`, `[16]loday-vallette`) describes a
rendering artifact in a stale earlier PDF, not a source-level
malformation in the present `main.tex`. No edit is required.

### §4.2 Mis-numbered citations

None to repair. The current build does not exhibit the alleged Priddy /
Loday-Vallette swap. `priddy` is `[23]` (= Priddy 1970), and
`loday-vallette` is `[24]` (= Loday-Vallette 2012); both citations land
on the intended source. No edit is required.

### §4.3 Orphan `\cite{}` invocations

None. Every cited key resolves.

### §4.4 Unused bibliography entry

The single unused entry is `beilinson-drinfeld-chiral` (printed as
`[28]`). Two stand-alone proposed patches, only one of which would be
applied if the editorial decision is made to discharge the unused-entry
flag.

**Patch 4.4(a) -- remove unused entry:**

```latex
% main.tex, lines 6266--6278: REMOVE the block
\bib{beilinson-drinfeld-chiral}{book}{
   author={Beilinson, Alexander},
   author={Drinfeld, Vladimir},
   title={Chiral Algebras},
   series={American Mathematical Society Colloquium Publications},
   volume={51},
   publisher={American Mathematical Society},
   place={Providence, RI},
   date={2004},
   pages={vi+375},
   isbn={978-0-8218-3528-9},
   doi={10.1090/coll/051},
}
```

After removal, the bibliography contains thirty-six entries; subsequent
auto-numbers shift by one (e.g. `berger-moerdijk-axiomatic` becomes
`[28]`).

**Patch 4.4(b) -- justified single citation:**

Insert a single `\cite{beilinson-drinfeld-chiral}` at a contextually
appropriate location in the chiral-algebra / factorization discussion
of `tate-P3-universality.tex` or near the Costello--Gwilliam framework
introduction in `main.tex`. Example proposed insertion at the
factorization-algebra introductory paragraph:

```latex
% PROPOSAL ONLY (location to be confirmed; current text in main.tex
% near line 1020):
%
% Old (current):
%   ...the operadic packaging.
% New (proposed):
%   ...the operadic packaging; for the chiral-algebra perspective on
%   the same packaging, see Beilinson--Drinfeld
%   \cite{beilinson-drinfeld-chiral}.
```

The integrator (not the W5-X9 attacker) chooses 4.4(a) or 4.4(b). W5-X9
does not edit manuscript TeX.

---

## §5. Em-dash / AI-tells / agent-language scan on proposed text

The proposed-patch text in §4 contains:
- No em-dashes (only ASCII hyphens `-` and double-hyphen `--` for
  number ranges and en-dashes inside titles).
- No AI tells: no "delve", "leverage", "comprehensive", "robust",
  "seamless", "navigate", "tapestry", "underscore", "in conclusion".
- No agent / swarm / ledger language inside the proposed patches
  themselves. Agent / ledger language appears only in this report's
  scaffolding (which is not destined for the manuscript), per
  proposal-only mode.
- No first-person plural rhetorical fluff ("we observe", "it is
  important to note", "evidently").

The proposed citation insertion in 4.4(b) uses neutral mathematical
prose ("for the chiral-algebra perspective on the same packaging, see
Beilinson--Drinfeld") that is consistent with the Russian-school voice
of the manuscript apparatus.

---

## §6. Certification

**Status. Certified clean.** No malformed bibliography entry exists
in the current source. No orphan citation. No Priddy / Loday-Vallette
mis-numbering in the current build. The W5-X6 severity-2 escalation
for objection #16 was directed at a stale earlier PDF; the current
build does not exhibit the reported defects.

**Residual editorial flag** (not severity-2; severity-3 cosmetic at
most): one unused bibliography entry, `beilinson-drinfeld-chiral`,
listed at `[28]` but never cited. Patch 4.4(a) or 4.4(b) discharges
this flag at the integrator's discretion. Either patch is single-line;
neither alters mathematical content.

**Recommendation.** Down-grade W5-X6 objection #16 from severity-2 to
severity-3 (cosmetic) for the unused-entry flag, and **resolved** for
the alleged malformed labels and Priddy / Loday-Vallette swap.

---

## §7. Files and lines verified

- `/Users/raeez/topological-strings/main.tex`, lines 5947--6379
  (`\begin{biblist} ... \end{biblist}`), thirty-seven `\bib{}` entries.
- `/Users/raeez/topological-strings/out/main.aux` (canonical, build
  timestamp 2026-04-28 23:14), thirty-seven `\bibcite` records,
  thirty-six unique `\citation` records.
- All twenty-three top-level `*.tex` files in
  `/Users/raeez/topological-strings/`, scanned for `\cite` and
  `\cites` invocations; thirty-six unique citation keys, all resolve.
- All `\cite{priddy}` (one site, `main.tex` line 3344) and
  `\cite{loday-vallette}` (nine sites in `main.tex`, `tate-T2`,
  `tate-T3`) verified to attribute Koszul-resolution and operadic-
  packaging content respectively to the correct source.

End of W5-X9 report.
