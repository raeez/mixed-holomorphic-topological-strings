# Build-Log and Layout Warning Audit - 2026-04-30

Agent: 327.
Scope: audit-only pass after Agent 319's reported successful `make pdf`.
No manuscript TeX was edited.

## Verdict

The latest build log present in `out/main.log` is a successful final
`pdflatex` pass from 2026-04-30 14:29 SAST.  It produced
`out/main.pdf`, 435 pages, 2,345,871 bytes.  The PDF metadata agrees:
creation and modification time 2026-04-30 14:29:33 SAST, author Raeez
Lorgat, producer `pdfTeX-1.40.27`, letter paper, PDF 1.7.

No TeX fatal error, undefined control sequence, LaTeX error, emergency
stop, runaway argument, unresolved reference, unresolved citation, rerun
request, package warning, or LaTeX warning is present in the latest
`out/main.log`.

The warning surface is layout-only, plus a stale-build caveat: five TeX
files changed after the 14:29 log was written.  Therefore the log audits
Agent 319's build state, not the current worktree state.  A fresh build is
needed before treating the present source tree as layout-cleared.

## Inputs Read

- `reconstitution/swarm-2026-04-30-agent-319-control-surface-post-bmk-theta3-lqt-audit.md`
- `reconstitution/control-surface-post-bmk-theta3-lqt-audit-2026-04-30.md`
- `out/main.log`
- `out/main.pdf` metadata from `pdfinfo`
- `out/main.aux`, `out/main.toc`, `out/main.idx`, `out/main.ilg`,
  `out/main.nlo`, `out/main.nls`
- Current source anchors for the warning lines.

## Build Artifact State

`out/main.pdf`:

- Pages: 435.
- Size: 2,345,871 bytes.
- SHA-256: `e750b627269ffaeb83a69816b37625bb294567bc9a7b503082bdff0353a7ab3c`.
- Log SHA-256: `b8d3007e8e8e1554e7c03f02b3fb724bfb3c6bdc71a989ca68dd81f7adfa69cb`.

Generated file timestamps:

- `out/main.pdf`: 2026-04-30 14:29:40 SAST.
- `out/main.log`: 2026-04-30 14:29:40 SAST.
- `out/main.aux`: 2026-04-30 14:29:40 SAST.
- `out/main.toc`: 2026-04-30 14:29:40 SAST.
- `out/main.ilg`: 2026-04-30 14:29:18 SAST.
- `out/main.nlo`: empty, 2026-04-28 01:21:49 SAST.
- `out/main.nls`: empty, 2026-04-30 14:29:18 SAST.

Post-log source modifications:

- `local-dictionary.tex`: 2026-04-30 14:30:44 SAST.
- `open-obligations.tex`: 2026-04-30 14:34:40 SAST.
- `claim-strength-ledger.tex`: 2026-04-30 14:35:22 SAST.
- `theorem-lanes.tex`: 2026-04-30 14:36:24 SAST.
- `main.tex`: 2026-04-30 14:38:32 SAST.

These post-log edits mean current line anchors were checked, but the
14:29 log cannot certify the current source tree.

## Fatal, Reference, and Bibliography Gate

Log scan result:

- Fatal TeX patterns: 0.
- Emergency stops: 0.
- Undefined control sequences: 0.
- LaTeX errors: 0.
- Runaway/file-ended scans: 0.
- Undefined references: 0.
- Undefined citations: 0.
- `Label(s) may have changed`: 0.
- `Rerun to get cross-references right`: 0.
- `LaTeX Warning`: 0.
- `Package ... Warning`: 0.

Bibliography state:

- The manuscript uses `amsrefs`-style inline bibliography entries in
  `main.tex`, not a `.bib` plus BibTeX/Biber pass.
- No `main.bbl` or `main.blg` exists under the current output surface.
- `out/main.aux` has 35 unique cited keys and 37 `\bibcite` entries.
- Missing cited keys: none.
- Uncited bibliography keys: `beilinson-drinfeld-chiral`,
  `cattaneo-felder-bv`.  These are not build defects.

