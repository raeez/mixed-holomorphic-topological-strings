# Agent 189 Report: Equivariant CE/PV Refined Bracket

Worktree: `/Users/raeez/topological-strings`

Owned paths:

- `reconstitution/equivariant-ce-pv-refined-bracket-thread-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-189-equivariant-ce-pv-refined-bracket-0957.md`

## Claim Attacked

The equivariant CE/PV lane could be misstated in three ways:

1. use the old scalar Hamiltonian bracket away from
   \(\epsilon_1+\epsilon_2=0\);
2. assign the shifted-cotangent coordinate \(u_{a,b}\) the weight of the
   cotangent generator rather than the coordinate-dual weight;
3. import the non-equivariant CE/PV theorem without the
   \(\hbar_\omega\)-weighted differential and without the topology
   obstruction.

## Verdict

Valid attack.  The strongest stable core is the
\(\hbar_\omega\)-weighted coordinate CE/PV theorem recorded in
`reconstitution/equivariant-ce-pv-refined-bracket-thread-2026-04-30.md`.
No theorem files were edited.

The generator weights are:

\[
  w(c^{a,b})=w(\theta^{a,b})=-a\epsilon_1-b\epsilon_2,\qquad
  w(u_{a,b})=w(O_{a,b})=a\epsilon_1+b\epsilon_2.
\]

The refined bracket is:

\[
  [f,g]_\Omega=\hbar_\omega
  (\partial_{z_1}f\,\partial_{z_2}g
  -\partial_{z_2}f\,\partial_{z_1}g),
  \qquad w(\hbar_\omega)=\epsilon_1+\epsilon_2.
\]

The equivariant CE differential is:

\[
  d_{\mathrm{CE},\Omega}c^K
  =
  -\frac12\hbar_\omega C^K_{IJ}c^Ic^J,\qquad
  d_{\mathrm{CE},\Omega}u_K
  =
  \hbar_\omega C^L_{KJ}u_Lc^J.
\]

The PV side has
\[
  \pi_\Omega=\frac12\hbar_\omega C^K_{IJ}O_K\theta^I\theta^J,
\]
so
\[
  d_{\pi,\Omega}\theta^K
  =
  -\frac12\hbar_\omega C^K_{IJ}\theta^I\theta^J,\qquad
  d_{\pi,\Omega}O_K
  =
  \hbar_\omega C^L_{KJ}O_L\theta^J.
\]
Thus \(\Phi_\Omega d_{\mathrm{CE},\Omega}
=d_{\pi,\Omega}\Phi_\Omega\) on generators and hence on the completed
coordinate dg algebra.

## Evidence Anchors

- `local-dictionary.tex:484-543`: Hamiltonian/cotangent weights,
  self-dual bracket, refined bracket, and CE/PV generator rule.
- `theorem-lanes.tex:678-742`: finite cotangent CE/PV identity and
  generator differentials.
- `theorem-lanes.tex:785-850`: formal-disk coordinate completion and its
  topology boundary.
- `theorem-lanes.tex:922-950`: monomial CE/PV differential formulas.
- `theorem-lanes.tex:1000-1136`: coordinate formal-disk CE/PV theorem,
  bracket-admissible restriction, kernel-admissible restriction, and
  strict Casimir obstruction.
- `theorem-lanes.tex:1138-1230`: abstract bracket-compatible recognition
  criterion and summability hypotheses.
- `main.tex:3434-3543`: cochain-level reduced Hamiltonian CE/PV map.
- `main.tex:3670-3768`: low-degree monomial verification.
- `reconstitution/critique-refresh-2026-04-30-0957-ingestion-and-swarm-plan.md:85-100`:
  refreshed critique surface for refined bracket and equivariant CE/PV.
- `references/primary-sources/omega-stratified-source-anchors-2026-04-30.md:51-54`:
  source-audit obligation for the normal \(\Omega\)-complex and
  localization.

## Attack Ledger

