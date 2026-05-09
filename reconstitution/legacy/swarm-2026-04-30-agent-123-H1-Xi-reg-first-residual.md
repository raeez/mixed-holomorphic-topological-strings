# Agent 123 - H1 Xi-reg First Residual

Status: regular-density \(H^1(\Xi^{\mathrm{reg}})\) image criterion
computed as a quotient obstruction; no commits or pushes.

## Stable core

The new proposition is
`prop:wt-Xi-reg-first-residual-quotient-obstruction` in
`tate-T1-weighted-completion.tex`.

For the inclusion
\[
  \Xi^{\mathrm{reg}}_M\colon
  \mathcal X^{\bullet,\mathrm{reg}}_{w,M}(I)
  \hookrightarrow
  \mathcal Q^\bullet_{w,M}(I),
\]
the exact fixed-window quotient complex is
\[
  \mathcal C^{\bullet,\mathrm{reg}}_{w,M}(I)
    =
  \mathcal Q^\bullet_{w,M}(I)/
  \mathcal X^{\bullet,\mathrm{reg}}_{w,M}(I).
\]
For the first non-scalar residual
\[
  \mathfrak o^{\mathrm{ns}}_{n_0,M}
    \in Z^1(\mathcal Q^\bullet_{w,M}(I)),
\]
the finite-window obstruction is
\[
  \eta^{\mathrm{reg}}_{n_0,M}
    =
  [q_M(\mathfrak o^{\mathrm{ns}}_{n_0,M})]
    \in
  H^1(\mathcal C^{\bullet,\mathrm{reg}}_{w,M}(I)).
\]
Exactness of
\[
  0\to\mathcal X^{\bullet,\mathrm{reg}}
    \to\mathcal Q^\bullet
    \to\mathcal C^{\bullet,\mathrm{reg}}\to0
\]
gives
\[
  [\mathfrak o^{\mathrm{ns}}_{n_0,M}]
  \in-\operatorname{im}H^1(\Xi^{\mathrm{reg}}_M)
  \Longleftrightarrow
  \eta^{\mathrm{reg}}_{n_0,M}=0.
\]

In the inverse limit, the quotient shadow is
\[
  \eta^{\mathrm{reg}}_{n_0}
    =
  (\eta^{\mathrm{reg}}_{n_0,M})_M
  \in
  \varprojlim_MH^1(\mathcal C^{\bullet,\mathrm{reg}}_{w,M}(I)).
\]
It is the image of the regular-density closed-exchange cokernel class
\[
  \beta^{\mathrm{cl},\mathrm{reg}}_{n_0}.
\]
Thus \(\eta^{\mathrm{reg}}_{n_0}\neq0\) proves
\(\beta^{\mathrm{cl},\mathrm{reg}}_{n_0}\neq0\).  If
\(\eta^{\mathrm{reg}}_{n_0}=0\), the remaining cohomology-lift
compatibility obstruction is
\[
  \kappa^{\mathrm{reg}}_{n_0}
  \in
  \varprojlim\nolimits^1_M
  \ker H^1(\Xi^{\mathrm{reg}}_M),
\]
represented by the Roos differences of windowwise preimages
\(\alpha_M\).  The exact inverse-limit criterion is
\[
  \beta^{\mathrm{cl},\mathrm{reg}}_{n_0}=0
  \Longleftrightarrow
  \eta^{\mathrm{reg}}_{n_0}=0
  \text{ and }
  \kappa^{\mathrm{reg}}_{n_0}=0.
\]

If the branch is restricted to a complete regular-density subhabitat
\[
  \mathcal Q^{\bullet,\mathrm{rd}}_{w,M}(I)
  =
  \mathcal X^{\bullet,\mathrm{reg}}_{w,M}(I)
\]
and the residual lies in that subhabitat, then the inclusion is the
identity.  The compatible choice
\[
  W_{n_0,M}=-\mathfrak o^{\mathrm{ns}}_{n_0,M},
  \qquad
  C_{n_0,M}=0
\]
kills the residual.  For this canonical branch,
\[
  \beta^{\mathrm{cl},\mathrm{reg}}_{n_0}=0,\qquad
  \mu^{\mathrm{cl}}_{n_0}=0,\qquad
  \lambda^{\mathrm{cl}}_{n_0}=0.
\]

## Attack ledger

