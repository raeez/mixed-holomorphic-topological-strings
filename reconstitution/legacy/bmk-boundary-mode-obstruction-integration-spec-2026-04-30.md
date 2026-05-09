# BMK Boundary-Mode Obstruction Integration Spec, 2026-04-30

Agent: 286.

Scope: report-only integration specification for
`main.tex` Proposition `prop:finite-window-bm-native-e2-transfer` and
`appendix-factorization-current-conventions.tex` Theorem
`thm:app-finite-window-bmk-current-transfer`.  No manuscript TeX is edited.

## Verdict

The finite-window BMK lane has a positive single-pair derived analytic
quotient after a full analytic BMK contraction is chosen, but it does not
have a strict support-local finite-current quotient compatible with the full
Hamiltonian current action.

The strongest true replacement is:

1. keep the BMK current limit, the finite moment map `p_N`, the
   derivative-delta inclusion `i_N`, and the arity-two Hamiltonian/Matlis
   output projection as proved or locally constructed data, subject to the
   diagonal orientation convention;
2. state a one-pair derived analytic quotient construction on
   `C^\bullet(B_2,B_1)` after choosing the full analytic BMK retract;
3. replace the overstrong finite-window transfer theorem by a strict
   support-local quotient obstruction theorem.

The decisive obstruction is the boundary-mode leakage
\[
  z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1},
\]
which carries a killed high mode into a retained finite-window mode.  Thus a
relation killing \(\rho_{N+1,0}\) is not a Hamiltonian submodule relation for
any \(N\geq1\).

## Exact Obstruction Vector

Use the sharpened finite-window obstruction vector
\[
  \operatorname{Ob}^{\mathrm{BMK\mbox{-}bdry}}_N
  =
  \left(
    \operatorname{ob}_{\mathrm{diag}},
    \operatorname{ob}_{\mathrm{an}/\mathrm{fin},N},
    \operatorname{ob}_{\partial,N},
    \operatorname{ob}_{\mathrm{collar\mbox{-}fact},N}
  \right).
\]

The components are:

- \(\operatorname{ob}_{\mathrm{diag}}\): sign and scalar comparison between
  the annular BMK diagonal current and the Matlis derivative-delta
  convention.  With the displayed kernel and real outward \(S^3\)
  orientation, the angular mass is \(-1\); the manuscript must either
  declare \([\Delta]_{\mathrm{BM}}=-[\Delta]_{\mathrm{real}}\) or reverse
  the kernel convention.
- \(\operatorname{ob}_{\mathrm{an}/\mathrm{fin},N}\): the quotient between
  the full analytic moment kernel
  \(K_N=\ker(\pi_N:\mathcal O(B_1)^\vee\to\mathcal P_{\leq N})\) and the
  smaller support-at-zero relation
  \(K_N^0=\C\delta_{0,0}\oplus\bigoplus_{a+b>N}\C\delta_{a,b}\).  The
  support-local quotient kills \(K_N^0\), not all of \(K_N\).
- \(\operatorname{ob}_{\partial,N}\): Hamiltonian boundary-mode leakage
  \[
    \operatorname{ob}_{\partial,N}
    =
    \pi_N\bigl(\mathfrak h\cdot K_N^0\bigr)
    \subset \mathcal P_{\leq N}.
  \]
  It is nonzero because
  \[
    z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1}.
  \]
- \(\operatorname{ob}_{\mathrm{collar\mbox{-}fact},N}\): failure of the
  chosen relation subspace to be a factorization ideal under extension by
  zero, disjoint products, and the BMK homotopy.  Concretely one needs
  \(j_!R_N(U)\subset R_N(V)\),
  \(\mu(R_N(U),C(W))+\mu(C(U),R_N(W))\subset R_N(U\sqcup W)\), and
  \(H_\chi R_N\subset R_N\).  Neither the analytic quotient nor the
  support-at-zero finite quotient supplies all three properties for the
  native current factorization object.

After the diagonal convention is fixed,
\(\operatorname{ob}_{\mathrm{diag}}\) can be set to zero.  The support-local
finite quotient remains blocked by
\(\operatorname{ob}_{\partial,N}\neq0\).

## TeX-Ready Main Replacement Blocks

### Proposition Title

Replace the title at `main.tex:1242` by:

```tex
\begin{prop}[BMK current-limit data, one-pair analytic quotient, and finite-window boundary obstruction]\label{prop:finite-window-bm-native-e2-transfer}
```

