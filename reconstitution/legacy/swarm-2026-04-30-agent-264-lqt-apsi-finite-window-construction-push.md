# Agent 264 Report: LQT A-psi Finite-Window Construction Push

Date: 2026-04-30

Worktree: `/Users/raeez/topological-strings`, branch `master`.

Write policy followed: only the two owned reports were written. No TeX,
scripts, bibliography, source fixtures, or build artifacts were edited. No PDF
build was run.

## Claim Attacked

The attacked finite-window claim is the K3 clause of the open
`A_infinity`/Koszul/cyclic acceptance datum:

```text
lambda_{LQT,W}: Prim C_*^CE(gl_N(A_{psi,W}))
  -> CC_red(A_{psi,W})[1],
```

for `A_psi=T(x,y,psi)`, `d psi=xy-yx`, in stable range `N>=W`, compatible
with connected single-trace projection and the Hamiltonian scalar quotient.

The primary-source boundary is fixed: LQ84 Theorem 6.2 proves the stable
ordinary unital associative statement on homology,

```text
Prim H_n^CE(gl_infty(A)) = HC_{n-1}(A),
```

not this dg finite-window chain map. The local source fixture records this
non-support boundary.

## Construction Attempted

The attempted construction succeeds after replacing the ambiguous domain by a
defined finite-window single-cycle invariant subcomplex.

Use the Koszul bidegree

```text
wt(x)=(1,0), wt(y)=(0,1), wt(psi)=(1,1).
```

For total window `W`, set

```text
A_{psi,W} = A_psi / F^{>W}A_psi,
```

where `F^{>W}` is the two-sided dg ideal spanned by words of total Koszul
weight `>W`. This is the necessary dg window. The ordinary word-length
subspace is not dg-stable because `psi` has length `1` and `d psi=xy-yx` has
length `2`.

Define the standard trace-cycle map

```text
Theta_{N,W}: CC_red(A_{psi,W})[1]
  -> C_*^CE(gl_N(A_{psi,W}))^{GL_N}
```

by

```text
Theta_{N,W}(a_0|...|a_r)
  =
  sum_{i_0,...,i_r=1}^N
  (E_{i_0 i_1}a_0) wedge ... wedge (E_{i_r i_0}a_r),
```

with CE written as `S(gl_N(A)[1])`, equivalently with the usual Koszul signs
in the unsuspended exterior notation. The cyclic rotation sign is

```text
(a_0|...|a_r) ~
(-1)^{r + |a_r|(|a_0|+...+|a_{r-1}|)}
(a_r|a_0|...|a_{r-1}).
```

The shift `[1]` is the LQT homological shift:

```text
CE_{r+1}(gl_N(A)) corresponds to CC_r(A).
```

Set

```text
Prim^{1cyc}_{N,W} C_*^CE(gl_N(A_{psi,W})) := image(Theta_{N,W}).
```

In the stable range

```text
N >= max{total Koszul weight in W, CE length + 1},
```

or simply `N>=W` after `W` is chosen to dominate both bounds, the map
`Theta_{N,W}` is injective on the window. The finite-window comparison is

```text
lambda_{LQT,W}(Theta_{N,W}(c)) = c.
```

On stable invariant CE chains, the connected single-trace version is

```text
lambda_{LQT,W} = Theta_{N,W}^{-1} o P_{1cyc},
```

where `P_{1cyc}` is the stable single-cycle projection. Multi-cycle summands
are decomposable multi-traces and are killed by connected extraction.

## Exact Low-Chain Formulas

For

```text
Theta_1(a)=sum_i E_{ii}a,
Theta_2(a,b)=sum_{i,j} E_{ij}a wedge E_{ji}b,
Theta_3(a,b,c)=sum_{i,j,k} E_{ij}a wedge E_{jk}b wedge E_{ki}c,
```

the inverse satisfies

```text
lambda Theta_1(a) = [a],
lambda Theta_2(a,b) = [a|b],
lambda Theta_3(a,b,c) = [a|b|c].
```

The dg generator check is