```yaml
- id: A1-123-01
  severity: 1
  status: healed
  lens: supremum discipline
  target: tate-T1-weighted-completion.tex, H^1(Xi^reg) criterion
  claim: It is enough to restate the abstract image condition for Xi^reg.
  broken_step: Xi^reg is an inclusion of a subcomplex, so the stronger fixed-window statement is the quotient class in H^1(Q/X^reg).
  evidence_type: proof_gap
  evidence_ref: prop:wt-regular-density-X-Xi-construction; prop:wt-Xi-reg-first-residual-quotient-obstruction
  files_read:
    - tate-T1-weighted-completion.tex
    - appendix-factorization-current-conventions.tex
    - reconstitution/swarm-2026-04-30-agent-111-closed-exchange-ml-tower.md
    - reconstitution/swarm-2026-04-30-agent-116-regular-density-graph-kernel.md
    - reconstitution/swarm-2026-04-30-agent-118-construct-X-Xi-closed-exchange.md
  tools_used: [sed, rg]
  confidence: high
  blast_radius: Would leave the branch abstract even after Agent 118 constructed Xi^reg as an inclusion.
  minimal_heal: Define C^reg=Q/X^reg and prove the fixed-window iff criterion.
  residual: Compute the actual quotient class for the supplied first residual.
  deciding_evidence: A representative showing q_M(o_{n0,M}) is exact, or a nonzero class in H^1(C^reg_M).

- id: A1-123-02
  severity: 1
  status: healed
  lens: inverse-limit compatibility
  target: beta^{cl,reg}_{n0}
  claim: Vanishing of all finite-window quotient classes automatically gives beta^{cl,reg}_{n0}=0.
  broken_step: Windowwise preimages in H^1(X^reg_M) need not be compatible; the defect lies in lim^1 ker H^1(Xi^reg_M).
  evidence_type: proof_gap
  evidence_ref: prop:wt-Xi-reg-first-residual-quotient-obstruction
  files_read:
    - tate-T1-weighted-completion.tex
    - reconstitution/swarm-2026-04-30-agent-111-closed-exchange-ml-tower.md
  tools_used: [sed, rg]
  confidence: high
  blast_radius: Would falsely kill the inverse-limit closed-exchange obstruction.
  minimal_heal: Add kappa^{reg}_{n0} in lim^1 K_M and prove beta=0 iff eta=0 and kappa=0.
  residual: Prove the relevant K_M tower is Mittag-Leffler or compute the Roos class.
  deciding_evidence: Compatible cohomology lifts alpha_M, or a nonzero Roos class.

- id: A1-123-03
  severity: 1
  status: healed
  lens: overclosure
  target: regular-density saturated case
  claim: The construction proves X^reg=Q in the full non-scalar tower.
  broken_step: Q still contains the ambient non-scalar counterterm habitat; Agent 118 constructed only the regular-density graph-generated subcomplex.
  evidence_type: line_reference
  evidence_ref: defn:wt-regular-density-closed-exchange-complex; prop:app-regular-density-costello-graph-kernel
  files_read:
    - tate-T1-weighted-completion.tex
    - appendix-factorization-current-conventions.tex
    - reconstitution/swarm-2026-04-30-agent-118-construct-X-Xi-closed-exchange.md
  tools_used: [sed, rg]
  confidence: high
  blast_radius: Would claim beta=0 for residuals outside the proved regular-density habitat.
  minimal_heal: State beta=mu=lambda=0 only on a specified subhabitat Q^rd=X^reg with the residual inside it.
  residual: Prove the actual first residual lies in Q^rd, or use the quotient obstruction outside it.
  deciding_evidence: Scalar-zero regular-density graph/counterterm representative for o_{n0,M}.

- id: A1-123-04
  severity: 2
  status: healed
  lens: secondary obstruction accounting
  target: mu^{cl}, lambda^{cl}
  claim: Once beta vanishes in the saturated case, the secondary classes need no representative-level check.
  broken_step: Agent 111's theorem requires compatible cocycle and primitive choices; these must be exhibited.
  evidence_type: proof_gap
  evidence_ref: thm:wt-closed-exchange-counterterm-criterion; prop:wt-Xi-reg-first-residual-quotient-obstruction
  files_read:
    - tate-T1-weighted-completion.tex
    - reconstitution/swarm-2026-04-30-agent-111-closed-exchange-ml-tower.md
  tools_used: [sed, rg]
  confidence: high
  blast_radius: Would leave mu/lambda unaccounted even where X^reg=Q^rd.
  minimal_heal: Choose W=-o and C=0; then both Roos difference systems are zero.
  residual: None in the saturated regular-density branch for this canonical representative.
  deciding_evidence: The displayed compatible W and zero primitive.
```

