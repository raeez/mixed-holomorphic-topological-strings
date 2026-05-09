# Source and Convention Ledger

Date: 2026-04-28

Scope: internal ledger for the reconstituted local theorem. It records
source obligations and convention translations. It does not import a
new theorem into the manuscript.

## Local Spine

The local theorem is the formal Hamiltonian disk theorem at
`\R\times\widehat{\C^2}_0`: Dirac brane probe, continuous CE/PV
derived centre, Matlis principal parts, de Rham-current factorization
on the brane line, scalar-reduced Moyal/Capelli degree-zero
quantization, and the scalar `U(1)` anomaly.

Claim strength is controlled by `claim-strength-ledger.tex:10-18` and
`claim-strength-ledger.tex:25-114`. The theorem-lane section is an
index, not an independent proof block (`theorem-lanes.tex:1-10`).
Open obligations are explicit in `open-obligations.tex:1-104`.

## Primary-Source Ledger

| Source family | Local use | Local anchors | Convention translation | Not imported | Residual source obligation |
|---|---|---|---|---|---|
| BCOV, Bershadsky-Cecotti-Ooguri-Vafa 1993/1994 | Motivation and closed B-model/Kodaira-Spencer convention template. | Bibliography key `bcov`; local use `main.tex:170-178`, `main.tex:689-696`, `main.tex:795-797`; BCOV comparison `tate-P3-universality.tex:140-147`; verified source anchors below. | The manuscript works on a holomorphic-symplectic surface, with Hamiltonian BF fields `\mathfrak h\ltimes\mathfrak h^\vee[1]`, not compact CY3 BCOV. | No compact CY3 anomaly cancellation, no global BCOV theorem, no `\Phi_d` output, no ambient Kodaira-Spencer realization theorem. | Closed to exact BCOV motivation/source equations: Sec. 5.2, Eq. (5.2), and Sec. 5.3, Eqs. (5.14),(5.15). Any stronger local cotangent/divergence normalization still needs a matched local comparison, not a BCOV import. |
| Witten open string field theory | Motivation for cyclic open field theory and the central-operation target. | Bibliography key `witten-cs`; principle use `principles.tex:56-71`; open-field convention `main.tex:940-943`; local centrality firewall `main.tex:230-237`; verified source anchors below. | Witten supplies cyclic open-field-theory and Chern-Simons/holomorphic-Chern-Simons source conventions. The local proof is the finite Dirac/Koszul matrix model and the CE/PV calculation. | No global open SFT construction, no physical centrality theorem beyond the local algebraic map, no theorem-level "closed fields act centrally" import. | Exact cyclic/open-SFT anchors found: Sec. 4.1, Eqs. (4.1),(4.2), Chan-Paton passage, Eqs. (4.8),(4.9),(4.52). "Witten centrality" remains residual if stated beyond the reduced local CE/PV theorem. |
| Loday-Quillen-Tsygan | Stable large-`N` analogy for matrix Lie algebra homology and cyclic homology. | Bibliography `main.tex:5922-5942`; local theorem statement `main.tex:1004-1027`. | LQT is a template. The local reduced Hamiltonian sector is proved using Procesi-Razmyslov plus the Koszul differential. | No global `HC_{*-1}` convention is imported into the local theorem (`main.tex:1022-1027`). | Add exact theorem/page references in Loday-Quillen 1984 and Tsygan 1983 if the manuscript uses LQT as proof rather than analogy. |
| Procesi-Razmyslov | Stable trace generators and finite trace identity background. | Bibliography `main.tex:6103-6123`; use `main.tex:984-989`, `theorem-lanes.tex:71-80`; verified source anchors below. | Work degreewise in the stable connected range. Finite-`N` identities remain present and are not erased by the stable statement. | No unstable finite-`N` freeness. No principal-part coadjoint module is obtained from trace-word invariant theory. | Stable trace generation and trace-identity ideal anchors are now verified from Procesi, Thms. 1.3, 4.5, 4.6, and Razmyslov, Thm. 2. Residual: Procesi PDF was verified from a local mirror copy, not an official publisher download. |
| Capelli and Howe-Capelli | Order-one normal-ordering/Capelli shift and Weyl trace basis change. | Bibliography `main.tex:6166-6184`; use `main.tex:436-450`; triangular formula `appendix-radial-parts-moyal.tex:102-143`; verified Howe anchor below. | The scalar line is killed in `\bar A_\hbar`; before reduction the same line appears as `\hbar N` (`appendix-radial-parts-moyal.tex:254-263`). | No extra anomaly beyond the scalar `U(1)` class. No descendant-sector quantization. | Howe, Sec. 5(f), Eq. (C), verifies the standard Capelli identity source. Residual remains closed negatively: no primary source was found for the exact bivariate triangular Weyl trace formula. The local contraction proof and `scripts/check_moyal_coefficients.py` are the proof/evidence for that normalization. |
| Harish-Chandra, Wallach, Levasseur-Stafford | External radial-parts input for invariant differential operators. | Bibliography `main.tex:6003-6047`; conditional use `main.tex:4895-4958`; restated input `appendix-radial-parts-moyal.tex:145-164`; verified Levasseur-Stafford 1996 anchors below. | The required convention is the Vandermonde-conjugated radial map whose kernel on invariants is the quantum moment-map ideal and whose quotient lands in Weyl-invariant differential operators on the regular Cartan. | The script is not an all-`N` proof. The radial input does not construct Costello graphs. | Levasseur-Stafford 1996 verifies the Harish-Chandra homomorphism, the kernel problem, and the kernel theorem at Thms. 1.1 and 5.5, with its introduction citing the 1995 surjectivity result. Residual remains: exact primary-source page anchors for the Vandermonde-conjugated injective radial-part convention used here were not verified from Harish-Chandra 1964, Wallach 1993, or Levasseur-Stafford 1995. |
| Costello 2011 | Heat-kernel BV, RG flow, graph grading, locality/QME vocabulary. | Bibliography `main.tex:6049-6060`; coefficient requirements `tate-T1-weighted-completion.tex:60-117`; Hadamard reduction `tate-P1-hadamard-mittag-leffler.tex:21-45`, `tate-P1-hadamard-mittag-leffler.tex:123-165`; verified arXiv anchors below and `references/primary-sources/costello-cg-source-anchors-2026-04-28.md`. | Costello's analytic formalism is used only after supplying the weighted coefficient kernel and the mixed brane-defect data. | No all-order Costello graph realization, no automatic QME solution, no regulator independence. | Costello arXiv anchors verify the formal heat-kernel/RG/QME package: Thms. A-D, Lem. 1.8.1, Thm. 15.5.2. Residual: exact AMS book anchors for `Thm. 5.0.7`, `Thm. 5.0.1`, `Sec. 5.6`, `Sec. 5.7`, and `Lem. 6.4.1` were not verified; TeX has been hardened so these exact numbers do not carry theorem weight. |
| Costello-Li 2012/2015 | Motivation and negative applicability check for pure/open-closed BCOV quantization. | Bibliography `main.tex:6062-6077`; hypotheses and failures `tate-T4-bv-vanishing.tex:17-45`, `tate-T4-bv-vanishing.tex:56-107`; non-transfer corollary `tate-T4-bv-vanishing.tex:126-150`; verified source anchors below. | Their compact/pure or flat supergroup hypotheses do not match `\R^2\times\C^2` with an ordinary `\mathfrak{gl}_N` brane line. | No Costello-Li anomaly cancellation or BV-cohomology vanishing closes the local unreduced cotangent lift. | Exact Costello-Li anchors found for BCOV field/quantization definitions and open-closed annulus quantization theorems. Residual remains the local extension listed in `tate-T4-bv-vanishing.tex:154-184`: noncompact/Omega background, mixed kinematics, brane-defect extension, and coefficient-system Tate completion. |
| Costello-Gwilliam factorization | Locally constant factorization, cosheaf/basis-extension, observables, and Noether vocabulary. | Bibliography `main.tex:6079-6100`; CG/Lurie comparison `tate-T3-quillen-equivalence.tex:453-461`; residual Weiss condition `tate-T3-quillen-equivalence.tex:524-554`; source anchor `references/primary-sources/costello-cg-source-anchors-2026-04-28.md`. | The brane-line current model is interval-wise locally constant by the local de Rham contraction. Costello-Gwilliam supplies vocabulary: Vol. I `Sec. 6.1`, `Sec. 6.4`, `Sec. 6.5`, `Sec. 7.2`; Vol. II `Sec. 8.5`, `Sec. 8.6`, `Secs. 11-13`, and excerpt `Thm. 1.5.1` for Noether/factorization-envelope language. | No unrestricted factorization-centre theorem, no unreduced BV/factorization-centre morphism, and no automatic Weiss descent for the higher-dimensional unreduced algebra. | Section-level Cambridge anchors are verified; theorem-level full-text anchors for Weiss descent/local constancy/central operations are not. The old `Vol. I Sec. 3.3` local-constancy citation was wrong for the published contents and has been replaced. |
| Matlis/local cohomology/Grothendieck residue | Continuous cotangent module, no-polynomial theorem, and limited Fourier--Rees label bridge. | Local proof `appendix-matlis-principal-parts.tex`; main form `main.tex:3890-3995`; local dictionary `local-dictionary.tex:116-152`; bibliography keys `matlis-injective`, `hartshorne-local-cohomology`, `kunz-residues-duality`; source anchor `references/primary-sources/matlis-local-cohomology-residue-anchor.md`. | `\mathfrak h^\vee_{\mathrm{cont}}` is the reduced scalar-annihilator `Ann(C.1) subset H^2_m(C[[z1,z2]]) dz1 dz2`; the basis is `\rho_{a,b}`, `a+b>0`. This is a `C`-linear Hamiltonian-coadjoint module, not an `R`-submodule. The Fourier twist is the Rees lattice `D_hbar/(z1,z2)`, embedded in the Cech model by `hbar^(a+b)a!b!rho_{a,b}` and equal to the full principal-part lattice only over `C((hbar))`. | No ordinary or same-action `\mathfrak h`-module isomorphism `\Psi_{a,b}\cong\rho_{a,b}`; no literal `R`-module Matlis dual of `R/C.1` because `C.1` is not an `R`-submodule. | Closed for this lane. Matlis duality anchors: Prop. 3.1, Thm. 4.2, Cor. 4.3. Grothendieck-Hartshorne anchors the local cohomology setting; Kunz-Cox-Dickenstein anchors the power-series residue/local-duality model. The Fourier--Rees statement is a local Rees Weyl calculation, not a separate sourced theorem. |
| Kontsevich deformation quantization | Formal Weyl/Moyal convention and translation-invariant constant-Poisson product. | Bibliography `main.tex:5991-6000`; use `main.tex:5381-5401`, `main.tex:5574-5579`. | The product is `m exp((hbar/2)P)` and the commutator has only odd powers. | No graph realization and no nonconstant Poisson formality issue. | Existing citation to Theorem 6.1 is sufficient for the constant-Poisson convention unless the text asks for global formality. |

