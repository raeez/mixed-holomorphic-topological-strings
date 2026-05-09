# Radial summary propagation final audit

Date: 2026-04-30.

Agent: 325.

Scope: audit only.  No manuscript TeX or script file was edited.

## Claim attacked

After Agent 320, every summary that mentions the all-\(N\) radial/Weyl
ordinary trace input should carry the full theorem surface:
\[
  \Omega^{\mathrm{rad}}_{a,b}
  =
  [(T_{a,b},E^+_{a,b})]\in\operatorname{coker}B_{a,b},
  \qquad
  B_{a,b}(W)=(\partial W,C^+_{a,b}(W)).
\]
The positive target is \(\Omega^{\mathrm{rad}}_{a,b}=0\), equivalently the
decorated PBW Stokes condition
\[
  D^\square_{a,b}=C^+_{a,b}\partial_2
\]
with no residual left-cokernel value on \(R^{\mathrm{free}}_{a,b}\).  Failure
is exactly a signed row
\[
  (\phi,-\lambda)\in\ker B_{a,b}^*,
  \qquad
  \lambda(E^+_{a,b})-\phi(T_{a,b})\ne0.
\]

## Inputs read

- `main.tex`
- `theorem-lanes.tex`
- `open-obligations.tex`
- `claim-strength-ledger.tex`
- `appendix-radial-parts-moyal.tex`
- Agent 303 reports:
  `reconstitution/radial-decorated-pbw-stokes-identity-construction-push-2026-04-30.md`,
  `reconstitution/swarm-2026-04-30-agent-303-radial-decorated-pbw-stokes-identity-construction-push.md`
- Agent 314 reports:
  `reconstitution/radial-all-n-decorated-pbw-stokes-attack-heal-2026-04-30.md`,
  `reconstitution/swarm-2026-04-30-agent-314-radial-all-n-decorated-pbw-stokes-attack-heal.md`
- Agent 320 reports:
  `reconstitution/radial-obstruction-surface-propagation-audit-2026-04-30.md`,
  `reconstitution/swarm-2026-04-30-agent-320-radial-obstruction-surface-propagation-audit.md`

The non-`swarm-*` report copies are not byte-identical to the `swarm-*`
copies; the non-`swarm-*` Agent 303 and Agent 314 reports contain the fuller
post-Stokes surface.  The current TeX changed during this audit, so all line
anchors below are from the final re-read before this report was written.

## Result

Status: partial propagation.  Several Agent 320 defects have been healed in
the current checkout.  The main theorem summary, the principal degree-zero
lane, the detailed open-obligations radial item, and the detailed ledger item
now carry \(\Omega^{\mathrm{rad}}\), decorated Stokes, and signed-row language.
Residual summary-level defects remain in `main.tex`, `theorem-lanes.tex`,
`claim-strength-ledger.tex`, and in the appendix theorem infrastructure.

Correctly propagated surfaces:

- `main.tex:1055-1080`: early quantum-data summary now states
  \(\Omega^{\mathrm{rad}}\), \(D^\square\), and signed-row failure.
- `main.tex:2750-2779`: local theorem package summary includes the full
  dual-potential and decorated Stokes surface.
- `main.tex:7414-7439`: `thm:finite-n-reduced-moyal` now states the
  \(\Omega^{\mathrm{rad}}\)/\(D^\square\)/signed-row equivalence.
- `main.tex:7628-7642`: Hamiltonian-sector status remark now includes the
  dual-potential obstruction and signed-row criterion.
- `main.tex:8294-8315`: `thm:phi-hbar-all-order` item (3) now includes
  \(\Omega^{\mathrm{rad}}\), decorated Stokes, and signed-row failure.
- `theorem-lanes.tex:2530-2555`: degree-zero Moyal/Weyl lane states the full
  obstruction theorem target.
- `theorem-lanes.tex:2670-2683`: scope clause names the signed row and
  \(\Omega^{\mathrm{rad}}\).
