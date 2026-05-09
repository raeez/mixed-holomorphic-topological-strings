# Agent 214 - Omega/QME Appendix Repair

Status: repaired in `appendix-unreduced-bv-qme.tex`; no commit or push.

## Anchors

- `appendix-unreduced-bv-qme.tex:2487`: normal
  \(\Omega\)-equivariant Costello kernel datum repaired.
- `appendix-unreduced-bv-qme.tex:2520`: finite moving-character set
  \(\mathsf X_{N,M}\) and coefficient ring
  \[
    R_\Omega^{N,M}
      =
    \C[\epsilon_s,\epsilon_1,\epsilon_2,\hbar_\omega]
    [\chi^{-1}\mid\chi\in\mathsf X_{N,M}].
  \]
- `appendix-unreduced-bv-qme.tex:2538`: self-dual branch guard:
  base-change to \(\epsilon_1+\epsilon_2=0\) first; invert only surviving
  nonzero characters; never invert \(\epsilon_1+\epsilon_2\) before
  specialization.
- `appendix-unreduced-bv-qme.tex:2546`: separated parameters
  \[
    \hbar_{\mathrm{QME}},\qquad
    \hbar_{\mathrm{W}},\qquad
    \hbar_\omega .
  \]
- `appendix-unreduced-bv-qme.tex:2631`: normalization branches
  \[
    \nu_\Omega^{\mathrm{res}}=1,\qquad
    \nu_\Omega^{\mathrm{Eu}}
      =
    \sigma_s(\epsilon_s\epsilon_1\epsilon_2)^{-1}.
  \]
- `appendix-unreduced-bv-qme.tex:2662`: scalar map is now an
  associated-graded extractor candidate; a filtered chain lift is supplied
  only after the Hom obstruction test.
- `appendix-unreduced-bv-qme.tex:2704`: QME statement retitled as an
  obstruction criterion.
- `appendix-unreduced-bv-qme.tex:2764`: order-\(n\) residual uses
  \([\hbar_{\mathrm{QME}}^n]\), not bare \(\hbar^n\).
- `appendix-unreduced-bv-qme.tex:2824`: localization supplies habitat,
  not a QME proof.  QME proof still requires chain scalar projection,
  non-scalar row classes, counterterms, primitive transport, and
  \(Q_\Omega\)-centrality homotopies.
- `appendix-unreduced-bv-qme.tex:3426`: centrality homotopy criterion now
  uses the \(\hbar_{\mathrm{QME}}\)-bracket.

Preserved Agent 198 surfaces:

- `appendix-unreduced-bv-qme.tex:2142`: native finite-window
  Costello/QME realization habitat.
- `appendix-unreduced-bv-qme.tex:2234`: constructive non-scalar
  Costello/QME realization criterion.
- `appendix-unreduced-bv-qme.tex:2387`: theta3 source-face row and finite
  obstruction certificate.

## Repairs

The old product-localized ring was replaced by the finite-window
localization \(R_\Omega^{N,M}\).  The moving characters are the nonzero
normal weights
\[
  n\epsilon_s+a\epsilon_1+b\epsilon_2,\qquad
  n\epsilon_s-a\epsilon_1-b\epsilon_2
\]
that occur in the chosen finite package.

The scalar-contact symbol is now
\[
  \nu_\Omega\,
  \hbar_{\mathrm{QME}}\,
  \operatorname{Str}_{\mathrm{cyc}}(\mathfrak m)\,
  [\{f,g\}_\Omega]_0\,\gamma_{\mathbf 1},
  \qquad
  \{f,g\}_\Omega=\hbar_\omega\{f,g\}_{\Omega_{\mathrm{loc}}}.
\]
The Weyl/Moyal deformation parameter is carried separately by
\(A_{\partial,\Omega,\hbar_{\mathrm{W}}}^{\mathrm{pp},w,M}(I)\).

The theorem surface is sharpened.  Normal localization gives the habitat:
coefficient ring, \(Q_\Omega\), normal contractions, and equivariant
propagator data.  It does not solve the QME.  The QME proof requires the
displayed Hom obstruction tower for the scalar projection, the non-scalar
\(H^1\)-row classes, explicit counterterms, \(\varprojlim^1H^0\) primitive
compatibility, and centrality homotopies.

## Commands

```bash
git status --short
git diff -- appendix-unreduced-bv-qme.tex
git diff --cached -- appendix-unreduced-bv-qme.tex
rg -n -F -e 'R_\Omega^{N,M}' -e '\hbar_{\mathrm{QME}}' -e '\hbar_{\mathrm{W}}' -e '\hbar_\omega' -e '\nu_\Omega^{\mathrm{res}}' -e '\nu_\Omega^{\mathrm{Eu}}' -e '\epsilon_s' -e '\epsilon_1' -e '\epsilon_2' appendix-unreduced-bv-qme.tex
git diff --check -- appendix-unreduced-bv-qme.tex
git add appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-214-omega-qme-appendix-repair.md
git diff --cached --check -- appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-214-omega-qme-appendix-repair.md
sed -n '2487,2866p' appendix-unreduced-bv-qme.tex | rg -n -F -e '\varepsilon_s' -e '\varepsilon_1' -e '\varepsilon_2' -e 'R_\Omega=' -e 'R_\Omega =' -e '(\varepsilon_s\varepsilon_1\varepsilon_2)^{-1}' -e '\}_{\hbar,M,\Omega}' -e '[[\hbar]]' -e '[\hbar^'
rg -n -i -e 'literal rotation' -e 'rotate' -e 'rotation' -e 't,s' appendix-unreduced-bv-qme.tex
rg -No '\\label\{[^}]+\}' appendix-unreduced-bv-qme.tex | sort | uniq -d
git status --short -- appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-214-omega-qme-appendix-repair.md
```

Results:

- `git diff --check -- appendix-unreduced-bv-qme.tex`: no output.
- `git diff --cached --check -- appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-214-omega-qme-appendix-repair.md`: no output.
- Old Omega-language scan on `2487,2866p`: no hits.
- Rotation scan: no hits.
- Duplicate-label scan on the appendix: no output.
- Final owned-path status: `M  appendix-unreduced-bv-qme.tex`,
  `A  reconstitution/swarm-2026-04-30-agent-214-omega-qme-appendix-repair.md`.