## Verified Source Downloads and Anchors

All files named here are local under `references/primary-sources/`.
Anchors are recorded only when verified in the downloaded PDF text or
official source page. Source files downloaded but not used for theorem
anchors are listed in the checks section.

### Matlis and Local Cohomology

- `matlis-injective-modules-noetherian-rings.pdf` / `.txt`:
  Matlis, "Injective modules over Noetherian rings", verifies the
  indecomposable-injective classification and complete-local duality
  package needed as background. Exact anchors:
  Prop. 3.1, printed pp. 518-519; Thm. 4.2, printed pp. 526-528;
  Cor. 4.3, printed p. 528.
- `matlis-local-cohomology-residue-anchor.md`: source-anchor metadata
  for the closure of the residual around
  `E_R(k) \cong H^2_m(C[[z1,z2]]) dz1 dz2` and the Cech-Laurent
  residue basis. The anchor records:
  Hartshorne's Grothendieck local-cohomology seminar, Springer LNM 41,
  DOI `10.1007/BFb0073971`; Kunz-Cox-Dickenstein, AMS University
  Lecture Series 47, Chapter 5, "Residues and local cohomology for
  power series rings"; and Stacks tags 0DW3, 0DW6, 01XS as modern
  cross-checks for the local-duality and all-negative-Cech-monomial
  translation.