### Replace `main.tex:1333-1349`

```tex
  These data do not define a finite-window homotopy
  \(H_{\chi,N}\) on the full compact-support/current complex.  The desired
  identity
  \[
    \bar\partial H_{\chi,N}+H_{\chi,N}\bar\partial
    =
    \operatorname{id}-i_Np_N+E_{\chi,N}
  \]
  is obstructed before any all-window question is reached.  The exact
  finite-window obstruction vector is
  \[
    \operatorname{Ob}^{\mathrm{BMK\mbox{-}bdry}}_N
    =
    \left(
      \operatorname{ob}_{\mathrm{diag}},
      \operatorname{ob}_{\mathrm{an}/\mathrm{fin},N},
      \operatorname{ob}_{\partial,N},
      \operatorname{ob}_{\mathrm{collar\mbox{-}fact},N}
    \right).
  \]
  Here \(\operatorname{ob}_{\mathrm{diag}}\) is the sign/scalar comparison
  between the annular diagonal BMK current and the Matlis
  derivative-delta convention.  With the displayed kernel and real outward
  \(S^3\)-orientation the annular mass is \(-1\), so the BMK diagonal
  current must be oriented as
  \([\Delta]_{\mathrm{BM}}=-[\Delta]_{\mathrm{real}}\), or equivalently
  the kernel sign must be reversed.  The term
  \(\operatorname{ob}_{\mathrm{an}/\mathrm{fin},N}\) is the nonzero gap
  between the full analytic moment kernel
  \(K_N=\ker(\pi_N:\mathcal O(B_1)^\vee\to\mathcal P_{\leq N})\) and the
  support-at-zero span
  \(K_N^0=\C\delta_{0,0}\oplus\bigoplus_{a+b>N}\C\delta_{a,b}\).
  The term
  \[
    \operatorname{ob}_{\partial,N}
    =
    \pi_N(\mathfrak h\cdot K_N^0)
    \subset\mathcal P_{\leq N}
  \]
  is the boundary-mode leakage under the full Hamiltonian action.  It is
  nonzero for every \(N\geq1\), since the Matlis coadjoint formula gives
  \[
    z_1^{N+2}\cdot\rho_{N+1,0}
      =
      -(N+2)\rho_{0,1}.
  \]
  Thus the high mode \(\rho_{N+1,0}\) is killed by a finite-window
  relation, while its Hamiltonian translate \(\rho_{0,1}\) is retained.
  Finally, \(\operatorname{ob}_{\mathrm{collar\mbox{-}fact},N}\) is the
  failure of the relation to be a factorization ideal compatible with
  extension by zero, disjoint products, and \(H_\chi\).
```

### Insert After The Obstruction Paragraph

```tex
  There is nevertheless a one-pair derived analytic quotient after the
  full analytic BMK contraction has been chosen.  Let
  \(C^\bullet(B_2,B_1)\) denote the single-pair collar quotient, and
  suppose that
  \[
    \bar\partial H_\chi^0+H_\chi^0\bar\partial
      =
    \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}},
    \qquad
    H_\chi^0I_{\mathrm{an}}=0,
  \]
  where \(P_{\mathrm{an}}:C^\bullet(B_2,B_1)\to\mathcal O(B_1)^\vee\) is
  the analytic Dolbeault moment map and \(I_{\mathrm{an}}\) is a chosen
  closed-current representative map.  Let
  \[
    \pi_N:\mathcal O(B_1)^\vee\longrightarrow\mathcal P_{\leq N},
    \qquad
    K_N=\ker\pi_N,
  \]
  and form the derived quotient
  \[
    C_N^{\mathrm{der}}(B_2,B_1)
      =
    \operatorname{cofib}\!\left(
      I_{\mathrm{an}}K_N\longrightarrow C^\bullet(B_2,B_1)
    \right).
  \]
  Here \(K_N\) is placed in the top Dolbeault degree represented by
  closed currents.
  Equivalently, when \(I_{\mathrm{an}}K_N\) is represented by a strict
  \(H_\chi^0\)-saturated subcomplex, this is the ordinary quotient
  \(C^\bullet(B_2,B_1)/I_{\mathrm{an}}K_N\).  On this one-pair derived
  quotient the homotopy descends and satisfies
  \[
    \bar\partial\overline H_{\chi,N}
    +\overline H_{\chi,N}\bar\partial
      =
    \operatorname{id}-i_Np_N,
  \]
  with \(p_N=\pi_NP_{\mathrm{an}}\) and \(i_N\) the finite
  derivative-delta section.  This quotient is analytic and one-pair
  dependent; it is not a support-local finite-current factorization
  quotient.
```

