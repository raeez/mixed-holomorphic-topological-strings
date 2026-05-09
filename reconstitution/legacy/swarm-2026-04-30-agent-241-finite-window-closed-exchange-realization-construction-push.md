# Agent 241 - Finite-Window Closed-Exchange Realization Construction Push

Status: report-only.  Owned files:

- `reconstitution/finite-window-closed-exchange-realization-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-241-finite-window-closed-exchange-realization-construction-push.md`

No TeX, script, bibliography, or figure file was edited.

## Stable Core

The ordinary scalar-reduced \(\mathfrak{gl}_N\) branch has scalar QME class
\[
  [\operatorname{Ob}_{\mathrm{sc}}]
    =
  \hbar N[\bar c],
  \qquad
  \bar c(f,g)=[\{f,g\}]_0,
  \qquad
  \bar c(z_1,z_2)=1.
\]
The class is nonzero on \(\bar A=\C[z_1,z_2]/\C\cdot1\).  A same-branch
closed-exchange repair must supply a class whose scalar image is
\(-\hbar N[\bar c]\), plus a finite-window scalar-contact gate, cochain
maps, compatible cocycles, counterterms, and zero Roos classes.

The construction push found a formal algebraic cone:
\[
  \mathcal X^{1,\mathrm{alg}}_{\mathrm{sc},w,M}(I)
  =\C[[\hbar]]e_M,\qquad d^X_Me_M=0,
\]
\[
  \Xi^{\mathrm{alg},\mathrm{sc}}_M(e_M)
  =
  -\hbar N\,\bar c_M(f,g)
  \int_Ia(t)b(t)\gamma_{\mathbf 1}(t)\,dt.
\]
With \(W_M=e_M\), \(C_M=0\), and \(\rho^X_{M,N}(e_M)=e_N\), it gives
\[
  \beta^{\mathrm{sc}}_M
  =
  \beta^{\mathrm{sc}}_{\mathrm{cl}}
  =
  \mu^{\mathrm{sc}}_{\mathrm{cl}}
  =
  \lambda^{\mathrm{sc}}_{C}
  =
  0
\]
inside the adjoined defect-supported central-contact extension.

This does not prove the genuine Costello-local closed-exchange branch.
For the original ordinary branch, the scalar-contact projection gate is
already obstructed by
\[
  o_{\sigma,M}^{(1),\mathrm{sc}}=\hbar N[\bar c_M]\neq0,
\]
and if a gate is assumed externally, the exact next obstruction is
\[
  \beta^{\mathrm{sc}}_M
  =
  [\hbar N[\bar c_M]]
  \in
  \operatorname{coker}
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{sc}}_M).
\]
For the currently constructed genuine towers, the scalar image needed to
hit \(-\hbar N[\bar c_M]\) is absent; hence the ordinary branch remains
obstructed.

## Attack Ledger

