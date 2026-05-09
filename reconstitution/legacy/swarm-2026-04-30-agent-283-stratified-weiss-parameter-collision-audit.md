# Agent 283 Stratified Weiss Parameter Collision Audit

Status: report-only audit.  No TeX file was edited.

Scope: the normal \(\Omega\), stratified Weiss, and physical trace theorem
lane, with emphasis on collisions among
\(\hbar_{\mathrm{W}}\), \(\hbar_{\mathrm{QME}}\), \(\hbar_\omega\), and
the \(P_0\)-bracket notation.

## Verdict

The three-parameter gate is installed in the dictionary, ledger,
open-obligation, and appendix sources:
\[
  \hbar_{\mathrm{QME}},\qquad
  \hbar_{\mathrm{W}},\qquad
  \hbar_\omega .
\]
\(\hbar_{\mathrm{QME}}\) is the Costello/BV loop parameter in curvature
and counterterm equations; \(\hbar_{\mathrm{W}}\) is the Weyl/Moyal
deformation parameter of the brane algebra; \(\hbar_\omega\) scalarizes
the equivariant Hamiltonian bracket.  The self-dual or Weyl branch may
identify \(\hbar_{\mathrm{W}}=\hbar_\omega\).  It must not identify either
with \(\hbar_{\mathrm{QME}}\) without a stated QME normalization theorem.

The live collision is in `theorem-lanes.tex`.  The QME residual and the
stratified \(P_0\)-centrality homotopy use the Weyl parameter where the
appendix and open-obligation source already use the QME parameter.  One
adjacent `open-obligations.tex` row still uses a bare \(\hbar\) in a
Costello centrality bracket.

## Source Anchors

- `local-dictionary.tex:567-581`: canonical three-parameter distinction.
- `appendix-unreduced-bv-qme.tex:2546-2558`: same distinction inside the
  normal \(\Omega\)-equivariant Costello datum.
- `appendix-unreduced-bv-qme.tex:2591-2595`: the equivariant
  local-functional differential uses
  \(\{I^w_{0,M,\Omega},-\}_{\hbar_{\mathrm{QME}},M,\Omega}\).
- `appendix-unreduced-bv-qme.tex:2777-2785`: the order-\(n\) QME residual
  extracts \([\hbar_{\mathrm{QME}}^n]\) and brackets counterterms with
  subscript \(\hbar_{\mathrm{QME}}\).
- `appendix-unreduced-bv-qme.tex:3461-3467`: the equivariant centrality
  row brackets graph kernels with subscript \(\hbar_{\mathrm{QME}}\).
- `open-obligations.tex:976-987`: the stratified obligation states the
  three formal parameters and allows only the Weyl branch
  \(\hbar_{\mathrm{W}}=\hbar_\omega\).
- `open-obligations.tex:1012-1024`: product centrality and
  \(P_{0,\hbar_{\mathrm{QME}}}\)-centrality homotopies are stated with the
  QME parameter.
- `open-obligations.tex:1030-1032`: reduced current brackets remain
  \(\hbar_{\mathrm{W}}\)-brackets.  This is correct: these are algebraic
  Weyl/Moyal current data, not QME local-functional homotopies.

## Mandatory Replacements

### 1. `theorem-lanes.tex:2934-2939`

Problem: the order-\(n\) QME residual extracts
\([\hbar_{\mathrm{QME}}^n]\) but brackets counterterms with
\(\hbar_{\mathrm W}\).  This makes the Weyl deformation parameter appear
to control the Costello graph bracket.

Replace the displayed residual by:

```tex
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
```

Reason: this matches the appendix criterion at
`appendix-unreduced-bv-qme.tex:2777-2785`.

### 2. `theorem-lanes.tex:3071-3084`

Problem: the stratified centrality homotopy is a
\(d_{\mathrm{QME}}\)-homotopy, but the bracket is printed as
\(P_{0,\hbar_{\mathrm W}}\).

Replace the paragraph and formula by:

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

Reason: this matches `open-obligations.tex:1012-1024` and the
Agent 273/278 internal stratified vector.  The algebraic current
brackets over \(\hbar_{\mathrm{W}}\) do not supply these homotopies.

### 3. `theorem-lanes.tex:1663-1674`

Problem: the equivariant CE/PV contraction may be scaled by
\(\hbar_\omega\), and the current sentence calls this simply a
\(P_0\) convention.  In the neighboring theorem lane, \(P_0\) also refers
to the brane-defect centrality bracket.  That creates a notation
collision.

Replace the final sentence after the displayed contractions by:

```tex
  The latter is the \(L_\omega\)-weighted classical \(P_0\) contraction
  convention.  It is neither the Weyl/Moyal
  \(P_{0,\hbar_{\mathrm{W}}}\) bracket nor the brane-defect
  \(P_{0,\hbar_{\mathrm{QME}}}\) bracket.
```

