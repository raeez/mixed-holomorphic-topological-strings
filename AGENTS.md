# Mixed holomorphic-topological strings: agent instructions

AGENTS.md and CLAUDE.md are identical entrypoints to maintained references.
Inherit `~/ecosystem/INVARIANTS.md` when available and use the applicable host adapter below.
Use the strongest available research model and highest supported effort for nontrivial mathematics.
Do not claim control of host settings that the runtime does not expose.

For Claude model controls and instruction loading, use `~/ecosystem/CLAUDE-HARNESS.md` when available.
For Codex, use the inherited `~/ecosystem/AGENTS-HARNESS.md` adapter. Read only the adapter relevant to the active host.

## Safety and ownership

Work in the assigned isolated worktree. Preserve concurrent work and the principal checkout's HEAD.
Do not use destructive Git operations, global process kills, or LLM commit attribution.
Only the main thread commits or publishes. Session authorization determines the permitted scope.
Read other repositories for comparison. Write there only under an explicit assignment.
Keep manuscripts free of agent instructions, task history, review status, TODO queues, and process metadata.
This applies to captions, tables, front matter, bibliography annotations, and PDF metadata.
State theorem, conditional consequence, conjecture, heuristic, and open-problem status accurately.
Pass these constraints to agents that write. Use literal prose without mannered language.

## Read for the task

- Mathematical edits: read the affected source and dependencies, then the relevant sections of
  [.agents/references/mathematical-contract.md](.agents/references/mathematical-contract.md).
  It retains the theorem scope, seventeen-site catalogue, conventions, comparison targets, and chapter sequence.
- Mathematical prose: read
  [the writing standards](MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md)
  and [.agents/references/terminology.md](.agents/references/terminology.md) as applicable.
- Structural rewrites and theorem-region reconstitution: use
  [.agents/skills/chriss-ginzburg-rectify/SKILL.md](.agents/skills/chriss-ginzburg-rectify/SKILL.md).
  A local correction does not require a global restructuring workflow.
- Builds, proof verification, or cross-volume work: read
  [.agents/references/research-workflow.md](.agents/references/research-workflow.md).

`main.tex` is the local paper root. `platonic/main.tex` is the integrated monograph root.
Read their actual include trees for the target artifact. Macros and conventions live in the root TeX files.
Do not load every source, skill, comparison repository, or memory file for every task.

## Mathematical scope and completion

The local result concerns the scalar-reduced stable trace-sector formal-Darboux stalk.
Ordinary E1/HKR comparison applies on the zero-Poisson special fibre with a compatible exact Roos system.
Nonzero linear-Poisson comparison requires supplied twisted formality and PBW data, as specified in the mathematical contract.
Native geometry is mixed holomorphic-topological theory on the topological plane times the holomorphic complex two-plane.
Curve-chiral reduction requires explicit mode data, brackets, BV pairing, brane image, and anomaly matching.
Compact Calabi–Yau, BCOV, Hall, Igusa, and BKM comparisons require separately assigned and justified comparison data.
Never infer an operator algebra from its scalar invariant or identify distinct E2 structures without comparison data.

Seek the strongest true result. Supply missing constructions before changing a theorem's target.
Claim strength always follows proof strength. A build, numerical check, or review consensus does not prove a theorem.
A bounded investigation may finish with a precise unresolved obligation, verified partial results, failed routes, and next discriminating step.
Keep the original theorem target explicit. Do not present an unresolved obstruction as a proved obstruction theorem.
For an active persistent goal, follow its completion and blocking rules.
