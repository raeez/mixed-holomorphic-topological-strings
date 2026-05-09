# Agent 125 - Quantum Shear Trace-Diagram Lemma

Status: obstruction inscribed.  Writable surface respected:
`appendix-radial-parts-moyal.tex` and this report.

## Claim Attacked

The open all-\(N\) input was the remaining primitive
\[
E_{a,b,N}=
\sum_{j=0}^b\operatorname{Tr}(Y^jX^aY^{b-j})
-J_N\!\left(\{z_1^{a+1}/(a+1),z_2^{b+1}\}_\hbar\right)
\]
as a left moment-ideal element
\[
E_{a,b,N}=\sum_W c_W^{a,b}\operatorname{Tr}(W M),
\qquad
M=YX-XY+\hbar N I.
\]
The attack was whether the universal free-word cyclic primitive from the
\(\hbar=0\) necklace equation already proves the quantum primitive.

## Valid Attacks

```yaml
id: A1-125-01
severity: 2
status: valid
lens: quantum lift
target: appendix-radial-parts-moyal.tex, primitive bottleneck
claim: The cyclic free-word equation is enough to prove the all-N primitive.
broken_step: Normal-ordering Tr(WM) produces contraction terms, including split trace diagrams, not seen in the cyclic quotient.
evidence_type: failing_test
evidence_ref: python3 scripts/quantum_shear_universal_formula.py --case 4,4 --classical-only --verify-ranks 2 --max-terms 20
files_read: [appendix-radial-parts-moyal.tex, scripts/quantum_shear_primitive_search.py, scripts/quantum_shear_universal_formula.py]
tools_used: [python3, sed, rg]
confidence: high
blast_radius: all-N radial-parts/Weyl-trace image remains conditional
minimal_heal: inscribe the free trace-diagram normal-form proof obligation and the first nonzero residual class
residual: no all-N contracting homotopy on the cyclic kernel has been proved
deciding_evidence: equality in the free indexed trace-diagram normal form before finite-rank specialization
```

```yaml
id: A1-125-02
severity: 2
status: healed
lens: finite-rank artifact
target: Agent 114 universal formula harness
claim: The N=2 correction for (4,4) can be promoted to theorem status.
broken_step: finite-rank normal monomial equality does not prove independence of free indexed trace diagrams.
evidence_type: unsupported
evidence_ref: python3 scripts/quantum_shear_universal_formula.py --case 4,4 --solve-ranks 2 --verify-ranks 3 --max-terms 12
files_read: [reconstitution/swarm-2026-04-30-agent-114-quantum-shear-universal-formula.md]
tools_used: [python3]
confidence: high
blast_radius: false all-N primitive theorem
minimal_heal: record ranks 2 and 3 as exact evidence only; state the missing normal-form theorem
residual: N=4 and free-diagram verification remain unproved
deciding_evidence: canonical free trace-diagram basis plus contracting homotopy
```

## Exact Residual

The lexicographic classical pivot solution in bidegree \((4,4)\) is
\[
\begin{aligned}
C^{\mathrm{cl}}_{4,4}
&=\frac{31}{7}\operatorname{Tr}(XXXYYY\,M)
-\frac{4}{7}\operatorname{Tr}(XXYXYY\,M)
-\frac{4}{7}\operatorname{Tr}(XXYYXY\,M)\\
&\quad+\frac{27}{7}\operatorname{Tr}(XXYYYX\,M)
+\frac{23}{7}\operatorname{Tr}(XYXXYY\,M)
+\frac{1}{7}\operatorname{Tr}(XYXYXY\,M)\\
&\quad+\operatorname{Tr}(XYXYYX\,M)
-\frac{2}{7}\operatorname{Tr}(XYYXXY\,M)
+\frac{15}{7}\operatorname{Tr}(XYYXYX\,M).
\end{aligned}
\]
It solves the cyclic \(\hbar=0\) equation but fails quantum lifting.
In rank \(N=2\),
\[
\begin{aligned}
R^{\mathrm{cl}}_{4,4,2}
&=E_{4,4,2}-C^{\mathrm{cl}}_{4,4}\\
&=\frac{43}{70}\hbar^2\bigl(
4\operatorname{Tr}(XXYY)-5\operatorname{Tr}(XYXY)
+2\operatorname{Tr}(XYYX)\\
&\hspace{4.2cm}
-5\operatorname{Tr}(YXYX)
+4\operatorname{Tr}(YYXX)\bigr)\neq0 .
\end{aligned}
\]
The normal-ordered monomial coefficient of
\(\hbar^2X^1{}_1X^1{}_1Y^1{}_2Y^2{}_1\) is \(43/7\).