Index/nomenclature state:

- `out/main.ilg` reports three `makeindex` style input errors from
  `nomencl.ist`: unknown `lethead_prefix`, `lethead_suffix`,
  `lethead_flag`.
- `out/main.nlo` is empty and `out/main.nls` is empty; makeindex accepted
  zero entries and wrote no nomenclature output.
- This is a support-surface warning, not a theorem-layout defect, and it is
  not caused by Agent 319.  The repository already carries older
  nomenclature reports; the active manuscript path does not depend on an
  emitted nomenclature list in this build.

## Layout Counts

From `out/main.log`:

- Overfull `\hbox`: 5.
- Overfull `\vbox`: 1.
- Underfull `\hbox`: 66.
- Underfull `\vbox`: 0.

Only the overfull boxes below are semantically meaningful enough to carry
patch targets.  Underfull boxes were not treated as theorem-surface
defects.

## Semantically Meaningful Layout Patch Targets

1. `claim-strength-ledger.tex:236-248`
   - Log: `out/main.log:2527`.
   - Warning: overfull `\vbox`, 299.21832pt too high, while output is
     active.
   - Surface: control ledger table, including the scalar-reduced QME
     branch and compact-CY/CoHA quarantine row.
   - Cause: today's control-ledger table expansion.  Agent 083 had zero
     overfulls earlier today; this block is added/expanded relative to
     `HEAD`.  The file was also modified after the 14:29 build, so a fresh
     build must remeasure it.
   - Exact patch target: convert the initial centered `tabular` ledger
     block into a breakable `longtable` or split the compact-CY/CoHA row
     into a separate paragraph/table row.  Preserve the quarantine meaning:
     no compact-CY/CoHA evidence supports local QME, Ext, cyclic,
     Weyl/Moyal, radial-parts, or kernel claims without
     `\operatorname{Ob}_{\mathfrak C_{\mathrm{tar}}}` and comparison
     morphisms.

2. `local-dictionary.tex:699-711`
   - Log: `out/main.log:4556`.
   - Warning: overfull `\hbox`, 36.48196pt too wide, detected at line 707.
   - Surface: Omega-background dictionary row naming
     `\operatorname{Ob}_\Omega`.
   - Cause: today's Omega obstruction-vector patch.  The displayed tuple is
     added relative to `HEAD`; `local-dictionary.tex` changed after the
     14:29 build, so current layout is unverified.
   - Exact patch target: split the `\operatorname{Ob}_\Omega` tuple into an
     `aligned` or `gathered` display with one or two obstruction symbols per
     line.  Do not rename or reorder the seven obstruction entries.

3. `tate-T1-weighted-completion.tex:1758-1772`
   - Log: `out/main.log:23743`.
   - Warning: overfull `\hbox`, 1.29213pt too wide, detected at line 1772.
   - Surface: finite-window quotient complex
     `\mathcal C^{\bullet,\mathrm{reg}}_{w,M}(I)` and quotient map `q_M`.
   - Cause: today's regular-density quotient-complex patch; this warning
     was already present in Agent 173's later build gate.
   - Exact patch target: separate the quotient definition from the
     `q_M` arrow, or use a short `alignedat` display.  The map
     `q_M\colon \mathcal Q^\bullet_{w,M}(I)\twoheadrightarrow
     \mathcal C^{\bullet,\mathrm{reg}}_{w,M}(I)` must remain explicit.

