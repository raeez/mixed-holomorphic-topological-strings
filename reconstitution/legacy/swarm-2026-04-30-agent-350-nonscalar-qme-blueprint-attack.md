# Agent 350: Non-Scalar QME Blueprint Attack

Status: report-only.  No TeX, script, figure, bibliography, PDF, or build
artifact was edited.

## Claim Attacked

Agent 344 proposes a manuscript insertion for a finite-window
\(\theta_3\) Bianchi counterterm-column theorem.  The proposed datum contains
\[
  B^M_{02,20}\in\mathcal K^0_{\mathrm{ns},M}(I),\qquad
  d_{\mathrm{ns},M}B^M_{02,20}=-\mathfrak b^M,
  \qquad
  \widehat\sigma_{\mathrm{sc},M}(B^M_{02,20})=0,
\]
plus transport corrections \(H^{M,N}_{02,20}\) and a secondary
\(\varprojlim^1H^0\) vanishing condition.  The theorem then asserts that
\[
  P^M_{02,20}=D^M_{02,20}+B^M_{02,20}
\]
kills the lower transported \(\theta_3\) residual.

## Verdict

Not admissible as a manuscript theorem skeleton in its present form.

The \(N=2\) matrix signs in Agent 344 are correct.  If a genuine column
\[
  A_B^2=(0,0,-1)^T
\]
is supplied, then
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
This is only the formal acceptance calculation.  The current checkout does
not construct \(B^2_{02,20}\), does not construct a tower \(B^M\), and does
not supply the Bianchi transport or secondary Roos data.

Under Supremum Discipline, the proposed block may be used only as a
proof-ledger criterion or recognition lemma after strengthening its
hypotheses.  It should not be inserted as a positive theorem called
"Finite-window \(\theta_3\) Bianchi counterterm column" unless the actual
local functional \(B^M_{02,20}\) and its transport data are constructed in
the text.

## Checked Anchors

- `main.tex:8613-8847`: non-scalar QME is a filtered local-functional
  obstruction problem requiring scalar projection, kernel, counterterms,
  centrality homotopies, and curved bulk-to-defect kernel.
- `main.tex:8849-9118`: current \(\theta_3\) acceptance gate, lower
  Bianchi-exposed matrix, cokernel certificate, and transport obstruction.
- `appendix-unreduced-bv-qme.tex:2077-2246`: the non-scalar kernel
  \(\mathcal K^\bullet_{\mathrm{ns},M}\) exists only after the scalar
  projection is a filtered chain map.
- `appendix-unreduced-bv-qme.tex:2248-2399`: finite-row criterion
  \(A^Mc=-r^M\), transition identities, and Roos \(H^0\) gate.
- `appendix-unreduced-bv-qme.tex:2501-2642`: appendix lower
  Bianchi-exposed gate with \(A_D^2\), \(r_2\), \(A_B^2\), and
  \(\Delta^1_{M,N}\).
- `open-obligations.tex:900-957`: current open target already names the
  missing \(B^2_{02,20}\), locality or wavefront admissibility,
  \(\Delta^1_{M,N}\), and secondary \(\varprojlim^1H^0\) class.
- `theorem-lanes.tex:3543-3611`: theorem lane already records the same
  controlled enlargement target.
- `claim-strength-ledger.tex:500-550` and `claim-strength-ledger.tex:924-994`:
  ledger classifies the lane as an exact obstruction target until a
  constructive witness is supplied.

## Formula Audit

The lower-window signs are coherent.  In the exposed basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}),
\]
the source-coordinate primitive
\[
  D^2_{02,20}=K^2_{\Theta_3}(u_{a,H_{1,0}}u_{b,H_{0,1}})
\]
has
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}+\mathfrak b^2_{02,20},
\]
so
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T.
\]
The equation \(A_D^2c=-r_2\) is inconsistent.  The cokernel
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*+(\mathfrak b^2_{02,20})^*
\]
annihilates \(A_D^2\), evaluates to \(1\) on \(r_2\), and evaluates to
\(-1\) on the desired target \((0,0,-1)^T\).  Thus the current habitat has
an exact obstruction, not a hidden primitive.

