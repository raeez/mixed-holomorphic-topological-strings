# Agent 143 - Local BV/QME Geometry Audit

Status: patched owned appendix surface; no commits or pushes.

## Stable core

The unreduced BV/QME appendix is now explicitly formal-local on
\[
  \mathbb R^2_{\mathrm{top}}\times\widehat{\mathbb C^2}_0,
  \qquad
  \Omega_{\mathrm{loc}}=dz_1\wedge dz_2 .
\]
The scalar-shadow calculation uses exactly the local Hamiltonian Poisson
bracket, the divergence-free Hamiltonian vector fields for
\(\Omega_{\mathrm{loc}}\), and the open Chan--Paton trace/supertrace
loop.  No compact Calabi--Yau target, global BCOV theorem, CoHA, quintic,
OSV/GV, Abel--Jacobi, Igusa, Borcherds, or BKM input enters the appendix.

## Valid attacks

```yaml
- id: A1-143-01
  severity: 1
  status: healed
  lens: local geometry underdefinition
  target: appendix-unreduced-bv-qme.tex, scalar-contact and scalar-shadow formulas
  claim: The scalar cocycle \(\omega(f,g)\) can be used without recording the local geometric source.
  broken_step: The appendix did not say where \(\Omega_{\mathrm{loc}}\), the Hamiltonian bracket, or divergence-free condition enter the scalar-shadow computation.
  evidence_type: proof_gap
  evidence_ref: prop:app-local-geometry-scalar-shadow
  minimal_heal: Add the local geometry proposition and define \(\omega(f,g)=[\{f,g\}_{\Omega_{\mathrm{loc}}}]_0\).
  residual: None for the scalar-contact shadow.

- id: A1-143-02
  severity: 2
  status: healed
  lens: supertrace cancellation habitat
  target: thm:app-balanced-supertrace-qme-cancellation and balanced habitat definitions
  claim: Balanced supertrace cancellation is an abstract trace identity detached from the local mixed HT model.
  broken_step: The cancellation is the product of the local scalar cocycle and \(\operatorname{sdim}\mathbb C^{N|N}\), not a global QME theorem.
  evidence_type: line_reference
  evidence_ref: prop:app-local-geometry-scalar-shadow; thm:app-balanced-supertrace-qme-cancellation
  minimal_heal: State the theorem and habitats over the formal-local model and \(I\subset\mathbb R_{\mathrm{brane}}\).
  residual: Non-scalar Costello graph classes remain outside the scalar projection.

- id: A1-143-03
  severity: 2
  status: healed
  lens: finite-window overreach
  target: finite-window and marked graph surfaces
  claim: Finite-window marked graph statements might be read as all-graph or compact-target Costello statements.
  broken_step: The finite window only restricts local Hamiltonian labels, graph labels, and counterterm tables.
  evidence_type: unsupported
  evidence_ref: def:app-balanced-costello-graph-subhabitat; def:app-finite-window-marked-costello-list; thm:app-full-equivariant-marked-shadow-vanishing
  minimal_heal: Thread "formal-local mixed HT" and "local finite-window" through the affected definitions and theorems; state that no all-topology, compact-target, or global BCOV datum is assumed.
  residual: Concrete Costello specializations must still supply finite graph tables and boundary signs.

- id: A1-143-04
  severity: 1
  status: healed
  lens: compact-CY firewall
  target: appendix opening and full-equivariant marked theorem
  claim: Compact CY/CoHA/quintic/OSV/GV/Abel-Jacobi/Igusa/BKM comparison language could leak into the local theorem surface.
  broken_step: The appendix had no local firewall at the point where scalar and graph claims start.
  evidence_type: missing_source
  evidence_ref: appendix opening lines after patch
  minimal_heal: Add explicit quarantine language and make the marked theorem exclude compact target/global BCOV data from its hypotheses.
  residual: Other files remain the integration owner's firewall surface.
```

## Repairs made

- Added `prop:app-local-geometry-scalar-shadow`.
- Renamed the scalar contact theorem heading to local scalar contact QME obstruction and tied \(\omega\) to \(\Omega_{\mathrm{loc}}\).
- Repaired `lem:app-unreduced-scalar-primitive` to use the local Hamiltonian bracket.
- Localized the balanced supertrace theorem, balanced scalar-contact habitat, balanced Costello graph subhabitat, first marked scalar-loop proposition, supertraceless-monodromy prehabitat, finite-window marked Costello list, finite-window marked habitat compatibility, full-equivariant marked scalar-shadow theorem, and ordinary scalar-reduced obstruction criterion.