- The theorem-status correction is explicit: the reduced
  scalar-annihilator `P = Ann(C.1)` is not an `R`-submodule and is not
  a literal `R`-module Matlis dual of `R/C.1`. It is the `C`-linear
  Hamiltonian-coadjoint scalar reduction of the Matlis residue pairing.
  Under this corrected status, no Matlis/local-cohomology source
  residual remains in this lane.

### Procesi and Razmyslov

- `procesi-invariant-theory-nxn-matrices.pdf` / `.txt`: local mirror
  copy of Procesi, "The invariant theory of n x n matrices". Verified
  anchors: Thm. 1.3, printed p. 313, first fundamental theorem for
  polynomial invariants as trace monomials; Cor. 4.4, printed
  pp. 319-320, minimal multilinear trace identities; Thm. 4.5,
  printed pp. 320-322, generators for the trace-identity ideals;
  Thm. 4.6, printed pp. 322-323, `T`-ideal generation by the formal
  characteristic-polynomial expressions.
- `razmyslov-trace-identities.pdf` / `.txt`: MathNet English PDF of
  Razmyslov, "Trace identities of full matrix algebras over a field of
  characteristic zero". Verified anchors: Thm. 2 in Sec. 2 states that
  all trace identities are consequences of the Hamilton-Cayley identity;
  Sec. 5 gives the proof of Thm. 2.
