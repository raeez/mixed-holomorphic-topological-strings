# Agent 159 Foreground Local Chiral Algebra

Date: 2026-04-30.

Owned writable surface: `abstract.tex`, `main.tex`, and this report.
No subagents were launched.  The checkout already contained staged swarm
edits in `abstract.tex` and `main.tex`, plus unstaged changes in
`local-dictionary.tex` and `theorem-lanes.tex` owned by other agents.
This pass edited only the assigned files.  The assigned paths were staged
after verification; pre-existing staged hunks in `abstract.tex` and
`main.tex` were preserved.

## Stable Core

The constructed local chiral/factorization object is now named in the
abstract and introduction:
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}
\]
the formal Hamiltonian holomorphic factorization algebra on the formal
\(\mathbb C^2\)-disk with dg Lie input
\[
  \mathfrak g=\mathfrak h\ltimes
  \mathfrak h^\vee_{\mathrm{cont}}[1],
  \qquad
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1 .
\]
Its mixed topological-current enhancement
\(\mathcal F_{\mathrm{Ham}}^{\mathrm{mix}}\) has input
\[
  \Omega_c^\bullet(U)\widehat\otimes
  \Omega_c^{0,\bullet}(B)\widehat\otimes\mathfrak g .
\]
The brane avatars are the Weyl/Moyal brane algebra, matrix or
supermatrix cyclic trace bar-cobar models, and the defect
principal-part current algebra on brane intervals.

## Valid Attacks

```yaml
id: A159-01
severity: 2
status: healed
lens: foregrounding
target: abstract.tex, main.tex introduction
claim: The main narrative already tells the reader what chiral/factorization algebra is constructed.
broken_step: The local dictionary and theorem lanes contained the taxonomy, but the abstract and introduction still foregrounded CE/PV and quantum coefficient data before naming the actual local chiral/factorization object.
evidence_type: line_reference
evidence_ref: pre-repair abstract.tex:18-24; main.tex:1069-1076
files_read: [abstract.tex, main.tex, local-dictionary.tex, theorem-lanes.tex, reports 136 and 149]
confidence: high
blast_radius: Readers could misread "chiral" as an unspecified VOA, compact-CY chiral homology object, or external comparison target.
minimal_heal: Name the formal Hamiltonian holomorphic factorization algebra and its mixed/current/brane avatars in the abstract and introduction.
residual: None for foregrounding; theorem-level constructions remain as cited.
deciding_evidence: rg scans for the inserted object names and exclusion language.
```

```yaml
id: A159-02
severity: 2
status: healed
lens: VOA/OPE overclaim
target: abstract.tex, main.tex introduction
claim: A one-dimensional VOA/OPE algebra follows from the brane-line current or chiral wording.
broken_step: The core holomorphic object is two-complex-dimensional on \(\mathbb C^2\), while the brane current object is real support-local on intervals. Neither supplies a complex-line restriction, transverse boundary condition, or Laurent OPE expansion.
evidence_type: proof_gap
evidence_ref: local-dictionary.tex local chiral/factorization taxonomy; theorem-lanes.tex local chiral taxonomy and holomorphic-defect VOA obstruction lane
files_read: [local-dictionary.tex, theorem-lanes.tex, main.tex]
confidence: high
blast_radius: Would import a false vertex-algebra theorem into the local theorem surface.
minimal_heal: State explicitly in abstract and introduction that a one-dimensional VOA/OPE claim requires a separate complex-line or holomorphic-defect restriction theorem.
residual: The restriction theorem remains open.
deciding_evidence: rg scan for VOA/OPE caveat in abstract.tex and main.tex.
```

```yaml
id: A159-03
severity: 3
status: healed
lens: avatar conflation
target: main.tex introduction
claim: Weyl/Moyal, cyclic trace, and principal-part current objects are one algebra.
broken_step: The Weyl/Moyal brane algebra is the degree-zero quantum brane target; cyclic/supercyclic complexes are trace bookkeeping avatars; principal-part currents realize the cotangent/defect sector after de Rham-current contraction.
evidence_type: line_reference
evidence_ref: main.tex formal Weyl/Moyal target; main.tex support-local principal-part current theorem; local-dictionary taxonomy
files_read: [main.tex, local-dictionary.tex, theorem-lanes.tex]
confidence: high
blast_radius: Could erase the PBW/principal-part separation and same-action obstruction.
minimal_heal: List the avatars separately in the new definition and abstract.
residual: Unreduced non-scalar Costello/QME lift remains open.
deciding_evidence: inserted definition separates the three avatars.
```

## Repairs Made

- `abstract.tex`: inserted a foregrounding paragraph naming
  \(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\),
  \(\mathcal F_{\mathrm{Ham}}^{\mathrm{mix}}\), the Weyl/Moyal brane
  algebra, cyclic trace avatars, principal-part current avatars, and the
  VOA/OPE restriction obligation.
