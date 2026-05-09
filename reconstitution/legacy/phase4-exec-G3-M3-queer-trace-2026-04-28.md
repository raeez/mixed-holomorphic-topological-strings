# Phase 4 Execution / P4-G3-M3 — Queer-trace `otr` chain-level QME discharge mechanism on q(N)

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Witten primary (physical consistency, dualities, anomalies,
two-supertrace structure as open-closed witness, examples on q(2));
Boundary secondary (boundary states, brane-defect comparison, parity
twist of the boundary evaluation).
**Mode.** Phase-4 EXEC. Master ledger schema; ID prefix
`P4-EXEC-G3-M3-`. Proposal-only — no manuscript edits, no commits.
**Posture.** P4-G3-M2 verdict closed q(N) at the *ordinary*-supertrace
layer via the even ad-invariant form $B_0(X,Y)=\Tr(\mathrm{ev}\,XY+
\mathrm{ev}\,YX)/2$. The queer-trace `otr` parallel was deferred to
Phase-5 as the "deeper structural question". This document executes
the chain-level attack-heal loop on `otr`: does it admit a parallel
discharge analogous to W22-T1/T2, or does it produce an **independent**
residue class that the manuscript's Theorem G does not absorb?

**Inputs (full reads).**
* `CLAUDE.md` (full).
* `reconstitution/phase4-exec-classical-super-extension-2026-04-28.md`
  (1247 lines; G3-M2 verdict on psl/p/q/sl(M|N), §3 q(N) full analysis
  lines 550–807).
* `reconstitution/phase4-exec-osp-supertrace-2026-04-28.md` (757 lines;
  P4-G3-T-A1 chain-level template).
* `reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md` (W22-T1
  chain-level one loop, W22-T2 all loops, W22-Obs M-31 deformation
  lines 1–420 read).
* `appendix-unreduced-bv-qme.tex` (full, 179 lines; Proposition with
  `Ob_sc(γ_1; a, f; b, g) = ℏN ω(f,g) ∫ a(t)b(t)γ_1(t) dt`, allowed
  escape routes in `rmk:app-scalar-contact-escape-routes`).
* `main.tex` lines 280–470 (Lemma `lem:omega-cocycle`, Theorems
  `thm:u1-center-anomaly` / `thm:u1-center-anomaly-open`, Theorem
  `thm:quantum-classical-anomaly`, the U(1)-center remark).

**Standard references (cited from memory).**
* Sergeev, A.N. *The centre of the enveloping algebra for the Lie
  superalgebra Q(N)*. Letters Math. Phys. **7** (1983), 177–179.
  **The original `otr` and odd-Casimir definition.**
* Sergeev, A.N. *The tensor algebra of the identity representation as
  a module over $\mathrm{Gl}(n|m)$ and $Q(n)$*. Math. USSR Sbornik
  **51** (1985), 419–427. **Schur–Weyl–Sergeev duality for q(N).**
* Berele, A. and Regev, A. *Hook Young diagrams with applications to
  combinatorics and representations of Lie superalgebras*. Adv. Math.
  **64** (1987), 118–175. **Sergeev–Berele–Regev hook formula.**
* Penkov, I.B. and Serganova, V.V. *Representations of classical Lie
  superalgebras of type I*. Indag. Math. **3** (1992), 419–466.
* Gorelik, M. *The Kac construction of the centre of $U(\lie g)$ for
  Lie superalgebras*. J. Nonlinear Math. Phys. **11** (2004), 325–349.
* Brundan, J. and Kleshchev, A. *Hecke–Clifford superalgebras,
  crystals of type $A_{2\ell}^{(2)}$ and modular branching rules for
  $\widehat{S}_n$*. Represent. Theory **5** (2001), 317–403.
* Cheng, S.-J. and Wang, W. *Dualities and representations of Lie
  superalgebras*. Graduate Studies in Mathematics, Vol. 144, AMS, 2012
  (q(N) Ch. 6.)
* Costello–Gwilliam Vol II Ch. 11 (BV regulators).
* Costello *Renormalization and effective field theory*, Ch. 4 §4.4
  (BV cohomology and obstruction class).

---

## §0. Executive verdict per (M3.1)–(M3.6)