- Residual: the Procesi file was verified from a local mirror PDF rather
  than an official publisher download. The theorem/page anchors are
  exact in that local source, but a publisher-grade archive copy would
  remove this provenance weakness.

### Capelli and Howe

- `howe-remarks-classical-invariant-theory.pdf` / `.txt`: official AMS
  PDF of Howe, "Remarks on classical invariant theory". Verified
  anchor: Sec. 5(f), "The Capelli identities", Eq. (C), printed p. 565,
  with the proof beginning immediately after the displayed identity.
- This verifies the standard Capelli source normalization, not the
  manuscript's exact bivariate triangular identity
  `sum_r (-hbar N/2)^r r! binom(a,r) binom(b,r) T_{a-r,b-r}`. Named
  residual closed negatively by the Worker 2 adversarial pass: no
  primary source for that exact triangular Weyl trace formula was
  found. The manuscript now relies on
  `appendix-radial-parts-moyal.tex:103-143` as the proof and on
  `scripts/check_moyal_coefficients.py` as bounded symbolic evidence.

### Harish-Chandra, Wallach, Levasseur-Stafford

- `levasseur-stafford-kernel-harish-chandra.pdf` / `.txt`: NUMDAM PDF
  of Levasseur-Stafford, "The kernel of an homomorphism of
  Harish-Chandra". Verified anchors: introduction states the
  Harish-Chandra homomorphism and surjectivity context; Thm. 1.1,
  printed p. 386, proves `J = D(g) tau(g)` and identifies the kernel;
  Thm. 5.5, printed p. 394, proves the reductive algebraic statement;
  Cor. 5.6, printed p. 395, gives the analytic-coefficient extension.
- This is not the exact radial-parts input used by
  `appendix-radial-parts-moyal.tex:145-164`. Named residual: exact
  theorem/page anchors are still needed for the Vandermonde-conjugated
  injective radial-part map into Weyl-invariant differential operators
  on the regular Cartan, preferably from Harish-Chandra 1964, Wallach
  1993, or Levasseur-Stafford 1995. The AMS pages downloaded in this
  pass did not expose a usable full-text source for those anchors.

### Witten

- `witten-hep-th-9207094.pdf` / `.txt`: arXiv PDF of Witten,
  "Chern-Simons gauge theory as a string theory". Verified anchors:
  Sec. 4.1, printed pp. 24-25, constructs open string field theory with
  product, BRST differential, trace, action Eq. (4.1), gauge variation
  Eq. (4.2), and Chan-Paton replacement by matrix factors; printed
  pp. 28-29 compute the cubic term and Chern-Simons Lagrangian,
  Eqs. (4.8),(4.9); Sec. 4.5 gives the B-model holomorphic
  Chern-Simons Lagrangian Eq. (4.52).
- Named residual: no Witten source theorem was found that would prove
  the manuscript's local centrality map. Witten should stay a cyclic
  open-SFT and Chern-Simons motivation/source-convention anchor.

### BCOV

- `bcov-hep-th-9309140.pdf` / `.txt`: arXiv PDF of
  Bershadsky-Cecotti-Ooguri-Vafa, "Kodaira-Spencer theory of gravity
  and exact results for quantum string amplitudes". Verified anchors:
  Sec. 5.1 introduces Kodaira-Spencer theory as a string field theory
  of the B-model; Sec. 5.2, printed pp. 64-65, writes the deformation
  field `A in Omega^{0,1}(TM)` and the Kodaira-Spencer equation,
  Eq. (5.2); Sec. 5.3 gives the constrained physical field and the
  action/equation of motion, Eqs. (5.14),(5.15), printed pp. 70, 75.
- Named residual: these anchors do not prove a theorem for the local
  holomorphic-symplectic surface model. Any exact divergence/cotangent
  convention for the manuscript's Hamiltonian BF complex must be checked
  locally against these equations.

### Costello

- `costello-renormalisation-bv-0706.1533.pdf` / `.txt`: arXiv preprint
  of Costello, "Renormalisation and the Batalin-Vilkovisky formalism".
  Verified anchors: Thm. A, asymptotics of Feynman graph integrals;
  Thm. B, counterterms/renormalization; Thm. C, bijection between local
  functionals and systems of effective actions; Lem. 1.8.1, QME/RG
  scale independence; Thm. D, local-to-global descent under triangular
  hypotheses; Thm. 15.5.2, local graph-integral asymptotics.
