# Appendix theta3/QME notation propagation audit, 2026-04-30

Report-only audit. No manuscript TeX edited. No build run.

## Claim attacked

After Agent 322, the appendices might still be a stale notation source for the
first `theta_3` non-scalar QME obstruction. The possible failure modes were:

- `\mathcal Q`/`\mathcal K` drift for the non-scalar kernel complex;
- missing appendix propagation of `A_D^2`, `r_2`, `A_B^2`, and
  `\Delta^1_{M,N}`;
- accidental promotion of the algebraic current interface to a non-scalar
  Costello/QME theorem;
- a false claim that the current appendix already contains a `B^2_{02,20}`
  local-functional counterterm.

## Verdict

No live TeX contradiction was found. The current main theorem surface is
mathematically enough: `main.tex:8810-9016`, `theorem-lanes.tex:3448-3591`,
`open-obligations.tex:793-955`, and
`claim-strength-ledger.tex:921-991` all keep the `theta_3` one-row obstruction,
the lower Bianchi matrix, and the tower transport obstruction separate.

The appendix is not yet the complete notation source. This is a propagation
gap, not a theorem failure. If TeX editing is opened, patch
`appendix-unreduced-bv-qme.tex` now with a short convention and a short
Bianchi-exposed corollary. `appendix-factorization-current-conventions.tex`
does not require a theta3-specific patch for correctness; it already states
the non-scalar current lift as an obstruction habitat, not a solved QME.

## Evidence

The main acceptance gate states the live notation:

- `main.tex:8815-8828`: one-row `\mathcal Q_{\theta_3,M}` complex and
  `\mathsf E_{\theta_3,M}`.
- `main.tex:8964-8977`: `A_D^2=(-2,2,1)^T`, `r_2=(2,-2,0)^T`, and
  the detecting cokernel.
- `main.tex:9000-9015`: required `A_B^2=(0,0,-1)^T` and
  `\Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N`.

The theorem lane repeats the same matrix:

- `theorem-lanes.tex:3463-3469`: one-row
  `\mathcal K_{\theta_3,M}` complex.
- `theorem-lanes.tex:3552-3591`: `A_D^2`, `r_2`, `A_B^2`, and
  `\Delta^1_{M,N}`.

The appendices currently stop one level earlier:

- `appendix-unreduced-bv-qme.tex:2224-2231` defines
  `\mathcal K^\bullet_{\mathrm{ns},M}(I)=\ker\widehat\sigma_{\mathrm{sc},M}`.
- `appendix-unreduced-bv-qme.tex:2302-2333` gives the generic matrix test
  `A^M c=-r^M` and Roos primitive class.
- `appendix-unreduced-bv-qme.tex:2416-2455` gives the first `theta_3`
  one-row obstruction in `\mathcal K_{\theta_3,M}`.
- It does not record the lower Bianchi basis
  `(E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})`, `A_D^2`,
  `r_2`, `A_B^2`, or `\Delta^1_{M,N}`.

The factorization-current appendix remains correctly scoped:

- `appendix-factorization-current-conventions.tex:1030-1042` says the
  algebraic current theorem does not prove the mixed brane-defect QME.
- `appendix-factorization-current-conventions.tex:1045-1118` defines the
  unreduced non-scalar current lift datum.
- `appendix-factorization-current-conventions.tex:1954-2033` lists the scalar,
  reduced-interface, centrality-homotopy, and residual non-scalar obstruction
  maps.

The script check was run:

```sh
python3 scripts/finite_window_graph_array.py
```

It verifies the one-row `theta_3` finite subcomplex and accepts only payloads
with an explicit `dC=-E` differential entry. It does not emit the
three-coordinate lower Bianchi matrix `A_D^2,r_2,A_B^2`.

## Attack-heal decision

1. `Q/K` consistency is compatible but not clean. In the main theorem surface,
   the finite-window non-scalar tower is `\mathcal Q^\bullet_{w,M}`. In the
   appendix and theorem lane, the same kernel is often called
   `\mathcal K^\bullet_{\mathrm{ns},M}` or `\mathcal K_{\theta_3,M}`. This
   is not false, because both mean `\ker\widehat\sigma_{\mathrm{sc},M}`.
   It should nevertheless be patched by a convention sentence.

