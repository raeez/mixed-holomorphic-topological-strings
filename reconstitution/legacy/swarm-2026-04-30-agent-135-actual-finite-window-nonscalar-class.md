# Agent 135 - Actual Finite-Window Non-Scalar Class

## Stable Core

The actual finite-window class from the graph/QME assembly is not
computable from Agent 127's abstract package alone.  The first computed
scalar-contact test is the one-cross-contraction boundary graph with two
Hamiltonian external legs and one open scalar loop.  It is an
\(\hbar^1\) graph.  In the full \(\mathfrak{gl}(N|N)\)-equivariant marked
habitat its scalar gate is zero because every cyclic supertrace of a
full-equivariant signed Brauer marker tensor is a power of
\(\operatorname{sdim}\mathbb C^{N|N}=0\).

The repaired manuscript label is:

- `thm:actual-finite-window-nonscalar-decision-datum`
- `rmk:actual-finite-window-scalar-gate-boundary`

## Graph Curvature Formula

For a labelled CE cycle \(\zeta_M\), the order-\(n\) graph curvature is

```tex
\operatorname{Ob}^{\mathrm{graph}}_{\mathcal G,M}[n](\zeta_M)
  =
[\hbar^n]\left(
  d_M\kappa^M_{\mathcal G,w,I}(\zeta_M)
  -\kappa^M_{\mathcal G,w,I}(d_{\mathrm{CE}}\zeta_M)
  +\frac12\sum_{(\zeta_M)}
    \{\kappa^M(\zeta'_M),\kappa^M(\zeta''_M)\}_{\hbar,M}
\right).
```

Expanded by graph components \(K^M_\Gamma\):

```tex
\sum_{|\Gamma|_\hbar=n}\varepsilon_\Gamma d_M K^M_\Gamma
-\sum_{|\Gamma'|_\hbar=n}\varepsilon^{\mathrm{CE}}_{\Gamma'}K^M_{\Gamma'}
+\frac12
 \sum_{|\Gamma_1|_\hbar+|\Gamma_2|_\hbar=n}
 \varepsilon_{\Gamma_1,\Gamma_2}
 \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar,M}.
```

With lower counterterms:

```tex
R_{n,M}
  =
\operatorname{Ob}^{\mathrm{graph}}_{\mathcal G,M}[n]
+[\hbar^n]\left(
  d_M C_{<n,M}
  +\frac12\{C_{<n,M},C_{<n,M}\}_{\hbar,M}
\right).
```

Then

```tex
\mathfrak s_{n,M}=\widehat\sigma_{\mathrm{sc},M}(R_{n,M}),
\qquad
[\mathfrak o^{\mathrm{fw}}_{n,M}]=[R_{n,M}]
\in H^1(\mathcal Q^\bullet_{\mathcal G,M}(I),d_M)
```

after the scalar gate vanishes.

## Scalar Gate

For the order-one marked scalar-contact graph:

```tex
\mathfrak s^{\mathrm{mk}}_{1,M}
  (X_{\Gamma,o,\mathfrak m,M})
  =
\sum_{i:\,r(\beta_i)=1}
  (-1)^{i-1}
  \operatorname{Str}_{\mathrm{cyc}}
    (\mu_{\beta_i}(\mathfrak m))
  \omega(f_{\partial_{\beta_i}\Gamma},
         g_{\partial_{\beta_i}\Gamma})
  \gamma_{\mathbf 1}.
```

Before extracting the coefficient, this is the \(\hbar^1\)-term
\(\hbar\mathfrak s^{\mathrm{mk}}_{1,M}\).

Full-equivariant marked result:

```tex
\operatorname{Str}_{\mathrm{cyc}}(\mathfrak C_\sigma)
  =
(\operatorname{sdim}V)^{c(\tau_m^{-1}\sigma)}=0,
\qquad V=\mathbb C^{N|N}.
```

Marker transport preserves the signed Brauer span, so every summand in
\(\mathfrak s^{\mathrm{mk}}_{1,M}\) has zero coefficient.  This kills the
scalar gate before the non-scalar class is formed.  It does not construct
a non-scalar primitive.

For comparison, ordinary scalar-reduced \(\mathfrak{gl}_N\) gives
\(N\omega(f,g)\gamma_{\mathbf 1}\) after extracting \(\hbar^1\), and an
even block marker \(T=\lambda_0P_{\bar0}+\lambda_1P_{\bar1}\) gives
\(N(\lambda_0-\lambda_1)\omega(f,g)\gamma_{\mathbf 1}\).

## Decision on the Non-Scalar Class

No counterterm was constructed.  The permitted files and reports do not
contain the actual finite graph-order table, CE cycle, orientation signs,
coproduct decomposition, graph weights, lower counterterm array, scalar
projection, and truncation data needed to decide the first non-scalar
order \(n_0\).

The exact missing datum inscribed in the manuscript is

