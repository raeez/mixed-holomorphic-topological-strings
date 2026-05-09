# Agent 313 - Theta3 Restricted Counterterm Theorem Frontier

Date: 2026-04-30.
Ownership: report-only. No TeX edits.

## Claim Attacked

Construct the theta3 restricted-habitat counterterm theorem, namely a genuine
scalar-zero local functional
\[
  B^2_{02,20}\in\mathcal K^0_{\mathrm{ns},2}(I)
\]
with
\[
  d_{\mathrm{ns},2}B^2_{02,20}
  =
  -\mathfrak b^2_{02,20},
  \qquad
  A_B^2=(0,0,-1)^T,
\]
plus locality or wavefront admissibility and finite-window tower transport.

## Result

Blocked. The current checkout does not construct \(B^2_{02,20}\) as a
Costello local functional. The formal column \(A_B^2=(0,0,-1)^T\) is the
right acceptance target, but it is not present in the restricted habitat.

The exact fixed-window obstruction is
\[
  \mathcal H^0_{\mathrm{cur}}=\mathbb C D^2_{02,20},
  \qquad
  \mathcal H^1_{\mathrm{cur}}
  =
  \mathbb C E^2_{\nu_{02}}
  \oplus
  \mathbb C E^2_{\nu_{20}}
  \oplus
  \mathbb C\mathfrak b^2_{02,20},
\]
with
\[
  D^2_{02,20}=K^2_{\Theta_3}(u_{a,H_{1,0}}u_{b,H_{0,1}}),
\]
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
  +\mathfrak b^2_{02,20}.
\]
Thus
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T.
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
  \widetilde\lambda_{02,\mathfrak b}(r_2)=1,\qquad
  \widetilde\lambda_{02,\mathfrak b}((0,0,-1)^T)=-1.
\]

## Formal Positive Target

If a genuine \(B^2_{02,20}\) is supplied, the lower matrix becomes
\[
  A^2_{D,B}
  =
  \begin{pmatrix}
    -2&0\\
     2&0\\
     1&-1
  \end{pmatrix},
\]
and
\[
  d_{\mathrm{ns},2}(D^2_{02,20}+B^2_{02,20})
  =
  (-2,2,0)^T=-r_2.
\]
This closes the fixed \(N=2\) matrix. It is theorem-grade only after the
actual local functional, scalar-zero projection, regular-density or
wavefront locality, and transport maps are built.

## Transport Obstruction

For a proposed tower \(B^M\), define
\[
  \Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N.
\]
Then
\[
  d_N(\pi_{M,N}B^M-B^N)=\Delta^1_{M,N}.
\]
The \(H^1\) gate is the vanishing of \([\Delta^1_{M,N}]\). If it is killed by
\[
  H^{M,N}\in\mathcal K^0_{\theta_3,N},
  \qquad
  d_NH^{M,N}=\Delta^1_{M,N},
\]
the secondary obstruction is
\[
  [\pi_{M,N}B^M-B^N-H^{M,N}]
  \in
  \varprojlim\nolimits^1_M
  H^0(\mathcal K^\bullet_{\theta_3,M}).
\]
The current data do not supply \(\pi_{M,N}\mathfrak b^M\), \(H^{M,N}\), or
the secondary zero class.

## TeX Patch Targets

Do not apply without later manuscript-edit authorization.

- `main.tex:8859-8867`: name
  \(\Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N\), then add the
  correction \(d_NH^{M,N}=\Delta^1_{M,N}\) and the secondary
  \(\varprojlim^1H^0\) class.
- `theorem-lanes.tex:3538-3541`: after the \(A_B^2=(0,0,-1)^T\) target,
  insert the same named \(\Delta^1\) and secondary class.
- `open-obligations.tex:897-905`: keep the displayed \(D\)-candidate
  transport sign, then add the opposite \(B\)-counterterm sign
  \(\Delta^1_{M,N}=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N\).
- `claim-strength-ledger.tex:950-954`: replace schematic Roos compatibility
  by the named \(\Delta^1\) gate and secondary
  \(\varprojlim^1H^0\) gate.

The detailed insertion blocks are in
`reconstitution/theta3-restricted-counterterm-theorem-frontier-2026-04-30.md`.

## Evidence

Read the requested governing files, manuscript/control anchors, and reports
for agents 294, 299, 301, 304, and 309. No agent-308 report was present under
`reconstitution/`.

Verification commands:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
rg -n "theta3|Theta_3|theta_3|B\^2_\{02,20\}|mathfrak b\^2|Delta\^1|lim\^1|secondary" main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex reconstitution -S
```

Decisive script evidence:

- current theta3 finite-row subcomplex has no primitive;
- counterterm payload without \(dC=-E\) is rejected;
- supplied exact payload is accepted only as an interface fixture;
- eight-face candidate is rejected and transports to
  \(2E^2_{\nu_{02}}-2E^2_{\nu_{20}}\) at \(N=2\).

## Files Changed

- `reconstitution/theta3-restricted-counterterm-theorem-frontier-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-313-theta3-restricted-counterterm-theorem-frontier.md`
