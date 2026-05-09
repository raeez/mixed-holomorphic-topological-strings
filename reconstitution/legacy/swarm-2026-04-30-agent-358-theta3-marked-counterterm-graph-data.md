# Agent 358 Theta3 Marked Counterterm Graph Data

Status: report-only. No TeX, script, figure, bibliography, PDF, or build
artifact was edited.

## Question

Specify the marked graph data needed to realize the formal B-column
\[
  B^2_{02,20},\qquad
  d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20},
\]
as an honest Costello local functional. The requested output is not another
existence claim. It is the precise datum whose absence keeps the current
formal column from being a theorem-grade counterterm.

## Verdict

The required object is a connected marked local counterterm graph
\[
  \Gamma_B=\Gamma^2_{B,02,20}
  \in \mathcal G^{B,\mathrm{mk}}_2
\]
whose represented generator
\[
  X_{\Gamma_B,o_B,\mathfrak m_B,2}=B^2_{02,20}
\]
lies in
\[
  \mathcal K^0_{\mathrm{ns},2}(I)
  =\ker \widehat\sigma_{\mathrm{sc},2}
\]
and has marked boundary
\[
  d_{\mathrm{mk}}X_{\Gamma_B,o_B,\mathfrak m_B,2}
  =
  -X_{\mathfrak b,02,20,2}.
\]
In the lower Bianchi-exposed row basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}),
\]
this is exactly the column
\[
  A_B^2=(0,0,-1)^T.
\]

The datum must include the graph type, fields, degree, scalar projection,
regular-density or wavefront admissibility, full boundary-face table, and
finite-window transport. Without these data \(B^2_{02,20}\) is only the
formal free cone generator of Agent 351.

## Sources Read

- `CLAUDE.md`
- `AGENTS.md`
- `~/ecosystem/INVARIANTS.md section IV`
- `~/ecosystem/AGENTS-HARNESS.md section VIII`
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `reconstitution/swarm-2026-04-30-agent-351-theta3-scalar-zero-habitat-construction.md`
- `reconstitution/swarm-2026-04-30-agent-294-theta3-actual-local-functional-b-column-construction-push.md`
- `reconstitution/swarm-2026-04-30-agent-346-theta3-bianchi-counterterm-supremum.md`
- `reconstitution/costello-local-functional-habitat-construction-push-2026-04-30.md`
- `reconstitution/regular-density-wavefront-current-graph-branch-construction-target-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-260-hormander-wavefront-source-fixture.md`
- `main.tex:8616-9118`
- `appendix-unreduced-bv-qme.tex:1623-1728`
- `appendix-unreduced-bv-qme.tex:2077-2245`
- `appendix-unreduced-bv-qme.tex:2501-2642`
- `tate-T1-weighted-completion.tex:2399-2578`
- `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:1-245`

## Fixed Row Target

Set
\[
  e_1=E^2_{\nu_{02}},\qquad
  e_2=E^2_{\nu_{20}},\qquad
  e_3=\mathfrak b^2_{02,20}.
\]
The current lower source-coordinate primitive is
\[
  D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2),
  \qquad
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},
\]
with
\[
  d_{\mathrm{CE}}\zeta^0_2=2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]
It has local-functional differential
\[
  d_{\mathrm{ns},2}D^2_{02,20}=-2e_1+2e_2+e_3.
\]
Thus the current column is
\[
  A_D^2=(-2,2,1)^T,
\]
and the lower residual is
\[
  r_2=(2,-2,0)^T.
\]
The B-column must contribute only
\[
  d_{\mathrm{ns},2}B^2_{02,20}=-e_3,
\]
so that
\[
  A_D^2+A_B^2=(-2,2,0)^T=-r_2.
\]
No \(E^2_{\nu_{02}}\) or \(E^2_{\nu_{20}}\) component is allowed in the
B-column. This is the decisive row-coordinate test.

## Marked Graph Type

