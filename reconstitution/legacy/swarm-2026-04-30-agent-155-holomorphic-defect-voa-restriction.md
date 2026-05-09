# Agent 155 Report: Holomorphic-Defect VOA Restriction

## Scope

Owned files:

- `local-dictionary.tex`
- `theorem-lanes.tex`
- `reconstitution/swarm-2026-04-30-agent-155-holomorphic-defect-voa-restriction.md`

Allowed reads used: `main.tex`, `appendix-factorization-current-conventions.tex`,
`appendix-unreduced-bv-qme.tex`, and the Agent 149 report.  No compact-CY,
CoHA, quintic, OSV/GV, Abel-Jacobi, Igusa, Borcherds, or BKM input was used.
No subagents were launched.

## Valid Attacks

1. **Word "chiral" was not enough.**  The local object currently proved in the
   manuscript is a holomorphic factorization algebra on the formal twofold
   \(\widehat{\C^2}_0\), not a one-dimensional vertex algebra.  A complex-line
   or holomorphic-defect restriction is extra structure.

2. **No canonical line exists in the stated data.**  The data
   \[
     \mathcal F_{\C^2},\qquad
     \mathfrak h=\C[[z_1,z_2]]/\C\cdot1,\qquad
     \mathfrak g=\mathfrak h\ltimes\mathfrak h^\vee_{\mathrm{cont}}[1]
   \]
   do not choose an embedding
   \[
     \iota_L\colon L=\operatorname{Spf}\C[[w]]
     \hookrightarrow\widehat{\C^2}_0 .
   \]

3. **No transverse boundary condition is present.**  Restricting from
   \(\C^2\) to a line requires a normal datum \(\mathcal B_\perp\) and a
   functorial construction
   \[
     \mathsf R_{L,\mathcal B_\perp}(\mathcal F_{\C^2})
     =
     \mathcal F_{L,\mathcal B_\perp},
   \]
   with independence of transverse radius/formal neighbourhood, disjoint disk
   compatibility, and translation covariance along \(w\).  These are absent.

4. **The principal-part current theorem is not an OPE theorem.**  The existing
   interval current brackets are support-local real-current brackets with
   Matlis principal parts in two holomorphic variables.  They do not supply
   Laurent modes \(a_{(n)}b\), a finite-pole expansion, vertex locality, a
   vacuum, or a translation operator.

5. **The Weyl/Moyal brane algebra has no proved vertex shadow.**  The
   manuscript proves the star product and reduced principal-part current
   compatibility.  It does not prove a map
   \[
     \zeta_{L,\hbar}\colon
     (\bar A_\hbar,*)\longrightarrow \operatorname{Zhu}(V_L)
   \]
   or fields \(J_f(w)\) with a singular OPE and specified central level.

## Repairs Inscribed

- `local-dictionary.tex:281`: added the missing complex-line /
  holomorphic-defect restriction datum
  \[
    \mathfrak R_L
    =
    (\iota_L,L,\mathcal B_\perp,\mathsf R_L,\mathbf 1_L,T_L).
  \]

- `local-dictionary.tex:306`: added the required restricted OPE data
  \[
    V_L=H^\bullet(\mathcal F_{L,\mathcal B_\perp}(\Delta_0)),
    \qquad
    Y_L(a,w)b=\sum_{n\in\Z}(a_{(n)}b)\,w^{-n-1}.
  \]

- `local-dictionary.tex:332`: added the Weyl/Moyal compatibility data:
  a Zhu/zero-mode map, or fields satisfying
  \[
    J_f(w)J_g(0)
    \sim
    \frac{\kappa_L(f,g)}{w^2}
    +
    \frac{J_{\{f,g\}_\hbar}(0)}{w},
  \]
  together with
  \[
    [J_{f,(0)},\Theta_\rho]
    =
    \Theta_{\operatorname{ad}^{\vee}_{f,\hbar}\rho}.
  \]

- `theorem-lanes.tex:349`: added
  `thm:lane-holomorphic-defect-voa-restriction`, an obstruction statement with
  a conditional theorem surface.

## Exact Obstruction Data

A genuine one-dimensional vertex/OPE theorem requires all five data:

1. A line or defect germ
   \[
     \iota_L\colon L=\operatorname{Spf}\C[[w]]
     \hookrightarrow\widehat{\C^2}_0 .
   \]

2. A transverse boundary condition or normal vacuum \(\mathcal B_\perp\) and
   a restriction functor
   \[
     \mathsf R_{L,\mathcal B_\perp}\colon
     \mathcal F_{\C^2}\longmapsto
     \mathcal F_{L,\mathcal B_\perp},
     \qquad D\subset L,
   \]
   for instance through
   \[
     \mathcal F_{L,\mathcal B_\perp}(D)
     =
     \mathsf R_{L,\mathcal B_\perp}
     \bigl(\mathcal F_{\C^2}(D\times \widehat N_L)\bigr).
   \]

