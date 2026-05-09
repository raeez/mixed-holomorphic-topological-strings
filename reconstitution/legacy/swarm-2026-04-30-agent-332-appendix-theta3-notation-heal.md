# Swarm 2026-04-30 Agent 332: Appendix theta3/QME Notation Heal

Status: appendix TeX patch plus report.  No build run.

## Claim Attacked

The appendix QME lane still lagged the live theta3 notation audit: it named
the one-row \(\theta_3\) obstruction but did not carry the lower
Bianchi-exposed matrix
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T,
\]
the missing scalar-zero local-functional column
\[
  A_B^2=(0,0,-1)^T,
\]
or the transport cocycle \(\Delta^1_{M,N}\).  It also did not explicitly
identify the windowed scalar-zero \(\mathcal Q\) notation with the appendix
non-scalar kernel \(\mathcal K_{\mathrm{ns}}\).

## Patch

- `appendix-unreduced-bv-qme.tex`: added a convention in
  `def:app-native-finite-window-realization-habitat`:
  \[
    \mathcal Q^\bullet_{w,M}(I)
      =
    \mathcal K^\bullet_{\mathrm{ns},M}(I)
      =
    \ker\widehat\sigma_{\mathrm{sc},M}.
  \]
- `appendix-unreduced-bv-qme.tex`: added
  `prop:app-theta-three-bianchi-exposed-lower-gate` after
  `prop:app-closed-rows-and-theta-three-source-face`.

## Fixed-Window Certificate

In the basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}),
\]
the source-coordinate primitive
\[
  D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2)
\]
has column
\[
  A_D^2=(-2,2,1)^T,
\]
while the lower residual is
\[
  r_2=(2,-2,0)^T.
\]
The equation \(A_D^2c=-r_2\) is inconsistent: the first two coordinates
force \(c=1\), and the Bianchi coordinate forces \(c=0\).  The cokernel
\[
  \widetilde\lambda_{02,\mathfrak b}
    =
  \frac12(E^2_{\nu_{02}})^*
    +(\mathfrak b^2_{02,20})^*
\]
kills \(A_D^2\) and evaluates to \(1\) on \(r_2\).

The target
\[
  -\mathfrak b^2_{02,20}=(0,0,-1)^T
\]
is not in the current image because the same cokernel evaluates to \(-1\).
The required controlled-enlargement column is
\[
  A_B^2=(0,0,-1)^T,\qquad
  d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}.
\]
This is recorded as a target, not as a constructed Costello local
functional.

## Transport Gate

For a tower \(B^M\), the appendix now names
\[
  \Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N.
\]
The repair transports only if
\[
  \Delta^1_{M,N}
    =
  d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N),
\]
possibly after an explicitly supplied scalar-zero transport correction.
Thus the \(H^1\) transport class must vanish before the secondary
\[
  \varprojlim\nolimits^1_N
  H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I))
\]
primitive-compatibility class is even the right gate.

## Verification

Commands run:

```sh
rg -n "mathcal Q|Bianchi-exposed lower gate|A_D\\^2|r_2|A_B\\^2|Delta\\^1|varprojlim|theta_3" appendix-unreduced-bv-qme.tex
git diff --check -- appendix-unreduced-bv-qme.tex
git diff --cached --check -- appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-332-appendix-theta3-notation-heal.md
```

Result: `git diff --check` passed on the touched files.

## Files Changed

- `appendix-unreduced-bv-qme.tex`
- `reconstitution/swarm-2026-04-30-agent-332-appendix-theta3-notation-heal.md`
