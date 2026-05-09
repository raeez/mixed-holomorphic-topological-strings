# Worker 2 Report: Wave 6 BV Cotangent / QME Obstruction

## Claim Attacked

The attacked claim was the unreduced BV cotangent centrality/QME lift
after wave5: the possibility that the reduced principal-part
factorization-current theorem, the primitive one-\(\psi\) descendants,
or the weighted Hadamard reduction already provide unreduced boundary
representatives and QME-compatible centrality homotopies.

## Result

The wave6 attack does not close the Costello graph theorem. It produces
a stronger obstruction than the wave5 index-shift mismatch:

1. In the polynomial unreduced BV/Koszul target, the two linear
   Hamiltonians act by scalar-translation derivations
   \[
     O_{1,0}\mapsto\partial_{\phi_2},\qquad
     O_{0,1}\mapsto-\partial_{\phi_1}.
   \]
   These commute with \(Q\psi=[\phi_1,\phi_2]\) and act locally
   nilpotently on every finite polynomial observable and on its
   \(Q\)-cohomology.

2. In the Matlis principal-part cotangent module,
   \[
     z_1\cdot\rho_{a,b}=-(b+1)\rho_{a,b+1},\qquad
     z_2\cdot\rho_{a,b}=(a+1)\rho_{a+1,b},
   \]
   hence
   \[
     z_1^r\cdot\rho_{a,b}
       =(-1)^r(b+1)\cdots(b+r)\rho_{a,b+r}\neq0,
       \qquad
     z_2^r\cdot\rho_{a,b}
       =(a+1)\cdots(a+r)\rho_{a+r,b}\neq0 .
   \]

Therefore no same-action centrality homotopy system can live inside the
polynomial unreduced boundary category. A corrected target would have
to add distributional principal-part boundary fields and then prove new
centrality homotopies there.

The mixed brane-defect QME obstruction was also sharpened. The scalar
contact is
\[
  \{I_\partial(a,f),I_\partial(b,g)\}_{\mathrm{open}}
  =
  I_\partial(ab,\{f,g\}_{\bar A})
  +N\,\omega(f,g)\int_\R a(t)b(t)\,dt ,
\]
and the quantum Capelli contact is
\[
  \operatorname{Tr}(A\,XY)-\operatorname{Tr}(A\,YX)
  =
  \hbar N\,\operatorname{Tr}(A)
  \quad\bmod\ \mathcal W_N\widehat\mu(\lie{gl}_N).
\]
With central boundary ghost \(|\gamma_{\mathbf 1}|=1\), the degree-one
QME representative is
\[
  \operatorname{Ob}_{\mathrm{sc}}(\gamma_{\mathbf 1};a,f;b,g)
  =
  \hbar N\,\omega(f,g)
  \int_\R a(t)b(t)\gamma_{\mathbf 1}(t)\,dt .
\]
Its associated graded CE class is \(\hbar N[\bar c]\). This class is
not exact in the scalar-reduced Hamiltonian source because
\(\omega(z_1,z_2)=1\) while \(\{z_1,z_2\}=1\) is zero in
\(\bar A=\C[z_1,z_2]/\C\cdot1\). The primitive
\(\eta(f)=-[f]_0\) exists only before scalar reduction.

## Heals Inscribed

- `principles.tex`: added the local-nilpotence obstruction and scalar
  QME obstruction summary.
- `open-obligations.tex`: upgraded the unreduced cotangent obligation
  from an index-shift mismatch to a polynomial-target no-go; made the
  scalar QME representative explicit.
- `theorem-lanes.tex`: added the local-nilpotence residual to the
  reduced principal-part lane; added the scalar associated-graded
  obstruction to the Moyal/QME lane; clarified the ordinary
  \(\lie{gl}_N\) scalar anomaly escape routes.
- `tate-T4-bv-vanishing.tex`: added
  `prop:t4-scalar-contact-obstruction` and made the brane-defect
  missing theorem decide the scalar class.
- `appendix-unreduced-bv-qme.tex`: added a self-contained no-go theorem
  and scalar-contact obstruction proposition.
- `main.tex`: included the new appendix after the factorization-current
  convention appendix.

## Sources and Anchors Used

- Costello renormalization/BV source ledger:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt`,
  especially the heat-kernel, locality, counterterm, and QME packages.
- Costello--Li open/closed BCOV ledger:
  `references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt`,
  including the \(\lie{gl}(N\mid N)\) cancellation theorem, the ordinary
  \(\lie{gl}_N\) anomaly warning, and the obstruction-class discussion.
- Costello--Li quantum BCOV ledger:
  `references/primary-sources/costello-li-quantum-bcov-1201.4501.txt`,
  for the QME/locality framing and why it does not directly close the
  mixed brane-defect coefficient problem.
- Internal anchors:
  `principles.tex`,
  `open-obligations.tex`,
  `theorem-lanes.tex`,
  `tate-T4-bv-vanishing.tex`,
  `appendix-factorization-current-conventions.tex`,
  `appendix-matlis-principal-parts.tex`,
  `appendix-radial-parts-moyal.tex`,
  `tate-T5-chain-level-primitive.tex`,
  and the wave5 report
  `reconstitution/attack-heal-wave5-unreduced-bv-2026-04-28.md`.

## Commands Run

```bash
python3 scripts/check_one_psi_homology.py
python3 scripts/check_moyal_coefficients.py
pdflatex -interaction=nonstopmode -halt-on-error -draftmode -output-directory=/tmp/topological-strings-wave6-bv main.tex
```

Both scripts passed. The one-\(\psi\) script reproduced the primitive
homology calculation and the quantum descendant mismatch
\(\operatorname{ad}^{\vee}_{z_1^4,\hbar}\delta_{1,1}
=-24\hbar^2\delta_{0,4}+\cdots\) versus the PBW action
\(\widetilde\Psi_{1,1}\mapsto4\widetilde\Psi_{4,0}\). The Moyal script
verified the first and third coefficients, Capelli round trip, radial
checks, rank-two commutators, cumulant, and open-line graph weights in
its finite sweeps.

The draft TeX pass completed without a fatal error and exercised
`appendix-unreduced-bv-qme.tex`. It still emitted ordinary one-pass
cross-reference warnings, including labels introduced in this wave.

## Operational Note

A relative `apply_patch` initially wrote the wave6 hunks to
`/Users/raeez/topological-strings`. I immediately reversed exactly
those hunks and deleted the two accidentally added files there. The
surviving edits are in
`/private/tmp/topological-strings-remainder-wave6-20260428-073738/bv-qme`.

## Remaining Open Questions

1. Construct a distributional principal-part boundary theory whose
   fields are not polynomial descendants and prove centrality homotopies
   there.
2. Produce a genuine closed-exchange graph with associated graded
   \(-\hbar N[\bar c]\), or choose a supertrace/central-character
   normalization that removes the scalar identity before claiming QME
   vanishing.
3. Match the all-order radial-parts source theorem to the precise
   quantum Hamiltonian reduction used here.
4. Prove the full mixed brane-defect Costello graph theorem, including
   locality, counterterms, BV Laplacian, and regulator independence in
   the weighted coefficient model.
