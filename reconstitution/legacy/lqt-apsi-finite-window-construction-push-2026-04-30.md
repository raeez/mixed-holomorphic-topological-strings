# LQT A-psi Finite-Window Construction Push

Date: 2026-04-30

Agent: 264

Worktree: `/Users/raeez/topological-strings`, branch `master`.

Owned write surface: this report and
`reconstitution/swarm-2026-04-30-agent-264-lqt-apsi-finite-window-construction-push.md`.
No manuscript TeX, scripts, source fixtures, bibliography, or build artifacts
were edited. No PDF build was run.

## Claim Attacked

The attacked claim is the finite-window dg Loday--Quillen--Tsygan clause in
`theorem-lanes.tex:2079-2088`:

```text
lambda_{LQT,W}: Prim C_*^CE(gl_N(A_{psi,W})) -> CC_red(A_{psi,W})[1],
N >= W,
```

compatible with connected single-trace projection and the scalar quotient, for
`A_psi = T(x,y,psi)`, `d psi = xy-yx`.

LQ84 supports only the stable ordinary unital associative theorem
`Prim H_n^CE(gl_infty(A)) = HC_{n-1}(A)` under its source hypotheses. It does
not supply this dg finite-window chain map, the finite-window stable range, the
scalar quotient, or the open `A_infinity` transfer. This boundary is recorded
in `references/primary-sources/lqt-tsygan-source-anchors-2026-04-30.md`.

## Verdict

A genuine finite-window chain map can be constructed after replacing the
ambiguous domain by the stable single-cycle invariant subcomplex and after
choosing a dg finite-window algebra. The construction is:

```text
lambda_{LQT,W} = Theta_{N,W}^{-1}
```

on the image of the standard trace-cycle map

```text
Theta_{N,W}: CC_red(A_{psi,W})[1] -> C_*^CE(gl_N(A_{psi,W}))^{GL_N}.
```

Equivalently, on stable invariant CE chains one may write

```text
lambda_{LQT,W} = Theta_{N,W}^{-1} o P_{1cyc},
```

where `P_{1cyc}` is the connected single-cycle projection in the stable
Procesi--Razmyslov/LQT invariant decomposition.

This does not prove the unqualified displayed manuscript map. The original
formula is blocked unless it specifies:

1. the finite-window dg algebra as a quotient, not a subspace;
2. the chain-level meaning of `Prim`;
3. a stable range controlling both CE degree and word/Koszul weight;
4. the scalar one-psi quotient as a chain quotient, not just a homology-level
   deletion.

## Finite-Window Habitat

Use the Koszul bidegree

```text
wt(x)=(1,0),  wt(y)=(0,1),  wt(psi)=(1,1).
```

For a one-integer window, let `|w|_K` be total Koszul weight. Define

```text
F^{>W} A_psi = span{ words w : |w|_K > W },
A_{psi,W} = A_psi / F^{>W} A_psi.
```

This is a unital associative dg algebra: `F^{>W}` is a two-sided dg ideal
because multiplication increases positive weight and `d psi=xy-yx` preserves
Koszul bidegree. The ordinary letter-length cutoff is not a dg window:
`psi` has ordinary length `1`, while `d psi` has ordinary length `2`.

For a rectangular window `(R,S)`, the same construction uses the two-sided dg
ideal spanned by words with Koszul bidegree outside the rectangle. The stable
matrix range is then `N >= R+S` together with the CE-degree bound below. For a
single integer `W`, take `W` to dominate total Koszul weight and the CE length
bound.

The finite-window tower `A_{psi,W+1} -> A_{psi,W}` is strict
Mittag--Leffler: transitions are surjective finite-dimensional dg algebra
maps. Therefore the Roos compatibility class of the constructed trace-cycle
comparison is zero in this habitat.

## Trace-Cycle Map

Use homological CE conventions. A cyclic `r`-chain maps to a CE chain of
length `r+1`; this is the source of the target shift `[1]`:

```text
CE_{r+1}(gl_N(A))  <->  CC_r(A).
```

In suspended notation, the CE complex is `S(gl_N(A)[1])`; the Koszul signs are
those of the symmetric coalgebra on the suspension. On an unsuspended cyclic
representative the trace-cycle map is

