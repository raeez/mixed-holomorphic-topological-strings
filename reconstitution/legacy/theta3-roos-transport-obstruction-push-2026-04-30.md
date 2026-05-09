# Theta3 Roos Transport Obstruction Push

Date: 2026-04-30.
Status: report-only construction and obstruction push. No TeX, script,
figure, source fixture, bibliography, PDF, or build artifact was edited.

## Decision

No theorem-grade compatible tower of local functionals
\[
  B^M
\]
was constructed from the current data.

There is a formal tower that would work if it were supplied as new
mathematics:
\[
  d_{\mathrm{ns},M}B^M=-\mathfrak b^M,\qquad
  \widehat\sigma_{\mathrm{sc},M}(B^M)=0,\qquad
  \pi_{M,N}\mathfrak b^M=\mathfrak b^N,\qquad
  \pi_{M,N}B^M=B^N .
\]
With these strict Bianchi-row and primitive transports the boundary
matrices commute and the Roos primitive class is zero. This is an
acceptance target, not a construction in the current checkout. The current
data do not supply the local functional \(B^M\), the scalar-zero proof, the
regular-density or wavefront habitat, the Bianchi-row transport matrices,
or the primitive transport maps.

In the actual current Bianchi-exposed lower habitat the obstruction already
appears at fixed window \(N=2\). The only available lower degree-zero column
is
\[
  D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2),
  \qquad
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},
\]
and
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
  +\mathfrak b^2_{02,20}.
\]
In the ordered basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})
\]
this is
\[
  A_D^2=(-2,2,1)^T.
\]
The desired Bianchi counterterm column is
\[
  A_B^2=(0,0,-1)^T.
\]
It is not in the image of the current boundary matrix. The cokernel
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*
\]
satisfies
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}A_B^2=-1.
\]
Thus the actual current habitat has a fixed-window \(H^1\) obstruction
before the Roos \(H^0\) primitive-compatibility problem is reached.

## Formal Tower Attempt

Suppose, as a controlled enlargement, that every window \(M\geq 2\) has a
Bianchi row \(\mathfrak b^M\), a source-coordinate column \(D^M\), and a
new column \(B^M\) with
\[
  d_{\mathrm{ns},M}D^M=-r^M+\mathfrak b^M,\qquad
  d_{\mathrm{ns},M}B^M=-\mathfrak b^M.
\]
Then
\[
  d_{\mathrm{ns},M}(D^M+B^M)=-r^M.
\]
At \(N=2\) this is exactly the matrix
\[
  A^2_{D,B}
  =
  \begin{pmatrix}
    -2&0\\
     2&0\\
     1&-1
  \end{pmatrix},
  \qquad
  d(D^2+B^2)=(-2,2,0)^T=-r_2 .
\]
The degree-zero kernel is zero:
\[
  \ker A^2_{D,B}=0.
\]
Indeed the first coordinate forces the \(D^2\)-coefficient to be zero, and
then the third coordinate forces the \(B^2\)-coefficient to be zero.

The same injectivity holds in any window where the residual row \(r^M\) and
Bianchi row \(\mathfrak b^M\) are independent. In that formal free
presentation
\[
  H^0(\mathcal H^{B,\bullet}_{\theta_3,M})=0.
\]
Consequently, once the \(H^1\) transport defect of the Bianchi rows is
killed, the secondary Roos \(H^0\) obstruction vanishes automatically in
this minimal free matrix habitat.

The matrix transport required for this formal tower is
\[
  T^{M,N}r^M=r^N,\qquad
  T^{M,N}\mathfrak b^M=\mathfrak b^N,
\]
and
\[
  P^{M,N}D^M=D^N,\qquad
  P^{M,N}B^M=B^N .
\]
Then
\[
  T^{M,N}A^M=A^NP^{M,N}
\]
for the two columns \(D^M,B^M\), and
\[
  [\,P^{M,N}B^M-B^N\,]=0
  \quad\text{in}\quad
  H^0(\mathcal H^{B,\bullet}_{\theta_3,N}).
\]
This proves only the formal sufficiency of the strict tower data. The
checkout does not construct those data as Costello local functionals.

