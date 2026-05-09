# Agent 164 Chiral-Algebra Proof Thread

Date: 2026-04-30.

Owned writable surface: `main.tex`, `theorem-lanes.tex`, and this report.
No subagents were launched.  The checkout already contained staged and
unstaged swarm edits in `main.tex` and `theorem-lanes.tex`; this pass
edited only the assigned files and did not revert or overwrite external
same-file work.

## Stable Core

The constructed local chiral/factorization object is theorem-grade in
the local sense used by the paper:
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \bigl(\Omega_c^{0,\bullet}(B)\widehat\otimes\mathfrak g\bigr),
  \qquad
  \mathfrak g=\mathfrak h\ltimes
  \mathfrak h^\vee_{\mathrm{cont}}[1],
  \quad
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1 .
\]
Its mixed topological-current enhancement is
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{mix}}(U\times B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \bigl(
    \Omega_c^\bullet(U)\widehat\otimes
    \Omega_c^{0,\bullet}(B)\widehat\otimes\mathfrak g
  \bigr).
\]
This is a two-complex-dimensional holomorphic or mixed
factorization object.  No one-dimensional VOA/OPE theorem is asserted.

## Valid Attacks

```yaml
id: A164-01
severity: 2
status: healed
lens: proof-thread closure
target: main.tex local Hamiltonian chiral/factorization definition
claim: The main text already gave a theorem-grade path from the local HT fields to the constructed factorization algebras.
broken_step: The definition named \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}} and \mathcal F_{\mathrm{Ham}}^{\mathrm{mix}}, but the field-to-\mathfrak g-to-CE-observable proof path was only distributed across later propositions.
evidence_type: proof_gap
evidence_ref: main.tex lines 1078-1140 before this pass; later proof anchors prop:hamiltonian-polyvector-reduction and prop:grav-ops
minimal_heal: Add a concise proposition proving the reduction to \mathfrak g and the CE/factorization observable assignments.
residual: None for the local CE/factorization construction.
```

```yaml
id: A164-02
severity: 2
status: healed
lens: theorem-lane dependency closure
target: theorem-lanes.tex thm:lane-holomorphic-defect-voa-restriction proof path
claim: The theorem lane made the constructed local chiral/factorization algebra prominent with a complete proof pointer.
broken_step: The lane named the constructed object and cited CE/PV and current theorems, but did not cite an explicit bridge from local mixed HT fields to \mathfrak g and then to CE factorization observables.
evidence_type: line_reference
evidence_ref: theorem-lanes.tex proof path around lines 419-441 before this pass
minimal_heal: Add Proposition~\ref{prop:local-hamiltonian-factorization-observables} to the proof path.
residual: None for theorem-lane closure.
```

```yaml
id: A164-03
severity: 3
status: healed
lens: vertex-overclaim firewall
target: main.tex and theorem-lanes.tex local chiral/factorization thread
claim: Strengthening the construction could accidentally assert a one-dimensional VOA/OPE algebra.
broken_step: A CE/factorization construction on \mathbb C^2 is not a VOA without a chosen complex line, transverse boundary datum, restriction functor, and finite Laurent OPE expansion.
evidence_type: proof_gap
evidence_ref: theorem-lanes.tex thm:lane-holomorphic-defect-voa-restriction vertex/OPE boundary
minimal_heal: State in the new proposition proof that no one-dimensional vertex/OPE structure is asserted.
residual: Complex-line or holomorphic-defect restriction remains open.
```

## Repairs Made

- Added Proposition `prop:local-hamiltonian-factorization-observables` in
  `main.tex`.  It proves the path
  \[
    \text{local mixed HT fields}
    \to
    \mathfrak g=\mathfrak h\ltimes
    \mathfrak h^\vee_{\mathrm{cont}}[1]
    \to
    \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}},
    \mathcal F_{\mathrm{Ham}}^{\mathrm{mix}} .
  \]
