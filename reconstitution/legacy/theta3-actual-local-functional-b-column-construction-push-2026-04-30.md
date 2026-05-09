# Theta3 Actual Local-Functional B-Column Construction Push

Date: 2026-04-30.
Status: report-only construction push. No TeX, script, figure, source,
bibliography, PDF, or build artifact was edited.

## Decision

No theorem-grade scalar-zero local functional
\[
  B^2_{02,20}\in\mathcal K^0_{\mathrm{ns},2}(I)
\]
was constructed from the current data.

The formal matrix target is clear:
\[
  d_{\mathrm{ns},2}B^2_{02,20}
    =-\mathfrak b^2_{02,20},\qquad
  \widehat\sigma_{\mathrm{sc},2}(B^2_{02,20})=0,
\]
with boundary column
\[
  A_B^2=(0,0,-1)^T
\]
in the ordered lower basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}).
\]
Adjoining that column as a formal vector closes the lower matrix. It is not
an actual Costello local functional until the graph/counterterm habitat,
locality or wavefront class, scalar projection, and finite-window transport
are supplied.

The current checkout supplies only the source-coordinate lower column
\[
  D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2),\qquad
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},
\]
whose boundary is
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
  +\mathfrak b^2_{02,20}.
\]
Thus
\[
  A_D^2=(-2,2,1)^T.
\]
The desired Bianchi target \((0,0,-1)^T\) is not in the present boundary
image. The obstruction is the fixed-window cokernel
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*,
\]
with
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}((0,0,-1)^T)=-1.
\]

This is not a universal no-go in the full Costello complex. It is the exact
obstruction for the instantiated finite-window lower habitat and for the
current regular-density/wavefront theorem surfaces before a new actual
degree-zero graph/counterterm column is constructed.

## Actual-Functional Attempt

### Source-coordinate route

The source calculation gives
\[
  d_{\mathrm{CE}}\zeta^0_2
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]
Applying \(K^2_{\Theta_3}\) would give the desired lower primitive only if
the kernel were a chain map on this input. The defect is exactly
\[
  \mathfrak b^2_{02,20}
  =
  d_{\mathrm{ns},2}K^2_{\Theta_3}(\zeta^0_2)
  -
  K^2_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_2).
\]
Therefore the only actual lower column now present, \(D^2_{02,20}\), does
not kill the Bianchi row. A scalar multiple \(xD^2_{02,20}\) would satisfy
\[
  x(-2,2,1)^T=(0,0,-1)^T.
\]
The first two coordinates force \(x=0\); the Bianchi coordinate forces
\(x=-1\). Hence no \(B^2_{02,20}\) is obtained from the source-coordinate
span.

### Coefficient-current route

The coefficient-current kernel of
Appendix~\ref{sec:app-factorization-current-conventions} is algebraic:
\[
  u_{a(t)dt\otimes f}\mapsto \iota_I(B_f^w(a)),\qquad
  c_{B,\rho}\mapsto \iota_I(\Theta^w_\rho(B)).
\]
It is compatible with finite windows and weights, and after scalar
reduction it recovers the reduced current interface. It does not construct
the small-diagonal graph extension whose extension ambiguity could be a
Costello counterterm. Hence it does not contain a degree-zero element whose
QME differential is the Hom-valued Bianchi row
\(\mathfrak b^2_{02,20}\).

This route fails before the matrix stage: no local-functional representative
for \(B^2_{02,20}\) is produced.

### Regular-density graph route

The regular-density graph theorem gives a genuine Costello graph-kernel
layer when all external cotangent labels are smooth compactly supported
densities:
\[
  B_j=b_j(t)dt\in\mathcal D^{\mathrm{reg}}_c(I).
\]
For a fixed graph \(\Gamma\), finite window \(M\), and regular labels, it
constructs renormalized graph weights and local counterterms compatible
with interval extension, finite-window truncation, and weight transport.

This theorem supplies a habitat, not the missing column. To turn it into
\(B^2_{02,20}\), the following data must be supplied:

1. the marked graph or counterterm source producing the lower Bianchi row;
2. the renormalized weight and local counterterm formula for that source;
3. the row-coordinate map into
   \((E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})\);
4. the equality of the differential column with \((0,0,-1)^T\);
5. the scalar-chain projection on this graph/counterterm subhabitat.

None of these is present in the current data. Regular density locality would
be sufficient once the column is constructed, but it does not construct it.

### Wavefront-admissible route

The wavefront theorem enlarges the regular-density branch for fixed
graphwise admissible tuples
\[
  B_\bullet\in\mathcal D'_{c,\mathrm{WF}}(I;\Gamma,M).
\]
The product
\[
  K^M_{\Gamma,\alpha}B_\Gamma
\]
is defined only under Hormander transversality, finite scaling degree along
collision diagonals, and proper pushforward. The extension ambiguity is a
local counterterm supported on collision loci:
\[
  \sum_{\Delta,\alpha}\sum_{|\beta|\leq N_{\Gamma,\alpha,\Delta}}
  \partial_\nu^\beta\delta_\Delta\,S_{\Delta,\beta}.
\]

This gives the correct analytic shape of a possible \(B^2_{02,20}\), but
not the element. The current data do not specify:

1. the graph \(\Gamma\) and Hadamard coefficient \(K^M_{\Gamma,\alpha}\)
   whose extension ambiguity is the Bianchi row;
2. the admissible current tuple attached to \(\zeta^0_2\) and the
   \(\Theta_3\) source face;
3. the finite scaling degree and extension order along the relevant
   diagonal;
4. a choice of extension difference whose \(d_{\mathrm{ns},2}\)-boundary is
   exactly \(-\mathfrak b^2_{02,20}\);
5. compatibility of those choices under \(\pi_{M,N}\) and weight transport.

Arbitrary \(\mathcal D'_c(I)\) labels are explicitly not supported by the
current theorem surface. The appendix gives the coincident-current
\(\delta_{t_0}\boxtimes\delta_{t_0}\) obstruction as the local microlocal
reason. Hence a distributional \(B^2_{02,20}\) cannot be asserted without a
named wavefront habitat and the graphwise extension data above.

## Cokernel Obstruction

Let
\[
  e_1=E^2_{\nu_{02}},\qquad
  e_2=E^2_{\nu_{20}},\qquad
  e_3=\mathfrak b^2_{02,20}.
\]
The current Bianchi-exposed finite row complex is
\[
  \mathcal H^0_{\mathrm{cur}}=\mathbb C D^2_{02,20},\qquad
  \mathcal H^1_{\mathrm{cur}}=\mathbb C e_1\oplus\mathbb C e_2\oplus
  \mathbb C e_3,
\]
with
\[
  dD^2_{02,20}=-2e_1+2e_2+e_3.
\]
Thus the image of \(d\) is the line spanned by \((-2,2,1)^T\).

The target for a Bianchi-killing counterterm is \(-e_3=(0,0,-1)^T\). The
functional
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12 e_1^*+e_3^*
\]
annihilates the image:
\[
  \widetilde\lambda_{02,\mathfrak b}(-2,2,1)=0,
\]
but
\[
  \widetilde\lambda_{02,\mathfrak b}(0,0,-1)=-1.
\]
Therefore \(-\mathfrak b^2_{02,20}\notin\operatorname{im}d\) in the
current finite-row habitat.

The same covector detects the lower residual
\[
  r_2=(2,-2,0)^T,\qquad
  \widetilde\lambda_{02,\mathfrak b}(r_2)=1.
\]
Thus \(D^2_{02,20}\) does not kill the transported lower residual unless
the Bianchi row is killed or quotiented.

## Roos Obstruction

Even a fixed-window \(B^2_{02,20}\) would not close the theorem. For a
tower \(B^M\), compatibility requires
\[
  d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N.
\]
Hence the primitive-compatibility class is closed only if the Bianchi rows
transport strictly, or if a supplied correction \(H^{M,N}\) kills the
right-hand side:
\[
  d_{\mathrm{ns},N}H^{M,N}
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N.
\]
Then one must still prove
\[
  [\,\pi_{M,N}B^M-B^N-H^{M,N}\,]=0
  \quad\text{in}\quad
  H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I)).
