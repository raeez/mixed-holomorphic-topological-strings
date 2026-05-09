# Agent 351 Theta3 Scalar-Zero Habitat Construction Report

Status: report-only. No TeX, script, figure, bibliography, PDF, or build
artifact was edited.

## Question

Construct, if possible, the minimal enlarged local-functional habitat in
which a scalar-zero
\[
  B^2_{02,20}
\]
can satisfy
\[
  d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}.
\]
The construction must specify generators, degrees, differential, scalar
projection, locality or wavefront class, and an exact universal property; if
this cannot be made honest in the present Costello package, the obstruction
must be named.

## Verdict

There are two different objects.

1. A minimal formal scalar-zero Bianchi-column extension exists. It is the
   initial filtered dg row habitat obtained from the current lower
   Bianchi-exposed complex by adjoining one degree-zero generator
   \(B^2_{02,20}\) with boundary \(-\mathfrak b^2_{02,20}\) and scalar
   projection zero.
2. This formal extension is not yet an honest Costello local-functional
   subhabitat of the current checkout. To make it honest one must supply a
   marked counterterm graph, regular-density or graphwise wavefront-admissible
   kernel data, a codimension-two closed boundary table, and finite-window
   transport. Without those data the obstruction is the current finite-row
   cokernel
   \[
     \widetilde\lambda_{02,\mathfrak b}
       =
     \frac12(E^2_{\nu_{02}})^*
       +(\mathfrak b^2_{02,20})^* .
   \]

Thus the supremum statement is not "there exists a Costello counterterm in
the current habitat." It is: the initial scalar-zero B-column extension is
defined, and an honest realization is equivalent to representing its new
generator by an admissible marked local counterterm with the displayed
boundary and transport data.

## Sources Read

- `reconstitution/swarm-2026-04-30-agent-346-theta3-bianchi-counterterm-supremum.md`
- `appendix-unreduced-bv-qme.tex:1600-1835`
- `appendix-unreduced-bv-qme.tex:2050-2675`
- `main.tex:8950-9135`
- `reconstitution/swarm-2026-04-30-agent-287-theta3-no-counterterm-controlled-enlargement-integration-spec.md`
- `reconstitution/swarm-2026-04-30-agent-294-theta3-actual-local-functional-b-column-construction-push.md`
- `reconstitution/swarm-2026-04-30-agent-304-theta3-h1-bianchi-transport-class-construction.md`
- `reconstitution/swarm-2026-04-30-agent-338-nonscalar-qme-next-supremum-plan.md`

## Current Lower Habitat

In the lower window \(N=2\), the Bianchi-exposed row basis is
\[
  e_1=E^2_{\nu_{02}},\qquad
  e_2=E^2_{\nu_{20}},\qquad
  e_3=\mathfrak b^2_{02,20}.
\]
The current degree-zero span is
\[
  \mathcal H^0_{\mathrm{cur}}
    =
  \mathbb C D^2_{02,20},
\]
and the current degree-one span is
\[
  \mathcal H^1_{\mathrm{cur}}
    =
  \mathbb C e_1\oplus\mathbb C e_2\oplus\mathbb C e_3.
\]
The source-coordinate primitive is
\[
  D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2),
  \qquad
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},
\]
with
\[
  d_{\mathrm{CE}}\zeta^0_2
    =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]
The local-functional differential is
\[
  d_{\mathrm{ns},2}D^2_{02,20}
    =
  -2e_1+2e_2+e_3.
\]
Thus the only current boundary column is
\[
  A_D^2=(-2,2,1)^T.
\]
The transported lower residual is
\[
  r_2=(2,-2,0)^T.
\]
The Bianchi-killing target is
\[
  A_B^2=(0,0,-1)^T=-e_3.
\]

The current habitat has no such column. Indeed
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}(A_B^2)=-1.
\]

## Minimal Formal Extension

