# Agent 094 finite-window counterterms report

## Verdict

The weighted finite-window machinery does not, by itself, construct
non-scalar Costello counterterms killing the reduced QME obstruction.
It supplies the coefficient kernel, Hadamard support control,
Mittag-Leffler finite-window transport, and admissible-weight
independence. The missing datum is the actual vanishing of a
finite-window non-scalar obstruction vector.

I strengthened `tate-T1-weighted-completion.tex` by adding an exact
criterion:

```tex
\mathcal Q^\bullet_{w,M}(I)
  =
  \ker(\widehat\sigma_{\mathrm{sc},M})
  \subset
  \left(
    \mathcal O_{\mathrm{loc}}^{\mathrm{bd}}\bigl(
      \mathcal E_w^M|_I;
      A_{\partial,\hbar}^{\mathrm{pp},w,M}(I)\bigr),
    d_M
  \right),
\qquad
d_M=Q+\{I^w_{0,M},-\}_{\hbar,M}.
```

At order `\hbar^n`, after lower counterterms have been chosen, the
window residual is

```tex
\mathfrak o^{\mathrm{ns}}_{n,M}
  =
  [\hbar^n]\left(
    \operatorname{Ob}^{\mathrm{red}}_{w,\partial,\hbar,M}
    +d_MC_{<n,M}
    +\frac12\{C_{<n,M},C_{<n,M}\}_{\hbar,M}
  \right)
  \in Z^1(\mathcal Q^\bullet_{w,M}(I)).
```

Compatible finite-window order-`n` counterterms exist exactly when both
obstructions vanish:

```tex
\bigl([\mathfrak o^{\mathrm{ns}}_{n,M}]\bigr)_M
  \in \varprojlim_M H^1(\mathcal Q^\bullet_{w,M}(I)),

\lambda_n
  \in
  \varprojlim\nolimits^1_M
  H^0(\mathcal Q^\bullet_{w,M}(I)),
```

where `\lambda_n` is the Milnor/Roos primitive-compatibility class
represented by

```tex
\bigl[\pi_{M,N}c_{n,M}-c_{n,N}\bigr]
  \in H^0(\mathcal Q^\bullet_{w,N}(I)).
```

If the `H^0` tower is Mittag-Leffler, the `\varprojlim^1` term vanishes.
Iterating this criterion constructs the `\hbar`-adic compatible
counterterm exactly on the vanishing locus of

```tex
\mathfrak O^{\mathrm{ns}}_n
  =
  \bigl(([\mathfrak o^{\mathrm{ns}}_{n,M}])_M,\lambda_n\bigr).
```

A nonzero first `\mathfrak O^{\mathrm{ns}}_n` is the precise obstruction.
Changing admissible weight transports the pair and does not kill it.

## Local anchors read

- `main.tex:7177`: componentwise quantum coefficient surface.
- `main.tex:7336`: non-scalar realization problem and A6b boundary.
- `main.tex:7407`: remaining reduced non-scalar class.
- `open-obligations.tex:292`: componentwise surface plus non-scalar
  Costello graph realization obligation.
- `open-obligations.tex:356`: construction or proof of vanishing of the
  non-scalar obstruction data is still required.
- `appendix-unreduced-bv-qme.tex:44`: scalar-reduced obstruction complex.
- `appendix-unreduced-bv-qme.tex:426`: scalar contact QME obstruction.
- `appendix-unreduced-bv-qme.tex:604`: balanced supertrace scalar
  cancellation.
- `appendix-unreduced-bv-qme.tex:666`: ordinary `gl_N` scalar obstruction
  criterion.
- `tate-P1-hadamard-mittag-leffler.tex:135`: Hadamard control on the
  Mittag-Leffler coefficient module.
- `tate-P1-hadamard-mittag-leffler.tex:300`: weighted QME lift reduced
  to the mixed brane-defect QME obstruction class.
- `tate-P1-hadamard-mittag-leffler.tex:335`: weighted RG locality
  criterion separating finite-window analytic control from QME
  vanishing.
- `tate-T4-bv-vanishing.tex:196`: endpoint obstruction tuple.
- `tate-T4-bv-vanishing.tex:225`: endpoint QME component.

## Files changed

