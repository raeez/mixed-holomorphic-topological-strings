# Strict Endpoint / Casimir Kernel Construction Target -- 2026-04-30

Status: construction target plus obstruction theorem. The positive object is
not the raw product/direct-sum endpoint. It is a coefficient habitat in which
the diagonal coevaluation exists as a tensor, the Hamiltonian bracket is
continuous, and the bar-cobar comparison has exact inverse-limit and
conilpotence input. The raw strict endpoint fails by the nonzero obstruction
\(o_{\mathrm{Cas}}\).

## Anchors

- `main.tex:330-351`: finite coordinate tests do not transport finite
  cotangent CE/PV by pretending Taylor cutoffs are Lie quotients.
- `main.tex:2176-2258`: coordinate CE/PV theorem, bracket/kernel
  admissibility, and bar-cobar obstruction tuple.
- `main.tex:5208-5460`: admissible Koszul duality and lower-central
  Tate-pronilpotence criterion.
- `main.tex:7363-7400`: coefficient coevaluation kernel obstruction for the
  raw Tate pair.
- `theorem-lanes.tex:1204-1270`: bracket- and kernel-admissible realizations.
- `theorem-lanes.tex:1351-1486`: coordinate formal-disk CE/PV theorem and
  admissible \(P_0\) realizations.
- `theorem-lanes.tex:1785-1811`: strict product/direct-sum Casimir
  obstruction.
- `tate-T1-weighted-completion.tex:31-64`: strict Tate Casimir diagnosis.
- `tate-T1-weighted-completion.tex:188-263`: weighted coefficient pair and
  convergent Casimir.
- `tate-T1-weighted-completion.tex:279-347`: finite-scale heat-kernel
  propagator after the coefficient kernel exists.
- `tate-T1-weighted-completion.tex:2785-3017`: strict unweighted endpoint
  no-go, endpoint-admissible modules, and \(q\to1^+\) finite-window
  stabilization.
- `tate-T3-quillen-equivalence.tex:48-130`: strict finite-window
  Mittag-Leffler Tate habitat and kernel existence from compatible finite
  Casimirs.
- `tate-T3-quillen-equivalence.tex:204-285`: closed-window bracket,
  coadjoint, and Casimir obstruction terms.
- `tate-T3-quillen-equivalence.tex:368-523`: open-side filtered-cobar
  obstruction complex and admissibility criterion.
- `tate-T3-quillen-equivalence.tex:1160-1178`: no universal strict
  product/direct-sum kernel habitat.
- `open-obligations.tex:33-100`: coordinate CE/PV admissibility and the
  Casimir transition term.
- `open-obligations.tex:237-254`: endpoint obstruction tuple.

## Stable Core

Let
\[
  H_d=\operatorname{Span}\{z_1^az_2^b:a+b=d\},\qquad
  \mathfrak h_\Pi=\prod_{d\geq1}H_d,\qquad
  D_\oplus=\bigoplus_{d\geq1}H_d^\vee .
\]
The strict pair \((\mathfrak h_\Pi,D_\oplus)\) is the raw
product/direct-sum Tate endpoint. It has the abstract evaluation
\(D_\oplus\otimes \mathfrak h_\Pi\to \mathbb C\). It does not have the
coevaluation tensor
\[
  C_{\mathfrak h}=\sum_{d\geq1}\sum_i e_{d,i}\otimes e^i_d
\]
as an element of
\(\mathfrak h_\Pi\widehat\otimes D_\oplus\), or of the reversed tensor
product. Every tensor with a \(D_\oplus\)-factor has finite support in the
dual degree direction. \(C_{\mathfrak h}\) has nonzero support in every
degree.

The coordinate CE/PV theorem is proved before this obstruction appears.
The generator map
\[
  c^I\mapsto\theta^I,\qquad u_I\mapsto O_I
\]
is a completed coordinate dg-algebra theorem. It becomes a \(P_0\)-theorem
only inside a bracket-admissible complete Hausdorff subalgebra \(B\). It
becomes a kernel theorem only after a kernel-admissible convolution dg Lie
algebra \(\mathcal K_B\) is supplied and the diagonal sums converge there.