## Repairs made

- Added `prop:wt-Xi-reg-first-residual-quotient-obstruction`.
- Defined the quotient complex
  \(\mathcal C^{\bullet,\mathrm{reg}}_{w,M}(I)\).
- Proved the fixed-window equivalence
  \([o]\in-\operatorname{im}H^1(\Xi^{\mathrm{reg}}_M)\)
  iff \([q_M(o)]=0\).
- Defined the inverse-limit quotient shadow
  \(\eta^{\mathrm{reg}}_{n_0}\) and the residual Roos lift obstruction
  \(\kappa^{\mathrm{reg}}_{n_0}\).
- Proved the saturated regular-density case:
  if \(Q^{\mathrm{rd}}=X^{\mathrm{reg}}\) and
  \(o_{n_0}\in Q^{\mathrm{rd}}\), then
  \(\beta^{cl}=\mu^{cl}=\lambda^{cl}=0\) for
  \(W=-o\), \(C=0\).

## Verification

Commands run:

```bash
git diff --check -- tate-T1-weighted-completion.tex
rg -n -F "Regular-density quotient obstruction for the first residual" tate-T1-weighted-completion.tex
rg -n -F "eta^{\\mathrm{reg}}_{n_0}" tate-T1-weighted-completion.tex
rg -n -F "kappa^{\\mathrm{reg}}_{n_0}" tate-T1-weighted-completion.tex
lacheck tate-T1-weighted-completion.tex
chktex -q tate-T1-weighted-completion.tex
git add tate-T1-weighted-completion.tex reconstitution/swarm-2026-04-30-agent-123-H1-Xi-reg-first-residual.md
git diff -- tate-T1-weighted-completion.tex reconstitution/swarm-2026-04-30-agent-123-H1-Xi-reg-first-residual.md
git diff --cached --check -- tate-T1-weighted-completion.tex reconstitution/swarm-2026-04-30-agent-123-H1-Xi-reg-first-residual.md
git diff --cached --name-status -- tate-T1-weighted-completion.tex reconstitution/swarm-2026-04-30-agent-123-H1-Xi-reg-first-residual.md
git status --short -- tate-T1-weighted-completion.tex reconstitution/swarm-2026-04-30-agent-123-H1-Xi-reg-first-residual.md
```

Results:

- `git diff --check` passed.
- The label/content scans found the new proposition and the two quotient
  obstruction symbols.
- `lacheck` reports pre-existing file-wide style warnings; after local
  punctuation cleanup, no whitespace-before-punctuation warning remains in
  the inserted proposition.
- `chktex` reports file-wide nonfatal style warnings, including local
  warnings in the same style class as the surrounding Tate fragment.  No
  fatal syntax failure was detected by the targeted checks.
- After staging, the unstaged diff for the two owned paths is empty;
  `git diff --cached --check` passes; scoped cached name-status lists
  exactly `tate-T1-weighted-completion.tex` and this report.
- `make pdf` was not run.  The shared checkout has concurrent staged
  manuscript edits, and the build writes `out/main.pdf`, outside this
  agent's writable surface.

## Residual theorem obligations

- Decide whether the actual first non-scalar residual
  \(\mathfrak o^{\mathrm{ns}}_{n_0,M}\) lies in the regular-density
  generated subhabitat \(Q^{\mathrm{rd}}=X^{\mathrm{reg}}\).  If yes,
  the branch is killed by \(W=-o\), \(C=0\).
- If not, compute
  \(\eta^{\mathrm{reg}}_{n_0,M}\in H^1(Q_M/X^{reg}_M)\) for the concrete
  residual representative.
- If all finite-window quotient classes vanish, compute or kill
  \(\kappa^{\mathrm{reg}}_{n_0}\in\varprojlim^1\ker H^1(\Xi^{reg}_M)\).
- After a compatible cohomology lift is chosen outside the saturated
  case, compute the Agent 111 secondary classes
  \(\mu^{cl}_{n_0}\) and \(\lambda^{cl}_{n_0}\), or prove the relevant
  \(H^0\) towers are Mittag-Leffler.
