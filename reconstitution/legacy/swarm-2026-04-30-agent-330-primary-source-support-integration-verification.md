# Swarm 2026-04-30 Agent 330: Primary Source Support Integration Verification

Agent: 330.

Assignment: verify Agent 323's primary-source support frontier against current `main.tex`, `theorem-lanes.tex`, `open-obligations.tex`, and `claim-strength-ledger.tex`; classify patch targets as semantic or citation polish; make no TeX edits.

## Controls Loaded

- `CLAUDE.md`
- `~/ecosystem/INVARIANTS.md`
- `~/ecosystem/AGENTS-HARNESS.md`
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`

Worktree rule observed: the checkout contains many concurrent edits.  I did not revert, overwrite, stash, or amend anything.  The only files created by this agent are this report and `reconstitution/primary-source-support-integration-verification-2026-04-30.md`.

## Files Read

- `reconstitution/primary-source-support-frontier-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-323-primary-source-support-frontier-audit.md`
- `reconstitution/primary-source-theorem-support-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-246-primary-source-theorem-support-audit.md`
- `main.tex`
- `theorem-lanes.tex`
- `open-obligations.tex`
- `claim-strength-ledger.tex`
- `references/source-provenance.md`
- Costello, BMK/Koppelman, LQT/Tsygan, Tate bar-cobar/Quillen, Hormander, Weiss/Ran, and Omega source fixtures under `references/primary-sources/`

## Findings

No checked primary source is presently used to assert an unsupported theorem in the current theorem surfaces.

Agent 323's main classification survives current-file verification:

- Costello supports universal finite-scale BV/RG/QME grammar only.
- Costello--Li is a BCOV/HCS comparison and exclusion source only.
- BMK/Koppelman supports the classical kernel and homotopy identity only.
- LQT/Tsygan supports stable primitive/cyclic homology only.
- Tate/Quillen/model-category sources support ordinary/conilpotent grammar only.
- Hormander supports microlocal operation criteria only.
- Weiss/Ran/AFT/CG sources support descent and stratified-factorization grammar only.

## Urgent Patch Targets

These are semantic source-boundary patches:

- `main.tex:1289-1301`: add the BMK boundary after the displayed kernel.
- `theorem-lanes.tex:481-494`: mirror the BMK boundary in the theorem lane.
- `main.tex:1578-1596`: if a BMK citation is inserted in the proof, state that cutoff, diagonal-current sign, finite moments, and Matlis orientation are local.
- `main.tex:1418-1437`: preserve the current conditional wording around the one-pair analytic quotient.

## Citation Polish

These are not semantic blockers:

- `main.tex:1967-1993`: optional exact LQ84/Tsy83 theorem anchors.
- `main.tex:3797-3800`, `main.tex:3985-4009`, `main.tex:4018-4020`: current Costello--Gwilliam boundary is adequate.
- `main.tex:7732-7735`: optional exact Costello--Gwilliam theorem/page anchor for the universal quantum-observables statement.
- `main.tex:5685-5904`, `open-obligations.tex:102-142`, `claim-strength-ledger.tex:1148-1164`: optional Tate source-template sentence; current admissibility hypotheses are adequate.
- `claim-strength-ledger.tex:557-576`, `open-obligations.tex:597-617`, `theorem-lanes.tex:3608-3651`: Hormander page-anchor upgrade only.
- `open-obligations.tex:999-1236`, `theorem-lanes.tex:2881-3350`, `claim-strength-ledger.tex:843-895`: no source import; keep obstruction vectors.
- `references/source-provenance.md:8`: add rows for LQT/Tate/Hormander/Weiss/Omega fixtures when provenance integration is scheduled.

## Commands Run

Read/search commands only: `sed`, `nl -ba`, `rg`, `find`, `wc`, `git status --short`, and `test -e`.

## Deliverables

- `reconstitution/primary-source-support-integration-verification-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-330-primary-source-support-integration-verification.md`
