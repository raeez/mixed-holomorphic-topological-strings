# Agent 356 postbuild log check spec

Date: 2026-04-30.

Scope: report-only postcheck specification for the root `make pdf` build.
No manuscript TeX was edited.  This spec reads Agent 353's prebuild plan as
the controlling build invocation:

```bash
ts=$(date +%Y%m%d-%H%M%S)
make pdf > ".build_logs/make-pdf-$ts.log" 2>&1
```

Run the commands below from `/Users/raeez/topological-strings` after
`make pdf` returns.  If `make pdf` exits nonzero, the build gate fails; still
run the grep commands to identify the first fatal cause.

## Postbuild commands

```bash
: "${ts:?set ts to the timestamp used for .build_logs/make-pdf-$ts.log}"
postcheck_dir=".build_logs/postbuild-$ts"
mkdir -p "$postcheck_dir"

root_build_paths=(
  main.tex
  raeez-math-template.sty
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
)
freshness_paths=(Makefile "${root_build_paths[@]}")

ls -l \
  ".build_logs/make-pdf-$ts.log" \
  out/main.pdf out/main.log out/main.aux out/main.toc out/main.idx \
  out/main.ilg out/main.nlo out/main.nls \
  > "$postcheck_dir/artifacts.txt"

stat -f '%Sm %N' \
  ".build_logs/make-pdf-$ts.log" \
  out/main.pdf out/main.log out/main.ilg out/main.nlo out/main.nls \
  > "$postcheck_dir/artifact-mtimes.txt"

test -s ".build_logs/make-pdf-$ts.log"
test -s out/main.log
test -s out/main.pdf
test -s out/main.aux
test -s out/main.toc
test -f out/main.idx
test -f out/main.ilg
test -f out/main.nlo
test -f out/main.nls

grep -aEn '^Output written on out/main\.pdf \([0-9]+ pages?, [0-9]+ bytes\)\.' \
  out/main.log > "$postcheck_dir/output-written.txt" || true

grep -aEn '(^!|Emergency stop|Fatal error|Undefined control sequence|Runaway argument|File ended while scanning|No pages of output|TeX capacity exceeded|LaTeX Error|Package [^ ]+ Error|Missing \$ inserted|Missing \\endcsname inserted|Extra \\end|Misplaced alignment tab character)' \
  ".build_logs/make-pdf-$ts.log" out/main.log \
  > "$postcheck_dir/fatal-tex.txt" || true

grep -aEn '(LaTeX Warning: (Reference|Citation) .* undefined|Citation .*undefined|Reference .*undefined|There were undefined references|There were undefined citations|Label\(s\) may have changed|Rerun to get cross-references right)' \
  out/main.log > "$postcheck_dir/undefined-crossrefs-cites.txt" || true

grep -aEn '(multiply[ -]defined|Label .* multiply defined|destination with the same identifier|pdfTeX warning.*duplicate|name\{.*\} has been referenced but does not exist)' \
  out/main.log > "$postcheck_dir/duplicate-labels-destinations.txt" || true

grep -aEn '((LaTeX|Package|Class|pdfTeX) Warning|Missing character:|Font shape .* undefined|Some font shapes were not available)' \
  out/main.log > "$postcheck_dir/warnings-all.txt" || true

grep -aEn '(LaTeX Warning: (Reference|Citation|Label)|There were undefined|multiply[ -]defined|Rerun to get cross-references right|Package (amsrefs|hyperref|nameref|cleveref|xr|refcount) Warning|pdfTeX warning.*(duplicate|destination)|Missing character:|Font shape .* undefined|Some font shapes were not available)' \
  out/main.log > "$postcheck_dir/warnings-that-matter.txt" || true

grep -aEn -B4 -A4 'Overfull \\[hv]box|Underfull \\[hv]box' \
  out/main.log > "$postcheck_dir/box-warnings-context.txt" || true

grep -aEn 'Overfull \\[hv]box' \
  out/main.log > "$postcheck_dir/overfull-boxes.txt" || true

grep -aEn 'Underfull \\vbox|Underfull \\hbox \(badness 10000\)' \
  out/main.log > "$postcheck_dir/underfull-high-badness.txt" || true

grep -aEn '(!!|Input style error|Unknown specifier|Error|Warning)' \
  out/main.ilg > "$postcheck_dir/main-ilg-errors.txt" || true

grep -ac 'Input style error' \
  out/main.ilg > "$postcheck_dir/main-ilg-input-style-error-count.txt" || true

grep -aE 'Unknown specifier' out/main.ilg \
  | sed -E 's/.*Unknown specifier ([^.]*)\..*/\1/' \
  | sort -u > "$postcheck_dir/main-ilg-unknown-specifiers.txt"

printf '%s\n' lethead_flag lethead_prefix lethead_suffix \
  | sort > "$postcheck_dir/main-ilg-known-specifiers.txt"

comm -23 \
  "$postcheck_dir/main-ilg-unknown-specifiers.txt" \
  "$postcheck_dir/main-ilg-known-specifiers.txt" \
  > "$postcheck_dir/main-ilg-unexpected-specifiers.txt"

wc -c out/main.nlo out/main.nls > "$postcheck_dir/nomenclature-sizes.txt"

find "${freshness_paths[@]}" -newer out/main.log -print \
  > "$postcheck_dir/sources-newer-than-main-log.txt"

find "${freshness_paths[@]}" -newer out/main.pdf -print \
  > "$postcheck_dir/sources-newer-than-main-pdf.txt"

find "${freshness_paths[@]}" -newer ".build_logs/make-pdf-$ts.log" -print \
  > "$postcheck_dir/sources-newer-than-make-log.txt"

for f in \
  fatal-tex.txt \
  undefined-crossrefs-cites.txt \
  duplicate-labels-destinations.txt \
  warnings-that-matter.txt \
  overfull-boxes.txt \
  main-ilg-unexpected-specifiers.txt \
  sources-newer-than-main-log.txt \
  sources-newer-than-main-pdf.txt \
  sources-newer-than-make-log.txt
do
  if [ -s "$postcheck_dir/$f" ]; then
    printf 'FAIL %s\n' "$postcheck_dir/$f"
  fi
done

test -s "$postcheck_dir/output-written.txt" \
  || printf 'FAIL missing final Output written line in out/main.log\n'
```