```yaml
- id: A1-189-01
  severity: 2
  status: healed
  lens: equivariant Hamiltonian bracket
  target: refined bracket off the self-dual locus
  claim: The old scalar Poisson bracket is T_Omega-equivariant for all epsilon_1,epsilon_2.
  broken_step: The Poisson tensor has weight -epsilon_1-epsilon_2, so {H_I,H_J} has weight W_I+W_J-(epsilon_1+epsilon_2).
  evidence_type: direct_derivation
  evidence_ref: local-dictionary.tex:484-531; thread weight calculation
  confidence: high
  blast_radius: wrong CE differential weights, wrong PV bivector, wrong brane Moyal parameter
  minimal_heal: Use the line-valued bracket or the scalar bracket [f,g]_Omega=hbar_omega{f,g}.
  residual: none for coordinate dg algebra; bracketed completions still require ob_Omega_top and ob_Omega_br

- id: A1-189-02
  severity: 2
  status: healed
  lens: generator weights
  target: c,u,O,theta dictionary
  claim: The assignment c_ab->theta_ab and u_ab->O_ab is automatically equivariant.
  broken_step: It is equivariant only if c/theta have weight -W_ab and u/O have weight W_ab.
  evidence_type: direct_derivation
  evidence_ref: theorem-lanes.tex:792-830; local-dictionary.tex:484-493
  confidence: high
  blast_radius: non-equivariant CE/PV map and wrong boundary Hamiltonian weight
  minimal_heal: Record the coordinate-dual weights explicitly.
  residual: none for labels; topology remains separate

- id: A1-189-03
  severity: 2
  status: healed
  lens: equivariant CE differential
  target: d_CE c and d_CE u
  claim: The non-equivariant CE differential can be reused unchanged off epsilon_1+epsilon_2=0.
  broken_step: Without hbar_omega, d_CE c^K and d_CE u_K have the wrong T_Omega weight.
  evidence_type: direct_derivation
  evidence_ref: theorem-lanes.tex:922-950; thread equivariant formulas
  confidence: high
  blast_radius: d_CE no longer preserves weights and cannot define the equivariant coordinate dg algebra
  minimal_heal: Multiply the structure-constant terms in both c and u formulas by hbar_omega.
  residual: none for the coordinate formula

- id: A1-189-04
  severity: 2
  status: healed
  lens: Schouten/PV compatibility
  target: d_pi and Phi_Omega
  claim: The PV side needs a new independent proof unrelated to the CE formula.
  broken_step: The same hbar_omega-scaled structure constants define the invariant linear Poisson tensor pi_Omega.
  evidence_type: proof
  evidence_ref: theorem-lanes.tex:1073-1087; main.tex:3490-3536; thread PV calculation
  confidence: high
  blast_radius: duplicated or inconsistent CE/PV conventions
  minimal_heal: Define pi_Omega=(hbar_omega/2)C^K_IJ O_K theta^I theta^J and check generators.
  residual: global Schouten biderivation still requires a bracket-admissible completion

- id: A1-189-05
  severity: 2
  status: healed
  lens: self-dual specialization
  target: epsilon_1+epsilon_2=0 branch
  claim: One can invert epsilon_1+epsilon_2 and then specialize to the self-dual branch.
  broken_step: The self-dual branch is exactly where that character vanishes.
  evidence_type: obstruction
  evidence_ref: local-dictionary.tex:445-457 and 508-515
  confidence: high
  blast_radius: invalid localized coefficient ring and wrong fixed/resonant mode handling
  minimal_heal: Treat self-dual as a separate branch; hbar_omega has weight zero and may be kept or set to one.
  residual: compute zero-character resonant summands in any chosen normal window

- id: A1-189-06
  severity: 1
  status: non_core
  lens: theorem-surface firewall
  target: QME, kernel, and physical trace consequences
  claim: The equivariant CE/PV theorem proves kernel convergence, Costello QME, or physical large-N traces.
  broken_step: CE/PV weights give a coefficient algebra; they do not construct the mixed Cartan model, normal contraction, diagonal kernel convergence, counterterms, trace state, or Ward identities.
  evidence_type: proof_gap
  evidence_ref: local-dictionary.tex:607-624; references/primary-sources/omega-stratified-source-anchors-2026-04-30.md:42-59
  confidence: high
  blast_radius: false closure of the graph and trace theorem surfaces
  minimal_heal: Keep these as named obstructions outside the stable CE/PV core.
  residual: ob_Omega_Cartan, ob_Omega_top, ob_Omega_diag, ob_Omega_norm, ob_Omega_QME
```

## Files Changed

- Added `reconstitution/equivariant-ce-pv-refined-bracket-thread-2026-04-30.md`.
- Added `reconstitution/swarm-2026-04-30-agent-189-equivariant-ce-pv-refined-bracket-0957.md`.

No manuscript theorem file was edited.

## Verification

Context read:

- `CLAUDE.md`
- `AGENTS.md`
- attack-heal swarm protocol
- Chriss-Ginzburg rectification skill
- `reconstitution/critique-refresh-2026-04-30-0957-ingestion-and-swarm-plan.md`
- `local-dictionary.tex`
- `theorem-lanes.tex`
- `commands.tex`
- `mathmacros.tex`
- relevant `main.tex` CE/PV regions
- adjacent Omega reports from agents 177, 179, 183, 184, 185, and 186

Checks run after writing:

```bash
git diff --cached --check -- reconstitution/equivariant-ce-pv-refined-bracket-thread-2026-04-30.md reconstitution/swarm-2026-04-30-agent-189-equivariant-ce-pv-refined-bracket-0957.md
rg -n -F -e 'd_{\mathrm{CE},\Omega}' -e '\pi_\Omega' -e 'w(c^{a,b})' -e 'Self-Dual Specialization' -e 'Ob}_{\Omega,\mathrm{CE/PV}}' reconstitution/equivariant-ce-pv-refined-bracket-thread-2026-04-30.md reconstitution/swarm-2026-04-30-agent-189-equivariant-ce-pv-refined-bracket-0957.md
```

No PDF build is needed for this report-only lane in a concurrent swarm
workspace.

Results:

- Staged `git diff --cached --check` passed.
- Targeted `rg` found the equivariant CE differential,
  \(\pi_\Omega\), generator weights, self-dual specialization, and
  obstruction vector in the owned reports.

## Remaining Obligations

- Construct the mixed \(T_\Omega\)-Cartan/basic coefficient model.
- Choose a weighted completion where \(d_{\mathrm{CE},\Omega}\),
  \(d_{\pi,\Omega}\), multiplication, and the refined cotangent/Schouten
  bracket are continuous.
- Prove diagonal kernel convergence in that completion.
- Compute resonant summands under self-dual or numeric equivariant
  specializations.
- Choose or compare residue and Euler normalizations.
- Keep Costello QME and physical large-\(N\) trace claims outside this
  CE/PV stable core until their obstruction complexes vanish.
