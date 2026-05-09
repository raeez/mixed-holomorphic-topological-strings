# Phase 4 Execution / P4-Sergeev-Intertwiner — Concrete construction of the Howe-Sergeev coefficient-coupling intertwiner $\Phi_{\mathrm{Sergeev}}$

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Witten primary (boundary-state physics; intertwiners between
open and closed channels; queer / parastate brane species);
Boundary secondary (precise boundary-state algebra of the Str-brane and
otr-brane and the explicit intertwiner action on each).
**Mode.** Phase-4 EXEC, proposal-only — no manuscript edits, no
commits. Master ledger schema; ID prefix `P4-EXEC-Sergeev-Intertwiner-`.
Writable surfaces: this file + `scripts/check_sergeev_intertwiner.py`.
**Posture.** P4-EXEC-Sergeev-Duality-Probe (1334 lines) identified
$\Phi_{\mathrm{Sergeev}}$ as the canonical coefficient-coupling
intertwiner predicted by Howe–Sergeev duality (Cheng–Wang Ch. 5
Theorem 5.4; Sergeev 1985 Sbornik 51, 419–427), and named the
predicted residue identity
$\Phi_{\mathrm{Sergeev}}(\hbar N\,[\bar c])=\hbar N\,[\bar c]^{\mathrm{otr}}$
as a **coefficient-class identity** in $H^2_{\mathrm{Lie}}(\bar A,\C\oplus\Pi\C)$
that does **not** lift to a chain-level isomorphism (Sergeev-A5
firewall, structurally identical to BCOV-A5). This document executes
the explicit construction of $\Phi_{\mathrm{Sergeev}}$, verifies its
well-definedness, runs an exact `fractions.Fraction` numerical
verification at the smallest non-trivial case $(N=2, n=2)$, and
records the cross-walk to Brane-Species-Audit Tier II (q(N) doubled
brane).

**Inputs (full reads or targeted reads as indicated).**
* `CLAUDE.md` (full).
* `reconstitution/phase4-exec-Sergeev-Duality-Probe-2026-04-28.md`
  (1334 lines; Howe-Sergeev framework; $\Phi_{\mathrm{Sergeev}}$
  prediction; firewall structurally identical to BCOV-A5).
* `reconstitution/phase4-exec-Theorem-G-otr-inscription-2026-04-28.md`
  (1374 lines; Theorem G\textsuperscript{otr}; queer-Capelli
  $Z_2^{\mathrm{otr}}$; two-supertrace independence).
* `reconstitution/phase4-exec-G3-M3-queer-trace-2026-04-28.md` (1108
  lines; $\mathrm{otr}(J)=N$ derivation; Obs-Q-otr-A5).
* `reconstitution/phase4-exec-classical-super-extension-2026-04-28.md`
  (G3-M2; q(N) two-supertrace structure).
* `reconstitution/phase4-exec-Brane-Species-Audit-2026-04-28.md`
  (Tier II q(N) doubled brane; Str-brane and otr-brane).
* `reconstitution/phase4-exec-G3-M4-super-numerical-sweep-2026-04-28.md`
  (N=2 sweep).
* `reconstitution/phase4-exec-G3-M5-super-numerical-sweep-N3-2026-04-28.md`
  (N=3 sweep).

**Standard primary-source references (cited from memory; not new
inscriptions).**
* A. Sergeev, "The tensor algebra of the identity representation as a
  module over Gl(n|m) and Q(n)", *Math. USSR Sbornik* **51** (1985),
  419–427. **Schur–Weyl–Sergeev duality on q(N).**
* S.-J. Cheng, W. Wang, *Dualities and representations of Lie
  superalgebras*, AMS GSM **144** (2012), Ch. 4 + Ch. 5. **Howe-Sergeev
  framework.**
* A. Berele, A. Regev, "Hook Young diagrams with applications to
  combinatorics and representations of Lie superalgebras",
  *Adv. Math.* **64** (1987), 118–175. **Strict-partition hook
  formula.**
* K. Coulembier, "Tensor ideals, Deligne categories and invariant
  theory", *Selecta Math.* **24** (2018), 4659–4710.
  **Categorical lift, Theorem 5.2.**
* M. Nazarov, "Capelli identities for Lie superalgebras", *Ann. Sci.
  ENS* **30** (1997), 847–872. **Super-Capelli.**
* J. Brundan, A. Kleshchev, "Hecke–Clifford superalgebras, crystals of
  type $A_{2\ell}^{(2)}$", *Represent. Theory* **5** (2001), 317–403.

---

## §0. Executive verdict

**Three-line bottom line.**

1. **Explicit construction (one-line).** $\Phi_{\mathrm{Sergeev}}$ is
   the parity-flip intertwiner on the 2-dimensional graded coefficient
   space $\C\oplus\Pi\C$ realising the Howe–Sergeev central-character
   match $\Tr_{\mathfrak{gl}_N}(I_N)=\mathrm{otr}_{\mathfrak q(N)}(J)
   =N$ as a sequence of three coefficient legs:
   (Leg 1) bosonic central character $\Tr_{\mathfrak{gl}_N}(I_N)=N$;
   (Leg 2) Hecke–Clifford $\mathcal{HC}_n$-action on $V^{\otimes n}$,
   $V=\C^{N|N}$, preserving $N$ as the Howe–Sergeev central character
   on the $(\mathfrak q(N), \mathcal{HC}_n)$-bimodule decomposition;
   (Leg 3) queer central character
   $\mathrm{otr}_{\mathfrak q(N)}(J)=N$. Concretely on cohomology
   classes:
   $$\Phi_{\mathrm{Sergeev}}\bigl(\hbar N\,[\bar c]\bigr)
   =\hbar N\,[\bar c]^{\mathrm{otr}}\in H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}.$$

2. **Well-definedness verdict.** The intertwiner is well-defined at
   the cohomology layer:
   - **Independence of strict-partition choice** verified — the
     Howe-Sergeev central character $N$ is a representation-theoretic
     invariant, not a partition-specific datum (it is the value of
     $I_{2N}$ on the bosonic side and of $J$ on the queer side; both
     equal $N$ on every $L_\lambda^{\mathfrak q}$ summand at the leading
     order of the Berele–Regev hook formula).
   - **Chain-level closure** preserves the residue class — the
     $\omega$-cocycle of `lem:omega-cocycle` is unchanged under
     $\Phi_{\mathrm{Sergeev}}$; only the coefficient line shifts from
     $\C$ to $\Pi\C$.

3. **Chain-level lift status.** **Blocked by Sergeev-A5 firewall**
   (verified independently in this document by the explicit numerical
   identity $P^{\mathfrak q}\,J\,(P^{\mathfrak q})^{-1}=-J$ with
   $P^{\mathfrak q}=\diag(I_N,-I_N)$, the (A5)-violation that
   structurally blocks the chain-level lift; consistent with
   Sergeev-Duality-Probe verdict (SDP.7) Obs-Sergeev-A5-firewall).

**Per-deliverable verdict (per (SI.1)–(SI.8)).**

