# Agent 355 priority-lane construction brief

Status: report-only.  No TeX, script, figure, bibliography, PDF, or build
artifact was edited.

## Lane selection

Chosen lane: rank 5, `stratified-omega-descent`.

Reason.  Rank 1 `theta3-bianchi-column` is covered by the fresh
theta reports, in particular Agents 350 and 351.  Rank 2
`nonscalar-marked-row-package` is covered by the live/non-scalar reports
around Agents 338 and 350.  Rank 3 `radial-decorated-stokes` is covered
by live radial ownership in the launch log.  Rank 4 `bmk-native-all-window`
is covered by the live BMK/source-boundary and bibliography lane around
Agents 333 and 339.  The first queue entry not covered by a live or fresh
same-lane agent is therefore the stratified Omega descent lane.

## Controlling claim

The manuscript has a proved reduced product-basis prefactorization datum
and a correctly exposed internal obstruction vector.  It does not yet have
a constructed stratified factorization algebra on
\[
  (X,L)=
  (\mathbb R_t\times\mathbb R_s\times\mathbb C^2_{z_1,z_2},
   \mathbb R_t\times\{s=z_1=z_2=0\})
\]
with collars, collared Weiss descent, Roos-compatible contractions,
\(Q_\Omega\)-basic centrality homotopies, and brane-defect QME curvature
cancellation.

The construction target is not a prose demotion.  It is:
\[
  \mathcal F^{\mathrm{str}}_{\Omega,N,M}\colon
  \operatorname{Disk}^{\mathrm{str}}_{X,L}
  \to
  \operatorname{Ch}_{R_\Omega^{N,M}[[\hbar_{\mathrm{QME}}]]}
\]
with the nine-component internal obstruction vector killed by explicit
null-homotopies, or an obstruction theorem naming the first nonzero
component.

## Definitions to fix

1. Normal equivariant data.
   Use the brane-preserving normal torus
   \[
     T_\Omega=\mathbb C^*_{\epsilon_s}\times
     \mathbb C^*_{\epsilon_1}\times\mathbb C^*_{\epsilon_2},
     \qquad
     V_\Omega=\epsilon_s s\partial_s+
     \epsilon_1z_1\partial_{z_1}+\epsilon_2z_2\partial_{z_2},
   \]
   with \(V_\Omega(t)=0\),
   \[
     Q_\Omega=Q+\iota_{V_\Omega},\qquad Q_\Omega^2=L_{V_\Omega}.
   \]
   Work in the invariant/basic subcomplex.  The coefficient ring is
   \[
     R_\Omega^{N,M}
     =
     \mathbb C[\epsilon_s,\epsilon_1,\epsilon_2,\hbar_\omega]
     [\chi^{-1}\mid \chi\in\mathsf X_{N,M}],
   \]
   where \(\mathsf X_{N,M}\) is the finite set of nonzero moving characters
   in the chosen normal/Hamiltonian window.  Keep
   \(\hbar_{\mathrm{QME}}\), \(\hbar_{\mathrm W}\), and \(\hbar_\omega\)
   distinct unless a branch theorem identifies them.

2. Stratified disk category.
   \(\operatorname{Disk}^{\mathrm{str}}_{X,L}\) has three basic local
   shapes: bulk mixed HT disks in \(X\setminus L\), brane intervals in
   \(L\), and product collars
   \(C(I;\epsilon,B)=I_t\times(-\epsilon,\epsilon)_s\times B_{z_1,z_2}\)
   meeting the lower stratum.  Operations are disjoint embeddings respecting
   strata and collars.

3. Reduced positive datum.
   On product basics the already proved datum is
   \[
     \mathcal F^{\mathrm{red}}_{\Omega,X}(U\times B)
     =
     C^\bullet_{\mathrm{CE},\mathrm{cont}}
     \left(
       \Omega_c^\bullet(U)\widehat\otimes
       \Omega_c^{0,\bullet}(B)\widehat\otimes
       (\mathfrak h\ltimes\mathcal P[1])
     \right)\widehat\otimes R_\Omega^{N,M},
   \]
   and on brane intervals, for the first construction pass, choose the
   stable principal-part branch
   \[
     \mathcal F^{\mathrm{red}}_{\Omega,L}(I)
     =
     A^{\mathrm{pp},w}_{\partial,\Omega,\hbar_{\mathrm W}}(I).
   \]
   Products are extension by zero on compact supports followed by CE or
   completed symmetric multiplication.  This proves only
   \(\delta_{\mathrm{pref}}=\delta_{\mathrm{assoc}}=0\) on the reduced
   product-basis object.