The weighted Mittag-Leffler habitat supplies the positive construction. For
a degree weight \(w(d)\), put
\[
  \mathfrak h_w=\varprojlim_M\prod_{1\leq d\leq M} w(d)H_d,\qquad
  D_w=\mathfrak h^{\vee,w}_{\mathrm{cont}}
       =\varprojlim_M\prod_{1\leq d\leq M} w(d)^{-1}H_d^\vee .
\]
Then
\[
  C_{\mathfrak h,w}
  =
  \sum_{d\geq1}\sum_i
  (w(d)e_{d,i})\otimes(w(d)^{-1}e^i_d)
  \in \mathfrak h_w\widehat\otimes D_w
\]
is the coefficient coevaluation. The second factor is a product module, not
the strict continuous dual of the first product space. This is a changed
coefficient category.

The finite-scale endpoint propagator in such a habitat is
\[
  P_{\epsilon,L}^{w}
  =
  P_{\epsilon,L}^{\mathrm{base}}\widehat\otimes
  C_{\mathfrak h\oplus\mathfrak h^\vee[1],w},
\]
with
\[
  [Q,P_{\epsilon,L}^{w}]=K_\epsilon^w-K_L^w .
\]
The spacetime heat-kernel part is Costello's bulk elliptic datum; the
coefficient part is the algebraic Casimir. The graphwise RG/QME step is a
separate locality and counterterm problem.

## Attack Ledger

### A233-01: finite windows do not give a strict endpoint kernel

Claim attacked: compatible finite Casimirs imply a tensor in
\(\mathfrak h_\Pi\widehat\otimes D_\oplus\).

Failure: compatibility under finite truncation is weaker than representability
by a strict tensor. The family \(C_{\le M}\) is compatible, but its support is
infinite in \(D_\oplus\).

Heal: record \(o_{\mathrm{Cas}}\) as the cokernel class of this compatible
family.

### A233-02: abstract evaluation is not coefficient coevaluation

Claim attacked: the BV pairing alone supplies Costello's coefficient kernel.

Failure: evaluation \(D_\oplus\otimes\mathfrak h_\Pi\to\mathbb C\) is a
continuous bilinear form. Costello's propagator needs the inverse pairing as
a kernel in a completed tensor product.

Heal: require a coefficient coevaluation tensor \(C_\ast\) projecting to all
finite Casimirs. The weighted habitat supplies it; the strict pair does not.

### A233-03: ambient product coordinate algebras do not carry the global
contraction bracket

Claim attacked: the coordinate product CE/PV is already a completed
\(P_0\)-algebra.

Failure: in the ambient product, contractions such as
\(\{\sum_I c^I,\sum_I u_I\}\) require the divergent diagonal
\(\sum_I1\). The coordinate theorem remains a dg commutative theorem until a
bracket-admissible \(B\) is specified.

Heal: keep \(P_0\) assertions inside bracket-admissible \(B\)'s with
continuous multiplication, \(d_\pi\), and Schouten contraction.

### A233-04: endpoint propagator fails exactly where the coefficient kernel
fails

Claim attacked: the strict pair has a Costello propagator because it has an
operator-level heat homotopy.

Failure: the operator homotopy
\(\int_\epsilon^LQ^{\mathrm{GF}}K_t^{\mathrm{base}}dt\) exists on the
spacetime factor, but the full BV propagator is
\(P_{\epsilon,L}^{\mathrm{base}}\widehat\otimes K\). No such \(K\) exists in
the strict pair.

Heal: endpoint propagator data must include the coevaluation kernel, not only
the heat operator.

### A233-05: bar-cobar is an admissible-envelope theorem, not a raw strict
endpoint consequence

