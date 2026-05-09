# Agent 295: LQT Fixed-Rank to Stable Hopf Bridge Construction

Date: 2026-04-30

Worktree: `/Users/raeez/topological-strings`.

Owned write paths:

- `reconstitution/lqt-fixed-rank-to-stable-hopf-bridge-construction-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-295-lqt-fixed-rank-to-stable-hopf-bridge-construction.md`

Report-only.  No TeX, bibliography, script, source fixture, or PDF was
edited.

## Loaded Context

Read:

- `CLAUDE.md`
- `AGENTS.md`
- `/Users/raeez/ecosystem/INVARIANTS.md`
- `/Users/raeez/ecosystem/AGENTS-HARNESS.md`
- `.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `commands.tex`
- `mathmacros.tex`
- `notation.tex`
- `preamble.tex`
- `reconstitution/lqt-eulerian-theorem-proof-upgrade-2026-04-30.md`
- `reconstitution/lqt-eulerian-projection-integration-spec-2026-04-30.md`
- `reconstitution/chain-level-lqt-projection-construction-push-2026-04-30.md`
- `reconstitution/lqt-apsi-finite-window-construction-push-2026-04-30.md`
- `reconstitution/lqt-scalar-koszul-quotient-audit-2026-04-30.md`
- `references/primary-sources/lqt-tsygan-source-anchors-2026-04-30.md`

Checked manuscript and ledger anchors:

- `main.tex:1795-1895`
- `main.tex:4447-4478`
- `main.tex:5135-5200`
- `theorem-lanes.tex:2079-2105`
- `open-obligations.tex:143-172`
- `claim-strength-ledger.tex:392-411`
- `tate-T5-chain-level-primitive.tex:101-151`
- `tate-T5-chain-level-primitive.tex:188-365`
- `tate-T5-chain-level-primitive.tex:690-815`

The worktree was already dirty with many modified and added files from other
agents.  None were reverted or overwritten.

## Claim Attacked

Claim: once the stable Eulerian Hopf idempotent
\[
  P_{1\mathrm{cyc}}=\log^*(\mathrm{id})
\]
is accepted, there should be a theorem-grade bridge from finite-rank matrix
CE windows to that stable projection, with explicit stabilization maps and
error bounds.  The hostile reading is that this bridge might secretly be the
false same-rank deletion of multicycles.

## Result

The bridge exists only in the separated-block stable-range sense.

For a window \((K,L)\), let
\[
  B(K,L)=\max(K,L+2).
\]
Use blocks of size at least \(B(K,L)\).  If at most \(L\) connected Hopf
factors occur, rank
\[
  M=L B(K,L)
\]
is a uniform finite separated-block rank.  Define
\[
  \beta_{M,K,L}\colon \mathsf H^{\mathrm{st}}_{K,L}(A_\psi)
  \to C_*^{\mathrm{CE}}(\mathfrak{gl}_M(A_{\psi,K}))_{\le L}
\]
by placing each connected trace-cycle factor in its own diagonal block, and
define
\[
  \alpha_{M,K,L}
\]
by reading those separated blocks back as the stable block-sum Hopf word.
Then
\[
  P^{\mathrm{sep}}_{M,K,L}
  =
  \beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L}
\]
is a strict finite-rank chain idempotent on the separated-block subcomplex.

This is the theorem-grade fixed-rank replacement.  It is not same-rank
deletion.

## Exact Obstruction

Folding separated blocks into a single matrix block is not a CE chain map.
The defect is
\[
  \Gamma_N=d_{\mathrm{same}}F_N-F_Nd_{\oplus}.
\]
On two diagonal one-cycles,
\[
  \Gamma_N(\Theta_1^N(a)\wedge\Theta_1^N(b))
  =
  \pm\Theta_1^N(ab-(-1)^{|a||b|}ba).
\]
For \(a=x\), \(b=y\), this is \(\Theta_1^N(xy-yx)\).  This is the exact
stabilization obstruction to a same-rank deletion/homotopy statement.

A same-rank chain-homotopy bridge would have to construct \(H\) with
\[
  d_{\mathrm{same}}H+Hd_{\oplus}=-\Gamma_N
\]
over every finite window, with Koszul signs, scalar-Koszul quotient, trace
stabilizers, and Roos compatibility.  The first two-cycle term is healed by
\(\Theta_2(a,b)\), but the all-window partition-lattice collision homotopy is
not presently inscribed.  Therefore the same-rank homotopy bridge remains a
construction target, not a theorem.

## Error Bounds

Per occupied block, the stable-range error is zero for
\[
  n\ge\max(K,L+2).
\]
Below that range the exact rank error is
\[
  I_{n,K,L}
  =
  \ker\!\left(
    \mathsf H^{\mathrm{st}}_{K,L}(A_\psi)
    \to
    \mathsf H^{(n)}_{K,L}(A_\psi)
  \right),
\]
the finite-window part of the polarized fundamental trace-identity ideal,
together with the possible Loday--Quillen homological stabilization gap in
CE degrees \(i\ge n-1\).

If one additionally normalizes trace diagrams by \(N^{-r}\) for \(r\le L\)
matrix factors and chooses the matrix-unit coefficient \(\ell^1\)-norm, the
folding error lies in the positive collision filtration and has first bound
\[
  \frac{\binom{L}{2}}{N}.
\]
The \(q\)-collision part is \(O_L(N^{-q})\).  This is only an asymptotic
collision estimate; it does not make same-rank deletion a chain map.

## Files Written

The detailed construction and obstruction report was written to:

`reconstitution/lqt-fixed-rank-to-stable-hopf-bridge-construction-2026-04-30.md`

This agent summary was written to:

`reconstitution/swarm-2026-04-30-agent-295-lqt-fixed-rank-to-stable-hopf-bridge-construction.md`

## Checks Run

Eulerian coefficient check:

```text
eulerian_log_coeff n=1: 1
eulerian_log_coeff n=2: 0
eulerian_log_coeff n=3: 0
eulerian_log_coeff n=4: 0
eulerian_log_coeff n=5: 0
eulerian_log_coeff n=6: 0
eulerian_log_coeff n=7: 0
```

Collision check:

```text
N=2: collision differential of Theta1(a)^Theta1(b)
  E_00 ab: 1
  E_00 ba: -1
  E_11 ab: 1
  E_11 ba: -1
N=3: collision differential of Theta1(a)^Theta1(b)
  E_00 ab: 1
  E_00 ba: -1
  E_11 ab: 1
  E_11 ba: -1
  E_22 ab: 1
  E_22 ba: -1
N=4: collision differential of Theta1(a)^Theta1(b)
  E_00 ab: 1
  E_00 ba: -1
  E_11 ab: 1
  E_11 ba: -1
  E_22 ab: 1
  E_22 ba: -1
  E_33 ab: 1
  E_33 ba: -1
```

No PDF build was run because this was report-only and no TeX was edited.

## Claim-Status Recommendation

Mark the bridge as theorem-grade only in the separated-block stable finite
window.  Keep the same-rank chain-homotopy bridge open with obstruction
\(\Gamma_N\).  Do not replace \(\Gamma_N\) by a vague "finite-rank error":
the obstruction is the explicit cross-block collision coderivation, with
first component
\[
  \Theta_1^N(ab-(-1)^{|a||b|}ba).
\]
