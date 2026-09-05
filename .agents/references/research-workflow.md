# Research workflow

Paths refer to the assigned repository worktree unless marked otherwise.

## Proof work

Read the affected definitions, sign conventions, macros, theorem dependencies, and cited primary sources before editing.
Track BV degree, ghost number, form degree, topology, completion, filtration, and claim status explicitly.
Verify formulas through derivation, primary literature, or reproducible computations.
Use independent derivations for load-bearing signs, measures, propagators, anomalies, and large-N limits when useful.
Examples should explain the general structure. Preserve every load-bearing expansion and hypothesis.

For each changed theorem, check mathematical truth, definitions before use, prose, motivation, and section structure.
Apply the seventeen-site catalogue and terminology test to relevant claims.
Consult sister antipattern catalogues when the work crosses their constructions.
Choose review depth from the theorem's risk. Repeat review when new evidence or a substantive repair warrants it.
Do not require fixed chunk sizes, pass counts, elapsed times, or reviewer counts.

For unresolved research, record the exact missing construction, tested routes, partial conclusions, and next discriminating step.
Continue independent authorized work. Do not invent a proof or repeat an unchanged failed route merely to keep working.
Keep these investigation records outside manuscript prose. The manuscript states the mathematical open problem directly.

## Figures and comparisons

When a figure disagrees with prose, inspect its source, generating computation, inputs, and conventions.
Neither surface has automatic priority. Repair the supported error within the authorized scope.
If evidence cannot decide, name the uncertainty and continue unaffected work.

Read comparison repositories only for assigned cross-volume claims.
Vol I governs shared chiral Koszul conventions. Vol II supplies controlled curve-chiral comparisons.
Vol III and Igusa supply compact-target comparisons only with explicit matched conventions.
Do not silently reconcile convention drift or import compact-target claims into the local theorem.
Read relevant `notes/antipatterns_catalogue.md` in sister repositories when comparing those constructions.
Record a recurring local confusion in `notes/first_principles_cache.md` when it adds a reusable mathematical check.
Use repository paths and current source labels. Historical memory directory names do not determine project identity.

## Builds and computations

Necessary local verification is authorized by the editing task. Run it when it can resolve an uncertainty or verify the final change.
Build in the assigned isolated worktree. Its local output directories isolate concurrent runs.
Inspect `Makefile` before choosing a target:

- `make pdf` builds the local paper into `out/main.pdf`.
- `make fast` runs a quick paper build and attempts to open a viewer.
- `make platonic` builds the integrated monograph into `out/platonic.pdf`. It is the default target.
- `make standalone` builds standalone papers into `out/`.

`make release` copies into iCloud and `~/mathematics`, and runs cross-volume architecture aggregation.
`icloud`, `mathematics-publish`, `architecture`, `unified-architecture`, `install`, and `all` also have external or broad effects.
Use these targets only within the session's explicit authorization for those destinations.
Do not substitute publication for local verification.

Inspect exit status, logs, output freshness, references, and citations. A pre-existing PDF does not prove a successful build.
Inspect affected rendered pages when layout changed. A clean build does not certify mathematics.
Use `scripts/check_moyal_coefficients.py` and `scripts/check_one_psi_homology.py` for their respective claims.
Read their assumptions before treating output as evidence. Use other relevant sign and homology checks when needed.

Stop only a process launched by this task whose PID or job handle and working directory are verified.
Request graceful termination first, then confirm its state. Forced termination requires verified task ownership and failed graceful termination.
Do not signal processes by a broad executable-name pattern. Preserve other sessions' builds.

## Parallel research

Use authorized parallel agents for independent proof obligations, computations, or review scopes.
Assign files, mathematical questions, and one integration owner. Do not duplicate active work.
Require each agent to return claims, proof or failure evidence, source anchors, computations, changed files, and unresolved questions.
The owner compares the mathematics and integrates the results. Agreement among agents is evidence, not proof.
Use available read and search tools. Tool names and model capabilities depend on the active runtime.
Report concise progress during long work and a checked proof trace at delivery. Keep private scratch reasoning private.
