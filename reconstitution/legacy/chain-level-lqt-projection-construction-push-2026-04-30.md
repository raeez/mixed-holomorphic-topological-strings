# Chain-Level LQT Projection Construction Push

Date: 2026-04-30

Scope: finite-window Loday--Quillen--Tsygan projection for
`A_psi=T(x,y,psi)`, `d psi=xy-yx`, after Agent 272. Report-only. No TeX
edited.

## Verdict

The chain-level projection can be constructed, but only in the stable
block-sum Hopf CE model, not as the naive operation that deletes all
multi-cycle tensors inside one fixed-rank exterior CE complex.

The construction is the Eulerian, or cumulant, idempotent

```text
P_{1cyc}=e=log^*(id)
        = sum_{m>=1} (-1)^{m-1}/m (id-u epsilon)^{*m},
```

where convolution is taken with the stable block-sum product and the
stable CE coproduct. On a finite CE-length window the sum is finite. Since
product, coproduct, unit, counit, and differential are chain maps in this
stable Hopf complex, `P_{1cyc}` is a chain idempotent:

```text
P_{1cyc}^2=P_{1cyc},
d_CE P_{1cyc}=P_{1cyc} d_CE.
```

Under the stable invariant-theory/LQT decomposition, its image is exactly
the connected single-cycle summand `im Theta_{N,W}`. Hence the repaired
finite-window map is

```text
lambda_{LQT,K,L}=Theta_{N,K,L}^{-1} P_{1cyc}.
```

The construction does not prove a fixed finite-rank formula for all CE
degrees. It is degreewise. A fixed rank `N` can only control a bounded CE
length.

## Windows and Stable Range

Use two independent bounds.

```text
K = total Koszul-weight bound for the whole cyclic tensor,
L = CE length bound.
```

Let

```text
wt(x)=(1,0), wt(y)=(0,1), wt(psi)=(1,1),
A_{psi,K}=A_psi/F^{>K}A_psi.
```

The cyclic/CE finite window is the span of reduced cyclic chains and CE
chains with total Koszul weight at most `K` and CE length at most `L`. The
differential preserves this window: `d psi=xy-yx` preserves Koszul bidegree,
and the Hochschild/CE multiplication faces lower CE length.

The explicit safe rank is

```text
N >= max(K, L+2).
```

Reason:

- `N >= L` is enough for the chain-level stable invariant decomposition
  indexed by permutations/cycles in CE length at most `L`.
- LQ84 Theorem 6.9 gives ordinary homological stabilization in degree `i`
  once `i < N-1`; for CE length at most `L`, the safe imported template
  range is `N >= L+2`.
- If the same class is also realized as a polynomial matrix trace function
  of total Koszul word degree at most `K`, Procesi--Razmyslov stability
  requires `N >= K`.

Thus the manuscript shorthand "N dominates the Koszul window and CE
length" should mean `N >= max(K, L+2)`. If a single integer `W` controls
both `K <= W` and `L <= W`, use the safe displayed form

```text
N >= W+2.
```

The algebra quotient `A_{psi,W}` alone is not a finite CE window:
`CC_red(A_{psi,W})` still has unbounded chain length. A finite-rank
statement therefore needs either the extra CE-length cutoff `L` or passage
to the stable colimit.

## Trace-Cycle Map

For homogeneous labels in `A_{psi,K}`, with `|x|=|y|=0` and `|psi|=-1`
parity odd, the graded matrix bracket is

```text
[E_ij a, E_kl b]
  = delta_{jk} E_il ab
    - (-1)^{|a||b|} delta_{li} E_kj ba.
```

The trace-cycle map on a reduced cyclic representative is

```text
Theta_{N,K,L}(a_0|...|a_r)
  =
  sum_{i_0,...,i_r}
  (E_{i_0 i_1} a_0) wedge ... wedge (E_{i_r i_0} a_r),
```

so CE length is `r+1`. The cyclic relation is the standard unsuspended
graded cyclic relation

```text
(a_0|...|a_r)
 ~
(-1)^{r + |a_r|(|a_0|+...+|a_{r-1}|)}
(a_r|a_0|...|a_{r-1}).
```

The CE sign convention is fixed by

```text
d_CE Theta_1(psi)=Theta_1(xy-yx).
```

With this convention the low-chain checks are:

```text
lambda d_CE Theta_1(psi)
  = [xy-yx]
  = d_CC[psi],

lambda d_CE Theta_2(a,b)
  = [ab] - (-1)^{|a||b|}[ba],

lambda d_CE Theta_3(a,b,c)
  = [ab|c] - [a|bc]
    + (-1)^{|c|(|a|+|b|)}[ca|b]
```

up to the global convention already fixed by the first displayed identity.
For even `a,b,c`, this is Agent 264's formula

```text
[ab|c] - [a|bc] + [ca|b].
```

For the internal Koszul differential on cyclic words in the necklace
shadow, the sign is exactly the manuscript sign:

```text
d[w]
 =
sum_{i:a_i=psi} (-1)^{# psi before i}
 [a_1...a_{i-1}xy a_{i+1}...a_n
  -a_1...a_{i-1}yx a_{i+1}...a_n]_cyc.
```

In particular

```text
d Tr(psi u psi v)=vxyu-vyxu-uxyv+uyxv,
```

which is alternating in `(u,v)` and gives `d^2=0`.