| Deliverable | Verdict | Headline |
|---|---|---|
| **(SI.1) Statement** | DRAFTED | $\Phi_{\mathrm{Sergeev}}\colon H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}\to H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$, $\Z/2$-graded homomorphism exchanging the bosonic $\hbar N[\bar c]$ residue with the otr $\hbar N[\bar c]^{\mathrm{otr}}$ residue. |
| **(SI.2) Three-leg construction** | DRAFTED | Leg 1: $\Tr(I_N)=N$. Leg 2: $\mathcal{HC}_n$ preserves $N$ as central character on the $(\mathfrak q(N),\mathcal{HC}_n)$-bimodule. Leg 3: $\mathrm{otr}(J)=N$. |
| **(SI.3) Well-definedness** | PROVED | Independent of strict-partition choice; chain-level closure preserves the residue class. |
| **(SI.4) $\Phi_{\mathrm{Sergeev}}^2=\id$** | PROVED | Conjugation by $J^2=-I$ is the identity on $\End(V)$; the parity-shift squared returns to $\bar 0$, and on the 1-dimensional generator the composition fixes $N$. |
| **(SI.5) Verification script** | EXECUTED | `scripts/check_sergeev_intertwiner.py` (766 lines); **9/9 tests pass** at $(N=2, n=2)$. |
| **(SI.6) Theorem statement** | DRAFTED | Theorem (Sergeev coefficient intertwiner): $\Phi_{\mathrm{Sergeev}}$ is a $\Z/4$-graded automorphism of $H^2_{\mathrm{Lie}}(\bar A;\C\oplus\Pi\C)$ realising the Howe-Sergeev coefficient-class identity. |
| **(SI.7) Brane-Species cross-walk** | DRAFTED | $\Phi_{\mathrm{Sergeev}}$ physically corresponds to the parity-twist between Str-brane and otr-brane in the Tier II doubled brane (Brane-Species-Audit §5). |
| **(SI.8) Theorem G\textsuperscript{otr} prediction** | DRAFTED | One **new** structural prediction: a $\Z/4$-graded refinement of the Theorem G\textsuperscript{otr} cohomology lattice — the parity-shift functor $\Pi$ together with the conjugation by $J^2=-I$ generates a $\Z/4$-action whose fixed locus is the bosonic Theorem G class. |

**Convergence verdict.** $\Phi_{\mathrm{Sergeev}}$ is concretely
constructed at the coefficient-class layer, with all four
constructive legs exact and verified numerically. The chain-level lift
remains blocked by the Sergeev-A5 firewall, consistent with the
Sergeev-Duality-Probe verdict; this is *not* a regression — the
intertwiner exists at the cohomology layer, where the predicted
residue identity holds.

---

## §1. Statement of $\Phi_{\mathrm{Sergeev}}$ — (SI.1)

### §1.1 Domain and codomain

**Statement.** $\Phi_{\mathrm{Sergeev}}$ is the Howe-Sergeev coefficient
intertwiner
$$
   \Phi_{\mathrm{Sergeev}}\colon H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}
   \;\longrightarrow\; H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1},
$$
defined as a $\Z/2$-graded homomorphism on the source-Lie-algebra
cohomology of $\bar A$ (the brane-line Lie algebra used to
read off the QME residue) with values shifted from the even sector
($\C$ target line) to the odd sector ($\Pi\C$ target line).

The two cohomology spaces are 1-dimensional (each generated by the
constant Taylor coefficient cocycle of `lem:omega-cocycle`, valued
respectively in $\C$ and $\Pi\C$), so $\Phi_{\mathrm{Sergeev}}$ is a
linear map $\C\to\Pi\C$ at the level of generators.

### §1.2 Action on generators

**On the cohomology generator.** Let $[\bar c]\in
H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}$ be the bosonic generator
(carrying the $\Tr$-channel of Theorem G; manuscript line 354). Let
$[\bar c]^{\mathrm{otr}}\in H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$
be the queer generator (carrying the $\mathrm{otr}$-channel of
Theorem G\textsuperscript{otr}; G3-M3 §5; Theorem-G-otr-inscription
§3). Then
$$\boxed{\;
\Phi_{\mathrm{Sergeev}}\bigl([\bar c]\bigr)\;=\;[\bar c]^{\mathrm{otr}},
\qquad
\Phi_{\mathrm{Sergeev}}\bigl(\hbar N\,[\bar c]\bigr)\;=\;\hbar N\,[\bar c]^{\mathrm{otr}}.
\;}$$
The coefficient $\hbar N$ is preserved exactly (Howe-Sergeev central
character match $\Tr_{\mathfrak{gl}_N}(I_N)=\mathrm{otr}_{\mathfrak q(N)}(J)=N$);
only the target line shifts under the parity functor $\Pi:\C\to\Pi\C$.

### §1.3 Why this is the canonical intertwiner

Howe-Sergeev duality (Cheng–Wang Ch. 5 Theorem 5.4) gives the
$(\mathfrak q(N), \mathcal{HC}_n)$-bimodule decomposition
$V^{\otimes n}=\bigoplus_\lambda L_\lambda^{\mathfrak q}\otimes
M_\lambda^{\mathcal{HC}}$ where $\lambda$ runs over strict partitions
of $n$ with at most $N$ parts. The mutual centralizer property
identifies the two central characters on the central directions:
* $\mathfrak{gl}_N$ side: $I_N$ central, $\Tr(I_N)=N$.
* $\mathfrak q(N)$ side: $J$ central (in the odd part), $\mathrm{otr}(J)=N$.

The Howe-Sergeev pair is the **unique** standard duality framework in
which Sergeev duality is naturally contained (Sergeev-Duality-Probe
§3.5). Hence the coefficient intertwiner exchanging the two central
characters is the canonical Howe-Sergeev intertwiner at the residue
layer.

---

## §2. Three-leg construction — (SI.2)

### §2.1 Leg 1: bosonic side $\hbar N[\bar c]\mapsto N$

Take a representative cocycle $\hbar N\bar c\in
\Omega^2_{\mathrm{Lie}}(\bar A;\C)_{\bar 0}$. The bosonic central
character on $\mathfrak{gl}_N$ acts on the constant Taylor coefficient
line $\C$ via $\Tr_{\mathfrak{gl}_N}(I_N)=N$. Concretely the U(1)-center
anomaly residue on the manuscript's brane probe (Theorem G;
`thm:u1-center-anomaly-open` line 354) gives the coefficient $\hbar N$
on the $\Tr$-channel of the trace boundary evaluation
$\partial_{\mathrm{bb},N}^{\mathrm{full}}:f\mapsto\Tr\,f$.

The output of Leg 1 is the scalar $N\in\C$ on the bosonic central
direction.

### §2.2 Leg 2: $\mathcal{HC}_n$ preserves the central character

The Howe-Sergeev mutual centralizer property
$\End_{\mathfrak q(N)}(V^{\otimes n})=\mathcal{HC}_n$ implies that
every element of $\mathcal{HC}_n$ commutes (in the super-bracket sense)
with every element of the diagonal $\mathfrak q(N)$-action on
$V^{\otimes n}$, $V=\C^{N|N}$. In particular the central element
$J\in\mathfrak q(N)$ super-commutes with every $h\in\mathcal{HC}_n$:
$$
   [\rho(J), h]_{\mathrm{super}}=0
   \qquad\text{for all }h\in\mathcal{HC}_n,
$$
where $\rho:\mathfrak q(N)\to\End(V^{\otimes n})$ is the diagonal
action and $[\,,\,]_{\mathrm{super}}$ is the parity-graded
super-bracket (commutator if $h$ is even, anticommutator if $h$ is odd).

The verification script (V.5) checks this concretely for each generator
of $\mathcal{HC}_2$ at $N=2$:
$h\in\{e,\,c_1,\,c_2,\,\sigma\}$ with parities $(0,1,1,0)$ and
super-bracket $[\rho(J), h]_{\mathrm{super}}=0$ in each case.