- `tate-T1-weighted-completion.tex:931`: added the finite-window
  non-scalar QME tower.
- `tate-T1-weighted-completion.tex:980`: added the finite-window
  counterterm criterion.
- `tate-T1-weighted-completion.tex:1088`: added the boundary corollary
  saying finite-window machinery does not itself kill the non-scalar
  class.
- `reconstitution/swarm-2026-04-30-agent-094-finite-window-counterterms.md`:
  this report.

## Attack ledger

Severity 1 - false promotion from componentwise surface to non-scalar QME.
The componentwise theorem proves weighted kernels, scalar cancellation,
and reduced principal-part currents, but not acyclicity of
`H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})`. Heal:
the new theorem states an iff counterterm criterion; the corollary
forbids claiming automatic vanishing.

Severity 1 - compatible primitives may fail even after windowwise
exactness. Windowwise solutions `d_Mc_{n,M}=-\mathfrak o_{n,M}` need not
truncate compatibly. Heal: the criterion includes the Milnor
`\varprojlim^1 H^0` primitive-compatibility class `\lambda_n`.

Severity 2 - naive finite-window brackets can destroy the QME complex.
The finite-window truncation must use the transported acceptance-gate
bracket and interaction, not a raw projected Hamiltonian bracket. Heal:
the definition explicitly fixes transported finite-window structures.

Severity 2 - scalar cancellation does not control the non-scalar kernel.
Balanced `gl(N|N)` kills the scalar supertrace branch only. Heal: the
new complex is `\ker(\widehat\sigma_{\mathrm{sc},M})`, so the theorem
attacks the residual non-scalar class rather than reusing the scalar
argument.

Severity 3 - changing admissible weight might be mistaken for a
renormalization that removes the obstruction. Heal: the obstruction pair
is transported by `R^M_{w,w'}` and is weight-invariant.

Severity 3 - strict unweighted endpoint no-go is a different problem.
Heal: the corollary separates the non-scalar finite-window obstruction
from the strict product/direct-sum Tate endpoint obstruction.

## Remaining obligations

- Compute or prove the vanishing of
  `\mathfrak O^{\mathrm{ns}}_n` in the actual non-scalar graph complex.
- Construct the scalar-contact projection
  `\widehat\sigma_{\mathrm{sc},M}` as a chain map in the graph model,
  compatible with finite-window truncation and weight transport.
- Prove the `H^0` tower is Mittag-Leffler, or supply explicit primitive
  normalizations killing `\lambda_n`.
- Build the curved bulk-to-defect kernel needed for the full non-scalar
  Costello graph/QME realization.

## Verification commands

```bash
rg -n "quantum-coefficient-surface|non-scalar|A6b" main.tex open-obligations.tex
rg -n "scalar-contact|non-scalar|QME obstruction|balanced|supertrace|ordinary" appendix-unreduced-bv-qme.tex
rg -n "Hadamard|Mittag|finite-window|QME|obstruction|counterterm|window" tate-P1-hadamard-mittag-leffler.tex
rg -n "o_QME|QME|endpoint|obstruction|Costello--Li|Costello-Li" tate-T4-bv-vanishing.tex
rg -n "Finite-window non-scalar QME tower|Finite-window counterterm criterion|finite-window machinery does not by itself" tate-T1-weighted-completion.tex
chktex -q tate-T1-weighted-completion.tex
lacheck tate-T1-weighted-completion.tex
make pdf
rg -n "Undefined control sequence|Emergency stop|Fatal error|LaTeX Error|There were undefined references|Citation.*undefined|Reference.*undefined" out/main.log
git status --short -- tate-T1-weighted-completion.tex reconstitution/swarm-2026-04-30-agent-094-finite-window-counterterms.md out/main.pdf out/main.log
```

Results:

- `chktex` and `lacheck` report style warnings only, mostly pre-existing
  spacing/reference/dash warnings in `tate-T1-weighted-completion.tex`.
- `make pdf` completed and wrote `out/main.pdf` with 263 pages.
- The final log scan found no fatal LaTeX errors, undefined control
  sequences, undefined references, or undefined citations.
- Workspace note: `make pdf` modified tracked `out/main.pdf`; it now
  shows as `MM out/main.pdf`. I did not revert, reset, stash, or check
  out any path.
