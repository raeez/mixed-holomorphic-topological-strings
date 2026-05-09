# Agent 119 - Supertraceless-Monodromy Subhabitat

Status: patched owned surfaces; no commits or pushes.

## Stable Core

The word-level condition is:
\[
  \operatorname{st}(T_\bullet)
    =
  \operatorname{Str}(T_1\cdots T_m)=0.
\]
It is a condition on the ordered product, not on the individual markers.
The empty word is allowed in the balanced model because
\[
  \operatorname{Str}(\operatorname{id}_{\mathbb C^{N|N}})=0.
\]

The supertraceless-monodromy prehabitat is the closed filtered span of
graph/counterterm representatives whose scalar-contact associated-graded
loop words are supertraceless.  The exact preservation obstruction is the
family
\[
  \mathcal B_{\operatorname{st}=0}(X;q)
    =
  \Pi_{\operatorname{st}\neq0}
  \left([d_{\mathrm{QME}}X]_{F^q/F^{q+1}}\right).
\]
It vanishes exactly when the prehabitat is a
\(d_{\mathrm{QME}}\)-stable subcomplex.  Under that hypothesis the zero
scalar projection is a filtered chain map, and the scalar-projection
obstruction tower vanishes there.

For the unmarked Hamiltonian boundary generators already treated in the
appendix, preservation holds: their scalar loops carry only the empty
word, and the displayed differential \(Q+\{I_0,-\}\) has no noncentral
\(\operatorname{End}(V)\)-marker to insert.  This does not prove
preservation for larger marked Costello specializations.

## Attack Ledger

```yaml
- id: A1-119-01
  severity: 1
  status: healed
  lens: monodromy-word definition
  target: appendix-unreduced-bv-qme.tex, marked-loop enlargement
  claim: It is enough for each marker T_i to be supertraceless.
  broken_step: Supertrace is applied to the ordered product T_1...T_m; products of traceless endomorphisms can have nonzero supertrace.
  evidence_type: direct_computation
  evidence_ref: prop:app-first-nonidentity-loop-scalar-symbol computes hbar Str(T_1...T_m) omega(f,g) gamma_1.
  files_read: [appendix-unreduced-bv-qme.tex, reconstitution/swarm-2026-04-30-agent-115-first-nonidentity-loop-symbol.md]
  tools_used: [sed, rg, nl]
  confidence: high
  blast_radius: Would admit marked loops with nonzero scalar CE class.
  minimal_heal: Define allowed words by Str(T_1...T_m)=0, explicitly not letterwise tracelessness.
  residual: None inside the word-level definition.
  deciding_evidence: The ordered-loop scalar contraction formula.

- id: A1-119-02
  severity: 1
  status: healed
  lens: differential preservation
  target: proposed supertraceless-monodromy subcomplex
  claim: Zero scalar symbols on generators automatically make a d_QME-stable subcomplex.
  broken_step: d_QME may create boundary terms with non-supertraceless loop words.
  evidence_type: proof_gap
  evidence_ref: Agent 115 residual obligation; thm:app-supertraceless-monodromy-projection now defines B_{st=0}.
  files_read: [appendix-unreduced-bv-qme.tex, reconstitution/swarm-2026-04-30-agent-110-balanced-graph-extension.md, reconstitution/swarm-2026-04-30-agent-115-first-nonidentity-loop-symbol.md]
  tools_used: [sed, rg, nl]
  confidence: high
  blast_radius: Would falsely turn a prehabitat into a chain complex.
  minimal_heal: Define the quotient obstruction Pi_{st!=0}([d_QME X]_{F^q/F^{q+1}}) and make vanishing equivalent to preservation.
  residual: Compute this quotient for any supplied marked graph/counterterm list.
  deciding_evidence: The actual d_QME boundary expansion in the chosen Costello specialization.

- id: A1-119-03
  severity: 1
  status: healed
  lens: scalar projection
  target: zero scalar projection on supertraceless monodromy
  claim: The zero projection remains a chain map without checking d_QME images.
  broken_step: A chain-map assertion requires the source to be preserved by the differential, or an explicit extension to the ambient complex.
  evidence_type: proof_gap
  evidence_ref: lem:filtered-scalar-projection-obstruction requires a filtered chain projection.
  files_read: [appendix-unreduced-bv-qme.tex]
  tools_used: [nl]
  confidence: high
  blast_radius: Would leave the scalar-lift obstruction tower unbound.
  minimal_heal: Prove zero projection only after B_{st=0}=0; then both d_CE sigma and sigma d_QME vanish.
  residual: None once preservation is verified.
  deciding_evidence: Vanishing of B_{st=0}.

- id: A1-119-04
  severity: 2
  status: healed
  lens: displayed-generator preservation
  target: actual Hamiltonian generators in the appendix
  claim: Preservation cannot be proved for any concrete generator set.
  broken_step: The unmarked Hamiltonian boundary generators and identity-loop graph generators carry only the empty word, and Q+{I_0,-} as displayed has no inserted noncentral marker.
  evidence_type: proof
  evidence_ref: thm:app-balanced-supertrace-qme-cancellation; def:app-balanced-costello-graph-subhabitat; thm:app-supertraceless-monodromy-projection.
  files_read: [appendix-unreduced-bv-qme.tex]
  tools_used: [nl, rg]
  confidence: medium
  blast_radius: Would leave a true positive preservation statement unrecorded.
  minimal_heal: Prove preservation for the unmarked/identity-loop displayed generator set and explicitly exclude larger marked specializations.
  residual: Does not decide graph habitats containing idempotents, holonomies, or counterterm tensors.
  deciding_evidence: A full marked graph/counterterm differential.
```

