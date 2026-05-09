# Agent 156 - Genuine Hbar-Two Graph Weights

Status: patched owned surfaces; no commits or pushes.

## Stable Core

The genuine \(|\Gamma|_\hbar=2\) seed-weight family is now separated from
the scalar-contact bracket family closed by Agent 151 and from the
codimension-two scalar boundary-composition rows closed by Agent 145.

For a genuine order-two seed graph
\(\Gamma\in\mathcal G^{\mathrm{gen}}_{2,M}\), with normalized
renormalized weight
\[
  K^M_\Gamma=W^{R,M}_{\Gamma,L,w}(B^\Gamma_\bullet),
\]
the graph-differential row is
\[
  R^{\mathrm{row}}_{d\Gamma,M}
    =
  \varepsilon_\Gamma\,d_MK^M_\Gamma,
  \qquad
  S_{d\Gamma,M}
    =
  \varepsilon_\Gamma\widehat\sigma_{\mathrm{sc},M}(d_MK^M_\Gamma).
\]
The CE-source face row, when the Hom-valued table is retained or the input
has not already been evaluated on a strict CE cycle, is
\[
  R^{\mathrm{row}}_{\mathrm{CE}(\Gamma,\nu),M}
    =
  -\varepsilon^{\mathrm{CE}}_{\Gamma,\nu}
  K^M_\Gamma(\zeta_{M,\nu}),
  \qquad
  S_{\mathrm{CE}(\Gamma,\nu),M}
    =
  -\varepsilon^{\mathrm{CE}}_{\Gamma,\nu}
  \widehat\sigma_{\mathrm{sc},M}
  (K^M_\Gamma(\zeta_{M,\nu})).
\]

In the full-equivariant marked habitat, the scalar gate is zero by
Theorem~\ref{thm:app-full-equivariant-marked-shadow-vanishing}.  This kills
only the scalar shadow.  It does not prove \(K^M_\Gamma=0\) or
\(d_MK^M_\Gamma=0\).

After scalar-gate vanishing, the genuine seed contribution is
\[
\begin{aligned}
  R^{\mathrm{ns,gen}}_{2,M}
    &=
    \sum_{\Gamma\in\mathcal G^{\mathrm{gen}}_{2,M}}
      \varepsilon_\Gamma\,d_MK^M_\Gamma\\
    &\quad -
    \sum_{\Gamma,\nu}
      \varepsilon^{\mathrm{CE}}_{\Gamma,\nu}
      K^M_\Gamma(\zeta_{M,\nu}).
\end{aligned}
\]
The second sum is absent after strict CE-cycle evaluation.

The minimal full-equivariant local package has
\(\mathcal G^{\mathrm{gen}}_{2,M}=\emptyset\), hence
\[
  R^{\mathrm{ns,gen}}_{2,M}=0,\qquad C^{\mathrm{gen}}_{2,M}=0.
\]
For a larger package this row family requires a counterterm exactly when
\([R^{\mathrm{ns,gen}}_{2,M}]=0\) in
\(H^1(\mathcal K^\bullet_{\mathrm{ns},M}(I),d_{\mathrm{ns},M})\).  A
nonzero class is the finite-window obstruction.  The present package has
not supplied enough data to decide this class.

## Valid Attacks

```yaml
- id: A1-156-01
  severity: 1
  status: healed
  lens: genuine order-two seed weights
  target: tate-P1-hadamard-mittag-leffler.tex order-two residual
  claim: The next larger order-two row family can be declared zero by the full-equivariant scalar gate.
  broken_step: Full-equivariant scalar shadow vanishing kills only the scalar projection. It does not kill a genuine non-scalar graph weight or its d_M-boundary.
  evidence_type: proof_gap
  evidence_ref: prop:genuine-order-two-graph-weight-rows
  minimal_heal: Define the genuine dK and CE-source rows, state scalar-gate zero only under full-equivariant marked-habitat membership, and leave the non-scalar H^1 class as the decision datum.
  residual: Supply actual K^M_Gamma, d_MK^M_Gamma, source faces, and truncation matrices.

- id: A1-156-02
  severity: 1
  status: healed
  lens: minimal package boundary
  target: minimal full-equivariant order-two conclusion
  claim: Genuine |Gamma|_hbar=2 weights vanish in the minimal package by computation.
  broken_step: The minimal package contains no genuine |Gamma|_hbar=2 seed rows. The contribution is empty, not a computed nonzero weight cancellation.
  evidence_type: line_reference
  evidence_ref: prop:order-two-finite-window-boundary-rows; prop:genuine-order-two-graph-weight-rows
  minimal_heal: State R^{ns,gen}_{2,M}=0 because G^{gen}_{2,M} is empty and C^{gen}_{2,M}=0.
  residual: Any enlargement must list the added seed graphs.

- id: A1-156-03
  severity: 2
  status: healed
  lens: CE source signs
  target: order-two source rows
  claim: The genuine graph-weight row family is just epsilon_Gamma d_M K^M_Gamma.
  broken_step: The Hom-valued convolution differential also contains -kappa(d_CE zeta_M); the source-face signs decide part of the row sum unless evaluation is on a strict CE cycle.
  evidence_type: proof_gap
  evidence_ref: def:app-bulk-defect-convolution-habitat; prop:genuine-order-two-graph-weight-rows
  minimal_heal: Add source rows with formula -epsilon^CE_{Gamma,nu} K^M_Gamma(zeta_{M,nu}) and mark them empty after strict CE-cycle evaluation.
  residual: Supply d_CE zeta_M and epsilon^CE_{Gamma,nu} for non-cycle or Hom-valued computations.

- id: A1-156-04
  severity: 2
  status: healed
  lens: finite-window truncation
  target: t^{M,N}_{alpha alpha'} for genuine rows
  claim: Truncation follows automatically from degree cutoff.
  broken_step: A genuine graph weight can truncate to a linear combination of lower-window normalized rows, and source faces need their own lower-window decomposition.
  evidence_type: proof_gap
  evidence_ref: prop:genuine-order-two-graph-weight-rows
  minimal_heal: Define u^{M,N}_{Gamma Gamma'} and v^{M,N}_{Gamma,nu;Gamma',nu'} as required row data; missing identities are exact missing entries.
  residual: Populate the matrices for every actual seed row.
```

