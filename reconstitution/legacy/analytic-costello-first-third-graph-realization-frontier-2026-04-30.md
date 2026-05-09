# Analytic Costello First/Third Graph Realization Frontier

Status: obstruction theorem target.  No manuscript or script files were
edited.

## Verdict

The coefficients \(1\) and \(1/24\) are proved for the formal Weyl/Moyal
algebra and for the reduced open-line Wick model with midpoint propagator.
They are not yet proved as coefficients of an actual Costello brane-defect
graph realization.

The proved reduced computation is:
\[
  f*g=m\circ\exp\left({\hbar\over2}P\right)(f\otimes g),
  \qquad
  P=\partial_{z_1}\otimes\partial_{z_2}
    -\partial_{z_2}\otimes\partial_{z_1}.
\]
Hence
\[
  [f,g]_{\rm raw}
  =
  \sum_{\substack{r\ge 1\\r\ {\rm odd}}}
    {2\over 2^r r!}\hbar^r P^r(f,g),
\]
so the first and third raw commutator coefficients are
\[
  \hbar P(f,g),\qquad {\hbar^3\over24}P^3(f,g).
\]
This is a formal product theorem.  A Costello theorem would have to produce
the same product from an elliptic mixed HT bulk-defect BV package, its
finite-scale propagator, its brane restriction, its counterterms, and its QME
row calculus.

## Stage Reports

Stage 1.  Controls loaded.  `CLAUDE.md`, `AGENTS.md`, the attack-heal swarm
protocol, ecosystem voice/rubric rules, the local rectify skill, and the Vol
II rectify harness were read.  Writable paths were restricted to this report
and `reconstitution/swarm-2026-04-30-agent-229-analytic-costello-first-third-graph-realization-frontier.md`.

Stage 2.  The coefficient surface was located.  The relevant manuscript
anchors are `main.tex:7250-7566`, `main.tex:7674-7715`,
`main.tex:8383-8509`, and `main.tex:8521-8771`.  The appendix duplicates the
formal proof and the reduced open-line proof at
`appendix-radial-parts-moyal.tex:39-70` and
`appendix-radial-parts-moyal.tex:1343-1418`.

Stage 3.  Exact arithmetic was rerun.  `python3 scripts/check_moyal_coefficients.py`
passed.  It checked 14641 monomial pairs through order 11, the Capelli
round-trip on 121 monomials, direct \(N=2,3\) radial restrictions, rank-two
radial commutators, scalar anomaly leading terms, and open-line \(r=1,3\)
weights.  The reported odd coefficients were \(1\), \(1/24\), \(1/1920\),
\(1/322560\), \(1/92897280\), and \(1/40874803200\).

Stage 4.  The finite-window QME row surface was attacked.  `python3
scripts/finite_window_graph_array.py` passed its internal checks and printed
the current obstruction data.  The current \(\theta_3\) one-row subcomplex has
\[
  \mathcal Q^0_{\theta_3,M}=0,\qquad
  \mathcal Q^1_{\theta_3,M}=\mathbb C E_{\theta_3,M},\qquad d=0,
\]
with residual \(E_{\theta_3,M}\), obstruction covector
\(\ell_{\theta_3}(E_{\theta_3,M})=1\), and no supplied primitive.  Synthetic
payloads with \(dC=-E\) are accepted by the script as interface fixtures, but
they are explicitly not present in the current data.

Stage 5.  Obstruction target named.  The current theorem surface proves the
Weyl/Moyal target and the reduced open-line Wick realization.  It does not
prove a Costello realization because the actual mixed HT Costello
specialization data below are not supplied.

## Attack

The false promotion is:

> The reduced open-line Wick coefficients \(1\) and \(1/24\) are already the
> Costello brane-defect graph coefficients.

This is false.  The reduced Wick model has already chosen:

- the first-order line action \(S_0=\int_{\mathbb R}\operatorname{Tr}(\phi_1\,d\phi_2)\);
- the zero-mode-removed midpoint propagator
  \(G(t,s)=\frac12\operatorname{sgn}(t-s)\);
