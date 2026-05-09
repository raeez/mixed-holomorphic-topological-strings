# Agent 140 - Trace-Diagram Normal Form

Status: attack-heal return.  Writable surface respected:
`appendix-radial-parts-moyal.tex`,
`scripts/quantum_shear_trace_diagram_normal_form.py`, and this report.

## Claim Attacked

After Agent 125 the bottleneck was the passage from the cyclic primitive
\[
  \partial c=
  \sum_{j=0}^b[Y^jX^aY^{b-j}]
  -\frac{b+1}{\binom{a+b}{a}}\sum_{U\in\operatorname{Sh}(a,b)}[U]
\]
to the quantum left-ideal primitive
\[
  E_{a,b,N}=\sum_W c_W^{a,b}\operatorname{Tr}(WM),
  \qquad M=YX-XY+\hbar NI,
\]
before imposing finite-rank trace identities.

## Repairs Inscribed

Added the following labels to `appendix-radial-parts-moyal.tex`.

- `def:app-free-indexed-normal-diagrams`
- `thm:app-free-indexed-normal-ordering`
- `lem:app-free-trace-diagram-stable-injectivity`
- `prop:app-free-trace-diagram-K44`
- `stmt:app-free-kernel-homotopy-obstruction`

The normal-ordering theorem is the free indexed formula
\[
  \mathcal N_{\mathrm{free}}\operatorname{Tr}(u)
  =
  \sum_{\Gamma}
  (-\hbar)^{|\Gamma|}N^{e(u,\Gamma)}\mathsf D(u,\Gamma),
\]
where \(\Gamma\) runs over partial matchings of original
\(Y\)-before-\(X\) inversions.  A matched pair \((p,q)\) deletes the
edges \(Y_p,X_q\) and imposes
\[
  v_q\sim v_{p+1},\qquad v_p\sim v_{q+1}.
\]
Disconnected components are retained as split-trace normal diagrams.

The stable injectivity lemma records the Procesi--Razmyslov bound used
here: diagrams of edge degree \(\le d\) are detected stably in ranks
\(N\ge d\).  It is not used to turn low-rank data into a theorem; it
only explains why free diagram equality is the correct all-\(N\) object.

## Exact \(4,4\) Formula

The uncorrected cyclic pivot residual is nonzero in the free diagram
basis:
\[
\begin{aligned}
  \mathcal N_{\mathrm{free}}
  (E_{4,4,N}-C^{\mathrm{cl}}_{4,4})
  &=
  \frac{43}{7}\hbar^2\Bigl(
    \mathsf D(X_{0\to1}X_{1\to2}Y_{2\to3}Y_{3\to0})\\
  &\quad
    -\mathsf D(X_{0\to1}X_{2\to3}Y_{1\to2}Y_{3\to0})\\
  &\quad
    -\hbar\,\mathsf D(X_{0\to0}\mid Y_{0\to0})
    +\hbar N\,\mathsf D(X_{0\to1}Y_{1\to0})
  \Bigr).
\end{aligned}
\]

The kernel correction is
\[
  K_{4,4}=\frac{43}{14}\bigl(
    \operatorname{Tr}(XXYXYY\,M)
    -\operatorname{Tr}(XYXXYY\,M)
    -\operatorname{Tr}(XYYXYX\,M)
    +\operatorname{Tr}(XYYYXX\,M)
  \bigr),
\]
with \(\partial K_{4,4}=0\), and the free normal form verifies
\[
  \mathcal N_{\mathrm{free}}(K_{4,4})
  =
  \mathcal N_{\mathrm{free}}
  (E_{4,4,N}-C^{\mathrm{cl}}_{4,4}).
\]
Thus \(E_{4,4,N}=C^{\mathrm{cl}}_{4,4}+K_{4,4}\) is all-\(N\) in the
free indexed diagram algebra.  This is stronger than the previous
rank-\(2,3\) check.

The edge-family candidates encoded in the script are
\[
  E_{2,b}^{\mathrm{cand}}
  =
  \sum_{r=0}^{\lfloor(b-2)/2\rfloor}
  (b-1-2r)\operatorname{Tr}(Y^rXY^{b-1-r}M)
\]
and
\[
  E_{a,2}^{\mathrm{cand}}
  =
  \frac{3}{a+1}
  \sum_{r=0}^{\lfloor(a-2)/2\rfloor}
  (a-1-2r)\operatorname{Tr}(X^{a-1-r}YX^rM).
\]
The free script verifies these through \((2,6)\) and \((6,2)\).  No
all-edge-family proof is claimed.

## Valid Attacks