## Repaired Labels

- `prop:genuine-order-two-graph-weight-rows`
- `prop:order-two-finite-window-boundary-rows` remains the minimal-order
  zero theorem; the new proposition explains the excluded genuine seed
  family.

## Script Results

`scripts/finite_window_graph_array.py` now emits
`order_2_genuine_graph_weight_rows` with two formal row classes:

- `dK genuine |Gamma|_hbar=2 seed`:
  `R_{dGamma,M}=epsilon_Gamma*d_M K^M_Gamma`, scalar gate zero only inside
  the full-equivariant marked habitat, truncation by normalized
  coefficients `u^{M,N}_{Gamma,Gamma'}`.
- `CE source face of genuine |Gamma|_hbar=2 seed`:
  `R_{CE(Gamma,nu),M}=-epsilon^CE_{Gamma,nu}*K^M_Gamma(zeta_{M,nu})`,
  empty after strict CE-cycle evaluation, truncation by coefficients
  `v^{M,N}_{Gamma,nu;Gamma',nu'}`.

The payload records
`order_2_genuine_graph_weight_contribution`:

- minimal full-equivariant contribution: `0 because G^{gen}_{2,M}=empty`;
- larger full-equivariant formula:
  `R^{ns,gen}_{2,M}=sum_Gamma epsilon_Gamma*d_M K^M_Gamma -sum_{Gamma,nu} epsilon^CE_{Gamma,nu}*K^M_Gamma(zeta_{M,nu})`;
- counterterm criterion:
  `C^{gen}_{2,M}` exists iff this class vanishes in \(H^1\);
- current status: undecided without the missing weight, locality, and
  truncation data.

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
git diff --check -- tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py
grep -n '[[:blank:]]$' tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py
rg -n -F "genuine-order-two-graph-weight-rows" tate-P1-hadamard-mittag-leffler.tex
rg -n -F "order_2_genuine_graph_weight_rows" scripts/finite_window_graph_array.py
rg -n -F "R^{\\mathrm{ns,gen}}_{2,M}" tate-P1-hadamard-mittag-leffler.tex
lacheck tate-P1-hadamard-mittag-leffler.tex
chktex -q tate-P1-hadamard-mittag-leffler.tex
```

Results:

- `py_compile` passed.
- The script printed the new genuine order-two row schema, the minimal
  full-equivariant zero contribution, and the larger-package undecided
  status.
- `git diff --check` passed.
- Trailing-whitespace grep returned no hits.
- Label/key scans found the new proposition and script payload key.
- `lacheck` reports only the pre-existing nonbreaking-space suggestions at
  lines 39, 218, and 221.
- `chktex` reports nonfatal style warnings, including the new local
  enumerate-label and sign-parenthesis suggestions; no fatal TeX syntax
  error was detected by the scoped check.
- `make pdf` was not run because the shared checkout has concurrent staged
  manuscript edits and the build writes tracked output outside this agent's
  owned paths.

## Files Changed/Staged

Changed:

- `tate-P1-hadamard-mittag-leffler.tex`
- `scripts/finite_window_graph_array.py`
- `reconstitution/swarm-2026-04-30-agent-156-genuine-hbar2-graph-weights.md`

Staged after scoped verification:

- `tate-P1-hadamard-mittag-leffler.tex`
- `scripts/finite_window_graph_array.py`
- `reconstitution/swarm-2026-04-30-agent-156-genuine-hbar2-graph-weights.md`

## Remaining Theorem Obligations

1. Supply the actual finite seed list
   \(\mathcal G^{\mathrm{gen}}_{2,M}\) and its \(\hbar\)-order assignment.
2. Supply renormalized local weights
   \(K^M_\Gamma=W^{R,M}_{\Gamma,L,w}(B^\Gamma_\bullet)\) with
   regular-density or wavefront-admissible current labels.
3. Expand \(d_MK^M_\Gamma\), including \(Q\), \(\{I^w_{0,M},-\}_{\hbar,M}\),
   collision faces, counterterm faces, and orientation/Koszul/symmetry
   coefficients.
4. Supply \(d_{\mathrm{CE}}\zeta_M\) and CE-source signs unless the
   computation is strictly evaluated on CE cycles.
5. Prove full-equivariant marked-habitat membership for every genuine row,
   or provide the scalar projection row by row.
6. Fill the normalized truncation matrices \(u^{M,N}\) and \(v^{M,N}\).
7. Compute the resulting \(H^1\) class and the Roos compatibility class for
   any nonzero windowwise primitive.