2. `A_D^2/r_2/A_B^2/\Delta^1` should be propagated to
   `appendix-unreduced-bv-qme.tex` if the appendix is expected to be
   self-contained. The main theorem surface is enough to block the false
   theorem, but a reader using only the appendix will miss the current
   lower Bianchi notation.

3. `appendix-factorization-current-conventions.tex` should not duplicate the
   theta3 matrix unless the manuscript policy becomes "all QME notation lives
   in appendices." Its current role is the current-interface and habitat
   boundary. A one-sentence pointer is optional.

## Exact patch targets

Patch target 1: `appendix-unreduced-bv-qme.tex`, immediately after
`def:app-native-finite-window-realization-habitat`, currently after
`appendix-unreduced-bv-qme.tex:2224-2231`.

Purpose: equate notations.

Required content:

```tex
In the main theorem lane the same non-scalar finite-window kernel is denoted
\(\mathcal Q^\bullet_{w,M}(I)\). Thus
\[
  \mathcal Q^\bullet_{w,M}(I)
  =
  \mathcal K^\bullet_{\mathrm{ns},M}(I)
  =
  \ker\widehat\sigma_{\mathrm{sc},M}
\]
on any habitat where the scalar projection is a chain map. The one-row
\(\theta_3\) subcomplex below may therefore be written either
\(\mathcal Q^\bullet_{\theta_3,M}\) or
\(\mathcal K^\bullet_{\theta_3,M}\).
```

Patch target 2: `appendix-unreduced-bv-qme.tex`, after
`prop:app-closed-rows-and-theta-three-source-face` and its proof, currently
after `appendix-unreduced-bv-qme.tex:2485`.

Purpose: propagate the lower Bianchi matrix without changing theorem strength.

Required content: a corollary or remark headed
`Bianchi-exposed lower theta_3 matrix`, cross-referencing
`prop:theta-three-finite-window-acceptance-gate`, with exactly these data:

```tex
\[
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},\qquad
  D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2),
  \qquad
  d_{\mathrm{CE}}\zeta^0_2=2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]
\[
  \mathfrak b^2_{02,20}
  =
  d_{\mathrm{ns},2}K^2_{\Theta_3}(\zeta^0_2)
  -
  K^2_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_2),
\]
and in the basis
\((E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})\),
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T.
\]
The current habitat contains no \(B^2_{02,20}\) column; the required
enlargement is
\[
  A_B^2=(0,0,-1)^T,\qquad
  d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}.
\]
For a tower the transport obstruction is
\[
  \Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N
  =
  d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N),
\]
with the associated \(H^1\) and secondary \(\varprojlim^1H^0\) classes.
```

The corollary must explicitly say that this is a notation propagation and a
fixed-window obstruction certificate, not a constructed Costello graph/QME
solution.

Patch target 3, optional: `appendix-factorization-current-conventions.tex`,
inside `prop:app-nonscalar-current-lift-obstructions`, after item (4), current
anchor `appendix-factorization-current-conventions.tex:2011-2025`.

Purpose: add a pointer only:

```tex
For the first tested larger source-face row, this residual is the
\(\theta_3\) gate of Proposition~\ref{prop:theta-three-finite-window-acceptance-gate};
the coefficient-current kernel does not supply the missing
\(A_B^2\) column or the \(\Delta^1_{M,N}\) transport primitive.
```

This optional pointer is useful, but not required for correctness.

Patch target 4, optional machine gate: `scripts/finite_window_graph_array.py`,
near the `theta3_eight_face_candidate_obstruction_check` block. Add a separate
record for the Bianchi-exposed lower matrix if future acceptance gates require
machine output for `A_D^2=(-2,2,1)^T`, `r_2=(2,-2,0)^T`,
`A_B^2=(0,0,-1)^T`, and the cokernel evaluation.

## Files changed

- `reconstitution/appendix-theta3-qme-notation-propagation-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-326-appendix-theta3-qme-notation-propagation-audit.md`