- Weyl-ordered boundary vertices;
- no self-contractions;
- only \(r\)-fold cross-contractions between two boundary vertices.

Under these choices, the ordered \(r\)-edge contribution is
\[
  W_r^>(f,g)={1\over r!}\left({\hbar\over2}\right)^r P^r(f,g),
\]
and antisymmetrisation gives \(2/(2^r r!)\) for odd \(r\).  This is the
complete proof of \(1\) and \(1/24\) in the reduced model.  It is not a heat
kernel integral, not a BV Laplacian calculation, not a renormalized Costello
counterterm theorem, and not a QME obstruction calculation.

The manuscript already states the boundary correctly: `main.tex:8511-8518`
says the reduced open-line theorem is not the Costello closed-open graph
theorem; `main.tex:8644-8650` says the third-order diagrams still require
sector specialization, propagator, counterterm, and anomaly checks; and
`main.tex:8720-8771` lists the analytic first/third normalization datum.

## Required Costello Specialization Data

To prove that the Costello graph realization has coefficients \(1\) and
\(1/24\), one must supply all of the following data in the local
\(\mathbb R^2_{\rm top}\times\mathbb C^2_{\rm hol}\) mixed HT model.

### 1. Parent elliptic mixed HT BV sector

One must construct either an elliptic closed-open parent theory or a precise
dimensional reduction whose restriction is the Hamiltonian BF sector
\[
  \Omega^\bullet(\mathbb R^2)\widehat\otimes
  \Omega^{0,\bullet}(\mathbb C^2)\widehat\otimes
  (\widehat{\mathfrak h}[1]\oplus
   \widehat{\mathfrak h}^{\vee}_{\rm cont}[2]).
\]
The construction must fix the field topology, degree \(-1\) BV pairing,
differential, local interaction, bracket degree, and a homotopy retract closed
under the propagator and RG flow.

The unweighted product/direct-sum Tate topology does not suffice:
`main.tex:7343-7400` proves that the formal coefficient Casimir does not
converge there.  A weighted Tate coefficient category, or a smaller declared
sector, is mandatory before the BV propagator exists as a kernel.

### 2. Propagator and measure

The Costello data must include a finite-scale gauge fixing, heat kernel, and
propagator
\[
  P_{\epsilon,L}^w=\int_\epsilon^L Q^{\rm GF}K_t^w\,dt
\]
with the weighted coefficient coevaluation inserted.  It must be a genuine
distributional BV kernel, not merely the operator-level homotopy
\[
  [Q,P_{\epsilon,L}]=K_\epsilon-K_L.
\]
The brane restriction of this propagator must be computed as a
configuration-space kernel with orientations, compactification faces, Koszul
signs, and measure normalization.  On degree-zero Hamiltonian boundary
observables it must induce
\[
  P_{\partial,L}\leadsto {1\over2}P
\]
after zero-mode removal and the chosen infrared/harmonic projection.  This is
the exact normalization defect
\[
  \mathfrak n_1
  :=
  P_{\partial,L}\big|_{\rm Ham^0}-{1\over2}P .
\]
The first coefficient \(1\) is proved in Costello's model only after
\(\mathfrak n_1=0\) in the boundary observable product.

