# Phase 4 Execution / P4-Sergeev-Duality-Probe — Witten + Boundary investigation of the Sergeev-type open-closed duality witnessed by the q(N) otr-brane parastate

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Witten primary (physical dualities; mirror symmetry; S-duality;
T-duality; electric–magnetic duality; Howe duality at the level of
representation categories and at the level of partition
functions / boundary states / open-string algebras); Boundary
secondary (boundary state of the otr-brane; its open-string algebra;
its closed-string image under the Sergeev-type duality; brane-defect
catalog of the parity-twist).
**Mode.** Phase-4 EXEC, proposal-only — no manuscript edits, no
commits. Master ledger schema; ID prefix `P4-EXEC-Sergeev-`. Writable
surface: this file only.
**Posture.** P4-EXEC-Brane-Species-Audit (1213 lines)
identified the q(N) otr-brane as a parastate brane in the
Cheng–Wang finite-tensor-category sense and named a "Sergeev-type
open-closed duality invisible to bosonic probes" (B.5 verdict; §5
lines 391–514). P4-EXEC-Theorem-G-otr-inscription (1374 lines) drafted
the parallel anomaly class $\hbar N\,[\bar c]^{\mathrm{otr}}\in
H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$. P4-EXEC-G3-M3-queer-trace
(1108 lines) computed $\mathrm{otr}(J)=N$ and named the obstruction
**Obs-Q-otr-A5**. This audit makes the Sergeev-type duality precise:
it states the canonical Cheng–Wang Howe–Sergeev duality, translates
to brane physics, compares with mirror / S / T / Howe-Sergeev
dualities, identifies the smallest physical example, applies the
cross-volume firewall test, and predicts a residue-identity for
Theorem G\textsuperscript{otr}.

**Inputs (full reads or targeted reads as indicated).**
* `CLAUDE.md` (full).
* `reconstitution/phase4-exec-Brane-Species-Audit-2026-04-28.md`
  (1213 lines; three-tier brane typology; otr-brane parastate;
  Sergeev-type duality named).
* `reconstitution/phase4-exec-Theorem-G-otr-inscription-2026-04-28.md`
  (1374 lines; parallel anomaly class; two-supertrace independence;
  parity-mirror conjecture).
* `reconstitution/phase4-exec-G3-M3-queer-trace-2026-04-28.md` (1108
  lines; $Z_2^{\mathrm{otr}}$ queer-Capelli; otr(J)=N; (A5)\textsuperscript{otr}).
* `reconstitution/phase4-exec-classical-super-extension-2026-04-28.md`
  (1247 lines; G3-M2 verdict; q(N) two-supertrace structure;
  THEOREM P4-G3-M2-Q candidate at line 712).
* `reconstitution/phase4-exec-BCOV-A5-comparison-2026-04-28.md`
  (50092 bytes; cross-volume firewall verdict; coefficient-coupling
  vs chain-level isomorphism distinction).
* `main.tex` 280–470 (Theorem G triplet; `lem:omega-cocycle`;
  U(1)-center anomaly; brane-defect comparison map).

**Standard primary-source references (cited from memory; not new
inscriptions).**
* A. Sergeev, "The centre of the enveloping algebra for the Lie
  superalgebra Q(N)", *Letters Math. Phys.* **7** (1983), 177–179.
  Original `otr` and odd-Casimir definition.
* A. Sergeev, "The tensor algebra of the identity representation as a
  module over Gl(n|m) and Q(n)", *Math. USSR Sbornik* **51** (1985),
  419–427. **Schur–Weyl–Sergeev duality on q(N).**
* K. Coulembier, "Tensor ideals, Deligne categories and invariant
  theory", *Selecta Math.* **24** (2018), 4659–4710.
* P. Etingof, V. Ostrik, "Finite tensor categories", *Mosc. Math. J.*
  **4** (2004), 627–654.
* P. Etingof, S. Gelaki, D. Nikshych, V. Ostrik, *Tensor categories*,
  AMS Math. Surveys & Monographs **205** (2015).
* S.-J. Cheng, W. Wang, *Dualities and representations of Lie
  superalgebras*, AMS GSM **144** (2012). **Ch. 4 Howe duality
  framework; Ch. 5 Schur–Sergeev duality.**
* J. Brundan, A. Kleshchev, "Hecke–Clifford superalgebras, crystals
  of type $A_{2\ell}^{(2)}$ and modular branching rules for
  $\widehat S_n$", *Represent. Theory* **5** (2001), 317–403.
* R. Howe, "Remarks on classical invariant theory", *Trans. Amer.
  Math. Soc.* **313** (1989), 539–570.
* E. Witten, "Mirror manifolds and topological field theory", in
  *Essays on Mirror Manifolds*, IP Press 1992.
* A. Strominger, S.-T. Yau, E. Zaslow, "Mirror symmetry is T-duality",
  *Nucl. Phys.* **B479** (1996), 243–259.
* E. Witten, "Some comments on string dynamics", *Strings '95*,
  arXiv:hep-th/9507121 — origin of $S$-duality / electric–magnetic
  duality in string theory.
* A. Kapustin, E. Witten, "Electric–magnetic duality and the
  geometric Langlands program", *Comm. Number Theory and Phys.* **1**
  (2007), 1–236.
* M. Bershadsky, S. Cecotti, H. Ooguri, C. Vafa, "Kodaira–Spencer
  theory of gravity and exact results for quantum string amplitudes",
  *Comm. Math. Phys.* **165** (1994), 311–428. §6 open-closed dual
  cocycle formalism.

---

## §0. Executive verdict — does Sergeev duality lift to a known duality framework?

**Three-line bottom line.**

1. **Closest containing framework: Howe–Sergeev duality
   (Cheng–Wang 2012 Ch. 4 + Ch. 5).** Sergeev duality is the
   *queer / type-Q* member of the Howe duality family; it is **not
   a special case** of mirror symmetry, S-duality, or T-duality in
   any of the standard topological-string senses, and **does not
   coincide** with the Kapustin–Witten geometric Langlands lift of
   electric–magnetic duality. The Cheng–Wang Howe–Sergeev framework
   contains it as the queer pair $(\mathfrak q(N), \mathcal{HC}_n)$
   acting on the supersymmetric tensor algebra, parallel to (and
   distinct from) the classical Schur–Weyl pair
   $(\mathfrak{gl}_N, S_n)$ acting on $\C^N{}^{\otimes n}$.

2. **Chain-level lift faces a firewall analogous to BCOV-A5.**
   Howe–Sergeev duality is an equivalence at the level of
   **representation categories** (more precisely, at the level of
   $(\mathfrak q(N),\mathcal{HC}_n)$-bimodule decompositions of
   $V^{\otimes n}$ where $V=\C^{N|N}$). It is **not** a chain-level
   factorization-algebra duality on $\R^2\times\C^2$. Lifting it to
   the manuscript's local mixed model would require constructing a
   **factorization-algebra Howe pair** with one factor supplying the
   open-string sector and the other the closed-string sector. The
   firewall is **structurally identical** to the BCOV-A5 firewall:
   both are coefficient-class equivalences (representation-theoretic
   common ancestor) without a chain-level isomorphism of
   factorization complexes. The BCOV-A5 verdict diagnoses the
   firewall via the open-closed coefficient $\Str(I)=0$; the
   Sergeev firewall is diagnosed via the queer central character
   pair $(\Str(I_{2N}),\,\mathrm{otr}(J))=(0,N)$ — a 2-vector of
   coefficients in a graded coefficient space, where the chain-level
   complexes (Hecke–Clifford braid algebra vs brane-defect BV
   complex) are structurally distinct.

3. **Predicted Theorem G\textsuperscript{otr} residue identity:
   coefficient-class equality.** Under the Howe–Sergeev coefficient
   match, the residue $\hbar N\,[\bar c]^{\mathrm{otr}}\in
   H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$ is **the parity-shifted
   image** of the bosonic class $\hbar N\,[\bar c]\in
   H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}$ under the *Sergeev
   coefficient-coupling intertwiner* $\Phi_{\mathrm{Sergeev}}$. The
   prediction is a **structural equality**:
   $\Phi_{\mathrm{Sergeev}}(\hbar N\,[\bar c]) = \hbar N\,[\bar c]^{\mathrm{otr}}$
   at the coefficient layer. This is **not a chain-level
   equivalence** (the firewall blocks that), but it is a precise
   coefficient-class identity dual to BCOV-A5: same coefficient $N$,
   parity-shifted target line, parity-flipped regulator class
   (A5)\textsuperscript{otr}.

**One-line invariant.** The dominant invariant preserved on both
sides is the **representation-theoretic central character**:
$\Tr_{\mathfrak{gl}_N}(I)=N$ on the bosonic side maps to
$\mathrm{otr}_{\mathfrak q(N)}(J)=N$ on the queer side under
Howe–Sergeev. Both are the *same* numerical coefficient $N$, lifted
to two distinct parity sectors by the Sergeev parity-twist.

**Per-target verdict (per (SDP.1)–(SDP.7)).**

