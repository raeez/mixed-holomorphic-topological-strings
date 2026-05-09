# Agent 134 - Costello Finite-Window Graph List

Status: patched owned appendix surface; no commits or pushes.

## Stable Core

The marked Costello differential is theorem-grade only after a finite
window supplies an actual boundary table.  The repaired appendix now
contains that table in
`def:app-finite-window-marked-costello-list`.

For a finite-window graph/QME package
\((I,w,M,\mathcal G_M)\), the marked graph list is a finite set
\(\mathcal G^{\mathrm{mk}}_M\) of package graphs and counterterm graphs
with admissible vertex labels, edge labels, incidence coefficients, marker
transport maps, and codimension-one boundary operations.  From a finite
seed set \(\mathcal S_M\),
\[
  \mathcal G^{\mathrm{mk}}_M
    =
  \{\partial_J\Gamma\mid
    \Gamma\in\mathcal S_M,\ J\subset\mathsf B_M(\Gamma)\}.
\]
Codimension-two closure makes \(\partial_J\) independent of the chosen
order of \(J\).  If this finite equality fails, the missing datum is the
omitted graph, coefficient, marker transport, or counterterm face.

The marked differential is now coefficient-bearing:
\[
  d_{\mathrm{mk}}X_{\Gamma,o,\mathfrak m,M}
    =
  \sum_i(-1)^{i-1}\varepsilon_{\beta_i}
  X_{\partial_{\beta_i}\Gamma,\;o/\beta_i,\;
    \mu_{\beta_i}(\mathfrak m),\;M}.
\]
The codimension-two closure condition is
\[
  \partial_{\beta_j|\beta_i}\partial_{\beta_i}\Gamma
    =
  \partial_{\beta_i|\beta_j}\partial_{\beta_j}\Gamma,
\]
\[
  \varepsilon_{\beta_i}\varepsilon_{\beta_j|\beta_i}
    =
  \varepsilon_{\beta_j}\varepsilon_{\beta_i|\beta_j},
  \qquad
  \mu_{\beta_j|\beta_i}\mu_{\beta_i}
    =
  \mu_{\beta_i|\beta_j}\mu_{\beta_j}.
\]
With the incidence signs \((-1)^{i-1}\), every codimension-two face
appears twice with opposite sign, so \(d_{\mathrm{mk}}^2=0\).

The full-equivariant scalar-shadow theorem is now explicitly finite-list:
it assumes codimension-two closed lists in each finite window and the
truncation/weight compatibility of the finite-window graph/QME package.
It does not assert all-graph summability.

## Valid Attacks

```yaml
- id: A1-134-01
  severity: 1
  status: healed
  lens: finite-window graph list
  target: appendix-unreduced-bv-qme.tex, marked boundary complex
  claim: Agent 129's oriented marked differential supplies the Costello graph list.
  broken_step: The previous text named elementary operations but did not specify a finite set of graphs, admissible labels, edge labels, contractions, collision faces, or counterterm faces.
  evidence_type: proof_gap
  evidence_ref: def:app-finite-window-marked-costello-list
  minimal_heal: Add the finite seed/list formula, admissible labels, and boundary operation table.
  residual: A concrete specialization must still fill the table with its actual graph entries.

- id: A1-134-02
  severity: 1
  status: healed
  lens: incidence coefficients
  target: eq:app-oriented-marked-differential
  claim: The marked differential can omit graph/BV/counterterm coefficients.
  broken_step: Field differentials, BV contractions, collision expansions, counterterm faces, and CE source faces carry coefficients and Koszul signs.
  evidence_type: proof_gap
  evidence_ref: eq:app-oriented-marked-differential
  minimal_heal: Insert \(\varepsilon_{\beta_i}\) in \(d_{\mathrm{mk}}\), in the first filtration-lowering boundary, and in the scalar-shadow formula.
  residual: Numerical values of \(\varepsilon_{\beta_i}\) are supplied by the chosen finite-window package.

- id: A1-134-03
  severity: 1
  status: healed
  lens: d_mk squared
  target: lem:app-oriented-marked-incidence-signs
  claim: Cellular signs alone prove \(d_{\mathrm{mk}}^2=0\).
  broken_step: Signs cancel only after the two codimension-two composites have the same output graph, same coefficient, and same marker transport.
  evidence_type: proof_gap
  evidence_ref: eq:app-codim-two-marked-closure
  minimal_heal: Add the coefficient/marker codimension-two closure equations and prove cancellation pairwise.
  residual: If a Costello specialization has an anomalous codimension-two face, that face is the exact missing graph/counterterm datum.

- id: A1-134-04
  severity: 2
  status: healed
  lens: kernel/counterterm habitat
  target: prop:app-finite-window-marked-habitat-compatibility
  claim: The marked graph list is automatically compatible with the constructed kernel and counterterms.
  broken_step: Compatibility requires the finite-window graph/QME package labels, counterterm faces, \(d_M\)-boundaries, \(\pi_{M,N}\), and \(R^M_{w,w'}\) to preserve the same finite boundary table.
  evidence_type: proof_gap
  evidence_ref: prop:app-finite-window-marked-habitat-compatibility
  minimal_heal: Add a proposition tying \(d_{\mathrm{mk}}\) to \(d_M\), and the Hom-valued table to \(d_{\mathbf K}=d_M-(-1)^{|\cdot|}(\cdot)d_{\mathrm{CE}}\).
  residual: A package that omits a graph component or counterterm face does not satisfy the theorem.

- id: A1-134-05
  severity: 2
  status: healed
  lens: all-graph overreach
  target: thm:app-full-equivariant-marked-shadow-vanishing
  claim: Full-equivariant scalar-shadow vanishing implies all-graph Costello summability.
  broken_step: The proof only uses finite lists in finite windows; no topology or Cauchy estimate for an infinite graph sum is supplied.
  evidence_type: unsupported
  evidence_ref: thm:app-full-equivariant-marked-shadow-vanishing
  minimal_heal: State inside the theorem that no summation over all graph topologies is part of the hypothesis.
  residual: All-graph summability remains the separate datum of the finite-window-to-limit criterion.
```

