# Agent 102 - Costello Graph/QME Source Fixture

Status: source fixture completed on owned paths. No manuscript theorem was
promoted.

## Owned Paths

- `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md`
- `references/source-provenance.md`
- `reconstitution/swarm-2026-04-30-agent-102-costello-graph-qme-source.md`

## Claim Attacked

The non-scalar Costello graph/QME theorem could be read as if Costello's
general finite-scale BV package automatically supplies the Hamiltonian
current target, \(\mathcal D'_c\)-wavefront control, and the
bulk-to-defect kernel.

That reading is false. Costello supplies the universal elliptic BV
renormalization calculus. The Hamiltonian brane-defect theorem needs
additional target, kernel, and obstruction-vanishing data.

## Supported Source Facts

- Heat-kernel propagator:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:77-90`;
  heat kernel existence:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1549-1557`.
- Regularized BV Laplacian:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:407-423`;
  finite-dimensional odd Laplacian comparison:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2088-2118`.
- RG/QME compatibility:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2121-2161`;
  renormalized QME:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2162-2190`.
- Counterterms and locality:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1746-1807`;
  RG/locality converse:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1967-2001`.
- Graph asymptotics:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:3544-3569`,
  `:3610-3625`, `:3660-3685`.
- Local obstruction calculus:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2376-2420`,
  `:2469-2483`, `:2554-2581`, `:2915-2938`, `:2975-3014`.
- \(H^1\) obstruction convention:
  `references/primary-sources/costello-li-quantum-bcov-1201.4501.txt:2493-2505`;
  open-closed lifting proposition:
  `references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt:2394-2412`.

## Non-Support

- No automatic current-valued target. `rg -n -F "current-valued"` over the
  local Costello/Costello--Li/Costello--Gwilliam mirrors returned no hits.
- No automatic \(\mathcal D'_c\) wavefront theorem. `rg -n -F "D'_c"` and
  `rg -n -F "compactly supported distributions"` over the same mirrors
  returned no hits. The only `wave.?front` mirror hit is Costello--Li's
  ordinary small-diagonal locality condition at
  `references/primary-sources/costello-li-quantum-bcov-1201.4501.txt:619`.
- No automatic bulk-to-defect kernel. Fixed-string searches for
  `bulk-to-defect` and `bulk to defect` over the same mirrors returned no
  hits.
- No exact published Costello 2011 theorem-number support beyond the
  prior source ledger. `references/primary-sources/costello-cg-source-anchors-2026-04-28.md:20-24`
  remains binding.

## Manuscript Alignment

The fixture supports the existing conservative posture:

- `main.tex:6641-6658`: universal Costello perturbative BV package.
- `main.tex:6783-6890`: Hamiltonian specialization data remain required.
- `main.tex:7334-7426`: non-scalar quantum \(P_0\)-operation is an
  obstruction-complex problem, not a proved graph theorem.
- `theorem-lanes.tex:1528-1572`: no non-scalar Costello graph/QME
  construction is asserted until the scalar-lift tower and reduced
  non-scalar class vanish.

## Files Changed

- Added `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md`.
- Appended the Agent 102 row to `references/source-provenance.md`.
- Added this report.

## Verification Commands

- `rg --files`
- `rg -n "Theorem|QME|quantum master|renormalization group|heat kernel|propagator|BV Laplacian|local functional|counterterm|obstruction|H\\^1" references/primary-sources/costello-renormalisation-bv-0706.1533.txt`
- `rg -n -F "current-valued" ...`
- `rg -n -F "D'_c" ...`
- `rg -n -F "bulk-to-defect" ...`
- `rg -n "wave.?front|wave front|wavefront" ...`
- `nl -ba` on all source and manuscript anchors recorded in the fixture.

No `make pdf` was run. This is a source-ledger edit, and the checkout is
under concurrent manuscript editing.

## Remaining Obligations

1. Import published Costello 2011 theorem/page anchors if the manuscript
   later needs exact AMS theorem numbers.
2. Prove the current-compatible wavefront/counterterm theorem for
   \(\mathcal D'_c\)-valued defect coefficients or restrict to regular
   densities.
3. Construct the Costello-category bulk-to-defect kernel and kill the
   reduced non-scalar class in
   \(H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})\).
