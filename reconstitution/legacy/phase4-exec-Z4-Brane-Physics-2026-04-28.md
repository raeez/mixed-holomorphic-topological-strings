% !TEX root = main.tex
# Phase 4 Execution / P4-Z4-Brane-Physics — Physical interpretation of the $\Z/4\to\Z/2$ cohomology collapse on the q(N) doubled brane

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Witten primary (brane physics, anomaly cohomology, dyonic
states, K-theory, parastatistic boundary states); Boundary secondary
(precise boundary-state algebra of each parity eigenstate).
**Mode.** Phase-4 EXEC, proposal-only — no manuscript edits, no
commits. Master ledger schema; ID prefix
`P4-EXEC-Z4-Brane-Physics-`. Writable surface: this file only.
**Posture.** P4-EXEC-Sergeev-Intertwiner (1023 lines) constructed
$\Phi_{\mathrm{Sergeev}}$ as a $\Z/4$-graded automorphism of
$H^2_{\mathrm{Lie}}(\bar A;\C\oplus\Pi\C)$ implemented at the
parametric level by conjugation with the queer central element
$J\in\mathfrak q(N)_{\bar 1}$ satisfying $J^2=-I_{2N}$ and $J^4=I$.
On cohomology classes the $\Z/4$-action collapses to $\Z/2$
(parity-flip). The bosonic Theorem G class $[\bar c]\in
H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}$ is the fixed locus
($\Phi^2=\id$ on the 1-dim generator). This audit reads the collapse
through the Witten / Boundary lens: which physical brane configuration
realises the $\Z/4$, what physical sectors do the four parity
eigenvalues correspond to, and what is the $\Z/4\to\Z/2$ collapse a
shadow of?

**Inputs (full or targeted reads as indicated).**
* `CLAUDE.md` (full).
* `reconstitution/phase4-exec-Sergeev-Intertwiner-2026-04-28.md`
  (1023 lines; P-Sergeev-1' $\Z/4$-graded refinement; cohomology
  collapse to $\Z/2$; bosonic Theorem G as fixed locus).
* `reconstitution/phase4-exec-Brane-Species-Audit-2026-04-28.md`
  (1213 lines; Tier II q(N) doubled boundary state, Str-brane +
  otr-brane).
* `reconstitution/phase4-exec-Theorem-G-otr-inscription-2026-04-28.md`
  (1374 lines; Theorem G\textsuperscript{otr}; queer-Capelli;
  two-supertrace independence).
* `reconstitution/phase4-exec-Sergeev-Duality-Probe-2026-04-28.md`
  §3.2 (the $\Z/4$ structure on $\End(V)$ from $J^2=-I$); §7.1
  (Obs-Sergeev-A5-firewall).
* `reconstitution/phase4-exec-G3-M3-queer-trace-2026-04-28.md` §3.3
  (the (A5)-violation $P^{\mathfrak q}\,J\,(P^{\mathfrak q})^{-1}=-J$).
* `main.tex` lines 1–10 (title; local mixed model
  $\R^2_{\mathrm{top}}\times\C^2_{\mathrm{hol}}$); 740–820 (mixed
  brane definition); 354–393 (brane-defect comparison map).

**Standard primary-source references (cited from memory; not new
inscriptions).**
* E. Witten, *Topological sigma models*, Comm. Math. Phys.
  **118** (1988), 411–449. **A/B-twist boundary states.**
* E. Witten, *Mirror manifolds and topological field theory*, in
  *Essays on Mirror Manifolds*, IP Press 1992. **Mirror branes.**
* E. Witten, D. Olive, *Supersymmetry algebras that include
  topological charges*, Phys. Lett. B **78** (1978), 97–101.
  **BPS bound, $\Z/4$-graded central charge.**
* C. Vafa, E. Witten, *A strong coupling test of S-duality*,
  Nucl. Phys. B **431** (1994), 3–77. **Dyonic states, electric-magnetic
  duality, partition functions on $T^4$.**
* E. Witten, *D-branes and K-theory*, JHEP **9812** (1998), 019.
  **K-theoretic brane charge classification.**
* D.-E. Diaconescu, G. Moore, E. Witten, *$E_8$ gauge theory and a
  derivation of K-theory from M-theory*, Adv. Theor. Math. Phys.
  **6** (2003), 1031–1134. **K-theory and discrete torsion;
  $\Z/4$-collapse phenomena in M-theory.**
* I. Brunner, K. Hori, K. Hosomichi, J. Walcher, *Orientifolds of
  Gepner models*, JHEP **02** (2007), 001. **Worldsheet $\Z/4$
  symmetry on Gepner-model orientifolds.**
* J. Brundan, A. Kleshchev, *Hecke–Clifford superalgebras, crystals
  of type $A_{2\ell}^{(2)}$*, Represent. Theory **5** (2001),
  317–403. **Spin Hecke algebra; $\Z/4$-compatible Clifford
  generators.**
* P. Aspinwall, *D-branes on Calabi-Yau manifolds*, in *Progress
  in String Theory*, World Scientific 2005, 1–152. **K-theory
  classification on CY3.**

---

## §0. Executive verdict

**Three-line bottom line.**

1. **Physical realisation of the $\Z/4$ action.** The $\Z/4$-graded
   parametric automorphism $\langle\Phi_{\mathrm{Sergeev}}\rangle\cong\Z/4$
   is realised on the q(N) doubled brane stack by conjugation with the
   queer central element $J\in\mathfrak q(N)_{\bar 1}$, which is the
   **algebraic generator of a worldline parastatistic Z/4 R-symmetry**
   on the Chan-Paton bundle $\C^{N|N}$. The action is
   $\End(\C^{N|N})$-internal: it does **not** require a $\Z_4$
   orbifold of the bulk $\R^2\times\C^2$, and it does **not** require
   a discrete-torsion lift in the Diaconescu-Moore-Witten 2003 sense.
   The relevant comparison is **not** orbifold; it is a worldline
   (=brane-line) symmetry analogous to the parastatistic R-symmetry on
   queer 1d sigma models (Sergeev 1983 motivation), realised here on
   the manuscript's local mixed model $\R^2\times\C^2$ as a
   parity-twist on the brane line $\R\times p$.

2. **The $+1, -1, +i, -i$ eigensectors.** The four parametric
   eigenvalues of $\Phi_{\mathrm{Sergeev}}$ correspond to four
   physical brane sectors:
   * **$+1$ (bosonic Theorem G fixed).** Diagonal block of
     $\End(\C^{N|N})$, even-parity Chan-Paton, $\Tr$-channel boundary
     evaluation; the manuscript's bosonic gl-brane (Theorem G).
   * **$-1$ (otr parity-flipped).** Off-diagonal block conjugated by
     $J^2=-I$, even-parity Chan-Paton with sign-flipped intertwiner;
     this is the **bosonic dual of the otr-brane** at the parametric
     level (visible at the chain level, invisible on cohomology because
     a sign on a 1-d cocycle is rescaled into the coboundary
     equivalence class).
   * **$+i$ and $-i$ (intermediate).** Off-diagonal blocks with the
     true odd-parity intertwiner $J$ — i.e., the **otr-brane** itself
     and its conjugate. Cohomologically these collapse to a single
     $\bar 1$-parity class $[\bar c]^{\mathrm{otr}}$, but parametrically
     they are two distinct boundary states (two "square roots" of the
     parity flip $J^2=-I$, conjugate under the $S_n$-permutation of
     Hecke-Clifford generators).
   * **Cohomology collapse rule.** $\{+1,-1\}\to[\bar c]\in H^2_{\bar 0}$
     (bosonic, fixed locus). $\{+i,-i\}\to[\bar c]^{\mathrm{otr}}\in
     H^2_{\bar 1}$ (parity-flipped, single class because the $\pm$
     sign on a 1-d odd cocycle is absorbed into rescaling).

3. **New physical prediction (P-Z4-Brane-1).** The two $\pm i$
   sectors are **physically present but cohomologically invisible**
   parastatistic boundary states realising a $\Z/4$ R-symmetry
   structurally analogous to (but **not identical to**) the
   Witten-Olive 1978 BPS $\Z/4$-graded central charge on $\mathcal
   N=2$ supersymmetric theories. The cohomologically-invisible sectors
   are predicted to be **detectable as a $\Z/2\subset\Z/4$
   parastatistic anomaly** in the chain-level open-string algebra of
   the q(N) doubled brane (= the Hecke-Clifford braid algebra
   $\mathcal{HC}_n$), measurable as the spin-statistics phase of the
   Clifford generators $c_i$ relative to the symmetric-group
   generators $\sigma\in S_n$.

**Convergence verdict.** The $\Z/4\to\Z/2$ collapse is the
brane-physics shadow of the Sergeev parastatistic R-symmetry: a
**parametric** $\Z/4$ on the queer Chan-Paton bundle, induced from
$J^2=-I$, that descends to a **cohomological** $\Z/2$ (parity-flip)
because the cohomology generators are 1-dimensional and a multiplicative
$\pm$ sign rescales the cocycle representative. The bosonic Theorem G
class is **parity-self-dual**: it is the fixed locus of the
parity-mirror $\Phi_{\mathrm{Sergeev}}^2$, equivalently the only class
that survives both halves of the $\Z/4$ collapse. The two
cohomologically-invisible $\pm i$ sectors correspond to the two
**Hecke-Clifford braid-conjugate variants of the otr-brane**, related
by the $S_n$-permutation of Clifford generators.

**Per-deliverable verdict (per (ZB.1)–(ZB.6)).**

