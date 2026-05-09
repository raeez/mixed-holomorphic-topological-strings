# Agent 212 Report: Supremum Downgrade Hunt

Date: 2026-04-30.

Owned write paths:

- `claim-strength-ledger.tex`
- `reconstitution/swarm-2026-04-30-agent-212-supremum-downgrade-hunt.md`

## Claim Attacked

The control surface still contained lazy status words: `open`,
`conditional`, and `external-input-relative` in places where the
manuscript already has a sharper construction theorem, exact finite-row
obstruction, or false-transfer fence.

## Repairs Inscribed

1. `Stage A6` no longer says the degree-zero Moyal trace comparison is
   external-input-relative.  It is now the finite-certificate-relative
   radial/Weyl trace comparison with a uniform-homotopy gate.

2. The two `open` status-table rows for
   \(Z^{P_0}_{\mathrm{fact}}\) and the full open BV identification were
   replaced by exact construction problems: product and \(P_0\)-centrality
   homotopies, stratified descent, Costello brane-defect QME kernel,
   principal-part current lift, coefficient kernel, and brane-defect
   propagator.

3. The `conditional finite-window datum` row was replaced by a
   finite-window row-closure datum.  A finite seed list becomes a theorem
   only after field-differential, BV-edge, collision, counterterm, and
   source faces close with codimension-two signs and marker transports.
   Before that, no non-scalar \(H^1/\varprojlim^1\) class is defined.

4. The radial/Weyl rows were upgraded from external-input language to the
   free normal-diagram obstruction
   \[
     \mathfrak o^{\mathrm{rad}}_{a,b}
       =[R^{\mathrm{free}}_{a,b}]
       \in\operatorname{coker}\mathcal C_{a,b}.
   \]
   The strongest theorem is the functorial splitting of
   \(\mathcal C_{a,b}\), equivalently compatible corrections
   \(K_{a,b}\).  A left-cokernel functional is the exact obstruction.
   The \((7,7)\) target is recorded as an unfinished computation, not a
   nonzero obstruction.

5. A dedicated Supremum controller item was added for radial/Weyl finite
   certificates and uniform homotopy.  It records the proved algebraic
   surface: Moyal coefficients, open-line Wick weights, Capelli
   triangular normalization, free normal ordering, stable trace-diagram
   injectivity, the all-\(N\) \(K_{4,4}\) correction, and the finite
   certificate range.

6. The quantum Hamiltonian/Moyal theorem-data row now points to the
   moment-ideal primitive first and then to the sharper
   \(\operatorname{coker}\mathcal C_{a,b}\) obstruction class.  The
   componentwise quantum coefficient surface is now relative to the
   finite-certificate radial/Weyl gate, not an unnamed external input.

7. The native \(\mathbb C^2\) \(E_2\)/BM controller was sharpened from a
   generic missing-transfer phrase to the strongest current form:
   CE/factorization and semidirect collision algebra proved, finite-window
   BM arity-two transfer proved, and all-window strict transfer obstructed
   precisely by
   \[
     \operatorname{Ob}^{\infty}_{\mathrm{BM}}
      =(\operatorname{ob}_{\mathrm{mom}},
        \operatorname{ob}_{\mathrm{collar}},
        \operatorname{ob}_{3},
        \operatorname{ob}_{\mathrm{unif}}).
   \]

## Evidence Checked

- `open-obligations.tex:298-515`: non-scalar QME obstruction vector and
  \(\theta_3\) one-row finite-window certificate.
- `open-obligations.tex:560-725`: normal \(\Omega\) finite-window
  localization, parameter separation, stratified object, and QME
  obstruction vector.
- `open-obligations.tex:833-886`: radial/Weyl finite certificates and
  uniform homotopy gate.
- `appendix-radial-parts-moyal.tex:455-895`: quantum shear primitive,
  free trace-diagram obstruction, \(K_{4,4}\), stable injectivity, and
  kernel-homotopy obstruction.
- `theorem-lanes.tex:2450-2635`, `2768-2820`, `2868-3090`: componentwise
  quantum surface, Omega gate, theta-row primitive interface, and graph
  branch catalogue.

## Verification Commands

```bash
git status --short
git diff -- claim-strength-ledger.tex
git diff --staged -- claim-strength-ledger.tex
sed -n '1,220p' CLAUDE.md
sed -n '1,260p' AGENTS.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,220p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '1,260p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
nl -ba claim-strength-ledger.tex
rg -n -i -e 'conditional' -e 'still open' -e '\bopen\b' -e 'external input' -e 'external-input' -e 'theorem surface' -e 'theorem-surface' -e 'conjectural' --glob '*.tex'
rg -n -e 'theta_3' -e 'theta3' -e 'Theta_3' -e 'finite-window' -e 'non-scalar' -e 'scalar-zero' -e 'Roos' -e 'companion' theorem-lanes.tex open-obligations.tex appendix-unreduced-bv-qme.tex tate-P1-hadamard-mittag-leffler.tex reconstitution/swarm-2026-04-30-agent-197-theta3-source-to-construction-spec.md reconstitution/swarm-2026-04-30-agent-198-nonscalar-costello-qme-realization.md reconstitution/swarm-2026-04-30-agent-204-nonscalar-qme-integration-consistency.md reconstitution/swarm-2026-04-30-agent-207-theta3-validator-manuscript-integration.md
rg -n 'radial|Weyl|Moyal|quantum shear|uniform homotopy|finite certificate|Capelli|moment-ideal|J_N|radial image|Hadamard|Mittag' appendix-radial-parts-moyal.tex tate-P1-hadamard-mittag-leffler.tex theorem-lanes.tex open-obligations.tex reconstitution/*.md scripts/*.py
python3 scripts/quantum_shear_trace_diagram_normal_form.py --case 4,4 --classical-only
python3 scripts/quantum_shear_trace_diagram_normal_form.py --case 4,4
python3 scripts/finite_window_graph_array.py
git diff --check -- claim-strength-ledger.tex reconstitution/swarm-2026-04-30-agent-212-supremum-downgrade-hunt.md
```

The classical-only radial command intentionally returned nonzero and
printed the four-term residual.  The corrected \(K_{4,4}\) command passed
with zero residual.  The finite-window graph-array output reproduced the
\(\theta_3\) cokernel covector \(\ell_{\theta_3}(\mathsf E_{\theta_3})=1\)
and the accepted payload gates only when \(dC=-E\) is supplied.

## Files Changed

- `claim-strength-ledger.tex`
- `reconstitution/swarm-2026-04-30-agent-212-supremum-downgrade-hunt.md`
