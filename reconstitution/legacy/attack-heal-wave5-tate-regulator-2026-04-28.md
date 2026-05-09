# Worker 3 Tate Regulator Attack-Heal Report

Date: 2026-04-28

Status: converged for admissible finite-window weight independence; blocked, by an explicit obstruction, for strict unweighted regulator independence.

## Claim Attacked

The weighted Tate replacement was tested against four possible interpretations:

1. merely a regulator;
2. a completion changing the theory;
3. a quasi-isomorphic replacement;
4. a false transfer from the weighted coefficient model to the original product/direct-sum Tate pair.

## Strongest Failure Mode

The weighted dual
\[
  \mathfrak h^{\vee,w}_{\mathrm{cont}}=\prod_d w(d)^{-1}H_d^\vee
\]
contains infinite product tails absent from the strict continuous dual
\[
  \mathfrak h^\vee_{\mathrm{cont}}=\bigoplus_d H_d^\vee.
\]
With zero differential, the inclusion
\[
  \bigoplus_d H_d^\vee\hookrightarrow \prod_d w(d)^{-1}H_d^\vee
\]
is not an ordinary quasi-isomorphism: the quotient has nonzero
\(H^0\). Thus weighted completion changes the ordinary chain complex
when tail-sensitive observables are admitted.

A second failure mode is non-admissible weighting. The function
\(w(d)=\exp(d^2)\) violates bracket tameness because
\[
  w(p+q-2)/(w(p)w(q))
\]
is unbounded along \(p=q\to\infty\). Such a topology is not compared
by the weighted regulator theorem.

## Heal Inscribed

The repair is Theorem
`\ref{thm:wt-regulator-independence-admissible}` in
`tate-T1-weighted-completion.tex`.

Exact theorem: for any two degree weights satisfying
Definition `\ref{defn:wt-degree-weight}`, diagonal finite-window
rescaling identifies the strict Mittag-Leffler local-functional
complexes in the regulator-admissible sector. Truncated Casimirs,
heat-kernel propagators, fixed graphwise Costello contractions, and the
mixed brane-defect obstruction class are transported isomorphically.
Hence vanishing or nonvanishing of the QME obstruction is independent
of the admissible weight.

Exact hypotheses:

- strict Mittag-Leffler finite-window presentation with surjective
  transition maps;
- vertexwise polynomial-degree bounds at each fixed graph and
  \(\hbar\)-order;
- diagonal rescaling transports the interaction, differential, bracket,
  and counterterm representative;
- cohomology is computed in the admissible filtered envelope of
  Statement `\ref{stmt:tate-model-envelope}`;
- no observable detects an infinite product tail invisible to finite
  quotients.

## Theorem Boundary

The weighted route is now classified as follows:

- regulator for finite-window graphwise calculations;
- filtered weak replacement only inside the admissible
  Mittag-Leffler envelope;
- genuine completion changing the ordinary chain complex once product
  tails are admitted;
- not a theorem about the strict unweighted Costello graph calculus,
  because the strict product/direct-sum pair has no coefficient Casimir.

Thus the false transfer is blocked. The original unweighted graph
theory remains undefined at the coefficient-kernel step unless another
sector restriction or coefficient category is supplied.

## Files Changed

- `tate-T1-weighted-completion.tex`
  - Added the regulator-admissible sector definition.
  - Added the finite-window weight-independence theorem.
  - Added counterexamples for ordinary cohomology and bad weights.
  - Added a status firewall for the weighted route.
- `tate-P1-hadamard-mittag-leffler.tex`
  - Renamed misleading internal labels from "unconditional/closed" to
    conditional/reduced forms.
  - Added the Hadamard relation to admissible regulator independence.
- `open-obligations.tex`
  - Replaced the old blanket regulator-independence obligation with the
    precise closed/open split.
- `references/source-provenance.md`
  - Recorded this pass and its local proof artifacts.
- `reconstitution/attack-heal-wave5-tate-regulator-2026-04-28.md`
  - This report.

## Commands Run

- `sed -n '1,220p' .../chriss-ginzburg-rectify/SKILL.md`
- `sed -n ... CLAUDE.md AGENTS.md ~/ecosystem/INVARIANTS.md ~/ecosystem/AGENTS-HARNESS.md`
- `git status --short`
- `rg -n "weighted|weight|regulator|completion|Tate|Hadamard|Mittag|admissib|quasi|duality|counterexample" ...`
- `nl -ba tate-T1-weighted-completion.tex`
- `nl -ba tate-P1-hadamard-mittag-leffler.tex`
- `nl -ba main.tex | sed -n '2580,2745p'`
- `nl -ba main.tex | sed -n '5220,5568p'`
- `nl -ba tate-T2-nilpotent-truncation.tex`
- `nl -ba tate-T3-quillen-equivalence.tex`
- `rg -n "cor:wt-cotangent-lift-unconditional|weighted-rg-locality-closed" .`
- `make pdf`
- `rg -n "undefined|Rerun|Fatal|Emergency|LaTeX Error|There were undefined references|Label\\(s\\) may have changed" out/main.log`

`make pdf` completed successfully in this worktree and updated the
generated PDF artifacts `main.pdf` and `out/main.pdf`.  The final log
scan found no unresolved-reference or fatal-error lines; the only
`Rerun` hit is the loaded `rerunfilecheck` package banner.  The build
still emits ordinary overfull/underfull box and font checksum/width
warnings from the manuscript.

## Remaining Open Questions

1. Compute the mixed brane-defect QME obstruction class
   \[
     \mathrm{Ob}_w\in
     H^1(\mathcal O_{\mathrm{loc}}(\mathcal E_w),Q+\{I_0,-\}).
   \]
   The new theorem proves weight independence of this class under
   admissibility, not its vanishing.
2. Construct a strict unweighted graph theory, or prove that no such
   theory exists, for the product/direct-sum Tate pair. The present
   obstruction is the missing Casimir.
3. Decide whether any natural tail-sensitive observables are physically
   required. If yes, they form a different completed theory and must be
   named separately.
4. If the main integration thread wants the claim ledger to reflect the
   finite-window weight-independence theorem, update
   `claim-strength-ledger.tex`; it was outside this worker's write
   surface.