### Replace The Arity-Two And All-Window Claim Tail

Use this in place of the current conclusion that the finite-window transfer
is proved:

```tex
  The arity-two coefficient calculation remains valid as an output
  projection:
  \[
    \ell_2^{\mathrm{Mat},N}(x,y)=p_N[ix,iy].
  \]
  Hence for Hamiltonians \(f,g\in\mathfrak h\),
  \[
    \ell_2^{\mathrm{Mat},N}(f,g)
      =
      \partial_{z_1}f\,\partial_{z_2}g
      -
      \partial_{z_2}f\,\partial_{z_1}g
      \pmod{\C},
  \]
  and for \(f=z_1^pz_2^q\),
  \[
    \ell_2^{\mathrm{Mat},N}(f,\rho_{i,j})
      =
      -(pj-qi+p-q)\,
      \operatorname{pr}_{\leq N}\rho_{i-p+1,j-q+1}.
  \]
  This is the Matlis coadjoint action of
  Theorem~\ref{thm:principal-part-coadjoint-uniqueness}, read after the
  coefficient has been computed and only then projected to the output
  window.  It is not the binary part of a strict support-local
  finite-current quotient.

  Consequently no strict support-local finite-current quotient \(Q_N\)
  exists with all of the following properties: the classes
  \(\rho_{a,b}\), \(0<a+b\leq N\), survive with the Matlis residue
  normalization; the scalar current and all support-at-zero high currents
  are killed; the full Hamiltonian current action and extension-by-zero
  factorization maps descend; and a finite-window BMK homotopy identity
  holds on \(Q_N\).  Indeed, the killed class \(\rho_{N+1,0}\) has the
  retained Hamiltonian translate
  \[
    z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1}.
  \]
  This contradicts Hamiltonian stability of the relation subspace.

  The strict all-window transfer is therefore downstream of this
  finite-window gate.  The all-window obstruction
  \(\operatorname{Ob}^{\infty}_{\mathrm{BM}}\) should be attacked only
  after the finite support-local obstruction is replaced either by the
  analytic derived quotient above or by a homotopy-coherent finite-window
  \(L_\infty\) package carrying the escaped boundary modes as extra
  operations.

  The principal-part face remains genuinely two-variable:
  \[
    \frac{1}{(2\pi i)^2}
    \frac{d\zeta_1\wedge d\zeta_2}
         {(\zeta_1-z_1)(\zeta_2-z_2)}
    =
    \sum_{a,b\geq0}z_1^az_2^b\rho_{a,b}(\zeta).
  \]
  Killing \(z_2\) kills the Hamiltonian bracket, and the \(b=0\)
  principal-part line is not stable because
  \(z_1\cdot\rho_{a,0}=-\rho_{a,1}\).  Thus the theorem proves BMK
  current-limit data, the one-pair analytic quotient under its stated
  analytic retract, and the support-local finite-current obstruction.  It
  does not prove a curve VOA, a Zhu algebra, a strict support-local
  finite-window transfer, or a strict all-arity transfer.
```

### Replace `main.tex:1422-1452` Proof

