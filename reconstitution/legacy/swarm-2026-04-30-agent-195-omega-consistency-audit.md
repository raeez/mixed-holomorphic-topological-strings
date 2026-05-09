# Agent 195 Report: Omega Consistency Audit

Status: report-only audit.  No TeX files edited.

Owned paths:

- `reconstitution/omega-consistency-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-195-omega-consistency-audit.md`

## Claim Attacked

The new Omega surfaces could be integrated with inconsistent notation or
formula conventions: \(\epsilon\) versus \(\varepsilon\), \(\hbar\) versus
\(\hbar_\omega\), self-dual specialization, \(Q_\Omega\), field weights,
normal localization denominators, and residue/Euler normalization.

## Verdict

Valid attack.  The stable mathematical core exists, but it is not yet
dependency-closed across the manuscript surfaces.  The main conflicts are:

- Omega weights must use \(\epsilon_s,\epsilon_1,\epsilon_2\).  Several
  current surfaces use \(\varepsilon_s,\varepsilon_1,\varepsilon_2\),
  colliding with the open trace orientation notation.
- The QME appendix localizes only at
  \((\epsilon_s\epsilon_1\epsilon_2)^{-1}\).  The weighted-kernel theorem
  requires finite-window inversion of all moving characters
  \(\chi\in\mathsf X_{N,M}\).
- \(\hbar_\omega\) is used both as an equivariant line scalarizer and as a
  possible Weyl/Moyal specialization.  QME scalar-contact formulas must
  state whether \(\hbar_\omega\) is independent of the QME/Weyl \(\hbar\)
  or identified after reindexing orders.
- The equivariant CE/PV weights and \(\hbar_\omega\)-scaled differential
  are in Agent 189's report but not yet in `theorem-lanes.tex`.
- Residue and Euler normalization are separated correctly in principle;
  the QME appendix must add the orientation sign \(\sigma_s\), and
  `open-obligations.tex` must not call an Euler-rescaled residue branch the
  plain residue normalization.

## Valid Attacks

```yaml
- id: A1-195-01
  severity: 2
  status: valid
  lens: notation
  target: Omega equivariant parameters
  claim: The manuscript can use epsilon and varepsilon interchangeably for Omega weights.
  broken_step: local-dictionary.tex reserves epsilon_s,epsilon_1,epsilon_2 for Omega weights and says varepsilon_1,varepsilon_2 are open trace orientation generators.
  evidence_type: line_reference
  evidence_ref: local-dictionary.tex:407-417; abstract.tex:195-208; appendix-unreduced-bv-qme.tex:2152-2184; open-obligations.tex:527,559-560,645,672
  confidence: high
  blast_radius: collision between equivariant weights and Ext/orientation variables
  minimal_heal: Replace Omega varepsilon symbols by epsilon symbols in Omega passages only.
  residual: none after glyph sync

- id: A1-195-02
  severity: 1
  status: valid
  lens: localization
  target: R_Omega
  claim: Inverting epsilon_s epsilon_1 epsilon_2 is enough for normal Omega contractions.
  broken_step: moving summands carry characters n epsilon_s+a epsilon_1+b epsilon_2 and n epsilon_s-a epsilon_1-b epsilon_2, not only coordinate-axis characters.
  evidence_type: source_conflict
  evidence_ref: local-dictionary.tex:445-457; tate-T1-weighted-completion.tex:398-409; appendix-unreduced-bv-qme.tex:2175-2183
  confidence: high
  blast_radius: false contraction of moving modes and wrong resonant projection
  minimal_heal: Use R_Omega^{N,M}=C[epsilon_s,epsilon_1,epsilon_2,hbar_omega][chi^{-1}|chi in X_{N,M}] or a named global character localization.
  residual: scalar specializations still need nonresonance or q-moderate bounds

- id: A1-195-03
  severity: 1
  status: undecided
  lens: quantum parameter
  target: hbar versus hbar_omega
  claim: hbar_omega may be identified with hbar without changing QME order bookkeeping.
  broken_step: appendix-unreduced-bv-qme.tex keeps hbar and hbar_omega simultaneously and forms scalar-contact terms with both.
  evidence_type: line_reference
  evidence_ref: local-dictionary.tex:503-530; appendix-unreduced-bv-qme.tex:2175-2197; appendix-unreduced-bv-qme.tex:2292-2297
  confidence: high
  blast_radius: possible one-order shift or double count in scalar-contact/QME expansion
  minimal_heal: State whether hbar_omega is independent of the QME expansion hbar, or rename the QME/Weyl parameter before identifying hbar_omega with it.
  residual: decide branch and propagate through all Omega QME obstruction rows

- id: A1-195-04
  severity: 2
  status: valid
  lens: CE/PV weights
  target: theorem-lanes.tex and local dictionary
  claim: The non-equivariant CE/PV theorem lane is already the Omega-refined theorem.
  broken_step: the Omega theorem needs c/theta weights, u/O weights, and hbar_omega-scaled CE/PV differentials.
  evidence_type: missing_hypothesis
  evidence_ref: theorem-lanes.tex:678-742; theorem-lanes.tex:922-950; theorem-lanes.tex:1000-1136; Agent 189 report lines 29-67
  confidence: high
  blast_radius: wrong equivariant cochain differential and non-equivariant theorem promoted beyond its hypotheses
  minimal_heal: Add an Omega-refined theorem lane or mark the current lane explicitly non-equivariant.
  residual: bracket-admissible completion still must be proved

- id: A1-195-05
  severity: 2
  status: valid
  lens: normalization
  target: residue/Euler normalization
  claim: Residue and Euler localization can be interchanged by prose.
  broken_step: Euler localization multiplies by sigma_s(epsilon_s epsilon_1 epsilon_2)^-1; residue normalization does not.
  evidence_type: normalization_mismatch
  evidence_ref: local-dictionary.tex:565-588; tate-T1-weighted-completion.tex:481-499; appendix-unreduced-bv-qme.tex:2258-2265; open-obligations.tex:668-675
  confidence: high
  blast_radius: wrong scalar-contact and trace coefficients
  minimal_heal: Add sigma_s to the QME appendix and name Euler-rescaled residue as a separate branch.
  residual: fix sigma_s by an orientation theorem

- id: A1-195-06
  severity: 3
  status: valid
  lens: report surface
  target: Agent 192 report
  claim: The requested Agent 192 report is present.
  broken_step: launch log records the lane, but no matching report file exists.
  evidence_type: file_absence
  evidence_ref: reconstitution/swarm-live-launch-log-2026-04-30.md:1226-1231; rg --files over reconstitution
  confidence: high
  blast_radius: current-bracket theorem lacks its requested compact attack-heal report
  minimal_heal: Obtain or regenerate reconstitution/swarm-2026-04-30-agent-192-equivariant-brane-current-brackets-0957.md.
  residual: appendix current-bracket theorem itself was locally audited and is formula-consistent
```

