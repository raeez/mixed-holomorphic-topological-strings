# Agent 237 attack-heal report: regular-density / wavefront current graph branch

Date: 2026-04-30.
Repo: `/Users/raeez/topological-strings`.
Owned files:

- `reconstitution/regular-density-wavefront-current-graph-branch-construction-target-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-237-regular-density-wavefront-current-graph-branch-construction-target.md`

No TeX/manuscript files were edited.

## Control surface

Loaded the repo instructions in `CLAUDE.md` and `AGENTS.md`, the ecosystem
attack-heal protocol, the Vol II `chriss-ginzburg-rectify` discipline, and the
Vol II notes/cache antipatterns for consistency only.  The Vol II check rules
out a false transfer from curve/chiral or chain-level MC/QME rhetoric into this
paper.  It supplies no theorem for the local mixed HT current graph branch.

The stable core is:

- native geometry remains `R^2_top x C^2_hol`;
- the non-scalar graph/QME target is the unreduced current/local-functional
  convolution habitat, not the reduced principal-part current algebra;
- regular densities give the strongest positive graph branch presently
  available, conditional on the named finite-window Costello graph calculus;
- wavefront distributions are allowed only by graphwise admissibility;
- arbitrary `D'_c(I)` graph contractions have a microlocal obstruction before
  cohomology unless extra renormalization data are supplied.

## Attack ledger

```yaml
- id: A237-01
  claim_attacked: "The coefficient-current kernel gives a graph/QME theorem for all D'_c(I)."
  failure_mode: "Coefficient pairing is not the same as multiplying propagator products by arbitrary pushed-forward currents and extending across diagonals."
  anchors:
    - "appendix-factorization-current-conventions.tex:1029"
    - "appendix-factorization-current-conventions.tex:1199"
    - "main.tex:7344"
    - "main.tex:7403"
  heal: "Separate the coefficient-current kernel from the Costello graph kernel.  Use D_c^reg(I) or named wavefront-admissible tuples for graph contractions."
  status: "repaired construction target"

- id: A237-02
  claim_attacked: "The regular-density package already proves the full non-scalar QME realization."
  failure_mode: "The package supplies a graph habitat and curvature certificate only after scalar-contact projection, finite-window graph data, and residual counterterm equations are fixed."
  anchors:
    - "theorem-lanes.tex:3212"
    - "claim-strength-ledger.tex:247"
    - "open-obligations.tex:342"
    - "local-dictionary.tex:1063"
  heal: "State the regular-density theorem as a certificate target: evaluated residual in X^reg, solution W=-o and C=0, with eta^reg/kappa^reg/beta/mu/lambda vanishing only under the package hypotheses."
  status: "healed without theorem downgrade"

- id: A237-03
  claim_attacked: "Wavefront-admissible labels form an automatic current source complex."
  failure_mode: "Admissibility is graphwise and tuplewise; closure under CE operations requires a chosen linear subspace whose every finite tuple remains admissible."
  anchors:
    - "appendix-factorization-current-conventions.tex:1394"
    - "appendix-factorization-current-conventions.tex:1482"
    - "claim-strength-ledger.tex:413"
  heal: "Define the wavefront branch first as D'_{c,WF}(I;Gamma,M), then require a linear subspace only after all finite tuple tests are stable."
  status: "repaired construction target"

- id: A237-04
  claim_attacked: "Singular wavefront currents can be smoothed away by finite-part choices."
  failure_mode: "The quotient S_c(I)=D'_c(I)/D_c^reg(I) detects non-smooth wavefront labels; zero-edge labels already survive as [B]."
  anchors:
    - "theorem-lanes.tex:3234"
    - "tate-T1-weighted-completion.tex:2398"
    - "claim-strength-ledger.tex:247"
  heal: "Use eta^reg_{n0,M}=[s^WF_{n0,M}] as the exact regular-density obstruction.  It is killed in the original complex only by a degree-zero singular primitive."
  status: "obstruction theorem"

- id: A237-05
  claim_attacked: "The wavefront primitive cone solves the original current graph branch."
  failure_mode: "Adjoining a formal primitive changes the complex; it proves a relative extension, not exactness in the original current/local-functional habitat."
  anchors:
    - "theorem-lanes.tex:3234"
    - "tate-T1-weighted-completion.tex:2584"
  heal: "Record the primitive equation d p^WF=-hat{s}^WF as an extension target.  Preserve the original exactness criterion bar d q(C^sing)=-s^WF."
  status: "healed by exact distinction"

- id: A237-06
  claim_attacked: "The Vol II chiral/topological apparatus can supply the missing graph branch."
  failure_mode: "Vol II control notes flag chain/model conflations and curve/chiral transfers.  This paper's native graph branch is local mixed HT on C^2 with current-compatible Costello kernels."
  anchors:
    - "/Users/raeez/chiral-bar-cobar-vol2/notes/first_principles_cache.md"
    - "/Users/raeez/chiral-bar-cobar-vol2/notes/antipatterns_catalogue.md"
    - "CLAUDE.md"
    - "AGENTS.md"
  heal: "Use Vol II only as a control-surface antipattern check.  Do not import SC_ch,top or chain-level MC/QME identifications."
  status: "quarantined"

- id: A237-07
  claim_attacked: "The finite-window script already enumerates the missing graph package."
  failure_mode: "The script explicitly refuses to guess Costello graph integrals/counterterms and lists regular-density/wavefront locality, row bases, signs, scalar projection, and graph weights as missing data."
  anchors:
    - "scripts/finite_window_graph_array.py:1"
    - "scripts/finite_window_graph_array.py:1872"
  heal: "Use the script as an obstruction ledger and verification guard, not as a graph construction."
  status: "repaired evidence status"
```