## Roos Obstruction Classes

Let \(\mathcal K^\bullet_M\) be the local-functional finite-window complex
in a proposed enlargement containing rows \(\mathfrak b^M\) and candidates
\(B^M\) with \(d_MB^M=-\mathfrak b^M\).

For \(M\geq N\), define the Bianchi-transport defect
\[
  \Delta^1_{M,N}
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N
  \in \mathcal K^1_N.
\]
Because \(d_MB^M=-\mathfrak b^M\),
\[
  d_N(\pi_{M,N}B^M-B^N)=\Delta^1_{M,N}.
\]
The first obstruction to a compatible \(B\)-tower is therefore
\[
  \operatorname{ob}^1_B
  =
  \bigl([\Delta^1_{M,N}]\bigr)_{M\geq N}
  \in C^1_{\mathrm{Roos}}\bigl(H^1(\mathcal K^\bullet_\bullet)\bigr).
\]
If this class is nonzero, the primitive difference
\(\pi_{M,N}B^M-B^N\) is not even closed in window \(N\). No Roos
\(H^0\)-class can be formed.

If \(\operatorname{ob}^1_B=0\), choose transport corrections
\[
  H^{M,N}\in \mathcal K^0_N,\qquad
  d_NH^{M,N}=\Delta^1_{M,N}.
\]
Then
\[
  \Delta^0_{M,N}
  =
  \pi_{M,N}B^M-B^N-H^{M,N}
\]
is closed. The secondary obstruction is the Roos class
\[
  \operatorname{ob}^0_B
  =
  \bigl([\Delta^0_{M,N}]\bigr)
  \in
  \varprojlim{}^1_M H^0(\mathcal K^\bullet_M).
\]
It vanishes exactly when the fixed-window primitives can be changed by
closed degree-zero terms so that the tower becomes compatible.

Thus the exact compatibility theorem for a hypothetical \(B^M\) column has
two gates:

1. \(H^1\) transport gate:
   \[
     [-\pi_{M,N}\mathfrak b^M+\mathfrak b^N]=0
     \quad\text{for all } M\geq N,
   \]
   with coherent choices \(H^{M,N}\).
2. \(H^0\) Roos gate:
   \[
     [\pi_{M,N}B^M-B^N-H^{M,N}]=0
     \quad\text{in } \varprojlim{}^1 H^0.
   \]

The current data fail before these gates can be evaluated as a theorem:
\(B^M\) and the Bianchi-row transport maps are not supplied. In the actual
window \(N=2\), even \(B^2\) is obstructed by
\(\widetilde\lambda_{02,\mathfrak b}\).

## Relation To The Eight-Face Transport

The tested eight-face companion row has vector
\[
  (2,-2,3,2,-1,1,-2,-3)
\]
on
\[
  E_{\nu_{02}},E_{\nu_{20}},E_{\nu_{03}},
  E_{\nu_{12}^{(1)}},E_{\nu_{12}^{(2)}},
  E_{\theta_3},E_{\nu_{21}^{(2)}},E_{\nu_{30}}.
\]
The current diagonal source-face transport to \(N=2\) gives
\[
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}}.
\]
In the empty lower primitive-slot presentation this is detected by
\[
  \lambda^{(2)}_{\nu_{02}}=\frac12(E^2_{\nu_{02}})^*,
  \qquad
  \lambda^{(2)}_{\nu_{02}}
  (2E^2_{\nu_{02}}-2E^2_{\nu_{20}})=1.
\]
After the formal \(B^2\) column is adjoined, this particular lower residual
would be exact:
\[
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}}
  =
  -d_{\mathrm{ns},2}(D^2_{02,20}+B^2_{02,20}).
