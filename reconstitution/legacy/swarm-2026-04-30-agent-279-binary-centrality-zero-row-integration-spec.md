# Agent 279 - Binary Centrality Zero-Row Integration Spec

Status: report-only.  No manuscript TeX, script, source fixture, figure,
bibliography, or build artifact was edited.  No PDF build was run.

Owned files:

- `reconstitution/swarm-2026-04-30-agent-279-binary-centrality-zero-row-integration-spec.md`
- `reconstitution/binary-centrality-zero-row-integration-spec-2026-04-30.md`

The canonical integration spec is
`reconstitution/binary-centrality-zero-row-integration-spec-2026-04-30.md`.

## Decision

Agent 275's binary centrality attack/heal report should be integrated as a
zero-row theorem plus an enlarged-row matrix obstruction.

The theorem-grade positive statement is:
\[
  R^{\mathrm{cent},\mathrm{coef}}_{x,y,M}=0,\qquad
  S^{\mathrm{cent},\mathrm{coef}}_{x,y,M}=0,\qquad
  H^{\mathrm{coef},M}_{x,y}=0
\]
for
\[
  x,y\in\{u_{a(t)dt\otimes f},c_{B,\rho}\}
\]
in the reduced coefficient-current/minimal full-equivariant zero-row
habitat.  In finite-row coordinates this is
\[
  A^M_{\min}:0\to0,\qquad r^M_{\min}=0,\qquad h^M_{\min}=0,
\]
with zero primitive Roos class.

The larger Costello row is not constructed by that theorem.  Once an
enlarged finite package supplies row bases, scalar-zero gate, candidate
homotopy rows, and transition matrices, it must be stated as
\[
  A^Mh^M=-r^M,
\]
where \(r^M\) is the coordinate vector of
\[
\begin{aligned}
  R^{\mathrm{cent}}_{x,y,M}
    ={}&
    \sum_{\Gamma\in\mathsf A^d_{x,y,M}}
      \varepsilon_\Gamma d_MK^M_\Gamma
    -\sum_{\Gamma\in\mathsf A^{\mathrm{CE}}_{x,y,M}}
      \varepsilon^{\mathrm{CE}}_\Gamma
      K^M_\Gamma(\zeta_{\Gamma,x,y}) \\
    &+\frac12
      \sum_{(\Gamma_1,\Gamma_2)\in\mathsf A^{\mathrm{br}}_{x,y,M}}
      \varepsilon_{\Gamma_1,\Gamma_2}
      \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar,M}
    +R^{\mathrm{ct}}_{x,y,M}.
\end{aligned}
\]
The unknown \(h^M\) is the coordinate vector of the binary homotopy row
\(H^M_{x,y}\), not evidence that such a row already exists.  The tower also
requires the Roos class
\[
  [P^{M,N}h^M-h^N_{\pi x,\pi y}]
\]
to vanish in degree \(|x|+|y|-1\).

## Manuscript integration

The companion spec gives exact insertion text and current line anchors.  The
minimal targets are:

- `main.tex:2091-2102`: add the front-facing zero-row/matrix-obstruction
  distinction.
- `main.tex:8121-8330`: add the binary centrality matrix form
  \(A^Mh^M=-r^M\) inside the non-scalar quantum \(P_0\)-operation obstruction
  complex.
- `appendix-factorization-current-conventions.tex:2022-2035`: optionally add
  the empty solved system for the coefficient-current kernel.
- `appendix-unreduced-bv-qme.tex:3369-3395`: add the empty solved matrix in
  the minimal full-equivariant branch and, if desired, the enlarged-row
  \(A^Mh^M=-r^M\) criterion.
- `theorem-lanes.tex:3279-3298`: add the binary centrality specialization of
  the minimal full-equivariant zero branch.
- `claim-strength-ledger.tex:449-457`: optionally record that binary
  centrality follows the same zero-row versus matrix-obstruction split.

## Verification

Read and checked:

- repo instructions: `CLAUDE.md`, `AGENTS.md`, the required ecosystem voice
  and self-reflection sections, and the local plus Vol II
  `chriss-ginzburg-rectify` standards;
- Agent 275's report;
- current anchors in `main.tex`, `theorem-lanes.tex`,
  `appendix-factorization-current-conventions.tex`,
  `appendix-unreduced-bv-qme.tex`, `claim-strength-ledger.tex`, and
  `open-obligations.tex`;
- `scripts/finite_window_graph_array.py`.

Direct verification command:

```text
python3 scripts/finite_window_graph_array.py
```

Relevant output confirmed:

- `minimal_full_equivariant_order_2_zero`: `primitive_exists=True`, empty
  residual vector, zero primitive, zero Roos class.
- `theta_3_current_finite_row_subcomplex`: `primitive_exists=False`, residual
  vector \(E_{\theta_3}\), left-cokernel certificate
  \(\ell_{\theta_3}(E_{\theta_3})=1\).

Current checkout note: many pre-existing staged and modified files are
present.  This agent owns only the two files listed above and stages only
those paths.
