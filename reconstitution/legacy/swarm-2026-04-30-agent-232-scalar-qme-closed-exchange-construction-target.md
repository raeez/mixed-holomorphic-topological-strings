# Agent 232 - Scalar QME Closed-Exchange Construction Target

Status: report-only construction target.  Owned files only:

- `reconstitution/scalar-qme-closed-exchange-construction-target-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-232-scalar-qme-closed-exchange-construction-target.md`

## Stable Core

The ordinary scalar-reduced \(\mathfrak{gl}_N\) branch has first scalar
QME class
\[
  \hbar N[\bar c]\in H^2_{\mathrm{Lie}}(\bar A;\C)[[\hbar]],
  \qquad \bar A=\C[z_1,z_2]/\C\cdot1.
\]
This is nonzero in the reduced source.  The only same-branch
closed-exchange repair has leading scalar class
\[
  [w_{\mathrm{cl}}]=-\hbar N[\bar c].
\]
The canonical target is recorded in
`reconstitution/scalar-qme-closed-exchange-construction-target-2026-04-30.md`.

## Attack Ledger

```yaml
- id: A1-232-01
  severity: 1
  status: healed
  lens: ordinary scalar branch
  target: scalar-reduced gl_N QME branch
  claim: An internal ordinary scalar local counterterm can cancel the scalar QME term.
  broken_step: The scalar associated-graded class is hbar N[bar c], and [bar c] is nonzero on bar A.
  evidence_type: line_reference
  evidence_ref: main.tex, theorem thm:scalar-qme-alternatives; appendix-unreduced-bv-qme.tex, thm:app-scalar-contact-qme-class
  files_read: [main.tex, appendix-unreduced-bv-qme.tex, claim-strength-ledger.tex]
  tools_used: [rg, sed]
  confidence: high
  blast_radius: false closure of the ordinary scalar-reduced QME branch
  minimal_heal: state the nonzero obstruction and require an opposite closed-exchange class
  residual: construct the closed-exchange source and Costello-local realization
  deciding_evidence: W_cl with scalar leading class -hbar N[bar c] and compatible counterterm

- id: A1-232-02
  severity: 1
  status: healed
  lens: source typing
  target: closed-exchange repair language
  claim: A closed-exchange term can be invoked without specifying its source extension.
  broken_step: The scalar class to be supplied is a central-extension class; without the source line K_cl and its CE class, the map has no typed domain.
  evidence_type: proof_gap
  evidence_ref: main.tex, U(1) center anomaly and scalar alternatives; tate-T1-weighted-completion.tex, closed-exchange criterion
  files_read: [main.tex, tate-T1-weighted-completion.tex, open-obligations.tex]
  tools_used: [rg, sed]
  confidence: high
  blast_radius: arbitrary external terms could masquerade as scalar QME repairs
  minimal_heal: define the opposite central extension bar A^{cl}_{-hbar N bar c}
  residual: realize that source extension by an actual closed-exchange complex
  deciding_evidence: cochain maps Xi_M from the closed-exchange tower into the scalar-contact QME complex

- id: A1-232-03
  severity: 1
  status: healed
  lens: scalar-contact projection
  target: compatibility with sigma_sc
  claim: Having a class W is enough, independently of scalar-contact projection.
  broken_step: The scalar obstruction is detected only after a filtered chain scalar projection; Xi(W) must map to -hbar N bar c under that projection.
  evidence_type: proof_gap
  evidence_ref: appendix-unreduced-bv-qme.tex, balanced scalar-contact projection; main.tex, non-scalar obstruction complex
  files_read: [appendix-unreduced-bv-qme.tex, main.tex, reconstitution/swarm-2026-04-30-agent-103-balanced-scalar-projection.md]
  tools_used: [rg, sed]
  confidence: high
  blast_radius: false cancellation in associated graded while a scalar chain defect survives
  minimal_heal: require sigma_sc Xi(W) = -hbar N bar c + d_CE eta windowwise
  residual: construct sigma_sc and Xi as compatible cochain maps in the ordinary branch
  deciding_evidence: filtered chain projection and commuting diagrams for truncation and weight transport

- id: A1-232-04
  severity: 1
  status: healed
  lens: finite-window inverse limit
  target: closed-exchange finite-window branch
  claim: Windowwise opposite classes automatically give an all-window closed-exchange kernel.
  broken_step: Compatible cohomology classes still require Roos representative and primitive compatibility.
  evidence_type: proof_gap
  evidence_ref: tate-T1-weighted-completion.tex, thm:wt-closed-exchange-counterterm-criterion
  files_read: [tate-T1-weighted-completion.tex, open-obligations.tex, reconstitution/swarm-2026-04-30-agent-111-closed-exchange-ml-tower.md]
  tools_used: [rg, sed]
  confidence: high
  blast_radius: false inverse-limit closure of the scalar branch
  minimal_heal: add beta_sc, mu_sc, and lambda_sc as mandatory obstructions
  residual: prove H0 towers are Mittag-Leffler or compute the Roos classes directly
  deciding_evidence: beta_sc = mu_sc = lambda_sc = 0 with compatible W_M and C_M

- id: A1-232-05
  severity: 2
  status: healed
  lens: alternative branches
  target: central-character and balanced-supertrace mechanisms
  claim: Central character and balanced supertrace are closed-exchange repairs of the ordinary branch.
  broken_step: Central character replaces the source before scalar reduction; balanced supertrace replaces the open model and uses sdim(C^{N|N})=0.
  evidence_type: line_reference
  evidence_ref: appendix-unreduced-bv-qme.tex, thm:app-central-character-qme-cancellation and thm:app-balanced-supertrace-qme-cancellation
  files_read: [appendix-unreduced-bv-qme.tex, reconstitution/swarm-2026-04-30-agent-103-balanced-scalar-projection.md]
  tools_used: [rg, sed]
  confidence: high
  blast_radius: conflates model replacement with same-branch cancellation
  minimal_heal: list them as alternatives, not as ordinary closed exchange
  residual: none for scalar-contact branch on their stated habitats
  deciding_evidence: not applicable
```

