# Agent 342 final build-readiness audit

Date: 2026-04-30.

Scope: report-only final TeX compile-blocker audit before the main thread
runs `make pdf`.  I did not run `make pdf`.  I made no manuscript TeX
patches.

## Root build surface

`main.tex` inputs the root build closure at:

- `main.tex:5` `mathmacros.tex`
- `main.tex:6` `authors.tex`
- `main.tex:66` `abstract.tex`
- `main.tex:68` `claim-strength-ledger.tex`
- `main.tex:69` `local-dictionary.tex`
- `main.tex:73` `principles.tex`
- `main.tex:2580` `theorem-lanes.tex`
- `main.tex:4350` `tate-T3-quillen-equivalence.tex`
- `main.tex:4650` `tate-T1-weighted-completion.tex`
- `main.tex:4656` `tate-P1-hadamard-mittag-leffler.tex`
- `main.tex:9600` `open-obligations.tex`
- `main.tex:9639` `appendix-matlis-principal-parts.tex`
- `main.tex:9640` `appendix-factorization-current-conventions.tex`
- `main.tex:9643` `appendix-unreduced-bv-qme.tex`
- `main.tex:9644` `appendix-radial-parts-moyal.tex`
- `main.tex:9645` `tate-P5-cross-volume.tex`

Changed TeX files outside this root closure:

- `preamble.tex`: changed, but not input by `main.tex`.
- `frontier_mnop_framing_volume.tex`: standalone, not input by `main.tex`.
- `references/primary-sources/gv-hep-th-9809187.tex`,
  `references/primary-sources/gv-hep-th-9812127.tex`,
  `references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex`,
  `references/primary-sources/osv-hep-th-0405146.tex`: staged source
  fixtures, not input by `main.tex`.

## Package gate

No fatal package blocker found for the changed root manuscript files.

- `main.tex:4` loads `raeez-math-template`.
- `raeez-math-template.sty:718` loads `longtable`.
- `raeez-math-template.sty:719` loads `booktabs`.
- `raeez-math-template.sty:726` loads `enumitem`.
- `raeez-math-template.sty:741` loads `makecell`; the local TeX Live
  `makecell.sty:26` loads `array`, so the current uses of
  `\arraybackslash` are covered.
- `claim-strength-ledger.tex:168` uses `longtable`.
- `local-dictionary.tex:17`, `local-dictionary.tex:127`,
  `local-dictionary.tex:179`, `local-dictionary.tex:435`,
  `local-dictionary.tex:726`, `local-dictionary.tex:845`,
  `local-dictionary.tex:1236` use `longtable`.

`preamble.tex:15` also now has `\usepackage{array,longtable}`, but the
root build does not input `preamble.tex`.

## Environment and delimiter gate

Static stack check on the changed files in the `main.tex` closure found
no unmatched `\begin{...}` / `\end{...}` pairs.

The same check on all changed tracked TeX files found no unmatched
environments.  A separate brace/display-delimiter scan on the changed
root closure also found no imbalance.

Spot anchors for the largest recent regions checked:

- `claim-strength-ledger.tex:168-252`: `longtable` closed.
- `claim-strength-ledger.tex:257-314`: `center` / `tabular` closed.
- `appendix-radial-parts-moyal.tex:631-642`: newly split `aligned`
  display closed.
- `appendix-radial-parts-moyal.tex:987-1151`: new square-cell / radial
  obstruction theorem lane environments closed.
- `main.tex:9645-10105`: `biblist` and document close normally.

## Citation and bibliography gate

Root closure citation scan:

- 39 unique `\bib{...}` keys in `main.tex:9645-10103`.
- 79 `\cite{...}` uses in the `main.tex` closure.
- No missing cite keys against the root `biblist`.
- No duplicate root `\bib{...}` keys found.

Recent BMK source keys are present:

- `main.tex:1291` cites `laurent-thiebaut-bmk`; key defined at
  `main.tex:10027`.
- `main.tex:1307` cites `ruppenthal-bmk`; key defined at
  `main.tex:10041`.
- `theorem-lanes.tex:483` and `theorem-lanes.tex:499` cite the same
  keys.

No malformed `\bibitem` surface appears in the root closure; the root
uses `amsrefs` `biblist`, not raw `\bibitem`.

## Label gate

No actual duplicate labels found in the `main.tex` closure.

The only duplicate in the root closure scan is the macro-template label
`fig:#1` in `mathmacros.tex:22` and `mathmacros.tex:33`; this is inside
macro definitions and is not a concrete manuscript label unless the
helper macro is expanded with the same filename.

Changed TeX outside the root closure has source-fixture duplicates:

- `references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex:828`
  and `references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex:854`
  both define `\label{quintic}`.
- `references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex:101`
  and `references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex:103`
  define wrapper macros containing `\label{#1}`; these are macro
  definitions, not concrete labels.

These source fixtures are not input by `main.tex`, so they are not root
build blockers.

## `git diff --check`

Commands run:

- `git diff --check -- '*.tex'`: passed.
- `git diff --cached --check --` restricted to the changed manuscript
  TeX path list: passed.
- `git diff --cached --check -- '*.tex'`: failed only on staged
  primary-source fixture TeX files outside the root build closure.

Exact staged fixture anchors:

- `references/primary-sources/gv-hep-th-9809187.tex:834`: new blank line
  at EOF.
- `references/primary-sources/gv-hep-th-9812127.tex:1012`: new blank line
  at EOF.
- `references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex`:
  trailing whitespace at lines 197, 204, 283, 342, 343, 344, 345, 384,
  385, 838, 839, 840, 841, 847, 848, 854, 855, 857, 858, 870, 871, 872,
  874, 1187, 1188, 1189, 1190, 1191, 1192, 1393, 1394, 1395, 1515,
  1516, 1517, 1535, 1536, 1576, 1578, 1579, 1580, 1581, 1582, 1583,
  1585, 1586, 1587, 1588, 1590, 1591, 1597, 1598, 1640, 1642, 1643,
  1644, 1647, 1648, 1650, 1651, 1657, 1664, 1666, 1667, 1669, 1670,
  1671, 1672, 1674, 1675, 1677, 1678, 1679, 1681, 1683, 1684, 1685,
  1702, 1703, 1704, 1705, 1706, 1707, 1708, 1709, 1753, 1754, 2166,
  2167, 2168, 2526, 2701, 2702, 2703, 2704, 2705, 2719, 2720, 2721,
  2722, 2728, 2742, 2743, 2744, 2758, 2759, 2778, 3488, 3490, 3491,
  3492, 3493, 3494, 3495.
- `references/primary-sources/osv-hep-th-0405146.tex`: trailing
  whitespace at lines 1256, 1510, 1528, 1529, 1552, 1711.

I did not patch these fixture whitespace findings because the assigned
ownership is report-only except for a one-line fatal TeX syntax/package
issue.  They do not block the root `main.tex` build because the files are
not input by `main.tex`.

## Decision

No root-manuscript compile blocker found in the changed TeX surface
checked here.  No minimal TeX patch was made.
