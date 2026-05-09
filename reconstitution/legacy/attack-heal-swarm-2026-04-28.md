# Attack-heal swarm log: rearchitecture closure

Date: 2026-04-28

Integration owner: main thread.

Objective: heal the remaining faults identified in
`reconstitution/adversarial-attack-ledger-2026-04-28.md` so the local
Dirac-Witten reconstitution becomes a dependency-closed stable core rather than
a relabeled umbrella theorem.

Protocol: `~/ecosystem/.agents/skills/attack-heal-swarm` with the shared
`protocol.md` ledger-closure rule.  Agent reports are evidence, not authority;
the main thread verifies and integrates by interpretation hunks.

## Workers

| Worker | Scope | Writable surface |
|---|---|---|
| H01 | Main structural surgery: date, numbering, theorem package, early conjecture, dictionary prose, overclaim words | `main.tex` |
| H02 | Theorem-lane proof/index discipline | `theorem-lanes.tex` |
| H03 | Front status surfaces: abstract, claim ledger, dictionary, open obligations | `abstract.tex`, `claim-strength-ledger.tex`, `local-dictionary.tex`, `open-obligations.tex` |
| H04 | Outlook and cross-volume firewalls | `tate-P3-universality.tex`, `tate-P5-cross-volume.tex` |
| H05 | Weighted Tate / QME / regulator-independence status | `tate-T1-weighted-completion.tex` |
| H06 | New proof-spine appendices | new appendix TeX files only |

## Integration gates

1. Every worker must return or be recorded unavailable before convergence.
2. No worker commit, push, stash, reset, checkout, restore, rebase, clean, or
   worktree removal is accepted.
3. The main thread reads each changed hunk before accepting it.
4. Accepted repairs must preserve true mathematical content and move false or
   unproved claims into exact residual obligations, not rhetorical demotion.
5. Session-end verification must include targeted `rg` scans, the local
   computation scripts where relevant, and `make pdf` if the integrated TeX
   surface changes.

## Precommitted scans

- stale metadata and numbering: `date{2018}`, `numberline {0.`, `numberline {.`
- forbidden dictionary conflation: `same .*module`, `different bases`, close
  proximity of `E_{k,l}` / `\Psi_{k,l}` / `\rho_{k,l}`
- theorem-package residue: large multi-part statement at `thm:main-local`
- overclaim terms: `universal`, `universality`, `full`, `complete`,
  `precisely`, `forced`, `unique`, `canonical`
- status terms: `proved`, `conditional`, `conjectural`, `open`, `not asserted`
- cross-volume exports: `Vol III`, `Igusa`, `BKM`, `follows`, `transfer`

## Live status

First wave joined.  H02 and H03 wrote scoped repairs in the shared checkout;
H01, H04, H05, and H06 correctly downgraded to proposal-only because the
shared checkout was dirty and not isolated.

The principal then authorized explicit worktree writes.  Wave 2 was launched
under `/private/tmp/topological-strings-rearch-wave2-20260428`.

| Worker | Worktree | Branch | Writable surface |
|---|---|---|---|
| W2-H01 | `main` | `agent/topological-strings-rearch2-main-20260428` | `main.tex` |
| W2-H02 | `theorem-front` | `agent/topological-strings-rearch2-theorem-front-20260428` | `theorem-lanes.tex`, `abstract.tex`, `claim-strength-ledger.tex`, `local-dictionary.tex`, `open-obligations.tex` |
| W2-H03 | `outlook` | `agent/topological-strings-rearch2-outlook-20260428` | `tate-P3-universality.tex`, `tate-P5-cross-volume.tex` |
| W2-H04 | `weighted` | `agent/topological-strings-rearch2-weighted-20260428` | `tate-T1-weighted-completion.tex` |
| W2-H05 | `appendices` | `agent/topological-strings-rearch2-appendices-20260428` | new appendix TeX files only |
| W2-H06 | `hygiene` | `agent/topological-strings-rearch2-hygiene-20260428` | `reconstitution/release-qa-2026-04-28.md`, safe support-file hygiene only |

