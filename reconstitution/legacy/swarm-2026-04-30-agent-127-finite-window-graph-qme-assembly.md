# Agent 127 - Finite-Window Graph/QME Assembly

## Stable Core

The non-scalar Costello graph/QME statement is theorem-grade at a fixed
finite Hamiltonian window after five pieces of data are supplied:

```tex
\text{labels} + \text{regulator/counterterms}
+ \mathfrak Q^\bullet_{\mathcal G,M}(I)
+ \widehat\sigma_{\mathrm{sc},M}
+ \kappa^M_{\mathcal G,w,I}.
```

The repaired theorem is
`thm:finite-window-graph-qme-assembly` in
`tate-P1-hadamard-mittag-leffler.tex`.  It proves the finite-window
analytic graph layer and reduces the QME step to an exact scalar
obstruction followed by a non-scalar \(H^1\) obstruction.

The limit step is not automatic.  The repaired proposition is
`prop:finite-window-qme-limit-condition`; it gives the precise
inverse-limit obstruction vector and refuses all-graph summability unless
a separate graph-summability datum is supplied.

## Valid Attacks

```yaml
- id: A1-127-01
  severity: 1
  status: healed
  target: finite-window graph labels
  claim: The new regular-density and wavefront-admissible layers allow all
    compactly supported distributional labels.
  broken_step: Wavefront admissibility is graphwise and tuple-level; it is
    not a theorem for all of \(\mathcal D'_c(I)\).
  minimal_heal: The finite-window package accepts only regular-density
    tuples or tuples in \(\mathcal D'_{c,\mathrm{WF}}(I;\Gamma,M)\).  A
    linear CE source is allowed only when every finite tuple satisfies the
    relation.

- id: A1-127-02
  severity: 1
  status: healed
  target: finite-window QME conclusion
  claim: A finite-window renormalized graph kernel solves the non-scalar
    QME.
  broken_step: The analytic kernel does not kill scalar projection defects
    or the residual non-scalar \(H^1\) class.
  minimal_heal: Add the scalar obstruction
    \(\mathfrak s_{n,M}\) and the non-scalar class
    \([\mathfrak o^{\mathrm{fw}}_{n,M}]\).

- id: A1-127-03
  severity: 1
  status: healed
  target: scalar projection
  claim: The scalar projection exists on any graph/counterterm habitat.
  broken_step: It exists only on the balanced graph subhabitat or after
    the relative scalar-extension classes are killed.
  minimal_heal: Require the balanced subhabitat or vanishing of
    \(\delta^{(0)}_{\mathrm{Cost},\sigma}\) and
    \(\mathfrak o^{(r)}_{\mathrm{Cost},\sigma}\).

- id: A1-127-04
  severity: 1
  status: healed
  target: finite-window-to-limit passage
  claim: Windowwise exactness gives compatible inverse-limit counterterms.
  broken_step: Windowwise primitives may fail to truncate compatibly.
  minimal_heal: Add
    \(\lambda^{\mathrm{fw}}_n\in\varprojlim^1_MH^0\) represented by
    \([\pi_{M,N}c_{n,M}-c_{n,N}]\).

- id: A1-127-05
  severity: 2
  status: healed
  target: graph sums
  claim: A finite-window graph package implies all-graph summability.
  broken_step: The theorem fixes a finite graph package; no Cauchy or
    summability statement is proved for a graph-topology sum.
  minimal_heal: The limit proposition includes graph finiteness or a
    separate graph-summability datum as hypothesis (L2).
```

## Repaired Labels

- `defn:finite-window-graph-qme-package`
- `thm:finite-window-graph-qme-assembly`
- `prop:finite-window-qme-limit-condition`

## Exact Obstruction Formulas

Scalar obstruction:

```tex
\mathfrak s_{n,M}
=
[\hbar^n]\widehat\sigma_{\mathrm{sc},M}
\left(
  \operatorname{Ob}^{\mathrm{graph}}_{\mathcal G,M}
  +d_M C_{<n,M}
  +\frac12\{C_{<n,M},C_{<n,M}\}_{\hbar,M}
\right).
```

Finite-window non-scalar obstruction:

```tex
\mathfrak o^{\mathrm{fw}}_{n,M}
=
[\hbar^n]\left(
  \operatorname{Ob}^{\mathrm{graph}}_{\mathcal G,M}
  +d_M C_{<n,M}
  +\frac12\{C_{<n,M},C_{<n,M}\}_{\hbar,M}
\right),
\qquad
[\mathfrak o^{\mathrm{fw}}_{n,M}]
\in H^1(\mathcal Q^\bullet_{\mathcal G,M}(I),d_M).
```

Finite-window counterterms exist exactly when the scalar obstruction
vanishes and the displayed \(H^1\)-class is zero.

Inverse-limit obstruction:

```tex
\mathfrak O^{\mathrm{fw}}_n
=
\left(
  ([\mathfrak o^{\mathrm{fw}}_{n,M}])_M,
  \lambda^{\mathrm{fw}}_n
\right),
\qquad
\lambda^{\mathrm{fw}}_n\in
\varprojlim\nolimits^1_M
H^0(\mathcal Q^\bullet_{\mathcal G,M}(I)),
```

with \(\lambda^{\mathrm{fw}}_n\) represented by

```tex
[\pi_{M,N}c_{n,M}-c_{n,N}]
\in H^0(\mathcal Q^\bullet_{\mathcal G,N}(I)).
```

## Files Changed/Staged

- `tate-P1-hadamard-mittag-leffler.tex`
- `reconstitution/swarm-2026-04-30-agent-127-finite-window-graph-qme-assembly.md`

Both paths were staged after the scoped verification checks.

## Verification

Commands run:

```bash
git diff --check -- tate-P1-hadamard-mittag-leffler.tex
grep -n '[[:blank:]]$' tate-P1-hadamard-mittag-leffler.tex
lacheck tate-P1-hadamard-mittag-leffler.tex
chktex -q tate-P1-hadamard-mittag-leffler.tex
```

Results:

- `git diff --check` passed.
- trailing-whitespace grep returned no hits.
- `lacheck` reports only three pre-existing `~` suggestions at lines 39,
  218, and 221.
- `chktex` reports style warnings only, mainly existing reference,
  parenthesis, and dash warnings; no fatal TeX error was detected.
- No full `make pdf` was run because this shared checkout has concurrent
  staged manuscript edits and the build writes tracked output outside
  this agent's writable surface.

## Remaining Obligations

- Prove or compute the scalar projection on any graph/counterterm habitat
  larger than the balanced identity-loop subhabitat.
- Compute the first nonzero
  \([\mathfrak o^{\mathrm{fw}}_{n,M}]\) for the actual Hamiltonian
  graph package, or exhibit finite-window counterterms killing it.
- Prove the \(H^0\) tower is Mittag-Leffler, or compute
  \(\lambda^{\mathrm{fw}}_n\) directly.
- Supply an all-graph summability theorem before claiming any graph
  topology sum or all-order inverse-limit QME solution.
- No theorem for all of \(\mathcal D'_c(I)\) follows; outside the
  wavefront-admissible relation one needs additional renormalization data.
