# Remarks on Mixed Holomorphic-Topological Strings

A research manuscript on formal local Hamiltonian BF theory, reduced
CE/PV central operations, and a Dirac brane probe on
\(\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}\).
The source root is `main.tex`.

The closed Hamiltonian Lie algebra is the Hamiltonian Lie algebra of
the formal symplectic disk modulo constants,
\(\mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot 1\); the closed
observables of the slice are the continuous CE cochains of the
shifted-cotangent extension
\(\mathfrak g=\mathfrak h\ltimes\mathfrak h^\vee_{\mathrm{cont}}[1]\).
A stack of \(N\) Dirac branes on the topological line carries a probe
pair of \(\mathfrak{gl}_N\)-valued matrices.  The manuscript proves a
coordinate CE/PV central-operation theorem identifying CE coordinates
with Schouten polyvectors of the boundary Hamiltonian polynomial
algebra; states and uses the abstract bracket-compatible CE/PV
recognition criterion; and bounds bar-cobar / kernel / quantum
extensions by named obstruction classes.  \(P_0\), kernel, analytic,
and global claims enter through explicit admissibility hypotheses and
named obstruction complexes, not by transfer from the formal disk
alone.

## Build

Prerequisites: a TeX installation with `pdflatex`, `makeindex`, GNU
`make`, and the local style files.

```bash
make fast        # one-pass build to out/main.pdf (fastest)
make pdf         # full multi-pass build with index
make standalone  # build standalone TeX artifacts
make help        # list all targets
```

The compiled PDF is written to `out/main.pdf`.  Build success is a
TeX integrity check; it is not a mathematical certification.

## Compiled source layout

- `main.tex` — root file.
- `abstract.tex` — abstract.
- `authors.tex` — author block.
- `mathmacros.tex` — mathematical macro layer.
- `section-pro-matlis-envelope.tex`,
  `appendix-factorization-current-conventions.tex`,
  `appendix-sign-conventions.tex`,
  `appendix-full-psi-homology.tex`,
  `appendix-unreduced-bv-qme.tex`,
  `appendix-radial-parts-moyal.tex` — appendices.
- `tate-T1-weighted-completion.tex`,
  `tate-T2-nilpotent-truncation.tex`,
  `tate-T3-quillen-equivalence.tex`,
  `tate-T4-bv-vanishing.tex`,
  `tate-T5-chain-level-primitive.tex`,
  `tate-P1-hadamard-mittag-leffler.tex` — Tate-residual / coefficient
  closure fragments.

## Reference catalogs (not compiled into the PDF)

- `claim-strength-ledger.tex` — epistemic-status ledger for each
  load-bearing theorem.
- `open-obligations.tex` — explicit list of conjectures, problems, and
  construction targets.
- `local-dictionary.tex` — cross-construction dictionary.
- `principles.tex` — voice and methodology principles.
- `reader-route.tex` — reading-order map.
- `frontier_mnop_framing_volume.tex` — MNOP / framing comparison
  surface (matched-conventions only, per `CLAUDE.md`).
- `tate-P3-universality.tex`, `tate-P5-cross-volume.tex` —
  reconstitution-stage coefficient files.

## Compute scripts

`scripts/` contains finite-window verification scripts:
`check_moyal_coefficients.py`, `check_one_psi_homology.py`,
`finite_window_graph_array.py`, and others.  These are run as part of
the local compute layer; they are not invoked by `make`.