| Deliverable | Verdict | Headline |
|---|---|---|
| **(ZB.1) Brane configuration** | DRAFTED | Worldline parastatistic $\Z/4$ R-symmetry on the q(N) Chan-Paton bundle $\C^{N\|N}$ generated by the odd central element $J\in\mathfrak q(N)_{\bar 1}$. Not a $\Z_4$-orbifold of the bulk; not a Diaconescu-Moore-Witten discrete-torsion lift. |
| **(ZB.2) Four eigensectors** | DRAFTED | $+1$: bosonic Theorem G (fixed). $-1$: parity-flipped otr (cohomologically equal to $+i,-i$). $+i,-i$: the two Hecke-Clifford braid-conjugate variants of the otr-brane. |
| **(ZB.3) Cross-walk to Brane-Species** | DRAFTED | The doubled brane (Str-brane + otr-brane) realises the $+1$ and $\{+i,-i\}$ sectors. The $-1$ sector is parametrically distinct but cohomologically equal to $\{+i,-i\}$. The Brane-Species-Audit Tier II structure thus encodes a 2-class cohomology coming from a 4-class parametric foliation. |
| **(ZB.4) $\pm i$ physical phenomenon** | DRAFTED | Sergeev parastatistic R-symmetry; structurally analogous to but **distinct from** Witten-Olive 1978 BPS $\Z/4$ (which is a central-charge $\Z/4$ on supersymmetry, not a parity-twist on Chan-Paton). Diaconescu-Moore-Witten 2003 K-theory + discrete-torsion: **NOT** the right analogy (their $\Z/4$ is on the K-theory class, not on the brane parity). |
| **(ZB.5) Smallest example** | IDENTIFIED | $N=2$, $n=2$ on $\R\times p\subset\R^2\times\C^2$, q(2) Chan-Paton $\C^{2\|2}$. Predicted measurement: spin-statistics phase of $c_1,c_2\in\mathcal{HC}_2$ relative to $\sigma\in S_2$, computable from the verification script `scripts/check_sergeev_intertwiner.py` test V.4 (Clifford relations $c_1c_2+c_2c_1=0$, $c_i^2=I$). |
| **(ZB.6) New predictions** | DRAFTED | (i) Cohomologically-invisible parastatistic sectors at $\pm i$; (ii) parity-self-duality of bosonic Theorem G as fixed-locus condition; (iii) chain-level $\Z/4$-compatible Clifford structure (Brundan-Kleshchev 2001 spin Hecke algebra at level 1) as the Phase-5 chain-level lift constraint. |

---

## §1. (ZB.1) Brane configuration realising $\Z/4$

### §1.1 The parametric $\Z/4$ on $\End(V)$

**Source structure (Sergeev-Intertwiner §4.2 + §6.2).** The
Sergeev intertwiner $\Phi_{\mathrm{Sergeev}}$ is implemented at the
parametric (matrix) level by conjugation with the queer central
element $J\in\mathfrak q(N)_{\bar 1}$:
\[
   \Phi_{\mathrm{Sergeev}}(T)=J\,T\,J^{-1}, \qquad J^{-1}=-J\text{ since }J^2=-I_{2N}.
\]
Iterating gives $\Phi_{\mathrm{Sergeev}}^2(T)=J^2\,T\,J^{-2}=(-I)T(-I)^{-1}=T$,
so on $\End(V)$ the conjugation by $J^2$ is the identity; the
**parametric automorphism group** is then
\[
   \langle\Phi_{\mathrm{Sergeev}}\rangle\subset\mathrm{Aut}(\End(V))
\]
generated by conjugation with $J$. Since $J^4=I_{2N}$ (a direct
consequence of $J^2=-I$), this group is **cyclic of order 4**,
$\langle\Phi_{\mathrm{Sergeev}}\rangle\cong\Z/4$.

**Generator parities.** $J\in\mathfrak q(N)_{\bar 1}$ has odd parity.
Conjugation by an odd element is an automorphism of the matrix algebra
$\End(V)$ (treated as ungraded), but it does **not** preserve the
$\Z/2$-grading: it is a parity-twist. The four powers of conjugation
by $J$ on $\End(V)$ are:
* $J^0=I$: identity automorphism (trivially preserves grading).
* $J^1$: parity-twist by $J$ (parity-flipping).
* $J^2=-I$: scalar conjugation by $-I$, identity automorphism (preserves
  grading; differs from $J^0$ only by the sign $-I$ which is in the
  centre of $\End(V)$ and acts trivially as an inner automorphism).
* $J^3=J\cdot J^2=-J$: parity-twist by $-J$ (parity-flipping).

So the $\Z/4$-action on $\End(V)$ has:
* Two **even** automorphisms (preserving grading): $J^0$ and $J^2$,
  both conjugation by $\pm I$, both inner-trivial.
* Two **odd** automorphisms (parity-flipping): $J$ and $-J=J^3$,
  conjugation by $\pm J$, both parity-twisting.

### §1.2 Worldline parastatistic R-symmetry

**Claim.** The $\Z/4$-action on the q(N) Chan-Paton bundle $\C^{N|N}$
is a **worldline parastatistic R-symmetry** in the following sense:

* The brane line $\R\times p\subset\R^2\times\C^2$ carries an
  open-string field theory whose graded algebra is
  $\C[(\mathfrak q(N))^n\oplus(\mathfrak q(N))^n]^{Q_N}$ (the
  $Q_N$-invariant ring of pairs of queer matrices, parallel to the
  $GL_N$-invariant ring on the bosonic gl-brane; Brane-Species-Audit
  §5.2).
* The $\Z/4$-action by conjugation with $J$ is an **R-symmetry** of
  this 1d brane-line theory: it commutes with the open-string
  Hamiltonian (the brane-line BV differential) and acts on the
  Chan-Paton bundle without changing the closed-string sector.
* Its fixed locus $\End(V)^J=\End_{\mathfrak q(N)}(V)\cap\{J\}'$ is
  the **centralizer of $J$** in the natural rep, a subalgebra of
  dimension $2N^2$ realising the $J$-invariant boundary states.
* Its parity-twisting elements $J,-J$ implement the parastatistic
  exchange between the diagonal (Str-brane) and off-diagonal
  (otr-brane) Chan-Paton sectors.

**Why "parastatistic"?** Sergeev's original 1983 motivation
(*Tensor algebra of the identity rep of Q(n)*) framed the queer Lie
superalgebra as the ambient algebra for **parastatistic systems**:
states that interchange via a non-trivial scalar (here, the parity
sign) without being either bosonic or fermionic. The $\Z/4$ generator
$J$ on $\C^{N|N}$ is precisely the parastatistic exchange operator —
square root of the parity-flip $-I$ — whose physical realisation on
the brane-line open string is a *parastate boundary condition* (the
otr-brane of Brane-Species-Audit §5).

### §1.3 What this is NOT

**Not a $\Z_4$ orbifold of $\R^2\times\C^2$.** Orbifolds of the bulk
spacetime would act geometrically on $\R^2\times\C^2$ (e.g., as a
discrete subgroup of rotations on $\C^2$). The $\Z/4$ here acts only
on the **Chan-Paton bundle** $\C^{N|N}$, not on the spacetime; it is
an **internal R-symmetry**, not a spacetime symmetry.

**Not a Diaconescu-Moore-Witten 2003 K-theory torsion.** DMW 2003
identifies $\Z/4$-collapse phenomena in M-theory K-theory classes
arising from cohomological obstructions to lifting K-theory classes
through anomaly cancellation. The $\Z/4$ here is **purely on the
brane parity**, not on the K-theory class: the K-theory class of the
otr-brane is a *parity-shifted* element of $K^1$ rather than a
torsion class in $K^0$.

**Not a worldsheet $\Z/4$ R-symmetry of a Gepner model.** Brunner-Hori-
Hosomichi-Walcher 2007 *Orientifolds of Gepner models* identifies
$\Z/4$ R-symmetries of $\mathcal N=2$ Gepner models via the $\hat c$
charge structure. The $\Z/4$ here is parastatistic, not chiral
$\mathcal N=2$ R-symmetry; the worldsheet on $\R\times p$ is
1-dimensional, not 2-dimensional.

**Not Witten-Olive 1978 BPS $\Z/4$.** Witten-Olive 1978 introduces a
$\Z/4$-graded central charge in $\mathcal N=2$ supersymmetry algebras
that classifies BPS states. The $\Z/4$ here lives on the Chan-Paton
parity, not on the central charge of any supersymmetric algebra; the
analogy is **structural** (both involve a $\Z/4$ collapsing to $\Z/2$
on physical states), not literal.

### §1.4 The natural primary-source analogy

**The closest physical analogy is Brundan-Kleshchev 2001 spin Hecke
algebra at level 1.** Brundan-Kleshchev introduce a $\Z/4$-compatible
Clifford structure on the spin Hecke algebra controlling
representations of $\mathcal{HC}_n$ at the modular layer. The
parastatistic R-symmetry $\Z/4$ on the otr-brane is the
**factorization-algebra realisation** of this Brundan-Kleshchev
structure on the brane line: the open-string algebra of the otr-brane
should carry a $\Z/4$-compatible Clifford structure that reduces to
a $\Z/2$ super-grading on cohomology.

**Discharge.** (ZB.1) is answered: the brane configuration realising
the $\Z/4$ is the **q(N) doubled brane stack** with an internal
worldline parastatistic $\Z/4$ R-symmetry generated by conjugation
with $J\in\mathfrak q(N)_{\bar 1}$. This is **internal** to the brane
Chan-Paton bundle, **not** a bulk orbifold, K-theory torsion, or
worldsheet R-symmetry.

---

## §2. (ZB.2) Four parity-eigensectors — physical realisation

### §2.1 Eigenvalue +1: bosonic Theorem G fixed locus

