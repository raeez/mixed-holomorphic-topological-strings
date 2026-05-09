# Agent 236 Report: Equivariant CE/PV Refined-Bracket Completion

Worktree: `/Users/raeez/topological-strings`

Owned paths:

- `reconstitution/equivariant-ce-pv-refined-bracket-completion-construction-target-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-236-equivariant-ce-pv-refined-bracket-completion-construction-target.md`

## Claim Attacked

The current theorem surface could be overread as a global
\(T_\Omega\)-equivariant \(P_0\) CE/PV/factorization theorem because the
coordinate formula has already been repaired by Agent 189.

That overread is false.  The repaired coordinate formula gives
\[
  \Phi_\Omega(c^I)=\theta^I,\qquad
  \Phi_\Omega(u_I)=O_I,
\]
with
\[
  d_{\mathrm{CE},\Omega}c^K
  =
  -\frac12\hbar_\omega C^K_{IJ}c^Ic^J,\qquad
  d_{\mathrm{CE},\Omega}u_K
  =
  \hbar_\omega C^L_{KJ}u_Lc^J,
\]
and
\[
  \pi_\Omega=\frac12\hbar_\omega C^K_{IJ}O_K\theta^I\theta^J.
\]
It does not by itself construct a completed bracket, diagonal kernel, basic
Cartan complex, factorization descent map, normalization comparison, or QME
solution.

## Stable Core

Stable core remains the \(\hbar_\omega\)-weighted coordinate dg CE/PV theorem
on finite coordinate tests and on any already supplied bracket-admissible
weighted completion.  It uses:

\[
  [f,g]_\Omega=\hbar_\omega\{f,g\},
  \qquad w(\hbar_\omega)=\epsilon_1+\epsilon_2,
\]
\[
  w(c^{a,b})=w(\theta^{a,b})=-a\epsilon_1-b\epsilon_2,
  \qquad
  w(u_{a,b})=w(O_{a,b})=a\epsilon_1+b\epsilon_2.
\]

The completion theorem target is written in
`reconstitution/equivariant-ce-pv-refined-bracket-completion-construction-target-2026-04-30.md`.

## Healed Construction Target

The strongest admissible theorem is:

Given finite normal/Hamiltonian windows \((N,M)\), coefficient rings
\[
  R_\Omega^{N,M}
  =
  \mathbb C[\epsilon_s,\epsilon_1,\epsilon_2,\hbar_\omega]
  [\chi^{-1}\mid\chi\in\mathsf X_{N,M}],
\]
an admissible degree weight \(w(d)=q^d\), \(q>1\), a basic Cartan model
for
\[
  Q_\Omega=Q+\iota_{V_\Omega},\qquad Q_\Omega^2=L_{V_\Omega},
\]
a bracket-admissible \(B_{\Omega,w}\), a kernel-admissible convolution target
\(\mathcal K_{\Omega,w,B}\), and Weiss descent data, the map
\[
  \Phi_{\Omega,w}^{\mathrm{fact}}\colon
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  (\mathfrak g^{\mathrm{mix}}_{U,B,\Omega,w})
  \to
  \mathrm{PV}_{\Omega,w}(U\times B)
\]
is an isomorphism of completed \(T_\Omega\)-basic dg \(P_0\)
prefactorization objects, and the induced map on global factorization
sections is a quasi-isomorphism precisely when the Roos/Weiss obstruction
classes vanish.

Here
\[
  \mathfrak g^{\mathrm{mix}}_{U,B,\Omega,w}
  =
  \Omega^\bullet_c(U)\widehat\otimes
  \Omega^{0,\bullet}_c(B)\widehat\otimes
  (\mathfrak h_{\Omega,w}\ltimes D_{\Omega,w}[1]).
\]

## Attack Ledger