Costello's general source supplies the heat-kernel/RG vocabulary, not this
specialization.  The local source mirror records the heat kernel at
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1549-1563`,
the propagator identity at `:2121-2138`, and QME/RG compatibility at
`:2139-2190`.

### 3. Brane-defect kernel

One must construct a continuous curved bulk-to-defect cochain
\[
  \kappa_{\hbar,w,I}\colon
  C^\bullet_{\rm CE,cont}(\mathfrak g^{w,{\rm cur}}_{\hbar,I})
  \longrightarrow
  \mathfrak Q^\bullet_{w,\partial,\hbar}(I),
\]
where the source is either regular-density restricted or includes a
wavefront/counterterm rule for
\[
  \mathcal D'_c(I)\widehat\otimes
  \mathfrak h^{\vee,w}_{\hbar,\rm cont}.
\]
The zero-edge values must be
\[
  u_{a(t)dt\otimes f}\mapsto B_f^{w,M}(a),\qquad
  c_{B,\rho}\mapsto \Theta_\rho^{w,M}(B),
\]
and the positive-edge values must be actual renormalized graph weights
\[
  K^M_\Gamma=W^{R,M}_{\Gamma,L,w}(B^\Gamma_\bullet).
\]
The cotangent summand must use the Moyal coadjoint action on the
principal-part current module, not the polynomial one-\(\psi\) PBW shadow.

### 4. Counterterms

For every divergent bulk, defect, collision, or source-face graph one must
choose local counterterms
\[
  C_{\Gamma,w}^{w_0}(\epsilon)\in
  \mathcal O_{\rm loc}(\mathcal E_w^{w_0})
\]
with
\[
  \pi_{w'_0w_0}C_{\Gamma,w}^{w'_0}=C_{\Gamma,w}^{w_0},
  \qquad
  R^{w_0}_{w,w'}C_{\Gamma,w}^{w_0}=C_{\Gamma,w'}^{w_0}.
\]
They must be supported on the relevant bulk diagonal or brane-collision
stratum, and RG flow must keep them inside the same local-functional
subcomplex.  If a finite counterterm changes the \(P\) or \(P^3\) coefficient,
the remaining normalization freedom is fixed exactly by matching \(1\) and
\(1/24\).

Costello's source mirror supplies the abstract counterterm theorem at
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1746-1807`.
It does not supply these mixed Hamiltonian brane-defect counterterms.

### 5. Scalar anomaly and scalar-contact lift

In the ordinary scalar-reduced \(\mathfrak{gl}_N\) branch, the Capelli contact
term is
\[
  \operatorname{Tr}(A\,XY)-\operatorname{Tr}(A\,YX)
  =\hbar N\operatorname{Tr}(A)
  \quad \bmod\ \mathcal W_N\widehat\mu(\mathfrak{sl}_N),
\]
and the scalar-symbol class is
\[
  \hbar N[\bar c]\in H^2_{\rm Lie}(\bar A;\mathbb C)[[\hbar]].
\]
This class must be removed by a proved mechanism before the non-scalar
Costello row complex is formed.  The current proved mechanisms are the
central-character source replacement and the balanced supertrace branch; any
ordinary closed-exchange repair must supply a leading class
\(-\hbar N[\bar c]\) and a local-functional null-homotopy.

After the scalar symbol is handled, one still needs a complete
\(d_{\rm QME}\)-stable scalar-contact filtration and a filtered chain map
\[
  \widehat\sigma_{\rm sc,M}\colon
  \mathfrak Q^\bullet_{\mathcal G,M}(I)
  \to C^\bullet_{\rm Lie}(\bar A;\mathbb C\gamma_{\mathbf 1})[1][[\hbar]].
\]
The associated graded scalar symbol is not enough.  The successive Hom
classes \(o_{\sigma,w}^{(r)}(I)\) must vanish before
\(\ker\widehat\sigma_{\rm sc}\) is a legitimate non-scalar QME complex.

### 6. QME rows and obstruction classes

For each finite window the graph list must be a codimension-two closed marked
Costello list \(\mathcal G_M^{\rm mk}\).  Every field-differential, BV-edge,
collision/contact, counterterm, and CE-source face must carry its output
graph, coefficient, marker transport, incidence sign, and lower-window
truncation.  The row formulas are
\[
  R^{\rm row}_{d\Gamma,M}
  =\varepsilon_\Gamma d_MK^M_\Gamma,
\]
\[
  R^{\rm row}_{{\rm CE}(\Gamma,\nu),M}
  =
  -\varepsilon^{\rm CE}_{\Gamma,\nu}K^M_\Gamma(\zeta_{M,\nu}),
\]
\[
  R^{\rm row}_{b(\Gamma_1,\Gamma_2),M}
  =
  {1\over2}\varepsilon_{\Gamma_1,\Gamma_2}
  \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar,M},
