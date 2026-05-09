# Radial all-N decorated PBW/Stokes attack-heal

Date: 2026-04-30.

## Status

The all-bidegree, all-N radial/Weyl trace input is not proved.  It is also
not obstructed by any computed row.  The exact theorem surface is now:

\[
  \Omega^{\mathrm{rad}}_{a,b}
  =
  [(T_{a,b},E^+_{a,b})]\in\operatorname{coker}B_{a,b}
\]

with

\[
  B_{a,b}(W)=(\partial W,C^+_{a,b}(W)),
  \qquad
  C^+_{a,b}(W)=\pi_+\mathcal N_{\mathrm{free}}\operatorname{Tr}(WM),
  \qquad
  M=YX-XY+\hbar NI .
\]

Vanishing of \(\Omega^{\mathrm{rad}}_{a,b}\) is equivalent to the existence of
a free indexed moment-ideal primitive, equivalently to a correction
\[
  K_{a,b}\in\ker\partial,\qquad
  C^+_{a,b}(K_{a,b})=R^{\mathrm{free}}_{a,b}.
\]

By the ordinary square-cell mechanism, \(\ker\partial=\operatorname{im}
\partial_2\) over \(\mathbb Q\) in the two-colour necklace graph.  Hence the
same condition may be written
\[
  D^\square_{a,b}H_{a,b}=R^{\mathrm{free}}_{a,b},
  \qquad
  D^\square_{a,b}=C^+_{a,b}\partial_2 .
\]

The missing theorem is the decorated PBW Stokes identity:
\[
  \lambda D^\square_{a,b}=0
  \quad\Longrightarrow\quad
  \lambda(R^{\mathrm{free}}_{a,b})=0 .
\]

Equivalently, every signed dual potential row
\[
  (\phi,-\lambda)\in\ker B_{a,b}^*
\]
must satisfy
\[
  \lambda(E^+_{a,b})=\phi(T_{a,b}).
\]
Failure is exactly a row with
\[
  \lambda(E^+_{a,b})-\phi(T_{a,b})\ne0 .
\]
After rescaling, the obstruction value can be normalized to \(1\).

## Files and reports read

- `CLAUDE.md`, `AGENTS.md`, `~/ecosystem/INVARIANTS.md`, and
  `~/ecosystem/AGENTS-HARNESS.md`.