- Added the theorem-lane proof pointer to
  `thm:lane-holomorphic-defect-voa-restriction`.
- Preserved the vertex/OPE boundary: a VOA requires the separate
  complex-line or holomorphic-defect restriction theorem.

## Exact References

- `main.tex:1142`:
  Proposition `prop:local-hamiltonian-factorization-observables`.
- `main.tex:1149`:
  \(\mathfrak g=\mathfrak h\ltimes
  \mathfrak h^\vee_{\mathrm{cont}}[1]\).
- `main.tex:1158`:
  \(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)\).
- `main.tex:1166`:
  \(\mathcal F_{\mathrm{Ham}}^{\mathrm{mix}}(U\times B)\).
- `main.tex:1182`:
  proof uses `prop:hamiltonian-polyvector-reduction`.
- `main.tex:1188`:
  proof uses `prop:grav-ops`.
- `theorem-lanes.tex:422`:
  theorem-lane proof path now cites
  `prop:local-hamiltonian-factorization-observables`.

## Verification

Commands run:

```bash
rg -n -F "prop:local-hamiltonian-factorization-observables" main.tex theorem-lanes.tex
rg -n -F "Constructed Hamiltonian CE/factorization observables" main.tex
rg -n -F "mathcal F_{\\mathrm{Ham}}^{\\mathrm{hol}}" main.tex theorem-lanes.tex abstract.tex local-dictionary.tex
rg -n "one-dimensional (VOA|vertex)|OPE|vertex algebra|compact-CY|CoHA|Igusa|BKM" main.tex theorem-lanes.tex abstract.tex local-dictionary.tex
git diff --check -- main.tex theorem-lanes.tex
mkdir -p /tmp/topological-strings-agent164-build
pdflatex -halt-on-error -interaction=nonstopmode -draftmode -output-directory=/tmp/topological-strings-agent164-build main.tex
pdflatex -halt-on-error -interaction=nonstopmode -draftmode -output-directory=/tmp/topological-strings-agent164-build main.tex
pdflatex -halt-on-error -interaction=nonstopmode -draftmode -output-directory=/tmp/topological-strings-agent164-build main.tex
rg -n "undefined|Label\\(s\\)|prop:local-hamiltonian-factorization-observables" /tmp/topological-strings-agent164-build/main.log
```

Results:

- Object-name scans find the new proposition, theorem-lane pointer, and
  existing abstract/dictionary foregrounding.
- The VOA/OPE/firewall scan finds only negative, conditional, or
  unrelated uses; no new VOA theorem claim was introduced.
- `git diff --check -- main.tex theorem-lanes.tex` passed.
- The first draft TeX run failed before manuscript processing because
  the `/tmp` output directory did not exist.  After `mkdir -p`, three
  draft `pdflatex` runs exited 0.
- The final `/tmp` log scan for `undefined`, `Label(s)`, and the new
  proposition label returned no hits.  Remaining TeX output consists of
  pre-existing underfull/overfull box and font metric warnings.

## Files Changed / Staged

Changed by Agent 164:

- `main.tex`
- `theorem-lanes.tex`
- `reconstitution/swarm-2026-04-30-agent-164-chiral-algebra-proof-thread.md`

Staged by Agent 164: this report only.  `main.tex` and
`theorem-lanes.tex` already had staged and unstaged same-file swarm
changes on entry; this pass left those index entries untouched to avoid
sweeping other agents' deltas into an Agent 164 staging action.

## Remaining Obligations

- A one-dimensional VOA/OPE algebra still requires a separate
  complex-line or holomorphic-defect restriction theorem with transverse
  datum and Laurent-mode construction.
- The unreduced non-scalar Costello graph/QME lift, finite-window
  counterterms, and curved bulk-to-defect kernel remain outside this
  local CE/factorization proof thread.
- Compact Calabi--Yau, CoHA, quintic, OSV/GV, Abel--Jacobi, Igusa,
  Borcherds, and BKM targets remain external comparison surfaces only.
