# Agent 290 Report: Stratified Weiss/Omega Parameter Repair Integration Spec

Status: report-only integration specification.

Worktree: `/Users/raeez/topological-strings`.

Owned writable files:

- `reconstitution/stratified-weiss-omega-parameter-repair-integration-spec-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-290-stratified-weiss-omega-parameter-repair-integration-spec.md`

No TeX file was edited.  No build was run.

## Claim Attacked

The attacked claim is that the current stratified Weiss/Omega TeX already
has a coherent internal obstruction vector and clean separation among
\[
  \hbar_{\mathrm{QME}},\qquad
  \hbar_{\mathrm{W}},\qquad
  \hbar_\omega .
\]

It does not.  The TeX still has the old seven-component vector with the
external source gate inside the internal theorem surface, and
`theorem-lanes.tex` still places the Weyl parameter in QME-bracket
positions.

## Evidence Read

- `CLAUDE.md`, `AGENTS.md`,
  `~/ecosystem/INVARIANTS.md`,
  `~/ecosystem/AGENTS-HARNESS.md`.
- `reconstitution/stratified-weiss-obstruction-integration-spec-2026-04-30.md`.
- `reconstitution/stratified-weiss-parameter-collision-audit-2026-04-30.md`.
- `reconstitution/swarm-2026-04-30-agent-273-stratified-weiss-obstruction-integration-spec.md`.
- `reconstitution/swarm-2026-04-30-agent-283-stratified-weiss-parameter-collision-audit.md`.
- `reconstitution/internal-stratified-weiss-descent-construction-push-2026-04-30.md`.
- `reconstitution/swarm-2026-04-30-agent-266-internal-stratified-weiss-descent-construction-push.md`.
- `reconstitution/swarm-2026-04-30-agent-278-internal-stratified-weiss-tex-audit.md`.
- `references/primary-sources/weiss-ran-stratified-descent-source-anchors-2026-04-30.md`.
- `references/primary-sources/omega-stratified-source-anchors-2026-04-30.md`.
- `theorem-lanes.tex:1640-1735`, `2820-3250`.
- `open-obligations.tex:870-1215`.
- `claim-strength-ledger.tex:530-855`.
- `local-dictionary.tex:548-720`.
- `commands.tex`, `mathmacros.tex`, `notation.tex`, `preamble.tex` by
  search for bracket and \(\hbar\) macros.

## Verification Commands

Current collision checks:

```bash
rg -n -F '\hbar_{\mathrm W' theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex appendix-unreduced-bv-qme.tex main.tex
rg -n -F 'P_{0,\hbar_{\mathrm W}}' theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex appendix-unreduced-bv-qme.tex main.tex
rg -n -F '}_{\hbar' theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex appendix-unreduced-bv-qme.tex main.tex
rg -n -F '\operatorname{Ob}_{\mathrm{str},\Omega,N}' theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex main.tex
rg -n -F '\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}' theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex main.tex
rg -n -F '\operatorname*{holim}' theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex main.tex
```

Observed facts:

- \(\operatorname{Ob}_{\mathrm{str},\Omega,N}\) occurs in
  `theorem-lanes.tex:3061`, `open-obligations.tex:1105`,
  `claim-strength-ledger.tex:553`, and `claim-strength-ledger.tex:789`.
- \(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) remains inside the
  old internal vector at `theorem-lanes.tex:3069`,
  `open-obligations.tex:1113`, and `claim-strength-ledger.tex:797`.
- `open-obligations.tex:1009` still uses
  `\operatorname*{holim}_{U\in\mathcal U}` for the Weiss defect.
- `theorem-lanes.tex:2938` uses
  `\hbar_{\mathrm W}` in a QME residual bracket.
- `theorem-lanes.tex:3072` and `theorem-lanes.tex:3082` use
  `P_{0,\hbar_{\mathrm W}}` in \(d_{\mathrm{QME}}\)-centrality
  homotopies.
- `open-obligations.tex:1049` uses a bare `\hbar` in a Costello graph
  bracket inside the stratified obligation.
- `theorem-lanes.tex` has unbraced `\hbar_{\mathrm W...}` occurrences at
  `1681`, `1683`, `1686`, `2938`, `3034`, `3035`, `3037`, `3043`,
  `3046`, `3072`, `3082`, `3090`, `3091`, `3107`, `3153`, `3195`,
  `3198`, `3232`, and `3236`.

## Integration Decision