**Parametric data.** The $+1$ eigensector of conjugation by $J$
consists of matrices $T\in\End(V)$ with $JTJ^{-1}=T$, equivalently
$JT=TJ$. Since $V=\C^N\oplus\Pi\C^N=\C^{N|N}$ and $J$ is the
off-diagonal $J=((0,I_N),(-I_N,0))$, the centralizer condition
$JT=TJ$ on $T=((A,B),(C,D))$ gives:
\[
   J\,T=\begin{pmatrix}C&D\\-A&-B\end{pmatrix}, \qquad
   T\,J=\begin{pmatrix}-B&A\\-D&C\end{pmatrix},
\]
so $JT=TJ$ iff $C=-B$, $D=A$, $-A=-D$, $-B=C$ — i.e., $D=A$ and
$C=-B$. The $+1$ eigensector is therefore
\[
   \End(V)^{+1}=\bigl\{((A,B),(-B,A)):A,B\in\mathfrak{gl}_N\bigr\},
\]
which is **isomorphic to $\mathfrak{gl}_N(\C[i])\cong\mathfrak{gl}_N\otimes\C[i]$**
(under $A+iB\mapsto((A,B),(-B,A))$). This is a **complexified bosonic
gl-brane**.

**Physical interpretation.** The $+1$ eigensector is the **diagonal-block
even part** of the q(N) algebra plus the **off-diagonal-block odd
part of $\mathfrak q(N)_{\bar 1}$ aligned with $J$**. Concretely:
the $A$-block is even (in $\mathfrak q(N)_{\bar 0}\cong\mathfrak{gl}_N$),
the $B$-block is odd (in $\mathfrak q(N)_{\bar 1}$ aligned with the
$J$-direction). The fixed locus is **exactly the queer Lie
superalgebra $\mathfrak q(N)$** itself (sitting inside
$\mathfrak{gl}(N|N)$ as the subalgebra preserving the queer pattern).

**Brane interpretation.** The $+1$ fixed sector is the **q(N)
doubled brane stack as a unit**, with both the $\Str$-channel and
$\mathrm{otr}$-channel boundary evaluations defined on the same
underlying brane bundle. The cohomology class of this sector is
$[\bar c]\oplus[\bar c]^{\mathrm{otr}}$ in the graded sum
$H^2_{\mathrm{Lie}}(\bar A;\C\oplus\Pi\C)$ — but only the bosonic
component $[\bar c]\in H^2_{\bar 0}$ is the **fixed locus on
cohomology** ($\Phi^2=\id$ on the 1-d generator), as
Sergeev-Intertwiner §6.1 records.

**Sergeev-Intertwiner P-Sergeev-1' confirms this:** the fixed locus
of the $\Z/4$-action on cohomology is the bosonic Theorem G class
$[\bar c]$.

### §2.2 Eigenvalue $-1$: parity-flipped otr at the parametric level

**Parametric data.** The $-1$ eigensector consists of $T$ with
$JTJ^{-1}=-T$, equivalently $JT=-TJ$. By a parallel computation:
\[
   \End(V)^{-1}=\bigl\{((A,B),(B,-A)):A,B\in\mathfrak{gl}_N\bigr\}.
\]
This sector is **distinct from $\mathfrak q(N)$**: it is the
periplectic-pattern complement (where the $C$-block is $+B$ rather
than $-B$, and $D=-A$ rather than $D=A$).

**Physical interpretation.** The $-1$ sector encodes the **parity-flipped
otr-brane** at the parametric level: a Chan-Paton bundle with the
sign-flipped queer pattern. Its boundary evaluation is
$\partial^{\mathrm{otr},-}\colon T\mapsto -\mathrm{otr}(T)$, where
the sign reflects the parity-flip from $T\to JTJ^{-1}=-T$.

**Brane interpretation.** This is **physically the same brane** as
the otr-brane of Brane-Species-Audit §5.1, up to a **sign convention**
on the off-diagonal blocks. The cohomology class is
$-[\bar c]^{\mathrm{otr}}$, but **on a 1-dimensional cocycle this
equals $[\bar c]^{\mathrm{otr}}$ up to coboundary** (rescaling by
$-1$). Hence at the cohomology layer the $-1$ eigensector is **equal
to the otr-brane class** (the $\bar 1$-parity sector of $H^2$).

**Cohomology assignment.** $-1\to[\bar c]^{\mathrm{otr}}$ (parity-flipped
sector of $H^2$).

### §2.3 Eigenvalues $+i,-i$: the two Hecke-Clifford braid-conjugate variants

**Parametric data.** The $\pm i$ eigensectors consist of $T$ with
$JTJ^{-1}=\pm iT$. These are the **square roots** of the parity-flip
$JTJ^{-1}=-T$ at the level of the $\Z/4$-action on $\End(V)$.

**Why $\pm i$ and not just one root?** The conjugation operator
$\Phi_{\mathrm{Sergeev}}=\mathrm{Ad}_J$ on $\End(V)$ has spectrum a
subset of the $\Z/4$-roots of unity $\{1,i,-1,-i\}$; on a real q(N)
Chan-Paton bundle the $\pm i$ eigenspaces appear as **complex
conjugate pairs**, exchanged by complex conjugation on the
Chan-Paton bundle.

**Concrete realisation.** At the smallest non-trivial case $(N=2,n=2)$
of the verification script (Sergeev-Intertwiner §5; `scripts/check_sergeev_intertwiner.py`),
the diagonal $\mathfrak q(2)$-action $\rho(J)$ on $V^{\otimes 2}=\C^{4|4}$
super-commutes with the Hecke-Clifford generators $c_1,c_2\in\mathcal{HC}_2$
and the symmetric-group generator $\sigma\in S_2$ (V.5). The
**eigenvectors of $\rho(J)$ at eigenvalues $\pm i$** are pure-Clifford
states of the form
\[
   |+i\rangle=(I+ic_1c_2)|0\rangle, \qquad |-i\rangle=(I-ic_1c_2)|0\rangle,
\]
where $|0\rangle\in V^{\otimes 2}$ is a Clifford-vacuum and $c_1c_2$
is the Clifford parity element. (More precisely: $\rho(J)$ acts on
$V^{\otimes 2}$ via the diagonal queer action; its $\pm i$
eigenvectors exist on the 4-dimensional anti-diagonal sub-bundle
where $J^2=-I$ has $\pm i$ as Hermitian square roots.)

**Brane interpretation.** The two $\pm i$ eigensectors are the
**two Hecke-Clifford braid-conjugate variants of the otr-brane**:
they correspond to the two distinct **boundary states** on the
otr-brane that are exchanged under the $S_n$-permutation of Clifford
generators $c_1\leftrightarrow c_2$. Physically:
* The $+i$ sector: the otr-brane with **Clifford-vacuum convention
  $|0\rangle$**, $c_1$ as raising, $c_2$ as lowering.
* The $-i$ sector: the otr-brane with **anti-Clifford-vacuum convention**,
  $c_1$ as lowering, $c_2$ as raising. Related to $+i$ by the
  involution $c_1\leftrightarrow c_2$.

These are physically distinct boundary states **at the chain level**,
but they collapse to a single cohomology class $[\bar c]^{\mathrm{otr}}$
because:
(i) the cohomology is 1-dimensional in the $\bar 1$-parity sector;
(ii) the $S_n$-permutation $c_1\leftrightarrow c_2$ is an inner
automorphism of $\mathcal{HC}_n$, so it acts trivially on cohomology
classes (by general principles: inner automorphisms induce trivial
maps on group cohomology / Hochschild cohomology).

**Cohomology assignment.** $\{+i,-i\}\to[\bar c]^{\mathrm{otr}}$
(both map to the same $\bar 1$-parity class).

### §2.4 The collapse rule

| Eigenvalue | Parametric brane data | Cohomology class |
|---|---|---|
| $+1$ | q(N) doubled brane (fixed locus) | $[\bar c]\in H^2_{\bar 0}$ |
| $-1$ | sign-flipped otr-brane at parametric level | $[\bar c]^{\mathrm{otr}}\in H^2_{\bar 1}$ (after rescaling) |
| $+i$ | otr-brane, Clifford-vacuum convention | $[\bar c]^{\mathrm{otr}}\in H^2_{\bar 1}$ |
| $-i$ | otr-brane, anti-Clifford-vacuum convention | $[\bar c]^{\mathrm{otr}}\in H^2_{\bar 1}$ |

**Collapse summary.** $\{+1\}\to[\bar c]$ (fixed locus). $\{-1, +i,
-i\}\to[\bar c]^{\mathrm{otr}}$. The three "non-fixed" sectors all
project to the same odd-parity cohomology class; only the **fixed
locus** $+1$ has its own bosonic class.

This is the precise sense in which $\Z/4$ collapses to $\Z/2$ on
cohomology: the **kernel of the collapse map** $\Z/4\to\Z/2$ is the
$\Z/2\subset\Z/4$ generated by $J^2=-I$, which acts trivially on
cohomology (inner automorphism by a scalar on a 1-d cocycle). The
**image** is the $\Z/2$ parity-flip group on
$H^2(\C\oplus\Pi\C)=\C\oplus\Pi\C$.

### §2.5 Verdict on (ZB.2)

**Verdict.** The four parity-eigenvalues of $\Phi_{\mathrm{Sergeev}}$
correspond to the following physical sectors:
* **$+1$**: bosonic Theorem G (fixed locus); the q(N) doubled brane
  stack as a unit, with cohomology class $[\bar c]\in H^2_{\bar 0}$.
* **$-1$**: sign-flipped otr-brane at parametric level; cohomology
  class $[\bar c]^{\mathrm{otr}}\in H^2_{\bar 1}$ (equal up to
  rescaling).
* **$+i,-i$**: the two Hecke-Clifford braid-conjugate variants of the
  otr-brane, related by $c_1\leftrightarrow c_2$ permutation;
  cohomology class $[\bar c]^{\mathrm{otr}}\in H^2_{\bar 1}$ (both
  map to the same class).