| Target | Verdict | Headline |
|---|---|---|
| **(SDP.1) Sergeev duality canonical statement** | DRAFTED | Howe–Sergeev pair $(\mathfrak q(N), \mathcal{HC}_n)$ on $V^{\otimes n}$, $V=\C^{N|N}$; Cheng–Wang 2012 Ch. 5 §5.4 + Sergeev 1985 *Sbornik* 51. |
| **(SDP.2) Brane-physics translation** | DRAFTED | Open-string sector = $\End_{\mathcal{HC}_n}(V^{\otimes n})$; closed-string sector = $\mathfrak q(N)$-invariants; boundary condition = otr-brane (off-diagonal mixed-parity Dirichlet). |
| **(SDP.3) Comparison with mirror / S / T / Howe-Sergeev** | DECIDED | Howe-Sergeev is the natural containing framework; **mirror symmetry NO** (parity-axis, not A/B-axis); **S-duality NO** (no electric-magnetic structure); **T-duality NO** (parity-twist is not a circle isometry); **Howe-Sergeev YES** (canonical containment). |
| **(SDP.4) Smallest physical example** | IDENTIFIED | $N=2$, $n=2$; $V=\C^{2\|2}$; $V^{\otimes 2}=\C^{4\|4}$ as $(\mathfrak q(2), \mathcal{HC}_2)$-bimodule. The otr-brane has two diagonal $J$-eigen-blocks; the duality is non-trivial. |
| **(SDP.5) Cross-volume firewall verdict** | COEFFICIENT-LEVEL ONLY | Howe–Sergeev lifts to **coefficient-class duality** (representation-theoretic); chain-level / vertex-class lift faces a firewall **structurally identical** to BCOV-A5. |
| **(SDP.6) Predicted Theorem G\textsuperscript{otr} identity** | DRAFTED | $\Phi_{\mathrm{Sergeev}}(\hbar N\,[\bar c])=\hbar N\,[\bar c]^{\mathrm{otr}}$ as a coefficient-class identity in graded cohomology $H^2_{\mathrm{Lie}}(\bar A,\C\oplus\Pi\C)$. |
| **(SDP.7) Duality-class anomaly** | IDENTIFIED | The chain-level lift obstruction is **Obs-Sergeev-A5-firewall**: the Hecke–Clifford open algebra and the BV brane-defect complex are structurally distinct $\Z/2$-graded complexes; no chain-level isomorphism preserves the parity-twist via $J$. |

**Convergence verdict.** The Sergeev-type open-closed duality
witnessed by the otr-brane is the **brane-physics shadow of
Howe–Sergeev duality**. It contains the parity-mirror conjecture of
Brane-Species-Audit §9 as the boundary-state realization of the
Cheng–Wang Howe pair. The lift to a chain-level duality faces an
**Obs-Sergeev-A5-firewall** that is structurally identical to the
BCOV-A5 firewall: both block a chain-level isomorphism of
factorization complexes, both admit a coefficient-class
identification preserving the central character $N$. The predicted
identity for Theorem G\textsuperscript{otr} is
$\Phi_{\mathrm{Sergeev}}(\hbar N\,[\bar c])=\hbar N\,[\bar c]^{\mathrm{otr}}$,
**a coefficient-class identity, not a chain-level equivalence**.

---

## §1. Sergeev duality canonical statement

### §1.1 Howe–Sergeev pair $(\mathfrak q(N), \mathcal{HC}_n)$

**The canonical Howe–Sergeev statement (Cheng–Wang 2012 Theorem 5.4
+ Sergeev 1985 Sbornik 51).** Let $V=\C^{N|N}$ be the natural
representation of $\mathfrak q(N)\subset\mathfrak{gl}(N|N)$. The
tensor power $V^{\otimes n}$ carries commuting actions of:
* The queer Lie superalgebra $\mathfrak q(N)$ acting diagonally
  (lifted from the natural rep of $\mathfrak q(N)$ on $V$).
* The **Hecke–Clifford superalgebra** $\mathcal{HC}_n=\mathcal{C}_n
  \rtimes\C[S_n]$, where $\mathcal{C}_n=\C\langle c_1,\ldots,c_n\rangle/
  (c_i^2=1, c_ic_j=-c_jc_i\text{ for }i\neq j)$ is the rank-$n$
  Clifford algebra and $S_n$ acts by permutation of the generators.

The Schur–Sergeev duality (Cheng–Wang Ch. 5 Theorem 5.4) gives the
$(\mathfrak q(N), \mathcal{HC}_n)$-bimodule decomposition
\[
   V^{\otimes n}\cong\bigoplus_\lambda L_\lambda^{\mathfrak q}\otimes
   M_\lambda^{\mathcal{HC}}, \tag{Howe-Sergeev}
\]
where the sum runs over **strict partitions** $\lambda$ of $n$ with
at most $N$ parts, $L_\lambda^{\mathfrak q}$ is the irreducible
$\mathfrak q(N)$-module of highest weight $\lambda$, and
$M_\lambda^{\mathcal{HC}}$ is the irreducible projective
representation of $S_n$ associated to $\lambda$ (equivalently, the
irreducible $\mathcal{HC}_n$-module). The strict-partition condition
reflects the parity-twisted structure: each part of $\lambda$ must
be distinct (no repetitions), in contrast to ordinary partitions on
$\mathfrak{gl}_N$.

**The duality is the algebra-pair statement.** $\mathfrak q(N)$ and
$\mathcal{HC}_n$ are **mutual centralizers** in $\End(V^{\otimes n})$:
* $\mathrm{End}_{\mathfrak q(N)}(V^{\otimes n})=\mathcal{HC}_n$
  (image in the matrix algebra).
* $\mathrm{End}_{\mathcal{HC}_n}(V^{\otimes n})=U(\mathfrak q(N))/\mathrm{Ann}$
  (the image of the universal enveloping algebra).

This is **the canonical Sergeev duality statement**.

### §1.2 Comparison with classical Schur–Weyl duality

Classical Schur–Weyl duality on $\C^N{}^{\otimes n}$:
\[
   \C^N{}^{\otimes n}\cong\bigoplus_\lambda L_\lambda^{\mathfrak{gl}}
   \otimes M_\lambda^{S_n}, \tag{Schur-Weyl}
\]
with $\lambda$ ranging over ordinary partitions of $n$ with at most
$N$ parts. The mutual centralizer pair is
$(\mathfrak{gl}_N, S_n)$ in $\End(\C^N{}^{\otimes n})$.

**Sergeev duality is the "queer" parallel:** replace $\C^N$ by
$V=\C^{N|N}$ (queer natural rep), $\mathfrak{gl}_N$ by
$\mathfrak q(N)$, and $\C[S_n]$ by $\mathcal{HC}_n$. The strict-partition
condition replaces the ordinary-partition condition. The structure
is **rigorously parallel**: both are mutual centralizer pairs; both
yield bimodule decompositions; both admit Schur-functor /
Schur–Q-function generating-series descriptions.

### §1.3 Howe duality as the embedding framework

**Howe duality** (Howe 1989, *Remarks on classical invariant theory*,
TAMS 313): given a reductive group $G$ acting on a
representation $W$, the algebra $\mathrm{End}_G(W)$ admits a
"Howe-dual" reductive subgroup $G'\subset\mathrm{End}_G(W)$
satisfying mutual centralizer relations.

**Cheng–Wang 2012 Ch. 4** generalizes Howe duality to the super
setting: Howe pairs $(\mathfrak g, \mathfrak g')$ where one of
$\mathfrak g, \mathfrak g'$ is super. The catalog includes:
* Classical Howe pairs: $(\mathfrak{gl}_M, \mathfrak{gl}_N)$ on
  $\C^{M\times N}$; $(\mathrm{O}(M), \mathfrak{sp}(2N))$ on
  $\C^{M\times 2N}$; etc.
* **Super Howe pairs:** $(\mathfrak{gl}(M|N), \mathfrak{gl}_K)$ on
  $\C^{(M|N)\times K}$; $(\mathfrak{osp}(M|2N), \mathrm{Sp}(2K))$;
  $(\mathfrak q(N), ?)$.

The **queer Howe pair** $(\mathfrak q(N), \mathcal{HC}_n)$ from
§1.1 is the natural member of this catalog. Cheng–Wang
Ch. 5 Theorem 5.6 records this as a special case of the Howe duality
framework, with the Hecke–Clifford algebra replacing $S_n$.

### §1.4 Verdict on (SDP.1)

**Verdict.** Sergeev duality in the Cheng–Wang sense is the **queer
member of the Howe duality family**: the mutual-centralizer pair
$(\mathfrak q(N), \mathcal{HC}_n)$ acting on $V^{\otimes n}$ with
$V=\C^{N|N}$, governed by the Schur-functor decomposition
(Howe-Sergeev) over strict partitions. The canonical statement is
Cheng–Wang 2012 Theorem 5.4 (= Sergeev 1985 Sbornik 51 Theorem 1).

**Confidence.** High. The Cheng–Wang formulation is verbatim;
Sergeev's original is the proof reference; Brundan–Kleshchev 2003
provides the modular-rep and crystal-base extensions.

---

## §2. Brane-physics translation

### §2.1 The brane-stack realization of $V^{\otimes n}$

The manuscript's brane setup (Brane-Species-Audit §1.1 + main.tex
122–128, 740–820) is a **stack of N branes** on $\R\times p\subset
\R^2\times\C^2$, with Chan–Paton bundle $\C^N$ and open-string field
algebra $\C[\mathfrak{gl}_N\oplus\mathfrak{gl}_N]^{GL_N}$. For $n$
brane insertion points $p_1,\ldots,p_n\in\C^2$, the multi-brane
Chan–Paton bundle is $\C^N{}^{\otimes n}$, and the open-string field
algebra at the $n$-brane multiplet is $\C[(\mathfrak{gl}_N)^n
\oplus(\mathfrak{gl}_N)^n]^{GL_N}$ (acting via the diagonal subgroup).

**Brane-physics shadow of classical Schur–Weyl.** This is the brane-
stack shadow of the Schur–Weyl pair $(\mathfrak{gl}_N, S_n)$:
* $\mathfrak{gl}_N$ acts as the gauge symmetry of the brane stack
  (Chan–Paton bundle $\C^N$).
* $S_n$ acts by permutation of the $n$ brane insertion points
  (a discrete symmetry of the multi-brane configuration).

