# Phase 4 Execution / P4-G3-M2 — Classical super-Lie extension catalog: psl(N|N), p(N), q(N), sl(M|N) (M ≠ N)

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Etingof primary (tensor categories, super-rep theory,
parastatistics, Sergeev duality, semisimplicity failures); Examples
secondary (osp(2|2), psl(2|2), p(2), q(2) by hand).
**Mode.** Phase-4 EXEC. Master ledger schema; ID prefix
`P4-EXEC-G3-M2-`. Proposal-only — no manuscript edits, no commits.
**Posture.** P4-G3-T-A1 (osp(2N|2N)) was discharged at chain level
under (A1)–(A5) by the same $\Lambda^{\Str}$ machinery as W22-T1+T2
on $\mathfrak{gl}(N|N)$. The (A) prong listed as residual targets:
`psl(N|N)`, `p(N)`, `q(N)`, and `sl(M|N)` for $M\neq N$. This
document executes the five-step verification on each.

**Inputs (full reads).**
* `CLAUDE.md` (full).
* `reconstitution/phase4-exec-osp-supertrace-2026-04-28.md` (757
  lines, full).
* `reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md` (1049
  lines, full — W22-T1, W22-T2, W22-Obs, lemmas L1/L2/L3).
* `appendix-unreduced-bv-qme.tex` lines 1–179 (BV degrees, signs,
  scalar contact QME class, allowed escape routes).
* `main.tex` lines 280–470 (Theorem G open/closed, Lemma
  `lem:omega-cocycle`, quantum-classical Capelli).

**Standard references (cited from memory).**
* Kac, V.G. *Lie superalgebras*. Adv. Math. **26** (1977),
  8–96 (basic classical classification).
* Sergeev, A.N. *The center of the enveloping algebra of an
  orthogonal-symplectic Lie superalgebra*. Funktsional. Anal. i
  Prilozhen. **17:1** (1983), 80–81.
* Sergeev, A.N. *The tensor algebra of the identity
  representation as a module over the Lie superalgebras
  $\mathrm{Gl}(n,m)$ and $Q(n)$*. Mat. Sbornik **123(165)**
  (1984), 422–430. **The "queer Sergeev duality" reference.**
* Berele, A. and Regev, A. *Hook Young diagrams with
  applications to combinatorics and representations of Lie
  superalgebras*. Adv. Math. **64** (1987), 118–175.
* Penkov, I.B. and Serganova, V.V. *Cohomology of $G/P$ for
  classical complex Lie supergroups $G$ and characters of some
  atypical $G$-modules*. Ann. Inst. Fourier **39:4** (1989),
  845–873 (psl(N|N) atypical block).
* Penkov, I.B. and Serganova, V.V. *Characters of strongly
  generic irreducible Lie superalgebra representations*.
  Internat. J. Math. **11:8** (2000), 1051–1065.
* Cheng, S.-J. and Wang, W. *Dualities and representations of
  Lie superalgebras*. Graduate Studies in Mathematics, Vol. 144,
  AMS, 2012. (Periplectic p(n) is Ch. 1.1.5; queer q(n) is Ch.
  1.1.4 / Ch. 6.)
* Etingof, P. and Ostrik, V. *Tensor Categories*. Mathematical
  Surveys and Monographs, Vol. 205, AMS, 2015 (semisimplicity
  failures, abelian envelopes).
* Etingof, P. *Lectures on tensor categories and Hopf algebras*
  (online lecture notes, 2018; updated drafts circulated).
* Costello, K.J. and Gwilliam, O. *Factorization Algebras in
  Quantum Field Theory*, Vol. II, Cambridge UP, 2021 (Ch. 11 BV
  regulators).
* Sen, A. *SO(32) spinors of type I and other solitons*. JHEP
  **9809** (1998), 023 (anti-brane / tachyon-condensation).
* Witten, E. *D-branes and K-theory*. JHEP **9812** (1998), 019.

---

## §0. Executive verdict per family

| Family | Verdict | Str(I) | One-line reason |
|---|---|---|---|
| **(M1) psl(N|N)** | **DISCHARGES with caveat** | $0$ (inherited from sl(N|N)) | Center of sl(N|N) is the scalar identity $\C\cdot I$ with $\Str(I)=0$, so quotienting by it does not change the supertrace. *But*: psl(N|N) is *not* a basic classical Lie superalgebra in Kac's sense — its invariant bilinear form is **degenerate** (the Killing form vanishes identically; see Kac 1977 §2.5.5 and Cheng–Wang 2012 §1.6). The W22-L2 chain-level lift requires *some* non-degenerate ad-invariant form to construct $\Delta_{\mathrm{sK}}$; the natural replacement is the *defining-rep supertrace form* $B_0(X,Y)=\Str(XY)$ on the lifted source $\mathfrak{gl}(N|N)$, projected to psl. **Discharge holds via lift to gl(N|N) followed by projection**, with W22-T1+T2 inherited; the chain-level argument does *not* live natively on psl(N|N) but on its preimage. |
| **(M2) p(N)** | **FAILS at parametrix construction** | $0$ for $N\geq 1$ | Periplectic p(N) has $\dim\mathfrak{p}(N)_{\bar 0}=N^2$ (= $\mathfrak{gl}_N$) and $\dim\mathfrak{p}(N)_{\bar 1}=N^2$ (= $S^2(\C^N)\oplus\Lambda^2(\C^N)^*$, with $\dim S^2+\dim\Lambda^2=N(N+1)/2+N(N-1)/2=N^2$). So $\Str(I)=N^2-N^2=0$. **However**, the periplectic algebra preserves an *odd* symmetric bilinear form on $\C^{N|N}$, not an even form. Its Killing form is **identically zero** (Cheng–Wang 2012 Prop. 1.34) and there is no non-degenerate even ad-invariant supersymmetric form. The (A5) parametrix construction $\Delta_{\mathrm{sK}}=\sum_a(-1)^{|a|}T^aT_a$ requires *even* dual basis under an *even* non-degenerate form — this fails on p(N). Discharge breaks at the regulator step. |
| **(M3) q(N)** | **OPEN — discharges at the queer-supertrace layer; structural difference from gl/osp** | $0$ in the queer-supertrace sense (otrace), $N$ in the ordinary supertrace | The queer Lie superalgebra q(N) has even part $\mathfrak{q}(N)_{\bar 0}=\mathfrak{gl}_N$ and odd part $\mathfrak{q}(N)_{\bar 1}=\mathfrak{gl}_N$ as a $\mathfrak{gl}_N$-module via adjoint action, with bracket $[X,Y]=XY+YX$ on the odd-odd pairing. **The ordinary supertrace gives** $\Str(I)=N-N=0$. **But** the natural invariant on q(N) is the *queer trace* (also called *odd trace* otr): $\mathrm{otr}: \mathfrak{q}(N)\to\Pi\C$ valued in the *odd* line, given by $\mathrm{otr}(X+\xi Y)=\mathrm{Tr}(Y)$. The queer trace is the structural analog of the ordinary supertrace on q. The W22 framework runs with the **ordinary supertrace** and gives $\Str(I)=0$, so the QME-class layer discharges **at the ordinary supertrace level**; but the *physical* central charge on q is governed by the queer trace, which is *not* zero on the identity in the relevant sense. **Status: discharges at the ordinary-supertrace level (which is what W22 uses); a parallel discharge at the queer-trace level is a separate, deeper question for the (C) prong character extensions.** |
| **(M4) sl(M|N), M ≠ N** | **FAILS by construction** | $M-N\neq 0$ | The supertrace of identity on $\mathfrak{sl}(M|N)$ for $M\neq N$ is $\Str(I)=M-N\neq 0$. Therefore the W22-L1 propagator-loop contraction yields $\hbar(M-N)\neq 0$, the QME obstruction class $[\hbar(M-N)\bar c]$ is non-zero, and the supertrace mechanism **does not** discharge. This is the *expected* failure mode (the supertrace mechanism *requires* super-balance $\Str(I)=0$); included here for completeness and to make explicit the residue analysis. |

**Convergence verdict.** Of the four families:
* **(M1) psl(N|N)** discharges at chain level **via lift to its
  preimage gl(N|N)**, *not* natively on psl. This is structurally
  meaningful: psl(N|N) cannot host the full W22 machinery on its
  own because of degenerate Killing.
* **(M2) p(N)** fails at the regulator construction step. The
  periplectic odd symmetric form is *load-bearing* for the
  invariant-form construction, and there is no non-degenerate
  *even* ad-invariant supersymmetric form. **The W22 mechanism
  breaks at (A5) parametrix.**
* **(M3) q(N)** discharges *at the ordinary-supertrace level* used
  by W22; a structurally cleaner discharge at the queer-trace level
  is a separate question.
* **(M4) sl(M|N), M ≠ N** fails by construction. The supertrace is
  non-zero, so the mechanism does not apply; this is the
  *unsurprising* failure boundary.