3. A Beilinson-Drinfeld / Costello-Gwilliam factorization-to-vertex
   comparison, producing \(V_L\), \(\mathbf 1_L\), and \(T_L\).

4. A finite singular OPE expansion
   \[
     \mu_{w,0}(a\boxtimes b)
     \sim
     \sum_{n\ge0}(a_{(n)}b)\,w^{-n-1}
     +\mu^{\mathrm{reg}}_{w,0}(a,b),
   \]
   with \(a_{(n)}b=0\) for \(n\gg0\), vacuum, translation
   \([T_L,Y_L(a,w)]=\partial_wY_L(a,w)\), and locality
   \[
     (w_1-w_2)^N[Y_L(a,w_1),Y_L(b,w_2)]=0
   \]
   for \(N\gg0\).

5. Weyl/Moyal compatibility through \(\zeta_{L,\hbar}\) or equivalent fields
   \(J_f(w)\), with the Moyal principal-part coadjoint action rather than the
   polynomial one-\(\psi\) PBW action.

## Claim Status

The restriction theorem cannot be proved from the currently inscribed local
data.  The repair states this as an obstruction theorem and records the exact
additional data needed.  The conditional implication is formal: if the
restriction tuple
\[
  \mathfrak R_L
  =
  (\iota_L,\mathcal B_\perp,\mathsf R_{L,\mathcal B_\perp},
  V_L,\mathbf 1_L,T_L,Y_L,\zeta_{L,\hbar})
\]
satisfying the five displayed obligations is supplied, then \(V_L\) is a
one-dimensional vertex/OPE algebra compatible with the Weyl/Moyal brane
algebra by those formulas.  This is not asserted as a theorem from the
existing mixed HT model.

## Verification

Commands run:

- `git diff --check -- local-dictionary.tex theorem-lanes.tex`
- `rg -n "label\\{thm:lane-holomorphic-defect-voa-restriction\\}|Complex-line / holomorphic-defect|OPE data for the restricted object|Compatibility with the Weyl/Moyal" local-dictionary.tex theorem-lanes.tex`
- `rg -n "label\\{(def:local-holomorphic-string-sector|def:local-th-string|thm:reduced-principal-part-boundary-current|cor:app-factorization-principal-part-current-brackets|thm:quantum-coefficient-surface)\\}" main.tex appendix-factorization-current-conventions.tex`
- `rg -n "label\\{([^}]*)\\}" theorem-lanes.tex local-dictionary.tex | sed 's/.*label{//; s/}.*//' | sort | uniq -d`
- `rg -n "compact-CY chiral homology|CoHA|quintic|OSV/GV|Abel--Jacobi|Igusa|Borcherds|BKM|vertex algebra|OPE|Zhu|holomorphic defect|complex line" local-dictionary.tex theorem-lanes.tex`
- `pdflatex -halt-on-error -interaction=nonstopmode -draftmode -output-directory=/tmp/topological-strings-agent155-build main.tex` run three times.

Results:

- No whitespace errors.
- New theorem label is unique in the checked files.
- Referenced labels exist in `main.tex` or
  `appendix-factorization-current-conventions.tex`.
- The local firewall terms occur only in intended obstruction/exclusion
  contexts in the checked files.
- The third LaTeX pass exited successfully.  Remaining TeX warnings are
  pre-existing overfull/underfull box and font checksum/width warnings outside
  this repair.

## Files Changed / Staging

Changed by Agent 155:

- `local-dictionary.tex`
- `theorem-lanes.tex`
- `reconstitution/swarm-2026-04-30-agent-155-holomorphic-defect-voa-restriction.md`

The two TeX files already had staged and unstaged swarm changes before this
repair.  Agent 155 did not revert or rewrite those changes; the repair was
inscribed on top of the current working tree.

Staging action after final verification: stage the current versions of the
three scoped files above.  For the two shared TeX files this necessarily stages
the current same-file swarm state together with Agent 155's local obstruction
repair.

## Remaining Theorem Obligations

1. Choose a specific line or holomorphic defect \(L\subset\widehat{\C^2}_0\)
   and state whether the choice is coordinate, symplectic, or invariant.
2. Construct the transverse restriction datum \(\mathcal B_\perp\) and prove
   functoriality/independence of auxiliary normal choices.
3. Prove the one-dimensional factorization-to-vertex comparison for the
   restricted object.
4. Compute the finite OPE singularities and verify vacuum, translation, and
   locality.
5. Relate the restricted zero modes to the Weyl/Moyal brane algebra through a
   proved \(\zeta_{L,\hbar}\) or explicit \(J_f(w)\)-OPE, including the
   central level \(\kappa_L\).
