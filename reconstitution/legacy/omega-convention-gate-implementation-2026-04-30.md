# Omega Convention Gate Implementation, 2026-04-30

Status: convention gate.  Report only.  No TeX files edited.

Source identity verified:

```text
4d2c7af70e52c51faef63177cd1b7e2a0e54ae08d1b42228d3f78746d6640b21  materials/raw/2026-04-30-mixed-holomorphic-topological-strings-critique.pdf
```

## Gate

Use the brane-preserving normal torus
\[
  T_\Omega=\C^*_{\epsilon_s}\times\C^*_{\epsilon_1}\times\C^*_{\epsilon_2},
  \qquad
  V_\Omega=
  \epsilon_s s\partial_s+\epsilon_1z_1\partial_{z_1}
  +\epsilon_2z_2\partial_{z_2},
  \qquad V_\Omega(t)=0 .
\]
The Cartan operator is
\[
  Q_\Omega=Q+\iota_{V_\Omega},\qquad Q_\Omega^2=L_{V_\Omega}.
\]
Every dg statement is on the \(T_\Omega\)-invariant/basic subcomplex, or
it keeps the \(L_{V_\Omega}\)-curvature explicitly.  This is not a
Costello QME solution.

Manuscript-wide symbol rule:

- \(\epsilon_s,\epsilon_1,\epsilon_2\): Omega equivariant weights.
- \(\varepsilon_1,\varepsilon_2\): open trace orientation generators, as
  in \([\varepsilon_1\varepsilon_2]\).
