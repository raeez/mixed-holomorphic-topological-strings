# Agent 205 Report: Omega Convention TeX Implementation

## Claim Attacked

Agent 200's Omega convention gate could remain report-only while the
controlled dictionary/ledger slice still allowed three confusions:
Omega weights written with the open Ext glyphs, localization by only the
Euler product, and a collapsed \(\hbar\)-notation that makes an Omega
normal contraction look like a QME solution.

## Implementation

Edited only:

- `local-dictionary.tex`
- `claim-strength-ledger.tex`
- `reconstitution/swarm-2026-04-30-agent-205-omega-convention-tex-implementation.md`

The TeX slice now uses
\[
  \epsilon_s,\epsilon_1,\epsilon_2
\]
for Omega weights and reserves
\[
  \varepsilon_1,\varepsilon_2
\]
for the already-local open Ext orientation
\([\varepsilon_1\varepsilon_2]\).

The finite-window localization is recorded as
\[
  R_\Omega^{N,M}
  =
  \C[\epsilon_s,\epsilon_1,\epsilon_2,\hbar_\omega]
  [\chi^{-1}\mid \chi\in\mathsf X_{N,M}],
\]
where \(\mathsf X_{N,M}\) contains the nonzero moving characters
\[
  n\epsilon_s+a\epsilon_1+b\epsilon_2,\qquad
  n\epsilon_s-a\epsilon_1-b\epsilon_2
\]
that occur in the chosen finite normal window.  The self-dual branch is
base-changed before further inversion, so \(\epsilon_1+\epsilon_2\) is
not inverted there.

The three \(\hbar\)-roles are separated:
\[
  \hbar_{\mathrm{QME}},\qquad
  \hbar_{\mathrm{W}},\qquad
  \hbar_\omega .
\]
\(\hbar_{\mathrm{QME}}\) is the Costello/BV loop-counting parameter;
\(\hbar_{\mathrm{W}}\) is the Weyl/Moyal deformation parameter; and
\(\hbar_\omega\) scalarizes the equivariant Poisson bracket.  A Weyl
branch may identify \(\hbar_{\mathrm{W}}=\hbar_\omega\).  No
identification with \(\hbar_{\mathrm{QME}}\) is asserted.

The normalization branches are recorded as
\[
  \nu_\Omega^{\mathrm{res}}=1,\qquad
  \nu_\Omega^{\mathrm{Eu}}
  =
  \sigma_s(\epsilon_s\epsilon_1\epsilon_2)^{-1}.
\]
The text keeps them separate until a comparison theorem fixes the sign
and factor.

## Attack-Heal Result

- Glyph attack: healed in owned TeX; out-of-scope `abstract.tex`,
  `appendix-unreduced-bv-qme.tex`, and `open-obligations.tex` still have
  Omega weights written as \(\varepsilon\).
- Localization attack: healed in owned TeX by finite-window
  \(R_\Omega^{N,M}\); out-of-scope theorem lanes already contain a
  compatible finite-window character list.
- Quantum-bookkeeping attack: healed in owned TeX by separating
  \(\hbar_{\mathrm{QME}}\), \(\hbar_{\mathrm{W}}\), and \(\hbar_\omega\).
- Normalization attack: healed in owned TeX by explicit residue and Euler
  \(\nu_\Omega\)-branches.
- QME-strength attack: guarded.  The ledger says the notation gate is not
  a QME theorem and the Costello curvature equation remains an obstruction
  equation over \(\hbar_{\mathrm{QME}}\).

## Residual TeX Anchors

Out-of-scope anchors for the integration owner:

- `abstract.tex:196-208` still uses \(\varepsilon_s,\varepsilon_1,\varepsilon_2\)
  for Omega weights.
- `appendix-unreduced-bv-qme.tex:2498-2608` still uses \(\varepsilon\)-Omega
  weights, localizes by the Euler product, and uses a collapsed
  \(R_\Omega\) convention.
- `open-obligations.tex:572-605` and `open-obligations.tex:690-720`
  still use \(\varepsilon\)-Omega weights and collapsed \(\hbar\)
  coefficient language.

## Checks

Commands run after edits:

```bash
git diff --check -- local-dictionary.tex claim-strength-ledger.tex reconstitution/swarm-2026-04-30-agent-205-omega-convention-tex-implementation.md
rg -n -F -e 'R_\Omega^{N,M}' -e '\hbar_{\mathrm{QME}}' -e '\hbar_{\mathrm{W}}' -e '\hbar_\omega' -e '\nu_\Omega^{\mathrm{res}}' -e '\nu_\Omega^{\mathrm{Eu}}' local-dictionary.tex claim-strength-ledger.tex reconstitution/swarm-2026-04-30-agent-205-omega-convention-tex-implementation.md
rg -n -F -e '\varepsilon_s' -e '\varepsilon_1' -e '\varepsilon_2' local-dictionary.tex claim-strength-ledger.tex
rg -n -F -e '\varepsilon_s' -e '\varepsilon_1' -e '\varepsilon_2' -e 'R_\Omega=' -e 'R_\Omega =' -e '(\varepsilon_s\varepsilon_1\varepsilon_2)^{-1}' abstract.tex appendix-unreduced-bv-qme.tex open-obligations.tex
rg -n -F -e 'not a QME theorem' -e 'not a Costello graph/QME theorem' -e 'separate QME obstruction' -e 'obstruction equation over \(\\hbar_{\mathrm{QME}}\)' local-dictionary.tex claim-strength-ledger.tex reconstitution/swarm-2026-04-30-agent-205-omega-convention-tex-implementation.md
```

Results:

- `git diff --check` returned no output.
- Formula scan found \(R_\Omega^{N,M}\), all three \(\hbar\)-symbols,
  and both \(\nu_\Omega\)-branches in the owned slice.
- Owned-TeX `\varepsilon` scan returned only the open Ext orientation
  uses in `local-dictionary.tex`.
- Residual scan found the out-of-scope anchors listed above.
