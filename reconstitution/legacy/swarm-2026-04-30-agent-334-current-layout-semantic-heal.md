# Agent 334 current layout semantic heal - 2026-04-30

## Scope

Build/layout semantic patch review only.  I inspected
`reconstitution/build-log-layout-warning-audit-2026-04-30.md`, the live
`out/main.log`, and the current staged/unstaged source diffs.  I did not
run `make pdf`: the existing log is stale relative to current TeX edits,
but the warning targets were already localized and the requested scope was
not a fresh build gate.

## Inputs

- `CLAUDE.md`, `AGENTS.md`.
- `~/ecosystem/INVARIANTS.md` voice rules and
  `~/ecosystem/AGENTS-HARNESS.md` self-reflection rubric.
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
  through the local `chriss-ginzburg-rectify` wrapper.
- `reconstitution/build-log-layout-warning-audit-2026-04-30.md`.
- `out/main.log`.
- Current source windows in `claim-strength-ledger.tex`,
  `local-dictionary.tex`, `tate-T1-weighted-completion.tex`,
  `open-obligations.tex`, and `appendix-radial-parts-moyal.tex`.

## Warning surface

The prior log records 5 overfull hboxes, 1 overfull vbox, and 66 underfull
hboxes.  The log was written at 14:29 SAST; current source files changed
after that time.  The log therefore identifies defects but cannot certify
the current worktree.

The underfull hboxes are narrow-column justification artifacts.  I found no
underfull warning encoding a mathematical readability defect.

The six overfull targets were mathematical readability defects:

- `claim-strength-ledger.tex`: the status table was an unbreakable
  `tabular`; the log reported a 299.21832pt overfull vbox.  This can hide
  the control ledger across a page break.
- `local-dictionary.tex`: `\operatorname{Ob}_\Omega` was written as one
  TeX math line although the source showed visual line breaks.  The seven
  obstruction names are a control surface and must be readable.
- `tate-T1-weighted-completion.tex`: the regular-density quotient complex
  and the computable obstruction target were long unaligned displays.
- `open-obligations.tex`: the internal Weiss vector and external
  `\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}` firewall paragraph
  formed one tight run-on status sentence.
- `appendix-radial-parts-moyal.tex`: the `K_{4,4}` correction display was
  one TeX math line; its coefficient, signs, and word order are load-bearing.

## Heal

Applied only layout-preserving edits:

- Converted the first `claim-strength-ledger.tex` status table to a
  breakable `longtable` with ragged p-columns.  Claim surfaces, statuses,
  and boundary text are unchanged.
- Rewrote the `local-dictionary.tex` `\operatorname{Ob}_\Omega` tuple as
  an `aligned` display.  The seven entries remain in the same order.
- Rewrote the regular-density quotient definition in
  `tate-T1-weighted-completion.tex` as an `aligned` display and used the
  already-defined quotient complex
  `\mathcal C^{\bullet,\mathrm{reg}}_{w,M}(I)` in the cohomology target.
- Split the `open-obligations.tex` source-primary firewall into shorter
  sentences.  Its status remains external.
- Rewrote the `appendix-radial-parts-moyal.tex` `K_{4,4}` correction as
  an `aligned` two-line display.  The coefficient `43/14`, all signs, all
  trace words, and the cyclic-boundary statement are unchanged.

## Status

No full build was run.  A later build is still needed to certify the final
layout surface because `out/main.log` predates current source edits.  The
semantic overfulls named by the available audit have been healed without
changing theorem strength.