The graph must be a connected brane-defect local counterterm graph, not a
CE-source row and not a purely formal row. It is attached to the same
\(\Theta_3\) Hom-valued kernel lane as \(D^2_{02,20}\), but represents the
local counterterm needed to remove the Hom-valued Bianchi defect
\[
  \mathfrak b^2_{02,20}
  =
  d_{\mathrm{ns},2}K^2_{\Theta_3}(\zeta^0_2)
  -
  K^2_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_2).
\]

Data:
\[
  (\Gamma_B,o_B,\mathfrak m_B,\mathsf B_2(\Gamma_B)).
\]
Here \(\Gamma_B\) belongs to a codimension-two closed finite-window marked
Costello list \(\mathcal G^{B,\mathrm{mk}}_2\), \(o_B\) orients the finite
set of boundary operations \(\mathsf B_2(\Gamma_B)\), and
\(\mathfrak m_B\) assigns full-equivariant marker tensors to open index
loops. The graph is supported on the small collision stratum whose boundary
row is \(X_{\mathfrak b,02,20,2}\).

The local counterterm vertex must be one of the allowed finite-window
counterterm vertices
\[
  C^2_{\Gamma_B,w}(\epsilon;B^\Gamma_\bullet),
\]
or its renormalized \(\epsilon\to0\) local extension, with the extension
choice recorded. Naming \(B^2_{02,20}\) without this vertex and extension
does not define a Costello local functional.

## Fields And Labels

The ambient target is the finite-window brane-defect local-functional complex
\[
  \mathfrak Q^\bullet_{\mathcal G^B,2}(I)
  =
  \mathcal O^{\mathrm{bd}}_{\mathrm{loc},\mathcal G^B,2}
  (\mathcal E^2_w|_I;A^{\mathrm{pp},w,2}_{\partial,\hbar}(I)),
  \qquad
  d_2=Q+\{I^w_{0,2},-\}_{\hbar,2}.
\]
The closed fields are the weighted finite-window Hamiltonian BF fields on
\[
  \Omega^\bullet(\mathbb R^2)\widehat\otimes
  \Omega^{0,\bullet}(\mathbb C^2)\widehat\otimes
  (\widehat{\mathfrak h}[1]\oplus
  \widehat{\mathfrak h}^{\vee}_{\mathrm{cont}}[2]),
\]
restricted to the chosen window \(M=2\). The external source labels in the
Bianchi lower lane are the two \(u\)-inputs
\[
  u_{a(t)dt\otimes H_{1,0}},
  \qquad
  u_{b(t)dt\otimes H_{0,1}},
\]
and all source-face outputs forced by
\[
  d_{\mathrm{CE}}\zeta^0_2=2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]
The graph may also use the finite-window interaction \(I^w_{0,2}\), the
finite-scale propagator \(P^{w,2}_{\epsilon,L}\), the regularized BV
contraction \(\Delta^{w,2}_{\epsilon,L}\), and the allowed boundary Weyl
edge. Every vertex and edge label must already be in the finite marked list.

## Degree And Order

The represented counterterm has cochain degree zero:
\[
  B^2_{02,20}\in \mathcal K^0_{\mathrm{ns},2}(I).
\]
Its boundary has degree one:
\[
  \mathfrak b^2_{02,20}\in \mathcal K^1_{\mathrm{ns},2}(I).
\]
The differential \(d_{\mathrm{ns},2}\) has degree \(+1\). The graph belongs
to the \(\theta_3\) order-three lane, but its row degree is the Costello
obstruction-complex degree above: \(H^0\) for counterterms, \(H^1\) for
obstructions.

## Scalar Projection Check

