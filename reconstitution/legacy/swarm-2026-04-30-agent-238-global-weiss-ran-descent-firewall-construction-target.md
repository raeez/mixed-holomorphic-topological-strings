# Agent 238 - Global Weiss/Ran Descent Firewall Construction Target

Status: report-only attack-heal construction target.

Owned writable files:

- `reconstitution/global-weiss-ran-descent-firewall-construction-target-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-238-global-weiss-ran-descent-firewall-construction-target.md`

No TeX, manuscript, script, or Vol II file was edited.

## Stable Core

The local theorem surface remains formal-local on
\[
  \mathbb R^2_{\mathrm{top}}\times\widehat{\mathbb C^2}_{0,\mathrm{hol}},
  \qquad
  L=\mathbb R_{\mathrm{brane}}\times\{0\}\times\{0\}.
\]
The native factorization object is
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \left(
    \Omega_c^{0,\bullet}(B)\widehat\otimes
    (\mathfrak h\ltimes\mathcal P[1])
  \right),
  \quad
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1.
\]
The mixed product-open enhancement and reduced brane-line
principal-part current \(P_0\) algebra are native.  A global
factorization-center morphism, arbitrary Weiss/Ran descent,
stratified brane factorization, compact CY/BCOV transfer, CoHA/BKM/Igusa
transfer, and curve VOA/Zhu transfer are not native.

The strongest true theorem target is recorded in
`reconstitution/global-weiss-ran-descent-firewall-construction-target-2026-04-30.md`.
Its acceptance class is
\[
  \operatorname{Ob}_{\mathrm{UKD}}(\mathfrak C_{\mathrm{tar}})
  =
  \left(
    \operatorname{Ob}_{\mathfrak C_{\mathrm{tar}}},
    [d\Theta_{\mathrm{KD}}+\tfrac12[\Theta_{\mathrm{KD}},\Theta_{\mathrm{KD}}]]
  \right).
\]
The theorem is positive only when this class vanishes with compatible
null-homotopies.  Otherwise the first nonzero component is the exact
obstruction theorem.

## Attack Ledger

