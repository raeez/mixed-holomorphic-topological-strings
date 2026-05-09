# Agent 301 - Theta3 Costello Counterterm Source Theorem Search

Date: 2026-04-30.
Status: report-only. No TeX, script, figure, bibliography, PDF, or source
fixture was edited.

Owned reports:

- `reconstitution/theta3-costello-counterterm-source-theorem-search-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-301-theta3-costello-counterterm-source-theorem-search.md`

## Claim Attacked

The searched claim is that a Costello source theorem, perhaps after
restricting to the regular-density or wavefront-admissible Costello
habitat, implies the theta3 lower Bianchi counterterm
\[
  B^2_{02,20}\in\mathcal K^0_{\mathrm{ns},2}(I),
  \qquad
  d_{\mathrm{ns},2}B^2_{02,20}
  =
  -\mathfrak b^2_{02,20}.
\]

The desired column is
\[
  A_B^2=(0,0,-1)^T
\]
in the exposed lower basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}).
\]

## Verdict

No located Costello, Costello--Li, Costello--Gwilliam, or Hormander source
theorem implies \(dB=-b\) for this theta3 Bianchi defect.

The strongest source-backed statement is a criterion:

1. Costello supplies the finite-scale elliptic BV/RG/QME graph calculus,
   local counterterms for renormalized effective actions, and a local
   obstruction calculus.
2. Costello's obstruction step says a partial QME solution lifts exactly
   when the next closed obstruction is made exact by a local functional.
3. Costello--Li records the same grading convention: obstructions live in
   \(H^1\) of the local-functional obstruction complex, while possible
   lifts form an \(H^0\)-torsor after the obstruction vanishes.
4. The manuscript's restricted Costello habitat converts this into the
   finite-window equation \(A^M c=-r^M\) plus a Roos compatibility class.

Thus the source theorem gives the correct habitat and exactness test. It
does not prove that the specific Hom-valued theta3 Bianchi defect is exact.

## Source Floor

Primary source anchors checked:

- Costello, arXiv `0706.1533`, official page
  `https://arxiv.org/abs/0706.1533`.
- Costello--Li, arXiv `1201.4501`, official page
  `https://arxiv.org/abs/1201.4501`.
- Costello--Li, arXiv `1505.06703`, official page
  `https://arxiv.org/abs/1505.06703`.

Local line anchors:

- Heat-kernel propagator:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:77-90`.
- Local functionals as polydifferential densities:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1122-1151`.
- Counterterm theorem and renormalized effective action:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1746-1807`.
- RG/locality converse:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1967-2001`.
- QME/RG compatibility and renormalized QME:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2121-2190`.
- Local obstruction and lift criterion:
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2376-2420`,
  `:2469-2483`, `:2554-2581`, `:2915-2938`, `:2975-3014`.
- Costello--Li \(H^1/H^0\) obstruction convention:
  `references/primary-sources/costello-li-quantum-bcov-1201.4501.txt:2493-2505`.
- Costello--Li open-closed lifting statement:
  `references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt:2394-2412`.

The negative source boundary is stable:

- `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:156-240`
  records no automatic current-valued target, no arbitrary
  \(\mathcal D'_c(I)\) wavefront theorem, and no automatic bulk-to-defect
  kernel.
- `references/primary-sources/local-costello-bv-kernel-source-anchors-2026-04-30.md`
  records the same boundary for the local mixed HT source surface.
- `references/primary-sources/hormander-wavefront-source-anchors-2026-04-30.md`
  supports microlocal operation criteria only, not Costello counterterm
  exactness, scalar-contact projection, Roos compatibility, or brane-defect
  QME cancellation.

## Local Habitat Checked

The current restricted Costello habitat is the finite-window
local-functional package with labels in either
\[
  \bigl(\mathcal D^{\mathrm{reg}}_c(I)\bigr)^{r_\Gamma}
  \quad\text{or}\quad
  \mathcal D'_{c,\mathrm{WF}}(I;\Gamma,M).
\]
It includes the completed complex
\[
  \mathfrak Q^\bullet_{\mathcal G,M}(I)
  =
  \left(
  \mathcal O^{\mathrm{bd}}_{\mathrm{loc},\mathcal G,M}
  (\mathcal E_w^M|_I;A^{\mathrm{pp},w,M}_{\partial,\hbar}(I)),
  d_M
  \right),
  \qquad
  d_M=Q+\{I^w_{0,M},-\}_{\hbar,M},
\]
the Hom kernel differential
\[
  d_{\mathbf K,M}T=d_MT-(-1)^{|T|}T\,d_{\mathrm{CE}},
\]
and a chain scalar projection
\[
  \widehat\sigma_{\mathrm{sc},M}
  \colon
  \mathfrak Q^\bullet_{\mathcal G,M}(I)
  \to
  C^\bullet_{\mathrm{Lie}}(\bar A;\mathbb C\gamma_{\mathbf 1})[1][[\hbar]].
\]

Local anchors:

- `appendix-factorization-current-conventions.tex:1390-1485`:
  regular-density and wavefront-admissible labels.
- `appendix-factorization-current-conventions.tex:1485-1668`:
  wavefront-admissible graph kernel layer.
- `appendix-factorization-current-conventions.tex:1710-1915`:
  current-compatible \(\mathcal D'_c\) theorem surface and arbitrary-current
  obstruction.
- `appendix-unreduced-bv-qme.tex:2142-2385`: native finite-window
  realization habitat and constructive non-scalar Costello/QME criterion.
- `tate-P1-hadamard-mittag-leffler.tex:379-705`: finite-window graph/QME
  package and finite-window-to-limit obstruction.
- `tate-T1-weighted-completion.tex:1172-1327`: non-scalar QME tower and
  Milnor/Roos counterterm criterion.

This habitat is strong enough to state \(dB=-b\) as a theorem-grade
obligation. It is not strong enough to infer it from Costello's general
counterterm theorem.

## First-Principles Check

The lower source-coordinate primitive is
\[
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},
  \qquad
  D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2),
\]
with source differential
\[
  d_{\mathrm{CE}}\zeta^0_2
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]

