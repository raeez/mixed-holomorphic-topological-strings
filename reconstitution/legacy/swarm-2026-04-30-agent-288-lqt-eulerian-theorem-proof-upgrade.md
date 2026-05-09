# Agent 288 Report: LQT Eulerian Theorem Proof Upgrade

Date: 2026-04-30

Worktree: `/Users/raeez/topological-strings`.

Owned write surface:

- `reconstitution/lqt-eulerian-theorem-proof-upgrade-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-288-lqt-eulerian-theorem-proof-upgrade.md`

Report-only.  No TeX, bibliography, script, or PDF was edited.

## Claim Attacked

The attacked surface is the Loday--Quillen--Tsygan Eulerian projection lane:

- `main.tex:1764-1785`, especially the paragraph after the external LQT
  theorem.
- `theorem-lanes.tex:2079-2105`, the K3 finite-window LQT item containing
  \(\lambda_{\mathrm{LQT},W}\).
- `open-obligations.tex:143-172`, the finite-window dg LQT obligation.
- `claim-strength-ledger.tex:392-411`, the LQT component of the open
  \(A_\infty\) ledger.
- `main.tex:5058-5062`, the connected single-trace extraction operation.

The risk was that \(P_{1\mathrm{cyc}}\) could be read as same-rank deletion
of multicycles.  That reading is false.

## Verdict

The stable finite-window LQT projection is proved in the stable block-sum
Hopf CE complex.

For a Koszul-weight bound \(K\) and CE-length bound \(L\),
\[
  A_{\psi,K}=A_\psi/F^{>K}A_\psi,
  \qquad
  A_\psi=T(x,y,\psi),\qquad d\psi=xy-yx.
\]
In the safe degreewise range
\[
  N\geq\max(K,L+2),
\]
or \(N\geq W+2\) when \(K,L\leq W\), define
\[
  P_{1\mathrm{cyc}}
  =
  \log^*(\mathrm{id})
  =
  \sum_{m=1}^{L}\frac{(-1)^{m-1}}{m}
  (\mathrm{id}-u\epsilon)^{*m}
\]
using the stable block-sum product and the CE coproduct.  Then
\[
  P_{1\mathrm{cyc}}^2=P_{1\mathrm{cyc}},
  \qquad
  d_{\mathrm{CE}}P_{1\mathrm{cyc}}
  =
  P_{1\mathrm{cyc}}d_{\mathrm{CE}},
  \qquad
  \operatorname{im}P_{1\mathrm{cyc}}=\operatorname{im}\Theta_{N,K,L}.
\]
The finite-window map is
\[
  \lambda_{\mathrm{LQT},K,L}
  =
  \Theta_{N,K,L}^{-1}P_{1\mathrm{cyc}}.
\]

The same-rank delete-multicycles operation is not a chain map.  For
homogeneous \(a,b\),
\[
  d_{\mathrm{CE}}\bigl(\Theta_1(a)\wedge\Theta_1(b)\bigr)
  =
  \pm\Theta_1(ab-(-1)^{|a||b|}ba).
\]
Thus
\[
  P_{\mathrm{del}}d_{\mathrm{CE}}
  \bigl(\Theta_1(a)\wedge\Theta_1(b)\bigr)
  =
  \pm\Theta_1(ab-(-1)^{|a||b|}ba),
  \qquad
  d_{\mathrm{CE}}P_{\mathrm{del}}
  \bigl(\Theta_1(a)\wedge\Theta_1(b)\bigr)=0.
\]
Taking \(a=x\), \(b=y\) already gives the nonzero chain-level obstruction
\(\Theta_1(xy-yx)\).  The stable Hopf projection avoids this by forming
products through block sum before applying the Hopf logarithm; after transfer
to a fixed stable rank it is a cumulant formula, not deletion.

The scalar one-\(\psi\) quotient remains chain-level only after the two-term
scalar-Koszul quotient
\[
  \Theta_1(\psi)\mapsto\Theta_1(xy-yx),
  \qquad
  [\psi]\mapsto[xy-yx],
\]
or after homology.  Killing \(\Theta_1(\psi)\) alone remains false.

## Proof Object Produced

The TeX-ready theorem, proof, false-projection fence, scalar quotient clause,
replacement snippets, source boundary, and exact insertion points were written
to:

`reconstitution/lqt-eulerian-theorem-proof-upgrade-2026-04-30.md`

The proof is first-principles in the finite stable Hopf window:

1. \(A_{\psi,K}\) is a dg quotient because \(d\psi=xy-yx\) preserves Koszul
   bidegree.
2. CE length \(L\) is a separate cutoff; \(A_{\psi,K}\) alone does not bound
   cyclic chain length.
3. The block-sum product is a chain map because cross-block brackets vanish.
4. The CE coproduct is a chain map because the CE differential is a
   coderivation.
5. Therefore each convolution power of \(J=\mathrm{id}-u\epsilon\) is a chain
   map.
6. Stable invariant tensors are indexed by permutations of CE factors; cycle
   decomposition identifies the stable Hopf window with a symmetric Hopf
   algebra on single cycles.
7. On a product of \(n\) positive single-cycle generators,
   \(J^{*m}\) has coefficient \(m!S(n,m)\).  The coefficient of the Hopf
   logarithm is
   \[
     \sum_{m=1}^{n}(-1)^{m-1}(m-1)!S(n,m),
   \]
   the coefficient of \(t^n/n!\) in \(\log(1+(e^t-1))=t\).  It is \(1\) for
   \(n=1\) and \(0\) for \(n\geq2\).