- Vol II manuscript-writing harness:
  `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- `appendix-radial-parts-moyal.tex`, `main.tex`, `theorem-lanes.tex`,
  `open-obligations.tex`, and `claim-strength-ledger.tex`.
- Agent 289 report:
  `reconstitution/swarm-2026-04-30-agent-289-radial-dual-potential-identity-construction-push.md`.
- Agent 296 report:
  `reconstitution/swarm-2026-04-30-agent-296-radial-structural-hodge-proof-mechanism.md`.
- No agent 303 report is present under `reconstitution/`.

No TeX or script file was edited.

## Local anchors

- `appendix-radial-parts-moyal.tex:267-315`: radial-parts input package.
  The exact Weyl-trace image clause is not supplied by the cited
  Harish--Chandra/Wallach/Levasseur--Stafford sources in this Weyl/Capelli
  normalization.
- `appendix-radial-parts-moyal.tex:455-557`: quantum shear congruence and
  moment-ideal primitive \(E_{a,b,N}=\sum A^j{}_i\widehat\mu^i{}_j\).
- `appendix-radial-parts-moyal.tex:559-645`: free trace-diagram obstruction,
  bare \((4,4)\) failure, and \(K_{4,4}\) correction.
- `appendix-radial-parts-moyal.tex:669-739`: free indexed normal-ordering
  formula.
- `appendix-radial-parts-moyal.tex:820-963`: \(C^+_{a,b}\), \(\mathcal C_{a,b}\),
  \(\mathfrak o_{a,b}\), decorated Hodge obstruction, and canonical Hodge
  correction.
- `appendix-radial-parts-moyal.tex:965-1059`: dual-potential form,
  \(\Omega^{\mathrm{rad}}_{a,b}\), signed row \((\phi,-\lambda)\), and
  \(D^\square_{a,b}=C^+_{a,b}\partial_2\).
- `appendix-radial-parts-moyal.tex:1113-1259`: proved edge PBW telescoping
  families.
- `appendix-radial-parts-moyal.tex:1261-1364`: finite non-edge certificates.
- `theorem-lanes.tex:2509-2669`: degree-zero Moyal/Weyl sector and radial
  obstruction gate.
- `open-obligations.tex:1304-1391`: radial/Weyl finite certificates and
  uniform homotopy gate.
- `claim-strength-ledger.tex:957-1015`: radial/Weyl finite certificates plus
  exact uniform-homotopy obstruction.
- `main.tex:2328-2350` and `main.tex:2640-2675`: current high-level theorem
  summaries.

## Checked formulas and constants

Formal Weyl/Moyal:

\[
  f*g=m\exp\left({\hbar\over2}P\right)(f\otimes g),
  \qquad
  P=\partial_{z_1}\otimes\partial_{z_2}
  -\partial_{z_2}\otimes\partial_{z_1}.
\]

For \(f=z_1^kz_2^l\), \(g=z_1^mz_2^n\),

\[
  P^r(f,g)=
  \sum_{\alpha=0}^r(-1)^\alpha\binom r\alpha
  (k)_{r-\alpha}(l)_\alpha(m)_\alpha(n)_{r-\alpha}
  z_1^{k+m-r}z_2^{l+n-r}.
\]

The raw commutator has only odd powers:

\[
  [f,g]_{\mathrm{raw}}^{(2s+1)}
  =
  {\hbar^{2s+1}\over 2^{2s}(2s+1)!}P^{2s+1}(f,g),
  \qquad
  [f,g]_{\mathrm{raw}}^{(2s)}=0 .
\]

Checked coefficients:

\[
  1,\quad {1\over24},\quad {1\over1920},\quad
  {1\over322560},\quad {1\over92897280},\quad
  {1\over40874803200}.
\]

Example \(f=z_1^4z_2^2\), \(g=z_1^2z_2^4\):

\[
  P(f,g)=12z_1^5z_2^5,\quad
  P^3(f,g)=-960z_1^3z_2^3,\quad
  P^5(f,g)=11520z_1z_2,
\]

so

\[
  [f,g]_{\mathrm{raw}}
  =
  12\hbar z_1^5z_2^5
  -40\hbar^3z_1^3z_2^3
  +6\hbar^5z_1z_2 .
\]

Capelli/Weyl triangular normalization:

\[
  J_N(z_1^az_2^b)
  \equiv
  \sum_{r=0}^{\min(a,b)}
  \left(-{\hbar N\over2}\right)^r
  r!\binom ar\binom br\,T_{a-r,b-r},
\]

\[
  T_{a,b}
  \equiv
  \sum_{r=0}^{\min(a,b)}
  \left({\hbar N\over2}\right)^r
  r!\binom ar\binom br\,J_N(z_1^{a-r}z_2^{b-r}).
\]

The moment contact relation is

\[
  YX-XY+\hbar NI\equiv0
  \pmod{\mathcal W_N\widehat\mu(\mathfrak{sl}_N)}.
\]

Edge families:

\[
  C^{\mathrm{edge}}_{2,b}
  =
  \sum_{r=0}^{\lfloor(b-2)/2\rfloor}
  (b-1-2r)\operatorname{Tr}(Y^rXY^{b-1-r}M),
\]

\[
  C^{\mathrm{edge}}_{a,2}
  =
  {3\over a+1}
  \sum_{r=0}^{\lfloor(a-2)/2\rfloor}
  (a-1-2r)\operatorname{Tr}(X^{a-1-r}YX^rM).
\]

Their free normal-diagram residuals vanish for all displayed edge bidegrees
by the manuscript proof, and the script regression was rerun through
\((2,9)\) and \((9,2)\).

Bare \((4,4)\) classical lift failure:

\[
\begin{aligned}
R^{\mathrm{cl}}_{4,4}
={43\over7}\bigl(
&\hbar^2D[X_{0\to1}X_{1\to2}Y_{2\to3}Y_{3\to0}]
-\hbar^2D[X_{0\to1}X_{2\to3}Y_{1\to2}Y_{3\to0}]\\
&-\hbar^3D[X_{0\to0}\mid Y_{0\to0}]
+\hbar^3N D[X_{0\to1}Y_{1\to0}]
\bigr).
\end{aligned}
\]

It is killed by

\[
  K_{4,4}={43\over14}\bigl(
  \operatorname{Tr}(XXYXYYM)
  -\operatorname{Tr}(XYXXYYM)
  -\operatorname{Tr}(XYYXYXM)
  +\operatorname{Tr}(XYYYXXM)
  \bigr).
\]

## Computations rerun

All commands used `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`.

1. Syntax:

```text
python3 -B -m py_compile \
  scripts/check_moyal_coefficients.py \
  scripts/quantum_shear_primitive_search.py \
  scripts/quantum_shear_universal_formula.py \
  scripts/quantum_shear_trace_diagram_normal_form.py