Claim attacked: CE/PV cochains automatically promote to enveloping/Koszul
duality for the full formal disk.

Failure: the bar-cobar comparison also needs lower-central
Tate-pronilpotence, conilpotent CE coalgebras in the completed sense,
strongly convergent filtered cobar maps, exact continuous duality, and
zero Milnor defects. Linear translations, the \(H_2\cong\mathfrak{sl}_2\)
sector, the associated-graded cone, and \(\varprojlim^1\) defects are
separate obstruction terms.

Heal: use the strict finite-window ML habitat, nilpotent truncations, or
weighted admissible envelopes. Do not use the raw pair as a universal
endpoint.

### A233-06: \(q\to1^+\) is finite-window stabilization, not strict
ordinary convergence

Claim attacked: regulator independence among weights identifies the weighted
product with \(D_\oplus\).

Failure: \(D_\oplus\hookrightarrow D_{\Pi,w}\) is a filtered finite-window
weak equivalence but not an ordinary quasi-isomorphism with zero
differential. The quotient \(D_{\Pi,w}/D_\oplus\) has nonzero \(H^0\).

Heal: state \(q\to1^+\) only as finite-window stabilization unless an
endpoint-admissible coefficient module satisfying (E1)--(E5) is constructed.

## Positive Theorem Target

Definition. A Casimir-admissible endpoint habitat for the Hamiltonian disk is
a tuple
\[
  \mathcal H_\ast
  =
  (\mathfrak h_\ast,D_\ast,
   \{(\mathfrak h_{\ast,\le M},D_{\ast,\le M})\}_M,
   C_\ast,\Phi_\ast,B_\ast,\mathcal K_\ast,R_\ast)
\]
with the following data.

1. Strict Mittag-Leffler finite windows:
\((\mathfrak h_{\ast,\le M},D_{\ast,\le M})\) are finite-dimensional
paired coefficient windows with surjective transition maps, complete
Hausdorff inverse limit \((\mathfrak h_\ast,D_\ast)\), and exact
\(\varprojlim\).

2. Coefficient coevaluation:
\[
  C_\ast\in\mathfrak h_\ast\widehat\otimes D_\ast,\qquad
  \pi_M(C_\ast)=C_{\le M}
\]
for every \(M\).

3. Continuous Hamiltonian operations: the bracket, coadjoint action,
coordinate CE differential, Schouten differential, multiplication, and
contraction bracket are continuous on the chosen bracket-admissible
realization \(B_\ast\).

4. Kernel realization: the diagonal element
\[
  \Theta_\ast=\sum_IH_I\otimes\theta^I+\sum_I\eta^I\otimes O_I
\]
converges in a specified convolution dg Lie algebra \(\mathcal K_\ast\) and
satisfies
\[
  d\Theta_\ast+\frac12[\Theta_\ast,\Theta_\ast]=0 .
\]

5. Endpoint propagator:
\[
  P_{\epsilon,L}^{\ast}
  =
  P_{\epsilon,L}^{\mathrm{base}}\widehat\otimes C_\ast
\]
is a continuous finite-scale BV propagator satisfying the BV heat-kernel
identity and compatible with the endpoint finite-window tower.

6. Bar-cobar compatibility: the CE coalgebra, completed cobar algebra, and
completed enveloping algebra lie in an admissible Tate model envelope with
lower-central Tate-pronilpotence, conilpotence, exact continuous duality,
strong convergence, zero associated-graded cone obstruction, and zero Milnor
\(\varprojlim^1\) defects.

7. RG/QME acceptance: if quantum graph claims are asserted, Costello RG
recursion preserves the habitat and the mixed brane-defect QME obstruction
class vanishes in the specified local-functional complex. This is not forced
by the Casimir alone.

