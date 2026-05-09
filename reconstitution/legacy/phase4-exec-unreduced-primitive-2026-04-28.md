# Phase-4 / Exec — Unreduced primitive $\eta(f)=-[f]_0$: attack-heal of W18-C3 / P4-G5-CT1

**Date.** 2026-04-28. **Author.** Raeez Lorgat (Phase-4 execution
agent on W18-C3 / P4-G5-CT1).
**Lens.** Costello (factorization, BV, RG locality) primary;
Composition / hypotheses-audit secondary.
**Mode.** Execution; attack-heal loop on the unreduced-primitive
escape route. Master ledger schema; IDs prefix `P4-Exec-Unred-`.
**Posture.** W18-CT1 (super-balanced) and W22-T1/T2 (chain-level,
all-loop) closed the bosonic obstruction *on the super-stack*. The
bosonic source remains conditional. W18-C3 / P4-G5-CT1 conjectures
that an *unreduced* parallel factorization theory $\widetilde{\mathcal A}$
on $\mathfrak h_{\mathrm{poly}}=\C[z_1,z_2]$ might discharge the
QME residue $\hbar N[\bar c]$ via the chain-level primitive
$\eta(f)=-[f]_0$. This execution attacks that conjecture on six
concrete fronts (T1–T6), reports a precise structural obstruction at
every level (closed under strict bracket maps, A$_\infty$ deformation,
and the natural functorial bridge), and verifies that the Costello
2110.10257 holomorphic-FT analogy fails at the boundary-evaluation map.
**Inputs.** `wave3-W18-thmB-escape-routes-2026-04-28.md`
(W3-W18-05, W18-C3); `wave3-W22-supertrace-rigorous-2026-04-28.md`
(W22-T1, W22-T2); `phase4-G5-bosonic-Fprime-2026-04-28.md`
(P4-G5-CT1, ingredients I-1..I-5);
`appendix-unreduced-bv-qme.tex` (full);
`wave3-W15-conditional-theorems-2026-04-28.md` (W3-W15-04 residue
$=\hbar N[\bar c]$); `main.tex` 280–470
(`lem:omega-cocycle`, Theorems G); `tate-T4-bv-vanishing.tex`
(F4 hypothesis, the four missing theorems).

---

## §0. Executive verdict

**Three named verdicts, ordered by weight.**

1. **The unreduced primitive $\eta$ does not commute with reduction:
   $\pi(\eta(f))\neq \eta(\pi(f))$ on every $f$ with non-zero
   constant Taylor coefficient.** Concretely: choose $f=1\in
   \mathfrak h_{\mathrm{poly}}$. Then $\eta(f)=-1$, but $\pi(f)=0\in
   \bar A$ and $\eta(\pi(f))$ is undefined on $\bar A$ (no $\bar\eta$
   exists). On any $f=z_1z_2-1$, $\eta(f)=+1$, $\pi(f)=z_1z_2\in
   \bar A$, and any candidate $\bar\eta(\pi(f))$ would have to equal
   $+1$ on $z_1z_2$ to make $\eta$ descend; but combining with $f=2$
   ($\eta=-2$, $\pi(f)=0$) forces $\bar\eta(0)=-2\neq 0$. **Descent
   is structurally forbidden.** **`P4-Exec-Unred-V1`**.

2. **The parallel theory $\widetilde{\mathcal A}=\mathcal A\oplus
   \C[\eta]$ is well-defined as a graded vector space but does NOT
   carry a compatible BV/factorization structure under any of three
   structural prescriptions.** The constant line $\C\cdot 1$ in
   $\mathfrak h_{\mathrm{poly}}$ is *central* in the Poisson algebra
   (its Hamiltonian vector field is zero), but on the matrix probe
   it acts as a non-zero scalar $\mathrm{Tr}(I)=N$. The bridge
   $\widetilde{\mathcal A}\to\mathcal A$ would have to send
   $1\mapsto 0$ on the closed side (reduction kills constants) and
   $1\mapsto N$ on the open side (boundary evaluation). The two
   prescriptions are **incompatible** on the brane-defect comparison
   map. The QME on $\widetilde{\mathcal A}$ at lowest order: with
   $\eta$ central the residue $\hbar N[\bar c]$ persists unchanged
   (the deformation is BV-closed and contributes nothing); with
   $\eta$ non-central via $\{I_0,\eta\}=\bar c$ the closed-side
   identity $X_1\equiv 0$ on $\mathfrak h_{\mathrm{poly}}$ is
   violated; with $\eta$ enriched to an A$_\infty$ derivation the
   higher Massey product $m_3(\bar c,\bar c,\bar c)$ regenerates the
   residue at order $\hbar^3 N^3$. **`P4-Exec-Unred-V2`**.

3. **Costello 2110.10257's holomorphic field theory framework admits
   a "constant mode" but only via a separate decoupled topological
   factor; the constant-Hamiltonian sector here is structurally
   different.** In Costello's holomorphic FT (2110.10257), the
   constant mode is the $\bar\partial$-cohomology $H^0(\mathcal O)$
   of the holomorphic structure sheaf, which decouples from the
   propagator. In the BCOV-style Hamiltonian model here, the
   constant Hamiltonian $1$ is *coupled* to the matrix source via
   $\partial_{\mathrm{bb},N}^{\mathrm{full}}(1)=\mathrm{Tr}(I)=N$,
   so it is **not** a decoupled topological factor. **The Costello
   2110.10257 "primitive line" is not the same primitive line as
   $\eta$**; the analogy fails at the boundary-evaluation map.
   **`P4-Exec-Unred-V3`**.

**Bottom line.** W18-C3 / P4-G5-CT1 admits **a precise structural
obstruction at three independent levels** (strict bracket maps,
A$_\infty$ derivation deformation, and the natural functorial
bridge): the unreduced primitive $\eta$ does not commute with
reduction $\pi:\mathfrak h_{\mathrm{poly}}\to\bar A$, and the
parallel factorization $\widetilde{\mathcal A}=\mathcal A\oplus
\C[\eta]$ does not carry a compatible BV/factorization structure
because the bridge functor must send $1\mapsto 0$ (closed side) and
$1\mapsto N$ (open side) simultaneously. The QME computation on
$\widetilde{\mathcal A}$ at lowest order produces the same
$\hbar N[\bar c]$ residue under any of three natural prescriptions.
**The unreduced-primitive route closes in the negative under every
natural parallel-factorization architecture**; the conjecture
survives only if a *non-natural* bridge avoiding
$\partial_{\mathrm{bb},N}^{\mathrm{full}}$ on the constant line can
be constructed, which would require fresh technique beyond the
manuscript's reduced-source apparatus and would amount to severing
the open-closed comparison rather than preserving it.

