# Failed-Theorem Surface Supremum Queue -- 2026-04-30

Scope: `main.tex`, `theorem-lanes.tex`, `open-obligations.tex`,
`claim-strength-ledger.tex`, `appendix-unreduced-bv-qme.tex`,
`appendix-radial-parts-moyal.tex`, and `scripts/`.

Status convention: a row is in the queue when the current text still
marks the surface as an exact obstruction, a theorem surface with missing
construction, a false-transfer gate, or script evidence that is not yet
theorem data. The supremum target is the strongest next true theorem: either
construct the missing habitat/map/homotopy/primitive/table, or prove the
named obstruction class nonzero.

## Stable Core Not In The Queue

- The native local model is the mixed HT theory on
  `R^2_top x C^2_hol`, with holomorphic `E_2`/factorization structure on
  `C^2`, not a curve VOA by default.
- The coordinate CE/PV and reduced Hamiltonian current surfaces are proved
  only in their admissible habitats.
- The formal Weyl/Moyal coefficients and reduced open-line Wick weights are
  algebraic target data. They do not, by themselves, solve analytic
  Costello graph/QME or unreduced factorization-center problems.

## Queue

### FTS-001 -- Native `E_2` all-window BM transfer

Anchors: `main.tex:1235-1445`, `theorem-lanes.tex:381-533`,
`claim-strength-ledger.tex:318-348`.

Still-visible failure: the finite-window arity-two BM transfer is present,
but strict all-window/all-arity BM transfer is not constructed. The exact
obstruction vector is
`Ob_BM^infty=(ob_mom, ob_collar, ob_3, ob_unif)`.

Supremum target: construct the strict filtered all-window BM transfer with
cutoff family, moment kernels, collar/support estimates on two- and
three-polydisk configurations, ternary homotopy, and uniform inverse-limit
control; or prove a named component of `Ob_BM^infty` nonzero.

### FTS-002 -- Native `E_2` to `C x R`, VOA, BRST, and Zhu gates

Anchors: `main.tex:1083-1166`, `theorem-lanes.tex:535-1024`,
`claim-strength-ledger.tex:350-386`.

Still-visible failure: the native object is the `C^2` holomorphic
factorization algebra. A curve VOA/OPE/Zhu statement needs a separate
controlled reduction; killing the `z_2` mode by slogan is false transfer.

Supremum target: construct
`R_CxR=(pi,B_z2,pi_!,K_red,L_red,pairing,H_anom)`, prove it preserves the
bracket, BV pairing, brane image, factorization products, and anomaly data,
then build the BRST differential, conformal/weight package, finite Laurent
OPE modes, and Zhu/zero-mode comparison. If this cannot be done, prove the
obstruction vector
`(ob_s,or, ob_z2,fib, ob_BV,pair, ob_fac, ob_brane, ob_anom, ob_Moyal)`.

### FTS-003 -- Strict product/direct-sum endpoints and Casimir kernels

Anchors: `main.tex:2164-2374`, `main.tex:7288-7397`,
`theorem-lanes.tex:1203-1270`, `theorem-lanes.tex:1350-1486`,
`theorem-lanes.tex:1784-1810`, `open-obligations.tex:33-100`,
`open-obligations.tex:237-254`, `claim-strength-ledger.tex:662-677`.

Still-visible failure: strict product/direct-sum completions do not carry the
global diagonal Casimir/kernel needed by the ambient `P_0`, boundary, or
bar-cobar claims. Finite-support checks remain finite-window tests, not a
strict endpoint theorem.

Supremum target: build a weighted/admissible coefficient habitat with a
convergent Casimir tensor, continuous bracket, coefficient coevaluation, and
bar-cobar compatibility; or prove the exact strict endpoint obstruction
`o_Cas`.

### FTS-004 -- Equivariant CE/PV refined bracket and global completion

Anchors: `theorem-lanes.tex:1488-1657`,
`claim-strength-ledger.tex:424-454`, `open-obligations.tex:571-729`.

Still-visible failure: the coordinate bracket formula is proved in a local
habitat, but mixed Cartan data, global completion, diagonal kernel,
normalization, and trace state data are not supplied.

Supremum target: construct the graded equivariant habitat with continuous
diagonal kernel, `Q_Omega=Q+iota_{V_Omega}`,
`Q_Omega^2=L_{V_Omega}`, coefficient ring, bracket continuity, and
normalization; or prove `ob_{Omega,CE/PV}`.

### FTS-005 -- Bar-cobar/open `A_infty` Koszul acceptance

Anchors: `main.tex:5352-5457`, `theorem-lanes.tex:1874-2132`,
`claim-strength-ledger.tex:679-695`.

