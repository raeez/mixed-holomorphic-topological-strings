# Agent 233 Report -- Strict Endpoint / Casimir Kernel Construction Target

Date: 2026-04-30.

Writable scope obeyed:

- `reconstitution/strict-endpoint-casimir-kernel-construction-target-2026-04-30.md`.
- `reconstitution/swarm-2026-04-30-agent-233-strict-endpoint-casimir-kernel-construction-target.md`.

No manuscript or script files were edited.

## Inputs Loaded

- `CLAUDE.md`.
- `AGENTS.md`.
- `/Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md`.
- `/Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md`.
- `/Users/raeez/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- `~/ecosystem/INVARIANTS.md`.
- `~/ecosystem/AGENTS-HARNESS.md`.
- `main.tex`, `commands.tex`, `mathmacros.tex`, `notation.tex`,
  `preamble.tex`.
- `theorem-lanes.tex`, `open-obligations.tex`,
  `claim-strength-ledger.tex`, `local-dictionary.tex`.
- `tate-T1-weighted-completion.tex`, `tate-T2-nilpotent-truncation.tex`,
  `tate-T3-quillen-equivalence.tex`,
  `tate-P1-hadamard-mittag-leffler.tex`.
- Relevant reconstitution reports: Agent 095, Agent 219, Agent 222,
  Agent 227, and the wave6 strict unweighted Tate endpoint report.

## Claim Attacked

Surface FTS-003:

> Strict product/direct-sum endpoints and Casimir kernels.

The vulnerable claim is that the finite-window cotangent CE/PV identities,
weighted regulator data, or \(q\to1^+\) finite-window stabilization supply a
strict global endpoint on
\[
  \mathfrak h_\Pi=\prod_{d\geq1}H_d,\qquad
  D_\oplus=\bigoplus_{d\geq1}H_d^\vee .
\]

They do not. The strict endpoint lacks the diagonal coefficient
coevaluation.

## Stable Core

The coordinate CE/PV theorem is proved as a completed coordinate dg-algebra
identity. \(P_0\), kernel, propagator, and bar-cobar conclusions require
additional admissibility data.

The positive kernel theorem target is the weighted or strict
Mittag-Leffler admissible coefficient habitat:

\[
  \mathfrak h_w=\varprojlim_M\prod_{d\le M}w(d)H_d,\qquad
  D_w=\varprojlim_M\prod_{d\le M}w(d)^{-1}H_d^\vee .
\]

In that habitat the Casimir
\[
  C_{\mathfrak h,w}
  =
  \sum_{d\geq1}\sum_i
  (w(d)e_{d,i})\otimes(w(d)^{-1}e^i_d)
\]
converges, the finite-scale propagator is
\[
  P_{\epsilon,L}^{w}
  =
  P_{\epsilon,L}^{\mathrm{base}}\widehat\otimes C_{\mathfrak h,w},
\]
and the bar-cobar comparison is allowed only in the admissible envelope with
the lower-central/conilpotence/exactness hypotheses.

## Valid Attacks

1. Finite-window Casimirs are compatible, but compatibility is not global
   strict tensor representability.
2. The abstract BV pairing is an evaluation map. Costello's propagator needs
   the inverse pairing as a coefficient kernel.
3. The ambient coordinate product does not carry the global contraction
   bracket; the diagonal contraction diverges outside bracket-admissible
   \(B\)'s.
4. The operator-level heat homotopy is not a BV propagator without a
   coefficient coevaluation tensor.
5. Bar-cobar duality needs an admissible envelope, lower-central
   Tate-pronilpotence, local conilpotence, exact continuous duality, and zero
   Milnor/cone defects.
6. Weight independence is finite-window regulator independence. It is not an
   ordinary quasi-isomorphism \(D_\oplus\simeq D_{\Pi,w}\).

## Healed Construction

Wrote
`reconstitution/strict-endpoint-casimir-kernel-construction-target-2026-04-30.md`.

The report defines a Casimir-admissible endpoint habitat
\[
  \mathcal H_\ast
  =
  (\mathfrak h_\ast,D_\ast,
   \{(\mathfrak h_{\ast,\le M},D_{\ast,\le M})\}_M,
   C_\ast,\Phi_\ast,B_\ast,\mathcal K_\ast,R_\ast)
\]
with:

- strict Mittag-Leffler finite windows;
- a coefficient coevaluation \(C_\ast\) projecting to all finite Casimirs;
- continuous bracket, coadjoint action, CE/PV differential, multiplication,
  and Schouten contraction on a bracket-admissible \(B_\ast\);
- a kernel-admissible convolution dg Lie algebra \(\mathcal K_\ast\);
- endpoint propagator
  \(P_{\epsilon,L}^{\ast}
  =P_{\epsilon,L}^{\mathrm{base}}\widehat\otimes C_\ast\);
- bar-cobar compatibility in the admissible envelope;
- a separate RG/QME acceptance gate.

## Exact Obstruction

The strict endpoint obstruction is the cokernel class
\[
  o_{\mathrm{Cas}}
  =
  [(C_{\le M})_{M\ge1}]
  \in
  Q_{\mathrm{Cas}}
  =
  \frac{\varprojlim_M(H_{\le M}\otimes H_{\le M}^\vee)}
       {\operatorname{im}(\mathfrak h_\Pi\widehat\otimes D_\oplus)} .
\]

It is nonzero. Every tensor with a \(D_\oplus\)-factor has finite support in
the dual degree direction; the finite Casimir family has a nonzero identity
component in every degree. The same obstruction holds with tensor factors
reversed.

Thus the raw strict product/direct-sum endpoint fails the coefficient kernel
condition before bracket, bar-cobar, or QME obstructions are evaluated.

## Recommendation

The manuscript target should state the supremum theorem as a dichotomy:

- positive branch: construct a weighted/ML Casimir-admissible habitat and
  prove the bracket, coevaluation, propagator, and bar-cobar clauses there;
- obstruction branch: for the raw strict pair, prove
  \(o_{\mathrm{Cas}}\neq0\), hence no strict endpoint coefficient kernel.

Do not identify weighted finite-window stabilization with ordinary
convergence in the strict product/direct-sum topology.

## Verification

Commands run:

- `rg` and `nl -ba ... | sed -n ...` over the relevant manuscript, Tate,
  obligation, and reconstitution anchors.
- `test -e` on both owned output paths before writing; both were absent.
- `apply_patch` to add only the two owned report files.
- `git diff --check --` on the two owned report files; clean.
- `rg -n -F` for `o_{\mathrm{Cas}}`, `Casimir-admissible`,
  `Strict Endpoint`, `Agent 233`, and the no-manuscript-edit marker.

No TeX build was run. This was a staged report-only task and no manuscript or
script file changed.
