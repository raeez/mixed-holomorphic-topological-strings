# Swarm 2026-04-30 Agent 327 Report - Build-Log and Layout Warning Audit

## Assignment

Audit the latest build log and layout warnings after Agent 319's successful
`make pdf`.  Read the latest log if present, `out/main.pdf` metadata/log
files, and Agent 319's report.  Identify fatal errors, undefined references,
bibliography problems, theorem-surface overfull boxes, and whether the
warnings are caused by today's patches.  Write reports only.  Do not edit
manuscript TeX.

Files changed by Agent 327:

- `reconstitution/build-log-layout-warning-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-327-build-log-layout-warning-audit.md`

No manuscript TeX edited.

## Result

The latest log present is `out/main.log` from 2026-04-30 14:29 SAST.  It is
a successful build log and writes `out/main.pdf`, 435 pages, 2,345,871 bytes.
The PDF metadata agrees with Agent 319's report.

Fatal/reference/bibliography gate for that build state: clean.

Layout gate for the current worktree: not closed.  `local-dictionary.tex`,
`open-obligations.tex`, `claim-strength-ledger.tex`, `theorem-lanes.tex`, and
`main.tex` were modified after the 14:29 log.  The log audits Agent 319's
build state, not the present source state.

## Evidence

Build artifact:

- `out/main.pdf`: 435 pages, 2,345,871 bytes.
- Creation/modification metadata: 2026-04-30 14:29:33 SAST.
- PDF SHA-256:
  `e750b627269ffaeb83a69816b37625bb294567bc9a7b503082bdff0353a7ab3c`.
- `out/main.log` SHA-256:
  `b8d3007e8e8e1554e7c03f02b3fb724bfb3c6bdc71a989ca68dd81f7adfa69cb`.

Fatal and reference scan:

- No `^!` TeX fatal entries.
- No `Emergency stop`.
- No `Fatal error`.
- No `Undefined control sequence`.
- No `LaTeX Error`.
- No undefined-reference or undefined-citation warnings.
- No rerun or changed-label warning.
- No `LaTeX Warning` or `Package ... Warning` entries in the final log.

Bibliography:

- The build uses inline `amsrefs` bibliography entries in `main.tex`.
- No `.bbl`/`.blg` surface is present.
- `out/main.aux`: 35 unique cited keys, 37 `\bibcite` entries.
- Missing cited keys: none.
- Uncited bibliography entries: `beilinson-drinfeld-chiral`,
  `cattaneo-felder-bv`.  Nonfatal.

Index/nomenclature:

- `out/main.ilg` reports three `nomencl.ist` input-style errors for
  `lethead_prefix`, `lethead_suffix`, and `lethead_flag`.
- `out/main.nlo` and `out/main.nls` are empty.  No nomenclature entries were
  accepted or emitted.
- This is pre-existing support-surface noise, not a theorem-surface blocker
  and not caused by Agent 319.

Layout counts:

- Overfull `\hbox`: 5.
- Overfull `\vbox`: 1.
- Underfull `\hbox`: 66.
- Underfull `\vbox`: 0.

## Theorem-Surface Layout Targets

Only semantically meaningful overfulls are listed as patch targets.  Underfull
boxes are not theorem-surface blockers.

1. `claim-strength-ledger.tex:236-248`
   - Log anchor: `out/main.log:2527`.
   - Warning: overfull `\vbox`, 299.21832pt too high.
   - Meaning: control-ledger table row for QME cancellation and
     compact-CY/CoHA quarantine.
   - Patch target: make the initial ledger table breakable or split the
     compact-CY/CoHA quarantine row into a separate paragraph/table row.
     Preserve the claim that compact-CY/CoHA material supplies no local QME,
     Ext, cyclic, Weyl/Moyal, radial-parts, or kernel theorem support without
     the named obstruction and comparison morphisms.

2. `local-dictionary.tex:699-711`
   - Log anchor: `out/main.log:4556`.
   - Warning: overfull `\hbox`, 36.48196pt too wide.
   - Meaning: Omega obstruction vector
     `\operatorname{Ob}_\Omega`.
   - Patch target: split the tuple into an `aligned`/`gathered` display with
     one or two obstruction symbols per line.  Preserve all seven entries.

