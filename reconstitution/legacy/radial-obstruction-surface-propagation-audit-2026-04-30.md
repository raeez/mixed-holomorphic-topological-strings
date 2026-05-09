# Radial obstruction surface propagation audit

Date: 2026-04-30.

Agent: 320.

Scope: audit only.  No manuscript TeX or script file was edited.

## Claim Attacked

After Agent 314, every reader-facing radial/Weyl theorem surface should
state the all-N ordinary Weyl-trace comparison as an exact obstruction
theorem:
\[
  \Omega^{\mathrm{rad}}_{a,b}
  =
  [(T_{a,b},E^+_{a,b})]\in\operatorname{coker}B_{a,b}.
\]
The accepted positive theorem is \(\Omega^{\mathrm{rad}}_{a,b}=0\) for
all bidegrees, equivalently the decorated PBW Stokes problem for
\[
  D^\square_{a,b}=C^+_{a,b}\partial_2.
\]
Failure is exactly a signed row
\[
  (\phi,-\lambda)\in\ker B_{a,b}^*
\]
with
\[
  \lambda(E^+_{a,b})-\phi(T_{a,b})\ne0.
\]
After rescaling, the first failing row may be normalized to value \(1\).

## Reports Read

- Agent 289:
  `reconstitution/swarm-2026-04-30-agent-289-radial-dual-potential-identity-construction-push.md`.
  Lines 64-93 give the dual-potential obstruction theorem; lines 244-251
  name the remaining decorated Stokes/Hodge construction target.
- Agent 296:
  `reconstitution/swarm-2026-04-30-agent-296-radial-structural-hodge-proof-mechanism.md`.
  Lines 41-68 prove the ordinary square-cell cycle mechanism and define
  \(D^\square=C^+\partial_2\); lines 77-98 give the signed-row failure
  criterion.
- Agent 314:
  `reconstitution/swarm-2026-04-30-agent-314-radial-all-n-decorated-pbw-stokes-attack-heal.md`.
  Lines 161-184 state the accepted all-N obstruction target and signed row;
  lines 186-204 list the next patch surface.

## Verification Result

Status: partial propagation.  The principal theorem-lane and the detailed
open-obligation/ledger surfaces now carry the exact obstruction theorem.
Several secondary theorem summaries still use the older
\(\mathcal C_{a,b}\)-cokernel language without naming
\(\Omega^{\mathrm{rad}}\), \(D^\square\), and the signed \(B^*\)-row.
These are reader-facing because they occur in frontmatter summaries,
theorem statements, lane summaries, and claim-ledger tables.

## Correct Surfaces

- `appendix-radial-parts-moyal.tex:965-1027` states
  \(\Omega^{\mathrm{rad}}_{a,b}=0\), the dual-potential identity,
  \(D^\square_{a,b}=C^+_{a,b}\partial_2\), and signed-row failure.
- `appendix-radial-parts-moyal.tex:1029-1059` proves the finite-dimensional
  duality equivalence by evaluating \((\phi,-\lambda)\) on
  \(\eta_{a,b}\).
- `main.tex:2727-2749` correctly phrases the local theorem package:
  \(\Omega^{\mathrm{rad}}\), signed rows, and \(D^\square\) appear.
- `theorem-lanes.tex:2525-2550` correctly states the degree-zero lane as a
  radial/Weyl obstruction theorem target with signed-row failure and the
  decorated PBW Stokes identity.
- `open-obligations.tex:1355-1437` correctly records the detailed
  acceptance gate, including \(\Omega^{\mathrm{rad}}\), signed row, and
  \(D^\square\).
- `claim-strength-ledger.tex:984-1043` correctly records the detailed
  ledger row with \(\Omega^{\mathrm{rad}}\), signed row, and
  \(D^\square\).

## Remaining TeX Defects And Patch Targets

1. `appendix-radial-parts-moyal.tex:888-939`.
   The "Decorated Hodge obstruction theorem" still states the all-bidegree
   closure only as
   \(\Pi^{\mathrm{harm}}R^{\mathrm{free}}=0\) or a left-cokernel functional
   on \(A_{a,b}=C^+|_{\ker\partial}\).  It should add the stronger
   reader-facing equivalence with
   \(\Omega^{\mathrm{rad}}_{a,b}=0\), the \(B_{a,b}\)-cokernel class, and
   signed-row failure.

2. `appendix-radial-parts-moyal.tex:965-1027`.
   The dual-potential proposition mentions \(D^\square=C^+\partial_2\) but
   does not formally define the square-cell complex
   \(C^\square_2(a,b)\), state \(\operatorname{im}\partial_2=\ker\partial\)
   after the ordinary cycle mechanism, or state the equivalent
   \(D^\square\)-left-cokernel condition
   \(\lambda D^\square=0\Rightarrow \lambda(R^{\mathrm{free}})=0\).
   Patch by inserting the square-cell definition and the decorated Stokes
   criterion before or inside this proposition.

3. `main.tex:1046-1064`.
   The early quantum-data summary says the all-interior statement is a
   functorial splitting of \(\mathcal C_{a,b}\) or a natural left-cokernel
   vanishing theorem.  It omits \(\Omega^{\mathrm{rad}}\), \(D^\square\),
   and the signed row.  Patch this summary to point to
   Proposition~\ref{prop:app-radial-dual-potential-obstruction}.