- Named residual: the manuscript bibliography cites Costello 2011.
  Exact AMS book anchors such as Ch. 5, Thm. 5.0.7, Thm. 5.0.1,
  Secs. 5.6-5.7, Chs. 6-7 were not verified from a book PDF/source.
  The manuscript now cites this material as the Costello
  heat-kernel/RG/locality package rather than relying on those exact
  theorem numbers.  The mixed brane-defect QME obstruction vanishing
  remains a local open theorem, not a consequence of the preprint
  anchors.

### Costello-Li

- `costello-li-quantum-bcov-1201.4501.pdf` / `.txt`: arXiv PDF of
  "Quantum BCOV theory on Calabi-Yau manifolds and the higher genus
  B-model". Verified anchors: Sec. 2 gives the BCOV fields and
  classical action conventions; Sec. 2.3-2.5 gives original and
  modified field complexes; Def. 3.4.1 states quantization by effective
  actions satisfying RG flow, QME, and locality.
- `costello-li-open-closed-bcov-1505.06703.pdf` / `.txt`: arXiv PDF of
  "Quantization of open-closed BCOV theory, I". Verified anchors:
  Thm. 9.0.11, printed p. 89, weak equivalence of quantization
  simplicial sets under the stated Calabi-Yau/conical/translation
  hypotheses; Thm. 9.0.12, printed p. 89, unique quantization of
  open-closed `(1,0)` BCOV theory to the annulus level; restated theorem
  on printed p. 97 for Calabi-Yau threefolds.
- Named residual: these hypotheses do not match the local
  `\R^2\times\C^2` ordinary `\mathfrak{gl}_N` brane-line model, so the
  source closes the negative applicability check but not the missing
  local mixed/Omega/brane-defect quantization theorem.

### Costello-Gwilliam

- `costello-gwilliam-vol1-cambridge.html` and
  `costello-gwilliam-vol2-cambridge.html`: official Cambridge Core
  pages verify the volume metadata and DOI records
  `10.1017/9781316678626` and `10.1017/9781316678664`.
- Official Cambridge frontmatter verifies section-level anchors:
  Vol. I `Sec. 6.1` factorization algebras, `Sec. 6.4` locally constant
  factorization algebras, `Sec. 6.5` cosheaf constructions, and
  `Sec. 7.2` extension from a basis; Vol. II `Sec. 8.5` and `Sec. 8.6`
  local observables as pre/factorization algebras, plus `Secs. 11-13`
  for the Noether theorem package.  The official Vol. II excerpt
  verifies `Thm. 1.5.1`, the introductory Noether statement producing a
  shifted central extension and a map from the twisted factorization
  envelope to quantum observables.
- Named residual: no official full-text theorem source was verified for
  Weiss descent/local constancy/central-operation theorem statements.
  These sources provide vocabulary and comparison structure only.  The
  local CE/PV and current computations remain the proof of the reduced
  Hamiltonian statements.

## Internal Proof and Computation Ledger

| Claim | Internal evidence | Script evidence | Status |
|---|---|---|---|
| Dirac brane probe | `theorem-lanes.tex:12-49`; local action and Ext/open field anchor `main.tex:927-944`. | None needed. | Proved in finite algebraic model. |
| Stable trace and one-psi PBW shadow | `theorem-lanes.tex:52-86`; dictionary separation `main.tex:1031-1088`; no-polynomial separation `appendix-matlis-principal-parts.tex:186-226`. | `python3 scripts/check_one_psi_homology.py`: 36 bidegrees through exponent 5; 240 Hamiltonian-action cases through exponent 3; 1225 Taylor-dual and 1225 principal-part coadjoint cases through exponent 5. | Proved degreewise stable; script is bounded reproduction. |
| CE/PV derived centre | `theorem-lanes.tex:88-138`; source-coordinate rule `local-dictionary.tex:79-113`. | None. | Proved cochain-level under completed continuous hypotheses; conilpotent bar-cobar only under its own hypothesis. |
| Matlis principal parts | `appendix-matlis-principal-parts.tex`; main theorem `main.tex:3907-3995`; source anchor `references/primary-sources/matlis-local-cohomology-residue-anchor.md`. | Same one-psi script checks the monomial coadjoint formulas; Wave 6 exact local calculation checks the Fourier--Rees `hbar^(a+b)a!b!` lattice factor. | Local coordinate proof present; Matlis duality and power-series local-cohomology/residue sources anchored; theorem status corrected to `C`-linear Hamiltonian-coadjoint module, not literal `R`-module quotient dual. The Fourier--Rees bridge is a Rees-lattice label comparison, not a same-action module isomorphism. |
| Factorization currents | `appendix-factorization-current-conventions.tex:12-169`; theorem lane `theorem-lanes.tex:188-241`. | None. | Reduced `P_0` current bookkeeping proved; unreduced centrality homotopies open. |
| Degree-zero Moyal/Capelli/radial parts | `appendix-radial-parts-moyal.tex:12-297`; conditional finite-`N` theorem `main.tex:4895-5020`; Moyal formula `main.tex:5403-5435`. | `python3 scripts/check_moyal_coefficients.py`: 14641 monomial pairs through order 11; 121 Capelli round trips; rank-2 radial tests; first/third open-line graph weights; all checks passed. | Capelli triangular formula locally proved; finite-`N` radial-parts theorem conditional on external Vandermonde-conjugated input; script is bounded reproduction. |
| First and third graph normalizations | Open-line computation `main.tex:5534-5638`; conditional Costello test `main.tex:5762-5821`; problem statement `main.tex:5824-5858`. | Moyal script confirms coefficients `1` and `1/24`. | Computed to stated order in reduced open-line model; Costello graph realization conditional. |
| Weighted Tate regulator | `tate-T1-weighted-completion.tex:15-23`; conditional lift `tate-T1-weighted-completion.tex:488-524`; sector restriction `tate-T1-weighted-completion.tex:571-586`. | None. | Proved in weighted coefficient model; regulator independence and QME obstruction remain open. |