## Healed Construction Target

The target is a theorem-or-obstruction package:

1. Construct the source extension
   \[
     \bar A^{\mathrm{cl}}_{-\hbar N\bar c}
       =\bar A\oplus \C K_{\mathrm{cl}},
       \qquad
     [(f,aK),(g,bK)]
       =
     (\{f,g\}_{\bar A},-\hbar N\bar c(f,g)K).
   \]
2. Construct finite-window closed-exchange complexes
   \(\mathcal X^\bullet_{\mathrm{sc},w,M}(I)\), truncation maps
   \(\rho^X_{M,N}\), and cochain maps
   \[
     \Xi^{\mathrm{sc}}_M\colon
     \mathcal X^\bullet_{\mathrm{sc},w,M}(I)
       \to
     \mathfrak Q^\bullet_{\mathrm{sc},w,M}(I).
   \]
3. Construct scalar-contact projections
   \[
     \widehat\sigma_{\mathrm{sc},M}\colon
     \mathfrak Q^\bullet_{\mathrm{sc},w,M}(I)
       \to
     \mathcal S^\bullet_M(I)
   \]
   as filtered chain maps.
4. Find \(W_M\) and \(C_M\) satisfying
   \[
     \operatorname{Ob}_{\mathrm{sc},M}
       +\Xi^{\mathrm{sc}}_M(W_M)+d_MC_M=0,
   \]
   with scalar leading class
   \[
     H^1(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{sc}}_M)[W_M]
       =
     -\hbar N[\bar c_M].
   \]
5. Prove the inverse-limit obstruction triple vanishes:
   \[
     \beta^{\mathrm{sc}}_{\mathrm{cl}}
       =
     \mu^{\mathrm{sc}}_{\mathrm{cl}}
       =
     \lambda^{\mathrm{sc}}_{\mathrm{cl}}
       =
     0.
   \]

If any of these objects cannot be constructed, the theorem becomes the
obstruction theorem naming the first failed datum: the nonzero scalar
class, the closed-exchange cokernel class, the scalar-projection defect,
or one of the Roos classes.

## Alternatives Recorded

Central-character branch:
\[
  \eta(f)=-[f]_0,\qquad d_{\mathrm{CE}}\eta=\omega,\qquad
  \chi_N(f)=N[f]_0,
\]
so
\[
  \hbar N\omega+d_{\mathrm{CE}}(\hbar\chi_N)=0
\]
on the unreduced source.  This is a source replacement.

Balanced supertrace branch:
\[
  \operatorname{sdim}\C^{N|N}=0.
\]
The scalar representative vanishes on the balanced scalar-contact
habitat.  This is an open-model replacement, not a repair of ordinary
\(\mathfrak{gl}_N\).

## Verification

Read:

- `CLAUDE.md`
- `AGENTS.md`
- attack-heal swarm skill and protocol
- Vol II `chriss-ginzburg-rectify` skill
- `main.tex`
- `appendix-unreduced-bv-qme.tex`
- `appendix-factorization-current-conventions.tex`
- `tate-T1-weighted-completion.tex`
- `open-obligations.tex`
- `claim-strength-ledger.tex`
- prior reports from agents 100, 103, 104, 109, 111, 198, 220, and 223

No manuscript or script file was edited.
