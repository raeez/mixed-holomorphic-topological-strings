# Agent 184 Report: Equivariant Weighted Kernels

Status: patched owned weighted-completion surface. No commit.

Owned paths:

- `tate-T1-weighted-completion.tex`
- `reconstitution/swarm-2026-04-30-agent-184-equivariant-weighted-kernels-0957.md`

## Stable Core

The normal \(\Omega\)-weights give a theorem-grade finite-window
coefficient kernel only after the character set, inversions, and
normalization are named.

For a finite normal/Hamiltonian window
\[
  \mathsf W_{N,M}
  =
  \{(n,a,b)\mid 0\le n\le N,\ a,b\ge0,\ 1\le a+b\le M\},
\]
the Hamiltonian character is
\[
  \chi^H_{n,a,b}
  =
  n\epsilon_s+a\epsilon_1+b\epsilon_2.
\]
For the residue-dual principal-part label with the same \(s\)-weight,
\[
  \chi^\vee_{n,a,b}
  =
  n\epsilon_s-a\epsilon_1-b\epsilon_2.
\]
Finite-window nonresonance means every character inverted in the chosen
moving normal summands remains nonzero. All-window analytic use requires
the stronger \(q\)-moderate small-denominator bound
\[
  |\chi_{n,a,b}|^{-1}\le A Q^{n+a+b}.
\]

The diagonal coefficient Casimir is
\[
  C_{\Omega,w}^{N,M}
  =
  \sum_{\alpha\in\mathsf A_{N,M}}
    e_{\alpha,w}\otimes e^\alpha_{w^{-1}},
  \qquad
  e_{\alpha,w}=w(d(\alpha))e_\alpha,\quad
  e^\alpha_{w^{-1}}=w(d(\alpha))^{-1}e^\alpha.
\]
It is a strict Mittag-Leffler finite-window kernel.

If the normal Koszul numerator satisfies
\[
  Q_\Omega k^{\mathrm{Kos}}_\alpha
  +k^{\mathrm{Kos}}_\alpha Q_\Omega
  =
  \chi_\alpha\,\operatorname{id}_\alpha,
\]
then the localized normal contracting kernel is
\[
  H_{\Omega,w}^{N,M}
  =
  \sum_{\alpha\in\mathsf A^{\mathrm{mov}}_{N,M}}
    \chi_\alpha^{-1}
    e_{\alpha,w}\otimes e^\alpha_{w^{-1}}
    \otimes k^{\mathrm{Kos}}_\alpha,
\]
with
\[
  Q_\Omega H_{\Omega,w}^{N,M}
  +H_{\Omega,w}^{N,M}Q_\Omega
  =
  \operatorname{id}-\operatorname{pr}_{\chi=0}.
\]
Zero characters are resonant summands, not regularizable denominators.

Residue and Euler conventions do not change the coefficient Casimir. They
change scalar-contact and trace rows:
\[
  \nu_\Omega^{\mathrm{res}}=1,\qquad
  \nu_\Omega^{\mathrm{Eu}}
  =
  \sigma_s(\epsilon_s\epsilon_1\epsilon_2)^{-1}.
\]
The comparison is \(K_{\Omega,w,\mathrm{res}}\mapsto
\nu_\Omega^{\mathrm{Eu}}K_{\Omega,w,\mathrm{res}}\). Mixing the two without
this scalar is the normalization obstruction.

The Costello QME remains controlled by
\[
  \operatorname{Ob}^{\mathrm{QME}}_{\Omega,w}
  =
  \left(
    \mathcal R_{\Omega},
    \operatorname{ob}_{\Omega,\nu},
    \{\mathfrak s_{n,\Omega}\}_{n\ge1},
    \{(([\mathfrak o^{\mathrm{ns}}_{n,\Omega,M}])_M,
      \lambda_{n,\Omega})\}_{n\ge1}
  \right).
\]
The weighted equivariant kernel package promotes to a Costello
brane-defect QME solution exactly on the common zero locus of this vector.

## Valid Attacks