3. `tate-T1-weighted-completion.tex:1758-1772`
   - Log anchor: `out/main.log:23743`.
   - Warning: overfull `\hbox`, 1.29213pt too wide.
   - Meaning: quotient complex and quotient map in the regular-density
     finite-window mechanism.
   - Patch target: separate the quotient-complex definition from the
     `q_M` arrow or use `alignedat`; preserve the map
     `q_M\colon\mathcal Q^\bullet_{w,M}(I)\twoheadrightarrow
     \mathcal C^{\bullet,\mathrm{reg}}_{w,M}(I)`.

4. `tate-T1-weighted-completion.tex:2065-2080`
   - Log anchor: `out/main.log:24769`.
   - Warning: overfull `\hbox`, 15.05399pt too wide.
   - Meaning: exact computable obstruction
     `\eta^{\mathrm{reg}}_{n_0,M}`.
   - Patch target: use the already-defined
     `\mathcal C^{\bullet,\mathrm{reg}}_{w,M}(I)` in the cohomology target,
     or line-break the quotient target in an aligned display.  Preserve the
     curvature expression.

5. `open-obligations.tex:1221-1236`
   - Log anchor: `out/main.log:41700`.
   - Warning: overfull `\hbox`, 1.62016pt too wide.
   - Meaning: internal Weiss/Cech-Roos vector and external source-primary
     firewall.
   - Patch target: keep the displayed
     `\delta_{\mathrm{Weiss}}^{\check C/R}` vector and split the following
     prose.  Preserve the statement that
     `\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}` is external until a
     matched-conventions source fixture is supplied.

6. `appendix-radial-parts-moyal.tex:629-638`
   - Log anchor: `out/main.log:50600`.
   - Warning: overfull `\hbox`, 9.61589pt too wide.
   - Meaning: radial/Weyl correction `K_{4,4}`.
   - Patch target: split the four trace terms over an aligned display.
     Preserve coefficient `43/14`, all signs, all word orders, and the cyclic
     boundary assertion.

## Agent 319 Targets Checked

Agent 319's two non-layout semantic patch targets appear healed in the
current source:

- `theorem-lanes.tex:2110-2124` now defines
  `\operatorname{Prim}^{1\mathrm{cyc}}_{N,K,L}` as
  `\operatorname{im}\Theta_{N,K,L}` inside the stable invariant CE complex
  and maps it to `CC_{\mathrm{red},\le L}(A_{\psi,K})[1]`.
- `main.tex:4658-4690` now names the Cech cone
  `\Delta^{N,M}_{V,\mathcal U}`, the Roos class
  `\mathfrak w^{\check C/R}_{V,\Omega,N,M}`, and
  `\delta_{\mathrm{Weiss}}^{\check C/R}`.

Both fixes are newer than the 14:29 build log.  They are not build-certified
by the available log.

## Causality

Agent 319 did not cause the warnings: its report states, and the worktree
confirms, that it edited report files only.

Against Agent 083's earlier clean overfull state, all six overfull warnings
come from later 2026-04-30 TeX patches.  Against Agent 173's later gate, the
two `tate-T1-weighted-completion.tex` warnings and the
`appendix-radial-parts-moyal.tex` `K_{4,4}` warning were already present; the
`claim-strength-ledger.tex`, `local-dictionary.tex`, and
`open-obligations.tex` warnings are later control-surface/layout additions or
mutations.

## Checks Run

- Loaded `CLAUDE.md`, `AGENTS.md`, ecosystem voice/rubric excerpts, and the
  Vol II rectification skill.
- Read Agent 319's two reports.
- Inspected `out/main.log`, `out/main.aux`, `out/main.toc`, `out/main.ilg`,
  `out/main.nlo`, `out/main.nls`, and `out/main.pdf` metadata.
- Scanned the log for fatal, undefined-reference, undefined-citation,
  bibliography, rerun, warning, and box-warning patterns.
- Compared cited keys against `\bibcite` keys in `out/main.aux`.
- Checked current source anchors for each semantically meaningful overfull.
- Checked source mtimes against `out/main.log`.

## Remaining Obligation

Run a fresh build after the post-14:29 TeX edits settle.  The current latest
log is clean for Agent 319's build state, but it is stale relative to the
current source tree.
