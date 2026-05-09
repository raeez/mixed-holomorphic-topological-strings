# Agent 158 - Minimal Full-Equivariant Order-Three Test

Status: patched owned appendix surface; no commits or pushes.

## Stable Core

The finite graph-list axioms do not prove an absence theorem for arbitrary
order-three rows.  A larger finite-window package may supply genuine
\(|\Gamma|_\hbar=3\) graph rows, order-three CE-source rows, or bracket rows
between already supplied nonzero lower-order components.  Those data are not
recoverable from the order-two scalar-shadow computation.

For the minimal full-equivariant package, the stronger true statement is
all-order vanishing.  The package contains only the strict current-interface
rows, the one-cross scalar-contact row \(\alpha_{\mathrm{sc}}\), and its
subset-deletion closure.  Since
\[
  K^M_{\alpha_{\mathrm{sc}}}=0
\]
as a full-equivariant local functional on \(V=\mathbb C^{N|N}\), every
positive-order scalar-contact closure row is zero before cohomology.  Hence
for every \(n\geq1\)
\[
  R^{\mathrm{ns}}_{n,M}=0,\qquad
  \mathfrak o^{\mathrm{ns}}_{n,M}=0,\qquad
  C_{n,M}=0 .
\]
If zero rows are suppressed, the minimal positive-order row arrays are empty.
If labelled zero rows are retained, every such row has
\[
  R^{\mathrm{row}}_{\alpha,M}=0,\qquad S_{\alpha,M}=0,
\]
with zero truncation row.

## Order-Three Datum

Under the minimal hypotheses through order two,
\[
  C_{1,M}=C_{2,M}=0
\]
and no nonzero order-one or order-two row exists outside the scalar-contact
closure.  Therefore the bracket and lower-counterterm order-three sums are
empty.  The first possible nonzero order-three datum in a larger package is
one of:
\[
  R^{\mathrm{row}}_{d\Gamma,M}
    =
  \varepsilon_\Gamma\,d_M K^M_\Gamma,\qquad
  S_{d\Gamma,M}
    =
  \varepsilon_\Gamma\widehat\sigma_{\mathrm{sc},M}(d_M K^M_\Gamma),
\]
for a genuine \(|\Gamma|_\hbar=3\) graph, or
\[
  R^{\mathrm{row}}_{\mathrm{CE}(\Gamma,\nu),M}
    =
  -\varepsilon^{\mathrm{CE}}_{\Gamma,\nu}K^M_\Gamma(\zeta_{M,\nu}),
\]
\[
  S_{\mathrm{CE}(\Gamma,\nu),M}
    =
  -\varepsilon^{\mathrm{CE}}_{\Gamma,\nu}
  \widehat\sigma_{\mathrm{sc},M}
    \bigl(K^M_\Gamma(\zeta_{M,\nu})\bigr).
\]
In a nonminimal package, bracket rows with
\(|\Gamma_1|_\hbar+|\Gamma_2|_\hbar=3\) must also be supplied:
\[
  R^{\mathrm{row}}_{b(\Gamma_1,\Gamma_2),M}
    =
  \frac12\varepsilon_{\Gamma_1,\Gamma_2}
  \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar,M}.
\]

The scalar gate is
\[
  \mathfrak s_{3,M}
    =
  \sum_{\alpha\in\mathsf A^{\mathrm{fw}}_{3,M}}S_{\alpha,M}=0.
\]
Only after this gate is supplied and vanishes is the non-scalar class
\[
  \mathfrak o^{\mathrm{ns}}_{3,M}
    =
  [R^{\mathrm{ns}}_{3,M}]
  \in H^1(\mathcal K^\bullet_{\mathrm{ns},M}(I),d_{\mathrm{ns},M})
\]
defined.

## Valid Attacks

