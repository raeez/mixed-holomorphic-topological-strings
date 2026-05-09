# Bochner-Martinelli Transfer for the Native C^2 E2 Lane

Date: 2026-04-30.
Lane: cutoff-controlled Bochner-Martinelli transfer for the native
holomorphic \(E_2\)-type factorization object on \(\mathbb C^2\).

## Verdict

The native object remains the two-complex-dimensional CE/factorization
algebra
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \bigl(\Omega_c^{0,\bullet}(B)\widehat\otimes
  (\mathfrak h\ltimes\mathcal P[1])\bigr),
  \qquad
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1 .
\]
The Bochner-Martinelli transfer can be made precise in finite
principal-part windows and in the support-at-the-collision subcomplex of
compactly supported Dolbeault currents.  The transfer identifies the
arity-two collision with the Hamiltonian bracket and the Matlis
coadjoint action.  It does not produce a curve VOA, a Zhu algebra, or a
Costello BV propagator.

The all-window strict transfer from the full smooth compact-support
Dolbeault complex to the direct-sum Matlis module
\(\mathcal P=\bigoplus_{a+b>0}\mathbb C\rho_{a,b}\) is not yet a theorem.
The full compact-support Dolbeault cohomology sees analytic functionals
on holomorphic functions; \(\mathcal P\) is the finite-order
support-at-zero part.  The exact remaining obstruction is therefore the
uniform finite-window/support-at-zero theorem stated below as
\(\operatorname{Ob}^{\infty}_{\mathrm{BM}}\).

## Transfer Habitat

Work with nested polydisks
\[
  B_0\Subset B_1\Subset B_2\Subset B\subset\mathbb C^2
\]
and choose \(\chi\in C_c^\infty(B_2)\), \(\chi=1\) on \(B_1\).  For a
finite Hamiltonian window \(N\), set
\[
  \mathfrak h_{\le N}=\mathfrak m/\mathfrak m^{N+1},\qquad
  \mathcal P_{\le N}
  =
  \bigoplus_{0<a+b\le N}\mathbb C\,\rho_{a,b},
  \qquad
  \mathfrak g_{\le N}=\mathfrak h_{\le N}\ltimes\mathcal P_{\le N}[1].
\]
The transfer is first a statement for
\[
  \Omega_c^{0,\bullet}(B)\widehat\otimes\mathfrak g_{\le N}
\]
and then for the filtered tower in \(N\).  Passing to
\(\mathcal P\) requires proving that all transferred operations preserve
finite principal-part order in this tower.

The principal-part basis is
\[
  \rho_{a,b}=z_1^{-a-1}z_2^{-b-1}\,dz_1dz_2,\qquad
  \operatorname{Res}_0(\rho_{a,b}z_1^mz_2^n)=\delta_{a,m}\delta_{b,n}.
\]
The support-at-zero Dolbeault current representing \(\rho_{a,b}\) is
normalized by
\[
  \Delta_{a,b}
  =
  \frac{(-1)^{a+b}}{a!\,b!}
  \partial_{z_1}^a\partial_{z_2}^b
  \delta_0\;d\bar z_1\wedge d\bar z_2,
  \qquad
  \langle \Delta_{a,b}, f\rangle
  =
  \operatorname{Res}_0(\rho_{a,b}f).
\]
This is the compact-support current model of the Matlis residue
functional.  A smooth compact-support top form generally has infinitely
many holomorphic moments and lands in the analytic dual, not in
\(\mathcal P\).

## Kernel

Put \(\eta=\zeta-z\), \(r^2=|\eta_1|^2+|\eta_2|^2\), and
\[
  d\bar\eta_j=d\bar\zeta_j-d\bar z_j .
\]
The homotopy kernel on
\((B_\zeta\times B_z)\setminus\Delta\) is the
Bochner-Martinelli-Koppelman current
\[
  K_{\mathrm{BM}}(\zeta,z)
  =
  \frac{1}{(2\pi i)^2}
  \frac{
    \overline{\eta_1}\,d\bar\eta_2
    -
    \overline{\eta_2}\,d\bar\eta_1
  }{r^4}
  \wedge d\zeta_1\wedge d\zeta_2 .
\]
The kernel displayed in `theorem-lanes.tex` is the \(d\bar z=0\)
component of this current.  That component is enough to write the scalar
Bochner-Martinelli integral, but the full Dolbeault homotopy requires the
\(d\bar z\)-terms.