## Failure criteria

Hard build failures:

- `make pdf` exits nonzero.
- Any required artifact test above fails: missing or empty
  `.build_logs/make-pdf-$ts.log`, `out/main.log`, `out/main.pdf`,
  `out/main.aux`, or `out/main.toc`; missing `out/main.idx`,
  `out/main.ilg`, `out/main.nlo`, or `out/main.nls`.
- `$postcheck_dir/output-written.txt` is empty.  The final `main.log` must
  contain the `Output written on out/main.pdf` line.
- `$postcheck_dir/fatal-tex.txt` is nonempty.
- `$postcheck_dir/undefined-crossrefs-cites.txt` is nonempty.
- `$postcheck_dir/duplicate-labels-destinations.txt` is nonempty.
- Any freshness file is nonempty.  A source in `freshness_paths` newer than
  `out/main.log`, `out/main.pdf`, or `.build_logs/make-pdf-$ts.log` means an
  agent edited a build input during or after the build; rerun after the tree
  settles.

Warnings that matter:

- `$postcheck_dir/warnings-that-matter.txt` must be empty for a closed build
  gate.  It catches reference/citation warnings, changed-label rerun
  warnings, duplicate destinations, `amsrefs`/`hyperref`/reference-system
  warnings, missing glyphs, and font-shape substitution warnings.
- `$postcheck_dir/warnings-all.txt` is an audit ledger.  If it is nonempty
  while `warnings-that-matter.txt` is empty, read it before accepting the
  build; accept only warnings with a named reason and no theorem-surface
  effect.

Layout failures:

- `$postcheck_dir/overfull-boxes.txt` is a layout failure.  Agent 327's stale
  warning surface named six old targets, but a fresh postbuild gate should
  not silently accept them.  If any overfull remains, inspect
  `$postcheck_dir/box-warnings-context.txt`, map the warning to the source
  line, and record whether it is a theorem/display/table surface needing TeX
  repair.
- `$postcheck_dir/underfull-high-badness.txt` is not automatically fatal.
  It becomes a failure when the context lies in a theorem statement, displayed
  coefficient identity, obstruction vector, longtable, or page break carrying
  mathematical data.

`main.ilg` and nomenclature:

- `$postcheck_dir/main-ilg-unexpected-specifiers.txt` is a hard failure.
- If `$postcheck_dir/main-ilg-errors.txt` is nonempty only because of the
  known `nomencl.ist` `lethead_prefix`, `lethead_suffix`, and `lethead_flag`
  support-surface errors, and `out/main.nlo` and `out/main.nls` are both
  zero bytes, record it as nonblocking support noise.
- Any other `main.ilg` error, warning, or unknown specifier fails the
  postbuild gate.
- If `out/main.nlo` is nonzero and `out/main.nls` is zero or stale, the
  nomenclature pass failed and the build is not closed.

## Notes from Agent 353

Agent 353's prebuild plan exempts raw primary-source fixture whitespace from
the root build gate.  This postbuild spec follows that decision.  The
freshness scan is restricted to the `main.tex` input closure and the build
recipe; it does not use a global `find . -name '*.tex' -newer ...` scan,
because standalone TeX files and raw source fixtures can be newer without
entering the root manuscript build.