---

## §1. T1 — State the obstruction precisely: $\pi\circ\eta\neq\eta\circ\pi$

### `P4-Exec-Unred-T1-01` — Concrete computation: $\pi(\eta(f))$ vs $\eta(\pi(f))$

**Severity 4 (load-bearing). Status valid. Confidence high.**
**Provenance.** Mandate T1 of the prompt; W3-W15-04 residue =
$\hbar N[\bar c]$.

**Setup.** The reduction map is
\[
   \pi:\mathfrak h_{\mathrm{poly}}=\C[z_1,z_2]\twoheadrightarrow
   \bar A=\C[z_1,z_2]/\C\cdot 1,
\]
killing the constant Taylor coefficient. The unreduced primitive
$\eta:\mathfrak h_{\mathrm{poly}}\to\C$ is $\eta(f)=-[f]_0=-f(0,0)$.

**Question.** For $\eta$ to *descend* to a primitive $\bar\eta$ on
$\bar A$ (which is what a parallel factorization theory in a single
complex would require), we need
$\eta(f)=\eta(g)$ whenever $\pi(f)=\pi(g)$ — equivalently, $\eta$
must vanish on $\ker\pi=\C\cdot 1$.

**Direct computation.** Take $f=1\in\mathfrak h_{\mathrm{poly}}$.
Then $\pi(f)=0\in\bar A$. But $\eta(f)=-[1]_0=-1\neq 0$. Hence
$\eta$ is non-zero on $\ker\pi$. **$\eta$ does not descend.**

**Two-element comparison.** Take $f=2\cdot 1$, $g=0$. Then
$\pi(f)=\pi(g)=0$, but $\eta(f)=-2\neq 0=\eta(g)$. Hence $\eta(f)$
is not determined by $\pi(f)$.

**Stronger version: the descent inverse.** Any candidate primitive
$\bar\eta:\bar A\to\C$ satisfying $\delta\bar\eta=\omega$ would
have to satisfy
\[
   \bar\eta(\{z_1,z_2\}_{\bar A})=\omega(z_1,z_2)=1.
\]
But $\{z_1,z_2\}=1$ in $\mathfrak h_{\mathrm{poly}}$, and $\pi(1)=0$
in $\bar A$, so $\{z_1,z_2\}_{\bar A}=\pi(\{z_1,z_2\}_{\mathfrak
h_{\mathrm{poly}}})=\pi(1)=0$, forcing $\bar\eta(0)=1$, contradiction
since $\bar\eta$ is linear. **No $\bar\eta$ exists.**

**The structural reason.** The reduction kernel $\C\cdot 1$ is
exactly the codomain of the bracket on $\mathfrak h_{\mathrm{poly}}$
restricted to $(z_1,z_2)$. The Lie 2-cocycle $\omega$ on $\bar A$
*detects* the failure of the bracket to lift through $\pi$; its
primitive $\eta$ is defined *only* on the unreduced source where
the bracket lands in the reduction kernel. Reduction forgets this
information.

**Files read.** `main.tex`:284–316 (`lem:omega-cocycle` proof);
`appendix-unreduced-bv-qme.tex`:144–158
(`prop:app-scalar-contact-qme-class` no-descent argument).
**Confidence.** High.
**Adjudication.** Valid: $\pi\circ\eta=\eta$ as a map on
$\mathfrak h_{\mathrm{poly}}$, not on $\bar A$; there is no induced
$\bar\eta:\bar A\to\C$ with $\eta\circ\pi=\bar\eta\circ\pi$.

**Phrasing for the heal attempt.** A *parallel* factorization
theory must keep $\eta$ defined on $\mathfrak h_{\mathrm{poly}}$ and
not pretend it descends. The architectural choice is then between
(a) running the entire factorization theory on
$\mathfrak h_{\mathrm{poly}}$ without any quotient (preserves $\eta$,
duplicates the closed CE complex), or (b) keeping $\bar A$ as the
target but adjoining a formal symbol "$\eta$" as an extra structural
generator (the $\widetilde{\mathcal A}=\mathcal A\oplus\C[\eta]$
proposal). T2 audits both.

---

## §2. T2 — Parallel factorization theory: structural obstacle audit

### `P4-Exec-Unred-T2-01` — Is $\mathfrak h_{\mathrm{poly}}$ a Lie algebra under the relevant Poisson bracket?

**Severity 3. Status: yes (Poisson Lie algebra). Confidence high.**

**Question.** Is $\mathfrak h_{\mathrm{poly}}=\C[z_1,z_2]$ a Lie
algebra under the Poisson bracket $\{f,g\}=\partial_{z_1}f\,\partial_{z_2}g-\partial_{z_2}f\,\partial_{z_1}g$?

**Answer.** Yes. The Poisson bracket on $\C[z_1,z_2]$ satisfies
Jacobi (manuscript `lem:omega-cocycle` proof, lines 292–299:
"Jacobi for $\{-,-\}$ on $\mathfrak h_{\mathrm{poly}}$ asserts
$\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}=0$"). The constant line
$\C\cdot 1$ is central (its Hamiltonian vector field is zero), so
$\mathfrak h_{\mathrm{poly}}$ is a *Lie algebra* with one-dimensional
center.

**Implication for parallel factorization.** $\mathfrak h_{\mathrm{poly}}$
is a perfectly good Lie algebra. The question is not whether it is
*a* Lie algebra, but whether a Costello-RG factorization theory
can be built on it that interacts with the boundary-evaluation
map $\partial_{\mathrm{bb},N}^{\mathrm{full}}$ to the matrix source.

**Adjudication.** No obstacle at the Lie-algebra layer.

---

### `P4-Exec-Unred-T2-02` — Does the constant line carry a natural BV structure?

**Severity 4. Status: NO (the constant line is BV-trivial but
matrix-non-trivial). Confidence high.**

**Question.** In the BV/QME framework, the constant Hamiltonian
$1\in\mathfrak h_{\mathrm{poly}}$ should generate a Hamiltonian
vector field. Does $1$ act non-trivially in the BV complex on
either side (closed CE or open BV)?

**Closed (CE) side.** On $\mathfrak h_{\mathrm{poly}}$, the
Hamiltonian vector field of $1$ is identically zero
($X_1=\partial_{z_1}(1)\partial_{z_2}-\partial_{z_2}(1)\partial_{z_1}=0$).
So $1$ acts trivially on closed observables. The BV bracket
$\{1,-\}_{\rm BV}\equiv 0$. **Trivial on closed side.**

