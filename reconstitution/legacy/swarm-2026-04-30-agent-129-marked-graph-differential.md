# Agent 129 - Marked Graph Differential

Status: patched owned appendix surface; no commits or pushes.

## Stable Core

The marked boundary/counterterm differential can be made theorem-grade as
an oriented finite-window complex.  A generator is
\[
  X_{\Gamma,o,\mathfrak m,M},
\]
where \(o=\beta_1\wedge\cdots\wedge\beta_s\) orients the elementary
codimension-one \(d_{\mathrm{QME}}\)-boundary operations and
\(\mathfrak m\) assigns full \(\mathfrak{gl}(N|N)\)-equivariant marker
tensors to scalar open loops.

The signed differential is
\[
  d_{\mathrm{mk}}X_{\Gamma,o,\mathfrak m,M}
    =
  \sum_i(-1)^{i-1}
    X_{\partial_{\beta_i}\Gamma,\;o/\beta_i,\;
      \mu_{\beta_i}(\mathfrak m),\;M}.
\]
The scalar-contact filtration is
\[
  p(\Gamma,\mathfrak m)=
  \#\{\text{scalar-contact open loops in }\Gamma\},\qquad
  r(\beta_i)=p(\Gamma,\mathfrak m)-
  p(\partial_{\beta_i}\Gamma,\mu_{\beta_i}(\mathfrak m)).
\]
The first filtration-lowering boundary is the sum over
\(r(\beta_i)=r\).  The incidence signs square to zero by the usual
codimension-two cancellation.

For the full-equivariant marker habitat,
\[
  \mathcal M_m^{\mathrm{full}}(V)
  =
  \operatorname{Span}\{\mathfrak C_\sigma:\sigma\in S_m\}
  \subset
  (\operatorname{End}(V)^{\otimes m})^{\mathfrak{gl}(V)},
\]
where \(\mathfrak C_\sigma\) is the signed super Brauer permutation
tensor.  Its cyclic supertrace is
\[
  \operatorname{Str}_{\mathrm{cyc}}(\mathfrak C_\sigma)
  =
  (\operatorname{sdim}V)^{c(\tau_m^{-1}\sigma)}.
\]
For \(V=\mathbb C^{N|N}\), this is zero for every nonempty marker tensor,
and the empty word also has coefficient
\(\operatorname{Str}(\operatorname{id}_V)=0\).  Hence the full-equivariant
marked \([\bar c]\)-shadow vanishes.

For the smaller even block-diagonal habitat, a single fixed marker is
\[
  T=\lambda_0P_{\bar0}+\lambda_1P_{\bar1},
\]
and its obstruction class is exactly
\[
  \hbar N(\lambda_0-\lambda_1)[\bar c]\,\gamma_{\mathbf 1}.
\]
It vanishes if and only if \(\lambda_0=\lambda_1\).  The non-equivariant
one-line \(P_+\) marker was not used.

## Attack Ledger

```yaml
- id: A1-129-01
  severity: 1
  status: healed
  lens: missing signed differential
  target: appendix-unreduced-bv-qme.tex, marked graph/counterterm branch
  claim: The marked obstruction can be evaluated from Agent 124's placeholder datum alone.
  broken_step: A theorem-grade calculation needs an oriented finite-window boundary complex, incidence signs, marker transport maps, and scalar-contact filtration order.
  evidence_type: proof_gap
  evidence_ref: def:app-oriented-full-equivariant-marked-boundary-complex and lem:app-oriented-marked-incidence-signs
  minimal_heal: Construct d_mk with signs (-1)^{i-1}, define r(beta), and prove d_mk^2=0 under codimension-two closure.
  residual: A concrete Costello specialization must still supply its finite graph list and boundary operations.

- id: A1-129-02
  severity: 1
  status: healed
  lens: full super-gauge equivariance
  target: invariant marker tensors
  claim: Full equivariant invariant marker tensors may still carry a nonzero [cbar] scalar shadow.
  broken_step: The admissible full-equivariant signed permutation tensors close into cyclic supertrace loops, each contributing sdim(C^{N|N})=0.
  evidence_type: direct_computation
  evidence_ref: lem:app-full-equivariant-cyclic-supertrace
  minimal_heal: Compute Str_cyc(C_sigma)=(sdim V)^{c(tau^{-1}sigma)} and prove full-equivariant marked scalar-shadow vanishing.
  residual: None inside the full-equivariant Brauer-generated marker habitat.

- id: A1-129-03
  severity: 1
  status: healed
  lens: smaller gauge habitat
  target: even block-diagonal markers
  claim: The P_+ one-line projection is an admissible test after merely weakening to the even block-diagonal group.
  broken_step: The even block-diagonal commutant admits parity block projections P_0 and P_1, not a projection onto one chosen even basis line.
  evidence_type: direct_computation
  evidence_ref: prop:app-even-block-marker-obstruction
  minimal_heal: Compute the honest even-block obstruction hbar N(lambda0-lambda1)[cbar] gamma_1.
  residual: Higher external marker tensors remain governed by the supertraceless-monodromy criterion.
```