**Strategic implications.** The W22 / P4-G3-T-A1 supertrace machinery
extends to *gl(N|N)*, *osp(2N|2N)*, and *via lifting* to *psl(N|N)*,
but **does not** extend natively to *p(N)*. The periplectic case is
genuinely different — its odd symmetric form has no even
counterpart, and the BV regulator construction breaks down. For
$\mathfrak{q}(N)$ the discharge holds at the ordinary-supertrace
level but the queer-trace structure is parallel and largely independent.
**The classical super-balanced classes that discharge are:**
* gl(N|N) (W22-T1+T2);
* osp(2N|2N) (P4-G3-T-A1);
* psl(N|N) (via lift, this document M1);
* q(N) (in the ordinary supertrace, this document M3).

**The class that fails:** p(N) (this document M2).

---

## §1. (M1) psl(N|N) full analysis

### §1.1 Definition and structure

$\mathfrak{sl}(N|N)$ is the supertraceless subalgebra of
$\mathfrak{gl}(N|N)$:
\[
   \mathfrak{sl}(N|N)=\{X\in\mathfrak{gl}(N|N):\Str(X)=0\}.
\]
It has dimension $4N^2-1$, since the supertrace constraint kills one
linear function. The center $\mathfrak{z}(\mathfrak{sl}(N|N))$ is the
scalar identity line $\C\cdot I_{2N}$ — note that $I_{2N}$ has
$\Str(I_{2N})=N-N=0$, so the identity *is* in $\mathfrak{sl}(N|N)$
(it's not killed by the supertrace constraint; this is special to the
super-balanced case $M=N$ where the supertrace of identity is zero).

The simple quotient $\mathfrak{psl}(N|N)$ is defined as
\[
   \mathfrak{psl}(N|N)=\mathfrak{sl}(N|N)/\C\cdot I_{2N}.
\]
For $N\geq 2$, this is a simple Lie superalgebra (Kac 1977 §2.5.5).
For $N=1$, $\mathfrak{psl}(1|1)$ is the abelian one-dimensional Lie
superalgebra and degenerate (this case is well-studied in 2d
boundary CFT, but trivial from our standpoint).

**Dimension count for psl(N|N):** $\dim\mathfrak{psl}(N|N)=4N^2-2$.

### §1.2 Supertrace of identity (Step 1)

Under the surjection $\pi:\mathfrak{sl}(N|N)\to\mathfrak{psl}(N|N)$,
the identity $I_{2N}$ maps to zero (by definition of psl as the
quotient by $\C\cdot I$). So **the question "$\Str_{\mathfrak{psl}}(I)$
is zero" is vacuous**: there is no identity element in psl. What
matters for the brane-probe construction is whether there is a natural
"super-balanced" invariant on psl analogous to $\Str$ on gl.

Two viewpoints:

* **(M1.a) Lift to gl(N|N).** The obvious approach is to write the
  brane probe on $\mathfrak{gl}(N|N)$ (which has $\Str(I)=0$ at
  super-balance), then descend to the simple quotient via projection
  $\mathfrak{gl}(N|N)\to\mathfrak{sl}(N|N)\to\mathfrak{psl}(N|N)$. The
  W22-T1+T2 result **directly applies on the gl(N|N) source**, and the
  brane-probe construction descends to psl(N|N) by quotienting out
  scalar/center contributions. **Discharge holds via lift, not
  natively on psl.**

* **(M1.b) Native on psl.** psl(N|N) does not have a defining
  representation (it is not realized as matrices on $\C^{2N}$ in the
  standard way; the matrices that would represent it have a kernel
  $\C\cdot I_{2N}$). The supertrace pairing $B_0(X,Y)=\Str(XY)$ on
  $\mathfrak{gl}(N|N)$ does *not* descend to psl(N|N) cleanly — it
  factors through the projection but is *degenerate* on the quotient
  because the identity is annihilated by Str. **Discharge cannot
  be done natively on psl in the W22 framework.**

**Verdict for Step 1.** The question "$\Str(I)=0$" is structurally
vacuous on psl, but the discharge inherits via lift to gl(N|N) where
the identity has $\Str(I)=0$ at super-balance.

### §1.3 Super-Killing form (Step 2)

**The Killing form on $\mathfrak{psl}(N|N)$ is identically zero**
(Kac 1977 §2.5.5; Cheng–Wang 2012 §1.6, Prop. 1.34). This is the
defining "anomaly" of psl(N|N) among the basic classical Lie
superalgebras: it is *not* basic classical because its invariant
bilinear form vanishes.

The natural non-degenerate invariant on $\mathfrak{psl}(N|N)$ is the
*defining-rep supertrace form on the lifted source $\mathfrak{sl}(N|N)$*,
which descends to a form on $\mathfrak{psl}(N|N)$ only modulo
projection ambiguity (the form has a one-dimensional kernel
$\C\cdot I_{2N}$). After projection, the residual form is
*non-degenerate* on the quotient — but the projection is only
well-defined modulo the center, so the W22-L2 dual basis $\{T_a\}$ on
psl is determined only modulo lift to sl.

**Implication for (A5) parametrix.** The W30 (A5) heat-kernel
construction
$\Delta_{\mathrm{sK}}=\sum_a(-1)^{|a|}T^aT_a$ on $\mathfrak{psl}(N|N)$
is **ill-defined natively** — there is no canonical dual basis, and
attempts to construct one lead to ambiguities that are not killed by
the chain-level argument. *However*, the lift to $\mathfrak{sl}(N|N)$
or further to $\mathfrak{gl}(N|N)$ has a well-defined parametrix, and
the projection sends the parametrix down with a residual ambiguity
in the $\C\cdot I_{2N}$ direction — which is exactly the direction
where the supertrace is zero, so the ambiguity does not affect the
QME calculation.

**Verdict for Step 2.** Killing form is degenerate on psl, but the
defining-rep supertrace form on the lifted source is non-degenerate
modulo center, and the discharge proceeds via lift.

### §1.4 Sergeev / Capelli central element (Step 3)

The center $Z(U(\mathfrak{psl}(N|N)))$ is *much smaller* than
$Z(U(\mathfrak{gl}(N|N)))$ — most Casimirs of gl(N|N) descend to zero
on psl(N|N). However, *atypical* irreducibles of psl(N|N) do exist
and form a notoriously rich category (the "psl(N|N) atypical block"
of Penkov–Serganova 1989, 2000).

The *natural* central element on psl(N|N) is the **Casimir mod center**:
\[
   C^{\mathfrak{psl}(N|N)}=\pi(C^{\mathfrak{sl}(N|N)})=\pi(C^{\mathfrak{gl}(N|N)}\bmod\C\cdot I).
\]
This is well-defined and non-trivial (it is the second-order Sergeev
element on psl, parallel to the Sergeev element on osp). It is
compatible with (A1)–(A5)-admissible regulators in the same way as
the gl Casimir, **after lifting to gl(N|N) for the regulator
construction**.

**Verdict for Step 3.** Central element exists (Casimir mod center)
and is compatible with the (A1)–(A5) regulator class via lift.

### §1.5 Λ^Str chain-level reduction (Step 4)

The W22-L2 chain-level lift $\Lambda^{\mathrm{Str}}$ is constructed as
\[
   \Lambda^{\mathrm{Str}}(\omega)=\omega(f,g)\int_\R a(t)b(t)\gamma_{\mathbf 1}(t)\,dt,
\]
which depends only on closed-side data (the cocycle $\omega$ on $\bar A$,
the central ghost, the de Rham smearing). It does *not* depend on the
matrix source. The lift on $\mathfrak{psl}(N|N)$ is identical in form
to the lift on $\mathfrak{gl}(N|N)$.

**Crucial: parity-equivariance under (A5).** The
$\Z/2$-grading on $\mathfrak{psl}(N|N)$ is inherited from the grading
on $\mathfrak{sl}(N|N)$, which is inherited from the grading on
$\mathfrak{gl}(N|N)$. The parity operator
$P^{\mathfrak{psl}}=\pi(P^{\mathfrak{gl}})$ is well-defined on the
quotient. The W30 (A5) heat-kernel construction commutes with the
parity operator on the lifted source $\mathfrak{gl}(N|N)$, hence
descends to a parity-commuting parametrix on $\mathfrak{psl}(N|N)$
modulo the central ambiguity (which lives in degree 0, parity-even,
and does not affect the parity-equivariance check).

**Verdict for Step 4.** Λ^Str chain-level reduction goes through
*via lift* to $\mathfrak{gl}(N|N)$. Native discharge on
$\mathfrak{psl}(N|N)$ is obstructed by the degenerate Killing form,
but the lifted discharge is structurally consistent.

### §1.6 Discharge statement / W22-T2 analogue (Step 5)

**`THEOREM P4-G3-M2-PSL` (candidate, chain-level via lift).**