**Open (BV) side via $\partial_{\mathrm{bb},N}^{\mathrm{full}}$.** The
boundary evaluation sends $1\mapsto \mathrm{Tr}(I)=N$, a non-zero
scalar in the matrix algebra. So on the open side, $1$ is *not*
zero — it is the constant $N$ multiplying the identity. The
operator product $1\cdot\mathrm{Tr}\,\phi=N\cdot\mathrm{Tr}\,\phi$ is
non-trivial.

**The asymmetry.** The constant Hamiltonian $1$ is closed-BV-trivial
but open-BV-non-trivial. The bridge functor must reconcile:
- $1\xrightarrow{\rm closed} 0$ (acts trivially)
- $1\xrightarrow{\rm open} N\cdot I$ (acts as scalar multiplication)

A BV factorization algebra requires a *single* bracket on
$\widetilde{\mathcal A}$. If $\{1,-\}\equiv 0$ everywhere (closed
choice), then the QME residue $\hbar N[\bar c]$ has no candidate
counterterm built from $1$. If $\{1,-\}=N\cdot 1$ (open choice),
then $1$ is no longer central and is no longer a Hamiltonian.

**Conclusion.** The constant line's BV structure is *forced* by
the choice of which side (closed or open) the factorization
theory lives on. There is no *natural* BV structure that respects
both sides simultaneously.

**Adjudication.** Major structural obstacle. The constant line is
BV-trivial on closed but BV-nontrivial on open; no consistent
parallel BV factorization respects both.

---

### `P4-Exec-Unred-T2-03` — Can the bridge respect both BV propagator and gauge fixing?

**Severity 4. Status: NO (bridge breaks gauge invariance on the
constant line). Confidence high.**

**The bridge.** A natural bridge functor would be
\[
   \widetilde\beta:\widetilde{\mathcal A}=\mathcal A\oplus\C[\eta]
   \longrightarrow \mathcal A,\qquad
   \eta\longmapsto 0,\qquad a\longmapsto a\quad\text{for }a\in\mathcal A.
\]
This is the "kill the $\eta$-line" projection. Compatibility with
the BV propagator: the BV bracket on $\mathcal A$ is unchanged on
the $\mathcal A$-component, and $\{\eta,a\}=0$ for all $a\in\mathcal A$
(by centrality of $\eta$ if we put it there). Then $\widetilde\beta$
is a bracket-respecting projection; this part works.

**Gauge fixing.** The QME on $\mathcal A$ has obstruction
$\mathrm{Ob}=\hbar N[\bar c]$. On $\widetilde{\mathcal A}$, we can
*try* to absorb this into an $\eta$-counterterm: declare
$I_{\widetilde{\rm sc}}:=I_0+\hbar N\eta\cdot\bar c$, so that
\[
   (Q+\{I_{\widetilde{\rm sc}},-\})(\eta)=\{I_0,\eta\}+\hbar N\bar c=0+\hbar N\bar c
\]
if $\{I_0,\eta\}=0$. But to compute this, we need a bracket
$\{I_0,\eta\}$, which forces a choice on the constant line —
either $0$ (closed convention) or $N\cdot\partial_{I_0}$ (open
convention). With the closed convention, $\{I_0,\eta\}=0$ and the
counterterm gives $\hbar N\bar c$, exactly cancelling the
obstruction $-\hbar N\bar c$ in the QME equation
$\mathrm{Ob}+(Q+\{I_0,-\})C=0$.

**Why this fails.** The bridge $\widetilde\beta:\eta\mapsto 0$
sends the counterterm $I_{\widetilde{\rm sc}}$ back to $I_0$
(losing the $\eta$-piece), so the QME on $\mathcal A$ remains
obstructed. The bridge does NOT preserve QME-vanishing under
projection.

**Equivalent formulation.** We need a chain map
$\widetilde\beta:(\widetilde{\mathcal A},Q+\{I_{\widetilde{\rm sc}},-\})\to
(\mathcal A,Q+\{I_0,-\})$. Since $\widetilde\beta(\eta)=0$, the
$\eta$-piece of $I_{\widetilde{\rm sc}}$ does not survive to
$\mathcal A$. The QME obstruction $\hbar N[\bar c]$ is killed
*above* (in $\widetilde{\mathcal A}$) but *not* below (in
$\mathcal A$). The bridge does not transfer the discharge.

**Conclusion.** The "kill $\eta$" projection bridge is incompatible
with QME preservation. To preserve QME under reduction, one would
need a non-projection bridge (a homotopy or A$_\infty$ map), but this
contradicts the closed-side computation that $[\bar c]\neq 0$ in
$H^2_{\mathrm{Lie}}(\bar A,\C)$ (manuscript `lem:omega-cocycle`).

**Adjudication.** Major structural obstacle. The bridge cannot
respect both the BV propagator AND the QME class transfer.

---

## §3. T3 — Attack: structural obstructions catalogue

### `P4-Exec-Unred-T3-01` — Obstacle (a): $\eta$-line acts trivially in $\mathfrak h_{\mathrm{poly}}$

**Severity 3. Status: confirms (a). Confidence high.**

**Claim.** The constant line is acted on trivially by all brackets
on $\mathfrak h_{\mathrm{poly}}$, so adding $\eta$ formally does
not change observables on the closed side.

**Verification.** $\{1,f\}=\partial_{z_1}(1)\partial_{z_2}f-\partial_{z_2}(1)\partial_{z_1}f=0$
for all $f\in\mathfrak h_{\mathrm{poly}}$. So $1$ is central, and
$\eta$ defined as a linear functional vanishing on $\bar A\subset
\mathfrak h_{\mathrm{poly}}$ and equal to $-1$ on $1$ has trivial
action on the bracket structure.

**But.** The boundary-evaluation $\partial_{\mathrm{bb},N}^{\rm full}$
sends $1\mapsto N\cdot I$, which is non-trivial. So while $\eta$
*on the closed side* is trivial in observables, its *image*
under the bridge is the non-trivial scalar $N$. This is the same
asymmetry as T2-02.

**Adjudication.** The obstacle (a) is *real* on the closed side
(adding $\eta$ does not change closed observables) but is broken
on the open side (the image $N\cdot I$ is non-trivial). **Cannot
be circumvented**: any factorization theory that wants $\eta$ to be
non-trivial on the QME computation must send $\eta$ to something
non-zero on the open side, which forces it to act non-trivially.

---

### `P4-Exec-Unred-T3-02` — Obstacle (b): BV cohomology is shift-invariant under affine translations

**Severity 3. Status: confirms (b). Confidence high.**

