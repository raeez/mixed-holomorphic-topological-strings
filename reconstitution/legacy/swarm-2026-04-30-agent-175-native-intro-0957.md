# Agent 175 Native Introduction Attack-Heal Report

Date: 2026-04-30.
Owned surface: `main.tex` introduction and local-model theorem-package region.
Report path: `reconstitution/swarm-2026-04-30-agent-175-native-intro-0957.md`.

## Stable Core

The native opening is now the formal local model
\[
  X=\mathbb R_t\times\mathbb R_s\times\mathbb C^2_{z_1,z_2},
  \qquad
  L=\mathbb R_t\times\{s=z_1=z_2=0\}.
\]
The holomorphic input is the Darboux normal disk
\((\widehat{\mathbb C^2}_0,dz_1\wedge dz_2)\).  The closed fields are
Hamiltonian BF fields for
\[
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C,\qquad
  P=\mathfrak h^\vee_{\mathrm{cont}},\qquad
  \mathfrak g=\mathfrak h\ltimes P[1].
\]
The open fields are the Dirac matrix probe with
\[
  Q\psi=[\phi_1,\phi_2].
\]
After scalar quotient, the coordinate CE/PV derived-centre map is
\[
  c^I\mapsto\theta^I,\qquad u_I\mapsto O_I.
\]
The PBW one-\(\psi\) labels remain the special-fibre shadow; the
deformation-level cotangent module is the Matlis/principal-part coadjoint
module.

## Attacks And Repairs

`A175-01` valid.  The opening did not force the native \(t,s,z_1,z_2\)
model before discussing probes.  Healed at `main.tex:79-99` by naming
\(X\), \(L\), the formal Darboux normal disk, and the firewall against
compact Calabi--Yau and curve-VOA imports.

`A175-02` valid.  The CE/PV map was present but not exposed as the
derived-centre map in the opening architecture.  Healed at
`main.tex:209-219`, `main.tex:1256-1263`, and `main.tex:2046-2051`.

`A175-03` valid.  The PBW/deformation split was proved later but not
front-loaded in the theorem package.  Healed at `main.tex:241-247`,
`main.tex:1262-1269`, and `main.tex:2052-2053`.

`A175-04` valid.  The phrase "chiral/factorization" still risked a
curve-VOA reading.  Healed by renaming the definition and tightening the
firewall at `main.tex:1099`, `main.tex:1153-1160`,
`main.tex:1195`, and `main.tex:1271-1274`.

`A175-05` valid.  The theorem package was distributed across the
introduction, local model, and theorem statement.  Healed by inserting
`Proposition~\ref{prop:native-darboux-theorem-package}` at
`main.tex:1230-1295` and rewriting the main local theorem statement and
proof at `main.tex:2026-2119`.

Concurrent note: `main.tex:1163-1228` contained a pre-existing unstaged
constructed Hamiltonian CE/factorization proposition when this agent
began.  I preserved it and used it as a proof anchor; only its local
wording was tightened to the holomorphic factorization register.

## Changed Line Bands

- `main.tex:79-99`: native \(X,L\) model, Darboux normal disk, and
  compact-CY / curve-VOA firewall in the opening.
- `main.tex:209-219`: cochain-level CE/PV derived-centre map
  \(c^I\mapsto\theta^I\), \(u_I\mapsto O_I\).
- `main.tex:241-247`: PBW special-fibre shadow separated from the
  deformation-level Matlis/coadjoint cotangent module.
- `main.tex:1080-1089`: local mixed model rewritten as
  \(X=\mathbb R_t\times\mathbb R_s\times\mathbb C^2\),
  \(L=\mathbb R_t\times\{s=z_1=z_2=0\}\).
- `main.tex:1099` and `main.tex:1153-1160`: native holomorphic
  factorization language and no-VOA firewall.
- `main.tex:1195`: concurrent constructed-observables proposition
  tightened from "chiral/factorization" to "holomorphic factorization."
- `main.tex:1230-1295`: new native Darboux theorem-package proposition.
- `main.tex:2026-2119`: main local theorem and proof reconstituted around
  Dirac probe, Hamiltonian BF fields, scalar quotient, CE/PV map, and
  PBW/deformation separation.

## Verification

Commands run:

```bash
git diff --check -- main.tex
git diff --check -- main.tex reconstitution/swarm-2026-04-30-agent-175-native-intro-0957.md
rg -n "label\\{(lem:dirac-probe-reduction|lem:open-action-reduction|prop:open-bv-truncation|thm:principal-part-coadjoint-uniqueness)\\}" main.tex appendix-*.tex theorem-lanes.tex
rg -n "ref\\{(prop:native-darboux-theorem-package|prop:local-hamiltonian-factorization-observables|lem:open-action-reduction|lem:dirac-probe-reduction|prop:open-bv-truncation|thm:principal-part-coadjoint-uniqueness)\\}" main.tex
make pdf
```

Results: whitespace check passed; all new proof anchors resolve to
existing labels or to the new native-package proposition.  `make pdf`
completed successfully and wrote `out/main.pdf` with existing
underfull/overfull/font warnings.

## Residual Theorem Obligations

1. Construct the full non-scalar Costello graph/QME realization in
   \(\mathfrak Q^\bullet_{w,\partial,\hbar}(I)\), including the
   bulk-to-defect kernel and compatible finite-window counterterms.
2. Upgrade the coordinate CE/PV map to any unreduced factorization-centre
   morphism only after the bracket-admissible completion, kernel
   convergence, and centrality homotopies are supplied.
3. Prove any one-dimensional VOA/OPE statement only after a separate
   holomorphic-defect or complex-line restriction theorem retaining the
   transverse coefficient system.
4. Keep compact Calabi--Yau, CoHA, BKM, and global twisted-M-theory claims
   outside the native theorem surface unless a matched-conventions theorem
   is supplied.