Still-visible failure: the open `A_infty` Koszul/cyclic comparison is not a
consequence of the reduced CE/PV theorem alone. It needs the acceptance data
for the open model, semidirect hypotheses, conilpotence/completion, cyclic
trace, and homotopy transfer.

Supremum target: supply the acceptance datum `K1`--`K7` and prove the
relative bar-cobar/Quillen comparison in the admissible envelope; or prove
the cone/Roos obstruction to that comparison.

### FTS-006 -- Full open BV factorization center and unreduced cotangent lift

Anchors: `main.tex:4063-4230`, `main.tex:4785-4833`,
`main.tex:6412-6457`, `open-obligations.tex:529-569`,
`claim-strength-ledger.tex:183-196`, `claim-strength-ledger.tex:903-929`,
`appendix-unreduced-bv-qme.tex:3316-3396`.

Still-visible failure: the reduced principal-part current target works only
after retaining descendants or changing target. Full
`Z_fact^{P_0}(Obs_open^cl)` and the unreduced open BV identification still
need distributional principal-part currents, boundary representatives,
centrality homotopies, `P_0` product homotopies, coefficient kernels,
brane-defect propagator, and QME solution.

Supremum target: construct the unreduced homotopy-coherent factorization
center with descendant module, `QH+HQ=id-iN`, all centrality/product
homotopies, coefficient kernel, and brane-defect QME kernel; or prove the
obstruction vector
`(ob_prod_cent, ob^P0_cent, ob^bd_QME, delta_Weiss)`.

### FTS-007 -- PBW/Rees source action and polynomial descendant obstruction

Anchors: `main.tex:4063-4168`, `main.tex:6054-6134`,
`open-obligations.tex:177-228`, `claim-strength-ledger.tex:747-756`.

Still-visible failure: one-psi primitive labels do not supply the quantum
principal-part target. The polynomial open BV/Koszul category cannot realize
the principal-part module with the same Hamiltonian action.

Supremum target: construct the quantum principal-part descendant target and
homotopical Rees action, including the changed boundary target and
naturality; or prove the categorical obstruction that no polynomial
sub-bimodule with the same action can realize it.

### FTS-008 -- Analytic Costello specialization and first/third graph normalization

Anchors: `main.tex:7167-7317`, `main.tex:7319-7559`,
`main.tex:8389-8596`, `main.tex:8720-8787`,
`appendix-radial-parts-moyal.tex:1343-1439`,
`appendix-radial-parts-moyal.tex:1510-1624`.

Still-visible failure: the reduced open-line Wick computation gives the
Moyal coefficients, including first and third order, but it is not the
Costello closed-open graph theorem. The elliptic parent, reduction,
propagator, measure, counterterms, anomaly, and graph-normalization rows are
not supplied.

Supremum target: build a local mixed-HT Costello specialization whose
first- and third-order brane-defect graph rows have the reduced coefficients
`1` and `1/24` and whose anomaly/counterterm class vanishes; or prove the
local anomaly/normalization obstruction.

### FTS-009 -- Ordinary scalar-reduced `gl_N` QME

Anchors: `main.tex:7485-7559`, `open-obligations.tex:256-296`,
`appendix-unreduced-bv-qme.tex:135-260`,
`appendix-unreduced-bv-qme.tex:591-687`,
`appendix-unreduced-bv-qme.tex:3621-3665`,
`scripts/check_derived_intersection_N_extended.py:135-166`,
`scripts/check_derived_intersection_N_extended.py:392-419`.

Still-visible failure: the ordinary scalar-reduced `gl_N` branch has the
nonzero scalar obstruction `hbar N [bar c]`; no internal scalar counterterm
kills it.

Supremum target: either change the source/open model by the proved
central-character or balanced-supertrace branches, or prove the obstruction
theorem that a closed-exchange term must have leading scalar class
`[w_ext]= - hbar N [bar c]`; with `W_ext=0` or exact `w_ext`, the ordinary
branch remains obstructed.

### FTS-010 -- Non-scalar Costello/QME beyond the minimal branch

Anchors: `main.tex:7900-8109`, `open-obligations.tex:342-482`,
`claim-strength-ledger.tex:811-879`,
`appendix-unreduced-bv-qme.tex:2077-2385`,
`appendix-unreduced-bv-qme.tex:2926-3235`,
`scripts/finite_window_graph_array.py:1462-1549`.

Still-visible failure: the minimal full-equivariant finite-window branch is
proved only in its named row-suppressed habitat. A larger non-scalar QME
claim is not even formed until the scalar projection is a chain map and the
finite row table, scalar gates, source faces, signs, marker transports,
primitive candidates, and truncation matrices are supplied.