Reason: \(\hbar_\omega\) scalarizes the equivariant Hamiltonian line; it
does not choose the Weyl deformation branch or solve a QME bracket.

### 4. `open-obligations.tex:1046-1050`

Problem: this centrality row still uses a bare \(\hbar\)-subscript in a
Costello graph bracket.

Replace:

```tex
        \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar,M}
```

by:

```tex
        \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar_{\mathrm{QME}},M}
```

Reason: the row is a QME/local-functional row.  The normal
\(\Omega\)-branch immediately below forms the same row over
\(R_\Omega^{N,M}[[\hbar_{\mathrm{QME}}]]\).

## Notation Normalizations

`theorem-lanes.tex` is the only checked TeX file still using the
unbraced spelling `\hbar_{\mathrm W}`.  Normalize it to the canonical
`\hbar_{\mathrm{W}}` at:

- `theorem-lanes.tex:1681`
- `theorem-lanes.tex:1683`
- `theorem-lanes.tex:3034`
- `theorem-lanes.tex:3035`
- `theorem-lanes.tex:3037`
- `theorem-lanes.tex:3043`
- `theorem-lanes.tex:3046`
- `theorem-lanes.tex:3232`

After the semantic replacements above, `theorem-lanes.tex:2938`,
`theorem-lanes.tex:3072`, and `theorem-lanes.tex:3082` no longer contain
the Weyl parameter.  If the non-\(\Omega\) graph catalogue at
`theorem-lanes.tex:3232-3236` remains a chosen Weyl branch, normalize the
bracing only.  Do not convert that line to \(\hbar_{\mathrm{QME}}\)
without also splitting the older generic-\(\hbar\) convention in
`appendix-unreduced-bv-qme.tex:2142-2167`.

## Vector Label Gate

The component name
\[
  \operatorname{ob}^{P_0}_{\mathrm{cent}}
\]
can remain as a type label only if the local text immediately defines it
as the \(P_{0,\hbar_{\mathrm{QME}}}\)-centrality obstruction in the
brane-defect local-functional complex.

Preferred exact insertion after the stratified vectors at
`theorem-lanes.tex:3061-3069`, `open-obligations.tex:1105-1113`, and
`claim-strength-ledger.tex:783-791`:

```tex
  Here \(\operatorname{ob}^{P_0}_{\mathrm{cent}}\) abbreviates the
  \(P_{0,\hbar_{\mathrm{QME}}}\)-centrality obstruction in the
  brane-defect local-functional complex.  It is not the reduced
  Weyl/Moyal current bracket over \(\hbar_{\mathrm{W}}\).
```

Stronger notation if the integrator wants no hidden parameter:

```tex
  \operatorname{ob}^{P_{0,\hbar_{\mathrm{QME}}}}_{\mathrm{cent}}
```

Use this only in the stratified/\(\Omega\) vector.  Do not globally
rewrite every historical \(P_0\) occurrence; many earlier occurrences
mean the classical bracket-admissible \(P_0\) realization.

## Non-Replacements

- `open-obligations.tex:1031-1032` should stay
  \(\hbar_{\mathrm{W}}\).  These are reduced current brackets on the
  Weyl/Moyal brane target.
- `claim-strength-ledger.tex:753-766`, `local-dictionary.tex:567-581`,
  and `appendix-unreduced-bv-qme.tex:2546-2558` already state the
  three-parameter gate correctly.
- \(\hbar_\omega\) in the coefficient ring
  \(R_\Omega^{N,M}\) at `theorem-lanes.tex:2836-2842`,
  `open-obligations.tex:919-925`, and `claim-strength-ledger.tex:699-704`
  is correct.  It is the equivariant line scalarizer, not the QME loop
  parameter.

## Attack-Heal Closure

Fatal attack: the current theorem lane lets the Weyl/Moyal deformation
parameter appear in a QME residual and in a \(d_{\mathrm{QME}}\)-centrality
homotopy.  This can falsely identify algebraic reduced current brackets
with Costello brane-defect graph brackets.

Heal: use \(\hbar_{\mathrm{QME}}\) for graph curvature, counterterm,
centrality, and \(P_0\)-homotopy brackets; use \(\hbar_{\mathrm{W}}\) only
for Weyl/Moyal brane algebra and reduced current brackets; use
\(\hbar_\omega\) only for equivariant line scalarization unless a branch
explicitly identifies it with \(\hbar_{\mathrm{W}}\).

Checks run:

```bash
rg -n -F '\hbar_{\mathrm W}' *.tex
rg -n -F 'P_{0,\hbar_{\mathrm W}}' *.tex
rg -n -F 'P_{0,\hbar_{\mathrm{QME}}}' *.tex
rg -n -F '}_{\hbar_{\mathrm W}' *.tex
rg -n -F '\hbar_{\mathrm{W}}' theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex appendix-unreduced-bv-qme.tex
rg -n -F '\hbar_{\mathrm{QME}}' theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex appendix-unreduced-bv-qme.tex
```