```text
d_CE Theta_1(psi) = Theta_1(xy-yx),
lambda d_CE Theta_1(psi) = [xy-yx] = d_CC[psi].
```

This vanishes only in the necklace `H_0` shadow
`Cyc(A_psi)=A_psi/[A_psi,A_psi]`; it is not zero as a full reduced cyclic
chain before taking that shadow.

For even `a,b,c`,

```text
lambda d_CE Theta_2(a,b)
  = [ab]-[ba]
  = b[a|b],
```

and

```text
lambda d_CE Theta_3(a,b,c)
  = [ab|c]-[a|bc]+[ca|b]
  = b[a|b|c].
```

These are the low-chain differential checks for the constructed map. The full
graded signs are the suspension signs above; `psi` is odd and `x,y` are even.

## Scalar Quotient Attack

The scalar quotient is the point where the unqualified manuscript formula
breaks at chain level.

The unit satisfies

```text
lambda Theta_1(1) = [1],
```

and is removed by reduced cyclic normalization and by the Hamiltonian scalar
quotient.

The scalar one-psi class is different. The Hamiltonian comparison removes
`Tr(psi)` because it is the cotangent class to the removed constant
Hamiltonian. But the CE chain has nonzero differential:

```text
d_CE Theta_1(psi) = Theta_1(xy-yx).
```

Matrix-unit calculation gives the sharper identity

```text
d_CE Theta_1(psi) = (1/N) d_Lie Theta_2(x,y).
```

Therefore one cannot form a chain quotient by killing `Theta_1(psi)` alone.
The source and target quotients must include the scalar-Koszul subcomplexes

```text
Theta_1(psi) -> Theta_1(xy-yx),
[psi] -> [xy-yx].
```

or else the scalar quotient must be taken only after homology. This is an
actual obstruction, not a wording issue.

## Roos Compatibility

For the healed quotient windows `A_{psi,W}=A_psi/F^{>W}`, the transition maps
`A_{psi,W+1}->A_{psi,W}` are surjective finite-dimensional dg algebra maps.
The trace-cycle maps commute with these projections, so the finite-window
Roos class of `lambda_{LQT,W}` is zero in the constructed single-cycle
habitat.

For ordinary length cutoffs or arbitrary subspace projections, no strict
finite-window dg algebra tower exists. In that habitat the Roos class is
undefined before any LQT comparison can be tested.

## Obstruction Theorem

For the original unqualified formula, the exact obstruction tuple is

```text
O_{LQT,W}
 =
 (O_win, O_Prim, O_stab, O_scalar, O_CC, O_Roos).
```

Here:

- `O_win` is nonzero for ordinary word-length windows: `d psi=xy-yx` leaves
  the cutoff.
- `O_Prim` is undefined unless `Prim` is replaced by the single-cycle stable
  invariant subcomplex or by a specified connected projection.
- `O_stab` is unresolved unless `N>=W` is expanded to cover both Koszul word
  weight and CE degree.
- `O_scalar` is the chain-level class
  `d_CE Theta_1(psi)=Theta_1(xy-yx)` after killing `Theta_1(psi)` alone.
- `O_CC` is the missing choice of reduced cyclic dg model and signs; LQ84 does
  not supply the dg `A_psi` convention by citation.
- `O_Roos` vanishes for the healed quotient tower and is not defined for
  non-dg subspace cutoffs.

Thus a finite-window repair was constructed only for the corrected statement:

```text
Prim^{1cyc}_{N,W} image of Theta_{N,W}
  -> CC_red(A_{psi,W})[1],
```

with Koszul-weight quotient windows, stable single-cycle projection, and the
scalar-Koszul quotient data. The unqualified finite-N primitive CE statement
remains blocked by the obstruction tuple above.

## TeX-Ready Replacement

This is justified as an insertion candidate, not applied to the manuscript:

```tex
Let \(A_{\psi,W}=A_\psi/F^{>W}A_\psi\), where \(F^{>W}\) is the
two-sided dg ideal generated by words of total Koszul weight \(>W\) for
\(\mathrm{wt}(x)=(1,0)\), \(\mathrm{wt}(y)=(0,1)\),
\(\mathrm{wt}(\psi)=(1,1)\).  Let
\[
  \Theta_{N,W}(a_0|\cdots|a_r)=
  \sum_{i_0,\ldots,i_r}
  E_{i_0i_1}a_0\wedge\cdots\wedge E_{i_ri_0}a_r
\]
be the standard trace-cycle map
\[
  CC_{\mathrm{red}}(A_{\psi,W})[1]\to
  C_*^{\mathrm{CE}}(\mathfrak{gl}_N(A_{\psi,W}))^{GL_N}.
\]
In the stable range \(N\geq\max\{W,r+2\}\), define
\[
  \operatorname{Prim}^{1\mathrm{cyc}}_{N,W}
  C_*^{\mathrm{CE}}(\mathfrak{gl}_N(A_{\psi,W}))
  :=\operatorname{im}\Theta_{N,W},
  \qquad
  \lambda_{\mathrm{LQT},W}:=\Theta_{N,W}^{-1}.
\]
Then \(\lambda_{\mathrm{LQT},W}\) is a dg chain map to
\(CC_{\mathrm{red}}(A_{\psi,W})[1]\).  If the Hamiltonian scalar quotient
removes the scalar one-\(\psi\) class, source and target must also
quotient by the corresponding two-term scalar subcomplexes
\[
  \Theta_{N,W}(\psi)\longmapsto\Theta_{N,W}(xy-yx),
  \qquad
  [\psi]\longmapsto[xy-yx],
\]
or the scalar quotient must be postponed to homology.
```

## Verification Commands

Successful commands run from `/Users/raeez/topological-strings`:

```bash
python3 scripts/check_one_psi_homology.py
rg -n -F -e 'lambda_{\mathrm{LQT}' -e 'lambda_LQT' -e 'Cone(lambda' -e 'Loday--Quillen--Tsygan comparison' -e 'Cone}\lambda' theorem-lanes.tex claim-strength-ledger.tex open-obligations.tex reconstitution -g '!out/**'
rg -n -F -e 'reduced cyclic' -e 'CC_{\mathrm{red}' -e 'CC_red' -e 'Cyc(A_' -e 'A_{\psi}' -e 'A_psi' -e 'cyclic quotient' -e 'Hochschild' -e 'Connes' main.tex theorem-lanes.tex tate-P1-hadamard-mittag-leffler.tex tate-T1-weighted-completion.tex tate-T3-quillen-equivalence.tex reconstitution/open-ainfty-koszul-cyclic-acceptance-construction-target-2026-04-30.md
```

The one-psi script passed:

```text
36 primitive one-psi bidegrees;
240 open Hamiltonian action cases;
1225 closed coadjoint Taylor-dual cases;
1225 principal-part coadjoint cases;
3375 corrected Moyal principal-part representation identities;
70 no-h-adic-deformation tests.
```

Additional direct checks run in local Python commands:

```text
ordinary word-length windows are not dg-stable;
Koszul bidegree/total-weight windows are dg-stable for d psi=xy-yx;
d_CE Theta1(psi) = (1/N) d_Lie Theta2(x,y) for N=2,3;
low CE/Hochschild compatibility holds for even chains of lengths 2 and 3.
```

Local anchors read include:

```text
theorem-lanes.tex:55-98
theorem-lanes.tex:2060-2228
main.tex:1738-1782
main.tex:4260-4325
main.tex:4420-4520
main.tex:4650-4830
main.tex:4970-5108
local-dictionary.tex:1188-1262
claim-strength-ledger.tex:360-392
open-obligations.tex:90-150
open-obligations.tex:780-820
references/primary-sources/lqt-tsygan-source-anchors-2026-04-30.md
reconstitution/open-ainfty-koszul-cyclic-acceptance-construction-target-2026-04-30.md
reconstitution/swarm-2026-04-30-agent-235-open-ainfty-koszul-cyclic-acceptance-construction-target.md
```

## Files Changed

```text
reconstitution/lqt-apsi-finite-window-construction-push-2026-04-30.md
reconstitution/swarm-2026-04-30-agent-264-lqt-apsi-finite-window-construction-push.md
```