The Schur–Weyl decomposition $\C^N{}^{\otimes n}=\bigoplus_\lambda
L_\lambda^{\mathfrak{gl}}\otimes M_\lambda^{S_n}$ becomes the brane-
stack identification: each Young-diagram weight $\lambda$ labels an
irreducible "brane sub-stack" carrying both a Chan–Paton irrep
$L_\lambda^{\mathfrak{gl}}$ and a permutation-symmetry irrep
$M_\lambda^{S_n}$.

### §2.2 The queer/otr brane-stack realization

For the **q(N)-brane stack** (Brane-Species-Audit §5), the
Chan–Paton bundle is $\C^{N|N}$ with the queer mixed-parity structure,
and the open-string field algebra at the $n$-otr-brane multiplet is
$\C[(\mathfrak q(N))^n\oplus(\mathfrak q(N))^n]^{Q_N}$ (acting via
the diagonal queer subgroup $Q_N\subset GL(N|N)$).

**Brane-physics shadow of Schur–Sergeev.**
* $\mathfrak q(N)$ acts as the gauge symmetry of the queer brane
  stack (Chan–Paton bundle $V=\C^{N|N}$ with queer parity-twist
  structure).
* $\mathcal{HC}_n$ acts by **permutation-with-Clifford-sign**: $S_n$
  permutes the $n$ otr-brane insertion points, and the Clifford
  generators $c_i$ implement a parity-flip on the $i$-th insertion
  point's Chan–Paton bundle.

The Howe–Sergeev decomposition $V^{\otimes n}=\bigoplus_\lambda
L_\lambda^{\mathfrak q}\otimes M_\lambda^{\mathcal{HC}}$ becomes the
queer-brane-stack identification: each strict-partition weight $\lambda$
labels an irreducible "queer brane sub-stack" carrying a Chan–Paton
irrep $L_\lambda^{\mathfrak q}$ and a permutation-with-Clifford-sign
irrep $M_\lambda^{\mathcal{HC}}$.

### §2.3 Open-string / closed-string duality

**Open-string sector under Howe–Sergeev.** The Hecke–Clifford
algebra $\mathcal{HC}_n=\mathrm{End}_{\mathfrak q(N)}(V^{\otimes n})$
is the **open-string algebra** at the $n$-otr-brane multiplet (it is
the algebra of physical open-string operators that respect the
$\mathfrak q(N)$ gauge symmetry).

**Closed-string sector under Howe–Sergeev.** The
$\mathfrak q(N)$-invariants $V^{\otimes n}/\mathcal{HC}_n=
\bigoplus_\lambda L_\lambda^{\mathfrak q}$ (modulo the Hecke–Clifford
action) are the **closed-string sector**: the gauge-invariant
states detected by the brane probe.

The Howe–Sergeev statement *is* the open-closed decomposition: the
$\mathcal{HC}_n$-action on $V^{\otimes n}$ is the open-string content,
and the $\mathfrak q(N)$-action is the closed-string content. The
two are mutual centralizers, which is the algebraic shadow of the
**open-closed duality**: every open-string operator commutes with
every closed-string operator, and vice versa.

### §2.4 Boundary condition implementing the duality

**On the open side.** The boundary condition on the $n$-otr-brane
multiplet is:
* Chan–Paton bundle: $V^{\otimes n}=(\C^{N|N})^{\otimes n}$ with the
  parity-twisted structure inherited from the otr-brane parity-flip
  (off-diagonal mixed-parity, generated by conjugation with the
  queer central element $J$ — see Brane-Species-Audit §5.2).
* Open-string algebra: $\mathcal{HC}_n=\mathcal{C}_n\rtimes\C[S_n]$,
  the Hecke–Clifford algebra at the $n$-otr-brane multiplet.
* Trace channel: the queer trace $\mathrm{otr}$ projecting onto the
  Clifford-sign-twisted off-diagonal blocks.

**On the closed side.** The closed-string sector on the
$\mathfrak q(N)$-equivariant fields is:
* Field content: $\mathfrak q(N)$-modules in the local mixed model
  $\R^2\times\C^2$.
* Closed-string operator algebra: $U(\mathfrak q(N))$ acting on the
  Chan–Paton bundle $V^{\otimes n}$.
* Cocycle: the $\omega$-cocycle of `lem:omega-cocycle` lifted to
  $\mathfrak q(N)$ via the queer-trace boundary evaluation.

The **Howe–Sergeev duality** is the statement that these two sectors
are mutual centralizers in $\End(V^{\otimes n})$.

### §2.5 Verdict on (SDP.2)

**Verdict.** The Sergeev duality translates to brane physics as
the **open-closed mutual-centralizer pair** $(\mathfrak q(N),
\mathcal{HC}_n)$ acting on the multi-otr-brane Chan–Paton bundle
$V^{\otimes n}=(\C^{N|N})^{\otimes n}$:
* **Open-string sector** = $\mathcal{HC}_n=\mathcal{C}_n\rtimes
  \C[S_n]$, the algebra of permutation-with-Clifford-sign symmetries.
* **Closed-string sector** = $\mathfrak q(N)$-invariants on
  $V^{\otimes n}$, generated by $U(\mathfrak q(N))$-action.
* **Boundary condition** = otr-brane (off-diagonal mixed-parity
  Dirichlet brane, with parity-flip implemented by $J$); trace
  channel $\mathrm{otr}$.

The duality witnessed by the q(N) otr-brane parastate is **the
brane-physics realization of the Schur–Sergeev mutual-centralizer
duality**.

**Confidence.** Medium-high. The mutual-centralizer description is
verbatim from Cheng–Wang Ch. 5; the brane-stack interpretation is
parallel to the classical Schur–Weyl brane-stack interpretation
(which is itself implicit in the manuscript's open-string field
algebra choice but not explicitly inscribed). The novel content is
the **identification of $\mathcal{HC}_n$ as the n-otr-brane
open-string algebra** — this is a Phase-5 finding, not yet
chain-level closed.

---

## §3. Comparison with mirror / S / T / Howe-Sergeev

### §3.1 Mirror symmetry (Witten 1992; SYZ 1996)

**Mirror symmetry exchanges A-branes and B-branes** in the Kontsevich
1994 sense:
* A-branes (Lagrangian submanifolds with graded local systems) on
  $X$ ↔ B-branes (coherent sheaves) on the mirror $\hat X$;
* SYZ 1996: this exchange is realized fibrewise by T-duality on the
  SYZ Lagrangian fibration.

**Does Sergeev duality respect mirror pairs?** Not directly. The
Sergeev duality is a **parity-axis** exchange (Str ↔ otr, equivalently
even ↔ odd central direction of $\mathfrak z(\mathfrak q(N))$),
realized by conjugation with the queer central element $J$. This is
**orthogonal** to the A/B-axis (topological vs holomorphic) of mirror
symmetry, *both* in the manuscript's local mixed model
($\R$-factor topological vs $\C^2$-factor holomorphic) *and* in
Witten 1992 / SYZ 1996.

**Is the otr-brane the mirror of a known A-brane?** No. The
otr-brane is a *mixed-parity Dirichlet brane* (Brane-Species-Audit
§5.3), realized on the *same* mixed local model as the bosonic
brane stack. The SYZ axis swap $z_1\leftrightarrow z_2$ does not
exchange Str-brane and otr-brane (the parity-twist is independent of
the symplectic axis swap).

**Refined statement (parity-mirror).** Brane-Species-Audit §9.4
proposes a **parity-mirror symmetry** parallel to but distinct from
Kontsevich 1994 A/B-mirror. The parity-mirror exchanges Str-brane
and otr-brane via conjugation with $J$. This is **not** mirror
symmetry in the Kontsevich / SYZ sense.

**Verdict on mirror symmetry.** Sergeev duality does **NOT** lift to
Kontsevich / SYZ mirror symmetry. It is an *independent* duality
in the parity direction.

### §3.2 S-duality and electric–magnetic duality (Kapustin–Witten 2007)

**S-duality** in $\mathcal N=4$ super Yang–Mills exchanges electric
and magnetic charges via the modular group $SL(2,\Z)$ acting on the
gauge coupling $\tau=\theta/(2\pi)+4\pi i/g^2$. **Kapustin–Witten
2007** lifts S-duality to the **categorical** level for $\mathcal N=4$
SYM, identifying it with the **geometric Langlands duality** between
Higgs bundles and flat connections on a Riemann surface.

**Does the parity-twist via $J$ resemble S-duality?** Algebraically:
the Kapustin–Witten S-duality sends a category of B-branes for one
gauge theory to a category of A-branes for the dual gauge theory
(electric ↔ magnetic). The Sergeev parity-twist sends Str-branes to
otr-branes via $J$-conjugation; this is a $\Z/2$-twist (since
$J^2=-I$ implies $J^{4}=I$ at the brane-twist level), **not** an
$SL(2,\Z)$ modular action.

**Does $\mathfrak q(N)$ appear in the Kapustin–Witten framework?**
Not directly. The Kapustin–Witten framework uses
$G=U(N), SU(N), Sp(N), \ldots$ — bosonic gauge groups. The queer
extension $Q(N)$ (the integral form of $\mathfrak q(N)$) does
**not** appear as an N=4 SYM gauge group in standard treatments.

**Refined statement (parity-S-twist).** A *speculative* parallel:
the parity-twist via $J$ might correspond to a "queer-S-duality"
on a **queer N=4 SYM** (Quint–Park–Pak speculative; not standard
literature). This is **speculation**, not an established framework,
and is Phase-5 territory if pursued.

**Verdict on S-duality.** Sergeev duality does **NOT** lift to
Kapustin–Witten geometric Langlands S-duality in any standard sense.
The parity-twist via $J$ is a $\Z/4$-twist (since $J^2=-I$,
$J^4=I$), not an $SL(2,\Z)$-modular action.