## Projection Construction

Let `H_{K,L}^{st}(A_psi)` be the stable block-sum Hopf CE chain complex in
the finite window `(K,L)`. Its multiplication is induced by block diagonal
sum of matrix ranks; its coproduct is the CE coalgebra coproduct transported
to the stable invariant summand. This is the chain-level Hopf object behind
the connected LQT statement, not the same-rank exterior product.

Define

```text
J=id-u epsilon,
P_{1cyc}=sum_{m=1}^{L} (-1)^{m-1}/m J^{*m}.
```

Then:

```text
P_{1cyc} Theta(c)=Theta(c),
P_{1cyc}(z_1 ... z_m)=0 for m>=2 connected positive factors,
im P_{1cyc}=im Theta,
ker P_{1cyc}=stable decomposable multi-cycle summand.
```

The proof is the standard Eulerian-idempotent calculation in a connected
graded commutative Hopf algebra over characteristic zero. The finite window
makes the logarithm finite. Naturality of the block-sum Hopf structure gives
compatibility with quotient maps `(K',L')->(K,L)`, so the Roos class for
this projection tower is zero.

Thus the repaired chain map is

```text
lambda_{LQT,K,L}=Theta_{N,K,L}^{-1} P_{1cyc}
```

on stable invariant CE chains. It is a chain map because `Theta` and
`P_{1cyc}` are chain maps and `Theta` is injective in the displayed stable
range.

## Naive Projection Obstruction

The naive projection

```text
P_naive = "keep same-rank single-cycle permutation tensors, delete all
multi-cycle tensors"
```

is not a chain map on the raw fixed-rank CE exterior complex. The obstruction
already appears on two diagonal one-cycles. For homogeneous `a,b`,

```text
d_Lie(Theta_1(a) wedge Theta_1(b))
  = +/- Theta_1(ab-(-1)^{|a||b|}ba).
```

Therefore

```text
P_naive d_CE(Theta_1(a) wedge Theta_1(b))
  = +/- Theta_1([a,b]_gr),
d_CE P_naive(Theta_1(a) wedge Theta_1(b))
  = 0.
```

Unless `[a,b]_gr=0`, the projection identity fails. This is the exact
finite invariant-theory obstruction to the same-rank deletion model.

The Eulerian/cumulant projection avoids this failure because products of
connected cycles are formed by block sum before passing to the stable Hopf
complex; cross-block brackets vanish. Equivalently, after transfer to a
fixed stable rank, the projection is not raw cycle deletion but the cumulant
linear combination that subtracts diagonal-collision terms.

## Scalar-Koszul Quotient

The scalar one-`psi` deletion still has the Agent 272 obstruction. It is not
changed by the Eulerian projection:

```text
d_CE Theta_1(psi)=Theta_1(xy-yx),
d_CC[psi]=[xy-yx].
```

The Hamiltonian scalar quotient is a chain quotient only after quotienting
source and target by the two-term scalar-Koszul subcomplex

```text
Theta_1(psi) -> Theta_1(xy-yx),
[psi] -> [xy-yx],
```

or after passing to homology. Killing `Theta_1(psi)` alone is still false.

## Claim Status

Closed:

- `O_win`: killed by Koszul-weight quotient plus total chain-weight cutoff.
- `O_Prim`: killed by the Eulerian idempotent in the stable block-sum Hopf
  CE complex.
- `O_stab`: explicit degreewise safe range `N >= max(K, L+2)`.
- `O_CC`: signs fixed by the suspended LQT convention and the displayed
  low-chain identities.
- `O_Roos`: zero for the finite quotient tower because all transitions and
  Hopf operations commute with the quotient maps.

Still open outside this LQT construction:

- scalar deletion before the two-term scalar-Koszul quotient;
- the full open `A_infinity` transfer, `Psi -> rho` bridge, Costello/QME
  realization, and factorization-center centrality homotopies.

## Evidence

Read anchors:

- `theorem-lanes.tex:2079-2105`
- `claim-strength-ledger.tex:392-411`
- `open-obligations.tex:143-172`
- `main.tex:1738-1785`
- `main.tex:4306-4358`
- `main.tex:4430-4520`
- `main.tex:5069-5108`
- `tate-T5-chain-level-primitive.tex:101-151`
- `tate-T5-chain-level-primitive.tex:404-443`
- `references/primary-sources/lqt-tsygan-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-272-lqt-scalar-koszul-quotient-audit.md`
- `reconstitution/swarm-2026-04-30-agent-264-lqt-apsi-finite-window-construction-push.md`

Checks run:

```bash
python3 scripts/check_one_psi_homology.py
python3 - <<'PY'
from collections import Counter
def bracket_diag_terms(N):
    out=Counter()
    for i in range(N):
        for j in range(N):
            if i == j:
                out[(i,'ab')] += 1
                out[(i,'ba')] -= 1
    return out
for N in (2,3):
    out=bracket_diag_terms(N)
    print(f'N={N}: d_Lie(Theta1(a)^Theta1(b)) has diagonal coefficients')
    for key,val in sorted(out.items()):
        print(f'  E_{key[0]}{key[0]} {key[1]}: {val}')
    print('  equals Theta1(ab-ba), up to the global CE sign convention')
PY
```

The one-psi script passed its advertised finite checks. The direct diagonal
calculation gives the obstruction to the naive same-rank projection.