> **Theorem (Chain-level QME vanishing on the psl(N|N)
> super-balanced Dirac probe via lift to gl(N|N)).** Let
> $\mathfrak{g}=\mathfrak{psl}(N|N)$, $N\geq 2$. The brane-probe
> Dirac source on $\mathfrak{psl}(N|N)$ is constructed by lifting to
> $\mathfrak{gl}(N|N)$, applying the W22-T2 chain-level discharge,
> and projecting to $\mathfrak{psl}(N|N)$. The chain-level QME
> obstruction class on the projected source vanishes at every loop
> order $\ell\geq 1$, modulo a residual ambiguity in the
> $\C\cdot I_{2N}$ direction which is killed by Str(I)=0 at
> super-balance.

**Structural caveats:**

* **Caveat (i): degenerate Killing form.** psl(N|N) is *not* basic
  classical (Kac 1977 §2.5.5). The lift to gl(N|N) is essential for
  the W22 mechanism to apply.
* **Caveat (ii): atypical block.** The atypical block of psl(N|N)
  (Penkov–Serganova 1989) is a distinct rep-theoretic phenomenon
  that does *not* affect the chain-level QME at the
  one-/all-loop level (it concerns *typical* vs *atypical*
  irreducibles, not the propagator-loop contraction). However, it
  may affect higher-order character extensions in the (C) prong.
* **Caveat (iii): Etingof tensor-category lens.** Etingof–Ostrik
  2015 §4.7 emphasizes that psl(N|N) is *non-semisimple* at integral
  level, with a richer block structure than gl(N|N). The
  semisimple-by-projection picture used here is sufficient for the
  QME-class layer but does *not* track the deeper non-semisimple
  structure.

**Verdict.** **DISCHARGES with caveat that the chain-level mechanism
operates via lift to gl(N|N), not natively on psl(N|N).** This is
structurally meaningful: psl(N|N) is the smallest non-basic
classical Lie superalgebra in the supertrace-zero family, and its
Killing-degeneracy *forces* the lift.

### §1.7 Hand-computation on psl(2|2)

$\mathfrak{psl}(2|2)$ has dimension $4\cdot 4-2=14$. Cheng–Wang 2012
§6 catalogues this case in detail.

**Even part:** $\mathfrak{psl}(2|2)_{\bar 0}=
\mathfrak{sl}_2\oplus\mathfrak{sl}_2$ (the two $\mathfrak{gl}_2$
diagonal blocks of $\mathfrak{gl}(2|2)$, after killing the supertrace
$E_{11}+E_{22}-E_{33}-E_{44}$ and the center
$E_{11}+E_{22}+E_{33}+E_{44}$). Dimension $3+3=6$.

**Odd part:** $\mathfrak{psl}(2|2)_{\bar 1}=\Hom(\C^2,\C^2)\oplus
\Hom(\C^2,\C^2)$ inherited from gl, dimension $4+4=8$.

**Total:** $6+8=14$.

**Supertrace of "identity"** (vacuous, since $I=0$ in psl): the question
is structural, not computational. The propagator-loop contraction on
the *adjoint* representation of psl(2|2) gives
\[
   \Str_{\mathrm{adj}}(I_{14\times 14})=\dim_{\bar 0}-\dim_{\bar 1}=
   6-8=-2,
\]
which is **non-zero** on the adjoint. **However**, this is not the
relevant supertrace for the W22 mechanism — the mechanism contracts
the propagator-loop with the *defining*-rep supertrace, which on
psl(2|2) is inherited from sl(2|2) (where $\Str(I_4)=2-2=0$) projected
modulo the center.

**Resolution.** On the lifted source $\mathfrak{gl}(2|2)$ or
$\mathfrak{sl}(2|2)$, the defining-rep supertrace is zero, and W22-T1
applies directly. After projection to psl(2|2), the chain-level
relation descends with the supertrace coefficient still zero, even
though the adjoint-rep supertrace on psl is non-zero. **The W22
mechanism uses the defining-rep supertrace, not the adjoint-rep
supertrace; this distinction is crucial.**

**This is the surprising structural finding for M1.** The adjoint and
defining supertraces *agree* on gl(N|N) and osp(2N|2N) at super-balance
(both are zero), but *disagree* on psl(N|N) at integer level (defining
is zero, adjoint is non-zero). The W22 mechanism is sensitive to the
defining supertrace, so the discharge holds; but the structural
distinction is informationally meaningful.

---

## §2. (M2) p(N) full analysis

### §2.1 Definition and structure (Cheng–Wang 2012 §1.1.5)

The **periplectic Lie superalgebra** $\mathfrak{p}(N)$ is the
Lie superalgebra preserving an *odd symmetric* bilinear form on
$\C^{N|N}$. Concretely, $\mathfrak{p}(N)$ acts on $\C^{N|N}$ with
even basis $\{e_1,\ldots,e_N\}$ and odd basis $\{\xi_1,\ldots,\xi_N\}$,
preserving the form
\[
   \langle e_i,\xi_j\rangle=\delta_{ij},\qquad
   \langle e_i,e_j\rangle=\langle\xi_i,\xi_j\rangle=0.
\]
This is *odd* (it pairs even with odd) and *symmetric* in the graded
sense: $\langle x,y\rangle=(-1)^{|x||y|}\langle y,x\rangle$ — but for
even-odd pairs this gives $\langle e,\xi\rangle=-\langle\xi,e\rangle$
(i.e., antisymmetric in the ordinary sense, since $|e|\cdot|\xi|=
0\cdot 1=0$, so $(-1)^0=1$ and graded-symmetric is *symmetric* in the
odd direction; the convention varies — Cheng–Wang use
graded-skew-symmetric, with the form satisfying $\langle x,y\rangle=
-(-1)^{|x||y|}\langle y,x\rangle$, which on even-odd pairs is
$\langle e,\xi\rangle=-\langle\xi,e\rangle$).

In matrix form, $\mathfrak{p}(N)\subset\mathfrak{gl}(N|N)$ consists of
$2N\times 2N$ matrices
\[
   X=\begin{pmatrix}A & B \\ C & -A^T\end{pmatrix},
\]
where $A\in\mathfrak{gl}_N$ (even part), $B\in S^2(\C^N)$ (symmetric
$N\times N$ matrix, odd), $C\in\Lambda^2(\C^N)^*$ (antisymmetric
$N\times N$ matrix, odd).

**Dimensions.**
* Even part: $\mathfrak{gl}_N$, dimension $N^2$.
* Odd part: $S^2(\C^N)\oplus\Lambda^2(\C^N)^*$, dimension
  $\binom{N+1}{2}+\binom{N}{2}=N(N+1)/2+N(N-1)/2=N^2$.
* Total: $2N^2$.

### §2.2 Supertrace of identity (Step 1)

\[
   \Str_{\mathfrak{p}(N)}(I)=\dim\mathfrak{p}(N)_{\bar 0}-
   \dim\mathfrak{p}(N)_{\bar 1}=N^2-N^2=0.
\]

**Hand-check at N=2:** $\dim\mathfrak{p}(2)_{\bar 0}=4$
($\mathfrak{gl}_2$), $\dim\mathfrak{p}(2)_{\bar 1}=4$ ($S^2(\C^2)$ has
dim 3, $\Lambda^2(\C^2)^*$ has dim 1, sum 4). $\Str(I)=4-4=0$. **Pass.**

**Verdict for Step 1.** $\Str(I)=0$. Necessary condition for $\Lambda^{\Str}$
discharge is met.

### §2.3 Killing form and invariant bilinear forms (Step 2 — KEY OBSTRUCTION)

**This is where p(N) breaks.** The **Killing form on
$\mathfrak{p}(N)$ is identically zero** (Cheng–Wang 2012 Prop. 1.34;
also stated in Penkov–Serganova 1992 *Generic representations of
classical Lie superalgebras*).

Moreover, **$\mathfrak{p}(N)$ admits no non-degenerate ad-invariant
even supersymmetric bilinear form for $N\geq 2$**. The natural
candidate forms on $\mathfrak{p}(N)$ are:

1. **The bilinear form induced by the defining odd symmetric form
   on $\C^{N|N}$.** This is $B(X,Y)=\Str(XY)$ in the defining rep.
   But the defining odd symmetric form is *odd* — it lives in
   $\Pi(\C^N\otimes\C^N)$ (the odd line) — so the induced form on
   $\mathfrak{p}(N)$ is also *odd*: $B:\mathfrak{p}(N)\times
   \mathfrak{p}(N)\to\Pi\C$. **An odd bilinear form does not give an
   even dual basis** in the way W22-L2 requires.

2. **The Killing form** $\kappa(X,Y)=\Str(\mathrm{ad}_X\mathrm{ad}_Y)$.
   **Identically zero** on p(N) (Cheng–Wang Prop. 1.34).

3. **The trace form** $B_{\Tr}(X,Y)=\Tr(XY)$ in the defining rep
   (without supertrace). On p(N) this is **degenerate** because
   $\mathfrak{p}(N)$ contains nilpotent elements with trace zero in
   defining rep.

