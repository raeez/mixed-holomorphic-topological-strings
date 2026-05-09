# Theta3 Restricted Counterterm Theorem Frontier

Date: 2026-04-30.
Status: report-only. No manuscript TeX, script, figure, bibliography, PDF, or
source fixture was edited.

## Decision

The controlled enlargement was attacked. It was not constructed from the
current checkout data.

The strongest true statement is an obstruction theorem with an exact positive
target. In the present Bianchi-exposed restricted habitat there is no
scalar-zero local functional \(B^2_{02,20}\) with
\[
  d_{\mathrm{ns},2}B^2_{02,20}
  =
  -\mathfrak b^2_{02,20}.
\]
The fixed-window obstruction is the cokernel functional
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*.
\]
The all-window obstruction, if a \(B^M\)-candidate is later supplied, is the
two-step class
\[
  \Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N
  \in Z^1(\mathcal K^\bullet_{\theta_3,N}),
\]
followed by the secondary primitive-transport class
\[
  \bigl[\pi_{M,N}B^M-B^N-H^{M,N}\bigr]
  \in
  \varprojlim\nolimits^1_M
  H^0(\mathcal K^\bullet_{\theta_3,M}).
\]

Thus the restricted-habitat theorem is not a demotion. It is a precise
frontier: construct the missing Costello local-functional column and transport
tower, or retain the displayed cokernel and Roos obstruction classes.

## Context Read

Governing files read:

- `CLAUDE.md`
- `AGENTS.md`
- `/Users/raeez/ecosystem/INVARIANTS.md`
- `/Users/raeez/ecosystem/AGENTS-HARNESS.md`
- `.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`

Manuscript/control anchors read:

- `main.tex:8640-8925`, `main.tex:9220-9345`
- `theorem-lanes.tex:2670-2848`, `theorem-lanes.tex:2990-3040`,
  `theorem-lanes.tex:3310-3694`
- `open-obligations.tex:590-930`
- `claim-strength-ledger.tex:480-560`, `claim-strength-ledger.tex:910-965`
- `commands.tex`, `mathmacros.tex`, `notation.tex`, `preamble.tex`
- `appendix-factorization-current-conventions.tex:1390-1705`
- `appendix-unreduced-bv-qme.tex:2142-2385`
- `tate-T1-weighted-completion.tex:1172-1327`

Reports read:

- Agent 294: `reconstitution/swarm-2026-04-30-agent-294-theta3-actual-local-functional-b-column-construction-push.md`
- Agent 299: `reconstitution/swarm-2026-04-30-agent-299-theta3-roos-transport-obstruction-push.md`
- Agent 301: `reconstitution/swarm-2026-04-30-agent-301-theta3-costello-counterterm-source-theorem-search.md`
- Agent 304: `reconstitution/swarm-2026-04-30-agent-304-theta3-h1-bianchi-transport-class-construction.md`
- Agent 309: `reconstitution/swarm-2026-04-30-agent-309-theta3-delta1-transport-integration-audit.md`
- Agent 308: no `agent-308` report was present under `reconstitution/` by
  `rg --files reconstitution | rg 'agent-308|308-'`.

Additional theta3 frontier reports read:

- `reconstitution/theta3-no-counterterm-controlled-enlargement-integration-spec-2026-04-30.md`
- `reconstitution/theta3-controlled-enlargement-witness-search-2026-04-30.md`
- `reconstitution/theta3-actual-local-functional-b-column-construction-push-2026-04-30.md`
- `reconstitution/theta3-h1-bianchi-transport-class-construction-2026-04-30.md`
- `reconstitution/theta3-delta1-transport-integration-audit-2026-04-30.md`

## Fixed-Window Calculation

Let
\[
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},
  \qquad
  D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2).
\]
The source differential is
\[
  d_{\mathrm{CE}}\zeta^0_2
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]
The Hom-valued Bianchi defect is
\[
  \mathfrak b^2_{02,20}
  =
  d_{\mathrm{ns},2}K^2_{\Theta_3}(\zeta^0_2)
  -
  K^2_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_2).
\]
Therefore
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
  +\mathfrak b^2_{02,20}.
\]

In the ordered lower basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})
\]
the current column and residual are
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T.
\]
The desired \(B\)-counterterm target is
\[
  A_B^2=(0,0,-1)^T
  =
  -\mathfrak b^2_{02,20}.
\]

The present degree-zero habitat is only
\[
  \mathcal H^0_{\mathrm{cur}}=\mathbb C D^2_{02,20},
\]
and the degree-one exposed habitat is
\[
  \mathcal H^1_{\mathrm{cur}}
  =
  \mathbb C E^2_{\nu_{02}}
  \oplus
  \mathbb C E^2_{\nu_{20}}
  \oplus
  \mathbb C\mathfrak b^2_{02,20}.
\]
The image is the line spanned by \(A_D^2\). The cokernel satisfies
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}(r_2)=1,\qquad
  \widetilde\lambda_{02,\mathfrak b}A_B^2=-1.
