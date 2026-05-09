# Agent 286 BMK Boundary-Mode Obstruction Integration Spec

Owned files:

- `reconstitution/bmk-boundary-mode-obstruction-integration-spec-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-286-bmk-boundary-mode-obstruction-integration-spec.md`

No manuscript TeX was edited.  No build was run.

## Claim Attacked

The attacked claim is the finite-window BMK current transfer assertion in
`main.tex:1242-1452` and
`appendix-factorization-current-conventions.tex:399-695`, especially the
identities
\[
  \bar\partial H_{\chi,N}+H_{\chi,N}\bar\partial
  =
  \operatorname{id}-i_Np_N+E_{\chi,N},
  \qquad
  \bar\partial H_{\mathrm{BM},N}
  +H_{\mathrm{BM},N}\bar\partial
  =
  \operatorname{id}-i_Np_N.
\]

The current manuscript still treats the finite-window transfer as a proved
strict support-local current/factorization identity.  That is false.

## Finding

The strongest true theorem surface found in this pass is:

1. a one-pair derived analytic quotient construction, conditional on a full
   analytic BMK contraction and a fixed diagonal orientation convention;
2. an unconditional strict support-local finite-current quotient obstruction
   theorem for \(N\geq1\);
3. the arity-two Hamiltonian/Matlis formula retained only as an output
   projection \(p_N[ix,iy]\), not as the binary term of a strict
   finite-current transfer.

The obstruction theorem is stronger than the previous current-limit ledger
because it does not merely say that \(H_{\chi,N}\) has not been built.  It
proves that the natural support-local relation is not stable under the full
Hamiltonian action.

## Boundary-Mode Calculation

The Matlis appendix proves
\[
  z_1^p z_2^q\cdot\rho_{i,j}
  =
  -(pj-qi+p-q)\rho_{i-p+1,j-q+1}.
\]
Taking \(p=N+2\), \(q=0\), \(i=N+1\), \(j=0\) gives
\[
  z_1^{N+2}\cdot\rho_{N+1,0}
  =
  -((N+2)0-0(N+1)+N+2)\rho_{0,1}
  =
  -(N+2)\rho_{0,1}.
\]
The source \(\rho_{N+1,0}\) is killed by every finite window
\(\mathcal P_{\leq N}\), while \(\rho_{0,1}\) is retained for every
\(N\geq1\).  Therefore the killed relation is not an
\(\mathfrak h\)-submodule relation.

The scalar line gives the same warning in the unreduced ambient local
cohomology module:
\[
  z_1\cdot\rho_{0,0}=-\rho_{0,1}.
\]
This is why scalar removal must be part of the reduced Hamiltonian
cotangent convention, not an ordinary support-local quotient relation in
the unreduced current module.

## Obstruction Components

The recommended finite-window obstruction vector is
\[
  \operatorname{Ob}^{\mathrm{BMK\mbox{-}bdry}}_N
  =
  \left(
    \operatorname{ob}_{\mathrm{diag}},
    \operatorname{ob}_{\mathrm{an}/\mathrm{fin},N},
    \operatorname{ob}_{\partial,N},
    \operatorname{ob}_{\mathrm{collar\mbox{-}fact},N}
  \right).
\]

- \(\operatorname{ob}_{\mathrm{diag}}\): annular diagonal sign/scalar.  The
  current local calculation from Agent 284 gives angular mass \(-1\) for
  the displayed kernel with real outward orientation.
- \(\operatorname{ob}_{\mathrm{an}/\mathrm{fin},N}\): the gap between the
  full analytic moment kernel
  \(K_N=\ker(\mathcal O(B_1)^\vee\to\mathcal P_{\leq N})\) and the smaller
  support-at-zero high-derivative span.
- \(\operatorname{ob}_{\partial,N}\): the Hamiltonian leakage
  \(\pi_N(\mathfrak h\cdot K_N^0)\), nonzero by
  \(z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1}\).
- \(\operatorname{ob}_{\mathrm{collar\mbox{-}fact},N}\): lack of a
  factorization ideal compatible with extension by zero, disjoint products,
  and \(H_\chi\).

## One-Pair Derived Analytic Quotient

Assume a single-pair analytic BMK contraction
\[
  \bar\partial H_\chi^0+H_\chi^0\bar\partial
  =
  \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}},
  \qquad
  H_\chi^0I_{\mathrm{an}}=0
