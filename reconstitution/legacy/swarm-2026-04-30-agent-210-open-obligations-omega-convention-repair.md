# Agent 210 Report: Open Obligations Omega Convention Repair

Status: implemented in `open-obligations.tex`; report written here.

## Concurrency

Before editing I inspected `open-obligations.tex` with `git status`,
`git diff -- open-obligations.tex`, and
`git diff --cached -- open-obligations.tex`.  The file already carried the
radial, theta-row, stratified, and trace additions.  During this run the
pre-existing open-obligations baseline was staged by another process.
Current state is therefore `MM open-obligations.tex`: the cached diff is
the pre-existing 563/38-line integration, and the unstaged diff is this
Omega repair.  I did not stage, revert, or rewrite the cached content.

## Claim Attacked

The open-obligations Omega entries still allowed four convention
collapses: Omega weights written with `\varepsilon_*`, coefficient
targets over an undeclared Laurent field, one bare `\hbar` used for QME,
Weyl, and equivariant scalarization, and residue/Euler normalization
treated as a single choice.  That could make normal localization look
like a Costello QME proof.

## Heal

The repaired anchors in `open-obligations.tex` are:

- `565-583`: finite-window character localization
  \[
    R_\Omega^{N,M}
    =
    \C[\epsilon_s,\epsilon_1,\epsilon_2,\hbar_\omega]
    [\chi^{-1}\mid\chi\in\mathsf X_{N,M}]
  \]
  with self-dual base-change before inversion.
- `588-640`: stratified target over
  \(R_\Omega^{N,M}[[\hbar_{\mathrm{QME}}]]\), brane Weyl branch over
  \(\hbar_{\mathrm{W}}\), and separate
  \(\hbar_{\mathrm{QME}},\hbar_{\mathrm{W}},\hbar_\omega\).
- `665-698`: centrality and curvature use the QME branch where relevant;
  the text states that the Omega habitat does not prove the brane-defect
  QME.
- `721-770`: trace state target and normalization branches:
  \[
    \nu_\Omega^{\mathrm{res}}=1,\qquad
    \nu_\Omega^{\mathrm{Eu}}
    =
    \sigma_s(\epsilon_s\epsilon_1\epsilon_2)^{-1},
    \qquad
    \nu_\Omega^{\mathrm{Eres}}
    =
    \sigma_s(\epsilon_s\epsilon_1\epsilon_2)^{-1}.
  \]
- `772-808`: Ward identities and large-\(N\) scaling are stated as
  trace/QME obligations, not consequences of localization.

The recent `\theta_3` row and radial/Weyl finite-certificate additions
were preserved at `472-515` and `833-885`.

## Residual Out-of-Scope Files

No disallowed TeX file was edited.  The targeted out-of-scope scan still
finds the older collapsed Omega convention in
`appendix-unreduced-bv-qme.tex:2498-2529` and
`appendix-unreduced-bv-qme.tex:2606`.  `abstract.tex` and
`theorem-lanes.tex` did not match the searched residual patterns in the
latest scan.

## Commands

Context and diff inspection:

```bash
sed -n '1,240p' CLAUDE.md
sed -n '1,260p' /Users/raeez/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
git status --short
git diff -- open-obligations.tex
git diff --cached -- open-obligations.tex
nl -ba open-obligations.tex | sed -n '559,820p'
```

Verification:

```bash
git diff --check -- open-obligations.tex
git diff --cached --check -- open-obligations.tex
rg -n -F -e '\varepsilon_s' -e '\varepsilon_1' -e '\varepsilon_2' open-obligations.tex || true
rg -n -F -e 'R_\Omega^{N,M}' -e '\hbar_{\mathrm{QME}}' -e '\hbar_{\mathrm{W}}' -e '\hbar_\omega' -e '\nu_\Omega^{\mathrm{res}}' -e '\nu_\Omega^{\mathrm{Eu}}' open-obligations.tex
rg -n -F -e '\operatorname{Ch}_{\C((\epsilon_s,\epsilon_1,\epsilon_2))[[\hbar]]}' -e '\operatorname{Ch}_{\C((\varepsilon_s,\varepsilon_1,\varepsilon_2))[[\hbar]]}' -e '(\varepsilon_s\varepsilon_1\varepsilon_2)^{-1}' -e 'Weyl}_\hbar' -e 'P_{0,\hbar}' open-obligations.tex || true
rg -n -F -e '\theta_3' -e 'Radial/Weyl finite certificates' -e 'R^{\mathrm{free}}_{a,b}' -e 'C_{\theta_3}' open-obligations.tex
rg -n -F -e '\varepsilon_s' -e '\varepsilon_1' -e '\varepsilon_2' -e '(\varepsilon_s\varepsilon_1\varepsilon_2)^{-1}' -e '\C((\epsilon_s,\epsilon_1,\epsilon_2))[[\hbar]]' abstract.tex appendix-unreduced-bv-qme.tex theorem-lanes.tex || true
```

Results: `git diff --check` returned no output.  The open-obligations
negative scans returned no collapsed Omega `\varepsilon_*`, product-only
Euler localization, old stratified Laurent target, `Weyl_\hbar`, or
`P_{0,\hbar}` occurrence in the repaired Omega slice.
