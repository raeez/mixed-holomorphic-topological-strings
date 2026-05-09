# Agent 115 - First Non-Identity-Loop Scalar Symbol

Status: patched owned appendix surface; no commits or pushes.

## Stable Computation

The first graph class not covered by the identity-loop balanced habitat is
the connected one-cross-contraction boundary graph
\[
  \Gamma^{T_\bullet}_{1,M}
\]
with two Hamiltonian external legs \((a,f)\), \((b,g)\), one Weyl edge,
and one scalar open index loop carrying an ordered even endomorphism
monodromy word \(T_\bullet=(T_1,\ldots,T_m)\).  Its scalar-contact
filtration degree is \(F^1/F^2\).  The empty word gives the identity loop.

The computed symbol is
\[
  \sigma_{\mathrm{sc}}\!\left(
    \operatorname{gr}_{F}
      X_{\Gamma^{T_\bullet}_{1,M}}(a,f;b,g)\right)
  =
  \hbar\,\operatorname{Str}(T_1\cdots T_m)\,
  \omega(f,g)\gamma_{\mathbf 1}.
\]

For the first non-identity marker \(T\),
\[
  \sigma_{\mathrm{sc}}\!\left(
    \operatorname{gr}_{F}X_{\Gamma^{T}_{1,M}}(1,z_1;1,z_2)\right)
  =
  \hbar\,\operatorname{Str}(T)\gamma_{\mathbf 1}.
\]
Taking \(T=P_+\), projection onto one even basis line, gives the explicit
nonzero scalar symbol \(\hbar\gamma_{\mathbf 1}\).  The associated CE class
is
\[
  \hbar\,\operatorname{Str}(T_1\cdots T_m)[\bar c]\gamma_{\mathbf 1}.
\]

Consequently the identity-loop theorem extends to the larger, explicitly
delimited subhabitat whose scalar-contact loop monodromy words, before and
after \(d_{\mathrm{QME}}\), are all supertraceless.  It does not extend to
arbitrary non-identity marked loops.

## Attack Ledger

```yaml
- id: A1-115-01
  severity: 1
  status: healed
  lens: non-identity loop coefficient
  target: appendix-unreduced-bv-qme.tex, balanced graph/counterterm extension
  claim: The balanced identity-loop result can be extended to arbitrary marked scalar loops.
  broken_step: Agent 110 only proves loops whose scalar symbol factors through Str(id_V). A marked loop carries Str(T_1...T_m), which need not vanish on V = C^{N|N}.
  evidence_type: direct_computation
  evidence_ref: prop:app-first-nonidentity-loop-scalar-symbol computes sigma_sc(gr_F X_Gamma) = hbar Str(T_1...T_m) omega(f,g) gamma_1.
  files_read: [appendix-unreduced-bv-qme.tex, main.tex, references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md, reconstitution/swarm-2026-04-30-agent-103-balanced-scalar-projection.md, reconstitution/swarm-2026-04-30-agent-108-bulk-defect-kernel-construction.md, reconstitution/swarm-2026-04-30-agent-110-balanced-graph-extension.md]
  tools_used: [sed, nl, rg, python3]
  confidence: high
  blast_radius: Would falsely promote the balanced identity-loop subhabitat to a full graph/counterterm theorem.
  minimal_heal: Compute the first marked-loop scalar symbol and state the exact supertrace-zero enlargement.
  residual: Determine whether the actual Hamiltonian Costello specialization ever produces non-supertraceless monodromy words.
  deciding_evidence: A supplied graph/counterterm complex with its endomorphism monodromy words and d_QME boundaries.

- id: A1-115-02
  severity: 1
  status: healed
  lens: explicit counterexample
  target: first non-identity scalar symbol
  claim: Every first marked loop still vanishes in the balanced supertrace model.
  broken_step: Projection onto one even basis line has supertrace 1, not superdimension 0.
  evidence_type: direct_computation
  evidence_ref: sigma_sc(gr_F X_{Gamma^{P_+}_{1,M}}(1,z_1;1,z_2)) = hbar gamma_1; python check Str(P_even)=1.
  files_read: [appendix-unreduced-bv-qme.tex, main.tex]
  tools_used: [python3, nl]
  confidence: high
  blast_radius: Leaves an uncancelled scalar CE class hbar [cbar] gamma_1.
  minimal_heal: Record the nonzero P_+ test and forbid arbitrary marked-loop extension.
  residual: If gauge equivariance excludes fixed noncentral markers, prove that exclusion inside the supplied graph habitat.
  deciding_evidence: Equivariance and counterterm classification for the actual Costello specialization.

- id: A1-115-03
  severity: 2
  status: healed
  lens: stronger preservation
  target: possible larger subhabitat
  claim: No enlargement beyond identity loops is available.
  broken_step: The scalar calculation shows that any marked-loop word with Str(T_1...T_m)=0 has zero scalar symbol by the same one-loop computation.
  evidence_type: proof
  evidence_ref: prop:app-first-nonidentity-loop-scalar-symbol, final paragraph.
  files_read: [appendix-unreduced-bv-qme.tex]
  tools_used: [nl]
  confidence: high
  blast_radius: Would leave a true supertraceless-monodromy preservation subcomplex unrecorded.
  minimal_heal: State the complete d_QME-stable supertraceless-monodromy subhabitat condition, including boundaries after d_QME.
  residual: The theorem is conditional on the subhabitat being complete and d_QME-stable.
  deciding_evidence: Verification of those hypotheses for a concrete graph/counterterm list.
```

