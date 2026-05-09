# Agent 111 closed-exchange ML tower report

## Stable core

The closed-exchange branch is a homological-algebra criterion, not a
vanishing theorem.  It requires a tower of complexes and cochain maps
```tex
\rho^X_{M,N}\colon
\mathcal X^\bullet_{w,M}(I)\to\mathcal X^\bullet_{w,N}(I),
\qquad
\Xi_M\colon
\mathcal X^\bullet_{w,M}(I)\to\mathcal Q^\bullet_{w,M}(I),
\qquad
\pi_{M,N}\Xi_M=\Xi_N\rho^X_{M,N}.
```

For a fixed window the branch equation
```tex
\mathfrak o^{\mathrm{ns}}_{n,M}
  +\Xi_M(W_{n,M})+d_M C_{n,M}=0
```
has a solution exactly when
```tex
[\mathfrak o^{\mathrm{ns}}_{n,M}]
  \in
  -\,\operatorname{im}\!\left(
    H^1(\Xi_M)\colon
    H^1(\mathcal X^\bullet_{w,M}(I))
    \to H^1(\mathcal Q^\bullet_{w,M}(I))
  \right).
```

In the finite-window inverse limit the first obstruction is
```tex
\beta^{\mathrm{cl}}_n
  =
  \left[\bigl([\mathfrak o^{\mathrm{ns}}_{n,M}]\bigr)_M\right]
  \in
  \operatorname{coker}\!\left(
    \varprojlim_M H^1(\mathcal X^\bullet_{w,M}(I))
    \xrightarrow{\ \varprojlim H^1(\Xi_M)\ }
    \varprojlim_M H^1(\mathcal Q^\bullet_{w,M}(I))
  \right).
```

After a lift
`\alpha\in\varprojlim_M H^1(\mathcal X^\bullet_{w,M}(I))`
with `H^1(\Xi_M)\alpha_M=-[\mathfrak o^{ns}_{n,M}]` is chosen, the
representative compatibility class is
```tex
\mu^{\mathrm{cl}}_n(\alpha)
  \in
  \varprojlim\nolimits^1_M H^0(\mathcal X^\bullet_{w,M}(I)).
```
It is represented by choosing cocycles `w_M` and cochains `u_M` with
```tex
\rho^X_{M+1,M}w_{M+1}-w_M=d^X_M u_M,
```
then taking the Roos class of `([u_M])_M`.

After compatible `W_{n,M}` are chosen, the counterterm compatibility
class is
```tex
\lambda^{\mathrm{cl}}_n(W)
  \in
  \varprojlim\nolimits^1_M H^0(\mathcal Q^\bullet_{w,M}(I)).
```
It is represented by choosing primitives
`d_M c_M=-(\mathfrak o^{ns}_{n,M}+\Xi_M(W_{n,M}))` and taking the Roos
class of
```tex
[\pi_{M+1,M}c_{M+1}-c_M].
```

If the `H^0(\mathcal X)` tower is Mittag-Leffler, then
`\mu^{cl}_n=0`.  If the `H^0(\mathcal Q)` tower is Mittag-Leffler, then
`\lambda^{cl}_n=0`.  Under both hypotheses, only
`\beta^{cl}_n` remains.  The counterterm-only theorem is the special
case `\mathcal X^\bullet=0`.

## Attack ledger