4. Collar datum.
   A collar value must be a module
   \[
     \mathcal M_{\Omega,N,M}(C;I)
   \]
   over the brane interval algebra, equipped with a bulk-to-brane collar
   map
   \[
     \pi^{\mathrm{coll}}_{L,\Omega,C}\colon
     \mathcal F^{\mathrm{red}}_{\Omega,X}(C)
     \to
     C^\bullet_{\mathrm{CE},\Omega,\mathrm{cont}}
     (\Omega_c^\bullet(I)\widehat\otimes(\mathfrak h\ltimes\mathcal P[1]))
   \]
   and a coefficient-current realization
   \[
     \kappa_{\mathrm{coef},\Omega}\colon
     C^\bullet_{\mathrm{CE},\Omega,\mathrm{cont}}
     (\Omega_c^\bullet(I)\widehat\otimes(\mathfrak h\ltimes\mathcal P[1]))
     \to
     A^{\mathrm{pp},w}_{\partial,\Omega,\hbar_{\mathrm W}}(I).
   \]
   The acceptance equation is a basic collar contraction
   \[
     Q_\Omega h_{\Omega,C}+h_{\Omega,C}Q_\Omega
     =
     \operatorname{id}-j_{L,C}\pi^{\mathrm{coll}}_{L,\Omega,C},
     \qquad
     [L_{V_\Omega},h_{\Omega,C}]=0,
   \]
   with support, wavefront, and finite-window estimates compatible with
   the chosen Costello local-functional habitat.  Failure is
   \(\operatorname{ob}_{\mathrm{collar}}\), not a missing citation.

5. Collared Cech/Roos descent.
   A collared stratified Weiss cover \(\mathcal U=\{U_i\}\) of \(V\) is a
   stratified cover such that every finite subset of \(V\) lies in some
   \(U_i\), and if that finite subset meets \(L\), the same \(U_i\)
   contains a product collar of its lower-stratum part.  The Cech complex is
   \[
     \check C^p(\mathcal U;\mathcal F^q)
     =
     \prod_{i_0<\cdots<i_p}
     \mathcal F^q(U_{i_0}\cap\cdots\cap U_{i_p}),
     \qquad
     \mathbb D=\check\delta+(-1)^p d_{\mathcal F},
   \]
   and
   \[
     \Delta^{N,M}_{V,\mathcal U}
     =
     \operatorname{Cone}\left(
       \mathcal F^{\mathrm{str}}_{\Omega,N,M}(V)
       \to
       \operatorname{Tot}\check C^\bullet
       (\mathcal U;\mathcal F^{\mathrm{str}}_{\Omega,N,M})
     \right).
   \]
   The construction must supply contractions
   \(s_{V,\mathcal U}^{N,M}\) with
   \[
     \mathbb D_\Delta s+s\mathbb D_\Delta=\operatorname{id}
   \]
   and prove compatibility under refinement, finite-window projection,
   interval inclusion, and admissible weight transport.  The remaining
   obstruction is
   \[
     \delta_{\mathrm{Weiss}}^{\check C/R}
     =
     \left(
       \{H^\bullet(\Delta^{N,M}_{V,\mathcal U})\}_{V,\mathcal U,N,M},
       \mathfrak w^{\check C/R}_{V,\Omega,N,M}
     \right).
   \]

6. Centrality and QME datum.
   After the scalar projection lift exists, centrality rows must live in
   \(\mathcal K^\bullet_{\mathrm{ns},\Omega,M}\).  For invariant generators
   \(x,y\),
   \[
     R^{\mathrm{cent}}_{x,y,\Omega,M}
     +d_{M,\Omega}H^\Omega_{x,y,M}=0,\qquad
     L_{V_\Omega}H^\Omega_{x,y,M}=0.
   \]
   The brane-defect QME kernel must satisfy
   \[
     \operatorname{Curv}(K_{\Omega,N})
     =
     d_{\mathrm{QME}}K_{\Omega,N}
     +\frac12[K_{\Omega,N},K_{\Omega,N}]_{\hbar_{\mathrm{QME}}}=0
   \]
   as a natural transformation of the stratified prefactorization object,
   not only as a reduced current identity.

## Proof sequence

1. Freeze the branch.
   Use the stable principal-part branch and residue normalization first:
   \(\nu_\Omega^{\mathrm{res}}=1\).  Do not mix in the Euler factor unless
   the proof also writes the sign
   \(\sigma_s(\epsilon_s\epsilon_1\epsilon_2)^{-1}\).

2. Record the reduced positive theorem.
   Cite the current anchors: `main.tex:1193-1250`,
   `appendix-factorization-current-conventions.tex:830-922`, and the
   current `theorem-lanes.tex:3165-3185`.  This closes only
   \(\delta_{\mathrm{pref}}\) and \(\delta_{\mathrm{assoc}}\) for the
   reduced product basis.

3. Construct the collar map.
   Build \(h_{\Omega,C}\), \(\pi^{\mathrm{coll}}_{L,\Omega,C}\), and
   \(j_{L,C}\) first on generators.  Check the Cartan equation, support
   localization on collars, finite-window compatibility, and wavefront
   admissibility.  If the contraction cannot be made Costello-local, prove
   an obstruction theorem identifying the nonzero
   \(\operatorname{ob}_{\mathrm{collar}}\) class.

