# Dangling Worktree Integration Ledger

Date: 2026-04-28

Scope: audit of side worktrees, dangling branches, staged worker edits,
untracked worker reports, and `/private/tmp` material after the attack-heal
cycles. This ledger records how each external material source was merged into
the shared checkout.

## Registered Worktrees

The registered worktree inventory was checked with `git worktree list
--porcelain`. The active shared checkout is `/Users/raeez/topological-strings`.
Side worktrees found:

- `/private/tmp/topological-strings-attack-20260428/{crossvolume,hygiene,quantum,scalar,tate,trace}`
- `/private/tmp/topological-strings-rearch-wave2-20260428/{appendices,hygiene,main,outlook,theorem-front,weighted}`
- `/private/tmp/topological-strings-rearch-wave3-20260428-0505/{appendix,layout,notation,overclaim,referee,sources}`
- `/private/tmp/topological-strings-rearch-wave4-20260428-0520/{crossrepo,ledgers,macros,referee,sources,visual}`
- `/Users/raeez/topological-strings/.claude/worktrees/ts-b-w2`

The `.claude` worktree had no diff and no untracked files.

## First Attack Worktrees

The first attack wave contained staged TeX/script repairs against the older
pre-rearchitecture manuscript. No standalone reports were present. The current
shared checkout was checked for the mathematical substance of those staged
repairs:

| Worktree | Material found | Shared-checkout disposition |
|---|---|---|
| `crossvolume` | protected-sector demotion, cross-volume firewall, Vol III/Igusa/BKM non-transfer language | Integrated in stronger form in `tate-P3-universality.tex`, `tate-P5-cross-volume.tex`, `claim-strength-ledger.tex`, and `open-obligations.tex`. |
| `hygiene` | bibliography hygiene around a removed Lichnerowicz entry | Superseded by the current bibliography and source-convention ledger. No unique theorem content remained. |
| `quantum` | Moyal graph coefficient correction, degree-zero quantum Hamiltonian comparison, descendant/QME separation | Integrated in stronger form in `main.tex`, `appendix-radial-parts-moyal.tex`, `scripts/check_moyal_coefficients.py`, and `open-obligations.tex`. |
| `scalar` | scalar-axis obstruction, Capelli moment relation, local quantum-status language | Integrated in stronger form in `main.tex`, `appendix-radial-parts-moyal.tex`, and `claim-strength-ledger.tex`. |
| `tate` | Hadamard/Mittag-Leffler demotion from unconditional QME closure to analytic reduction plus obstruction | Integrated in stronger form in `tate-P1-hadamard-mittag-leffler.tex`, `tate-T1-weighted-completion.tex`, and `open-obligations.tex`. |
| `trace` | alternating two-psi source and script basis correction | Integrated in stronger form in `main.tex` and `scripts/check_one_psi_homology.py`. |

No first-wave staged patch was applied mechanically, because the shared
checkout already contains the rearchitected version of its mathematical
content. Applying those older patches would reintroduce pre-split theorem
structure.

## Wave 2 and Wave 3 Worktrees

Wave 2 and Wave 3 produced the core rearchitecture. Their TeX, script, and
report materials are present in the shared checkout:

- front matter, claim ledger, local dictionary, theorem lanes, principles,
  and open obligations;
- protected-sector and cross-volume firewalls;
- weighted Tate/QME split;
- Matlis, factorization-current, and radial-parts appendices;
- source-convention, release-QA, and referee reports;
- macro and notation hygiene that survives the final build.

Their side worktrees still show diffs because they were branched before the
main-thread semantic merge. The accepted content was merged into the shared
checkout, not by branch merge, to avoid overwriting later stronger repairs.

## Wave 4 Worktrees

Wave 4 was a release and anchoring cycle. Integrated materials:

- `sources`: copied the full `references/primary-sources/` bundle and replaced
  `reconstitution/source-convention-ledger-2026-04-28.md` with the stronger
  source-anchored version.
- `visual`: copied `reconstitution/pdf-visual-qa-2026-04-28.md`; attribution
  phrasing was normalized to manual image inspection.
