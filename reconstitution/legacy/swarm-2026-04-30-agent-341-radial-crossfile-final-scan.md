# Agent 341 radial cross-file final scan

Scope: `main.tex`, `theorem-lanes.tex`, `open-obligations.tex`,
`claim-strength-ledger.tex`, `CLAUDE.md`, `AGENTS.md`, and
`reconstitution/attack-heal-latest-2026-04-30.md`.  The radial appendix was
not edited.

## Result

The stale uniform-homotopy / radial-contracting-homotopy surface is removed
from the requested files.  The live radial/Weyl theorem surface is now
`\Omega^{\mathrm{rad}}_{a,b}`, equivalently decorated PBW Stokes
`D^\square_{a,b}=C^+_{a,b}\partial_2`, with failure certified by a signed
row `(\phi,-\lambda)\in\ker B_{a,b}^*`.

## Minimal patches made

- `reconstitution/attack-heal-latest-2026-04-30.md:101`: replaced
  "all-bidegree homotopy remains open" by "the signed-row obstruction surface
  remains open."
- `reconstitution/attack-heal-latest-2026-04-30.md:277`: replaced obligation
  8's "Construct the radial contracting homotopy on \(\ker\partial\)" by the
  current `\Omega^{\mathrm{rad}}` / decorated PBW Stokes / signed-row
  obstruction formulation.  The main-thread follow-up tail at lines 281-282,
  "certified bidegrees and the exact signed-row obstruction theorem," is
  present and preserved.
- `claim-strength-ledger.tex:581`: replaced "Radial all-\(N\) image and
  all-bidegree homotopy" by "Radial all-\(N\) image and signed-row obstruction
  surface."
- `main.tex:2786`: replaced the older "uniform splitting" / "stable
  left-cokernel" lead sentence by the dual-potential obstruction problem.
- `open-obligations.tex:1438`: changed the radial free-complex shadow from
  "equivalently a left-cokernel functional" to "in the older free-complex
  shadow, a functional"; the theorem-grade signed-row criterion remains at
  lines 1441-1445.

## Remaining keyword hits checked

- `theorem-lanes.tex:2585`: "matched-normalization" belongs to the
  Capelli/Weyl and radial-parts comparison paragraph.  It is immediately
  controlled by the current radial/Weyl gate at lines 2620-2626, so no patch.
- `main.tex:1080`: explicitly says the current signed-row surface sharpens
  older `\mathcal C_{a,b}` left-cokernel language.  No patch.
- `open-obligations.tex:681`: non-scalar finite-window matrix criterion
  `A^Mc=-r^M`, not the radial lane.  No patch.
- `claim-strength-ledger.tex:523`, `main.tex:8959`, `main.tex:9066`: theta-3
  finite-row / CE-source cokernel certificates, not the radial lane.  No patch.
- `AGENTS.md:132`: generic supremum-discipline obstruction list.  No patch.

## Verification

- `rg -n -i "uniform[- ]?homotop|all-bidegree homotopy|radial contracting homotopy|uniform splitting|stable left-cokernel|radial[^\n]{0,80}homotop|homotop[^\n]{0,80}radial" main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex CLAUDE.md AGENTS.md reconstitution/attack-heal-latest-2026-04-30.md`
  returned zero hits.
- `rg -n -i "radial[^\n]{0,120}normaliz|normaliz[^\n]{0,120}radial|normalis[^\n]{0,120}radial|radial[^\n]{0,120}normalis|left[- ]?cokernel|cokernel functional" ...`
  was manually classified as above.
- `git diff --check -- main.tex open-obligations.tex claim-strength-ledger.tex reconstitution/attack-heal-latest-2026-04-30.md reconstitution/swarm-2026-04-30-agent-341-radial-crossfile-final-scan.md`
  passed.
