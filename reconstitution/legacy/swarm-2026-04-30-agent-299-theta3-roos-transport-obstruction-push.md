# Agent 299 - Theta3 Roos Transport Obstruction Push

## Claim Attacked

The attacked claim is that the lower \(\theta_3\) Bianchi counterterm can be
promoted from the fixed-window target
\[
  A_B^2=(0,0,-1)^T
\]
to a compatible finite-window tower \(B^M\) using the data currently present
in the checkout.

I tried to construct the compatible tower data. The only construction found
is formal: adjoin \(B^M\) in every window, impose
\[
  d_MB^M=-\mathfrak b^M,\qquad
  \pi_{M,N}\mathfrak b^M=\mathfrak b^N,\qquad
  \pi_{M,N}B^M=B^N .
\]
This gives \(TA=AP\) and zero Roos class. It is not a theorem-grade
construction, because the local functional \(B^M\), scalar-zero value,
locality or wavefront habitat, and Bianchi transport matrices are absent.

## Fixed-Window Obstruction

The current \(N=2\) Bianchi-exposed lower basis is
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}).
\]
The only current degree-zero column is
\[
  A_D^2=(-2,2,1)^T.
\]
The desired Bianchi counterterm column is
\[
  A_B^2=(0,0,-1)^T.
\]
The cokernel
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
Thus \(B^2_{02,20}\) is not present in the actual finite-row habitat. The
actual current obstruction is fixed-window \(H^1\), before a Roos \(H^0\)
compatibility class can be formed.

## Formal Positive Tower

If \(B^M\) is adjoined as a genuine column, the lower matrix at \(N=2\) is
\[
  A^2_{D,B}
  =
  \begin{pmatrix}
    -2&0\\
     2&0\\
     1&-1
  \end{pmatrix}.
\]
Then
\[
  d(D^2+B^2)=(-2,2,0)^T=-r_2.
\]
The kernel is zero:
\[
  \ker A^2_{D,B}=0.
\]
Hence \(H^0=0\) in the minimal free Bianchi-exposed lower extension. If the
same row-independence holds in every window, the secondary Roos
\(\varprojlim^1H^0\) obstruction vanishes automatically once the \(H^1\)
Bianchi transport defect is killed.

This formal construction is exactly the acceptance target. It is not
contained in the present graph/local-functional data.

## Exact Roos Classes

For a proposed tower with
\[
  d_MB^M=-\mathfrak b^M,
\]
the first obstruction is the \(H^1\) transport defect
\[
  \Delta^1_{M,N}
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N.
\]
Since
\[
  d_N(\pi_{M,N}B^M-B^N)=\Delta^1_{M,N},
\]
the primitive difference is closed only if
\[
  [\Delta^1_{M,N}]=0
  \quad\text{in}\quad
  H^1(\mathcal K^\bullet_N).
\]
This is the Roos \(H^1\) gate.

If it vanishes and one chooses
\[
  H^{M,N}\in\mathcal K^0_N,\qquad
  d_NH^{M,N}=\Delta^1_{M,N},
\]
then
\[
  \Delta^0_{M,N}
  =
  \pi_{M,N}B^M-B^N-H^{M,N}
\]
is closed. The secondary obstruction is
\[
  [\Delta^0]\in
  \varprojlim{}^1_M H^0(\mathcal K^\bullet_M).
\]
This class vanishes exactly when the fixed-window primitives can be chosen
compatibly.

In the current checkout the class cannot be evaluated as zero: the
Bianchi-row transport \(\pi_{M,N}\mathfrak b^M\) is not supplied, and even
the \(N=2\) column \(B^2\) is obstructed by
\(\widetilde\lambda_{02,\mathfrak b}\).

## Relation To The Eight-Face Residual

The eight-face companion candidate transports diagonally to
\[
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}},
\]
detected in the empty lower primitive slots by
\[
  \lambda^{(2)}_{\nu_{02}}=\frac12(E^2_{\nu_{02}})^*.
\]
If a genuine \(B^2\) were adjoined, this specific lower residual would
become exact:
\[
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}}
  =
  -d(D^2+B^2).
\]
The remaining tower question would then be precisely the Bianchi-row
transport class
\[
  [-\pi_{M,N}\mathfrak b^M+\mathfrak b^N]
\]
and, after it is killed, the Roos \(H^0\) class above.

## Claim-Status Recommendation

Allowed:

- The actual current finite-row habitat has no \(B^2_{02,20}\).
- The obstruction is the fixed-window cokernel
  \(\widetilde\lambda_{02,\mathfrak b}\).
- A formal \(B^M\)-tower with strict Bianchi and primitive transport has
  zero Roos class.
- The theorem-grade tower is blocked exactly by the \(H^1\) Bianchi
  transport class, then by the \(\varprojlim^1H^0\) primitive class.

Forbidden without new data:

- A Costello local-functional \(B^M\) exists.
- The Bianchi rows transport strictly.
- The Roos primitive class is closed or zero.
- The validator's supplied-exact payload is current mathematics rather than
  an interface fixture.

## Verification

Read:

- `CLAUDE.md`
- `AGENTS.md`
- `~/ecosystem/INVARIANTS.md`
- `~/ecosystem/AGENTS-HARNESS.md`
- `.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `preamble.tex`, `commands.tex`, `mathmacros.tex`, `notation.tex`
- `main.tex:8588-8878`
- `theorem-lanes.tex:3348-3508`
- `open-obligations.tex:720-887`
- `scripts/finite_window_graph_array.py:430-560`
- `scripts/finite_window_graph_array.py:980-2060`
- theta3 Agent 257, 263, 270, 277, 282, 287, and 294 reports

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py | head -c 20000
python3 - <<'PY'
# Bianchi-exposed A_D/A_B matrix and H^0 kernel check
PY
git status --short
```

Decisive output:

```text
ell_A_D= 0
ell_A_B= -1
ell_r= 1
d(D+B)= [-2, 2, 0]
-r= [-2, 2, 0]
small_kernel_solutions= [(0, 0)]
```

## Files Changed

- `reconstitution/theta3-roos-transport-obstruction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-299-theta3-roos-transport-obstruction-push.md`