Wave 2 returned, was integrated by the main thread, and all six agents were
closed.  Integrated repairs include:

- front-matter status ledger, two-paragraph abstract, local dictionary, theorem
  lanes, and open-obligation surfaces;
- short main theorem package replacing the old umbrella theorem;
- protected-sector outlook and cross-volume firewall;
- weighted Tate theorem split from conditional QME lift;
- Matlis, factorization-current, and radial-parts appendices;
- safe nomenclature hygiene.

Shared-checkout verification after Wave 2:

- `make pdf` produced `out/main.pdf` with 137 pages.
- No unresolved references or citations surfaced in `out/main.log`.
- `git diff --check` passed.
- `python3 scripts/check_one_psi_homology.py` passed.
- `python3 scripts/check_moyal_coefficients.py` passed.
- TOC scan confirms main sections number `1,2,...` and appendices number
  `A,...`.

The principal then requested the next attack-heal cycle.  Wave 3 was launched
under `/private/tmp/topological-strings-rearch-wave3-20260428-0505`.

| Worker | Worktree | Branch | Writable surface |
|---|---|---|---|
| W3-H01 | `layout` | `agent/topological-strings-rearch3-layout-20260428` | `abstract.tex`, `claim-strength-ledger.tex`, `local-dictionary.tex` |
| W3-H02 | `overclaim` | `agent/topological-strings-rearch3-overclaim-20260428` | `main.tex`, `principles.tex`, `tate-*.tex` |
| W3-H03 | `notation` | `agent/topological-strings-rearch3-notation-20260428` | `commands.tex`, `mathmacros.tex`, `notation.tex`, `nomenclature.tex`, `preamble.tex` |
| W3-H04 | `sources` | `agent/topological-strings-rearch3-sources-20260428` | `reconstitution/source-convention-ledger-2026-04-28.md`, `reconstitution/release-qa-2026-04-28.md` |
| W3-H05 | `appendix` | `agent/topological-strings-rearch3-appendix-20260428` | `appendix-matlis-principal-parts.tex`, `appendix-factorization-current-conventions.tex`, `appendix-radial-parts-moyal.tex`, `theorem-lanes.tex`, `open-obligations.tex` |
| W3-H06 | `referee` | `agent/topological-strings-rearch3-referee-20260428` | `reconstitution/wave3-referee-report-2026-04-28.md` |

Wave 3 returned and was integrated by the main thread.  All six agents were
closed.  Accepted repairs include:

- front-matter table layout fixes for the claim ledger and dictionary;
- body overclaim hardening around twisted-M motivation, Darboux/scalar/Weyl
  normalizations, residue pairing, reduced principal-part targets, and quantum
  candidate maps;
- theorem-lane and appendix hardening for the interval source
  \(u_{a(t)dt\otimes f}\) and conditional radial-parts input;
- source-convention and convergence-referee ledgers;
- safe notation hygiene: removed the active `\dim` override and fixed
  `\rrp` in `commands.tex`.

Shared-checkout verification after Wave 3:

- `git diff --check` passed.
- No stale TeX hits for `u_{a\otimes f}`, `(a\otimes f)^\vee[-1]`,
  `C^\infty_c(I)`, `different bases`, `Twisted-M-theory universality`, or
  `Universal generality`.
- `python3 scripts/check_one_psi_homology.py` passed.
- `python3 scripts/check_moyal_coefficients.py` passed.
- `make pdf` produced `out/main.pdf`, 137 pages, with no unresolved
  references, citations, multiply-defined labels, fatal errors, rerun
  requests, or overfull boxes.
- TOC scan confirms main sections number `1,2,...` and appendices number
  `A,...`.

The W3 referee verdict was convergence for the stable local core.  Residuals
are outside the theorem-grade core: primary-source equation/page anchoring for
external normalization inputs, visual/page-level QA, and any future attempt to
promote QME, regulator-independence, descendant, Rees/Fourier, Costello
all-order, or global-transfer problems into proved theorem status.