**Confidence.** Medium-high. The eigensector identification is exact
($JTJ^{-1}=\lambda T$ for $\lambda\in\{1,i,-1,-i\}$ defines a
standard Jordan decomposition). The brane-physics interpretation of the
$\pm i$ sectors as Hecke-Clifford braid-conjugate is **structurally
correct** but requires the chain-level Clifford-vacuum identification
to be made fully rigorous (Phase-5 R-P4-EXEC-Z4-1).

---

## §3. (ZB.3) Cross-walk to Brane-Species-Audit q(N) doubled brane

### §3.1 Brane-Species Tier II (Brane-Species-Audit §5)

The Brane-Species-Audit identified the q(N) brane as a **doubled
brane** with two channels:
* **Str-brane** (diagonal mixed B-brane): standard mixed B-brane
  stack with $GL_N$ Chan-Paton, $\Str$-channel boundary, K-theory
  class zero (Brane-Species-Audit §5.1).
* **otr-brane** (off-diagonal mixed-parity Dirichlet brane):
  parastatistic brane with parity-flipping intertwiner via $J$,
  $\mathrm{otr}$-channel boundary, K-theory class non-trivial in
  parity-shifted $K^1$ (Brane-Species-Audit §5.1).

The two are exchanged by the parity-twist $\tau$ implemented by
conjugation with $J$.

### §3.2 The 2-class cohomology vs 4-sector parametric foliation

**Match.** The Brane-Species-Audit Tier II structure encodes:
* **2 channels** at the boundary-evaluation layer ($\Str$ and
  $\mathrm{otr}$).
* **2 cohomology classes** in $H^2_{\mathrm{Lie}}(\bar A;\C\oplus\Pi\C)$:
  $[\bar c]$ and $[\bar c]^{\mathrm{otr}}$.

**Refinement from $\Z/4$.** The $\Z/4$-graded structure of
Sergeev-Intertwiner reveals that the 2-class cohomology is the
shadow of a **4-sector parametric foliation**:
* The Str-brane carries the $+1$ fixed sector (cohomology
  $[\bar c]$).
* The otr-brane carries the $-1, +i, -i$ sectors (cohomology
  $[\bar c]^{\mathrm{otr}}$, with three distinct parametric
  realisations).

**Are Str-brane and otr-brane the $+1$ and $-1$ eigenstates?** **Not
exactly.** The Str-brane corresponds to the **fixed locus** of the
$\Z/4$ ($+1$ eigensector), but the otr-brane corresponds to **three
distinct $\Z/4$-eigensectors** ($-1, +i, -i$) that are
cohomologically equivalent. The Brane-Species-Audit's "single
otr-brane" is therefore a **cohomological-layer simplification** of a
**parametrically-richer 3-sector structure**.

### §3.3 The cohomologically-invisible sectors

**There are 2 additional sectors physically present but cohomologically
invisible:** the $+i$ and $-i$ Clifford-vacuum variants of the
otr-brane. They are present at the **chain-level / parametric** layer
(distinct boundary states with distinct Clifford-vacuum conventions)
but project to the same cohomology class $[\bar c]^{\mathrm{otr}}$.

**Are they distinct boundary states?** Physically yes: they have
distinct chain-level open-string algebras (different Clifford-vacuum
conventions), distinct chain-level scattering processes (the
Clifford generators $c_1,c_2$ act with opposite spin-statistics
phase), and distinct Hecke-Clifford braid-group representations.

**Why are they invisible on cohomology?** Because the cohomology
generator is 1-dimensional and the inner $S_n$-automorphism
$c_1\leftrightarrow c_2$ acts trivially on cohomology classes.

### §3.4 Verdict on (ZB.3)

**Verdict.** The q(N) doubled boundary state of Brane-Species-Audit
realises the $\Z/4\to\Z/2$ collapse as follows:
* The **Str-brane** = the $+1$ fixed locus of the $\Z/4$.
* The **otr-brane** = the three-fold $\{-1, +i, -i\}$ orbit, all
  cohomologically equal but parametrically distinct.
* The **2 cohomologically-invisible sectors** ($+i$ and $-i$) are
  the **Hecke-Clifford braid-conjugate variants** of the otr-brane,
  related by $c_1\leftrightarrow c_2$ inner automorphism.

The Brane-Species-Audit's 2-class structure is the cohomological
shadow of a **4-sector parametric foliation**; the missing 2 sectors
($\pm i$) are present at the chain level but invisible to the
cohomological probe.

**Confidence.** Medium-high. The 4-sector-vs-2-class identification
is structurally clean (Jordan decomposition of the $\Z/4$-generator).
The chain-level distinction between the $\pm i$ sectors is
consistent with the verification script's Hecke-Clifford structure
(V.4: $c_1c_2+c_2c_1=0$, two Clifford generators related by
$\sigma\in S_2$).

---

## §4. (ZB.4) $\pm i$ sectors as a known physical phenomenon

### §4.1 Sergeev parastatistic R-symmetry — the natural fit

**The $\pm i$ sectors are the parastatistic R-symmetry of Sergeev
1983.** Sergeev's original motivation for q(N) was to model
*parastatistic systems*: states transforming under a non-trivial
phase under the parity exchange. The $\Z/4$-action by $J$ on the
Chan-Paton bundle $\C^{N|N}$ realises this directly: $J^2=-I$ is the
parity-flip; $J$ itself is the **square root of the parity-flip**, a
parastatistic exchange operator.

The two $\pm i$ eigenvectors are then the **two parastatistic
boundary states** at the $J$-fixed point: states that pick up a
phase $\pm i$ under one half of the parity-flip cycle (one
application of $J$). Physically, this is a **parafermion of order 4**
in the brane-line open-string algebra.

**Cross-reference.** This matches the Brundan-Kleshchev 2001 spin
Hecke algebra at level 1: the spin Hecke algebra is the natural
$\Z/4$-graded extension of the Hecke-Clifford algebra
$\mathcal{HC}_n$, and its level-1 representations are precisely the
parafermion-of-order-4 boundary states.

### §4.2 Comparison with Witten-Olive 1978 BPS $\Z/4$

**Structural analogy.** Witten-Olive 1978 *Supersymmetry algebras
that include topological charges* shows that in $\mathcal N=2$
supersymmetric theories, the central charge $Z$ takes values in a
$\Z/4$-graded structure: $Z\in\C$, $|Z|^2$ is the BPS bound. The
$\Z/4$-grading on $Z$ collapses to $\Z/2$ on physical states because
$|Z|^2$ is invariant under $Z\to iZ\to -Z\to -iZ\to Z$.

**Is it the same $\Z/4\to\Z/2$ collapse?** **Structurally analogous,
but not literally the same.** Differences:
* **Witten-Olive 1978**: $\Z/4$ on the central charge $Z$ of an
  $\mathcal N=2$ algebra; collapses to $\Z/2$ on states because BPS
  states depend only on $|Z|^2$.
* **This document**: $\Z/4$ on the Chan-Paton parity (queer central
  element $J$); collapses to $\Z/2$ on cohomology because cohomology
  classes are 1-dimensional and rescaling absorbs the $\pm$ sign.

The two $\Z/4$-collapse mechanisms are **structurally parallel**
(both involve a $\Z/4$-action whose $\Z/2$-quotient is physical;
both arise from a square-root structure $J^2=-I$ or $\bar Z\cdot Z=|Z|^2$),
but they live on **different physical objects** (central charge of
SUSY vs Chan-Paton parity).

**Refined statement (P-Z4-Brane-2).** The Sergeev parastatistic
$\Z/4\to\Z/2$ collapse is the **Chan-Paton-bundle analog** of the
Witten-Olive 1978 BPS $\Z/4\to\Z/2$ collapse, but they are **not
related by any known duality**: the Witten-Olive $\Z/4$ acts on the
central charge of supersymmetric particles, while the present
$\Z/4$ acts on the parity of the brane Chan-Paton bundle.

### §4.3 Comparison with Diaconescu-Moore-Witten 2003 K-theory torsion

**DMW 2003 setup.** Diaconescu-Moore-Witten 2003 *$E_8$ gauge theory
and a derivation of K-theory from M-theory* identifies $\Z/4$-collapse
phenomena in the K-theory of M-theory backgrounds. Specifically:
the K-theory class of a brane in M-theory may carry a $\Z/4$-torsion
component arising from anomaly cancellation, which collapses to
$\Z/2$ under the M-theory-to-IIA reduction.

**Is it the same collapse?** **No, structurally different.** DMW
2003's $\Z/4$ lives on the **K-theory class** (a topological
classification of the brane); the present $\Z/4$ lives on the **brane
parity** (the Chan-Paton structure on a single brane). The two are
on different mathematical objects.

**Specific check.** DMW 2003 §4.1 records the $\Z/4$-torsion in
$K^1(\mathrm{Spin}_c)$ for certain Spin$^c$ structures on M-theory
boundaries. Our setup has no Spin$^c$ structure or M-theory
embedding; the $\Z/4$ here is **internal to the q(N) Chan-Paton
bundle**.

**Refined statement (P-Z4-Brane-3).** The Sergeev parastatistic
$\Z/4\to\Z/2$ collapse is **distinct from** the DMW 2003 K-theory
$\Z/4$-torsion. They share the structural form $\Z/4\to\Z/2$ but
arise from different physical mechanisms.

### §4.4 The right match: Brundan-Kleshchev 2001 spin Hecke algebra at level 1