- `theorem-lanes.tex:2774-2783`: componentwise proof-input paragraph cites
  the dual-potential proposition and \(D^\square\).
- `theorem-lanes.tex:3646-3689`: radial trace-diagram lane now states
  \(\Omega^{\mathrm{rad}}\), decorated Stokes, and signed-row failure.
- `open-obligations.tex:512-529`: componentwise theorem datum summary is
  repaired.
- `open-obligations.tex:1350-1440`: detailed radial/Weyl obligation item is
  repaired.
- `claim-strength-ledger.tex:987-1043`: detailed radial/Weyl ledger item is
  repaired.
- `appendix-radial-parts-moyal.tex:965-1027`: dual-potential proposition
  states \(\Omega^{\mathrm{rad}}\), \(D^\square\), and signed-row failure.

## Remaining TeX defects and patch targets

1. `main.tex:2434-2442`.
   This high-level theorem narrative still says the remaining uniform radial
   theorem is compatible \(K_{a,b}\) or a left-cokernel theorem for
   \(\mathfrak o_{a,b}\).  Patch to the full
   \(\Omega^{\mathrm{rad}}\)/\(D^\square\)/signed-row surface.

2. `main.tex:7554-7563`.
   `cor:degree-zero-quantum-upgrade` still summarizes the ordinary Weyl-trace
   obstruction as \(\mathfrak o_{a,b}=0\) with functorial lifts or an
   equivalent left-cokernel theorem.  Patch the corollary statement to point to
   \(\Omega^{\mathrm{rad}}_{a,b}=0\), decorated PBW Stokes, and signed
   \(B_{a,b}^*\)-rows.

3. `main.tex:8430-8435`.
   The componentwise coefficient-surface theorem introduces
   \(T_{\mathrm{Ham},\hbar}\) using only \(\mathfrak o_{a,b}\), homotopy, and
   left-cokernel language.  Patch this local definition of the fourth factor
   to include the accepted dual-potential obstruction surface.

4. `main.tex:8545-8548`.
   The proof of the componentwise theorem says the all-interior
   ordinary-trace comparison is the named radial-normalization obstruction, but
   does not name the \(\Omega^{\mathrm{rad}}\)/\(D^\square\)/signed-row form.
   Patch by citing `prop:app-radial-dual-potential-obstruction`.

5. `theorem-lanes.tex:2718-2723`.
   The componentwise coefficient-surface local assertion still says the
   remaining interior bidegrees require a functorial kernel homotopy or
   left-cokernel vanishing theorem.  Patch that sentence to state the
   equivalent dual-potential signed-row theorem.

6. `claim-strength-ledger.tex:103-109`.
   Stage A6a names the finite-certificate-relative radial/Weyl trace comparison
   with a uniform-homotopy gate but omits the exact obstruction surface.  Patch
   the stage summary to name \(\Omega^{\mathrm{rad}}\), \(D^\square\), and
   signed-row failure.

7. `claim-strength-ledger.tex:207-215`.
   The top claim table's radial/Weyl row remains old
   \(\mathcal C_{a,b}\)-splitting language only.  Patch to the full
   obstruction theorem surface.

8. `claim-strength-ledger.tex:300-308`.
   The radial trace-diagram branch row remains
   \(\operatorname{coker}\mathcal C_{a,b}\), uniform contracting homotopy, or
   left-cokernel language only.  Patch to the \(B_{a,b}\)-cokernel,
   \(D^\square\), and signed-row criterion.

9. `claim-strength-ledger.tex:577-585`.
   The frontier item "Radial all-\(N\) image and all-bidegree homotopy" still
   says functorial splitting of \(\mathcal C_{a,b}\) and left-cokernel
   detection.  Patch to \(\Omega^{\mathrm{rad}}\) and normalized signed-row
   failure.