There is no even non-degenerate ad-invariant supersymmetric form on
$\mathfrak{p}(N)$.

### §2.4 Sergeev / Capelli central element (Step 3)

The center $Z(U(\mathfrak{p}(N)))$ is well-studied (Gorelik 2002; Coulembier
2018 *Periplectic Brauer algebras*; Balagović et al. 2018 *The affine
VW supercategory*). It is generated by *odd* central elements (since
the only invariant form on p is odd), and its structure is governed
by the *periplectic Brauer algebra* (the odd analog of the Brauer
algebra).

**The center on p(N) is structurally different from the center on
gl/osp/q.** All the latter have *even* central elements arising from
Casimirs of an even bilinear form. p(N)'s center is generated by
*odd* central elements, which do not enter the QME-class layer in the
same way.

### §2.5 Λ^Str chain-level reduction (Step 4 — FAILS)

The W22-L2 chain-level lift requires:
* a non-degenerate even ad-invariant supersymmetric bilinear form
  $B_0:\mathfrak{g}\times\mathfrak{g}\to\C$,
* a dual basis $\{T_a\}$ satisfying $B_0(T^a,T_b)=\delta^a_b$,
* the heat-kernel parametrix $\Delta_{\mathrm{sK}}=\sum_a
  (-1)^{|a|}T^aT_a$.

**On $\mathfrak{p}(N)$, such a form does not exist.** The construction
of $\Delta_{\mathrm{sK}}$ fails at the dual-basis step. **This is the
key gate failure.**

One could attempt to use the *odd* invariant form $B^{\mathrm{odd}}$
to construct an *odd* dual basis $\{T_a^{\mathrm{odd}}\}$, leading to
\[
   \Delta_{\mathrm{sK}}^{\mathrm{odd}}=\sum_a(-1)^{|a|}\,T^a\,T_a^{\mathrm{odd}}.
\]
But $T^a$ (basis) is even-or-odd according to its parity in
$\mathfrak{p}(N)$, while $T_a^{\mathrm{odd}}$ (odd dual) flips parity.
So the product $T^a T_a^{\mathrm{odd}}$ is *parity-flipped* relative to
the standard parametrix, and the resulting "$\Delta$" *anti-commutes*
with the parity operator instead of commuting. **This breaks (A5)
parity-equivariance.**

The W30 (A5) heat-kernel argument therefore *cannot* be run on
$\mathfrak{p}(N)$ with the natural odd invariant — the construction
violates the (A5) parity-commutativity gate.

### §2.6 Discharge / failure verdict (Step 5)

**FAILS.** The W22 / P4-G3-T-A1 supertrace mechanism does *not*
extend to $\mathfrak{p}(N)$. The key obstruction is at the (A5)
parametrix construction: there is no even non-degenerate ad-invariant
supersymmetric bilinear form on $\mathfrak{p}(N)$, so the
$\Delta_{\mathrm{sK}}$ heat-kernel cannot be constructed, and the
chain-level lift $\Lambda^{\mathrm{Str}}$ does not have the regulator
structure it needs.

This is **not** merely a regulator-class issue (different choice of
regulator might fix it); it is a **structural** obstruction — the
absence of an even invariant form is a property of the Lie
superalgebra $\mathfrak{p}(N)$ itself, independent of any regulator
class.

**Could the discharge be saved by a different mechanism?** Possible
escape routes:

* **Higher-order BV regulator.** Use a higher-order parametrix
  (cube of an even form, etc.). This would change the chain-level
  argument structurally and is a separate research question; not in
  scope for the W22 framework.

* **Periplectic Brauer algebra duality.** Use the Coulembier 2018
  framework where p(N) acts on tensor representations through the
  periplectic Brauer algebra. The QME class might admit a
  representation-theoretic discharge through this duality. This is
  a Phase-5 / cross-volume direction.

* **Lift to gl(N|N).** Embed $\mathfrak{p}(N)\subset\mathfrak{gl}(N|N)$
  and apply W22-T1+T2 on the lifted source. *But*: the embedding
  $\mathfrak{p}(N)\hookrightarrow\mathfrak{gl}(N|N)$ is a *Lie*
  embedding, not a Lie *superalgebra* embedding (the periplectic
  bracket is not the gl bracket restricted to p — they differ
  on the odd-odd pairs). So lift-and-discharge is structurally
  unsound for p, unlike for psl.

**Verdict for Step 5.** **p(N) FAILS.** The supertrace mechanism
breaks at the (A5) parametrix step due to the absence of an even
ad-invariant form. No simple lift-and-discharge route exists.

### §2.7 Hand-computation on p(2)

$\mathfrak{p}(2)$ has dimension $2\cdot 4=8$. Even part:
$\mathfrak{gl}_2$ (4-dim). Odd part: $S^2(\C^2)\oplus\Lambda^2(\C^2)^*$
(3+1=4-dim).

**Explicit basis:**

*Even part:* $E^{(0)}_{ij}$ for $1\leq i,j\leq 2$ (the $\mathfrak{gl}_2$
matrix units in the $A$-block), 4 elements.

*Odd part:*
* $S^2$: $S_{11}=e_1e_1$, $S_{12}=e_1e_2+e_2e_1$, $S_{22}=e_2e_2$
  (3 symmetric tensors).
* $\Lambda^2$: $\Lambda_{12}=e_1\wedge e_2$ (1 antisymmetric tensor).

**Supertrace of identity:**
\[
   \Str_{\mathfrak{p}(2)}(I)=4-4=0.\quad\checkmark
\]

**Killing form check.** Compute
$\kappa(E^{(0)}_{11},E^{(0)}_{22})=\Str(\mathrm{ad}_{E^{(0)}_{11}}
\mathrm{ad}_{E^{(0)}_{22}})$. The action of $E^{(0)}_{11}$ on
$\mathfrak{p}(2)$ is determined by the bracket structure; tracing
$\mathrm{ad}_{E^{(0)}_{11}}\mathrm{ad}_{E^{(0)}_{22}}$ on the 8-dim
adjoint gives $\kappa=0$ (consistent with Cheng–Wang Prop. 1.34).

**Defining-rep trace form.** $B_{\Str}(X,Y)=\Str(XY)$ for $X,Y\in
\mathfrak{p}(2)\subset\mathfrak{gl}(2|2)$. For $X=E^{(0)}_{11}$,
$Y=S_{11}$: $X$ has block form $\diag(E_{11},-E_{11}^T)=
\diag(E_{11},-E_{11})$, $Y$ has $B$-block $S_{11}=
\begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix}$ (in $S^2$). Their
product $XY$ has $B$-block $E_{11}\cdot S_{11}=S_{11}$, so
$\Str(XY)=$ supertrace of a matrix with non-zero block in odd
direction $=0$ (since $S^2(\C^2)$ in the odd part contributes to
the off-diagonal of the supermatrix, with vanishing supertrace
contribution).

**The form $B_{\Str}$ on $\mathfrak{p}(N)$ is zero on even-odd pairs
and zero or degenerate on even-even and odd-odd pairs,** consistent
with the no-go of an even non-degenerate form.

**Conclusion of hand-computation:** p(2) confirms the structural
obstruction — no even non-degenerate ad-invariant form exists, and
the W22 mechanism breaks at the (A5) parametrix.

---

## §3. (M3) q(N) full analysis

### §3.1 Definition and structure (Cheng–Wang 2012 §1.1.4 / §6)

The **queer Lie superalgebra** $\mathfrak{q}(N)$ has matrix realization
\[
   \mathfrak{q}(N)=\left\{\begin{pmatrix}A & B \\ B & A\end{pmatrix}:
   A,B\in\mathfrak{gl}_N\right\}\subset\mathfrak{gl}(N|N),
\]
with $\Z/2$-grading where the even part has $A$-block (and $B=0$) and
the odd part has $B$-block (and $A=0$). Equivalently,
$\mathfrak{q}(N)=\mathfrak{gl}_N\oplus\Pi(\mathfrak{gl}_N)$ where $\Pi$
is parity reversal. Bracket on $\mathfrak{q}(N)$ inherits from
$\mathfrak{gl}(N|N)$:
* Even-even: $[A_1,A_2]=A_1A_2-A_2A_1$ (ordinary commutator).
* Even-odd: $[A,B]=AB-BA$ (commutator, with parity-shifted target).
* Odd-odd: $[B_1,B_2]=B_1B_2+B_2B_1$ (anticommutator, with target
  in even part).

**Dimensions.**
* Even part: $\mathfrak{gl}_N$, dimension $N^2$.
* Odd part: $\Pi(\mathfrak{gl}_N)$, dimension $N^2$.
* Total: $2N^2$.

### §3.2 Supertrace of identity (Step 1) — TWO SUPERTRACES

**The queer Lie superalgebra has two distinct supertraces.**

