# Agent 139 - Wavefront Counterterm Eta Kill

Status: patched owned Tate theorem surface and this report. No commits or
pushes.

## Stable Core

The non-regular wavefront branch does not enlarge
\(\mathcal X^{\bullet,\mathrm{reg}}\) by a canonical smoothing or
renormalized-density representative.

The reason is formal at the current-label level:
\[
  \mathcal S_c(I)=
  \mathcal D'_c(I)/\mathcal D^{\mathrm{reg}}_c(I).
\]
If \(B\notin\mathcal D^{\mathrm{reg}}_c(I)\) has non-empty wavefront,
then \([B]\neq0\in\mathcal S_c(I)\).  If a smooth density
\(B^{\mathrm{sm}}\) satisfied
\[
  B-B^{\mathrm{sm}}\in\mathcal D^{\mathrm{reg}}_c(I),
\]
then \(B\) would already be regular.  Thus smoothing cannot make a
singular current a regular-density generator modulo
\(\mathcal X^{\mathrm{reg}}\).

For the first wavefront residual the exact quotient component is
\[
\begin{aligned}
  \mathfrak s^{\mathrm{WF}}_{n_0,M}
    =
    q_M[\hbar^{n_0}]\Bigl(
      &\operatorname{Ob}^{\mathrm{red},\neg\mathrm{rd}}_{w,\partial,\hbar,M}
      +d_MC^{\neg\mathrm{rd}}_{<n_0,M} \\
      &+\{C^{\mathrm{reg}}_{<n_0,M},
           C^{\neg\mathrm{rd}}_{<n_0,M}\}_{\hbar,M}
      +\frac12
        \{C^{\neg\mathrm{rd}}_{<n_0,M},
           C^{\neg\mathrm{rd}}_{<n_0,M}\}_{\hbar,M}
    \Bigr)
    \in
    \mathcal C^{1,\mathrm{reg}}_{w,M}(I).
\end{aligned}
\]
The obstruction is
\[
  \eta^{\mathrm{reg}}_{n_0,M}
    =
  [\mathfrak s^{\mathrm{WF}}_{n_0,M}]
  \in
  H^1(\mathcal C^{\bullet,\mathrm{reg}}_{w,M}(I)).
\]

The branch is killed exactly when there is a degree-zero distributional
counterterm
\[
  C^{\mathrm{sing}}_{n_0,M}\in\mathcal Q^0_{w,M}(I)
\]
with
\[
  \bar d_Mq_M(C^{\mathrm{sing}}_{n_0,M})
    =
  -\mathfrak s^{\mathrm{WF}}_{n_0,M}.
\]
If no such primitive exists, then
\(\eta^{\mathrm{reg}}_{n_0,M}\neq0\).  The strongest true theorem is
therefore an obstruction theorem, not a smoothing theorem.

The zero-internal-edge test detects the obstruction on scalar-zero current
generators:
\[
  q_M\iota_I(\Theta^w_\rho(B))
    =
  [B]\otimes\rho
  \in
  \mathcal S_c(I)\widehat\otimes D_{w,\leq M}.
\]
Thus a non-smooth current with nonzero coefficient is already nonzero in
the regular-density quotient unless an ambient distributional primitive
appears.

## Repaired Labels

- `thm:wt-wavefront-singular-current-eta-obstruction`
- `eq:wt-wavefront-singular-component`

## Valid Attacks

