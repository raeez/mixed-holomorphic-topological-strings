# Agent 148 - Non-Scalar Kernel QME Class

Status: patched owned appendix surface; no commits or pushes.

## Stable core

The scalar-shadow computation does not decide the kernel class.  The
appendix now defines the fixed-window non-scalar complex
\[
  \mathcal K^\bullet_{\mathrm{ns},M}(I)
    =
  \ker\bigl(
    \widehat\sigma_{\mathrm{sc},M}\colon
    \mathfrak Q^\bullet_{\mathcal G,M}(I)\to
    C^\bullet_{\mathrm{Lie}}(\bar A;\mathbb C\gamma_{\mathbf 1})[1][[\hbar]]
  \bigr).
\]
In the full-equivariant marked habitat
\(\widehat\sigma_{\mathrm{sc},M}=0\), so the kernel is the whole
full-equivariant marked graph/counterterm habitat.

For a valid finite-window row array,
\[
  R^{\mathrm{ns}}_{n,M}
    =
  \sum_{\alpha\in\mathsf A^{\mathrm{fw}}_{n,M}}
    R^{\mathrm{row}}_{\alpha,M}
  \quad\text{when}\quad
  \sum_{\alpha}S_{\alpha,M}=0,
\]
and the obstruction class is
\[
  \mathfrak o^{\mathrm{ns}}_{n,M}
    =
  [R^{\mathrm{ns}}_{n,M}]
  \in
  H^1(\mathcal K^\bullet_{\mathrm{ns},M}(I),d_{\mathrm{ns},M}).
\]
A counterterm exists exactly when this class is zero.

For the minimal full-equivariant closed array containing only the strict
current-interface rows, the one-cross two-Hamiltonian scalar-contact row,
and the codimension-two closure faces forced by it,
\[
  R^{\mathrm{ns}}_{1,M}=R^{\mathrm{ns}}_{2,M}=0,
  \qquad
  C_{1,M}=C_{2,M}=0.
\]
Thus no genuinely non-scalar class exists in that minimal array through
the first codimension-two closure level.

## Valid attacks

```yaml
- id: A1-148-01
  severity: 1
  status: healed
  lens: scalar-kernel separation
  target: appendix-unreduced-bv-qme.tex, full-equivariant marked branch
  claim: Vanishing of the scalar shadow decides the non-scalar QME class.
  broken_step: The zero scalar projection only places the residual in
    \(\ker\widehat\sigma_{\mathrm{sc},M}\); it does not construct a
    primitive in that kernel.
  minimal_heal: Define \(\mathcal K^\bullet_{\mathrm{ns},M}\) and the
    class \(\mathfrak o^{\mathrm{ns}}_{n,M}\in H^1(\mathcal K_{\mathrm{ns},M})\).

- id: A1-148-02
  severity: 1
  status: healed
  lens: first-row overclaim
  target: minimal full-equivariant array
  claim: The first non-scalar obstruction appears at the computed
    one-cross row after the scalar gate is killed.
  broken_step: In the full-equivariant array that row is zero as a local
    functional, not merely scalar-zero.
  minimal_heal: Prove \(R^{\mathrm{ns}}_{1,M}=0\) and \(C_{1,M}=0\).

- id: A1-148-03
  severity: 2
  status: healed
  lens: codimension-two closure
  target: first order-two boundary rows
  claim: Two scalar-contact faces may produce the first hidden non-scalar row.
  broken_step: In the minimal full-equivariant list the two codimension-two
    composites cancel by incidence signs, and each scalar-loop cyclic
    supertrace is already zero.
  minimal_heal: Prove \(R^{\mathrm{ns}}_{2,M}=0\) and \(C_{2,M}=0\) under
    the minimal-list hypotheses.

- id: A1-148-04
  severity: 1
  status: healed
  lens: missing concrete graph data
  target: larger finite marked Costello packages
  claim: A first non-scalar class can be identified without the remaining
    row array.
  broken_step: The first class is the least scalar-zero row sum whose
    cohomology class is nonzero; absent row values, signs, scalar gates,
    and truncation coefficients, the cochain is not defined.
  minimal_heal: Name the first missing row: an additional order-one
    scalar-zero row outside \(\alpha_{\mathrm{sc}}\), or, if none exists,
    the order-two row sum of genuine graph, CE-source, bracket, and
    lower-counterterm rows.
```

