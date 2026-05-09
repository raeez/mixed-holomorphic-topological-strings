# Agent 181 Report: Controlled CxR Reduction

## Claim Attacked

The reduction claim that
\[
  \pi(t,s;z_1,z_2)=(t;z_1)
\]
can produce a \(C\times R\) curve theory by contracting \(s\), pushing
along \(z_2\), and then importing a one-dimensional chiral/BRST/Zhu
surface.

## Verdict

Stable core exists only for the retained-\(z_2\) branch:
\[
  \mathfrak h_{\mathrm{red}}
  =
  \mathbb C[[z_1]][[z_2]]/\mathbb C\cdot1,
  \qquad
  \mathcal P_{\mathrm{red}}
  =
  \operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)
  \subset H^2_{(z_1,z_2)}(\mathbb C[[z_1,z_2]])\,dz_1dz_2.
\]
A one-variable quotient \(\mathbb C[[z_1]]/\mathbb C\) is false for this
purpose.

## Failure Modes Found

- Killing \(z_2\) kills the Hamiltonian bracket.  The required bracket is
  \[
    \{f,g\}_{\mathrm{red}}
    =
    \partial_{z_1}f\,\partial_{z_2}g
    -
    \partial_{z_2}f\,\partial_{z_1}g.
  \]
- Literal residue along \(z_2\) keeping only \(b=0\) principal parts is not
  stable: \(z_1\cdot\rho_{a,0}=-\rho_{a,1}\).
- The brane image is \(L_{\mathrm{red}}=\mathbb R_t\times\{z_1=0\}\),
  but the second matrix \(Y=\phi_2\) remains in the coefficient/open
  algebra.
- The scalar class survives:
  \[
    \operatorname{Ob}^{\mathrm{red}}_{\mathrm{sc}}
    =
    \hbar N\,\omega(f,g)\int a(t)b(t)\gamma_{\mathbf1}(t)\,dt.
  \]
- Moyal compatibility forces retained \(z_2\):
  \[
    f*g=m\circ\exp\left(\frac{\hbar}{2}
    (\partial_{z_1}\otimes\partial_{z_2}
    -\partial_{z_2}\otimes\partial_{z_1})\right)(f\otimes g).
  \]

## Healed Construction

Use \(\pi_!\) as a controlled pushforward with:

1. compact-support de Rham contraction along \(s\),
   \(p_s(\alpha)=\int_J\alpha\), \(i_s(1)=\lambda_Jds\), and
   \(dK_s+K_sd=\operatorname{id}-i_sp_s\);
2. a mode-retaining \(z_2\) datum, or an equivalent full
   principal-part residue-pairing model;
3. coefficient algebra \(\mathfrak g_{\mathrm{red}}
   =\mathfrak h_{\mathrm{red}}\ltimes\mathcal P_{\mathrm{red}}[1]\);
4. brane evaluation \(f\mapsto\overline{\operatorname{Tr}f(X,Y)}\);
5. the existing scalar-anomaly alternatives and Weyl/Capelli
   normalization.

Full thread written to
`reconstitution/controlled-CxR-reduction-thread-2026-04-30.md`.

## Manuscript Edits Needed

No main/theorem file was edited.  A manuscript edit is needed only if the
paper wants to assert a reduced Dirac BRST chiral algebra, Zhu bridge, or
\(SC^{\mathrm{ch},\mathrm{top}}\) comparison as a theorem.  That edit
should add a controlled \(C\times R\) theorem lane with the maps and
obstruction vector in the thread file.

## Checks

Read-only anchors inspected: `CLAUDE.md`, `AGENTS.md`,
`reconstitution/critique-refresh-2026-04-30-0957-ingestion-and-swarm-plan.md`,
`reconstitution/local-theorem-obligations-2026-04-30.md`,
`reconstitution/chiral-algebra-construction-thread-2026-04-30.md`,
`main.tex`, `theorem-lanes.tex`, `local-dictionary.tex`,
`open-obligations.tex`, and the relevant Vol II `SC^{ch,top}` passage.

No build run.  The changes are markdown-only reconstitution artifacts.
