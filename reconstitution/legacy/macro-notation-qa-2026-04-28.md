# Macro and Notation QA

## Safe repairs

- Collapsed the duplicate active renewal block in `mathmacros.tex` and
  mirrored the same support-file cleanup in `notation.tex`.
- Preserved the previous final rendered bodies for the named residuals:
  `\Ind` remains `\mathbf{Ind}`, `\Fun` remains `#1( #2 )`,
  `\Frac` remains `\mathbf{Frac}( #1 )`, `\shfcoH` remains
  `\mathbf{H}^{#3}(#1,#2)`, `\Schemes` remains `\Cat{Sch}`, and
  `\IndNSt` remains `\Cat{Ind}-\textsc{N}-\Cat{Stacks}`.
- Removed later renewals for identical bodies in the class-formation block:
  `\Pic`, `\AJ`, `\divisor`, `\divisoridshf`, `\IndProSch`,
  `\FinIndProSch`, `\Pro`, `\IndPro`, `\FinIndSch`, `\A`,
  `\curriedleftarg`, `\Zp`, `\Qp`, `\Hilb`, `\inj`, `\injects`,
  `\fst`, `\snd`, `\thrd`, `\nth`, `\hshfcoH`, `\Obj`, `\grpring`,
  `\Ext`, `\Exts`, `\dualmod`, `\LModCat`, `\RModCat`, `\indlim`,
  `\NoethSch`, `\NoethIntSch`, `\Sch`, `\IndSch`, `\ModCat`,
  `\grkAlg`, and `\ZAlg`.
- Collapsed `\T` by defining it directly as `\mathbf{T}` and removing the
  later renewal. This preserves the active final meaning and avoids passing
  through `\mbf`.

## Rejected risky repairs

- `\mbf` divergence is unresolved. `commands.tex` defines
  `\mbf` as `\mathbf`, while `mathmacros.tex` defines it as `\mathbb`.
  The active root uses `mathmacros.tex`; the direct live consumers are
  `\Hirz` and `\Tot`, and scan evidence found no direct manuscript use.
  Trusted context forbids changing this without a full semantic decision.
- `commands.tex` and `mathmacros.tex` still overlap. The root manuscript
  inputs `mathmacros.tex`, not `commands.tex`; unifying these support
  surfaces would alter image, nomenclature, and `\mbf` behavior.
- `\Vec` in `mathmacros.tex` and `notation.tex`, `\P` in
  `mathmacros.tex`, and `\dim` in `notation.tex` remain active renewals.
  They are not duplicate self-overwrites in the healed block; they touch
  pre-existing LaTeX/template commands and require a separate convention
  pass.
- Nomenclature remains a support-surface risk. `nomenclature.tex` is not
  input by `main.tex`, `\printnomenclature` is absent, and `mathmacros.tex`
  disables `\nm`. Entries such as `\Schemes` and `\IndNSt` describe the
  long names while the active macros render abbreviated category symbols.

## Verification

- `pdflatex` macro smoke passed with the local template path and exercised
  `\Ind`, `\Fun`, `\Frac`, `\shfcoH`, `\Schemes`, `\IndNSt`, and `\T`:
  `TEXINPUTS=.:/Users/raeez/latex-template: pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/topological-strings-macro-smoke-20260428 ...`
- The same smoke passed under `memoir` with `mathmacros.tex` and
  `authors.tex` loaded.
- Duplicate-renewal scan for the healed named set returned zero active
  hits:
  `rg -n '\\rc\s*\\(Ind|Pic|AJ|divisor|divisoridshf|IndProSch|FinIndProSch|Pro|IndPro|FinIndSch|A|Fun|Frac|curriedleftarg|Zp|Qp|Hilb|inj|injects|fst|snd|thrd|nth|shfcoH|hshfcoH|Obj|grpring|Ext|Exts|dualmod|LModCat|RModCat|indlim|Schemes|NoethSch|NoethIntSch|Sch|IndSch|ModCat|grkAlg|ZAlg|IndNSt|T)\b' mathmacros.tex notation.tex`.
- Direct-use scan found the named residuals only in macro surfaces and
  nomenclature/support entries, not in `main.tex` content.
- `git diff --check -- mathmacros.tex notation.tex commands.tex nomenclature.tex preamble.tex`
  passed.