```tex
\begin{proof}
  The Koppelman identity applies to the uncut BMK kernel on the punctured
  product.  After multiplication by
  \(\chi(\zeta)\chi(z)\vartheta_\epsilon(|\zeta-z|)\), differentiation
  gives three terms:
  \[
  \begin{aligned}
    \bar\partial
    \bigl(\chi(\zeta)\chi(z)\vartheta_\epsilon K_{\mathrm{BM}}\bigr)
      &=
      \chi(\zeta)\chi(z)\vartheta_\epsilon\,
      \bar\partial K_{\mathrm{BM}}  \\
      &\quad
      +\bar\partial(\chi(\zeta)\chi(z))\,
      \vartheta_\epsilon K_{\mathrm{BM}}  \\
      &\quad
      +\chi(\zeta)\chi(z)\,
      \bar\partial\vartheta_\epsilon\wedge K_{\mathrm{BM}} .
  \end{aligned}
  \]
  The second term is collar-supported.  The third term is the annular
  diagonal current; it is not a collar term and fixes
  \(\operatorname{ob}_{\mathrm{diag}}\).  The current limit of \(H_\chi\)
  follows from \(|K_{\mathrm{BM}}|\sim r^{-3}\) in real dimension four on
  each fixed finite configuration stratum.

  The derivative-delta normalization is the integration-by-parts identity
  \[
    \left\langle
      \frac{(-1)^{a+b}}{a!\,b!}
      \partial_{z_1}^a\partial_{z_2}^b\delta_0,\,
      f
    \right\rangle
    =
    [z_1^az_2^b]f
    =
    \operatorname{Res}_0(\rho_{a,b}f).
  \]
  Thus \(p_N\) and \(i_N\) are the finite Matlis moment map and
  derivative-delta section once the diagonal orientation convention is
  declared.

  For the analytic one-pair quotient, the normalized contraction satisfies
  \(H_\chi^0I_{\mathrm{an}}=0\), so \(H_\chi^0\) preserves the homotopy
  cofiber of \(I_{\mathrm{an}}K_N\to C^\bullet(B_2,B_1)\).  On this
  quotient \(I_{\mathrm{an}}P_{\mathrm{an}}\) is identified with
  \(i_Np_N\), proving the displayed derived quotient identity.

  A strict support-local quotient cannot replace this analytic quotient.
  By the Matlis coadjoint formula,
  \[
    z_1^p z_2^q\cdot\rho_{i,j}
    =
    -(pj-qi+p-q)\rho_{i-p+1,j-q+1}.
  \]
  Taking \(p=N+2\), \(q=0\), \(i=N+1\), and \(j=0\) gives
  \[
    z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1}.
  \]
  The source is killed by any finite-window support-local relation, while
  the target survives for \(N\geq1\).  Therefore the relation is not a
  Hamiltonian submodule relation, and the full Hamiltonian current action
  cannot descend to such a strict quotient.  The arity-two formulas are
  the same residue-transpose calculation followed by output projection,
  not evidence for a strict finite-current transfer.
\end{proof}
```

## TeX-Ready Appendix Replacement Blocks

### Theorem Title

Replace `appendix-factorization-current-conventions.tex:399` by:

```tex
\begin{thm}[BMK current-limit data and finite-window boundary-mode obstruction]
```

### Replace `appendix-factorization-current-conventions.tex:482-614`