Local-functionally,
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
  +\mathfrak b^2_{02,20}.
\]
Thus in the Bianchi-exposed lower basis the only current column is
\[
  A_D^2=(-2,2,1)^T,
  \qquad
  r_2=(2,-2,0)^T.
\]
The desired Bianchi counterterm target is
\[
  -\mathfrak b^2_{02,20}=(0,0,-1)^T.
\]
The cokernel
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*
\]
satisfies
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}r_2=1,\qquad
  \widetilde\lambda_{02,\mathfrak b}(0,0,-1)^T=-1.
\]

Therefore \(-\mathfrak b^2_{02,20}\) is not in the image of the current
finite-row differential. This is not a source-citation gap. It is the
current finite-row \(H^1\) obstruction.

If a new column
\[
  A_B^2=(0,0,-1)^T
\]
is adjoined, then
\[
  A_D^2+A_B^2=(-2,2,0)^T=-r_2,
\]
so \(D^2_{02,20}+B^2_{02,20}\) kills the lower residual. In the minimal
free two-column lower presentation the kernel of \((A_D^2,A_B^2)\) is
zero, so no secondary \(H^0\) class remains at \(N=2\). This is a formal
acceptance calculation, not a Costello local-functional construction.

## Why The Source Theorem Does Not Close The Row

Costello's counterterm theorem constructs local counterterms that remove
short-distance divergences for a chosen local action and renormalization
scheme. It does not assert that every closed QME obstruction cocycle is a
boundary.

Costello's obstruction lemma gives the missing equation directly: after a
partial QME solution, lifting to the next order amounts to finding a local
functional \(S'\) whose differential is the negative obstruction. In the
theta3 notation, \(S'\) is exactly the missing \(B^2_{02,20}\) or its tower
analogue. The source theorem therefore identifies the problem; it does not
solve it.

Costello--Li reinforces this boundary. Obstructions live in \(H^1\), and
possible lifts are controlled by \(H^0\) only after the obstruction
vanishes. Thus a source-backed proof of \(dB=-b\) must compute the
\(H^1\)-class of \(\mathfrak b^2_{02,20}\) as zero in the chosen restricted
Costello complex. No cited source supplies that computation.

Hormander wavefront calculus supplies pullback, product, pushforward, and
finite-scaling operation criteria. It can make a proposed distributional
counterterm meaningful. It cannot decide that the theta3 Bianchi defect is
a \(d_M\)-boundary.

Costello--Gwilliam local mirrors supply factorization-algebra vocabulary
and Noether/factorization-envelope metadata only in this checkout. They do
not supply the theta3 local-functional counterterm or its transport.

## Exact Missing Analytic Statement

The missing theorem is the following.

**Theta3 Bianchi-defect counterterm theorem in the restricted Costello
habitat.** Fix the finite-window marked Costello graph package containing
the \(\Theta_3\) source-face row and its lower
\(\nu_{02},\nu_{20}\) Bianchi-exposed presentation. Restrict external
cotangent-current labels to regular compactly supported densities or to
graphwise wavefront-admissible finite-scaling labels. Then for every
window \(M\ge2\) there are degree-zero local functionals
\[
  B^M_{02,20}\in\mathcal K^0_{\mathrm{ns},M}(I)
\]
such that:

1. \(B^M_{02,20}\) is an allowed Costello local counterterm supported on
   the relevant graph collision/source-face strata. In local normal
   coordinates it is represented by a finite sum
   \[
     \sum_{\Delta,\alpha,|\beta|\le N_{\Delta,\alpha}}
     \partial_\nu^\beta\delta_\Delta\otimes
     S^M_{\Delta,\alpha,\beta},
   \]
   with \(S^M_{\Delta,\alpha,\beta}\) supported in
   \(\Delta\cap\operatorname{supp}(B_\Gamma)\), satisfying the declared
   wavefront bound and finite scaling-degree condition.
2. It is scalar-zero:
   \[
     \widehat\sigma_{\mathrm{sc},M}(B^M_{02,20})=0.
   \]
3. Its differential is the Bianchi row:
   \[
     d_{\mathrm{ns},M}B^M_{02,20}
     =
     -\mathfrak b^M_{02,20},
   \]
   and at \(N=2\) its boundary column is exactly
   \(A_B^2=(0,0,-1)^T\).
4. The Bianchi rows transport compatibly. Equivalently the first transport
   defect
   \[
     \Delta^1_{M,N}
     =
     -\pi_{M,N}\mathfrak b^M+\mathfrak b^N
   \]
   is exact in \(\mathcal K^\bullet_{\mathrm{ns},N}(I)\), and after a
   chosen correction \(H^{M,N}\) the degree-zero Roos class
   \[
     [\pi_{M,N}B^M-B^N-H^{M,N}]
     \in
     H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I))
   \]
   vanishes in \(\varprojlim^1H^0\). The strict special case is
   \(\pi_{M,N}\mathfrak b^M=\mathfrak b^N\) and
   \(\pi_{M,N}B^M=B^N\).
