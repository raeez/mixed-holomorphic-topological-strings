# Agent 104 - External-Counterterm Branch

Status: patched owned ledger surface and staged owned files only.

## Stable Core

The external-counterterm branch is not decided by the scalar QME
calculation.  After the scalar-contact projection has been lifted to an
actual filtered chain map, the first non-scalar residual is a cocycle

```tex
\mathfrak o^{\mathrm{ns}}_{n_0,M}
  \in Z^1(\mathcal Q^\bullet_{w,M}(I)),
\qquad
\mathcal Q^\bullet_{w,M}(I)=\ker\widehat\sigma_{\mathrm{sc},M}.
```

Finite-window local counterterms alone kill it exactly on the vanishing
locus of

```tex
\mathfrak O^{\mathrm{ns}}_{n_0}
  =
  \bigl(([\mathfrak o^{\mathrm{ns}}_{n_0,M}])_M,\lambda_{n_0}\bigr),
```

the obstruction vector of
Theorem `thm:wt-nonscalar-counterterm-criterion`.

A genuine closed-exchange repair requires extra cochain data:

```tex
\Xi_M:
\mathcal X^\bullet_{w,M}(I)
  \longrightarrow
\mathcal Q^\bullet_{w,M}(I),
```

where `\mathcal X^\bullet_{w,M}(I)` is the finite-window complex of
regulator-admissible closed-exchange kernels.  At the first non-scalar
order the branch equation is

```tex
\mathfrak o^{\mathrm{ns}}_{n_0,M}
  +\Xi_M(W_{n_0,M})
  +d_M C_{n_0,M}=0,
\qquad
W_{n_0,M}\in Z^1(\mathcal X^\bullet_{w,M}(I)),
\quad
C_{n_0,M}\in\mathcal Q^0_{w,M}(I).
```

For fixed `M`, this equation has a solution if and only if

```tex
[\mathfrak o^{\mathrm{ns}}_{n_0,M}]
  \in
-\,\operatorname{im}
\bigl(H^1(\Xi_M):
H^1(\mathcal X^\bullet_{w,M}(I))
\to H^1(\mathcal Q^\bullet_{w,M}(I))\bigr).
```

In the inverse-limit tower the exact branch obstruction is the triple

```tex
\beta^{\mathrm{cl}}_{n_0}
  \in
  \operatorname{coker}\!\left(
    \varprojlim_M H^1(\mathcal X^\bullet_{w,M}(I))
    \xrightarrow{\ \varprojlim H^1(\Xi_M)\ }
    \varprojlim_M H^1(\mathcal Q^\bullet_{w,M}(I))
  \right),
```

```tex
\mu^{\mathrm{cl}}_{n_0}
  \in
  \varprojlim\nolimits^1_M H^0(\mathcal X^\bullet_{w,M}(I)),
\qquad
\lambda^{\mathrm{cl}}_{n_0}
  \in
  \varprojlim\nolimits^1_M H^0(\mathcal Q^\bullet_{w,M}(I)).
```

Vanishing of all three classes is equivalent to a compatible
closed-exchange kernel plus local counterterm killing the first
non-scalar residual.

## Proposed Costello Graph/QME Pathway

1. Construct the scalar-contact lift
   `\widehat\sigma_{\mathrm{sc}}` by killing the tower
   `o_{\sigma,w}^{(r)}(I)` in the completed finite-window filtration.
2. Build the current-source bulk-to-defect kernel
   `\kappa_{\hbar,w,I}` in the Costello local-functional category,
   not only after reduced current contraction.
3. Form the residual curvature in
   `\mathcal Q^\bullet_{w,M}(I)=\ker\widehat\sigma_{\mathrm{sc},M}`.
4. Build the closed-exchange complex `\mathcal X^\bullet_{w,M}(I)`
   with closed propagator, bulk-to-defect restriction, wavefront/locality
   rule, and Costello counterterm support.
5. Prove that the cochain map `\Xi_M` is compatible with finite-window
   truncation and weight transport.
6. Kill the first residual by the branch equation above.  Iterate the
   same criterion at higher `\hbar`-orders.

## Attack Ledger

