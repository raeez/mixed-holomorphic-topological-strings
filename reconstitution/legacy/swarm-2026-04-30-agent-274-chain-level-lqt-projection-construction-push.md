# Agent 274 Report: Chain-Level LQT Projection Construction Push

Date: 2026-04-30

Worktree: `/Users/raeez/topological-strings`, branch `master`.

Owned write surface:

- `reconstitution/swarm-2026-04-30-agent-274-chain-level-lqt-projection-construction-push.md`
- `reconstitution/chain-level-lqt-projection-construction-push-2026-04-30.md`

No TeX, script, bibliography, source fixture, or PDF was edited.

## Claim Attacked

Agent 272 left the finite-window LQT clause open at exactly three points:
construct `P_{1cyc}`, state a real finite stable range, and fix the
cyclic/CE signs for `A_{psi,W}`. The attacked surface is the K3 clause in
`theorem-lanes.tex:2079-2105`, with ledger status in
`claim-strength-ledger.tex:392-411` and `open-obligations.tex:143-172`.

## Verdict

The construction closes in the stable block-sum Hopf CE model.

Define

```text
P_{1cyc}=log^*(id)
        = sum_{m>=1} (-1)^{m-1}/m (id-u epsilon)^{*m}.
```

The convolution uses the stable block-sum product and the stable CE
coproduct. On a CE-length window `L` the sum stops at `m=L`. This is a chain
idempotent, and its image is the connected single-cycle summand
`im Theta_{N,K,L}`. Therefore

```text
lambda_{LQT,K,L}=Theta_{N,K,L}^{-1} P_{1cyc}
```

is the chain-level finite-window LQT projection in the corrected habitat.

The construction does not close for the naive fixed-rank projection that
simply deletes multi-cycle tensors in one exterior CE complex. The exact
failed identity is

```text
P_naive d_CE(Theta_1(a) wedge Theta_1(b))
  = +/- Theta_1(ab-(-1)^{|a||b|}ba),
d_CE P_naive(Theta_1(a) wedge Theta_1(b))=0.
```

Thus the same-rank deletion model fails whenever the graded commutator of
`a` and `b` is nonzero. The stable Hopf/cumulant model is not this operation;
it subtracts diagonal-collision terms after transfer to a fixed stable rank.

## Stable Range

Use a two-parameter window:

```text
K = total Koszul weight of the whole cyclic tensor,
L = CE length.
```

For the combined trace-function and LQT finite-window statement, the safe
range is

```text
N >= max(K, L+2).
```

If the manuscript uses one integer `W` with `K <= W` and `L <= W`, write

```text
N >= W+2.
```

The algebra quotient `A_{psi,W}` alone is not a complete finite window for a
fixed `N`, because the reduced cyclic complex still has unbounded chain
length. A fixed-rank theorem must be degreewise in `L`, or else pass to
`gl_infty`.

## Sign Model

The graded matrix bracket is

```text
[E_ij a, E_kl b]
  = delta_{jk} E_il ab
    - (-1)^{|a||b|} delta_{li} E_kj ba.
```

The trace-cycle map is

```text
Theta(a_0|...|a_r)
  = sum_{i_0,...,i_r}
    (E_{i_0 i_1}a_0) wedge ... wedge (E_{i_r i_0}a_r).
```

The cyclic relation is

```text
(a_0|...|a_r)
 ~
(-1)^{r + |a_r|(|a_0|+...+|a_{r-1}|)}
(a_r|a_0|...|a_{r-1}).
```

The CE convention is fixed by

```text
d_CE Theta_1(psi)=Theta_1(xy-yx).
```

Low-chain checks:

```text
lambda d_CE Theta_1(psi)=[xy-yx]=d_CC[psi],
lambda d_CE Theta_2(a,b)=[ab]-(-1)^{|a||b|}[ba],
lambda d_CE Theta_3(a,b,c)
  =[ab|c]-[a|bc]+(-1)^{|c|(|a|+|b|)}[ca|b].
```

For the necklace/Koszul shadow, the manuscript sign survives:

```text
d[w]=sum_{i:a_i=psi} (-1)^{# psi before i}
([a_1...a_{i-1}xy a_{i+1}...a_n]
 -[a_1...a_{i-1}yx a_{i+1}...a_n]).
```

In particular,

```text
d Tr(psi u psi v)=vxyu-vyxu-uxyv+uyxv.
```

## Scalar Quotient

Agent 272's scalar obstruction remains exact:

```text
d_CE Theta_1(psi)=Theta_1(xy-yx).
```

The Hamiltonian scalar quotient is chain-level only after quotienting by

```text
Theta_1(psi) -> Theta_1(xy-yx),
[psi] -> [xy-yx],
```

or after homology. Killing `Theta_1(psi)` alone is still false.

## Status of the Obstruction Tuple

For the corrected stable Hopf finite-window habitat:

- `O_win=0` after using Koszul-weight quotient plus total chain-weight
  cutoff.
- `O_Prim=0` by the Eulerian idempotent.
- `O_stab=0` in the degreewise range `N >= max(K,L+2)`.
- `O_CC=0` after the displayed sign convention.
- `O_Roos=0` because quotient maps are surjective and commute with the Hopf
  operations.
- `O_scalar=0` only after the two-term scalar-Koszul quotient or after
  homology.

The full open `A_infinity` comparison, the `Psi -> rho` bridge, and the
Costello/QME realization are still outside this LQT repair.

## Evidence

Read:

- `CLAUDE.md`, `AGENTS.md`, `~/ecosystem/INVARIANTS.md §IV`,
  `~/ecosystem/AGENTS-HARNESS.md §VIII`
- `main.tex:1738-1785`, `main.tex:4306-4358`,
  `main.tex:4430-4520`, `main.tex:5069-5108`
- `theorem-lanes.tex:2079-2105`
- `claim-strength-ledger.tex:392-411`
- `open-obligations.tex:143-172`
- `tate-T5-chain-level-primitive.tex:101-151`,
  `tate-T5-chain-level-primitive.tex:404-443`
- `references/primary-sources/lqt-tsygan-source-anchors-2026-04-30.md`
- Agent 272 and Agent 264 LQT reports.

Checks run:

```bash
python3 scripts/check_one_psi_homology.py
```

Result: passed all advertised primitive one-psi, Hamiltonian action,
coadjoint, principal-part, Moyal-principal-part, and no-deformation checks.

Direct obstruction check:

```text
N=2,3: d_Lie(Theta1(a)^Theta1(b)) has diagonal coefficients
E_ii ab: +1, E_ii ba: -1,
so it equals Theta1(ab-ba), up to global CE sign.
```

No PDF build was run; this was report-only.