10. `claim-strength-ledger.tex:1238-1270`.
    The quantum Hamiltonian/Moyal sector item still ends at the
    \(\operatorname{coker}\mathcal C_{a,b}\) and uniform contracting homotopy
    formulation.  Patch to cite the dual-potential obstruction theorem and the
    \(D^\square\) decorated Stokes gate.

11. `claim-strength-ledger.tex:1288-1294`.
    The componentwise quantum coefficient surface summary still says
    "finite-certificate radial/Weyl gate and uniform-homotopy obstruction".
    Patch to name the same \(\Omega^{\mathrm{rad}}\)/\(D^\square\)/signed-row
    theorem surface.

12. `appendix-radial-parts-moyal.tex:888-939`.
    The decorated Hodge obstruction theorem remains an
    \(A_{a,b}=C^+|_{\ker\partial}\) theorem only.  Add the reader-facing
    equivalence with \(\Omega^{\mathrm{rad}}_{a,b}=0\), \(B_{a,b}\), and
    signed-row failure, or explicitly point forward to
    `prop:app-radial-dual-potential-obstruction`.

13. `appendix-radial-parts-moyal.tex:965-1027`.
    The dual-potential proposition names \(D^\square\), but still does not
    formally define the square-cell complex \(C^\square_\bullet(a,b)\), prove
    \(\operatorname{im}\partial_2=\ker\partial\) over \(\mathbb Q\), or state
    the explicit left-cokernel Stokes criterion
    \(\lambda D^\square_{a,b}=0\Rightarrow
    \lambda(R^{\mathrm{free}}_{a,b})=0\).  Insert the square-cell refinement
    around this proposition.

14. `appendix-radial-parts-moyal.tex:1061-1111`.
    The potential-form remark distinguishes the bare graph Green operator from
    \(A_{a,b}A_{a,b}^*\), but not from the proved ordinary square-cell cycle
    mechanism and the still-missing decorated Stokes identity.  Patch the
    remark to say ordinary square cells generate \(\ker\partial\), while
    \(D^\square=C^+\partial_2\) decides the PBW/split-trace/Capelli decorated
    residual.

15. `appendix-radial-parts-moyal.tex:1434-1440`.
    The proof of `thm:app-radial-finite-N` still describes the exact target as
    moment-ideal primitives, free corrections \(K_{a,b}\), or a left-cokernel
    obstruction.  Patch to include the dual-potential and decorated Stokes
    normal form.

16. `appendix-radial-parts-moyal.tex:1820-1830`.
    The final proof item cites only the primitive and Hodge obstruction
    formulations.  Patch to include
    `prop:app-radial-dual-potential-obstruction` and the \(D^\square\)
    criterion.

## Attack-heal conclusion

The all-\(N\) radial/Weyl trace input remains an exact obstruction theorem,
not a proved all-bidegree vanishing theorem.  The invariant that must appear
in every summary is:
\[
  \Omega^{\mathrm{rad}}_{a,b}=0
  \Longleftrightarrow
  (T_{a,b},E^+_{a,b})\in\operatorname{im}B_{a,b}
  \Longleftrightarrow
  R^{\mathrm{free}}_{a,b}\in\operatorname{im}D^\square_{a,b},
\]
with failure precisely a signed row
\((\phi,-\lambda)\in\ker B_{a,b}^*\) detecting a nonzero value
\(\lambda(E^+_{a,b})-\phi(T_{a,b})\).  The remaining defects above are patch
targets only; no TeX was edited in this pass.

## Commands run

- `sed -n` and `nl -ba` on the requested TeX files and reports.
- `rg` for `radial/Weyl`, `ordinary Weyl-trace`,
  `Omega^{\mathrm{rad}}`, `D^\square`, `signed row`,
  `\mathcal C_{a,b}`, `left-cokernel`, and homotopy language.
- `cmp -s` on the non-`swarm-*` and `swarm-*` copies of Agent 303, 314, and
  320 reports; all three pairs differed.
- `git status --short` on the target TeX files and requested report paths.

No build was run.  This was a report-only audit.