\]
plus lower-counterterm contributions.  After scalar projection vanishes, the
non-scalar residual defines
\[
  [\operatorname{Ob}^{\rm red}_{w,\partial,\hbar}]
  \in H^1(\ker\widehat\sigma_{\rm sc},d_{\rm QME}).
\]
At finite windows, counterterms close order \(n\) exactly when
\[
  \mathfrak O_n^{\rm ns}
  =
  \bigl(([\mathfrak o^{\rm ns}_{n,M}])_M,\lambda_n\bigr)
\]
vanishes, where \(\lambda_n\) is the Roos primitive-compatibility class.

The first certified order-three row obstruction in the current row array is
\[
  \mathfrak O_{\theta_3,M}
  =
  [E_{\theta_3,M}],
  \qquad
  \ell_{\theta_3}(E_{\theta_3,M})=1.
\]
It is killed only by one of:

- a CE ancestor \(\eta_{\theta_3,M}\) with
  \(d_{\rm CE}\eta_{\theta_3,M}=\zeta_{M,\nu_3}\) and
  \(d_MK^M_{\Theta_3}(\eta_{\theta_3,M})=-E_{\theta_3,M}\);
- a local counterterm \(C^{\rm ct}_{\theta_3,M}\) with
  \(d_MC^{\rm ct}_{\theta_3,M}=-E_{\theta_3,M}\), scalar projection zero,
  and finite-window transport;
- a complete companion-face table whose signed source-face residual is zero
  and whose \(v^{M,N}\)-transport preserves that zero sum.

A name \(C_{\theta_3}\) without \(dC=-E\), scalar-zero value, and tower
compatibility is not a counterterm.

### 7. Graph normalization

The observable product and the connected effective action must not be
identified.  Costello's connected effective action carries the graph power
\(\hbar^{b_1(\Gamma)+\sum_v g_v}\) in `main.tex:7260-7277`.  The Moyal
observable product counts boundary cross-contractions.  A Costello
realization must prove that the brane-defect observable product restricts to
this edge-counting convention on degree-zero Hamiltonians.

For the first graph one must identify the one-propagator ribbon graph with
tensor contraction \(P(f,g)\), trivial edge automorphism, ordered weight
\(\hbar P/2\), and antisymmetrized weight \(\hbar P\).

For the third graph one must identify the three-propagator graphs with tensor
contraction \(P^3(f,g)\), ordered aggregate weight
\[
  {1\over 3!}\left({\hbar\over2}\right)^3P^3(f,g)
  =
  {\hbar^3\over48}P^3(f,g),
\]
and antisymmetrized weight
\[
  {\hbar^3\over24}P^3(f,g).
\]
If the orientation classes are expanded, their residual symmetry factors are
\(S_a\times S_{3-a}\), and the binomial factor satisfies
\[
  {\binom 3a\over 3!}={1\over a!(3-a)!}.
\]
The aggregate \(S_3\) denominator and the residual orientation-class
denominator must not both be applied.

The third-order Costello normalization defect is therefore
\[
  \mathfrak n_3
  :=
  \left[
    {\rm ObsProd}^{(3)}_{\rm Costello}(f,g)
    -{\hbar^3\over24}P^3(f,g)
  \right]_{\rm Ham^0,conn,red},
\]
where the quotient is taken only after subtracting declared local
counterterms, killing scalar-contact terms, and projecting to connected
single-trace or primitive trace classes.  A Costello proof of \(1/24\) is the
vanishing of \(\mathfrak n_3\), together with the proof that all other
order-\(\hbar^3\) connected local terms vanish, are counterterm-exact, or lie
in the discarded scalar trace.

