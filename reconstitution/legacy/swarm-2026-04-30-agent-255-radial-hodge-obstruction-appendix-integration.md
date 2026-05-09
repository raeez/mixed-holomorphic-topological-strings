# Agent 255: radial Hodge obstruction appendix integration

Date: 2026-04-30.

Owned write paths:

- `appendix-radial-parts-moyal.tex`
- `reconstitution/swarm-2026-04-30-agent-255-radial-hodge-obstruction-appendix-integration.md`

## Stable Core

Agent 248's decorated Hodge obstruction theorem was integrated into the
radial appendix near the all-bidegree obstruction block.  The manuscript now
records the exact finite-dimensional obstruction:
\[
  \Pi^{\mathrm{harm}}_{a,b}R^{\mathrm{free}}_{a,b}=0
\]
for the decorated graph complex is equivalent to solving
\[
  C^+_{a,b}(K_{a,b})=R^{\mathrm{free}}_{a,b},\qquad
  K_{a,b}\in\ker\partial .
\]
The theorem does not assert that the projection vanishes in all bidegrees.
If the projection is nonzero, its detecting functional is the left-cokernel
obstruction.

## Repairs Made

- Defined the two-colour necklace graph \(G_{a,b}\), its incidence map
  \(\partial W=[WYX]-[WXY]\), and \(Z_{a,b}=\ker\partial\).
- Replaced the bare correction map by the positive decorated map
  \[
    C^+_{a,b}(W)=
    \pi_+\mathcal N_{\mathrm{free}}\operatorname{Tr}(WM),
    \qquad
    A_{a,b}=C^+_{a,b}|_{Z_{a,b}}.
  \]
- Added the decorated Laplacian
  \[
    \Delta^{\mathrm{dec}}_{a,b}=A_{a,b}A_{a,b}^{*}
  \]
  and the harmonic projection
  \(\Pi^{\mathrm{harm}}_{a,b}\).
- Added the potential-form identity
  \[
    \lambda\pi_+\mathcal N_{\mathrm{free}}(E_{a,b,N})
    =
    \phi_\lambda(T_{a,b})
  \]
  for every decorated left-cokernel functional.
- Recorded why the bare necklace graph Green operator is insufficient: it
  solves only the classical incidence equation \(\partial c=T_{a,b}\), while
  the quantum correction equation lives in the positive PBW diagram target
  and sees contractions, split traces, and the Capelli term.

Finite certificate statements for \(K_{4,4}\), the edge PBW strip, and the
listed finite obstruction certificates were preserved.

## Attack-Heal Ledger

```yaml
- id: A255-01
  severity: 2
  status: healed
  lens: theorem strength
  target: all-bidegree radial/Weyl homotopy
  claim: the appendix should close the all-bidegree homotopy
  broken_step: Agent 248 did not prove uniform vanishing of the harmonic row
  evidence_ref: reconstitution/swarm-2026-04-30-agent-248-radial-necklace-hodge-homotopy-construction-push.md
  minimal_heal: state only the equivalence with Pi_harm R_free=0
  residual: prove the potential identity in all bidegrees or exhibit a failing row

- id: A255-02
  severity: 2
  status: healed
  lens: decorated complex
  target: graph Green operator
  claim: the bare incidence Green operator supplies K_ab
  broken_step: the correction equation is A K=R in the positive diagram target,
    not partial K=R in the necklace incidence complex
  minimal_heal: define A=C^+|_{ker partial} and Delta_dec=A A^*
  residual: none for the obstruction theorem

- id: A255-03
  severity: 3
  status: healed
  lens: finite certificates
  target: existing low-bidegree certificates
  claim: integrating the Hodge theorem may overwrite finite certificates
  broken_step: finite certificates are evidence for specific bidegrees, not
    the all-bidegree theorem
  minimal_heal: leave the finite certificate propositions unchanged and
    place the Hodge theorem before them
  residual: none
```

## Verification

Commands run:

```text
git diff --check -- appendix-radial-parts-moyal.tex
git status --short -- appendix-radial-parts-moyal.tex reconstitution/swarm-2026-04-30-agent-255-radial-hodge-obstruction-appendix-integration.md
git diff --numstat -- appendix-radial-parts-moyal.tex
git diff --check --cached -- appendix-radial-parts-moyal.tex reconstitution/swarm-2026-04-30-agent-255-radial-hodge-obstruction-appendix-integration.md
git diff -- appendix-radial-parts-moyal.tex reconstitution/swarm-2026-04-30-agent-255-radial-hodge-obstruction-appendix-integration.md
git diff --cached --stat -- appendix-radial-parts-moyal.tex reconstitution/swarm-2026-04-30-agent-255-radial-hodge-obstruction-appendix-integration.md
```

The unstaged and cached whitespace checks returned clean.  After staging,
there was no unstaged diff on the owned paths.  No build was run:
`make pdf` would write shared build artifacts outside the assigned
ownership surface.