```yaml
- id: A1-241-01
  severity: 1
  status: healed
  lens: scalar source class
  target: ordinary scalar-reduced gl_N QME branch
  claim: Naming an opposite class is already a closed-exchange repair.
  broken_step: The target requires a finite-window complex X_sc,w,M, cochain maps Xi_M^sc, scalar-contact chain projection, W_M, C_M, and Roos-compatible inverse-system data.
  evidence_type: line_reference
  evidence_ref: reconstitution/scalar-qme-closed-exchange-construction-target-2026-04-30.md:62-265; main.tex:7606-7624
  files_read:
    - reconstitution/scalar-qme-closed-exchange-construction-target-2026-04-30.md
    - main.tex
    - appendix-unreduced-bv-qme.tex
  tools_used: [rg, nl, sed]
  confidence: high
  blast_radius: false closure of the scalar QME branch
  minimal_heal: write the finite-window branch equations and obstruction sequence
  residual: construct a genuine Costello-local source for the opposite class
  deciding_evidence: accepted Xi_M^sc with scalar image -hbar N[bar c_M] and zero Roos classes

- id: A1-241-02
  severity: 1
  status: valid
  lens: scalar-contact projection gate
  target: widehat sigma_sc,M in the ordinary branch
  claim: The ordinary scalar-symbol extractor can be used as a chain projection.
  broken_step: The manuscript proves the first chain-defect class is hbar N[bar c], nonzero on (z1,z2).
  evidence_type: line_reference
  evidence_ref: appendix-unreduced-bv-qme.tex:236-305; local-dictionary.tex:840-874
  files_read:
    - appendix-unreduced-bv-qme.tex
    - local-dictionary.tex
  tools_used: [rg, nl, sed]
  confidence: high
  blast_radius: non-scalar complex ker widehat sigma_sc is formed before the gate exists
  minimal_heal: make o_sigma,M^(1),sc the first obstruction before beta_M^sc
  residual: kill the scalar-lift tower by additional data with leading class -hbar N[bar c]
  deciding_evidence: filtered chain projection commuting with d_M and finite-window transport

- id: A1-241-03
  severity: 1
  status: valid
  lens: algebraic cone audit
  target: minimal one-dimensional X_alg construction
  claim: The cone X_alg with Xi(e)=-Ob_sc is a genuine Costello closed exchange.
  broken_step: The cone adjoins the negative contact generator directly; it supplies no closed propagator, source-face computation, wavefront extension, local counterterm support, RG compatibility, or graph table.
  evidence_type: proof_gap
  evidence_ref: main.tex:7441-7510; appendix-unreduced-bv-qme.tex:2142-2232; tate-T1-weighted-completion.tex:1526-1548
  files_read:
    - main.tex
    - appendix-unreduced-bv-qme.tex
    - tate-T1-weighted-completion.tex
  tools_used: [rg, nl, sed]
  confidence: high
  blast_radius: turns an obstruction into a tautological added generator
  minimal_heal: classify the cone as a defect-supported central-contact extension, not as a proved Costello-local closed exchange
  residual: construct the actual closed source line and bulk-to-defect map from Costello-local data
  deciding_evidence: finite-window closed field, propagator/locality rules, source faces, and d_K Xi=0

- id: A1-241-04
  severity: 1
  status: healed
  lens: finite-window image criterion
  target: beta_M^sc
  claim: Any closed-exchange tower, including the regular-density non-scalar tower, can cancel the scalar class.
  broken_step: The fixed-window equation requires -hbar N[bar c_M] in the image of H^1(widehat sigma_sc,M Xi_M^sc). Scalar-zero regular-density towers have zero scalar image.
  evidence_type: line_reference
  evidence_ref: reconstitution/swarm-2026-04-30-agent-118-construct-X-Xi-closed-exchange.md:8-53; reconstitution/scalar-qme-closed-exchange-construction-target-2026-04-30.md:156-200
  files_read:
    - reconstitution/swarm-2026-04-30-agent-118-construct-X-Xi-closed-exchange.md
    - reconstitution/scalar-qme-closed-exchange-construction-target-2026-04-30.md
  tools_used: [rg, nl, sed]
  confidence: high
  blast_radius: imports a non-scalar construction into the scalar branch
  minimal_heal: define beta_M^sc as the cokernel of H^1(widehat sigma Xi)
  residual: compute or construct an admissible scalar-image class
  deciding_evidence: explicit W_M with H^1(widehat sigma Xi)[W_M] = -hbar N[bar c_M]

- id: A1-241-05
  severity: 1
  status: healed
  lens: inverse-system compatibility
  target: beta_cl^sc, mu_cl^sc, lambda_C^sc
  claim: Windowwise W_M and C_M automatically give an inverse-limit repair.
  broken_step: Cohomology lifts, cocycle representatives, and counterterm primitives carry independent Roos compatibility classes.
  evidence_type: line_reference
  evidence_ref: tate-T1-weighted-completion.tex:1576-1735; reconstitution/scalar-qme-closed-exchange-construction-target-2026-04-30.md:204-265
  files_read:
    - tate-T1-weighted-completion.tex
    - reconstitution/scalar-qme-closed-exchange-construction-target-2026-04-30.md
  tools_used: [rg, nl, sed]
  confidence: high
  blast_radius: false all-window QME closure
  minimal_heal: record beta_cl^sc first, then mu_cl^sc and lambda_C^sc with Roos representatives
  residual: prove H^0 Mittag-Leffler for X and Q, or compute the Roos classes directly
  deciding_evidence: compatible W_M and C_M or zero Roos classes
```

## Healed Construction Package

The scalar finite-window equations are:
\[
  \widehat\sigma_{\mathrm{sc},M}d_M
  =
  d_{\mathrm{CE}}\widehat\sigma_{\mathrm{sc},M},
\]
\[
  \widehat\sigma_{\mathrm{sc},M}(\operatorname{Ob}_{\mathrm{sc},M})
  =
  \hbar N\bar c_M,
\]
\[
  \widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{sc}}_M(W_M)
  =
  -\hbar N\bar c_M+d_{\mathrm{CE}}\eta_M,
\]
\[
  \operatorname{Ob}_{\mathrm{sc},M}
    +\Xi^{\mathrm{sc}}_M(W_M)+d_MC_M=0.
\]
The map \(\Xi_M^{\mathrm{sc}}\) must obey
\[
  \pi_{M,N}\Xi^{\mathrm{sc}}_M
  =
  \Xi^{\mathrm{sc}}_N\rho^X_{M,N},
\]
and the weight transports must commute with both sides.

The algebraic cone satisfies these equations after adjoining a central
defect-supported source line:
\[
  W_M=e_M,\qquad C_M=0,\qquad
  \rho^X_{M,N}e_M=e_N.
\]
This gives a precise construction target for a stronger theorem: replace the
formal generator \(e_M\) by a Costello-local closed field and prove the same
equations from the closed-source differential, bulk-to-defect restriction,
and local counterterm calculus.

## Exact Obstruction Surface

Without that replacement, the ordinary scalar-reduced branch is obstructed.
The first obstruction is the scalar-contact gate:
\[
  o_{\sigma,M}^{(1),\mathrm{sc}}
  =
  \hbar N[\bar c_M]\neq0.
\]