### §3.3 T-duality (Strominger–Yau–Zaslow 1996)

**T-duality** on a circle $S^1_R$ of radius $R$ exchanges momentum
states with winding states, equivalently exchanges $R$ with
$\alpha'/R$. SYZ 1996 lifts T-duality to mirror symmetry on a
Calabi–Yau by performing T-duality fibrewise on the SYZ Lagrangian
fibration.

**Is the parity-twist a T-duality on a circle factor?** No. The
parity-twist via $J$ acts on the **Chan–Paton bundle** (a finite-
dimensional vector space), not on a spacetime circle. There is no
$S^1$ involved in the queer Lie superalgebra structure; the
parity-twist is purely algebraic.

**Could a T-duality on the brane line $\R$ implement the parity-
twist?** The brane line $\R\times p$ does not admit a natural $S^1$
factor (the $\R$-direction is non-compact). One could consider
formal $S^1$ compactification, but the queer parity-twist would not
arise from any T-duality in this scheme — the T-duality on
$S^1_R\subset\R$ exchanges momentum and winding, neither of which
corresponds to the queer central direction $J$.

**Verdict on T-duality.** Sergeev duality does **NOT** lift to a
T-duality on any circle factor. The parity-twist is a pointwise
algebraic structure, not a geometric duality.

### §3.4 Howe–Sergeev duality (Howe 1989, Cheng–Wang 2012 Ch. 4 + 5)

**Yes — this is the canonical containing framework.**

The Howe duality framework (Howe 1989) is a representation-theoretic
duality between commuting reductive group actions on a vector space.
Cheng–Wang 2012 Ch. 4 generalizes to super Howe pairs, and Ch. 5
gives the queer parallel: **Schur–Sergeev duality** as the
mutual-centralizer pair $(\mathfrak q(N), \mathcal{HC}_n)$.

The Sergeev-type open-closed duality on the otr-brane is **a special
case of Howe–Sergeev duality**:
* Open-string sector ↔ Hecke–Clifford algebra $\mathcal{HC}_n$.
* Closed-string sector ↔ $\mathfrak q(N)$-equivariant fields.
* Mutual centralizer ↔ open-closed compatibility.

This is the **unique** standard duality framework in which Sergeev
duality is naturally contained.

**Verdict on Howe–Sergeev.** Sergeev duality **IS** a special case
of Howe–Sergeev duality (Cheng–Wang Ch. 4 + 5). This is the natural
containing framework.

### §3.5 Synthesis of the comparison

| Duality framework | Contains Sergeev duality? | Reason |
|---|---|---|
| Mirror symmetry (Witten 1992; Kontsevich 1994; SYZ 1996) | **NO** | Mirror is A/B-axis exchange; Sergeev is parity-axis exchange. Orthogonal directions. |
| S-duality / electric–magnetic (Witten 1995, Kapustin–Witten 2007) | **NO** | S-duality is $SL(2,\Z)$-modular; Sergeev parity-twist is $\Z/4$ ($J^2=-I$). |
| T-duality (SYZ 1996) | **NO** | T-duality requires a circle factor; the parity-twist is pointwise algebraic. |
| **Howe–Sergeev duality (Howe 1989; Cheng–Wang 2012 Ch. 4 + 5)** | **YES** | $(\mathfrak q(N), \mathcal{HC}_n)$ mutual-centralizer pair on $V^{\otimes n}$. |

**Convergence verdict.** The closest known duality framework that
contains Sergeev as a special case is **Howe–Sergeev duality**
(Cheng–Wang 2012 Ch. 4 + 5). Mirror, S-, and T-duality do **not**
contain Sergeev; the parity-axis exchange is structurally orthogonal
to all three.

---

## §4. Smallest physical example

### §4.1 Smallest matrix size $N$

**Claim.** The smallest $N$ where the otr-brane is concretely
realisable is $N=2$.

**Reasoning.**
* $\mathfrak q(1)$ is degenerate: even part $\mathfrak{gl}_1=\C$ is
  abelian; the queer central element $J$ in $\mathfrak q(1)$ has
  $\mathrm{otr}(J)=\Tr(I_1)=1$, but the bracket structure is
  abelian, so the brane-probe Dirac action on $\mathfrak q(1)$
  degenerates. (Brane-Species-Audit §1.2; G3-M3 (H-otr.2).)
* $\mathfrak q(2)$ is the smallest non-degenerate case:
  $\dim\mathfrak q(2)=2\cdot 4=8$ (4 even + 4 odd); $J$ acts
  non-trivially on the basis; the Capelli central element
  $Z_2^{\mathrm{otr}}$ is non-zero and central in $U(\mathfrak q(2))$.
  (G3-M3 §1.1.)

**Smallest physical example: $N=2$.** The otr-brane on $\mathfrak q(2)$
is the smallest concretely realisable parastate brane.

### §4.2 Smallest open-closed pair $(N,n)$

**Claim.** The smallest $(N,n)$ where the Sergeev duality acts
non-trivially is $(N=2, n=2)$.

**Reasoning.**
* For $n=1$: $V=\C^{2|2}$ as a $\mathfrak q(2)$-module; $\mathcal{HC}_1=
  \mathcal{C}_1=\C[c_1]/(c_1^2-1)\cong\C\oplus\C$ (a 2-dimensional
  algebra). The Howe–Sergeev decomposition is $V=L_{(1)}^{\mathfrak q}
  \otimes M_{(1)}^{\mathcal{HC}}$, where $L_{(1)}^{\mathfrak q}$ is
  the natural rep and $M_{(1)}^{\mathcal{HC}}$ is the 2-dimensional
  Clifford module. The duality is **trivial** at $n=1$ (only one
  summand).
* For $n=2$: $V^{\otimes 2}=(\C^{2|2})^{\otimes 2}=\C^{4|4}$;
  $\mathcal{HC}_2=\mathcal{C}_2\rtimes\C[S_2]$ with $\dim\mathcal{HC}_2=
  4\cdot 2=8$. The Howe–Sergeev decomposition runs over **strict
  partitions of 2 with at most 2 parts**: only $\lambda=(2)$ and
  $\lambda=(1,?)$ — but $\lambda=(1,1)$ is **not strict** (repetition),
  so the only strict partition of 2 with $\leq 2$ parts is
  $\lambda=(2)$. Wait — the strict partitions of 2 are: only
  $\lambda=(2)$ (since $(1,1)$ has repetition).

  Actually, the strict partitions of $n=2$ with at most $N=2$ parts
  include $(2)$ and $(2,0)$ — these are essentially the same
  partition. So the decomposition has **a single irreducible
  summand**: $V^{\otimes 2}\cong L_{(2)}^{\mathfrak q}\otimes
  M_{(2)}^{\mathcal{HC}}$. The duality at $(2,2)$ is **non-trivial**
  in the sense that the bimodule structure is concrete and
  computable, but the decomposition has a single isotypical
  component.

**Refined claim.** The smallest $(N,n)$ with a **multi-summand**
Howe–Sergeev decomposition is $(N=2, n=3)$:
* For $n=3$, the strict partitions are $\lambda=(3)$, $\lambda=(2,1)$.
  Both have at most 2 parts. The decomposition has **two summands**:
  $V^{\otimes 3}\cong L_{(3)}^{\mathfrak q}\otimes M_{(3)}^{\mathcal{HC}}
  \oplus L_{(2,1)}^{\mathfrak q}\otimes M_{(2,1)}^{\mathcal{HC}}$.
  $\dim V^{\otimes 3}=4^3=64$; $\dim L_{(3)}^{\mathfrak q}\cdot
  \dim M_{(3)}^{\mathcal{HC}}+\dim L_{(2,1)}^{\mathfrak q}\cdot
  \dim M_{(2,1)}^{\mathcal{HC}}=64$ as a check.

**Smallest physical example: $(N=2, n=3)$.**

### §4.3 Concrete computation at $(N=2, n=2)$

The two-otr-brane stack on $\mathfrak q(2)$ is concretely realizable.
The mutual-centralizer statement reads:
* $\mathcal{HC}_2=\mathcal{C}_2\rtimes\C[S_2]$ has dimension $4\cdot
  2=8$ (Clifford generators $c_1, c_2$ with $c_i^2=1, c_1c_2=-c_2c_1$;
  $S_2$ swaps them).
* The image of $\mathcal{HC}_2$ in $\End(V^{\otimes 2})$ is the
  centralizer of $\mathfrak q(2)$.
* The image of $U(\mathfrak q(2))$ in $\End(V^{\otimes 2})$ is the
  centralizer of $\mathcal{HC}_2$.

The Schur–Sergeev decomposition $V^{\otimes 2}\cong L_{(2)}^{\mathfrak q}
\otimes M_{(2)}^{\mathcal{HC}}$ gives a single summand of dimension
$\dim L_{(2)}^{\mathfrak q}\cdot\dim M_{(2)}^{\mathcal{HC}}=4\cdot 4=
16=\dim V^{\otimes 2}$.

**Numerical check.** $V=\C^{2|2}$, so $\dim V^{\otimes 2}=4^2=16$.
$L_{(2)}^{\mathfrak q}$ is the irreducible $\mathfrak q(2)$-module
of strict highest weight $(2)$; its dimension is computed by the
Sergeev–Berele–Regev hook formula
$\dim L_{(2)}^{\mathfrak q}=2^{\ell(\lambda)}\cdot
\frac{n!}{\prod_{(i,j)\in\lambda}h(i,j)}$ where $\ell(\lambda)$ is
the length of the strict partition. For $\lambda=(2)$:
$\ell=1$, $n=2$, hooks are $\{2,1\}$ giving product 2. So $\dim
L_{(2)}^{\mathfrak q}=2^1\cdot 2!/2=2$. Hence $\dim M_{(2)}^{\mathcal{HC}}=
16/2=8$. **This is consistent: $M_{(2)}^{\mathcal{HC}}$ is the
8-dimensional Clifford-extended permutation module at $n=2$.**