```yaml
- id: A1-236-01
  severity: 1
  status: valid
  lens: global-completion overclaim
  target: theorem-lanes.tex:1489-1658
  claim: The equivariant CE/PV coordinate formula is already a global completed P0 theorem.
  broken_step: The statement itself records that mixed Cartan complex, bracket-admissible global completion, diagonal kernel convergence, normalization, QME, and physical trace state are not constructed.
  evidence_type: line_reference
  evidence_ref: theorem-lanes.tex:1638-1657; theorem-lanes.tex:1180-1271
  confidence: high
  blast_radius: false P0/factorization/global-section theorem
  minimal_heal: State the weighted basic-Cartan prefactorization theorem target with explicit B_{Omega,w}, K_{Omega,w,B}, descent, and Roos data.
  residual: Ob^{glob}_{Omega,CE/PV}

- id: A1-236-02
  severity: 1
  status: valid
  lens: Cartan curvature
  target: local-dictionary.tex:433-443
  claim: Q_Omega is an ordinary differential before invariants.
  broken_step: Q_Omega^2=L_{V_Omega}; only the invariant/basic subcomplex is an ordinary dg complex.
  evidence_type: line_reference
  evidence_ref: local-dictionary.tex:433-443; theorem-lanes.tex:2679-2695
  confidence: high
  blast_radius: every CE/PV and factorization differential can be curved
  minimal_heal: Use D_CE,Omega=Q_Omega+d_CE,Omega and D_PV,Omega=Q_Omega+d_pi,Omega as curved Cartan differentials, then restrict to basic objects or retain curvature.
  residual: ob_{Omega,Cartan}=[L_{V_Omega}] unless basic contraction data are supplied

- id: A1-236-03
  severity: 1
  status: valid
  lens: topology and diagonal kernel
  target: theorem-lanes.tex:1440-1474; tate-T1-weighted-completion.tex:33-64
  claim: The strict product/direct-sum endpoint carries the global contraction bracket and Casimir kernel.
  broken_step: The contraction of infinite coordinate sums gives a divergent diagonal; the strict Casimir has a nonzero covector component in every degree and is not in the strict product/direct-sum tensor product.
  evidence_type: obstruction
  evidence_ref: theorem-lanes.tex:1452-1457; tate-T1-weighted-completion.tex:33-64; tate-T1-weighted-completion.tex:2785-3000
  confidence: high
  blast_radius: false Costello kernel, false MC tensor, false global P0 bracket
  minimal_heal: Change category to the weighted Mittag-Leffler pair h_w, h^{vee,w}_{cont}; require B_{Omega,w} and K_{Omega,w,B}.
  residual: ob_{Omega,top}, ob_{Omega,br}, ob_{Omega,diag}

- id: A1-236-04
  severity: 2
  status: valid
  lens: resonance and localization
  target: local-dictionary.tex:445-468; theorem-lanes.tex:2721-2765
  claim: One may invert all equivariant characters and then specialize.
  broken_step: Self-dual and zero-character summands are residual modes; base-change precedes inversion and only surviving nonzero characters are inverted.
  evidence_type: line_reference
  evidence_ref: local-dictionary.tex:445-468; theorem-lanes.tex:2721-2765
  confidence: high
  blast_radius: invalid normal contraction and wrong Cartan homotopy
  minimal_heal: Keep pr_{chi=0}; use Q_Omega H+H Q_Omega=id-pr_{chi=0}.
  residual: ob_{Omega,res}

- id: A1-236-05
  severity: 2
  status: valid
  lens: factorization/global sections
  target: open-obligations.tex:674-888
  claim: Reduced current brackets imply global stratified factorization sections.
  broken_step: A global theorem needs extension-by-zero products, collar modules, associativity, Weiss descent, and centrality homotopies; reduced brackets do not supply these.
  evidence_type: line_reference
  evidence_ref: open-obligations.tex:699-800; open-obligations.tex:841-888
  confidence: high
  blast_radius: false global factorization-center morphism
  minimal_heal: State Phi^{fact}_{Omega,w} as a natural transformation and make delta_pref, delta_assoc, delta_Weiss, centrality, and Roos classes part of the theorem data.
  residual: ob_{Omega,fact}, ob_{Omega,Roos}

- id: A1-236-06
  severity: 2
  status: valid
  lens: normalization
  target: local-dictionary.tex:594-628
  claim: Residue and Euler normalization are interchangeable without a theorem.
  broken_step: Residue has nu_res=1; Euler has sigma_s(epsilon_s epsilon_1 epsilon_2)^{-1}; the comparison constant and real s-orientation sign are theorem data.
  evidence_type: line_reference
  evidence_ref: local-dictionary.tex:594-628; theorem-lanes.tex:2767-2777
  confidence: high
  blast_radius: wrong trace/current normalization and wrong scalar-contact rows
  minimal_heal: Choose one branch or prove the exact comparison constant.
  residual: ob_{Omega,norm}

- id: A1-236-07
  severity: 2
  status: valid
  lens: Vol II control surface
  target: cross-volume consistency
  claim: Vol II curve chiral, Swiss-cheese, or bar-cobar grammar supplies the native C^2 global CE/PV theorem.
  broken_step: Vol II supplies discipline and grammar, not a theorem import; the native object here is the C^2 holomorphic factorization algebra and mixed current enhancement.
  evidence_type: control_surface
  evidence_ref: /Users/raeez/chiral-bar-cobar-vol2/notes/first_principles_cache_comprehensive.md:10964-11033; /Users/raeez/chiral-bar-cobar-vol2/notes/vol1_imported_antipatterns_catalogue_2026_04_30.md:168-170
  confidence: high
  blast_radius: false curve/VOA/Zhu transfer
  minimal_heal: Keep the theorem in the mixed HT C^2 habitat; any curve reduction must construct its own pushforward, bracket, BV pairing, brane image, and anomaly data.
  residual: none inside CE/PV completion once firewall is kept
```