Define the formal B-column row habitat
\[
  \mathcal H^{B,\bullet}_{2}
    =
  \mathcal H^\bullet_{\mathrm{cur}}
    \oplus
  \mathbb C B^2_{02,20}
\]
with \(B^2_{02,20}\) placed in degree \(0\). Explicitly,
\[
  \mathcal H^{B,0}_{2}
    =
  \mathbb C D^2_{02,20}\oplus \mathbb C B^2_{02,20},
\]
\[
  \mathcal H^{B,1}_{2}
    =
  \mathbb C e_1\oplus\mathbb C e_2\oplus\mathbb C e_3,
\]
and, in this extracted finite row complex,
\[
  \mathcal H^{B,k}_{2}=0\qquad(k\neq0,1).
\]
The differential is
\[
  dD^2_{02,20}=-2e_1+2e_2+e_3,\qquad
  dB^2_{02,20}=-e_3,
\]
\[
  de_1=de_2=de_3=0.
\]
The last line uses the row-closure datum already required to form the
non-scalar \(H^1\) obstruction: \(e_1,e_2\) are source-face rows in the
closed row table, and \(e_3\) is closed because \(d^2D^2_{02,20}=0\).

In matrix form,
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
  A^2_{D,B}(1,1)^T=(-2,2,0)^T=-r_2,
\]
or equivalently
\[
  d(D^2_{02,20}+B^2_{02,20})
    =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}.
\]
This kills the lower Bianchi residual. It does not solve the full
\(\theta_3\) tower and does not assert a complete Costello QME kernel.

## Scalar Projection

Let
\[
  \widehat\sigma_{\mathrm{sc},2}\colon
  \mathfrak Q^\bullet_{\mathcal G,2}(I)\to
  S^\bullet_2
\]
be the filtered chain scalar projection from the appendix, and let
\[
  \mathcal K^\bullet_{\mathrm{ns},2}(I)
    =
  \ker\widehat\sigma_{\mathrm{sc},2}.
\]
The formal extension is scalar-zero by definition:
\[
  \widehat\sigma^{B}_{\mathrm{sc},2}|_{\mathcal H_{\mathrm{cur}}}
    =
  \widehat\sigma_{\mathrm{sc},2}|_{\mathcal H_{\mathrm{cur}}},
  \qquad
  \widehat\sigma^{B}_{\mathrm{sc},2}(B^2_{02,20})=0.
\]
Since \(e_3=\mathfrak b^2_{02,20}\) is a scalar-zero Bianchi row,
\[
  \widehat\sigma^{B}_{\mathrm{sc},2}(dB^2_{02,20})
    =
  -\widehat\sigma_{\mathrm{sc},2}(e_3)=0.
\]
Hence the projection remains a chain map on the formal B-column extension.
If an intended enlargement has no filtered chain scalar projection extending
this rule, then \(\ker\widehat\sigma_{\mathrm{sc},2}\) is not a complex and
the B-column theorem cannot even be stated.

## Locality And Wavefront Class

The new generator cannot be an arbitrary distributional current. The minimal
admissible Costello-local version must be a new oriented marked counterterm
graph
\[
  \Gamma_B=\Gamma^2_{B,02,20}
\]
in a finite-window marked Costello list \(\mathcal G^{B,\mathrm{mk}}_2\),
with one represented local functional
\[
  X_{\Gamma_B,o_B,\mathfrak m_B,2}
    =
  B^2_{02,20}.
\]
Its admissible labels must be those allowed in
`appendix-unreduced-bv-qme.tex:1624`: finite-window CE labels, the local
interaction \(I^w_{0,2}\), supplied renormalized graph-weight or local
counterterm vertices, admissible propagator or BV-contraction edges, and
full-equivariant marker tensors.

There are two acceptable analytic branches.