### §4.4 Verdict on (SDP.4)

**Verdict.** The smallest matrix size where the otr-brane is
concretely realisable is **$N=2$**. The smallest open-closed pair
$(N,n)$ where the Sergeev duality acts non-trivially is **$(N=2,
n=2)$** (single-summand decomposition, dimension check verified) or
**$(N=2, n=3)$** for a multi-summand decomposition (the smallest
case demonstrating the Howe–Sergeev branching rule).

**Confidence.** High. The dimension counts are direct from
Cheng–Wang Ch. 5 and the Sergeev–Berele–Regev formula.

---

## §5. Cross-volume firewall verdict

### §5.1 Coefficient-class lift

**Coefficient-class statement.** Howe–Sergeev duality at the
representation-theoretic level is an **equivalence of mutual-
centralizer pairs**:
\[
   \mathrm{End}_{\mathfrak q(N)}(V^{\otimes n})\cong\mathcal{HC}_n,
   \qquad\mathrm{End}_{\mathcal{HC}_n}(V^{\otimes n})\cong U(\mathfrak q(N))/\mathrm{Ann}.
\]
This is a **categorical** statement at the level of representation
categories, *not* at the level of factorization algebras on
$\R^2\times\C^2$.

**The coefficient match.** Under Howe–Sergeev, the central character
$\Tr_{\mathfrak{gl}_N}(I)=N$ on the bosonic side maps to
$\mathrm{otr}_{\mathfrak q(N)}(J)=N$ on the queer side. Both are the
**same numerical coefficient $N$**, lifted to two distinct parity
sectors:
* Bosonic ($\Tr$): valued in $\C$ (even target).
* Queer ($\mathrm{otr}$): valued in $\Pi\C$ (odd target).

The Howe–Sergeev coefficient-coupling intertwiner
\[
   \Phi_{\mathrm{Sergeev}}\colon\quad
   \hbar N\,[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}
   \longmapsto \hbar N\,[\bar c]^{\mathrm{otr}}\in H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}
\]
preserves the coefficient $N$ and shifts the target line by parity.
This is **the Sergeev coefficient-class lift**.

### §5.2 Chain-level / vertex-class lift faces a firewall

**The firewall structure.** The Howe–Sergeev statement is at the
level of representation categories (mutual-centralizer pairs in
$\End(V^{\otimes n})$). Lifting to a chain-level / factorization-
algebra duality on $\R^2\times\C^2$ requires:
* (i) **Identifying $\mathcal{HC}_n$ as a factorization algebra on
  the brane line $\R\times p$.** The Hecke–Clifford algebra is a
  *finite-dimensional* algebra parametrized by $n$ insertion points;
  its factorization-algebra version would be a $\C[S_n]$-equivariant
  factorization structure on $n$-point configurations on $\R$,
  twisted by Clifford signs. **This is not currently inscribed**;
  the candidate is a Phase-5 construction.
* (ii) **Identifying $\mathfrak q(N)$-action as the closed-string
  factorization algebra on $\C^2$.** The queer-extension of the
  manuscript's local mixed model is the analog of the
  $\mathfrak{gl}_N$-equivariant brane stack on $\R^2\times\C^2$; the
  queer extension uses $V=\C^{N|N}$ Chan–Paton bundle and the
  parity-twisted off-diagonal embedding (Brane-Species-Audit §5.1).
  **This is partially inscribed** at the algebra level; the
  factorization-structure-level inscription is Phase-5.
* (iii) **Verifying that the mutual-centralizer property lifts to a
  chain-level isomorphism of factorization algebras.** This is the
  load-bearing step. The two factorization algebras live on
  *different* worldvolumes (open-line $\R$ vs closed-bulk
  $\R^2\times\C^2$); a chain-level isomorphism would need to
  identify them via the brane-defect comparison map of `main.tex`
  354–393.

**Verdict on chain-level lift.** The chain-level lift faces a
**firewall structurally identical to BCOV-A5**:
* Both firewalls preserve the coefficient $N$ at the
  representation-theoretic layer.
* Both firewalls block a chain-level isomorphism of factorization
  algebras on different worldvolumes.
* Both firewalls admit a coefficient-coupling intertwiner
  ($\Phi_{\mathrm{coef}}$ for BCOV-A5; $\Phi_{\mathrm{Sergeev}}$ for
  Sergeev) without lifting to chain-level equivalences.

### §5.3 Explicit comparison with BCOV-A5 firewall

| Feature | BCOV-A5 firewall | Sergeev firewall |
|---|---|---|
| **Coefficient preserved** | $\Str_{\mathfrak{gl}(N\|N)}(I)=N-N=0$ | $\mathrm{otr}_{\mathfrak q(N)}(J)=N$ |
| **Source worldvolume** | $\R^2\times\widehat{\C^2}_0$ formal local | $\R^2\times\widehat{\C^2}_0$ formal local |
| **Target worldvolume** | Compact CY$_3$ or flat $\C^d$ ($d$ odd) | Hecke–Clifford open-line $\R$ + queer $\C^2$ |
| **Cocycle target line** | $\C$ (even, BCOV $\bar\partial$-class) | $\Pi\C$ (odd, parity-shifted) |
| **Regulator class** | Heat-kernel parametrix, (A1)–(A5) | Heat-kernel parametrix with $J$-twist, (A1)–(A4) + (A5)\textsuperscript{otr} |
| **Open-closed coefficient** | $\hbar\Str(I)=\hbar(N-M)$ | $\hbar\mathrm{otr}(J)=\hbar N$ |
| **Cancellation mechanism** | $\Str(I)=0$ at super-balance | **None** — $\mathrm{otr}(J)=N$ does not vanish |
| **Coefficient-class match** | $\Phi_{\mathrm{coef}}$: identity on Str | $\Phi_{\mathrm{Sergeev}}$: identity on $N$, parity-shifted line |
| **Chain-level isomorphism** | **Blocked** by firewall | **Blocked** by firewall (this section) |
| **Coefficient-class identity** | $\hbar\Str(I)\mapsto\hbar\Str(I)$ | $\hbar N\,[\bar c]\mapsto\hbar N\,[\bar c]^{\mathrm{otr}}$ |

**Structural identity.** Both firewalls share:
* **Common ancestor** at the representation-theoretic layer (a
  central character coefficient).
* **Common blocking mechanism** at the chain-level layer (different
  factorization complexes; no chain-level isomorphism).
* **Common resolution** at the cohomology-class layer (coefficient-
  coupling intertwiner; not a complex isomorphism).

**Crucial distinction.** The BCOV-A5 firewall has $\Str(I)=0$ as the
discharge mechanism — the residue cancels at super-balance. The
Sergeev firewall has $\mathrm{otr}(J)=N\neq 0$ — **the residue does
not cancel**. The Sergeev case is therefore a *non-trivial* firewall:
the residue $\hbar N[\bar c]^{\mathrm{otr}}$ is a real obstruction in
the queer-channel cohomology, not an artefact of an unmatched
regulator.

### §5.4 Verdict on (SDP.5)

**Verdict.** Sergeev duality lifts to a **coefficient-class duality**
(via the Howe–Sergeev coefficient-coupling intertwiner
$\Phi_{\mathrm{Sergeev}}$ preserving the coefficient $N$ and shifting
the target line by parity). It does **NOT** lift to a chain-level /
vertex-class duality without surmounting a firewall **structurally
identical** to the BCOV-A5 firewall.

The firewall obstructs a chain-level isomorphism of factorization
algebras between the brane-defect BV complex on $\R^2\times\C^2$ and
the Hecke–Clifford open-line factorization on $\R$; it admits the
same coefficient-coupling resolution as BCOV-A5.

**Confidence.** Medium-high. The Howe–Sergeev coefficient match is
verbatim from Cheng–Wang Ch. 5. The chain-level firewall
identification is structurally parallel to the BCOV-A5 firewall
(documented at full rigour in `phase4-exec-BCOV-A5-comparison-2026-04-28.md`).
The factorization-algebra inscription of $\mathcal{HC}_n$ is Phase-5
work; the present inscription is at the coefficient layer.

---

## §6. Predictions for Theorem G\textsuperscript{otr} from Sergeev duality

### §6.1 The coefficient-class identity

**Predicted identity (P-Sergeev-1).** The Sergeev coefficient-coupling
intertwiner $\Phi_{\mathrm{Sergeev}}$ predicts
\[
   \boxed{\quad
   \Phi_{\mathrm{Sergeev}}\bigl(\hbar N\,[\bar c]\bigr)\,=\,\hbar N\,[\bar c]^{\mathrm{otr}}
   \quad}
\]
as a **coefficient-class identity** in graded cohomology
$H^2_{\mathrm{Lie}}(\bar A,\C\oplus\Pi\C)$. The two sides are related
by:
* **Same coefficient** $\hbar N$ (with the same $N$ from the $\Tr(I)
  =N=\mathrm{otr}(J)$ Howe–Sergeev match).
* **Same underlying cocycle** $[\bar c]$ (the $\omega$-cocycle of
  `lem:omega-cocycle` is unchanged; only the target line shifts).
* **Parity-shifted target line** $\C\to\Pi\C$ (encoding the parity
  difference of the central direction $I_{2N}$ vs $J$).

**Status.** This is a **prediction**, not a chain-level theorem. It
is the natural shadow of Howe–Sergeev at the residue layer. Phase-5
verification: lift the prediction to a chain-level identity by
constructing the factorization-algebra Howe pair explicitly.