Theorem target. If \(\mathcal H_\ast\) is Casimir-admissible, then the
coordinate CE/PV map promotes to a completed dg \(P_0\)-isomorphism on
\(B_\ast\), the diagonal \(\Theta_\ast\) is a Maurer-Cartan kernel in
\(\mathcal K_\ast\), \(P_{\epsilon,L}^{\ast}\) is the endpoint BV propagator,
and the closed bar-cobar/enveloping comparison holds in the admissible
envelope. For \(w_q(d)=q^d\), any endpoint satisfying the same conditions
receives the finite-window stabilized \(q\to1^+\) representative.

Proof route. Conditions (1)--(2) give strict ML exactness and the coefficient
kernel. Conditions (3)--(4) let the generator-level CE/PV calculation extend
from finite words to the completed \(P_0\) and convolution brackets. Condition
(5) tensors Costello's base propagator with the coefficient coevaluation.
Condition (6) is the bar-cobar theorem's actual hypothesis. Condition (7) is
the quantum graph acceptance gate.

## Exact Obstruction \(o_{\mathrm{Cas}}\)

Let
\[
  H_{\le M}=\bigoplus_{1\le d\le M}H_d,\qquad
  D_{\le M}=H_{\le M}^\vee,\qquad
  C_{\le M}=\sum_{1\le d\le M}\sum_i e_{d,i}\otimes e^i_d .
\]
Set
\[
  \mathcal C_{\mathrm{fin}}
  =
  \varprojlim_M(H_{\le M}\otimes D_{\le M})
\]
and let
\[
  \gamma\colon
  \mathfrak h_\Pi\widehat\otimes D_\oplus
  \longrightarrow
  \mathcal C_{\mathrm{fin}}
\]
be finite-window projection. Define
\[
  Q_{\mathrm{Cas}}
  =
  \mathcal C_{\mathrm{fin}}/
  \operatorname{im}\gamma,\qquad
  o_{\mathrm{Cas}}
  =
  [(C_{\le M})_{M\ge1}]\in Q_{\mathrm{Cas}} .
\]
Define the reversed obstruction \(o_{\mathrm{Cas}}^{\mathrm{op}}\) by the
same formula with tensor factors reversed.

Obstruction theorem. For the strict product/direct-sum endpoint,
\[
  o_{\mathrm{Cas}}\neq0,\qquad
  o_{\mathrm{Cas}}^{\mathrm{op}}\neq0 .
\]
Indeed, any tensor in
\(\mathfrak h_\Pi\widehat\otimes D_\oplus\) has finite support in the
\(D_\oplus\)-degree. Thus there is \(M_0\) such that all
\((H_d^\vee)_{d>M_0}\)-components vanish. Its image in the window
\(M_0+1\) has zero \(H_{M_0+1}\otimes H_{M_0+1}^\vee\) component, while
\(C_{\le M_0+1}\) has the identity tensor there. Hence the compatible
finite Casimir family is not in \(\operatorname{im}\gamma\).

Equivalence. A strict endpoint coefficient kernel exists if and only if
\(o_{\mathrm{Cas}}=0\) and \(o_{\mathrm{Cas}}^{\mathrm{op}}=0\), before the
independent bracket, bar-cobar, and QME obstructions are evaluated. Since
these classes are nonzero for \((\mathfrak h_\Pi,D_\oplus)\), the raw strict
endpoint cannot carry the coefficient coevaluation, endpoint propagator, or
kernel-admissible CE/PV diagonal.

## Inscription Boundary

The next theorem should not say that the weighted category proves the raw
strict endpoint. It should say:

1. the weighted/ML habitat proves the positive kernel and propagator data;
2. finite-window \(q\to1^+\) stabilization is theorem-grade inside
   endpoint-admissible habitats;
3. the raw product/direct-sum pair fails exactly by \(o_{\mathrm{Cas}}\);
4. bar-cobar and graph/QME claims remain behind their own admissibility and
   obstruction gates.

No compact Calabi-Yau, curve VOA, CoHA, Igusa/BKM, or global BCOV evidence is
needed for this surface.
