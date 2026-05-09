# Agent 114 - Quantum Shear Universal Formula

Status: attack-heal return.  Writable surface respected:
`scripts/quantum_shear_universal_formula.py` and this report only.

## Target

Agent 107 produced exact finite primitives for
\[
  E_{a,b,N}
  =
  \sum_{j=0}^b \operatorname{Tr}(Y^jX^aY^{b-j})
  -
  J_N\!\left(
    \{z_1^{a+1}/(a+1),z_2^{b+1}\}_\hbar
  \right)
\]
using the left-ideal convention
\[
  \operatorname{Tr}(WM)=\sum_{i,j}W^j{}_iM^i{}_j,\qquad
  M^i{}_j=(YX-XY+\hbar N I)^i{}_j .
\]
The theorem-grade target is a coefficient system
\[
  E_{a,b,N}=\sum_W c_W^{a,b}\operatorname{Tr}(WM)
\]
with \(c_W^{a,b}\in\mathbb Q\) independent of \(N\), before imposing
finite-rank trace identities.

## Repair Artifact

Created `scripts/quantum_shear_universal_formula.py`.

The script keeps the unknowns as free words \(W\) with \(a-1\) letters
\(X\) and \(b-1\) letters \(Y\).  It first imposes the universal
classical cyclic equation
\[
\sum_W c_W^{a,b}
  \bigl(\operatorname{Tr}(WYX)-\operatorname{Tr}(WXY)\bigr)
=
\sum_{j=0}^b \operatorname{Tr}(Y^jX^aY^{b-j})
-\frac{b+1}{\binom{a+b}{a}}
  \sum_{U\in\operatorname{Sh}(a,b)}\operatorname{Tr}(U).
\]
It can then impose exact finite Weyl-algebra rows using the same
coefficients.  Thus the word support is universal; the quantum lift is
still finite evidence until the normal-ordering lemma below is proved.

The diagnostic `--classical-only` mode is load-bearing.  It shows that
the \(\hbar=0\) cyclic primitive alone is not automatically a quantum
primitive.

## Primitive Patterns Found

The following representatives are computed by the new script.  They are
finite-verified candidate universal formulas, not all-\(N\) theorems.
The representative is not unique because the word-to-primitive map has a
kernel; for example Agent 107's
\(-\operatorname{Tr}(YX\,M)\) and the script's
\(\operatorname{Tr}(XY\,M)\) both verify for \((a,b)=(2,2)\) in the
tested ranks.

\[
\begin{aligned}
E_{2,2,N}&=\operatorname{Tr}(XY\,M),\\
E_{2,3,N}&=2\operatorname{Tr}(XYY\,M),\\
E_{3,2,N}&=\frac32\operatorname{Tr}(XXY\,M),\\
E_{3,3,N}&=\frac{14}{5}\operatorname{Tr}(XXYY\,M)
 +\frac25\operatorname{Tr}(XYXY\,M)
 +\frac85\operatorname{Tr}(XYYX\,M),\\
E_{2,4,N}&=3\operatorname{Tr}(XYYY\,M)
 +\operatorname{Tr}(YXYY\,M),\\
E_{4,2,N}&=\frac95\operatorname{Tr}(XXXY\,M)
 +\frac35\operatorname{Tr}(XXYX\,M),\\
E_{3,4,N}&=4\operatorname{Tr}(XXYYY\,M)
 +2\operatorname{Tr}(XYXYY\,M)
 -\operatorname{Tr}(XYYXY\,M)
 +3\operatorname{Tr}(XYYYX\,M),\\
E_{4,3,N}&=\frac{16}{5}\operatorname{Tr}(XXXYY\,M)
 -\frac45\operatorname{Tr}(XXYXY\,M)
 +\frac{12}{5}\operatorname{Tr}(XXYYX\,M)
 +\frac85\operatorname{Tr}(XYXXY\,M).
\end{aligned}
\]

