# Agent 106 — Non-scalar QME Dictionary

Writable scope:

- `local-dictionary.tex`
- `reconstitution/swarm-2026-04-30-agent-106-nonscalar-qme-dictionary.md`

## Stable Core

The non-scalar Costello graph/QME realization is not a consequence of
the componentwise quantum coefficient surface or of the reduced
principal-part current brackets.  The usable theorem habitat is the
filtered brane-defect local-functional complex
\[
  \mathfrak Q^\bullet_{w,\partial,\hbar}(I)
  =
  \varprojlim_M
  \left(
    \mathcal O_{\mathrm{loc}}^{\mathrm{bd}}\bigl(
      \mathcal E_w^M|_I;
      A_{\partial,\hbar}^{\mathrm{pp},w,M}(I)\bigr),
    d_M
  \right),
  \qquad
  d_M=Q+\{I^w_{0,M},-\}_{\hbar,M}.
\]

The scalar-symbol map is associated-graded data.  The scalar-contact
projection is a filtered chain map whose existence is controlled by the
classes \(o_{\sigma,w}^{(r)}(I)\).  Only after this projection exists
does the residual class in
\[
  H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})
\]
make sense.  The full theorem then requires a continuous current-source
bulk-to-defect kernel and compatible finite-window counterterms solving
the unreduced QME curvature equation.

## Attack Ledger