8. Hence \(P_{1\mathrm{cyc}}\) fixes single cycles, kills decomposable
   multicycles, is idempotent, and has image \(\operatorname{im}\Theta\).

## Exact Insertion Points

- `main.tex:1780-1785`: replace the paragraph after the external LQT theorem
  by the stable Hopf finite-window construction and same-rank obstruction.
- `theorem-lanes.tex:2079-2105`: replace the K3 LQT clause by the full
  theorem data: \(K,L\), \(\Theta_{N,K,L}\), \(P_{1\mathrm{cyc}}\),
  \(N\geq\max(K,L+2)\), scalar quotient, and false projection fence.
- `open-obligations.tex:143-172`: change the LQT item from open obstruction
  tuple to healed stable tuple, while retaining scalar-before-quotient and
  larger open \(A_\infty\), \(\Psi\to\rho\), BV/cyclicity, and QME
  obligations.
- `claim-strength-ledger.tex:392-411`: mark the LQT component theorem-grade
  only in the stable block-sum Hopf finite window and false for same-rank
  deletion.
- `main.tex:5058-5062`: sharpen connected single-trace extraction to the
  stable Hopf cumulant idempotent \(P_{1\mathrm{cyc}}=\log^*(\mathrm{id})\).
- `main.tex:5040-5042`: optional proof sentence: fixed-rank same-rank deletion
  is not used.

## Source Boundary

Primary-source support is bounded as follows:

- Loday--Quillen 1984, Theorem 6.2 supports the stable
  \(\operatorname{Prim}H_n(\mathfrak{gl}_\infty(A))\cong HC_{n-1}(A)\)
  template.
- Loday--Quillen 1984, Theorem 6.9 supports the safe homological stable
  inequality \(i<N-1\), hence \(N\geq L+2\) for length \(L\).
- Tsygan 1983 supports the same stable matrix-Lie/cyclic-homology mechanism
  as a source precursor.
- The dg \(A_\psi\) window, scalar-Koszul quotient, open \(A_\infty\)
  transfer, \(\Psi\to\rho\) bridge, and BV/QME package are not imported from
  these sources.

## Evidence

Read:

- `CLAUDE.md`
- `AGENTS.md`
- `/Users/raeez/ecosystem/INVARIANTS.md`
- `/Users/raeez/ecosystem/AGENTS-HARNESS.md`
- `main.tex:1745-1795`
- `theorem-lanes.tex:2068-2110`
- `open-obligations.tex:136-176`
- `claim-strength-ledger.tex:360-416`
- `main.tex:4980-5065`
- `commands.tex`
- `mathmacros.tex`
- `notation.tex`
- `preamble.tex`
- `tate-T5-chain-level-primitive.tex:101-151`
- `tate-T5-chain-level-primitive.tex:404-443`
- `references/primary-sources/lqt-tsygan-source-anchors-2026-04-30.md`
- `reconstitution/lqt-eulerian-projection-integration-spec-2026-04-30.md`
- `reconstitution/chain-level-lqt-projection-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-272-lqt-scalar-koszul-quotient-audit.md`
- `reconstitution/swarm-2026-04-30-agent-274-chain-level-lqt-projection-construction-push.md`
- `reconstitution/swarm-2026-04-30-agent-280-lqt-eulerian-projection-integration-spec.md`

Commands run:

```bash
python3 scripts/check_one_psi_homology.py
```

Result:

```text
checked primitive one-psi homology in 36 bidegrees with exponents <= 5
checked open Hamiltonian action on primitive descendants in 240 cases with exponents <= 3
checked closed coadjoint Taylor-dual formula in 1225 cases with exponents <= 5
checked principal-part coadjoint realization in 1225 cases with exponents <= 5
attacked naive quantum descendant lift in 1225 cases with exponents <= 5 and Moyal order <= 5: 1200 PBW-vs-Moyal mismatches, 958 cases with genuine higher Moyal coadjoint terms
explicit obstruction: ad^*_{z1^4}(delta_1,1) has -24 hbar^2 delta_0,4, while the polynomial one-psi action sends Psi_1,1 to 4 Psi_4,0
checked corrected Moyal principal-part coadjoint target in 3375 representation identities with exponents <= 3, Moyal order <= 5, and hbar power <= 4
checked no h-adic deformation of the classical Psi->rho label projection at the linear-generator leading term in 70 tests with labels <= 5
```

Direct diagonal obstruction:

```text
N=2
  E_00 ab: 1
  E_00 ba: -1
  E_11 ab: 1
  E_11 ba: -1
  equals Theta_1(ab-ba), up to the global CE sign convention
N=3
  E_00 ab: 1
  E_00 ba: -1
  E_11 ab: 1
  E_11 ba: -1
  E_22 ab: 1
  E_22 ba: -1
  equals Theta_1(ab-ba), up to the global CE sign convention
N=4
  E_00 ab: 1
  E_00 ba: -1
  E_11 ab: 1
  E_11 ba: -1
  E_22 ab: 1
  E_22 ba: -1
  E_33 ab: 1
  E_33 ba: -1
  equals Theta_1(ab-ba), up to the global CE sign convention
```

No PDF build was run because this was report-only and TeX was not edited.