The edge families now have a visible pattern:
\[
  E_{2,b,N}
  =
  \sum_{r=0}^{\lfloor(b-2)/2\rfloor}
  (b-1-2r)\operatorname{Tr}(Y^rXY^{b-1-r}M),
\]
computed and finite-verified for \(2\le b\le6\), and
\[
  E_{a,2,N}
  =
  \frac{3}{a+1}
  \sum_{r=0}^{\lfloor(a-2)/2\rfloor}
  (a-1-2r)\operatorname{Tr}(X^{a-1-r}YX^rM),
\]
computed and finite-verified for \(2\le a\le6\).

For \((a,b)=(4,4)\), the classical cyclic solution fails the quantum
test at \(N=2\).  Adding a finite-detected classical-kernel correction
gives the verified \(N=2\) candidate
\[
\begin{aligned}
E_{4,4,2}
&=\frac{31}{7}\operatorname{Tr}(XXXYYY\,M)
 +\frac52\operatorname{Tr}(XXYXYY\,M)
 -\frac47\operatorname{Tr}(XXYYXY\,M)\\
&\quad+\frac{27}{7}\operatorname{Tr}(XXYYYX\,M)
 +\frac{3}{14}\operatorname{Tr}(XYXXYY\,M)
 +\frac17\operatorname{Tr}(XYXYXY\,M)\\
&\quad+\operatorname{Tr}(XYXYYX\,M)
 -\frac27\operatorname{Tr}(XYYXXY\,M)
 -\frac{13}{14}\operatorname{Tr}(XYYXYX\,M)\\
&\quad+\frac{43}{14}\operatorname{Tr}(XYYYXX\,M).
\end{aligned}
\]
This is evidence only.  The \(N=2\) kernel is too large to certify this
as the all-\(N\) representative.

## Exact Tested Range

Default command:

```text
python3 scripts/quantum_shear_universal_formula.py
```

passed 11 cases:
\[
(2,2),(2,3),(3,2),(3,3),(2,4),(4,2),(3,4),(4,3),(2,5),(5,2),(4,4).
\]
Ranks checked:
\[
\begin{gathered}
N=2,3 \text{ for all listed cases except } (4,4),\\
N=4 \text{ for } (2,2),(2,3),(3,2),\\
N=2 \text{ for } (4,4).
\end{gathered}
\]

Additional targeted checks passed:
\[
\begin{gathered}
N=4 \text{ for } (3,3),(2,4),(4,2),\\
N=3 \text{ for } (2,6),(6,2) \text{ after solving with } N=2.
\end{gathered}
\]

The diagnostic check

```text
python3 scripts/quantum_shear_universal_formula.py --case 4,4 --classical-only --verify-ranks 2
```

failed as expected: the pure cyclic \(\hbar=0\) representative has
support 9 and does not reconstruct the finite \(N=2\) quantum defect.

## Attack Ledger

```yaml
id: A1-114-01
severity: 2
status: healed
lens: finite-rank artifact
target: Agent 107 primitive table
claim: Stable finite primitives give a universal all-N formula.
broken_step: finite matrix ranks can satisfy trace identities absent in the free indexed algebra.
evidence_type: unsupported
evidence_ref: scripts/quantum_shear_universal_formula.py default run separates free-word unknowns from finite rows
files_read: [appendix-radial-parts-moyal.tex, scripts/quantum_shear_primitive_search.py, reconstitution/swarm-2026-04-30-agent-099-quantum-shear-congruence.md, reconstitution/swarm-2026-04-30-agent-107-quantum-shear-primitive.md]
tools_used: [rg, sed, python3 scripts/quantum_shear_universal_formula.py]
confidence: high
blast_radius: all-N radial-parts theorem remains conditional
minimal_heal: create a free-word coefficient harness and record exact finite verification separately
residual: no trace-diagram proof of all-N normal-ordering yet
deciding_evidence: equality in the free indexed Weyl algebra with formal hbar and N
```

```yaml
id: A1-114-02
severity: 2
status: valid
lens: quantum lift
target: classical cyclic primitive equation
claim: solving the hbar=0 cyclic trace equation suffices for the quantum primitive.
broken_step: the (4,4) classical-only solution fails exact finite verification at N=2.
evidence_type: failing_test
evidence_ref: python3 scripts/quantum_shear_universal_formula.py --case 4,4 --classical-only --verify-ranks 2
files_read: [scripts/quantum_shear_universal_formula.py]
tools_used: [python3]
confidence: high
blast_radius: theorem cannot be closed by classical necklace calculus alone
minimal_heal: add a quantum normal-ordering condition, or prove a canonical kernel correction exists in every bidegree
residual: kernel correction is finite-detected, not proved in the free indexed algebra
deciding_evidence: the normal-ordering lemma stated below
```