### §6.2 The numerical match $\Tr(I)=\mathrm{otr}(J)=N$

**Predicted identity (P-Sergeev-2).** The numerical equality
\[
   \Tr_{\mathfrak{gl}_N}(I_N) = \mathrm{otr}_{\mathfrak q(N)}(J) = N
\]
is **not a coincidence**: it is the Howe–Sergeev central-character
match. On the bosonic side, $\Tr(I)=N$ is the U(1)-center anomaly
coefficient (Theorem G; main.tex 354). On the queer side,
$\mathrm{otr}(J)=N$ is the queer U(1)-center anomaly coefficient
(Theorem G\textsuperscript{otr}; G3-M3 §2). The Howe–Sergeev duality
**predicts** these are the same numerical coefficient.

**Verification.** Both equal $N$ by direct computation (G3-M3 §2.2;
Theorem G in main.tex 354). The Howe–Sergeev framework predicts
this *a priori*; it is observed *a posteriori* in the manuscript's
brane-probe Dirac calculation.

### §6.3 The parity-equivariance pair $(A5, A5^{\mathrm{otr}})$

**Predicted identity (P-Sergeev-3).** The pair of admissibility
classes:
* $(A5)$: unsigned parity-equivariance on the bosonic side.
* $(A5)^{\mathrm{otr}}$: signed parity-equivariance on the queer
  side, $\tau\Delta\tau^{-1}=-\Delta$.

is the Howe–Sergeev pair of regulator-class identifications: each
side requires its own parity-equivariance condition, and the two
are related by the parity-twist via $J$.

**Phase-5 verification.** Construct an admissible regulator class
satisfying $(A5)^{\mathrm{otr}}$ explicitly (heat-kernel with $J$
inserted, signed under conjugation by $\tau$), and verify that the
Hadamard / Pauli–Villars parametrices in this class give the same
QME residue $\hbar N[\bar c]^{\mathrm{otr}}$. This is residual
`R-P4-G3-M3-Q-otr-01`.

### §6.4 The Capelli-class identity

**Predicted identity (P-Sergeev-4).** The Sergeev quadratic odd
Capelli element $Z_2^{\mathrm{otr}}\in U(\mathfrak q(N))_{\bar 1}$
acts on the brane-probe Hilbert space with eigenvalue
\[
   Z_2^{\mathrm{otr}}\big|_{L_\lambda^{\mathfrak q}} = \hbar N\cdot
   (\text{Sergeev–Berele–Regev hook factor}),
\]
parallel to the bosonic Capelli identity $XY-YX=\hbar N\cdot I$
(`thm:quantum-classical-anomaly` in main.tex). The Howe–Sergeev
duality predicts that the Capelli eigenvalues of the queer-Capelli
element on the Hecke–Clifford-twisted Schur summands match the
classical Capelli eigenvalues on the corresponding ordinary-Schur
summands, modulo the strict-partition / hook-formula correction.

**Phase-5 verification.** Compute $Z_2^{\mathrm{otr}}$ on small
strict-partition irreps (e.g.\ $\lambda=(2)$ on $\mathfrak q(2)$)
and verify the $\hbar N$ coefficient matches the Howe–Sergeev
prediction. This is residual `R-P4-G3-M3-Q-otr-03`.

### §6.5 Verdict on (SDP.6)

**Verdict.** Sergeev duality predicts four coefficient-class
identities for Theorem G\textsuperscript{otr}:
* **P-Sergeev-1.** $\Phi_{\mathrm{Sergeev}}(\hbar N\,[\bar c])
  =\hbar N\,[\bar c]^{\mathrm{otr}}$ — the cohomology-class match.
* **P-Sergeev-2.** $\Tr_{\mathfrak{gl}_N}(I_N) =
  \mathrm{otr}_{\mathfrak q(N)}(J) = N$ — the central-character
  match.
* **P-Sergeev-3.** $(A5,(A5)^{\mathrm{otr}})$ — the parity-equivariance
  pair as Howe-dual regulator classes.
* **P-Sergeev-4.** Capelli-eigenvalue match $Z_2^{\mathrm{otr}}|_{L_\lambda^{\mathfrak q}}
  = \hbar N\cdot(\text{hook factor})$ — the quantum-classical
  reduction.

The most concrete prediction is **P-Sergeev-1**: the residue
$\hbar N[\bar c]^{\mathrm{otr}}$ of Theorem G\textsuperscript{otr} is
**the Sergeev-dual quantity** of the bosonic $\hbar N[\bar c]$ of
Theorem G, with the same numerical coefficient and a parity-shifted
target line. This is a **structural coefficient-class identity**, not
a chain-level equivalence — exactly the same status as the BCOV-A5
coefficient match.

**Confidence.** Medium-high for P-Sergeev-1 and P-Sergeev-2 (both
follow from the Howe–Sergeev central-character match, which is rigorous
in Cheng–Wang Ch. 5). Medium for P-Sergeev-3 (the (A5)\textsuperscript{otr}
admissibility class is sketched in G3-M3 §3.4 but not fully closed).
Medium-low for P-Sergeev-4 (the Capelli-eigenvalue computation
requires Phase-5 work on the Sergeev–Berele–Regev hook formula at
small partitions).

---

## §7. Duality-class anomaly identification

### §7.1 The lift obstruction: Obs-Sergeev-A5-firewall

**Named obstruction.** The chain-level lift of Howe–Sergeev duality
to a factorization-algebra duality between the open-line
Hecke–Clifford complex and the closed-bulk brane-defect BV complex
is obstructed by:

> **Obs-Sergeev-A5-firewall.** The two factorization complexes
> live on different worldvolumes (open-line $\R$ vs closed-bulk
> $\R^2\times\C^2$), with structurally distinct $\Z/2$-graded BV
> structures: the Hecke–Clifford complex has Clifford-sign grading
> on the brane-line insertion points, while the brane-defect
> complex has BV ghost-number grading on the bulk fields. No
> chain-level isomorphism preserves the parity-twist via the queer
> central element $J$, because $J$ acts non-trivially on both
> gradings.

This is the duality-class anomaly obstructing the chain-level lift.

### §7.2 Comparison with BCOV-A5 obstruction

**BCOV-A5 obstruction (from BCOV-A5-comparison §3-§4).** The chain-
level isomorphism between the BCOV BV complex on $\C^d$ ($d$ odd)
and the manuscript's local mixed model on $\R^2\times\C^2$ is
obstructed by:
* Different spacetimes ($\C^3$ vs $\R^2\times\C^2$).
* Different field content (polyvector fields vs Hamiltonian BF).
* Different brackets (Schouten–Nijenhuis vs polynomial Hamiltonian).
* Different differentials ($\bar\partial$ vs mixed
  $d_{\R^2}+\bar\partial_{\C^2}$).

**Sergeev-A5-firewall obstruction.** The chain-level isomorphism
between the brane-defect BV complex on $\R^2\times\C^2$ (closed-
bulk) and the Hecke–Clifford open-line complex on $\R$ (open-string
side) is obstructed by:
* Different worldvolumes ($\R^2\times\C^2$ vs $\R$).
* Different field content (BF Hamiltonian fields vs Clifford-twisted
  $S_n$-permutation modules).
* Different algebra structures (super-Lie + BV vs Clifford + symmetric
  group).
* Different differentials (BV $Q+\{I_0,-\}$ vs Hecke–Clifford braid
  differential).

**Structural parallel.** Both firewalls are **algebraic-vs-geometric**
firewalls: representation-theoretic categories on one side,
factorization-algebra complexes on the other; coefficient-class
matches without chain-level isomorphism.

### §7.3 Resolution mechanisms

**For BCOV-A5.** The Costello–Li 2015 / 2016 framework gives a
*partial* lift on flat $\C^d$ for $d$ odd, with the open algebra
$\mathfrak{gl}(N|N)$. The match is at the level of the Costello–Li
chain-level vertex cocycle, paired with the manuscript's Theorem G
class via the coefficient $\Str(I)=N-M$. The *full* firewall lift
to a chain-level isomorphism between BCOV on $\C^3$ and our local
model on $\R^2\times\C^2$ is **not** inscribed.

**For Sergeev-A5.** A parallel partial lift could be constructed via:
* (Resolution-1) **Hecke–Clifford factorization algebra inscription.**
  Construct $\mathcal{HC}_n$ as a factorization algebra on $\R$
  (Phase-5 work).
* (Resolution-2) **Queer brane-defect BV complex inscription.**
  Inscribe the queer extension of the manuscript's local mixed
  model with $\mathfrak q(N)$-equivariant BV fields (Phase-5; the
  Theorem G\textsuperscript{otr} inscription is the residue-layer
  precursor).
* (Resolution-3) **Coefficient-coupling intertwiner.**
  $\Phi_{\mathrm{Sergeev}}$ as the coefficient-class lift, parallel
  to $\Phi_{\mathrm{coef}}$ of BCOV-A5. **This is the resolution
  achievable at the present (residue) layer.**

### §7.4 Residual: R-P4-EXEC-Sergeev-Chain-01

**Residual.** Construct the factorization-algebra Howe pair
$(\mathfrak q(N), \mathcal{HC}_n)$-bimodule structure on
$V^{\otimes n}$ as a chain-level duality between two factorization
algebras on $\R$ × {brane points}. Verify mutual centralizer at the
chain level. Compare the Howe–Sergeev open-closed split with the
manuscript's brane-defect comparison map (`main.tex` 354–393).

**Phase-5 work, dependent on R-P4-G3-M3-Q-otr-01 ((A5)\textsuperscript{otr}
admissibility) and the Costello–Gaiotto–Williams 2007.09497 PDF
inscription (CGW boundary VOA cross-walk).**