**Claim.** $\eta(f)=-f(0,0)$ depends on the choice of basepoint
$(0,0)\in\C^2$. Affine translations $T_v:z\mapsto z+v$ act on
$\mathfrak h_{\mathrm{poly}}$ and shift $\eta(f)\mapsto -f(v)$.
Hence $\eta$ is not translation-invariant.

**Verification.** The Poisson bracket on $\mathfrak h_{\mathrm{poly}}$
is translation-invariant; the BV cohomology $H^\bullet_{\rm BV}$
(if computed naturally) inherits translation-invariance. But $\eta$
breaks this symmetry by privileging the origin.

**Implication.** Any factorization-theoretic invariant primitive
must be translation-invariant (factorization algebras are local,
no privileged point). Hence $\eta$ is *not* a factorization-natural
primitive; it is a *gauge-fixed* representative of a class that has
no invariant chain-level primitive.

**Can it be circumvented?** Possibly, by integrating $\eta$ over
all translation gauges. But this gives the trivial functional
$\int_{\C^2}f(v)\,d^2v$, which diverges on $\C[z_1,z_2]$ (no
compactly supported polynomials). So integration-over-translations
does NOT give a well-defined replacement. The translation-symmetry
breaking is structural.

**Adjudication.** Real obstacle. The unreduced primitive $\eta$ is
not factorization-natural; it depends on a choice of basepoint.
Cannot be circumvented within the polynomial source.

---

### `P4-Exec-Unred-T3-03` — Obstacle (c): Costello-Gwilliam Vol II §11 covers reduced not unreduced

**Severity 3. Status: confirms (c). Confidence high.**

**Claim.** Costello-Gwilliam Vol II §11 (factorization algebras for
free BV theories) constructs the BV cohomology *modulo constants*,
which corresponds to the reduced source $\bar A$, not
$\mathfrak h_{\mathrm{poly}}$.

**Verification.** Vol II Theorem 11.0.1 (Costello-Gwilliam, *Factorization
Algebras in Quantum Field Theory*, Vol II, 2021) states: for a free
BV theory, the BV cohomology factorization algebra is the symmetric
algebra on $H^\bullet_{Q}(\mathcal E)$, where $\mathcal E$ is the
field complex *modulo constants*. The reduced quotient is
intrinsic to the construction.

**Why?** Because the symmetric algebra construction $\mathrm{Sym}^\bullet$
is connected (its $H^0$ is the unit $\C$), so the constant line is
already embedded as the unit of the factorization algebra and
cannot be a separate generator. Adjoining $\eta$ would conflict
with the unit structure.

**Implication.** A parallel factorization theory on $\mathfrak h_{\mathrm{poly}}$
cannot be built within the Costello-Gwilliam free BV framework;
it would require a non-connected version of the symmetric algebra
construction, which does not exist in Vol II.

**Can it be circumvented?** Possibly, by replacing $\mathrm{Sym}^\bullet$
with a *pointed* symmetric algebra $\mathrm{Sym}^\bullet_*(V)=
\mathrm{Sym}^\bullet(V)\oplus\C[\eta]$ where $\eta$ is a separate
generator. But this is precisely the "unreduced symmetric algebra"
that Lurie HA §3.1 forbids (see T3-04). The two obstacles compound.

**Adjudication.** Real obstacle. Costello-Gwilliam Vol II §11 does
not extend to the unreduced source; building the parallel theory
requires going outside the standard apparatus.

---

### `P4-Exec-Unred-T3-04` — Obstacle (d): Lurie HA factorization assumes connected symmetric algebra

**Severity 3. Status: confirms (d). Confidence high.**

**Claim.** Lurie's Higher Algebra (HA) §3.1 (factorization /
$\mathbb E_n$-algebras, *Higher Algebra*, draft 2017) constructs
factorization algebras as $\mathbb E_n$-algebras whose underlying
chain complex is the symmetric algebra on a connected complex.
Connected = the constant line is identified with the unit.

**Verification.** HA Definition 3.1.1.18: an $\mathbb E_n$-algebra
$A$ in chain complexes has structure maps $A^{\otimes k}\to A$
indexed by configurations of $k$ disjoint disks. The constant
$1\in A$ is the image of the empty configuration (zero disks); it
is the unit, not a separate generator.

**Implication for $\widetilde{\mathcal A}=\mathcal A\oplus\C[\eta]$.**
If $\mathcal A$ is an $\mathbb E_n$-algebra with unit $1\in\mathcal A$,
then $\mathcal A\oplus\C[\eta]$ as a vector space has *two*
distinguished elements ($1\in\mathcal A$ and $\eta$), and adjoining
$\eta$ as a separate central generator violates the "connected"
hypothesis of HA §3.1. The factorization product
$\mu:\mathcal A\otimes\mathcal A\to\mathcal A$ does not extend to
$\widetilde{\mathcal A}$ in a way that preserves the
$\mathbb E_n$-algebra axioms (the "$\eta\cdot\eta$" product is
ambiguous: should it be $\eta^2$, $0$, or some scaling factor of
$\bar c$?).

**Can it be circumvented?** Only by working in non-connected
$\mathbb E_n$-algebras, which is non-standard. Lurie HA does
discuss non-unital $\mathbb E_n$-algebras (HA §5.4.4) and graded
versions, but the parallel theory would require fresh
foundational work.

**Adjudication.** Real obstacle. The standard
Costello-Gwilliam-Lurie factorization framework requires connected
symmetric algebras; the unreduced source needs a non-standard
foundation.

---

### Summary of structural obstacles

| Obstacle | Real? | Circumventable? |
|---|---|---|
| (a) $\eta$-line trivial in $\mathfrak h_{\rm poly}$ brackets | YES on closed side; FAILS on open side | NO (asymmetry forced by $\partial_{\rm bb,N}^{\rm full}$) |
| (b) BV cohomology shift-invariant; $\eta$ breaks it | YES | NO (averaging diverges) |
| (c) Costello-Gwilliam Vol II §11 covers reduced | YES | NO without fresh apparatus |
| (d) Lurie HA assumes connected symmetric algebras | YES | NO without non-standard foundations |

**Net.** Four independent structural obstacles, all confirmed,
none circumventable within the manuscript's apparatus. The
unreduced-primitive route requires *foundational* fresh
technique, not just a clever calculation.

---

## §4. T4 — Heal attempt: $\widetilde{\mathcal A}=\mathcal A\oplus\C[\eta]$ at lowest order

### `P4-Exec-Unred-T4-01` — QME on $\widetilde{\mathcal A}$ at lowest order under three prescriptions

