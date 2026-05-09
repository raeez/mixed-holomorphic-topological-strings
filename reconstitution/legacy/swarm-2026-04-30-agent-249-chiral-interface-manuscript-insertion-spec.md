# Swarm Report: Agent 249, Chiral Interface Manuscript Insertion Spec

Date: 2026-04-30.

Owned files:

- `reconstitution/chiral-interface-manuscript-insertion-spec-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-249-chiral-interface-manuscript-insertion-spec.md`

No TeX, script, source, or Vol II file was edited.

## Claim Attacked

Target: turn Agent 243's constructed chiral algebra interface tuple into a
precise manuscript insertion spec without either false move:

- false-native import: replacing the native \(\C^2\) holomorphic
  \(E_2\)/factorization algebra by a curve chiral algebra;
- false-external downgrade: treating the constructed chiral algebra as a
  citation rather than a local reduced theorem target.

## Evidence Read

- Repo rules: `CLAUDE.md`, `AGENTS.md`, `commands.tex`,
  `mathmacros.tex`, `notation.tex`, `preamble.tex`.
- Ecosystem rules and skill: `~/ecosystem/INVARIANTS.md`,
  `~/ecosystem/AGENTS-HARNESS.md`, attack-heal skill and protocol.
- Vol II rectification discipline:
  `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- Agent 243 reports:
  `reconstitution/constructed-chiral-algebra-interface-integration-target-2026-04-30.md`,
  `reconstitution/swarm-2026-04-30-agent-243-constructed-chiral-algebra-interface-integration-target.md`.
- Chiral/reduction reports:
  `reconstitution/chiral-algebra-construction-thread-2026-04-30.md`,
  `reconstitution/native-E2-factorization-construction-2026-04-30.md`,
  `reconstitution/controlled-CxR-reduction-thread-2026-04-30.md`,
  `reconstitution/reduced-dirac-brst-zhu-thread-2026-04-30.md`,
  `reconstitution/native-cxr-voa-zhu-reduction-construction-target-2026-04-30.md`,
  and Agent 228's summary report.
- Manuscript anchors:
  `main.tex:530-610`, `main.tex:1111-1529`,
  `main.tex:6379-6473`, `main.tex:6934-6987`,
  `main.tex:7744-8020`,
  `theorem-lanes.tex:227-1025`,
  `local-dictionary.tex:170-374`,
  `claim-strength-ledger.tex:312-331`,
  `claim-strength-ledger.tex:524-592`,
  `open-obligations.tex:140-247`,
  `open-obligations.tex:281-395`.
- Vol II controls:
  `chapters/connections/concordance.tex:12-19`,
  `chapters/theory/sc_chtop_heptagon.tex:218-265`,
  `chapters/connections/hochschild.tex:392-410`,
  `chapters/connections/hochschild.tex:674-782`,
  `notes/first_principles_cache.md:98-106`.

## Stable Core

The stable core is the tuple
\[
  \mathfrak I_{\mathrm{ch}}
  =
  (\mathcal R_{\C\times\R},
   \mathcal F_{\mathrm{red}},
   V_{\mathrm{red}},
   Q_{\mathrm{BRST}},
   \mathbf 1,T,Y,
   \operatorname{wt},
   \zeta_\hbar,
   H_{\mathrm{anom}}).
\]

Its source is the native two-complex-dimensional factorization algebra
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \bigl(\Omega_c^{0,\bullet}(B)\widehat\otimes
  (\mathfrak h\ltimes\mathcal P[1])\bigr),
  \qquad
  \mathfrak h=\C[[z_1,z_2]]/\C\cdot1.
\]

The reduced coefficient system is
\[
  \mathfrak h_{\mathrm{red}}=\C[[z_1]][[z_2]]/\C\cdot1,\qquad
  \mathcal P_{\mathrm{red}}
  =
  \operatorname{Ann}_{\mathrm{res}}(\C\cdot1)
  \subset H^2_{(z_1,z_2)}(\C[[z_1,z_2]])\,dz_1dz_2.
\]
The bracket remains
\[
  \{f,g\}_{\mathrm{red}}
  =
  \partial_{z_1}f\,\partial_{z_2}g
  -
  \partial_{z_2}f\,\partial_{z_1}g .
\]

Thus \(z_2=0\) and the \(b=0\) principal-part residue line are both
destroyed claims, not reductions.  The \(b=0\) line fails because
\[
  z_1\cdot\rho_{a,0}=-\rho_{a,1}.
\]

## Valid Attacks

```yaml
- id: A249-01
  severity: 1
  status: healed
  lens: native geometry
  claim: The constructed chiral algebra can be stated as the native object.
  broken_step: The native object is a holomorphic factorization algebra on C^2 polydisks; a vertex algebra is a curve object.
  evidence_ref: "main.tex:1111-1240; theorem-lanes.tex:227-696; local-dictionary.tex:170-374"
  minimal_heal: Make the chiral algebra V_red inside I_ch after R_{C x R}.
  residual: Reduction and vertex data remain construction targets.