```yaml
- id: A1-238-01
  severity: 1
  status: healed
  lens: Beilinson descent
  target: global factorization-center morphism
  claim: Stalkwise formal Darboux maps glue to a global factorization-center morphism.
  broken_step: A local formal disk map does not carry source comparison, cotangent boundary realization, P0-center homotopies, Weiss/Ran cocycles, or hyperdescent.
  evidence_type: line_reference
  evidence_ref: main.tex:4168-4172; main.tex:4231-4247; tate-P5-cross-volume.tex:153-188
  files_read: [main.tex, tate-P5-cross-volume.tex, open-obligations.tex, claim-strength-ledger.tex]
  tools_used: [rg, nl, sed]
  confidence: high
  blast_radius: false global closed-open map and false external comparison surface
  minimal_heal: require the Weiss/Ran total complex and obstruction tower
  residual: construct the global descent datum or identify the first nonzero WR class
  deciding_evidence: vanishing of ob_WR^(1) and all ob_WR^(r) with compatible null-homotopies

- id: A1-238-02
  severity: 1
  status: healed
  lens: Hamiltonian period
  target: compact holomorphic symplectic globalization
  claim: Locally Hamiltonian symplectic vector fields on compact holomorphic symplectic surfaces globalize as Hamiltonian fields.
  broken_step: The local primitives glue only when per_X(v)=delta(-i_v omega) vanishes; on compact connected X this forces v=0.
  evidence_type: derivation
  evidence_ref: tate-P5-cross-volume.tex:131-151; tate-P5-cross-volume.tex:260-284
  files_read: [tate-P5-cross-volume.tex, local-dictionary.tex]
  tools_used: [nl, sed]
  confidence: high
  blast_radius: importing compact global symmetry from formal Darboux data
  minimal_heal: make per_X(v) a first obstruction component
  residual: noncompact, meromorphic, or twisted targets require a new period complex
  deciding_evidence: explicit target period complex and zero period class

- id: A1-238-03
  severity: 1
  status: healed
  lens: product site versus arbitrary Ran
  target: mixed product-disk factorization
  claim: Product-disk mixed factorization on Ran_prod(M,Y) gives ordinary Ran(M x Y) descent.
  broken_step: The manuscript explicitly does not assert cofinality of product-disk covers inside arbitrary Weiss covers.
  evidence_type: line_reference
  evidence_ref: tate-P5-cross-volume.tex:428-435
  files_read: [tate-P5-cross-volume.tex]
  tools_used: [nl, sed]
  confidence: high
  blast_radius: false arbitrary Weiss/Ran descent
  minimal_heal: require ob_WR, ob_hyp, and null-homotopies for arbitrary covers
  residual: prove product-disk cofinality or construct the ordinary Ran descent object
  deciding_evidence: cofinality theorem or direct hyperdescent proof

- id: A1-238-04
  severity: 1
  status: healed
  lens: stratified brane factorization
  target: brane-localized factorization on (X,L)
  claim: Reduced brane current brackets supply the stratified brane factorization theorem.
  broken_step: Reduced brackets do not supply collar modules, products, Weiss descent, product centrality homotopies, P0 centrality homotopies, or brane-defect QME curvature.
  evidence_type: proof_gap
  evidence_ref: open-obligations.tex:757-888; theorem-lanes.tex:2935-2963; claim-strength-ledger.tex:619-640
  files_read: [open-obligations.tex, theorem-lanes.tex, claim-strength-ledger.tex]
  tools_used: [nl, sed]
  confidence: high
  blast_radius: false stratified factorization and false physical trace-state claims
  minimal_heal: keep Ob_str,Omega,N as the top obstruction vector
  residual: construct F_str, collar module, centrality homotopies, and QME kernel
  deciding_evidence: delta_Weiss=0 plus centrality and QME primitives in the stratified object

- id: A1-238-05
  severity: 1
  status: healed
  lens: external comparison firewall
  target: compact CY, CoHA, BKM, Igusa, Vol III, MNOP, BCOV
  claim: The local Hamiltonian BF/Moyal theorem supports compact/global or sibling-volume consequences.
  broken_step: The local convention base lacks compact topology, negative-cyclic CY class, Hall orientation, Weyl chamber, global BV propagator, holomorphic anomaly equation, and target comparison maps.
  evidence_type: line_reference
  evidence_ref: local-dictionary.tex:151-166; main.tex:8796-8818; claim-strength-ledger.tex:1094-1117; open-obligations.tex:1083-1122
  files_read: [local-dictionary.tex, main.tex, claim-strength-ledger.tex, open-obligations.tex, tate-P5-cross-volume.tex]
  tools_used: [rg, nl, sed]
  confidence: high
  blast_radius: false compact CY3, CoHA, BKM, or global BCOV theorem
  minimal_heal: require C_tar, Ob_Ctar, Ob_UKD, comparison morphisms, and null-homotopies
  residual: target-specific compact/CoHA/BKM source fixtures
  deciding_evidence: a matched-conventions theorem for the named target

- id: A1-238-06
  severity: 1
  status: healed
  lens: curve and Vol II control surface
  target: VOA, Zhu, and C x R reduction
  claim: A curve VOA/Zhu theorem or Vol II C x R apparatus is native to the topological-strings local model.
  broken_step: The native object is on C^2; a curve theorem requires a chosen reduction, retained z2-mode or principal-part system, pushforward, bracket, BV pairing, brane image, and anomaly transport.
  evidence_type: line_reference
  evidence_ref: AGENTS.md; local-dictionary.tex:290-365; claim-strength-ledger.tex:513-546
  files_read: [AGENTS.md, local-dictionary.tex, claim-strength-ledger.tex, reconstitution/native-cxr-voa-zhu-reduction-construction-target-2026-04-30.md]
  tools_used: [rg, nl, sed]
  confidence: high
  blast_radius: false one-dimensional chiral algebra in the native C^2 theorem surface
  minimal_heal: quarantine VOA/Zhu claims behind the controlled C x R reduction datum
  residual: construct the reduction and factorization-to-vertex package
  deciding_evidence: R_{C x R} plus finite-pole OPE and Zhu/zero-mode map

- id: A1-238-07
  severity: 2
  status: healed
  lens: CoHA/BKM antipatterns
  target: cross-volume analogies used as proof support
  claim: Finite Rees Hall gluing, CoHA(C^3), character equalities, or BKM constants close the compact comparison.
  broken_step: Vol II antipatterns separate finite Rees, completed Rees, realized compact critical CoHA, positive half, double, representation, vertex algebra, and BKM denominator scopes.
  evidence_type: control_surface
  evidence_ref: /Users/raeez/chiral-bar-cobar-vol2/notes/antipatterns_catalogue.md:9860-9892; :9986-9992; :10110-10117
  files_read: [/Users/raeez/chiral-bar-cobar-vol2/notes/antipatterns_catalogue.md]
  tools_used: [rg, nl, sed]
  confidence: high
  blast_radius: false source theorem imported from sibling volumes
  minimal_heal: make every cross-volume use target-data dependent
  residual: none inside topological-strings core; sibling targets need their own theorem data
  deciding_evidence: not applicable for the local report
```

