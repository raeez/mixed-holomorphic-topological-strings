# Agent 092 — Non-Scalar QME Habitat

Status: integrated by the main thread after proposal-only return.

## Stable Core

The unconditional non-scalar Costello graph/QME realization is not yet a
theorem.  The theorem-grade replacement is an obstruction-theory
criterion in the filtered local-functional complex

```tex
\mathfrak Q^\bullet_{w,\partial,\hbar}(I)
=
\varprojlim_{w_0}
\left(
\mathcal O_{\mathrm{loc}}^{\mathrm{bd}}
(\mathcal E_w^{w_0}|_I;
A^{\mathrm{pp},w,w_0}_{\partial,\hbar}(I)),
d_{\mathrm{QME}}
\right),
\qquad
d_{\mathrm{QME}}=Q+\{I_0^w,-\}_\hbar .
```

The scalar-symbol map becomes usable only after it is lifted to a
filtered chain projection

```tex
\widehat\sigma_{\mathrm{sc}}\colon
\mathfrak Q^\bullet_{w,\partial,\hbar}(I)
\to
C^\bullet_{\mathrm{Lie}}(\bar A;\C\gamma_{\mathbf 1})[1][[\hbar]] .
```

The sharp non-scalar obstruction then lies in

```tex
H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}}).
```

## Integrated Repair

The main thread added
`appendix-unreduced-bv-qme.tex`, Lemma
`filtered-scalar-projection-obstruction`: a filtered lift
`\widehat\sigma_{\mathrm{sc}}` exists exactly when the successive
chain-map obstruction classes

```tex
o_\sigma^{(r)}
\in
H^1(
\operatorname{Hom}(\operatorname{gr}_F\mathfrak Q^\bullet_{\mathrm{bd}},
C^\bullet_{\mathrm{Lie}}(\bar A;\C\gamma_{\mathbf 1})[1])_{-r})
```

vanish in the complete scalar-contact filtration.

## Valid Attacks

```yaml
- id: A1-092-01
  severity: 1
  status: valid
  target: main.tex:7334, open-obligations.tex:324
  claim: Non-scalar graph realization follows from the componentwise surface.
  broken_step: componentwise data do not construct the obstruction cocycle,
    finite-window counterterms, or bulk-to-defect kernel.
  minimal_heal: state and then prove the vanishing criterion in
    H^1(ker sigma_sc,d_QME).
  residual: explicit all-order Costello counterterm and kernel construction.

- id: A1-092-02
  severity: 1
  status: healed
  target: appendix-unreduced-bv-qme.tex
  claim: scalar-symbol projection is already an actual projection.
  broken_step: an associated-graded projection does not define
    H^1(ker sigma_sc) until a filtered chain lift is supplied.
  minimal_heal: add the filtered chain-map obstruction tower.
  residual: kill the o_sigma classes in the weighted brane-defect habitat.

- id: A1-092-03
  severity: 2
  status: valid
  target: principal-part current target
  claim: distributional principal-part currents are automatically
    Costello-local.
  broken_step: support-local D'_c brackets do not supply wavefront/RG
    admissibility.
  minimal_heal: use finite-window regular densities or prove
    current-compatible wavefront/counterterm rules.
  residual: Costello-local theorem for the current target.
```

## Remaining Obligation

Agents 093 and 094 must decide whether the bulk-to-defect kernel and
finite-window counterterm recursion can kill both the scalar-lift tower
`o_sigma^{(r)}` and the reduced non-scalar class.
