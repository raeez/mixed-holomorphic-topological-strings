# Phase-4 / G3 — Supertrace / QME beyond gl(N|N): research outline

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Witten primary (physical consistency, brane configurations,
anomaly cancellation); Costello secondary (factorization, BV/QME,
regulator class); Composition tertiary (admissibility audit, M-31 deformation).
**Mode.** Proposal-only. Master ledger schema; IDs prefix `P4-G3-`.
**Posture.** Wave 3 has CERTIFIED CONVERGED. W22-T1 closes
chain-level QME on $\mathfrak{gl}(N|N)$ at $N=M$ at one loop;
W22-T2 with W30's (A5) heal closes all-loop. The route is rigorous
on $\mathfrak{gl}(N|N)$. Phase-4 question: **beyond gl(N|N) — what
other supersymmetric Lie superalgebras supply zero supertrace
sources, what physical brane configurations realize them, what
escape routes remain open in the unreduced primitive (W18-C3) and
character (W18-CT2) directions, and how do these interact with
G2 (column-Verma / Symp-equivariance) and G4 (5d M-theory CGW
boundary VOA)?**

This is **a research outline, not a theorem ledger**. Each task
identifies the precise question, names the candidate constructions,
flags the load-bearing obstructions, and proposes 3 mo / 6 mo / 12
mo milestones for the three-pronged Phase-4 program.

**Inputs (light reads).** `CLAUDE.md`;
`reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md` (full,
W22-T1, W22-T2);
`reconstitution/wave3-W30-A5-heal-2026-04-28.md` (full, (A5) heal);
`reconstitution/wave3-W25-supertrace-verification-2026-04-28.md`
(full, independent verification + W25 counterexamples);
`reconstitution/wave3-W18-thmB-escape-routes-2026-04-28.md`
(W18-CT1 verbatim, W18-CT2 character resolution, W18-C3 unreduced
primitive conjecture); cross-walk to
`reconstitution/wave3-W26-column-verma-2026-04-28.md` (G2 column-Verma);
`reconstitution/wave3-W31-5dM-obstructions-2026-04-28.md` (G4 CGW
boundary VOA obstruction audit). Standard references:
Kac 1977 *Lie superalgebras* (classical / exceptional);
Cheng–Wang 2012 *Dualities and representations of Lie superalgebras*;
Sergeev–Veselov 2011 *Generalised discriminants*; Faddeev 1980
*Methods of path integration*; Costello *Renormalization* §5.2;
Costello–Gwilliam Vol II §11.

---

## §0. Executive verdict (precedes the ledger)

**Three-line summary.** The super-balanced gl(N|N) closure of
W22-T1+T2 is the *first* example, not the *only* example. (A) Other
classical Lie superalgebras (osp(2N|2N), p(N), q(N)) supply
zero-supertrace sources under their own balancing conditions; the
exceptional D(2,1;α) does not (it has non-degenerate Killing form).
(B) The unreduced primitive (W18-C3) requires constructing a parallel
factorization theory on $\mathfrak{h}_{\mathrm{poly}}$ where the
constant line is retained — Costello-Gwilliam Vol II prefactorization
machinery covers the *target* but not the *construction* of such
theories from scratch; Lurie HA gives the homotopy-coherent skeleton
but neither package supplies the explicit Hamiltonian primitive.
(C) The central-character escape (W18-CT2) was declared resolved into
Capelli; there *is* a non-trivial extension to higher Capelli /
Sergeev-Veselov characters worth recording, but it is informationally
parallel to Capelli at the QME-class layer.

**Three-pronged Phase-4 program.** (A) extend W22-T1/T2 to other
classical superalgebras; (B) construct unreduced primitive in
parallel factorization theory; (C) survey character extensions.
Each prong gets 3 / 6 / 12 mo milestones in §6.

**Cross-group coupling.** G2 column-Verma extends to gl(N|N) with
graded-Borel and the four-cone Čech-SES super-extension is a natural
candidate. G4 CGW boundary VOA admits a super-VOA refinement; if
yes, Symp-form-equivariance on super-balanced is free.

---

## §1. Ledger entries

### P4-G3-01 — T1: Super-balancing beyond gl(N|N)

**Severity 4 (research outline; load-bearing for the (A) prong).
Status: outline. Confidence high on classical, medium on exceptional.**
**Lens.** Witten primary; Costello secondary.
**Provenance.** Mandate T1 of the Phase-4 G3 prompt.

The supertrace identity on a basic classical Lie superalgebra is
governed by the *super-Killing form* and its degeneracies. The
question is: for which classical (and exceptional) Lie superalgebras
is there a natural identity-like element $I$ with $\mathrm{Str}_g(I)=0$
under a balancing condition?

**Catalog.**

**(a) gl(N|N) — covered.** Even part $\mathfrak{gl}_N\oplus
\mathfrak{gl}_N$, identity $I=\mathbf 1_N\oplus\mathbf 1_N$, supertrace
$\mathrm{Str}(I)=N-N=0$. Balancing condition: $N=M$ on $\mathfrak{gl}(N|M)$.
Closed by W22-T1+T2 + W30 (A5). The Killing form $B(X,Y)=
\mathrm{Str}(\mathrm{ad}_X\mathrm{ad}_Y)$ is degenerate on the
center (trace direction) and the orthogonal $\mathfrak{sl}(N|N)$ has
*non-trivial radical* — this is the source of the projective
embedding subtlety, but does **not** affect the W22-T1+T2 obstruction
class which is sensitive only to $\mathrm{Str}(I)$, not the radical.

**(b) sl(N|N).** The simple supertrace-zero subalgebra is
$\mathfrak{sl}(N|N)=\{X\in\mathfrak{gl}(N|N)\,:\,\mathrm{Str}(X)=0\}$,
which **automatically** has $\mathrm{Str}(I)=0$ (the identity is *not*
in $\mathfrak{sl}(N|N)$ by construction). Subtle: the natural
matrix-source role for the BCOV / topological B-model open string
sector is gauge group $U(N|M)$ (with $\mathfrak{u}(N|N)$ unitary
form), where $\mathfrak{su}(N|N)$ is the supertrace-zero piece
*plus* a one-dimensional center coming from $\mathfrak{psl}(N|N)=
\mathfrak{sl}(N|N)/\C\cdot I$. The center is *not* the identity (it is
the matrix $\mathrm{diag}(\mathbf 1_N,-\mathbf 1_N)$, the parity
matrix $P$). **Verdict: $\mathfrak{sl}(N|N)$ is a sub-source of
$\mathfrak{gl}(N|N)$ on which W22-T1+T2 holds vacuously
($\mathrm{Str}(I)=0$ tautologically); no new content beyond gl(N|N).**

