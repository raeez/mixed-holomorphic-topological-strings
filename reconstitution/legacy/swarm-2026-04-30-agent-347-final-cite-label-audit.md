# Agent 347 final cite/label audit

Date: 2026-04-30

Scope: final citation/label audit after Agent 339 DOI patch and late integrations. No full `make` run. Report-only; no TeX repair was made.

## Verdict

Manuscript-bound TeX is clean.

- Undefined cite keys in changed manuscript TeX: 0.
- Undefined refs in changed manuscript TeX: 0.
- Duplicate `amsrefs` bibliography keys in the `main.tex` closure: 0.
- Duplicate labels in the `main.tex` closure: 0.
- Empty or malformed `\cite`, `\ref`, `\eqref`, `\label`, `\cref`, `\Cref`, `\autoref`, `\pageref`, or `\hyperref[...]` commands in the `main.tex` closure: 0.

External primary-source TeX fixtures are not input by `main.tex`; they were scanned separately. They contain raw-source internal reference defects recorded below. These are not manuscript cite/label failures.

`git diff --check` is clean on unstaged changes. `git diff --cached --check` fails only on staged markdown reports and staged external primary-source fixtures, not on the touched manuscript TeX files.

## Touched TeX surface

Command:

```bash
git status --short -- '*.tex' '*.bib'
```

Result:

```text
M  abstract.tex
MM appendix-factorization-current-conventions.tex
M  appendix-matlis-principal-parts.tex
MM appendix-radial-parts-moyal.tex
M  appendix-unreduced-bv-qme.tex
MM claim-strength-ledger.tex
M  frontier_mnop_framing_volume.tex
MM local-dictionary.tex
MM main.tex
MM open-obligations.tex
 M preamble.tex
M  principles.tex
A  references/primary-sources/gv-hep-th-9809187.tex
A  references/primary-sources/gv-hep-th-9812127.tex
A  references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex
A  references/primary-sources/osv-hep-th-0405146.tex
M  tate-P1-hadamard-mittag-leffler.tex
M  tate-P5-cross-volume.tex
MM tate-T1-weighted-completion.tex
M  tate-T3-quillen-equivalence.tex
MM theorem-lanes.tex
?? references/primary-sources/normal-function-morrison-walcher-0709.4028.tex
?? references/primary-sources/normal-function-walcher-0705.4098.tex
```

Command:

```bash
find . -name '*.bib' -print
```

Result:

```text
```

There are no `.bib` files. The active bibliography is the `amsrefs` `biblist` in `main.tex`.

## Manuscript closure scanner

Command:

```bash
python3 - <<'PY'
# Scanner used: recursively follows \input/\include from main.tex;
# scans the main closure for \bib keys and labels; scans changed
# manuscript files for cite/ref use; strips full-line comments.
PY
```

Exact result:

