# BMK Current-Limit Obstruction Integration Spec, 2026-04-30

## Verdict

Agent 276 turns the BMK finite-window lane from a proved transfer theorem
into a partially constructed current-limit package with a named
finite-window obstruction.  The manuscript must not assert
\[
  \bar\partial H_{\chi,N}+H_{\chi,N}\bar\partial
  =
  \operatorname{id}-i_Np_N+E_{\chi,N}
\]
on the undeclared compact-support/current complex, nor the relative
identity
\[
  \bar\partial H_{\mathrm{BM},N}
  +H_{\mathrm{BM},N}\bar\partial
  =
  \operatorname{id}-i_Np_N .
\]
The symbol \(H_{\chi,N}\) is not yet defined, and the identity is false
on the full current complex.

## Obstruction Vector

Name the finite-window current obstruction
\[
  \operatorname{Ob}^{\mathrm{BMK\mbox{-}curr}}_N
  =
  \left(
    \operatorname{ob}_{\mathrm{diag\mbox{-}sign}},
    \operatorname{ob}_{\mathrm{curr},N},
    \operatorname{ob}_{\mathrm{collar\mbox{-}fact}}
  \right).
\]

Components:

- \(\operatorname{ob}_{\mathrm{diag\mbox{-}sign}}\): missing computation
  of the annular cutoff current
  \(\bar\partial\vartheta_\epsilon(|\zeta-z|)\wedge K_{\mathrm{BM}}\),
  including sign and scalar relative to the manuscript
  \((2\pi i)^{-2}\) convention and the residue-current convention.
- \(\operatorname{ob}_{\mathrm{curr},N}\): the nonzero scalar and
  high-moment current classes
  \[
    [\Delta_{0,0}]
    \oplus
    \bigoplus_{a+b>N}\C[\Delta_{a,b}]
  \]
  together with the missing descent of \(H_\chi\) through the quotient
  killing those classes.
- \(\operatorname{ob}_{\mathrm{collar\mbox{-}fact}}\): missing proof
  that the collar-support quotient is compatible with all
  extension-by-zero factorization maps, not only with one nested pair of
  polydisks.

This vector is prior to the all-window vector
\(\operatorname{Ob}^{\infty}_{\mathrm{BM}}\).  The all-window obstruction
only becomes the next target after
\(\operatorname{Ob}^{\mathrm{BMK\mbox{-}curr}}_N=0\) or after a
finite-window relative current habitat is constructed where the displayed
identity is true.

## What Is Partially Constructed

Keep these as proved or locally constructed data, with the stated
normalization caveats:

- The cutoff integral defining \(H_\chi\) has a locally integrable current
  limit on each fixed finite configuration stratum.  The estimate
  \(|K_{\mathrm{BM}}|\sim r^{-3}\) in real dimension four gives local
  integrability.
- The finite moment map \(p_N\) is a chain map on compactly supported top
  Dolbeault degree by Stokes.
- The derivative-delta inclusion
  \[
    i_N(\rho_{a,b})=
    \frac{(-1)^{a+b}}{a!\,b!}
    \partial_{z_1}^a\partial_{z_2}^b
    \delta_0\,d\bar z_1\wedge d\bar z_2
  \]
  has the correct algebraic Taylor-residue sign once the current-pairing
  convention for \(d\bar z_1\wedge d\bar z_2\) against
  \(dz_1\wedge dz_2\) is declared.
- The single-pair collar quotient kills terms supported on
  \(\operatorname{supp}d\chi\).
- The arity-two Hamiltonian/Matlis coefficient formula remains an
  internal residue calculation.  It should be stated as an arity-two
  Matlis comparison induced by \(p_N\) and \(i_N\), not as a consequence of
  a proved finite-window homotopy identity.

## False Identity Test

Insert the counterexample, or at least keep it in the proof ledger:
for the closed top current \(T=\Delta_{N+1,0}\), \(p_N(T)=0\).  If the
relative finite-window identity held on the full current complex, then
\[
  T=\bar\partial H_{\mathrm{BM},N}T .
\]
Pairing with \(z_1^{N+1}\) gives
\[
  \langle T,z_1^{N+1}\rangle=1,\qquad
  \langle\bar\partial H_{\mathrm{BM},N}T,z_1^{N+1}\rangle=0
\]
by Stokes and \(\bar\partial z_1^{N+1}=0\).  The scalar current
\(\Delta_{0,0}\) gives the same obstruction because the reduced
principal-part module excludes \(\rho_{0,0}\).

## Manuscript Integration Instructions

Line anchors are from the shared checkout read pass on 2026-04-30.
Re-run the indicated searches before editing because concurrent agents
are active.