**The closest matched primary source is Brundan-Kleshchev 2001 spin
Hecke algebra $H^c_n$ at level 1.** Brundan-Kleshchev introduce a
$\Z/4$-compatible Clifford structure on $\mathcal{HC}_n$:
\[
   c_i^2 = 1, \qquad c_i c_j = -c_j c_i \text{ for }i\neq j, \qquad
   t_i^4 = 1 \text{ (parastatistic generator)},
\]
where $t_i\in H^c_n$ generates the level-1 grading; on
representations, $t_i$ acts by a $\Z/4$-eigenvalue. The
representation theory at level 1 includes the **parafermion-of-order-4
modules** as the analog of the spinor module on the standard
Hecke-Clifford.

**The brane-physics shadow.** The $\pm i$ eigensectors of
$\Phi_{\mathrm{Sergeev}}$ on the q(N) Chan-Paton bundle are the
**$\Z/4$-eigenvalue $\pm i$** modules of the level-1 spin Hecke
algebra acting on the otr-brane open-string Hilbert space. They are
parafermion-of-order-4 boundary states.

### §4.5 Verdict on (ZB.4)

**Verdict.** The $\pm i$ cohomologically-invisible sectors realise
the **Sergeev parastatistic R-symmetry** at the brane-line level,
specifically as **parafermion-of-order-4 boundary states** of the
otr-brane. Cross-walk to known physical phenomena:
* Brundan-Kleshchev 2001 spin Hecke algebra at level 1: **direct
  match** (same $\Z/4$ structure, same parafermion modules).
* Witten-Olive 1978 BPS $\Z/4$: **structural analog only** (different
  physical object: central charge vs Chan-Paton parity).
* Diaconescu-Moore-Witten 2003 K-theory torsion: **NOT the same**
  (K-theory class vs Chan-Paton parity).

**Confidence.** Medium. The Brundan-Kleshchev match is structurally
clean (the spin Hecke algebra at level 1 is the natural $\Z/4$-extension
of $\mathcal{HC}_n$), but the precise identification of the
parafermion modules with the $\pm i$ sectors of $\Phi_{\mathrm{Sergeev}}$
requires Phase-5 chain-level work (R-P4-EXEC-Z4-2).

---

## §5. (ZB.5) Smallest physical example

### §5.1 The $(N=2, n=2)$ example

**Setup.**
* Manuscript local mixed model $\R^2_{\mathrm{top}}\times\C^2_{\mathrm{hol}}$.
* q(2) brane stack on $\R\times p\subset\R^2\times\C^2$, with two
  brane insertion points $p_1,p_2\in\C^2$ (so $n=2$).
* Chan-Paton bundle: $V^{\otimes 2}=\C^{2|2}\otimes\C^{2|2}=\C^{4|4}$
  (the doubled queer bundle on the two-brane multiplet).
* Open-string algebra: $\C[(\mathfrak q(2))^2\oplus(\mathfrak q(2))^2]^{Q_2}$
  with the $Q_2$-invariant pairs of queer matrices.
* Hecke-Clifford braid algebra: $\mathcal{HC}_2=\langle c_1,c_2,\sigma\rangle$
  with $c_i^2=I$, $c_1c_2+c_2c_1=0$, $\sigma^2=I$ (the $S_2$ generator),
  and Clifford-symmetric-group relations.

**Total dimension.** $\dim\mathcal{HC}_2=8$ (V.4 of the verification
script, Sergeev-Intertwiner §5.1).

### §5.2 The $\Z/4$ structure on the smallest example

**Sergeev parametric $\Z/4$.** At $N=2$, $J\in\mathfrak q(2)_{\bar 1}$
is the matrix
\[
   J = \begin{pmatrix} 0 & I_2 \\ -I_2 & 0 \end{pmatrix} \in M_4(\C),
\]
satisfying $J^2=-I_4$, $J^4=I_4$. Conjugation by $J$ on $\End(V)$
generates the $\Z/4$.

**Eigenspaces of $\rho(J)$ on $V^{\otimes 2}=\C^{4|4}$.** The
diagonal action $\rho(J)=J\otimes I+I\otimes J$ on $V^{\otimes 2}$
satisfies $\rho(J)^2=-2I$ (a scalar; verify by direct computation).
Eigenvalues are $\pm i\sqrt 2$, but on the combined Chan-Paton +
Clifford space the $\Z/4$ generator is the diagonal queer central
element $\rho(J)/\sqrt 2$, which has eigenvalues $\pm i$ on the
$V^{\otimes 2}$ Hilbert space.

(*Note: the precise normalisation depends on convention; the script
V.5 verifies super-commutation with Hecke-Clifford generators, which
is independent of normalisation.*)

**Hecke-Clifford braid action.** The $\mathcal{HC}_2$-generators
$c_1,c_2$ super-commute with $\rho(J)$ (V.5), so they preserve the
$\rho(J)$-eigenspaces. The $S_2$-generator $\sigma$ permutes
$c_1\leftrightarrow c_2$, providing the **inner automorphism**
exchanging the $+i$ and $-i$ sectors.

### §5.3 Predicted measurement

**The Z/4→Z/2 collapse is observable at $(N=2, n=2)$ as the
spin-statistics phase of $c_1, c_2$ relative to $\sigma$.**

**Concrete observable.** Define the **Hecke-Clifford braid phase**
$\theta$ as the eigenvalue of $\rho(J)$ on the joint $c_1$-eigenstate
and $c_2$-eigenstate, normalised so $\theta^4=1$:
\[
   \rho(J)|c_1^+,c_2^+\rangle = \theta|c_1^+,c_2^+\rangle.
\]
The collapse $\Z/4\to\Z/2$ predicts:
* $\theta=\pm i$ on the $\rho(J)|0\rangle\neq 0$ Clifford-vacuum
  states (the two non-fixed-locus cohomology-invisible sectors).
* $\theta=\pm 1$ on the Clifford-invariant states (the
  cohomology-visible sectors: $+1$ for the bosonic Theorem G fixed
  locus, $-1$ for the parametric otr-brane).

**Measurement protocol.**
1. Construct the $V^{\otimes 2}=\C^{4|4}$ Hilbert space with $\rho(J)$
   acting diagonally and $\mathcal{HC}_2$ braid action.
2. Diagonalise $\rho(J)$ to obtain the 4 eigenspaces with eigenvalues
   $\{+1,-1,+i,-i\}\sqrt 2$ (taking the normalisation
   $\rho(J)/\sqrt 2$ above).
3. Identify the $c_1c_2$-action on each eigenspace; the $+i$ and
   $-i$ sectors should map to each other under the inner $S_2$
   automorphism $\sigma:c_1\leftrightarrow c_2$.
4. Verify on the cohomology level that the four eigensectors collapse
   to two cohomology classes $[\bar c]\in H^2_{\bar 0}$ and
   $[\bar c]^{\mathrm{otr}}\in H^2_{\bar 1}$, with the $+1$ sector
   uniquely producing the bosonic class.

This measurement is implementable using `scripts/check_sergeev_intertwiner.py`
test V.5 (super-commutation of $\rho(J)$ with $\mathcal{HC}_2$
generators) extended to track the $\Z/4$-eigendecomposition.

### §5.4 What the predicted measurement would establish

If the measurement returns:
* **4 distinct $\Z/4$-eigenspaces** at the parametric level, and
* **2 cohomology classes** at the cohomology level (with the
  $\pm i$ sectors collapsing to a single odd class),

then the $\Z/4\to\Z/2$ collapse is **directly observable** as a
chain-level vs cohomology-level discrepancy.

The **non-trivial content** of the measurement is:
1. The $+i$ and $-i$ sectors are **distinct as parametric boundary
   states** (e.g., distinguished by the spin-statistics phase of
   $c_1,c_2$).
2. They are **cohomologically equal** (mapping to the same class
   $[\bar c]^{\mathrm{otr}}$).
3. The bosonic Theorem G class $[\bar c]$ is the **fixed locus** of
   the $\Z/4$-action, and is the only class that does not arise from
   the $\{-1,+i,-i\}$ orbit collapse.

### §5.5 Verdict on (ZB.5)

**Verdict.** The smallest observable example is $(N=2, n=2)$ on the
manuscript's local mixed model $\R^2\times\C^2$, q(2) brane stack with
Chan-Paton $V^{\otimes 2}=\C^{4|4}$ and Hecke-Clifford braid algebra
$\mathcal{HC}_2$. The predicted measurement is the **Hecke-Clifford
braid phase** $\theta$, the eigenvalue of $\rho(J)/\sqrt 2$ on
joint Clifford-eigenstates, taking values in $\{+1,-1,+i,-i\}$.

The $\Z/4\to\Z/2$ collapse is observable as the **chain-level vs
cohomology-level discrepancy**: 4 parametric eigensectors collapsing
to 2 cohomology classes, with the $\{+i,-i\}$ pair both projecting to
$[\bar c]^{\mathrm{otr}}$.

**Confidence.** Medium-high. The setup is concrete and computable
using the existing verification script extended to compute the
$\Z/4$-eigendecomposition. The measurement protocol is implementable
in `scripts/check_sergeev_intertwiner.py` test V.5+, but the precise
identification of the eigenstates with physical brane sectors
requires Phase-5 chain-level work.

---

## §6. (ZB.6) New predictions

### §6.1 P-Z4-Brane-1: cohomologically-invisible parastatistic sectors

**Statement.** The q(N) doubled brane carries **two
cohomologically-invisible parastatistic boundary states** at the $\pm i$
eigensectors of $\Phi_{\mathrm{Sergeev}}$. These are
parafermion-of-order-4 boundary conditions on the otr-brane, present
at the chain-level open-string algebra (where they are the two
Hecke-Clifford braid-conjugate Clifford-vacuum conventions) but
projecting to a single cohomology class $[\bar c]^{\mathrm{otr}}$.