**(c) psl(N|N) and the exceptional center.** $\mathfrak{psl}(N|N)=
\mathfrak{sl}(N|N)/\C\cdot P$ is the projective simple super-Lie
algebra, with $P$ the parity matrix. $\mathfrak{psl}(N|N)$ has
*degenerate* super-Killing form — a load-bearing pathology. **Open
question P4-G3-01-Q1**: does the W22-T2 chain-level argument
$\mathrm{Ob}_{\mathrm{sc}}^{\mathrm{super}}=\hbar\mathrm{Str}(I)
\Lambda^{\mathrm{Str}}(\omega)$ remain meaningful when the Killing
form is degenerate? The W30 (A5) construction of the heat kernel
$\Delta_{\mathrm{sK}}=\sum_a(-1)^{|a|}T^aT_a$ requires a
*non-degenerate* super-Killing form. On psl(N|N) the form is
degenerate; one would need to use a non-Killing parity-equivariant
bilinear form (e.g.\ a partial trace) or replace the heat-kernel
construction by Pauli–Villars. **Status: research outline;
W30-style verification on psl(N|N) is non-trivial.**

**(d) osp(2M|2N).** Orthosymplectic. Even part $\mathfrak{so}_{2M}
\oplus\mathfrak{sp}_{2N}$. Identity $I=\mathbf 1_{2M}\oplus\mathbf 1_{2N}$,
supertrace $\mathrm{Str}(I)=2M-2N$. **Balancing condition: $M=N$,
giving $\mathrm{Str}(I)=0$.** This is the "orthosymplectic balanced"
configuration. The Killing form on osp(2N|2N) is non-degenerate (it
is a basic classical Lie superalgebra in Kac's list), so the W30
(A5) heat-kernel construction goes through verbatim:
$\Delta_{\mathrm{sK}}^{\mathrm{osp}}=\sum_a(-1)^{|a|}T^aT_a$ commutes
with the parity operator $P$ on osp(2N|2N), and the propagator-loop
contraction yields $\mathrm{Str}(I)=2N-2N=0$. **Verdict: a genuine
new candidate theorem on the osp-balanced source.** Phase-4 P4-G3-T-A1.

**Physical interpretation (Witten lens).** osp(2N|2N) is the natural
gauge superalgebra for the *type-IIB* topological string on a
Calabi–Yau threefold with O-plane / orientifold projection. The
balanced configuration $\mathrm{Str}(I)=0$ corresponds to *brane–anti-brane
+ orientifold* charge cancellation. References: Sen 1999 *Tachyon
condensation on the brane antibrane system* (general framework);
Witten 1998 *D-branes and K-theory* for K-theory underpinning;
Bergman–Gimon–Sugimoto 2001 *Orientifolds, RR fluxes, and K-theory*
for the osp specifically.

**(e) p(N).** Periplectic $\mathfrak{p}(N)\subset\mathfrak{gl}(N|N)$
preserves an *odd* symplectic form on $\mathbf C^{N|N}$. Even part
$\mathfrak{gl}_N$, odd part fits in $\mathrm{Sym}^2\C^N\oplus
\Lambda^2\C^N$. Supertrace properties: the $\mathfrak{p}(N)$
super-Killing form is **identically zero** (it is the prototypical
*non-classical* basic Lie superalgebra). **Open question
P4-G3-01-Q2**: with vanishing Killing form, is there a meaningful
heat-kernel construction at all? Likely no in the W30 sense; one
would need to take the quadratic Casimir from a *higher-order*
invariant or use a $\Z/2$-graded analogue. **Status: probably outside
W22-T2 reach; alternative regulator constructions needed.**

**(f) q(N).** Queer Lie superalgebra. Even part $\mathfrak{gl}_N$;
odd part $\mathfrak{gl}_N$ (anti-diagonal copy). The "queer trace"
$\mathrm{otr}$ replaces the supertrace. **Critical feature:** q(N)
has *two* trace-like invariants — the ordinary trace
$\mathrm{Str}=\mathrm{Tr}_+-\mathrm{Tr}_-$ on the even sector, and
the "odd trace" $\mathrm{otr}$ on the odd sector. The standard
identity $I_{q(N)}\in q(N)$ has $\mathrm{Str}(I)=N$ (non-zero!),
since the odd part of q(N) does not contribute a $\mathrm{Tr}_-$
piece in the Berezin sum. **Verdict: q(N) does not give zero
supertrace under the W22 mechanism; a different cancellation pattern
is needed.** However, *Sergeev's super-Capelli identity* (Sergeev 1984;
Cheng–Wang 2012 §5) on q(N) gives a non-trivial central element
$C^q$ that could replace the Capelli central element in the Theorem
G coefficient computation. **Status: research outline P4-G3-Q3 —
investigate q(N) via Sergeev central element.**

**(g) D(2,1;α).** Exceptional, dim 17, depending on a continuous
parameter $\alpha\in\C\setminus\{0,-1\}$. Even part $\mathfrak{sl}_2
\oplus\mathfrak{sl}_2\oplus\mathfrak{sl}_2$, odd part is a tensor
product of three two-dim representations. Killing form is
non-degenerate (it is basic classical). The "identity" is the
Cartan-element direction; supertrace of identity is **non-zero
generically**. **No natural balancing condition** giving zero
supertrace for D(2,1;α). **Verdict: exceptional D(2,1;α) does not
admit a W22-T2 super-balanced theorem.**

**(h) F(4) and G(3) exceptional.** Same verdict as D(2,1;α): basic
classical Lie superalgebras with non-degenerate Killing form and no
natural balancing condition giving $\mathrm{Str}(I)=0$. **No candidate.**

**Summary table.**

| Lie superalgebra | Even part | $\mathrm{Str}(I)$ | Balancing condition | W22-T2 reach | Status |
|------------------|-----------|------------------|--------------------|--------------| -------|
| gl(N\|M) | $\mathfrak{gl}_N\oplus\mathfrak{gl}_M$ | $N-M$ | $N=M$ | YES | covered (W22-T1+T2) |
| sl(N\|N) | $\mathfrak{s}\subset\mathfrak{gl}_N\oplus\mathfrak{gl}_N$ | $0$ tautologically | trivial | YES (vacuous) | sub-source |
| psl(N\|N) | $\mathfrak{psl}/\C\cdot P$ | $0$ tautologically | trivial | OPEN (degenerate Killing) | research |
| osp(2M\|2N) | $\mathfrak{so}_{2M}\oplus\mathfrak{sp}_{2N}$ | $2(M-N)$ | $M=N$ | YES | **NEW CANDIDATE** P4-G3-T-A1 |
| p(N) | $\mathfrak{gl}_N$ | $0$ tautologically | trivial | UNCLEAR (zero Killing) | outside W22 |
| q(N) | $\mathfrak{gl}_N$ | $N$ | none | NO | Sergeev mechanism |
| D(2,1;α) | $\mathfrak{sl}_2^{\oplus 3}$ | $\neq 0$ | none | NO | no candidate |
| F(4), G(3) | classical | $\neq 0$ | none | NO | no candidate |