The transport sign is also correct:
\[
  d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N
  =
  \Delta^1_{M,N}.
\]
If \(d_{\mathrm{ns},N}H^{M,N}=\Delta^1_{M,N}\), then
\[
  \pi_{M,N}B^M-B^N-H^{M,N}
\]
is closed.  The missing point is not this sign; it is the absence of
coherent transition and Roos data.

## Fatal Admissibility Defects

1. The theorem assumes the missing object.  The proposed datum includes
   \(B^M_{02,20}\) with \(dB=-\mathfrak b^M\).  The proof then expands this
   hypothesis.  This is a valid recognition criterion, not a positive
   theorem under Supremum Discipline.

2. The current manuscript already contains the criterion.  Main,
   appendix, theorem-lane, open-obligation, and claim-ledger anchors already
   say that a genuine scalar-zero local-functional column
   \(A_B^2=(0,0,-1)^T\) with locality and transport would heal the lower row.
   Agent 344's insertion would mostly duplicate the live theorem surface.

3. The skeleton does not state that \(D^M_{02,20}\) is scalar-zero.  It calls
   \(P^M=D^M+B^M\) a scalar-zero local functional, but the definition only
   puts \(B^M\) in \(\mathcal K^0_{\mathrm{ns},M}\).  It must require
   \(D^M_{02,20}\in\mathcal K^0_{\mathrm{ns},M}(I)\), or directly require
   \(\widehat\sigma_{\mathrm{sc},M}(P^M_{02,20})=0\).

4. The finite-window habitat is under-specified.  The theorem must fix the
   marked Costello graph package, the codimension-two closed row table, the
   source-face signs, the row basis containing
   \(E^M_{\nu_{02}},E^M_{\nu_{20}},\mathfrak b^M\), and the renormalized
   weights \(K^M_{\Theta_3}\).  A formal column is not a local functional.

5. The analytic representative is not constructed.  The missing \(B^M\) needs
   a regular-density graph counterterm or a graphwise wavefront-admissible
   counterterm with pullback, product, extension, finite-scaling, pushforward,
   and counterterm estimates.  Costello/Hormander source theorems give the
   habitat and obstruction calculus; they do not prove this particular
   Bianchi defect exact.

6. The scalar projection hypothesis is too compressed.  Since
   \(\mathcal K_{\mathrm{ns},M}\) is a complex only when
   \(\widehat\sigma_{\mathrm{sc},M}\) is a filtered chain map, the enlarged
   \(B\)-habitat must carry the scalar projection lift, not merely the
   equation \(\widehat\sigma_{\mathrm{sc},M}(B^M)=0\).

7. The Roos condition is not fully typed.  The proposed
   \(\Delta^0_{M,N}\) defines a \(\varprojlim^1\) class only after the
   transition maps form an inverse system on cohomology and the chosen
   corrections \(H^{M,N}\) give a Roos \(1\)-cocycle, or after the defect of
   that cocycle is itself killed.  The zero-class assertion should be stated
   as a class of \([\Delta^0_{M,N}]\in H^0(\mathcal K^\bullet_{\mathrm{ns},N})\)
   in the Roos complex, with the explicit coboundary witnessing zero.

8. The all-window source-coordinate formula is not proved by the current
   lower-window calculation.  The live TeX proves the \(N=2\) source
   primitive and names \(\mathfrak b^M\) for the tower.  A theorem over all
   \(M\ge2\) must provide the \(M\)-window source-face decomposition and
   transition matrices, not just extrapolate the \(N=2\) row.

9. The open-obligations and theorem-lanes patch blocks should not be appended
   verbatim.  They duplicate existing paragraphs at `open-obligations.tex:940-957`
   and `theorem-lanes.tex:3593-3611`.  If a patch is later authorized, it
   should replace and sharpen those paragraphs, not create a second copy.

## Admissible Replacement

The admissible manuscript object is a criterion with a guarded title, for
example:

\[
  \text{Criterion: supplied \(\theta_3\) Bianchi counterterm column.}
\]

It may state:

- fix a native finite-window realization habitat with a filtered chain
  scalar projection and a codimension-two closed marked row table;
- assume \(D^M_{02,20}\), \(B^M_{02,20}\), and all rows lie in the
  scalar-zero kernel;