## Exact formulas to carry forward

Source:

```tex
\mathfrak g^{w,cur}_{\hbar,I}
  =
  (\Omega_c^\bullet(I)\widehat\otimes \mathfrak h_{w,\hbar})
  \ltimes
  (\mathcal D'_c(I)\widehat\otimes \mathfrak h^\vee_{w,\hbar})[1].
```

Curvature:

```tex
Curv(\kappa) = d_{QME}\kappa + {1\over 2}[\kappa,\kappa]_\hbar.
```

Scalar-contact gate:

```tex
\widehat\sigma_{sc}(Curv(\kappa))=0,
\qquad
[Curv(\kappa)] \in H^1(\ker\widehat\sigma_{sc},d_{QME}).
```

First non-scalar residual after lower counterterms:

```tex
o^{ns}_{n_0,M}
 =
[\hbar^{n_0}]
\left(
 Ob^{red}_{w,\partial,\hbar,M}
 + d_M C_{<n_0,M}
 + {1\over 2}\{ C_{<n_0,M}, C_{<n_0,M}\}_{\hbar,M}
\right).
```

Wavefront quotient obstruction:

```tex
S_c(I)=D'_c(I)/D_c^{reg}(I),
\qquad
\eta^{reg}_{n_0,M}=[s^{WF}_{n_0,M}]
  \in H^1(\mathfrak Q^\bullet_{w,M}(I)/X^{reg}_{w,M}(I)).
```

Original-complex kill criterion:

```tex
\bar d_M q_M(C^{sing}_{n_0,M})=-s^{WF}_{n_0,M}.
```

Fixed-window linear obstruction:

```tex
A^M c=-r^M,
\qquad
\ell A^M=0,\quad \ell(r^M)\ne 0.
```

## Construction target

The next theorem should assert a current-compatible finite-scale graph calculus
on `D_c^reg(I)` and on a named wavefront-admissible subspace, with:

- finite-scale weighted propagator `P^{w,M}_{epsilon,L}` and BV Laplacian;
- graph products passing Hormander transversality;
- finite-scaling diagonal extensions and local counterterms;
- interval, truncation, and weight compatibility;
- chain scalar-contact projection `\widehat\sigma_{sc}`;
- fixed-window counterterm equations and Roos tower compatibility;
- exact obstruction class `\eta^{reg}` for surviving singular wavefront
  components;
- explicit microlocal no-canonical-product obstruction for non-admissible
  arbitrary `D'_c(I)` labels.

## Verification commands

Commands run or used as anchors:

```bash
git status --short
rg -n "regular-density|wavefront|eta\\^\\{reg\\}|D'_c|scalar-contact|Curv\\(\\kappa\\)" \
  local-dictionary.tex claim-strength-ledger.tex open-obligations.tex theorem-lanes.tex main.tex
rg -n "regular-density|wavefront|D'_c|Hormander|eta\\^\\{reg\\}|primitive" \
  appendix-factorization-current-conventions.tex tate-T1-weighted-completion.tex
python3 scripts/finite_window_graph_array.py
rg -n "QME|MC|chiral|antipattern|strict|model" /Users/raeez/chiral-bar-cobar-vol2/notes
```

`python3 scripts/finite_window_graph_array.py` exited successfully and reported
the relevant missing order-two row types, including regular-density or
wavefront-admissible locality data for every external current label.  This
supports the obstruction-ledger status and does not construct the missing
Costello graph package.
