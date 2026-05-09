# Agent 151 - Finite-Window Larger Package Rows

Status: patched owned surfaces; no commits or pushes.

## Stable Core

The closed family is the order-two BV/convolution bracket rows containing
the universal one-cross scalar-contact component
\(\alpha_{\mathrm{sc}}\) in the full-equivariant
\(\lie{gl}(N|N)\) marked branch.

The decisive input is not merely scalar-gate vanishing.  By
Proposition~\ref{prop:first-finite-window-array-rows},
\[
  K^M_{\alpha_{\mathrm{sc}}}=0
\]
as a finite-window local functional.  Hence bilinearity of the
BV/convolution bracket gives the row formulas
\[
\begin{array}{c|c}
  \text{row} & R^{\mathrm{row}}_{b,M} \\ \hline
  b(\alpha_{\mathrm{sc}},\beta) &
    \frac12\varepsilon_{\alpha_{\mathrm{sc}},\beta}
    \{K^M_{\alpha_{\mathrm{sc}}},K^M_\beta\}_{\hbar,M}=0\\
  b(\beta,\alpha_{\mathrm{sc}}) &
    \frac12\varepsilon_{\beta,\alpha_{\mathrm{sc}}}
    \{K^M_\beta,K^M_{\alpha_{\mathrm{sc}}}\}_{\hbar,M}=0\\
  b(\alpha_{\mathrm{sc}},\alpha_{\mathrm{sc}}) &
    \frac12\varepsilon_{\alpha_{\mathrm{sc}},\alpha_{\mathrm{sc}}}
    \{K^M_{\alpha_{\mathrm{sc}}},
      K^M_{\alpha_{\mathrm{sc}}}\}_{\hbar,M}=0
\end{array}
\]
For every such row,
\[
  S_{b,M}=0,\qquad
  t^{M,N}_{bb'}=0\quad\text{for all lower-window bracket rows }b'.
\]
Thus this family contributes no order-two obstruction and requires no
counterterm.  The remaining order-one bracket rows are exactly those
\(b(\beta_1,\beta_2)\) with
\(\beta_1,\beta_2\neq\alpha_{\mathrm{sc}}\); those are still package data.

## Valid Attacks

```yaml
- id: A1-151-01
  severity: 2
  status: healed
  lens: order-two bracket rows
  target: tate-P1-hadamard-mittag-leffler.tex order-two larger-package residual
  claim: All order-one bracket rows remain missing in a larger package.
  broken_step: Bracket rows containing the universal scalar-contact row are
    decidable because that row is zero as a full-equivariant local functional.
  evidence_type: direct_computation
  evidence_ref: prop:first-finite-window-array-rows; prop:universal-scalar-contact-bracket-rows
  minimal_heal: Inscribe the zero formulas for b(alpha_sc,beta),
    b(beta,alpha_sc), and b(alpha_sc,alpha_sc).
  residual: Bracket rows between two added order-one components remain
    package data.

- id: A1-151-02
  severity: 3
  status: healed
  lens: finite-window truncation
  target: zero bracket rows
  claim: These rows still need unspecified truncation coefficients.
  broken_step: A zero row has a canonical compatible truncation row, namely
    t^{M,N}_{bb'}=0 for every lower-window row.
  evidence_type: direct_computation
  evidence_ref: prop:universal-scalar-contact-bracket-rows
  minimal_heal: Record the zero truncation coefficients in the proposition
    and script payload.
  residual: Nonzero order-two rows still need actual truncation matrices.

- id: A1-151-03
  severity: 2
  status: healed
  lens: non-scalar QME theorem surface
  target: order-two residual row sum
  claim: The universal scalar-contact row may feed a non-scalar bracket
    obstruction at order two.
  broken_step: It cannot, because the local functional value is zero before
    cohomology and before applying the scalar projection.
  evidence_type: proof
  evidence_ref: prop:universal-scalar-contact-bracket-rows
  minimal_heal: Refine the residual list to bracket rows not containing
    alpha_sc.
  residual: Genuine added order-one components can still produce a nonzero
    bracket obstruction.
```

## Repaired Labels

- `prop:universal-scalar-contact-bracket-rows`
- `prop:order-two-finite-window-boundary-rows`

## Script Results

`scripts/finite_window_graph_array.py` now emits
`order_2_universal_scalar_contact_bracket_rows` with three rows:

- `b(alpha_sc,beta)`: row formula
  `1/2*epsilon_{alpha_sc,beta}*{K^M_{alpha_sc},K^M_beta}_{hbar,M}=0`.
- `b(beta,alpha_sc)`: row formula
  `1/2*epsilon_{beta,alpha_sc}*{K^M_beta,K^M_{alpha_sc}}_{hbar,M}=0`.
- `b(alpha_sc,alpha_sc)`: row formula
  `1/2*epsilon_{alpha_sc,alpha_sc}*{K^M_{alpha_sc},K^M_{alpha_sc}}_{hbar,M}=0`.

The payload also refines the larger-package missing list to
BV/convolution bracket rows between order-one components not containing
`alpha_sc`.

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
rg -n -F "universal-scalar-contact-bracket-rows" tate-P1-hadamard-mittag-leffler.tex
rg -n -F "order_2_universal_scalar_contact_bracket_rows" scripts/finite_window_graph_array.py
git diff --check -- tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py reconstitution/swarm-2026-04-30-agent-151-finite-window-larger-package-rows.md
grep -n '[[:blank:]]$' tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py reconstitution/swarm-2026-04-30-agent-151-finite-window-larger-package-rows.md
lacheck tate-P1-hadamard-mittag-leffler.tex
chktex -q tate-P1-hadamard-mittag-leffler.tex
git diff --cached --check -- tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py reconstitution/swarm-2026-04-30-agent-151-finite-window-larger-package-rows.md
git diff --cached --name-only -- tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py reconstitution/swarm-2026-04-30-agent-151-finite-window-larger-package-rows.md
```

Results:

- `py_compile` passed.
- The script printed the order-zero, order-one, order-two boundary, and
  universal scalar-contact bracket-row JSON payloads.
- Label/key scans found the new proposition and script payload key.
- `git diff --check` passed.
- Trailing-whitespace grep returned no hits.
- `lacheck` reports only the pre-existing `~` suggestions at lines 39,
  218, and 221.
- `chktex` reports nonfatal style warnings in this manuscript fragment,
  including pre-existing table-style warnings and the new local table
  warning; no fatal TeX syntax error was detected by the scoped check.
- `git diff --cached --check` passed after staging.
- `git diff --cached --name-only` listed exactly the three owned paths.
- `make pdf` was not run because the shared checkout has concurrent staged
  manuscript edits and the build writes tracked output outside this
  agent's owned paths.

## Files Changed/Staged

Changed:

- `tate-P1-hadamard-mittag-leffler.tex`
- `scripts/finite_window_graph_array.py`
- `reconstitution/swarm-2026-04-30-agent-151-finite-window-larger-package-rows.md`

Staged after scoped verification:

- `tate-P1-hadamard-mittag-leffler.tex`
- `scripts/finite_window_graph_array.py`
- `reconstitution/swarm-2026-04-30-agent-151-finite-window-larger-package-rows.md`

## Remaining Theorem Obligations

1. Supply genuine \(|\Gamma|_\hbar=2\) graph weights
   \(K^M_\Gamma\) and \(d_MK^M_\Gamma\).
2. Supply order-two CE-source faces with orientation signs.
3. Supply bracket rows \(b(\beta_1,\beta_2)\) for added order-one
   components \(\beta_1,\beta_2\neq\alpha_{\mathrm{sc}}\).
4. If a nonminimal \(C_{1,M}\) is chosen, supply
   \([\hbar^2]d_MC_{<2,M}\) and
   \(\frac12[\hbar^2]\{C_{<2,M},C_{<2,M}\}_{\hbar,M}\).
5. Define the scalar projection for non-full-equivariant two-contact
   symbols.
6. Fill truncation coefficients for every nonzero order-two row.