| Sub-question | Verdict | Headline reason |
|---|---|---|
| **(M3.1) Queer-Capelli central element $Z_2^{\mathrm{otr}}\in U(\mathfrak{q}(N))$** | **EXISTS, odd parity** | The Sergeev quadratic odd Casimir $Z_2^{\mathrm{otr}}=\sum_{i,j}T_{ij}T_{ji}^{(\mathrm{odd})}+T_{ji}^{(\mathrm{odd})}T_{ij}$ where $T_{ij}\in\mathfrak{gl}_N\subset\mathfrak{q}(N)_{\bar 0}$ and $T_{ij}^{(\mathrm{odd})}\in\Pi(\mathfrak{gl}_N)\subset\mathfrak{q}(N)_{\bar 1}$. It lies in $Z(U(\mathfrak{q}(N)))_{\bar 1}$ — the *odd* part of the centre. The Capelli analogue of the W22 quadratic element is therefore odd-graded. |
| **(M3.2) $\mathrm{otr}(I_{q(N)})$ vacuous** | **VACUOUS** | The queer identity $I_{q(N)}=\mathrm{diag}(I_N,I_N)$ has $B$-block zero, so $\mathrm{otr}(I)=\Tr(0)=0$. *But* this is not a propagator-loop coefficient: the relevant evaluation on a queer-twisted heat-kernel diagram is $\mathrm{otr}(I_{2N})$ acting via the queer central element $J$, which gives $\mathrm{otr}(J^2)=\mathrm{otr}(-I)=0$ in either sign convention — **but** the *propagator-loop sum* on the queer-twisted kernel is $\mathrm{otr}(J)$, not $\mathrm{otr}(I)$, and that gives $\Tr(I_N)=N$ on the appropriate basis. |
| **(M3.3) Queer-twisted heat kernel survives (A1)–(A5)** | **FAILS at (A5) parity-equivariance** | The naive twist $\Delta^{\mathrm{otr}}_{\mathrm{sK}}=\sum_a(-1)^{|a|}J\cdot T^a\cdot J\cdot T_a$ is **not parity-commuting** with the queer parity operator $P^{\mathfrak{q}}=\diag(\mathbf 1_N,-\mathbf 1_N)$ on the diagonal blocks because $J$ swaps the blocks, anticommuting with $P^{\mathfrak{q}}$. The corrected (signed-parity) heat kernel produces a *different* admissibility class that does **not** reduce to (A5); a new condition (A5')\textsuperscript{otr} replaces (A5). |
| **(M3.4) One-loop QME residue in queer channel** | **NON-TRIVIAL: $\hbar N\,\omega(f,g)$ in odd parity** | The queer-channel propagator-loop on the brane probe contributes $\hbar\cdot\mathrm{otr}(J\cdot I)=\hbar N$ (odd-graded), with the closed-side cocycle $\omega$ unchanged. The chain-level cocycle is $\hbar N\,[\bar c]^{\mathrm{otr}}\in H^1(\mathcal O_{\mathrm{loc}}, Q+\{I_0,-\})_{\bar 1}$, the *odd-shifted* analogue of the bosonic Theorem-G class. **This is non-trivial, but it sits in a different parity sector of the BV cohomology.** |
| **(M3.5) Discharge analogue / failure** | **FAILS at (A5)\textsuperscript{otr}; new obstruction class** | The naive parallel of W22-T2 on `otr` does *not* close: the queer-twisted regulator class violates the unsigned (A5), and even with (A5)\textsuperscript{otr} the propagator-loop coefficient is $\mathrm{otr}(J^k)\neq 0$ generically. The discharge mechanism that worked on $\Str$ does **not** apply to `otr`. The named obstruction is **(Obs-Q-otr-A5)**: the queer central element $J$ anticommutes with the parity operator. |
| **(M3.6) Cross-walk to manuscript Theorem G** | **NEW INDEPENDENT RESIDUE** | The manuscript's Theorem G records a *single* class $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)\cong\C$ via the U(1)-center of $\mathfrak{gl}_N$ with character $\Tr$. On $\mathfrak{q}(N)$, the U(1)-center decomposes as $\C\cdot I\oplus\C\cdot J$ — a **2-dimensional** centre with characters $\Str$ and $\mathrm{otr}$. Theorem G absorbs the $\Str$-component (which is zero at q-balance); it does **not** absorb the `otr`-component, which produces a *new* class $\hbar N\,[\bar c]^{\mathrm{otr}}$ in the odd-parity sector of the BV obstruction complex. This is a Phase-5 structural finding. |

**Convergence verdict.** The queer trace `otr` does **not** admit a
chain-level discharge analogous to W22-T1/T2 on $\mathfrak{gl}(N|N)$.
The structural obstruction is twofold: (i) the queer central element
$J$ anticommutes with the parity operator $P^{\mathfrak{q}}$, breaking
the (A5) parity-equivariance; (ii) the natural evaluation
$\mathrm{otr}(J)=N$ in the appropriate basis is *non-zero*, parallel
to the bosonic $\Tr(I)=N$ on $\mathfrak{gl}_N$. The two-supertrace
structure $(\Str, \mathrm{otr})$ on $\mathfrak{q}(N)$ produces
**independent** residue classes: $\Str$ discharges (G3-M2 verdict);
`otr` does not discharge and produces a new $\hbar N[\bar c]^{\mathrm{otr}}$
class in the odd-parity sector.

**Phase-5 escalation.** P4-EXEC-G3-M3 is **NOT discharged**. Escalate
to Phase-5 with **Obs-Q-otr-A5** as the deciding obstruction:
parity-equivariance of the queer central element. Two routes for
Phase-5:
* **(Phase-5-Q-A)** Replace (A5) with a *signed* parity-equivariance
  $(A5)^{\mathrm{otr}}$ matching the queer parity twist; check whether
  any admissible regulator class satisfies it, and whether the
  propagator-loop coefficient $\mathrm{otr}(J^k)$ vanishes at
  q-balance.
* **(Phase-5-Q-B)** Treat $\mathrm{otr}$ as a *new* anomaly source
  parallel to Theorem G; extend the manuscript's cocycle $[\bar c]$
  to a 2-dimensional class space $[\bar c]\oplus[\bar c]^{\mathrm{otr}}$
  in $H^2_{\mathrm{Lie}}(\bar A,\C\oplus\Pi\C)$, with the q(N)
  brane-probe seeing both. This is the "queer extension of Theorem G"
  and a candidate structural finding for the Vol III frontier.

---

## §1. (M3.1) Queer-Capelli central element $Z_2^{\mathrm{otr}}$

### §1.1 Sergeev's centre of $U(\mathfrak{q}(N))$

Sergeev 1983 *Letters Math. Phys.* (177–179) computed
$Z(U(\mathfrak{q}(N)))$ as a free supercommutative algebra on
generators of two types:
* **Even Casimirs** at *odd* total degrees (1, 3, 5, ...): obtained
  from the projection of the gl Casimirs through the embedding
  $\mathfrak{q}(N)\hookrightarrow\mathfrak{gl}(N|N)$. The lowest is
  $Z_1^{\mathrm{ev}}=\sum_i T_{ii}$ (the trace), even-parity, central.
* **Odd Casimirs** at *even* total degrees (2, 4, ...): the genuinely
  *queer* central elements, obtained by mixing one even and one odd
  generator. The lowest is the **quadratic odd Casimir**
  \[
     Z_2^{\mathrm{otr}}
       =\sum_{i,j=1}^N\bigl(T_{ij}\,T_{ji}^{(\mathrm{odd})}
                          +T_{ji}^{(\mathrm{odd})}\,T_{ij}\bigr),
  \]
  where $T_{ij}\in\mathfrak{gl}_N=\mathfrak{q}(N)_{\bar 0}$ are the
  even matrix units and $T_{ij}^{(\mathrm{odd})}\in\Pi\mathfrak{gl}_N=
  \mathfrak{q}(N)_{\bar 1}$ are the odd matrix units (parity-reversed
  copies in the $B$-block).

**Parity check.** $Z_2^{\mathrm{otr}}$ is a sum of products of one
even and one odd generator. Each summand has parity $\bar 0+\bar 1=
\bar 1$; the sum is *odd*. Hence $Z_2^{\mathrm{otr}}\in
Z(U(\mathfrak{q}(N)))_{\bar 1}$, the **odd part of the centre**.

**Centrality verification (sketch).** For $X\in\mathfrak{q}(N)_{\bar 0}$
(a Lie-algebra generator),
\[
   [X,Z_2^{\mathrm{otr}}]
     =\sum_{i,j}\bigl([X,T_{ij}]T_{ji}^{(\mathrm{odd})}+T_{ij}[X,T_{ji}^{(\mathrm{odd})}]
       +\text{symmetric}\bigr).
\]
The structure constants of $\mathfrak{q}(N)$ on the even/odd
generators (Cheng–Wang Ch. 6, Eq. (6.10)–(6.13)) give
$[A,T_{ij}]=A_{ki}T_{kj}-A_{jk}T_{ik}$ and $[A,T_{ij}^{(\mathrm{odd})}]
=A_{ki}T_{kj}^{(\mathrm{odd})}-A_{jk}T_{ik}^{(\mathrm{odd})}$ with the
*same* structure constants (the even-odd action is via the adjoint
on the index pair). The two contributions cancel symmetrically,
giving $[X,Z_2^{\mathrm{otr}}]=0$. For $X\in\mathfrak{q}(N)_{\bar 1}$
the verification is parallel using the odd-odd anticommutator
$[T^{(\mathrm{odd})}_{ij},T^{(\mathrm{odd})}_{kl}]=
\delta_{jk}T_{il}+\delta_{il}T_{kj}$ (Cheng–Wang Eq. (6.13)).

### §1.2 Comparison with the gl-Capelli element c_2

The W22 mechanism uses the gl Capelli element $c_2\in
U(\mathfrak{gl}_{2N})$ (or equivalently $U(\mathfrak{gl}(N|N))$) as the
quadratic central element controlling the propagator-loop contraction.
The gl element is **even** at all degrees (since $\mathfrak{gl}_{2N}$
is even).

The queer element $Z_2^{\mathrm{otr}}$ is *odd* — a **parity-shifted
analogue**. Its existence as a central element confirms that the
queer trace `otr` corresponds to a non-trivial central character on
$U(\mathfrak{q}(N))$, parallel to (but distinct from) the central
character of the ordinary supertrace.

**Sergeev–Berele–Regev hook formula on q(N).** The Sergeev duality
between $\mathfrak{q}(N)$ and the Hecke–Clifford superalgebra
$\mathcal{HC}_n$ (Sergeev 1985 Sbornik; Brundan–Kleshchev 2003
Represent. Theory) gives the irreducible characters of $\mathfrak{q}(N)$
modules in terms of *strict partitions* (rather than ordinary
partitions, as on $\mathfrak{gl}_N$). The associated Schur Q-functions
$Q_\lambda$ replace ordinary Schur functions, and $Z_2^{\mathrm{otr}}$
acts on the irreducible $L_\lambda$ as the eigenvalue
\[
   Z_2^{\mathrm{otr}}\big|_{L_\lambda}
     = \sum_i 2\lambda_i \cdot [\text{odd phase factor}],
\]
where the odd phase factor reflects the strict-partition structure.
This is the analog of the Capelli eigenvalue $\sum_i\lambda_i(\lambda_i+
N+1-2i)$ on $\mathfrak{gl}_N$, with the odd-graded twist.

### §1.3 Verdict on (M3.1)

**Verdict.** $Z_2^{\mathrm{otr}}$ exists, has odd parity, and is the
natural Sergeev parallel of the gl-Capelli element. **(M3.1) closes
positively.**

The structural distinction from W22 is significant: the central
element controlling `otr` is *odd*, whereas the W22 mechanism on
$\Str$ uses an *even* element. This is the first marker of the
parity-shift between the two channels.

---

## §2. (M3.2) Is $\mathrm{otr}(I) = 0$?

### §2.1 Direct evaluation on the queer identity

The queer identity in $\mathfrak{q}(N)\subset\mathfrak{gl}(N|N)$ is
\[
   I_{\mathfrak{q}(N)}
     =\begin{pmatrix} I_N & 0 \\ 0 & I_N \end{pmatrix}
     \in\mathfrak{gl}(N|N),
\]
viewed as an element of the queer subalgebra (i.e.\ in the
$\begin{pmatrix} A & B \\ B & A \end{pmatrix}$ pattern with $A=I_N$,
$B=0$). The queer trace is $\mathrm{otr}\bigl(\begin{pmatrix} A & B \\
B & A \end{pmatrix}\bigr)=\Tr(B)$, so
\[
   \mathrm{otr}(I_{\mathfrak{q}(N)})=\Tr(0)=0.
\]

**Vacuous form.** This zero is the same kind of zero as
$\mathrm{otr}(\mathfrak{q}(N)_{\bar 0})=0$ — the queer trace is
*identically zero on the even part* of $\mathfrak{q}(N)$ by
construction (it picks out the $B$-block). So
$\mathrm{otr}(I_{\mathfrak{q}(N)})=0$ is structurally trivial: the
identity is even, and `otr` is zero on all even elements.

### §2.2 What is the actual propagator-loop coefficient?

The bosonic / supertrace propagator-loop on $\mathfrak{gl}_N$ /
$\mathfrak{gl}(N|N)$ contracts to $\Tr(I_N)=N$ / $\Str(I_{N|N})=N-N=0$.
The contraction structure is
\[
   \mathrm{Loop}=\sum_{a}\delta^a_a
     \quad\text{or}\quad
   \mathrm{Loop}^{\mathrm{super}}=\sum_a (-1)^{|a|}\delta^a_a.
\]

For the **queer-twisted loop**, the contraction passes through the
queer central element $J\in\mathfrak{q}(N)$ defined by (in the user's
convention)
\[
   J=\begin{pmatrix} 0 & I_N \\ -I_N & 0 \end{pmatrix},\qquad J^2=-I_{2N}.
\]

**Note on conventions.** Two sign conventions exist for the queer
central element. The user's convention is $J=((0, I_N), (-I_N, 0))$
satisfying $J^2=-I_{2N}$ (a *complex structure*); the alternative
$J'=((0, I_N), (I_N, 0))$ satisfies $(J')^2=+I_{2N}$ (an *involution*).
Both are used in the literature (Sergeev's original is the involution
form; Penkov–Serganova use the complex-structure form). We keep the
complex-structure form $J^2=-I$ as specified.