1. `main.tex:1242-1420`

   Rename the proposition from "Finite-window Bochner--Martinelli
   transfer" to a current-limit and obstruction statement, for example:
   `Bochner--Martinelli current-limit data and finite-window obstruction
   for the native \(E_2\) lane`.

   Preserve the definitions of \(\mathcal P_{\leq N}\),
   \(K_{\mathrm{BM}}\), \(H_\chi\), \(i_N\), and \(p_N\).  Replace
   `main.tex:1333-1348` by a statement that the displayed differential
   identity is a theorem target, not a proved identity, unless a
   finite-window relative current habitat and a descending operator
   \(H_{\chi,N}\) are defined.

   Minimal replacement content:

   ```tex
   The data above do not yet define a finite-window homotopy
   \(H_{\chi,N}\) on the full compact-support/current complex.  The
   desired identity
   \[
     \bar\partial H_{\chi,N}+H_{\chi,N}\bar\partial
     =
     \operatorname{id}-i_Np_N+E_{\chi,N}
   \]
   is a construction target.  Its exact finite-window obstruction is
   \[
     \operatorname{Ob}^{\mathrm{BMK\mbox{-}curr}}_N
     =
     (\operatorname{ob}_{\mathrm{diag\mbox{-}sign}},
      \operatorname{ob}_{\mathrm{curr},N},
      \operatorname{ob}_{\mathrm{collar\mbox{-}fact}}).
   \]
   ```

   Then define the three components as above and state the counterexample
   with \(T=\Delta_{N+1,0}\) and \(\Delta_{0,0}\).

2. `main.tex:1422-1452`

   Replace the proof sentence saying the cutoff "adds only the displayed
   collar term" with the three-term differentiation:
   \[
     \bar\partial(\chi(\zeta)\chi(z)\vartheta_\epsilon K_{\mathrm{BM}})
     =
     \chi\chi\,\vartheta_\epsilon\,\bar\partial K_{\mathrm{BM}}
     +\bar\partial(\chi\chi)\,\vartheta_\epsilon K_{\mathrm{BM}}
     +\chi\chi\,\bar\partial\vartheta_\epsilon\wedge K_{\mathrm{BM}}.
   \]
   The second term is collar-supported.  The third term is the annular
   diagonal current and must be computed; it is not a collar term.

3. `appendix-factorization-current-conventions.tex:399-628`

   Apply the same reclassification to
   `thm:app-finite-window-bmk-current-transfer`.  The theorem title should
   become current-limit data plus obstruction vector.  Replace
   `appendix-factorization-current-conventions.tex:482-498` and the proof
   lines `630-640` with the obstruction-gated statement.  Do not leave the
   normalized finite-window identity as a theorem unless the appendix also
   defines the finite-window current quotient and proves descent of
   \(H_{\chi,N}\).

4. `main.tex:1494-1502`, `2142-2147`, `2174-2181`,
   `2321-2329`, and `2394-2395`

   Replace phrases such as "finite-window BMK arity-two transfer" and
   "obligation is discharged" with:

   ```tex
   the BMK current-limit data, the finite-window Matlis moment maps, and
   the arity-two Hamiltonian/Matlis comparison; the finite-window
   differential identity is blocked by
   \(\operatorname{Ob}^{\mathrm{BMK\mbox{-}curr}}_N\)
   ```

   When discussing all-window transfer, say that
   \(\operatorname{Ob}^{\infty}_{\mathrm{BM}}\) is downstream of this
   finite-window current gate.

5. `theorem-lanes.tex:381-533`

   Update the lane status from a generic construction obligation to the
   sharper state: CE/factorization object and semidirect collision algebra
   are proved; BMK current limit, \(p_N\), \(i_N\), and single-pair collar
   quotient are partially constructed; finite-window differential identity
   is obstructed by
   \(\operatorname{Ob}^{\mathrm{BMK\mbox{-}curr}}_N\).

   Also replace the displayed kernel at `theorem-lanes.tex:477-486` with
   the full Koppelman form using
   \(d\bar\eta_j=d\bar\zeta_j-d\bar z_j\).  A \(d\bar z=0\) component is
   not enough for the Dolbeault homotopy.

6. `claim-strength-ledger.tex:319-325` and `585-615`

   Replace "proved finite-window BM transfer at arity two" by "proved
   BMK current-limit data and arity-two Matlis comparison; finite-window
   differential identity obstructed."  Add
   \(\operatorname{Ob}^{\mathrm{BMK\mbox{-}curr}}_N\) as the finite-window
   gate preceding \(\operatorname{Ob}^{\infty}_{\mathrm{BM}}\).

## Acceptance Gate

The finite-window identity may be restored only after one of the following
is written and checked:

- A relative finite-window current complex
  \[
    \mathcal C_N^\bullet(B_2,B_1)
    =
    \mathcal D'^{0,\bullet}(B_2)/
    \bigl(\mathcal D'^{0,\bullet}_{B_2\setminus B_1}(B_2)
    +\mathcal K_N^\bullet\bigr)
  \]
  plus homotopy saturation of \(\mathcal K_N^\bullet\) proving that
  \(H_\chi\) descends.
- A modified finite-window kernel \(H_{\chi,N}\) whose Taylor/current
  subtraction is built in and whose annular diagonal term gives exactly
  \(i_Np_N\) with the declared sign and scalar.

Until then, the manuscript status is:

- proved: native CE/factorization object and semidirect
  Hamiltonian-cotangent collision algebra;
- constructed: BMK cutoff current limit \(H_\chi\), finite moments
  \(p_N\), residue currents \(i_N\), and one nested-pair collar quotient;
- computed: arity-two Hamiltonian/Matlis coefficient formulas;
- blocked: finite-window BMK differential identity on the full current
  complex;
- downstream: strict all-window native \(E_2\) transfer governed by
  \(\operatorname{Ob}^{\infty}_{\mathrm{BM}}\) only after the
  finite-window current obstruction is killed.