- assume \(B^M_{02,20}\) is an actual regular-density or graphwise
  wavefront-admissible local functional with
  \(d_{\mathrm{ns},M}B^M_{02,20}=-\mathfrak b^M\);
- assume explicit transition maps and corrections \(H^{M,N}\) kill
  \(\Delta^1_{M,N}\) and that the resulting closed classes are a zero Roos
  \(1\)-cocycle in \(\varprojlim^1H^0\).

Then the proof is the two-line calculation
\[
  d_{\mathrm{ns},M}(D^M_{02,20}+B^M_{02,20})
  =
  -2E^M_{\nu_{02}}+2E^M_{\nu_{20}}.
\]
This is useful as a gate.  It does not construct the gate.

## Claim-Status Recommendation

Reject Agent 344's theorem skeleton as a positive manuscript insertion.
Keep the finite-window matrix calculation and \(\Delta^1\) sign.  Convert the
block, if used, into a recognition criterion after adding the missing
scalar-zero \(D\)-hypothesis, habitat data, analytic local-functional
construction clause, transition matrices, Roos cocycle typing, and explicit
zero-class witness.

The theorem-grade construction target remains:
\[
  B^M_{02,20}\in\mathcal K^0_{\mathrm{ns},M}(I),
  \qquad
  d_{\mathrm{ns},M}B^M_{02,20}=-\mathfrak b^M,
\]
as an actual Costello-local regular-density or wavefront-admissible
counterterm with scalar projection lift and compatible finite-window Roos
transport.  Until that object is supplied, the current exact obstruction
\(\widetilde\lambda_{02,\mathfrak b}\) remains binding.

## Verification

Read:

- `CLAUDE.md`
- `AGENTS.md`
- `/Users/raeez/ecosystem/INVARIANTS.md`
- `/Users/raeez/ecosystem/AGENTS-HARNESS.md`
- `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `reconstitution/swarm-2026-04-30-agent-344-nonscalar-qme-patch-blueprint.md`
- `reconstitution/swarm-2026-04-30-agent-338-nonscalar-qme-next-supremum-plan.md`
- `reconstitution/swarm-2026-04-30-agent-294-theta3-actual-local-functional-b-column-construction-push.md`
- `reconstitution/swarm-2026-04-30-agent-299-theta3-roos-transport-obstruction-push.md`
- `reconstitution/swarm-2026-04-30-agent-301-theta3-costello-counterterm-source-theorem-search.md`
- `reconstitution/swarm-2026-04-30-agent-304-theta3-h1-bianchi-transport-class-construction.md`
- `reconstitution/swarm-2026-04-30-agent-308-theta3-restricted-habitat-counterterm-theorem-design.md`
- `reconstitution/swarm-2026-04-30-agent-313-theta3-restricted-counterterm-theorem-frontier.md`
- `reconstitution/swarm-2026-04-30-agent-322-theta3-matrix-notation-consistency-audit.md`
- `reconstitution/swarm-2026-04-30-agent-332-appendix-theta3-notation-heal.md`
- `main.tex`, `appendix-unreduced-bv-qme.tex`, `open-obligations.tex`,
  `theorem-lanes.tex`, and `claim-strength-ledger.tex` at the anchors above.

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
rg -n "theta|theta_3|Bianchi|non-scalar|nonscalar|Costello|Roos|counterterm|A_D|A_B|Delta\\^1|varprojlim\\^1|b\\^M|mathfrak b" claim-strength-ledger.tex
rg -n "theta|theta_3|Bianchi|non-scalar|nonscalar|Costello|Roos|counterterm|A_D|A_B|Delta\\^1|varprojlim\\^1|b\\^M|mathfrak b" main.tex appendix-unreduced-bv-qme.tex theorem-lanes.tex open-obligations.tex
```

`git diff --check -- reconstitution/swarm-2026-04-30-agent-350-nonscalar-qme-blueprint-attack.md`
produced no output.  Since the report is untracked, I also ran
`git diff --no-index --check /dev/null reconstitution/swarm-2026-04-30-agent-350-nonscalar-qme-blueprint-attack.md`;
result: no whitespace or conflict-marker warnings.