**Files read.** `wave3-W22-supertrace-rigorous-2026-04-28.md` (full);
`wave3-W30-A5-heal-2026-04-28.md` (full); Kac 1977 *Lie superalgebras*
(catalog of basic classical and exceptional); Cheng-Wang 2012
*Dualities and representations of Lie superalgebras* (the q(N) and
osp story).
**Confidence.** High on classical (gl, osp); medium on psl, p, q
(degenerate / non-classical Killing form is a real obstruction);
high on D(2,1;α), F(4), G(3) (non-zero Str(I) is direct).
**Blast radius.** **One new candidate theorem P4-G3-T-A1 on osp(2N|2N)**
fully parallel to W22-T1+T2, with W30-style (A5) parity-equivariance
verification straightforward. Two open research questions on
psl(N|N) and p(N) where Killing-form degeneracy needs alternative
regulator. q(N) requires the Sergeev mechanism, distinct from
super-balancing.
**Adjudication.** Valid outline. The (A) prong of the Phase-4 program
has a clear first target: osp(2N|2N).
**Residual.** P4-G3-R-01: psl(N|N), p(N) regulator construction;
P4-G3-R-02: Sergeev central element on q(N); P4-G3-R-03: physical
brane configurations realizing each (see T2).

---

### P4-G3-02 — T2: Physical brane configurations realizing super-balanced sources

**Severity 4 (physics motivation, Witten primary). Status: outline.
Confidence high.**
**Lens.** Witten primary; Costello secondary.
**Provenance.** Mandate T2 of the Phase-4 G3 prompt.

The W22-T1+T2 closure on gl(N|N) is mathematically rigorous; the
*physical interpretation* is a Phase-4 question. Three brane
configurations naturally produce super-balanced sources.

**(a) D-brane / anti-brane pairs.** $N$ D-branes + $M$ anti-branes
on a Calabi–Yau threefold give gauge group $U(N)\times U(M)$ in the
bosonic limit and gauge supergroup $U(N|M)$ when the brane–anti-brane
tachyon condensation is included (Sen 1998, *SO(32) spinors of type
I and other solitons*, JHEP 9809:023; Witten 1998, *D-branes and
K-theory*, JHEP 9812:019). The boundary topological B-model on a
brane–anti-brane stack realizes the gauge superalgebra
$\mathfrak{gl}(N|M)$ as the open-string vertex operator algebra at
ghost number 0. **At $N=M$**: the brane–anti-brane charge cancels
(K-theory triviality), tachyon condensation drives the system to the
closed-string vacuum, and the QME anomaly vanishes consistent with
W22-T1+T2.

**Reference.** Bergman–Gaberdiel 1999, *A non-supersymmetric open
string theory and S-duality*, JHEP 9907:022; Polchinski 1996
*Notes on D-branes*, hep-th/9602052 (D-brane review).

**(b) N=4 SYM with R-symmetry breaking partial twist.** N=4 super
Yang–Mills theory with gauge group $U(N|M)$ has been studied as a
mathematical object even outside its standard supersymmetric content
(Costello 2017, *Holography and Koszul duality*; Costello–Gaiotto 2018,
*Twisted holography*). The R-symmetry $SU(4)$ acts on the four
fermions; a *holomorphic-topological* partial twist (selecting a
$\mathfrak{u}(1)\subset\mathfrak{su}(4)$ subgroup) leaves the super
gauge group $U(N|M)$ as the residual symmetry. **At $N=M$**: the
holomorphic-topological N=4 theory on $\R\times\C^2$ becomes the
W22 brane probe of $\widehat\C^2_0$ with super-balanced source.

**Reference.** Costello 2017, *Holography and Koszul duality*,
arXiv:1610.04144 (the holomorphic-topological twist and its W22
relevance); Costello–Gaiotto 2018, *Twisted holography*,
arXiv:1812.09257.

**(c) Topologically twisted theories (Vafa–Witten / Kapustin–Witten).**
The Vafa–Witten theory and Kapustin–Witten gauge theory on a
Calabi-Yau threefold accommodate super-gauge groups under specific
topological twists. The twist of N=4 SYM gauge group $U(N|N)$ (with
the standard A-twist) gives a topological theory whose partition
function counts BPS states with super-balanced configurations
(Donaldson-Witten / Kapustin-Witten reduction). **The W22-T1+T2
QME vanishing is then the topological-twist statement that the
super-balanced configuration is anomaly-free at every loop.**

**Reference.** Vafa-Witten 1994, *A strong coupling test of S-duality*,
hep-th/9408074; Kapustin-Witten 2007, *Electric-magnetic duality and
the geometric Langlands program*, hep-th/0604151.

**(d) Orientifold + brane systems for osp(2N|2N).** Type IIB string
theory with O-plane projection produces gauge groups $SO(2N)$,
$Sp(2N)$, and on brane–anti-brane stacks with O-plane, the gauge
supergroup $\mathfrak{osp}(2N|2N)$. **At $M=N$**: orientifold + brane
+ anti-brane charge cancellation, $\mathrm{Str}(I)=2N-2N=0$.
**Phase-4 P4-G3-T-A1's physical origin.**

**Reference.** Bergman–Gimon–Sugimoto 2001, *Orientifolds, RR fluxes,
and K-theory*, JHEP 0105:023.

**Files read.** Sen 1998, Witten 1998, Costello 2017, Bergman–Gimon–Sugimoto 2001 (cited from memory).
**Confidence.** High on the physical lineage (D-brane / anti-brane,
N=4 holomorphic-topological twist, orientifold). Medium on the rigorous
BCOV / topological B-model embedding of the super-balanced
source — this is R-W3-W22-05 (Phase-4).
**Blast radius.** Each physical configuration supplies a load-bearing
*motivation* for the corresponding (A)-prong theorem. The brane–anti-brane
realization is the first and tightest link to the manuscript's BCOV
posture.
**Adjudication.** Valid physical-origin outline.
**Residual.** P4-G3-R-04: rigorous BCOV / topological B-model embedding
of the super-balanced sources (cross-walk to R-W3-W22-05; this is
the Phase-3/4 deferred question).

---

### P4-G3-03 — T3: Unreduced primitive (W18-C3) — parallel factorization theory required

**Severity 4 (research outline; load-bearing for the (B) prong).
Status: outline.**
**Lens.** Costello primary; Composition secondary.
**Provenance.** Mandate T3 of the Phase-4 G3 prompt.

**Recap of W18-C3.** W18 conjectured that the unreduced primitive
$\eta(f)=-[f]_0$ on $\mathfrak{h}_{\mathrm{poly}}=\C[z_1,z_2]$
(retaining the constant line) might descend to $\bar A=
\mathfrak{h}_{\mathrm{poly}}/\C\cdot 1$ if a *parallel* factorization
theory exists on $\mathfrak{h}_{\mathrm{poly}}$. The descent through
the canonical projection $\mathfrak{h}_{\mathrm{poly}}\to\bar A$
*destroys* the primitive: $\eta(1)=-1\neq 0$ in
$\mathfrak{h}_{\mathrm{poly}}$ but the constant-Hamiltonian acts
trivially on $\bar A$. **The conjecture asks: is there a
parallel theory whose objects retain the constant line?**