For \(\epsilon>0\), choose a radial cutoff
\(\vartheta_\epsilon(r)\) equal to \(0\) for \(r\le\epsilon\) and \(1\)
for \(r\ge2\epsilon\).  Define
\[
  K_{\chi,\epsilon}(\zeta,z)
  =
  \chi(\zeta)\chi(z)\vartheta_\epsilon(|\zeta-z|)
  K_{\mathrm{BM}}(\zeta,z),
\]
and let \(H_{\chi}\) be the current limit
\[
  H_{\chi}\alpha(z)
  =
  \lim_{\epsilon\to0}
  \int_{\zeta\in B}
  K_{\chi,\epsilon}(\zeta,z)\wedge\alpha(\zeta).
\]
The singularity is locally integrable in real dimension four:
\(|K_{\mathrm{BM}}|\sim r^{-3}\), while the volume element contributes
\(r^3dr\).  Derivatives of order \(k\) satisfy the finite-distance
estimate
\[
  |\nabla^k K_{\mathrm{BM}}(\zeta,z)|
  \le C_k|\zeta-z|^{-3-k}.
\]

The principal-part face of the same transfer is the Cauchy expansion on
the product annulus \(|z_i|<|\zeta_i|\):
\[
  \frac{1}{(2\pi i)^2}
  \frac{d\zeta_1\wedge d\zeta_2}
       {(\zeta_1-z_1)(\zeta_2-z_2)}
  =
  \sum_{a,b\ge0}
  z_1^az_2^b\,\rho_{a,b}(\zeta).
\]
This is where the two-index principal-part module enters.  Replacing it
by a one-variable residue or the \(b=0\) line is not stable under the
Hamiltonian action.

## Normalized \(\bar\partial\) Identity

Let \(p_{\mathrm{an}}\) denote the compact-support Dolbeault moment map
on top degree:
\[
  p_{\mathrm{an}}(\alpha)(f)
  =
  \int_B f(z)\,\alpha^{0,2}(z)\wedge dz_1\wedge dz_2,
  \qquad f\in\mathcal O(B),
\]
and let \(i_{\mathrm{an}}\) be the corresponding support-at-the-collision
Dolbeault current inclusion.  With the normalization above,
\[
  \bar\partial H_{\chi}+H_{\chi}\bar\partial
  =
  \operatorname{id}-i_{\mathrm{an}}p_{\mathrm{an}}
  +E_{\chi},
\]
where the collar error \(E_{\chi}\) is supported in
\[
  \{z\in\operatorname{supp}d\chi\}\cup
  \{\zeta\in\operatorname{supp}d\chi\}.
\]
On the relative pair \(B_1\Subset B_2\), or after quotienting by collar
terms in the extension-by-zero factorization structure, the normalized
identity is
\[
  \bar\partial H_{\mathrm{BM}}+
  H_{\mathrm{BM}}\bar\partial
  =
  \operatorname{id}-i_{\mathrm{an}}p_{\mathrm{an}}.
\]
In the finite principal-part window this becomes
\[
  \bar\partial H_{\mathrm{BM},N}
  +H_{\mathrm{BM},N}\bar\partial
  =
  \operatorname{id}-i_Np_N
\]
on the finite moment quotient, where
\[
  p_N(\alpha)
  =
  \sum_{0<a+b\le N}
  p_{\mathrm{an}}(\alpha)(z_1^az_2^b)\,\rho_{a,b},
  \qquad
  i_N(\rho_{a,b})=\Delta_{a,b}.
\]
This is the correct normalized \(\bar\partial\) homotopy identity for
principal-part transfer.  The projection is not a projection from all
smooth compact-support top forms to the direct-sum \(\mathcal P\) unless
finite-order support at the collision has already been imposed.

## Support Estimates

Let \(K_i\Subset B_i\) be compact supports and let
\[
  \delta_{ij}=\operatorname{dist}(K_i,K_j)>0 .
\]
For disjoint binary configurations, the regularized kernel is smooth on
\(K_i\times K_j\), and for each finite \(C^k\)-seminorm
\[
  \|H_\chi\alpha\|_{C^k(K_j)}
  \le
  C_{k,K_i,K_j}\,
  \delta_{ij}^{-3-k}\,
  \|\alpha\|_{C^k(K_i)} .
\]
For three supports with pairwise distance at least \(\delta\), the
iterated kernels obey
\[
  \|H_\chi(H_\chi\alpha\wedge\beta)\|_{C^k(K_3)}
  \le
  C_{k,K_1,K_2,K_3}\,
  \delta^{-6-k}\,
  \|\alpha\|_{C^k(K_1)}\|\beta\|_{C^k(K_2)} .
\]
Thus binary and ternary factorization products are continuous on every
finite configuration stratum.  The only possible new term is supported
on collision faces, and at arity three on the small diagonal.

## Arity-Two Comparison