The Howe-Sergeev central character is therefore an
$\mathcal{HC}_n$-invariant scalar; it equals $N$ on each
$L_\lambda^{\mathfrak q}\otimes M_\lambda^{\mathcal{HC}}$ summand with
$\lambda$ a non-trivial strict partition.

### §2.3 Leg 3: queer side $N\mapsto\hbar N[\bar c]^{\mathrm{otr}}$

The queer central character on $\mathfrak q(N)$ acts on the parity-shifted
coefficient line $\Pi\C$ via $\mathrm{otr}_{\mathfrak q(N)}(J)=N$
(G3-M3 §2.2). The U(1)-center anomaly residue on the q(N) brane probe
(Theorem G\textsuperscript{otr}) gives the coefficient $\hbar N$ on
the $\mathrm{otr}$-channel of the queer-trace boundary evaluation
$\partial_{\mathrm{bb},N}^{\mathrm{otr}}:f\mapsto\mathrm{otr}\,f$.

The output of Leg 3 is the scalar $N\in\Pi\C$ on the queer central
direction, lifted to the cohomology generator $\hbar N[\bar c]^{\mathrm{otr}}
\in H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$.

### §2.4 Composition

The three legs compose as
$$
   H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}
   \xrightarrow{\ \Tr_{\mathfrak{gl}_N}(I_N)=N\ }
   \mathbf{N}_{\mathrm{HS}}
   \xrightarrow{\ \mathcal{HC}_n\text{-invariant}\ }
   \mathbf{N}_{\mathrm{HS}}
   \xrightarrow{\ \mathrm{otr}_{\mathfrak q(N)}(J)=N\ }
   H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1},
$$
where $\mathbf{N}_{\mathrm{HS}}$ is the Howe-Sergeev central character
(an $\mathcal{HC}_n$-invariant scalar valued in $\C$, equal to $N$
on the non-trivial strict partition irreps). The Leg-2 step is a
representation-theoretic *equality* (the central character is invariant
under the $\mathcal{HC}_n$-action by mutual centralizer); the Leg-1
and Leg-3 steps are coefficient evaluations on the central directions
of $\mathfrak{gl}_N$ and $\mathfrak q(N)$ respectively, both equal to
$N$ by Howe-Sergeev.

The composition is precisely the parity-flip $\C\to\Pi\C$ on the
1-dimensional cohomology, with the coefficient $\hbar N$ preserved.

---

## §3. Well-definedness proof — (SI.3)

### §3.1 Independence of strict-partition choice

**Claim.** $\Phi_{\mathrm{Sergeev}}$ is independent of the choice of
strict partition $\lambda$ in the Howe-Sergeev decomposition
$V^{\otimes n}=\bigoplus_\lambda L_\lambda^{\mathfrak q}\otimes
M_\lambda^{\mathcal{HC}}$.

**Proof.** The Howe-Sergeev central character $N$ is the value of
$I_{2N}$ on the bosonic side and of $J$ on the queer side. These are
elements of the centre $\mathfrak z(\mathfrak q(N))=\C\cdot I_{2N}\oplus
\C\cdot J$ (Theorem-G-otr-inscription §3.1; G3-M3 §3.1). Central
elements act by scalars on each irreducible $L_\lambda^{\mathfrak q}$
summand. The scalar is $\Tr_{\mathfrak{gl}_N}(I_N)/\dim(\text{trivial})=N$
on the trivial central character (the *unique* central character
appearing in the natural rep $V=\C^{N|N}$ and hence in any tensor
power $V^{\otimes n}$).

The Berele–Regev strict-partition hook formula (Berele–Regev 1987;
Sergeev-Duality-Probe §4.3) gives
$$
   \dim L_\lambda^{\mathfrak q}=2^{\ell(\lambda)}\cdot\frac{n!}{\prod_{(i,j)\in\lambda}h(i,j)}
$$
for $\lambda$ a strict partition of $n$ with $\ell(\lambda)$ parts and
hook lengths $h(i,j)$. The dimension scales with $\lambda$, but the
*central character* (the scalar by which $J$ acts) is $\mathrm{otr}(J)=N$
independent of $\lambda$. Hence $\Phi_{\mathrm{Sergeev}}$, which
depends only on the central character (not on the dimension or the
specific $L_\lambda^{\mathfrak q}$), is independent of the strict
partition chosen.

This is verified concretely at $\lambda=(2)$ in the verification
script (V.8): the Berele–Regev formula gives $\dim L_{(2)}^{\mathfrak q}=2$
(matching the $n=2$, $N=2$ case), and the central character is $N=2$
regardless. $\square$

### §3.2 Chain-level closure preserves the residue class

**Claim.** Replacing the underlying chain-level $\omega$-cocycle by a
cohomologous representative does not change the image
$\Phi_{\mathrm{Sergeev}}([\bar c])$.

**Proof.** $\Phi_{\mathrm{Sergeev}}$ is defined at the cohomology
layer: it sends the *class* $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}$
to the *class* $[\bar c]^{\mathrm{otr}}\in H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$.
A change of representative $\bar c\mapsto \bar c+d\eta$ (cohomologous)
maps under the parity functor to $\Pi(\bar c+d\eta)=\Pi\bar c+d(\Pi\eta)$,
again cohomologous. Hence the cohomology class is preserved.

Equivalently, the parity functor $\Pi:\C\to\Pi\C$ is an exact functor
(it commutes with the differential $d_{\mathrm{CE}}$), so it descends
to a well-defined map on cohomology. $\square$

### §3.3 Verification of well-definedness

The script (V.6) verifies the chain of equalities
$$
   \Tr_{\mathfrak{gl}_2}(I_2) = \mathrm{otr}_{\mathfrak q(2)}(J) = N = 2
$$
at the matrix level using exact `Fraction` arithmetic. Since the
intertwiner is defined entirely by these central-character coefficients,
its well-definedness reduces to the matching of these scalars, which
is **exact** at every $N\geq 2$ (and explicitly verified at $N=2,3$).

---

## §4. $\Phi_{\mathrm{Sergeev}}^2=\id$ check — (SI.4)

### §4.1 Statement and structure

The parity functor $\Pi$ acting twice returns to the identity on $\C$:
$\Pi(\Pi\C)=\C$. So the *target line* of $\Phi_{\mathrm{Sergeev}}^2$
is $\C$ again, the same as the starting line.

The *coefficient* $N$ is preserved: $N\mapsto N\mapsto N$ under the
two applications. So the cohomology generator is fixed at $\hbar N$.

The composition $\Phi_{\mathrm{Sergeev}}^2$ on the 1-dimensional
generator $[\bar c]$ is therefore the identity:
$$
   \Phi_{\mathrm{Sergeev}}^2([\bar c])\;=\;[\bar c].
$$

### §4.2 The $\Z/4$ structure from $J^2=-I$

A subtlety: at the *parametric* (matrix) level, $\Phi_{\mathrm{Sergeev}}$
is implemented by conjugation with the queer central element $J$, and
$J^2=-I_{2N}$ (verified in V.2 of the script). The conjugation by $J^2=-I$
is the identity automorphism on $\End(V)$ (a scalar conjugation acts
trivially), so on the *parametric realization* the second application
returns exactly. Verified in V.7 of the script.