```yaml
- id: A1-104-01
  severity: 1
  status: healed
  lens: scalar/non-scalar separation
  target: open-obligations.tex, item "Componentwise quantum coefficient surface and non-scalar obstruction complex"
  claim: The scalar QME branch decides the non-scalar Costello graph/QME realization.
  broken_step: Balanced supertrace kills only the scalar-symbol representative; the filtered scalar projection and the residual class in ker sigma_sc remain separate.
  evidence_type: line_reference
  evidence_ref: main.tex:7334-7456; appendix-unreduced-bv-qme.tex:143-210; tate-T1-weighted-completion.tex:931-1115
  files_read: [main.tex, appendix-unreduced-bv-qme.tex, tate-T1-weighted-completion.tex, open-obligations.tex]
  tools_used: [rg, nl, sed]
  confidence: high
  blast_radius: false theorem promotion from componentwise surface to graph/QME theorem
  minimal_heal: state scalar-lift tower first, then form the non-scalar kernel complex
  residual: construct the scalar-contact filtered chain projection
  deciding_evidence: vanishing of all o_{sigma,w}^{(r)} with compatible finite-window choices

- id: A1-104-02
  severity: 1
  status: healed
  lens: finite-window counterterm exactness
  target: open-obligations.tex, finite-window residual language
  claim: Finite-window counterterms automatically kill the first non-scalar obstruction.
  broken_step: The counterterm criterion requires both inverse-limit H^1 vanishing and primitive compatibility in varprojlim^1 H^0.
  evidence_type: proof_gap
  evidence_ref: tate-T1-weighted-completion.tex:980-1086
  files_read: [tate-T1-weighted-completion.tex, open-obligations.tex]
  tools_used: [rg, nl, sed]
  confidence: high
  blast_radius: hides a genuine obstruction behind regulator language
  minimal_heal: record the obstruction vector O^{ns}_{n_0}
  residual: compute or prove vanishing of O^{ns}_{n_0} in the graph complex
  deciding_evidence: explicit compatible C_{n_0,M} or a proof that the two obstruction components vanish

- id: A1-104-03
  severity: 1
  status: healed
  lens: closed-exchange typing
  target: closed-exchange / external-counterterm branch
  claim: A closed-exchange term can be invoked without specifying its complex or map into the defect obstruction complex.
  broken_step: The QME equation is meaningful only after a cochain map from a closed-exchange source complex to ker sigma_sc is supplied.
  evidence_type: unsupported
  evidence_ref: appendix-factorization-current-conventions.tex:374-550; main.tex:7384-7439
  files_read: [appendix-factorization-current-conventions.tex, main.tex, open-obligations.tex]
  tools_used: [rg, nl, sed]
  confidence: high
  blast_radius: permits arbitrary terms to masquerade as Costello local counterterms
  minimal_heal: define X_{w,M}, Xi_M, and the branch equation o + Xi(W) + dC = 0
  residual: construct X and Xi from actual closed propagator and bulk-to-defect locality data
  deciding_evidence: a regulator-admissible cochain map Xi_M compatible with truncation and weights

- id: A1-104-04
  severity: 2
  status: healed
  lens: inverse-limit compatibility
  target: proposed closed-exchange criterion
  claim: A compatible cohomology class in lim H^1(X_M) is already a compatible chain-level closed-exchange kernel.
  broken_step: Choosing cocycle representatives in a tower has a Roos compatibility obstruction.
  evidence_type: proof_gap
  evidence_ref: tate-T1-weighted-completion.tex:1015-1080, same Milnor mechanism
  files_read: [tate-T1-weighted-completion.tex, open-obligations.tex]
  tools_used: [nl, sed]
  confidence: high
  blast_radius: would falsely close the branch while leaving no actual kernel W_M
  minimal_heal: add mu^{cl}_{n_0} in varprojlim^1 H^0(X_M)
  residual: prove the H^0(X_M) tower is Mittag-Leffler or choose compatible closed-exchange representatives
  deciding_evidence: ML proof for H^0(X_M) or explicit chain-level W_{n_0,M}
```

## Repairs Made

Patched `open-obligations.tex` to replace vague residual language with:

- the order of construction: scalar-contact lift, then reduced
  non-scalar kernel complex, then first residual;
- the counterterm-only obstruction vector
  `\mathfrak O^{\mathrm{ns}}_{n_0}`;
- the closed-exchange complex `\mathcal X^\bullet_{w,M}(I)`;
- the cochain map `\Xi_M`;
- the finite-window branch equation;
- the fixed-window image criterion;
- the inverse-limit obstruction triple
  `(\beta^{cl}_{n_0},\mu^{cl}_{n_0},\lambda^{cl}_{n_0})`.

## What Would Close It

The branch closes only after the following objects are supplied:

- a complete filtered chain projection `\widehat\sigma_{\mathrm{sc}}`;
- a Costello-local current-source kernel `\kappa_{\hbar,w,I}`;
- a closed-exchange tower `\mathcal X^\bullet_{w,M}(I)`;
- compatible cochain maps `\Xi_M`;
- a closed-exchange class `[W]` with
  `H^1(\Xi)[W]=-[\mathfrak o^{ns}_{n_0}]`;
- vanishing of `\mu^{cl}_{n_0}` and `\lambda^{cl}_{n_0}`;
- wavefront, support, RG, and finite-window transport checks for the
  chosen closed propagator and counterterms.

Until those data exist, the theorem-grade statement is the obstruction
criterion, not a vanishing theorem.

## Verification

Local verification used targeted reads and diff checks only.  I did not
run `make pdf`, because this shared checkout already has concurrent
tracked changes and `out/main.pdf` is outside my writable surface.