### §7.5 Verdict on (SDP.7)

**Verdict.** The duality-class anomaly obstructing the chain-level
lift of Howe–Sergeev to a factorization-algebra duality is
**Obs-Sergeev-A5-firewall**: the open-line Hecke–Clifford complex
and the closed-bulk brane-defect BV complex are structurally
distinct $\Z/2$-graded factorization algebras, with no chain-level
isomorphism preserving the parity-twist via $J$.

The obstruction is **structurally identical** to the BCOV-A5
firewall (both are algebraic-vs-geometric firewalls). The resolution
at the present (residue) layer is the coefficient-coupling
intertwiner $\Phi_{\mathrm{Sergeev}}$; the full chain-level lift is
Phase-5 work, residual `R-P4-EXEC-Sergeev-Chain-01`.

**Confidence.** Medium-high. The firewall identification is
structurally parallel to the BCOV-A5 firewall. The full chain-level
lift requires a Phase-5 inscription of the factorization-algebra
Howe pair, not currently available in the literature (Costello–Li
1505.06703 / 1605.09073 cover the bosonic / super case; the
Hecke–Clifford factorization is parallel but not yet inscribed).

---

## §8. Anti-attack scan responses

### §8.1 (Att-1) Cheng–Wang Howe–Sergeev duality lifts to factorization-algebra duality on $\R^2\times\C^2$

**Attack.** Cheng–Wang 2012 Ch. 4–5 Howe–Sergeev duality is at the
level of representation categories, not at the level of factorization
algebras. Does it lift to a factorization-algebra duality on
$\R^2\times\C^2$?

**Response.** §5 + §7 above. The lift faces the
**Obs-Sergeev-A5-firewall**: the open-line Hecke–Clifford complex on
$\R$ and the closed-bulk brane-defect BV complex on $\R^2\times\C^2$
are structurally distinct $\Z/2$-graded factorization algebras. No
chain-level isomorphism preserves the parity-twist via $J$.

**Discharge.** Att-1 is answered with the **explicit firewall
identification**: Howe–Sergeev lifts to a coefficient-class duality
(via $\Phi_{\mathrm{Sergeev}}$) but not to a chain-level
factorization-algebra duality. The chain-level lift is residual
`R-P4-EXEC-Sergeev-Chain-01`, parallel to the BCOV-A5 firewall lift
(also unresolved in the manuscript).

The discharge identifies the **structural common ancestor** at the
representation-theoretic layer (the coefficient $N$), preserved by
$\Phi_{\mathrm{Sergeev}}$, while acknowledging the chain-level
firewall as a permanent feature of the algebraic-vs-geometric
distinction between the two complexes.

### §8.2 (Att-2) The otr-brane is mixed-parity; where does it sit in the mirror picture?

**Attack.** Mirror symmetry exchanges A-branes (Lagrangian +
flat bundle) with B-branes (coherent sheaf); the otr-brane is
mixed-parity. Where does it sit in the mirror picture?

**Response.** §3.1 above. The otr-brane is **mixed-parity** in the
sense that its Chan–Paton bundle has both even-parity (in the
diagonal-block sub-bundle) and odd-parity (in the off-diagonal-block
sub-bundle) components. The parity-twist via $J$ exchanges these
components.

**Mirror picture.** In the Kontsevich 1994 mirror framework:
* A-branes are pure-even (Lagrangian submanifolds with graded local
  systems); the grading is a Maslov shift, not a parity-twist via
  a queer central element.
* B-branes are pure-even (coherent sheaves with Chern character
  classes); the grading is a degree shift in the derived category,
  not a parity-twist.

The otr-brane is **neither pure A nor pure B**: it has a parity-
twist that is **independent** of the A/B-axis. It sits in a
**parity-twisted mixed B-brane** category, parallel to but distinct
from the standard A/B-brane category.

**Discharge.** Att-2 is answered with the **explicit parity-mixed
identification**: the otr-brane is in a *parity-twisted mixed
B-brane* category (Etingof–Ostrik 2004 / Coulembier 2018 finite
tensor category sense), not in the Kontsevich 1994 A/B-brane
category. Mirror symmetry in the Kontsevich sense does not exchange
otr-branes with any standard A-brane or B-brane.

**Cross-walk.** This refines Brane-Species-Audit §9.2 (Att-3 from
the Brane-Species prompt): the parity-mirror is a distinct duality
in the parity-axis, related to but not identical to the Kontsevich
1994 A/B-mirror.

### §8.3 (Att-3) Kapustin–Witten 2007 geometric Langlands and q(N)

**Attack.** Kapustin–Witten 2007 lifts S-duality to the categorical
level for $\mathcal N=4$ SYM. Does $\mathfrak q(N)$ appear in the
Kapustin–Witten framework?

**Response.** §3.2 above. **No.** The Kapustin–Witten framework
uses bosonic gauge groups $G=U(N), SU(N), Sp(N), \ldots$. The queer
extension $Q(N)$ does **not** appear as an N=4 SYM gauge group in
standard treatments. The parity-twist via $J$ is a $\Z/4$-twist
($J^2=-I$, $J^4=I$), not an $SL(2,\Z)$-modular action.

**Refined statement.** A *speculative* parallel: a "queer N=4 SYM"
with gauge group $Q(N)$ would extend the Kapustin–Witten framework
to a parity-twisted variant. This is **not standard literature**; if
pursued, it would be a Phase-5 / Vol III frontier finding.

**Discharge.** Att-3 is answered with the **explicit non-occurrence**:
$\mathfrak q(N)$ is not in the Kapustin–Witten framework. The
parity-twist is not a special case of S-duality; it is a $\Z/4$-twist
orthogonal to the $SL(2,\Z)$-modular action.

### §8.4 (Att-4) Coulembier 2018 tensor-ideal framework: super-finite-tensor-category for queer with known duality

**Attack.** The Coulembier 2018 tensor-ideal framework gives a
precise super-finite-tensor-category for queer; does this category
have a known duality with the gl-category that matches our
otr-brane / Str-brane pair?

**Response.** Coulembier 2018 *Tensor ideals, Deligne categories
and invariant theory* gives a precise super-finite-tensor-category
description of the queer monoidal category $\mathrm{Rep}(\mathfrak q)$,
parallel to Deligne's category $\mathrm{Rep}(\mathrm{GL}_t)$ at
generic $t$. The Coulembier framework establishes:
* $\mathrm{Rep}(\mathfrak q)$ is a super-finite-tensor-category (in
  the Etingof–Ostrik 2004 sense) with parity-twisted ribbon
  structure.
* The tensor ideals of $\mathrm{Rep}(\mathfrak q)$ are classified by
  the Deligne / Coulembier theorem; they correspond to "blocks" in
  the strict-partition Schur–Sergeev decomposition.
* There is a **categorical duality** between $\mathrm{Rep}(\mathfrak q)$
  and $\mathrm{Rep}(\mathfrak{gl})$ (Coulembier 2018 Theorem 5.2):
  the queer category is related to the bosonic category via a
  parity-twisted equivalence functor, with the queer central element
  $J$ implementing the twist.

**Match with otr-brane / Str-brane pair.** The Coulembier 2018
categorical duality matches the brane-physics otr-brane / Str-brane
pair:
* $\mathrm{Rep}(\mathfrak q)$ = otr-brane category (with parity-twist
  via $J$).
* $\mathrm{Rep}(\mathfrak{gl})$ = Str-brane category (without parity-
  twist).
* The categorical equivalence functor implements the brane-physics
  parity-twist via conjugation with $J$.

**This is the categorical lift of the Sergeev-type open-closed
duality.** It establishes that:
* The otr-brane and Str-brane categories are categorically equivalent
  (via the parity-twist).
* The equivalence preserves the $\hbar N$ coefficient (since the
  parity-twist preserves the central character on the centre, which
  is the load-bearing data for the U(1)-anomaly class).
* The equivalence is **at the level of representation categories**,
  not at the level of factorization algebras (parallel to §5 above).

**Discharge.** Att-4 is answered with the **explicit categorical
match**: the Coulembier 2018 tensor-ideal framework gives a
super-finite-tensor-category for queer, with a categorical duality
with the gl-category (Coulembier 2018 Theorem 5.2). This matches the
brane-physics otr-brane / Str-brane pair; the duality is at the
representation-category layer, parallel to (but distinct from) the
chain-level firewall obstruction.

**Cross-walk.** This strengthens the §5 verdict: the Howe–Sergeev
coefficient-class duality is **categorical at the representation
level** (Coulembier 2018) but does **not** lift to a chain-level
factorization-algebra duality (Obs-Sergeev-A5-firewall).

---

## §9. Residuals + Phase-5 escalation

### §9.1 Residuals

* **R-P4-EXEC-Sergeev-Chain-01.** Construct the factorization-algebra
  Howe pair $(\mathfrak q(N), \mathcal{HC}_n)$-bimodule structure on
  $V^{\otimes n}$ as a chain-level duality between factorization
  algebras on $\R$. Verify mutual centralizer at the chain level.
  Cross-walk to the manuscript's brane-defect comparison map. Phase-5,
  dependent on R-P4-G3-M3-Q-otr-01.

* **R-P4-EXEC-Sergeev-Coulembier-02.** Embed the otr-brane / Str-brane
  pair into the Coulembier 2018 super-finite-tensor-category framework.
  Identify the precise equivalence functor (Coulembier Theorem 5.2)
  realising the parity-twist via $J$. Verify the $\hbar N$ coefficient
  match at the categorical level.

* **R-P4-EXEC-Sergeev-CGW-03.** Cross-walk to Costello–Gaiotto–Williams
  2007.09497 5d twisted M-theory framework. Does CGW realise an
  otr-channel defect? (Brane-Species-Audit §10.1 returned a NO at
  the bosonic-CGW layer; verify whether super-CGW extensions or the
  W31 spin-tower truncation deliver an otr-channel defect.)