## Repairs Made

Added to `appendix-unreduced-bv-qme.tex`:

- `def:app-oriented-full-equivariant-marked-boundary-complex`;
- `lem:app-oriented-marked-incidence-signs`;
- `lem:app-full-equivariant-cyclic-supertrace`;
- `thm:app-full-equivariant-marked-shadow-vanishing`;
- `prop:app-even-block-marker-obstruction`.

Also adjusted Agent 124's marked-datum proposition so larger marked
specializations point to the new oriented marked boundary complex rather
than remaining as an unspecified placeholder.

## Verification

Commands run:

```bash
sed -n '1,240p' CLAUDE.md
sed -n '1,220p' AGENTS.md
sed -n '1,240p' /Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,260p' appendix-unreduced-bv-qme.tex
sed -n '261,620p' appendix-unreduced-bv-qme.tex
sed -n '621,1040p' appendix-unreduced-bv-qme.tex
sed -n '1041,1420p' appendix-unreduced-bv-qme.tex
sed -n '1421,1800p' appendix-unreduced-bv-qme.tex
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-103-balanced-scalar-projection.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-110-balanced-graph-extension.md
sed -n '1,300p' reconstitution/swarm-2026-04-30-agent-115-first-nonidentity-loop-symbol.md
sed -n '1,320p' reconstitution/swarm-2026-04-30-agent-119-supertraceless-monodromy-subhabitat.md
sed -n '1,360p' reconstitution/swarm-2026-04-30-agent-124-Bst0-marked-differential.md
git diff --check -- appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-129-marked-graph-differential.md
chktex -q appendix-unreduced-bv-qme.tex
git diff --cached --check -- appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-129-marked-graph-differential.md
git status --short -- appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-129-marked-graph-differential.md
python3 - <<'PY'
from itertools import permutations
def cycles(p):
    n=len(p); seen=[False]*n; c=0
    for i in range(n):
        if not seen[i]:
            c+=1; j=i
            while not seen[j]:
                seen[j]=True; j=p[j]
    return c
for m in range(1,5):
    tau=tuple(list(range(1,m))+[0])
    tau_inv=[0]*m
    for i,t in enumerate(tau): tau_inv[t]=i
    print(m, sorted({cycles(tuple(tau_inv[sig[i]] for i in range(m)))
                     for sig in permutations(range(m))}))
PY
```

`git diff --check` and `git diff --cached --check` passed.  `chktex`
returned the existing appendix style-warning class and warnings on the
new displayed formulas; it reported no fatal TeX error.  The Python check
confirms the cyclic composition always has at least one supertrace loop
for \(m\geq1\).  No full `make pdf` was run because the shared checkout
contains concurrent staged changes and the build writes tracked artifacts
outside this agent's owned paths.

## Remaining Obligations

The full-equivariant marked scalar shadow is killed on the constructed
habitat.  What remains outside this agent's scope is a concrete Costello
finite-window graph list with its boundary operations, plus any genuinely
non-scalar class in the kernel of the zero scalar projection.  If the
principal chooses the even block-diagonal or external-marker habitat, the
remaining scalar obstruction is exactly the displayed
\(\operatorname{Str}_{\mathrm{cyc}}\)-weighted \([\bar c]\)-class and must
be killed by explicit closed-exchange or counterterm data.