4. Extend products through collars.
   Define mixed bulk/collar/brane products by extension by zero followed by
   the collar module action.  Verify the chain defect
   \(\delta_{\mathrm{pref}}\mu_{\mathrm{str}}\) and associativity defect
   \(\delta_{\mathrm{assoc}}\mu_{\mathrm{str}}\).  Any failure must be a
   named cochain in the collar module complex.

5. Prove Cech descent by contraction, not by slogan.
   For each finite collared cover, build a Cech contraction of
   \(\Delta^{N,M}_{V,\mathcal U}\).  Then place these contractions in the
   Roos complex over refinements and windows.  The closure condition is a
   zero Roos class, not the phrase "Weiss descent".

6. Add \(Q_\Omega\)-basic centrality.
   Form the finite-row centrality table from the equivariant Costello list.
   Check the scalar gate
   \(\widehat\sigma_{\mathrm{sc},\Omega,M}
     (R^{\mathrm{cent}}_{x,y,\Omega,M})=0\), solve for
   \(H^\Omega_{x,y,M}\), and then check
   \(L_{V_\Omega}H^\Omega_{x,y,M}=0\).  If a primitive exists only before
   taking invariants, the surviving class
   \([L_{V_\Omega}H]\) is the exact obstruction.

7. Close the brane-defect QME only after the non-scalar gates close.
   Use the criterion of
   `appendix-unreduced-bv-qme.tex:2866-3028`: scalar projection lift,
   scalar gates \(\mathfrak s_{n,\Omega,M}\), non-scalar classes
   \(\mathfrak o^{\mathrm{ns}}_{n,\Omega,M}\), counterterms, and
   \(\varprojlim^1H^0\) primitive compatibility.  The trace-state topology
   remains dependent on this closure and should not be advertised as solved
   in this lane.

## Exact future write scopes

The construction agent should write only the following TeX ranges, after
the construction data exist.  If line numbers drift, locate by the labels
and statement names listed here.

- `main.tex:4672-4704`, label
  `rmk:weiss-ran-descent-obstruction`: replace the current obstruction
  remark by a construction/obstruction theorem for the collar Cech/Roos
  datum, or append the theorem immediately after it.  Do not edit compact
  CY, radial, BMK, or LQT regions.
- `theorem-lanes.tex:2901-3250`, labels
  `thm:lane-omega-weighted-kernel-qme-surface` and
  `thm:lane-stratified-trace-physical-large-n`: add the collar/Cech/Roos
  construction steps and keep the QME boundary as a separate gate.
- `open-obligations.tex:1001-1238`: replace open obligations only when a
  component is actually constructed or obstructed by a named cohomology
  class.  Do not write the trace-state block beginning after this range.
- `claim-strength-ledger.tex:846-940`: update claim strength for the
  stratified factorization and QME package only.  Keep physical trace
  status separate unless \(\operatorname{Ob}_{\mathrm{tr},\Omega}\) is
  explicitly attacked in a new lane.
- `reconstitution/`: reports only.  This Agent 355 report is the only file
  written in the present turn.

Do not write `local-dictionary.tex` under this queue item.  If the
integration owner wants canonical-symbol table changes, launch a separate
dictionary propagation lane.

## Verification commands

For this report:

```bash
git diff --check -- reconstitution/swarm-2026-04-30-agent-355-priority-lane-construction-brief.md
git diff --check --no-index -- /dev/null reconstitution/swarm-2026-04-30-agent-355-priority-lane-construction-brief.md
```

For a future TeX integration of this lane:

```bash
rg -n -F '\\operatorname*{holim}' main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex
rg -n -F 'Ob^{266}' main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex
rg -n -F 'P_{0,\\hbar_{\\mathrm{W}}}' theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex
rg -n -F '\\operatorname{Ob}^{\\mathrm{int}}_{\\mathrm{str},\\Omega,N}' main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
rg -n -F '\\delta_{\\mathrm{Weiss}}^{\\check C/R}' main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
rg -n -F 'Q_\\Omega=Q+\\iota_{V_\\Omega}' main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex appendix-unreduced-bv-qme.tex
rg -n -F '\\hbar_{\\mathrm{QME}}' theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex appendix-unreduced-bv-qme.tex
git diff --check -- main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
```

If QME rows or finite-window arrays are changed, also run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
```

At session-end integration, after active agents settle:

```bash
make pdf
```

## Acceptance criterion

The lane is closed only in one of two forms.

Positive form: the manuscript contains the collar module, collared
Cech/Roos contractions, \(Q_\Omega\)-basic centrality primitives,
finite-window QME counterterms, and transition/Roos compatibility, all in
the stated local mixed HT habitat.

Obstruction form: the manuscript proves that one named entry of
\[
  \operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}
\]
is nonzero, with the detecting class written in the appropriate Cech,
Roos, non-scalar kernel, centrality, or basic Cartan cohomology group.
External Costello--Gwilliam, AFT, CFG, Weiss/Ran, or Omega-background
analogies do not count as closure without a matched-conventions morphism
to this local pair \((X,L)\).