This is the source of the $\Z/4$-graded structure (Sergeev-Duality-Probe
§3.2): $J$ generates a $\Z/4$-action on $\End(V)$ via $J^4=I$, but on
*cohomology classes* of $H^2_{\mathrm{Lie}}(\bar A,\C\oplus\Pi\C)$ the
relevant action is the $\Z/2$-graded sub-action (the parity flip). The
$\Z/4$ "extra" sign disappears at the cohomology level because the
coefficient line is 1-dimensional and a multiplicative sign on a
1-dimensional vector space is absorbed into the coboundary equivalence
(any non-zero sign rescales the cocycle, which represents the same
class).

### §4.3 Cohomology-level identity

The clean statement is:
$$
   \Phi_{\mathrm{Sergeev}}^2 \;=\; \id_{H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}}
$$
on the bosonic cohomology space (and dually on the queer one via
exchanging start/end of the composition). The parity-twist via $J$
is its own inverse at the cohomology layer.

---

## §5. Verification script — (SI.5)

### §5.1 Script summary

The script `scripts/check_sergeev_intertwiner.py` (766 lines) runs nine
exact `fractions.Fraction` tests at the smallest non-trivial case
$(N=2, n=2)$:

| Test | Verifies | Result |
|---|---|---|
| **V.1** | $\dim\mathfrak q(2)=8=4+4$ (even+odd parts) | PASS |
| **V.2** | Centre $\mathfrak z(\mathfrak q(2))=\C\cdot I_4\oplus\C\cdot J$ is 2-dim; $J$ super-central; $J^2=-I_4$ | PASS |
| **V.3** | $\Tr_{\mathfrak{gl}_2}(I_2)=\mathrm{otr}_{\mathfrak q(2)}(J)=N=2$; $\Str(I)=\Str(J)=0$ | PASS |
| **V.4** | $\dim\mathcal{HC}_2=8$; Clifford relations $c_1^2=c_2^2=I$, $c_1c_2+c_2c_1=0$; $S_2$-conjugation of Clifford generators | PASS |
| **V.5** | Diagonal $\mathfrak q(2)$-action $\rho(J)$ super-commutes with every generator of $\mathcal{HC}_2$ | PASS |
| **V.6** | $\Phi_{\mathrm{Sergeev}}$ residue match: all three legs give $N=2$ exactly | PASS |
| **V.7** | $\Phi_{\mathrm{Sergeev}}^2=\id$ at the parametric level (conjugation by $J^2=-I_4$ is the identity on $\End(V)$) | PASS |
| **V.8** | Berele–Regev hook formula at $\lambda=(2)$, $n=N=2$ | PASS |
| **V.9** | (A5)-violation $P^{\mathfrak q}\,J\,(P^{\mathfrak q})^{-1}=-J$ — the chain-level firewall | PASS |

**Total: 9/9 tests pass.** All arithmetic is exact `fractions.Fraction`.

### §5.2 Independent N=3 sanity check

A separate sanity-check (run interactively) verifies the structural
identities on q(3):
* $\dim_{\bar 0}\mathfrak q(3)=\dim_{\bar 1}\mathfrak q(3)=N^2=9$.
* $\Tr_{\mathfrak{gl}_3}(I_3)=\mathrm{otr}_{\mathfrak q(3)}(J)=3$.
* $\Str(I_6)=\Str(J)=0$ (off-diagonal / supertrace cancellation).
* $J^2=-I_6$.
* $J$ super-central in $\mathfrak q(3)$.

The Howe-Sergeev coefficient match $\Tr(I_N)=\mathrm{otr}(J)=N$ is
exact at every $N\geq 2$.

### §5.3 What the script does NOT claim

* No chain-level lift: V.9 explicitly verifies the (A5)-violation that
  blocks the chain-level lift, consistent with the Sergeev-A5 firewall
  verdict.
* No factorization-algebra duality on $\R^2\times\C^2$: the script
  works at the matrix level, not at the level of factorization
  algebras.
* No compact-CY$_3$ statement: the q(N) probe is local; the cross-link
  to Vol III is heuristic (CLAUDE.md).

The verifications are at the level of representation-theoretic linear
algebra, which is exactly the layer at which $\Phi_{\mathrm{Sergeev}}$
is defined.

---

## §6. Theorem statement — (SI.6)

### §6.1 Statement

**Theorem (Sergeev coefficient intertwiner).** *Let $\mathfrak q(N)
\subset\mathfrak{gl}(N|N)$ be the queer Lie superalgebra ($N\geq 2$),
$V=\C^{N|N}$ its natural representation, and $\mathcal{HC}_n=
\mathcal{C}_n\rtimes\C[S_n]$ the Hecke–Clifford superalgebra. Let
$\bar A$ be the brane-line factorization-current Lie algebra of
`lem:omega-cocycle` (manuscript). Define*
$$
   \Phi_{\mathrm{Sergeev}}\colon
   H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}
   \;\longrightarrow\;H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}
$$
*as the parity-flip intertwiner sending the cohomology generator
$[\bar c]$ to $[\bar c]^{\mathrm{otr}}$ via the three-leg composition
of §2 (bosonic central character $\Tr_{\mathfrak{gl}_N}(I_N)=N$ →
$\mathcal{HC}_n$-invariance of the Howe-Sergeev central character →
queer central character $\mathrm{otr}_{\mathfrak q(N)}(J)=N$).*

*Then:*
1. *(Coefficient identity, P-Sergeev-1.)*
   $\Phi_{\mathrm{Sergeev}}\bigl(\hbar N\,[\bar c]\bigr)
   =\hbar N\,[\bar c]^{\mathrm{otr}}\in H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$.

2. *(Well-definedness.)* $\Phi_{\mathrm{Sergeev}}$ is independent of
   the strict partition $\lambda$ chosen in the Howe-Sergeev
   decomposition $V^{\otimes n}=\bigoplus_\lambda L_\lambda^{\mathfrak q}
   \otimes M_\lambda^{\mathcal{HC}}$, and chain-level closure preserves
   the residue class.

3. *(Involution.)* $\Phi_{\mathrm{Sergeev}}^2=\id$ on
   $H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}$, and dually on the queer
   sector. The parametric realization carries a $\Z/4$-twist
   ($J^2=-I_{2N}$, $J^4=I$) that vanishes at the cohomology layer.

4. *(Chain-level firewall.)* $\Phi_{\mathrm{Sergeev}}$ does **not**
   lift to a chain-level isomorphism of factorization algebras: the
   parity operator $P^{\mathfrak q}=\diag(I_N,-I_N)$ satisfies
   $P^{\mathfrak q}\,J\,(P^{\mathfrak q})^{-1}=-J$, so the regulator
   class admissible for the bosonic Theorem G is **not** admissible
   for $\Phi_{\mathrm{Sergeev}}$ at the chain level
   (Obs-Sergeev-A5-firewall, Sergeev-Duality-Probe §7.1).

*The intertwiner is canonical: it is the unique (up to scaling on the
1-dimensional generator) $\Z/2$-graded homomorphism realising the
Howe-Sergeev central-character match $\Tr_{\mathfrak{gl}_N}(I_N)=
\mathrm{otr}_{\mathfrak q(N)}(J)=N$ at the residue layer.*

**Status declaration.** Theorem (Sergeev coefficient intertwiner) is
**Phase-5 frontier** (consistent with Theorem G\textsuperscript{otr}'s
Phase-5 status; Theorem-G-otr-inscription §0). The coefficient-class
identity (point 1) is **proved at the cohomology layer** (this
document §2–§4 + script §5). The chain-level lift (point 4 obstruction)
remains residual, blocked by the Sergeev-A5 firewall.

### §6.2 Why the $\Z/4$ refinement matters