\]

The current data do not provide the Bianchi-row transport matrices, the
correction \(H^{M,N}\), or the zero Roos class. Diagonal source-face
transport for the eight-face candidate exposes the lower residual
\[
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}},
\]
not a zero lower row. Thus the transport problem is not solved by the
existing companion table.

## Exact Missing Data

A future positive construction must supply the following object, not only
the formal vector \(A_B^2\).

1. A marked finite graph/counterterm habitat
   \(\mathcal G^B_2\) containing the lower Bianchi row and a degree-zero
   local counterterm generator.
2. A local functional
   \[
     B^2_{02,20}\in
     \mathcal O^{\mathrm{bd}}_{\mathrm{loc},\mathcal G^B,2}
     (\mathcal E_w^2|_I;A_{\partial,\hbar}^{\mathrm{pp},w,2}(I)).
   \]
3. A row-coordinate computation proving
   \[
     d_{\mathrm{ns},2}B^2_{02,20}
     =
     -\mathfrak b^2_{02,20}
   \]
   and no extra \(E^2_{\nu_{02}}\) or \(E^2_{\nu_{20}}\) coordinates.
4. A scalar-chain projection on this habitat with
   \[
     \widehat\sigma_{\mathrm{sc},2}(B^2_{02,20})=0.
   \]
5. Regular-density locality or a named finite tuple in
   \(\mathcal D'_{c,\mathrm{WF}}(I;\Gamma,2)\), including the finite-scaling
   extension data and counterterm support.
6. Bianchi-row transport and primitive transport satisfying
   \[
     d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)
     =
     -\pi_{M,N}\mathfrak b^M+\mathfrak b^N,
   \]
   followed by vanishing of the resulting Roos \(H^0\)-class.

Until these are constructed, the strongest true statement is the exact
finite-window obstruction above.

## Verification

Read anchors:

- `CLAUDE.md`
- `AGENTS.md`
- `~/ecosystem/INVARIANTS.md`
- `~/ecosystem/AGENTS-HARNESS.md`
- `.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `reconstitution/theta3-no-counterterm-controlled-enlargement-integration-spec-2026-04-30.md`
- `main.tex:8370-8845`
- `theorem-lanes.tex:3288-3440`
- `appendix-factorization-current-conventions.tex:1-399`
- `appendix-factorization-current-conventions.tex:992-1905`
- `scripts/finite_window_graph_array.py:1-280`
- `scripts/finite_window_graph_array.py:1040-2045`
- `reconstitution/theta3-bianchi-counterterm-construction-push-2026-04-30.md`
- `reconstitution/nonscalar-costello-graph-qme-realization-next-construction-push-2026-04-30.md`

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 - <<'PY'
# focused theta3 primitive, companion, eight-face, and Bianchi matrix check
PY
```

Decisive output:

```text
theta_3_current_finite_row_subcomplex exists= False ell_r= 1 deg0= []
theta3_counterterm_without_differential_entry supplied= True accepted= False dC= 0 missing= ['differential entry dC=-E']
theta3_counterterm_supplied_exact_payload supplied= True accepted= True dC= -1 missing= []
theta3_eight_face_candidate_source_algebraic_obstruction accepted= False residual_zero= False
eight_face_accepted= False
eight_face_coeff_sum= 0
eight_face_n2= [['E_nu02', '2'], ['E_nu20', '-2']]
bianchi_A_D= ['-2', '2', '1']
target_minus_b= ['0', '0', '-1']
ell_A_D= 0
ell_r= 1
ell_target= -1
formal_A_DB_solution= ['-2', '2', '0']
```

## Files Changed

- `reconstitution/theta3-actual-local-functional-b-column-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-294-theta3-actual-local-functional-b-column-construction-push.md`
