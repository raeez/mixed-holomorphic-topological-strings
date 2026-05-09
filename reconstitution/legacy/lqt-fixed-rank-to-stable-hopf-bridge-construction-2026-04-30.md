# LQT Fixed-Rank to Stable Hopf Bridge Construction

Date: 2026-04-30

Scope: report-only attack-heal pass on the finite-rank matrix
Chevalley--Eilenberg window versus the accepted stable Eulerian Hopf
idempotent.  No TeX was edited.

## Verdict

There is a theorem-grade bridge, but only as a separated-block stabilization
zigzag.  It is not a raw endomorphism of one same-rank exterior CE complex.

For a Koszul-weight bound \(K\) and CE-length bound \(L\), set
\[
  A_{\psi,K}=A_\psi/F^{>K}A_\psi,\qquad
  A_\psi=T(x,y,\psi),\qquad d\psi=xy-yx,
\]
with
\[
  \operatorname{wt}(x)=(1,0),\qquad
  \operatorname{wt}(y)=(0,1),\qquad
  \operatorname{wt}(\psi)=(1,1).
\]
Let
\[
  B(K,L)=\max(K,L+2).
\]
The accepted projection is the stable block-sum Hopf idempotent
\[
  P_{1\mathrm{cyc}}
  =
  \log^*(\mathrm{id})
  =
  \sum_{m=1}^{L}\frac{(-1)^{m-1}}{m}
  (\mathrm{id}-u\epsilon)^{*m}.
\]
It becomes a finite-rank chain idempotent after placing the Hopf factors in
mutually disjoint matrix blocks, each block of size at least \(B(K,L)\).  If a
window contains at most \(L\) Hopf factors, one uniform finite rank is
\[
  M=L\,B(K,L).
\]
The resulting separated-block finite-rank operator is
\[
  P^{\mathrm{sep}}_{M,K,L}
  =
  \beta_{M,K,L}\,P_{1\mathrm{cyc}}\,\alpha_{M,K,L},
\]
where \(\beta_{M,K,L}\) places stable trace-cycle factors in disjoint diagonal
blocks and \(\alpha_{M,K,L}\) reads those separated blocks back as the stable
block-sum Hopf word.  This is a strict chain idempotent on the separated-block
subcomplex.

The stronger same-rank statement is false without additional collision
correction.  Folding the separated blocks into one matrix block is not a chain
map.  The exact obstruction is the cross-block collision coderivation
\[
  \Gamma_N=d_{\mathrm{same}}F_N-F_Nd_{\oplus},
\]
where \(F_N\) is the fold from separated blocks to one same-rank block,
\(d_{\oplus}\) is the separated-block differential, and
\(d_{\mathrm{same}}\) is the ordinary CE differential in the one-block
complex.  Already
\[
  \Gamma_N\bigl(\Theta^N_1(a)\wedge\Theta^N_1(b)\bigr)
  =
  \pm\Theta^N_1(ab-(-1)^{|a||b|}ba).
\]
For \(a=x\), \(b=y\), this is the nonzero chain
\(\Theta^N_1(xy-yx)\).  This is precisely the same obstruction that made raw
same-rank deletion fail.

Thus the replacement for fixed-rank deletion is:

1. stabilize by separated blocks;
2. apply the stable Eulerian Hopf idempotent;
3. only then, if a one-block expression is wanted, fold with the collision
   defect explicitly retained.

No theorem-grade report should say that same-rank deletion is chain homotopic
to \(P_{1\mathrm{cyc}}\) until a full collision homotopy killing
\(\Gamma_N\) is constructed with signs.

## Stable Window and Trace-Cycle Maps

For homogeneous \(a_i\in A_{\psi,K}\), write
\[
  \Theta_N(a_0|\cdots|a_r)
  =
  \sum_{i_0,\ldots,i_r=1}^{N}
  (E_{i_0i_1}a_0)\wedge\cdots\wedge(E_{i_ri_0}a_r),
  \qquad r+1\le L.
\]
The reduced cyclic relation is
\[
  (a_0|\cdots|a_r)
  \sim
  (-1)^{r+|a_r|(|a_0|+\cdots+|a_{r-1}|)}
  (a_r|a_0|\cdots|a_{r-1}).
\]
The sign convention is fixed by
\[
  d_{\mathrm{CE}}\Theta_1(\psi)=\Theta_1(xy-yx).
\]

Let \(\mathsf H^{\mathrm{st}}_{K,L}(A_\psi)\) be the finite stable
block-sum Hopf window: the symmetric Hopf algebra on stable single-cycle
trace diagrams, truncated by total Koszul weight \(K\) and total CE length
\(L\).  Its product is block sum.  Its coproduct is the CE coalgebra coproduct
transported to this stable trace-diagram model.