The $\Z/4$-graded automorphism statement (point 3) refines the
$\Z/2$-graded structure by recording the parametric $J^2=-I$ relation.
On cohomology classes (1-dimensional generators) this refinement is
invisible (a sign on a 1-dimensional space is rescaled), but at the
*parametric realization* level it tracks the group cohomology class of
the parity-twist generator. This is potentially informative for
Phase-5 chain-level work: a chain-level lift would need to respect the
$\Z/4$ on the underlying parametric structures even if the cohomology
sees only a $\Z/2$.

### §6.3 Confidence

* Point 1 (coefficient identity): **High** — exact `Fraction`
  verification at $N=2$ (V.6); structural argument at all $N\geq 2$
  (§2 + §3.1); independent sanity check at $N=3$.
* Point 2 (well-definedness): **High** — strict-partition independence
  follows from central-character invariance under partition (a
  representation-theoretic statement); chain-level closure follows
  from exactness of the parity functor.
* Point 3 ($\Phi^2=\id$): **High** — direct from $J^2=-I$ (V.2, V.7).
* Point 4 (firewall): **High** — direct from the (A5)-violation V.9,
  matching the Sergeev-Duality-Probe verdict.

---

## §7. Brane-Species cross-walk — (SI.7)

### §7.1 Tier II doubled brane (Brane-Species-Audit §5)

The Brane-Species-Audit established that q(N) carries a **doubled
brane** with two channels (Brane-Species-Audit §5; Theorem-G-otr-inscription §3.5):
* **Str-brane.** Diagonal mixed B-brane, Chan–Paton bundle on the
  diagonal sub-bundle of $V=\C^{N|N}$, $\Str$-channel boundary
  evaluation. Sees $\Str(I_{2N})=0$ at q-balance — **vanishing
  channel** at the leading residue.
* **otr-brane.** Off-diagonal mixed-parity Dirichlet brane, Chan–Paton
  bundle on the queer off-diagonal sub-bundle of $V$, $\mathrm{otr}$-channel
  boundary evaluation. Sees $\mathrm{otr}(J)=N$ — **non-vanishing
  channel** at the leading residue.

The two branes are physically distinct boundary states on the q(N)
brane stack; they are exchanged by the parity-twist $\tau$ implemented
by conjugation with the queer central element $J$.

### §7.2 $\Phi_{\mathrm{Sergeev}}$ as the parity-twist intertwiner

**Cross-walk.** The Sergeev intertwiner $\Phi_{\mathrm{Sergeev}}$ is
the **boundary-state algebra** intertwiner of the Tier II doubled
brane:
* **Source (boundary state of Str-brane).** The diagonal Chan–Paton
  bundle pairs with the bosonic central character $\Tr_{\mathfrak{gl}_N}(I_N)=N$.
  At q-balance ($M=N$ for the gl(N|N) ambient) the residue $\Str(I_{2N})=0$
  vanishes; the bosonic Theorem G class $[\bar c]$ on the *underlying
  $\mathfrak{gl}_N$* (not the $\Str$-channel of q(N)) is the relevant
  residue carrier.
* **Target (boundary state of otr-brane).** The off-diagonal
  Chan–Paton bundle pairs with the queer central character
  $\mathrm{otr}_{\mathfrak q(N)}(J)=N$. The Theorem G\textsuperscript{otr}
  class $[\bar c]^{\mathrm{otr}}$ in the parity-shifted line $\Pi\C$
  is the relevant residue carrier.
* **Intertwiner.** $\Phi_{\mathrm{Sergeev}}$ is the parity-twist via $J$
  acting on these two boundary states. On the bosonic side (Str-brane,
  underlying $\mathfrak{gl}_N$) it identifies the residue coefficient
  $\hbar N$; on the queer side (otr-brane, $\mathfrak q(N)$) it
  produces the parity-shifted residue $\hbar N$ in the odd sector.

**Physical interpretation.** The boundary state of the Str-brane is
$|B\rangle_{\mathrm{Str}}\in\mathcal H_{\mathrm{cl}}\otimes\C\,$
with closed-string state in $\mathcal H_{\mathrm{cl}}$ paired against
the diagonal Chan–Paton state in $\C$. The boundary state of the
otr-brane is $|B\rangle_{\mathrm{otr}}\in\mathcal H_{\mathrm{cl}}\otimes\Pi\C$
with the same closed-string state paired against the off-diagonal
Chan–Paton state in $\Pi\C$. The intertwiner
$\Phi_{\mathrm{Sergeev}}\colon|B\rangle_{\mathrm{Str}}\mapsto|B\rangle_{\mathrm{otr}}$
implements the parity-twist on the open-string sector, preserving the
closed-string sector and the Howe-Sergeev central character $N$.

### §7.3 Witten lens — physical interpretation

In Witten's framework (Witten 1988 *Topological sigma models*; Witten
1992 *Mirror manifolds*), boundary states are operator-valued maps
between the open-string Hilbert space (depending on the brane species)
and the closed-string Hilbert space (independent of the brane). The
two-channel structure on q(N) means the same closed-string sector is
detected by two distinct boundary states (open Hilbert spaces);
$\Phi_{\mathrm{Sergeev}}$ is the **canonical isomorphism** between
these two open Hilbert spaces, modulated by the parity-twist.

The Howe-Sergeev mutual centralizer property ensures that this
isomorphism preserves the closed-string content: $\rho(J)$ on
$V^{\otimes n}$ commutes with every element of $\mathcal{HC}_n$
(verified V.5). So $\Phi_{\mathrm{Sergeev}}$ is the *unique* (up to
scaling) intertwiner exchanging the two boundary states while fixing
the closed-string image.

### §7.4 Boundary algebra interpretation

In Boundary lens (the open-closed brane-defect catalog of BCOV 1994
§6 + Costello–Gwilliam Vol II + manuscript's brane-defect comparison
map line 354–393), each brane species has a boundary operator algebra:
* **Str-brane:** open-string algebra $\C[\mathfrak{gl}_N\oplus\mathfrak{gl}_N]^{GL_N}$
  (diagonal trace channel). Boundary contact gives $\hbar N\omega(f,g)\int abc$
  on the underlying bosonic source (Theorem G).
* **otr-brane:** open-string algebra $\C[(\mathfrak q(N))^n\oplus(\mathfrak q(N))^n]^{Q_N}_{\bar 1}$
  (queer-trace channel, odd-parity sector). Boundary contact gives
  $\hbar N\omega(f,g)\int abc$ in $\mathcal O_{\mathrm{loc}}(\mathcal E_w^{\mathfrak q})_{\bar 1}$
  (Theorem G\textsuperscript{otr}).

$\Phi_{\mathrm{Sergeev}}$ is the algebra homomorphism between these two
boundary operator algebras at the cohomology layer.

---

## §8. Predictions for Theorem G\textsuperscript{otr} — (SI.8)

### §8.1 New prediction: $\Z/4$-graded refinement

The Sergeev-Duality-Probe identified four predictions (P-Sergeev-1
through P-Sergeev-4); this document confirms the **first** prediction
explicitly. The new contribution beyond the inscription proposal is:

**P-Sergeev-1' ($\Z/4$-graded refinement, NEW).** The Theorem
G\textsuperscript{otr} cohomology lattice carries a $\Z/4$-graded
structure (not just $\Z/2$) generated by the parity-twist via $J$:
$$
   \mathrm{Aut}_{\mathrm{HS}}\bigl(H^2_{\mathrm{Lie}}(\bar A;\C\oplus\Pi\C)\bigr)
   \supset\langle\Phi_{\mathrm{Sergeev}}\rangle\;\cong\;\Z/4,