```yaml
- id: A1-184-01
  severity: 1
  status: healed
  lens: finite-window kernel convergence
  target: tate-T1-weighted-completion.tex, weighted/equivariant kernel lane
  claim: Normal Omega weights automatically give a convergent weighted Tate kernel.
  broken_step: The denominators are characters; they require a named localized coefficient ring and nonresonance. Analytic all-window use needs a quantitative small-denominator bound.
  evidence_type: proof_gap
  evidence_ref: defn:wt-omega-normal-window; thm:wt-omega-kernel-admissibility
  confidence: high
  blast_radius: false all-window kernel convergence and false analytic boundedness
  minimal_heal: Add finite-window character ring, nonresonance, q-moderate condition, diagonal Casimir, and normal contracting kernel.
  residual: prove q-moderate bounds for any numeric specialization used analytically

- id: A1-184-02
  severity: 1
  status: healed
  lens: resonance
  target: normal-mode denominators
  claim: A zero character can be treated as a removable small denominator.
  broken_step: If \(\chi_\alpha=0\), \(\chi_\alpha^{-1}\) is absent and the homotopy identity cannot divide by it.
  evidence_type: direct_derivation
  evidence_ref: Q_Omega k_alpha + k_alpha Q_Omega = chi_alpha id_alpha
  confidence: high
  blast_radius: wrong contraction of fixed modes, invalid reduced complex
  minimal_heal: Keep resonant modes in \(\operatorname{pr}_{\chi=0}\) and record \(\operatorname{Res}_\Omega\).
  residual: compute resonant summands on any self-dual specialization

- id: A1-184-03
  severity: 2
  status: healed
  lens: residue/Euler normalization
  target: scalar-contact and trace normalization
  claim: Residue-normalized and Euler-localized kernels are the same kernel.
  broken_step: The coefficient Casimir is the same, but the brane pushforward/scalar row differs by \(\nu_\Omega^{Eu}\).
  evidence_type: normalization_mismatch
  evidence_ref: thm:wt-omega-kernel-admissibility
  confidence: high
  blast_radius: wrong scalar-contact coefficient and wrong trace normalization
  minimal_heal: Add \(\nu_\Omega^{res}=1\), \(\nu_\Omega^{Eu}=\sigma_s(\epsilon_s\epsilon_1\epsilon_2)^{-1}\), and the comparison map.
  residual: fix the orientation sign \(\sigma_s\) in the chosen convention

- id: A1-184-04
  severity: 1
  status: healed
  lens: Costello QME firewall
  target: weighted/equivariant kernel to QME implication
  claim: The equivariant weighted kernel solves the Costello brane-defect QME.
  broken_step: Kernel admissibility only forms the equivariant kernel complex; QME closure needs scalar gates, non-scalar H^1 classes, and Milnor primitive compatibility to vanish.
  evidence_type: proof_gap
  evidence_ref: cor:wt-omega-denominators-qme-boundary; thm:app-equivariant-brane-defect-qme-criterion
  confidence: high
  blast_radius: erases the actual graph/counterterm obstruction problem
  minimal_heal: Add \(\operatorname{Ob}^{QME}_{\Omega,w}\) with resonance, normalization, scalar, H^1, and lim^1 components.
  residual: compute those classes for the chosen equivariant graph package
```

## Files Changed

- `tate-T1-weighted-completion.tex`
- `reconstitution/swarm-2026-04-30-agent-184-equivariant-weighted-kernels-0957.md`

## Checks

Commands run:

```bash
git diff --check -- tate-T1-weighted-completion.tex reconstitution/swarm-2026-04-30-agent-184-equivariant-weighted-kernels-0957.md
rg -n 'label\{([^}]*)\}' tate-T1-weighted-completion.tex | sed 's/.*label{//; s/}.*//' | sort | uniq -d
lacheck tate-T1-weighted-completion.tex
chktex -q tate-T1-weighted-completion.tex | rg 'line (3[6-9][0-9]|4[0-9][0-9]|5[0-9][0-9])'
```

Results:

- `git diff --check` passed.
- Duplicate-label scan returned no duplicate labels.
- `lacheck` reports only pre-existing style warnings outside the inserted
  block after the local punctuation repair.
- `chktex` reports formula-style warnings in the inserted block
  (`Mittag--Leffler`, parenthesized exponents, set subscripts) and shifted
  pre-existing nonbreaking-space warnings immediately after it. No syntax
  blocker was found.
- `make pdf` was not run because it writes the tracked build artifact
  outside the owned path in a concurrent swarm checkout.

## Remaining Obligations

- Prove the normal Koszul numerator signs in the mixed de Rham/Dolbeault
  coefficient category, including \(ds\)-weight shifts.
- Decide the residue or Euler convention globally and fix
  \(\sigma_s\).
- For a numeric equivariant specialization, prove nonresonance; for an
  analytic all-window theorem, prove \(q\)-moderate bounds.
- Construct the equivariant Costello graph package and compute
  \(\mathfrak s_{n,\Omega}\),
  \(([\mathfrak o^{\mathrm{ns}}_{n,\Omega,M}])_M\), and
  \(\lambda_{n,\Omega}\).