\]
Hence \(A_B^2\notin\operatorname{im}(d_{\mathrm{ns},2})\) in the current
restricted finite-row habitat.

Equivalently, a scalar \(xD^2_{02,20}\) would need
\[
  x(-2,2,1)^T=(0,0,-1)^T.
\]
The first two coordinates force \(x=0\). The Bianchi coordinate forces
\(x=-1\). This is the exact fixed-window obstruction.

## Formal Enlargement Target

If a genuine scalar-zero local functional \(B^2_{02,20}\) is adjoined, the
formal lower boundary matrix becomes
\[
  A^2_{D,B}
  =
  \begin{pmatrix}
    -2&0\\
     2&0\\
     1&-1
  \end{pmatrix}.
\]
Then
\[
  d_{\mathrm{ns},2}(D^2_{02,20}+B^2_{02,20})
  =
  (-2,2,0)^T
  =
  -r_2,
\]
and the minimal free two-column lower presentation has \(\ker A^2_{D,B}=0\).

This is only an acceptance calculation. It becomes a theorem exactly after
one supplies:
\[
  B^M_{02,20}\in\mathcal K^0_{\mathrm{ns},M}(I),
  \qquad
  \widehat\sigma_{\mathrm{sc},M}(B^M_{02,20})=0,
\]
\[
  d_{\mathrm{ns},M}B^M_{02,20}
  =
  -\mathfrak b^M_{02,20},
\]
and regular-density or wavefront-admissible locality. In the wavefront
branch, the local counterterm must be represented by a finite sum of the
form
\[
  \sum_{\Delta,\alpha,|\beta|\le N_{\Delta,\alpha}}
  \partial_\nu^\beta\delta_\Delta\otimes S^M_{\Delta,\alpha,\beta},
\]
with support on the relevant collision/source-face stratum and with the
declared wavefront and finite-scaling bounds. The current regular-density
and wavefront layers provide habitats and operation criteria; they do not
construct this specific \(B\)-column.

## Tower Obstruction

For \(M\geq N\), define the \(H^1\) Bianchi transport defect
\[
  \Delta^1_{M,N}
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N.
\]
If a genuine \(B\)-tower satisfies \(d_MB^M=-\mathfrak b^M\), then
\[
  d_N(\pi_{M,N}B^M-B^N)
  =
  \Delta^1_{M,N}.
\]
Thus the first tower gate is
\[
  [\Delta^1_{M,N}]=0
  \quad\text{in}\quad
  H^1(\mathcal K^\bullet_{\theta_3,N})
\]
for every transition, compatibly as a Roos \(1\)-cochain:
\[
  \operatorname{ob}^1_{\mathfrak b}
  =
  \bigl([\Delta^1_{M,N}]\bigr)_{M\geq N}
  \in
  C^1_{\mathrm{Roos}}
  \bigl(H^1(\mathcal K^\bullet_{\theta_3,\bullet})\bigr).
\]

If the \(H^1\) gate vanishes, choose
\[
  H^{M,N}\in\mathcal K^0_{\theta_3,N},
  \qquad
  d_NH^{M,N}=\Delta^1_{M,N}.
\]
Then
\[
  \Delta^0_{M,N}
  =
  \pi_{M,N}B^M-B^N-H^{M,N}
  \in Z^0(\mathcal K^\bullet_{\theta_3,N}),
\]
and the secondary obstruction is
\[
  \operatorname{ob}^0_B
  =
  [(\Delta^0_{M,N})]
  \in
  \varprojlim\nolimits^1_M
  H^0(\mathcal K^\bullet_{\theta_3,M}).
\]
It must vanish for a compatible counterterm tower.

The current checkout has neither \(B^2_{02,20}\) nor the Bianchi-row
transport matrices \(\pi_{M,N}\mathfrak b^M\). The diagonal source-face
transport for the eight-face candidate controls source rows, not Bianchi
rows, and leaves the \(N=2\) residual
\[
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}}.
\]
Replacing the missing Bianchi transition by that diagonal source-face
transport would be a false proof.

## Source-Theorem Attack

Costello's BV/RG/QME source theorems identify the correct obstruction
complex and the correct lift criterion: a closed obstruction in degree \(1\)
must be made exact by a local functional in degree \(0\), and lifts form an
\(H^0\)-torsor only after the \(H^1\)-class vanishes. They do not prove that
the specific theta3 Bianchi defect \(\mathfrak b^2_{02,20}\) is exact.

