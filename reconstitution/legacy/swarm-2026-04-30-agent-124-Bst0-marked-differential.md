# Agent 124 - Marked \(\mathcal B_{\operatorname{st}=0}\) Differential

Status: patched owned surfaces; no commits or pushes.

## Stable Core

The current manuscript does not contain an actual signed marked
Costello graph/counterterm differential beyond the unmarked
\(Q+\{I_0,-\}\) generator calculation and the identity-loop balanced
graph/counterterm subhabitat.  Thus the theorem-grade computation
available now is:
\[
  \mathcal B_{\operatorname{st}=0}=0
\]
on the displayed unmarked Hamiltonian generator set and on the balanced
identity-loop graph/counterterm subhabitat.

For a larger marked specialization the missing datum is exact.  One must
supply
\[
  d_{\mathrm{QME}}X_{\Gamma,M}
    =
  \sum_{\Gamma',\lambda}
    \varepsilon_{\Gamma,\Gamma',\lambda}
    X_{\Gamma'^{\,\mathfrak m_{\Gamma,\Gamma',\lambda}},M}
    \quad \bmod F^{p-r+1},
\]
with signs and even invariant marker tensors
\[
  \mathfrak m_{\Gamma,\Gamma',\lambda}
    \in
  (\operatorname{End}(V)^{\otimes m_\lambda})^{\lie{gl}(V)}.
\]
For
\[
  \mathfrak m=\sum_\alpha T_{\alpha,1}\otimes\cdots\otimes T_{\alpha,m},
\]
the scalar shadow is controlled by
\[
  \operatorname{Str}_{\mathrm{cyc}}(\mathfrak m)
    =
  \sum_\alpha \operatorname{Str}(T_{\alpha,1}\cdots T_{\alpha,m}).
\]
The first scalar CE shadow is
\[
  \hbar
  \sum_{\Gamma',\lambda}
    \varepsilon_{\Gamma,\Gamma',\lambda}
    \operatorname{Str}_{\mathrm{cyc}}
      (\mathfrak m_{\Gamma,\Gamma',\lambda})
    \omega(f_{\Gamma'},g_{\Gamma'})\gamma_{\mathbf 1},
\]
and in cohomology it is the same coefficient times
\([\bar c]\gamma_{\mathbf 1}\).

Full \(\lie{gl}(N|N)\)-equivariance excludes a single fixed noncentral
marker.  Such a marker must commute with all of \(\lie{gl}(V)\), hence is
\(\lambda\operatorname{id}_V\), and its cyclic supertrace is
\(\lambda\operatorname{sdim}(V)=0\).  The \(P_+\) test remains the first
nonzero scalar shadow for a non-equivariant or externally marked
enlargement, not for the full super-gauge-equivariant Costello
differential.

## Attack Ledger

```yaml
- id: A1-124-01
  severity: 1
  status: healed
  lens: missing actual differential
  target: appendix-unreduced-bv-qme.tex, supertraceless-monodromy obstruction
  claim: Agent 119's formal \(\mathcal B_{\operatorname{st}=0}\) formula can be numerically evaluated for the actual marked Costello differential in this checkout.
  broken_step: The repo supplies no signed marked graph/counterterm boundary expansion with marker tensors; it only supplies \(Q+\{I_0,-\}\), identity-loop preservation, and formal \(\sum \varepsilon X_{\Gamma'}\) placeholders.
  evidence_type: missing_source
  evidence_ref: "appendix-unreduced-bv-qme.tex:1271-1326 before this pass; main.tex:7364-7573; references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md"
  files_read:
    - appendix-unreduced-bv-qme.tex
    - main.tex
    - reconstitution/swarm-2026-04-30-agent-110-balanced-graph-extension.md
    - reconstitution/swarm-2026-04-30-agent-115-first-nonidentity-loop-symbol.md
    - reconstitution/swarm-2026-04-30-agent-119-supertraceless-monodromy-subhabitat.md
    - references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md
  tools_used: [sed, nl, rg]
  confidence: high
  blast_radius: A claimed scalar value for a nonexistent marked differential would be invented mathematics.
  minimal_heal: State the exact marked boundary datum required and the scalar-shadow formula once it is supplied.
  residual: Supply the actual marked graph/counterterm list, signs, orientations, and invariant marker tensors.
  deciding_evidence: A committed marked Costello specialization with its \(d_{\mathrm{QME}}\)-boundary table.

- id: A1-124-02
  severity: 1
  status: healed
  lens: gauge equivariance
  target: noncentral marker \(P_+\)
  claim: The first nonzero \(P_+\) marked-loop shadow can occur in the full \(\lie{gl}(N|N)\)-equivariant Costello differential.
  broken_step: A single fixed marker in an equivariant differential must be invariant under conjugation by the full super-gauge algebra; the commutant of the defining \(\lie{gl}(N|N)\)-module is the scalar identity.
  evidence_type: proof
  evidence_ref: "appendix-unreduced-bv-qme.tex:1461-1505 after this pass; Costello-Li invariant-function grammar at references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt:1140-1207"
  files_read:
    - appendix-unreduced-bv-qme.tex
    - references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt
  tools_used: [nl, rg]
  confidence: high
  blast_radius: Would admit a non-gauge-invariant idempotent as if it were Costello open-sector data.
  minimal_heal: Prove single-marker centrality under full \(\lie{gl}(V)\)-equivariance and compute the zero scalar shadow of \(\lambda\operatorname{id}_V\).
  residual: If only the even block-diagonal group is imposed, or if external marker tensors are supplied, the invariant tensor family must be declared explicitly.
  deciding_evidence: The chosen gauge-equivariance class for the marked specialization.

- id: A1-124-03
  severity: 2
  status: healed
  lens: invariant tensor alternative
  target: marker tensors beyond one fixed endomorphism
  claim: Gauge equivariance alone means no marked obstruction formula is needed.
  broken_step: Full equivariance excludes single noncentral fixed markers, but higher invariant tensors may still be supplied as external marked data; their scalar shadow is the cyclic supertrace contraction.
  evidence_type: proof
  evidence_ref: "appendix-unreduced-bv-qme.tex:1402-1445 after this pass"
  files_read:
    - appendix-unreduced-bv-qme.tex
    - reconstitution/swarm-2026-04-30-agent-115-first-nonidentity-loop-symbol.md
    - reconstitution/swarm-2026-04-30-agent-119-supertraceless-monodromy-subhabitat.md
  tools_used: [nl, sed]
  confidence: high
  blast_radius: Would falsely close the marked obstruction branch without accounting for invariant marker tensors.
  minimal_heal: Define \((\operatorname{End}(V)^{\otimes m})^{\lie{gl}(V)}\) as the marker habitat and compute the scalar shadow by \(\operatorname{Str}_{\mathrm{cyc}}\).
  residual: Compute \(\operatorname{Str}_{\mathrm{cyc}}\) for the actual invariant tensors once supplied.
  deciding_evidence: The invariant marker tensor list in the marked graph/counterterm differential.
```

## Repairs Made

Added
`prop:app-marked-bst0-equivariant-differential` to
`appendix-unreduced-bv-qme.tex`.  It:

- states the exact marked \(d_{\mathrm{QME}}\)-boundary datum needed to
  compute \(\mathcal B_{\operatorname{st}=0}\);
- gives the obstruction family and scalar CE shadow for invariant marker
  tensors;
- proves full \(\lie{gl}(N|N)\)-equivariance forces a single fixed marker
  to be scalar;
- records that the actual displayed unmarked/identity-loop surface has
  \(\mathcal B_{\operatorname{st}=0}=0\);
- fences all larger marked Costello specializations behind the missing
  signed boundary and invariant-marker tensor data.

## Verification

```bash
rg -n -F "prop:app-marked-bst0-equivariant-differential" appendix-unreduced-bv-qme.tex
rg -n -F "eq:app-marked-differential-datum" appendix-unreduced-bv-qme.tex
git diff --check -- appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-124-Bst0-marked-differential.md
chktex -q appendix-unreduced-bv-qme.tex
```

The `rg` checks found the new proposition and marked-differential datum.
`git diff --check` passed.  `chktex` returned the existing appendix-style
warnings, plus warnings on the new displayed invariant-tensor lines; it
reported no fatal TeX error.  No full `make pdf` was run because the
shared checkout already has concurrent tracked edits and the build writes
the tracked PDF outside this agent's writable surface.

## Residual Theorem Obligations

1. Supply the actual marked Hamiltonian Costello graph/counterterm
   differential: graph list, orientations, signs, filtration order, and
   counterterm boundary terms.
2. Declare the gauge-equivariance class.  Full \(\lie{gl}(N|N)\)
   equivariance kills single noncentral markers; a weaker even subgroup
   or external marker sector must be stated explicitly.
3. If external invariant marker tensors are admitted, compute
   \(\operatorname{Str}_{\mathrm{cyc}}\) for each tensor and test whether
   the resulting scalar shadow is zero in the \([\bar c]\) line.
4. If a nonzero scalar shadow survives, kill it by a specified
   closed-exchange or counterterm branch before any full non-scalar
   Costello graph/QME theorem is asserted.