Supremum target: construct the native finite-window realization habitat with
`widehat sigma_sc`, codimension-two closed row array, residual vector
`r^M`, boundary matrix `A^M`, solvability `A^M c=-r^M`, truncation identity
`T^{M,N} A^M=A^N P^{M,N}`, and zero Roos `lim^1` class at every order; or
prove the obstruction pair `(([o^ns_M])_M, lambda)` and, for the
closed-exchange branch, the triple `(beta^cl, mu^cl, lambda^cl)`.

### FTS-011 -- `theta3` primitive and companion-face table

Anchors: `main.tex:8111-8225`, `open-obligations.tex:484-527`,
`claim-strength-ledger.tex:506-542`,
`appendix-unreduced-bv-qme.tex:2387-2485`,
`scripts/finite_window_graph_array.py:922-1455`,
`scripts/finite_window_graph_array.py:1498-1589`.

Still-visible failure: the current finite row package contains a closed
scalar-zero one-row complex
`K^0=0`, `K^1=C E_theta3`, `d=0`, with
`ell_theta3(E_theta3)=1`. No degree-zero primitive, CE ancestor, local
counterterm, or complete companion-face table is present.

Supremum target: heal by one of exactly three data:

- a CE ancestor with source boundary data, Hom-valued Bianchi closure,
  differential entry `dC=-E`, scalar projection zero, primitive transport,
  and zero Roos class;
- a local counterterm primitive with locality, `dC=-E`, scalar zero,
  transport, and zero Roos class;
- a complete companion-face table derived from the actual CE/source-face
  differential, with all scalar-zero faces, signed residual sum zero,
  codimension-two closure, and genuine truncation `v`-cocycle.

If none exists, prove the obstruction theorem represented by
`ell_theta3(E_theta3)=1`.

### FTS-012 -- Larger finite-window graph packages and marked scalar shadow

Anchors: `claim-strength-ledger.tex:253-280`,
`theorem-lanes.tex:3037-3265`,
`appendix-unreduced-bv-qme.tex:1900-1998`,
`appendix-unreduced-bv-qme.tex:3205-3315`,
`scripts/finite_window_graph_array.py:1539-1554`.

Still-visible failure: scalar-contact projection and marked-shadow
vanishing hold only in named habitats. Full finite closed graph lists need
actual boundary entries, incidence signs, marker transports, scalar gates,
row bases, locality data, and truncation matrices.

Supremum target: construct the full marked row table of `dK`, CE-source,
BV bracket, and counterterm rows with codimension-two closure; or identify
the first undefined/nonzero row and prove its finite-window cokernel class.

### FTS-013 -- Regular-density and wavefront-current graph branches

Anchors: `claim-strength-ledger.tex:289-295`,
`appendix-unreduced-bv-qme.tex:2209-2215`,
`appendix-unreduced-bv-qme.tex:2335-2346`.

Still-visible failure: the native finite-window habitat admits regular
compactly supported densities and graphwise wavefront-admissible currents
only when supplied for the chosen row. No theorem is present for arbitrary
`D'_c(I)` currents.

Supremum target: construct the wavefront-admissible current class and
renormalized graph weights with closure under all required faces; or prove
the exact wavefront obstruction `eta^reg`.

### FTS-014 -- Radial all-N image and all-bidegree homotopy/cokernel

Anchors: `main.tex:6933-7130`, `main.tex:7733-7898`,
`open-obligations.tex:845-898`, `claim-strength-ledger.tex:544-582`,
`claim-strength-ledger.tex:775-809`,
`appendix-radial-parts-moyal.tex:268-315`,
`appendix-radial-parts-moyal.tex:455-585`,
`appendix-radial-parts-moyal.tex:820-884`,
`appendix-radial-parts-moyal.tex:898-1125`,
`appendix-radial-parts-moyal.tex:1182-1496`,
`scripts/quantum_shear_primitive_search.py:1-28`,
`scripts/quantum_shear_universal_formula.py:397-431`,
`scripts/quantum_shear_trace_diagram_normal_form.py:1-19`,
`scripts/quantum_shear_trace_diagram_normal_form.py:745-760`.

Still-visible failure: the formal Moyal coefficients, reduced open-line
Wick expansion, edge strips, and finite certificates do not prove the
all-`N` radial image or the all-bidegree primitive. The exact obstruction is
the moment-ideal primitive problem, equivalently the free normal-diagram
cokernel class `o_{a,b}`. The `(7,7)` case is computationally open in the
current basis, not a proved nonzero obstruction.

Supremum target: prove the quantum shear congruence for all `a,b,N` by
constructing moment-ideal primitives
`E_{a,b,N}=sum A^j_i(a,b,N) muhat^i_j`; equivalently construct a functorial
all-bidegree splitting/homotopy `K_{a,b}` for
`C_{a,b}: ker partial -> Diag_{a,b}`. If false, produce a left-cokernel
functional annihilating `im C_{a,b}` and detecting `R^{free}_{a,b}`.

