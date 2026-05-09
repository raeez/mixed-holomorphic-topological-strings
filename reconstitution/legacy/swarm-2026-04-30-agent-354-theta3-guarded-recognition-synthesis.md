# Agent 354: Theta3 Guarded Recognition Synthesis

Status: report-only. No TeX, script, figure, bibliography, PDF, or build
artifact was edited.

## Inputs

Read the repository and harness controls:

- `CLAUDE.md`
- `AGENTS.md`
- `/Users/raeez/ecosystem/INVARIANTS.md`
- `/Users/raeez/ecosystem/AGENTS-HARNESS.md`
- `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`

Read the assigned swarm reports:

- `reconstitution/swarm-2026-04-30-agent-344-nonscalar-qme-patch-blueprint.md`
- `reconstitution/swarm-2026-04-30-agent-346-theta3-bianchi-counterterm-supremum.md`
- `reconstitution/swarm-2026-04-30-agent-350-nonscalar-qme-blueprint-attack.md`

Checked the live manuscript surfaces:

- `main.tex:8613-9118`
- `appendix-unreduced-bv-qme.tex:2077-2642`
- `open-obligations.tex:900-957`
- `theorem-lanes.tex:3540-3611`
- `claim-strength-ledger.tex:500-550`
- `claim-strength-ledger.tex:924-994`
- `commands.tex`
- `mathmacros.tex`

The working tree already has concurrent modifications in
`main.tex`, `appendix-unreduced-bv-qme.tex`, `open-obligations.tex`,
`theorem-lanes.tex`, and `claim-strength-ledger.tex`. They were not touched.

## Verdict

The corrected insertion plan is not a positive theorem. The live manuscript
should retain the current obstruction:
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T,
  \qquad
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^* .
\]
The covector kills \(A_D^2\), detects \(r_2\), and detects the desired
Bianchi target:
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}(r_2)=1,\qquad
  \widetilde\lambda_{02,\mathfrak b}((0,0,-1)^T)=-1 .
\]
Thus the present lower finite-row habitat contains no scalar-zero
local-functional column \(B^2_{02,20}\) with
\[
  d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}.
\]

Agent 344's matrix calculation is correct as a formal recognition gate:
if a genuine column \(A_B^2=(0,0,-1)^T\) is supplied, then
\[
  \begin{pmatrix}
    -2&0\\
     2&0\\
     1&-1
  \end{pmatrix}
  \binom{1}{1}
  =
  (-2,2,0)^T=-r_2 .
\]
Agent 346 proves that this column is absent from the current habitat. Agent
350 correctly blocks insertion as a positive theorem and requires the block
to become a guarded recognition criterion or a habitat-construction target.

## Insertion Plan

Do not append Agent 344's theorem block after
`prop:theta-three-finite-window-acceptance-gate`. The current manuscript
already contains the obstruction and target at `main.tex:8997-9054` and in
the appendix at `appendix-unreduced-bv-qme.tex:2501-2642`.

If a later manuscript edit is authorized, use one of two controlled moves.

First, for minimal integration, replace the existing target paragraphs at
`main.tex:9036-9054`, `appendix-unreduced-bv-qme.tex:2561-2604`,
`open-obligations.tex:940-957`, and `theorem-lanes.tex:3593-3611` with a
short reference to the guarded criterion below. Do not duplicate the same
matrix and Roos discussion in each file.

Second, if the manuscript needs a formal theorem-lane object, insert a
proposition immediately after the proof of
`prop:theta-three-finite-window-acceptance-gate` and before
`prob:tate-coefficient-descendant-lift`. The title must mark recognition, not
existence. The appendix may carry the same statement only if it replaces
`prop:app-theta-three-bianchi-exposed-lower-gate` or is cross-referenced from
it.

## Exact Future Wording

Use `prop`, not `thm`.