1. Regular-density branch:
   all brane labels of \(\Gamma_B\) lie in
   \(\mathcal D^{\mathrm{reg}}_c(I)\). The counterterm is supported on the
   small diagonal collision stratum that produces
   \(\mathfrak b^2_{02,20}\), and its boundary table contains the single
   Bianchi face with coefficient \(-1\), plus any further faces forced by
   codimension-two closure.
2. Wavefront branch:
   the brane labels lie in a graphwise admissible class
   \(\mathcal D'_{c,\mathrm{WF}}(I;\Gamma_B,2)\). The wavefront set must be
   contained in the chosen conormal collision cone, all incidence pullbacks
   and products must satisfy the Hormander noncharacteristic criterion, the
   scaling degree at the small diagonal must admit the declared local
   extension, and the same extension must be used in the marked boundary
   table.

In both branches the marked boundary differential must satisfy
\[
  d_{\mathrm{mk}}X_{\Gamma_B,o_B,\mathfrak m_B,2}
    =
  -X_{\mathfrak b,02,20,2},
\]
with no \(E^2_{\nu_{02}}\) or \(E^2_{\nu_{20}}\) component. The scalar marker
must have zero cyclic supertrace, or the scalar projection must be otherwise
proved zero by the chain scalar projection. Codimension-two closure is part of
the datum; without it \(d^2=0\) has not been proved in the enlarged marked
habitat.

## Universal Property

Let \(\mathbf{Hab}_{B,2}\) be the category whose objects are tuples
\[
  (\mathcal L^\bullet,d_{\mathcal L},i,\sigma_{\mathcal L},x)
\]
where:

- \(\mathcal L^\bullet\) is a complete filtered finite-row dg habitat with a
  regular-density or graphwise wavefront-admissible local-functional label
  class;
- \(i\colon\mathcal H^\bullet_{\mathrm{cur}}\to\mathcal L^\bullet\) is a
  filtered dg map preserving the lower row basis;
- \(\sigma_{\mathcal L}\) is a filtered chain scalar projection extending
  the current scalar projection;
- \(x\in\mathcal L^0\) is scalar-zero and admissible in the chosen locality
  class;
- \(d_{\mathcal L}x=-i(e_3)\), with zero \(i(e_1)\) and \(i(e_2)\)
  components.

Morphisms preserve \(i\), \(\sigma\), filtrations, locality class, and the
chosen element \(x\).

Then \(\mathcal H^{B,\bullet}_2\) is initial in the formal version of
\(\mathbf{Hab}_{B,2}\): for every object
\((\mathcal L,d_{\mathcal L},i,\sigma_{\mathcal L},x)\) there is a unique
filtered dg map
\[
  \Phi\colon \mathcal H^{B,\bullet}_2\to\mathcal L^\bullet
\]
with
\[
  \Phi|_{\mathcal H_{\mathrm{cur}}}=i,\qquad
  \Phi(B^2_{02,20})=x.
\]
The proof is immediate: the old generators are fixed by \(i\), the new
generator is forced to go to \(x\), and the differential relation
\(dB^2_{02,20}=-e_3\) is exactly the defining relation on \(x\). The scalar
projection condition is also forced by
\(\sigma_{\mathcal L}(x)=0\).

This universal property is the precise meaning of "minimal enlargement."
It is a free scalar-zero cone extension on the Bianchi cycle
\(\mathfrak b^2_{02,20}\), not a hidden primitive in the present habitat.

## Obstruction To Honest Realization In The Current Checkout

Let \(\mathcal L\) be any lower finite-row subhabitat of the current
Costello package whose degree-zero lower row span is generated by the current
source-coordinate primitive \(D^2_{02,20}\), and whose differential column is
therefore contained in the span of
\[
  A_D^2=(-2,2,1)^T.
\]
Then no scalar-zero element \(x\in\mathcal L^0\) satisfies
\[
  dx=-\mathfrak b^2_{02,20}.
\]
Indeed \(\widetilde\lambda_{02,\mathfrak b}\) annihilates every current
boundary column but evaluates to \(-1\) on the target:
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}(-\mathfrak b^2_{02,20})=-1.
\]
Equivalently, the equation
\[
  c(-2,2,1)^T=(0,0,-1)^T
\]
forces \(c=0\) from the first two coordinates and \(c=-1\) from the third.

