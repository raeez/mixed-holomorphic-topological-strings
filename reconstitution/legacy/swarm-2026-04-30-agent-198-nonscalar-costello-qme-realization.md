# Agent 198 - Non-scalar Costello/QME realization

Status: theorem-grade habitat inserted in
`appendix-unreduced-bv-qme.tex`; no commit or push.

## Source Identity

Verified source hashes:

```text
4d2c7af70e52c51faef63177cd1b7e2a0e54ae08d1b42228d3f78746d6640b21  materials/raw/2026-04-30-mixed-holomorphic-topological-strings-critique.pdf
5e56a4a3fdb694d7de8bd24dcfe18b1f519b31c2a1b89229259415054fd0ca13  materials/processed/2026-04-30-mixed-holomorphic-topological-strings-critique.txt
```

## Manuscript Insertions

Added:

- `def:app-native-finite-window-realization-habitat`
- `thm:app-constructive-nonscalar-costello-qme-realization`
- `prop:app-closed-rows-and-theta-three-source-face`

The habitat is native to
\[
  \R^2_{\mathrm{top}}\times\widehat{\C^2}_{0,\mathrm{hol}}.
\]
It uses the completed filtered local-functional complex
\[
  \mathfrak Q^\bullet_{\mathcal G,M}(I)
    =
  \left(
    \mathcal O^{\mathrm{bd}}_{\mathrm{loc},\mathcal G,M}
    (\mathcal E_w^M|_I;
     A^{\mathrm{pp},w,M}_{\partial,\hbar}(I)),
    d_M
  \right),
  \qquad
  d_M=Q+\{I^w_{0,M},-\}_{\hbar,M}.
\]

The Hom-valued kernel complex is
\[
  \mathbf K^\bullet_{\mathcal G,M}(I)
    =
  \operatorname{Hom}_{\mathrm{cont}}
  \left(C^\bullet_{\mathrm{lab}}(\mathcal G_M),
  \mathfrak Q^\bullet_{\mathcal G,M}(I)\right),
\]
\[
  d_{\mathbf K,M}T=d_MT-(-1)^{|T|}T\,d_{\mathrm{CE}},
  \qquad
  \operatorname{Curv}_{\mathbf K,M}(\kappa)
  =d_{\mathbf K,M}\kappa+\frac12[\kappa,\kappa]_{\mathbf K,M}.
\]

The zero-edge bulk-to-defect layer is fixed:
\[
  \kappa^{\mathrm{coef},M}_{\hbar,w,I}(u_{a(t)dt\otimes f})
    =\iota_I(B^{w,M}_f(a)),
  \qquad
  \kappa^{\mathrm{coef},M}_{\hbar,w,I}(c_{B,\rho})
    =\iota_I(\Theta^{w,M}_\rho(B)).
\]

## Row Criterion

The finite-window non-scalar residual is constructed from actual rows:
\[
  R^{\mathrm{row}}_{d\Gamma,M}
    =\varepsilon_\Gamma d_MK^M_\Gamma,
\]
\[
  R^{\mathrm{row}}_{\mathrm{CE}(\Gamma,\nu),M}
    =-\varepsilon^{\mathrm{CE}}_{\Gamma,\nu}
      K^M_\Gamma(\zeta_{M,\nu}),
\]
\[
  R^{\mathrm{row}}_{b(\Gamma_1,\Gamma_2),M}
    =
  \frac12\varepsilon_{\Gamma_1,\Gamma_2}
  \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar,M}.
\]

Scalar gate:
\[
  \mathfrak s_{n,M}
  =
  \sum_{\alpha\in\mathsf A^{\mathrm{fw}}_{n,M}}
  \widehat\sigma_{\mathrm{sc},M}(R^{\mathrm{row}}_{\alpha,M})=0.
\]

If the gate vanishes,
\[
  R^{\mathrm{ns}}_{n,M}
  =
  \sum_\alpha R^{\mathrm{row}}_{\alpha,M}
  \in \mathcal K^1_{\mathrm{ns},M}(I),
  \qquad
  \mathfrak o^{\mathrm{ns}}_{n,M}=[R^{\mathrm{ns}}_{n,M}].
\]

Primitive criterion:
\[
  R^{\mathrm{ns}}_{n,M}=\sum_i r^M_i\rho^M_i,\qquad
  d_{\mathrm{ns},M}\eta^M_j=\sum_iA^M_{ij}\rho^M_i.
\]
A finite-row counterterm exists exactly when
\[
  A^M c=-r^M.
\]
Failure is certified by a covector
\[
  \ell A^M=0,\qquad \ell(r^M)\neq0.
\]
Tower compatibility requires
\[
  T^{M,N}r^M=r^N,\qquad
  T^{M,N}A^M=A^N P^{M,N},
\]
and vanishing of the Roos class
\[
  [P^{M,N}c_M-c_N]\in
  H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I)).
\]

## Closed and Open Rows

Closed row:
\[
  R^{\mathrm{row}}_{\alpha_{\mathrm{sc}},M}=0,\qquad
  S_{\alpha_{\mathrm{sc}},M}=0,\qquad
  C_{\alpha_{\mathrm{sc}},M}=0
\]
in the full-equivariant \(V=\C^{N|N}\) branch.

