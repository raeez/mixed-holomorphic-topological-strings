# Batch 1 Agent 002 Introduction Attack-Heal Report

## Habitat and claim attacked

Lane: introduction / front door.

Claim attacked: the opening could still be read as a one-theorem
collapse from the reduced Hamiltonian CE/PV--Moyal skeleton to a full
renormalized mixed holomorphic-topological string theorem.

Status after repair: conditional proof-ledger, not demotion.  The
strongest true front-door statement is that the proved local algebraic
skeleton
\[
  U^w_{\mathfrak h}
   =
   (\Phi_{\mathrm{coord}},\Phi^B_{P_0},C_{-,+},\Theta_{-,+},
      \Phi^{pp}_I,\Phi^{pp}_\hbar)
\]
is only a skeleton until each habitat supplies its objects, topology,
maps, obstruction complex, and first coordinate checks.

## File anchors and edits

- `main.tex:77`: inserted `The realization theorem is habitat-gated`.
- `main.tex:79-94`: separated the proved reduced Hamiltonian CE/PV
  skeleton from the stronger mixed HT realization theorem.
- `main.tex:96-169`: added the six-habitat realization front door,
  exposing the CE/PV and Matlis/MC algebraic spine as separate gates and
  listing the required data for `Coeff`, `CE/PV`, `Matlis/MC`,
  `FactCenter`, `BV/Graph/QME`, `KoszulSC`, `LargeN`, and `GlobDesc`.

`abstract.tex` was not edited.

Ownership note: `main.tex` already contains other modified regions in
the shared worktree.  This report owns only the localized introduction
block at `main.tex:77-169`.

## Checks

- Loaded `~/ecosystem/INVARIANTS.md`, `~/ecosystem/AGENTS-HARNESS.md`,
  `CLAUDE.md`, `AGENTS.md`, source provenance, current claim catalogue,
  metacognitive controller, roadmap index, Vol II synthesis, Vol II
  rectify skill, Vol II concordance/theorem registry, and the imported
  Vol II anti-pattern / first-principles surfaces AP2170--AP2189 and
  Patterns 490--509.
- Verified the relevant front-door anchors with `rg` and `nl -ba`.
- Ran `make pdf`.  First `pdflatex` pass wrote `out/main.pdf`; the
  second pass failed reading generated `out/main.aux` with invalid
  auxiliary content at line 115.
- Ran `pdflatex -output-directory=out -interaction=nonstopmode main.tex`
  once more.  It wrote `out/main.pdf` but exited nonzero because the
  generated `out/main.aux` ends with an extra `}` and contains stale
  auxiliary corruption.
- Ran `rg -n --text -P '\x00' . --glob '*.tex' --glob '*.sty'
  --glob '*.aux' --glob '*.toc'`; no NUL bytes were found in
  TeX/sty/aux/toc files.
- Ran a separate-output `pdflatex` pass to
  `/tmp/topological-strings-agent002-build`; it exited 0 and wrote a
  PDF.  This verifies that the inserted introduction subsection parses
  outside the stale `out/main.aux` state.

## Remaining obligations

- `Coeff`: construct the two-weight scale, strong duals, tensor
  topology, bracket/coadjoint estimates, diagonal convergence, and MC
  kernel habitat.
- `CE/PV`: keep the coordinate dg theorem distinct from \(P_0\)
  realization until bracket-admissible \(B\) is fixed.
- `Matlis/MC`: keep principal parts as the residue cotangent module and
  construct the completed convolution dg Lie algebra for
  \(\Theta_{-,+}\).
- `FactCenter`: prove arbitrary-open centrality and QME compatibility
  before calling the current target the unreduced factorization centre.
- `BV/Graph/QME`: construct fields, pairing, heat kernel, propagator,
  counterterms, RG flow, and non-scalar obstruction classes; Moyal
  normalization remains weaker than Costello graph realization.
- `KoszulSC`: specialize the two-colour \(\mathsf{SC}^{\mathrm{ch,top}}\)
  grammar locally; Vol II grammar is not a theorem import.
- `LargeN`: preserve the separation between degreewise stable algebra,
  admissible Koszul deformation, and physical BV/correlator large \(N\).
- `GlobDesc`: require \(C_{\mathrm{tar}}\), \(Ob_{UKD}(C_{\mathrm{tar}})\),
  and null-homotopies before any global transfer.