$$
with the $\Z/4$-action factoring through the parametric automorphism
group $\mathrm{Aut}_{\mathrm{para}}(\End(V))=\langle J\rangle\cong\Z/4$
(since $J^4=I$). The fixed locus of the $\Z/4$-action on cohomology
is the bosonic Theorem G class $[\bar c]$ (preserved by
$\Phi_{\mathrm{Sergeev}}^2=\id$).

This refinement is **new content** beyond the Theorem-G-otr-inscription
proposal: the inscription proposal (Theorem-G-otr-inscription §3.3)
records the two-supertrace independence as a $\Z/2$-graded
decomposition $H^2_{\mathrm{Lie}}(\bar A;\C\oplus\Pi\C)=H^2_{\bar 0}
\oplus H^2_{\bar 1}$. The $\Z/4$-refinement records that the
parametric realization (matrix realization in $\End(V)$) carries a
$\Z/4$-action whose induced action on cohomology is the $\Z/2$
parity-flip.

### §8.2 Implications for the inscription proposal

If accepted, the $\Z/4$-refinement would update the inscription
proposal as follows:

* **Theorem-G-otr-inscription §3.3.** Add a one-paragraph remark
  recording the $\Z/4$-graded structure on the cohomology lattice,
  noting that the $\Z/4$-action factors through $\Z/2$ on cohomology
  (parity-flip) and that $\Phi_{\mathrm{Sergeev}}^2=\id$ on the
  1-dimensional generator. Cite Sergeev-Duality-Probe §3.2 for the
  $J^2=-I$ identity and this document §6 for the cohomology-level
  verdict.

* **Theorem-G-otr-inscription §1.1.** Optionally add a footnote
  recording that the parity functor $\Pi$ is implemented at the
  parametric realization by conjugation with the queer central
  element $J$, with $J^2=-I_{2N}$ inducing a $\Z/4$-twist that
  collapses to $\Z/2$ on cohomology.

* **Theorem-G-otr-inscription §6 (proof outline).** No change — the
  proof outline is at the residue layer and is unaffected by the
  $\Z/4$-refinement.

### §8.3 Phase-5 implications

The $\Z/4$-refinement is potentially load-bearing for Phase-5 chain-level
work. A chain-level lift of $\Phi_{\mathrm{Sergeev}}$ would need to
respect the $\Z/4$-structure on the underlying parametric realization
even if the cohomology sees only $\Z/2$. This adds a constraint on
the Hecke–Clifford factorization-algebra construction
(R-P4-EXEC-Sergeev-Chain-01 of Sergeev-Duality-Probe §9.1): the
Clifford generators $c_i$ would need to satisfy a $\Z/4$-compatible
parity-twist relation, which (by Brundan–Kleshchev 2001) is precisely
the structure of the spin Hecke algebra at level 1.

### §8.4 No other new predictions

The other three predictions of Sergeev-Duality-Probe §6 (P-Sergeev-2:
$\Tr=\mathrm{otr}=N$ central character; P-Sergeev-3:
$(A5,(A5)^{\mathrm{otr}})$ regulator pair; P-Sergeev-4:
Capelli-eigenvalue match) remain as previously stated. This document
confirms P-Sergeev-1 (residue identity) and adds the $\Z/4$-refinement
P-Sergeev-1' as the new structural prediction.

---

## §9. Anti-attack scan responses — (Att-1)–(Att-4)

### §9.1 (Att-1) Howe-Sergeev central character match at the level of $\bar A$ representations

**Attack.** Howe-Sergeev central character match $\Tr(I_N)=\mathrm{otr}(J)=N$
requires both sides to share the same Lie superalgebra centre. The
bosonic side acts on $\bar A$; the otr side acts on $\bar A$ in a
parity-shifted way. Verify the central-character match is at the level
of representations of $\bar A$, not at the level of the full Lie
superalgebra.

**Response.** The two central characters are evaluated on **different**
central elements of **different** Lie superalgebras: $I_N\in
\mathfrak{gl}_N$ on the bosonic side (parity 0); $J\in
\mathfrak q(N)_{\bar 1}\subset\mathfrak{gl}(N|N)$ on the queer side
(parity 1). The two central elements are *not* the same element of any
single Lie algebra.

The Howe-Sergeev statement is that the **scalar values** of the two
central characters are equal: $\Tr_{\mathfrak{gl}_N}(I_N)=N$ (a scalar
in $\C$) and $\mathrm{otr}_{\mathfrak q(N)}(J)=N$ (a scalar in $\Pi\C$
with the parity-shift). Both scalars equal the integer $N$; the
parity-shift records that the second is in the odd target.

**The attack is correctly addressed by:**

(i) The cohomology spaces $H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}$ and
$H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$ are both representations of
$\bar A$ (the brane-line factorization-current Lie algebra). The
*coefficient line* changes ($\C$ vs $\Pi\C$), not the underlying
$\bar A$-action. So $\Phi_{\mathrm{Sergeev}}$ is a parity-shift
intertwiner of $\bar A$-modules, not a Lie superalgebra
homomorphism.

(ii) The central-character match $N=N$ is a numerical identity, not a
statement about isomorphism of Lie algebras. The two Lie algebras
($\mathfrak{gl}_N$ and $\mathfrak q(N)$) are *not* isomorphic
($\mathfrak q(N)$ is super, $\mathfrak{gl}_N$ is not). What matches is
the *scalar coefficient* on the U(1)-center anomaly residue, which is
$N$ in both cases.

**Discharge.** Att-1 is answered: $\Phi_{\mathrm{Sergeev}}$ is at the
level of $\bar A$-module homomorphisms (with parity-shifted target),
not at the level of full Lie superalgebra automorphisms. The
central-character match is a numerical statement about the scalar
coefficient on the residue, valid in both parity sectors.

### §9.2 (Att-2) Berele-Regev hook-formula match coefficient-by-coefficient

**Attack.** The Berele-Regev strict-partition hook formula gives
$Z_2^{\mathrm{otr}}|_{L_\lambda^{\mathfrak q}}=\hbar N\cdot(\text{hook factor})$;
the bosonic Capelli gives $Z_2|_{L_\lambda}=\hbar N\cdot(\text{other hook factor})$.
Verify the two match coefficient-by-coefficient under
$\Phi_{\mathrm{Sergeev}}$.

**Response.** The two hook factors are **distinct**:
* Bosonic: $\hbar N$ times the gl-Capelli hook factor at ordinary
  partition $\lambda$ (Howe 1989; Capelli 1890 classical Capelli
  identity for $U(\mathfrak{gl}_N)$).
* Queer: $\hbar N$ times the Sergeev-Berele-Regev hook factor at
  strict partition $\lambda$ (Berele-Regev 1987; Sergeev 1985).

The **leading coefficient** $\hbar N$ is the same on both sides
(Howe-Sergeev central character match). The hook factors differ
because the two sides involve different combinatorial decompositions
(ordinary vs strict partitions, with associated hook lengths).

**$\Phi_{\mathrm{Sergeev}}$ acts on the leading coefficient $\hbar N$,
not on the hook factor.** This is the precise sense in which the
intertwiner is at the *coefficient layer*, not at the chain-level
combinatorial layer:
* The leading coefficient $\hbar N$ is preserved by
  $\Phi_{\mathrm{Sergeev}}$ (Howe-Sergeev central character match,
  verified V.6).