4. `tate-T1-weighted-completion.tex:2065-2080`
   - Log: `out/main.log:24769`.
   - Warning: overfull `\hbox`, 15.05399pt too wide, detected at line 2080.
   - Surface: exact computable obstruction
     `\eta^{\mathrm{reg}}_{n_0,M}`.
   - Cause: today's regular-density obstruction patch; this warning was
     already present in Agent 173's later build gate.
   - Exact patch target: replace the long displayed target
     `H^1(\mathcal Q^\bullet_{w,M}(I)/
     \mathcal X^{\bullet,\mathrm{reg}}_{w,M}(I))` by
     `H^1(\mathcal C^{\bullet,\mathrm{reg}}_{w,M}(I),\bar d_M)` after the
     quotient complex has been defined, or line-break the cohomology target
     inside an `aligned` block.  Do not change the curvature expression or
     the obstruction class.

5. `open-obligations.tex:1221-1236`
   - Log: `out/main.log:41700`.
   - Warning: overfull `\hbox`, 1.62016pt too wide, in paragraph at
     lines 1226--1234.
   - Surface: internal Weiss/Cech-Roos obstruction vector and the external
     source-primary firewall.
   - Cause: today's Weiss obstruction-vector patch.  This block is added
     relative to `HEAD`; `open-obligations.tex` changed after the 14:29
     build, so current layout is unverified.
   - Exact patch target: keep the displayed
     `\delta_{\mathrm{Weiss}}^{\check C/R}` vector, then split the
     following prose into shorter sentences.  The external status of
     `\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}` must remain explicit.

6. `appendix-radial-parts-moyal.tex:629-638`
   - Log: `out/main.log:50600`.
   - Warning: overfull `\hbox`, 9.61589pt too wide, detected at line 638.
   - Surface: radial/Weyl kernel correction
     `K_{4,4}` in the free trace-diagram normal-form computation.
   - Cause: today's radial all-`N` correction patch; this warning was
     already present in Agent 173's later build gate.
   - Exact patch target: split the four trace terms in `K_{4,4}` over an
     `aligned` display, likely two terms per line.  Preserve the coefficient
     `43/14`, all signs, all word orders, and the trailing statement that
     the cyclic boundary is zero.

## Agent 319 Semantic Targets

Agent 319 named two semantic TeX targets independent of layout:

- `theorem-lanes.tex:2107-2111`, malformed LQT source display.
- `main.tex:4639-4655`, stale Weiss/Ran total-complex wording.

In the current worktree both appear healed:

- `theorem-lanes.tex:2110-2124` now defines
  `\operatorname{Prim}^{1\mathrm{cyc}}_{N,K,L}:=
  \operatorname{im}\Theta_{N,K,L}\subset
  C_{*,\le L}^{\mathrm{CE}}(\mathfrak{gl}_N(A_{\psi,K}))^{GL_N}`
  and maps it to `CC_{\mathrm{red},\le L}(A_{\psi,K})[1]`.
- `main.tex:4658-4690` now names
  `\Delta^{N,M}_{V,\mathcal U}`,
  `\mathfrak w^{\check C/R}_{V,\Omega,N,M}`, and
  `\delta_{\mathrm{Weiss}}^{\check C/R}`.

These fixes landed after the 14:29 build log.  They need a fresh build
before the build gate can certify them.

## Causality

None of the warnings is caused by Agent 319's own edits: Agent 319 changed
only two report files and no manuscript TeX.

Against Agent 083's 2026-04-30 clean overfull baseline, all six current
overfull warnings are caused by later 2026-04-30 TeX patches.  Against Agent
173's later build gate, the two `tate-T1-weighted-completion.tex` hboxes and
the `appendix-radial-parts-moyal.tex` `K_{4,4}` hbox were already present;
the `claim-strength-ledger.tex`, `local-dictionary.tex`, and
`open-obligations.tex` warnings are later control-surface/layout additions or
mutations.

## Status

Build-log fatal/reference/bibliography gate: passed for the 14:29 build
state.

Current-worktree layout gate: not decided.  The latest log is stale relative
to post-log TeX edits in `main.tex`, `theorem-lanes.tex`,
`open-obligations.tex`, `claim-strength-ledger.tex`, and
`local-dictionary.tex`.