## Repaired Labels

- `def:app-finite-window-marked-costello-list`
- `eq:app-codim-two-marked-closure`
- `def:app-oriented-full-equivariant-marked-boundary-complex`
- `eq:app-oriented-marked-differential`
- `eq:app-oriented-marked-first-lowering`
- `lem:app-oriented-marked-incidence-signs`
- `prop:app-finite-window-marked-habitat-compatibility`
- `thm:app-full-equivariant-marked-shadow-vanishing`

## Verification

Commands run:

```bash
git diff --check -- appendix-unreduced-bv-qme.tex
grep -n '[[:blank:]]$' appendix-unreduced-bv-qme.tex
rg -n "Agent|swarm|phase|draft|prior draft" appendix-unreduced-bv-qme.tex
chktex -q appendix-unreduced-bv-qme.tex
git diff --cached --check -- appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-134-costello-finite-window-graph-list.md
git diff -- appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-134-costello-finite-window-graph-list.md
git diff --cached --name-only -- appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-134-costello-finite-window-graph-list.md
git status --short -- appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-134-costello-finite-window-graph-list.md
```

Results:

- `git diff --check` passed after removing one trailing space.
- trailing-whitespace grep returned no hits after the repair.
- the process-language scan returned no manuscript hits.
- `chktex` returned the existing appendix style-warning class and warnings
  on the new displayed formulas; no fatal TeX error was reported.
- `git diff --cached --check` passed after staging.
- the unstaged diff for the two owned paths was empty after staging.
- `git diff --cached --name-only` listed exactly the two owned paths.
- scoped `git status --short` showed `M` for the appendix and `A` for
  this report.
- No full `make pdf` was run because the checkout has concurrent staged
  manuscript edits and the build writes tracked output outside this
  agent's owned paths.

## Files Changed/Staged

Changed:

- `appendix-unreduced-bv-qme.tex`
- `reconstitution/swarm-2026-04-30-agent-134-costello-finite-window-graph-list.md`

Staged after scoped verification:

- `appendix-unreduced-bv-qme.tex`
- `reconstitution/swarm-2026-04-30-agent-134-costello-finite-window-graph-list.md`

## Remaining Obligations

1. Fill the finite table for any concrete Hamiltonian Costello
   specialization: seed graphs, boundary operations, coefficients
   \(\varepsilon_{\beta}\), marker transports, and counterterm faces.
2. Verify codimension-two closure for that concrete table.  Failure names
   the exact missing graph, coefficient, marker map, or counterterm.
3. Preserve the table under \(\pi_{M,N}\) and \(R^M_{w,w'}\) before taking
   a finite-window inverse limit.
4. Supply a separate graph-summability datum before making any all-graph
   or all-topology Costello QME statement.
5. The full-equivariant scalar shadow is zero on this habitat; non-scalar
   \(H^1\) obstructions in the kernel of the zero scalar projection remain
   governed by the finite-window counterterm criteria.