## Repairs Made

Added `def:app-supertraceless-monodromy-prehabitat`, defining allowed
monodromy words, the prehabitat, and the quotient preservation
obstruction \(\mathcal B_{\operatorname{st}=0}\).

Added `thm:app-supertraceless-monodromy-projection`, proving:

- the prehabitat is \(d_{\mathrm{QME}}\)-stable exactly when
  \(\mathcal B_{\operatorname{st}=0}=0\);
- under that condition, \(\widehat\sigma_{\operatorname{st}=0}=0\) is a
  filtered chain map;
- the first obstruction on a generator is the non-supertraceless quotient
  of its \(d_{\mathrm{QME}}\)-boundary, with scalar CE shadow
  \[
    \hbar\sum \varepsilon_{\Gamma,\Gamma',U_\bullet}
      \operatorname{Str}(M(U_\bullet))[\bar c]\gamma_{\mathbf 1};
  \]
- the unmarked Hamiltonian boundary generators and identity-loop graph
  generators appearing in the appendix satisfy preservation.

## Verification

Commands run:

```bash
git diff --check -- appendix-unreduced-bv-qme.tex
chktex -q appendix-unreduced-bv-qme.tex
rg -n -F "def:app-supertraceless-monodromy-prehabitat" appendix-unreduced-bv-qme.tex
rg -n -F "thm:app-supertraceless-monodromy-projection" appendix-unreduced-bv-qme.tex
rg -n -F "mathcal B_{\\operatorname{st}=0}" appendix-unreduced-bv-qme.tex
rg -n -F "widehat\\sigma_{\\operatorname{st}=0}" appendix-unreduced-bv-qme.tex
```

`git diff --check` passed.  The `rg -F` anchor checks found the new
definition, theorem, obstruction, and zero projection.  `chktex` returned
style warnings in the existing appendix pattern, including label-spacing,
dash, and parenthesis warnings; it reported no fatal TeX error.  No full
`make pdf` was run because the shared checkout has concurrent tracked
edits and the build writes tracked output outside this agent's writable
surface.

## Residual Obligations

1. Supply the actual marked Hamiltonian Costello graph/counterterm
   complex, including all monodromy words and \(d_{\mathrm{QME}}\)
   boundary signs.
2. Compute \(\mathcal B_{\operatorname{st}=0}\) for that marked complex.
3. Prove gauge equivariance excludes noncentral fixed markers, or include
   the resulting invariant tensors in the obstruction calculation.
4. If \(\mathcal B_{\operatorname{st}=0}\neq0\), kill its scalar shadow by
   an explicit closed-exchange or counterterm branch before claiming a
   full non-scalar Costello graph/QME theorem.