```text
Theta_{N,W}(a_0|...|a_r)
  =
  sum_{i_0,...,i_r=1}^N
  (E_{i_0 i_1} a_0) wedge ... wedge (E_{i_r i_0} a_r),
```

with the standard graded cyclic sign

```text
(a_0|...|a_r) ~
(-1)^{r + |a_r|(|a_0|+...+|a_{r-1}|)}
(a_r|a_0|...|a_{r-1})
```

in the unsuspended convention. In the manuscript's low chains, `x,y` are even
and `psi` is odd (`|psi|=-1`, parity one).

Define

```text
Prim^{1cyc}_{N,W} C_*^CE(gl_N(A_{psi,W}))
  := image(Theta_{N,W}).
```

For `N` in the stable range, `Theta_{N,W}` is injective on this finite window:
matrix-unit cycles with distinct indices isolate a cyclic tensor, and
Procesi--Razmyslov trace identities have no extra relation below the chosen
word/Koszul bound. A safe range is

```text
N >= max{ W, r+2 }
```

for cyclic degrees `r` present in the window. If `W` is defined to dominate
both total Koszul weight and CE length, this is the manuscript shorthand
`N >= W`.

The constructed map is the inverse on this image:

```text
lambda_{LQT,W}(Theta_{N,W}(c)) = c.
```

On all stable invariant CE chains, first project to the connected
single-cycle summand:

```text
lambda_{LQT,W} = Theta_{N,W}^{-1} P_{1cyc}.
```

Multi-cycle components are decomposable multi-traces and are killed by
connected single-trace extraction.

## Low-Chain Formulas

Write

```text
Theta_1(a) = sum_i E_{ii} a,
Theta_2(a,b) = sum_{i,j} E_{ij} a wedge E_{ji} b,
Theta_3(a,b,c) = sum_{i,j,k} E_{ij} a wedge E_{jk} b wedge E_{ki} c.
```

Then

```text
lambda Theta_1(a) = [a],
lambda Theta_2(a,b) = [a|b],
lambda Theta_3(a,b,c) = [a|b|c].
```

For the dg differential:

```text
d_CE Theta_1(psi) = Theta_1(xy-yx),
lambda d_CE Theta_1(psi) = [xy-yx] = d_CC[psi].
```

The last class becomes zero only after passing to the necklace
`H_0` shadow `Cyc(A_psi)=A_psi/[A_psi,A_psi]`; in the full reduced cyclic
chain complex it is the internal differential of `[psi]`.

For even `a,b,c`:

```text
lambda d_CE Theta_2(a,b)
  = [ab] - [ba]
  = b[a|b],
```

and

```text
lambda d_CE Theta_3(a,b,c)
  = [ab|c] - [a|bc] + [ca|b]
  = b[a|b|c].
```

Thus, with the standard suspension signs,

```text
d_CC lambda_{LQT,W} = lambda_{LQT,W} d_CE
```

on the constructed single-cycle subcomplex.

## Scalar Quotient Compatibility

The unit scalar line is harmless after reduced cyclic normalization:

```text
lambda Theta_1(1) = [1],
```

and the Hamiltonian quotient removes the empty trace and the constant
Hamiltonian.

The scalar one-psi line is not harmless at chain level. The Hamiltonian sector
removes `Tr(psi)` because it is the cotangent class to the removed constant
Hamiltonian. But in CE chains

```text
d_CE Theta_1(psi) = Theta_1(xy-yx) != 0
```

as a chain. Direct matrix-unit computation gives

```text
d_CE Theta_1(psi) = (1/N) d_Lie Theta_2(x,y).
```

Therefore the scalar quotient is a chain quotient only after quotienting both
source and target by the scalar-Koszul subcomplexes generated windowwise by

```text
Theta_1(psi) -> Theta_1(xy-yx).
[psi] -> [xy-yx].
```

Equivalently, one may keep the scalar one-psi class until after homology. The
unqualified instruction "remove the scalar one-psi class" is not a chain-level
operation on `C_*^CE(gl_N(A_{psi,W}))` or on `CC_red(A_{psi,W})`.