If a gate is externally supplied, the fixed-window obstruction is
\[
  \beta^{\mathrm{sc}}_M
  =
  [\hbar N[\bar c_M]]
  \in
  \operatorname{coker}
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{sc}}_M).
\]

The inverse-limit obstruction is
\[
  \beta^{\mathrm{sc}}_{\mathrm{cl}}
  =
  \left[(\hbar N[\bar c_M])_M\right]
  \in
  \operatorname{coker}\!\left(
    \varprojlim_M H^1(\mathcal X^\bullet_{\mathrm{sc},w,M}(I))
    \to
    \varprojlim_M H^1(\mathcal S^\bullet_M(I))
  \right),
\]
where the arrow is \(\varprojlim H^1(\widehat\sigma_{\mathrm{sc},M}
\Xi^{\mathrm{sc}}_M)\).

After a cohomology lift \(\alpha\) is chosen, the representative Roos class is
\[
  \mu^{\mathrm{sc}}_{\mathrm{cl}}(\alpha)
  \in
  \varprojlim\nolimits^1_M
  H^0(\mathcal X^\bullet_{\mathrm{sc},w,M}(I)),
\]
represented by
\[
  \rho^X_{M+1,M}w_{M+1}-w_M=d^X_Mu_M.
\]

After compatible \(W_M\) are chosen, the counterterm Roos class is
\[
  \lambda^{\mathrm{sc}}_{C}(W)
  \in
  \varprojlim\nolimits^1_M
  H^0(\mathfrak Q^\bullet_{\mathrm{sc},w,M}(I)),
\]
represented by
\[
  [\pi_{M+1,M}c_{M+1}-c_M],
  \qquad
  d_Mc_M=-(\operatorname{Ob}_{\mathrm{sc},M}
      +\Xi^{\mathrm{sc}}_M(W_M)).
\]

The current genuine branch fails before \(\mu\) and \(\lambda_C\): the
scalar image needed to make \(\beta^{\mathrm{sc}}_M\) vanish has not been
constructed.

## Verification

Read:

- `CLAUDE.md`
- `AGENTS.md`
- `~/ecosystem/INVARIANTS.md`
- `~/ecosystem/AGENTS-HARNESS.md`
- `~/ecosystem/.agents/skills/attack-heal-swarm/SKILL.md`
- `~/ecosystem/.agents/skills/attack-heal-swarm/references/protocol.md`
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `main.tex`
- `open-obligations.tex`
- `claim-strength-ledger.tex`
- `appendix-unreduced-bv-qme.tex`
- `local-dictionary.tex`
- `mathmacros.tex`
- `commands.tex`
- `reconstitution/scalar-qme-closed-exchange-construction-target-2026-04-30.md`
- prior reports 100, 104, 111, 118, and 232

Commands run:

```bash
rg -n "scalar|closed-exchange|closed exchange|opposite class|beta|mu|lambda|Xi|QME|counterterm|Roos|finite-window|scalar-contact" \
  main.tex open-obligations.tex claim-strength-ledger.tex appendix-unreduced-bv-qme.tex local-dictionary.tex

rg -n "X\\^|Xi\\^|closed-exchange|scalar-contact|beta\\^|mu\\^|lambda\\^|regular-density|finite-window" \
  reconstitution/swarm-2026-04-30-agent-1*.md reconstitution/swarm-2026-04-30-agent-2*.md \
  reconstitution/*closed-exchange*.md reconstitution/*scalar-qme*.md

PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from itertools import product
def bracket(x,y):
    a,b=x; c,d=y
    coeff=a*d-b*c
    exp=(a+c-1,b+d-1)
    if coeff==0 or exp[0]<0 or exp[1]<0:
        return []
    if exp==(0,0):
        return []
    return [(coeff,exp)]
def omega(x,y):
    a,b=x; c,d=y
    return (a*d-b*c) if (a+c,b+d)==(1,1) else 0
monos=[(a,b) for a in range(5) for b in range(5) if (a,b)!=(0,0)]
fail=[]
for x,y,z in product(monos, repeat=3):
    s=0
    for coeff,e in bracket(x,y): s += coeff*omega(e,z)
    for coeff,e in bracket(y,z): s += coeff*omega(e,x)
    for coeff,e in bracket(z,x): s += coeff*omega(e,y)
    if s!=0:
        fail.append((x,y,z,s)); break
print('CE cocycle failures through bidegree<5:', len(fail))
print('omega(z1,z2)=', omega((1,0),(0,1)))
print('If eta descends to bar A then d eta(z1,z2)= -eta(0)=0, so omega non-exact on the quotient.')
PY

git diff --cached --check -- \
  reconstitution/finite-window-closed-exchange-realization-construction-push-2026-04-30.md \
  reconstitution/swarm-2026-04-30-agent-241-finite-window-closed-exchange-realization-construction-push.md
```

Observed computation:

```text
CE cocycle failures through bidegree<5: 0
omega(z1,z2)= 1
If eta descends to bar A then d eta(z1,z2)= -eta(0)=0, so omega non-exact on the quotient.
```

No build was run.  The task is report-only, and the shared checkout already
contains concurrent TeX and PDF changes outside this agent's ownership.
