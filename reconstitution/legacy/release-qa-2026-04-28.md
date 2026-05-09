# Release QA ledger

Date: 2026-04-28

Worker: W2-H06, hygiene and release-QA scope.

Writable scope honored: this pass edited only `nomenclature.tex` and this
ledger.  No theorem-bearing manuscript file was changed.

## Verdict

The narrow publication-facing hygiene repair is complete: the active
nomenclature entries no longer contain the informal quotient-category joke,
the stale `blah` nomenclature residue was removed, and one duplicate active
`\Set` nomenclature row was deleted.

The manuscript is not release-clean.  The strongest surviving QA risks are
visible document numbering (`0.x` sections and `.1` appendix numbering),
stale manuscript date, broad duplicate macro/convention surfaces across
`mathmacros.tex` and `notation.tex`, and rendered cross-volume/process
phrasing that must be handled by theorem-file owners.

## Macro and notation hygiene

Checked files: `commands.tex`, `mathmacros.tex`, `notation.tex`,
`nomenclature.tex`, plus `preamble.tex` for front-matter package/counter
surface.

Safe edits made:

- `nomenclature.tex:38`: replaced `everyone's favourite quotient category`
  for `\B{G}` by a neutral classifying-quotient description.
- `nomenclature.tex:39`: replaced the same phrase for `\ptmod{G}` by a
  neutral point-quotient description.
- Removed commented `blah` nomenclature residue.
- Removed one duplicate active `\Set` nomenclature row.

Post-edit scan:

- `rg -n -F "favourite" commands.tex mathmacros.tex notation.tex nomenclature.tex main.tex`
  returned no matches.
- `rg -n -F "blah" commands.tex mathmacros.tex notation.tex nomenclature.tex main.tex`
  returned no matches.
- `rg -n "TODO|blah|favourite|favorite" commands.tex mathmacros.tex notation.tex nomenclature.tex`
  still reports many TODO comments, especially in `commands.tex`,
  `mathmacros.tex`, and `notation.tex`.  These are repository-hygiene debt,
  not all publication-facing text.

Duplicate/convention risks found but not edited:

- `mathmacros.tex` and `notation.tex` duplicate a large inherited notation
  block almost verbatim.  A mechanical duplicate scan reports repeated
  definitions for `\Cat`, `\Ind`, `\Pic`, `\AJ`, `\Ext`, `\Spec`,
  `\Hilb`, `\DMod`, and many others.
- `commands.tex` overlaps with `mathmacros.tex` on `\image`, `\imageopt`,
  `\mc`, `\mbb`, `\mbf`, delimiter macros, and `\nc`/`\rc`.
- High-risk example: `commands.tex:160` defines `\mbf` as `\mathbf`, while
  `mathmacros.tex:16` defines `\mbf` as `\mathbb`.  Main currently inputs
  `mathmacros.tex`, not `commands.tex`, but the convention risk is real if
  support files are combined later.
- High-risk example: `mathmacros.tex:10` disables `\nm`, while
  `commands.tex:154` maps `\nm` to `\nomenclature`.

No broad macro edits were made because the duplicate surface is too wide for a
safe hygiene patch.

## Rendered front matter and table risk

Anchors:

- `main.tex:12`: `\date{2018}` is stale for this 2026 reconstitution.
- `main.tex:43-46`: abstract, claim-strength ledger, local dictionary, and
  table of contents are rendered before the body.
- `main.toc:2-52`: rendered main sections are numbered `0.1`, `0.2`, etc.
- `main.toc:53-71`: the cross-volume section is numbered `.1`, with
  subsections `.1.1`, etc.

Risk status: release-blocking visual/document-integrity issue.  Not edited
here because `main.tex` is outside this worker's writable scope.

## Figure and proof alignment

Figure-reference scan:

- `rg -n "firstorder|thirdordera|thirdorderb" .` finds the static assets only
  in instruction files.  `main.tex` does not include those PNG/SVG assets.
- `rg -n -F "\includegraphics" main.tex commands.tex mathmacros.tex preamble.tex`
  finds only helper macro definitions in support files, not graph inclusion
  in `main.tex`.
- `main.tex:4794-4808` is the inline TikZ caption for `fig:gamma1`.
- `main.tex:5944-5960` is the inline TikZ caption for `fig:gamma3`.

Caption status:

- `fig:gamma1` states first-order status and explicitly identifies the
  order-`\hbar` Moyal coefficient at `main.tex:4804-4805`.
- The prose after `fig:gamma1` says the graph records the single contraction
  and is not a separate Feynman-integral proof (`main.tex:4810-4813`).
- `fig:gamma3` states the third-order graphs, the order-`\hbar^3` boundary
  contractions, the symmetry factors, the sum for `P^3(f,g)`, and the
  third-order Moyal weight `\hbar^3/24` (`main.tex:5944-5956`).
- The same caption and following prose keep Costello counterterm/anomaly
  checks conditional (`main.tex:5956-5959`, `main.tex:5962-5968`).