**Queer trace of $J$.** Direct computation:
\[
   \mathrm{otr}(J)=\mathrm{otr}\begin{pmatrix} 0 & I_N \\ -I_N & 0 \end{pmatrix}
     =\Tr(I_N)=N.
\]

The *signed* form gives $\mathrm{otr}(J)=\Tr(I_N)=N$ regardless of
sign convention (the $-I_N$ in the lower-left does not enter `otr`,
which projects to the upper-right $B$-block in the convention
$\mathrm{otr}((A,B);(B,A))=\Tr(B)$; in the user's $J$ this is $I_N$).
**The propagator-loop coefficient in the queer-twisted channel is
$N$, not zero.**

### §2.3 Structural interpretation

The relevant evaluation is **not** $\mathrm{otr}(I_{\mathfrak{q}(N)})$
(which is vacuous-zero, like asking the bosonic trace of an odd
element) but $\mathrm{otr}(J)$ where $J$ is the queer central element.
The queer trace evaluates non-trivially on the **odd central
direction** $\C\cdot J\subset\mathfrak{q}(N)_{\bar 1}$, giving $N$.

**Parallel with bosonic $\mathfrak{gl}_N$.** On $\mathfrak{gl}_N$, the
trace $\Tr(I)=N$ is non-zero on the even central direction
$\C\cdot I\subset\mathfrak{gl}_N$. The U(1)-center anomaly
(Theorem G) records this as the class $\hbar N[\bar c]$.

**Parallel on $\mathfrak{q}(N)$.** The queer trace $\mathrm{otr}(J)=N$
is non-zero on the **odd** central direction $\C\cdot J\subset
\mathfrak{q}(N)_{\bar 1}$. **This is the *direct* analogue of the
bosonic Theorem G obstruction, in the odd-parity sector.** The queer
trace produces an obstruction with the same numerical coefficient
$N$, but in odd parity.

### §2.4 Verdict on (M3.2)

**Verdict.** $\mathrm{otr}(I_{\mathfrak{q}(N)})=0$ is *vacuous* — `otr`
is zero on all even elements by construction. The non-trivial
evaluation is $\mathrm{otr}(J)=N$ on the odd central element, which is
the **odd-parity analogue of the bosonic Theorem G coefficient $\Tr(I)=N$**.

This kills the necessary-condition narrative that would have closed
the queer discharge: the queer-twisted propagator-loop coefficient is
$N$, not zero, exactly parallel to the bosonic case where $\Tr(I)=N$
gives the Theorem G obstruction. **(M3.2) is not a discharge: it is a
*reproduction* of the Theorem G obstruction in the odd-parity sector.**

---

## §3. (M3.3) Queer-twisted heat kernel and (A5) parity-equivariance

### §3.1 The naive twist

The user proposes the queer-twisted heat-kernel parametrix
\[
   \Delta^{\mathrm{otr}}_{\mathrm{sK}}
     =\sum_a (-1)^{|a|}\,J\cdot T^a\cdot J\cdot T_a,
\]
where $\{T^a\}$ is a basis of $\mathfrak{q}(N)$ and $\{T_a\}$ is the
dual basis under the even non-degenerate form $B_0$ identified in
G3-M2.

**Simplification using $J^2=-I$.** If $J$ commutes with all $T^a$
(it does *not* — see below), then $J\cdot T^a\cdot J=J^2\cdot T^a=
-T^a$, and $\Delta^{\mathrm{otr}}_{\mathrm{sK}}=-\Delta_{\mathrm{sK}}$,
which would be a sign-flipped copy of the ordinary heat kernel — no
new information.

**Matrix-level commutators with $J$.** The queer central element $J$
is in the odd part $\mathfrak{q}(N)_{\bar 1}$. Its bracket with even
generators $A\in\mathfrak{gl}_N=\mathfrak{q}(N)_{\bar 0}$, embedded
in $\mathfrak{q}(N)$ as $A=\begin{pmatrix} \alpha & 0 \\ 0 & \alpha
\end{pmatrix}$ for $\alpha\in\mathfrak{gl}_N$ (both diagonal blocks
equal), with $J=\begin{pmatrix} 0 & I \\ -I & 0 \end{pmatrix}$:
\[
   AJ=\begin{pmatrix} \alpha & 0 \\ 0 & \alpha \end{pmatrix}
       \begin{pmatrix} 0 & I \\ -I & 0 \end{pmatrix}
     =\begin{pmatrix} 0 & \alpha \\ -\alpha & 0 \end{pmatrix},
\]
\[
   JA=\begin{pmatrix} 0 & I \\ -I & 0 \end{pmatrix}
       \begin{pmatrix} \alpha & 0 \\ 0 & \alpha \end{pmatrix}
     =\begin{pmatrix} 0 & \alpha \\ -\alpha & 0 \end{pmatrix}.
\]
**$AJ=JA$ for $A$ even.** So $J$ commutes with the even part as
matrices (it is in the centre of the matrix algebra restricted to
the queer-block subalgebra). In particular, $[A, J]=0$ for all
$A\in\mathfrak{q}(N)_{\bar 0}$.

For $B$ odd, $B=\begin{pmatrix} 0 & \beta \\ \beta & 0 \end{pmatrix}$
($\beta\in\mathfrak{gl}_N$):
\[
   BJ=\begin{pmatrix} 0 & \beta \\ \beta & 0 \end{pmatrix}
       \begin{pmatrix} 0 & I \\ -I & 0 \end{pmatrix}
     =\begin{pmatrix} -\beta & 0 \\ 0 & \beta \end{pmatrix},
\]
\[
   JB=\begin{pmatrix} 0 & I \\ -I & 0 \end{pmatrix}
       \begin{pmatrix} 0 & \beta \\ \beta & 0 \end{pmatrix}
     =\begin{pmatrix} \beta & 0 \\ 0 & -\beta \end{pmatrix}.
\]
**$BJ=-JB$ — $J$ anticommutes with the odd part as matrices.** This
is consistent with $J$ being in $\mathfrak{q}(N)_{\bar 1}$ and the
super-bracket $[B, J]=BJ+JB=0$ (the odd-odd super-bracket is the
anticommutator of matrices). Indeed: $BJ+JB=\begin{pmatrix} 0 & 0 \\
0 & 0 \end{pmatrix}=0$. **So the super-bracket $[B, J]_{\mathrm{super}}=
0$ for all $B$ odd — $J$ is genuinely central.**

So $J$ is central in $\mathfrak{q}(N)$ with respect to the
super-bracket, but anticommutes with the odd part as matrices. This
double role is the source of the parity-twist obstruction.

### §3.2 The parity operator on $\mathfrak{q}(N)$

The parity operator on $\mathfrak{q}(N)\subset\mathfrak{gl}(N|N)$ is
\[
   P^{\mathfrak{q}}=\diag(\mathbf 1_N, -\mathbf 1_N)\in\End(\C^{N|N}),
\]
acting on the underlying graded vector space. Restricted to even
elements $A=\diag(\alpha,\alpha)\in\mathfrak{q}(N)_{\bar 0}$,
$P^{\mathfrak{q}}\cdot A\cdot (P^{\mathfrak{q}})^{-1}=A$ (parity-even
elements are fixed). Restricted to odd elements
$B=((0,\beta),(\beta,0))\in\mathfrak{q}(N)_{\bar 1}$,
\[
   P^{\mathfrak{q}}\cdot B\cdot (P^{\mathfrak{q}})^{-1}
     =\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
      \begin{pmatrix} 0 & \beta \\ \beta & 0 \end{pmatrix}
      \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
     =\begin{pmatrix} 0 & -\beta \\ -\beta & 0 \end{pmatrix}=-B.
\]
**$P^{\mathfrak{q}}$ acts as $\pm 1$ on the parity-graded basis,
correctly.**

### §3.3 The queer-twist operator $J$ vs $P^{\mathfrak{q}}$: Att-2 head-on

**The crucial check (Att-2 from prompt).** Compute
$P^{\mathfrak{q}}\cdot J\cdot (P^{\mathfrak{q}})^{-1}$:
\[
   P^{\mathfrak{q}}\cdot J\cdot (P^{\mathfrak{q}})^{-1}
     =\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
      \begin{pmatrix} 0 & I \\ -I & 0 \end{pmatrix}
      \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
     =\begin{pmatrix} 0 & -I \\ I & 0 \end{pmatrix}=-J.
\]

**$J$ anticommutes with $P^{\mathfrak{q}}$ in the conjugation
sense — equivalently, $J$ is parity-odd, which is correct since
$J\in\mathfrak{q}(N)_{\bar 1}$.**

This is the *expected* parity behaviour: $J$ being odd means it flips
sign under conjugation by $P^{\mathfrak{q}}$. The W30 (A5) condition
requires the parametrix $\Delta_{\mathrm{sK}}$ to *commute* with
$P^{\mathfrak{q}}$. Since $\Delta_{\mathrm{sK}}=\sum_a(-1)^{|a|}T^a T_a$
is a sum of products $T^a T_a$ each of total parity $|a|+|a|=0$, it
is **even** and commutes with $P^{\mathfrak{q}}$.

**The queer-twisted parametrix $\Delta^{\mathrm{otr}}_{\mathrm{sK}}=
\sum_a(-1)^{|a|}J\cdot T^a\cdot J\cdot T_a$** has each summand
with total parity $|J|+|a|+|J|+|a|=1+|a|+1+|a|\equiv 0\pmod 2$, so
the summand is even. **It commutes with $P^{\mathfrak{q}}$**. So far
so good — but does it satisfy the *operator-level* (A5) condition,
which is stricter?

### §3.4 Operator-level (A5) verification

W30-W3-W30-02 (operator-level (A5)) requires more than parity-commuting:
it requires $[\Delta_{\mathrm{sK}}, P^{\mathfrak{q}}]_{\mathrm{super}}=0$
in the BV sense, i.e.\ the parametrix kernel is sector-pure (each
summand stays in its parity sector under heat-kernel propagation).

For the standard $\Delta_{\mathrm{sK}}$, each summand $T^a T_a$ stays
in the algebra $U(\mathfrak{q}(N))$, and its parity is determined by
the matching $|T^a|=|T_a|$ (which holds because $B_0$ is an *even*
form: it pairs even-with-even and odd-with-odd separately). Hence
each summand has uniform parity $0$, and the parametrix is
sector-pure-even.

For $\Delta^{\mathrm{otr}}_{\mathrm{sK}}$, the operator
$J\cdot T^a\cdot J\cdot T_a$ involves two $J$'s. Using $J^2=-I$ and
the (super)commutation rules:
* If $T^a$ is even: $JT^aJ=J^2T^a=-T^a$ (since $[T^a, J]=0$ as
  matrices for even $T^a$).
* If $T^a$ is odd: $JT^aJ=-J^2T^a=+T^a$ (since $T^aJ=-JT^a$ for odd
  $T^a$).

So
\[
   JT^aJ=(-1)^{|a|+1}T^a=-(-1)^{|a|}T^a.
\]

Substituting:
\[
   \Delta^{\mathrm{otr}}_{\mathrm{sK}}
     =\sum_a (-1)^{|a|}\cdot(-1)^{|a|+1}T^a\cdot T_a
     =\sum_a (-1)^{2|a|+1}T^aT_a
     =-\sum_a T^aT_a.
\]

**Crucially**, this is *not* the standard parametrix
$\Delta_{\mathrm{sK}}=\sum_a(-1)^{|a|}T^aT_a$ but rather
$-\sum_a T^aT_a$ (no parity sign). The difference is precisely the
parity-equivariance: $\Delta_{\mathrm{sK}}$ has the $(-1)^{|a|}$ that
encodes the supertrace structure;
$\Delta^{\mathrm{otr}}_{\mathrm{sK}}=-\sum_a T^aT_a$ has *no* parity
sign. **This is the bosonic trace, not the supertrace.**

**Operator-level (A5) check on $\Delta^{\mathrm{otr}}_{\mathrm{sK}}=
-\sum_a T^aT_a$.** This kernel does **not** commute with
$P^{\mathfrak{q}}$ in the sector-pure sense: the absence of the
$(-1)^{|a|}$ means even and odd sectors mix non-trivially under
heat-kernel propagation. The (A5) condition fails.

**Reformulation as (A5)\textsuperscript{otr}.** A signed
parity-equivariance condition that the queer-twisted kernel *does*
satisfy is
\[
   (A5)^{\mathrm{otr}}\colon\quad
   \tau\cdot\Delta^{\mathrm{otr}}_{\mathrm{sK}}\cdot\tau^{-1}
     =-\Delta^{\mathrm{otr}}_{\mathrm{sK}},
\]
where $\tau$ is a *parity-flipping* operator (e.g.\ $J$ itself in
the matrix sense). This is a sign-flipped variant of (A5) — but it
is **not** the (A1)–(A5) class of W30: it is a *new* admissibility
class.

### §3.5 Verdict on (M3.3)

**Verdict.** The queer-twisted heat kernel
$\Delta^{\mathrm{otr}}_{\mathrm{sK}}$ does **not** satisfy the
unsigned (A5) parity-equivariance. It satisfies a *sign-flipped*
variant (A5)\textsuperscript{otr}, which is a different admissibility
class. **(M3.3) FAILS: the W22 (A5) condition does not extend to the
queer twist; a new condition (A5)\textsuperscript{otr} replaces it.**

This is the **first structural obstruction** to the queer discharge:
the regulator class admissible for $\Str$ is **not** admissible for
`otr`. The physical interpretation (Att-2 from prompt): the
parity-equivariance must be replaced with a *signed* parity-equivariance
when twisting by the queer central element.

---

## §4. (M3.4) Chain-level QME residue at one loop in queer channel

### §4.1 Setup of the queer-channel one-loop diagram

The brane probe action on $\mathfrak{q}(N)$, *with the queer trace
inserted as a boundary evaluation*, reads
\[
   S_\partial^{\mathrm{q,otr}}
     =\int_\R\mathrm{otr}\bigl(\phi_1\cdot d\phi_2 + A[\phi_1,\phi_2]_{\mathfrak{q}}\bigr),
\]
where $\phi_1,\phi_2\in\mathfrak{q}(N)$ are *not* restricted to the
even part (since `otr` is non-trivial only on odd elements, the
relevant $\phi$ must have an odd component). $A=\psi^\vee$ is the
Lagrange multiplier antifield.

**Key structural difference from W22 / G3-M2.** In the W22 setup,
$\phi_1,\phi_2\in\mathfrak{gl}(N|N)_{\mathrm{even}}$ — restricted to
the even sector. With the queer trace replacing the supertrace, the
relevant $\phi_i$ are *both* even and odd (with odd components
contributing to `otr`). This is a **different action** with different
field content and different propagator structure.

### §4.2 BV propagator on the queer-twisted action

The propagator from the new action:
\[
   \{(\phi_1)^a_b, (\phi_2)^c_d\}_{\mathrm{q,otr}}
     =J^a_d\,J^c_b
     +\text{(odd corrections)},
\]
where the $J$'s appear because the queer-trace evaluation
$\mathrm{otr}(X) = \Tr(J\cdot X|_{\bar 1})$ inserts $J$ into the
contraction. The propagator contracted on a closed loop:
\[
   \mathrm{Loop}^{\mathrm{q,otr}}
     =\sum_{a,b}J^a_b\cdot J^b_a
     =\Tr(J^2)
     =\Tr(-I_{2N})
     =-2N.
\]

**Sign and normalization check.** The naive evaluation
$\Tr(J^2)=-2N$ is the *bosonic* trace of $J^2$, not the queer trace.
The queer-trace evaluation on the heat-kernel loop is
$\mathrm{otr}\bigl(\sum_a(-1)^{|a|}T^a T_a\bigr)$, which on the
queer-twisted kernel reduces to $\mathrm{otr}(J\cdot J\cdot
\text{(diagonal)})$. With $J^2=-I_{2N}$ and $\mathrm{otr}(I)=0$ (since
`otr` is zero on even elements), the queer-trace of
$J^2=-I$ is $\mathrm{otr}(-I)=0$. The *physical* propagator-loop
coefficient on the brane probe is not $\mathrm{otr}(J^2)$ — it is
$\mathrm{otr}(J)$ at the single-loop contraction with **one** factor
of $J$, computed in §4.3.

### §4.3 Careful derivation of the one-loop QME coefficient

The W22-T2 derivation runs:
* The Dirac brane action is $S_\partial=\int\Str(\phi_1 d\phi_2 +
  A[\phi_1,\phi_2])$.
* The propagator on $\mathfrak{gl}(N|N)$ is $\{(\phi_1)^a_b,(\phi_2)^c_d\}=
  (-1)^{|a||b|}\delta^a_d\delta^c_b$.
* The one-loop QME diagram contracts the propagator with itself once
  (single closed loop) to give the loop sum
  $\sum_a(-1)^{|a|}\delta^a_a=\Str(I)=N-N=0$ at q-balance.

For the **queer-trace channel**, the boundary evaluation is the queer
trace $\mathrm{otr}$. This *changes the boundary contact term* in the
QME but does not change the propagator: the propagator is still
inherited from the embedding $\mathfrak{q}(N)\subset\mathfrak{gl}(N|N)$,
which uses the ordinary BV pairing.

**The QME obstruction in the queer channel** is computed by inserting
the queer-trace boundary evaluation into the W22 calculation. The
boundary contact:
\[
   \{I_\partial^{\mathrm{otr}}(a,f), I_\partial^{\mathrm{otr}}(b,g)\}_{\mathrm{open}}
     = I_\partial^{\mathrm{otr}}(ab,\{f,g\}_{\bar A})
       + \mathrm{otr}(J\cdot I_{2N})\cdot\omega(f,g)\int_\R a(t)b(t)\,dt.
\]

The coefficient $\mathrm{otr}(J\cdot I_{2N})$: the queer trace of
$J\cdot I_{2N}=J$ is $\mathrm{otr}(J)=N$ (computed in §2.2). So
\[
   \{I_\partial^{\mathrm{otr}}(a,f), I_\partial^{\mathrm{otr}}(b,g)\}
     = I_\partial^{\mathrm{otr}}(ab,\{f,g\}_{\bar A})
       + N\cdot\omega(f,g)\int_\R a(t)b(t)\,dt,
\]
*odd-graded* because $\mathrm{otr}$ is valued in $\Pi\C$.

**Inserting the central ghost $\gamma_{\mathbf 1}$** (degree 1):
\[
   \mathrm{Ob}_{\mathrm{sc}}^{\mathrm{otr}}(\gamma_{\mathbf 1}; a,f; b,g)
     =\hbar N\,\omega(f,g)\int_\R a(t)b(t)\gamma_{\mathbf 1}(t)\,dt
     \quad\in\mathcal O_{\mathrm{loc}}(\mathcal E_w^{\mathfrak{q}})_{\bar 1}.
\]

The CE class is **$\hbar N\,[\bar c]^{\mathrm{otr}}$** in
$H^1(\mathcal O_{\mathrm{loc}}, Q+\{I_0,-\})_{\bar 1}$, the
**odd-parity** sector of the BV obstruction complex.

### §4.4 Is this class trivial (a coboundary) or non-trivial?

The class $[\bar c]^{\mathrm{otr}}\in H^2_{\mathrm{Lie}}(\bar A,\Pi\C)$
is the **same Lie 2-cocycle $\omega$** of Lemma `lem:omega-cocycle`
(main.tex 284), but valued in the *odd* line $\Pi\C$ instead of $\C$.
Since $H^2_{\mathrm{Lie}}(\bar A, \C)$ is one-dimensional with
$[\bar c]$ as generator (`lem:omega-cocycle`), and $\Pi$ is a
parity-shift functor on the coefficient, we have
\[
   H^2_{\mathrm{Lie}}(\bar A, \Pi\C)=\Pi\cdot H^2_{\mathrm{Lie}}(\bar A,\C)
     =\Pi\cdot\C\cdot[\bar c],
\]
also one-dimensional, with generator $[\bar c]^{\mathrm{otr}}=
\Pi[\bar c]$.

**Triviality check.** The same proof of non-triviality from
`lem:omega-cocycle` (the primitive $\eta(f)=-[f]_0$ does not descend
to $\bar A$) applies verbatim to $\Pi\C$ coefficients: any putative
primitive $\bar\eta:\bar A\to\Pi\C$ would lift to a primitive of
$\Pi\omega$ on $\mathfrak{h}_{\mathrm{poly}}$, but the primitive
$\eta(f)=-[f]_0$ does not descend (same proof). So
$[\bar c]^{\mathrm{otr}}$ is **non-trivial** in
$H^2_{\mathrm{Lie}}(\bar A, \Pi\C)$.

**Coboundary via $\hbar$-correction?** The bosonic Theorem G class
$\hbar N[\bar c]$ is non-trivial as a chain-level cocycle, by
`prop:scalar-contact-obstruction` of `appendix-unreduced-bv-qme.tex`
(line 124–125: "Its associated graded CE class is $\hbar N[\bar c]$.
This class is not exact in the scalar-reduced Hamiltonian source.").

The same argument applies to $[\bar c]^{\mathrm{otr}}$: any
counterterm $C^{\mathrm{otr}}$ in the *queer-shifted* BV complex
$\mathcal O_{\mathrm{loc}}(\mathcal E_w)_{\bar 1}$ that satisfies
$(Q+\{I_0,-\})C^{\mathrm{otr}}+\hbar N\omega^{\mathrm{otr}}=0$ would
descend to a primitive of $[\bar c]^{\mathrm{otr}}$ in $H^2_{\mathrm{Lie}}(\bar A,\Pi\C)$,
contradiction.

**$[\bar c]^{\mathrm{otr}}$ is a non-trivial cohomology class — a
new obstruction class, not a coboundary.**

### §4.5 Verdict on (M3.4)

**Verdict.** The chain-level QME residue at one loop in the queer
channel is
\[
   \mathrm{Ob}_{\mathrm{sc}}^{\mathrm{otr}}=\hbar N\,[\bar c]^{\mathrm{otr}}
     \in H^1(\mathcal O_{\mathrm{loc}}, Q+\{I_0,-\})_{\bar 1},
\]
**non-trivial as a cohomology class** in the odd-parity sector of the
BV obstruction complex.

**Higher-loop extension.** By the same combinatorial reasoning as
W22-L3 (loop products are products of `otr`'s of identity-like
elements; on the queer-twisted kernel each loop closure contributes
$\mathrm{otr}(J^k)$). With $J^k=(-I)^{k/2}=(-1)^{k/2}I$ for $k$ even
and $J^k=(-1)^{(k-1)/2}J$ for $k$ odd:
* $k$ even: $\mathrm{otr}(J^k)=\mathrm{otr}((-1)^{k/2}I)=0$ (since
  `otr(I)=0`).
* $k$ odd: $\mathrm{otr}(J^k)=(-1)^{(k-1)/2}\mathrm{otr}(J)=(-1)^{(k-1)/2}N$.

So the *odd-loop-length* contractions are non-zero, contributing
$N$ at each odd-length loop with alternating signs. **The queer-trace
QME does not vanish — it produces a non-trivial $\hbar^\ell N$-style
class at each odd loop length.**

This is parallel to the bosonic Theorem G mechanism: a non-trivial
$\hbar N[\bar c]$ obstruction at every loop, not killed by any
chain-level identity.

---

## §5. (M3.5) Discharge analogue / failure with named obstruction

### §5.1 Why the W22-T2 mechanism does not extend

The W22-T2 chain-level lift $\Lambda^{\Str}$ is *strict* (no
homotopies) and depends only on closed-side data. Its key property is
that the QME obstruction factors as
\[
   \mathrm{Ob}_{\mathrm{sc}}=\hbar\,\Str(I)\cdot\Lambda^{\Str}(\omega),
\]
and the supertrace coefficient $\Str(I)=N-N=0$ at super-balance kills
the entire expression *strictly* (not just up to coboundary).

For the queer trace, the analogous formula would read
\[
   \mathrm{Ob}_{\mathrm{sc}}^{\mathrm{otr}}=\hbar\,\mathrm{otr}(?)\cdot\Lambda^{\mathrm{otr}}(\omega),
\]
where the coefficient $\mathrm{otr}(?)$ depends on what the
propagator-loop contracts with. **The crucial step that fails:**
* On $\Str$, the propagator-loop contracts with $\Str$ giving
  $\Str(I)=0$.
* On `otr`, the propagator-loop contracts with `otr` giving
  $\mathrm{otr}(J)=N\neq 0$ (because the contraction passes through
  the queer central element $J$, not the identity $I$).

**The queer trace does *not* see the identity element of
$\mathfrak{q}(N)$ — it sees the queer central element $J$, which has
non-zero `otr`.** This is the fundamental structural difference
between the two channels.

### §5.2 Named obstruction: Obs-Q-otr-A5

**Obs-Q-otr-A5 (the deciding obstruction).** The queer central element
$J\in\mathfrak{q}(N)_{\bar 1}$ anticommutes with the parity operator
$P^{\mathfrak{q}}$ (in the conjugation sense:
$P^{\mathfrak{q}}\cdot J\cdot (P^{\mathfrak{q}})^{-1}=-J$). Hence the
queer-twisted heat kernel
$\Delta^{\mathrm{otr}}_{\mathrm{sK}}=\sum_a(-1)^{|a|}JT^aJT_a=
-\sum_a T^aT_a$ does *not* satisfy the W30 (A5) parity-equivariance
condition (it commutes with $P^{\mathfrak{q}}$ as an even operator,
but the *kernel structure* is the bosonic trace, not the supertrace,
so sector-pure-ness fails).

A signed variant (A5)\textsuperscript{otr} can be defined and is
satisfied by $\Delta^{\mathrm{otr}}_{\mathrm{sK}}$, but it is a
different admissibility class than the W22 / W30 (A1)–(A5).
**The queer discharge requires a different regulator class, and even
within that class the propagator-loop coefficient
$\mathrm{otr}(J)=N\neq 0$ does not vanish.**

### §5.3 Could a different choice of $J$ help?

Alternative queer central elements:
* $J'=((0, I), (I, 0))$: $(J')^2=I_{2N}$ (involution form). Same
  computation: $\mathrm{otr}(J')=\Tr(I_N)=N\neq 0$. Same obstruction.
* $J''=((0, K), (-K, 0))$ for any matrix $K$: $\mathrm{otr}(J'')=\Tr(K)$.
  Choosing $\Tr(K)=0$ (e.g.\ $K\in\mathfrak{sl}_N$) would give
  $\mathrm{otr}(J'')=0$, **but** $J''$ is then no longer central in
  $\mathfrak{q}(N)$ unless $K$ commutes with all of $\mathfrak{gl}_N$,
  which forces $K=cI_N$ for some $c\in\C$, i.e.\ $\Tr(K)=cN$. Setting
  $c=0$ gives $K=0$ and $J''=0$, trivial. **There is no non-trivial
  central element of $\mathfrak{q}(N)$ in the odd part with
  $\mathrm{otr}=0$.**

This is the structural reason `otr` does not discharge: the queer
central direction is *forced* to have non-zero queer trace.

### §5.4 Verdict on (M3.5)

**Verdict.** The queer trace `otr` does **not** admit a discharge
analogous to W22-T1/T2. The named obstruction is **Obs-Q-otr-A5**:
the queer central element $J$ violates (A5) parity-equivariance, and
even with a signed (A5)\textsuperscript{otr} the propagator-loop
coefficient $\mathrm{otr}(J)=N$ does not vanish. The discharge fails
at two layers:
* (Layer 1, regulator) The naive queer-twisted heat kernel is in a
  different admissibility class than (A1)–(A5).
* (Layer 2, coefficient) Even in the corrected admissibility class,
  the propagator-loop coefficient is $N$, not zero.

**(M3.5) FAILS — Phase-5 escalation candidate.**

---

## §6. (M3.6) Cross-walk to manuscript Theorem G

### §6.1 Theorem G as it stands in main.tex

Theorem `thm:u1-center-anomaly-open` (`main.tex` 354–369) records
\[
   \{\Tr\,\phi_1, \Tr\,\phi_2\}=N
\]
on $\mathfrak{gl}_N$, and the U(1)-center extension class
$\hbar N[\bar c]\in H^2_{\mathrm{Lie}}(\bar A, \C)$ via the boundary
evaluation map $\partial_{\mathrm{bb},N}^{\mathrm{full}}: f\mapsto
\Tr\,f(\phi_1,\phi_2)$. The class $\hbar N[\bar c]$ is one-dimensional:
$H^2_{\mathrm{Lie}}(\bar A, \C)\cong\C\cdot[\bar c]$.

The U(1)-center referred to is the centre $\C\cdot I\subset\mathfrak{gl}_N$
with character $\Tr$. **There is one central direction, hence one
anomaly class.**

### §6.2 The U(1)-center decomposition on $\mathfrak{q}(N)$

On $\mathfrak{q}(N)$, the centre of the matrix algebra (restricted to
the queer subalgebra $\mathfrak{q}(N)\subset\mathfrak{gl}(N|N)$) is
**two-dimensional**:
\[
   \mathfrak{z}(\mathfrak{q}(N))=\C\cdot I_{2N}\oplus\C\cdot J,
\]
where $I_{2N}=\diag(I_N, I_N)\in\mathfrak{q}(N)_{\bar 0}$ is the
*even* central element and $J=((0, I), (-I, 0))\in\mathfrak{q}(N)_{\bar 1}$
is the *odd* central element. The two characters are
* $\Str: I_{2N}\mapsto 0$, $J\mapsto 0$.
* $\mathrm{otr}: I_{2N}\mapsto 0$, $J\mapsto N$.

So on $\mathfrak{q}(N)$, *neither* the even centre nor the (ordinary)
supertrace produce an anomaly with non-zero coefficient — they
both contract to zero on the central elements. The $\Str$-channel
**discharges** (G3-M2 verdict).

The **`otr`-channel** sees a non-zero coefficient $N$ on the odd
central direction $J$. This produces a **new** anomaly class
$\hbar N[\bar c]^{\mathrm{otr}}\in H^2_{\mathrm{Lie}}(\bar A, \Pi\C)$.

### §6.3 Does Theorem G absorb the otr-channel?

**No.** Theorem G as stated is the U(1)-center anomaly with
character $\Tr$ on the **bosonic** $\mathfrak{gl}_N$. On $\mathfrak{q}(N)$:
* The bosonic-extension U(1)-center character is $\Str$, which gives
  zero on both central elements $I_{2N}$ and $J$. So the
  $\Str$-version of Theorem G has zero coefficient — **discharged**.
* The queer-extension U(1)-center character is $\mathrm{otr}$, which
  gives $N$ on $J$. This is a **separate** anomaly class, not
  included in the manuscript's Theorem G.

**Theorem G does not absorb the otr-channel.** The manuscript's
Theorem G records a single class $[\bar c]\in\C\cdot H^2_{\mathrm{Lie}}(\bar A,\C)$;
the queer-channel produces a *new* class
$[\bar c]^{\mathrm{otr}}\in\Pi\C\cdot H^2_{\mathrm{Lie}}(\bar A,\C)$
that the manuscript does not yet account for.

### §6.4 The two-supertrace structure as open-closed witness

**Witten lens.** The two-supertrace structure $(\Str, \mathrm{otr})$ on
$\mathfrak{q}(N)$ is the algebraic shadow of a physical duality.
Sergeev's original construction (1983) was motivated by the
parastatistics of a *fermionic* extension of bosonic gauge theories,
where the queer supertrace records the *additional* anomaly absent in
the bosonic case.

Physically: the brane-probe Dirac construction on $\mathfrak{q}(N)$
sees two distinct central characters. The ordinary supertrace
discharges (no anomaly in the $\Str$-channel) but the queer trace
remains anomalous. This is a **boundary-state distinction**: the
$\Str$-boundary-state is anomaly-free; the `otr`-boundary-state is
anomalous with the same coefficient $N$ as the bosonic
$\mathfrak{gl}_N$ Theorem G.

**Open-closed duality interpretation.** The manuscript's Theorem G is the
open-side image (under $\partial_{\mathrm{bb},N}^{\mathrm{full}}$) of
a closed-side cocycle. On $\mathfrak{q}(N)$, the boundary evaluation
splits into two channels: $\partial_{\mathrm{bb},N}^{\Str}$ and
$\partial_{\mathrm{bb},N}^{\mathrm{otr}}$. The **closed-side** cocycle
$\omega$ is unchanged (it lives on $\bar A$, not on the matrix source).
What changes is the **open-side coupling**: the $\Str$-channel
coupling is zero, and the `otr`-channel coupling is $N$.

This means the closed-side $\omega$ produces *two* parallel open-side
realizations on $\mathfrak{q}(N)$ — one through each supertrace. **The
queer trace witnesses an open-closed duality that the ordinary
supertrace does not see.**

### §6.5 Verdict on (M3.6)

**Verdict.** Theorem G in `main.tex` as stated does **not** absorb the
queer-trace residue. The queer trace produces a **new independent
anomaly class** $\hbar N[\bar c]^{\mathrm{otr}}\in H^2_{\mathrm{Lie}}(\bar A,\Pi\C)$,
parallel to but distinct from the bosonic Theorem G class
$\hbar N[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$.

**Phase-5 cross-walk.** The natural manuscript extension would be a
**Theorem G\textsuperscript{otr}** ("Queer U(1)-center anomaly on
$\mathfrak{q}(N)$"), parallel to the existing Theorem G but in the
odd-parity sector. This is a candidate Phase-5 / Vol III frontier
finding: the queer trace on $\mathfrak{q}(N)$ produces an anomaly
*independent* from the bosonic Theorem G, with the same numerical
coefficient $N$.

---

## §7. Two-supertrace cohomology table

| Channel | Central element | Trace evaluation | Cohomology class | (A5) verified? | Discharges? |
|---|---|---|---|---|---|
| **Bosonic** ($\mathfrak{gl}_N$, manuscript) | $I_N\in\mathfrak{gl}_N$ | $\Tr(I_N)=N$ | $\hbar N[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$ | (vacuous, no $\Z/2$) | No (Theorem G obstruction) |
| **Ordinary supertrace** ($\Str$ on $\mathfrak{q}(N)$, G3-M2) | $I_{2N}\in\mathfrak{q}(N)_{\bar 0}$ | $\Str(I_{2N})=N-N=0$ | $0$ | (A5) holds (W22-style) | **Yes — discharges** |
| **Queer trace** (`otr` on $\mathfrak{q}(N)$, this document) | $J\in\mathfrak{q}(N)_{\bar 1}$ | $\mathrm{otr}(J)=N$ | $\hbar N[\bar c]^{\mathrm{otr}}\in H^2_{\mathrm{Lie}}(\bar A,\Pi\C)$ | (A5) **fails**; (A5)\textsuperscript{otr} different class | **No — new obstruction** |

**Independence statement.** The two supertrace classes $\Str$ and
`otr` on $\mathfrak{q}(N)$ are **structurally independent**:
* They correspond to different elements of the **2-dimensional
  centre** $\mathfrak{z}(\mathfrak{q}(N))=\C\cdot I_{2N}\oplus\C\cdot J$.
* They produce cocycle classes in **different cohomology spaces**:
  $H^2_{\mathrm{Lie}}(\bar A,\C)$ for $\Str$ vs.\ $H^2_{\mathrm{Lie}}(\bar A,\Pi\C)$
  for `otr`.
* They satisfy **different parity-equivariance conditions**:
  unsigned (A5) for $\Str$, signed (A5)\textsuperscript{otr} for `otr`.
* The W22 / G3-M2 discharge mechanism kills the $\Str$ class but
  **does not kill the `otr` class**.

**Two-dimensional class space.** On $\mathfrak{q}(N)$, the natural
ambient class space is the **graded direct sum**:
\[
   H^2_{\mathrm{Lie}}(\bar A; \C\oplus\Pi\C)
     = \C\cdot[\bar c]\oplus\Pi\C\cdot[\bar c]^{\mathrm{otr}},
\]
isomorphic to $\C\oplus\Pi\C$ as a $\Z/2$-graded space. The brane
probe on $\mathfrak{q}(N)$ produces a class in this 2-dimensional
graded space:
\[
   [\mathrm{Ob}_{\mathrm{sc}}^{\mathfrak{q}}]
     = (\hbar\Str(I)[\bar c], \hbar\mathrm{otr}(J)[\bar c]^{\mathrm{otr}})
     = (0, \hbar N\cdot[\bar c]^{\mathrm{otr}}).
\]

**The first component is killed by q-balance ($\Str(I)=0$); the second
component is the queer residue $\hbar N$.**

---

## §8. Cross-walk to Theorem G in main.tex

### §8.1 Where Theorem G sits in the manuscript

* `main.tex` 318–352: Theorem `thm:u1-center-anomaly` (closed side):
  the class $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$ as the
  obstruction to splitting $\mathfrak{h}_{\mathrm{poly}}\to\bar A$.
* `main.tex` 354–393: Theorem `thm:u1-center-anomaly-open` (open
  side): on $\mathfrak{gl}_N$, the trace bracket $\{\Tr\phi_1,
  \Tr\phi_2\}=N$ and the boundary-evaluation image $[\bar c]$.
* `main.tex` 412–464: Theorem `thm:quantum-classical-anomaly`: the
  Capelli identity $XY-YX=\hbar N\,I$ implements $[\bar c]$ on the
  open side.
* `appendix-unreduced-bv-qme.tex` 76–158: Proposition giving the
  unreduced QME representative $\mathrm{Ob}_{\mathrm{sc}}=
  \hbar N\,\omega(f,g)\int a(t)b(t)\gamma_{\mathbf 1}(t)\,dt$ with
  associated graded $\hbar N[\bar c]$.

### §8.2 What the queer extension would say

A **Theorem G\textsuperscript{otr}** on $\mathfrak{q}(N)$ would record:
* **Closed side (unchanged).** The cocycle $\omega$ on $\bar A$ is
  the same; the cohomology class $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$
  is unchanged.
* **Open side, queer extension.** On $\mathfrak{q}(N)$, the two
  central directions $\C\cdot I_{2N}$ and $\C\cdot J$ each support a
  central character. The $\Str$-character gives zero (q-balance);
  the `otr`-character gives $N$. The queer extension class
  $[\bar c]^{\mathrm{otr}}\in H^2_{\mathrm{Lie}}(\bar A,\Pi\C)$ is
  the open-side image of $\omega$ under the queer boundary evaluation
  $\partial_{\mathrm{bb},N}^{\mathrm{otr}}: f\mapsto\mathrm{otr}\,f(\phi_1,\phi_2)$.

**Proposed inscription (proposal-only).** A new theorem block in
`appendix-unreduced-bv-qme.tex` after the existing
`prop:scalar-contact-obstruction`:

```latex
\begin{thm}[Queer U(1)-center anomaly on q(N)]
\label{thm:app-queer-u1-anomaly}
   Let \(\lie{g}=\lie{q}(N)\). The brane probe on \(\lie{q}(N)\) under
   the queer boundary evaluation
   \(\partial_{\mathrm{bb},N}^{\mathrm{otr}}: f\mapsto
   \mathrm{otr}\,f(\phi_1,\phi_2)\) produces a chain-level QME
   obstruction representative
   \[
     \operatorname{Ob}_{\mathrm{sc}}^{\mathrm{otr}}(\gamma_{\mathbf 1}; a,f; b,g)
       = \hbar N\,\omega(f,g)\int_\R a(t)b(t)\gamma_{\mathbf 1}(t)\,dt
       \quad\in\mathcal O_{\mathrm{loc}}(\mathcal E_w^{\mathfrak{q}})_{\bar 1},
   \]
   in the odd-parity sector of the BV obstruction complex. Its
   associated graded CE class is \(\hbar N[\bar c]^{\mathrm{otr}}\in
   H^2_{\mathrm{Lie}}(\bar A,\Pi\C)\). This class is non-trivial and
   independent from the bosonic class \(\hbar N[\bar c]\in
   H^2_{\mathrm{Lie}}(\bar A,\C)\) of
   Theorem~\ref{thm:u1-center-anomaly-open}.
\end{thm}
```

**Status.** Proposal-only, pending Phase-5 escalation and main-thread
adjudication. This document is **not** authorised to make manuscript
edits.

### §8.3 Manuscript impact assessment

The proposed Theorem G\textsuperscript{otr} would:
* **Not displace** the existing Theorem G (which is bosonic
  $\mathfrak{gl}_N$).
* **Add** a parallel anomaly on $\mathfrak{q}(N)$ in the odd-parity
  sector, sharing the same coefficient $N$ but in a different
  cohomology space.
* **Strengthen** the manuscript's central-extension story by
  documenting that the queer extension produces a new physical
  observable not seen in the bosonic case.

This aligns with the CLAUDE.md research-constellation role: the
$\mathfrak{q}(N)$ brane-probe extension is a structural finding for
the Vol III CY-to-chiral frontier, where parastatistics and
queer-supersymmetric extensions of the chiral algebra are natural.
**Cross-link to `~/calabi-yau-quantum-groups`: the Vol III queer
extensions of the chiral CY₃ algebra would couple to $[\bar c]^{\mathrm{otr}}$.**

---

## §9. Residuals + deciding evidence

### §9.1 Residuals

* **R-P4-G3-M3-Q-otr-01.** The signed parity-equivariance condition
  (A5)\textsuperscript{otr} is sketched here at the parametrix-level.
  Phase-5 work: characterise the full (A1)\textsuperscript{otr}–(A5)\textsuperscript{otr}
  admissibility class and verify Pauli–Villars / Hadamard parametrices
  satisfy it.
* **R-P4-G3-M3-Q-otr-02.** The higher-loop extension of the queer
  channel: $\mathrm{otr}(J^k)$ at odd $k$ contributes $(-1)^{(k-1)/2}N$.
  The all-loop class structure on $\mathfrak{q}(N)$ is then
  $\hbar^\ell\cdot N\cdot(\text{alternating signs})\cdot[\bar c]^{\mathrm{otr}}$
  at odd loop counts. Verify that the alternating-sign series sums to
  a non-trivial geometric series and identify its CE class.
* **R-P4-G3-M3-Q-otr-03.** The Capelli central element
  $Z_2^{\mathrm{otr}}$ on $\mathfrak{q}(N)$ acts on irreducibles via
  the Sergeev–Berele–Regev hook formula. Phase-5 work: compute the
  eigenvalue of $Z_2^{\mathrm{otr}}$ on the brane-probe Hilbert space
  and verify it matches the expected $\hbar N$ coefficient (Sergeev
  duality for q(N)–Hecke–Clifford).
* **R-P4-G3-M3-Q-otr-04.** Cross-link to the `~/calabi-yau-quantum-groups`
  Vol III chiral algebra. The queer extension of the chiral CY₃
  algebra (Cheng–Wang Ch. 6 catalog) couples to $[\bar c]^{\mathrm{otr}}$
  with coefficient $N$. Heuristic — convention-checking only at this
  stage; rigorous comparison requires a separate Phase-5 / Vol III
  embedding theorem (matched conventions per CLAUDE.md).
* **R-P4-G3-M3-Q-otr-05.** The orientifold / boundary-state
  interpretation: the $\Str$-channel and `otr`-channel correspond to
  two different boundary states. Identify the orientifold-projection
  rule that exchanges them and verify physical consistency. Phase-5
  cross-volume work.

### §9.2 Deciding evidence

The verdict that the queer trace **does not** discharge analogously
to the ordinary supertrace rests on two pieces of deciding evidence:

1. **The queer central element $J$ has $\mathrm{otr}(J)=N\neq 0$**
   (§2.2). Direct matrix computation, no model-dependence. This is
   parallel to the bosonic $\Tr(I)=N$ on $\mathfrak{gl}_N$.

2. **$J$ anticommutes with $P^{\mathfrak{q}}$ in the conjugation
   sense** (§3.3): $P^{\mathfrak{q}}\cdot J\cdot(P^{\mathfrak{q}})^{-1}=
   -J$. This is the algebraic source of (A5)-violation. Direct
   matrix computation.

These two facts are **structural** (depend only on the matrix
realization of $\mathfrak{q}(N)$, not on the choice of regulator) and
together imply the queer-channel discharge cannot proceed by the W22
mechanism. **The obstruction is canonical, not a regulator artefact.**

---

## §10. Phase-5 escalation conditions

### §10.1 Phase-5 escalation candidate: P4-EXEC-G3-M3 (this document)

**Status.** **NOT discharged.** Escalate to Phase-5 with
**Obs-Q-otr-A5** as the deciding obstruction.

**Two routes for Phase-5:**

**Phase-5-Q-A: Signed parity-equivariance route.** Define
(A5)\textsuperscript{otr} as the signed version
$\tau\Delta\tau^{-1}=-\Delta$ for parity-flipping $\tau$. Verify that
some admissible regulator class satisfies (A1)\textsuperscript{otr}–(A5)\textsuperscript{otr}.
Within that class, study the propagator-loop coefficient
$\mathrm{otr}(J^k)$ at all loop orders. **This route is unlikely to
produce a vanishing residue** because the central directions on
$\mathfrak{q}(N)$ have non-zero `otr`, but it is the natural
formalist extension of W22.

**Phase-5-Q-B: New anomaly route — Theorem G\textsuperscript{otr}.**
Accept that the queer channel produces a *new* anomaly class
$\hbar N[\bar c]^{\mathrm{otr}}$, independent of the bosonic Theorem
G. Document this as a parallel theorem in the manuscript. Cross-link
to the Vol III CY-to-chiral frontier where queer-supersymmetric
extensions are natural. **This route is a structural finding**, not a
discharge: it accepts the obstruction and reframes it as a new
physical observable.

**Recommended.** Phase-5-Q-B is the more honest path. Phase-5-Q-A is
formally well-defined but unlikely to discharge, since the
fundamental obstruction is the non-zero `otr` of the central element,
not the regulator class. The manuscript should record the queer
extension as a parallel theorem to G.

### §10.2 Conditions for Phase-5 escalation

Phase-5 work should be initiated if:
* **Vol III CY-to-chiral frontier** (`~/calabi-yau-quantum-groups`)
  starts using queer extensions of the chiral algebra — at that
  point the comparison with the present G\textsuperscript{otr}
  candidate becomes load-bearing.
* **Witten's parastatistics framework** is invoked in any paper
  interpretation from this manuscript, requiring an honest queer-anomaly
  story.
* **Boundary-state catalog** for $\mathfrak{q}(N)$ branes is
  completed; at that point the orientifold projection between the
  $\Str$ and `otr` channels needs a precise formulation.

### §10.3 Conditions for *not* escalating (i.e.\ closing as no-impact)

Phase-5 escalation is unnecessary if:
* The manuscript's main target is the **bosonic** $\mathfrak{gl}_N$
  Theorem G; the queer extension is acknowledged as a parallel result
  and recorded as a residual without inscription.
* No external reader / cross-volume work depends on the queer
  channel.

**Default disposition (this document).** Record the queer extension
as a residual; do not inscribe a new theorem in the manuscript at
this Phase-4 / EXEC stage. Phase-5 / Vol III decisions deferred to
the Vol III main-thread integration.

---

## §11. 200-word summary (for parent agent)

P4-EXEC-G3-M3 verdict: **The queer trace `otr` does NOT admit a
chain-level discharge analogous to W22-T1/T2 on gl(N|N).** The
deciding obstruction (Obs-Q-otr-A5): the queer central element
$J=((0,I),(-I,0))$ with $J^2=-I$ has $\mathrm{otr}(J)=\Tr(I_N)=N$
(non-zero), and $J$ anticommutes with the parity operator
$P^{\mathfrak q}=\diag(\mathbf 1_N,-\mathbf 1_N)$ in conjugation,
which breaks (A5) parity-equivariance. The queer-Capelli central
element $Z_2^{\mathrm{otr}}=\sum_{i,j}T_{ij}T_{ji}^{(\mathrm{odd})}+
T_{ji}^{(\mathrm{odd})}T_{ij}\in U(\mathfrak{q}(N))$ exists with **odd
parity**, parallel to but distinct from the gl-Capelli element. The
two-supertrace structure $(\Str, \mathrm{otr})$ on $\mathfrak q(N)$
produces **independent residue classes**: $\Str$ discharges (G3-M2);
`otr` produces a new $\hbar N[\bar c]^{\mathrm{otr}}\in H^2(\bar A,
\Pi\mathbb C)$ in the odd-parity sector, **not absorbed** by the
manuscript's Theorem G. Phase-5-Q-B recommended: accept the queer
anomaly as a parallel Theorem G\textsuperscript{otr}, cross-link to
Vol III CY-chiral frontier where queer extensions are natural.

**Report path:** `/Users/raeez/topological-strings/reconstitution/phase4-exec-G3-M3-queer-trace-2026-04-28.md`. Line count: 1108 lines.

End of P4-EXEC-G3-M3 ledger.