```yaml
- id: A1-139-01
  severity: 1
  status: healed
  lens: singular-current quotient
  target: non-regular branch after prop:wt-regular-density-curvature-certificate
  claim: A wavefront-admissible singular label can be canonically smoothed
    into the regular-density branch.
  broken_step: The quotient
    D'_c(I)/D^{reg}_c(I) is nonzero, and a non-smooth distribution cannot
    differ from a smooth density by a smooth density.
  evidence_type: proof
  evidence_ref: thm:wt-wavefront-singular-current-eta-obstruction
  minimal_heal: Add the singular-current quotient and rule out canonical
    smoothing at the current-label level.
  residual: A separate wavefront-labelled closed-exchange complex could be
    built, but it is not X^{reg}.

- id: A1-139-02
  severity: 1
  status: healed
  lens: primitive type
  target: proof of prop:wt-regular-density-curvature-certificate
  claim: A non-regular quotient component can be killed by a regular-density
    primitive.
  broken_step: A regular-density primitive maps to zero under q_M, so it
    cannot cancel a nonzero singular quotient component.
  evidence_type: proof_gap
  evidence_ref: tate-T1-weighted-completion.tex, corrected proof paragraph
  minimal_heal: Replace the claim by a degree-zero primitive in the ambient
    distributional quotient complex.
  residual: Existence of such a primitive remains a genuine finite-window
    H^1 computation.

- id: A1-139-03
  severity: 1
  status: healed
  lens: exact eta component
  target: eta^{reg}_{n0,M}
  claim: The wavefront branch can remain an unnamed obstruction.
  broken_step: The exact non-regular summands are the non-regular graph
    curvature, d_M of non-regular lower counterterms, the mixed bracket
    with regular counterterms, and the non-regular quadratic bracket.
  evidence_type: formula
  evidence_ref: eq:wt-wavefront-singular-component
  minimal_heal: Name
    s^{WF}_{n0,M} and set eta^{reg}_{n0,M}=[s^{WF}_{n0,M}].
  residual: The actual numerical graph coefficient array is still needed
    to decide whether s^{WF}_{n0,M} is a boundary.

- id: A1-139-04
  severity: 2
  status: healed
  lens: wavefront support
  target: distributional counterterms
  claim: Wavefront-admissible counterterms have no additional quotient
    datum once the graph product exists.
  broken_step: The extension ambiguity is supported on graph collision
    diagonals meeting supp(B_Gamma) and remains distributional unless the
    singular current coefficient vanishes.
  evidence_type: line_reference
  evidence_ref: prop:app-wavefront-admissible-costello-graph-kernel and
    thm:wt-wavefront-singular-current-eta-obstruction
  minimal_heal: Record the wavefront/support containment for
    s^{WF}_{n0,M}.
  residual: Concrete support coefficients must be supplied by the finite
    graph table.
```

## Verification

Commands run:

```bash
git diff --check -- tate-T1-weighted-completion.tex
grep -n '[[:blank:]]$' tate-T1-weighted-completion.tex
grep -n $'\t' tate-T1-weighted-completion.tex
rg -n -F "regular-density primitive" tate-T1-weighted-completion.tex
rg -n -F "thm:wt-wavefront-singular-current-eta-obstruction" tate-T1-weighted-completion.tex
rg -n -F "\\tag{\\ast}" tate-T1-weighted-completion.tex
lacheck tate-T1-weighted-completion.tex
chktex -q tate-T1-weighted-completion.tex
```

Results:

- `git diff --check` passed for the TeX patch.
- trailing-whitespace and tab scans returned no hits.
- the obsolete phrase `regular-density primitive` returned no hits.
- label and tag scans found the inserted theorem and component formula.
- `lacheck` reports file-wide pre-existing style warnings; after the local
  `eqref` repair it reports no new warning on the inserted theorem block.
- `chktex` reports file-wide nonfatal style warnings, including local
  formula-style warnings of the same class as the surrounding Tate fragment.
- Full `make pdf` was not run; this shared checkout has concurrent staged
  manuscript edits and the build writes tracked output outside this
  agent's writable surface.

## Files Changed/Staged

- `tate-T1-weighted-completion.tex`
- `reconstitution/swarm-2026-04-30-agent-139-wavefront-counterterm-eta-kill.md`

## Remaining Theorem Obligations

- Supply the actual finite-window graph coefficient array for the
  wavefront branch.
- Compute whether
  \(\mathfrak s^{\mathrm{WF}}_{n_0,M}\) is
  \(\bar d_M\)-exact in
  \(\mathcal Q^\bullet_{w,M}/\mathcal X^{\bullet,\mathrm{reg}}_{w,M}\).
- If it is exact, construct compatible primitives
  \(C^{\mathrm{sing}}_{n_0,M}\) and then compute
  \(\kappa^{\mathrm{reg}}_{n_0}\).
- If it is not exact, keep
  \(\eta^{\mathrm{reg}}_{n_0,M}\neq0\) as the obstruction to the
  regular-density closed-exchange branch.
