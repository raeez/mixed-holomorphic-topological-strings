# Agent 271 - Scalar Central-Extension Integration Spec

Status: report-only.  No manuscript TeX, script, source fixture, figure, PDF,
or bibliography file was edited.

Owned files:

- `reconstitution/scalar-central-extension-integration-spec-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-271-scalar-central-extension-integration-spec.md`

The canonical integration spec is
`reconstitution/scalar-central-extension-integration-spec-2026-04-30.md`.

## Decision

Agent 265's branch is theorem-grade in the CE source-replacement category:
\[
  L^-_N=\bar A^{\mathrm{cl}}_{-\hbar N\bar c}
  =
  \bar A\oplus\C[[\hbar]]K_{\mathrm{cl}},
  \qquad
  [(f,aK),(g,bK)]
  =
  (\{f,g\}_{\bar A},-\hbar N\bar c(f,g)K).
\]
With \(k^\vee(K_{\mathrm{cl}})=1\) and \(k^\vee(\bar A)=0\),
\[
  d_{\mathrm{CE}}k^\vee=\hbar N\bar c,\qquad
  d_{\mathrm{CE}}(-k^\vee)=-\hbar N\bar c.
\]
Thus the scalar QME representative
\(\operatorname{Ob}_{\mathrm{sc}}=\hbar N\bar c\) is killed in
\(C^\bullet_{\mathrm{Lie}}(L^-_N)\) by \(J_{\mathrm{op}}=-k^\vee\).

It is not a same-branch Costello-local closed exchange.  The cancelling
cochain is not closed; its CE differential is the contact term being killed.
It is also not a BV field or graph source: no \(K_{\mathrm{cl}}\)-dual,
coevaluation kernel, propagator, bulk-to-defect graph map, source-face Hom
calculus, or current-compatible counterterm theorem has been constructed.

## Manuscript Integration

Integrate the theorem into `main.tex` at
Theorem `\ref{thm:scalar-qme-alternatives}`:

1. Add a separate branch for \(L^-_N\), preferably after the unreduced
   central-character branch and before the algebraic central-contact cone.
2. Include the CE sign computation
   \(d_{\mathrm{CE}}(-k^\vee)=-\hbar N\bar c\).
3. State the pushout relation to the unreduced extension:
   \(1\mapsto-\hbar N K_{\mathrm{cl}}\), with pullback
   \(J_{\mathrm{op}}\Phi=\hbar\chi_N\), \(\chi_N(f)=N[f]_0\).
4. Keep the Costello-local obstruction paragraph unchanged in strength:
   the ordinary scalar-reduced branch still needs a closed source complex,
   finite-scale propagator, bulk-to-defect map, source-face Hom differential,
   scalar-contact chain projection, and finite-window/Roos-compatible
   counterterms.

Update the control surfaces:

- `theorem-lanes.tex`: add the proved source-replacement status to the
  scalar \(U(1)\) anomaly lane; do not replace the balanced
  \(\{0_{\mathrm{sc}}\}\) component of the quantum coefficient surface.
- `open-obligations.tex`: mark the opposite central source branch closed only
  after source replacement; keep the same-branch Costello-local scalar
  exchange obligation open.
- `claim-strength-ledger.tex`: classify the branch as proved CE
  source replacement and keep the ordinary Costello-local obstruction vector
  \((o_{\sigma}^{(1),\mathrm{sc}},\beta,\mu,\lambda_C)\).

## Verification

Read and checked:

- `CLAUDE.md`, `AGENTS.md`, ecosystem invariants and harness sections, and the
  Vol II `chriss-ginzburg-rectify` standard.
- `main.tex`, `theorem-lanes.tex`, `open-obligations.tex`,
  `claim-strength-ledger.tex`, `appendix-unreduced-bv-qme.tex`,
  `local-dictionary.tex`, `tate-T1-weighted-completion.tex`.
- Agent reports 232, 241, 247, 259, and 265.
- Costello graph/QME source fixture.

Direct check:

```text
CE cocycle failures through bidegree<6: 0
cbar(z1,z2)= 1
bar bracket {z1,z2}_bar terms: []
d(-kvee)(z1,z2) in L_-: -hbar*N
Ob_sc(z1,z2): +hbar*N
```

No PDF build was run.