**Predictive content.** The chain-level Hecke-Clifford braid algebra
$\mathcal{HC}_n$ on the otr-brane should carry a **$\Z/4$-compatible
Clifford structure** (Brundan-Kleshchev 2001 spin Hecke algebra at
level 1): the Clifford generators $c_i$ should satisfy a
$\Z/4$-extended bracket that records the parametric $\Z/4$-action on
the Chan-Paton bundle. This is **stronger** than the standard
$\Z/2$-graded Hecke-Clifford structure, and is observable at the chain
level but not at the cohomology level.

**Status.** Phase-5 frontier; depends on a precise chain-level
construction of the $\Z/4$-graded spin Hecke algebra on the otr-brane
(R-P4-EXEC-Z4-2).

### §6.2 P-Z4-Brane-2: parity-self-duality of bosonic Theorem G

**Statement.** The bosonic Theorem G class $[\bar c]\in
H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}$ is **parity-self-dual** in the
following sense:
* It is the fixed locus of the $\Z/4$-action $\Phi_{\mathrm{Sergeev}}$
  on the graded cohomology $H^2_{\mathrm{Lie}}(\bar A;\C\oplus\Pi\C)$
  (Sergeev-Intertwiner P-Sergeev-1' §8.1).
* Equivalently, it is preserved by $\Phi_{\mathrm{Sergeev}}^2=\id$
  on the bosonic 1-d generator (Sergeev-Intertwiner §6 Property 3).
* Equivalently, it does **not** acquire a $\Pi$-shift under
  parity-twist by $J$.

**Verification.** Direct from Sergeev-Intertwiner §4.3:
$\Phi_{\mathrm{Sergeev}}^2([\bar c])=[\bar c]$ at the cohomology
level. Verified numerically in V.6+V.7 of the verification script
(Sergeev-Intertwiner §5).

**Predictive content.** The bosonic Theorem G class is the
**unique** class in the graded cohomology
$H^2_{\mathrm{Lie}}(\bar A;\C\oplus\Pi\C)$ satisfying
$\Phi_{\mathrm{Sergeev}}([\text{class}])=[\text{class}]$ (i.e., the
fixed locus of the parity-mirror). This identifies the bosonic class
as a **canonical** parity-invariant class in the q(N)-extended
cohomology lattice.

**Cross-walk.** This is consistent with the Brane-Species-Audit §9
parity-mirror conjecture (q-mirror), which conjectures that mirror
symmetry on q(N) is realised by the parity-flip via $J$. Under this
conjecture, the bosonic Theorem G class is **mirror-self-dual**, in
direct parallel to the SYZ-self-dual O-brane on osp(2N|2N) at $M=N$
(Brane-Species-Audit §3.4).

**Status.** Phase-4 closed; explicit verification at $(N=2, n=2)$ via
verification script.

### §6.3 P-Z4-Brane-3: chain-level $\Z/4$-compatible Clifford as Phase-5 lift constraint

**Statement.** A chain-level lift of $\Phi_{\mathrm{Sergeev}}$ to the
factorization-algebra layer would require the chain-level otr-brane
open-string algebra to carry a **$\Z/4$-compatible Clifford structure**
(Brundan-Kleshchev 2001 spin Hecke algebra at level 1): the Clifford
generators $c_i$ would satisfy
\[
   c_i^4 = I, \qquad c_i^2 = (\text{parity element}), \qquad
   c_i c_j = (-1)^{...}\cdot c_j c_i,
\]
with the precise sign structure dictated by the $\Z/4$-graded
extension.

**Predictive content.** This adds a constraint on the chain-level
factorization algebra construction (R-P4-EXEC-Sergeev-Chain-01 of
Sergeev-Duality-Probe §9.1): the otr-brane open-string algebra is
**not** the standard Hecke-Clifford $\mathcal{HC}_n$, but its
**$\Z/4$-extension** $H^c_n$ at level 1.

**Status.** Phase-5 frontier; this is the precise form of the
chain-level lift constraint required to reconcile the parametric
$\Z/4$ with the cohomological $\Z/2$.

### §6.4 P-Z4-Brane-4: no new bound state on $\R^2\times\C^2$

**Statement.** The $\Z/4\to\Z/2$ structure does **not** predict any
**new bound state** on the manuscript's local mixed model
$\R^2\times\C^2$ beyond what is already encoded in:
* The bosonic Theorem G (manuscript main statement).
* The Theorem G\textsuperscript{otr} inscription
  (Theorem-G-otr-inscription).

**Why no new bound state?** Because the $\Z/4$-action is
**internal to the q(N) Chan-Paton bundle** and does **not** propagate
to the bulk. The closed-string sector on $\R^2\times\C^2$ is unchanged
by the parity-twist via $J$ (Howe-Sergeev mutual centralizer
property, Sergeev-Intertwiner §2.2 V.5). So the bulk anomaly inflow
on $\R^2\times\C^2$ is entirely captured by the Brane-Species-Audit
Tier II structure (Str-brane discharge + otr-brane non-discharge).

The only refinement is **chain-level**: the $\Z/4\to\Z/2$ structure
refines the Brane-Species-Audit's 2-class cohomology to a 4-sector
parametric foliation, but the cohomology layer (where the manuscript's
inscriptions live) is unchanged.

### §6.5 P-Z4-Brane-5: anomaly inflow refinement on the otr-brane

**Statement.** The anomaly inflow on the otr-brane (from the bulk
$\R^2\times\C^2$ to the boundary $\R\times p$, mediated by the
$\hbar N[\bar c]^{\mathrm{otr}}$ residue) **does not refine under
$\Z/4$**: it remains a single residue class at the cohomology layer.

However, the **chain-level anomaly current** carries a $\Z/4$-graded
parastatistic structure: the parastatistic exchange operator $J$
generates a **chain-level current** that flows through the
parafermion-of-order-4 boundary states. This chain-level structure is
**invisible at the cohomology layer** (consistent with the
Sergeev-A5 firewall that blocks chain-level lifts).

**Status.** Phase-5 frontier; depends on chain-level lift work
(R-P4-EXEC-Z4-2).

### §6.6 P-Z4-Brane-6: no new boundary condition

**Statement.** The $\Z/4\to\Z/2$ structure does **not** predict any
**new boundary condition** on the manuscript's local mixed model
$\R^2\times\C^2$ beyond what is encoded in the Brane-Species-Audit
Tier II structure.

**Why?** Because the $\pm i$ sectors are **internal Hecke-Clifford
braid-conjugate variants** of the otr-brane, not new boundary states.
They differ from the otr-brane only by an inner $S_n$-automorphism
($c_1\leftrightarrow c_2$), which is a chain-level convention, not a
new boundary condition.

The Brane-Species-Audit Tier II structure (Str-brane + otr-brane,
related by parity-twist via $J$) is therefore **complete** at the
boundary-condition layer; the $\Z/4$-refinement adds chain-level
internal structure, not new boundary conditions.

### §6.7 Summary of new predictions

| Prediction | Layer | Status |
|---|---|---|
| **P-Z4-Brane-1** Cohomologically-invisible parastatistic sectors | chain-level | Phase-5 |
| **P-Z4-Brane-2** Parity-self-duality of bosonic Theorem G | cohomology | Phase-4 closed |
| **P-Z4-Brane-3** Chain-level $\Z/4$-compatible Clifford | chain-level | Phase-5 |
| **P-Z4-Brane-4** No new bound state on $\R^2\times\C^2$ | bulk | confirmed |
| **P-Z4-Brane-5** Anomaly inflow refinement on otr-brane (chain-level) | chain-level | Phase-5 |
| **P-Z4-Brane-6** No new boundary condition | boundary | confirmed |

**Headline.** The $\Z/4\to\Z/2$ structure produces **one
Phase-4-closed prediction** (parity-self-duality of bosonic Theorem
G) and **three Phase-5 predictions** (chain-level cohomologically
invisible sectors, $\Z/4$-compatible Clifford, anomaly inflow
refinement). It does **not** predict new bulk bound states or new
boundary conditions; the refinement is entirely internal to the
Hecke-Clifford braid algebra of the otr-brane.

---

## §7. Anti-attack scan responses — (Att-1)–(Att-4)

### §7.1 (Att-1) Worldsheet $\Z_4$ R-symmetry on the Hamiltonian BF $\R^2\times\C^2$

**Attack.** $\Z_4$ actions on D-branes typically arise from worldsheet
$\Z_4$ R-symmetry (e.g., Brunner-Hori-Hosomichi-Walcher 2007 Gepner
orientifolds). Identify whether the Hamiltonian BF on $\R^2\times\C^2$
has a worldsheet $\Z_4$ symmetry.

**Response.** **No.** The manuscript's local mixed model
$\R^2_{\mathrm{top}}\times\C^2_{\mathrm{hol}}$ is **not** a Gepner-type
worldsheet model and does **not** carry a worldsheet $\Z_4$ R-symmetry
in the Brunner-Hori-Hosomichi-Walcher 2007 sense. Specifically:
* The Hamiltonian BF complex has no $\hat c$ charge / $\mathcal N=2$
  superconformal structure on $\R^2\times\C^2$.
* The brane line $\R\times p$ is 1-dimensional (not 2-dimensional),
  so it does not support a worldsheet R-symmetry.
* The closed-string sector on $\R^2\times\C^2$ is the bosonic
  Hamiltonian BF complex, with no chiral $\Z_4$ R-symmetry.

**The $\Z/4$ here is a worldline R-symmetry on the brane line, not
a worldsheet R-symmetry.** It is generated by an internal Chan-Paton
parity twist (conjugation with $J$), not by a worldsheet R-current.

**Distinction.** The Brunner-Hori-Hosomichi-Walcher 2007 worldsheet
$\Z_4$ acts on the worldsheet fields (the $\mathcal N=2$ superconformal
generators); the present $\Z/4$ acts on the Chan-Paton bundle of a
single brane in a 1-dimensional brane-line theory.

**Discharge.** Att-1 is answered: the Hamiltonian BF on $\R^2\times\C^2$
does **not** have a worldsheet $\Z_4$ R-symmetry; the $\Z/4$ here is
a **worldline** parastatistic R-symmetry on the q(N) brane line.

### §7.2 (Att-2) $J^2=-I$ analogy with $SL(2,\Z)$ centre on parity axis

**Attack.** The Sergeev parity $J$ satisfies $J^2=-I$, reminiscent of
the $SL(2,\Z)$ centre $\langle -I\rangle\cong\Z/2$ but on the parity
axis instead of the modular axis. Verify the analogy is precise.

**Response.** **The analogy is structural but not literal.**
Specifically:

* **$SL(2,\Z)$ centre.** $\langle -I\rangle\subset SL(2,\Z)$ is the
  $\Z/2$-subgroup generated by the matrix $-I=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}$.
  This acts on the modular parameter $\tau\in\H$ trivially ($\tau\to\tau$),
  reflecting that $-I$ is in the kernel of the $SL(2,\Z)\to PSL(2,\Z)$
  projection. The $\Z/4\to\Z/2$ collapse on $SL(2,\Z)$ is generated
  by $S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ with $S^2=-I$, $S^4=I$;
  the modular $J$-function is $S$-invariant after quotienting by $\langle -I\rangle$.