- `main.tex`: added
  `def:local-hamiltonian-chiral-factorization-algebra` in the
  introduction, with formulas for the holomorphic dg Lie input, the mixed
  topological-current input, the brane Weyl/Moyal avatar, and the
  defect principal-part current target.
- `main.tex`: added a local-theorem bridge paragraph saying that the
  theorem constructs and compares these named local objects, not a
  one-dimensional VOA/OPE algebra.

## Exact Statements Inserted

- Formal Hamiltonian holomorphic factorization algebra:
  \[
    \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}},\qquad
    \Omega_c^{0,\bullet}(B)\widehat\otimes
    (\mathfrak h\ltimes\mathfrak h^\vee_{\mathrm{cont}}[1]).
  \]
- Mixed topological-current enhancement:
  \[
    \mathcal F_{\mathrm{Ham}}^{\mathrm{mix}}(U\times B),\qquad
    \Omega_c^\bullet(U)\widehat\otimes
    \Omega_c^{0,\bullet}(B)\widehat\otimes\mathfrak g .
  \]
- Defect/principal-part current avatar:
  \[
    \mathfrak h_I=\Omega^\bullet_c(I)\widehat\otimes\mathfrak h,\quad
    \mathcal P_I=\mathcal D'_c(I)\widehat\otimes\mathcal P,\quad
    \mathfrak g_I=\mathfrak h_I\ltimes\mathcal P_I[1],
  \]
  \[
    A^{\mathrm{pp}}_\partial(I)
    =
    \widehat{\mathbf S}(\Omega_c^0(I)\widehat\otimes\bar A)
    \widehat\otimes
    \widehat{\mathbf S}(\mathcal D'_c(I)\widehat\otimes\mathcal P[1]).
  \]
- Caveat: a one-dimensional VOA/OPE statement requires a separate
  complex-line or holomorphic-defect restriction theorem.

## Files Changed / Staged

Changed by Agent 159:

- `abstract.tex`
- `main.tex`
- `reconstitution/swarm-2026-04-30-agent-159-foreground-local-chiral-algebra.md`

Staged after this pass:

- `abstract.tex`
- `main.tex`
- `reconstitution/swarm-2026-04-30-agent-159-foreground-local-chiral-algebra.md`

`abstract.tex` and `main.tex` already had staged swarm edits on entry;
staging these paths preserves those index hunks and adds the Agent 159
foregrounding edits.

## Verification

```bash
rg -n -F \
  -e 'F_{\mathrm{Ham}}' \
  -e 'local-hamiltonian-chiral-factorization-algebra' \
  -e 'formal Hamiltonian holomorphic factorization algebra' \
  -e 'mixed topological-current' \
  -e 'Weyl/Moyal brane' \
  -e 'principal-part current' \
  -e 'one-dimensional VOA' \
  -e 'OPE' \
  -- abstract.tex main.tex reconstitution/swarm-2026-04-30-agent-159-foreground-local-chiral-algebra.md
rg -n "compact Calabi|compact-CY|CoHA|quintic|OSV|GV|Abel|Igusa|BKM|Borcherds|VOA|OPE|vertex" abstract.tex main.tex
git diff --check -- abstract.tex main.tex reconstitution/swarm-2026-04-30-agent-159-foreground-local-chiral-algebra.md
pdflatex -halt-on-error -interaction=nonstopmode -draftmode -output-directory=/tmp/topological-strings-agent159-build main.tex
```

Results:

- The object-name scan finds the new abstract paragraph, the new
  introduction definition, and the local-theorem bridge paragraph.
- The firewall scan finds only negative/caveat uses, existing
  comparison-firewall text, and unrelated graph-vertex uses of
  "vertex".  No new compact-CY, CoHA, Igusa, BKM, or VOA theorem claim was
  introduced.
- `git diff --check` passed.
- Three `/tmp` draft `pdflatex` passes exited 0.  The final pass had no
  fatal TeX errors.  Remaining output consists of pre-existing
  underfull/overfull box warnings, including in
  `appendix-radial-parts-moyal.tex` and `tate-P5-cross-volume.tex`, and
  font metric warnings from the local TeX installation.  No failure came
  from the new abstract or introduction text.

## Remaining Theorem Obligations

- Prove the complex-line or holomorphic-defect restriction theorem before
  asserting a one-dimensional vertex algebra or OPE-mode algebra.
- Construct the unreduced non-scalar Costello graph/QME realization,
  finite-window counterterms, and curved bulk-to-defect kernel before
  upgrading the componentwise quantum coefficient surface.
- Keep compact Calabi-Yau, CoHA, quintic, OSV/GV, Abel-Jacobi, Igusa,
  Borcherds, and BKM material outside the local theorem unless a separate
  matched-conventions theorem and obstruction-vanishing proof are supplied.