The repair is not a demotion.  It is a sharper obstruction theorem.

The reduced product-basis object is proved:
\[
  \delta_{\mathrm{pref}}=\delta_{\mathrm{assoc}}=0
\]
on product disks and brane intervals with extension-by-zero products.
The full stratified theorem is the exact vanishing problem
\[
  \operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}=0
\]
with compatible null-homotopies.  The source class
\(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) is external.  It does
not belong to the internal vector.

## TeX-Ready Replacement Packet

### Internal stratified vector

```tex
\[
  \operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}
  =
  (
    \delta_{\mathrm{pref}},
    \delta_{\mathrm{assoc}},
    \delta_{\mathrm{Weiss}},
    \operatorname{ob}_{\mathrm{collar}},
    \operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}},
    \operatorname{ob}^{P_0}_{\mathrm{cent}},
    \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}},
    \operatorname{ob}_{\Omega\mathrm{-basic}},
    \operatorname{ob}_{\mathrm{tr}\mathrm{-top}}
  ).
\]
Here \(\operatorname{ob}^{P_0}_{\mathrm{cent}}\) abbreviates the
\(P_{0,\hbar_{\mathrm{QME}}}\)-centrality obstruction in the
brane-defect local-functional complex.  It is not the reduced
Weyl/Moyal current bracket over \(\hbar_{\mathrm{W}}\).
```

Source gate:

```tex
The source-primary class
\(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) is not an internal
component of
\(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\).  It is an
external matched-conventions gate for importing Costello--Gwilliam,
AFT, CFG, Weiss/Ran, or Costello \(\Omega\)-background source theorems.
```

### Reduced product-basis positive datum

```tex
Let \(\mathcal B^{\mathrm{red}}_{\mathrm{prod}}(X,L)\) be the
two-color product basis whose basics are bulk product disks
\(U\times B\subset X\setminus L\), brane intervals \(I\subset L\), and
finite disjoint unions.  Put
\[
  \mathcal F^{\mathrm{red}}_{\Omega,X}(U\times B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \left(
    \Omega_c^\bullet(U)\widehat\otimes
    \Omega_c^{0,\bullet}(B)\widehat\otimes
    (\mathfrak h\ltimes\mathcal P[1])
  \right)
  \widehat\otimes R_\Omega^{N,M},
\]
where
\(\mathcal P=\operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)
\cong\mathfrak h^\vee_{\mathrm{cont}}\), and
\[
  \mathcal F^{\mathrm{red}}_{\Omega,L}(I)
  =
  A^{\mathrm{pp},w}_{\partial,\Omega,\hbar_{\mathrm{W}}}(I).
\]
The products are extension by zero on compact supports followed by CE
or completed symmetric multiplication.  Hence
\(\delta_{\mathrm{pref}}=\delta_{\mathrm{assoc}}=0\) on this reduced
product-basis datum.  No collar module, arbitrary collared Weiss
descent, unreduced centrality homotopy, brane-defect QME curvature
cancellation, basic \(\Omega\)-primitive, or trace-state topology is
constructed here.
```

### Cech cone Weiss defect

```tex
A collared stratified Weiss cover \(\mathcal U=\{U_i\}\) of \(V\) is a
stratified cover such that every finite subset of \(V\) lies in some
\(U_i\), and if the subset meets \(L\), the same \(U_i\) contains a
product collar of its lower-stratum part.  For a candidate
\(\mathcal F^{\mathrm{str}}_{\Omega,N}\), put
\[
  \check C^p(\mathcal U;\mathcal F^q)
  =
  \prod_{i_0<\cdots<i_p}
  \mathcal F^q(U_{i_0}\cap\cdots\cap U_{i_p}),
  \qquad
  \mathbb D=\check\delta+(-1)^p d_{\mathcal F},
\]
and
\[
  \delta_{\mathrm{Weiss}}(V,\mathcal U)
  =
  \operatorname{Cone}\left(
    \mathcal F^{\mathrm{str}}_{\Omega,N}(V)
    \to
    \operatorname{Tot}\check C^\bullet
    (\mathcal U;\mathcal F^{\mathrm{str}}_{\Omega,N})
  \right).
\]
```

### QME and centrality parameter repairs

QME residual:

```tex
  \[
  \begin{aligned}
    R^{\mathrm{ns}}_{n,\Omega,M}
      =
    [\hbar_{\mathrm{QME}}^n]\bigl(
      &\operatorname{Curv}_{\mathbf K,\Omega,M}
      +d_{M,\Omega}C_{<n,\Omega,M}\\
      &+\frac12
      \{C_{<n,\Omega,M},C_{<n,\Omega,M}\}_{\hbar_{\mathrm{QME}},M,\Omega}
    \bigr),
  \end{aligned}
  \]
```

Stratified centrality:

```tex
  The centrality terms require product and
  \(P_{0,\hbar_{\mathrm{QME}}}\)-homotopies
  against unreduced brane observables:
  \[
    d_{\mathrm{QME}}H^{\mathrm{prod}}_{x,a}
    =
    \rho(x)a-(-1)^{|x||a|}a\rho(x),
  \]
  \[
    d_{\mathrm{QME}}H^{P_0}_{x,a}
    =
    \{\rho(x),a\}_{P_{0,\hbar_{\mathrm{QME}}}}
    -\rho_{\mathrm{mod}}(x;a).
  \]
```

Open-obligation centrality row:

```tex
        \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar_{\mathrm{QME}},M}
```

Weighted classical contraction sentence:

```tex
  The latter is the \(L_\omega\)-weighted classical \(P_0\) contraction
  convention.  It is neither the Weyl/Moyal
  \(P_{0,\hbar_{\mathrm{W}}}\) bracket nor the brane-defect
  \(P_{0,\hbar_{\mathrm{QME}}}\) bracket.
```

Trace aggregate:

```tex
The component \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\) is the
aggregate trace-state topology obstruction; its expanded trace vector is
\(\operatorname{Ob}_{\mathrm{tr},\Omega}\).
```

## Parameter Normalization Rules

Apply semantic replacements first:

- `theorem-lanes.tex:2938`:
  \(\hbar_{\mathrm W}\mapsto\hbar_{\mathrm{QME}}\) inside the QME
  residual bracket.
- `theorem-lanes.tex:3072` and `theorem-lanes.tex:3082`:
  \(P_{0,\hbar_{\mathrm W}}\mapsto
  P_{0,\hbar_{\mathrm{QME}}}\).
- `open-obligations.tex:1049`:
  \(\hbar\mapsto\hbar_{\mathrm{QME}}\) inside the Costello centrality
  bracket.

Then apply bracing normalizations:

- \(\hbar_{\mathrm W}\mapsto\hbar_{\mathrm{W}}\) at the remaining
  Weyl/Moyal current, Hamiltonian-reduction, and chosen-Weyl-branch
  sites.
- \(\hbar_{\mathrm W,N}\mapsto\hbar_{\mathrm{W},N}\) at the physical
  finite-\(N\) trace sites.

Do not rewrite the algebraic reduced current brackets over
\(\hbar_{\mathrm{W}}\) to \(\hbar_{\mathrm{QME}}\).  Do not rewrite older
non-Omega generic-\(\hbar\) graph rows in the appendix as part of this
lane; that is a separate convention split.

## File Integration Targets

`theorem-lanes.tex`:

- install the weighted contraction sentence around `1663-1674`;
- repair the QME residual at `2931-2940`;
- add the \(\operatorname{ob}_{\Omega\mathrm{-basic}}\) cross-reference
  after the QME vector;
- insert the reduced product-basis datum after `3055`;
- replace `3057-3070` with the internal vector and source gate;
- replace `3071-3084` with the QME-parameter centrality homotopies;
- normalize all remaining unbraced Weyl symbols.

`open-obligations.tex`:

- insert the reduced product-basis datum before the full target;
- replace `1005-1010` by the Cech cone;
- repair `1049`;
- replace `1103-1114` by the internal vector, \(P_0\)-gate, and source
  gate;
- tie the trace block to
  \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\).

`claim-strength-ledger.tex`:

- add a proved reduced product-basis row;
- replace the old vector at `789-798`;
- replace the generic reference at `553`;
- tie the protected trace row to
  \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\) and
  \(\operatorname{Ob}_{\mathrm{tr},\Omega}\).

`local-dictionary.tex`:

- define the reduced product basis, Cech cone, internal vector,
  \(\operatorname{ob}_{\Omega\mathrm{-basic}}\), and
  \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\);
- expand \(\operatorname{ob}_{\Omega,\mathrm{strat}}\) through the
  internal vector;
- route \(\operatorname{ob}_{\Omega,N\to\infty}\) through the trace
  topology component.

## Closure

This report writes the integration specification only.  It leaves every
TeX file untouched for the integration owner.