## Convention Boundaries

- `\Psi_{a,b}` and `\rho_{a,b}` are different modules. The dictionary
  states this at `local-dictionary.tex:42-77` and `local-dictionary.tex:145-152`;
  the Matlis appendix proves the no-polynomial statement at
  `appendix-matlis-principal-parts.tex:186-226`.
- The Fourier--Rees bridge changes polarization and changes the lattice:
  `D_hbar/(z1,z2)` embeds in the Cech model as
  `sum hbar^(a+b) C[[hbar]] rho_{a,b}`. It becomes the full
  principal-part lattice only after `hbar` is inverted.
- Boundary Hamiltonian observables come from shifted-cotangent CE
  coordinates `u`, not Hamiltonian CE coordinates `c`; see
  `theorem-lanes.tex:118-123` and
  `appendix-factorization-current-conventions.tex:61-89`.
- Interval factorization uses
  `\Omega^\bullet_c(I)\widehat\otimes\mathfrak h`, with degree-zero
  measurement notation only after choosing a compactly supported density;
  see `appendix-factorization-current-conventions.tex:12-35`.
- The scalar line is killed in the reduced Hamiltonian algebra and
  appears before reduction as the Capelli shift; see
  `main.tex:157-167` and `appendix-radial-parts-moyal.tex:254-263`.
- The Weyl/Moyal product and local Capelli contraction proof fix the
  algebraic coefficients. They do not
  reconstruct an elliptic BV source or Costello brane-defect graph
  realization; see `main.tex:5365-5379` and
  `appendix-radial-parts-moyal.tex:290-297`.

## Physics-Motivation Attack-Heal Addendum

Worker 4 attacked the physics-first claims whose wording could smuggle
source-convention material into theorem status.

| Claim attacked | Failure mode | Local heal | Source anchors | Status recommendation |
|---|---|---|---|---|
| Witten centrality: "closed fields act centrally." | Witten 1992 verifies cyclic open SFT, Chan-Paton factors, Chern-Simons, and holomorphic Chern-Simons conventions; it does not prove the local CE/PV factorization-centre map. | `principles.tex:56-71` now labels Witten as a source convention; `main.tex:230-237` states that theorem-level centrality is not imported; `tate-P3-universality.tex:157-168` restricts protected-sector centrality to Theorem `\ref{thm:main-local}`. | Witten 1992, Sec. 4.1, Eqs. (4.1),(4.2); Chan-Paton passage; Eqs. (4.8),(4.9),(4.52). | Motivation/source convention. Theorem status only for the reduced local CE/PV calculation and its stated factorization-current consequences. |
| BCOV/Kodaira-Spencer prescription for the closed sector. | BCOV is a Calabi-Yau threefold B-model/Kodaira-Spencer theory. Treating it as prescribing the present holomorphic-symplectic surface model would import a compact/global theorem not proved here. | `main.tex:170-178` now says BCOV is a source-convention template and the local Hamiltonian sector is checked directly; `main.tex:689-696` and `tate-P3-universality.tex:140-147` block compact CY3 import. | BCOV 1993/1994, Sec. 5.2, Eq. (5.2); Sec. 5.3, Eqs. (5.14),(5.15). | Motivation/source convention. The local theorem proves only the Hamiltonian BF/CE/PV surface calculation. |
| Twisted-M protected-sector universality. | Costello twisted M-theory can motivate the protected sector, but no arbitrary ambient background is shown to produce the admissible Hamiltonian restriction. | `tate-P3-universality.tex:13-20`, `tate-P3-universality.tex:74-80`, and `tate-P3-universality.tex:149-168` keep the statement conditional on admissibility and deny ambient centrality. | Costello twisted-M citation remains motivational; the local proof anchors are Theorem `\ref{thm:main-local}` and Definition `\ref{defn:admissible-protected-hamiltonian-restriction}`. | Conditional protected-sector reduction only. No global twisted-M theorem. |
| Compact CY3 / Vol III / Igusa / BKM transfer. | The local Hamiltonian BF/Moyal calculation contains no compact CY3 datum, `\Phi_d` functor, Borcherds input, or BKM denominator identity. | No new transfer language was introduced; `tate-P3-universality.tex:168-179` and the no-transfer firewall below remain the governing boundary. | Cross-volume convention requires a separate matched theorem naming dimension, curve/worldsheet specialization, trace pairing, framing, topology, anomaly, deformation parameter, and QME hypothesis. | Not asserted. Any transfer remains a separate matched-conventions theorem. |