```tex
  These data do not define a finite-window homotopy
  \(H_{\chi,N}\) on the full compact-support/current complex.  The desired
  identity
  \[
    \bar\partial H_{\chi,N}+H_{\chi,N}\bar\partial
    =
    \operatorname{id}-i_Np_N+E_{\chi,N}
  \]
  is obstructed before any all-window question is reached.  The exact
  finite-window obstruction vector is
  \[
    \operatorname{Ob}^{\mathrm{BMK\mbox{-}bdry}}_N
    =
    \left(
      \operatorname{ob}_{\mathrm{diag}},
      \operatorname{ob}_{\mathrm{an}/\mathrm{fin},N},
      \operatorname{ob}_{\partial,N},
      \operatorname{ob}_{\mathrm{collar\mbox{-}fact},N}
    \right).
  \]
  The diagonal component is the sign/scalar comparison between the
  annular diagonal BMK current and the Matlis derivative-delta convention.
  With the displayed kernel and real outward \(S^3\)-orientation the
  annular mass is \(-1\), so the BMK diagonal current must be oriented as
  \([\Delta]_{\mathrm{BM}}=-[\Delta]_{\mathrm{real}}\), or equivalently
  the kernel sign must be reversed.  The analytic-versus-finite component
  is the nonzero gap between
  \(K_N=\ker(\pi_N:\mathcal O(B_1)^\vee\to\mc P_{\leq N})\) and the
  support-at-zero span
  \(K_N^0=\C\delta_{0,0}\oplus\bigoplus_{a+b>N}\C\delta_{a,b}\).
  The boundary component
  \[
    \operatorname{ob}_{\partial,N}
    =
    \pi_N(\mathfrak h\cdot K_N^0)
    \subset\mc P_{\leq N}
  \]
  is nonzero for every \(N\geq1\), since
  \[
    z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1}.
  \]
  Thus a high support-at-zero relation killed by the finite window has a
  retained Hamiltonian translate.  The collar-factorization component is
  the remaining failure of the relation to be compatible with extension
  by zero, disjoint products, and \(H_\chi\).

  There is nevertheless a one-pair derived analytic quotient after the
  full analytic BMK contraction has been chosen.  Let
  \(C^\bullet(B_2,B_1)\) be the single-pair collar quotient, and suppose
  \[
    \bar\partial H_\chi^0+H_\chi^0\bar\partial
      =
    \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}},
    \qquad
    H_\chi^0I_{\mathrm{an}}=0.
  \]
  Let
  \[
    \pi_N:\mathcal O(B_1)^\vee\longrightarrow\mc P_{\leq N},
    \qquad
    K_N=\ker\pi_N.
  \]
  Then
  \[
    C_N^{\mathrm{der}}(B_2,B_1)
      =
    \operatorname{cofib}\!\left(
      I_{\mathrm{an}}K_N\longrightarrow C^\bullet(B_2,B_1)
    \right)
  \]
  where \(K_N\) is placed in the top Dolbeault degree represented by
  closed currents.  This quotient
  carries the descended identity
  \[
    \bar\partial\overline H_{\chi,N}
    +\overline H_{\chi,N}\bar\partial
      =
    \operatorname{id}-i_Np_N.
  \]
  This is a one-pair analytic quotient, not a support-local finite-current
  factorization quotient.

  The arity-two coefficient calculation remains valid as an output
  projection:
  \[
    \ell^{\mathrm{Mat},N}_2(x,y)=p_N[ix,iy].
  \]
  For monomials,
  \[
    \ell^{\mathrm{Mat},N}_2
    (z_1^pz_2^q,z_1^rz_2^s)
      =
      (ps-qr)\,
      \operatorname{pr}_{\leq N}
      (z_1^{p+r-1}z_2^{q+s-1})
      \pmod{\C},
  \]
  and
  \[
    \ell^{\mathrm{Mat},N}_2(z_1^pz_2^q,\rho_{i,j})
      =
      -(pj-qi+p-q)\,
      \operatorname{pr}_{\leq N}\rho_{i-p+1,j-q+1},
  \]
  with negative-index targets equal to zero, while
  \[
    \ell^{\mathrm{Mat},N}_2(\rho,\sigma)=0 .
  \]
  This is the Matlis coadjoint action of
  Proposition~\ref{prop:app-matlis-coadjoint-action}, read after the
  coefficient has been computed and only then projected to the output
  window.

  Consequently no strict support-local finite-current quotient \(Q_N\)
  exists with all of the following properties: the classes
  \(\rho_{a,b}\), \(0<a+b\leq N\), survive with the Matlis residue
  normalization; the scalar current and all support-at-zero high currents
  are killed; the full Hamiltonian current action and extension-by-zero
  factorization maps descend; and a finite-window BMK homotopy identity
  holds on \(Q_N\).  The killed class \(\rho_{N+1,0}\) has the retained
  Hamiltonian translate
  \[
    z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1},
  \]
  contradicting Hamiltonian stability of the relation subspace.

  The principal-part face remains two-variable:
  \[
    \frac{1}{(2\pi i)^2}
    \frac{d\zeta_1\wedge d\zeta_2}
         {(\zeta_1-z_1)(\zeta_2-z_2)}
    =
    \sum_{a,b\geq0}z_1^az_2^b\rho_{a,b}(\zeta).
  \]
  Killing \(z_2\) kills the Hamiltonian bracket, and the \(b=0\)
  principal-part line is not stable since
  \(z_1\cdot\rho_{a,0}=-\rho_{a,1}\).  No curve VOA, Zhu algebra, or
  one-variable transfer follows from this theorem.

  The proved theorem here is the BMK current-limit data, the finite Matlis
  moment maps, the arity-two Hamiltonian/Matlis output projection, the
  one-pair derived analytic quotient under the stated analytic retract,
  and the obstruction theorem for strict support-local finite-current
  quotients.  The finite-window normalized BMK identity is not asserted on
  the native current factorization object.
```

### Replace `appendix-factorization-current-conventions.tex:630-695`