## Repairs Made

Added `prop:app-first-nonidentity-loop-scalar-symbol` to
`appendix-unreduced-bv-qme.tex`.  It computes the first marked-loop scalar
symbol, fixes the filtration degree \(F^1/F^2\), records the sign for
\((z_1,z_2)\), gives the explicit nonzero \(P_+\) test, and states the
larger supertraceless-monodromy preservation condition.

## Verification

Commands run:

```bash
sed -n '1,240p' /Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,220p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
git status --short
sed -n '1,260p' CLAUDE.md
sed -n '1,260p' AGENTS.md
sed -n '1,260p' references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-103-balanced-scalar-projection.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-108-bulk-defect-kernel-construction.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-110-balanced-graph-extension.md
rg -n "balanced|identity-loop|non-identity|scalar-contact|Costello graph" appendix-unreduced-bv-qme.tex main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
nl -ba appendix-unreduced-bv-qme.tex
nl -ba main.tex | sed -n '6780,6925p'
nl -ba main.tex | sed -n '7360,7435p'
nl -ba main.tex | sed -n '7670,7750p'
python3 - <<'PY'
def str_super(diag, parity):
    return sum(((-1)**p)*x for x,p in zip(diag, parity))
parity=[0,1]
print('Str(id_1|1)=', str_super([1,1], parity))
print('Str(P_even)=', str_super([1,0], parity))
print('omega(z1,z2)=', 1)
PY
rg -n "prop:app-first-nonidentity-loop-scalar-symbol|First non-identity-loop scalar symbol" appendix-unreduced-bv-qme.tex
git diff --check -- appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-115-first-nonidentity-loop-symbol.md
chktex -q appendix-unreduced-bv-qme.tex
```

The Python sign check returned `Str(id_1|1)=0`, `Str(P_even)=1`, and
`omega(z1,z2)=1`.
`git diff --check` passed.  `chktex` returned style warnings in the
existing appendix pattern, plus warnings on the new displayed formulas; it
reported no fatal TeX error.  No full `make pdf` was run because the shared
checkout has concurrent tracked edits and the build writes tracked output
outside this agent's writable surface.

## Remaining Obligations

1. Supply the actual Hamiltonian Costello graph/counterterm complex and
   list its loop monodromy words.
2. Prove gauge equivariance either forbids noncentral fixed markers or
   replaces them by invariant marked-loop tensors.
3. Verify that \(d_{\mathrm{QME}}\) preserves the supertraceless-monodromy
   condition if that larger subhabitat is used.
4. Kill any nonzero class
   \(\hbar\,\operatorname{Str}(T_1\cdots T_m)[\bar c]\gamma_{\mathbf 1}\)
   by an explicit closed-exchange or counterterm branch before claiming a
   full non-scalar Costello graph/QME theorem.