## Healed Construction Target

The positive target is a matched-conventions theorem datum
\[
\mathfrak C_{\mathrm{tar}}
=
(d,Y,\eta,(\Sigma_{d-1},C),L,\tau,\lambda,\mathfrak f,\Lambda,
\hbar_{\mathrm{tar}},\mathcal O_{\mathrm{tar}},
\chi_{\mathrm{cl}},\chi_{\mathrm{op}},\chi_{\mathrm{anom}},
\mathcal K_{\mathrm{obs}},\mathfrak K_{\mathrm{KD}},\Theta_{\mathrm{KD}})
\]
with formal restriction
\[
  \chi_{\mathrm{op}}^{-1}
  \Phi^{\mathrm{Ham}}_{\mathrm{fact}}
  \chi_{\mathrm{cl}}.
\]
It must supply:

1. period classes and their null-homotopies;
2. the Weiss/Ran total complex and all descent primitives;
3. anomaly matching to \([\bar c]\);
4. cotangent boundary realization;
5. product and \(P_0\)-centrality homotopies;
6. brane-defect QME curvature cancellation;
7. convergence and no hidden \(\varprojlim^1\);
8. mixed six-relation and mixed-Dunn data when asserted;
9. Vol III, Igusa/BKM, compact-CY, CoHA, or VOA target components only
   when those structures are part of the target theorem.

Failure gives the exact obstruction theorem naming the first nonzero
component of
\[
  (
  \operatorname{per}_{\mathrm{tar}},
  \operatorname{ob}_{\mathrm{WR}},
  \operatorname{ob}_{\mathrm{anom}},
  \operatorname{ob}_{\mathrm{QME}},
  \operatorname{ob}_{\mathrm{conv}},
  \operatorname{ob}_{\mathrm{hyp}},
  \operatorname{ob}_{\mathrm{VolIII}},
  \operatorname{ob}_{\mathrm{Igusa/BKM}},
  \operatorname{ob}_{6r},
  \operatorname{ob}_{\mathrm{MD}},
  [d\Theta_{\mathrm{KD}}+\tfrac12[\Theta_{\mathrm{KD}},\Theta_{\mathrm{KD}}]]
  ).
\]

## Files Changed

- `reconstitution/global-weiss-ran-descent-firewall-construction-target-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-238-global-weiss-ran-descent-firewall-construction-target.md`

## Verification

Read:

- `CLAUDE.md`
- `AGENTS.md`
- `/Users/raeez/ecosystem/INVARIANTS.md`
- `/Users/raeez/ecosystem/AGENTS-HARNESS.md`
- `/Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md`
- `/Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md`
- `/Users/raeez/ecosystem/skills/shared/attack-heal-swarm/lens-library.md`
- `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `/Users/raeez/chiral-bar-cobar-vol2/notes/antipatterns_catalogue.md`
- `/Users/raeez/chiral-bar-cobar-vol2/notes/vol1_imported_antipatterns_catalogue_2026_04_30.md`
- `main.tex`
- `theorem-lanes.tex`
- `open-obligations.tex`
- `claim-strength-ledger.tex`
- `local-dictionary.tex`
- `principles.tex`
- `mathmacros.tex`
- `commands.tex`
- `tate-P5-cross-volume.tex`
- prior relevant reports: agent 012, agent 228, agent 234, native E2 report.

Commands:

```bash
git status --short
rg -n "Weiss|Ran|descent|firewall|matched-conventions|compact|CoHA|BKM|VOA|Vol III" main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex principles.tex tate-P5-cross-volume.tex
nl -ba main.tex | sed -n '4118,4247p'
nl -ba main.tex | sed -n '8790,8830p'
nl -ba tate-P5-cross-volume.tex | sed -n '153,415p'
nl -ba tate-P5-cross-volume.tex | sed -n '428,566p'
nl -ba open-obligations.tex | sed -n '757,888p'
nl -ba open-obligations.tex | sed -n '1083,1122p'
nl -ba claim-strength-ledger.tex | sed -n '481,546p'
nl -ba claim-strength-ledger.tex | sed -n '619,640p'
nl -ba local-dictionary.tex | sed -n '13,166p'
nl -ba local-dictionary.tex | sed -n '189,365p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/notes/antipatterns_catalogue.md | sed -n '9860,9892p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/notes/antipatterns_catalogue.md | sed -n '9980,10005p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/notes/antipatterns_catalogue.md | sed -n '10106,10124p'
```

The requested `cache` path under
`/Users/raeez/chiral-bar-cobar-vol2/cache` was absent; the available
Vol II `notes/` antipattern catalogues were inspected for control-surface
consistency and not edited.