## Exact formulas

\[
  \Omega_{\mathrm{loc}}=dz_1\wedge dz_2,\qquad
  \{f,g\}_{\Omega_{\mathrm{loc}}}
    =
  \partial_{z_1}f\,\partial_{z_2}g
    -
  \partial_{z_2}f\,\partial_{z_1}g .
\]
\[
  \iota_{X_f}\Omega_{\mathrm{loc}}=-df,\qquad
  X_f=(\partial_{z_1}f)\partial_{z_2}
      -(\partial_{z_2}f)\partial_{z_1},\qquad
  \operatorname{div}_{\Omega_{\mathrm{loc}}}X_f=0 .
\]
\[
  \omega(f,g)=[\{f,g\}_{\Omega_{\mathrm{loc}}}]_0,\qquad
  \omega(z_1,z_2)=1 .
\]
\[
  \text{ordinary scalar shadow: }\quad
  \hbar N\,\omega(f,g)\gamma_{\mathbf 1}.
\]
\[
  \text{balanced supertrace shadow: }\quad
  \hbar\,\operatorname{sdim}(\mathbb C^{N|N})
  \omega(f,g)\gamma_{\mathbf 1}=0 .
\]
\[
  \text{marked scalar-loop shadow: }\quad
  \hbar\,\operatorname{Str}_{\mathrm{cyc}}(\mathfrak m)
  \omega(f,g)\gamma_{\mathbf 1}.
\]

## Verification

Commands run:

```bash
sed -n '1,240p' /Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,260p' ./CLAUDE.md
sed -n '1,260p' appendix-unreduced-bv-qme.tex
sed -n '261,620p' appendix-unreduced-bv-qme.tex
sed -n '621,1040p' appendix-unreduced-bv-qme.tex
sed -n '1041,1460p' appendix-unreduced-bv-qme.tex
sed -n '1461,1880p' appendix-unreduced-bv-qme.tex
sed -n '1881,2300p' appendix-unreduced-bv-qme.tex
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-129-marked-graph-differential.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-134-costello-finite-window-graph-list.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-137-local-unimodularity-dictionary.md
rg -n -e 'compact Calabi' -e 'global BCOV' -e 'CoHA' -e 'quintic' -e 'OSV/GV' -e 'Abel--Jacobi' -e 'Igusa' -e 'BKM' appendix-unreduced-bv-qme.tex
rg -n -e 'Local geometry of scalar shadows' -e 'Omega_\{\\mathrm\{loc\}\}' -e 'div_\{\\Omega' -e 'formal-local mixed HT' -e 'finite-window graph/QME package for the local' -e 'Local scalar contact QME obstruction' appendix-unreduced-bv-qme.tex
git diff --check -- appendix-unreduced-bv-qme.tex
chktex -q appendix-unreduced-bv-qme.tex
```

Results:

- `git diff --check` passed.
- The compact/global scan returns only the two explicit quarantine lines now added to the appendix.
- The local-geometry scan finds the new proposition, \(\Omega_{\mathrm{loc}}\), divergence-free statement, and localized finite-window/marked surfaces.
- `chktex` returned its existing warning class plus warnings on the new displayed formulas and quarantine dashes; no TeX parse crash was observed.
- No full `make pdf` was run. The build writes tracked output outside this agent's writable surface, and Agent 137 already recorded an out-of-scope `main.tex:5103` build blocker in the shared checkout.

## Files changed and staged

Changed:

- `appendix-unreduced-bv-qme.tex`
- `reconstitution/swarm-2026-04-30-agent-143-local-bv-qme-geometry-audit.md`

Staged after scoped verification:

- `appendix-unreduced-bv-qme.tex`
- `reconstitution/swarm-2026-04-30-agent-143-local-bv-qme-geometry-audit.md`

## Remaining obligations

- Supply concrete finite-window Costello graph tables, boundary signs, marker transports, and counterterm faces for any larger specialization.
- Solve non-scalar QME classes in the kernel of the zero scalar projection; this audit only closes the scalar-shadow local-geometry surface.
- Keep the compact-CY/global comparison firewall active in other manuscript files.