- id: A249-02
  severity: 1
  status: healed
  lens: supremum discipline
  claim: The chiral algebra should be quarantined as an external reference.
  broken_step: Agent 243 constructed a local interface tuple; demoting it loses theorem data rather than naming the exact obstruction.
  evidence_ref: "reconstitution/constructed-chiral-algebra-interface-integration-target-2026-04-30.md"
  minimal_heal: Specify I_ch, V_red, Q_BRST, weights, zeta_hbar, and Ob_{I_ch} as manuscript theorem data.
  residual: Each obstruction component must be closed or hypothesized in TeX.

- id: A249-03
  severity: 1
  status: healed
  lens: retained modes
  claim: The C x R reduction can set z2=0.
  broken_step: This kills partial_{z2}, hence the Hamiltonian bracket, Moyal bivector, scalar class, and second Weyl matrix.
  evidence_ref: "theorem-lanes.tex:746-854; Agent 228 target lines 119-192"
  minimal_heal: Retain h_red=C[[z1]][[z2]]/C and P_red.
  residual: Analytic z2-fiber pushforward remains open.

- id: A249-04
  severity: 1
  status: healed
  lens: principal parts
  claim: A one-variable b=0 residue line is enough.
  broken_step: The line is not stable under the Hamiltonian coadjoint action.
  evidence_ref: "theorem-lanes.tex:850-854; open-obligations.tex:186-204; claim-strength-ledger.tex:967-990"
  minimal_heal: Keep the full two-index Matlis principal-part module.
  residual: None for the algebraic coefficient target.

- id: A249-05
  severity: 1
  status: healed
  lens: factorization-to-vertex
  claim: Reduced factorization automatically supplies a vertex algebra.
  broken_step: A vertex algebra needs finite Laurent singularities, vacuum, translation, locality, and weights.
  evidence_ref: "theorem-lanes.tex:638-676; theorem-lanes.tex:893-1024"
  minimal_heal: Add Ob_vert and make V_red part of the theorem target.
  residual: ob_FV, ob_Laurent, ob_loc, ob_wt, ob_BRST.

- id: A249-06
  severity: 1
  status: healed
  lens: Zhu and Moyal
  claim: Zhu automatically realizes the Weyl/Moyal brane algebra.
  broken_step: Zhu needs weights and zero-mode conventions; multiplicativity and Capelli shift are separate data.
  evidence_ref: "theorem-lanes.tex:950-995; Vol II hochschild.tex:687-752"
  minimal_heal: Add zeta_hbar and Ob_Zhu with zero-mode, multiplicativity, Capelli, and HKR components.
  residual: ob_zero, ob_Zhu^mult, ob_Capelli, ob_HKR.

- id: A249-07
  severity: 2
  status: healed
  lens: Vol II control
  claim: Vol II constructs the interface by itself.
  broken_step: Vol II supplies SC^{ch,top} and Zhu grammar after a reduced vertex algebra exists; it does not construct pi_!, retained z2 modes, anomaly transport, or native-source compatibility.
  evidence_ref: "Vol II concordance.tex:12-19; sc_chtop_heptagon.tex:218-265; hochschild.tex:392-410,674-782"
  minimal_heal: Use Vol II as a control surface only after R_{C x R} and V_red.
  residual: Source fixtures and finiteness hypotheses for any Vol II bridge.
```

## Repairs Made

The companion spec file records:

- exact theorem-lane insertion after `thm:lane-reduced-dirac-brst-zhu`;
- exact dictionary row after the Weyl/Moyal compatibility row;
- exact claim-ledger failed-surface replacement and supremum-controller row;
- exact open-obligations row for
  \(\operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}\);
- exact main-text remark after `prop:native-darboux-theorem-package`;
- full obstruction vector
  \[
    \operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}
    =
    (\operatorname{Ob}_{\mathrm{red}},
     \operatorname{Ob}_{\mathrm{vert}},
     \operatorname{Ob}_{\mathrm{Zhu}},
     \operatorname{Ob}_{\mathrm{nat}}).
  \]

## Files Changed And Staged

- Added `reconstitution/chiral-interface-manuscript-insertion-spec-2026-04-30.md`.
- Added `reconstitution/swarm-2026-04-30-agent-249-chiral-interface-manuscript-insertion-spec.md`.

These are the only paths staged by this pass.  Pre-existing concurrent
staged paths were not modified.

## Verification

Read-only checks used `rg`, `sed`, `nl -ba`, and `git status --short`
over the requested TeX files, Agent 243 reports, chiral reports, and
Vol II controls.  No TeX build is needed because the pass creates
report-only Markdown artifacts.

Post-write checks run in this pass:

```bash
git diff --check -- reconstitution/chiral-interface-manuscript-insertion-spec-2026-04-30.md reconstitution/swarm-2026-04-30-agent-249-chiral-interface-manuscript-insertion-spec.md
rg -n -F -e 'mathfrak I_{\\mathrm{ch}}' -e 'operatorname{Ob}_{\\mathfrak I_{\\mathrm{ch}}}' -e 'z_1\\cdot\\rho_{a,0}=-\\rho_{a,1}' reconstitution/chiral-interface-manuscript-insertion-spec-2026-04-30.md reconstitution/swarm-2026-04-30-agent-249-chiral-interface-manuscript-insertion-spec.md
LC_ALL=C grep -n '[^ -~]' reconstitution/chiral-interface-manuscript-insertion-spec-2026-04-30.md reconstitution/swarm-2026-04-30-agent-249-chiral-interface-manuscript-insertion-spec.md || true
```