Closed scalar-zero row:
\[
  R^{\mathrm{row}}_{\alpha_{11},M}
  =
  \operatorname{Str}_{\mathrm{cyc}}
  (\mu_{\beta_{11}}(\mathfrak m))\,
  \omega(z_1,z_1)
  \int_Ia(t)b(t)\gamma_{\mathbf 1}(t)\,dt
  =0,
\]
because \(\omega(z_1,z_1)=0\).  Primitive: \(C_{\alpha_{11},M}=0\).

First supplied open row:
\[
  R^{\mathrm{row}}_{\theta_3,M}
    =
  -K^M_{\Theta_3}(\zeta_{M,\nu_3})
    =:\mathsf E_{\theta_3,M},
  \qquad
  S_{\theta_3,M}=0.
\]
If \(d_{\mathrm{ns},M}\mathsf E_{\theta_3,M}=0\) is supplied, then
\[
  \mathfrak o^{\mathrm{ns}}_{\theta_3,M}
  =[\mathsf E_{\theta_3,M}].
\]
In the currently supplied one-row finite subcomplex,
\[
  \mathcal K^0_{\theta_3,M}=0,\qquad
  \mathcal K^1_{\theta_3,M}=\C\mathsf E_{\theta_3,M},\qquad
  d_{\theta_3,M}=0,
\]
the covector
\[
  \ell_{\theta_3}(\mathsf E_{\theta_3,M})=1
\]
certifies nonzero finite-row obstruction.  Missing healing data:
either \(C_{\theta_3,M}\) with
\[
  d_{\mathrm{ns},M}C_{\theta_3,M}
  =-\mathsf E_{\theta_3,M}
\]
and compatible truncation, or Hom-valued companion rows changing the
residual vector.

## Claim Status

Proved in the inserted appendix block:

- finite-window habitat and convolution differential;
- source-face contribution \(-\kappa d_{\mathrm{CE}}\);
- scalar gate before non-scalar class formation;
- fixed-window primitive linear system and cokernel certificate;
- Roos primitive-compatibility obstruction;
- closed \(\alpha_{\mathrm{sc}}\) and \(\alpha_{11}\) rows with zero
  primitive.

Precise open class:

- \(\mathfrak o^{\mathrm{ns}}_{\theta_3,M}
  =[\mathsf E_{\theta_3,M}]\) in the supplied finite row subcomplex.
  It is not a full-complex obstruction until the larger local-functional
  primitive search space is fixed.

Not claimed:

- arbitrary \(\mathcal D'_c(I)\)-labelled Costello graph theorem;
- all-graph summability;
- compact Calabi--Yau, global BCOV, CoHA, quintic, GV/OSV,
  Abel--Jacobi, Igusa, Borcherds, or BKM consequence.

## Files Changed

- `appendix-unreduced-bv-qme.tex`
- `reconstitution/swarm-2026-04-30-agent-198-nonscalar-costello-qme-realization.md`

## Verification Commands

```bash
shasum -a 256 materials/raw/2026-04-30-mixed-holomorphic-topological-strings-critique.pdf materials/processed/2026-04-30-mixed-holomorphic-topological-strings-critique.txt
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py >/tmp/finite-window-agent198.json
python3 -m json.tool /tmp/finite-window-agent198.json >/tmp/finite-window-agent198.pretty.json
python3 - <<'PY'
import json
with open('/tmp/finite-window-agent198.json') as f:
    data=json.load(f)
for row in data['finite_row_primitive_search_results']:
    print(row['case'], row['primitive_exists'],
          row['obstruction_value_on_residual'],
          row['primitive_coefficients'], row['obstruction_covector'])
PY
rg -n "native-finite-window-realization-habitat|constructive-nonscalar-costello-qme-realization|closed-rows-and-theta-three-source-face" appendix-unreduced-bv-qme.tex
git diff --check -- appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-198-nonscalar-costello-qme-realization.md
grep -n '[[:blank:]]$' appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-198-nonscalar-costello-qme-realization.md
rg -n "compact Calabi|CoHA|quintic|OSV|GV|Abel|Igusa|Borcherds|BKM" appendix-unreduced-bv-qme.tex
chktex -q appendix-unreduced-bv-qme.tex
```

Results:

- source hashes matched the prompt;
- `python3 -m py_compile scripts/finite_window_graph_array.py` passed;
- `python3 scripts/finite_window_graph_array.py` emitted the expected
  primitive-search decisions:
  `minimal_full_equivariant_order_2_zero` solved by zero primitive,
  `theta_3_current_finite_row_subcomplex` obstructed by covector
  \(\ell_{\theta_3}=1\), and
  `theta_3_with_supplied_candidate_C_theta_3` solved by the supplied
  candidate primitive;
- label scan found the three inserted anchors;
- `git diff --check` passed;
- trailing-whitespace grep returned no hits;
- duplicate-label scan returned no hits;
- compact/global firewall scan found only the appendix firewall sentence
  at the opening of `appendix-unreduced-bv-qme.tex`;
- `chktex -q appendix-unreduced-bv-qme.tex` returned non-fatal style
  warnings already characteristic of this appendix: label-placement,
  dash-length, bracket-spacing, and nonbreaking-space suggestions.  The
  inserted block has only the same style class; no fatal TeX error was
  reported by this lint pass.

Full `make pdf` not run in this subagent lane: the shared checkout has
large concurrent staged manuscript edits and tracked build output outside
the owned write paths.