## Obstruction Theorem Target

The current data prove the following obstruction theorem target.

Let \(\mathcal D_{\rm Cost}^{1,3}\) denote the full specialization datum
consisting of:

- the elliptic mixed HT parent or dimensional reduction;
- the weighted coefficient Casimir and BV propagator;
- the brane-restricted boundary kernel and measure normalization;
- the continuous bulk-to-defect kernel \(\kappa_{\hbar,w,I}\);
- scalar-contact chain projection \(\widehat\sigma_{\rm sc}\);
- local counterterms with RG, support, and finite-window compatibility;
- marked Costello row tables with \(d\), CE-source, bracket, collision, and
  counterterm faces;
- connected trace extraction and principal-part current compatibility;
- normalization equations \(\mathfrak n_1=0\) and \(\mathfrak n_3=0\).

Then the first/third Costello realization theorem is equivalent to the
vanishing of
\[
  \mathfrak O_{\rm Cost}^{1,3}
  =
  \bigl(
    \mathfrak o_{\rm Cas},
    \hbar N[\bar c]\ {\rm or}\ o_{\sigma,w}^{(r)},
    [\operatorname{Ob}^{\rm red}_{w,\partial,\hbar}],
    \mathfrak O_{\theta_3},
    \mathfrak n_1,
    \mathfrak n_3
  \bigr)
\]
in the corresponding weighted finite-window inverse system.

In the present repository state, \(\mathfrak n_1\) and \(\mathfrak n_3\) are
defined only for the reduced open-line Wick model, where they vanish by
construction.  They are not defined as Costello defects until
\(\mathcal D_{\rm Cost}^{1,3}\) is supplied.  The ordinary \(\mathfrak{gl}_N\)
scalar branch has the nonzero class \(\hbar N[\bar c]\), and the current
\(\theta_3\) one-row package has the nonzero finite-row class
\([E_{\theta_3,M}]\).  Thus the actual Costello first/third graph theorem is
blocked by a named construction problem, not by an ambiguity in the formal
Moyal coefficients.

## Local Anchors

- Formal Moyal product and monomial coefficients: `main.tex:7674-7731`.
- Degree-zero target separated from Costello realization:
  `main.tex:7733-7741`.
- Hamiltonian Costello specialization datum:
  `main.tex:7402-7566`.
- Reduced open-line midpoint product:
  `main.tex:8383-8442`.
- Reduced open-line Wick theorem:
  `main.tex:8444-8509`.
- First/third Costello normalization target:
  `main.tex:8521-8771`.
- Componentwise quantum coefficient surface, not full graph realization:
  `main.tex:7845-8019`.
- Non-scalar QME obstruction complex:
  `main.tex:8021-8230`.
- Theta3 finite-window acceptance gate:
  `main.tex:8232-8346`.
- Appendix exact formal coefficients:
  `appendix-radial-parts-moyal.tex:39-70`.
- Appendix reduced open-line graph expansion:
  `appendix-radial-parts-moyal.tex:1343-1418`.
- Appendix realization boundary:
  `appendix-radial-parts-moyal.tex:1510-1588`.
- Open obligations finite-window rows:
  `open-obligations.tex:342-630`.

## Verification

Commands run:

```bash
python3 scripts/check_moyal_coefficients.py
python3 scripts/finite_window_graph_array.py
rg -n "Moyal|first-order|third-order|1/24|Costello|graph|Wick|QME|anomaly|counterterm|propagator|finite-window|theta" main.tex appendix-radial-parts-moyal.tex open-obligations.tex scripts/*.py
nl -ba main.tex | sed -n '7200,8778p'
nl -ba appendix-radial-parts-moyal.tex | sed -n '1,220p'
nl -ba appendix-radial-parts-moyal.tex | sed -n '1330,1635p'
nl -ba open-obligations.tex | sed -n '205,640p'
```

No `make pdf` was run.  This was a report-only task under concurrent
manuscript editing.