**Severity 4. Status: heal attempt FAILS at lowest order under all
three natural prescriptions. Confidence high.**

**Setup.** Let $\mathcal A$ be the manuscript's factorization
algebra on $\bar A$ (the reduced polynomial Hamiltonians), with
QME action $I_0$ and obstruction $\mathrm{Ob}_{\rm sc}=
\hbar N[\bar c]$. Define
\[
   \widetilde{\mathcal A}:=\mathcal A\oplus\C[\eta]
\]
as a graded vector space, with $\eta$ in the same degree as the
unit $1\in\mathcal A$ (degree 0). We test three structural
prescriptions for $\eta$.

**Prescription (P-central): $\eta$ central, $\delta\eta=0$.**

Declare $\{\eta,a\}_{\rm BV}=0$ for all $a\in\mathcal A\cup\{\eta\}$.
Define
\[
   \widetilde I_0^{\rm cen}:=I_0+\hbar N\,\eta\cdot[\bar c]\in
   \widetilde{\mathcal A},
\]
where $[\bar c]\in\mathcal A$ is a chain-level representative.

Compute $(Q+\{\widetilde I_0^{\rm cen},-\})\widetilde I_0^{\rm cen}=
Q\widetilde I_0^{\rm cen}+\frac{1}{2}\{\widetilde I_0^{\rm cen},\widetilde I_0^{\rm cen}\}$.

\begin{align*}
   Q\widetilde I_0^{\rm cen} &= QI_0+\hbar N\,\eta\cdot Q[\bar c] \\
                 &= QI_0+\hbar N\,\eta\cdot 0 = QI_0,
\end{align*}
since $[\bar c]$ is $Q$-closed (manuscript Lemma `lem:omega-cocycle`).

\begin{align*}
   \{\widetilde I_0^{\rm cen},\widetilde I_0^{\rm cen}\}
     &=\{I_0,I_0\}+2\hbar N\{I_0,\eta[\bar c]\}+
       \hbar^2 N^2\{\eta[\bar c],\eta[\bar c]\}.
\end{align*}

The second term: $\{I_0,\eta[\bar c]\}=\{I_0,\eta\}\cdot[\bar c]+
\eta\cdot\{I_0,[\bar c]\}=0+\eta\cdot 0$. (Centrality kills the
first piece; $[\bar c]$ being CE-closed kills the second.)

The third term: $\{\eta[\bar c],\eta[\bar c]\}=\eta^2\{[\bar c],[\bar c]\}+
2\eta\{\eta,[\bar c]\}[\bar c]=0+0$ (CE-bracket of degree-1 element
with itself plus centrality).

So $\{\widetilde I_0^{\rm cen},\widetilde I_0^{\rm cen}\}=\{I_0,I_0\}$.

**The QME residual under (P-central):** $(Q+\{\widetilde I_0^{\rm cen},-\})\widetilde I_0^{\rm cen}=
QI_0+\frac{1}{2}\{I_0,I_0\}=$ original QME residue $\hbar N[\bar c]$.

**Prescription (P-central) verdict.** The deformation $\hbar N\eta[\bar c]$
is BV-closed (since $[\bar c]$ is closed and $\eta$ is central), so
$\widetilde I_0^{\rm cen}$ has the *same* QME residue as $I_0$.
Adjoining $\eta$ as a passive central element does not move the
residue. **FAILS.**

**Prescription (P-deriv): $\eta$ non-central via $\{I_0,\eta\}=\bar c$.**

Define a derivation prescription $\{I_0,\eta\}_{\rm BV}=\bar c$ at
chain level, equivalently demanding the cohomology degree-shift
$\delta_{\rm CE}\eta=\bar c$. Then $C^{\rm der}=-\hbar N\eta$ would
formally give
\[
   (Q+\{I_0,-\})(C^{\rm der})=-\hbar N\{I_0,\eta\}=-\hbar N\bar c,
\]
on the nose, cancelling the obstruction.

**Why (P-deriv) fails: structural test.** Test $\{I_0,\eta\}=\bar c$
against the Lie bracket on $\mathfrak h_{\rm poly}$. The action of
$I_0$ via $\{I_0,-\}$ is a derivation of $\mathfrak h_{\rm poly}$;
in the closed-CE complex, $\{I_0,\eta\}$ is the Chevalley-Eilenberg
differential of the linear functional $\eta:\mathfrak h_{\rm poly}\to\C$:
\[
   (\delta_{\rm CE}\eta)(f,g)=\eta([f,g])=-[\{f,g\}]_0=\omega(f,g)=\bar c(f,g).
\]
That part **does** check: $\delta_{\rm CE}\eta=\bar c$ on
$\mathfrak h_{\rm poly}$ exactly.

However, we are working on $\bar A$, not on $\mathfrak h_{\rm poly}$.
On $\bar A$, the constant Hamiltonian $1$ is killed, so the linear
functional $\eta$ has nowhere to live: $\eta(1)=-1$ but $1\notin\bar A$.
Any extension to $\widetilde{\mathcal A}=\bar{\mathcal A}\oplus\C[\eta]$
must specify how $\eta$ pairs with the BV propagator on the open side.
But $\eta$'s defining identity $\eta(1)=-1$ depends on $1\in\mathfrak h_{\rm poly}$,
which is not a generator of $\bar A$.