```text
MANUSCRIPT_INPUT_CLOSURE_COUNT 23
MANUSCRIPT_INPUT_CLOSURE
main.tex
mathmacros.tex
authors.tex
abstract.tex
claim-strength-ledger.tex
local-dictionary.tex
principles.tex
theorem-lanes.tex
tate-T3-quillen-equivalence.tex
tate-T4-bv-vanishing.tex
tate-T1-weighted-completion.tex
tate-T2-nilpotent-truncation.tex
tate-T5-chain-level-primitive.tex
tate-P1-hadamard-mittag-leffler.tex
open-obligations.tex
tate-P3-universality.tex
appendix-matlis-principal-parts.tex
appendix-factorization-current-conventions.tex
appendix-sign-conventions.tex
appendix-full-psi-homology.tex
appendix-unreduced-bv-qme.tex
appendix-radial-parts-moyal.tex
tate-P5-cross-volume.tex
CHANGED_MANUSCRIPT_TEX_COUNT 15
abstract.tex
appendix-factorization-current-conventions.tex
appendix-matlis-principal-parts.tex
appendix-radial-parts-moyal.tex
appendix-unreduced-bv-qme.tex
claim-strength-ledger.tex
local-dictionary.tex
main.tex
open-obligations.tex
principles.tex
tate-P1-hadamard-mittag-leffler.tex
tate-P5-cross-volume.tex
tate-T1-weighted-completion.tex
tate-T3-quillen-equivalence.tex
theorem-lanes.tex
CHANGED_TEX_NOT_IN_MAIN_CLOSURE_COUNT 2
frontier_mnop_framing_volume.tex
preamble.tex
BIB_KEYS_DEFINED 39
LABELS_DEFINED 560
CITES_IN_CHANGED_MANUSCRIPT 69
REFS_IN_CHANGED_MANUSCRIPT 1335
UNDEFINED_CITES_IN_CHANGED_MANUSCRIPT_COUNT 0
UNDEFINED_REFS_IN_CHANGED_MANUSCRIPT_COUNT 0
DUPLICATE_BIB_KEYS_IN_MAIN_CLOSURE_COUNT 0
DUPLICATE_LABELS_IN_MAIN_CLOSURE_COUNT 0
EMPTY_OR_MALFORMED_COMMANDS_IN_MAIN_CLOSURE_COUNT 0
```

## Changed TeX outside `main.tex`

Command:

```bash
python3 - <<'PY'
# Scanner used: checks frontier_mnop_framing_volume.tex and preamble.tex
# against local labels plus the main bibliography/label universe; ignores
# macro-parameter placeholders such as #1.
PY
```

Exact result:

```text
NON_MAIN_CHANGED_TEX_FILES
frontier_mnop_framing_volume.tex
preamble.tex
LOCAL_LABELS 15
LOCAL_CITES 0
LOCAL_REFS 19
UNDEFINED_CITES_AGAINST_MAIN_BIBLIST_COUNT 0
UNDEFINED_REFS_AGAINST_MAIN_LABELS_OR_LOCAL_LABELS_COUNT 0
DUPLICATE_LOCAL_LABELS_COUNT 0
MALFORMED_COUNT 0
```

## External primary-source TeX fixtures

These files are not input by `main.tex`. They were scanned per file, using comment-stripping and whole-file regexes that permit line-wrapped citations.

Command:

```bash
python3 - <<'PY'
# Scanner used: per-file scan of references/primary-sources/*.tex touched
# today; checks local \bibitem/\bib keys, local labels, refs, cites, and
# empty malformed commands after stripping comments.
PY
```

Exact result:

```text
FILE references/primary-sources/gv-hep-th-9809187.tex
  LABELS 0 REFS 0 CITES 0 BIBKEYS 0
  UNDEFINED_CITES 0
  UNDEFINED_REFS 0
  DUPLICATE_LABELS 0
  DUPLICATE_BIB_KEYS 0
  MALFORMED 0
FILE references/primary-sources/gv-hep-th-9812127.tex
  LABELS 0 REFS 0 CITES 0 BIBKEYS 0
  UNDEFINED_CITES 0
  UNDEFINED_REFS 0
  DUPLICATE_LABELS 0
  DUPLICATE_BIB_KEYS 0
  MALFORMED 0
FILE references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex
  LABELS 86 REFS 140 CITES 165 BIBKEYS 69
  UNDEFINED_CITES 0
  UNDEFINED_REFS 1
    1156: leadingconifold
  DUPLICATE_LABELS 1
    quintic: [828, 854]
  DUPLICATE_BIB_KEYS 0
  MALFORMED 0
FILE references/primary-sources/osv-hep-th-0405146.tex
  LABELS 0 REFS 0 CITES 0 BIBKEYS 0
  UNDEFINED_CITES 0
  UNDEFINED_REFS 0
  DUPLICATE_LABELS 0
  DUPLICATE_BIB_KEYS 0
  MALFORMED 0
FILE references/primary-sources/normal-function-morrison-walcher-0709.4028.tex
  LABELS 10 REFS 96 CITES 130 BIBKEYS 71
  UNDEFINED_CITES 0
  UNDEFINED_REFS 78
    1330: actionon
    2145: anyway
    594: asin
    1991: boundary1
    1995: boundary1
    2125: boundary1
    1996: boundary2
    2132: boundary2
    1964: comb1
    1964: comb2
    2174: comb2
    1911: convenient
    1912: convenient
    1960: convenient
    1715: cplusminus
    2168: cplusminus
    1394: cylgquintic
    1424: decomp
    1426: decomp
    1172: deform
    1260: deform1
    1281: deform1
    1310: deform1
    1326: deform1
    1393: deform1
    1618: deform1
    1665: deform1
    1041: domainwall
    1754: ePF
    1955: ePF
    1964: ePF
    2153: ePF
    2184: ePF
    2092: exact
    2088: expan1
    997: extension
    1948: fundamental
    859: hCS
    862: hCS
    874: hCS
    879: hCS
    904: hCS
    956: hCS
    1663: indextheorem
    1185: inhomopf
    1741: inhomopf
    2154: inhomopf
    1377: inter1
    1377: inter2
    698: interjac
    708: interjacfib
    2164: lvasym
    904: mina
    957: mina
    1670: neq3
    1683: neq3
    718: normtrans
    759: note
    815: note
    1971: now
    1979: now
    1992: now
    1228: onepar
    1711: onepar
    1942: our
    1973: our
    1999: patch1
    2040: patch1
    2104: patch2
    1729: pfop
    1941: pfop
    604: similar
    809: toll
    823: toll
    2041: tube
    2067: tube
    793: wellgiven
    796: wellgiven
  DUPLICATE_LABELS 0
  DUPLICATE_BIB_KEYS 0
  MALFORMED 0
FILE references/primary-sources/normal-function-walcher-0705.4098.tex
  LABELS 18 REFS 157 CITES 113 BIBKEYS 51
  UNDEFINED_CITES 0
  UNDEFINED_REFS 120
    1512: Fgclosed
    2126: Fgclosed
    976: algebra
    1021: algebra
    1487: algebra
    1516: algebra
    2446: annhan
    2457: annhan
    2476: annhan
    2488: annhan
    2645: annhan
    1599: bcov
    1304: boundary
    2098: cancelwarner
    1656: central
    1694: central
    2516: covdiff
    2532: covdiff
    1651: decompose
    1403: deform
    2543: diskhan
    2547: diskhan
    1955: equivalent
    2986: expambi
    3015: expambi
    3026: expambi
    3065: expambi
    2036: explderiv
    2928: exprop
    2928: expsols
    2960: expsols
    2296: extended
    1693: filtration
    1739: filtration
    2759: funda
    2800: funda
    2413: g00
    3056: gauge
    3154: gauge
    3079: generically
    822: given
    842: given
    1981: holcs
    1227: ident
    1043: identify
    2420: incomplete
    2430: incomplete
    1388: infaj
    2046: infinv
    2055: infinv
    2797: infinv
    2825: infinv
    2835: infinv
    2801: inhomo
    2936: inhomo
    3179: inhomo
    2545: inshan
    1866: integral
    1851: intermediate
    1911: intermediate
    2485: intermediate
    1262: kahler
    2984: lmv
    2994: lmv
    3014: lmv
    3026: lmv
    705: master
    711: master
    762: master
    764: master
    1112: metric1
    1124: metric1
    1134: metric1
    1112: metric2
    1125: metric2
    1385: mn
    2002: newbasis
    1870: normtrans
    1881: normtrans
    1912: normtrans
    1960: normtrans
    3206: note
    3153: notknown
    1387: obmap
    1974: obmap
    2395: opencc
    2621: over
    2633: over
    2657: over
    1763: period1
    1763: period2
    2603: propagators
    2470: quillen
    2475: quillen
    2950: raw
    2954: raw
    3082: raw
    3190: raw
    1997: reallift
    1422: relation
    1262: riemann
    2534: riemann
    2250: rough
    1171: rrbasis
    2953: simply
    3086: simply
    3194: simply
    820: strictly
    2339: struccon
    1262: symm
    1827: tension
    1866: tension
    1935: tension
    2332: torushan
    2480: torushan
    811: transverse
    2634: useful
    1419: warner
    2097: warner
    1765: witten
  DUPLICATE_LABELS 0
  DUPLICATE_BIB_KEYS 0
  MALFORMED 0
```

