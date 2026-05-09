# Swarm 2026-04-30 Agent 003 Local Dictionary Report

Lane: local dictionary / type system.

Owned edit: `local-dictionary.tex`.

## Claim Attacked

The 04:11 critique attacks symbol/type collapse in the local Hamiltonian
dictionary: \(c\)-coordinates versus \(u\)-coordinates, \(H_I\),
\(\rho_I\), \(\eta^I\), \(\Psi\)-labels, open traces, Matlis
principal parts, and the negative-transpose coadjoint action.

## Repair

The dictionary now has an explicit type gate:

\[
  \mathcal I=\{(a,b)\in\mathbb Z_{\geq0}^2:\ a+b>0\},\qquad
  H_I=z_1^az_2^b,\quad
  \rho_I=z_1^{-a-1}z_2^{-b-1}dz_1dz_2,\quad
  \eta^I=\rho_I[1].
\]

The CE/PV map is typed as
\[
  c^I\mapsto\theta^I,\qquad u_I\mapsto O_I.
\]
Here \(c^I\) is dual to \(H_I\); \(u_I\) is dual to \(\eta^I\).
Boundary Hamiltonians are sourced by \(u_I\), not by \(c^I\).

The Matlis target is
\[
  \mathcal P=\operatorname{Ann}_{\mathrm{res}}(\mathbb C1)
  \cong\mathfrak h^\vee_{\mathrm{cont}},
  \qquad
  \rho_{a,b}=z_1^{-a-1}z_2^{-b-1}dz_1dz_2.
\]
The coadjoint action is recorded as
\[
  \langle f\cdot\rho,g\rangle=-\langle\rho,\{f,g\}\rangle,
  \qquad
  z_1^p z_2^q\cdot\rho_{a,b}
  =-(pb-qa+p-q)\rho_{a-p+1,b-q+1},
\]
with negative-index and scalar targets equal to \(0\).

The PBW one-\(\psi\) action remains a different module:
\[
  H_{p,q}\cdot\widetilde\Psi_{a,b}
  =(pb-qa)\widetilde\Psi_{a+p-1,b+q-1}.
\]
Thus \(\Psi_{a,b}\mapsto\rho_{a,b}\) is only a label comparison when a
separate Fourier--Rees polarization is named; it is not an
\(\mathfrak h\)-module map.

The open trace source is
\[
  u_{a(t)dt\otimes f}\longmapsto
  B_f(a)=\int_I a(t)\overline{\operatorname{Tr}
  f(\phi_1(t),\phi_2(t))}\,dt.
\]

Weighted symbols are now typed:
\[
  C_{-,+}=\sum_I H_I\otimes\rho_I\in H_-\widehat\otimes P_+,
  \qquad
  \Theta_{-,+}=\sum_IH_I\otimes\theta^I+\sum_I\eta^I\otimes O_I.
\]
Both are recorded as construction obligations until the coefficient and
MC lanes prove convergence in the stated completed habitats; the
dictionary does not promote them to constructed Costello or MC objects.

## Local Anchors

- `local-dictionary.tex:218`: index/type convention.
- `local-dictionary.tex:236`: source/habitat/target type gate.
- `local-dictionary.tex:560`: Matlis principal-part module.
- `local-dictionary.tex:622`: open trace source \(u_{a(t)dt\otimes f}\).

## Checks

- `local-dictionary.tex` contains no claim that \(\Psi_{a,b}\) and
  \(\rho_{a,b}\) are bases of the same module.
- The type gate explicitly names the habitat, source, and target/action
  for \(H_I,\rho_I,\eta^I,c^I,u_I,\theta^I,O_I,\Psi_I,B_f(a),
  C_{-,+},\Theta_{-,+},P_\hbar\).
- The pre-existing Moyal correction was preserved:
  \(\bar A_\hbar\) is now the formal Moyal Lie quotient, not an
  associative quotient by constants.

## Remaining Obligations

The dictionary does not prove the weighted estimates, diagonal
convergence, or MC cancellation.  Those belong to the coefficient and MC
lanes.