## Files Changed

- Added `reconstitution/omega-consistency-audit-2026-04-30.md`.
- Added `reconstitution/swarm-2026-04-30-agent-195-omega-consistency-audit.md`.

## Checks

Context and scans run:

```bash
# read requested attack-heal-swarm SKILL.md and references/protocol.md
rg --files -g 'CLAUDE.md' -g 'AGENTS.md' -g '*local-dictionary*' -g '*tate-T1*' -g '*appendix-unreduced-bv-qme*' -g '*appendix-factorization-current-conventions*' -g '*theorem-lanes*'
rg -n -F -e '\\varepsilon_s' -e '\\varepsilon_1' -e '\\varepsilon_2' -e '\\epsilon_s' -e '\\epsilon_1' -e '\\epsilon_2' local-dictionary.tex tate-T1-weighted-completion.tex appendix-unreduced-bv-qme.tex appendix-factorization-current-conventions.tex theorem-lanes.tex abstract.tex claim-strength-ledger.tex open-obligations.tex
rg -n -F -e '\\hbar_\\omega' -e '\\hbar' local-dictionary.tex tate-T1-weighted-completion.tex appendix-unreduced-bv-qme.tex appendix-factorization-current-conventions.tex theorem-lanes.tex abstract.tex claim-strength-ledger.tex open-obligations.tex
rg -n -F -e 'Q_\\Omega=Q+\\iota' -e 'Q_\\Omega^2=L' -e 'V_\\Omega' -e 'L_{V_\\Omega}' local-dictionary.tex appendix-unreduced-bv-qme.tex abstract.tex claim-strength-ledger.tex open-obligations.tex
git diff --check -- reconstitution/omega-consistency-audit-2026-04-30.md reconstitution/swarm-2026-04-30-agent-195-omega-consistency-audit.md
```

`git diff --check` passed.  No PDF build was run.  This lane changed only
Markdown reports.

## Remaining Obligations

The exact TeX fix list is in
`reconstitution/omega-consistency-audit-2026-04-30.md`.  The mathematical
residuals are: mixed Cartan model, normal contraction signs, nonresonance
or small-denominator bounds, \(\hbar/\hbar_\omega\) branch choice,
equivariant CE/PV completion, residue/Euler comparison sign, equivariant
QME graph package, stratified factorization, trace state, Ward identities,
and physical large-\(N\) topology.
