# Agent 170 Chiral-Algebra Frontmatter/Theorem Sync

Date: 2026-04-30.

Owned writable surface: `abstract.tex`, `theorem-lanes.tex`, and this report.
No subagents were launched.  I read `main.tex` and
`reconstitution/swarm-2026-04-30-agent-164-chiral-algebra-proof-thread.md`;
I did not edit `main.tex`.

## Stable Core

The frontmatter and theorem lanes now state the constructed local
chiral/factorization algebra at theorem strength:
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
This is the two-complex-dimensional holomorphic or mixed
factorization object proved by
Proposition~\ref{prop:local-hamiltonian-factorization-observables}.  It
is not a one-dimensional VOA/OPE theorem.

## Valid Attacks

```yaml
id: A170-01
severity: 2
status: healed
lens: frontmatter theorem-surface sync
target: abstract.tex opening and chiral/factorization paragraph
claim: The abstract foregrounded the constructed chiral object at the same strength as the new main-text bridge.
broken_step: The abstract said the local chiral object was constructed, but the proved-results sentence did not include the Hamiltonian CE/factorization-observables construction and the displayed CE observable formulas were absent.
evidence_type: line_reference
evidence_ref: main.tex prop:local-hamiltonian-factorization-observables; abstract.tex pre-patch lines 6-38
minimal_heal: Add the local Hamiltonian CE/factorization-observables construction to the proved surface and display the F_Ham^hol and F_Ham^mix CE formulas.
residual: None for frontmatter theorem-strength synchronization.
```

```yaml
id: A170-02
severity: 2
status: healed
lens: theorem-lane dependency closure
target: theorem-lanes.tex thm:lane-local-chiral-taxonomy
claim: The taxonomy lane was theorem-bridged to the new proof bridge.
broken_step: The lane still read as a definitional firewall and cited the sector definitions and CE/PV/current theorems, but not the new proposition proving the field-to-g-to-CE factorization-observable bridge.
evidence_type: line_reference
evidence_ref: theorem-lanes.tex pre-patch proof inputs around lines 327-339; main.tex:1142
minimal_heal: Mark the lane as a theorem-bridged local construction, display the exact CE observable assignments, and add Proposition~\ref{prop:local-hamiltonian-factorization-observables} to the proof inputs.
residual: None for this lane.
```

```yaml
id: A170-03
severity: 3
status: healed
lens: overclaim firewall
target: abstract.tex and theorem-lanes.tex chiral/factorization wording
claim: Strengthening the chiral/factorization language might import a one-dimensional VOA/OPE theorem or collapse the open QME/radial obligations into the local construction.
broken_step: The word chiral is ambiguous unless the text keeps the C^2 holomorphic factorization object separate from complex-line vertex/OPE data and from the larger QME/radial packages.
evidence_type: proof_gap
evidence_ref: theorem-lanes.tex thm:lane-holomorphic-defect-voa-restriction; abstract.tex quantum coefficient paragraph
minimal_heal: State explicitly that the constructed objects are two-complex-dimensional holomorphic or mixed factorization objects, preserve the separate VOA/OPE boundary, and leave the QME/radial obligations in the componentwise quantum paragraph.
residual: VOA/OPE restriction, non-scalar QME, and radial-parts normalization remain separate obligations.
```

## Repairs Made

- `abstract.tex` now lists the local Hamiltonian
  CE/factorization-observables construction among the proved results and
  displays the exact \(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)\) and
  \(\mathcal F_{\mathrm{Ham}}^{\mathrm{mix}}(U\times B)\) CE formulas.
- `theorem-lanes.tex` now marks
  `thm:lane-local-chiral-taxonomy` as a theorem-bridged local construction,
  gives the exact formal-disk and mixed-current CE assignments, keeps the
  CE object distinct from the coordinate/admissible PV identification, and
  cites `prop:local-hamiltonian-factorization-observables`.
- The existing vertex/OPE boundary and the separate QME/radial obstruction
  lanes were preserved.

## Exact References

- `main.tex:1142`: Proposition
  `prop:local-hamiltonian-factorization-observables`.
- `main.tex:1158`: \(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)\).
- `main.tex:1166`: \(\mathcal F_{\mathrm{Ham}}^{\mathrm{mix}}(U\times B)\).
- `abstract.tex:7`: proved-surface list now includes the local Hamiltonian
  CE/factorization-observables construction.
- `abstract.tex:26`: theorem-grade local chiral/factorization construction.
- `theorem-lanes.tex:227`: `thm:lane-local-chiral-taxonomy`.
- `theorem-lanes.tex:344`: taxonomy proof input now cites
  `prop:local-hamiltonian-factorization-observables`.
- `theorem-lanes.tex:440`: constructed-object lane proof path cites the
  same proposition.

## Verification

Commands run:

```bash
git diff --check -- abstract.tex theorem-lanes.tex
rg -n -F -e "theorem-grade local chiral/factorization construction" -e "theorem-bridged local construction" -e "Proposition~\\ref{prop:local-hamiltonian-factorization-observables}" -e "one-dimensional VOA/OPE claim requires" -e "does not yet assert the stronger one-dimensional VOA/OPE" abstract.tex theorem-lanes.tex
rg -n "one-dimensional (VOA|vertex)|VOA/OPE|compact-CY|CoHA|Igusa|BKM|QME|radial" abstract.tex theorem-lanes.tex
pdflatex -halt-on-error -interaction=nonstopmode -draftmode -output-directory=/tmp/topological-strings-agent170-build main.tex
pdflatex -halt-on-error -interaction=nonstopmode -draftmode -output-directory=/tmp/topological-strings-agent170-build main.tex
pdflatex -halt-on-error -interaction=nonstopmode -draftmode -output-directory=/tmp/topological-strings-agent170-build main.tex
rg -n "undefined|Label\\(s\\)|prop:local-hamiltonian-factorization-observables" /tmp/topological-strings-agent170-build/main.log
```

Results:

- `git diff --check` passed.
- Anchor scans found the theorem-grade construction, the theorem-bridged
  taxonomy status, and both proposition citations.
- The firewall scan found only negative, conditional, or separate-obligation
  uses for VOA/OPE, compact targets, QME, and radial language.
- Three draft `pdflatex` passes exited 0.  The final log scan returned no
  hits for undefined references, changed labels, or unresolved uses of the
  new proposition label.  Remaining TeX output is pre-existing
  underfull/overfull and font metric noise.

## Files Changed / Staged

Changed by Agent 170:

- `abstract.tex`
- `theorem-lanes.tex`
- `reconstitution/swarm-2026-04-30-agent-170-chiral-algebra-frontmatter-theorem-sync.md`

Staged by Agent 170: this report only.  `abstract.tex` and
`theorem-lanes.tex` already had staged swarm changes on entry; I left those
index entries untouched to avoid sweeping other agents' same-file deltas into
this agent's staging action.

## Remaining Obligations

- A one-dimensional VOA/OPE algebra still requires the separate complex-line
  or holomorphic-defect restriction theorem with transverse datum,
  factorization-to-vertex comparison, and finite Laurent OPE modes.
- The unreduced non-scalar Costello graph/QME lift, finite-window
  counterterms, curved bulk-to-defect kernel, and scalar-extension towers
  remain outside this frontmatter/theorem-lane synchronization.
- The all-\(N\) radial-parts normalization and compact/global comparison
  surfaces remain external or conditional, not consequences of the local
  Hamiltonian CE/factorization construction.