4. `main.tex:7379-7410`.
   The finite-N theorem statement gives the signed-row criterion but not the
   \(\Omega^{\mathrm{rad}}\) class or the decorated Stokes map
   \(D^\square\).  Patch lines 7405-7410 to state the full equivalence.

5. `main.tex:7552-7597`.
   The degree-zero quantum Hamiltonian-sector remark ends with
   "associated-graded two-colour necklace homotopy" or "stable
   left-cokernel vanishing theorem."  It should name the
   \(\Omega^{\mathrm{rad}}\) obstruction and signed \(B^*\)-row.

6. `main.tex:8219-8270`.
   The theorem `thm:phi-hbar-all-order` item (3) still presents the missing
   theorem as \(\mathfrak o_{a,b}\in\operatorname{coker}\mathcal C_{a,b}\)
   plus \(K_{a,b}\).  Patch item (3) to include the dual-potential
   formulation and \(D^\square\) Stokes criterion.

7. `main.tex:8372-8380`.
   The componentwise quantum coefficient surface says the ordinary-trace
   comparison is pinned to \(\mathfrak o_{a,b}\), requiring homotopy or a
   left-cokernel theorem.  Patch it to use the accepted
   \(\Omega^{\mathrm{rad}}\)/signed-row obstruction surface.

8. `theorem-lanes.tex:2665-2674`.
   The scope clause for the degree-zero lane says a nonzero functional on
   \(\operatorname{coker}\mathcal C_{a,b}\) is the obstruction theorem.
   Patch it to name the stronger equivalent signed row
   \((\phi,-\lambda)\in\ker B_{a,b}^*\) and the nonzero value.

9. `theorem-lanes.tex:2765-2771`.
   The componentwise coefficient-surface proof-input paragraph cites the
   radial/Weyl gate through the older primitive/Hodge references only.
   Patch it to cite Proposition~\ref{prop:app-radial-dual-potential-obstruction}
   and the \(D^\square\) decorated Stokes problem.

10. `theorem-lanes.tex:3634-3674`.
    The radial trace-diagram theorem lane is still an older
    \(\mathcal C_{a,b}\)-left-cokernel formulation.  Patch this lane to
    state the all-N statement as
    \(\Omega^{\mathrm{rad}}_{a,b}=0\), equivalently decorated Stokes for
    \(D^\square\), with failure exactly a signed row in \(\ker B^*\).

11. `open-obligations.tex:500-526`.
    The componentwise theorem datum summary says the remaining
    all-bidegree theorem is a functorial splitting of \(\mathcal C_{a,b}\)
    or a left-cokernel functional.  Patch it to the full
    \(\Omega^{\mathrm{rad}}\)/\(D^\square\)/signed-row formulation.

12. `claim-strength-ledger.tex:207-215`.
    The top claim table's radial/Weyl row omits
    \(\Omega^{\mathrm{rad}}\), \(D^\square\), and signed-row failure.
    Patch the row text.

13. `claim-strength-ledger.tex:300-308`.
    The "Radial trace-diagram branch" row still says uniform contracting
    homotopy or left-cokernel functional.  Patch to the exact
    \(B_{a,b}\)-cokernel and signed-row obstruction theorem.

14. `claim-strength-ledger.tex:577-585`.
    The frontier list item "Radial all-N image and all-bidegree homotopy"
    still names only \(\mathcal C_{a,b}\) and a left-cokernel functional.
    Patch it to the accepted \(\Omega^{\mathrm{rad}}\) theorem surface.

15. `claim-strength-ledger.tex:1238-1270`.
    The "Quantum Hamiltonian and Moyal sector" item still ends with a
    uniform contracting homotopy on \(\ker\partial\).  Patch it to cite the
    dual-potential obstruction and \(D^\square\) Stokes gate.

## Attack-Heal Conclusion

The all-N radial/Weyl theorem is not a theorem of vanishing yet.  The
reader-facing invariant to propagate is the exact obstruction theorem:
\[
  \Omega^{\mathrm{rad}}_{a,b}=0
  \Longleftrightarrow
  [(T_{a,b},E^+_{a,b})]\in\operatorname{im}B_{a,b}
  \Longleftrightarrow
  \text{decorated Stokes vanishing for }D^\square_{a,b}.
\]
The first fatal failure, if it exists, is not a vague missing homotopy but a
printed signed row \((\phi,-\lambda)\in\ker B_{a,b}^*\) with
\(\lambda(E^+_{a,b})-\phi(T_{a,b})\ne0\).

## Commands Run

- `sed -n` and `nl -ba` on `CLAUDE.md`, `AGENTS.md`, ecosystem rules, the
  Vol II rectification skill, the five requested TeX files, and reports
  289/296/314.
- `rg` over the five requested TeX files for radial/Weyl, Moyal, Stokes,
  \(\Omega^{\mathrm{rad}}\), \(D^\square\), \(\mathcal C_{a,b}\), and
  signed-row language.
- `wc -l` on the requested files.
- `git status --short` to observe concurrent dirty state.

No build was run.  This was a report-only audit.

## Files Changed

- `reconstitution/radial-obstruction-surface-propagation-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-320-radial-obstruction-surface-propagation-audit.md`
