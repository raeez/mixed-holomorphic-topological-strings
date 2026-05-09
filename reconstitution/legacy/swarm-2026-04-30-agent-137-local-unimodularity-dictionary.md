# Agent 137 Local Unimodularity Dictionary

Date: 2026-04-30

Scope: Agent 137 owns only `local-dictionary.tex` and this report. Other repository changes were treated as concurrent swarm work and were not reverted.

## Stable core

The local Calabi--Yau input used by the paper is exactly the formal orientation/unimodularity datum
\[
  (\widehat{\mathbb C^2}_0,\Omega_{\mathrm{loc}}),
  \qquad \Omega_{\mathrm{loc}}=dz_1\wedge dz_2 .
\]
It supplies the local canonical trivialization, the Hamiltonian Poisson bracket, the divergence operator, the BV density, and residue/cyclic trace orientations. It is not a compact Calabi--Yau threefold hypothesis and it does not import compact BCOV, holomorphic anomaly, GW/GV, quintic, OSV/GV, Abel--Jacobi, CoHA, Igusa, Borcherds, or BKM input into the core local SFT.

## Valid attacks

- A137-01, compact-CY import risk: The word "Calabi--Yau" could be read as a compact CY3 target or compact BCOV theorem input. Valid. Healed by defining the datum as only \((\widehat{\mathbb C^2}_0,dz_1\wedge dz_2)\) and by adding explicit inadmissible imports.
- A137-02, orientation versus symplectic ambiguity: The manuscript uses \(\Omega=dz_1\wedge dz_2\) both as the holomorphic volume density and as the symplectic form on the holomorphic surface. Valid. Healed by recording the Poisson tensor, bracket, Hamiltonian vector field convention, and divergence convention together.
- A137-03, BV-pairing overclaim: A cyclic/BV pairing statement could be mistaken for a convergent Costello coefficient-kernel or graph-QME theorem. Valid. Healed by separating the local continuous evaluation pairing from any Tate/coefficient-kernel coevaluation claim.
- A137-04, residue/cyclic-trace underdefinition: The open cyclic trace and principal-part duality need the residue orientation fixed by \(dz_1dz_2\). Valid. Healed by recording the residue basis \(\rho_{a,b}\) and the trace formula.
- A137-05, admissibility firewall missing: Future agents needed a mechanically checkable admissible/inadmissible-use list. Valid. Healed by adding a two-column admissibility table.

## Repairs made

- Added a theorem-grade dictionary entry `Local Calabi--Yau/unimodularity datum` to `local-dictionary.tex`.
- Added an admissible/inadmissible uses table that quarantines compact CY3, CoHA, quintic, OSV/GV, Abel--Jacobi, Igusa, Borcherds, and BKM imports from the local theorem surface.
- Preserved pre-existing staged changes in `local-dictionary.tex` from other agents.

## Exact definitions and formulas

- Local datum:
  \[
    \Omega_{\mathrm{loc}}=dz_1\wedge dz_2
    \quad\text{on}\quad
    \widehat{\mathbb C^2}_0=\operatorname{Spf}\mathbb C[[z_1,z_2]] .
  \]
- Poisson bracket:
  \[
    \{f,g\}
    =
    \frac{\partial f}{\partial z_1}\frac{\partial g}{\partial z_2}
    -
    \frac{\partial f}{\partial z_2}\frac{\partial g}{\partial z_1}.
  \]
- Hamiltonian vector field:
  \[
    \iota_{X_f}\Omega_{\mathrm{loc}}=-df,\qquad
    X_f=(\partial_{z_1}f)\partial_{z_2}-(\partial_{z_2}f)\partial_{z_1},
    \qquad
    X_f(g)=\{f,g\}.
  \]
- Divergence:
  \[
    L_X\Omega_{\mathrm{loc}}=\operatorname{div}_{\Omega_{\mathrm{loc}}}(X)\Omega_{\mathrm{loc}},
    \qquad
    \operatorname{div}_{\Omega_{\mathrm{loc}}}(a_1\partial_{z_1}+a_2\partial_{z_2})
    =
    \partial_{z_1}a_1+\partial_{z_2}a_2,
  \]
  and \(\operatorname{div}_{\Omega_{\mathrm{loc}}}(X_f)=0\).
- Formal disk Poincare lemma:
  \[
    \ker(\partial_{\Omega_{\mathrm{loc}}}:{\rm PV}^1\to{\rm PV}^0)
    \cong
    \{df:f\in\mathbb C[[z_1,z_2]]\}
    \cong
    \mathbb C[[z_1,z_2]]/\mathbb C\cdot 1 .
  \]
- Residue basis:
  \[
    \rho_{a,b}=z_1^{-a-1}z_2^{-b-1}\,dz_1dz_2,\qquad
    \operatorname{Res}_0(\rho_{a,b}z_1^mz_2^n)=\delta_{a,m}\delta_{b,n}.
  \]
- Open cyclic trace:
  \[
    {\rm Tr}_{\rm open}(\eta\otimes u\otimes M)
    =
    \int_{\mathbb R}\eta\;[\epsilon_1\epsilon_2]u\;{\rm Tr}_N(M).
  \]

## Verification commands

- `rg -n -e 'Local Calabi' -e 'Omega_\\{\\\\mathrm\\{loc\\}\\}' -e 'Inadmissible' -e 'compact Calabi' local-dictionary.tex`
- `nl -ba local-dictionary.tex | sed -n '1,190p'`
- `git diff -- local-dictionary.tex`
- `make pdf`

`make pdf` loaded `local-dictionary.tex` successfully. The command exited with status 2 because of an out-of-scope pre-existing TeX error at `main.tex:5103`, where `\drop:open-descendant-action` is parsed as an undefined control sequence and triggers follow-on math-mode errors. The generated `out/main.pdf` was updated by the build, but it is outside Agent 137's writable surface and was not staged.

## Files changed and staged

- `local-dictionary.tex`: changed by Agent 137 on top of pre-existing staged swarm edits; staged after this report was written.
- `reconstitution/swarm-2026-04-30-agent-137-local-unimodularity-dictionary.md`: created and staged after this report was written.

No other files were staged by Agent 137.

## Remaining obligations

- Fix the out-of-scope `main.tex:5103` control-sequence typo or malformed reference before treating the full PDF build as clean.
- Integration owner should continue the compact-CY firewall audit across other agents' surfaces. Agent 137 only inscribed the local dictionary entry and report.