\]
on the collar quotient \(C^\bullet(B_2,B_1)\).  Let
\[
  \pi_N:\mathcal O(B_1)^\vee\to\mathcal P_{\leq N},
  \qquad
  K_N=\ker\pi_N.
\]
Then the homotopy descends to
\[
  C_N^{\mathrm{der}}(B_2,B_1)
  =
  \operatorname{cofib}\!\left(
    I_{\mathrm{an}}K_N\to C^\bullet(B_2,B_1)
  \right)
\]
where \(K_N\) is placed in the top Dolbeault degree represented by closed
currents, and satisfies
\[
  \bar\partial\overline H_{\chi,N}
  +\overline H_{\chi,N}\bar\partial
  =
  \operatorname{id}-i_Np_N.
\]

This quotient is not support-local and not native factorization data.  It
kills all analytic classes with zero selected finite moments, not merely the
support-at-zero high derivative currents.

## TeX Replacement Blocks

TeX-ready replacement blocks are written in
`reconstitution/bmk-boundary-mode-obstruction-integration-spec-2026-04-30.md`.
They cover:

- the proposition title at `main.tex:1242`;
- the false identity block at `main.tex:1333-1349`;
- the arity-two/all-window conclusion at `main.tex:1351-1419`;
- the proof at `main.tex:1422-1452`;
- the appendix theorem title and replacement regions at
  `appendix-factorization-current-conventions.tex:399`, `482-614`, and
  `630-695`.

## Claim-Status Recommendation

- Proved: boundary-mode obstruction to a strict support-local finite-current
  quotient for \(N\geq1\).
- Proved as output calculation: arity-two Hamiltonian bracket and Matlis
  coadjoint formula after finite projection.
- Conditional construction: one-pair derived analytic quotient after the
  analytic BMK contraction and diagonal orientation convention are supplied.
- False: finite-window normalized BMK identity on the full current complex
  or on a strict support-local finite-current factorization quotient.
- Next theorem target: all-window/pro-Matlis transfer, or a projected
  finite-window \(L_\infty\) package whose first escaped operation is
  \(\kappa_N(z_1^{N+2},\rho_{N+1,0})=-(N+2)\rho_{0,1}\).

## Files Read

- `CLAUDE.md`
- `AGENTS.md`
- `/Users/raeez/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `/Users/raeez/ecosystem/INVARIANTS.md`
- `/Users/raeez/ecosystem/AGENTS-HARNESS.md`
- `reconstitution/bmk-current-limit-obstruction-integration-spec-2026-04-30.md`
- `reconstitution/bmk-finite-current-quotient-construction-push-2026-04-30.md`
- `main.tex:1235-1465`
- `appendix-factorization-current-conventions.tex:320-700`
- `appendix-matlis-principal-parts.tex:1-280`
- `references/primary-sources/bmk-koppelman-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-268-bmk-koppelman-source-fixture.md`

## Commands Run

```bash
sed -n '1,220p' /Users/raeez/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,260p' CLAUDE.md
sed -n '1,260p' AGENTS.md
sed -n '1,240p' reconstitution/bmk-current-limit-obstruction-integration-spec-2026-04-30.md
sed -n '1,520p' reconstitution/bmk-finite-current-quotient-construction-push-2026-04-30.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
rg -n "§IV|Voice|Russian|Self-reflection|VIII|Correctness|Rigor|Attribution|Standalone" /Users/raeez/ecosystem/INVARIANTS.md /Users/raeez/ecosystem/AGENTS-HARNESS.md
sed -n '1200,1525p' main.tex
sed -n '360,720p' appendix-factorization-current-conventions.tex
git status --short
nl -ba main.tex | sed -n '1235,1465p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '395,700p'
rg -n "principal-part|coadjoint|rho_\\{i,j\\}|z_1\\^p|p-q|Matlis|boundary|finite-window|BMK|finite window" appendix-matlis-principal-parts.tex appendix-factorization-current-conventions.tex main.tex theorem-lanes.tex claim-strength-ledger.tex open-obligations.tex
nl -ba appendix-matlis-principal-parts.tex | sed -n '1,280p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '320,390p'
sed -n '1,260p' references/primary-sources/bmk-koppelman-source-anchors-2026-04-30.md
sed -n '1,280p' reconstitution/swarm-2026-04-30-agent-268-bmk-koppelman-source-fixture.md
```

Suggested arithmetic verification before integration:

```bash
python3 - <<'PY'
for N in [1, 2, 5, 12]:
    p, q, i, j = N + 2, 0, N + 1, 0
    coeff = -(p*j - q*i + p - q)
    target = (i - p + 1, j - q + 1)
    assert coeff == -(N + 2)
    assert target == (0, 1)
print("boundary-mode check passed")
PY
```

## Files Changed

- Added `reconstitution/bmk-boundary-mode-obstruction-integration-spec-2026-04-30.md`.
- Added `reconstitution/swarm-2026-04-30-agent-286-bmk-boundary-mode-obstruction-integration-spec.md`.

No other file should be staged by this agent.