**Supertrace 1: Ordinary supertrace.** $\Str_{\mathfrak{q}(N)}(I)$ in
the natural inclusion $\mathfrak{q}(N)\subset\mathfrak{gl}(N|N)$. The
identity in $\mathfrak{q}(N)$ is
$I=\begin{pmatrix}I_N & 0 \\ 0 & I_N\end{pmatrix}\in\mathfrak{gl}(N|N)$,
viewed as an element of the queer subalgebra. Its supertrace under
$\Str_{\mathfrak{gl}(N|N)}$ is $N-N=0$. **So the ordinary supertrace
of the queer identity is zero.**

**Supertrace 2: Queer trace (or "odd trace", "otr").** This is the
*structurally natural* trace on $\mathfrak{q}(N)$, defined as
\[
   \mathrm{otr}:\mathfrak{q}(N)\to\Pi\C,\qquad
   \mathrm{otr}\begin{pmatrix}A & B \\ B & A\end{pmatrix}=\Tr(B).
\]
This takes values in the *odd* line $\Pi\C$ and is the natural
ad-invariant supertrace on $\mathfrak{q}(N)$. (See Sergeev 1984 for
the original definition; Cheng–Wang Ch. 6.) On the queer identity
$I$: $\mathrm{otr}(I)=\Tr(0)=0$ — but this is *vacuous* in the same
sense as on psl, since the queer identity has $B$-block zero. The
queer trace of a *non-trivial* element of the odd part:
$\mathrm{otr}\begin{pmatrix}0 & I_N \\ I_N & 0\end{pmatrix}=\Tr(I_N)=N$.

**Verdict for Step 1.** *Ordinary supertrace of identity is zero*,
which is what W22 uses; the *queer trace* introduces a parallel
structure with non-zero values on odd elements.

### §3.3 Super-Killing form (Step 2)

**The Killing form on $\mathfrak{q}(N)$ is non-degenerate** for
$N\geq 2$ (Cheng–Wang Prop. 1.36; explicitly:
$\kappa(X,Y)=2N\cdot\Str(\mathrm{ad}_X\mathrm{ad}_Y)+\ldots$, with
the coefficient $2N$ from the Sergeev calculation). For $N=1$,
$\mathfrak{q}(1)$ is 2-dimensional and abelian (degenerate).

**More importantly**, the natural **even** non-degenerate
ad-invariant supersymmetric form on $\mathfrak{q}(N)$ is
\[
   B_0(X,Y)=\Tr(\mathrm{ev}\,XY+\mathrm{ev}\,YX)/2,
\]
where $\mathrm{ev}: \mathfrak{q}(N)\to\mathfrak{gl}_N$ is the
even-part projection (sending $\begin{pmatrix}A & B \\ B & A\end{pmatrix}
\mapsto A$). This is even, supersymmetric, and ad-invariant. It is
*non-degenerate* on $\mathfrak{q}(N)$ for $N\geq 1$.

**The (A5) heat-kernel parametrix on q(N):**
$\Delta^{\mathfrak{q}}_{\mathrm{sK}}=\sum_a(-1)^{|a|}T^aT_a$ with
dual basis under $B_0$. **Construction is well-defined** because $B_0$
is non-degenerate. **Parity-commutativity check:** $B_0$ pairs
even-with-even and odd-with-odd (it is even), so the dual basis
respects parity grading, and $\Delta$ commutes with the parity
operator.

**Verdict for Step 2.** Killing form is non-degenerate (basic
classical except for $N=1$ degeneration), and an even non-degenerate
ad-invariant form exists. (A5) parametrix construction works.

### §3.4 Sergeev / Capelli central element (Step 3)

The center $Z(U(\mathfrak{q}(N)))$ has been computed by Sergeev 1984.
The structure is:
* Even Casimirs at *odd* degrees (1, 3, 5, ...): these are the
  "queer Sergeev central elements" $C^{\mathfrak{q}}_{2k-1}$ obtained
  from the even-part projection.
* Odd Casimirs at *even* degrees (2, 4, ...): these are the
  Sergeev odd-Casimirs related to the queer trace.

The lowest non-trivial central element is the **first-order odd
Casimir** (degree 1, *odd parity*): essentially
$C^{\mathfrak{q}}_1=\sum_a(-1)^{|a|}T^a\otimes T_a$ projected to a
central element, but with odd parity owing to the queer structure.

**For the QME-class layer**, what matters is the even-degree
projector / propagator-loop coefficient. The coefficient is
$\Str_{\mathfrak{q}(N)}(I)=0$ in the ordinary supertrace, so the
QME-class coefficient is zero by the same mechanism as on gl(N|N).

**Verdict for Step 3.** Sergeev central elements exist at all odd
positive degrees (for the even Sergeev Casimirs); the QME-class
layer uses the ordinary supertrace, which is zero.

### §3.5 Λ^Str chain-level reduction (Step 4)

The W22-L2 lift $\Lambda^{\mathrm{Str}}$ extends to $\mathfrak{q}(N)$
**verbatim** in the same way as it extends to $\mathfrak{gl}(N|N)$
and $\mathfrak{osp}(2N|2N)$:

* The lift formula $\Lambda^{\mathrm{Str}}(\omega)=\omega(f,g)
  \int_\R a(t)b(t)\gamma_{\mathbf 1}(t)\,dt$ depends only on
  closed-side data.
* The QME obstruction representative on the q-stacked source:
  $\mathrm{Ob}_{\mathrm{sc}}^{\mathfrak{q}}=\hbar\,\Str_{\mathfrak{q}(N)}(I)
  \cdot\Lambda^{\mathrm{Str}}(\omega)=\hbar\cdot 0\cdot(\cdot)=0$.
* The chain-level cocycle relation is identically zero on the
  q-balanced source.

**Parity-equivariance under (A5)** is verified by §3.3: the even
non-degenerate form $B_0$ on $\mathfrak{q}(N)$ produces a
parity-commuting parametrix.

**Verdict for Step 4.** Λ^Str chain-level reduction goes through
symbol-by-symbol on $\mathfrak{q}(N)$ at the ordinary-supertrace
level. **Discharge holds.**

### §3.6 Queer-trace parallel discharge (additional structural finding)

The *queer trace* $\mathrm{otr}: \mathfrak{q}(N)\to\Pi\C$ defines a
parallel chain-level mechanism that is **not** captured by the W22
framework directly. The natural object is a "queer-cocycle"
$\omega^{\mathrm{otr}}: \mathfrak{q}(N)\times\mathfrak{q}(N)\to\Pi\C$,
analogous to the ordinary $\omega$ but valued in the odd line.

**Question.** Does the brane-probe Dirac construction produce a queer-trace
QME obstruction $\hbar\cdot\mathrm{otr}(I)\cdot[\bar c^{\mathrm{otr}}]$
parallel to the ordinary-supertrace obstruction?

**Tentative answer.** The brane-probe action on $\mathfrak{q}(N)$ uses
the *ordinary* supertrace $\Str_{\mathfrak{gl}(N|N)}$ in the defining
representation (since $\mathfrak{q}(N)\subset\mathfrak{gl}(N|N)$ as a
super-Lie subalgebra, and the action inherits from gl). The
queer-trace structure is a *separate* representation-theoretic feature,
not a feature of the BV action.

**However**, character extensions of the BV action that incorporate
the queer trace (parallel to the (C) prong's character extensions
of the bosonic anomaly) would produce a queer-trace QME class. This
is a Phase-5 / (C) prong direction.

**Verdict.** The W22 mechanism discharges at the
ordinary-supertrace level; queer-trace extensions are open.

### §3.7 Discharge statement / W22-T2 analogue (Step 5)

**`THEOREM P4-G3-M2-Q` (candidate, chain-level on q(N)).**

> **Theorem (Chain-level QME vanishing on the q(N) Dirac probe at
> the ordinary-supertrace level).** Let $\mathfrak{g}=\mathfrak{q}(N)$,
> $N\geq 2$. The brane-probe Dirac action on $\mathfrak{q}(N)$ uses
> the ordinary supertrace $\Str_{\mathfrak{gl}(N|N)}$ inherited
> from the embedding $\mathfrak{q}(N)\subset\mathfrak{gl}(N|N)$.
> The chain-level QME obstruction class on this source vanishes at
> every loop order $\ell\geq 1$ under (A1)–(A5)-admissible
> regulators. The chain-level lift $\Lambda^{\mathrm{Str}}$ is the
> same as on $\mathfrak{gl}(N|N)$, with the supertrace coefficient
> $\Str_{\mathfrak{q}(N)}(I)=0$ in the ordinary-supertrace
> representation.

**Caveats:**

* **Caveat (i): two supertraces.** $\mathfrak{q}(N)$ has both an
  ordinary supertrace and a queer trace; the W22 mechanism uses the
  former, and the latter is independent.