The enlarged marked habitat must carry a filtered chain scalar projection
\[
  \widehat\sigma^B_{\mathrm{sc},2}
  \colon
  \mathfrak Q^\bullet_{\mathcal G^B,2}(I)
  \to
  C^\bullet_{\mathrm{Lie}}(\bar A;\mathbb C\gamma_{\mathbf 1})[1][[\hbar]].
\]
The check is:
\[
  \widehat\sigma^B_{\mathrm{sc},2}(B^2_{02,20})=0,
  \qquad
  \widehat\sigma^B_{\mathrm{sc},2}(\mathfrak b^2_{02,20})=0,
\]
and
\[
  d_{\mathrm{CE}}\widehat\sigma^B_{\mathrm{sc},2}
  -
  \widehat\sigma^B_{\mathrm{sc},2}d_{\mathrm{mk}}
  =0
\]
on every marked face of \(\Gamma_B\).

The clean branch is the full-equivariant supertrace branch: each marker
transport output remains a signed Brauer tensor for \(V=\mathbb C^{N|N}\),
and every cyclic supertrace appearing in the scalar-contact projection is
zero. If the graph is not in that branch, the scalar-contact extension
classes must be computed and killed. An associated-graded scalar symbol is
not enough; without an actual chain projection
\(\mathcal K_{\mathrm{ns},2}\) is not a complex.

## Regular-Density Or Wavefront Condition

One of the following analytic branches must be chosen and recorded.

### Regular-Density Branch

All defect current labels of \(\Gamma_B\) lie in
\[
  \mathcal D^{\mathrm{reg}}_c(I).
\]
The counterterm is a local extension supported on the small diagonal
collision stratum producing \(X_{\mathfrak b,02,20,2}\). Its support is
contained in the collision diagonal meeting the supports of \(a(t)dt\) and
\(b(t)dt\). The graph contraction, counterterm extension, interval
extension, finite-window projection, and weight restriction all remain in
the regular-density local-functional subcomplex.

### Wavefront Branch

The labels lie in a specified graphwise admissible relation
\[
  B^\Gamma_\bullet\in
  \mathcal D'_{c,\mathrm{WF}}(I;\Gamma_B,2).
\]
The required checks are:

- every incidence pullback used to form \(B_{\Gamma_B}\) is
  non-characteristic;
- every product \(K^2_{\Gamma_B,\alpha}B_{\Gamma_B}\) satisfies
  Hormander transversality;
- the product has finite scaling degree along each collision diagonal;
- the chosen local extension across the small diagonal is fixed once and for
  all;
- the extension ambiguity is a finite local counterterm supported on the
  relevant diagonal stratum;
- the final pushforward lands in the allowed brane-defect wavefront class.

