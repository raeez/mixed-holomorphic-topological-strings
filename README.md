# Mixed Holomorphic–Topological Strings

Raeez Lorgat

Hamiltonian fields on a holomorphic symplectic plane act on matrix boundary observables. The book develops finite Hamiltonian and cotangent constructions, chiral operations, and comparisons between bulk observables and boundary actions, with the hypotheses for continuous, quantum, and global extensions stated separately. The accompanying paper studies scalar Donaldson–Thomas/Pandharipande–Thomas factorisation on Calabi–Yau threefolds, framing, and conjectural comparisons with centre lifts and Bershadsky–Cecotti–Ooguri–Vafa amplitudes.

- Hamiltonian fields, chiral operations, and reconstruction: [PDF](platonic/main.pdf), [LaTeX](platonic/main.tex).
- Compact Calabi–Yau threefold comparisons: [PDF](frontier_mnop_framing_volume.pdf), [LaTeX](frontier_mnop_framing_volume.tex).

With TeX Live and latexmk, run these commands from a copy of this directory:

```sh
TEXINPUTS=.:..: latexmk -norc -pdf -cd -interaction=nonstopmode -halt-on-error platonic/main.tex
TEXINPUTS=.:..: latexmk -norc -pdf -interaction=nonstopmode -halt-on-error frontier_mnop_framing_volume.tex
```