```tex
\mathsf A^{\mathrm{fw}}_{n,M}
  =
(
  \mathcal G^{\leq n}_M,\ |\Gamma|_\hbar,\ \zeta_M,\
  \varepsilon,\ d_{\mathrm{CE}},\ \Delta_{\mathrm{CE}},\
  K^M_\Gamma,\ C_{<n,M},\
  \widehat\sigma_{\mathrm{sc},M},\ \pi_{M,N}
).
```

With this datum supplied, \(n_0\) is the least order for which
\(R_{n_0,M}\) is defined after scalar-gate vanishing and is not already
killed by lower choices.  Fixed-window solvability is equivalent to

```tex
[\mathfrak o^{\mathrm{fw}}_{n_0,M}]=0.
```

After choosing primitives \(C_{n_0,M}\), compatible finite-window
counterterms exist exactly when

```tex
\lambda^{\mathrm{fw}}_{n_0}
  =
\left[
  \bigl(
    [\pi_{M+1,M}C_{n_0,M+1}-C_{n_0,M}]
  \bigr)_M
\right]
\in
\varprojlim\nolimits^1_M
H^0(\mathcal Q^\bullet_{\mathcal G,M}(I))
```

vanishes.

## Valid Attacks

```yaml
- id: A1-135-01
  severity: 1
  status: healed
  lens: actual graph data
  target: tate-P1-hadamard-mittag-leffler.tex finite-window class
  claim: Agent 127's abstract finite-window graph package determines the
    first non-scalar order and its counterterm.
  broken_step: The graph package names \(\mathcal G_M\) but does not supply
    a graph-order table, CE cycle, orientation signs, graph weights, lower
    counterterms, scalar projection, or truncation data.
  minimal_heal: Inscribe the finite-window coefficient array
    \(\mathsf A^{\mathrm{fw}}_{n,M}\) as the exact missing datum.

- id: A1-135-02
  severity: 1
  status: healed
  lens: scalar/non-scalar separation
  target: scalar gate at order one
  claim: Full-equivariant marked scalar vanishing constructs a non-scalar
    primitive.
  broken_step: The cyclic-supertrace computation kills only
    \(\mathfrak s_{1,M}\); it does not decide
    \([\mathfrak o^{\mathrm{fw}}_{n_0,M}]\).
  minimal_heal: State the scalar gate formula and record that it vanishes
    before the kernel \(H^1\) class is formed.

- id: A1-135-03
  severity: 2
  status: healed
  lens: inverse-limit primitive
  target: finite-window-to-limit counterterms
  claim: Windowwise primitive existence is enough for a compatible
    counterterm tower.
  broken_step: Primitives may fail to truncate compatibly.
  minimal_heal: State the actual Roos class
    \(\lambda^{\mathrm{fw}}_{n_0}\in\varprojlim^1H^0\).
```

## Files Changed

- `tate-P1-hadamard-mittag-leffler.tex`
- `reconstitution/swarm-2026-04-30-agent-135-actual-finite-window-nonscalar-class.md`

Both paths are staged.

## Verification

Commands run:

```bash
git diff --check -- tate-P1-hadamard-mittag-leffler.tex reconstitution/swarm-2026-04-30-agent-135-actual-finite-window-nonscalar-class.md
git diff --cached --check -- tate-P1-hadamard-mittag-leffler.tex reconstitution/swarm-2026-04-30-agent-135-actual-finite-window-nonscalar-class.md
rg -n -F "actual-finite-window-nonscalar-decision-datum" tate-P1-hadamard-mittag-leffler.tex
rg -n -F "\\mathsf A^{\\mathrm{fw}}_{n,M}" tate-P1-hadamard-mittag-leffler.tex
rg -n -F "\\lambda^{\\mathrm{fw}}_{n_0}" tate-P1-hadamard-mittag-leffler.tex
grep -n '[[:blank:]]$' tate-P1-hadamard-mittag-leffler.tex reconstitution/swarm-2026-04-30-agent-135-actual-finite-window-nonscalar-class.md
lacheck tate-P1-hadamard-mittag-leffler.tex
chktex -q tate-P1-hadamard-mittag-leffler.tex
```

Results:

- `git diff --check` and `git diff --cached --check` passed.
- Label and formula scans found the new theorem, missing-datum array, and
  Roos obstruction formula.
- Trailing-whitespace grep returned no hits.
- `lacheck` and `chktex` reported nonfatal style warnings in the file;
  no fatal TeX syntax error was detected by the targeted checks.
- `make pdf` was not run because this shared checkout has concurrent
  staged manuscript edits and the build writes tracked output outside this
  agent's writable surface.

## Remaining Obligations

- Supply \(\mathsf A^{\mathrm{fw}}_{n,M}\) for the actual finite graph
  package.
- Compute whether any order-one non-scalar component remains after the
  full-equivariant scalar gate is killed.
- If a first non-scalar order \(n_0\) is found, compute
  \([R_{n_0,M}]\in H^1(\mathcal Q^\bullet_{\mathcal G,M})\).
- If the fixed-window classes vanish, construct primitives
  \(C_{n_0,M}\) and compute \(\lambda^{\mathrm{fw}}_{n_0}\).