- `macros`: integrated surviving macro/notation repairs into `commands.tex`,
  `mathmacros.tex`, `notation.tex`, and `nomenclature.tex`; copied
  `reconstitution/macro-notation-qa-2026-04-28.md`.
- `ledgers`: integrated the stable-core verdict into
  `reconstitution/architecture.md` and
  `reconstitution/adversarial-attack-ledger-2026-04-28.md`; this file and the
  swarm log carry the final dangling-worktree audit.
- `crossrepo`: copied
  `reconstitution/cross-repo-firewall-audit-2026-04-28.md`.
- `referee`: copied `reconstitution/wave4-referee-report-2026-04-28.md`.

## Temporary Build Directories

The following `/private/tmp` directories were build or inspection scratch
surfaces, not sources of independent manuscript material:

- `topological-strings-appendix-build`
- `topological-strings-layout-heal`
- `topological-strings-macro-compile-*`
- `topological-strings-macro-smoke-*`
- `topological-strings-notation-compile`
- `topological-strings-overclaim-build`
- `topological-strings-referee-*`
- `topological-strings-visual-pages`
- `topological-strings-wave4-referee-build-*`
- `topological-strings-weighted-build`
- `topological-strings-worker3-tex`
- `topological-strings-worker4-build`
- `topological-strings-worker5-tex`

They were not deleted. Their substantive outputs are represented by the
integrated TeX changes, QA ledgers, source bundle, and final PDFs in the shared
checkout. Logs and selected build artifacts from the current worker
directories are preserved under
`reconstitution/private-tmp-artifacts-2026-04-28/current-worker-builds/`.

## Loose `/private/tmp` Artifacts

Loose patch, visual-QA, and cross-repo proposal artifacts were preserved under
`reconstitution/private-tmp-artifacts-2026-04-28/`.

| Artifact family | Repository copy | Disposition |
|---|---|---|
| First attack patch files: `topological-strings-crossvolume.patch`, `topological-strings-hygiene-main.patch`, `topological-strings-quantum.patch`, `topological-strings-scalar*.patch`, `topological-strings-tate.patch` | `reconstitution/private-tmp-artifacts-2026-04-28/patches/` | Preserved as historical patch artifacts. Their mathematical content is already integrated in stronger form in the shared checkout; the patches were not mechanically applied because they target the older pre-rearchitecture manuscript. |
| Visual QA scratch: rendered pages, contact-sheet images/PDF, layout text, `pdfjam` log | `reconstitution/private-tmp-artifacts-2026-04-28/visual/` | Preserved as QA evidence. The authoritative written QA conclusion is `reconstitution/pdf-visual-qa-2026-04-28.md`. |
| Igusa cross-repo proposal | `reconstitution/private-tmp-artifacts-2026-04-28/igusa-crossrepo/topological-strings-patches.md` | Preserved as proposal-only. It was not applied: the proposed target docs are not part of the present local theorem, and the current paper deliberately firewalls BKM/Igusa consequences. |
| Registered worktree diffs | `reconstitution/private-tmp-artifacts-2026-04-28/worktree-diffs/` | Preserves each registered side worktree's path, status, staged diff, unstaged diff, untracked list, and unique-vs-root list. This keeps obsolete but substantive side-worktree material reconstructible without mechanically applying patches over the stronger semantic merge. |
| Current worker build scratch | `reconstitution/private-tmp-artifacts-2026-04-28/current-worker-builds/` | Preserves selected logs, aux/toc files, and the worker-4 draft PDF from the current six-agent pass. |

The old `/private/tmp/claude-501/.../tasks/*.output` files were inspected but
not copied into the repository because they are raw execution transcripts,
not manuscript material. Their substantive mathematical content is represented
by the integrated cross-repo firewall reports and the proposal artifact above.

## Branch Ancestry

All local branches were checked against `master`. No side branch was ahead of
`master`; `ts-b-w2` and the first attack branches are behind the current
shared checkout, while Wave 2--4 branches point at the shared base commit and
carry their material only as worktree diffs/untracked files already audited
above.

## Release Artifact

The tracked root `main.pdf` was identified as stale relative to `out/main.pdf`
after Wave 4. The release copy was regenerated from `out/main.pdf` during final
verification. Both tracked PDFs now carry the reconstituted title and 137-page
build.