The finite correction detected by the harness is the classical-kernel
element
\[
K_{4,4}=\frac{43}{14}\bigl(
\operatorname{Tr}(XXYXYY\,M)
-\operatorname{Tr}(XYXXYY\,M)
-\operatorname{Tr}(XYYXYX\,M)
+\operatorname{Tr}(XYYYXX\,M)\bigr),
\]
with \(\partial K_{4,4}=0\) in the cyclic associated graded.  Exact
normal-ordering verifies \(E_{4,4,N}=C^{\mathrm{cl}}_{4,4}+K_{4,4}\) for
\(N=2,3\).  This is evidence, not an all-\(N\) theorem.

## Repairs Made

Edited `appendix-radial-parts-moyal.tex`:

- Added `stmt:app-quantum-shear-trace-diagram-obstruction`.
- Defined the cyclic boundary \(\partial W=[WYX]-[WXY]\).
- Stated that the all-\(N\) primitive requires equality in the free
  indexed trace-diagram normal form, including multi-trace contractions.
- Recorded the \((4,4)\) classical residual and the kernel correction.
- Marked the remaining all-\(N\) theorem obligation explicitly.

## Commands Run

```text
sed -n '1,240p' ./CLAUDE.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/references/protocol.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,220p' ./AGENTS.md
sed -n '1,220p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '1,220p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
sed -n '1,260p' scripts/quantum_shear_primitive_search.py
sed -n '1,260p' scripts/quantum_shear_universal_formula.py
nl -ba appendix-radial-parts-moyal.tex | sed -n '1,838p'
python3 -m py_compile scripts/quantum_shear_primitive_search.py scripts/quantum_shear_universal_formula.py
python3 scripts/quantum_shear_primitive_search.py
python3 scripts/quantum_shear_universal_formula.py
python3 scripts/quantum_shear_universal_formula.py --case 4,4 --classical-only --verify-ranks 2 --max-terms 20
python3 scripts/quantum_shear_universal_formula.py --case 3,3 --case 2,4 --case 4,2 --solve-ranks 2,3 --verify-ranks 4 --max-terms 12
python3 scripts/quantum_shear_universal_formula.py --case 2,6 --case 6,2 --solve-ranks 2 --verify-ranks 3 --max-terms 20
python3 scripts/quantum_shear_universal_formula.py --case 4,4 --classical-only --verify-ranks 3 --max-terms 12
python3 scripts/quantum_shear_universal_formula.py --case 4,4 --solve-ranks 2 --verify-ranks 3 --max-terms 12
PYTHONPATH=scripts python3 - <<'PY'
# computed C^{cl}_{4,4}, K_{4,4}, and the residual class
PY
```

## Remaining Theorem Obligations

1. Construct the free indexed trace-diagram normal form for
   \(\mathcal N_{\mathrm{free}}(\operatorname{Tr}(WM))\), with
   multi-trace contraction terms retained before finite-rank trace
   identities.
2. Prove stable injectivity of that normal form in the degree range used,
   or state the precise Procesi--Razmyslov bound needed.
3. Build a canonical contracting homotopy on \(\ker\partial\) which
   chooses kernel corrections \(K_{a,b}\) and proves that their quantum
   contractions cancel the residuals in every bidegree.
4. Only after these three items close can
   \(E_{a,b,N}=\sum_W c_W^{a,b}\operatorname{Tr}(WM)\) be promoted to an
   all-\(N\) theorem.