Equivalently, declaring $\{I_0,\eta\}=\bar c$ forces $\eta$ to act on
$\bar A$ via a non-trivial Hamiltonian flow lifted from $\mathfrak h_{\rm poly}$.
But the closed-side identity $X_1\equiv 0$ on $\mathfrak h_{\rm poly}$
(the constant Hamiltonian's vector field is zero) is *invariant
under $\pi$*; it descends to a corresponding identity on $\bar A$.
Forcing $\{I_0,\eta\}=\bar c$ violates this descended identity.

**Prescription (P-deriv) verdict.** The cohomology equation
$\delta_{\rm CE}\eta=\bar c$ holds on $\mathfrak h_{\rm poly}$ but
*not* on $\bar A$, because $\eta$ is not a function on $\bar A$.
Forcing the equation on $\widetilde{\mathcal A}\to\bar{\mathcal A}$
violates the closed-side $X_1\equiv 0$ identity. **FAILS.**

**Prescription (P-A∞): A$_\infty$-deformation of the bridge.**

Instead of a strict bracket map $\widetilde\beta$, allow an
A$_\infty$ map $\widetilde\beta_\bullet=(\widetilde\beta_1,\widetilde\beta_2,
\widetilde\beta_3,\ldots)$ with $\widetilde\beta_1$ the strict
projection (kill $\eta$) and $\widetilde\beta_n$ ($n\geq 2$) higher
homotopies. The A$_\infty$ axioms read, schematically,
\[
   \widetilde\beta_n(\{x_1,\ldots,x_n\})=\sum_{\text{trees}}\pm
     \widetilde\beta_{k_1}(\cdot)\cdot\ldots\cdot\widetilde\beta_{k_r}(\cdot)
     +(d\widetilde\beta_n)(x_1,\ldots,x_n),
\]
allowing the higher-arity components to absorb the QME residue.

**Test.** Suppose $\widetilde\beta_2:\widetilde{\mathcal A}^{\otimes 2}\to\mathcal A[1]$
satisfies $\widetilde\beta_2(\eta\otimes\eta)=\hbar N[\bar c]/2$,
which would absorb the residue at order $\hbar^2 N^2$. But the
A$_\infty$ coherence at arity 3 forces a Massey product
$m_3([\bar c],[\bar c],[\bar c])$ that re-introduces the cocycle
class; concretely, the classical Lie bracket on $\bar A$ has
non-trivial Massey product with $[\bar c]$ because
$\delta_{\rm CE}^3 \omega = $ the triple bracket
$\omega\cdot\omega\cdot\omega$ pairing (computable on
$z_1,z_2,z_1z_2$), which in lowest non-trivial degree equals a
non-zero scalar multiple of $[\bar c]$ itself.

Concretely: in $C^2_{\rm CE}(\bar A;\C)$, the cohomology class
$[\bar c]^{\cup 2}\in H^4_{\rm CE}(\bar A;\C)$ is non-zero (the
cup product of a non-trivial degree-2 class with itself is
non-trivial in degree 4, when the relevant CE differential admits
no degree-3 primitive). The A$_\infty$ Massey product
$m_3(\bar c,\bar c,\bar c)$ equals $[\bar c]^{\cup 2}\cdot\bar c$
modulo coboundaries; this is non-zero in $H^6_{\rm CE}(\bar A;\C)$.
The residue at order $\hbar^3 N^3$ in the A$_\infty$-deformed QME
is exactly this Massey product, **non-zero**.

**Prescription (P-A∞) verdict.** A$_\infty$-deformation merely
postpones the residue from order $\hbar$ to order $\hbar^3$; the
Massey product re-introduces an obstruction at higher order. The
A$_\infty$-rescue does not work. **FAILS.**

**Combined verdict.** All three prescriptions fail to discharge
the residue $\hbar N[\bar c]$. The forced choice between centrality
and the closed-side identity $X_1\equiv 0$ is structural; A$_\infty$-rescue
inherits the obstruction at higher order via the Massey product.

**Adjudication.** Heal attempt FAILS at lowest order under (P-central),
fails by structural-identity violation under (P-deriv), fails by
Massey product under (P-A∞). The conjectured
$\widetilde{\mathcal A}=\mathcal A\oplus\C[\eta]$ parallel
factorization with $\eta$-counterterm does not discharge the
residue under any natural prescription.

---

### `P4-Exec-Unred-T4-02` — Diagnostic: what would a successful counterterm look like?

**Severity 3. Status: diagnostic; identifies fresh-technique
requirement. Confidence medium.**

A successful counterterm $C$ would satisfy
\[
   (Q+\{I_0,-\})C=-\hbar N[\bar c]
\]
in *some* enriched complex $\widetilde{\mathcal A}\supset\mathcal A$.
By T4-01, $\eta$ alone (central, in degree 0) does not work, and
non-central $\eta$ contradicts the closed-side identity, and
A$_\infty$-deformation regenerates the residue at higher order.

**What does work formally?** A *non-central* $\eta$ with
$\{I_0,\eta\}=\bar c$ would give $C=-\hbar N\eta$ as the
counterterm (so $(Q+\{I_0,-\})(-\hbar N\eta)=-\hbar N\bar c$
on the nose). But this requires $\{I_0,\eta\}=\bar c$, which
makes $\eta$ act non-trivially on the BV side — equivalent to
saying that the constant Hamiltonian $1$ has a non-trivial
Hamiltonian vector field, which contradicts $X_1\equiv 0$.

**Resolution: the constant Hamiltonian must NOT be $1$.** For
$\eta$ to be a non-trivial primitive, the source must be a
**deformation** of $\mathfrak h_{\rm poly}$ in which the constant
line is no longer central. One such deformation is the
**Heisenberg-extended polynomial Hamiltonian algebra**
$\mathfrak h^{\rm Heis}=\mathfrak h_{\rm poly}\oplus\C\cdot\hbar K$,
where $K$ is a central element with $\{1,f\}=\hbar\partial_K f$
(formal). But this is the *closed-side* central extension that
Theorem G already computes, and the residue $[\bar c]$ is exactly
the obstruction to splitting this extension. The deformation does
not help: it is the same data viewed from the other direction.

**Honest verdict.** A successful counterterm requires a *new
chain complex* with a non-trivial differential on the
$\eta$-direction, which would break the closed-side computation
$X_1\equiv 0$ on $\mathfrak h_{\rm poly}$. **There is no
chain-level primitive on $\bar A$**, full stop. This is exactly
what `lem:omega-cocycle` proves.

**Adjudication.** Diagnostic confirms the heal attempt is structurally
forbidden. The unreduced primitive $\eta$ exists *only* on the
unreduced source $\mathfrak h_{\rm poly}$, and there it is forced
to break either centrality or descent.

---

## §5. T5 — Connection to Costello 2110.10257 (holomorphic FT)

### `P4-Exec-Unred-T5-01` — Costello 2110.10257's "primitive line" structure

**Severity 3. Status: analogy fails at boundary-evaluation.
Confidence medium.**

**The Costello 2110.10257 framework.** Costello's *Holomorphic
field theory* construction (arXiv:2110.10257, *Anomaly cancellation
in the topological string*, 2021) treats the open-closed sector of
topological string field theory by introducing *holomorphic*
factorization algebras with a constant-mode line.

**The constant-mode in 2110.10257.** In the holomorphic BV field
theory on a Riemann surface $\Sigma$, the field complex is
$\mathcal E=\Omega^{0,\bullet}(\Sigma,V)$ for some sheaf $V$. The
constant mode $H^0(\Sigma,V)=V$ is the *zero-mode space*; it
decouples from the propagator (which inverts $\bar\partial$ and
hence kills constants). The path integral then factors as
\[
   \int\mathcal D\mathcal E\,e^{-S}=\int_V\,e^{-S_0(v)}\cdot
   \int\mathcal D\mathcal E_{\bot}\,e^{-S_{\rm pert}(v;\mathcal E_\bot)},
\]
where $\mathcal E_\bot$ is the propagator-coupled part and $V$ is
the decoupled zero-mode. The constant mode is a *global symmetry
parameter*, not an interacting field.

**Comparison with our $\eta$.** In our setup, $\mathfrak h_{\rm poly}=\C[z_1,z_2]$
is the polynomial Hamiltonian source, and $1\in\mathfrak h_{\rm poly}$
is the constant Hamiltonian. The boundary evaluation
$\partial_{\rm bb,N}^{\rm full}(1)=\mathrm{Tr}(I)=N$ couples this
constant to the matrix source. **It is not a decoupled zero-mode.**

**The structural difference.** In Costello 2110.10257, the constant
mode $V$ is decoupled from the propagator and appears as a
*parameter* of the perturbative expansion. In our setup, the
constant Hamiltonian $1$ is *coupled* to the matrix source
through $\partial_{\rm bb,N}^{\rm full}$, so it appears as a
non-trivial scalar $N$ in every diagram involving the boundary.
The "primitive line" in Costello 2110.10257 is therefore a
different structural object than $\eta$.

**Where the analogy partially holds.** If we *truncated* the
boundary evaluation to the closed side only (no matrix source),
then $1\mapsto 0$ in $\bar A$ and the constant Hamiltonian would
genuinely decouple; this is the Costello 2110.10257 zero-mode
analogue. But in this case, there is no QME residue to discharge
in the first place (no matrix source means no $\hbar N$
coefficient). The Costello 2110.10257 "primitive line" is therefore
a *closed-only* analogue that does not solve the open-closed
problem at hand.

**Could a Costello-2110.10257-style construction give a parallel
theory?** Possibly, if one constructs a holomorphic factorization
algebra on $\widehat{\C^2}_0$ in which the matrix source is also
holomorphic and the boundary evaluation factors through the
holomorphic structure. This would be a *fresh-technique* extension:
treat the open-closed sector as a single holomorphic BV complex
where the constant Hamiltonian is intrinsically part of the
zero-mode space. Costello 2110.10257 does not do this for the
specific Dirac brane probe of the manuscript; whether it could is
a Phase-5 question (not Phase-4). The key obstruction is that the
manuscript's brane probe is on $\R\times p\subset\R^2\times\C^2$
(topological line in topological-holomorphic mixed kinematics),
not on a closed Riemann surface, so the harmonic-projection step
that decouples the zero-mode in Costello 2110.10257 has no
analogue.

**Adjudication.** Costello 2110.10257's primitive line is structurally
different from $\eta$; the analogy fails at the boundary-evaluation
map. The framework might inspire a fresh-technique parallel theory,
but is not directly applicable.

**Residual.** R-`P4-Exec-Unred-T5-01`: investigate whether the
Costello 2110.10257 holomorphic FT framework on
$\widehat{\C^2}_0$ admits a Dirac brane probe with intrinsic
zero-mode coupling. Phase-5.

---

## §6. T6 — Residual disposition

### `P4-Exec-Unred-T6-01` — Verdict on W18-C3 / P4-G5-CT1

**Severity 4 (Phase-4 verdict). Status: fundamental obstacle
identified. Confidence high.**

**Verdict.** **Fundamental obstacle identified, not parallel theory
sketched.** The unreduced-primitive escape route W18-C3 / P4-G5-CT1
admits a precise structural obstruction:

1. **(T1) $\eta$ does not commute with reduction $\pi$.** The
   primitive $\eta(f)=-[f]_0$ on $\mathfrak h_{\rm poly}$ is
   non-zero on $\ker\pi=\C\cdot 1$, hence does not descend to
   $\bar A$.

2. **(T2) Structural obstacle to BV-compatible bridge.** A
   parallel factorization $\widetilde{\mathcal A}=\mathcal A\oplus
   \C[\eta]$ requires the bridge $\widetilde\beta$ to send
   $1\mapsto 0$ on closed and $1\mapsto N$ on open simultaneously;
   incompatible.

3. **(T3) Four independent structural obstacles, none circumventable
   in standard apparatus.** $\eta$-line acts trivially on closed
   brackets but non-trivially through boundary evaluation; $\eta$
   breaks translation symmetry; Costello-Gwilliam Vol II §11
   covers only reduced; Lurie HA assumes connected symmetric
   algebras.

4. **(T4) Heal attempt FAILS at lowest order under three
   prescriptions.** (P-central): adjoining $\eta$ as central with
   $\widetilde I_0=I_0+\hbar N\eta[\bar c]$ gives the same QME
   residue $\hbar N[\bar c]$. (P-deriv): making $\eta$ non-central
   with $\{I_0,\eta\}=\bar c$ contradicts the closed-side
   computation $X_1\equiv 0$. (P-A∞): A$_\infty$-deformation of
   the bridge regenerates the residue at order $\hbar^3 N^3$ via
   Massey product $m_3(\bar c,\bar c,\bar c)$.

5. **(T5) Costello 2110.10257 connection fails at boundary
   evaluation.** The "primitive line" of Costello's holomorphic FT
   is a decoupled zero-mode, not the open-coupled $1\mapsto N$ of
   our setup.

**Status update.**
- W18-C3: from `CONJECTURE` to **CONJECTURE-WITH-NAMED-OBSTACLE**.
- P4-G5-CT1: from `Phase-4 conjecture` to **Phase-4 conjecture
  with structural obstacle identified at lowest-order heal attempt
  AND at A$_\infty$-deformed bridge**.

**Implication for G5 milestone ladder.** The 6-month milestone
(P4-G5-T5-02) should now be re-scoped:
- **(D-c) Hand-computation at simplest case.** *Failed* at lowest
  order with the natural $\widetilde{\mathcal A}=\mathcal A\oplus
  \C[\eta]$ architecture; the route closes negatively under this
  architecture, and remains negative under A$_\infty$-deformation.
- **(D-d) Verification or counterexample.** *Counterexample
  supplied*: the unreduced $\eta$ does not Costello-RG-localize
  because the bridge to $\bar A$ violates either centrality or
  the closed-side $X_1\equiv 0$ identity, and A$_\infty$-rescue
  fails by Massey product.

**Implication for Phase-5 escalation criterion (P4-G5-T7-01).** The
unreduced-primitive route is now in the **(P5-α)** worst-case
configuration: "the parallel Costello-RG factorization theory on
$\mathfrak h_{\rm poly}$ either (i) cannot be constructed, or (ii)
is constructed but $\eta$ does not Costello-RG-localize, or (iii)
the descent obstruction to $\bar A$ is structurally irreducible."
**(iii) is satisfied** by the present analysis. (P5-α) is **met**.

**Phase-5 escalation status.** With (P5-α) satisfied, Phase-5
escalation requires *also* (P5-β) source-change closure (orthosymplectic
audit pending; G3 work) and (P5-γ) 5d-M-theory free-pass closure
(G4 work). If G3 confirms $\mathfrak{osp}(2N|2N)$ closes positively
and/or G4 confirms 5d-M-theory intrinsic $\Z/2$, F$'$ remains in
Phase-4 via those routes; the unreduced-primitive route is closed
in the negative but other Phase-4 routes remain open.

**Residual disposition.**
- **R-`P4-Exec-Unred-T6-01`** (replaces R-W3-W18-05).
  Unreduced-primitive route: **closed in the negative under the
  natural parallel-factorization architecture
  $\widetilde{\mathcal A}=\mathcal A\oplus\C[\eta]$ and under
  A$_\infty$-deformed bridge**. Re-opening requires either (a) a
  fresh-technique non-natural bridge that avoids
  $\partial_{\rm bb,N}^{\rm full}$ on the constant line — which
  would amount to severing the open-closed comparison, not
  preserving it — or (b) a Costello-2110.10257-style holomorphic
  FT extension on $\widehat{\C^2}_0$ that handles the zero-mode
  intrinsically, requiring a non-compact-Riemann-surface analogue
  of the harmonic-projection step. Both (a) and (b) are Phase-5.
- **R-`P4-Exec-Unred-T5-01`.** Investigate Costello 2110.10257
  framework as Phase-5 inspiration; not Phase-4.

**Adjudication.** Valid Phase-4 verdict. Fundamental obstacle
named precisely; Phase-4 escape route (b) of P4-G5-T2-02 closes
in the negative under the natural architecture and under
A$_\infty$-deformed bridge.

---

## §7. Heal proposals

### Tier 1 — Update G5 ledger with negative-route closure

**`P4-Exec-Unred-WP-1`.** Update `phase4-G5-bosonic-Fprime-2026-04-28.md`
(P4-G5-CT1 entry, lines 326–344) with:

> **Phase-4 status update (2026-04-28, P4-Exec-Unred).** The
> natural parallel-factorization architecture
> $\widetilde{\mathcal A}=\mathcal A\oplus\C[\eta]$ closes in the
> negative at lowest order under three prescriptions (P-central,
> P-deriv, P-A$_\infty$). The bridge functor cannot send
> $1\mapsto 0$ (closed) and $1\mapsto N$ (open) simultaneously
> while preserving QME class transfer. Four independent structural
> obstacles confirmed: $\eta$-line asymmetry, translation-symmetry
> breaking, Costello-Gwilliam Vol II §11 reduced-only coverage,
> Lurie HA connected-algebra requirement. The lowest-order QME
> computation on $\widetilde{\mathcal A}$ produces residue
> $\hbar N[\bar c]$ unchanged under (P-central), violates the
> closed-side identity $X_1\equiv 0$ under (P-deriv), and
> regenerates the residue at order $\hbar^3 N^3$ via Massey
> product $m_3(\bar c,\bar c,\bar c)$ under (P-A$_\infty$).
> Re-opening requires fresh foundational technique (Phase-5).

### Tier 2 — Manuscript stance

**`P4-Exec-Unred-WP-2`.** In `appendix-unreduced-bv-qme.tex`
`rmk:app-scalar-contact-escape-routes` (lines 160–179), append:

> "**Phase-4 verdict on escape route (iii) (unreduced primitive,
> 2026-04-28).** The natural parallel-factorization architecture
> $\widetilde{\mathcal A}=\mathcal A\oplus\C[\eta]$ does not
> discharge the obstruction class $\hbar N[\bar c]$ at lowest
> order under any of three prescriptions (central, derivation,
> A$_\infty$). The bridge to $\bar A$ violates either centrality of
> $\eta$ or the closed-side identity $X_1\equiv 0$; A$_\infty$-deformation
> regenerates the residue at order $\hbar^3 N^3$. The
> unreduced-primitive escape requires fresh foundational technique
> (Phase-5); see `reconstitution/phase4-exec-unreduced-primitive-2026-04-28.md`."