```

Result: exit code `0`.

2. Formal Moyal/Capelli/radial finite harness:

```text
python3 -B scripts/check_moyal_coefficients.py
```

Key output:

```text
Moyal sweep: checked 14641 monomial pairs, exponents <= 10, orders <= 11. PASS.
Capelli triangular round-trip: checked 121 monomials with a, b <= 10. PASS.
N=2: checked 80 operator/test-polynomial pairs. PASS.
N=3: checked 80 operator/test-polynomial pairs. PASS.
Rank-2 radial-parts commutator: all listed pairs PASS.
Open-line midpoint graph weights: all listed pairs PASS.
ALL CHECKS PASS.
```

3. Free normal-ordering self-test and bare \((4,4)\) failure:

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --self-test --self-test-rank 2 --self-test-max-length 5 \
  --case 4,4 --classical-only --max-terms 8
```

Result: PBW self-test checked `63` words and passed; the bare \((4,4)\)
classical lift failed with the four-term \(43/7\) residual above.

4. Decorated diagonal corrections:

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --case 5,5 --case 6,6 \
  --kernel-correction --progress --max-terms 3
```

Result:

```text
(4,4): residual_terms=4,  correction_terms=4,  rank=10, rows=49,  cols=20,  corrected_residual_terms=0
(5,5): residual_terms=22, correction_terms=16, rank=29, rows=143, cols=70,  corrected_residual_terms=0
(6,6): residual_terms=96, correction_terms=54, rank=93, rows=446, cols=252, corrected_residual_terms=0
```

5. Edge regression:

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --family-only --edge-family-max 9 --kernel-correction --progress --max-terms 1
```

Result: all edge cases \((2,b)\) and \((b,2)\) for \(2\leq b\leq9\)
passed with `residual_terms=0`, `correction_terms=0`,
`corrected_residual_terms=0`.

6. Total degree 13 interior certificate:

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,10 --case 10,3 --case 4,9 --case 9,4 \
  --case 5,8 --case 8,5 --case 6,7 --case 7,6 \
  --kernel-correction --progress --max-terms 1
```

Result:

```text
(3,10): residual_terms=0,   correction_terms=0,  rank=21,  rows=104, cols=55,  corrected_residual_terms=0
(10,3): residual_terms=0,   correction_terms=0,  rank=21,  rows=104, cols=55,  corrected_residual_terms=0
(4,9):  residual_terms=10,  correction_terms=12, rank=57,  rows=285, cols=165, corrected_residual_terms=0
(9,4):  residual_terms=10,  correction_terms=12, rank=57,  rows=285, cols=165, corrected_residual_terms=0
(5,8):  residual_terms=78,  correction_terms=46, rank=111, rows=542, cols=330, corrected_residual_terms=0
(8,5):  residual_terms=90,  correction_terms=49, rank=111, rows=542, cols=330, corrected_residual_terms=0
(6,7):  residual_terms=165, correction_terms=83, rank=154, rows=744, cols=462, corrected_residual_terms=0
(7,6):  residual_terms=170, correction_terms=79, rank=154, rows=744, cols=462, corrected_residual_terms=0
```

7. Displayed non-edge formulas:

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,5 --case 5,3 --solve-free --progress --max-terms 12
```