Thus any honest positive theorem must add an actual new local-functional
column whose \(\widetilde\lambda_{02,\mathfrak b}\)-value is \(-1\). Naming
\(B^2_{02,20}\) without a marked graph, scalar-zero proof, admissible
locality or wavefront representative, and boundary table does not cross this
obstruction.

## Tower Gate

A fixed-window B-column is not a tower. For \(M\ge N\), a compatible family
\(B^M\) must satisfy
\[
  d_{\mathrm{ns},M}B^M=-\mathfrak b^M
\]
and
\[
  \Delta^1_{M,N}
    :=
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N
    =
  d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N),
\]
possibly after a supplied scalar-zero correction \(H^{M,N}\). After choosing
such corrections, the secondary primitive class
\[
  [\pi_{M,N}B^M-B^N-H^{M,N}]
  \in
  \varprojlim\nolimits^1_N
  H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I))
\]
must vanish. Agent 304 constructs this \(H^1\) transport class formally; it
does not construct the \(B^M\)-tower.

## Report-Level Construction Target

The next theorem-grade definition should be a supplied datum
\[
  \mathfrak B_{\theta_3}
  =
  \left(
    \mathcal G^{B,\mathrm{mk}}_M,\,
    B^M_{02,20},\,
    \widehat\sigma^B_{\mathrm{sc},M},\,
    \pi^B_{M,N},\,
    H^{M,N}
  \right)
\]
such that:

1. \(B^M_{02,20}\in\mathcal K^0_{\mathrm{ns},M}(I)\);
2. \(d_{\mathrm{ns},M}B^M_{02,20}=-\mathfrak b^M\);
3. \(\widehat\sigma^B_{\mathrm{sc},M}(B^M_{02,20})=0\);
4. \(B^M_{02,20}\) is represented by a regular-density or graphwise
   wavefront-admissible marked counterterm graph;
5. the marked boundary table is codimension-two closed;
6. \(\Delta^1_{M,N}\) is killed by the displayed transport primitive or by
   supplied corrections \(H^{M,N}\);
7. the resulting secondary \(\varprojlim^1H^0\) class is zero.

Only after this datum is constructed may the manuscript say that the
scalar-zero \(B^2_{02,20}\) exists as a Costello local-functional
counterterm. Until then, the current true statement is the obstruction
theorem plus the initial formal B-column extension above.

## Verification

Commands run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile scripts/finite_window_graph_array.py
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from fractions import Fraction
AD=(Fraction(-2),Fraction(2),Fraction(1))
r=(Fraction(2),Fraction(-2),Fraction(0))
AB=(Fraction(0),Fraction(0),Fraction(-1))
ell=(Fraction(1,2),Fraction(0),Fraction(1))
def dot(u,v): return sum(a*b for a,b in zip(u,v))
print('ell_A_D', dot(ell, AD))
print('ell_r', dot(ell, r))
print('ell_A_B', dot(ell, AB))
print('equals_minus_r', tuple(a+b for a,b in zip(AD,AB)) == tuple(-x for x in r))
PY
git diff --check --no-index -- /dev/null reconstitution/swarm-2026-04-30-agent-351-theta3-scalar-zero-habitat-construction.md
```

Decisive output:

```text
ell_A_D 0
ell_r 1
ell_A_B -1
equals_minus_r True
```

The `git diff --check --no-index` command emitted no whitespace diagnostics;
its nonzero exit status is the standard `--no-index` difference status for
`/dev/null` versus the new report file.

Files changed:

- `reconstitution/swarm-2026-04-30-agent-351-theta3-scalar-zero-habitat-construction.md`
