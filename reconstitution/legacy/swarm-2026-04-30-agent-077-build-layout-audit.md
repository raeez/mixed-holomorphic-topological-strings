# Agent 077 Build/Layout/Reference Audit

Lane: fresh build/layout/reference audit after layout repairs 058/059/062/067/068/072 and theorem repair 066.

## Inputs Loaded

- `CLAUDE.md`
- `Makefile`
- `main.tex`
- stale `out/main.log` before rebuild
- present prior reports:
  - `reconstitution/swarm-2026-04-30-agent-062-cross-volume-layout.md`
  - `reconstitution/swarm-2026-04-30-agent-066-quantum-coefficient-surface.md`
  - `reconstitution/swarm-2026-04-30-agent-067-open-obligations-layout.md`
  - `reconstitution/swarm-2026-04-30-agent-068-hadamard-ml-layout.md`
  - `reconstitution/swarm-2026-04-30-agent-072-t3-mc-layout.md`
- absent prior reports:
  - no `agent-058` report found under `reconstitution/`
  - no `agent-059` report found under `reconstitution/`

## Commands Run

- `pwd && git status --short`
- `sed -n '1,220p' CLAUDE.md`
- `sed -n '1,220p' Makefile`
- `sed -n '221,520p' Makefile`
- `wc -l main.tex`
- `wc -l out/main.log`
- `stat -f '%Sm %N' out/main.log`
- `sed -n '1,140p' main.tex`
- `rg --files reconstitution | rg 'agent-0(58|59|62|66|67|68|72)'`
- `sed -n '1,220p'` on reports 062, 067, 068, 072
- `sed -n '1,260p'` on report 066
- `make pdf`
- post-build diagnostic scans with `rg`, `sed`, `nl`, `stat`, `find`, and `git status --short --ignored out`

Two exploratory `rg` commands failed because of an over-escaped regex; they did
not modify the tree and were replaced by fixed `rg -e` / `rg -F` scans.

## Build Status

- Fresh build command: `make pdf`
- Result: pass, exit code `0`
- Final output: `out/main.pdf`, 254 pages, 1,501,480 bytes
- Final transcript: `out/main.log`, timestamp `Apr 30 06:31:31 2026`

## Fatal / Reference / Citation Status

Final-pass `out/main.log` contains:

- Fatal errors: `0`
- Emergency stops: `0`
- Undefined control sequences: `0`
- Runaway arguments / file-ended scans / no-pages failures: `0`
- Undefined LaTeX references: `0`
- Undefined citations: `0`
- `There were undefined references`: `0`
- `There were undefined citations`: `0`
- `Label(s) may have changed`: `0`
- Missing pdfTeX destination warnings: `0`

The first build pass still saw stale references to
`thm:quantum-coefficient-surface`, but the final `make pdf` pass resolved them.
Current anchors are present at `main.tex:7131`, `main.tex:7290`,
`claim-strength-ledger.tex:88`, and `theorem-lanes.tex:1459`.

Non-fatal non-layout warnings:

- `hyperref` removes a superscript twice from a PDF string at `main.tex:39`,
  inside `\hypersetup` metadata.  This is not a reference/citation blocker.

## Box Counts

Final-pass box warnings in `out/main.log`:

- Overfull `\hbox`: `2`
- Overfull `\vbox`: `1`
- Underfull `\hbox`: `24`
- Underfull `\vbox`: `0`

## Top Remaining Warnings

Overfulls:

- `appendix-radial-parts-moyal.tex:711`: overfull `\hbox`, `85.42854pt` too
  wide, in the display ending the primary/higher-order Cartan and graph-weight
  checklist at lines 706--710.
- `local-dictionary.tex:284--285`: overfull `\hbox`, `17.2633pt` too wide,
  in the dictionary table row beginning
  `cofactorization/opposite-interval source`.
- `local-dictionary.tex`: overfull `\vbox`, `61.49878pt` too high, while
  outputting the local dictionary table page immediately before the line-284
  table overfull.  The log gives no source line for this `\output` warning.

Highest-badness underfulls:

- `claim-strength-ledger.tex:170--173`: badness `10000`, ledger row for the
  open non-scalar Costello graph/QME construction.
- `tate-T1-weighted-completion.tex:246--256`: badness `7558` and `10000`,
  Casimir finite-window paragraph.
- `tate-T1-weighted-completion.tex:1103--1107`: badness `10000`, finite-window
  weighted CE/PV conjugacy sentence.
- `tate-T2-nilpotent-truncation.tex:9--29`: badness `5345`, opening theorem
  status paragraph.
- `tate-T5-chain-level-primitive.tex:83--99`: badness `7308`, open `P_0`
  bracket filtration paragraph.
- `main.tex:5196--5213` and `main.tex:5214--5235`: badness `10000`, `5970`,
  and `6575`, Matlis/principal-part equivariance coefficient proof.
- `main.tex:6362--6368`: badness `10000` and `2990`, connected single-trace
  projection display sentence.
- `main.tex:7164--7185`: badness `4608`, weighted Moyal principal-part target
  paragraph in `thm:quantum-coefficient-surface`.
- `main.tex:7679--7682`: badness `10000`, first-order ribbon-graph coefficient
  item.
- `tate-P3-universality.tex:449--457`: badness `8038`, admissible
  protected-sector reduction proposition.
- `appendix-factorization-current-conventions.tex:361--372`: badness `3439`
  and `5548`, boundary remark for the algebraic current theorem.
- `tate-P5-cross-volume.tex:132--134`: badness `4060`, compact Hamiltonian
  period complex definition.
- `main.tex:8145`: badness `3601`, bibliography entry for Costello 2016.

Other underfulls remain in `main.tex:453--456`, `main.tex:2239--2244`,
`main.tex:2731--2741`, and `main.tex:2797--2820`.

## Generated Artifacts Touched

The build regenerated or touched:

- `out/main.aux`
- `out/main.idx`
- `out/main.ilg`
- `out/main.log`
- `out/main.nls`
- `out/main.pdf`
- `out/main.toc`

Only `out/main.pdf` is tracked and now appears as an unstaged modification.
Ignored generated files remain unstaged.  No generated artifact was staged.

## Recommended Next Repair Lanes

1. `appendix-radial-parts-moyal.tex:706--711`: split or restructure the
   checklist display; this is the largest remaining overfull and the only
   80pt+ box warning.
2. `local-dictionary.tex:276--299`: repair the table layout; this lane owns
   both the remaining `17.2633pt` hbox and the unline-numbered `61.49878pt`
   output-active vbox.
3. `tate-T1-weighted-completion.tex`: repair the Casimir and finite-window
   conjugacy paragraphs at lines 246--256 and 1103--1107.
4. `main.tex` quantum/layout lane: repair the dense Matlis/principal-part and
   quantum coefficient-surface paragraphs at lines 5196--5235, 6362--6368,
   7164--7185, and 7679--7682 without changing theorem strength.
5. Lower-priority underfull cleanup: `claim-strength-ledger.tex:170--173`,
   `tate-T2-nilpotent-truncation.tex:9--29`,
   `tate-T5-chain-level-primitive.tex:83--99`,
   `tate-P3-universality.tex:449--457`,
   `appendix-factorization-current-conventions.tex:361--372`,
   `tate-P5-cross-volume.tex:132--134`, and the bibliography line
   `main.tex:8145`.

No current TeX fatal, unresolved reference, unresolved citation, or undefined
control-sequence lane is needed.