## No-Transfer Firewall

No compact CY3, Vol III, chiral-homology, Igusa, Borcherds, BKM,
`K3 x E`, or global BCOV consequence follows from the local theorem
without a separate matched-conventions theorem.

Local anchors:

- Claim ledger: `claim-strength-ledger.tex:112-117`.
- Open obligation: `open-obligations.tex:84-91`.
- Main convention firewall: `main.tex:5379-5392`.
- Costello-Li firewall: `tate-T4-bv-vanishing.tex:187-197`.
- Weighted Tate firewall: `tate-T1-weighted-completion.tex:590-602`.
- Protected-sector firewall: `tate-P3-universality.tex:171-180`.
- Cross-volume appendix: `tate-P5-cross-volume.tex:23-52`.

Any future transfer theorem must state at least: holomorphic dimension,
worldsheet or specialization curve, trace pairing, framing datum,
coefficient topology, anomaly normalization, deformation parameter, and
QME hypothesis (`tate-P5-cross-volume.tex:41-49`).

Sibling-side audit notes, 2026-04-28:

- Vol III has its own firewall at
  `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:223`:
  the comparison between the shadow tower and the B-model topological
  string genus expansion is separate and open for `g >= 2`. Stronger
  sibling text at
  `/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:1290`
  and
  `/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:1727`
  must be read under that firewall unless Vol III supplies an internal
  matched-conventions theorem. The local Hamiltonian BF/Moyal theorem is
  not evidence for those global BCOV/topological-string claims.
- Vol II actively includes
  `/Users/raeez/chiral-bar-cobar-vol2/appendices/cfg_side_by_side.tex`
  at `/Users/raeez/chiral-bar-cobar-vol2/main.tex:2244`; its Row 14
  theorem at `cfg_side_by_side.tex:659-697` states a BKM identification
  as proved. That claim, if retained, needs a Vol II/CFG proof. It cannot
  import the local Costello first/third graph-normalization calculation
  as an all-order BKM or compact `K3 x E` source theorem.
- The Igusa manuscript currently treats compact `K3 x E` realization
  data as conditional or separately supplied; no active Igusa import of
  the local theorem as a compact BKM proof was found in the checked
  anchors.

## Residual Missing Sources

1. Capelli/Howe: Howe's Capelli identity is anchored, but no primary
   source was found for the exact bivariate triangular normal-ordering
   formula used in the Weyl trace basis change. The manuscript now
   treats that formula as locally proved, not externally sourced.
2. Harish-Chandra/Wallach/Levasseur-Stafford: Levasseur-Stafford 1996
   kernel/surjectivity context is anchored, but exact theorem/page
   anchors for the Vandermonde-conjugated radial-parts injection remain
   missing. The manuscript now marks the finite-`N` theorem and
   degree-zero quantum upgrade as conditional on that external input.
3. Costello 2011: arXiv preprint anchors verify the analytic package,
   but exact AMS book theorem/page anchors for the 2011 book remain
   unverified. The TeX no longer depends on exact unverified theorem
   numbers such as `Thm. 5.0.7`.
4. Costello-Gwilliam: official Cambridge section-level anchors are
   verified for factorization, local constancy, cosheaves,
   extension-from-a-basis, observables, and Noether vocabulary. Full-text
   theorem anchors for Weiss descent and central operations remain
   unverified.
5. Witten centrality: Witten open-SFT/Chern-Simons anchors are verified;
   any theorem-level "centrality" claim remains unanchored and should be
   local or removed.
