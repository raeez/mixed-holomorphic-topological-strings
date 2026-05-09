# Agent 221 - Theta3 Marked Companion-Face Integration

## Status

Integrated Agent 215's companion-face attempt into the Tate finite-window
theta3 theorem surface as an obstruction theorem.  No companion cancellation
is claimed.  The current one-row obstruction remains active until the marked
Costello incidence/weight table is supplied.

## Manuscript Anchors

- `tate-P1-hadamard-mittag-leffler.tex:2092`: primitive and local-counterterm
  acceptance gate preserved.
- `tate-P1-hadamard-mittag-leffler.tex:2171`: companion-face gate kept
  separate from primitive search.
- `tate-P1-hadamard-mittag-leffler.tex:2226`: new
  `theta_3` companion-face construction obstruction theorem.
- `tate-P1-hadamard-mittag-leffler.tex:2248`: eight candidate faces.
- `tate-P1-hadamard-mittag-leffler.tex:2281`: signed residual
  \(R^{\mathrm{cand}}_{\Theta_3,M}\).
- `tate-P1-hadamard-mittag-leffler.tex:2293`: diagonal \(v^{M,N}\)
  source-face transport.
- `tate-P1-hadamard-mittag-leffler.tex:2307`: lower-window \(N=2\)
  residual \(2E^2_{\nu_{02}}-2E^2_{\nu_{20}}\).
- `tate-P1-hadamard-mittag-leffler.tex:2317`: exact missing marked Costello
  incidence/weight table.

## Stable Core

The primitive gates remain:
\[
  A^M_{\theta_3,C}=-1,\qquad
  d_{\mathrm{ns},M}C_{\theta_3,M}=-\mathsf E_{\theta_3,M},
  \qquad
  T^{M,N}A^M=A^NP^{M,N}.
\]
The CE-ancestor and local-counterterm cases are accepted only after this
degree-zero column, scalar projection zero, identity/zero transport, and
zero Roos class are supplied.

Agent 215's table gives a source-algebraic companion route, not a primitive:
\[
\begin{aligned}
  R^{\mathrm{cand}}_{\Theta_3,M}
    ={}&2E^M_{\nu_{02}}-2E^M_{\nu_{20}}
        +3E^M_{\nu_{03}}+2E^M_{\nu_{12}^{(1)}}
        -E^M_{\nu_{12}^{(2)}}\\
     &+\mathsf E_{\theta_3,M}
        -2E^M_{\nu_{21}^{(2)}}-3E^M_{\nu_{30}} .
\end{aligned}
\]
This residual is not proved zero.  The diagonal transport keeps degrees
\(\leq N\) and exposes the lower-window residual
\[
  \pi_{M,2}R^{\mathrm{cand}}_{\Theta_3,M}
    =
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}}.
\]

## Exact Residual Obligation

The missing theorem datum is
\[
  \left(
    d_{\mathrm{CE}}\zeta_M,\,
    \epsilon^{\mathrm{CE}}_{\Theta_3,\nu},\,
    K^M_{\Theta_3}(\zeta_{M,\nu}),\,
    \mu_\nu,\,
    v^{M,N}_{\nu;\nu'},\,
    \mathcal C^{(2)}_{\nu,\nu'}
  \right)_{\nu,\nu'} .
\]
It must provide every marked output, marker transport, orientation/Koszul
coefficient, renormalized row coordinate, codimension-two closure entry, and
lower-window transport identity.  Without it, the one-row obstruction of
Proposition `prop:theta-three-finite-row-obstruction` remains the theorem
surface.

## Checks

- `git diff --check -- tate-P1-hadamard-mittag-leffler.tex
  reconstitution/swarm-2026-04-30-agent-221-theta3-marked-companion-face-integration.md`:
  passed.
- `git diff --cached --check -- tate-P1-hadamard-mittag-leffler.tex
  reconstitution/swarm-2026-04-30-agent-221-theta3-marked-companion-face-integration.md`:
  passed after staging.
- `python3 -m py_compile scripts/finite_window_graph_array.py`: passed.
- Focused theta3 validator inspection: current one-row obstruction remains
  unsolved; CE-ancestor and counterterm exact payload fixtures accept only
  with differential entry \(-1\); incomplete one-face companion table rejects;
  cancelling coordinates without CE verification reject.

No PDF build was run because it would write build artifacts outside the two
owned paths in a concurrent shared checkout.

## Files Changed

- `tate-P1-hadamard-mittag-leffler.tex`
- `reconstitution/swarm-2026-04-30-agent-221-theta3-marked-companion-face-integration.md`