This is not a theorem over all compactly supported distributions
\(\mathcal D'_c(I)\). Coincident singular labels require extra
renormalization data or are outside the graph.

## Boundary Faces

The marked boundary table must contain a distinguished Bianchi face
\[
  \beta_{\mathfrak b}\in\mathsf B_2(\Gamma_B)
\]
with
\[
  \partial_{\beta_{\mathfrak b}}\Gamma_B=\Gamma_{\mathfrak b,02,20},
  \qquad
  \varepsilon_{\beta_{\mathfrak b}}=-1,
  \qquad
  \mu_{\beta_{\mathfrak b}}(\mathfrak m_B)=\mathfrak m_{\mathfrak b}.
\]
This row is
\[
  -X_{\mathfrak b,02,20,2}.
\]

All remaining codimension-one faces must be explicit. They are allowed only
from the marked Costello list:

- field differential faces \(Q\ell_v\);
- BV edge-contraction faces and brackets with \(I^w_{0,2}\);
- boundary collision/contact faces;
- counterterm expansion faces;
- the Hom-valued source face \(-\kappa d_{\mathrm{CE}}\), if the graph is
  still used as a Hom-valued kernel before evaluation on fixed CE inputs.

Their signed sum must have zero row projection to \(E^2_{\nu_{02}}\) and
\(E^2_{\nu_{20}}\). Equivalently,
\[
  [d_{\mathrm{mk}}X_{\Gamma_B}]_{E^2_{\nu_{02}}}=0,
  \qquad
  [d_{\mathrm{mk}}X_{\Gamma_B}]_{E^2_{\nu_{20}}}=0,
  \qquad
  [d_{\mathrm{mk}}X_{\Gamma_B}]_{\mathfrak b^2_{02,20}}=-1.
\]
If additional degree-one outputs occur, a companion face table must be
included and must prove their signed sum is zero before projecting to the
three-row Bianchi basis.

Codimension-two closure is mandatory. For every pair
\(\beta_i,\beta_j\in\mathsf B_2(\Gamma_B)\), both composites must be present
in the finite list and must satisfy
\[
  \partial_{\beta_j|\beta_i}\partial_{\beta_i}\Gamma_B
  =
  \partial_{\beta_i|\beta_j}\partial_{\beta_j}\Gamma_B,
\]
\[
  \varepsilon_{\beta_i}\varepsilon_{\beta_j|\beta_i}
  =
  \varepsilon_{\beta_j}\varepsilon_{\beta_i|\beta_j},
  \qquad
  \mu_{\beta_j|\beta_i}\mu_{\beta_i}
  =
  \mu_{\beta_i|\beta_j}\mu_{\beta_j}.
\]
This is the finite graph version of \(d_{\mathrm{mk}}^2=0\). Without it the
new row is not a Costello complex row.

## Contribution To The Matrix

Once the preceding data are supplied, the row-coordinate map sends
\[
  B^2_{02,20}\longmapsto
  0\cdot E^2_{\nu_{02}}
  +0\cdot E^2_{\nu_{20}}
  -1\cdot \mathfrak b^2_{02,20}.
\]
Hence
\[
  A_B^2=(0,0,-1)^T.
\]
The enlarged fixed-window matrix is
\[
  A^2_{D,B}
  =
  \begin{pmatrix}
    -2&0\\
     2&0\\
     1&-1
  \end{pmatrix},
  \qquad
  A^2_{D,B}(1,1)^T=(-2,2,0)^T=-r_2.
\]
The old cokernel functional
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*
\]
evaluates by
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}A_B^2=-1.
\]
Thus the marked graph crosses exactly the obstruction that the current
habitat cannot cross.

## Tower Compatibility

The fixed-window graph is not a tower. For \(M\ge N\), one must also supply
graphs \(\Gamma^M_B\), truncation maps, and primitive transport maps such
that
\[
  d_{\mathrm{ns},M}B^M_{02,20}=-\mathfrak b^M
\]
and
\[
  \Delta^1_{M,N}
  :=
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N
  =
  d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N),
\]
possibly after explicit scalar-zero corrections \(H^{M,N}\). After those
corrections the secondary class
\[
  [\pi_{M,N}B^M-B^N-H^{M,N}]
  \in
  \varprojlim\nolimits^1_N
  H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I))
\]
must vanish. A fixed \(A_B^2\) column without this data solves only the
lower \(N=2\) matrix.

## Acceptance Gate

The marked counterterm graph is accepted only if all checks below pass.

1. \(\Gamma_B\) is a connected marked local counterterm graph in a finite
   codimension-two closed Costello list.
2. \(X_{\Gamma_B,o_B,\mathfrak m_B,2}\) is a genuine local functional in
   \(\mathfrak Q^0_{\mathcal G^B,2}(I)\).
3. \(X_{\Gamma_B,o_B,\mathfrak m_B,2}\in\ker\widehat\sigma^B_{\mathrm{sc},2}\).
4. The scalar projection is a filtered chain map on the enlarged table.
5. The graph is regular-density or graphwise wavefront-admissible.
6. The boundary table gives exactly
   \(d_{\mathrm{mk}}X_{\Gamma_B}=-X_{\mathfrak b,02,20,2}\) in the lower
   Bianchi basis.
7. Codimension-two faces close, including marker transport signs.
8. Finite-window transport kills \(\Delta^1_{M,N}\) and the secondary
   \(\varprojlim^1H^0\) primitive class.

Until these items are supplied, the correct theorem status remains:
formal scalar-zero B-column extension exists; honest Costello local
counterterm graph is not yet constructed.
