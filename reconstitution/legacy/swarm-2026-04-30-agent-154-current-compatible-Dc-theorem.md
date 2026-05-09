# Agent 154 Current-Compatible D'_c Theorem

Status: arbitrary \(\mathcal D'_c(I)\) Costello graph labels remain
obstructed.  The appendix is repaired to state the theorem-grade surface:
all compactly supported currents are allowed in the algebraic
coefficient-current kernel, while Costello graph kernels and counterterms
are proved only for regular compactly supported densities or finite
graphwise wavefront-admissible tuples.

## Owned Paths

- `appendix-factorization-current-conventions.tex`
- `reconstitution/swarm-2026-04-30-agent-154-current-compatible-Dc-theorem.md`

## Valid Attacks

```yaml
id: A1-154-01
severity: 1
status: healed
lens: source-supported theorem boundary
target: appendix-factorization-current-conventions.tex current-valued D'_c graph surface
claim: Costello or Costello--Gwilliam can be cited as proving current-valued arbitrary D'_c brane-defect graph kernels.
broken_step: Agent 147's source audit found no source support for current-valued, D'_c, bulk-to-defect, or compactly supported distributional targets in the local Costello/CG mirrors.
evidence_type: missing_source
evidence_ref: references/primary-sources/local-costello-bv-kernel-source-anchors-2026-04-30.md; appendix-factorization-current-conventions.tex:1277
confidence: high
minimal_heal: State that arbitrary D'_c graph kernels need extra renormalization data not supplied by Costello's general finite-scale package or CG vocabulary.
residual: A future theorem may import or prove such a package, but it is not in the present source fixture.
```

```yaml
id: A1-154-02
severity: 2
status: healed
lens: overclaim audit
target: appendix-factorization-current-conventions.tex:1096
claim: The wavefront relation is "the maximal extension" supplied by the graph products.
broken_step: Maximality among all possible renormalization prescriptions is not proved; only the extension asserted by the present H\"ormander/Costello operations is proved.
evidence_type: unsupported
evidence_ref: appendix-factorization-current-conventions.tex:1096
confidence: high
minimal_heal: Replace "maximal extension" by "exact extension asserted here" and add a theorem-surface proposition.
residual: None for current manuscript wording.
```

```yaml
id: A1-154-03
severity: 2
status: healed
lens: counterterm formula
target: wavefront-admissible counterterm statement
claim: Saying the extension ambiguity is supported on the collision diagonal is enough to identify the counterterm class.
broken_step: A theorem-grade current-valued counterterm statement must record the finite normal-derivative order and the distributional coefficient along the diagonal.
evidence_type: proof_gap
evidence_ref: appendix-factorization-current-conventions.tex:1215-1251
confidence: high
minimal_heal: Add \(N_{\Gamma,\alpha,\Delta}=\max\{-1,\lfloor \operatorname{sd}_\Delta(T)-\operatorname{codim}\Delta\rfloor\}\) and the formula \(\sum_{|\beta|\le N}\partial_\nu^\beta\delta_\Delta\otimes S_{\Delta,\beta}\).
residual: Actual numerical scaling-degree bounds remain part of each supplied finite-window graph package.
```

```yaml
id: A1-154-04
severity: 2
status: healed
lens: finite-window compatibility
target: distributional current counterterms
claim: Interval extension, finite-window truncation, and weight transport failures are all the same Milnor primitive obstruction.
broken_step: The Milnor \(\varprojlim^1H^0\) obstruction governs finite-window and weight-compatible primitives; interval extension failure is a factorization-compatibility residual.
evidence_type: proof_gap
evidence_ref: appendix-factorization-current-conventions.tex:1252-1276, 1313-1322
confidence: high
minimal_heal: Write the three compatibility formulas separately and separate interval-factorization failure from finite-window/weight primitive failure.
residual: None for the typed obstruction ledger.
```

```yaml
id: A1-154-05
severity: 2
status: healed
lens: arbitrary distribution counterexample
target: full \(\mathcal D'_c(I)\) graph theorem
claim: The graph theorem can be extended from wavefront-admissible tuples to every compactly supported distributional label.
broken_step: The coincident-current graph with \(B_1=B_2=\delta_{t_0}\) violates H\"ormander product transversality against the diagonal conormal of the singular boundary propagator.
evidence_type: counterexample
evidence_ref: appendix-factorization-current-conventions.tex:1148-1160, 1277-1285
confidence: high
minimal_heal: Keep arbitrary \(\mathcal D'_c(I)\) as an obstruction problem; prove only regular-density and graphwise wavefront-admissible habitats.
residual: Extra renormalization rules for failed products would be new data.
```

## Repaired Proposition

Added:

- `prop:app-current-compatible-Dprimec-theorem-surface`

Adjusted:

- `prop:app-wavefront-admissible-costello-graph-kernel` now says
  "exact extension asserted here" instead of unsupported maximality.

## Exact Formulas Added

Coefficient-current kernel, valid for arbitrary
\(B\in\mathcal D'_c(I)\):
\[
  \kappa^{\mathrm{coef}}_{\hbar,w,I}(u_{a(t)dt\otimes f})
    =\iota_I(B^w_f(a)),\qquad
  \kappa^{\mathrm{coef}}_{\hbar,w,I}(c_{B,\rho})
    =\iota_I(\Theta^w_\rho(B)).
\]

Graph product wavefront bound for
\(T^M_{\Gamma,\alpha}=K^M_{\Gamma,\alpha}B_\Gamma\):
\[
\mathrm{WF}(T^M_{\Gamma,\alpha})
\subset
\mathrm{WF}(K^M_{\Gamma,\alpha})\cup \mathrm{WF}(B_\Gamma)
\cup(\mathrm{WF}(K^M_{\Gamma,\alpha})+\mathrm{WF}(B_\Gamma)).
\]

Graph pushforward bound:
\[
  \mathrm{WF}(p_{\Gamma,*}T^M_{\Gamma,\alpha})
  \subset
  \{(y,\eta)\mid \exists x\in p_\Gamma^{-1}(y),\
  (x,dp_{\Gamma,x}^{\,t}\eta)\in
  \mathrm{WF}(T^M_{\Gamma,\alpha})\}.
\]

Counterterm ambiguity along a collision diagonal \(\Delta\):
\[
  N_{\Gamma,\alpha,\Delta}
  =
  \max\{-1,\lfloor
  \operatorname{sd}_\Delta(T^M_{\Gamma,\alpha})
  -\operatorname{codim}\Delta\rfloor\},
\]
\[
  \widetilde T'-\widetilde T
  =
  \sum_{|\beta|\leq N_{\Gamma,\alpha,\Delta}}
  \partial_\nu^\beta\delta_\Delta\otimes S_{\Delta,\beta},
  \qquad
  \operatorname{supp}S_{\Delta,\beta}
  \subset \Delta\cap\operatorname{supp}(B_\Gamma).
\]

Counterterm compatibility:
\[
  j_*C_{\Gamma,I}^{\mathrm{WF},M}(\epsilon;B_\bullet)
  =
  C_{\Gamma,J}^{\mathrm{WF},M}(\epsilon;j_*B_\bullet),
\]
\[
  \pi_{M,N}C_{\Gamma,w}^{\mathrm{WF},M}(\epsilon;B_\bullet)
  =
  C_{\Gamma,w}^{\mathrm{WF},N}(\epsilon;B_\bullet)\pi^{\mathrm{CE}}_{M,N},
\]
\[
  R^M_{w,w'}C_{\Gamma,w}^{\mathrm{WF},M}(\epsilon;B_\bullet)
  =
  C_{\Gamma,w'}^{\mathrm{WF},M}(\epsilon;B_\bullet)R^{M,\mathrm{CE}}_{w,w'}.
\]

## Verification Commands

```bash
sed -n '1,220p' CLAUDE.md
sed -n '1,240p' /Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,240p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,340p' references/primary-sources/local-costello-bv-kernel-source-anchors-2026-04-30.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-121-Dc-wavefront-extension.md
sed -n '1,280p' reconstitution/swarm-2026-04-30-agent-142-local-kernel-geometry-audit.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-147-local-costello-bv-source-audit.md
rg -n "D'_c|wavefront|H\\\"ormander|Costello|counterterm|finite-window|regular-density|current-compatible" main.tex tate-T1-weighted-completion.tex appendix-unreduced-bv-qme.tex appendix-factorization-current-conventions.tex
git diff --check -- appendix-factorization-current-conventions.tex
grep -n '[[:blank:]]$' appendix-factorization-current-conventions.tex
rg -n "label\\{([^}]*)\\}" appendix-factorization-current-conventions.tex | sed 's/.*label{//; s/}.*//' | sort | uniq -d
rg -n -e "Current-compatible" -e "maximal extension" -e "Dprimec" -e "Costello--Gwilliam" -e "compact Calabi" -e "CoHA" -e "quintic" -e "OSV" -e "GV" -e "Abel" -e "Igusa" -e "BKM" appendix-factorization-current-conventions.tex
rg -n "Agent|swarm|prior draft|previous draft|phase|version" appendix-factorization-current-conventions.tex
chktex -q appendix-factorization-current-conventions.tex
```

Results:

- `git diff --check` passed.
- trailing-whitespace grep returned no hits.
- duplicate-label scan returned no hits.
- compact/global scan found only the appendix firewall and the new
  Costello--Gwilliam non-support sentence.
- process-language scan found only ordinary mathematical uses of
  "version".
- `chktex` returned existing style warnings plus the new standard label
  placement warning for `prop:app-current-compatible-Dprimec-theorem-surface`.
  No fatal TeX error was reported.

No full `make pdf` was run because the shared checkout has concurrent
staged manuscript edits and the build writes generated output outside
this agent's assigned writable surface.

## Files Changed / Staged

- `appendix-factorization-current-conventions.tex`
- `reconstitution/swarm-2026-04-30-agent-154-current-compatible-Dc-theorem.md`

These are the only paths this agent edited and staged.

## Remaining Theorem Obligations

- No arbitrary \(\mathcal D'_c(I)\) Costello graph theorem.  Coincident
  singular labels still require new renormalization data.
- The finite-window graph package must still provide actual scaling
  degrees, graph tables, local counterterms, and incidence maps for each
  chosen graph family.
- The filtered scalar projection is proved only on its stated habitat.
  Extending it to a larger wavefront graph/counterterm complex remains a
  separate theorem.
- Vanishing of
  \(H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})\) and the
  compatible \(\varprojlim^1H^0\) primitive obstruction remains open.
- Compact Calabi--Yau, CoHA, quintic/GV/OSV, Abel--Jacobi, Igusa, and
  BKM claims remain external comparison only.