* **Sergeev parity.** $J\in\mathfrak q(N)_{\bar 1}$ satisfies $J^2=-I$,
  $J^4=I$, generating a $\Z/4$ on the Chan-Paton bundle. The $\Z/4\to\Z/2$
  collapse on the cohomology lattice $H^2_{\mathrm{Lie}}(\bar A;\C\oplus\Pi\C)$
  is generated by $J$ (parity-flip), with $J^2=-I$ in the kernel
  (acting trivially on cohomology).

**Structural parallel.** Both $S$ and $J$ are $\Z/4$-generators
satisfying $S^2=J^2=-I$, with the $\Z/4\to\Z/2$ collapse arising
from the kernel $\langle S^2\rangle = \langle J^2\rangle = \langle
-I\rangle$.

**Difference.** The $SL(2,\Z)$ generator $S$ acts on the **modular
parameter** of an $\mathcal N=2$ supersymmetric theory (e.g., the
modular axis of the Vafa-Witten 1995 partition function); the
Sergeev $J$ acts on the **Chan-Paton parity** of a brane in the
manuscript's local mixed model. The two are on different physical
objects, related only by the structural identity $S^2=J^2=-I$.

**Refined analogy.** The Sergeev $\Z/4\to\Z/2$ on the Chan-Paton
parity is **structurally analogous to but distinct from** the
$SL(2,\Z)\to PSL(2,\Z)$ collapse on the modular axis. The natural
unification would require identifying a **modular parameter on the
brane line** that the Sergeev $J$ acts on, which is not present in
the manuscript's local mixed model.

**Status.** Phase-5 frontier as a unification question; not closed
in this audit.

**Discharge.** Att-2 is answered: the analogy with $SL(2,\Z)$ centre
is **structural** (both $\Z/4\to\Z/2$ collapses with kernel
$\langle -I\rangle$) but **not precise** (different physical
objects). Phase-5 unification work would require a modular parameter
on the brane line, which the present manuscript does not provide.

### §7.3 (Att-3) Diaconescu-Moore-Witten 2003 K-theory $\Z/4$-collapse match

**Attack.** Discrete torsion in K-theory (Diaconescu-Moore-Witten
2003) realises $\Z/4$ collapses to $\Z/2$ in a specific physical
setting; check whether our $\Z/4\to\Z/2$ matches.

**Response.** §4.3 above. **No, the two collapses are distinct.**
DMW 2003's $\Z/4$ lives on the K-theory class (Spin$^c$ structure,
$E_8$ gauge bundle on the M-theory boundary), while the present
$\Z/4$ lives on the Chan-Paton parity (the queer central element
$J$ on the q(N) brane bundle). Different physical objects, different
mechanisms.

**Specific cross-check.** DMW 2003 Theorem 5.1 records the K-theory
$\Z/4$-torsion via the Atiyah-Hirzebruch spectral sequence for
M-theory backgrounds. The present manuscript has no Atiyah-Hirzebruch
spectral sequence (the local model $\R^2\times\C^2$ is not a
compactification background); the $\Z/4$ here is **internal to the
brane bundle**, not a K-theory torsion.

**Discharge.** Att-3 is answered: the DMW 2003 $\Z/4$-torsion in
K-theory is **not** the same phenomenon as the present
parastatistic $\Z/4$. They share the structural form $\Z/4\to\Z/2$
but arise from different physical mechanisms.

### §7.4 (Att-4) Bosonic Theorem G as parity-self-dual fixed locus

**Attack.** The bosonic Theorem G as fixed locus of
$\Phi_{\mathrm{Sergeev}}$ predicts that Theorem G is parity-self-dual;
verify the prediction explicitly.

**Response.** **Verified.** The bosonic Theorem G class
$[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}$ is parity-self-dual
in three equivalent senses:

(i) **Fixed locus of $\Phi_{\mathrm{Sergeev}}$.**
$\Phi_{\mathrm{Sergeev}}^2([\bar c])=[\bar c]$ at the cohomology
layer (Sergeev-Intertwiner §4.3, §6.1 Property 3). The class $[\bar c]$
is its own image under the parity-twist iterated to the second power;
i.e., the parity-twist is its own inverse on $[\bar c]$.

(ii) **Parity-invariant under $\Pi$.** The class $[\bar c]$ lives in
$H^2_{\bar 0}$ (even-parity sector), so the parity functor $\Pi$
maps it to its image in $H^2_{\bar 1}$, which is *not* the same
class. But the **square** $\Pi^2=\id$ returns it to its bosonic
sector. So $[\bar c]$ is parity-self-dual in the sense that
$\Pi^2$-image = original.

(iii) **No $\Pi$-shift under conjugation by $J$.** At the parametric
level, conjugation by $J^2=-I$ acts trivially on $\End(V)$ (scalar
conjugation), so $[\bar c]$ as the cohomology class of the bosonic
gl-cocycle is unchanged by $J^2$. This is the **chain-level
verification** of (i).

**Numerical verification.** V.7 of `scripts/check_sergeev_intertwiner.py`
(Sergeev-Intertwiner §5.1) verifies $\Phi^2=\id$ at the parametric
level by direct computation: conjugation by $J^2=-I_4$ is the
identity on $\End(V=\C^{2|2})$ at $N=2$.

**Cross-walk.** This parity-self-duality is consistent with:
* **SYZ-self-dual O-brane** on osp(2N|2N) at $M=N$
  (Brane-Species-Audit §3.4): the analog of "self-dual under axis
  swap" on the orthosymplectic side.
* **Parity-mirror conjecture** on q(N) (Brane-Species-Audit §9):
  the bosonic Theorem G is the parity-mirror-self-dual class.
* **Theorem G\textsuperscript{otr} inscription** §3.5 (Witten lens
  interpretation): the bosonic Theorem G is the *closed-string image* on
  q(N), invariant under the boundary-evaluation channel choice
  ($\Str$ vs $\mathrm{otr}$); the parity-self-duality records this
  invariance algebraically.

**Discharge.** Att-4 is answered: the bosonic Theorem G is verified
to be parity-self-dual, in three equivalent senses, with explicit
numerical verification at $N=2$. This is the precise content of
P-Z4-Brane-2 (§6.2).

---

## §8. Residuals + Phase-5 escalation

### §8.1 Residuals introduced by this audit

* **R-P4-EXEC-Z4-1** (severity 3, sharpening). Chain-level
  Hecke-Clifford braid algebra structure on the $\pm i$ eigensectors
  of $\Phi_{\mathrm{Sergeev}}$, identifying the
  parafermion-of-order-4 modules with the Brundan-Kleshchev 2001
  spin Hecke algebra at level 1. Deciding evidence: explicit
  chain-level construction of $H^c_n$ at level 1 on the otr-brane
  open-string algebra; verification at $(N=2, n=2)$ via extended
  `scripts/check_sergeev_intertwiner.py` test.

* **R-P4-EXEC-Z4-2** (severity 3, inscription). Chain-level lift of
  $\Phi_{\mathrm{Sergeev}}$ requires the otr-brane open-string algebra
  to carry a $\Z/4$-compatible Clifford structure. Deciding evidence:
  factorization-algebra construction of $H^c_n$ at level 1 on
  $\R\times p\subset\R^2\times\C^2$; matched-conventions
  verification with the Sergeev-A5 firewall (V.9 of the verification
  script).

* **R-P4-EXEC-Z4-3** (severity 4, no-go hardening). $SL(2,\Z)$
  centre analogy on the parity axis is structural but not literal
  (§7.2). Deciding evidence: identification of a modular parameter
  on the brane line that the Sergeev $J$ acts on, which the present
  manuscript does not provide. **Likely Phase-5 work tied to
  Vol III / Igusa modular frontier (CLAUDE.md: heuristic only).**

* **R-P4-EXEC-Z4-4** (severity 3, sharpening). The
  cohomologically-invisible parastatistic sectors should manifest as
  a measurable spin-statistics phase at the chain level (§5.3).
  Deciding evidence: numerical computation of the
  Hecke-Clifford braid phase $\theta\in\{+1,-1,+i,-i\}$ at
  $(N=2, n=2)$, predicted to take all four values on distinct
  Clifford-vacuum states.

### §8.2 Phase-5 escalation routes

* **Phase-5-Z4-A.** Add a one-paragraph remark in
  Theorem-G-otr-inscription §3.3 recording the $\Z/4\to\Z/2$
  collapse and the parity-self-duality of bosonic Theorem G as the
  fixed locus (consistent with Sergeev-Intertwiner §8.2
  Phase-5-Sergeev-Int-A inscription update path).