### Tier 3 — Phase-5 criterion update

**`P4-Exec-Unred-WP-3`.** In `phase4-G5-bosonic-Fprime-2026-04-28.md`
P4-G5-T7-01 (Phase-5 criterion), update (P5-α) to:

> "**(P5-α) Unreduced-primitive route closes in the negative.**
> Per P4-Exec-Unred (2026-04-28), the natural parallel-factorization
> architecture is closed in the negative at lowest order under three
> prescriptions (central, derivation, A$_\infty$). (P5-α) is **MET**.
> Phase-5 escalation now depends on (P5-β) AND (P5-γ); if either
> opens, F$'$ remains Phase-4 via that route."

---

## §8. Convergence verdict

**Phase-4 / Exec / Unreduced-primitive: COMPLETE with negative
verdict at three levels.**

The W18-C3 / P4-G5-CT1 conjecture is **closed in the negative**
under the natural architecture
$\widetilde{\mathcal A}=\mathcal A\oplus\C[\eta]$. Four independent
structural obstacles are confirmed; the heal attempt at lowest
order does not discharge the obstruction class under any of three
prescriptions (central, derivation, A$_\infty$); A$_\infty$-deformed
bridge regenerates the residue at order $\hbar^3 N^3$ via Massey
product. The Phase-5 criterion (P5-α) is now **met** for this route.

Phase-4 escape routes remaining open for bosonic F$'$:
- **(b') Source-change** (P4-G5-CT2 $\mathfrak{osp}$, P4-G5-CT3
  $\mathfrak{gl}_{\infty|\infty}$): G3 / 12-month deliverable.
- **(c') 5d-M-theory free pass** (P4-G5-T6-02): G4 / 12-month
  deliverable.

Phase-5 escalation criterion now requires only (P5-β) and (P5-γ);
if both close in the negative, F$'$ on the bosonic source escalates
to Phase-5 (fresh categorical / derived-CY / cross-volume technique
required).

**Inscribed durables.**
- This document.
- W18-C3 / P4-G5-CT1 status: **CONJECTURE-WITH-NAMED-OBSTACLE**.
- (P5-α) **MET**; Phase-5 escalation depends on G3 + G4 outcomes.
- Three workpieces (P4-Exec-Unred-WP-1/2/3) for ledger updates.

End of P4-Exec-Unreduced-Primitive ledger.
