# Agent 110 - Balanced Graph Extension

Status: patched owned appendix surface; no commits or pushes.

## Stable Core

The balanced scalar-contact theorem does not extend automatically to the
full Costello graph/counterterm habitat.  The theorem-grade positive
extension is the identity-loop subcomplex: every new graph or
counterterm scalar symbol, and the scalar symbol of its
`d_QME`-boundary, must factor as

```tex
\sigma_{\mathrm{sc}}(\operatorname{gr}_F X_{\Gamma,M})
  =
\operatorname{Str}(\operatorname{id}_V)\tau_{\Gamma,M}.
```

For `V = C^{N|N}`, this coefficient is `sdim(V)=0`, so the zero
scalar projection remains a filtered chain map on that specified
graph/counterterm subcomplex.

For any larger graph/counterterm enlargement, the exact obstruction is
relative to the already proved balanced habitat:

```tex
\overline{\mathfrak G}_{\mathrm{Cost}}
  =
\mathfrak G_{\mathrm{Cost}}/
\mathfrak H_{\mathrm{bal,sc}}.
```

The associated-graded defect is the actual chain-map defect

```tex
\delta^{(0)}_{\mathrm{Cost},\sigma}
  =
d_{\mathrm{CE}}\bar\sigma_{\mathrm{Cost}}
  -\bar\sigma_{\mathrm{Cost}}d_{\operatorname{gr}}.
```

After this vanishes, the first positive filtration obstruction is the
relative Hom-complex class

```tex
\mathfrak o^{(r)}_{\mathrm{Cost},\sigma}
  =
[\delta_s^{(-r)}]
  \in
H^1 Hom(gr_F(\overline{\mathfrak G}_{\mathrm{Cost}}), S)_{-r}.
```

On a graph or counterterm generator this is computed by

```tex
\mathfrak o^{(r)}_{\mathrm{Cost},\sigma}(X_{\Gamma,M})
  =
\left[
  d_{\mathrm{CE}}s(X_{\Gamma,M})
  -
  \sum_{\Gamma'}\varepsilon_{\Gamma,\Gamma'}s(X_{\Gamma',M})
\right]_{F^{p-r}/F^{p-r+1}},
```

where

```tex
d_{\mathrm{QME}}X_{\Gamma,M}
  =
\sum_{\Gamma'}\varepsilon_{\Gamma,\Gamma'}X_{\Gamma',M}
\quad \bmod F^{p-r+1}.
```

## Attack Ledger

```yaml
- id: A1-110-01
  severity: 1
  status: healed
  lens: full-graph overreach
  target: balanced scalar-contact extension
  claim: Agent 103's balanced scalar-contact zero projection extends to the full Costello graph/counterterm habitat.
  broken_step: Costello's general graph calculus does not imply that Hamiltonian brane-defect graph counterterms have only identity-loop scalar symbols.
  evidence_type: source_conflict
  evidence_ref: references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md, reports 102 and 103
  confidence: high
  blast_radius: false non-scalar Costello graph/QME theorem
  minimal_heal: restrict the positive theorem to the identity-loop balanced graph subhabitat and state the relative obstruction for enlargements
  residual: construct the actual Hamiltonian Costello graph/counterterm complex and compute its scalar symbols

- id: A1-110-02
  severity: 1
  status: healed
  lens: associated-graded chain map
  target: graph scalar-symbol extractor
  claim: The first obstruction is always a positive-filtration Hom cohomology class.
  broken_step: Before the positive-filtration class is defined, the associated-graded scalar extractor must already be a chain map.
  evidence_type: proof_gap
  evidence_ref: Lemma app filtered scalar projection obstruction assumes the associated graded projection is a chain map
  confidence: high
  blast_radius: would call a non-chain scalar extractor a filtered projection
  minimal_heal: add the zeroth defect delta^(0) = d_CE sigma - sigma d_gr as an equality, then define the positive Hom class
  residual: none inside the obstruction theorem

- id: A1-110-03
  severity: 2
  status: healed
  lens: computability
  target: extension obstruction formula
  claim: Saying "some o_sigma class" is enough for the graph/counterterm extension.
  broken_step: The graph habitat needs a formula in terms of the actual graph differential, counterterm boundary, and scalar-symbol lift.
  evidence_type: proof_gap
  evidence_ref: task evidence standard; open-obligations closed-exchange branch
  confidence: high
  blast_radius: leaves the next agent without a computable obstruction
  minimal_heal: add the generator-level formula using d_QME X_Gamma = sum eps X_Gamma'
  residual: compute epsilons and scalar symbols for a supplied Costello specialization
```

## Repairs Made

Added `def:app-balanced-costello-graph-subhabitat`, defining the
identity-loop graph/counterterm subcomplex with finite-window and weight
compatibility.

Added `prop:app-balanced-costello-graph-preservation`, proving that this
specified graph/counterterm subcomplex remains inside the balanced
scalar-contact habitat and has zero scalar projection for `C^{N|N}`.

Added `thm:app-costello-graph-extension-obstruction`, giving the exact
relative obstruction for any larger Costello graph/counterterm
enlargement, including the generator-level formula.

## Verification

Run in this turn:

```bash
rg -n "balanced-costello-graph|costello-graph-extension|Balanced graph/counterterm preservation" appendix-unreduced-bv-qme.tex
git diff --check -- appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-110-balanced-graph-extension.md
chktex -q appendix-unreduced-bv-qme.tex
```

`git diff --check` passed.  `chktex` returned style warnings in the
existing appendix pattern, including label and parenthesis warnings; it
reported no fatal TeX error.  No `make pdf` was run.  The shared checkout already has concurrent
tracked changes, and the build writes tracked output outside this
agent's writable surface.

## Remaining Obligations

1. Supply the actual Hamiltonian Costello graph/counterterm complex
   `\mathfrak G_{\mathrm{Cost}}`.
2. Compute the graph orientation signs
   `\varepsilon_{\Gamma,\Gamma'}` and scalar symbols for each first
   non-identity-loop graph or counterterm.
3. Prove that the closed-exchange complex and map `\Xi` of the Agent 104
   branch land in the relative kernel after the zeroth and positive
   scalar-extension obstructions vanish.
