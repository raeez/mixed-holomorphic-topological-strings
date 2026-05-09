# BMK Bibliography Build-Risk Audit

Date: 2026-04-30.

Scope: live worktree audit of the BMK source-boundary patch and nearby
top-level control patches in `main.tex`.  No theorem text was reworked.
One permitted one-line bibliography patch was made.

## Finding

- Fatal bibliography risk found and patched.  The new
  `laurent-thiebaut-bmk` DOI had an unescaped underscore.  A minimal
  `amsrefs` `pdflatex -halt-on-error` test failed with
  `Missing $ inserted` on `10.1007/978-0-85729-030-4_3`.  After the patch to
  `10.1007/978-0-85729-030-4\_3`, the same minimal test passed.
- No duplicate `\bib{...}` keys were found in root TeX files.
- No `\cite{...}` or `\cites{...}` keys in root TeX files were missing
  from the `main.tex` bibliography.
- No duplicate `\label{...}` keys were found in root TeX files.
- Introduced BMK citations and top-level control references resolve to
  bibliography entries or labels.

## Minimal Patch

- `main.tex:10041`: escaped the DOI underscore in
  `doi={10.1007/978-0-85729-030-4\_3}`.

## Grep Anchors

BMK citation anchors:

```text
main.tex:1291:  \cite{laurent-thiebaut-bmk}*{Ch.~III, Def.~1.2, Lem.~1.3}
main.tex:1307:  \cite{ruppenthal-bmk}*{\S5, Def.~5.1, Thm.~5.2, Eq.~(10)}.  They do
main.tex:1594:  \cite{ruppenthal-bmk}*{\S5, Thm.~5.2}.  The cutoff derivative,
```

BMK bibliography anchors:

```text
main.tex:10030:\bib{laurent-thiebaut-bmk}{article}{
main.tex:10041:   doi={10.1007/978-0-85729-030-4\_3},
main.tex:10044:\bib{ruppenthal-bmk}{article}{
```

Changed BMK theorem-lane anchor:

```text
main.tex:1260:\begin{prop}[Bochner--Martinelli current data and finite-window obstruction for the native \(E_2\) lane]\label{prop:finite-window-bm-native-e2-transfer}
```

Introduced reference anchors checked against labels:

```text
main.tex:676:Definition~\ref{def:local-hamiltonian-chiral-factorization-algebra}; no
main.tex:840:Statement~\ref{thm:lane-constructed-chiral-interface}.  If
main.tex:1129:\begin{defn}[Local Hamiltonian holomorphic factorization algebra]\label{def:local-hamiltonian-chiral-factorization-algebra}
main.tex:1260:\begin{prop}[Bochner--Martinelli current data and finite-window obstruction for the native \(E_2\) lane]\label{prop:finite-window-bm-native-e2-transfer}
theorem-lanes.tex:1061:\begin{stmt}[Statement: constructed chiral algebra interface]\label{thm:lane-constructed-chiral-interface}
appendix-radial-parts-moyal.tex:908:\label{stmt:app-free-kernel-homotopy-obstruction}
appendix-radial-parts-moyal.tex:1037:\label{prop:app-radial-dual-potential-obstruction}
```

## Mechanical Checks

Commands with empty output:

```text
perl -0ne 'while(/\\bib\{([^}]+)\}/g){$n{$1}++; push @order,$1} END{for $k (@order){next if $seen{$k}++; print "$k\n" if $n{$k}>1}}' *.tex
perl -0ne 'while(/\\cites?\{([^{}]+)\}/g){for $k (split /\s*,\s*/,$1){$cite{$k}=1 if length $k}} while(/\\bib\{([^}]+)\}/g){$bib{$1}=1} END{for $k (sort keys %cite){print "$k\n" unless $bib{$k}}}' *.tex
perl -0ne 'while(/\\label\{([^}]+)\}/g){$n{$1}++; push @order,"$1:$ARGV"} END{for $entry (@order){($k,$f)=split /:/,$entry,2; next if $seen{$k}++; print "$k\n" if $n{$k}>1}}' *.tex
rg -n -P "doi=\{[^}]*([^\\\\])_" main.tex
```

New BMK `amsrefs` entry brace counts:

```text
laurent-thiebaut-bmk braces 11/11
ruppenthal-bmk braces 9/9
```

Minimal `amsrefs` compilation:

```text
Before patch: failed on unescaped DOI underscore with Missing $ inserted.
After patch: pdflatex exited 0.
```

Final whitespace check:

```text
git diff --check -- main.tex
Output: none; exit 0.
git diff --check --no-index -- /dev/null reconstitution/swarm-2026-04-30-agent-339-bmk-bibliography-build-risk-audit.md
Output: none; no whitespace diagnostics.  Exit code 1 is the normal
no-index diff-exists status for a new file.
```