Because block-sum factors live in disjoint matrix blocks, cross-block brackets
vanish.  Hence product, coproduct, unit, counit, and the differential are
chain maps in this stable Hopf window.  The Hopf logarithm
\[
  P_{1\mathrm{cyc}}=\log^*(\mathrm{id})
\]
is therefore a chain map.  The usual Stirling-number calculation gives
\[
  P_{1\mathrm{cyc}}(z_1\cdots z_n)
  =
  \left(
    \sum_{m=1}^{n}(-1)^{m-1}(m-1)!S(n,m)
  \right)z_1\cdots z_n,
\]
which is \(z_1\) for \(n=1\) and \(0\) for \(n\ge2\).

## Separated-Block Stabilization Maps

Choose \(B=B(K,L)\).  For a Hopf monomial with \(m\le L\) connected factors,
choose \(m\) diagonal blocks
\[
  \C^{B}\oplus\cdots\oplus\C^{B}\subset\C^{M},
  \qquad M=L B.
\]

The stabilization map
\[
  \beta_{M,K,L}\colon
  \mathsf H^{\mathrm{st}}_{K,L}(A_\psi)
  \longrightarrow
  C_*^{\mathrm{CE}}(\mathfrak{gl}_M(A_{\psi,K}))_{\le L}
\]
places the \(j\)-th connected trace-cycle factor in the \(j\)-th block and
wedges the resulting CE chains.  Empty blocks are filled by the unit.  Since
different blocks commute as Lie subalgebras, \(\beta_{M,K,L}\) is a chain
map.

The read-back map
\[
  \alpha_{M,K,L}\colon
  C_*^{\mathrm{CE}}(\mathfrak{gl}_M(A_{\psi,K}))^{\mathrm{sep}}_{\le L}
  \longrightarrow
  \mathsf H^{\mathrm{st}}_{K,L}(A_\psi)
\]
forgets the block labels and records the ordered product of the corresponding
stable connected trace-cycle diagrams.  On the separated-block subcomplex,
\[
  \alpha_{M,K,L}\beta_{M,K,L}=\mathrm{id}.
\]
The composite \(\beta\alpha\) is the projection to the chosen separated-block
representative.  Thus
\[
  P^{\mathrm{sep}}_{M,K,L}
  =
  \beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L}
\]
satisfies
\[
  (P^{\mathrm{sep}}_{M,K,L})^2=P^{\mathrm{sep}}_{M,K,L},
  \qquad
  d_{\mathrm{CE}}P^{\mathrm{sep}}_{M,K,L}
  =
  P^{\mathrm{sep}}_{M,K,L}d_{\mathrm{CE}}.
\]
This is the finite-rank theorem-grade bridge.  Its image is the separated
single-cycle subspace.

## Rank Error Bound

The rank bound has two independent parts.

First, finite trace identities disappear in total trace word degree at most
\(K\) once the block size is at least \(K\), by the Procesi--Razmyslov stable
range used in `main.tex:4447-4478`.

Second, Loday--Quillen stabilization gives the homological safe range
\(i<N-1\).  For CE length at most \(L\), this is safely recorded as
\[
  N\ge L+2.
\]

Thus one block of size \(B(K,L)=\max(K,L+2)\) has zero stable-range error on
the \((K,L)\) window.  If a smaller block size \(n\) is used, the exact
algebraic stabilization error is
\[
  I_{n,K,L}
  =
  \ker\!\left(
    \mathsf H^{\mathrm{st}}_{K,L}(A_\psi)
    \longrightarrow
    \mathsf H^{(n)}_{K,L}(A_\psi)
  \right),
\]
the intersection of the finite window with the polarized fundamental
trace-identity ideal of matrix size \(n\), together with the possible
homological stabilization gap in CE degrees \(i\ge n-1\).  In the displayed
stable range \(I_{n,K,L}=0\).

This is the clean error bound:
\[
  I_{n,K,L}=0
  \quad\text{for}\quad n\ge\max(K,L+2).
\]
Below that range, \(I_{n,K,L}\) is the exact obstruction to choosing a
canonical chain-level inverse from the finite-rank window back to the stable
Hopf window.

## Same-Rank Fold and Collision Obstruction

Let
\[
  F_N\colon C_*^{\mathrm{CE}}(\mathfrak{gl}_{N_1}(A))\otimes
  C_*^{\mathrm{CE}}(\mathfrak{gl}_{N_2}(A))
  \longrightarrow
  C_*^{\mathrm{CE}}(\mathfrak{gl}_N(A))
\]
denote any fold which identifies separated blocks with one common rank-\(N\)
matrix block.  This is not induced by a Lie algebra map from
\(\mathfrak{gl}_{N_1}(A)\oplus\mathfrak{gl}_{N_2}(A)\) to
\(\mathfrak{gl}_N(A)\) preserving the cross-bracket-zero property.  Therefore
it is not a CE chain map.

The failure is the collision coderivation
\[
  \Gamma_N=d_{\mathrm{same}}F_N-F_Nd_{\oplus}.
\]
On two diagonal one-cycles,
\[
  \Theta^N_1(a)=\sum_i E_{ii}a,
\]
one has
\[
\begin{aligned}
  d_{\mathrm{same}}
  \bigl(\Theta^N_1(a)\wedge\Theta^N_1(b)\bigr)
  &=
  \pm\sum_{i,j}[E_{ii}a,E_{jj}b] \\
  &=
  \pm\sum_iE_{ii}
  \bigl(ab-(-1)^{|a||b|}ba\bigr) \\
  &=
  \pm\Theta^N_1(ab-(-1)^{|a||b|}ba).
\end{aligned}
\]
The separated-block differential gives zero on the corresponding external
product when \(a\) and \(b\) have zero internal differential.  Hence this
term is exactly \(\Gamma_N\).