```yaml
- id: A1-111-01
  severity: 1
  status: healed
  lens: theorem-grade promotion
  target: open-obligations.tex:380-464; reconstitution/swarm-2026-04-30-agent-104-external-counterterm-branch.md
  claim: The closed-exchange branch was sufficiently typed by the ledger statement.
  broken_step: The ledger named beta, mu, and lambda but did not inscribe the fixed-window equivalence, the Roos representatives, or the proof in a theorem surface.
  evidence_type: proof_gap
  evidence_ref: tate-T1-weighted-completion.tex:1088
  files_read:
    - tate-T1-weighted-completion.tex
    - open-obligations.tex
    - appendix-unreduced-bv-qme.tex
    - appendix-factorization-current-conventions.tex
    - reconstitution/swarm-2026-04-30-agent-094-finite-window-counterterms.md
    - reconstitution/swarm-2026-04-30-agent-104-external-counterterm-branch.md
  tools_used: [rg, nl, sed]
  confidence: high
  blast_radius: without a theorem, the branch can be cited as if it were constructed rather than criterion-controlled
  minimal_heal: add theorem thm:wt-closed-exchange-counterterm-criterion with proof
  residual: construct the actual closed-exchange tower and cochain maps
  deciding_evidence: a Costello-local closed-exchange tower with compatible Xi_M

- id: A1-111-02
  severity: 1
  status: healed
  lens: fixed-window cohomology
  target: branch equation
  claim: A closed-exchange term can be inserted without an image criterion.
  broken_step: The equation is solvable at window M exactly when the non-scalar class lies in the negative image of H^1(Xi_M).
  evidence_type: proof_gap
  evidence_ref: tate-T1-weighted-completion.tex:1119-1136
  files_read: [tate-T1-weighted-completion.tex, open-obligations.tex]
  tools_used: [nl, sed]
  confidence: high
  blast_radius: arbitrary external terms could masquerade as QME repairs
  minimal_heal: prove the fixed-window iff criterion
  residual: compute H^1(Xi_M) for the actual closed-exchange complex
  deciding_evidence: explicit image calculation or a class W_M mapping to -[o_M]

- id: A1-111-03
  severity: 1
  status: healed
  lens: inverse-limit obstruction
  target: beta^{cl}, mu^{cl}, lambda^{cl}
  claim: Vanishing of the coker H^1 class alone gives chain-level compatible W and C.
  broken_step: Compatible cohomology classes still require representative and primitive compatibility in the Roos complex.
  evidence_type: proof_gap
  evidence_ref: tate-T1-weighted-completion.tex:1138-1228
  files_read: [tate-T1-weighted-completion.tex, reconstitution/swarm-2026-04-30-agent-104-external-counterterm-branch.md]
  tools_used: [nl, sed]
  confidence: high
  blast_radius: false closure of the branch in the inverse limit
  minimal_heal: define beta^{cl}, mu^{cl}, lambda^{cl} with representative formulas
  residual: prove or compute vanishing of these classes for the constructed tower
  deciding_evidence: zero Roos classes or Mittag-Leffler H^0 towers

- id: A1-111-04
  severity: 2
  status: healed
  lens: quantifier hygiene
  target: Agent 104 triple criterion
  claim: The triple vanishes without specifying the chosen lift alpha and representative W.
  broken_step: mu is attached to a lift alpha of the coker equation; lambda is attached after compatible W representatives are chosen.
  evidence_type: unsupported
  evidence_ref: tate-T1-weighted-completion.tex:1157-1228
  files_read: [tate-T1-weighted-completion.tex, theorem-lanes.tex, open-obligations.tex]
  tools_used: [nl, sed]
  confidence: high
  blast_radius: different lifts can carry different secondary Roos data
  minimal_heal: state existence of a lift alpha with mu=0 and then W with lambda=0
  residual: classify possible lifts only after X and Xi are built
  deciding_evidence: full H^1 and H^0 tower computation

- id: A1-111-05
  severity: 2
  status: healed
  lens: ML precision
  target: stronger hypotheses
  claim: A generic finite-window ML slogan kills all secondary obstructions.
  broken_step: The precise sufficient hypotheses are Mittag-Leffler for the H^0(X) and H^0(Q) cohomology towers; they kill mu and lambda respectively by vanishing of lim^1.
  evidence_type: proof_gap
  evidence_ref: tate-T1-weighted-completion.tex:1229-1243
  files_read: [tate-T1-weighted-completion.tex, tate-P1-hadamard-mittag-leffler.tex]
  tools_used: [rg, nl, sed]
  confidence: high
  blast_radius: would hide a real primitive-compatibility obstruction
  minimal_heal: state the two H^0 ML hypotheses separately
  residual: prove these H^0 towers are ML in the actual graph-current habitat
  deciding_evidence: eventual image stabilization or explicit surjectivity on H^0 towers
```

## Repairs made

- Added `thm:wt-closed-exchange-counterterm-criterion` to
  `tate-T1-weighted-completion.tex`.
- The theorem gives the fixed-window iff criterion, the inverse-limit
  coker class `\beta^{cl}_n`, the representative class
  `\mu^{cl}_n`, the counterterm class `\lambda^{cl}_n`, the ML
  sufficient hypotheses, the weight-transport statement, and the
  counterterm-only specialization.

## Verification

Commands run:

```bash
rg -n -F "Closed-exchange plus counterterm criterion" tate-T1-weighted-completion.tex
rg -n -F "\operatorname{coker}" tate-T1-weighted-completion.tex
rg -n -F "\varprojlim\nolimits^1_M" tate-T1-weighted-completion.tex
lacheck tate-T1-weighted-completion.tex
chktex -q tate-T1-weighted-completion.tex
git diff --check -- tate-T1-weighted-completion.tex
```

Results:

- `git diff --check` passed.
- `lacheck` reports only pre-existing style warnings outside the new
  theorem block.
- `chktex` reports pre-existing file-wide style warnings and harmless
  local warnings about labels/dashes; no fatal TeX syntax failure was
  detected.
- `make pdf` was not run because this shared checkout already has
  concurrent tracked changes and `out/main.pdf` is outside the assigned
  writable surface.

## Residual theorem obligations

- Construct the closed-exchange complexes
  `\mathcal X^\bullet_{w,M}(I)` from actual closed propagator,
  bulk-to-defect restriction, wavefront/locality rules, and Costello
  counterterm support.
- Prove the maps `\Xi_M` are cochain maps compatible with truncation and
  admissible weight transport.
- Compute whether `\beta^{cl}_n` vanishes for the first non-scalar
  residual.
- Prove the `H^0(\mathcal X)` and `H^0(\mathcal Q)` towers are
  Mittag-Leffler, or compute the Roos classes `\mu^{cl}_n` and
  `\lambda^{cl}_n` directly.
- Finish the analytic distributional-kernel theorem: H\"ormander
  wavefront transversality, extension across small diagonals, support on
  brane-collision strata, RG preservation, and finite-window
  compatibility.
