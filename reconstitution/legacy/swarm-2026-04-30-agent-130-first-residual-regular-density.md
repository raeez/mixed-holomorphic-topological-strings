# Agent 130 - First Residual Regular-Density Decision

Status: patched owned theorem surface and report.  No commits or pushes.

## Stable core

The actual first non-scalar residual used by the manuscript is the
finite-window curvature coefficient

```tex
\mathfrak o^{\mathrm{ns}}_{n_0,M}
  =
  [\hbar^{n_0}]\left(
    \operatorname{Ob}^{\mathrm{red}}_{w,\partial,\hbar,M}
    +d_MC_{<n_0,M}
    +\frac12\{C_{<n_0,M},C_{<n_0,M}\}_{\hbar,M}
  \right)
  \in Z^1(\mathcal Q^\bullet_{w,M}(I)).
```

It lies in the saturated regular-density branch
`\mathcal Q^{\bullet,\mathrm{rd}}_{w,M}(I)
=\mathcal X^{\bullet,\mathrm{reg}}_{w,M}(I)` exactly when a compatible
regular-density residual certificate is supplied: scalar-zero
regular-density graph/counterterm expansion, equality with the curvature
coefficient in the local-functional complex, and compatibility with
finite-window truncation and admissible weight transport.

If that certificate exists, the representatives are explicit:

```tex
W_{n_0,M}=-\mathfrak o^{\mathrm{ns}}_{n_0,M},
\qquad
C_{n_0,M}=0.
```

Then

```tex
\eta^{\mathrm{reg}}_{n_0}
=\kappa^{\mathrm{reg}}_{n_0}
=\beta^{\mathrm{cl},\mathrm{reg}}_{n_0}
=\mu^{\mathrm{cl}}_{n_0}
=\lambda^{\mathrm{cl}}_{n_0}=0.
```

The current manuscript does not supply the finite-window coefficient
array of `\operatorname{Ob}^{\mathrm{red}}`, the lower counterterm array
`C_{<n_0,M}`, and the quotient reduction modulo
`\mathcal X^{\mathrm{reg}}`.  Therefore the saturated branch is not
proved for the actual residual.  The exact quotient obstruction is

```tex
\eta^{\mathrm{reg}}_{n_0,M}
  =
\left[
  q_M[\hbar^{n_0}]\left(
    \operatorname{Ob}^{\mathrm{red}}_{w,\partial,\hbar,M}
    +d_MC_{<n_0,M}
    +\frac12\{C_{<n_0,M},C_{<n_0,M}\}_{\hbar,M}
  \right)
\right]
\in
H^1(\mathcal Q^\bullet_{w,M}/
\mathcal X^{\bullet,\mathrm{reg}}_{w,M}).
```

If all finite-window quotient classes vanish, choose quotient primitives
`C_{n_0,M}` with

```tex
q_M(\mathfrak o^{\mathrm{ns}}_{n_0,M}+d_MC_{n_0,M})=0,
\qquad
x_{n_0,M}:=\mathfrak o^{\mathrm{ns}}_{n_0,M}+d_MC_{n_0,M}
\in Z^1(\mathcal X^{\bullet,\mathrm{reg}}_{w,M}),
\qquad
\alpha_M=[-x_{n_0,M}].
```

The remaining cohomology-lift obstruction is

```tex
\kappa^{\mathrm{reg}}_{n_0}
  =
\left[
  \bigl(
    \rho^{X,\mathrm{reg}}_{M+1,M}\alpha_{M+1}-\alpha_M
  \bigr)_M
\right]
\in
\varprojlim\nolimits^1_M\ker H^1(\Xi^{\mathrm{reg}}_M).
```

Only after this class vanishes does the regular-density branch have a
compatible cohomology lift; the Agent 111 secondary Roos classes
`\mu^{\mathrm{cl}}_{n_0}` and `\lambda^{\mathrm{cl}}_{n_0}` remain the
chain-level representative and primitive obligations outside the
saturated `W=-o`, `C=0` branch.

## Repaired label

- `prop:wt-actual-first-residual-regular-density-decision`

## Valid attacks