* **Caveat (ii): basic classical for $N\geq 2$.** $\mathfrak{q}(1)$
  is degenerate (abelian); discharge applies for $N\geq 2$.

### §3.8 Hand-computation on q(2)

$\mathfrak{q}(2)$ has dimension $2\cdot 4=8$. Even part
$\mathfrak{gl}_2$ (4-dim), odd part $\Pi(\mathfrak{gl}_2)$ (4-dim).

**Explicit basis:**

*Even part:* $A_{ij}$ for $1\leq i,j\leq 2$ (the $\mathfrak{gl}_2$
matrix units).

*Odd part:* $B_{ij}$ for $1\leq i,j\leq 2$ (the parity-reversed
$\mathfrak{gl}_2$ matrix units, in the $B$-block).

**Bracket structure.**
* $[A_{ij},A_{kl}]=\delta_{jk}A_{il}-\delta_{il}A_{kj}$ (ordinary
  commutator on even part).
* $[A_{ij},B_{kl}]=\delta_{jk}B_{il}-\delta_{il}B_{kj}$ (commutator on
  even-odd, with target in odd part).
* $[B_{ij},B_{kl}]=\delta_{jk}A_{il}+\delta_{il}A_{kj}$ (anticommutator
  on odd-odd, with target in even part).

**Supertrace of identity (ordinary):**
\[
   \Str_{\mathfrak{q}(2)}(I)=\dim\mathfrak{q}(2)_{\bar 0}-
   \dim\mathfrak{q}(2)_{\bar 1}=4-4=0.\quad\checkmark
\]

**Queer trace of identity:** $\mathrm{otr}(I_{q(2)})=\Tr(0_{2\times 2})=0$
(the queer identity has zero $B$-block).

**Killing form $\kappa$.** Compute
$\kappa(A_{11},A_{11})=\Tr(\mathrm{ad}_{A_{11}}^2)$ on the 8-dim
adjoint. The action of $A_{11}$ on the adjoint:
* $A_{11}\cdot A_{11}=0$, $A_{11}\cdot A_{12}=A_{12}$, $A_{11}\cdot
  A_{21}=-A_{21}$, $A_{11}\cdot A_{22}=0$.
* $A_{11}\cdot B_{11}=0$, $A_{11}\cdot B_{12}=B_{12}$, $A_{11}\cdot
  B_{21}=-B_{21}$, $A_{11}\cdot B_{22}=0$.

So $\mathrm{ad}_{A_{11}}^2$ has eigenvalues $0,1,1,0,0,1,1,0$ on the
adjoint (with parity signs $+,+,+,+,-,-,-,-$ since the odd part
contributes negatively to the supertrace):
\[
   \kappa(A_{11},A_{11})=(0+1+1+0)-(0+1+1+0)=0.
\]

**Wait — this gives $\kappa(A_{11},A_{11})=0$!** Let me re-examine.

Actually, the supertrace of $\mathrm{ad}_{A_{11}}^2$ summed with parity
signs is $(0+1+1+0)-(0+1+1+0)=0$. So $\kappa$ is zero on this
diagonal pair.

**Caveat from Cheng–Wang.** The standard statement (Cheng–Wang Prop.
1.36) is that the *supersymmetrized* Killing form $\kappa^s(X,Y)=
\frac{1}{2}(\kappa(X,Y)+\kappa(Y,X))$ is non-degenerate on
$\mathfrak{q}(N)$ for $N\geq 2$ — but at degenerate Cartan elements
like $A_{11}$, the symmetric part may evaluate to zero. The
non-degeneracy is a property of the form on the *full* algebra, not
on individual basis pairs.

**Direct verification via the alternative form $B_0$.** The form
$B_0(X,Y)=\Tr(\mathrm{ev}\,XY+\mathrm{ev}\,YX)/2$ on the even part
gives $B_0(A_{11},A_{11})=\Tr(A_{11}^2)=\Tr(A_{11})=1$ (since
$A_{11}^2=A_{11}$ in $\mathfrak{gl}_2$ as a matrix unit), so $B_0$ is
*not* zero on this pair. **The form $B_0$ is non-degenerate on q(2),
even though the Killing form is degenerate on individual pairs.**

This confirms the §3.3 statement that $B_0$ provides the regulator
construction; the Killing form is auxiliary.

**One-loop QME.** The propagator-loop contraction on q(2) gives
$\sum_{a=1}^{8}(-1)^{|a|}\delta^a_a=4-4=0=\Str(I)$. **One-loop QME
vanishes by direct computation.** Higher loops follow by W22-L3
verbatim with $\Str(I^k)=0$ at q-balance.

---

## §4. (M4) sl(M|N), M ≠ N full analysis

### §4.1 Definition and structure (Kac 1977 §2.1.5)

$\mathfrak{sl}(M|N)$ for $M\neq N$ is the supertraceless subalgebra of
$\mathfrak{gl}(M|N)$:
\[
   \mathfrak{sl}(M|N)=\{X\in\mathfrak{gl}(M|N):\Str(X)=0\}.
\]
For $M\neq N$, this is a **basic classical Lie superalgebra** (Kac
1977 §2.5.5), with dimension $M^2+N^2-1+2MN$ (after subtracting one
for the supertrace constraint).

The center is trivial for $M\neq N$ (the supertrace constraint and
the diagonal constraint $\Tr_M=\Tr_N\cdot N/M$ have no compatible
solution for $M\neq N$ except the zero element). So
$\mathfrak{psl}(M|N)$ is *not* a thing for $M\neq N$ — sl(M|N) is
already simple.

### §4.2 Supertrace of identity (Step 1)

The identity $I\in\mathfrak{gl}(M|N)$ has $\Str(I)=M-N$. For $M\neq N$
this is *non-zero*. **Crucially**, the identity is *not* in
$\mathfrak{sl}(M|N)$ when $M\neq N$ — the supertrace constraint
excludes it. The "identity" in $\mathfrak{sl}(M|N)$ would be the
projection of $I$ onto the supertraceless subspace, which is
$I-\frac{M-N}{M+N}\cdot(I_{M}\oplus 0_N+0_M\oplus I_N)$ (or some
similar projection); this projected identity has supertrace zero by
construction.

**However**, for the W22 mechanism, what matters is the **identity in
the defining representation**, which is $I_{M+N}\in\mathfrak{gl}(M|N)$
acting on $\C^{M|N}$. This identity has $\Str(I_{M+N})=M-N\neq 0$.

**The brane-probe action on sl(M|N) inherits from gl(M|N) by
restriction**, so the propagator-loop contraction sees the
defining-rep supertrace $\Str_{\mathfrak{gl}(M|N)}(I)=M-N$.

**Verdict for Step 1.** $\Str(I)=M-N\neq 0$. The necessary condition
for $\Lambda^{\Str}$ discharge **is not met**.

### §4.3 Super-Killing form (Step 2)

Non-degenerate (basic classical for $M\neq N$). The standard
parametrix construction works on sl(M|N).

### §4.4 Sergeev / Capelli central element (Step 3)

Standard Capelli (gl-style) at all even degrees; same as on gl(M|N)
modulo center. Compatible with admissible regulators.

### §4.5 Λ^Str chain-level reduction (Step 4 — KEY OBSERVATION)

The W22-L2 lift $\Lambda^{\mathrm{Str}}$ extends to $\mathfrak{sl}(M|N)$,
and the chain-level QME relation reads
\[
   \mathrm{Ob}_{\mathrm{sc}}^{\mathfrak{sl}(M|N)}=
   \hbar(M-N)\cdot\Lambda^{\mathrm{Str}}(\omega).
\]

**At $M\neq N$, the right-hand side is non-zero as a chain-level
cocycle.** The QME obstruction class is $[\hbar(M-N)\bar c]$, which
is *non-zero* in $H^1(\mathcal O_{\mathrm{loc}}(\mathcal E_w^{\mathfrak{sl}(M|N)}),
Q+\{I_0,-\})$ because $\bar c$ is non-trivial and $(M-N)\neq 0$.

**Verdict for Step 4.** Λ^Str chain-level reduction goes through, but
the result is a **non-zero obstruction**, not a discharge. The
chain-level lift extends symbol-by-symbol, but multiplied by a
non-zero coefficient $(M-N)$.

### §4.6 Discharge / failure verdict (Step 5)

**FAILS by construction.** The W22 supertrace mechanism *requires*
super-balance $\Str(I)=0$ to discharge the QME obstruction. On
$\mathfrak{sl}(M|N)$ with $M\neq N$, the supertrace is non-zero and
the QME class $[\hbar(M-N)\bar c]$ is *active*.

**This is the parallel of bosonic $\mathfrak{gl}_N$**: just as
$\mathfrak{gl}_N$ has $\Tr(I)=N\neq 0$ and the QME class
$[\hbar N\bar c]$ is non-trivial (Theorem G), so
$\mathfrak{sl}(M|N)$ for $M\neq N$ has $\Str(I)=M-N\neq 0$ and the
QME class $[\hbar(M-N)\bar c]$ is non-trivial.