```tex
\begin{prop}[Guarded recognition criterion for a supplied \(\theta_3\)
Bianchi column]
\label{prop:theta-three-bianchi-column-recognition}
  Work in a native finite-window realization habitat of
  Definition~\ref{def:app-native-finite-window-realization-habitat}.  Thus
  the scalar projection
  \[
    \widehat\sigma_{\mathrm{sc},M}\colon
    \mathfrak Q^\bullet_{\mathcal G,M}(I)\to
    C^\bullet_{\mathrm{Lie}}(\bar A;\C\gamma_{\mathbf 1})[1][[\hbar]]
  \]
  is a filtered chain map, and
  \(\mathcal K^\bullet_{\mathrm{ns},M}(I)=
  \ker\widehat\sigma_{\mathrm{sc},M}\) is a complex.

  Suppose the package supplies, for every \(M\ge2\), a lower
  Bianchi-exposed row basis containing
  \[
    E^M_{\nu_{02}},\quad E^M_{\nu_{20}},\quad \mathfrak b^M,
  \]
  and a source-coordinate primitive
  \(D^M_{02,20}\in\mathcal K^0_{\mathrm{ns},M}(I)\) satisfying the
  row-coordinate identity
  \[
    d_{\mathrm{ns},M}D^M_{02,20}
    =
    -2E^M_{\nu_{02}}+2E^M_{\nu_{20}}+\mathfrak b^M .
  \]
  This identity is part of the supplied \(M\)-window row table; it is not
  inferred from the \(N=2\) calculation.

  Suppose also that the same habitat supplies a genuine degree-zero local
  functional
  \[
    B^M_{02,20}\in\mathcal K^0_{\mathrm{ns},M}(I)
  \]
  represented by a regular-density counterterm or by a graphwise
  wavefront-admissible counterterm, with
  \[
    d_{\mathrm{ns},M}B^M_{02,20}=-\mathfrak b^M,\qquad
    \widehat\sigma_{\mathrm{sc},M}(B^M_{02,20})=0 .
  \]

  Finally suppose the row and primitive transition maps are supplied.  For
  \(M\ge N\), put
  \[
    \Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N .
  \]
  The datum must contain scalar-zero cochains
  \(H^{M,N}_{02,20}\in\mathcal K^0_{\mathrm{ns},N}(I)\) with
  \[
    d_{\mathrm{ns},N}H^{M,N}_{02,20}=\Delta^1_{M,N}.
  \]
  The closed degree-zero defects
  \[
    \Delta^0_{M,N}
    =
    \pi_{M,N}B^M_{02,20}
    -B^N_{02,20}
    -H^{M,N}_{02,20}
  \]
  must define a Roos \(1\)-cocycle in
  \(H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I))\), and that Roos cocycle
  must be zero.  Equivalently, an explicit Roos \(0\)-cochain of
  \(H^0\)-classes must be supplied whose coboundary is
  \(([\Delta^0_{M,N}])_{M\ge N}\).

  Then the supplied package passes the lower \(\theta_3\) Bianchi-column
  recognition gate.  For every \(M\),
  \[
    P^M_{02,20}:=D^M_{02,20}+B^M_{02,20}
  \]
  satisfies
  \[
    d_{\mathrm{ns},M}P^M_{02,20}
    =
    -2E^M_{\nu_{02}}+2E^M_{\nu_{20}} .
  \]
  In the \(N=2\) Bianchi-exposed basis
  \((E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})\), the two
  columns \(D^2_{02,20},B^2_{02,20}\) have boundary matrix
  \[
    A^2_{D,B}
    =
    \begin{pmatrix}
      -2&0\\
       2&0\\
       1&-1
    \end{pmatrix},
    \qquad
    A^2_{D,B}(1,1)^T=(-2,2,0)^T=-r_2 .
  \]
  After the supplied Roos-zero adjustment, the primitives are compatible in
  the finite-window inverse system.

  This proposition recognizes a supplied habitat.  It does not construct
  \(B^M_{02,20}\), the scalar projection lift, the row table, the analytic
  local functional, the transition maps, a CE ancestor, a complete
  companion-face table, centrality homotopies, or the full curved
  bulk-to-defect Costello kernel.
\end{prop}
```

Pair it with a construction target, not an existence theorem.

```tex
\begin{prob}[Habitat construction target for the \(\theta_3\) Bianchi column]
\label{prob:theta-three-bianchi-column-habitat}
  Construct a native finite-window realization habitat satisfying
  Proposition~\ref{prop:theta-three-bianchi-column-recognition}.  In
  particular, construct the scalar-chain projection
  \(\widehat\sigma_{\mathrm{sc},M}\), the codimension-two closed marked row
  table containing \(E^M_{\nu_{02}},E^M_{\nu_{20}},\mathfrak b^M\), the
  local-functional primitive \(D^M_{02,20}\), a genuine scalar-zero
  regular-density or graphwise wavefront-admissible counterterm
  \(B^M_{02,20}\) with
  \(d_{\mathrm{ns},M}B^M_{02,20}=-\mathfrak b^M\), and transition data
  killing \(\Delta^1_{M,N}\) and the secondary
  \(\varprojlim^1H^0\) primitive-compatibility class.

  Until these data are constructed, the lower \(\theta_3\) Bianchi column
  remains an exact obstruction in the current finite-row habitat, detected by
  \(\widetilde\lambda_{02,\mathfrak b}\).
\end{prob}
```

## Proof Boundaries

Allowed proof content:

- Expand the supplied identities
  \(dD=-2E_{\nu_{02}}+2E_{\nu_{20}}+\mathfrak b\) and
  \(dB=-\mathfrak b\).
- Verify
  \(d(D+B)=-2E_{\nu_{02}}+2E_{\nu_{20}}\).
- In the \(N=2\) basis, multiply
  \[
    A^2_{D,B}(1,1)^T=(-2,2,0)^T=-r_2 .
  \]
- Compute
  \[
    d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)
    =
    -\pi_{M,N}\mathfrak b^M+\mathfrak b^N
    =
    \Delta^1_{M,N}.
  \]
- Use the supplied \(H^{M,N}\) and explicit Roos coboundary witness to pass
  from fixed-window primitives to compatible tower primitives.

Forbidden proof content:

- Do not infer the existence of \(B^M_{02,20}\) from the formal matrix
  \(A_B^2=(0,0,-1)^T\).
- Do not infer local-functional exactness from source exactness of
  \(\zeta^0_2\).
- Do not assume that \(\mathcal K_{\mathrm{ns},M}\) is a complex unless
  \(\widehat\sigma_{\mathrm{sc},M}\) is a filtered chain map on the enlarged
  habitat.
- Do not extrapolate the all-window \(D^M\) source-face identity from the
  lower \(N=2\) computation without an \(M\)-window row table.
- Do not replace the Hom-valued Bianchi transport by diagonal source-face
  transport.
- Do not treat Costello's general BV/RG formalism, Costello--Li flat
  open-closed BCOV, or compact Calabi-Yau analogies as proof of this local
  counterterm.
- Do not claim a CE ancestor, complete companion-face table, centrality
  homotopy, or curved bulk-to-defect QME kernel from this recognition
  criterion.

## Final Claim Status

The theta3 Bianchi column is a guarded recognition criterion and a
habitat-construction target. It is not presently a positive theorem.

The current exact theorem surface is:

- proved fixed-window obstruction in the present lower habitat;
- formal matrix acceptance if a genuine \(B\)-column is supplied;
- open construction of the scalar-zero local functional, its analytic
  admissibility, its scalar-chain projection habitat, and its compatible
  Roos transport.