## `git diff --check`

Command:

```bash
git diff --check
```

Result:

```text
```

Exit status: 0.

Command:

```bash
git diff --cached --check
```

Result: exit status 2. Raw output length was 474 lines. Exact diagnostic-count reduction:

```text
1 reconstitution/admissible-tate-barcobar-quillen-envelope-construction-target-2026-04-30.md
1 reconstitution/swarm-2026-04-30-agent-194-0957-theorem-lane-integration.md
1 reconstitution/swarm-2026-04-30-agent-239-admissible-tate-barcobar-quillen-envelope-construction-target.md
1 references/primary-sources/gv-hep-th-9809187.tex
1 references/primary-sources/gv-hep-th-9812127.tex
114 references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex
114 references/primary-sources/hkq-compact-cy-hep-th-0612125.txt
6 references/primary-sources/osv-hep-th-0405146.tex
```

Command:

```bash
git diff --check -- abstract.tex appendix-factorization-current-conventions.tex appendix-matlis-principal-parts.tex appendix-radial-parts-moyal.tex appendix-unreduced-bv-qme.tex claim-strength-ledger.tex frontier_mnop_framing_volume.tex local-dictionary.tex main.tex open-obligations.tex preamble.tex principles.tex tate-P1-hadamard-mittag-leffler.tex tate-P5-cross-volume.tex tate-T1-weighted-completion.tex tate-T3-quillen-equivalence.tex theorem-lanes.tex
```

Result:

```text
```

Exit status: 0.

Command:

```bash
git diff --cached --check -- abstract.tex appendix-factorization-current-conventions.tex appendix-matlis-principal-parts.tex appendix-radial-parts-moyal.tex appendix-unreduced-bv-qme.tex claim-strength-ledger.tex frontier_mnop_framing_volume.tex local-dictionary.tex main.tex open-obligations.tex preamble.tex principles.tex tate-P1-hadamard-mittag-leffler.tex tate-P5-cross-volume.tex tate-T1-weighted-completion.tex tate-T3-quillen-equivalence.tex theorem-lanes.tex
```

Result:

```text
```

Exit status: 0.

Command:

```bash
git diff --cached --check -- abstract.tex appendix-factorization-current-conventions.tex appendix-matlis-principal-parts.tex appendix-radial-parts-moyal.tex appendix-unreduced-bv-qme.tex claim-strength-ledger.tex frontier_mnop_framing_volume.tex local-dictionary.tex main.tex open-obligations.tex preamble.tex principles.tex tate-P1-hadamard-mittag-leffler.tex tate-P5-cross-volume.tex tate-T1-weighted-completion.tex tate-T3-quillen-equivalence.tex theorem-lanes.tex references/primary-sources/gv-hep-th-9809187.tex references/primary-sources/gv-hep-th-9812127.tex references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex references/primary-sources/osv-hep-th-0405146.tex
```

Exact diagnostic-count reduction:

```text
1 references/primary-sources/gv-hep-th-9809187.tex
1 references/primary-sources/gv-hep-th-9812127.tex
114 references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex
6 references/primary-sources/osv-hep-th-0405146.tex
```

Raw output length for the preceding command was 242 lines.

## Conclusion

No one-line fatal cite/label typo was found in the manuscript TeX. No full build was run. No manuscript file was edited.