```tex
\begin{proof}
  The Bochner--Martinelli--Koppelman identity applies to the uncut kernel
  on \(B_\zeta\times B_z\setminus\Delta\).  After multiplication by
  \(\chi(\zeta)\chi(z)\vartheta_\epsilon(|\zeta-z|)\), differentiation
  gives
  \[
  \begin{aligned}
    \bar\partial
    \bigl(\chi(\zeta)\chi(z)\vartheta_\epsilon K_{\mathrm{BM}}\bigr)
      &=
      \chi(\zeta)\chi(z)\vartheta_\epsilon\,
      \bar\partial K_{\mathrm{BM}} \\
      &\quad
      +\bar\partial(\chi(\zeta)\chi(z))\,
      \vartheta_\epsilon K_{\mathrm{BM}} \\
      &\quad
      +\chi(\zeta)\chi(z)\,
      \bar\partial\vartheta_\epsilon\wedge K_{\mathrm{BM}} .
  \end{aligned}
  \]
  The second term is collar-supported.  The third term is the annular
  diagonal current and is not a collar term.  The estimate
  \(|K_{\mathrm{BM}}|\sim r^{-3}\) in real dimension four gives the
  current limit on every fixed finite configuration stratum.

  The formula for \(i_N\) is fixed by integration by parts:
  \[
    \left\langle
      \frac{(-1)^{a+b}}{a!\,b!}
      \partial_{z_1}^a\partial_{z_2}^b\delta_0,\,
      f
    \right\rangle
    =
    [z_1^az_2^b]f
    =
    \operatorname{Res}_0(\rho_{a,b}f).
  \]
  Hence \(p_N\) and \(i_N\) are the finite Matlis moment map and
  derivative-delta section after the diagonal orientation convention is
  declared.

  For the analytic one-pair quotient, \(H_\chi^0I_{\mathrm{an}}=0\)
  implies that the homotopy descends to the homotopy cofiber of
  \(I_{\mathrm{an}}K_N\to C^\bullet(B_2,B_1)\).  In that quotient
  \(I_{\mathrm{an}}P_{\mathrm{an}}\) is identified with \(i_Np_N\), giving
  the displayed derived quotient identity.

  The strict support-local quotient is impossible.  By
  Proposition~\ref{prop:app-matlis-coadjoint-action},
  \[
    z_1^p z_2^q\cdot\rho_{i,j}
    =
    -(pj-qi+p-q)\rho_{i-p+1,j-q+1}.
  \]
  With \(p=N+2\), \(q=0\), \(i=N+1\), and \(j=0\),
  \[
    z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1}.
  \]
  The source is killed by a support-local finite-window relation, while
  the target is retained for \(N\geq1\).  Thus the relation is not stable
  under the full Hamiltonian action, so the current action and hence the
  native factorization-current bracket cannot descend to such a quotient.
\end{proof}
```

## Claim-Status Recommendation

- Proved: BMK kernel/current-limit data on fixed finite strata; Matlis
  derivative-delta normalization after diagonal orientation is declared;
  finite moment maps; arity-two Hamiltonian/Matlis coefficient formulas as
  output projections; strict support-local finite-current quotient
  obstruction for \(N\geq1\).
- Conditional construction: one-pair derived analytic quotient, conditional
  on choosing the full analytic BMK contraction
  \(\bar\partial H_\chi^0+H_\chi^0\bar\partial
  =\operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}}\) and the diagonal
  convention.
- False as currently written: the finite-window normalized identity on the
  full compact-support/current complex or on a strict support-local
  finite-current factorization quotient.
- Downstream target: either all-window/pro-Matlis transfer, or a finite
  projected \(L_\infty\) factorization package whose first escaped-mode
  operation satisfies
  \[
    \kappa_N(z_1^{N+2},\rho_{N+1,0})=-(N+2)\rho_{0,1}.
  \]

## Verification Commands

Run these before applying the TeX replacements, because concurrent agents
are active:

```bash
git status --short
rg -n "finite-window BMK|H_\\{chi,N\\}|H_\\{mathrm\\{BM\\},N\\}|Ob\\^\\{\\\\infty\\}_\\{\\\\mathrm\\{BM\\}\\}|finite-window arity-two|normalized finite-window identity" main.tex appendix-factorization-current-conventions.tex theorem-lanes.tex claim-strength-ledger.tex open-obligations.tex
nl -ba main.tex | sed -n '1235,1465p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '395,700p'
nl -ba appendix-matlis-principal-parts.tex | sed -n '163,217p'
```

Boundary-mode arithmetic check:

```bash
python3 - <<'PY'
N = 5
p, q, i, j = N + 2, 0, N + 1, 0
coeff = -(p*j - q*i + p - q)
target = (i - p + 1, j - q + 1)
print(coeff, target)
assert coeff == -(N + 2)
assert target == (0, 1)
PY
```

No PDF build is required for this report-only pass.  Build only after the
integration owner edits TeX.