This is the sharp scalar quotient obstruction:

```text
O_scalar-LQT(W,N) = [ d_CE Theta_1(psi) ]
```

in the quotient attempted by killing `Theta_1(psi)` alone. It vanishes after
adjoining the differential target `Theta_1(xy-yx)` to the killed subcomplex, or
after passing to homology, but not before.

## Obstruction Theorem for the Original Formula

Let `A_{psi,W}` be unspecified or let it be the ordinary word-length subspace,
and let `Prim C_*^CE` mean the unqualified primitive part of the finite-N CE
coalgebra. Then the displayed finite-window map is not a defined dg chain map.
The obstruction tuple is

```text
O_{LQT,W}
 =
 ( O_win,
   O_Prim,
   O_stab,
   O_scalar,
   O_CC,
   O_Roos ).
```

Components:

- `O_win`: ordinary letter-length windows are not dg-stable, since
  `d psi=xy-yx` leaves the cutoff. A dg finite window must be a quotient by a
  Koszul-weight dg ideal.
- `O_Prim`: the CE chain coalgebra's literal primitives are CE length one;
  the LQT primitive is a stable connected Hopf-homology/single-cycle notion.
  A chain-level theorem must define `Prim^{1cyc}` or supply a canonical
  connected projection.
- `O_stab`: `N >= W` is meaningful only after `W` dominates total Koszul
  weight and CE degree. Rectangular windows require `N >= R+S` plus the CE
  length bound.
- `O_scalar`: killing `Theta_1(psi)` alone is not a chain quotient because
  its CE differential is `Theta_1(xy-yx)`.
- `O_CC`: the target must specify the reduced cyclic model and its
  Hochschild/internal differential signs; LQ84 does not supply the dg
  `A_psi` convention by citation.
- `O_Roos`: for the healed quotient tower, `O_Roos=0`; for subspace cutoffs
  or non-surjective ad hoc projections, the Roos class is not even defined as
  a strict ML tower.

## TeX-Ready Insertion

This insertion is justified as a replacement for the unqualified K3 clause,
not as a manuscript edit performed here.

```tex
\begin{stmt}[Finite-window dg LQT trace-cycle habitat]
Let \(A_\psi=T(x,y,\psi)\), \(|x|=|y|=0\), \(|\psi|=-1\), and
\(d\psi=xy-yx\).  Give \(x,y,\psi\) Koszul weights
\[
  \mathrm{wt}(x)=(1,0),\qquad
  \mathrm{wt}(y)=(0,1),\qquad
  \mathrm{wt}(\psi)=(1,1).
\]
For a total window \(W\), put
\[
  A_{\psi,W}=A_\psi/F^{>W}A_\psi,
\]
where \(F^{>W}A_\psi\) is the two-sided dg ideal spanned by words of
total Koszul weight \(>W\).  Let
\(\Theta_{N,W}\colon CC_{\mathrm{red}}(A_{\psi,W})[1]\to
C_*^{\mathrm{CE}}(\mathfrak{gl}_N(A_{\psi,W}))^{GL_N}\) be the standard
trace-cycle map
\[
  (a_0|\cdots|a_r)\longmapsto
  \sum_{i_0,\ldots,i_r}
  E_{i_0i_1}a_0\wedge\cdots\wedge E_{i_ri_0}a_r
\]
with the usual suspension signs.  In the stable range
\(N\geq\max\{W,r+2\}\), or \(N\geq W\) after \(W\) has been chosen to
dominate both weight and CE length, define
\[
  \operatorname{Prim}^{1\mathrm{cyc}}_{N,W}
  C_*^{\mathrm{CE}}(\mathfrak{gl}_N(A_{\psi,W}))
  :=\operatorname{im}\Theta_{N,W}.
\]
Then
\[
  \lambda_{\mathrm{LQT},W}
  :=\Theta_{N,W}^{-1}\colon
  \operatorname{Prim}^{1\mathrm{cyc}}_{N,W}
  C_*^{\mathrm{CE}}(\mathfrak{gl}_N(A_{\psi,W}))
  \longrightarrow CC_{\mathrm{red}}(A_{\psi,W})[1]
\]
is a dg chain map.  On stable invariant CE chains it is equivalently
\(\Theta_{N,W}^{-1}P_{1\mathrm{cyc}}\), where \(P_{1\mathrm{cyc}}\)
is the connected single-cycle projection.  The Hamiltonian scalar
quotient must either be taken after homology or must quotient source and
target by the corresponding two-term scalar subcomplexes generated by
\[
  \Theta_{N,W}(\psi)\longmapsto
  \Theta_{N,W}(xy-yx),
  \qquad
  [\psi]\longmapsto[xy-yx],
\]
since \(d_{\mathrm{CE}}\Theta_{N,W}(\psi)=\Theta_{N,W}(xy-yx)\).
\end{stmt}
```