```yaml
- id: A1-130-01
  severity: 1
  status: healed
  lens: actual-residual identification
  target: tate-T1-weighted-completion.tex, first residual branch
  claim: The first residual after Agent 123 can remain an abstract
    \mathfrak o^{ns}_{n_0}.
  broken_step: The manuscript already defines it as the
    [\hbar^{n_0}] reduced curvature coefficient after lower-order
    counterterms.
  minimal_heal: Inscribe the formula and make all subsequent tests apply
    to that coefficient.

- id: A1-130-02
  severity: 1
  status: healed
  lens: saturated-branch overclosure
  target: Q^{rd}=X^{reg}
  claim: Agent 123's saturated case kills the actual residual.
  broken_step: The actual residual must first be proved to have a
    scalar-zero regular-density graph/counterterm representative.
  minimal_heal: Add the regular-density residual certificate and state
    W=-o, C=0 only under that certificate.

- id: A1-130-03
  severity: 1
  status: healed
  lens: quotient computation
  target: eta^{reg}_{n_0}
  claim: The quotient obstruction can be computed from the abstract
    closed-exchange criterion alone.
  broken_step: The quotient class requires the finite-window coefficient
    array of the reduced curvature, lower counterterms, scalar projection,
    and reduction modulo X^{reg}.
  minimal_heal: Inscribe the exact formula for eta and the exact data
    required to decide it.

- id: A1-130-04
  severity: 2
  status: healed
  lens: inverse-limit compatibility
  target: eta=0 branch
  claim: Vanishing quotient classes close the regular-density branch.
  broken_step: Windowwise lifts may fail to be compatible; the defect is
    the Roos class in lim^1 ker H^1(Xi^{reg}_M).
  minimal_heal: Define alpha_M from quotient primitives and inscribe
    kappa^{reg}_{n_0}.
```

## Verification

Commands run:

```bash
git diff --check -- tate-T1-weighted-completion.tex
rg -n -F "Actual first residual and the regular-density decision" tate-T1-weighted-completion.tex
rg -n -F "regular-density residual certificate" tate-T1-weighted-completion.tex
rg -n -F "W_{n_0,M}=-\\mathfrak o^{\\mathrm{ns}}_{n_0,M}" tate-T1-weighted-completion.tex
rg -n -F "\\kappa^{\\mathrm{reg}}_{n_0}" tate-T1-weighted-completion.tex
grep -n $'\\t' tate-T1-weighted-completion.tex
lacheck tate-T1-weighted-completion.tex
chktex -q tate-T1-weighted-completion.tex
```

Results:

- `git diff --check` passed.
- Label/content scans found the new proposition, the certificate, the
  explicit `W=-o` representative, and `\kappa^{reg}_{n_0}`.
- No tab characters remain in `tate-T1-weighted-completion.tex`.
- `lacheck` reports file-wide pre-existing style warnings; no local
  whitespace-before-punctuation warning remains in the inserted block.
- `chktex` reports file-wide nonfatal style warnings, including local
  formula-spacing warnings in the same style class as the surrounding
  Tate fragment.  No fatal syntax failure was detected by the targeted
  checks.
- `make pdf` was not run.  The shared checkout has concurrent staged
  manuscript edits, and the build writes `out/main.pdf`, outside this
  agent's writable surface.

## Files changed

- `tate-T1-weighted-completion.tex`
- `reconstitution/swarm-2026-04-30-agent-130-first-residual-regular-density.md`

## Remaining theorem obligations

- Supply the finite-window graph/coefficient array for
  `\operatorname{Ob}^{\mathrm{red}}_{w,\partial,\hbar,M}` and
  `C_{<n_0,M}`.
- Prove or refute the regular-density residual certificate for the actual
  curvature coefficient.
- If the certificate fails, compute
  `\eta^{\mathrm{reg}}_{n_0,M}` in
  `H^1(Q_M/X^{reg}_M)`.
- If `\eta^{reg}_{n_0}=0`, compute or kill
  `\kappa^{\mathrm{reg}}_{n_0}`.
- Outside the saturated branch, compute the representative and primitive
  Roos classes `\mu^{cl}_{n_0}` and `\lambda^{cl}_{n_0}`.

Agent 127's expected report path was named in the launch log, but the
file was not present on disk during this pass.