The transferred binary operation is
\[
  \ell_2^{\mathrm{BM}}(x,y)=p\,[i x,i y].
\]
For Hamiltonians \(f,g\in\mathfrak h\),
\[
  \ell_2^{\mathrm{BM}}(f,g)
  =
  \{f,g\}
  =
  \partial_{z_1}f\,\partial_{z_2}g
  -
  \partial_{z_2}f\,\partial_{z_1}g
  \pmod{\mathbb C}.
\]
For \(f=z_1^pz_2^q\) and
\(\rho_{i,j}=z_1^{-i-1}z_2^{-j-1}dz_1dz_2\),
\[
  \ell_2^{\mathrm{BM}}(f,\rho_{i,j})
  =
  f\cdot\rho_{i,j}
  =
  -(pj-qi+p-q)\rho_{i-p+1,j-q+1},
\]
with negative-index targets equal to zero, and
\[
  \ell_2^{\mathrm{BM}}(\rho,\sigma)=0 .
\]
The sign is forced by residue integration by parts:
\[
  \operatorname{Res}_0((f\cdot\rho)g)
  =
  -\operatorname{Res}_0(\rho\,\{f,g\}).
\]
This proves the arity-two Hamiltonian/coadjoint comparison in finite
principal-part windows and on the support-at-zero current subcomplex.

## First Ternary Compatibility

Homotopy transfer of the dg Lie bracket gives the first possible
higher operation
\[
  \ell_3^{\mathrm{BM}}(x,y,z)
  =
  p\,[H_{\mathrm{BM}}[i x,i y],i z]
  +\text{cyclic Koszul terms}.
\]
Equivalently, with
\[
  \kappa_\chi(x,y)=[i x,i y]-i\,\ell_2^{\mathrm{BM}}(x,y),
\]
the strict-Lie obstruction is
\[
  \operatorname{Ob}_3^\chi(x,y,z)
  =
  p\,[H_{\mathrm{BM}}\kappa_\chi(x,y),i z]
  +\text{cyclic Koszul terms}.
\]
For separated supports this vanishes by the support estimates.  On the
collision stratum its coefficient part is the Jacobiator of
\(\mathfrak h\ltimes\mathcal P[1]\), hence zero.  Any surviving term is
therefore a pure cutoff/collar term supported on the small diagonal.  The
remaining compatibility check is precisely
\[
  \operatorname{Ob}_3^\chi=0
\]
after passing from finite windows to the completed native habitat.  If it
does not vanish strictly, the correct output is an \(L_\infty\)-transfer
with this displayed \(\ell_3\), not a curve OPE.

## Attack-Heal Ledger

1. False full Dolbeault kernel.
   Attack: the displayed BM form without \(d\bar z\)-terms cannot be the
   homotopy kernel on all Dolbeault degrees.
   Heal: use the Koppelman form with
   \(d\bar\eta_j=d\bar\zeta_j-d\bar z_j\).  The displayed form is only
   its scalar component.

2. False projection to \(\mathcal P\).
   Attack: a general compact-support top form has infinitely many
   holomorphic moments and lands in the analytic dual of
   \(\mathcal O(B)\), not in the direct sum \(\mathcal P\).
   Heal: work in finite principal-part windows or in the finite-order
   support-at-zero current subcomplex.  The all-window theorem is
   \(\operatorname{Ob}^{\infty}_{\mathrm{BM}}\).

3. False one-variable reduction.
   Attack: setting \(z_2=0\) kills
   \(\{f,g\}=\partial_{z_1}f\partial_{z_2}g
   -\partial_{z_2}f\partial_{z_1}g\), and the \(b=0\) principal-part line
   is not coadjoint-stable.
   Heal: retain the two-index principal-part system.  A curve theorem may
   be stated only after the controlled \(\mathbb C\times\mathbb R\)
   reduction retaining \(z_2\).

4. False strict associativity from binary data alone.
   Attack: a homotopy transfer of a dg Lie bracket generally produces an
   \(L_\infty\) ternary operation.
   Heal: the first obstruction is the explicit
   \(\operatorname{Ob}_3^\chi\) above.  Its coefficient Jacobiator
   vanishes; the remaining term is the cutoff/collar small-diagonal
   check.

## Remaining Obstruction

\[
  \operatorname{Ob}^{\infty}_{\mathrm{BM}}
  =
  (\operatorname{ob}_{\mathrm{mom}},
   \operatorname{ob}_{\mathrm{collar}},
   \operatorname{ob}_{3},
   \operatorname{ob}_{\mathrm{unif}})
\]
where:

- \(\operatorname{ob}_{\mathrm{mom}}\): prove that the transfer restricts
  from analytic compact-support moments to finite-order principal parts,
  or keep finite windows explicitly.
- \(\operatorname{ob}_{\mathrm{collar}}\): prove that cutoff collar terms
  vanish in the extension-by-zero factorization maps for all chosen
  nested polydisks.
- \(\operatorname{ob}_{3}\): prove
  \(\operatorname{Ob}_3^\chi=0\) on the completed native habitat, or keep
  the resulting \(L_\infty\) ternary operation.
- \(\operatorname{ob}_{\mathrm{unif}}\): prove uniform estimates in \(N\)
  for the \(m\)-adic/principal-part tower.

Until these four components are closed, the manuscript may claim the
native CE/factorization object, the finite-window BM transfer datum, and
the arity-two Hamiltonian/coadjoint comparison.  It may not claim an
all-window strict BM transfer, a one-dimensional VOA, a Zhu comparison,
or a Costello graph/QME construction from this kernel.
