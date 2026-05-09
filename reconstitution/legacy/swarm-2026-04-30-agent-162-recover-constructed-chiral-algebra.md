# Agent 162 Report: Recover Constructed Chiral Algebra

Date: 2026-04-30.

Owned writable surface:

- `local-dictionary.tex`
- `theorem-lanes.tex`
- `reconstitution/swarm-2026-04-30-agent-162-recover-constructed-chiral-algebra.md`

Allowed reads used: `CLAUDE.md`, the ecosystem attack-heal protocol,
the Vol II rectify skill, `main.tex`, `commands.tex`, `mathmacros.tex`,
`preamble.tex`, `notation.tex`, `appendix-factorization-current-conventions.tex`,
`appendix-unreduced-bv-qme.tex`, the `tate*.tex` files, and reports 149
and 155.  No compact-CY, CoHA, quintic, OSV/GV, Abel-Jacobi, Igusa,
Borcherds, or BKM input was used.  No subagents were launched.

## Stable Core

The manuscript has constructed a local chiral/factorization algebra in
the precise formal-local sense used by the paper:
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}
\]
on \((\widehat{\mathbb C^2}_0,dz_1\wedge dz_2)\), with dg Lie input
\[
  \Omega_c^{0,\bullet}(B)\widehat\otimes
  (\mathfrak h\ltimes\mathfrak h^\vee_{\mathrm{cont}}[1]),
  \qquad
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1 .
\]
Its mixed enhancement, brane Weyl/Moyal avatar, cyclic trace avatars,
and support-local principal-part current avatar are part of the same
local construction.

The surviving gap is narrower.  The manuscript does not yet construct a
one-complex-dimensional vertex algebra or VOA/OPE mode algebra obtained
by restricting the above object to a complex line or holomorphic defect.

## Attack Ledger

```yaml
id: A162-01
severity: 2
status: healed
lens: obstruction overreach
target: theorem-lanes.tex, local-dictionary.tex
claim: The chiral-algebra claim is obstructed because no one-dimensional vertex algebra is present.
broken_step: Agent 155's obstruction proves only the absence of a complex-line VOA/OPE restriction, while main.tex already names and uses the local Hamiltonian chiral/factorization algebra.
evidence_type: line_reference
evidence_ref: main.tex:1078 def:local-hamiltonian-chiral-factorization-algebra; main.tex:1728 local theorem summary; local-dictionary.tex taxonomy
files_read: [main.tex, local-dictionary.tex, theorem-lanes.tex, reconstitution/swarm-2026-04-30-agent-155-holomorphic-defect-voa-restriction.md]
tools_used: [rg, sed]
confidence: high
blast_radius: Would wrongly demote a constructed higher-dimensional holomorphic factorization object into an obstruction.
minimal_heal: State the constructed local chiral/factorization theorem first, then record the one-dimensional VOA/OPE boundary as an additional specialization.
residual: None for the local chiral/factorization construction.
deciding_evidence: The repaired theorem lane cites the manuscript definition and component theorems.
```

```yaml
id: A162-02
severity: 2
status: valid
lens: vertex specialization gap
target: main.tex, theorem-lanes.tex
claim: The manuscript has a one-dimensional vertex/OPE algebra compatible with Weyl/Moyal.
broken_step: The searched files contain no holomorphic line germ \(\operatorname{Spf}\mathbb C[[w]]\), no transverse boundary datum, no restriction functor, no \(Y_L(a,w)\), and no Zhu map except in the obstruction/boundary ledger.
evidence_type: missing_source
evidence_ref: rg scan for Zhu, Y_L, finite Laurent, VOA, vertex algebra, OPE in main.tex, appendices, tate files, local-dictionary.tex, theorem-lanes.tex
files_read: [main.tex, appendix-factorization-current-conventions.tex, appendix-unreduced-bv-qme.tex, tate*.tex]
tools_used: [rg, sed]
confidence: high
blast_radius: A false VOA theorem would conflate the real brane interval current algebra with a complex curve OPE.
minimal_heal: Keep the exact five extra data required for a one-dimensional vertex/OPE specialization.
residual: Constructing those five data remains a future theorem obligation.
deciding_evidence: A future line/defect theorem must supply \(\iota_L,\mathcal B_\perp,\mathsf R_L,V_L,Y_L,\zeta_{L,\hbar}\).
```