## Repaired labels

- `def:app-nonscalar-kernel-row-complex`
- `thm:app-minimal-full-equivariant-kernel-vanishing`
- `prop:app-first-missing-nonscalar-row`

## Exact obstruction formulas

First possible order-one missing row:
\[
  \alpha\in
  \mathsf A^{\mathrm{fw}}_{1,M}\setminus\{\alpha_{\mathrm{sc}}\},
  \qquad
  S_{\alpha,M}=0,
\]
with row value one of
\[
  \varepsilon_\Gamma d_M K^M_\Gamma,\qquad
  -\varepsilon^{\mathrm{CE}}_{\Gamma'}K^M_{\Gamma'},\qquad
  \frac12\varepsilon_{\Gamma_0,\Gamma_1}
    \{K^M_{\Gamma_0},K^M_{\Gamma_1}\}_{\hbar,M}.
\]

If no order-one scalar-zero row exists, the next missing row sum is
\[
\begin{aligned}
  R^{\mathrm{ns}}_{2,M}
    ={}&
    \sum_{|\Gamma|_\hbar=2}
      \varepsilon_\Gamma\,d_M K^M_\Gamma
    -\sum_{|\Gamma'|_\hbar=2}
      \varepsilon^{\mathrm{CE}}_{\Gamma'}K^M_{\Gamma'}\\
    &\quad
    +\frac12
    \sum_{|\Gamma_1|_\hbar=|\Gamma_2|_\hbar=1}
      \varepsilon_{\Gamma_1,\Gamma_2}
      \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar,M}
    +[\hbar^2]d_M C_{<2,M}\\
    &\quad
    +\frac12[\hbar^2]
      \{C_{<2,M},C_{<2,M}\}_{\hbar,M}.
\end{aligned}
\]

## Files changed

- `appendix-unreduced-bv-qme.tex`
- `reconstitution/swarm-2026-04-30-agent-148-nonscalar-kernel-qme-class.md`

## Verification

Commands run:

```bash
git diff --check -- appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-148-nonscalar-kernel-qme-class.md
grep -n '[[:blank:]]$' appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-148-nonscalar-kernel-qme-class.md
python3 scripts/finite_window_graph_array.py
python3 -m py_compile scripts/finite_window_graph_array.py
chktex -q appendix-unreduced-bv-qme.tex
lacheck appendix-unreduced-bv-qme.tex
rg -n -e "app-nonscalar-kernel-row-complex" -e "app-minimal-full-equivariant-kernel-vanishing" -e "app-first-missing-nonscalar-row" appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-148-nonscalar-kernel-qme-class.md
```

Results:

- `git diff --check` passed.
- trailing-whitespace grep returned no hits.
- `scripts/finite_window_graph_array.py` reports the full-equivariant
  order-one residual and minimal order-two row sum as zero with
  \(C_{1,M}=C_{2,M}=0\).
- `py_compile` passed.
- `chktex` reported the existing warning class plus warnings on the new
  displayed formulas; no fatal TeX parse error was observed.
- `lacheck` exited zero and reported the existing whitespace-before-period
  warning class plus the `i.e.` spacing warning.
- the label scan found the three new appendix labels and the report entries.

No full `make pdf` was run because the shared checkout has concurrent
staged edits and the build writes tracked output outside this agent's
owned paths.

## Remaining obligations

- For any larger finite marked package, supply the order-one scalar-zero
  row outside \(\alpha_{\mathrm{sc}}\), if it exists.
- If no such row exists, supply the order-two genuine graph weights,
  CE-source faces, BV bracket rows, lower-counterterm rows, scalar gates,
  and truncation coefficients.
- After the row array is supplied, compute
  \(\mathfrak o^{\mathrm{ns}}_{n,M}\) and, if it vanishes windowwise, the
  Roos compatibility class for the counterterm tower.