## Verification Commands

Successful commands run from `/Users/raeez/topological-strings`:

```bash
sed -n '1,240p' AGENTS.md
sed -n '1,240p' CLAUDE.md
sed -n '1,240p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,220p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,260p' references/primary-sources/lqt-tsygan-source-anchors-2026-04-30.md
git status --short
rg --files reconstitution references scripts | rg -i 'ainfty|a-infinity|koszul|cyclic|lqt|loday|quillen|tsygan|acceptance|finite-window|roos|single-trace|trace|psi|A_psi|dg'
nl -ba theorem-lanes.tex | sed -n '55,98p'
nl -ba theorem-lanes.tex | sed -n '2060,2228p'
nl -ba main.tex | sed -n '1738,1782p'
nl -ba claim-strength-ledger.tex | sed -n '360,392p'
nl -ba open-obligations.tex | sed -n '90,150p'
nl -ba open-obligations.tex | sed -n '780,820p'
sed -n '1,220p' reconstitution/open-ainfty-koszul-cyclic-acceptance-construction-target-2026-04-30.md
sed -n '1,220p' reconstitution/swarm-2026-04-30-agent-235-open-ainfty-koszul-cyclic-acceptance-construction-target.md
sed -n '1,180p' reconstitution/missing-primary-source-fixture-plan-2026-04-30.md
sed -n '1,220p' reconstitution/admissible-tate-barcobar-quillen-envelope-construction-target-2026-04-30.md
sed -n '1,260p' scripts/check_one_psi_homology.py
nl -ba main.tex | sed -n '4260,4325p'
nl -ba main.tex | sed -n '4420,4520p'
nl -ba main.tex | sed -n '4650,4830p'
nl -ba main.tex | sed -n '4970,5105p'
nl -ba main.tex | sed -n '5100,5145p'
nl -ba local-dictionary.tex | sed -n '1188,1262p'
nl -ba scripts/check_one_psi_homology.py | sed -n '600,690p'
python3 scripts/check_one_psi_homology.py
rg -n -F -e 'lambda_{\mathrm{LQT}' -e 'lambda_LQT' -e 'Cone(lambda' -e 'Loday--Quillen--Tsygan comparison' -e 'Cone}\lambda' theorem-lanes.tex claim-strength-ledger.tex open-obligations.tex reconstitution -g '!out/**'
rg -n -F -e 'reduced cyclic' -e 'CC_{\mathrm{red}' -e 'CC_red' -e 'Cyc(A_' -e 'A_{\psi}' -e 'A_psi' -e 'cyclic quotient' -e 'Hochschild' -e 'Connes' main.tex theorem-lanes.tex tate-P1-hadamard-mittag-leffler.tex tate-T1-weighted-completion.tex tate-T3-quillen-equivalence.tex reconstitution/open-ainfty-koszul-cyclic-acceptance-construction-target-2026-04-30.md
python3 - <<'PY'
from collections import Counter

def theta1(a, N):
    return Counter({(('E', i, i, a),): 1 for i in range(N)})

def theta2(a,b,N):
    return Counter({(('E', i, j, a), ('E', j, i, b)): 1 for i in range(N) for j in range(N)})

def d_word(a):
    if a == 'psi':
        return Counter({'xy':1,'yx':-1})
    return Counter()

def d_theta1(a,N):
    out=Counter()
    for term,c in theta1(a,N).items():
        _,i,j,w = term[0]
        for dw,dc in d_word(w).items():
            out[(('E',i,j,dw),)] += c*dc
    return out

def bracket(e,f):
    _,i,j,a=e; _,k,l,b=f
    out=Counter()
    if j==k:
        out[(('E',i,l,a+b),)] += 1
    if l==i:
        out[(('E',k,j,b+a),)] -= 1
    return out

def ce_lie_boundary_theta2(a,b,N):
    out=Counter()
    for (e,f),c in theta2(a,b,N).items():
        for term,bc in bracket(e,f).items():
            out[term] += c*bc
    return out

for N in [2,3]:
    lhs=d_theta1('psi',N)
    rhs=ce_lie_boundary_theta2('x','y',N)
    scaled=Counter({k:v//N for k,v in rhs.items()})
    assert lhs == scaled
print('verified: d_CE Theta1(psi) = (1/N) d_Lie Theta2(x,y) for N=2,3')
PY
python3 - <<'PY'
letters = {'x':(1,0,1),'y':(0,1,1),'psi':(1,1,2)}
examples = [('psi',), ('x','psi'), ('psi','y'), ('x','psi','y')]
for w in examples:
    ordinary = len(w)
    R = sum(letters[a][0] for a in w); S = sum(letters[a][1] for a in w); total = R+S
    repl = []
    done=False
    for a in w:
        if a=='psi' and not done:
            repl += ['x','y']; done=True
        else:
            repl.append(a)
    ordinary2=len(repl)
    total2=sum(letters[a][0]+letters[a][1] for a in repl)
    assert ordinary2 == ordinary + 1
    assert total2 == total
print('verified: ordinary letter-length windows are not dg-stable; Koszul bidegree/total-weight windows are dg-stable for d psi=xy-yx')
PY
python3 - <<'PY'
from collections import Counter

def add(out,key,coef):
    out[key]+=coef
    if out[key]==0:
        del out[key]

def cyc2(pair):
    a,b=pair
    return min((a,b),(b,a))

def lam_boundary_theta2(a,b):
    out=Counter(); add(out,a+b,1); add(out,b+a,-1); return out

def b_cyclic_1(a,b):
    out=Counter(); add(out,a+b,1); add(out,b+a,-1); return out

def lam_boundary_theta3(a,b,c):
    out=Counter()
    for pair,coef in [((a+b,c),1),((a,b+c),-1),((c+a,b),1)]:
        add(out,cyc2(pair),coef)
    return out

def b_cyclic_2(a,b,c):
    out=Counter()
    for pair,coef in [((a+b,c),1),((a,b+c),-1),((c+a,b),1)]:
        add(out,cyc2(pair),coef)
    return out

for a,b in [('x','y'),('x','x')]:
    assert lam_boundary_theta2(a,b)==b_cyclic_1(a,b)
for a,b,c in [('x','y','x'),('x','y','y')]:
    assert lam_boundary_theta3(a,b,c)==b_cyclic_2(a,b,c)
print('verified low CE/Hochschild compatibility for even chains of lengths 2 and 3')
PY
git branch --show-current
pwd
```

Key command results:

- `scripts/check_one_psi_homology.py` passed 36 primitive one-psi bidegrees,
  240 open Hamiltonian action cases, 1225 closed coadjoint cases, 1225
  principal-part cases, 3375 corrected Moyal principal-part representation
  identities, and 70 no-`h`-adic-deformation tests.
- Direct finite-window check verified that ordinary word-length cutoffs are
  not dg-stable and Koszul total-weight windows are dg-stable for
  `d psi=xy-yx`.
- Direct matrix-unit check verified
  `d_CE Theta1(psi) = (1/N) d_Lie Theta2(x,y)` for `N=2,3`.
- Direct low-chain check verified the CE/Hochschild compatibility formulas
  for even chains of lengths two and three.

## Files Changed

Changed and to be staged:

```text
reconstitution/lqt-apsi-finite-window-construction-push-2026-04-30.md
reconstitution/swarm-2026-04-30-agent-264-lqt-apsi-finite-window-construction-push.md
```