```yaml
id: A162-03
severity: 3
status: healed
lens: real-line versus complex-line
target: theorem-lanes.tex
claim: The brane line and reduced open-line Weyl product are already the complex OPE line.
broken_step: The brane is a real topological interval direction. Its support-local current brackets use extension by zero and pointwise multiplication of test functions, not finite Laurent singularities in a complex coordinate.
evidence_type: line_reference
evidence_ref: main.tex:2942 thm:hamiltonian-current-factorization; main.tex:5793 thm:reduced-principal-part-boundary-current; appendix-factorization-current-conventions.tex:277 thm:app-factorization-universal-current-interface
files_read: [main.tex, appendix-factorization-current-conventions.tex]
tools_used: [rg, sed]
confidence: high
blast_radius: Would identify \(P_0\) support locality with VOA locality.
minimal_heal: State explicitly that the brane interval is a real topological current direction, not the complex line \(L=\operatorname{Spf}\mathbb C[[w]]\).
residual: None inside the repaired local theorem lane.
deciding_evidence: The theorem lane's vertex/OPE boundary separates the two line notions.
```

## Recovered Construction

The recovered object is the formal Hamiltonian holomorphic
factorization algebra
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}
\]
and its mixed enhancement
\[
  \mathfrak g^{\mathrm{mix}}_{U,B}
  =
  \Omega^\bullet_c(U)\widehat\otimes
  \Omega^{0,\bullet}_c(B)\widehat\otimes
  (\mathfrak h\ltimes\mathfrak h^\vee_{\mathrm{cont}}[1]).
\]
The brane/current avatars are:

- the Weyl/Moyal algebra
  \[
    f*g=m\circ\exp\!\left(\frac{\hbar}{2}P\right)(f\otimes g);
  \]
- the support-local principal-part current algebra
  \[
    \{B_f(a),B_g(b)\}=B_{\{f,g\}}(ab),\qquad
    \{B_f(a),\Theta_\rho(B)\}=\Theta_{f\cdot\rho}(aB);
  \]
- the quantum replacement \(f\cdot\rho\mapsto
  \operatorname{ad}^{\vee}_{f,\hbar}\rho\).

This is the constructed local chiral/factorization algebra.  It is not
compact-CY chiral homology, a CoHA, a quintic/GV/OSV object, an
Abel-Jacobi object, an Igusa product, a Borcherds lift, or a BKM algebra.

## Exact Remaining Gap

The one-dimensional vertex/OPE specialization still requires:

1. a complex line or holomorphic defect
   \(\iota_L\colon \operatorname{Spf}\mathbb C[[w]]
   \hookrightarrow\widehat{\mathbb C^2}_0\);
2. a transverse datum \(\mathcal B_\perp\) and restriction functor
   \(\mathsf R_{L,\mathcal B_\perp}\);
3. a factorization-to-vertex comparison producing
   \(V_L,\mathbf 1_L,T_L\);
4. finite Laurent modes \(Y_L(a,w)\) with vacuum, translation, and
   locality;
5. a Weyl/Moyal zero-mode or Zhu map
   \(\zeta_{L,\hbar}\colon(\bar A_\hbar,*)\to\operatorname{Zhu}(V_L)\),
   or equivalent fields \(J_f(w)\) with the Moyal coadjoint action.

## Repairs Inscribed

- `local-dictionary.tex`: changed the taxonomy so the constructed
  local chiral/factorization algebra is named first; the vertex/OPE
  material is now a restriction boundary, not an obstruction to the
  constructed object.