```yaml
id: A1-114-03
severity: 3
status: valid
lens: nonuniqueness
target: coefficients c_W^{a,b}
claim: the displayed coefficient vector is canonical.
broken_step: different word representatives verify the same finite primitive; the linear map has kernel.
evidence_type: other
evidence_ref: Agent 107 E_{2,2,N}=-Tr(YX M), new script E_{2,2,N}=Tr(XY M)
files_read: [reconstitution/swarm-2026-04-30-agent-107-quantum-shear-primitive.md]
tools_used: [python3 scripts/quantum_shear_universal_formula.py]
confidence: high
blast_radius: a theorem statement needs a chosen gauge/normal form for c_W
minimal_heal: define coefficients as the lexicographic pivot solution or give a canonical homotopy inverse
residual: no canonical homotopy inverse has been proved
deciding_evidence: a free-word complex with a specified contracting homotopy
```

## Residual Theorem Obligation

The exact missing lemma is:

**Free indexed quantum-lift lemma.**  For every \(a,b\ge2\), let
\(c_W^{a,b}\) be the chosen free-word solution of the cyclic equation
above, after the prescribed kernel correction.  In the free indexed Weyl
algebra, before imposing any finite \(N\) trace identity,
\[
  \operatorname{NO}\!\left(
    \sum_W c_W^{a,b}\operatorname{Tr}(W(YX-XY+\hbar N I))
  \right)
  =
  E_{a,b,N}
\]
as a polynomial in \(\hbar\), \(N\), and normal-ordered trace diagrams.

Equivalently, the contraction terms produced by normal-ordering
\(\sum_W c_W^{a,b}\operatorname{Tr}(WM)\) must equal exactly the higher
odd Moyal terms
\[
  \sum_{s\ge1}
  \frac{\hbar^{2s}(a+1)_{2s+1}(b+1)_{2s+1}}
  {(a+1)2^{2s}(2s+1)!}
  J_N(z_1^{a-2s}z_2^{b-2s})
\]
with the signs fixed by \(Y X=X Y-\hbar(\delta\delta)\).

This lemma must be proved in a trace-diagram normal form that allows
multi-trace contractions.  Finite \(N\) monomial expansion is not a
substitute: it collapses diagrams by rank-dependent trace identities.

## Verification Run

Commands run:

```text
python3 -m py_compile scripts/quantum_shear_universal_formula.py
python3 scripts/quantum_shear_universal_formula.py
python3 scripts/quantum_shear_universal_formula.py --case 4,4 --classical-only --verify-ranks 2
python3 scripts/quantum_shear_universal_formula.py --case 2,4 --case 4,2 --solve-ranks 2,3 --verify-ranks 4
python3 scripts/quantum_shear_universal_formula.py --case 3,3 --solve-ranks 2,3 --verify-ranks 4
python3 scripts/quantum_shear_universal_formula.py --case 2,6 --solve-ranks 2 --verify-ranks 3 --max-terms 20
python3 scripts/quantum_shear_universal_formula.py --case 6,2 --solve-ranks 2 --verify-ranks 3 --max-terms 20
```

Results:

- `py_compile`: PASS.
- Default universal-formula run: PASS, 11 cases.
- Classical-only \((4,4)\): expected FAIL; records the quantum-lift
  obstruction.
- Targeted \(N=4\) and edge-family checks: PASS.

## Claim-Status Recommendation

Do not state the all-\(N\) primitive as proved.  The stable claim is:
there is a hbar-free free-word primitive ansatz; it satisfies the
universal classical cyclic equation in the tested bidegrees; and exact
finite Weyl-algebra checks verify the same coefficients in the ranks
listed above.  The theorem closes only after the free indexed
quantum-lift lemma is proved.