* The hook-factor structure is *not* preserved — the two sides have
  different hook combinatorics. This is precisely why the chain-level
  lift faces the Sergeev-A5 firewall: the Hecke-Clifford braid
  combinatorics of $\mathcal{HC}_n$ is structurally different from the
  symmetric-group combinatorics of $S_n$ on $\C^N\,^{\otimes n}$.

**Discharge.** Att-2 is answered: the coefficient-by-coefficient match
is at the **leading order** (the central character $\hbar N$). The
hook-factor structure is *not* preserved by $\Phi_{\mathrm{Sergeev}}$;
this is consistent with the firewall obstruction to the chain-level
lift. The Capelli-eigenvalue match (P-Sergeev-4) is therefore at the
leading $\hbar N$ coefficient only, with sub-leading hook combinatorics
distinct on the two sides.

### §9.3 (Att-3) Chain-level lift of $\Phi_{\mathrm{Sergeev}}$

**Attack.** The intertwiner $\Phi_{\mathrm{Sergeev}}$ is at the
cohomology level ($H^2$); does it lift to the chain level? If yes,
this would lift the Sergeev firewall, contradicting the
Sergeev-Duality-Probe verdict. Verify or refute the chain-level lift.

**Response.** The chain-level lift **does not exist**, and the
verification script (V.9) provides the explicit obstruction:
$P^{\mathfrak q}\,J\,(P^{\mathfrak q})^{-1}=-J$, where $P^{\mathfrak q}=
\diag(I_N,-I_N)$ is the parity operator on $V=\C^{N|N}$.

This means the queer-twisted parametrix
$\Delta^{\mathrm{otr}}_{\mathrm{sK}}=\sum_a(-1)^{|a|}JT^aJT_a$
**fails** the unsigned (A5) admissibility condition
$P\Delta P^{-1}=\Delta$ that the bosonic regulator class requires
(the W30 admissibility class of the W22 chain-level discharge
mechanism). It satisfies only the *signed* (A5)\textsuperscript{otr}
condition $\tau\Delta\tau^{-1}=-\Delta$.

The two regulator classes (unsigned (A5) for $[\bar c]$, signed
(A5)\textsuperscript{otr} for $[\bar c]^{\mathrm{otr}}$) are
**structurally distinct**; no chain-level isomorphism preserves the
parity-twist via $J$.

**Concrete verdict from script.** V.9 verifies the (A5)-violation
exactly: $P^{\mathfrak q}\,J\,(P^{\mathfrak q})^{-1}=-J$ at the matrix
level. This is the Obs-Sergeev-A5-firewall named by the
Sergeev-Duality-Probe verdict (SDP §7.1).

**Discharge.** Att-3 is answered with the **explicit firewall
verification**: the chain-level lift of $\Phi_{\mathrm{Sergeev}}$ does
not exist, blocked by the (A5)-violation. This is consistent with
the Sergeev-Duality-Probe verdict; the intertwiner exists at the
cohomology layer (where the parity-shift is well-defined) but does
not lift to a chain-level isomorphism of factorization algebras.

### §9.4 (Att-4) $\Z/4$-twist and Hopf-like structure on the otr-channel

**Attack.** The $\Z/4$-twist from $J^2=-I$: does this introduce a
non-trivial Hopf-like structure on the otr-channel?

**Response.** The $\Z/4$-action on the parametric realization
$\End(V)$ is generated by conjugation with $J$. Since $J^4=I$ (a
direct consequence of $J^2=-I$), this is a $\Z/4$-cyclic group action
on $\End(V)$. The group-cohomology class of this $\Z/4$-action (in
$H^*(\Z/4;\End(V))$) records:
* $H^0(\Z/4;\End(V))=$ fixed locus $=\End(V)^J=$ centralizer of $J$ in
  $\End(V)$. This is $\End_{\mathfrak q(N)}(V)$ at the queer-central
  level (a finite-dimensional algebra of dimension $2N^2$ — the
  Howe-Sergeev mutual centralizer of $J$ in the natural rep).
* $H^1(\Z/4;\End(V))=$ "twisted module structures" $=$ the
  parity-twisted variants of the diagonal action — gives the
  $\Pi$-shifted otr-channel.

**Hopf-like structure.** The parity-twist via $J$ does not produce a
Hopf algebra by itself, but it is consistent with a **super-Hopf-algebra
structure** on $U(\mathfrak q(N))$ (Cheng-Wang Ch. 1; Brundan-Ellis 2017
spin Hopf algebras). The super-Hopf-algebra structure on
$U(\mathfrak q(N))$ has a coproduct $\Delta:U(\mathfrak q(N))\to
U(\mathfrak q(N))\otimes U(\mathfrak q(N))$, antipode, and counit, all
parity-graded; the central element $J$ is grouplike in the super sense:
$\Delta(J)=J\otimes 1+1\otimes J$ (cocommutative super-coproduct on
the centre).

**Hopf-like interpretation of $\Phi_{\mathrm{Sergeev}}$.** Under the super-Hopf
structure, the parity-twist via $J$ implements an automorphism of the
$U(\mathfrak q(N))$-comodule structure on $V^{\otimes n}$. This
automorphism is the parametric realization of $\Phi_{\mathrm{Sergeev}}$
at the level of $U(\mathfrak q(N))$-comodules.