```yaml
- id: A1-106-01
  severity: 1
  status: healed
  lens: scalar-contact filtration
  target: local-dictionary.tex; main.tex Problem prob:quantum-p0-operation-realization
  claim: The scalar-symbol projection can be used as an actual projection.
  broken_step: An associated-graded extractor does not define a chain map on the filtered QME complex.
  evidence_type: line_reference
  evidence_ref: appendix-unreduced-bv-qme.tex, Lemma filtered-scalar-projection-obstruction; Agent 100 report
  files_read: [main.tex, appendix-unreduced-bv-qme.tex, reconstitution/swarm-2026-04-30-agent-100-scalar-lift-obstruction-tower.md]
  tools_used: [sed, rg]
  confidence: high
  blast_radius: H^1(ker sigma_sc) is undefined; reduced non-scalar obstruction is promoted too early.
  minimal_heal: Add separate dictionary entries for sigma_sc, widehat sigma_sc, and o_sigma.
  residual: Prove existence of the projection beyond the balanced scalar-contact habitat.
  deciding_evidence: A constructed filtered cochain map on the full local-functional complex.

- id: A1-106-02
  severity: 1
  status: healed
  lens: reduced/unreduced separation
  target: local-dictionary.tex source-target table and reduced current rows
  claim: Reduced principal-part brackets realize the full non-scalar Costello QME.
  broken_step: The reduced brackets live after scalar reduction and de Rham-current contraction; they do not construct Costello locality, propagator, counterterms, or unreduced homotopies.
  evidence_type: line_reference
  evidence_ref: appendix-factorization-current-conventions.tex, Definition app-unreduced-nonscalar-current-lift-datum and Proposition app-nonscalar-current-lift-obstructions
  files_read: [appendix-factorization-current-conventions.tex, main.tex, reconstitution/swarm-2026-04-30-agent-093-bulk-defect-kernel.md]
  tools_used: [sed, rg]
  confidence: high
  blast_radius: A reduced algebraic theorem would be falsely read as the analytic graph theorem.
  minimal_heal: Add reduced-bracket and unreduced-QME rows with source, target, and proof role.
  residual: Construct unreduced centrality and P0-bracket homotopies against arbitrary open observables.
  deciding_evidence: Homotopies compatible with intervals, disjoint products, and finite-window maps.

- id: A1-106-03
  severity: 1
  status: healed
  lens: functional-analytic habitat
  target: local-dictionary.tex
  claim: The local-functional complex can be named without topology or filtration.
  broken_step: The obstruction theory depends on the hbar-adic, scalar-contact, and finite-window inverse-limit filtrations.
  evidence_type: line_reference
  evidence_ref: tate-T1-weighted-completion.tex, Definition wt-nonscalar-qme-tower
  files_read: [tate-T1-weighted-completion.tex, reconstitution/swarm-2026-04-30-agent-092-nonscalar-qme-habitat.md]
  tools_used: [sed, rg]
  confidence: high
  blast_radius: Counterterm compatibility and obstruction cohomology become ambiguous.
  minimal_heal: Define Q as a finite-window inverse-limit complex with transported differential.
  residual: Prove Costello locality for the current-valued local functionals.
  deciding_evidence: A finite-scale BV/RG construction preserving the same completed tower.

- id: A1-106-04
  severity: 2
  status: healed
  lens: finite-window counterterms
  target: local-dictionary.tex
  claim: A counterterm is any finite local change killing the residual.
  broken_step: Compatible counterterms must be degree-zero primitives in Q_{w,M}, commute with truncation, and kill the lim H1 plus lim1 H0 obstruction pair.
  evidence_type: line_reference
  evidence_ref: tate-T1-weighted-completion.tex, Theorem wt-nonscalar-counterterm-criterion; Agent 094 report
  files_read: [tate-T1-weighted-completion.tex, reconstitution/swarm-2026-04-30-agent-094-finite-window-counterterms.md]
  tools_used: [sed, rg]
  confidence: high
  blast_radius: Windowwise exactness could be mistaken for a compatible all-order counterterm.
  minimal_heal: Add C_{n,M}, C_{\Gamma,w}^{w_0}, and O_n^ns dictionary entries.
  residual: Compute or prove vanishing of O_n^ns in the actual graph complex.
  deciding_evidence: Compatible primitives or a Mittag-Leffler H0 theorem for the relevant tower.

- id: A1-106-05
  severity: 2
  status: healed
  lens: kernel construction
  target: local-dictionary.tex
  claim: The reduced current presentation supplies the bulk-to-defect kernel.
  broken_step: The kernel must be a continuous curved map from the unreduced current CE source to the brane-defect local-functional complex.
  evidence_type: line_reference
  evidence_ref: main.tex Problem quantum-p0-operation-realization; Agent 093 report
  files_read: [main.tex, appendix-factorization-current-conventions.tex, reconstitution/swarm-2026-04-30-agent-093-bulk-defect-kernel.md]
  tools_used: [sed, rg]
  confidence: high
  blast_radius: The QME curvature class would lack a source, target, and degree.
  minimal_heal: Add g^{cur}, kappa, and Ob_{w,partial,hbar} entries.
  residual: Build kappa with Costello finite-scale BV propagator and locality estimates.
  deciding_evidence: A continuous kernel whose curvature is killed by compatible counterterms.

- id: A1-106-06
  severity: 2
  status: healed
  lens: moment-ideal primitive
  target: local-dictionary.tex
  claim: The scalar primitive is a reduced counterterm.
  broken_step: The primitive eta(f)=-[f]_0 lives on the unreduced source A and does not descend to A/C.
  evidence_type: line_reference
  evidence_ref: appendix-unreduced-bv-qme.tex, Lemma app-unreduced-scalar-primitive and Theorem app-central-character-qme-cancellation
  files_read: [appendix-unreduced-bv-qme.tex, appendix-radial-parts-moyal.tex, main.tex]
  tools_used: [sed, rg]
  confidence: high
  blast_radius: The ordinary scalar-reduced obstruction would be falsely cancelled internally.
  minimal_heal: Add I_N, eta, chi_N entry separating source replacement from reduced counterterm.
  residual: None inside the scalar primitive dictionary; the non-scalar QME remains open.
  deciding_evidence: Already supplied by the unreduced scalar primitive computation.

- id: A1-106-07
  severity: 3
  status: healed
  lens: CE/PV current degrees
  target: local-dictionary.tex current source entries
  claim: The current-source generators can be left degree-free.
  broken_step: The source-target map depends on c_{B,rho} having CE degree 1 and u_{a(t)dt otimes f} having degree 0.
  evidence_type: line_reference
  evidence_ref: appendix-factorization-current-conventions.tex, Definition app-factorization-current-coordinates
  files_read: [appendix-factorization-current-conventions.tex, local-dictionary.tex]
  tools_used: [sed, rg]
  confidence: high
  blast_radius: The curvature and bracket-defect degrees become ambiguous.
  minimal_heal: Add degree data to the current-source and kernel entries.
  residual: None for the dictionary entry.
  deciding_evidence: Existing current-coordinate definition.

- id: A1-106-08
  severity: 2
  status: healed
  lens: moment-ideal primitive
  target: local-dictionary.tex
  claim: The phrase moment-ideal primitive denotes the same object as the scalar CE primitive eta.
  broken_step: Agent 099 isolates a separate all-N quantum shear primitive in the left moment-map ideal W_N mu(sl_N), with coefficients A^j_i(a,b,N).
  evidence_type: line_reference
  evidence_ref: appendix-radial-parts-moyal.tex, Lemma app-quantum-shear-primitive-obstruction; Agent 099 report
  files_read: [appendix-radial-parts-moyal.tex, reconstitution/swarm-2026-04-30-agent-099-quantum-shear-congruence.md]
  tools_used: [sed, rg]
  confidence: high
  blast_radius: The radial/Weyl all-N bottleneck could be confused with scalar QME cancellation.
  minimal_heal: Add a separate E_{a,b,N}, A^j_i(a,b,N) dictionary row.
  residual: Construct the all-N coefficients or prove they cannot exist.
  deciding_evidence: A formula for A^j_i(a,b,N) proving left-ideal membership for all N,a,b.
```

