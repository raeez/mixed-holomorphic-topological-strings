# Agent 153 - First Scalar-Zero Row

Status: patched owned appendix surface; no commits or pushes.

## Stable core

Under the finite closed graph-list axioms there is no absence theorem for
literal order-one scalar-zero rows outside
\(\alpha_{\mathrm{sc}}\).  A finite list may retain zero labelled
scalar-contact rows.

The first explicit local row is the one-cross scalar-contact row with
ordered Hamiltonian inputs \((a,z_1)\), \((b,z_1)\).  Its extracted
\(\hbar^1\)-coefficient has
\[
  \omega(z_1,z_1)=0.
\]
With positive incidence convention:
\[
  |\alpha_{11}|_\hbar=1,\quad
  d_{\max}(\alpha_{11})=1,\quad
  p_{\alpha_{11}}=1,\quad
  r_{\alpha_{11}}=1,\quad
  \iota_{\alpha_{11},M}=+1.
\]
The row value and scalar gate are
\[
  R^{\mathrm{row}}_{\alpha_{11},M}
    =
  \operatorname{Str}_{\mathrm{cyc}}
    (\mu_{\beta_{11}}(\mathfrak m))
  \omega(z_1,z_1)
  \int_I a(t)b(t)\gamma_{\mathbf 1}(t)\,dt
    =0,
\]
\[
  S_{\alpha_{11},M}
    =
  \operatorname{Str}_{\mathrm{cyc}}
    (\mu_{\beta_{11}}(\mathfrak m))
  \omega(z_1,z_1)\gamma_{\mathbf 1}=0.
\]
For \(M\geq N\geq1\), retain the labelled row and set
\[
  t^{M,N}_{\alpha_{11}\alpha_{11}}=1,\qquad
  t^{M,N}_{\alpha_{11}\alpha'}=0\quad(\alpha'\neq\alpha_{11}).
\]
The class is
\[
  [R^{\mathrm{row}}_{\alpha_{11},M}]
    =
  0
  \in H^1(\mathcal K^\bullet_{\mathrm{ns},M}(I),d_{\mathrm{ns},M}),
\]
and the counterterm contribution is \(C_{1,M}=0\).

If zero rows are suppressed and no nonzero order-one row outside
\(\alpha_{\mathrm{sc}}\) is supplied, the order-two scalar-zero row sum is
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
    \sum_{\substack{|\Gamma_1|_\hbar=|\Gamma_2|_\hbar=1\\
      \Gamma_i\neq\alpha_{\mathrm{sc}}}}
      \varepsilon_{\Gamma_1,\Gamma_2}
      \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar,M}.
\end{aligned}
\]
Under Agent 148's minimal full-equivariant hypotheses the three sums are
empty, hence \(R^{\mathrm{ns}}_{2,M}=0\) and \(C_{2,M}=0\).

## Valid attacks

```yaml
- id: A1-153-01
  severity: 2
  status: healed
  lens: literal scalar-zero row
  target: appendix-unreduced-bv-qme.tex, first order beyond alpha_sc
  claim: The finite closed graph-list axioms prove that no order-one scalar-zero row exists outside alpha_sc.
  broken_step: The axioms allow a finite list to retain a zero labelled scalar-contact row; the pair (z1,z1) has omega(z1,z1)=0.
  evidence_type: direct_computation
  evidence_ref: prop:app-first-scalar-zero-order-one-row; scripts/finite_window_graph_array.py reports omega_z1_z1 = 0
  confidence: high
  blast_radius: An absence theorem would be false unless "row" is restricted to nonzero summands.
  minimal_heal: Add the explicit row alpha_11 and compute its zero class in H^1(K_ns).
  residual: Nonzero order-one rows still require actual K^M_Gamma values and signs from the finite package.

- id: A1-153-02
  severity: 2
  status: healed
  lens: order-two reduction
  target: order-two scalar-zero row sum
  claim: If no order-one row appears, the order-two formula still includes brackets with alpha_sc or lower-counterterm terms.
  broken_step: In the full-equivariant minimal branch K^M_{alpha_sc}=0 and C_{1,M}=0.
  evidence_type: direct_computation
  evidence_ref: prop:universal-scalar-contact-bracket-rows; rmk:app-order-two-after-no-nonzero-order-one-row
  confidence: high
  blast_radius: Extra spurious order-two terms would create a false obstruction surface.
  minimal_heal: Remove bracket rows containing alpha_sc and lower-counterterm terms under the no-nonzero-order-one hypothesis.
  residual: Genuine order-two graph weights and CE-source faces remain package data.
```

## Repaired labels

- `prop:app-first-scalar-zero-order-one-row`
- `rmk:app-order-two-after-no-nonzero-order-one-row`

## Commands and results

```bash
python3 scripts/finite_window_graph_array.py
```

Reported \(\omega(z_1,z_1)=0\), \(\omega(z_1,z_2)=1\), minimal
full-equivariant \(R^{\mathrm{ns}}_{2,M}=0\), and \(C_{2,M}=0\).

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
git diff --check -- appendix-unreduced-bv-qme.tex
grep -n '[[:blank:]]$' appendix-unreduced-bv-qme.tex
chktex -q appendix-unreduced-bv-qme.tex
lacheck appendix-unreduced-bv-qme.tex
```

`py_compile` and `git diff --check` passed.  The trailing-whitespace grep
returned no hits.  `chktex` and `lacheck` reported the existing warning
class in this appendix; no fatal TeX parse error was observed.

## Files changed/staged

Changed:

- `appendix-unreduced-bv-qme.tex`
- `reconstitution/swarm-2026-04-30-agent-153-first-scalar-zero-row.md`

Not changed by this agent:

- `scripts/finite_window_graph_array.py` was read and executed only.  It
  already reports the needed \(\omega(z_1,z_1)=0\) check.

Staged:

- `appendix-unreduced-bv-qme.tex` (Agent 153 hunk staged on top of the
  pre-existing staged appendix changes)
- `reconstitution/swarm-2026-04-30-agent-153-first-scalar-zero-row.md`

## Remaining obligations

- Decide whether the canonical row convention suppresses zero rows.  If it
  does, \(\alpha_{11}\) is only a diagnostic row and not part of the final
  array.
- Supply any nonzero order-one row outside \(\alpha_{\mathrm{sc}}\) with
  its actual \(K^M_\Gamma\), sign, scalar gate, and truncation data.
- If no nonzero order-one row is supplied, populate the genuine order-two
  graph weights, CE-source faces, bracket signs, scalar gates, and
  truncation coefficients before claiming a nonzero class in
  \(H^1(\mathcal K_{\mathrm{ns},M})\).