## Exact Obstruction Data

The global theorem is blocked precisely by
\[
  \operatorname{Ob}^{\mathrm{glob}}_{\Omega,\mathrm{CE/PV}}
  =
  (
  \operatorname{ob}_{\Omega,\mathrm{Cartan}},
  \operatorname{ob}_{\Omega,\mathrm{top}},
  \operatorname{ob}_{\Omega,\mathrm{br}},
  \operatorname{ob}_{\Omega,\mathrm{diag}},
  \operatorname{ob}_{\Omega,\mathrm{res}},
  \operatorname{ob}_{\Omega,\mathrm{norm}},
  \operatorname{ob}_{\Omega,\mathrm{fact}},
  \operatorname{ob}_{\Omega,\mathrm{Roos}},
  \operatorname{ob}_{\Omega,\mathrm{QME}}
  ).
\]

The first eight are the CE/PV completion and global-sections obstruction.
The last is a firewall: the Costello graph/QME package is separate and cannot
be inferred from equivariant CE/PV localization.

## Files Changed

- Added `reconstitution/equivariant-ce-pv-refined-bracket-completion-construction-target-2026-04-30.md`.
- Added `reconstitution/swarm-2026-04-30-agent-236-equivariant-ce-pv-refined-bracket-completion-construction-target.md`.

No TeX or manuscript file was edited.

## Verification Commands

Run:

```bash
git diff --check -- reconstitution/equivariant-ce-pv-refined-bracket-completion-construction-target-2026-04-30.md reconstitution/swarm-2026-04-30-agent-236-equivariant-ce-pv-refined-bracket-completion-construction-target.md
rg -n -F -e 'Ob}^{\\mathrm{glob}}_{\\Omega,\\mathrm{CE/PV}}' -e 'D_{\\mathrm{CE},\\Omega}' -e 'Q_\\Omega^2=L_{V_\\Omega}' -e 'R_\\Omega^{N,M}' -e 'Roos' reconstitution/equivariant-ce-pv-refined-bracket-completion-construction-target-2026-04-30.md reconstitution/swarm-2026-04-30-agent-236-equivariant-ce-pv-refined-bracket-completion-construction-target.md
git status --short -- reconstitution/equivariant-ce-pv-refined-bracket-completion-construction-target-2026-04-30.md reconstitution/swarm-2026-04-30-agent-236-equivariant-ce-pv-refined-bracket-completion-construction-target.md
```

No PDF build is appropriate for this report-only ownership lane.