Result: both free solves passed with zero residual, reproducing the
coefficients printed in Proposition `prop:app-free-obstruction-certificates`.

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,6 --case 6,3 --solve-classical --progress --max-terms 12
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,6 --case 6,3 --kernel-correction --progress --max-terms 1
```

Result: both classical lifts passed, and both kernel-correction checks had
`residual_terms=0`, `correction_terms=0`, and `corrected_residual_terms=0`.

## Attack-heal ledger

### A314-01: generic radial-parts appeal

Claim attacked: the finite-\(N\) radial-parts theorem alone proves the exact
ordinary Weyl-trace image \(J_N(f)=J_N^{\mathrm{rad}}(f)\).

Finding: false at current proof strength.  The cited radial-parts sources
support the Harish--Chandra homomorphism, regular-Cartan landing, and kernel
statement, but not the exact Weyl/Capelli image normalization used here.
`appendix-radial-parts-moyal.tex:286-292` already records this boundary.

Heal: keep Statement `stmt:app-radial-external-input` as the input package
unless the quantum shear primitive or the free diagram obstruction is closed
internally.

### A314-02: ordinary incidence Green operator

Claim attacked: solving \(\partial c=T_{a,b}\) by the ordinary graph Green
operator is enough.

Finding: false.  The \((4,4)\) bare cyclic lift has the nonzero four-term
\(43/7\) free residual above.  This residual is invisible to the ordinary
\(\hbar^0\) incidence equation and is killed only by a decorated
\(\ker\partial\) correction.

Heal: theorem object is \(C^+_{a,b}|_{\ker\partial}\), or equivalently
\(D^\square_{a,b}=C^+_{a,b}\partial_2\), not the ordinary graph Laplacian.

### A314-03: edge families

Claim attacked: edge rows are only finite evidence.

Finding: healed.  `appendix-radial-parts-moyal.tex:1113-1259` proves the
closed PBW telescoping formulas for \((2,b)\) and \((a,2)\).  The regression
through \(b=9\) agrees.

Heal: edge families should be treated as proved theorem data, not part of
the open all-interior theorem.

### A314-04: all-interior decorated PBW Stokes

Claim attacked: the all-interior theorem is proved by the existing finite
table.

Finding: not proved.  The total-degree 13 interior run, \((5,5)\), and
\((6,6)\) all close, but the computation is pivot-gauge rational linear
algebra.  It does not construct a natural all-bidegree homotopy and does not
prove the potential identity for arbitrary signed rows.

Heal: state the theorem target as the decorated PBW Stokes identity
\(\lambda D^\square_{a,b}=0\Rightarrow
\lambda(R^{\mathrm{free}}_{a,b})=0\), or else exhibit the first normalized
violating row.

## Exact TeX patch targets

No TeX was edited.  If the manuscript is patched later, the exact targets are:

1. `appendix-radial-parts-moyal.tex:965-1059`.
   After Proposition `prop:app-radial-dual-potential-obstruction`, insert a
   square-cell refinement:
   - define the based shuffle square complex \(C^\square_\bullet(a,b)\);
   - quotient by cyclic rotation over \(\mathbb Q\);
   - prove \(\operatorname{im}\partial_2=\ker\partial\);
   - define \(D^\square_{a,b}=C^+_{a,b}\partial_2\);
   - state the finite-dimensional Hodge equivalence
     \[
       \Omega^{\mathrm{rad}}_{a,b}=0
       \Longleftrightarrow
       R^{\mathrm{free}}_{a,b}\in\operatorname{im}D^\square_{a,b}
       \Longleftrightarrow
       \Pi^\square_{a,b}R^{\mathrm{free}}_{a,b}=0.
     \]

2. `appendix-radial-parts-moyal.tex:1061-1111`.
   In the potential-form remark, replace the bare "ordinary graph Green
   operator is insufficient" boundary with the sharper distinction:
   ordinary square cells generate \(\ker\partial\), but only the decorated
   map \(D^\square\) can decide PBW contraction and split-trace residues.

3. `theorem-lanes.tex:2509-2669`.
   Keep status as "proved finite algebraic model plus exact radial/Weyl
   obstruction theorem target".  Add the square-cell criterion explicitly:
   every \(\lambda\in\ker(D^\square_{a,b})^*\) must vanish on
   \(R^{\mathrm{free}}_{a,b}\).  Do not upgrade to all-bidegree proved.

4. `open-obligations.tex:1304-1391`.
   Update the radial/Weyl row so the acceptance gate is either
   \[
     \Pi^\square_{a,b}R^{\mathrm{free}}_{a,b}=0
     \quad\text{for all }a,b
   \]
   or a normalized signed row
   \[
     (\phi,-\lambda)\in\ker B_{a,b}^*,\qquad
     \lambda(E^+_{a,b})-\phi(T_{a,b})=1 .
   \]

5. `claim-strength-ledger.tex:957-1015`.
   Retain "proved finite certificates plus exact uniform-homotopy
   obstruction"; add that \(D^\square_{a,b}\) is the cellular decorated map
   deciding the same cokernel class.

6. `main.tex:2328-2350` and `main.tex:2640-2675`.
   The summary language is currently accurate.  If tightened, replace
   "uniform splitting problem" by the equivalent square-cell decorated Stokes
   problem for \(D^\square_{a,b}\).  Do not cite the finite table as proof of
   the all-interior theorem.

## Remaining obligations

1. Prove the decorated PBW Stokes identity:
   \[
     \lambda D^\square_{a,b}=0
     \Rightarrow
     \lambda(R^{\mathrm{free}}_{a,b})=0
   \]
   for all \(a,b\).

2. Or construct the first exact obstruction row:
   \[
     (\phi,-\lambda)\in\ker B_{a,b}^*,
     \qquad
     \lambda(E^+_{a,b})-\phi(T_{a,b})=1.
   \]

3. Add a dual-row extraction mode to the sparse solver.  On inconsistency it
   should print \((\phi,-\lambda)\), the row support, and the obstruction
   value.  That would turn a failed finite solve into a proof-grade
   obstruction theorem.

4. Construct a closed-form PBW matching-stratum proof for the width-one
   interior strips \(a=3\) or \(b=3\).  Finite evidence shows zero correction
   through the checked strip, but the manuscript needs the two-moving-letter
   telescoping identity.

5. Keep the all-N radial/Weyl trace comparison separate from Costello graph/QME
   realization, one-antifield principal-part lifting, and physical trace-state
   construction.  None follows from the algebraic radial/PBW certificates.
