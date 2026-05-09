# Agent 292 BMK Projected Finite-Window \(L_\infty\) Escape Operations

Owned files:

- `reconstitution/bmk-projected-finite-window-linfty-escape-operations-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-292-bmk-projected-finite-window-linfty-escape-operations.md`

No manuscript TeX was edited.  No PDF build was run.

## Claim Attacked

After the strict support-local finite BMK current quotient is obstructed,
construct the alternative projected finite-window \(L_\infty\) package, or
prove the exact next obstruction.  The first required escape operation is
\[
  \kappa_N(z_1^{N+2},\rho_{N+1,0})=-(N+2)\rho_{0,1}.
\]

## Finding

The escape operation exists as the return block of the full Matlis
coadjoint action.  It is not enough to define a finite \(L_\infty\) package.
Jacobi forces the escape-out map and the high-mode action as well.

Write
\[
  \mathcal P=\mathcal P_{\leq N}\oplus K_N,\qquad
  K_N=\bigoplus_{a+b>N}\C\rho_{a,b}.
\]
For the coadjoint action \(A_f\), use the block form
\[
  A_f=
  \begin{pmatrix}
    a_f & \kappa_f\\
    b_f & c_f
  \end{pmatrix}.
\]
Then \(a_f\) is the visible projected action, \(b_f\) sends finite modes out
of the window, \(\kappa_f\) sends escaped modes back into the window, and
\(c_f\) is the high-mode action.  The full representation identity
\([A_f,A_g]=A_{\{f,g\}}\) gives four block identities; the first is
\[
  [a_f,a_g]-a_{\{f,g\}}
    =
  -\kappa_fb_g+\kappa_gb_f.
\]
Thus the finite projected action fails Jacobi exactly by escape-return
terms.

## First Jacobi Test

The two decisive computations are
\[
  b_{z_2}(\rho_{N,0})=(N+1)\rho_{N+1,0},
\]
\[
  \kappa_{z_1^{N+2}}(\rho_{N+1,0})
    =-(N+2)\rho_{0,1}.
\]
Therefore, with \(f=z_1^{N+2}\), \(g=z_2\), and
\(\rho=\rho_{N,0}\),
\[
  a_fa_g\rho-a_ga_f\rho-a_{\{f,g\}}\rho
    =
  (N+1)(N+2)\rho_{0,1}\neq0.
\]
This is the first projected Jacobi obstruction.  The requested
\(\kappa_N\)-row accounts for it only after the escaped intermediate
\((N+1)\rho_{N+1,0}\) is retained as input data.

## Exact Next Obstruction

A finite semistrict \(L_\infty\) repair would need an
\(\ell_1\)-boundary whose boundary is the displayed Jacobiator.  Hence
\[
  \rho_{0,1}\in\operatorname{im}\ell_1.
\]
This contradicts the requirement that the retained Matlis finite moments
survive as the output of \(p_N\).

The problem is total, not local to \(\rho_{0,1}\).  For every
\(0<r+s\leq N\),
\[
  \kappa_{z_1^{N+1}z_2}(\rho_{N+r,s})
    =
  -\bigl((N+1)s-r\bigr)\rho_{r,s},
\]
and the coefficient is nonzero.  Thus
\[
  \operatorname{im}\kappa_N=\mathcal P_{\leq N}.
\]
Any \(L_\infty\) repair that absorbs all return maps as unary boundaries
makes every retained principal part exact.

The other escape strategy is to keep high-mode generators.  That is not
finite.  Since
\[
  c_{z_2}(\rho_{m,0})=(m+1)\rho_{m+1,0},
  \qquad m\geq N+1,
\]
any escape color containing the first forced mode \(\rho_{N+1,0}\) and
stable under the full Hamiltonian action contains an infinite tail.

## Factorization Attack

The split block package is compatible with the reduced interval-current
algebra after tensoring with \(\mathcal D'_c(I)\): coefficient maps commute
with extension by zero, and current multiplication by a test function is
associative.  This is only a split full-current ledger.

It is not a support-local finite quotient.  Killing \(K_N\) breaks Jacobi by
the first block identity.  Retaining \(K_N\) restores Jacobi but restores an
infinite high-mode color.  Treating \(\kappa_N\) as a boundary kills all of
\(\mathcal P_{\leq N}\) in cohomology.  The BMK collar and analytic moment
obstructions remain separate.

## Claim-Status Recommendation

- Proved: the first escape operation
  \(\kappa_N(z_1^{N+2},\rho_{N+1,0})=-(N+2)\rho_{0,1}\).
- Proved: the projected finite-window binary action has nonzero Jacobiator
  on \((z_1^{N+2},z_2,\rho_{N,0})\).
- Constructed: the TeX-ready split escape block
  \((a_N,b_N,\kappa_N,c_N)\) with four block identities.
- Obstructed: a genuinely finite \(L_\infty\) package preserving
  \(\mathcal P_{\leq N}\) as surviving finite moment classes.
- Remaining possible theorem target: an all-window/pro-Matlis BMK transfer
  or an explicitly infinite two-color current package retaining
  \(K_N\), with separate BMK collar, diagonal, and analytic-moment data.

## Files Read

- `CLAUDE.md`
- `AGENTS.md`
- `/Users/raeez/ecosystem/INVARIANTS.md`
- `/Users/raeez/ecosystem/AGENTS-HARNESS.md`
- `~/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `commands.tex`
- `mathmacros.tex`
- `notation.tex`
- `preamble.tex`
- `main.tex:1210-1555`
- `appendix-factorization-current-conventions.tex:1-220`, `360-820`
- `appendix-matlis-principal-parts.tex:150-230`
- `reconstitution/bmk-finite-current-quotient-construction-push-2026-04-30.md`
- `reconstitution/bmk-current-limit-obstruction-integration-spec-2026-04-30.md`
- `reconstitution/bmk-boundary-mode-obstruction-integration-spec-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-284-bmk-finite-current-quotient-construction-push.md`
- `reconstitution/swarm-2026-04-30-agent-286-bmk-boundary-mode-obstruction-integration-spec.md`

## Verification

Arithmetic check run:

```bash
python3 - <<'PY'
for N in range(1,8):
    def act(p,q,i,j):
        ii, jj = i - p + 1, j - q + 1
        if ii < 0 or jj < 0:
            return 0, None
        coeff = -(p*j - q*i + p - q)
        return coeff, (ii,jj)
    c1, t1 = act(0,1,N,0)
    c2, t2 = act(N+2,0,*t1)
    c3, t3 = act(N+1,0,N,0)
    assert c1 == N+1 and t1 == (N+1,0)
    assert c2 == -(N+2) and t2 == (0,1)
    assert c1*c2 == (N+2)*c3
PY
```

No PDF build is required for this report-only pass.