- `theorem-lanes.tex`: replaced the obstruction-only lane at
  `thm:lane-holomorphic-defect-voa-restriction` by a repaired theorem
  lane: constructed local chiral/factorization algebra first, exact
  five-part vertex/OPE boundary second.
- `reconstitution/swarm-2026-04-30-agent-162-recover-constructed-chiral-algebra.md`:
  recorded the attacks, recovered construction, remaining gap, and
  verification.

## Verification

Commands run:

```bash
rg -n -F -e "local-hamiltonian-chiral-factorization-algebra" -e "F_{\\\\mathrm{Ham}}^{\\\\mathrm{hol}}" -e "Zhu" -e "Y_L" -e "finite Laurent" -e "VOA" -e "vertex algebra" -e "OPE" -e "one-dimensional" main.tex local-dictionary.tex theorem-lanes.tex appendix-factorization-current-conventions.tex appendix-unreduced-bv-qme.tex tate*.tex
rg -n "label\\{(def:local-hamiltonian-chiral-factorization-algebra|prop:local-hamiltonian-factorization-observables|def:local-holomorphic-string-sector|def:local-th-string|thm:formal-disk-completed-ce-pv|thm:reduced-ce-pv-central-operation|thm:hamiltonian-current-factorization|thm:reduced-principal-part-boundary-current|cor:app-factorization-principal-part-current-brackets|prop:moyal-monomial|thm:finite-n-reduced-moyal|thm:quantum-coefficient-surface)\\}" main.tex theorem-lanes.tex appendix-factorization-current-conventions.tex
rg -n "label\\{([^}]*)\\}" theorem-lanes.tex local-dictionary.tex | sed 's/.*label{//; s/}.*//' | sort | uniq -d
git diff --check -- local-dictionary.tex theorem-lanes.tex reconstitution/swarm-2026-04-30-agent-162-recover-constructed-chiral-algebra.md
mkdir -p /tmp/topological-strings-agent162-build
pdflatex -halt-on-error -interaction=nonstopmode -draftmode -output-directory=/tmp/topological-strings-agent162-build main.tex
```

Results:

- The fixed-string scan found the constructed local chiral/factorization
  object at `main.tex:1078`, `main.tex:1728`, `local-dictionary.tex:190`,
  and `theorem-lanes.tex:349`, and found `Zhu`, `Y_L`, finite Laurent,
  VOA, and OPE data only in the one-dimensional boundary/obligation
  contexts.
- The label scan found the cited construction, CE/PV, current, Moyal, and
  quantum coefficient labels in `main.tex`, `theorem-lanes.tex`, and
  `appendix-factorization-current-conventions.tex`.
- The duplicate-label scan returned no hits for `local-dictionary.tex`
  and `theorem-lanes.tex`.
- `git diff --check` passed for the three scoped files.
- The draft `pdflatex` pass exited with status 0 after creating the `/tmp`
  output directory.  It reports pre-existing undefined-reference,
  underfull/overfull box, and font checksum/width warnings outside this
  repair.

## Files Changed / Staging

Changed by Agent 162:

- `local-dictionary.tex`
- `theorem-lanes.tex`
- `reconstitution/swarm-2026-04-30-agent-162-recover-constructed-chiral-algebra.md`

Staged by Agent 162: none.  The two TeX files had pre-existing staged
swarm changes and same-file concurrent edits; I left staging unchanged to
avoid sweeping unrelated hunks.  The report file remains untracked until
the integration owner stages it.

## Remaining Obligations

- Prove the complex-line or holomorphic-defect restriction theorem before
  asserting a one-dimensional vertex algebra or OPE-mode algebra.
- Keep compact-CY chiral homology, CoHA, quintic/GV/OSV, Abel-Jacobi,
  Igusa, Borcherds, and BKM material outside the core local theorem
  unless a matched-conventions theorem is explicitly supplied.
