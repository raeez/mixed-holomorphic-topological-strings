# Agent 183 report: Moyal-Capelli normalization

Date: 2026-04-30.

## Scope

Owned manuscript path:

- `appendix-radial-parts-moyal.tex`

Owned script path allowed only if essential:

- `scripts/quantum_shear_trace_diagram_normal_form.py`

The script was read and executed but not edited.  The existing staged script
addition predates this pass.

## Stable core after attack

The Weyl/Moyal algebraic target is stable with the raw odd coefficients
\[
  [f,g]_{\mathrm{raw}}^{(2s+1)}
  =
  \frac{\hbar^{2s+1}}{2^{2s}(2s+1)!}P^{2s+1}(f,g),
  \qquad
  [f,g]_{\mathrm{raw}}^{(2s)}=0.
\]
The third raw term is therefore \(\hbar^3P^3(f,g)/24\).  I added the
explicit finite check
\[
  f=z_1^4z_2^2,\qquad g=z_1^2z_2^4,
\]
for which
\[
  P(f,g)=12z_1^5z_2^5,\quad
  P^3(f,g)=-960z_1^3z_2^3,\quad
  P^5(f,g)=11520z_1z_2,
\]
and hence
\[
  [f,g]_{\mathrm{raw}}
  =
  12\hbar z_1^5z_2^5
  -40\hbar^3 z_1^3z_2^3
  +6\hbar^5 z_1z_2 .
\]
This is in `appendix-radial-parts-moyal.tex:142`.

## Healed theorem surface

I added Proposition `prop:app-moyal-capelli-realization-boundary` at
`appendix-radial-parts-moyal.tex:1368`.  It records the exact surface now used
by the degree-zero sector:

1. Formal Weyl/Moyal coefficients, including the \(1/24\) third term.
2. The finite-rank brane algebra as the degree-zero normalizer quotient by the
   traceless quantum moment ideal.
3. The normal-ordered contact relation
   \[
     YX-XY+\hbar N I\equiv0
     \pmod{\mathcal W_N\widehat\mu(\mathfrak{sl}_N)}.
   \]
   This is the scalar Capelli shift.  It is absorbed by the triangular
   \(T_{a,b}\leftrightarrow J_N(z_1^az_2^b)\) change of basis.  The scalar
   Hamiltonian line is killed only after passing to \(\bar A_\hbar\) and to the
   empty-trace quotient.
4. The finite-\(N\) Hamiltonian-reduction identity
   \[
     \hbar^{-1}[J_N(f),J_N(g)]
     =
     J_N(\{f,g\}_\hbar)
   \]
   is proved only relative to the stated radial-parts input.  Without that
   input, the exact obstruction is the moment-ideal primitive
   \(E_{a,b,N}=\sum A^j{}_i(a,b,N)\widehat\mu^i{}_j\), equivalently the free
   normal-diagram obstruction class \(\mathfrak o_{a,b}\).
5. The principal-part target is the continuous \(\bar A_\hbar\)-coadjoint
   module
   \[
     (\operatorname{ad}^{\vee}_{f,\hbar}\rho)(g)
     =
     -\rho(\{f,g\}_\hbar),
   \]
   with the displayed finite monomial formula.  The \(r=1\) term is the
   classical Matlis action; the \(r\ge3\) terms are genuine Moyal corrections,
   not the polynomial one-\(\psi\) PBW action.
6. The reduced open-line Wick graph computation realizes the algebraic Moyal
   product with midpoint propagator.  It does not prove an unreduced
   Costello graph/QME realization.  That realization still requires the
   brane-defect propagator, counterterms, anomaly cancellation, and
   \(d_{\mathrm{QME}}\)-homotopies in the local BV complex.

## Attacks and outcomes

- Coefficient attack: passed.  The direct \(P^1,P^3,P^5\) computation above
  fixes the \(1/24\) and \(1/1920\) normalizations independently of radial
  parts.
- Scalar attack: healed.  The Capelli contact term is now explicitly separated
  from the reduced scalar quotient.  The theorem no longer silently identifies
  the unreduced \(U(1)\) line with the scalar-free Moyal target.
- Finite-\(N\) attack: conditionally healed.  The finite-\(N\) relation is
  stated relative to radial parts; the exact obstruction is named when that
  input is absent.
- Principal-part attack: healed at the algebraic target level.  The action is
  Moyal coadjoint, not merely classical Matlis and not the one-\(\psi\) PBW
  action.
- Costello/QME attack: boundary healed.  The reduced Wick graph result is not
  promoted to an unreduced Costello graph/QME theorem.

## Commands

- `python3 scripts/check_moyal_coefficients.py`
  - PASS.
  - Moyal sweep: 14641 monomial pairs, exponents \(\le 10\), odd orders
    \(\le 11\).
  - Coefficients: \(1\), \(1/24\), \(1/1920\), \(1/322560\),
    \(1/92897280\), \(1/40874803200\).
  - Capelli round trip: 121 monomials PASS.
  - Direct radial restrictions for \(N=2,3\): 80 checks each PASS.
  - Higher pair above: PASS with
    \(12\hbar z_1^5z_2^5-40\hbar^3z_1^3z_2^3+6\hbar^5z_1z_2\).

- `python3 scripts/quantum_shear_trace_diagram_normal_form.py`
  - PASS.
  - Default candidates reduce to zero free residual, including the \(K_{4,4}\)
    correction.

- `python3 scripts/quantum_shear_trace_diagram_normal_form.py --case 4,4 --classical-only --max-terms 8`
  - Expected failure.
  - The residual has four displayed terms:
    \[
      \frac{43}{7}\hbar^2D[(X0>1,X1>2,Y2>3,Y3>0)]
      -\frac{43}{7}\hbar^2D[(X0>1,X2>3,Y1>2,Y3>0)]
    \]
    plus
    \[
      -\frac{43}{7}\hbar^3D[(X0>0)(Y0>0)]
      +\frac{43}{7}\hbar^3N D[(X0>1,Y1>0)].
    \]
  - This confirms that the classical cyclic lift alone is not the finite
    correction.

- `python3 scripts/quantum_shear_trace_diagram_normal_form.py --case 3,7 --solve-classical --max-terms 20`
  - PASS.
  - Classical cyclic lift found with support 11 and zero residual.

- `make pdf`
  - PASS.
  - Output: `out/main.pdf`, 372 pages.
  - Remaining TeX warnings are ordinary underfull/overfull box warnings and
    font metric warnings already present in the manuscript build.  The appendix
    still has the pre-existing overfull display at line 638.

Exploratory larger kernel-correction runs were stopped before completion and
are not used as evidence.

## Residual obligations

1. The all-bidegree radial-parts closure remains open.  Existing certificates
   cover \(K_{4,4}\) and finite cases such as \((3,6),(6,3)\), but they are not
   a uniform contracting homotopy.
2. The finite-\(N\) theorem is still conditional on the external radial-parts
   input unless the moment-ideal primitive or free normal-diagram obstruction
   is killed uniformly.
3. The principal-part Moyal coadjoint action is an algebraic target statement.
   It is not yet a full factorization-algebra or unreduced BV/QME realization.
4. The Costello graph/QME realization requires separate propagator,
   counterterm, anomaly, and \(d_{\mathrm{QME}}\)-homotopy data.