```yaml
- id: A1-158-01
  severity: 1
  status: healed
  lens: order-three absence theorem
  target: appendix-unreduced-bv-qme.tex, minimal full-equivariant rows after order two
  claim: The finite graph-list axioms alone imply order-three rows are empty.
  broken_step: The axioms allow a larger package to add genuine |Gamma|_hbar=3 graph rows, CE-source rows, and bracket rows involving supplied nonzero lower-order components.
  evidence_type: proof_gap
  evidence_ref: thm:actual-finite-window-nonscalar-decision-datum; defn:finite-window-graph-array
  confidence: high
  blast_radius: A false absence theorem would erase the first possible non-scalar finite-window obstruction.
  minimal_heal: Prove emptiness/zero only under the minimal no-added-row hypothesis and record the exact order-three row formula for larger packages.
  residual: Populate any actual larger package row by row.

- id: A1-158-02
  severity: 1
  status: healed
  lens: induction gap
  target: thm:app-minimal-full-equivariant-kernel-vanishing
  claim: The order-one and order-two computation automatically proves the pattern.
  broken_step: The old theorem stopped at codimension-two closure and did not state the all-order minimal hypothesis.
  evidence_type: proof_gap
  evidence_ref: thm:app-minimal-full-equivariant-all-order-vanishing
  confidence: high
  blast_radius: Order three remained undecided despite the zero local-functional mechanism.
  minimal_heal: Add the all-order theorem using K^M_{alpha_sc}=0, bilinearity, zero lower counterterms, and absence of genuine positive-order rows.
  residual: None inside the minimal package.

- id: A1-158-03
  severity: 2
  status: healed
  lens: scalar/non-scalar gate separation
  target: order-three larger-package residual
  claim: Full-equivariant scalar-shadow vanishing decides the order-three non-scalar class.
  broken_step: Scalar-gate vanishing only places the row sum in the kernel; the H^1 class and inverse-limit compatibility remain separate.
  evidence_type: proof_gap
  evidence_ref: def:app-nonscalar-kernel-row-complex; prop:app-first-order-three-larger-package-datum
  confidence: high
  blast_radius: A scalar-zero row could still be a nontrivial kernel class.
  minimal_heal: State the scalar gate, kernel cohomology class, fixed-window counterterm criterion, and Roos compatibility condition.
  residual: Compute H^1 and the Roos class after concrete row values exist.
```

## Files Changed/Staged

Changed:

- `appendix-unreduced-bv-qme.tex`
- `reconstitution/swarm-2026-04-30-agent-158-minimal-full-equivariant-order3-test.md`

Staged:

- none by this agent.

## Commands And Results

```bash
python3 scripts/finite_window_graph_array.py
python3 -m py_compile scripts/finite_window_graph_array.py
```

Reported \(\omega(z_1,z_2)=1\), \(\omega(z_1,z_1)=0\), full-equivariant
order-one scalar-contact value \(0\), minimal full-equivariant
\(R^{\mathrm{ns}}_{2,M}=0\), and \(C_{2,M}=0\).  The script does not
enumerate order three.  `py_compile` passed.

```bash
git diff --check -- appendix-unreduced-bv-qme.tex
git diff --no-index --check /dev/null reconstitution/swarm-2026-04-30-agent-158-minimal-full-equivariant-order3-test.md
grep -n '[[:blank:]]$' appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-158-minimal-full-equivariant-order3-test.md
rg -n "app-minimal-full-equivariant-all-order-vanishing|app-first-order-three-larger-package-datum" appendix-unreduced-bv-qme.tex
chktex -q appendix-unreduced-bv-qme.tex
lacheck appendix-unreduced-bv-qme.tex
```

`git diff --check` passed on the appendix.  The no-index diff check on the
new report emitted no whitespace diagnostics; its exit code is nonzero because
the file differs from `/dev/null`.  The trailing-whitespace grep returned no
hits.  The label scan found both new appendix labels.  `chktex` and `lacheck`
reported the existing appendix warning class, plus formula-style warnings on
the new displayed order-three bracket expressions; no fatal TeX parse error was
observed.

`make pdf` was not run because the shared checkout has many concurrent staged
edits and tracked build output.

## Remaining Obligations

- For any larger package, supply the actual order-three graph weights
  \(K^M_\Gamma\), differential expansions, CE-source faces, signs, scalar
  gates, and truncation matrices.
- If nonzero order-one or order-two rows are later added, supply all
  \(|\Gamma_1|_\hbar+|\Gamma_2|_\hbar=3\) bracket rows.
- After the row array exists, compute
  \([R^{\mathrm{ns}}_{3,M}]\in H^1(\mathcal K^\bullet_{\mathrm{ns},M})\)
  and the inverse-limit compatibility class.