A same-rank chain-homotopy bridge would have to solve
\[
  d_{\mathrm{same}}H+Hd_{\oplus}=-\Gamma_N
\]
compatibly over every finite window and every quotient map.  The first
two-cycle term can be healed by the familiar cyclic chain
\(\Theta_2(a,b)\), because
\[
  d_{\mathrm{CE}}\Theta_2(a,b)
  =
  \Theta_1(ab-(-1)^{|a||b|}ba).
\]
The all-window theorem would require the full partition-lattice collision
homotopy with Koszul signs, stabilizers, scalar-Koszul quotient, and Roos
compatibility.  That object is not presently inscribed in the checked LQT
lane.  Therefore a report may assert the separated-block bridge, but may not
assert a same-rank homotopy bridge.

## Collision Filtration Estimate

There is also a useful finite-\(N\) estimate, but it is not a replacement for
the algebraic obstruction above.

Normalize a trace diagram with \(r\le L\) matrix factors by \(N^{-r}\), and
put the \(\ell^1\)-norm on the matrix-unit coefficient basis in a fixed
finite window.  The fold from separated blocks to one block differs from the
collision-free part by assignments in which at least two of the \(r\) matrix
indices coincide.  The one-collision coefficient is bounded by
\[
  \frac{\binom{r}{2}N^{r-1}}{N^r}
  \le
  \frac{\binom{L}{2}}{N}.
\]
The \(q\)-collision part is \(O_L(N^{-q})\).  Algebraically this says that
the fold error lies in the positive collision filtration.  It does not make
the same-rank deletion map a chain map; it only records that the fold becomes
asymptotically collision-free after a separate normalized large-\(N\)
topology is chosen.

## Claim Status

Closed in this report:

- construction of a finite-rank separated-block chain idempotent
  \(P^{\mathrm{sep}}_{M,K,L}\);
- explicit stabilization maps \(\beta_{M,K,L}\) and \(\alpha_{M,K,L}\);
- explicit zero-error rank bound \(B(K,L)=\max(K,L+2)\) per occupied block;
- exact rank-error kernel \(I_{n,K,L}\) below the stable range;
- exact same-rank fold obstruction \(\Gamma_N\);
- direct two-cycle obstruction check.

Not closed:

- a theorem-grade same-rank endomorphism of
  \(C_*^{\mathrm{CE}}(\mathfrak{gl}_N(A_{\psi,K}))\) homotopic to the stable
  Hopf projection;
- the all-window partition-lattice collision homotopy killing \(\Gamma_N\);
- any claim that raw same-rank deletion is chain homotopic to the stable
  Eulerian idempotent.

## Evidence

Local anchors read:

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
- `main.tex:1795-1895`
- `main.tex:4447-4478`
- `main.tex:5135-5200`
- `theorem-lanes.tex:2079-2105`
- `open-obligations.tex:143-172`
- `claim-strength-ledger.tex:392-411`
- `tate-T5-chain-level-primitive.tex:101-151`
- `tate-T5-chain-level-primitive.tex:188-365`
- `tate-T5-chain-level-primitive.tex:690-815`
- `reconstitution/chain-level-lqt-projection-construction-push-2026-04-30.md`
- `reconstitution/lqt-apsi-finite-window-construction-push-2026-04-30.md`
- `reconstitution/lqt-scalar-koszul-quotient-audit-2026-04-30.md`
- `reconstitution/lqt-eulerian-projection-integration-spec-2026-04-30.md`
- `reconstitution/lqt-eulerian-theorem-proof-upgrade-2026-04-30.md`
- `references/primary-sources/lqt-tsygan-source-anchors-2026-04-30.md`

Checks run:

```bash
python3 - <<'PY'
from math import factorial

def stirling2(n,m):
    if n==m==0: return 1
    if n==0 or m==0: return 0
    dp=[[0]*(m+2) for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j]=j*dp[i-1][j]+dp[i-1][j-1]
    return dp[n][m]
for n in range(1,8):
    coeff=sum(((-1)**(m-1))*factorial(m-1)*stirling2(n,m) for m in range(1,n+1))
    print(f"eulerian_log_coeff n={n}: {coeff}")
PY
```

Output:

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

```bash
python3 - <<'PY'
from collections import Counter
for N in (2,3,4):
    out=Counter()
    for i in range(N):
        for j in range(N):
            if i==j:
                out[(i,'ab')]+=1
                out[(i,'ba')]-=1
    print(f"N={N}: collision differential of Theta1(a)^Theta1(b)")
    for (i,word), coeff in sorted(out.items()):
        print(f"  E_{i}{i} {word}: {coeff}")
PY
```

Output:

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

No PDF build was run because no TeX was edited.