6. BCOV cotangent/divergence: BCOV source equations are verified only as
   motivation/convention templates; any stronger local cotangent or
   divergence normalization needs a local comparison proof.

## Scans and Checks Run

- `rg --files`
- `rg -n "BCOV|Bershadsky|Costello|Costello--Li|Costello-Li|Costello--Gwilliam|Costello-Gwilliam|Witten|factorization|factorisation|Matlis|local[- ]cohomology|Hartshorne|Grothendieck|Procesi|Razmyslov|Capelli|Harish|Wallach|Levasseur|Stafford|Loday|Quillen|Tsygan|cyclic" ...`
- `rg -n "Vol III|Igusa|BKM|Borcherds|compact CY|compact Calabi|CY3|CY_3|global BCOV|cross-volume|sister-volume|calabi-yau-quantum-groups|no.*transfer|not asserted|matched-conventions|matched proof|consequence" ...`
- `rg -n "script|computed|check_moyal|check_one_psi|finite.*check|Moyal|Weyl|radial|Capelli|one-psi|Psi|rho|principal-part|principal part" ...`
- Worker 5 cross-repo firewall audit: targeted `rg -n` scans for
  `topological-strings`, `BCOV`, `BKM`, `Borcherds`, `Igusa`,
  `compact CY`, `K3`, `Phi_d`, and global topological-string language
  in the four sibling repositories, followed by
  `nl -ba ... | sed -n ...` anchor inspection.
- Fixed-string scans for `cite{bcov}`, `cite{witten-cs}`,
  `cites{loday-quillen,tsygan}`, `cites{procesi,razmyslov}`,
  `cites{capelli,howe-capelli}`, `costello-renormalization`,
  `costello-li-quantum-bcov`, `costello-li-open-closed-bcov`,
  `costello-gwilliam`, `Matlis`, `Grothendieck`,
  `local cohomology`, `local-cohomology`, `Hartshorne`,
  `Harish-Chandra`, `Wallach`, and `Levasseur`.
- `python3 scripts/check_one_psi_homology.py`
- `python3 scripts/check_moyal_coefficients.py`
- `curl -L` downloads from arXiv, MSP/Pacific Journal, MathNet,
  AMS, NUMDAM, Cambridge Core, and a Procesi mirror PDF.
- `pdftotext -layout references/primary-sources/*.pdf ...`
- `pdfinfo references/primary-sources/*.pdf`
- Targeted `rg -n` and `sed -n` checks inside the extracted
  `references/primary-sources/*.txt` files for theorem/equation
  anchors.
- Worker 2 adversarial radial-parts pass:
  `rg -n "radial|Harish|Wallach|Levasseur|Stafford|Capelli|Howe|Vandermonde|normal-order|normal order|triangular|Moyal" ...`;
  targeted `sed -n`/`nl -ba` reads of `appendix-radial-parts-moyal.tex`,
  `main.tex`, `scripts/check_moyal_coefficients.py`,
  `references/primary-sources/howe-remarks-classical-invariant-theory.txt`,
  and `references/primary-sources/levasseur-stafford-kernel-harish-chandra.txt`;
  direct AMS PDF probes for Levasseur-Stafford 1995, Wallach 1993, and
  Harish-Chandra 1964 returned HTTP 403; web search found secondary
  Cherednik/Calogero-Moser lecture-note statements of the desired
  Vandermonde-conjugated theorem but no new primary full-text anchor.

- Worker 3 Costello/Costello-Gwilliam source-posture pass:
  `rg -n "Costello|Gwilliam|Weiss|locally constant|central operation|central operations|factorization centre|factorization center|descent|cosheaf|prefactorization|Hadamard|QME|RG flow|locality theorem" ...`;
  targeted `nl -ba ... | sed -n ...` reads of `main.tex`,
  `tate-T1-weighted-completion.tex`,
  `tate-P1-hadamard-mittag-leffler.tex`,
  `tate-T3-quillen-equivalence.tex`,
  `appendix-factorization-current-conventions.tex`, and this ledger;
  official-web checks of AMS and Cambridge pages/frontmatter/excerpts;
  local `rg` checks in `costello-renormalisation-bv-0706.1533.txt`;
  final negative scans for unverified `costello-renormalization` theorem
  cites and the stale `Vol. I Sec. 3.3` local-constancy anchor.

- Worker 5 ran a one-pass draft TeX check to `/tmp`:
  `pdflatex -interaction=nonstopmode -halt-on-error -draftmode
  -output-directory=/tmp/topological-strings-worker5-tex main.tex`.
  It exited 0. It reported ordinary one-pass undefined-reference
  warnings and pre-existing font/box warnings. No repo PDF build was run.