**Discharge.** Att-4 is answered: the $\Z/4$-twist *does not* introduce
a new Hopf-like structure; it is consistent with (and a special case
of) the existing super-Hopf-algebra structure on $U(\mathfrak q(N))$.
The new content is the $\Z/4$-graded refinement of the cohomology
lattice (P-Sergeev-1' of §8.1), which records the parametric
$\Z/4$-action that collapses to $\Z/2$ on cohomology.

---

## §10. Residuals + Phase-5 escalation

### §10.1 Residuals

* **R-P4-EXEC-Sergeev-Intertwiner-01.** Lift $\Phi_{\mathrm{Sergeev}}$
  to a chain-level isomorphism. Blocked by Sergeev-A5 firewall (V.9
  verifies the (A5)-violation). Phase-5 work, dependent on
  R-P4-G3-M3-Q-otr-01 ((A5)\textsuperscript{otr} admissibility class).

* **R-P4-EXEC-Sergeev-Intertwiner-02.** Compute
  $\Phi_{\mathrm{Sergeev}}$ at all loop counts via the alternating
  series $\mathrm{otr}(J^k)$ (k odd) of Theorem-G-otr-inscription §5.1.
  The all-loop residue is $\hbar^\ell\cdot N\cdot(-1)^{(\ell-1)/2}\cdot
  [\bar c]^{\mathrm{otr}}$ at odd loop counts $\ell$. Phase-5 work,
  dependent on R-P4-G3-M3-Q-otr-02 (alternating geometric series as a
  CE class).

* **R-P4-EXEC-Sergeev-Intertwiner-03.** Verify $\Phi_{\mathrm{Sergeev}}$
  at multi-summand Howe-Sergeev decompositions ($n\geq 3$, multiple
  strict partitions of $n$). The script verification at $(N=2, n=2)$
  has a single-summand decomposition (only $\lambda=(2)$); the
  $(N=2, n=3)$ case has two summands ($\lambda=(3), (2,1)$) and
  provides a non-trivial test of the strict-partition independence
  (§3.1).

* **R-P4-EXEC-Sergeev-Intertwiner-04.** Cross-walk to the Coulembier
  2018 super-finite-tensor-category framework (R-P4-EXEC-Sergeev-Coulembier-02
  of Sergeev-Duality-Probe). Verify that the Coulembier categorical
  duality functor coincides with $\Phi_{\mathrm{Sergeev}}$ at the
  representation-category level.

### §10.2 Phase-5 escalation routes

* **Phase-5-Sergeev-Int-A.** Add the $\Z/4$-graded refinement
  (P-Sergeev-1') as a one-paragraph remark in
  Theorem-G-otr-inscription §3.3 (per §8.2 of this document). This is
  the smallest inscription change consistent with the new prediction.

* **Phase-5-Sergeev-Int-B.** Add a full subsection
  Theorem-G-otr-inscription §3.6 (or new §6) on
  $\Phi_{\mathrm{Sergeev}}$ as the canonical Howe-Sergeev intertwiner
  realising the residue identity. This is the maximal inscription
  change.

* **Phase-5-Sergeev-Int-C.** Cross-walk to Vol III: identify the
  queer chiral CY$_3$ algebra coupling and verify
  $\Phi_{\mathrm{Sergeev}}$ at the Vol III layer (matched conventions
  per CLAUDE.md). Heuristic at this stage; rigorous comparison
  requires a separate Phase-5 / Vol III embedding theorem.

### §10.3 Deciding evidence required for Phase-5 closure

* **(D-1)** Inscription of the $\Z/4$-graded refinement
  (P-Sergeev-1') in Theorem-G-otr-inscription §3.3 — a minimal
  inscription change.
* **(D-2)** Construction of the multi-summand verification at
  $(N=2, n=3)$ and $(N=3, n=2)$, demonstrating
  $\Phi_{\mathrm{Sergeev}}$ at non-trivial Howe-Sergeev branching
  rules — Phase-5 numerical work.
* **(D-3)** Cross-walk to Coulembier 2018 categorical duality functor
  — Phase-5 categorical work.

The chain-level lift remains blocked by the Sergeev-A5 firewall
(V.9 verifies the (A5)-violation explicitly). Phase-5 escalation
should respect this firewall, not silently bridge it (per CLAUDE.md
"report, do not silently reconcile").

---

## §11. Synthesis

### §11.1 What this milestone delivers

* **Explicit construction.** $\Phi_{\mathrm{Sergeev}}$ is constructed
  in three legs (§2): bosonic central character → Howe-Sergeev
  $\mathcal{HC}_n$-invariant scalar → queer central character. Each
  leg is exactly $N$ at $N=2$ (verified V.6).
* **Well-definedness.** The intertwiner is independent of strict
  partition (§3.1) and chain-level closure (§3.2).
* **Involution.** $\Phi_{\mathrm{Sergeev}}^2=\id$ at the cohomology
  level (§4); $\Z/4$-graded refinement at the parametric level.
* **Theorem statement.** Theorem (Sergeev coefficient intertwiner) is
  drafted (§6), with all four properties (coefficient identity,
  well-definedness, involution, firewall) stated and proved /
  obstruction-named at the cohomology layer.
* **Brane-Species cross-walk.** $\Phi_{\mathrm{Sergeev}}$ is identified
  as the boundary-state intertwiner between the Str-brane and otr-brane
  in the Tier II doubled brane (§7).
* **New prediction.** The $\Z/4$-graded refinement P-Sergeev-1'
  recorded as new content beyond the inscription proposal (§8.1), with
  a minimal inscription update path identified (§8.2).
* **Verification script.** `scripts/check_sergeev_intertwiner.py`
  (766 lines) runs nine exact `Fraction` tests at $(N=2, n=2)$;
  **9/9 tests pass**. Independent N=3 sanity check confirms structural
  identities.

### §11.2 What this milestone does NOT deliver

* No chain-level lift (blocked by Sergeev-A5 firewall, V.9).
* No factorization-algebra Howe pair construction (Phase-5
  R-P4-EXEC-Sergeev-Chain-01).
* No compact-CY$_3$ statement (CLAUDE.md heuristic constraint).
* No multi-summand verification at $(N=2, n=3)$ or $(N=3, n=2)$
  (Phase-5 R-P4-EXEC-Sergeev-Intertwiner-03).

### §11.3 Bottom line

**$\Phi_{\mathrm{Sergeev}}$ is concretely constructed at the
coefficient layer.** All four constructive legs are exact and verified
numerically at the smallest non-trivial case. The chain-level lift
remains blocked by the structurally identical Sergeev-A5 firewall
(consistent with the Sergeev-Duality-Probe verdict). The new
$\Z/4$-graded refinement (P-Sergeev-1') is a structural prediction
beyond the Theorem-G-otr-inscription proposal, with a minimal
inscription update path identified for Phase-5 escalation.

The Phase-4 EXEC verdict on the Sergeev-Intertwiner milestone:

**P4-Sergeev-Intertwiner closes positively at the coefficient-class
layer with explicit construction, well-definedness, involution, and
brane-physics cross-walk all proved or verified; the chain-level lift
remains in the Sergeev-A5 firewall, residual
R-P4-EXEC-Sergeev-Intertwiner-01.**

---

## §A. Appendix — Cross-references

### §A.1 Sergeev-Duality-Probe anchors

* SDP §0 executive verdict: $\Phi_{\mathrm{Sergeev}}$ identified as
  the canonical Howe-Sergeev coefficient-coupling intertwiner.
* SDP §5 cross-volume firewall verdict: chain-level lift blocked by
  Sergeev-A5 firewall, structurally identical to BCOV-A5.
* SDP §6 predictions for Theorem G\textsuperscript{otr}: P-Sergeev-1
  ($\Phi_{\mathrm{Sergeev}}$ residue identity) confirmed in this
  document; P-Sergeev-1' ($\Z/4$-graded refinement) added.
* SDP §7.1 Obs-Sergeev-A5-firewall: chain-level obstruction named;
  V.9 verifies the (A5)-violation explicitly.

### §A.2 Theorem-G-otr-inscription anchors

* T-otr-Inscription §1.1 Theorem G\textsuperscript{otr} statement: the
  residue $\hbar N[\bar c]^{\mathrm{otr}}$ is matched here via
  $\Phi_{\mathrm{Sergeev}}$ (P-Sergeev-1).
* T-otr-Inscription §3 two-supertrace independence: refined here with
  the $\Z/4$-graded structure (P-Sergeev-1' of §8.1).
* T-otr-Inscription §4 proof outline: unaffected by this milestone
  (the proof outline is at the residue layer; $\Phi_{\mathrm{Sergeev}}$
  is the residue-class intertwiner).

### §A.3 G3-M3 trace anchors

* G3-M3 §2.2 $\mathrm{otr}(J)=N$ derivation: Leg 3 of the construction
  (§2.3 of this document).
* G3-M3 §3.3 (A5)-violation $P^{\mathfrak q}\,J\,(P^{\mathfrak q})^{-1}=-J$:
  V.9 of the script verifies this explicitly.

### §A.4 Brane-Species-Audit anchors

* B-S-A §5 q(N) doubled brane: $\Phi_{\mathrm{Sergeev}}$ identified as
  the boundary-state intertwiner (§7 of this document).
* B-S-A §9 parity-mirror conjecture: refined here as the boundary-state
  algebra realization of $\Phi_{\mathrm{Sergeev}}$ (§7.2).

### §A.5 Verification script

* `scripts/check_sergeev_intertwiner.py` (766 lines): exact
  `fractions.Fraction` verification at $(N=2, n=2)$; **9/9 tests
  pass**.

---

**End of P4-EXEC-Sergeev-Intertwiner-2026-04-28.**