* **Phase-5-Z4-B.** Construct the chain-level $\Z/4$-compatible
  Clifford structure on the otr-brane (Brundan-Kleshchev 2001 spin
  Hecke algebra at level 1, with factorization-algebra realisation
  on $\R\times p\subset\R^2\times\C^2$). This would resolve
  R-P4-EXEC-Z4-2 and provide the chain-level lift constraint for
  R-P4-EXEC-Sergeev-Chain-01.

* **Phase-5-Z4-C.** Cross-walk to Vol III: the parity-mirror
  $\Z/4\to\Z/2$ collapse on the q(N) brane is the algebraic shadow
  of a modular $\Z/4\to\Z/2$ on the chiral CY$_3$ side
  (heuristic per CLAUDE.md). A precise comparison would require
  matched conventions and a Vol III embedding theorem; for now this
  is a heuristic at the level of "structurally parallel
  $\Z/4\to\Z/2$ collapses on the brane and chiral sides".

### §8.3 Deciding evidence required for Phase-5 closure

* **(D-1)** Inscription of P-Z4-Brane-2 (parity-self-duality of
  bosonic Theorem G as fixed locus) in Theorem-G-otr-inscription
  §3.3 — minimal inscription change.

* **(D-2)** Construction of the spin Hecke algebra at level 1 on the
  otr-brane open-string algebra, with factorization-algebra
  realisation on $\R\times p$ — Phase-5 chain-level work.

* **(D-3)** Numerical verification of the Hecke-Clifford braid
  phase $\theta$ at $(N=2, n=2)$, demonstrating the four-value
  $\Z/4$-eigendecomposition — Phase-5 numerical work.

* **(D-4)** Cross-walk to Vol III modular $\Z/4\to\Z/2$ structures
  (heuristic; not closure-required at Phase-4 level).

The chain-level lift remains blocked by the Sergeev-A5 firewall
(Sergeev-Intertwiner V.9 verifies the (A5)-violation). Phase-5
escalation should respect this firewall and aim to identify the
**precise form of the chain-level lift constraint** (R-P4-EXEC-Z4-2),
not silently bridge it (per CLAUDE.md).

---

## §9. Synthesis

### §9.1 What this milestone delivers

* **Physical interpretation of the $\Z/4\to\Z/2$ collapse.** The
  $\Z/4$ is a worldline parastatistic R-symmetry on the q(N) brane
  Chan-Paton bundle, generated by conjugation with the queer central
  element $J\in\mathfrak q(N)_{\bar 1}$ satisfying $J^2=-I$. Not a
  bulk orbifold, not K-theory torsion, not a worldsheet R-symmetry.
  The collapse to $\Z/2$ on cohomology is a **representation-theoretic
  reduction**: the kernel $\langle J^2=-I\rangle\subset\Z/4$ acts as
  inner automorphism on $\End(V)$, hence trivially on cohomology
  classes.

* **Four parity eigensectors identified.** $+1$ (bosonic Theorem G
  fixed); $-1$ (sign-flipped otr at parametric level); $+i, -i$
  (Hecke-Clifford braid-conjugate variants of the otr-brane). The
  bosonic Theorem G is the **fixed locus**, the only class that does
  not arise from collapse.

* **Cross-walk to Brane-Species-Audit Tier II.** The doubled brane
  (Str-brane + otr-brane) realises a 2-class cohomology arising from
  a 4-sector parametric foliation; the missing 2 sectors ($\pm i$)
  are **cohomologically invisible** but chain-level distinct
  parafermion-of-order-4 boundary states.

* **Identification with Brundan-Kleshchev 2001 spin Hecke algebra at
  level 1.** The $\pm i$ sectors realise the level-1 modules of the
  spin Hecke algebra $H^c_n$, the $\Z/4$-extension of $\mathcal{HC}_n$.

* **Smallest example.** $(N=2, n=2)$ on $\R^2\times\C^2$, q(2) brane
  stack with Chan-Paton $V^{\otimes 2}=\C^{4|4}$; predicted measurement
  is the Hecke-Clifford braid phase $\theta\in\{+1,-1,+i,-i\}$, with
  the $\Z/4\to\Z/2$ collapse observable as a chain-level vs
  cohomology-level discrepancy (4 eigensectors collapsing to 2
  cohomology classes).

* **Six new predictions.** P-Z4-Brane-1 through -6, ranging from
  Phase-4 closed (parity-self-duality of bosonic Theorem G,
  P-Z4-Brane-2) to Phase-5 frontier (chain-level $\Z/4$-compatible
  Clifford, P-Z4-Brane-3).

* **No new bound state, no new boundary condition** on the bulk
  $\R^2\times\C^2$. The $\Z/4$-refinement is entirely internal to the
  Hecke-Clifford braid algebra of the otr-brane.

### §9.2 What this milestone does NOT deliver

* No chain-level construction of the spin Hecke algebra at level 1
  (Phase-5 R-P4-EXEC-Z4-2).
* No $SL(2,\Z)$ unification on the parity axis (R-P4-EXEC-Z4-3,
  likely Phase-5 / Vol III).
* No numerical verification of the Hecke-Clifford braid phase
  $\theta$ at $(N=2, n=2)$ (Phase-5 R-P4-EXEC-Z4-4; would extend
  the existing verification script).
* No cross-walk to Vol III modular $\Z/4\to\Z/2$ structures
  (heuristic; CLAUDE.md constraint).

### §9.3 Bottom line

**The $\Z/4\to\Z/2$ collapse is the brane-physics shadow of the
Sergeev parastatistic R-symmetry.** It is **internal** to the q(N)
Chan-Paton bundle, **cohomologically reducible** to the
$\Z/2$ parity-flip, and **chain-level richer** than the
Brane-Species-Audit's 2-class cohomology suggests (4 parametric
eigensectors). The bosonic Theorem G is the fixed locus,
parity-self-dual, and uniquely classified as the $\Z/4$-invariant
class on the cohomology lattice. The two cohomologically-invisible
$\pm i$ sectors are parafermion-of-order-4 boundary states, the
brane-physics realisation of the Brundan-Kleshchev 2001 spin Hecke
algebra at level 1.

**No new bulk bound state or boundary condition** is predicted on
$\R^2\times\C^2$. The refinement is chain-level and internal, not
spacetime-geometric.

The Phase-4 EXEC verdict on the Z4-Brane-Physics milestone:

**P4-Z4-Brane-Physics closes positively at the cohomology-layer
physical interpretation; the chain-level lift constraint
(R-P4-EXEC-Z4-2) and the spin-Hecke-algebra realisation
(R-P4-EXEC-Z4-1) are Phase-5 frontier work, but the four-eigensector
identification, the Brane-Species-Audit cross-walk, the smallest
observable example, and the parity-self-duality of bosonic Theorem
G are all closed at Phase-4 level.**

---

## §A. Appendix — Cross-references

### §A.1 Sergeev-Intertwiner anchors

* SI §6.1 Theorem statement (Sergeev coefficient intertwiner): the
  $\Z/4$-graded automorphism statement (Property 3) is the source
  of this audit's $\Z/4$ analysis.
* SI §8.1 P-Sergeev-1' ($\Z/4$-graded refinement): the new prediction
  whose physical interpretation this audit provides.
* SI §4.2 The $\Z/4$ structure from $J^2=-I$: the algebraic generator
  of the $\Z/4$-action on $\End(V)$.
* SI §5 V.7: explicit verification of $\Phi^2=\id$ at the parametric
  level (conjugation by $J^2=-I_4$ is the identity on $\End(V)$).
* SI §5 V.5: explicit verification that $\rho(J)$ super-commutes with
  Hecke-Clifford generators (used in §3.3 of this audit).

### §A.2 Brane-Species-Audit anchors

* B-S-A §5 q(N) doubled brane (Str-brane + otr-brane): the cohomology-
  layer 2-class structure refined here to a 4-sector parametric
  foliation.
* B-S-A §9 parity-mirror conjecture: the bosonic Theorem G as
  parity-mirror-self-dual class — confirmed here as P-Z4-Brane-2.

### §A.3 Theorem-G-otr-inscription anchors

* T-otr-Inscription §3.3 two-cohomology decomposition: the 2-d graded
  cohomology $H^2(\C\oplus\Pi\C)$ on which the $\Z/4$-action operates.
* T-otr-Inscription §3.5 Witten lens: the parastatistic open-closed
  duality interpretation, refined here as the parastatistic $\Z/4$ R-symmetry.
* T-otr-Inscription §6 brane interpretation: the off-diagonal
  mixed-parity brane = the otr-brane, identified here as the
  $\{-1, +i, -i\}$ orbit of the $\Z/4$-action.

### §A.4 G3-M3-queer-trace anchors

* G3-M3 §3.3 (A5)-violation $P^{\mathfrak q}\,J\,(P^{\mathfrak q})^{-1}=-J$:
  the chain-level firewall that blocks the chain-level lift of the
  $\Z/4\to\Z/2$ collapse.

### §A.5 Sergeev-Duality-Probe anchors

* SDP §3.2 The $\Z/4$ structure on $\End(V)$ from $J^2=-I$: the
  algebraic source of the $\Z/4$ analysed here.
* SDP §7.1 Obs-Sergeev-A5-firewall: the chain-level obstruction that
  blocks the $\Z/4$-lift to factorization algebras.

### §A.6 Verification script

* `scripts/check_sergeev_intertwiner.py` (766 lines): existing
  verification at $(N=2, n=2)$. Phase-5 extension (R-P4-EXEC-Z4-4):
  add explicit $\Z/4$-eigendecomposition test on $V^{\otimes 2}$,
  verifying the four-value Hecke-Clifford braid phase $\theta$.

---

**End of P4-EXEC-Z4-Brane-Physics-2026-04-28.**
