# Agent 192 Report: Equivariant Brane Current Brackets

Worktree: `/Users/raeez/topological-strings`.

Branch: `master`.

Owned paths:

- `appendix-factorization-current-conventions.tex`
- `reconstitution/swarm-2026-04-30-agent-192-equivariant-brane-current-brackets-0957.md`

## Stable Core

The algebraic brane-line current theorem now has a normal
\(\Omega\)-weighted refinement in
`appendix-factorization-current-conventions.tex`.

For \(t\) fixed, \(z_1,z_2\) of weights
\(\epsilon_1,\epsilon_2\), and
\[
  \chi_\omega=\epsilon_1+\epsilon_2,\qquad
  \operatorname{wt}_\Omega(\hbar_\omega)=\chi_\omega,
\]
the current generators have weights
\[
  \operatorname{wt}_\Omega B_{p,q}(a)=p\epsilon_1+q\epsilon_2,
  \qquad
  \operatorname{wt}_\Omega \Theta_{r,s}(B)
    =-r\epsilon_1-s\epsilon_2 .
\]
Here \(a\in C^\infty_c(I)\) and \(B\in\mathcal D'_c(I)\) carry no
\(\Omega\)-weight because they live on the fixed brane line.

The scalarized refined current brackets are
\[
\begin{aligned}
  \{B_{p,q}(a),B_{r,s}(b)\}_{\Omega}
    &=
    \hbar_\omega(ps-qr)B_{p+r-1,q+s-1}(ab),\\
  \{B_{p,q}(a),\Theta_{r,s}(B)\}_{\Omega}
    &=
    -\hbar_\omega(ps-qr+p-q)
    \Theta_{r-p+1,s-q+1}(aB),\\
  \{\Theta_{r,s}(B),\Theta_{u,v}(C)\}_{\Omega}
    &=0 .
\end{aligned}
\]
Negative-index targets and the scalar-residue target \((0,0)\) are zero.
Without adjoining \(\hbar_\omega\), the first two brackets are
\(\mathbb L_\omega^{-1}\)-valued.  On the self-dual branch
\(\epsilon_1+\epsilon_2=0\), \(\mathbb L_\omega\) is trivial and, after
choosing \(\hbar_\omega=1\), the formulas reduce to the ordinary reduced
current brackets.

Compact-support functoriality is strict:
\[
  j_!B_{p,q,I}(a)=B_{p,q,J}(j_!a),\qquad
  j_!\Theta_{r,s,I}(B)=\Theta_{r,s,J}(j_!B),
\]
and \(j_!\{x,y\}_{\Omega,I}=\{j_!x,j_!y\}_{\Omega,J}\).  Mixed brackets on
disjoint intervals vanish because \(ab=0\) and \(aB=0\) after extension to
a common interval.

This is an algebraic current theorem for all
\(B,C\in\mathcal D'_c(I)\).  It is not a Costello graph theorem for
arbitrary distributional labels.  Graph lifts remain restricted to
regular densities or graphwise wavefront-admissible tuples, with
\(Q_\Omega\), normal contraction, normalization, counterterms, scalar
gates, non-scalar \(H^1\) classes, and Milnor primitive compatibility
still required.

## Valid Attacks

```yaml
- id: A1-192-01
  severity: 2
  status: healed
  lens: equivariant weight bookkeeping
  target: appendix-factorization-current-conventions.tex, brane current generators
  claim: The reduced current brackets can be used equivariantly without recording generator weights.
  broken_step: \(B_{p,q}(a)\) and \(\Theta_{r,s}(B)\) carry opposite Hamiltonian/principal-part characters, while \(a\) and \(B\) are fixed-line data of weight zero.
  evidence_type: direct_derivation
  evidence_ref: local-dictionary.tex:484-543; appendix-factorization-current-conventions.tex:399-550
  confidence: high
  blast_radius: wrong equivariant CE/PV map and wrong current bracket homogeneity
  minimal_heal: Add explicit weights for \(B_{p,q}(a)\) and \(\Theta_{r,s}(B)\).
  residual: none for algebraic current generators
  deciding_evidence: theorem \ref{thm:app-omega-weighted-current-brackets}

- id: A1-192-02
  severity: 2
  status: healed
  lens: refined bracket
  target: off-self-dual current brackets
  claim: The old scalar Hamiltonian current bracket is \(T_\Omega\)-equivariant off \(\epsilon_1+\epsilon_2=0\).
  broken_step: The Poisson bivector has character \(-(\epsilon_1+\epsilon_2)\), so the ordinary bracket is inverse-line-valued.
  evidence_type: direct_derivation
  evidence_ref: critique-refresh-2026-04-30-0957-ingestion-and-swarm-plan.md:85-100; reconstitution/swarm-2026-04-30-agent-189-equivariant-ce-pv-refined-bracket-0957.md
  confidence: high
  blast_radius: non-homogeneous CE differential and wrong principal-part action
  minimal_heal: Insert \(\hbar_\omega\) in the scalarized brackets and record the line-valued alternative.
  residual: if a raw Weyl commutator convention is used, \(\hbar_\omega\) must be identified with the deformation parameter explicitly
  deciding_evidence: displayed \(\Omega\)-bracket formulas

- id: A1-192-03
  severity: 2
  status: healed
  lens: self-dual specialization
  target: \(\epsilon_1+\epsilon_2=0\) branch
  claim: One can invert \(\chi_\omega\) and then specialize to the self-dual branch.
  broken_step: The self-dual branch is exactly the vanishing locus of \(\chi_\omega\); inverting it erases the resonant branch.
  evidence_type: obstruction
  evidence_ref: local-dictionary.tex:445-457; reconstitution/swarm-2026-04-30-agent-184-equivariant-weighted-kernels-0957.md
  confidence: high
  blast_radius: invalid normal localization and false scalar bracket comparison
  minimal_heal: State self-dual as a separate specialization with \(\hbar_\omega\) weight zero.
  residual: resonant normal summands remain a kernel/QME obligation, not a current-bracket obligation
  deciding_evidence: self-dual paragraph in theorem \ref{thm:app-omega-weighted-current-brackets}

- id: A1-192-04
  severity: 2
  status: healed
  lens: compact-support functoriality
  target: interval inclusions and disjoint products
  claim: Equivariance might alter extension-by-zero functoriality.
  broken_step: The normal torus fixes \(t\), so extension by zero has weight zero and commutes with \(ab\) and \(aB\).
  evidence_type: proof
  evidence_ref: appendix-factorization-current-conventions.tex:190-216 and 464-477
  confidence: high
  blast_radius: false factorization-current compatibility
  minimal_heal: Add explicit \(j_!\)-compatibility and disjoint-interval vanishing.
  residual: none for algebraic current brackets
  deciding_evidence: extension-by-zero equations in theorem \ref{thm:app-omega-weighted-current-brackets}

- id: A1-192-05
  severity: 1
  status: healed
  lens: Costello graph firewall
  target: arbitrary \(\mathcal D'_c\) graph claims
  claim: The \(\Omega\)-weighted current bracket proves a graph/QME theorem for arbitrary compactly supported distributions.
  broken_step: The algebraic bracket only multiplies a distribution by a smooth function; graph kernels require products with singular propagator boundary values and extensions across collision diagonals.
  evidence_type: proof_gap
  evidence_ref: appendix-factorization-current-conventions.tex:943-1331; CLAUDE.md normal Omega discipline; reports 177 and 184
  confidence: high
  blast_radius: false brane-defect QME theorem and false protected-trace theorem
  minimal_heal: State the graph boundary in the theorem and retain regular-density/wavefront-admissible restrictions.
  residual: construct the equivariant Costello graph package and compute scalar/non-scalar obstruction classes
  deciding_evidence: last paragraph and proof boundary of theorem \ref{thm:app-omega-weighted-current-brackets}
```

## Files Changed

- `appendix-factorization-current-conventions.tex`
- `reconstitution/swarm-2026-04-30-agent-192-equivariant-brane-current-brackets-0957.md`

## Checks

Context read:

- `CLAUDE.md`
- `AGENTS.md`
- attack-heal swarm protocol
- Vol II Chriss-Ginzburg rectify skill
- `reconstitution/critique-refresh-2026-04-30-0957-ingestion-and-swarm-plan.md`
- `appendix-factorization-current-conventions.tex`
- `local-dictionary.tex`
- reports 177, 184, and adjacent refined-bracket report 189
- relevant `main.tex`, `mathmacros.tex`, `commands.tex`, `notation.tex`

Commands run:

```bash
git diff --check -- appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-192-equivariant-brane-current-brackets-0957.md
rg -n 'label\{([^}]*)\}' appendix-factorization-current-conventions.tex | sed 's/.*label{//; s/}.*//' | sort | uniq -d
rg -n -F -e 'thm:app-omega-weighted-current-brackets' -e '\hbar_\omega' -e 'B_{p,q}(a)' -e 'Theta_{r,s}(B)' -e 'wavefront-admissible' appendix-factorization-current-conventions.tex reconstitution/swarm-2026-04-30-agent-192-equivariant-brane-current-brackets-0957.md
```

Results:

- `git diff --check` passed for both owned paths after insertion.
- Duplicate-label scan returned no output.
- Targeted formula scan found the inserted theorem label, weights,
  \(\hbar_\omega\)-brackets, and wavefront boundary.
- A full PDF build was not run because it would write generated artifacts
  outside the owned path in an active concurrent swarm checkout.

## Remaining Obligations

- Construct the mixed \(T_\Omega\)-Cartan/basic coefficient model and prove
  the \(Q_\Omega\)-identities in that topology.
- Build the normal contraction and record resonant summands on each
  specialization.
- Decide or compare residue and Euler normalizations.
- Extend the equivariant theorem from algebraic currents to Costello graph
  kernels only on regular-density or wavefront-admissible current classes.
- Compute the equivariant scalar gate, non-scalar \(H^1\) classes, and
  \(\varprojlim^1H^0\) primitive compatibility for the graph/QME package.
