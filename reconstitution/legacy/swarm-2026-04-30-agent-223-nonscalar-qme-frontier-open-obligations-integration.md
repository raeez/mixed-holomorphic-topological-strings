# Agent 223 - Non-Scalar QME Frontier Open Obligations Integration

Status: implemented in `open-obligations.tex`; this report records the
owned integration.

## Stable Core

Agent 220's report is now reflected in the obligation ledger as a construction
frontier, not as a habitat slogan.  The stable statement is:

- the componentwise Moyal/current surface is theorem data;
- the non-scalar Costello/QME theorem starts only after marked graph rows,
  completed local-functional and Hom complexes, scalar-contact projection,
  current bulk-to-defect kernel, finite-window row equations, and Roos
  compatibilities are supplied;
- the `\theta_3` one-row obstruction remains active until a CE ancestor, local
  counterterm primitive, or complete companion-face table supplies the required
  differential and transport data;
- the normal `\Omega` branch remains a habitat plus centrality/basicness
  obligation, not a QME proof.

## Open-Obligations Anchors

- `open-obligations.tex:342`: constructive non-scalar Costello/QME problem.
- `open-obligations.tex:344`: codimension-two closed marked Costello list.
- `open-obligations.tex:352`: completed local-functional complex.
- `open-obligations.tex:366`: Hom-valued kernel complex and curvature.
- `open-obligations.tex:385`: current-valued bulk-to-defect kernel and
  zero-edge values.
- `open-obligations.tex:413`: filtered scalar-contact chain projection.
- `open-obligations.tex:436`: mandatory marked row formulas.
- `open-obligations.tex:464`: finite-window row equation `A^M c=-r^M`.
- `open-obligations.tex:478`: truncation and Roos compatibility.
- `open-obligations.tex:587`: preserved `\theta_3` one-row gate.
- `open-obligations.tex:609`: standardized source face `\zeta_{M,\nu_3}`.
- `open-obligations.tex:689`: Agent 210 Omega coefficient ring preserved.
- `open-obligations.tex:746`: separate `\hbar_{\mathrm{QME}}`,
  `\hbar_{\mathrm{W}}`, and `\hbar_\omega` gate preserved.
- `open-obligations.tex:802`: centrality Hom-curvature row.
- `open-obligations.tex:841`: normal `\Omega` centrality row and basic
  primitive obstruction.

## Attack-Heal Items

- `A223-01`: Habitat-only non-scalar QME language was too weak.  Healed by
  requiring marked graph rows, completed Hom complex, and actual kernel
  weights before curvature vanishing is meaningful.
- `A223-02`: Scalar-symbol vanishing did not form the non-scalar complex.
  Healed by making the filtered chain projection and
  `o_{\sigma,w}^{(r)}` tower the first gate.
- `A223-03`: Fixed-window exactness could be mistaken for all-window QME.
  Healed by displaying `A^M c=-r^M`, cokernel certificates, transport
  identities, and the Roos primitive class.
- `A223-04`: Centrality was too implicit.  Healed by adding the marked
  Hom-curvature row, primitive equation, finite-window compatibility, and
  `Q_\Omega` basicness obstruction.
- `A223-05`: The `\theta_3` and Omega repairs could have been overwritten.
  They were preserved; no cancellation is claimed without the listed
  differential data.

## Checks

Passed:

```bash
git diff --check -- open-obligations.tex
rg -n -F -e 'constructive non-scalar' -e 'codimension-two closed marked Costello list' -e 'mathbf K^\bullet' -e 'A^Mc=-r^M' -e 'u^{M,N}' -e 'R^{\mathrm{cent}}_{x,y,M}' -e 'L_{V_\Omega}H^\Omega' -e '\zeta_{M,\nu_3}' open-obligations.tex
rg -n -F -e '\varepsilon_s' -e '\varepsilon_1' -e '\varepsilon_2' -e '\operatorname{Ch}_{\C((\epsilon_s,\epsilon_1,\epsilon_2))[[\hbar]]}' -e '\operatorname{Ch}_{\C((\varepsilon_s,\varepsilon_1,\varepsilon_2))[[\hbar]]}' -e '(\varepsilon_s\varepsilon_1\varepsilon_2)^{-1}' -e 'Weyl}_\hbar' -e 'P_{0,\hbar}' open-obligations.tex || true
rg -n -F -e 'R_\Omega^{N,M}' -e '\hbar_{\mathrm{QME}}' -e '\hbar_{\mathrm{W}}' -e '\hbar_\omega' -e '\nu_\Omega^{\mathrm{res}}' -e '\nu_\Omega^{\mathrm{Eu}}' open-obligations.tex
grep -n '[[:blank:]]$' open-obligations.tex || true
```

The collapsed Omega scans returned no hits.  No PDF build was run because the
writable surface for this lane is limited to the two owned files and the shared
checkout has concurrent manuscript/build-output edits.

## Files Changed

- `open-obligations.tex`
- `reconstitution/swarm-2026-04-30-agent-223-nonscalar-qme-frontier-open-obligations-integration.md`
