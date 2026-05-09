# Agent 248: radial necklace Hodge homotopy construction push

Date: 2026-04-30.

Owned write paths:

- `reconstitution/radial-necklace-hodge-homotopy-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-248-radial-necklace-hodge-homotopy-construction-push.md`

No manuscript or script file was edited.

## Loaded protocol

Read `CLAUDE.md`, `AGENTS.md`, `~/ecosystem/INVARIANTS.md`,
`~/ecosystem/AGENTS-HARNESS.md`, the `~/ecosystem` attack-heal protocol, the
local `chriss-ginzburg-rectify` skill, and the Vol II rectify skill.  Read
the radial appendix, theorem lane, open-obligations ledger, claim-strength
ledger, both quantum shear scripts, Agent 230's report, and the radial
reports from Agents 191, 203, 209, and 217.

## Stable core

The all-bidegree homotopy was not constructed.  The exact obstruction theorem
was constructed.

For \(a,b\geq1\), define the two-colour necklace graph \(G_{a,b}\) with
vertices cyclic words with \(a\) \(X\)'s and \(b\) \(Y\)'s and edges
\[
  e_W:[WXY]\to[WYX],
  \qquad W\in\mathbb Q\langle X,Y\rangle_{a-1,b-1}.
\]
Then \(\partial W=[WYX]-[WXY]\) is the graph incidence map and
\(\ker\partial\) is the cycle space.

Let
\[
  C^+_{a,b}(W)=
  \pi_+\mathcal N_{\mathrm{free}}\operatorname{Tr}(WM),
  \qquad M=YX-XY+\hbar NI,
\]
and set
\[
  A_{a,b}=C^+_{a,b}|_{\ker\partial}.
\]
The decorated Laplacian is
\[
  \Delta^{\mathrm{dec}}_{a,b}=A_{a,b}A_{a,b}^*,
  \qquad
  \mathsf H^{\mathrm{dec}}_{a,b}=\ker A_{a,b}^*.
\]
The exact obstruction is
\[
  \Pi^{\mathrm{harm}}_{a,b}R^{\mathrm{free}}_{a,b}.
\]
It vanishes if and only if there exists
\[
  K_{a,b}\in\ker\partial
  \quad\text{with}\quad
  C^+_{a,b}(K_{a,b})=R^{\mathrm{free}}_{a,b}.
\]
When it vanishes, the Hodge correction is
\[
  K_{a,b}=A_{a,b}^*
  (\Delta^{\mathrm{dec}}_{a,b})^{-1}R^{\mathrm{free}}_{a,b},
\]
with the inverse on \(\operatorname{im}A_{a,b}\).  When it does not vanish,
any functional detecting the harmonic component is the exact left-cokernel
obstruction to the all-bidegree radial/Weyl theorem.

## Potential form

A diagram functional \(\lambda\) is a left-cokernel functional precisely when
the edge cochain
\[
  W\longmapsto \lambda C^+_{a,b}(W)
\]
has zero periods on \(G_{a,b}\).  Since \(G_{a,b}\) is connected, this is
equivalent to a vertex potential \(\phi_\lambda\) satisfying
\[
  \lambda C^+_{a,b}(W)
  =
  \phi_\lambda([WYX])-\phi_\lambda([WXY]).
\]
For
\[
  T_{a,b}
  =
  \sum_{j=0}^{b}[Y^jX^aY^{b-j}]
  -
  {b+1\over\binom{a+b}{a}}
  \sum_{U\in\operatorname{Sh}(a,b)}[U],
\]
the all-bidegree vanishing condition is exactly
\[
  \lambda\pi_+\mathcal N_{\mathrm{free}}(E_{a,b,N})
  =
  \phi_\lambda(T_{a,b})
\]
for every such \(\lambda\).  This is the next theorem target.  Finite tables
do not prove it.

## Valid attacks

```yaml
- id: A248-01
  severity: 2
  status: healed
  target: Agent 230 Hodge formula
  finding: the bare graph Laplacian inverts incidence, but the quantum
    correction equation is C^+(K)=R on ker(partial)
  repair: define the relative decorated Laplacian A A^* for
    A=C^+|_{ker partial}

- id: A248-02
  severity: 2
  status: valid-not-closed
  target: all-bidegree Pi_harm R=0
  finding: no proof of the potential identity was found
  residual: prove lambda(E^+)=phi_lambda(T) for every decorated left-cokernel
    functional, or exhibit the first failing harmonic row

- id: A248-03
  severity: 3
  status: healed
  target: failure mode
  finding: failure is not vague; it is the nonzero harmonic projection
    Pi_harm R_free, equivalently a stable left-cokernel functional with
    nonzero residual pairing
```

## Finite calibration

Commands run with `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`.

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --self-test --self-test-rank 2 --self-test-max-length 5 \
  --case 4,4 --max-terms 0

PASS self-test rank=2 max_length=5 checked=63
PASS a=4 b=4 mode=candidate target_terms=39 candidate_terms=10 residual_terms=0
```

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --case 5,5 --kernel-correction --max-terms 0

PASS a=4 b=4 mode=kernel-correction ... residual_terms=4
  correction_terms=4 rank=10 rows=49 cols=20 corrected_residual_terms=0
PASS a=5 b=5 mode=kernel-correction ... residual_terms=22
  correction_terms=16 rank=29 rows=143 cols=70 corrected_residual_terms=0
```

Read-only rank calibration:

```text
(3,3): cycle_dim=3, rank_A=0, residual_terms=0
(4,4): cycle_dim=11, rank_A=1, residual_terms=4
(5,5): cycle_dim=45, rank_A=4, residual_terms=22
```

These checks guided the proof.  They are not used as all-bidegree evidence.

## Proposed insertion

The detailed report gives a manuscript-ready insertion after
Statement `stmt:app-free-kernel-homotopy-obstruction`: a definition of the
decorated necklace Hodge obstruction, a proposition proving the equivalence
\[
  \mathfrak o_{a,b}=0
  \Longleftrightarrow
  \Pi^{\mathrm{harm}}_{a,b}R^{\mathrm{free}}_{a,b}=0,
\]
and the potential-form remark.  It should not assert
\(\Pi^{\mathrm{harm}}_{a,b}=0\) in all bidegrees until the potential identity
is proved.

## Files changed

- `reconstitution/radial-necklace-hodge-homotopy-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-248-radial-necklace-hodge-homotopy-construction-push.md`