```yaml
id: A1-140-01
severity: 2
status: healed
lens: quantum lift
target: stmt:app-quantum-shear-trace-diagram-obstruction
claim: The cyclic hbar=0 primitive is enough to lift to the quantum primitive.
broken_step: Normal ordering produces free indexed contraction diagrams, including split components, invisible in the cyclic quotient.
evidence_type: failing_test
evidence_ref: python3 scripts/quantum_shear_trace_diagram_normal_form.py --case 4,4 --classical-only --max-terms 12
files_read: [appendix-radial-parts-moyal.tex, scripts/quantum_shear_primitive_search.py, scripts/quantum_shear_universal_formula.py, reports 099/107/114/125]
tools_used: [python3, sed, rg]
confidence: high
blast_radius: all-N radial-parts/Weyl-trace primitive cannot be closed from necklace calculus alone
minimal_heal: define the free indexed normal form and record the four-term free residual
residual: global kernel homotopy not constructed
deciding_evidence: functorial K_{a,b} with N_free(K_{a,b})=R^{free}_{a,b}
```

```yaml
id: A1-140-02
severity: 2
status: healed
lens: finite-rank artifact
target: K_{4,4}
claim: The finite N=2,3 correction can be promoted only from finite checks.
broken_step: finite ranks may collapse free diagrams by trace identities.
evidence_type: other
evidence_ref: prop:app-free-trace-diagram-K44; trace-diagram script zero residual
files_read: [appendix-radial-parts-moyal.tex, reconstitution/swarm-2026-04-30-agent-125-quantum-shear-trace-diagram-lemma.md]
tools_used: [python3 scripts/quantum_shear_trace_diagram_normal_form.py --case 4,4]
confidence: high
blast_radius: false all-N primitive theorem if only finite ranks are used
minimal_heal: verify K_{4,4} in the free diagram basis
residual: none for bidegree (4,4)
deciding_evidence: zero free residual before finite-rank specialization
```

```yaml
id: A1-140-03
severity: 2
status: valid
lens: homotopy
target: all bidegrees (a,b)
claim: The all-N quantum shear primitive is now proved in every bidegree.
broken_step: No contracting homotopy on ker(partial) has been constructed.
evidence_type: proof_gap
evidence_ref: stmt:app-free-kernel-homotopy-obstruction
files_read: [appendix-radial-parts-moyal.tex]
tools_used: [python3 scripts/quantum_shear_trace_diagram_normal_form.py]
confidence: high
blast_radius: full radial-parts/Weyl-trace image remains conditional beyond certified bidegrees
minimal_heal: state the exact residual equation N_free(K_{a,b})=R^{free}_{a,b}
residual: construct functorial K_{a,b} and prove it cancels all contraction residuals
deciding_evidence: explicit contracting homotopy or equivalent closed formula
```

## Verification

Commands run:

```text
python3 -m py_compile scripts/quantum_shear_primitive_search.py scripts/quantum_shear_universal_formula.py scripts/quantum_shear_trace_diagram_normal_form.py
python3 scripts/quantum_shear_trace_diagram_normal_form.py --self-test --self-test-rank 2 --self-test-max-length 6 --max-terms 8
python3 scripts/quantum_shear_trace_diagram_normal_form.py --case 4,4 --classical-only --max-terms 12
python3 scripts/quantum_shear_universal_formula.py --case 4,4 --classical-only --verify-ranks 2 --max-terms 12
python3 scripts/quantum_shear_universal_formula.py --case 4,4 --solve-ranks 2 --verify-ranks 3 --max-terms 12
python3 scripts/quantum_shear_primitive_search.py --max-terms 6
python3 scripts/quantum_shear_universal_formula.py --max-terms 8
make pdf
```

Results:

- `py_compile`: PASS.
- Free normal-form default plus PBW self-test: PASS, 127 rank-two trace-word comparisons through length 6; all built-in free candidates have zero residual, including \(K_{4,4}\).
- Free `--classical-only` \(4,4\): expected FAIL with the four-term residual above.
- Universal finite `--classical-only` \(4,4\): expected FAIL.
- Universal corrected \(4,4\): PASS, solved at \(N=2\), verified at \(N=3\).
- Primitive finite harness: PASS, 19 cases.
- Universal finite harness: PASS, 11 cases.
- `make pdf`: PASS.  Existing underfull/overfull warnings remain; the appendix still has a small overfull line at the displayed \(K_{4,4}\) formula, but no TeX error.

## Remaining Theorem Obligations

1. Construct a contracting homotopy on \(\ker\partial\) which produces
   \(K_{a,b}\) functorially.
2. Prove \(\mathcal N_{\mathrm{free}}(K_{a,b})=R^{\mathrm{free}}_{a,b}\)
   for every bidegree.
3. Prove or replace the edge-family formulas beyond the checked window.
4. Only after these are closed may the quantum shear congruence be used
   as an unconditional all-bidegree theorem.