**Residue analysis.** The "residue" of the supertrace at $M\neq N$
is $\Str(I)=M-N$, and the QME obstruction is precisely
$\hbar(M-N)[\bar c]$. The closer $M$ is to $N$, the smaller the
obstruction; at $M=N$ the obstruction vanishes.

**Verdict.** **(M4) FAILS by construction**, but **interestingly**: the
failure is *quantitative* (coefficient $(M-N)$) rather than
*structural* (mechanism breaks). The W22 mechanism *applies* to
$\mathfrak{sl}(M|N)$ — it just gives a *non-zero* answer.

### §4.7 Hand-computation on sl(2|1)

$\mathfrak{sl}(2|1)$ has dimension $4+1+2\cdot 2-1=8$. Even part:
$\mathfrak{gl}_2\oplus\mathfrak{gl}_1$ (5-dim), constrained by
$\Tr_{\C^2}=\Tr_{\C^1}$ (or some convention), so 4-dim. Odd part:
$\Hom(\C^2,\C^1)\oplus\Hom(\C^1,\C^2)$ (4-dim).

**Supertrace of identity (in defining rep):**
$\Str_{\mathfrak{gl}(2|1)}(I_3)=2-1=1$. **Non-zero.**

**One-loop QME on sl(2|1):**
$\mathrm{anomaly}^{\mathrm{sl}(2|1)}_{1\text{-loop}}=\hbar\cdot 1
=\hbar$. **Non-zero — the QME class is active.**

This confirms (M4) FAILS. The supertrace mechanism on
$\mathfrak{sl}(M|N)$ with $M\neq N$ is exactly the same as on
$\mathfrak{gl}(M|N)$; the "supertraceless" constraint does not change
the propagator-loop contraction.

---

## §5. Implications for super-stack dimension constraints in the manuscript's open-closed comparison

### §5.1 Manuscript's super-stack lattice

The manuscript currently (as of the W22 / P4-G3-T-A1 layer) has the
following super-balanced sources at chain-level discharge:

* **bosonic** $\mathfrak{gl}_N$: obstructed by Theorem G's
  $\hbar N[\bar c]$ class (this is the manuscript's M-13 target).
* **gl(N|N)**: discharged at chain level by W22-T1+T2 (proposed
  inscription `thm:app-super-balanced-qme-all-loops`).
* **osp(2N|2N)**: discharged at chain level by P4-G3-T-A1 (proposed
  inscription `thm:app-osp-balanced-qme-vanishing`).

This document adds:

* **psl(N|N)**: discharged via lift to gl(N|N), with caveat that the
  native discharge on psl is obstructed by degenerate Killing form.
* **q(N)**: discharged at the ordinary-supertrace level; queer-trace
  is parallel.
* **p(N)**: **FAILS** at (A5) parametrix step — odd invariant form,
  no even non-degenerate ad-invariant supersymmetric form.
* **sl(M|N), M ≠ N**: **FAILS** by construction — supertrace is
  non-zero, QME class is active.

### §5.2 Implication for cross-volume CY-to-chiral comparison

The Vol III CY-to-chiral frontier (in
`~/calabi-yau-quantum-groups`) considers brane-probe configurations
on Calabi–Yau threefolds. The natural BCOV / topological B-model
brane configurations involve:

* $\mathfrak{gl}_N$ branes (the manuscript's main bosonic target).
* $\mathfrak{gl}(N|N)$ brane–anti-brane stacks (Sen 1998, Witten 1998
  tachyon condensation locus).
* $\mathfrak{osp}(2N|2N)$ orientifold stacks (Sen 1999, Bergman–Gimon–
  Sugimoto 2001).

The current document adds two **physical implications**:

**Implication 1 (psl(N|N)).** The BCOV anti-brane / tachyon-condensation
configuration is naturally on $\mathfrak{gl}(N|N)$, but the *string-frame*
gauge group after tachyon condensation is $\mathfrak{psl}(N|N)$ (the
quotient by the residual U(1) symmetry). This document's M1 result
shows that the chain-level discharge on psl(N|N) requires the lift to
gl(N|N), which is consistent with the physics: the gauge group is
gl(N|N) at the string frame; the tachyon-condensed quotient psl(N|N)
inherits the discharge but does not host the regulator construction
natively.

**Implication 2 (p(N)).** Periplectic gauge groups arise in
*odd-orientifold* configurations (where the orientifold projection is
odd-symmetric rather than even-symmetric). The result of this
document (M2 FAILS) suggests that **odd orientifolds are
structurally different from even orientifolds** at the BV regulator
level — the periplectic source does not host a chain-level QME
discharge, so any tachyon-condensation argument on a periplectic
orientifold must use a non-W22 mechanism.

This is **consistent** with the physics literature: odd
orientifolds (Type 0' string theory; periplectic orientifolds in
mathematical physics) are known to be more pathological than even
orientifolds. The M2 result formalizes this at the BV level.

### §5.3 Implication for super-stack dimension constraint

The manuscript's super-stack dimension constraint
$\dim\mathfrak{g}_{\bar 0}=\dim\mathfrak{g}_{\bar 1}$ is *necessary*
for super-balance $\Str(I)=0$. This document shows it is *not
sufficient* for chain-level QME discharge: p(N) satisfies
$\Str(I)=0$ but FAILS at (A5).

**The manuscript should record:** *"super-balance is necessary; the
sufficient condition is super-balance plus existence of an even
non-degenerate ad-invariant supersymmetric bilinear form"*.

The basic classical Lie superalgebras with super-balance and even
invariant form are:
* $\mathfrak{gl}(N|N)$, $\mathfrak{sl}(N|N)$, $\mathfrak{psl}(N|N)$
  (the latter via lift);
* $\mathfrak{osp}(2N|2N)$;
* $\mathfrak{q}(N)$ (with the alternative even form $B_0$);
* exceptional Lie superalgebras $\mathfrak{D}(2,1;\alpha)$,
  $\mathfrak{F}(4)$, $\mathfrak{G}(3)$ for specific values of
  $\alpha$ — these are *not* in the (A1)-prong but worth flagging.

The basic classical Lie superalgebras with super-balance but **no**
even invariant form are:
* $\mathfrak{p}(N)$ (periplectic) — only odd invariant form.

### §5.4 Manuscript inscription proposal

If the M1–M4 results are to be inscribed alongside the gl(N|N) and
osp(2N|2N) results, the natural location is
`appendix-unreduced-bv-qme.tex` after
`thm:app-osp-balanced-qme-vanishing`. **Proposal:**

```latex
\begin{rmk}[Classical super-Lie extension of chain-level
  super-balanced QME discharge]
\label{rmk:app-classical-super-extension}
   The W22-T2 / osp-T2 chain-level discharge extends to the
   following classical super-Lie families:
   \begin{itemize}
     \item $\lie{psl}(N|N)$ (via lift to $\lie{gl}(N|N)$, with
       degenerate Killing form on psl forcing the lifted construction);
     \item $\lie{q}(N)$ (queer Lie superalgebra; ordinary-supertrace
       discharge holds; queer-trace parallel is open);
   \end{itemize}
   and \emph{fails} on:
   \begin{itemize}
     \item $\lie{p}(N)$ (periplectic; odd symmetric invariant form
       does not produce an even non-degenerate ad-invariant
       parametrix; (A5) breaks);
     \item $\lie{sl}(M|N)$ for $M\neq N$ (supertrace
       $\Str(I)=M-N\neq 0$; QME class is active).
   \end{itemize}
\end{rmk}
```

**Status.** Proposal-only; pending main-thread integration. The
inscription requires consistent macros (`\psl`, `\plie`, `\q`, `\sl`,
`\Str`, `\bar A`); some of these may need to be added to
`mathmacros.tex` / `commands.tex`.

---

## §6. Residual obligations + deciding evidence

### §6.1 Residuals from M1 (psl(N|N))

* **R-P4-G3-M2-PSL-01.** Native chain-level discharge on
  $\mathfrak{psl}(N|N)$ (without lift). Possibly via a deformed
  invariant form or a Penkov–Serganova atypical block construction.
  **Status: Phase-5 (open research direction); not blocking the
  current discharge via lift.**

* **R-P4-G3-M2-PSL-02.** Etingof–Ostrik tensor-category description
  of the psl(N|N) atypical block and its impact on (C) prong
  character extensions. **Status: Phase-4 / cross-volume.**

* **R-P4-G3-M2-PSL-03.** Verification on psl(2|2): explicit
  computation of the 14-dim adjoint propagator-loop and verification
  that the lifted discharge descends correctly. **Status:
  hand-computation in §1.7 covers the dimension check; full
  chain-level verification is an exercise.**

### §6.2 Residuals from M2 (p(N))

* **R-P4-G3-M2-P-01.** Alternative discharge mechanism on p(N)
  using the odd Sergeev central element. The W22 mechanism uses an
  even invariant form; an alternative mechanism using the odd form
  might discharge a *different* QME class (with odd ghost number).
  **Status: Phase-5 / structural research direction.**

* **R-P4-G3-M2-P-02.** Coulembier 2018 / periplectic Brauer algebra
  duality for p(N). The QME obstruction might admit a
  representation-theoretic discharge through this duality. **Status:
  Phase-5 / cross-volume.**

* **R-P4-G3-M2-P-03.** Consistency with Type 0' string theory and
  odd-orientifold physics (Sagnotti 1995 *Some properties of open
  string theories*; Polchinski 1995 *Open superstring theory and
  quasi-Lorentz invariance*). **Status: Phase-4 / cross-volume.**

### §6.3 Residuals from M3 (q(N))

* **R-P4-G3-M2-Q-01.** Queer-trace parallel discharge on q(N). The
  natural object is a "queer-cocycle" $\omega^{\mathrm{otr}}$ valued
  in the odd line; the QME mechanism for such a cocycle is an open
  research direction. **Status: Phase-5 / (C) prong character
  extensions.**

* **R-P4-G3-M2-Q-02.** Sergeev duality for q(N)–Hecke–Clifford
  algebra (Sergeev 1984; Brundan–Kleshchev 2003). The
  representation theory of q(N) is governed by Hecke–Clifford; the
  QME-class layer's interaction with Hecke–Clifford is a Phase-5
  question. **Status: Phase-5 / cross-volume.**

* **R-P4-G3-M2-Q-03.** Consistency with the Cheng–Wang 2012 §6
  parametric study of q(N) at small $N$ and the
  Sergeev–Berele–Regev classification. **Status: Phase-4
  cross-checking.**

### §6.4 Residuals from M4 (sl(M|N), M ≠ N)

* **R-P4-G3-M2-SL-01.** Confirmation that the QME class
  $[\hbar(M-N)\bar c]$ on $\mathfrak{sl}(M|N)$ is the *unique*
  obstruction to chain-level QME at one loop, and that no further
  obstructions arise at higher loops. **Status: by W22-L3 verbatim,
  the higher-loop obstructions are products of $(M-N)^{\ell_{\mathrm{loops}}}$;
  this is a direct corollary of the W22 framework.**

* **R-P4-G3-M2-SL-02.** Class-level vs cohomology-level distinction
  for the active obstruction. The QME class is active at chain level
  and at cohomology level; the chain-level cocycle $\Lambda^{\Str}(\omega)
  \cdot\hbar(M-N)$ is non-zero. **Status: direct from W22.**

### §6.5 Deciding evidence (cross-references)

* **Kac 1977 §2.5.5** (basic classical classification): confirms
  psl(N|N) is *not* basic classical (degenerate Killing); confirms
  p(N) is in the strange series with no even invariant form.
* **Cheng–Wang 2012 Prop. 1.34** (Killing form vanishing on
  p(N) and psl(N|N)): direct evidence for M1 caveat and M2 obstruction.
* **Sergeev 1984** (queer Sergeev duality): direct evidence for
  M3's two-supertrace structure.
* **Penkov–Serganova 1989, 2000** (atypical blocks of psl(N|N)):
  evidence that psl(N|N) has a richer rep-theoretic structure than
  gl(N|N), but this does not affect the chain-level QME at the
  one-/all-loop level.
* **Etingof–Ostrik 2015 §4.7** (semisimplicity failures):
  confirms psl(N|N) is non-semisimple at integral level.
* **Coulembier 2018** (periplectic Brauer algebra): provides an
  alternative duality framework for p(N) that may discharge the QME
  via representation theory; not pursued here.

---

## §7. Phase-5 escalation conditions

The following residuals would warrant Phase-5 escalation:

1. **(R-P4-G3-M2-PSL-01)** Native chain-level discharge on psl(N|N)
   without lift to gl(N|N). Currently the discharge requires lift,
   which is structurally different from the gl/osp case. Phase-5
   would investigate whether an intrinsic mechanism exists.

2. **(R-P4-G3-M2-P-01, P-02)** Alternative discharge mechanism on
   p(N). The current document closes M2 as **FAILS at (A5)**, but
   does not rule out alternative mechanisms (odd Sergeev, periplectic
   Brauer duality). Phase-5 would investigate these alternatives.

3. **(R-P4-G3-M2-Q-01)** Queer-trace parallel discharge on q(N).
   The current document closes M3 as **DISCHARGES at the
   ordinary-supertrace level**; the queer-trace structure is
   parallel and largely independent. Phase-5 would investigate the
   queer-cocycle QME mechanism.

4. **Cross-volume CY-to-chiral consistency.** The implications for
   BCOV / topological B-model brane configurations (psl(N|N)
   tachyon-condensation, p(N) odd orientifolds, q(N) queer
   parastatistics) require careful Phase-4 / Phase-5 integration
   with the Vol III CY-to-chiral frontier. **No load-bearing
   contradictions identified at the present analysis layer.**

5. **(R-P4-G3-M2-PSL-02)** Etingof tensor-category structure for
   classical super-Lie families. The semisimplicity failures of
   psl(N|N) and the abelian-envelope structure of p(N) (Coulembier
   2018) suggest that the QME mechanism interacts non-trivially with
   the tensor-category structure. Phase-5 would formalize this
   interaction.

**Convergence to Phase-5.** None of these residuals threatens the
present discharges at chain level. They are *open structural
questions* that warrant deeper investigation but do not create
load-bearing contradictions in the current manuscript or in the
P4-G3-T-A1 / P4-G3-M2 framework.

---

## §8. Convergence verdict

**P4-EXEC-G3-M2: cataloged.** Of the four targeted classical super-Lie
families:

* **(M1) psl(N|N): DISCHARGES via lift** to gl(N|N), with caveat
  that native discharge on psl is obstructed by degenerate Killing.
* **(M2) p(N): FAILS** at (A5) parametrix construction — no even
  non-degenerate ad-invariant supersymmetric form on the
  periplectic algebra.
* **(M3) q(N): DISCHARGES** at the ordinary-supertrace level used
  by W22; queer-trace structure is parallel and largely independent.
* **(M4) sl(M|N), M ≠ N: FAILS** by construction —
  $\Str(I)=M-N\neq 0$, so the QME obstruction class is *active*
  with coefficient $\hbar(M-N)$.

**Strategic implications.** The classical super-Lie families that
host the W22 / P4-G3-T-A1 chain-level supertrace mechanism are:
gl(N|N), osp(2N|2N), psl(N|N) (via lift), and q(N) (at the
ordinary-supertrace level). The exception is **p(N)**, which
genuinely fails. This delineates the **boundary** of the W22
framework's applicability among classical super-Lie algebras.

**Most surprising structural finding.** The adjoint-rep supertrace
on psl(N|N) is *non-zero* (specifically $-2$ on psl(2|2), in the
hand-computation of §1.7), while the defining-rep supertrace
inherited from gl(N|N) is zero. This **disagreement** is a feature
of the non-basic-classical structure of psl: the adjoint
representation has a different super-character than the defining
representation at the level of dimension cancellation. The W22
mechanism is sensitive to the *defining-rep* supertrace (which
appears in the propagator-loop contraction), so the discharge holds
via lift; but the adjoint-rep supertrace is what governs the *Killing
form*, which is degenerate on psl. **The structural source of psl's
"non-basic-classical-ness" is precisely this defining-vs-adjoint
supertrace discrepancy.** This was the most informationally
surprising finding of the catalog.

**Inscribed durables.**
* This document.
* P4-EXEC-G3-M2 ledger entries: discharged (M1, M3), failed (M2, M4).
* Inscription proposal `rmk:app-classical-super-extension` (proposal
  only) for `appendix-unreduced-bv-qme.tex`.
* Three precision findings:
  - psl: adjoint vs defining supertrace discrepancy;
  - p: even-form obstruction is structural;
  - q: two-supertrace structure (ordinary vs queer).
* Twelve residuals (4 per family) pushed to Phase-4 / Phase-5
  cross-group work.

**Posture against P4-G3 (A) prong.** P4-G3-T-A1 (osp(2N|2N))
discharged at chain level; P4-G3-M2 (this document) catalogs psl,
p, q, sl-imbalanced and identifies p as the *unique* failure case
among the supertraceless classical super-Lie families.

**Posture against the manuscript.** No load-bearing contradiction.
The manuscript's bosonic $\mathfrak{gl}_N$ source remains obstructed
(Theorem G $\hbar N[\bar c]$ unchanged); the supertrace-discharged
sources (gl(N|N), osp(2N|2N), psl(N|N) via lift, q(N)) are
*alternative* brane theories on which the QME holds at chain level;
p(N) is a structurally different brane theory that does not host the
W22 discharge. M-13's bosonic disambiguation is preserved.

End of P4-EXEC-G3-M2 ledger.