Risk status: the inline graph captions satisfy the order/conditional-status
QA obligation.  The old static graph assets are unreferenced by the manuscript
and may be stale archival assets.

## Primary-source anchoring

Scan command:

`rg -n -F "\cite" main.tex abstract.tex claim-strength-ledger.tex open-obligations.tex theorem-lanes.tex local-dictionary.tex tate-*.tex`

Evidence:

- Core source keys are present in the bibliography (`main.tex:6112` for BCOV,
  `main.tex:6149` for Witten, `main.tex:6254` for Costello renormalization,
  `main.tex:6267` and `main.tex:6276` for Costello-Li, `main.tex:6308` and
  `main.tex:6319` for Procesi/Razmyslov, `main.tex:6371` for Capelli).
- Several technical imports have section/theorem anchors, e.g.
  `tate-T1-weighted-completion.tex:55`, `tate-T1-weighted-completion.tex:323`,
  `tate-P1-hadamard-mittag-leffler.tex:31`, and `main.tex:5787`.
- The manuscript still lacks a dedicated citation ledger translating each
  imported theorem into local conventions.  Several high-level invocations in
  the introduction cite a source but not an exact theorem/equation anchor
  (`main.tex:151`, `main.tex:474`, `main.tex:960`, `main.tex:977`).

Risk status: adequate citation presence, incomplete primary-source audit
surface.

## Process-language scan

Scan command:

`rg -n "\b(phase|phases|rewrite|rewritten|reconstitution|process|draft|previous draft|old theorem|old|new paper|inscription pass|attack ledger|critique)\b" *.tex reconstitution/*.md`

Result:

- Most `phase` hits in `main.tex` are mathematical `phase space` language,
  not process language.
- Process-language hits are concentrated in `reconstitution/*.md`, which is
  acceptable for internal audit files.
- The earlier theorem-lane process-language risk is closed: the rendered
  theorem-lane preamble now says only that the entries keep stable
  cross-reference labels, with no old-label or prior-draft language.

Risk status: no rendered process-language risk remains in the theorem-status
surface checked here.

## Closed/global transfer scan

Scan command:

`rg -n "Vol III|Igusa|BKM|Borcherds|compact CY|compact CY3|CY3|global BCOV|consequence|not asserted|firewall|cross-volume|calabi-yau-quantum-groups" *.tex reconstitution/*.md`

Evidence:

- Good local firewalls are present in `abstract.tex:42-43`,
  `claim-strength-ledger.tex:103-105`, `open-obligations.tex:74-76`,
  `main.tex:5573-5585`, and `main.tex:6080-6107`.
- `tate-T4-bv-vanishing.tex:187-195` and
  `tate-T1-weighted-completion.tex:562-571` also contain explicit no-transfer
  firewall language.
- Residual risk: `tate-P5-cross-volume.tex` remains a large bidirectional
  transfer dictionary, with many Vol III/Igusa/BKM forward/backward transfer
  entries.  This matches the adversarial ledger's P1.7 concern and should be
  compressed or externalized by the owner of that theorem/outlook scope.

Risk status: local no-transfer disclaimers are present, but the volume and
placement of cross-volume material remain a release risk.

## Commands run

- `git branch --show-current` confirmed
  `agent/topological-strings-rearch2-hygiene-20260428`.
- `git status --short` showed the swarm worktree already had many unrelated
  modified/untracked files before this pass.
- Read: `CLAUDE.md`,
  `reconstitution/adversarial-attack-ledger-2026-04-28.md`,
  `preamble.tex`, `commands.tex`, `mathmacros.tex`, `notation.tex`,
  `nomenclature.tex`, graph figure anchors in `main.tex`, and the static
  `firstorder.svg`, `thirdordera.svg`, `thirdorderb.svg` assets.
- Ran the required `rg` scans for TODO/informal text, process language,
  cross-volume transfer terms, and graph labels.
- Ran a duplicate macro scan over `commands.tex`, `mathmacros.tex`, and
  `notation.tex`.
- Ran `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp main.tex`
  because this pass touched a TeX support file.  The draft compile stopped
  before the manuscript body with `File 'raeez-math-template.sty' not found`;
  `kpsewhich raeez-math-template.sty` and a repository file scan found no
  local style file.  The log was written to `/tmp/main.log`.

No commit, push, stash, reset, checkout, switch, restore, rebase, clean,
remove-worktree, or staging command was run.

## Residual risks

1. Fix `main.tex:12` and the `0.x`/`.1` numbering before release.
2. Remove rendered process-language residue from `theorem-lanes.tex:5`.
3. Decide whether `notation.tex` is dead support or a true source of notation;
   if it is active, deduplicate it against `mathmacros.tex` in one controlled
   macro pass.
4. Compress or externalize `tate-P5-cross-volume.tex` if the local theorem
   paper must avoid the appearance of exporting Vol III/Igusa/BKM claims.
5. Add a primary-source convention-translation ledger for BCOV, Witten,
   Costello, Costello-Li, Loday-Quillen-Tsygan, Procesi-Razmyslov, Capelli,
   Matlis/local cohomology, and radial-parts inputs.