5. The same choices are compatible with interval extension and admissible
   weight transport \(R^M_{w,w'}\).

This is the exact analytic statement that would imply \(dB=-b\). It is not
present in Costello's general theorem, in Costello--Li, in the
Costello--Gwilliam metadata mirrors, or in the current finite-row data.

## Claim Status

Blocked.

Allowed:

- Costello supplies the source-backed BV/RG/QME local-functional calculus
  and obstruction-exactness criterion.
- In the restricted habitat, \(dB=-b\) is the correct theorem target.
- The current finite-row habitat has no \(B^2_{02,20}\).
- The fixed-window obstruction is the cokernel functional
  \(\widetilde\lambda_{02,\mathfrak b}\).
- A formal column \(A_B^2=(0,0,-1)^T\), if constructed by genuine
  Costello local-functional data, would kill the lower residual.

Forbidden without new data:

- Costello's counterterm theorem proves \(d_{\mathrm{ns},2}B^2_{02,20}
  =-\mathfrak b^2_{02,20}\).
- The formal \(A_B^2\) column is a Costello local functional.
- The Bianchi rows transport strictly.
- The Roos class is formed or zero in the current data.
- The validator's supplied-exact payload is current mathematics rather
  than an interface fixture.

## Verification

Read:

- `CLAUDE.md`
- `AGENTS.md`
- `/Users/raeez/ecosystem/INVARIANTS.md`
- `/Users/raeez/ecosystem/AGENTS-HARNESS.md`
- `.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `main.tex:8360-8950`
- `theorem-lanes.tex:3280-3525`
- `open-obligations.tex:715-940`
- `claim-strength-ledger.tex:455-520`, `:835-930`
- `commands.tex`, `mathmacros.tex`, `notation.tex`, `preamble.tex`
- `reconstitution/costello-local-functional-habitat-construction-push-2026-04-30.md`
- theta3 Agent 287, 294, and 299 reports
- Costello source fixtures and local primary mirrors listed above
- `appendix-factorization-current-conventions.tex:1390-1915`
- `appendix-unreduced-bv-qme.tex:2140-2390`
- `tate-P1-hadamard-mittag-leffler.tex:379-705`
- `tate-T1-weighted-completion.tex:1170-1335`
- `scripts/finite_window_graph_array.py:960-2055`

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
python3 - <<'PY'
# focused A_D/A_B/cokernel check
PY
rg -n -F "B^2_{02,20}" ...
rg -n -F "mathfrak b^2_{02,20}" ...
```

Decisive output:

```text
theta_3_current_finite_row_subcomplex False 1 []
theta3_counterterm_without_differential_entry False 0 ['differential entry dC=-E']
theta3_counterterm_supplied_exact_payload True -1 []
eight_face False 0 [['E_nu02', '2'], ['E_nu20', '-2']]
ell_A_D 0
ell_r 1
ell_A_B -1
D_plus_B [-2, 2, 0]
minus_r [-2, 2, 0]
kernel_A_DB [(0, 0)]
```

No build was run because this was report-only and no TeX was edited.

## Files Changed

- `reconstitution/theta3-costello-counterterm-source-theorem-search-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-301-theta3-costello-counterterm-source-theorem-search.md`