The principal requested continued attack-heal work until no meaningful
rearchitecture residual remains.  Wave 4 was launched under
`/private/tmp/topological-strings-rearch-wave4-20260428-0520` as a release and
anchoring cycle, not a mathematical rescue cycle.

| Worker | Worktree | Branch | Writable surface |
|---|---|---|---|
| W4-H01 | `sources` | `agent/topological-strings-rearch4-sources-20260428` | `reconstitution/source-convention-ledger-2026-04-28.md`, `references/` reports only |
| W4-H02 | `visual` | `agent/topological-strings-rearch4-visual-20260428` | `reconstitution/pdf-visual-qa-2026-04-28.md`, TeX line-wrap fixes only if verified |
| W4-H03 | `macros` | `agent/topological-strings-rearch4-macros-20260428` | `commands.tex`, `mathmacros.tex`, `notation.tex`, `nomenclature.tex`, `preamble.tex`, macro QA report |
| W4-H04 | `ledgers` | `agent/topological-strings-rearch4-ledgers-20260428` | `reconstitution/architecture.md`, `reconstitution/adversarial-attack-ledger-2026-04-28.md`, `reconstitution/attack-heal-swarm-2026-04-28.md` |
| W4-H05 | `crossrepo` | `agent/topological-strings-rearch4-crossrepo-20260428` | `reconstitution/cross-repo-firewall-audit-2026-04-28.md` |
| W4-H06 | `referee` | `agent/topological-strings-rearch4-referee-20260428` | `reconstitution/wave4-referee-report-2026-04-28.md` |

Wave 4 returned and was integrated by the main thread.  All six reports were
read.  Accepted materials include:

- source-bundle anchoring under `references/primary-sources/` and the stronger
  `reconstitution/source-convention-ledger-2026-04-28.md`;
- visual QA report for the rebuilt 137-page PDF;
- macro and notation QA plus the surviving macro cleanup in `commands.tex`,
  `mathmacros.tex`, `notation.tex`, and `nomenclature.tex`;
- cross-repo firewall audit;
- Wave 4 referee report;
- architecture and attack-ledger status preambles recording convergence of the
  stable local core.

The Wave 4 referee did not identify a mathematical reason for a fifth
six-agent attack-heal wave.  Remaining work is explicitly outside the current
theorem-grade core: additional primary-source anchors for residual external
normalizations, the unreduced QME/Costello graph realization, regulator
independence, descendant quantum lift, Rees/Fourier interpolation, and global
transfer theorems.

Dangling-worktree and `/private/tmp` integration was audited in
`reconstitution/dangling-worktree-integration-2026-04-28.md`.  First-wave
staged edits were compared semantically and are present in stronger form in the
shared checkout; Wave 2--4 reports and source bundles are copied into the
shared checkout; stale root release PDF status is closed by regenerating
`main.pdf` from the final `out/main.pdf`.

Final shared-checkout verification after Wave 4:

- `git diff --check` passed.
- No stale TeX hits for `u_{a\otimes f}`, `(a\otimes f)^\vee[-1]`,
  `C^\infty_c(I)`, `different bases`, `Twisted-M-theory universality`, or
  `Universal generality`.
- `python3 scripts/check_one_psi_homology.py` passed.
- `python3 scripts/check_moyal_coefficients.py` passed.
- `make pdf` produced `out/main.pdf`, 137 pages.
- The tracked root `main.pdf` was synchronized from `out/main.pdf`; both PDFs
  report the title `Closed Hamiltonian BF Theory as the Derived Poisson Center
  of a Dirac Brane Probe: A formal local mixed holomorphic-topological model
  on R2 x C2`.
- `out/main.log` contains no unresolved references, unresolved citations,
  multiply-defined labels, fatal errors, rerun requests, or overfull boxes; the
  only `Rerun` match is the package metadata line for `rerunfilecheck`.
- Attribution hygiene scan over local reports/material ledgers found no
  model-attribution strings.