**The required structure.** The parallel factorization theory must:

- *(R1)* Live on the unreduced source $\mathfrak{h}_{\mathrm{poly}}$,
  not on $\bar A$ (the constant line is preserved).
- *(R2)* Define a Costello-RG factorization product on
  $\mathfrak{h}_{\mathrm{poly}}$-Hamiltonian observables, with
  associated graded compatible with the polynomial-degree filtration
  (admissibility (A1)–(A5)).
- *(R3)* Realize $\eta(f)=-[f]_0$ as a chain-level cocycle in the
  unreduced BV complex $\Omega^*(\mathcal E_w^{\mathrm{unreduced}})$
  with $\delta\eta=\omega$ exactly (no homotopies, no degenerations).
- *(R4)* On this parallel theory, the mixed brane-defect QME
  obstruction class is **exact** (chain-level boundary), and
  `prob:weighted-rg-locality` is true.
- *(R5)* The descent $\mathfrak{h}_{\mathrm{poly}}\to\bar A$ is *not*
  required to preserve the primitive (so the parallel theory is not
  obtained by lifting from the manuscript's reduced theory).

**Does Lurie HA (Higher Algebra) supply this?**

**No, not directly.** Lurie HA Chapter 5 develops $E_n$-algebras,
factorization homology, $\infty$-operads, and topological-chiral
homology. The Lurie machinery covers:
- The *target* of factorization homology (a presentable
  $\infty$-category) — abstractly present.
- The *operad* governing factorization (the disk operad, $E_n$ in
  Lurie HA §5.4, factorization $\infty$-operads in HA §3 / Higher
  Topos Theory §3.3) — abstractly present.
- The *coloring* of objects (Hamiltonian-algebra valued) —
  *not* directly provided by Lurie; one must build the specific
  factorization $\infty$-operad encoding $\mathfrak{h}_{\mathrm{poly}}$
  with the constant line retained.
- The *primitive* $\eta$ on the unreduced source — *not* in Lurie
  machinery; this requires a manual chain-level construction.

**Lurie HA gives the homotopy-coherent skeleton (the formal $\infty$-
operad and its colorings) but does not supply the explicit
Hamiltonian primitive or its RG flow.** The construction is
Hamiltonian-algebra-specific and is *not* of the standard form
covered in HA Chapter 5.

**Does Costello–Gwilliam Vol II supply this?**

**Partially.** Costello-Gwilliam *Factorization Algebras Vol II*
(*Quantum Field Theory*, AMS 2021) develops:
- Chapter 8: *Quantum Master Equation* — full BV/QME machinery;
  the *target* of unreduced QME is in scope but the *unreduced
  source* is not specifically discussed.
- Chapter 11: *Local Lie Algebras and the BV Bracket* — covers the
  Lie-algebra-valued case but assumes the algebra is *reduced*
  (i.e.\ centerless or with the central line projected out).
- Appendix: *Renormalization* — the regulator class machinery in
  the (A1)-(A4) sense; (A5) is W30 / W22 contribution.

**The Vol II machinery supports unreduced theories *abstractly* but
does not include a specific construction of the parallel
factorization theory on $\mathfrak{h}_{\mathrm{poly}}$.** Vol II's
local-Lie-algebra setup assumes the algebra is reduced. The
unreduced extension would require:
- a *new* chapter on unreduced local Lie algebras;
- a *new* result on chain-level primitive existence on the unreduced
  source;
- a *new* descent obstruction analysis for the constant-line projection.

These are not in Vol II.

**Is there *any* existing machinery for unreduced factorization theories?**

**No standard package.** The closest analogue:
- **Reduced vs unreduced factorization.** In CFT (Beilinson–Drinfeld
  *Chiral Algebras*), there is a distinction between *unital* (with
  unit / vacuum) and *reduced* chiral algebras. The unital chiral
  algebra retains the constant line; the reduced is obtained by
  projecting out. This is **structurally analogous** to our
  $\mathfrak{h}_{\mathrm{poly}}$ vs $\bar A$ distinction. **However**,
  the BD chiral-algebra setup is for the *closed* sector (vertex
  operator algebras and their factorization) and does not directly
  cover the BV/QME open-string setup of W22.
- **Costello–Lazarev–Yoo on unital factorization?** Not a standard
  reference. There is no published construction of unreduced BV
  factorization theory on the Hamiltonian Lie algebra
  $\mathfrak{h}_{\mathrm{poly}}$ that I am aware of.

**Verdict: P4-G3-C1 (unreduced primitive escape, W18-C3 cousin) is
genuinely Phase-4. No standard machinery exists; a new chapter of
Costello-Gwilliam-style work or a Beilinson–Drinfeld-style unital
chiral algebra adaptation is required.**

**Three sub-questions for the (B) prong.**

- *(B1)* Does the *unital* Beilinson–Drinfeld chiral algebra setup
  on $\mathfrak{h}_{\mathrm{poly}}$ (with constant line retained as
  the unit) admit a BV/QME refinement? Cross-walk to BD §3.4 unital
  chiral algebras + Costello-Gwilliam Vol II §11 BV pairing.
- *(B2)* Is the chain-level primitive $\eta(f)=-[f]_0$ an
  *unreduced* coboundary in the BD-style unital chiral algebra
  cohomology? Answer probably yes by direct computation; the
  obstruction is whether this lifts to a Costello-RG renormalized
  factorization on the unreduced source.
- *(B3)* Does the unreduced obstruction class for `prob:weighted-rg-locality`
  vanish on the unreduced parallel theory? This is the load-bearing
  question — the descent obstruction blocking W18-C3.

**Files read.** `appendix-unreduced-bv-qme.tex` 33–179 (centrality
no-go on bosonic source); `attack-heal-platonic-2026-04-28.md` M-29
closure (Obligation II, four named extensions); Costello-Gwilliam
Vol II §11 (cited from memory); Lurie HA §5.4 and Chapter 5 (cited
from memory); Beilinson-Drinfeld *Chiral Algebras* §3.4 (cited from
memory).
**Confidence.** High on Lurie HA scope (it does not supply the
specific construction); high on Costello-Gwilliam Vol II scope (it
covers reduced not unreduced); medium on BD unital chiral algebra
adaptation potential (it is structurally analogous but BV/QME
refinement is non-trivial).
**Blast radius.** **The (B) prong is the *hardest* of the three
Phase-4 prongs.** No standard machinery exists; the work is fresh
chapter-of-Vol-III scale. 12 mo milestone realistic.
**Adjudication.** Valid research outline. The question is not a
technical extension but a foundational extension of factorization
theory.
**Residual.** P4-G3-R-05: BD unital chiral algebra adaptation;
P4-G3-R-06: Costello-Gwilliam Vol III chapter on unreduced local
Lie algebras (proposal-only, not in scope for the present
manuscript).

---

### P4-G3-04 — T4: Central-character escape route status

**Severity 3 (status check; W18-CT2 declared resolved). Status:
resolution holds; non-trivial extensions exist but are
informationally parallel.**
**Lens.** Composition primary; Costello secondary.
**Provenance.** Mandate T4 of the Phase-4 G3 prompt.

**Recap of W18-CT2.** W18 declared the central-character escape
route (route (ii) of `rmk:app-scalar-contact-escape-routes`)
*resolved into the existing Capelli normalization*
(`lem:capelli-renormalized-stable-trace`). The character $\chi_\hbar$
absorbing $\hbar N$ coincides with the Capelli counterterm; the
route is informationally redundant.

**Does the resolution actually close the route?**

**Yes, at the QME-class level for the *bosonic* source.** The
Capelli normalization on $\mathfrak{gl}_N$ is a specific
$\hbar$-deformation of the trace that absorbs the $\hbar N$ anomaly.
Equivalently, the $\hbar$-deformed center $Z_\hbar(\mathfrak{gl}_N)$
admits a character $\chi_\hbar$ with $\chi_\hbar(C_1)=0$ on the
linear Casimir; this gives the same QME-class trivialization at
one loop.

**However**, three non-trivial extensions are worth recording.

**(a) Higher Capelli central elements (Sergeev 1984, Olshanski 1995).**
The center of $\widehat U(\mathfrak{gl}_N)$ has Capelli central
elements $C_1, C_2, \ldots, C_N$ (the higher Capelli elements
generate the center). The W18-CT2 resolution covers $C_1$
(linear Capelli, $\hbar N$ anomaly). **For higher-loop / higher-order
anomalies, higher Capelli characters $\chi_\hbar^{(k)}$ may be
relevant.** Specifically, the $\ell$-loop QME anomaly on
$\mathfrak{gl}_N$ has potential contributions from products of
Capelli elements; a complete character normalization would require
a character on the *full* $Z_\hbar(\mathfrak{gl}_N)$, not just on
$C_1$.

**Is this a non-trivial extension?** Yes, *if* higher-loop QME
anomalies on the bosonic source produce non-zero higher Capelli
contributions. In W22-T2 (after (A5) heal) the *super-balanced*
source has all higher loops killed by the supertrace, so this is not
relevant on the super-balanced side. On the *bosonic* source, the
higher-loop anomalies are obstructed (W3-W10 + W3-W6 closure of
`prob:weighted-rg-locality` *in the negative*); the $\ell$-loop
anomaly is $\hbar^\ell N^\ell[\bar c]^\ell$, with simple coupling
$\hbar N$ at each loop. **The higher Capelli characters do not
discharge the bosonic obstruction**; they only re-normalize the
linear Capelli coefficient at each loop. Verdict: **non-trivial in
formulation, equivalent in QME-class effect.**

**(b) Sergeev central element on q(N).** On the queer Lie superalgebra
q(N), the center of $\widehat U(q(N))$ is generated by the *Sergeev
central element* $C^q$ (Sergeev 1984, *The center of enveloping
algebra for Lie superalgebra Q(n)*; Cheng-Wang 2012 §5). $C^q$ is
analogous to the Capelli element but takes values in the *odd*
central direction (q(N) has both even and odd central elements).
**Central-character escape on q(N): does $\chi_\hbar^q(C^q)=0$
discharge the anomaly?** Open question P4-G3-04-Q1.

**Status:** This is genuinely a non-trivial extension of the W18-CT2
resolution to a *different superalgebra* (q(N) vs $\mathfrak{gl}_N$).
The Sergeev central element gives a new character-class candidate
for the QME normalization on q(N) — independent of the (A) prong's
super-balancing route (since q(N) doesn't admit super-balancing).

**(c) Olshanski's stable Capelli for large $N$.** Olshanski 1995
*Olshanski's twisted Yangian*; the *stable* Capelli element
$C_1^\infty$ on the inverse limit $\widehat U(\mathfrak{gl}_\infty)$
has a well-defined character $\chi^\infty$ that is the natural large-$N$
limit of $\chi_\hbar^{(N)}$. The manuscript's stable-large-$N$
posture (M-13: bosonic Dirac probe at large $N$) corresponds to the
stable Capelli; the W18-CT2 resolution is *automatic* in this large-$N$
limit. **No new content beyond the manuscript's existing stable-trace
machinery.**

**Verdict on T4.** The W18-CT2 resolution closes the route at the
*QME-class level for $\mathfrak{gl}_N$ at one loop*. Two non-trivial
extensions are worth recording:
- *Higher Capelli characters at higher loops*: parallel to the
  $\hbar^\ell N^\ell[\bar c]^\ell$ obstruction layer; informationally
  equivalent to the linear Capelli at each loop.
- *Sergeev central character on q(N)*: a genuinely new candidate
  *on a different superalgebra*; this is the "(C) prong" of the
  Phase-4 program.

**Files read.** `appendix-unreduced-bv-qme.tex` 33–179;
`attack-heal-platonic-2026-04-28.md` (M-31, M-45 region cited from
W18); Sergeev 1984 *Center of enveloping algebra for Lie superalgebra
Q(n)*; Cheng-Wang 2012 *Dualities and representations of Lie superalgebras*
§5; Olshanski 1995 (cited from memory).
**Confidence.** High on the resolution status; medium on the
non-trivial extensions (the higher Capelli higher-loop investigation
needs explicit higher-loop QME computation).
**Blast radius.** W18-CT2 resolution holds. The non-trivial extensions
are research-outline content for the (C) prong, not corrections to
the Wave 3 closure.
**Adjudication.** Valid status check.
**Residual.** P4-G3-R-07: higher-Capelli higher-loop computation;
P4-G3-R-08: Sergeev central element on q(N) and its character class.

---

### P4-G3-05 — T5: Three-pronged Phase-4 program with milestones

**Severity 4 (program; integrates T1–T4). Status: outline.**
**Lens.** Witten primary; Costello + Composition secondary.
**Provenance.** Mandate T5 of the Phase-4 G3 prompt.

**(A) prong — Extend W22-T1+T2 to other classical superalgebras.**

Target: New candidate theorems P4-G3-T-A1 (on osp(2N|2N)) and
research questions on psl(N|N), p(N), q(N).

**3 mo milestone.** P4-G3-T-A1: rigorous proof of W22-T2 analogue on
osp(2N|2N). Steps:
- Verify W30 (A5) parity-equivariance for osp(2N|2N) heat-kernel
  from super-Killing form (the form is non-degenerate; standard
  argument applies).
- Compute one-loop propagator-loop contraction on osp(2N|2N) using
  super-Berezin / Berezin-Pfaffian (the orthosymplectic measure).
- Confirm $\mathrm{Str}(I)=2N-2N=0$ at the balanced configuration.
- Run hand-computation at $(M,N)=(1,1)$ for sanity check.

**6 mo milestone.** Resolve psl(N|N) via Pauli-Villars: identify a
parity-equivariant non-Killing bilinear form and verify (A5);
extend W22-T2 if possible, else flag as residual.

**12 mo milestone.** Complete catalog: q(N) via Sergeev central
element (depends on (C) prong); p(N) via alternative regulator
(Phase-4); D(2,1;α), F(4), G(3) confirmed as no-candidate.

**Deliverables.** Two new candidate theorems (P4-G3-T-A1 on osp,
and a variant on psl if it goes through); a clean catalog of
super-balanced sources for BCOV / topological-string applications.

**(B) prong — Construct unreduced primitive in parallel factorization theory.**

Target: Resolve W18-C3 by constructing a parallel Costello-RG
factorization theory on $\mathfrak{h}_{\mathrm{poly}}$.

**3 mo milestone.** Adapt Beilinson–Drinfeld unital chiral algebra
machinery to the BV/QME setting on $\mathfrak{h}_{\mathrm{poly}}$.
Construct the unital factorization product at the chain level.

**6 mo milestone.** Verify chain-level $\eta(f)=-[f]_0$ as a coboundary
in the unital BD/BV cohomology. Identify the unreduced QME obstruction
class and check its vanishing condition.

**12 mo milestone.** Either: (i) resolve W18-C3 affirmatively by
constructing the parallel theory and proving QME-vanishing on the
unreduced source; or (ii) name the precise structural obstruction
that blocks the construction and reformulate W18-C3 as a *no-go*
theorem.

**Deliverables.** Either a new "Volume III" chapter of factorization
theory (unreduced local Lie algebras + unreduced BV/QME) or a
precise no-go theorem with ledger entry. **This is the hardest
prong; 12 mo is realistic.**

**(C) prong — Survey character extensions beyond Capelli.**

Target: Characterize the central-character escape route on
non-Capelli central elements (Sergeev on q(N), higher Capelli at
higher loops, and the manuscript's stable-trace large-$N$ analogue).

**3 mo milestone.** Sergeev central element survey on q(N): explicit
form of $C^q$, its eigenvalues on the basic q(N)-modules, the
character $\chi^q_\hbar$ and its compatibility with the brane-defect
twist on the q(N) source.

**6 mo milestone.** Higher Capelli computation: at $\ell$-loops, what
combinations of $C_1, \ldots, C_N$ enter the QME anomaly on
$\mathfrak{gl}_N$, and what character normalization is required?
This is a manuscript-internal sharpening of W3-W10's $\ell$-loop
anomaly catalog.

**12 mo milestone.** Full survey: all non-trivial central-character
escape routes catalogued, with formal status (informationally
equivalent to existing / genuinely new). Cross-link to T1 catalog
(superalgebra side) and T3 unreduced primitive (factorization side).

**Deliverables.** A catalog of central-character normalizations for
the QME, with each row indexed by (superalgebra, central element,
character, status). The (C) prong is the *informational* prong;
its output is mostly knowledge consolidation rather than new
theorems.

**Cross-prong dependencies.**
- (A) prong and (C) prong share the q(N) target: (A) tests super-balancing
  on q(N) (no), (C) tests Sergeev central character on q(N) (open).
- (A) prong and (B) prong share the unreduced osp(2N|2N) question:
  does the parallel factorization on $\mathfrak{h}_{\mathrm{poly}}$
  generalize from gl to osp? This is a 12 mo follow-up.
- (B) prong is *most independent* of (A), (C): the unreduced
  primitive question is fundamentally about factorization theory
  on the unreduced source, not about the source-Lie-algebra choice.

**Resource estimate.** (A) prong: 2 senior researchers, 3-12 mo.
(B) prong: 3 senior researchers + Costello-Gwilliam consult, 12 mo.
(C) prong: 1 researcher + Etingof / Olshanski consult, 6 mo.

**Files read.** All Phase-4 G3 mandate inputs.
**Confidence.** High on the milestone structure; medium on the
12-month feasibility of (B) prong.
**Blast radius.** Three-pronged research program with clear
deliverables. Phase-4 work, not in scope for present manuscript.
**Adjudication.** Valid program proposal.
**Residual.** P4-G3-R-09: cross-prong integration after 12 mo.

---

### P4-G3-06 — T6: Interaction with G2 — column-Verma extension to gl(N|N)

**Severity 3 (cross-group interaction). Status: outline.**
**Lens.** Etingof primary; Functoriality + Witten secondary.
**Provenance.** Mandate T6 of the Phase-4 G3 prompt.

**Recap of G2 column-Verma.** W26 verified W21's identification of
$M_a\subset\mathcal P$ as a column-Verma module of the 3-dim solvable
Borel $\mathfrak{b}=\langle z_1, z_2, z_1z_2\rangle\subset\bar A$,
with hand-computation on 168 basis vectors. The identification is
GL$_2\times T^2$-natural but breaks at quadratic symplectomorphisms.

**Does the column-Verma identification extend to gl(N|N)?**

**Yes — under the natural graded-Borel construction.** Let
$\mathfrak{gl}(N|N)$-equivariant Hamiltonian observables on the
super-stack form a $\Z^2$-graded super-$\bar A$-module
$\mathcal P^{\mathrm{super}}$. The graded Borel is
$\mathfrak{b}^{\mathrm{super}}=\langle z_1, z_2, z_1z_2\rangle$
*acting on the super-stack via the super-Berezin extension*.

**Key new feature.** The super-stack module $\mathcal P^{\mathrm{super}}$
has an *additional* $\Z/2$-grading from the parity of the
$\mathfrak{gl}(N|N)$-equivariance label. The column-Verma module
$M_a^{\mathrm{super}}$ on the super-stack splits as:
\[
   M_a^{\mathrm{super}}=M_a^{\mathrm{ev}}\oplus M_a^{\mathrm{odd}}
\]
along the parity grading. Each parity-pure piece is itself a
column-Verma of the (graded) Borel $\mathfrak{b}^{\mathrm{super}}$.
**At super-balance ($N=M$), the relative-difference cycle
$M_a^{\mathrm{ev}}\ominus M_a^{\mathrm{odd}}$ is the *parity-graded*
column-Verma**, and this cycle is precisely the LHS of the W22-Obs
relative-difference Tor class identification (M-31 deformation,
W3-W22-08).

**Cross-link to four-cone Čech-SES.** The four-cone Čech-SES (W14
mixed-cones; cross-walk to W3-W14) on the bosonic
$\widehat\C^2_0$-module category extends naturally to the super-stack
via the super-extension of the Čech presheaf. The four cones become
*eight cones* (four bosonic + four parity-flipped fermionic), and
the column-Verma fits into the parity-graded Čech SES:
\[
   0\to M_a^{\mathrm{ev}}\to\mathcal P^{\mathrm{super}}\to
   M_a^{\mathrm{odd}}\to 0
\]
(super-balanced at $N=M$). **This is a natural new structure on
the super-stack, not a downgrade of the bosonic four-cone SES.**

**Functoriality.** The graded-Borel column-Verma identification on
gl(N|N) is GL$_2\times T^2$-natural in the same sense as the bosonic
case (W26 W3-W26-T1). The super-stacking adds the parity-grading
naturality but does not break the GL$_2\times T^2$ structure.
**Symp$_\mathrm{form}$-equivariance** still breaks at quadratic
symplectomorphisms in the same way as the bosonic case (W26 W3-W26-08:
explicit quadratic-symplectomorphism column-mixing demonstrated).

**Verdict T6.** **The column-Verma extends naturally to gl(N|N) with
parity-graded refinement. The four-cone Čech-SES super-extension is
a load-bearing object for the (A) prong.** P4-G3-T-A1 (on osp(2N|2N))
should also receive a parallel column-Verma analysis, but the
orthosymplectic Borel structure is non-trivial (mixed parity-orthogonal
generators); 6 mo milestone for the explicit construction.

**Files read.** `wave3-W26-column-verma-2026-04-28.md` 1–80,
mandate-region; `wave3-W14-mixed-cones-2026-04-28.md` (cited from
ledger structure); `wave3-W21-wakimoto-2026-04-28.md` (cited from
W26 mandate).
**Confidence.** High on the parity-graded extension; medium on
osp(2N|2N) Borel structure (technical but standard).
**Blast radius.** Cross-group interaction with G2 unlocks new
structural objects on the super-stack: parity-graded column-Verma,
super-Čech-SES, parity-graded relative-difference cycle = M-31
deformed LHS.
**Adjudication.** Valid cross-group outline.
**Residual.** P4-G3-R-10: explicit column-Verma on osp(2N|2N).

---

### P4-G3-07 — T7: Interaction with G4 — super-VOA boundary and free Symp$_{\mathrm{form}}$-equivariance

**Severity 3 (cross-group interaction). Status: outline.**
**Lens.** Witten primary; Drinfeld secondary.
**Provenance.** Mandate T7 of the Phase-4 G3 prompt.

**Recap of G4 CGW boundary VOA.** W31 audited the W23 conjecture
that the 5d twisted M-theory boundary admits a CGW (Costello-Gaiotto-Witten)
boundary VOA realization. The audit produced five precise
obstructions; the central-charge mismatch is load-bearing. W3-W31-T2
gave a partial Symp$_{\mathrm{form}}$-equivariance result on the
bosonic boundary VOA.

**Does the CGW boundary VOA admit a super-balanced sector (super-VOA)?**

**Plausibly yes.** A *super-vertex operator algebra* (super-VOA) has
been studied extensively (Frenkel-Lepowsky-Meurman 1988 *Vertex
Operator Algebras and the Monster*, with later super-extensions by
Tsuchiya-Kanie 1986, Kac 1996 *Vertex algebras for beginners*, Lam
2008 *Lattice vertex superalgebras*). The CGW VOA, if it admits a
super-extension, would have:
- Even sector: the bosonic CGW boundary states.
- Odd sector: parity-flipped fermionic CGW states from the
  brane–anti-brane configuration.

**Specifically, the gl(N|M) gauge symmetry of the brane–anti-brane
boundary lifts to a $\widehat{gl(N|M)}_{k,k}$ super-affine vertex
algebra at level $(k, k)$**, generalizing the bosonic
$\widehat{gl(N)}_k$ (Frenkel-Reshetikhin 1996, *Quantum affine algebras
and holonomic difference equations*; Kac 1996 §2.5). The super-affine
algebra has:
- Even part $\widehat{gl(N)}_k\oplus\widehat{gl(M)}_k$ (two copies of
  bosonic affine algebras).
- Odd part: bi-fundamental fermionic generators.

**At super-balance ($N=M$, $k=k$): the central charge of
$\widehat{gl(N|N)}_{k,k}$ vanishes** (the supertrace of the central
extension is zero by the same mechanism as W22-T1+T2). This is the
*super-VOA analogue of the QME vanishing*. **Free of all the
central-charge obstructions catalogued in W3-W31-T2 for the bosonic
case.**

**Symp$_{\mathrm{form}}$-equivariance on super-VOA.** W3-W31-T2 gave
partial Symp-form-equivariance on the bosonic CGW VOA at quadratic
symplectomorphism order; full Symp-form-equivariance broke at higher
orders. **Conjecture: on the super-balanced sector of the
super-CGW-VOA (gl(N|N) at super-balance), Symp-form-equivariance is
*free* — no anomaly obstruction to higher-order equivariance.**
The mechanism: the central charge vanishes by super-balancing
($\mathrm{Str}(I)=0$ in the super-affine central extension), so the
projective representation of Symp-form on the super-VOA is *honest*
(non-projective), and equivariance extends from quadratic to all
orders without obstruction.

**Verdict T7.** **The super-VOA refinement of CGW is a natural object,
realized concretely by the super-affine $\widehat{gl(N|N)}_{k,k}$ at
the central-extension-vanishing locus. Symp-form-equivariance is
plausibly free on this sector by the same supertrace-vanishing
mechanism as W22-T1+T2. This converts W3-W31-T2 from "partial
equivariance with obstruction" to "free equivariance on super-balanced
sector".**

**Phase-4 deliverable.** A precise theorem statement of the form:

> **Conjecture P4-G3-T-7-1.** *On the super-balanced sector of the
> super-CGW VOA (corresponding to gl(N|N) gauge symmetry at $N=M$),
> the Symp$_{\mathrm{form}}$-equivariance of the boundary VOA holds
> at every order of the quadratic-and-higher expansion. The
> obstruction to bosonic equivariance (W3-W31-T2 partial result) is
> killed by the supertrace vanishing of the central charge.*

12 mo milestone for rigorous proof; 6 mo for explicit central-charge
computation.

**Files read.** `wave3-W31-5dM-obstructions-2026-04-28.md` 1–60
(mandate region); cross-walk to `wave3-W23-5dM-sigma-2026-04-28.md`
(via W31 inputs); Frenkel-Lepowsky-Meurman 1988, Kac 1996 (super-VOA
references, cited from memory); Frenkel-Reshetikhin 1996 (super-affine
algebras, cited from memory).
**Confidence.** Medium-high. The super-VOA structure is standard;
the central-charge vanishing on super-balanced is direct from the
super-affine construction. The "free equivariance" conjecture is
plausible but needs explicit verification.
**Blast radius.** **Cross-group interaction with G4 unlocks a
super-VOA refinement of CGW with free Symp-form-equivariance on
super-balanced.** This is a load-bearing connection: the super-balanced
locus is *simultaneously* QME-anomaly-free (W22-T1+T2) and
Symp-form-equivariance-anomaly-free (P4-G3-T-7-1 conjecture).
**Adjudication.** Valid cross-group outline.
**Residual.** P4-G3-R-11: rigorous proof of P4-G3-T-7-1 conjecture
on super-CGW-VOA Symp-equivariance.

---

## §2. Three-pronged Phase-4 program — consolidated milestones

### (A) prong: Other classical superalgebras

| Phase | Milestone | Deliverable | Confidence |
|-------|-----------|-------------|------------|
| 3 mo  | osp(2N\|2N) W22-T2 analogue | P4-G3-T-A1 rigorous theorem | High |
| 6 mo  | psl(N\|N) regulator + (A5) | Either theorem or named obstruction | Medium |
| 12 mo | Full catalog (q via Sergeev, p via alt regulator, exceptional no-go) | Complete superalgebra catalog | High |

### (B) prong: Unreduced primitive parallel factorization

| Phase | Milestone | Deliverable | Confidence |
|-------|-----------|-------------|------------|
| 3 mo  | BD unital chiral algebra + BV/QME adaptation | Conceptual framework | Medium |
| 6 mo  | Chain-level $\eta$ as coboundary in unital BV cohomology | Explicit construction | Low-Medium |
| 12 mo | Resolve W18-C3 (affirmative or precise no-go) | Vol III chapter or no-go theorem | Low-Medium |

### (C) prong: Character extensions beyond Capelli

| Phase | Milestone | Deliverable | Confidence |
|-------|-----------|-------------|------------|
| 3 mo  | Sergeev central character on q(N) | Explicit $\chi^q_\hbar$ computation | High |
| 6 mo  | Higher Capelli at higher loops | $\ell$-loop character normalization catalog | Medium |
| 12 mo | Full character-class survey | Knowledge consolidation document | High |

---

## §3. Cross-group interactions

| Interaction | Object | Status | Phase-4 milestone |
|-------------|--------|--------|------------------|
| G3 + G2 | Parity-graded column-Verma on gl(N\|N) | Outline | 6 mo |
| G3 + G2 | Super-Čech-SES four-cone | Outline | 6 mo |
| G3 + G2 | osp(2N\|2N) column-Verma | Outline | 12 mo |
| G3 + G4 | Super-CGW VOA (super-affine $\widehat{gl(N\|N)}_{k,k}$) | Outline | 6 mo |
| G3 + G4 | Free Symp-form-equivariance on super-balanced | Conjecture P4-G3-T-7-1 | 12 mo |

---

## §4. Residuals after this G3 outline

- **P4-G3-R-01.** psl(N|N), p(N) regulator construction (degenerate Killing form). Phase-4 (A) prong.
- **P4-G3-R-02.** q(N) Sergeev central element investigation. Phase-4 (C) prong.
- **P4-G3-R-03.** Physical brane configurations rigorous BCOV embedding. Cross-walk to R-W3-W22-05.
- **P4-G3-R-04.** Rigorous BCOV / topological B-model embedding of super-balanced sources. Phase-3/4.
- **P4-G3-R-05.** BD unital chiral algebra adaptation to BV/QME. Phase-4 (B) prong.
- **P4-G3-R-06.** Costello-Gwilliam Vol III chapter on unreduced local Lie algebras. Phase-4 (B) prong.
- **P4-G3-R-07.** Higher-Capelli higher-loop computation on $\mathfrak{gl}_N$. Phase-4 (C) prong.
- **P4-G3-R-08.** Sergeev central element on q(N) and its character class. Phase-4 (C) prong.
- **P4-G3-R-09.** Cross-prong integration after 12 mo. Phase-4 program-level.
- **P4-G3-R-10.** Explicit column-Verma on osp(2N|2N). Phase-4 G3+G2.
- **P4-G3-R-11.** Rigorous proof of P4-G3-T-7-1 (super-CGW Symp-equivariance). Phase-4 G3+G4.

---

## §5. Convergence verdict

**Three-pronged Phase-4 program: WELL-DEFINED.**

* **(A) prong (other classical superalgebras): TIGHTEST.** osp(2N|2N)
  is the cleanest first target; the same W22-T2 + W30 (A5) machinery
  applies directly. New theorem P4-G3-T-A1 is 3 mo realistic. The
  q(N) and psl(N|N) cases need alternative regulators / central
  elements.
* **(B) prong (unreduced primitive): HARDEST.** No standard machinery
  exists; Lurie HA gives the homotopy skeleton but not the
  Hamiltonian-specific construction; Costello-Gwilliam Vol II covers
  reduced not unreduced. A new chapter of factorization theory or a
  no-go theorem is the 12 mo deliverable. Beilinson–Drinfeld unital
  chiral algebra is the closest existing analogue.
* **(C) prong (character extensions): MOSTLY KNOWLEDGE-CONSOLIDATION.**
  W18-CT2 resolution holds; non-trivial extensions (higher Capelli,
  Sergeev on q(N), stable Capelli at large $N$) are mostly informationally
  parallel. The (C) prong's main novelty is the q(N) Sergeev central
  character investigation.

**Cross-group interactions.** G3+G2 unlocks parity-graded
column-Verma and super-Čech-SES. G3+G4 unlocks super-CGW VOA with
free Symp-form-equivariance on super-balanced. Both interactions
carry P4-G3-T-7-1 as a load-bearing conjecture.

**Phase-4 deliverables consolidated.**
- 1 new candidate theorem at 3 mo: P4-G3-T-A1 on osp(2N|2N).
- 1 conjecture at 12 mo: P4-G3-T-7-1 on super-CGW Symp-equivariance.
- 1 binary outcome at 12 mo: W18-C3 affirmative or no-go.
- 1 catalog at 12 mo: complete superalgebra+character catalog for
  super-balanced sources (the (C) prong consolidation).

**Posture against Wave 3.** Wave 3 closed the gl(N|N) super-balanced
case rigorously (W22-T1+T2 + W30 (A5)). Phase-4 G3 program extends
the methodology to other classical superalgebras (osp at minimum;
psl, p, q with caveats), opens the unreduced primitive question
(W18-C3) as a research-scale Phase-4 problem, and surveys character
extensions. The bosonic source obstruction (Theorem G $\hbar N[\bar c]$,
M-13) is preserved intact across all prongs.

**Inscribed durables.**
* This document.
* Three-pronged Phase-4 program (A / B / C) with milestones.
* P4-G3-T-A1 candidate-theorem proposal on osp(2N|2N).
* P4-G3-T-7-1 conjecture proposal on super-CGW Symp-equivariance.
* Cross-group interaction outline (G3+G2 column-Verma, G3+G4 super-VOA).

End of P4-G3 outline.