## Repairs Made

Added a new `Non-scalar Costello/QME dictionary` block to
`local-dictionary.tex`.  It defines:

- the filtered local-functional complex \(\mathfrak Q\);
- the scalar-contact filtration \(F^\bullet\);
- the associated-graded scalar-symbol map \(\sigma_{\mathrm{sc}}\);
- the actual scalar-contact projection \(\widehat\sigma_{\mathrm{sc}}\);
- the scalar-lift obstruction tower \(o_{\sigma,w}^{(r)}\);
- the current source \(\mathfrak g^{w,\mathrm{cur}}_{\hbar,I}\);
- the bulk-to-defect kernel \(\kappa_{\hbar,w,I}\);
- the curvature cocycle \(\operatorname{Ob}_{w,\partial,\hbar}\);
- the reduced non-scalar obstruction class;
- finite-window residual complexes and counterterms;
- the order-\(n\) obstruction vector \(\mathfrak O_n^{\mathrm{ns}}\);
- the moment-ideal/scalar primitive data \(I_N,\eta,\chi_N\);
- the all-\(N\) quantum shear moment-ideal primitive
  \(E_{a,b,N}=\sum A^j{}_i\widehat\mu^i{}_j\);
- the reduced principal-part bracket scope;
- the unreduced non-scalar QME realization equation.

## Residual Missing Definitions

1. A constructed full balanced scalar-contact habitat containing all
   local functionals needed by the non-scalar graph theorem.
2. Current-compatible wavefront, locality, and counterterm rules for
   \(\mathcal D'_c\)-valued principal-part coefficients, or a proved
   restriction to regular densities.
3. The finite-scale Costello BV propagator and BV Laplacian for the
   weighted brane-defect current complex.
4. A continuous bulk-to-defect kernel
   \(\kappa_{\hbar,w,I}\) before reduced current contraction.
5. Product and \(P_0\)-bracket homotopies against arbitrary unreduced
   open observables.
6. Vanishing or computation of every
   \(\mathfrak O^{\mathrm{ns}}_n\), including the
   \(\varprojlim^1H^0\) primitive-compatibility component.
7. Construction of the all-\(N\) quantum shear coefficients
   \(A^j{}_i(a,b,N)\) proving
   \(E_{a,b,N}\in\mathcal W_N\widehat\mu(\lie{sl}_N)\), or a proof of
   nonexistence.

## Verification

Commands run:

- `git diff --check -- local-dictionary.tex reconstitution/swarm-2026-04-30-agent-106-nonscalar-qme-dictionary.md`
- `rg -n -F -e 'Non-scalar Costello/QME dictionary' -e 'mathfrak Q^\bullet_{w,\partial,\hbar}' -e 'widehat\sigma_{\mathrm{sc}}' -e 'mathfrak O^{\mathrm{ns}}_n' -e 'E_{a,b,N}' -e 'Unreduced non-scalar QME realization' local-dictionary.tex`
- `pdflatex -draftmode -interaction=nonstopmode -halt-on-error -output-directory=/tmp main.tex`
- `rg -n "Overfull|Undefined control sequence|Emergency stop|Fatal error|LaTeX Error|There were undefined references" /tmp/main.log`

Results:

- `git diff --check` returned clean.
- Targeted dictionary-entry search found the new block and the required
  non-scalar entries.
- Draft TeX build completed with output directed to `/tmp`; no repo build
  artifacts were written.
- The first draft pass exposed one overfull box in the new unreduced QME
  display; the display was rewritten using
  \(K_{\hbar,w,I}=\kappa_{\hbar,w,I}+C_{\hbar,w}\).
- The final log scan returned no overfull boxes, undefined control
  sequences, fatal errors, LaTeX errors, or undefined-reference summary.
  Existing underfull warnings and a rerun notice remain outside the
  dictionary repair.