\]
Therefore the remaining tower obstruction for the \(B\)-column is not the
old lower residual. It is the Bianchi-row transport class
\[
  [-\pi_{M,N}\mathfrak b^M+\mathfrak b^N]
  \in H^1(\mathcal K^\bullet_N),
\]
followed, if that vanishes, by the Roos \(H^0\)-class above.

## Exact Missing Data

A future positive theorem must supply all of the following.

1. A genuine local functional
   \[
     B^M\in\mathcal K^0_{\mathrm{ns},M}(I)
   \]
   for every relevant finite window.
2. Boundary and scalar projection:
   \[
     d_{\mathrm{ns},M}B^M=-\mathfrak b^M,\qquad
     \widehat\sigma_{\mathrm{sc},M}(B^M)=0.
   \]
3. Regular-density locality or a named wavefront-admissible graph/current
   habitat for \(B^M\).
4. Bianchi-row transport matrices proving
   \[
     \pi_{M,N}\mathfrak b^M=\mathfrak b^N
   \]
   or explicit \(H^{M,N}\) with
   \[
     d_NH^{M,N}=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N.
   \]
5. Primitive transport matrices for \(B^M\) satisfying
   \[
     [\pi_{M,N}B^M-B^N-H^{M,N}]=0
   \]
   in the Roos \(\varprojlim^1H^0\)-class.
6. Row-independence or kernel computation for the enlarged degree-zero
   matrix, if one wants to use the automatic \(H^0=0\) argument.

Until these are constructed, the strongest true statement is:

- current actual habitat: fixed-window \(H^1\) obstruction detected by
  \(\widetilde\lambda_{02,\mathfrak b}\);
- formal controlled enlargement: strict \(B^M\)-row and primitive transport
  gives zero Roos class;
- theorem-grade tower: blocked exactly by the \(H^1\) Bianchi transport
  class and then by the Roos \(H^0\) primitive class.

## Verification

Read anchors:

- `CLAUDE.md`
- `AGENTS.md`
- `~/ecosystem/INVARIANTS.md`
- `~/ecosystem/AGENTS-HARNESS.md`
- `.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `preamble.tex`
- `commands.tex`
- `mathmacros.tex`
- `notation.tex`
- `main.tex:8588-8878`
- `theorem-lanes.tex:3348-3508`
- `open-obligations.tex:720-887`
- `scripts/finite_window_graph_array.py:430-560`
- `scripts/finite_window_graph_array.py:980-2060`
- `reconstitution/theta3-actual-local-functional-b-column-construction-push-2026-04-30.md`
- `reconstitution/theta3-no-counterterm-controlled-enlargement-integration-spec-2026-04-30.md`
- `reconstitution/theta3-bianchi-counterterm-construction-push-2026-04-30.md`
- `reconstitution/theta3-bianchi-defect-closure-push-2026-04-30.md`
- `reconstitution/theta3-bianchi-matrix-integration-spec-2026-04-30.md`
- `reconstitution/theta3-nondiagonal-transport-counterterm-construction-push-2026-04-30.md`
- `reconstitution/theta3-controlled-enlargement-witness-search-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-257-theta3-marked-source-hom-companion-repair-push.md`
- `reconstitution/swarm-2026-04-30-agent-270-theta3-bianchi-defect-closure-push.md`

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py | head -c 20000
python3 - <<'PY'
# Bianchi-exposed A_D/A_B matrix and H^0 kernel check
PY
git status --short
```

Decisive matrix output:

```text
ell_A_D= 0
ell_A_B= -1
ell_r= 1
ell_target_minus_b= -1
d(D+B)= [-2, 2, 0]
-r= [-2, 2, 0]
small_kernel_solutions= [(0, 0)]
rank_A_DB=2, H0=0 follows from first coordinate forcing x=0 and third forcing y=0
```

The `git status --short` scan showed many pre-existing staged, modified,
and untracked files from the concurrent swarm. This report touched only the
two Agent 299 owned reconstitution paths.

## Files Changed

- `reconstitution/theta3-roos-transport-obstruction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-299-theta3-roos-transport-obstruction-push.md`