### FTS-015 -- Normal `Omega` finite-window habitat and QME

Anchors: `theorem-lanes.tex:2622-2834`,
`open-obligations.tex:571-729`, `claim-strength-ledger.tex:388-454`,
`claim-strength-ledger.tex:881-901`,
`appendix-unreduced-bv-qme.tex:2487-2835`,
`appendix-unreduced-bv-qme.tex:3431-3555`.

Still-visible failure: the normal `Omega` localization supplies a habitat,
coefficient ring, Cartan differential, normal contractions, and branch
normalization. It does not prove scalar projection, non-scalar QME, local
counterterms, primitive transport, or `Q_Omega` centrality.

Supremum target: construct the finite-window package over
`R_Omega^{N,M}` with `Q_Omega=Q+iota_{V_Omega}`,
`Q_Omega^2=L_{V_Omega}`, normal-weight contraction, residue/Euler
normalization, equivariant propagator, scalar projection with
`delta^0_{Omega,sigma,M}=0` and all `o^{(r)}_{Omega,sigma,M}=0`, kernel
counterterms, zero `lim^1 H^0`, and basic centrality homotopies; or prove
the corresponding obstruction classes.

### FTS-016 -- Stratified factorization on `(X,L)`

Anchors: `theorem-lanes.tex:2836-3035`,
`open-obligations.tex:571-729`, `claim-strength-ledger.tex:456-479`.

Still-visible failure: no stratified prefactorization/factorization functor
has been constructed with values on bulk opens, brane opens, collars,
products, descent, centrality homotopies, and QME curvature. Reduced current
brackets do not supply it.

Supremum target: construct `F^str_{Omega,N}` with branch choice, collar
module, products, descent, centrality homotopies, and QME curvature
calculation; or prove the vector `Ob_str,Omega,N`.

### FTS-017 -- Protected trace and physical `Omega` large-N state

Anchors: `theorem-lanes.tex:2836-3035`, `open-obligations.tex:730-843`,
`claim-strength-ledger.tex:482-504`, `claim-strength-ledger.tex:584-604`.

Still-visible failure: no continuous trace state, topology, normalization,
kernel/counterterm system, Ward identities, or cumulant/asymptotic theorem is
present. Algebraic brackets do not imply the physical protected trace.

Supremum target: construct the state `omega`, topology `T_Omega`,
normalization `nu_Omega`, kernels/counterterms, Ward identities, and
large-`N` cumulant/asymptotic estimates; or prove `Ob_Omega,phys`.

### FTS-018 -- Global Weiss/Ran descent and external comparison firewalls

Anchors: `main.tex:4215-4230`, `main.tex:8787-8814`,
`open-obligations.tex:923-963`, `claim-strength-ledger.tex:931-954`.

Still-visible failure: compact Calabi-Yau, CoHA, quintic, Igusa/BKM, and
cross-volume statements are external comparison lanes. A local theorem does
not transfer into them without matched conventions. Weiss/Ran descent also
requires period, source comparison, cotangent boundary, `P_0` center
homotopies, and descent data.

Supremum target: construct the matched-conventions comparison theorem and
vanishing obstruction vector, or quarantine the claim as external. For
Weiss/Ran, construct the descent package or prove the descent obstruction.

### FTS-019 -- Full Hamiltonian finite-dimensional truncation and Tate kernel

Anchors: `main.tex:7218-7397`, `claim-strength-ledger.tex:881-901`.

Still-visible failure: a naive finite-dimensional Lie truncation of the full
Hamiltonian sector is not a Lie/BV kernel theorem. The linear heat operator
does not supply the coefficient coevaluation, and the unweighted Tate
Casimir diverges.

Supremum target: build the weighted finite-window coefficient kernel with
coherent heat/gauge-fixing, coevaluation, admissible weights, and endpoint
control; or prove the finite-window/Tate Casimir obstruction.

## Script-Ledger Summary

- `scripts/finite_window_graph_array.py`: current `theta3` one-row case is
  asserted unsolved; exact primitive and complete companion-face payloads are
  interface fixtures, not present data.
- `scripts/check_derived_intersection_N_extended.py`: the ordinary scalar
  QME branch has nonzero one-loop obstruction `hbar N [bar c]`; the
  unconditional weighted quantum lift is false on the standard
  scalar-reduced branch.
- `scripts/quantum_shear_primitive_search.py`: finite-rank moment-ideal
  searches are evidence only, not all-`N` proof.
- `scripts/quantum_shear_universal_formula.py`: finite rows are explicitly
  evidence only; all-`N` proof requires a free indexed normal-ordering
  theorem.
- `scripts/quantum_shear_trace_diagram_normal_form.py`: free indexed normal
  diagrams give finite cokernel/kernel-correction certificates; they do not
  construct the all-bidegree homotopy.