- \(\varepsilon_\Gamma\), \(\varepsilon_{\Gamma,\Gamma'}\): graph/Koszul
  signs.  These are not Omega weights.
- \(\chi_\omega=\epsilon_1+\epsilon_2\).

## Localization

For a finite normal/Hamiltonian window \((N,M)\), use the character set
\[
  \chi^H_{n,a,b}=n\epsilon_s+a\epsilon_1+b\epsilon_2,\qquad
  \chi^\vee_{n,a,b}=n\epsilon_s-a\epsilon_1-b\epsilon_2,
\]
and let \(\mathsf X_{N,M}\) be the nonzero characters among these which
occur on moving summands in that window.  The finite-window coefficient
ring is
\[
  R_\Omega^{N,M}
  =
  \C[\epsilon_s,\epsilon_1,\epsilon_2,\hbar_\omega]
  [\chi^{-1}\mid \chi\in\mathsf X_{N,M}],
  \qquad
  \operatorname{wt}(\hbar_\omega)=\chi_\omega .
\]
The product localization
\(\C[\epsilon_s,\epsilon_1,\epsilon_2,\hbar_\omega]
[(\epsilon_s\epsilon_1\epsilon_2)^{-1}]\) is not enough for normal
contractions: it misses characters such as
\(n\epsilon_s+a\epsilon_1+b\epsilon_2\) and
\(n\epsilon_s-a\epsilon_1-b\epsilon_2\).

If a theorem needs a single coefficient field, define it explicitly:
\[
  R_\Omega^{\mathrm{all}}
  =
  \C[\epsilon_s,\epsilon_1,\epsilon_2,\hbar_\omega]
  [\lambda^{-1}\mid
    0\ne\lambda\in\Z\epsilon_s+\Z\epsilon_1+\Z\epsilon_2],
  \qquad
  K_\Omega=\operatorname{Frac}(R_\Omega^{\mathrm{all}}).
\]
Then targets may be written over \(R_\Omega^{N,M}\) in finite windows or
over \(K_\Omega\) in field-valued theorem surfaces.  Do not use
\(\C((\epsilon_s,\epsilon_1,\epsilon_2))\) unless it is declared to be a
field containing all inverted normal characters required by the window.

Self-dual branch:
\[
  \chi_\omega=\epsilon_1+\epsilon_2=0.
\]
This is a separate base change.  If
\(\bar\chi\) is the image of a normal character after the base change,
invert only those \(\bar\chi\ne0\).  Characters with \(\bar\chi=0\) are
resonant summands and remain in \(\operatorname{pr}_{\chi=0}\).  No
statement may invert \(\epsilon_1+\epsilon_2\) and then specialize to the
self-dual branch.

## \(\hbar\) Branches

The gate separates three symbols.

\[
  \hbar_{\mathrm{QME}}:
  \text{ Costello/QME loop-counting parameter, weight }0.
\]
\[
  \hbar_{\mathrm W}:
  \text{ Weyl/Moyal deformation parameter, weight }\chi_\omega.
\]
\[
  \hbar_\omega:
  \text{ equivariant scalarizer for the inverse symplectic-character line,
  weight }\chi_\omega.
\]

Default Omega-QME branch:
\[
  [f,g]_\Omega=\hbar_\omega\{f,g\}_{\mathrm{Poiss}},
  \qquad \hbar_{\mathrm{QME}}\text{ is independent of }\hbar_\omega .
\]
The scalar contact symbol is therefore
\[
  \nu_\Omega\,
  \hbar_{\mathrm{QME}}\,
  \operatorname{Str}_{\mathrm{cyc}}(\mathfrak m)\,
  [[f,g]_\Omega]_0\,\gamma_{\mathbf 1}
  =
  \nu_\Omega\,
  \hbar_{\mathrm{QME}}\hbar_\omega\,
  \operatorname{Str}_{\mathrm{cyc}}(\mathfrak m)\,
  [\{f,g\}_{\mathrm{Poiss}}]_0\,\gamma_{\mathbf 1}.
\]
The QME order filtration is by \(\hbar_{\mathrm{QME}}\), not by
\(\hbar_\omega\).

Weyl branch:
\[
  \hbar_\omega=\hbar_{\mathrm W}.
\]
In this branch the QME expansion parameter must be written
\(\hbar_{\mathrm{QME}}\) or \(\hbar_{\mathrm{loop}}\).  If one instead
identifies all three symbols with one bare \(\hbar\), the contact term
becomes order \(\hbar^2\), shifting the \([\hbar^n]\) bookkeeping.  That
identification is forbidden unless the order filtration is rewritten.

Self-dual branch:
\(\hbar_\omega\) has weight zero and may be kept as a central formal
parameter or set to \(1\) after the self-dual base change.

## Normalization

Residue and Euler conventions are distinct:
\[
  \nu_\Omega^{\mathrm{res}}=1,\qquad
  \nu_\Omega^{\mathrm{Eu}}
  =
  \sigma_s(\epsilon_s\epsilon_1\epsilon_2)^{-1}.
\]
Here \(\sigma_s=\pm1\) is the real \(s\)-orientation sign.  It remains an
orientation theorem obligation until fixed.  If the Euler factor is
absorbed into a residue orientation, call the result the
Euler-rescaled residue convention:
\[
  \nu_\Omega^{\mathrm{Eres}}
  =
  \sigma_s(\epsilon_s\epsilon_1\epsilon_2)^{-1},
\]
not the plain residue convention.  Scalar contacts, graph rows, trace
states, and large-\(N\) normalizations must name which \(\nu_\Omega\) is
used.

## Attacks and Heals

1. Glyph collision.

   Broken formula: Omega weights written as
   \(\varepsilon_s,\varepsilon_1,\varepsilon_2\).  This collides with the
   open trace orientation variables.

   Heal: replace Omega weights by
   \(\epsilon_s,\epsilon_1,\epsilon_2\) only in Omega passages.  Do not
   change \([\varepsilon_1\varepsilon_2]\) or graph sign notation.

2. Product-only localization.

   Broken formula:
   \[
     R_\Omega=
     \C[\varepsilon_s,\varepsilon_1,\varepsilon_2,\hbar_\omega]
     [(\varepsilon_s\varepsilon_1\varepsilon_2)^{-1}].
   \]

   Heal:
   \[
     R_\Omega^{N,M}
     =
     \C[\epsilon_s,\epsilon_1,\epsilon_2,\hbar_\omega]
     [\chi^{-1}\mid \chi\in\mathsf X_{N,M}].
   \]
   The Euler product belongs to \(\nu_\Omega^{\mathrm{Eu}}\), not to the
   whole moving-character localization.

3. Silent \(\hbar/\hbar_\omega\) identification.

   Broken formula:
   \[
     \nu_\Omega\,\hbar\,[\{f,g\}_\Omega]_0
   \]
   without a branch declaration, while
   \(\{f,g\}_\Omega\) already contains \(\hbar_\omega\).

   Heal: write the branch explicitly.  In the default QME branch, use
   \[
     \nu_\Omega\,\hbar_{\mathrm{QME}}\,
     [[f,g]_\Omega]_0
     =
     \nu_\Omega\,\hbar_{\mathrm{QME}}\hbar_\omega\,
     [\{f,g\}_{\mathrm{Poiss}}]_0 .
   \]

4. Self-dual inversion.

   Broken operation: invert \(\epsilon_1+\epsilon_2\) and then impose
   \(\epsilon_1+\epsilon_2=0\).

   Heal: perform the self-dual base change first, remove
   \(\epsilon_1+\epsilon_2\) and every character specializing to zero from
   the inverted set, and retain those terms in \(\operatorname{pr}_{\chi=0}\).

5. Residue/Euler identification.

   Broken formula:
   \[
     \nu_\Omega=(\epsilon_s\epsilon_1\epsilon_2)^{-1}
   \]
   called residue normalization.

   Heal: either
   \(\nu_\Omega^{\mathrm{res}}=1\), or
   \(\nu_\Omega^{\mathrm{Eu}}=\sigma_s(\epsilon_s\epsilon_1\epsilon_2)^{-1}\).
   If this factor is absorbed into residue, name it Euler-rescaled residue.

6. QME overclaim.

   Broken implication: normal Omega localization proves the Costello
   brane-defect QME.

   Heal: preserve the obstruction criterion.  The QME closes only after
   the equivariant propagator, counterterms, scalar projection, non-scalar
   \(H^1\)-classes, \(\varprojlim^1H^0\) primitive compatibility, and
   invariant centrality homotopies are constructed and vanish.

## Post-Swarm TeX Edits

Exact locations requiring later TeX edits, after live agents clear the
owned paths:

1. `abstract.tex:195-208`
   Replace Omega \(\varepsilon_*\) by \(\epsilon_*\).  Keep the normal
   torus and self-dual branch with the gate symbols.

2. `local-dictionary.tex:445-457`
   Replace the unnamed global localization paragraph by the named
   \(R_\Omega^{N,M}\), \(R_\Omega^{\mathrm{all}}\), and \(K_\Omega\)
   conventions above.  Retain the self-dual no-inversion guard.

3. `local-dictionary.tex:503-530`
   Split \(\hbar_{\mathrm W}\), \(\hbar_{\mathrm{QME}}\), and
   \(\hbar_\omega\).  State that \(\hbar_\omega=\hbar_{\mathrm W}\) is only
   the Weyl branch, not QME order identification.

4. `local-dictionary.tex:545-559`
   Clarify that the displayed \(w(\hbar)=\epsilon_1+\epsilon_2\) is the
   Weyl/Moyal brane parameter \(\hbar_{\mathrm W}\), not the QME loop
   parameter.

5. `local-dictionary.tex:565-588`
   Name \(\nu_\Omega^{\mathrm{res}}\), \(\nu_\Omega^{\mathrm{Eu}}\), and
   the optional Euler-rescaled residue branch with the \(\sigma_s\) sign.

6. `appendix-unreduced-bv-qme.tex:2152-2184`
   Replace \(\varepsilon_*\) by \(\epsilon_*\), replace product-only
   \(R_\Omega\) by \(R_\Omega^{N,M}\), and state the self-dual base-change
   guard next to the ring.

7. `appendix-unreduced-bv-qme.tex:2184-2198`
   Rename the weighted bracket to match the gate, preferably
   \([f,g]_\Omega=\hbar_\omega\{f,g\}_{\mathrm{Poiss}}\).  Add the branch
   declaration before using any QME order.

8. `appendix-unreduced-bv-qme.tex:2215`, `2256`, `2259`, `2289-2296`,
   `2379-2392`
   Use \(R_\Omega^{N,M}\) in finite-window targets and
   \(\hbar_{\mathrm{QME}}\) in QME filtrations.  Rewrite the scalar contact
   row as the gate formula above.

9. `appendix-unreduced-bv-qme.tex:2227-2237`
   If the contraction is written characterwise, use
   \(Q_\Omega h_\chi+h_\chi Q_\Omega=\operatorname{id}_\chi\) for
   \(\chi\ne0\).  For the summed finite window use
   \(Q_\Omega H+HQ_\Omega=\operatorname{id}-\operatorname{pr}_{\chi=0}\).

10. `appendix-unreduced-bv-qme.tex:2258-2265`
    Add \(\sigma_s\) to the Euler normalization and distinguish plain
    residue from Euler-rescaled residue.

11. `claim-strength-ledger.tex:397-405` and `claim-strength-ledger.tex:423-439`
    Replace \(\operatorname{Ch}_{\C((\epsilon_s,\epsilon_1,\epsilon_2))[[\hbar]]}\)
    and \(\C((\epsilon_s,\epsilon_1,\epsilon_2))[[\hbar]]\) by the chosen
    \(R_\Omega^{N,M}[[\hbar_{\mathrm{QME}}]]\) or
    \(K_\Omega[[\hbar_{\mathrm{QME}}]]\) target.

12. `open-obligations.tex:559-608` and `open-obligations.tex:683-721`
    Replace Omega \(\varepsilon_*\) by \(\epsilon_*\), replace ambiguous
    coefficient fields by \(R_\Omega^{N,M}\) or \(K_\Omega\), and rename
    "built into the residue orientation" as "built into an Euler-rescaled
    residue convention" if that branch is intended.

13. `theorem-lanes.tex:1466-1620`
    The equivariant CE/PV lane is now present.  Add only the
    \(\hbar_{\mathrm W}\)/\(\hbar_{\mathrm{QME}}\)/\(\hbar_\omega\) branch
    guard if later edits connect it directly to QME order bookkeeping.

14. `theorem-lanes.tex:2585-2782`
    The normal Omega kernel/QME boundary lane already uses \(\epsilon\),
    the normal characters, \(\sigma_s\), and the QME firewall.  Add the
    named coefficient ring \(R_\Omega^{N,M}\) and the \(\hbar_{\mathrm{QME}}\)
    filtration if the lane is made fully notation-complete.

15. `theorem-lanes.tex:2796-2802`, `theorem-lanes.tex:2859-2862`, and
    `theorem-lanes.tex:2871-2877`
    Replace \(\C((\epsilon_s,\epsilon_1,\epsilon_2))[[\hbar]]\) and bare
    \(R_\Omega\) by the selected \(K_\Omega[[\hbar_{\mathrm{QME}}]]\) or
    finite-window \(R_\Omega^{N,M}\) target, and keep residue/Euler
    normalization branch names.

16. `reconstitution/swarm-2026-04-30-agent-179-equivariant-qme-kernel-0957.md`
    This is not TeX, but it is stale convention surface: it uses
    \(\varepsilon_*\) and product-only localization.  Do not propagate it
    without the gate corrections.

## Current Ground Truth Corrections

Agent 195 recorded the Agent 192 report as absent.  That claim is stale
in the current worktree: `reconstitution/swarm-2026-04-30-agent-192-equivariant-brane-current-brackets-0957.md`
exists and matches the brane-current theorem
`appendix-factorization-current-conventions.tex:399-550`.

## Status Recommendations

- Enforce this gate before any further Omega TeX integration.
- Treat glyph sync and ring naming as convention fixes, not theorem
  downgrades.
- Do not assert a Costello QME solution from Omega notation.
- Run `git diff --check` on the edited TeX bundle and a final `make pdf`
  only after active swarm edits settle.