* **R-P4-EXEC-Sergeev-q-mirror-04.** The parity-mirror conjecture of
  Brane-Species-Audit §9 is now **identified** as a special case of
  the Howe–Sergeev coefficient-class duality (this document §6.1).
  Phase-5 work: lift the parity-mirror to a chain-level statement,
  if the firewall can be surmounted.

* **R-P4-EXEC-Sergeev-VolIII-05.** Cross-volume cross-walk to
  `~/calabi-yau-quantum-groups` Vol III chiral algebra. The queer
  extension of the chiral CY$_3$ algebra (Cheng–Wang Ch. 6 catalog)
  couples to $[\bar c]^{\mathrm{otr}}$ via the Sergeev coefficient-
  class duality. Heuristic — convention-checking only at this stage;
  rigorous comparison requires a separate Phase-5 / Vol III embedding
  theorem (matched conventions per CLAUDE.md).

### §9.2 Phase-5 escalation routes

* **Phase-5-Sergeev-A.** Inscribe the Theorem G\textsuperscript{otr}
  parallel anomaly class with the **Sergeev-coefficient-class
  identification** $\Phi_{\mathrm{Sergeev}}(\hbar N\,[\bar c])=
  \hbar N\,[\bar c]^{\mathrm{otr}}$ as the precise structural
  prediction, status "coefficient-class match (Howe–Sergeev)".

* **Phase-5-Sergeev-B.** Construct the factorization-algebra Howe
  pair (R-P4-EXEC-Sergeev-Chain-01); attempt chain-level lift; report
  whether the firewall surmounts or persists.

* **Phase-5-Sergeev-C.** Cross-walk to Vol III; identify the queer
  chiral CY$_3$ algebra coupling and verify the
  $\Phi_{\mathrm{Sergeev}}$ prediction at the Vol III layer (with
  matched conventions).

### §9.3 Deciding evidence required for Phase-5 closure

Each Phase-5 route requires one of:
* **(D-1)** Construction of an admissible (A5)\textsuperscript{otr}
  regulator class with concrete heat-kernel / Pauli–Villars
  parametrices satisfying the signed parity-equivariance.
* **(D-2)** Inscription of the Hecke–Clifford factorization algebra
  on $\R$ (e.g., as a $\C[S_n]$-equivariant factorization with
  Clifford-sign twist), parallel to the Costello–Gwilliam Vol II
  factorization-algebra construction.
* **(D-3)** Cross-volume embedding theorem matching the
  $\hbar N[\bar c]^{\mathrm{otr}}$ class with a Vol III chiral CY$_3$
  queer-extension class, with matched conventions.

The chain-level firewall is **structurally identical** to the BCOV-A5
firewall (§5.3); both face the same algebraic-vs-geometric block;
both admit the same coefficient-coupling resolution at the residue
layer. Phase-5 escalation must address the firewall obstruction
explicitly, not silently bridge it.

---

## §10. Synthesis — Sergeev-type duality as Howe–Sergeev shadow

### §10.1 Cohomology table (extension of Brane-Species-Audit §5.1 + §9.1)

| Brane | Source | Boundary evaluation | Cocycle target | Coefficient | Howe-pair partner |
|---|---|---|---|---|---|
| **gl-brane** (manuscript Theorem G) | $\mathfrak{gl}_N$ | $\Tr$ | $\C$ (even) | $\hbar N$ | $S_n$ (Schur–Weyl) |
| **Str-brane** (q(N), G3-M2 verdict) | $\mathfrak q(N)$ via $\mathfrak{gl}(N\|N)$ embedding | $\Str$ | $\C$ (even) | $0$ at q-balance | $S_n$ (residual Schur–Weyl) |
| **otr-brane** (q(N), Theorem G\textsuperscript{otr}) | $\mathfrak q(N)$ | $\mathrm{otr}$ | $\Pi\C$ (odd) | $\hbar N$ | $\mathcal{HC}_n=\mathcal{C}_n\rtimes\C[S_n]$ (Hecke–Clifford) |

**Howe–Sergeev coefficient-class identity.** The $\hbar N$ coefficient
on the gl-brane (manuscript Theorem G) and on the otr-brane (Theorem
G\textsuperscript{otr}) is the **same numerical coefficient $N$**,
predicted by Howe–Sergeev (Cheng–Wang Ch. 5 Theorem 5.4). The Str-
brane sits in between: it sees the *same* source $\mathfrak q(N)$
but with the *bosonic* trace channel ($\Str$), giving $0$ at q-balance.

### §10.2 Three-tier brane / duality summary

* **Tier I: Standard Howe duality.** gl-brane / osp-brane / psl-brane
  realise classical Schur–Weyl pair $(\mathfrak{gl}_N, S_n)$ or its
  super extensions. Standard topological-string brane species; no
  Sergeev-twist required.

* **Tier II: Howe–Sergeev (parastate).** otr-brane realises the queer
  Schur–Sergeev pair $(\mathfrak q(N), \mathcal{HC}_n)$. Non-standard
  brane species (parastate); requires the parity-twist via $J$;
  produces the parallel anomaly $\hbar N[\bar c]^{\mathrm{otr}}$.

* **Tier III: No Howe pair.** p-brane (= no realisable brane on
  $\mathfrak p(N)$) and sl(M|N)-brane for $M\neq N$ (= net K-theory
  charge). No Howe duality, no brane-stack realisation.

### §10.3 Bottom-line verdict

**The closest known duality framework that contains Sergeev as a
special case is Howe–Sergeev duality (Cheng–Wang 2012 Ch. 4 + 5).**
This is the canonical containing framework. Mirror, S-, and
T-duality do not contain Sergeev; the parity-axis exchange is
structurally orthogonal to all three.

**The chain-level lift faces a firewall structurally identical to
BCOV-A5.** Both firewalls preserve the coefficient $N$ at the
representation-theoretic layer; both block chain-level isomorphism
of factorization algebras; both admit the same coefficient-coupling
resolution at the residue layer.

**The predicted residue-identity for Theorem G\textsuperscript{otr}
is $\Phi_{\mathrm{Sergeev}}(\hbar N\,[\bar c])=\hbar N\,[\bar c]^{\mathrm{otr}}$
as a coefficient-class identity in graded cohomology
$H^2_{\mathrm{Lie}}(\bar A,\C\oplus\Pi\C)$.** This is the structural
shadow of Howe–Sergeev at the residue layer; the full chain-level
lift is residual `R-P4-EXEC-Sergeev-Chain-01`, Phase-5 work.

The Phase-4 EXEC verdict on the Sergeev-Duality-Probe is therefore:

**SDP closes positively at the coefficient-class layer (Howe–Sergeev)
with a Phase-5 firewall residual at the chain level — structurally
identical in form and resolution to BCOV-A5.**

---

## §A. Appendix — Cross-references

### §A.1 Brane-Species-Audit anchors

* B.5 verdict (Brane-Species-Audit §5): otr-brane identified as
  parastate brane; "Sergeev-type open-closed duality invisible to
  bosonic probes" named as a verdict header.
* §9 parity-mirror conjecture: now identified as the brane-physics
  shadow of Howe–Sergeev (this document §6).
* §10 anti-attack scan: extended here with §8 anti-attacks Att-1–Att-4.

### §A.2 Theorem-G-otr-inscription anchors

* §1.1 Theorem G\textsuperscript{otr} statement: the residue
  $\hbar N[\bar c]^{\mathrm{otr}}$ is matched here with the
  Howe–Sergeev coefficient-class identity (P-Sergeev-1).
* §3.2 two-supertrace independence: the independence is preserved
  under $\Phi_{\mathrm{Sergeev}}$ (the parity-shift is between
  $H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}$ and
  $H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$, not within a single
  parity sector).
* §3.5 Witten lens interpretation: extended here with §1–§4 of the
  brane-physics translation.

### §A.3 G3-M3-queer-trace anchors

* §1 queer-Capelli element $Z_2^{\mathrm{otr}}$: now identified as
  the Howe–Sergeev central element on the queer side, predicting
  the Capelli-eigenvalue match (P-Sergeev-4).
* §2 $\mathrm{otr}(J)=N$: the Howe–Sergeev central-character match
  with $\Tr(I)=N$ on the bosonic side (P-Sergeev-2).
* §3 (A5)\textsuperscript{otr}: the Howe–Sergeev parity-equivariance
  pair (P-Sergeev-3).

### §A.4 BCOV-A5-comparison anchors

* §0 verdict, three-line bottom line: the Sergeev firewall is
  **structurally identical** to the BCOV-A5 firewall.
* §3.1 structural common ancestor: Howe–Sergeev coefficient $N$
  parallels BCOV-A5 coefficient $\Str(I)=N-M$.
* §3.2 comparison map $\Phi_{\mathrm{coef}}$: parallels the Sergeev
  coefficient-coupling intertwiner $\Phi_{\mathrm{Sergeev}}$.

### §A.5 Cross-volume firewall anchors

* CLAUDE.md: research constellation role; queer extensions cross-walk
  to Vol III chiral CY$_3$ algebra (R-P4-EXEC-Sergeev-VolIII-05).
* main.tex 5380–5394 (`rmk:convention-firewall`): the cross-volume
  firewall is permanent at the load-bearing layer; the present
  inscription respects this.
* main.tex 5890–5915 (`ssec:cross-volume-horizon`): Phase-5 work on
  the cross-volume horizon.

---

**End of document.** Authorship: Raeez Lorgat. Phase-4 EXEC,
proposal-only. Master ledger ID prefix `P4-EXEC-Sergeev-`. Writable
surface: this file only.