Costello--Li gives the same \(H^1/H^0\) obstruction convention. Hormander
wavefront calculus supplies operation criteria and admissible extension
habitats. It does not decide the fixed Bianchi row as a boundary.

Therefore the source-backed theorem target is:

\[
  \text{construct }B^M_{02,20}\text{ in the restricted Costello habitat,}
\]
not:
\[
  \text{cite Costello to infer }dB=-\mathfrak b.
\]

## Exact TeX Patch Targets

These are report-only patch targets. Do not apply without manuscript-edit
authorization.

1. `main.tex:8859-8867`.

Current surface already has the correct tower sign but does not name
\(\Delta^1_{M,N}\). Replace the unnamed paragraph beginning `In a tower this
requires' by:

```tex
In a tower define the Bianchi transport defect
\[
  \Delta^1_{M,N}
  :=
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N .
\]
For a proposed \(B\)-tower,
\[
  d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)
  =
  \Delta^1_{M,N}.
\]
Thus the first transport gate is
\[
  [\Delta^1_{M,N}]=0
  \quad\text{in}\quad
  H^1(\mathcal K^\bullet_{\theta_3,N}),
\]
compatibly in the Roos complex.  After choosing
\[
  H^{M,N}\in\mathcal K^0_{\theta_3,N},
  \qquad d_NH^{M,N}=\Delta^1_{M,N},
\]
the remaining primitive-transport obstruction is the class
\[
  [\pi_{M,N}B^M-B^N-H^{M,N}]
  \in
  \varprojlim\nolimits^1_M
  H^0(\mathcal K^\bullet_{\theta_3,M}).
\]
```

2. `theorem-lanes.tex:3538-3541`.

After the sentence ending with `otherwise the Bianchi row remains
obstructed', insert:

```tex
For a tower of such columns the named Bianchi transport defect is
\[
  \Delta^1_{M,N}
  :=
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N .
\]
It must vanish in \(H^1(\mathcal K^\bullet_{\theta_3,N})\), or be killed by
some \(H^{M,N}\) with \(d_NH^{M,N}=\Delta^1_{M,N}\).  After such a
correction, the secondary class
\[
  [\pi_{M,N}B^M-B^N-H^{M,N}]
  \in
  \varprojlim\nolimits^1_M
  H^0(\mathcal K^\bullet_{\theta_3,M})
\]
must vanish.
```

3. `open-obligations.tex:897-905`.

The current display there is the \(D\)-candidate sign. Keep it, but add the
\(B\)-counterterm sign immediately after it:

```tex
For the \(B\)-counterterm tower the sign is opposite.  Define
\[
  \Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N .
\]
Then
\[
  d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)=\Delta^1_{M,N}.
\]
The \(H^1\)-gate is the vanishing of \([\Delta^1_{M,N}]\); after a
correction \(H^{M,N}\), the secondary gate is
\[
  [\pi_{M,N}B^M-B^N-H^{M,N}]
  \in
  \varprojlim\nolimits^1_MH^0(\mathcal K^\bullet_{\theta_3,M}).
\]
```

4. `claim-strength-ledger.tex:950-954`.

Replace the schematic sentence `These witnesses must also satisfy the
finite-window Roos compatibility condition' by:

```tex
For a \(B\)-counterterm tower the first named transport class is
\[
  \Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N .
\]
It must vanish in \(H^1\), or be killed by \(H^{M,N}\) with
\(d_NH^{M,N}=\Delta^1_{M,N}\); after that, the secondary class
\[
  [\pi_{M,N}B^M-B^N-H^{M,N}]
  \in
  \varprojlim\nolimits^1_MH^0(\mathcal K^\bullet_{\theta_3,M})
\]
must vanish.
```

## Verification

Commands run:

```bash
rg -n "theta3|Theta_3|theta_3|B\^2_\{02,20\}|mathfrak b\^2|Delta\^1|lim\^1|secondary" main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex reconstitution -S
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
```

Script evidence:

- `theta_3_current_finite_row_subcomplex`: `primitive_exists=false`,
  residual \(E_{\theta_3}\), obstruction value \(1\).
- `theta3_counterterm_without_differential_entry`: rejected; missing
  `differential entry dC=-E`.
- `theta3_counterterm_supplied_exact_payload`: accepted only as an interface
  fixture with differential entry \(-1\), scalar zero, transport, and zero
  Roos class. It is not current mathematics.
- eight-face candidate: rejected; vector
  \((2,-2,3,2,-1,1,-2,-3)\), diagonal \(N=2\) transport
  \(2E^2_{\nu_{02}}-2E^2_{\nu_{20}}\), marked Costello incidence/weight
  table absent.

No PDF build was run. This was a report-only assignment and no TeX was
edited.
