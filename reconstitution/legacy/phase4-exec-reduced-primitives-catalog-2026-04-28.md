# Phase-4 / Exec — Reduced-only chain-level primitives compatible with reduction (P4-G5-M2)

**Date.** 2026-04-28. **Author.** Raeez Lorgat (Phase-4 execution
agent, P4-G5-M2 milestone, follow-up to G5 RELAUNCH-2 closure).
**Lens.** Costello (factorization algebras, BV/BRST, RG locality;
local-to-global compose) primary; Composition (associativity,
coherence, transactionality) secondary.
**Mode.** Proposal-only — no manuscript edits, no commits.
**Schema.** ID prefix `P4-Exec-RedCat-`. Severity 1–5; Status
`valid|partial|invalid`; Confidence high/medium/low.

**Mandate.** Catalog all chain-level primitives
$\bar\eta:\bar A\to\C$ where $\bar A=\C[z_1,z_2]/\C\cdot 1$
satisfying simultaneously
- **(C1)** $\bar\eta$ is $\C$-linear and BV-closed on the reduced
  side (i.e., a chain map in the relevant cochain complex).
- **(C2)** $\bar\eta$ is **natural** under the open-closed
  comparison map: compatible with reduction
  $\pi:\mathfrak h_{\mathrm{poly}}\to\bar A$ and with the boundary
  evaluation $\partial_{\mathrm{bb},N}^{\mathrm{full}}$.
- **(C3)** $\bar\eta$ produces a coboundary in Lie-algebra cohomology
  for the residue $\hbar N[\bar c]$ when paired with the matrix
  probe.

**Inputs read.**
- `reconstitution/phase4-exec-unreduced-primitive-2026-04-28.md`
  (full, 933 lines) — G5 RELAUNCH-2 closure of W18-C3.
- `reconstitution/wave3-W18-thmB-escape-routes-2026-04-28.md`
  (W3-W18-05 lines 625–765, W18-C3 statement lines 916–950).
- `reconstitution/wave3-W15-conditional-theorems-2026-04-28.md`
  (W3-W15-04 lines 679–773; residue $=\hbar N[\bar c]$).
- `reconstitution/phase4-exec-osp-supertrace-2026-04-28.md`
  (chain-level lift $\Lambda^{\Str}$; W22-T1+T2 super-balancing).
- `appendix-unreduced-bv-qme.tex` (full, 179 lines).
- `main.tex` lines 280–470 (`lem:omega-cocycle`,
  `thm:u1-center-anomaly`, `thm:u1-center-anomaly-open`,
  `thm:quantum-classical-anomaly`).

**Independence.** Inputs taken under attack. The deliverable is a
verified catalog of every reduced-only primitive matching (C1)–(C3),
with explicit obstruction-class computations in
$H^1(\mathfrak g, M)$ for the relevant Hamiltonian Lie algebra
$\mathfrak g$ and module $M$.

---

## §0. Executive verdict

**Five candidates tested; ALL fail.** No natural $\bar\eta:\bar A\to\C$
satisfying (C1)–(C3) exists. The dominant obstruction is **the
forced equation $\bar\eta(\{z_1,z_2\}_{\bar A})=\omega(z_1,z_2)=1$**:
since $\{z_1,z_2\}_{\mathfrak h_{\mathrm{poly}}}=1\in\C\cdot 1$
is the kernel of $\pi$, the bracket on $\bar A$ at the pair
$(z_1,z_2)$ vanishes ($\pi(1)=0$), so any candidate primitive must
both vanish at $0\in\bar A$ (linearity) and equal $1$ (cocycle
identity), which is contradictory. This is the same structural
obstacle that closes W18-C3 in the negative on the unreduced side,
restated on the reduced side: there is no reduced-only chain-level
primitive, period.

**Per-candidate verdicts (one line each).**
- **(A)** $\bar\eta(f)=\partial_{z_1^a z_2^b}f|_0$ for $a+b\geq 1$:
  **fails (C3)** at the pair $(z_1,z_2)$ for every $(a,b)$. Either
  the pairing vanishes against $\{z_1,z_2\}_{\bar A}=0$ trivially
  (gives $\bar\eta(0)=0\neq 1$, contradiction) or it depends on a
  basepoint and breaks translation invariance (C2 fails).
  **`P4-Exec-RedCat-V-A`**.
- **(B)** Residue against a meromorphic 1-form $\omega^{\mathrm{res}}$
  on $\bar A$: **fails (C1)** because no meromorphic 1-form on
  $\C[z_1,z_2]$ is BV-closed in the CE differential of $\bar A$ that
  pairs to a non-zero scalar on $\{z_1,z_2\}_{\bar A}=0$. The
  Grothendieck residue is supported on the puncture, but the puncture
  is precisely the constant line killed by $\pi$.
  **`P4-Exec-RedCat-V-B`**.
- **(C)** Pairing of $f$ with a fixed degree-2 cohomology class on the
  formal disk: **fails (C2)** because every non-zero element of
  $H^2(D^2,\C)=0$ (formal disk is contractible) gives the trivial
  pairing; alternatively, an $\Omega^2$-pairing forces $\bar\eta$
  through the Hochschild-to-CE map, which lands in
  $H^2_{\mathrm{Lie}}(\bar A,\C)\ni[\bar c]\neq 0$, not in the
  primitive complex. **`P4-Exec-RedCat-V-C`**.
- **(D)** Supertrace pairing with a Berezinian on the super-stack
  (open-closed coupled): **fails on the bosonic source** because the
  supertrace pairing requires a $\Z/2$-grading not present on
  $\bar A$ alone. On the supertraced source $\Str_{\mathrm{gl}(N|N)}(I)=0$,
  the residue $\hbar N[\bar c]$ is replaced by $\hbar\cdot 0\cdot[\bar c]=0$,
  so the primitive becomes vacuously trivial — but this is **not a
  primitive on $\bar A$**; it is a different theorem on a different
  source. **`P4-Exec-RedCat-V-D`**.
- **(E)** Capelli/Sergeev central-element trace pairing: **fails (C3)**
  because the Capelli central element acts on $\bar A$ as the
  scalar $\hbar N$, which is *exactly* the residue we are trying to
  cancel. Sergeev's central element on $\mathrm{osp}$ acts as $0$,
  but again on a different (super) source, not on bosonic $\bar A$.
  **`P4-Exec-RedCat-V-E`**.

**Dominant obstruction class.** The class
$[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)\cong\C$ is **non-zero**
(`lem:omega-cocycle` in `main.tex`:284–316), and the residue
$\hbar N[\bar c]\in H^1(\mathcal O_{\mathrm{loc}}(\mathcal E_w),
Q+\{I_0,-\})$ is its image under the contact-multiplication-by-
$\gamma_{\mathbf 1}$ functor. Its preimage under the differential
$\delta_{\mathrm{CE}}:C^1(\bar A,\C)\to C^2(\bar A,\C)$
**does not exist** in $C^1$, because $C^1(\bar A,\C)=
\Hom_\C(\bar A,\C)$ has no element pairing to $1$ on the bracket
$\{z_1,z_2\}_{\bar A}=0$. **The Theorem G residue $\hbar N[\bar c]$
is genuinely cohomologically non-trivial.**

**Bottom line.** The G5 RELAUNCH-2 negative closure of W18-C3 was
not contingent on the unreduced architecture; it reflects a
structural obstruction *intrinsic to the reduced source*. No
chain-level primitive on $\bar A$ exists in any of the five natural
candidate forms. The Theorem G residue is genuinely
cohomologically non-trivial. Any positive Phase-4 route requires
a **change of source** (W22-T1+T2 super-balancing on $\mathrm{gl}(N|N)$;
$\mathrm{osp}$ extensions in P4-G3-T-A1) or a **change of theorem**
(5d-M-theory free pass; G4 milestone).

---

## §1. Candidate (A) — Higher derivative at the origin

### `P4-Exec-RedCat-A-01` — Definition and (C1) test

**Severity 4. Status invalid (fails C2 and C3). Confidence high.**

**Setup.** For fixed multi-index $(a,b)$ with $a+b\geq 1$, define
\[
   \bar\eta_{a,b}(f)=\frac{\partial^{a+b}f}{\partial z_1^a\partial z_2^b}\bigg|_{(0,0)}.
\]
This is well-defined on $\bar A=\C[z_1,z_2]/\C\cdot 1$ because the
derivative of a constant vanishes (so $\bar\eta_{a,b}(1)=0$
automatically; the pullback to $\C[z_1,z_2]$ vanishes on $\C\cdot 1$).
Candidate (A) is the family of all such $\bar\eta_{a,b}$ for
$a+b\geq 1$.

**(C1) BV-closedness on the reduced side.** $\bar\eta_{a,b}$ is
$\C$-linear by construction. BV-closedness in the CE complex of
$\bar A$ requires
$\delta_{\mathrm{CE}}\bar\eta_{a,b}\in C^2_{\mathrm{Lie}}(\bar A,\C)$
to vanish, where
$(\delta_{\mathrm{CE}}\bar\eta_{a,b})(f,g)=\bar\eta_{a,b}(\{f,g\}_{\bar A})$.
This is **not** zero in general: e.g., for $(a,b)=(0,0)$ formally
we get the constant Taylor coefficient (which is $-\eta$, the
unreduced primitive), and we recover the Lie 2-cocycle $\omega$.
For $(a,b)$ with $a+b\geq 1$, the differential
$(\delta_{\mathrm{CE}}\bar\eta_{a,b})(f,g)$ is a non-zero element
of $C^2$ in general; we are *trying* to find one for which it
equals $\omega$ (the residue cocycle).

So (C1) reads: $\bar\eta_{a,b}$ is itself a candidate primitive of
$\omega$, i.e., we ask
\[
   \bar\eta_{a,b}(\{f,g\}_{\bar A})\stackrel{?}{=}\omega(f,g)
   =[\{f,g\}_{\mathfrak h_{\mathrm{poly}}}]_0
\]
for all $f,g\in\bar A$. The right-hand side is non-zero only when
$\{f,g\}_{\mathfrak h_{\mathrm{poly}}}\in\C\cdot 1\subset\mathfrak h_{\mathrm{poly}}$,
which forces the bracket to land in the kernel of $\pi$.

**Evaluation at $f=z_1$, $g=z_2$.** $\{z_1,z_2\}_{\mathfrak h_{\mathrm{poly}}}=1$,
hence $\omega(z_1,z_2)=[1]_0=1$. On $\bar A$, $\pi(\{z_1,z_2\})=
\pi(1)=0$, so the LHS is $\bar\eta_{a,b}(0)=0$ by linearity.

**Contradiction.** $0\neq 1$. **(C1) fails for every $(a,b)$ with
$a+b\geq 1$.**

**`P4-Exec-RedCat-A-01` adjudication.** The candidate is
*structurally orthogonal* to the residue: any $\bar\eta_{a,b}$
defined at the origin has $\bar\eta_{a,b}|_{\C\cdot 1}=0$ on the
unreduced lift, so the primitive equation can never be satisfied
on the bracket $\{z_1,z_2\}=1\in\ker\pi$. This is a re-statement
of `prop:app-scalar-contact-qme-class` proof's obstruction.

### `P4-Exec-RedCat-A-02` — Translation invariance (C2)

**Severity 3. Status invalid (fails C2 separately). Confidence high.**

**Statement.** Even setting (C1) aside, $\bar\eta_{a,b}$ depends
on the choice of basepoint $(0,0)\in\C^2$. Affine translations
$T_v:z\mapsto z+v$ act on $\C[z_1,z_2]$ by ring automorphisms,
and conjugating
$\bar\eta_{a,b}\circ T_v(f)=\partial^{a+b}f|_{(v_1,v_2)}/\partial z_1^a\partial z_2^b$
gives a different functional. The Poisson bracket on
$\mathfrak h_{\mathrm{poly}}$ is translation-invariant, so the
residue cocycle $\omega$ is translation-invariant; but
$\bar\eta_{a,b}$ is not. Composition with the boundary evaluation
$\partial_{\mathrm{bb},N}^{\mathrm{full}}:\C[z_1,z_2]\to
\C[\mathfrak{gl}_N^2]^{GL_N}$ would force a basepoint dependence
in the open-side observables, breaking $GL_N$-equivariance.

**Per-loop check.** At one loop, the propagator on the matrix
brane is the heat-kernel parametrix
$\Delta_{\mathrm{sK}}=\sum_a T^aT_a$, which is translation-invariant
in the $\mathfrak{gl}_N$ source. Pairing against $\bar\eta_{a,b}$
introduces a basepoint that is not respected by the propagator.
Hence the local-functional cocycle
$\Lambda(\bar\eta_{a,b})=\bar\eta_{a,b}\cdot\gamma_{\mathbf 1}\cdot a(t)b(t)$
is *not* invariant under the (A1)-shift symmetry of the regulator
class. (A1) requires shift-invariance in the $\R$-direction; the
extension to translation invariance in the $\C^2$-direction is
the next layer up, and $\bar\eta_{a,b}$ violates it.

**Adjudication.** Even if some hypothetical $\bar\eta_{a,b}$ could
satisfy (C1) on a non-commutative target, (C2) would still fail
because translation invariance on $\C^2$ is required by
factorization-algebra naturality (Costello-Gwilliam Vol II §11
emphasizes locality, which in particular requires translation
invariance for shift-symmetric BV theories).

### `P4-Exec-RedCat-A-03` — Composition test: do candidates of type (A) glue across opens?

**Severity 3. Status invalid (no cover-glueing). Confidence high.**

**Composition lens.** A factorization-algebra primitive must
restrict consistently to opens $U\subset\R^2\times\C^2$ and glue
via Mayer-Vietoris. The basepoint $0\in\C^2$ does not lift to
multiple opens: the formal disk $\widehat{\C^2}_0$ is one open;
on a translated copy $\widehat{\C^2}_v$ the candidate
$\bar\eta_{a,b}$ pulls back to $\bar\eta_{a,b}\circ T_{-v}$, a
different functional. The Čech complex of the cover by translates
detects this: $\bar\eta_{a,b}|_{U_0}-\bar\eta_{a,b}|_{U_v}=
\bar\eta_{a,b}-\bar\eta_{a,b}\circ T_{-v}\neq 0$ in
$C^1_{\mathrm{Cech}}$, so the candidate is not a global section.

**Costello locality.** The RG flow of a basepoint-dependent
functional is not locally constructible: the heat-kernel evolution
of $\bar\eta_{a,b}$ involves the full $\C^2$-Laplacian, which is
not local to the basepoint. Any Costello-RG-renormalized version
of $\bar\eta_{a,b}$ would smear it over a length scale $\sqrt t$
proportional to the heat-kernel time; the point-supported
distribution at $0$ is not in the RG-stable class.

**Adjudication.** Composition / Mayer-Vietoris fails. Candidate (A)
is not a factorization-algebra natural primitive in any concrete
form.

### `P4-Exec-RedCat-V-A` — Verdict

**Verdict.** Candidate (A) **invalid** for all $(a,b)$ with
$a+b\geq 1$.
- **(C1) fails** at $(z_1,z_2)$: $0\neq 1$.
- **(C2) fails** by translation non-invariance.
- **(C3) cannot even be tested** since (C1) already fails.
- **Composition** fails by Mayer-Vietoris non-glueability.

**Cohomology-class computation (§6 entry).** The image
$\bar\eta_{a,b}$ in $C^1_{\mathrm{Lie}}(\bar A,\C)\subset C^\bullet$
is a non-zero element, but its CE-coboundary is *not* the cocycle
$\omega$; rather, it is some other 2-cocycle (whose computation
depends on $(a,b)$). The class $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$
is one-dimensional (Theorem `thm:u1-center-anomaly` proof,
`main.tex`:334–352), spanned by $\omega$. The image
$\delta_{\mathrm{CE}}\bar\eta_{a,b}$ is in a *different* cohomology
class (the trivial class, in fact, since $\bar\eta_{a,b}$ exists),
not $[\bar c]$.

**Compatibility with $\Lambda^{\Str}$ super-balancing (W22-T1+T2).**
The regulator $\Lambda^{\Str}$ acts on $\bar A^{\mathrm{super}}=
\C[z_1,z_2;\theta_1,\theta_2]/\C\cdot 1$ as parity-equivariant smoothing.
On the bosonic restriction $\bar A\hookrightarrow\bar A^{\mathrm{super}}$,
$\Lambda^{\Str}|_{\bar A}=\Lambda^{\mathrm{ord}}|_{\bar A}$, so
$\bar\eta_{a,b}$ inherits no parity weight. The basepoint at $(0,0)$
is parity-invariant; super-balancing does not repair the
translation-non-invariance of (A). $\bar\eta_{a,b}$ remains
basepoint-dependent on the super source, hence still violates (C2).
**Compatibility: vacuous; super-balancing does not rescue (A).**

---

## §2. Candidate (B) — Meromorphic 1-form residue

### `P4-Exec-RedCat-B-01` — Definition and (C1) test

**Severity 4. Status invalid (fails C1 in any geometric setup).
Confidence high.**

**Setup.** Let $\omega^{\mathrm{res}}=h(z_1,z_2)dz_1+k(z_1,z_2)dz_2$
be a meromorphic 1-form on $\C^2$, possibly with poles on a divisor
$D\subset\C^2$. Define
\[
   \bar\eta^{\mathrm{res}}(f)=\mathrm{Res}_{D}(f\cdot\omega^{\mathrm{res}})
   =\frac{1}{2\pi i}\oint_{\partial T(D)}f\cdot\omega^{\mathrm{res}}
\]
where $T(D)$ is a tubular neighborhood. Two natural choices:
- (B1) $\omega^{\mathrm{res}}=dz_1\wedge dz_2/(z_1z_2)$ — the
  punctured-disk pairing at $D=\{z_1z_2=0\}$.
- (B2) $\omega^{\mathrm{res}}=dz_1/z_1+dz_2/z_2$ — the dual log-form.
- (B3) $\omega^{\mathrm{res}}=dz_1\wedge dz_2/(z_1+z_2)$ — pairing
  against a generic transverse slice.

**Domain consideration.** The candidate $\bar\eta^{\mathrm{res}}$
acts on $f\in\C[z_1,z_2]$ by extracting the residue. For
polynomial $f$, the residue at a polynomial pole is computed as a
finite Laurent expansion coefficient; since $f$ is polynomial,
the residue is *exactly* a particular Taylor coefficient of
$f$ (specifically, the coefficient of $z_1^a z_2^b$ matching the
pole order). So $\bar\eta^{\mathrm{res}}$ is a **finite linear
combination of higher-derivative-at-origin functionals**, i.e., it
reduces to candidate (A).

**Concrete reduction.** For (B1), the residue against
$dz_1\wedge dz_2/(z_1z_2)$ extracts the constant Taylor coefficient
$[f]_{(0,0)}=f(0,0)$. But this is **exactly $-\eta(f)$**, the
unreduced primitive, which does not descend to $\bar A$.

For (B2), the residue against $dz_1/z_1+dz_2/z_2$ extracts the
coefficient sum $[f]_{(0,0)}\cdot 2$ on $\C[z_1,z_2]$, again the
unreduced primitive (up to a factor of $2$).

For (B3), the residue against $dz_1\wedge dz_2/(z_1+z_2)$ extracts
the integral $\int_{|z_1+z_2|=\epsilon}f(z_1,z_2)dz_1dz_2/(z_1+z_2)$,
which is the constant Taylor coefficient on the line $z_1+z_2=0$,
again equivalent to the unreduced primitive.

**Conclusion: every meromorphic-residue candidate (B) reduces to
candidate (A) at $(a,b)=(0,0)$ — the unreduced primitive.** Since
the unreduced primitive does not descend to $\bar A$ (T1 of the
unreduced report; `prop:app-scalar-contact-qme-class`), no candidate
(B) descends either. **(C1) fails — $\bar\eta^{\mathrm{res}}$ is
ill-defined on $\bar A$.**

**`P4-Exec-RedCat-B-01` adjudication.** Meromorphic residue is the
*structural origin* of the unreduced primitive $\eta(f)=-[f]_0$: the
constant Taylor coefficient is the residue at the origin against
$dz_1\wedge dz_2/(z_1z_2)$. Repackaging as a meromorphic-residue
form does not bypass the descent obstruction.

### `P4-Exec-RedCat-B-02` — Higher-pole and twisted residue extensions

**Severity 3. Status invalid (twisted forms also reduce to (A)).
Confidence high.**

**Higher-pole extension.** Consider
$\omega^{\mathrm{res}}_{(p,q)}=dz_1\wedge dz_2/(z_1^p z_2^q)$ for
$p,q\geq 1$. The residue extracts the coefficient of
$z_1^{p-1}z_2^{q-1}$ in the Taylor expansion. For $p+q\geq 2$,
this lands in the *non-constant* Taylor coefficients, and so
*does descend to $\bar A$* (the constant line is in the kernel
of $\pi$, and the higher Taylor coefficients survive).

**Hope: $\bar\eta^{\mathrm{res}}_{(p,q)}$ is a primitive of $\omega$
on $\bar A$ for some $(p,q)$ with $p+q\geq 2$.** Test at $(p,q)=
(1,1)$, giving $\bar\eta(f)=$ coefficient of $z_1^0z_2^0$ in $f/(z_1z_2)$
= coefficient of $z_1z_2$ in $f$ = $\partial_{z_1}\partial_{z_2}f|_0$.
This is candidate (A) at $(a,b)=(1,1)$: $\bar\eta_{1,1}(f)=
\partial_{z_1}\partial_{z_2}f|_0$.

**Apply (C1) test.** $\bar\eta_{1,1}(\{z_1,z_2\}_{\bar A})=
\bar\eta_{1,1}(0)=0\neq 1=\omega(z_1,z_2)$. **(C1) fails** at
this pair, exactly as in §1.

**Twisted residue with weight.** Try
$\omega^{\mathrm{res,w}}=dz_1\wedge dz_2\cdot e^{-w(z_1^2+z_2^2)/2}/(z_1z_2)$
for $w>0$ (Gaussian-twisted). The residue against this becomes
a Gaussian-weighted Taylor coefficient
$\int_{\C^2}f(z)e^{-w|z|^2/2}d^2z$ (after deforming the contour),
which is the Bargmann-Fock pairing. On polynomial $f=z_1^a z_2^b$,
this gives $a!b!w^{-(a+b+1)}$ at the origin moment, a non-zero
multiple of the constant.

**Test (C1) for the Bargmann pairing.** On $\bar A$, $f=1$ is
killed; for $f=z_1^k z_2^l$ with $k+l\geq 1$, the Bargmann pairing
gives $k!l!w^{-(k+l+1)}$. Apply to $\{z_1,z_2\}_{\bar A}=0$: get
$0\neq 1$. **(C1) fails again.**

**Structural reason.** The fundamental obstruction is that
$\{z_1,z_2\}_{\mathfrak h_{\mathrm{poly}}}=1$ projects to $0\in\bar A$,
so any *linear* functional $\bar\eta:\bar A\to\C$ has
$\bar\eta(\{z_1,z_2\}_{\bar A})=\bar\eta(0)=0$, but the cocycle
identity demands this equal $\omega(z_1,z_2)=1$. **No linear
functional on $\bar A$ — meromorphic, smooth, distributional, or
otherwise — can satisfy $\bar\eta(0)=1$.**

**`P4-Exec-RedCat-B-02` adjudication.** The obstruction is independent
of the regularity class of $\omega^{\mathrm{res}}$. Even smooth or
distributional residues fail (C1) by linearity at $0$.

### `P4-Exec-RedCat-V-B` — Verdict

**Verdict.** Candidate (B) **invalid** for every choice of
$\omega^{\mathrm{res}}$ — meromorphic, twisted, or distributional.
- **(C1) fails universally** by the linearity obstruction at $0\in\bar A$.
- The candidate either reduces to (A) or to a Bargmann-Fock pairing,
  both of which fail (C1).
- **Composition** test irrelevant — (C1) fails first.

**Cohomology-class computation.** Every $\bar\eta^{\mathrm{res}}$
is in $C^1_{\mathrm{Lie}}(\bar A,\C)$, and its differential
$\delta\bar\eta^{\mathrm{res}}$ is a *different* 2-cocycle (one
that *does* lift), but **not $\omega$**. The class
$[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$ is therefore
**not in the image of $\delta_{\mathrm{CE}}|_{C^1}$**, i.e., it
is a genuine non-trivial class. **Confirmed: $[\bar c]\neq 0$.**

**Compatibility with $\Lambda^{\Str}$ super-balancing (W22-T1+T2).**
A meromorphic 1-form on $\C^2$ does not naturally extend to a
parity-equivariant form on $\C^{2|2}$ without choosing a fermion
direction. The Berezinian $dz_1dz_2d\theta_1d\theta_2$ is the
natural super-equivariant top form; its $\theta$-projection (Candidate D)
trivializes on the bosonic restriction. Restricted to bosonic input,
$\bar\eta^{\mathrm{res}}$ is parity-trivial. **Super-balancing does
not lift the linearity-at-$0$ obstruction; (B) remains invalid on
both bosonic $\bar A$ and on the bosonic sub-sector of
$\bar A^{\mathrm{super}}$.**

---

## §3. Candidate (C) — Pairing with degree-2 cohomology class on the formal disk

### `P4-Exec-RedCat-C-01` — Definition and (C1) test

**Severity 4. Status invalid (fails C1; cohomology of disk
trivial). Confidence high.**

**Setup.** The formal disk $\widehat D^2=\Spf\C[[z_1,z_2]]$ has
trivial topology: $H^\bullet(\widehat D^2,\C)=\C$ concentrated in
degree 0. The polynomial sub-algebra $\bar A=\C[z_1,z_2]/\C\cdot 1$
inherits the same trivial cohomology: $H^\bullet(\bar A,\C)=\C$
in degree $0$, $0$ elsewhere (as a commutative $\C$-algebra
augmented at $0$).

**Pairing with a degree-2 class.** "Pair $f$ with a degree-2 class
$[\theta]\in H^2(\widehat D^2,\C)$" requires $[\theta]\neq 0$,
which forces us to a *modified* cohomology theory:
- **(C-i)** Hochschild cohomology $HH^\bullet(\bar A,\bar A)$, where
  $HH^2$ is non-zero (it carries the deformation classes).
- **(C-ii)** Lie-algebra cohomology $H^\bullet_{\mathrm{Lie}}(\bar A,\C)$,
  where $H^2_{\mathrm{Lie}}=\C\cdot[\bar c]$ (one-dimensional, by
  Theorem `thm:u1-center-anomaly`).
- **(C-iii)** Cyclic cohomology $HC^\bullet(\bar A)$, where
  $HC^2$ contains the relative trace classes.

**Reduction to (C-ii).** The $\Z/2$-graded cyclic class agrees
with the Lie-algebra class $[\bar c]$ (Loday, *Cyclic Homology*,
1998, §3.3.2: $HC^2_\lambda(\C[z_1,z_2])\cong H^2_{\mathrm{Lie}}(\bar A,\C)$
in this small case). Pairing $f$ against $[\bar c]$ via the
canonical $C^1\otimes C^2\to C^3$ wedge gives:
\[
   \bar\eta^{(C)}(f)=\langle f,[\bar c]\rangle\in C^3_{\mathrm{Lie}},
\]
which is *not* a scalar — it is a 3-cocycle. So the pairing
does **not** produce a $\C$-valued primitive.

**Reduction to scalar.** To get a scalar from $\langle f,[\bar c]\rangle$,
one must contract against a degree-$(-3)$ cycle. The minimal such
cycle on $\bar A$ is the fundamental class $[\bar A]$ in cyclic
*homology* $HC_3(\bar A)$, but $HC_3(\bar A)=0$ on the polynomial
disk (no top-dimensional class without compactification).

**Conclusion.** No non-trivial pairing $\bar A\to\C$ arises from a
degree-2 cohomology class on the formal disk. The pairing either
gives zero (C-i, C-iii on the polynomial disk) or gives a 3-cocycle
not a scalar (C-ii).

**`P4-Exec-RedCat-C-01` adjudication.** Candidate (C) **fails (C1)**:
no scalar primitive arises from a degree-2 pairing on the formal
disk. The closest analogue is the cup product
$[\bar c]\cup[\bar c]\in H^4_{\mathrm{Lie}}(\bar A,\C)$, which
*does* live in cohomology but is in the wrong degree.

### `P4-Exec-RedCat-C-02` — Hochschild-to-CE comparison

**Severity 3. Status invalid (Hochschild route gives a different
class). Confidence medium.**

**Setup.** Hochschild cohomology $HH^\bullet(\bar A,\bar A)$ has
$HH^2(\bar A,\bar A)=\Hom(\Lambda^2\bar A,\bar A)$ (skew-symmetric
maps) for the polynomial $\bar A$; the universal Maurer-Cartan
class is the bracket $\{-,-\}$ itself.

**HKR isomorphism.** Hochschild-Kostant-Rosenberg gives
$HH^\bullet(\C[z_1,z_2],\C[z_1,z_2])\cong\Omega^\bullet(\C^2)$;
restricting to $\bar A=\C[z_1,z_2]/\C\cdot 1$ gives
$HH^\bullet(\bar A,\bar A)\cong\bar A\otimes\Omega^\bullet$ in
each degree. The "degree-2 class" is then a 2-form, e.g.,
$dz_1\wedge dz_2$.

**Pairing via integration.** Pair $f$ against $dz_1\wedge dz_2$ via
$\int_{\C^2}f\,dz_1dz_2$: this diverges on polynomial $f$ (no
compact support). Pair against the Berezin integral $\int^{\rm Ber}$:
on the bosonic side this requires a fermionic completion (going
to candidate D). Pair against the localized integral
$\int_{|z|\leq R}f\,dz_1dz_2$: gives a polynomial in $R$, not a
scalar in the limit.

**Holomorphic regularization.** The most natural regulated pairing
is the Bergman/Bargmann pairing
$\int_{\C^2}f\,e^{-|z|^2/2}d^2z$ (Bergman kernel). For
$f=z_1^a z_2^b$, this gives $a!b!\cdot 2\pi$. Restriction to
$\bar A$: vanishes on $f=1$ (after subtracting), gives $1$ on
$f=z_1z_2$ etc. So this is the Bargmann-Fock pairing, identical
to candidate (B) at the Gaussian-weighted residue.

**(C1) test.** Apply to $\{z_1,z_2\}_{\bar A}=0$: get
$\bar\eta^{\mathrm{Berg}}(0)=0\neq 1$. **(C1) fails.**

### `P4-Exec-RedCat-V-C` — Verdict

**Verdict.** Candidate (C) **invalid**.
- The formal disk has trivial topology, so any "degree-2 class
  pairing" must be in a derived cohomology theory (Hochschild,
  cyclic, Lie-algebra), and then reduces to candidates (A)/(B) or
  to the *cup-square* $[\bar c]\cup[\bar c]$, which lives in
  degree 4, not degree 1.
- **(C1) fails** in every concrete realization.
- **Composition** test irrelevant.

**Cohomology-class computation.** $H^2(\widehat D^2,\C)=0$
geometrically. The Lie-algebra version
$H^2_{\mathrm{Lie}}(\bar A,\C)=\C\cdot[\bar c]$, but pairing with
this class lands in degree 3 not degree 1, so it does not produce
a primitive in $C^1$. **Confirmed: no (C)-type primitive exists.**

**Compatibility with $\Lambda^{\Str}$ super-balancing (W22-T1+T2).**
The HKR/Hochschild route on $\bar A^{\mathrm{super}}$ extends to
$HH^\bullet(\bar A^{\mathrm{super}})\cong\bar A^{\mathrm{super}}\otimes
\Omega^\bullet_{\C^{2|2}}$ with the super-Berezinian top form. Pairing
against $\mathrm{Ber}=dz_1dz_2d\theta_1d\theta_2$ is exactly Candidate
(D); on the bosonic sub-algebra it trivializes. The cup-square
$[\bar c]\cup[\bar c]$ lifts to $[\Lambda^{\Str}\bar c]^{\cup 2}$ on
the super source and is *also non-zero* in $H^4_{\mathrm{Lie}}
(\bar A^{\mathrm{super}},\C)$ before the supertrace coefficient
collapses it; the parity weighting from $\Lambda^{\Str}$ does not
move this class into the primitive complex $C^1$. **Super-balancing
does not lift (C); the degree mismatch persists.**

---

## §4. Candidate (D) — Supertrace pairing with Berezinian on the super-stack

### `P4-Exec-RedCat-D-01` — Definition and (C1) test

**Severity 4. Status: changes the source (escapes the bosonic
problem), but does NOT define a primitive on $\bar A$.
Confidence high.**

**Setup.** Replace $\mathfrak{gl}_N$ by the super-stack
$\mathfrak{gl}(N|N)$ with the supertrace $\Str$. The Hamiltonian
source is now $\bar A^{\mathrm{super}}=\C[z_1,z_2;\theta_1,\theta_2]/(\C\cdot 1)$
where $\theta_i$ are odd; the "Berezinian" is
$\mathrm{Ber}=dz_1\,dz_2\,d\theta_1\,d\theta_2$ with the Berezin
integral conventions
$\int^{\rm Ber}\theta_1\theta_2\,dz_1dz_2=1$ on the Grassmann
generators.

Define
\[
   \bar\eta^{\mathrm{Ber}}(f)=\int^{\rm Ber}f(z,\theta)\cdot\mathrm{Ber}.
\]

**Bosonic projection.** For $f\in\bar A=\C[z_1,z_2]/\C\cdot 1$
(no $\theta$-dependence), the Berezin integral picks out the
$\theta_1\theta_2$-coefficient of $f$, which is **zero** since
$f$ has no $\theta$. So $\bar\eta^{\mathrm{Ber}}(f)=0$ for all
$f\in\bar A$. **(C1) is satisfied trivially: the differential
$\delta\bar\eta^{\mathrm{Ber}}=0$, so it is BV-closed.**

**(C3) test.** Apply $\bar\eta^{\mathrm{Ber}}$ to the residue
cocycle $\omega$ on $\bar A$: $\delta\bar\eta^{\mathrm{Ber}}(f,g)=
\bar\eta^{\mathrm{Ber}}(\{f,g\}_{\bar A})=0$ by the projection
above. The residue cocycle $\omega$ has $\omega(z_1,z_2)=1\neq 0$,
so $\delta\bar\eta^{\mathrm{Ber}}\neq\omega$. **(C3) fails: the
candidate is identically zero on bosonic input, hence does not
discharge the residue.**

**`P4-Exec-RedCat-D-01` adjudication.** On the bosonic source
$\bar A$, the Berezin integral pairing trivializes (zero output).
This is the wrong source.

### `P4-Exec-RedCat-D-02` — Super-stacked source: changes the residue

**Severity 4. Status: *not* a reduced primitive on $\bar A$;
discharges the residue on $\bar A^{\mathrm{super}}$. Confidence high.**

**Replace the source.** Work on $\bar A^{\mathrm{super}}=
\C[z_1,z_2;\theta_1,\theta_2]/(\C\cdot 1)$. The residue cocycle
on the super-stack is computed by `appendix-unreduced-bv-qme.tex`:106–107
in the unreduced form:
\[
   \mathrm{Ob}_{\mathrm{sc}}^{\mathrm{super}}=
   \hbar\Str_{\mathrm{gl}(N|N)}(I)\omega(f,g)\int_\R a(t)b(t)\,dt
   =\hbar\cdot 0\cdot\omega(f,g)\cdot(\ldots)=0.
\]
**The residue itself vanishes** on the super-balanced source; no
primitive needed.

**This is W22-T1+T2** (`reconstitution/phase4-exec-osp-supertrace-2026-04-28.md`:33–67).
The supertrace coefficient $\Str_{\mathrm{gl}(N|N)}(I)=N-N=0$ kills
the residue at the *coefficient level*, so the chain-level lift
$\Lambda^{\mathrm{Str}}(\omega)$ is well-defined and BV-closed, and
the residue is zero (not merely a coboundary).

**Critical distinction.** On $\bar A^{\mathrm{super}}$, the residue
is *zero*; no primitive is required. On $\bar A$ (bosonic), the
residue is $\hbar N[\bar c]\neq 0$, and no primitive exists.
Candidate (D) **does not** provide a primitive on $\bar A$; it
**replaces $\bar A$ with $\bar A^{\mathrm{super}}$** and observes
that the new residue is zero.

**Composition test.** The bridge functor between $\bar A$ and
$\bar A^{\mathrm{super}}$ is *not* a primitive map; it is a
*source replacement*. The functoriality requirement (C2) is
violated at the level of the source: there is no natural
$\bar\eta^{(D)}:\bar A\to\C$ induced by $\bar\eta^{\mathrm{Ber}}$
on $\bar A^{\mathrm{super}}$. The composition
$\bar A\hookrightarrow\bar A^{\mathrm{super}}\xrightarrow{\bar\eta^{\mathrm{Ber}}}\C$
gives identically zero on $\bar A$.

**`P4-Exec-RedCat-D-02` adjudication.** Candidate (D) does not
provide a reduced-only primitive on $\bar A$. It is a *change of
source*, which is the W22-T1+T2 escape route, not a reduced
primitive.

### `P4-Exec-RedCat-V-D` — Verdict

**Verdict.** Candidate (D) **invalid as a reduced-only primitive**.
- Bosonic projection trivializes: $\bar\eta^{\mathrm{Ber}}(f)=0$
  for $f\in\bar A$.
- Super-source replacement: discharges the residue by changing the
  coefficient $N\to\Str(I)=0$, but this is W22-T1+T2, not a
  primitive on $\bar A$.
- **(C1)** trivially satisfied; **(C2) fails** (no natural map
  $\bar A\to\C$); **(C3) fails** on $\bar A$.

**Compatibility with $\Lambda^{\mathrm{Str}}$ super-balancing.**
The super-balanced regulator $\Lambda^{\mathrm{Str}}$ is naturally
parity-equivariant on $\bar A^{\mathrm{super}}$; the bosonic
restriction is parity-trivial (all even), so $\Lambda^{\mathrm{Str}}|_{\bar A}=
\Lambda^{\mathrm{ord}}|_{\bar A}$. The super-balancing does not
provide a non-trivial parity weight on the bosonic primitive.
**Parity weighting does not survive the bosonic restriction.**

**Cohomology-class computation.** On $\bar A^{\mathrm{super}}$,
the residue class is $\hbar\Str(I)\cdot[\bar c]=0$. On $\bar A$,
the residue class remains $\hbar N[\bar c]\neq 0$. The candidate
(D) primitive $\bar\eta^{\mathrm{Ber}}|_{\bar A}=0$ has zero
differential, so it cannot be a primitive of $\hbar N[\bar c]$
on $\bar A$.

---

## §5. Candidate (E) — Capelli/Sergeev central-element trace pairing

### `P4-Exec-RedCat-E-01` — Definition and (C3) test on Capelli

**Severity 4. Status invalid (the Capelli central element *is*
the residue; pairing with it is circular). Confidence high.**

**Setup.** The Capelli central element $C_\hbar\in U_\hbar(\bar A)$
acts on the trace algebra $\C[\mathfrak{gl}_N^2]^{GL_N}$ by the
scalar $\hbar N$, per Theorem `thm:quantum-classical-anomaly`
(`main.tex`:412–464). Define
\[
   \bar\eta^{\mathrm{Cap}}(f)=\langle f,C_\hbar\rangle_{\mathrm{trace}}=
   \mathrm{Tr}(f(\phi_1,\phi_2))/(\hbar N),
\]
the Capelli-normalized boundary trace.

**Boundary evaluation.** On $\bar A$, the boundary evaluation is
$\partial_{\mathrm{bb},N}^{\mathrm{full}}(f)=\mathrm{Tr}\,f(\phi_1,\phi_2)$.
Dividing by $\hbar N$ gives the Capelli-renormalized trace, which
is a candidate primitive — by Theorem
`thm:quantum-classical-anomaly`, the Capelli relation
$YX-XY=\hbar N$ on the trace generators encodes the residue.

**(C1) test.** Compute $\delta\bar\eta^{\mathrm{Cap}}(f,g)=
\bar\eta^{\mathrm{Cap}}(\{f,g\}_{\bar A})$. By the Capelli
identity:
\[
   \mathrm{Tr}(\{f,g\}_{\bar A}(\phi_1,\phi_2))=\hbar N\cdot
   \omega(f,g)+\text{higher Moyal corrections}.
\]
The leading $\hbar^1$ coefficient is $\hbar N\omega(f,g)$, exactly
the residue. So
$\delta\bar\eta^{\mathrm{Cap}}(f,g)=\omega(f,g)$ at order $\hbar^0$.

**Wait — this looks like a primitive at first glance!** Let us
check (C2) and the chain-level structure.

**(C2) Naturality with $\partial_{\mathrm{bb},N}^{\mathrm{full}}$.**
The map $\bar\eta^{\mathrm{Cap}}$ factors through the boundary
evaluation: $\bar\eta^{\mathrm{Cap}}=\mathrm{Tr}/(\hbar N)\circ
\partial_{\mathrm{bb},N}^{\mathrm{full}}$. So far, compatibility
with the boundary evaluation is *automatic*.

**The trap: the residue lives in BV cohomology, not Lie cohomology.**
$\bar\eta^{\mathrm{Cap}}$ as defined above is a *boundary-trace*
pairing, not a *bulk* primitive. It lives in
$\C[\mathfrak{gl}_N^2]^{GL_N}$, not in $C^1_{\mathrm{Lie}}(\bar A,\C)$.
The pullback $\bar\eta^{\mathrm{Cap}}\circ\partial_{\mathrm{bb},N}^{\mathrm{full}}$
is a functional on $\bar A$, but its differential is *not* the
CE differential — it is the Hamiltonian-reduction differential,
which annihilates the constant trace $\mathrm{Tr}(I)/(\hbar N)=
1/\hbar$.

**Concrete contradiction.** Apply $\bar\eta^{\mathrm{Cap}}\circ\pi$
to $1\in\mathfrak h_{\mathrm{poly}}$: get
$\mathrm{Tr}(I)/(\hbar N)=1/\hbar$. So $\bar\eta^{\mathrm{Cap}}(\pi(1))=
\bar\eta^{\mathrm{Cap}}(0)=1/\hbar$ via the trace. But linearity
demands $\bar\eta^{\mathrm{Cap}}(0)=0$. **Contradiction at the
constant Hamiltonian: the Capelli pairing requires the trace of
the identity, which is $N$, not $0$ — and after dividing by
$\hbar N$, gives $1/\hbar$ on the constant.**

**`P4-Exec-RedCat-E-01` adjudication.** The Capelli central element
$C_\hbar$ acts as $\hbar N$ on the constant Hamiltonian $1$, so the
pairing $f\mapsto C_\hbar(f)/(\hbar N)$ gives $1$ on $f=1$, which
*does not vanish on $\C\cdot 1=\ker\pi$*. Hence the pairing does
**not descend to $\bar A$**. This is the same descent obstruction
as the unreduced primitive $\eta$: candidate (E) is structurally
identical to candidate (A) at $(a,b)=(0,0)$, the unreduced
primitive in disguise.

### `P4-Exec-RedCat-E-02` — Sergeev central element on the super source

**Severity 3. Status: discharges on super source, not on $\bar A$.
Confidence high.**

**Sergeev central element.** On $U(\mathfrak{osp}(2N|2N))$, the
Sergeev central element acts on the brane Hilbert space by the
scalar $\hbar\Str_{\mathrm{osp}}(I)=\hbar\cdot 0=0$ (cf.
`reconstitution/phase4-exec-osp-supertrace-2026-04-28.md`:36–67).
The analogous pairing $\bar\eta^{\mathrm{Sergeev}}$ would give $0$
on $f=1$, but again does not satisfy (C1) on $\bar A$ since the
underlying source is no longer bosonic.

**On the bosonic restriction.** Restricting Sergeev to $\bar A$
(forgetting the super structure) reduces to the Capelli central
element with the bosonic dimension $N$, which equals $\hbar N$.
**Same obstruction as (E1).**

**Capelli/Sergeev synthesis.** The two central elements differ in
their source ($\mathfrak{gl}_N$ vs $\mathfrak{osp}(2N|2N)$) and
their coefficient ($\hbar N$ vs $0$), but on $\bar A$ both reduce
to the bosonic $\hbar N$. **Neither produces a primitive on
$\bar A$**; both are source-change escapes.

### `P4-Exec-RedCat-V-E` — Verdict

**Verdict.** Candidate (E) **invalid as a reduced-only primitive**.
- The Capelli pairing equals $\hbar N$ on $f=1$, not $0$, so it
  does not descend to $\bar A$. Same obstruction as candidate (A)
  at $(a,b)=(0,0)$.
- The Sergeev pairing is identical on the bosonic restriction.
- **(C1) failure** at the constant Hamiltonian (the descent
  obstruction).
- The "circular" structure: pairing with the Capelli central
  element gives back the residue $\hbar N[\bar c]$, not its
  primitive.

**Compatibility with $\Lambda^{\mathrm{Str}}$ super-balancing.**
Candidate (E) collapses to the bosonic Capelli pairing on $\bar A$;
the parity weighting from $\Lambda^{\mathrm{Str}}$ requires the
super source. The bosonic version *is* the residue itself.

**Cohomology-class computation.** The Capelli central element
$[C_\hbar/(\hbar N)]\in HH^0(U_\hbar(\bar A))$ is a deformation
class (not a Lie-cohomology primitive). Its image under the
Hochschild-to-CE map is *the residue $[\bar c]$ itself*, not its
primitive. **Capelli pairing is the residue, not a primitive of it.**

---

## §6. Obstruction-class table — explicit $H^1(\mathfrak g, M)$ computations

### `P4-Exec-RedCat-OBS-01` — Setup of the cohomology computation

**Severity 5 (load-bearing). Status valid. Confidence high.**

We compute the Lie-algebra cohomology obstruction
$[\bar\eta(\bar c)]\in H^1(\mathfrak g, M)$ where:
- $\mathfrak g=\bar A$ as a Lie algebra under the Poisson bracket
  $\{f,g\}=\partial_{z_1}f\partial_{z_2}g-\partial_{z_2}f\partial_{z_1}g$
  (with the constant Hamiltonian killed; the bracket is well-defined
  on $\bar A$ because the constant line is central in
  $\mathfrak h_{\mathrm{poly}}$ — its bracket with anything lies in
  $\C\cdot 1=\ker\pi$).
- $M$ is the trivial $\mathfrak g$-module $\C$ for primitives in
  $C^1_{\mathrm{Lie}}(\bar A,\C)$, or twisted modules for
  candidates (D)/(E).

**The class $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$.** By
`lem:omega-cocycle` (`main.tex`:284–316), the cocycle
$\omega(f,g)=[\{f,g\}_{\mathfrak h_{\mathrm{poly}}}]_0$ is non-trivial
modulo coboundaries; it spans the one-dimensional subspace of
$H^2_{\mathrm{Lie}}(\bar A,\C)$ (Theorem `thm:u1-center-anomaly`,
`main.tex`:318–352). The kernel of $\delta_{\mathrm{CE}}:C^1\to C^2$
is the space of $\mathfrak g$-invariants in $\C$ (= $\C$ trivially);
the image $\delta_{\mathrm{CE}}(C^1)$ is a subspace of $C^2$ that
**does not contain $\omega$**, by the proof of `lem:omega-cocycle`.

**Dimension count.**
- $\dim H^0_{\mathrm{Lie}}(\bar A,\C)=1$ (constants).
- $\dim H^1_{\mathrm{Lie}}(\bar A,\C)=0$ (in the trivial module;
  every $\C$-linear $\bar A\to\C$ is a coboundary iff... no, in
  general $H^1_{\mathrm{Lie}}(\bar A,\C)$ is large, equal to the
  abelianization of $\bar A$ as a Lie algebra). The relevant
  question for primitives is: which $\bar\eta\in C^1$ have
  $\delta\bar\eta=\omega$? Answer: NONE, because $\omega$ is non-
  exact.
- $\dim H^2_{\mathrm{Lie}}(\bar A,\C)\geq 1$ (contains $[\bar c]$;
  the full second cohomology is computed in Tsygan/Nest 2002 for
  the polynomial Poisson algebra; the scalar-axis component is
  one-dimensional and is what we care about).

### `P4-Exec-RedCat-OBS-02` — Per-candidate obstruction class

| Candidate | $\bar\eta$ on $\bar A$ | $\delta_{\mathrm{CE}}\bar\eta$ | Class $[\delta\bar\eta]\in H^2_{\mathrm{Lie}}(\bar A,\C)$ | (C3) discharged? |
|---|---|---|---|---|
| (A) $(a,b)=(0,0)$ | undefined (= unreduced $-\eta$, doesn't descend) | n/a | n/a | NO (descent obstruction) |
| (A) $(a,b)\geq(1,0)$ | $\partial^{a+b}f|_0$ | non-zero 2-coboundary | $0\in H^2$ (it IS a coboundary) | NO (different class than $[\bar c]$) |
| (B) any meromorphic | reduces to (A) | ditto | $0$ or undefined | NO |
| (C) degree-2 pairing | $0$ on bosonic disk | $0$ | $0$ | NO (vacuously trivial) |
| (D) Berezin on super | $0$ on bosonic restriction | $0$ | $0$ on $\bar A$; replaces source on $\bar A^{\mathrm{super}}$ | NO on $\bar A$; vacuous on super |
| (E) Capelli | $\hbar N$ on $f=1$ (doesn't descend) | n/a | n/a | NO (descent obstruction; circular) |

**Interpretation the table.** No row has `(C3) discharged = YES`. The
class $[\bar c]$ remains non-zero in $H^2_{\mathrm{Lie}}(\bar A,\C)$;
no candidate primitive trivializes it.

### `P4-Exec-RedCat-OBS-03` — Adjudication and structural meaning

**Severity 5. Status valid. Confidence high.**

**Structural fact.** $\dim H^2_{\mathrm{Lie}}(\bar A,\C)\geq 1$
with $[\bar c]$ as a generator of the scalar-axis component.
$[\bar c]$ is **not in the image of $\delta_{\mathrm{CE}}|_{C^1(\bar A,\C)}$**
because every linear functional on $\bar A$ vanishes at $0\in\bar A$,
but the cocycle identity demands evaluation at $0\in\bar A$ to
give $\omega(z_1,z_2)=1\neq 0$. **There is no primitive in
$C^1$.**

**Why the unreduced primitive exists.** On $\mathfrak h_{\mathrm{poly}}$,
the linear functional $\eta(f)=-[f]_0$ has $\eta(1)=-1\neq 0$;
the cocycle identity is satisfied because $\{z_1,z_2\}=1$ in
$\mathfrak h_{\mathrm{poly}}$ (not $0$ as in $\bar A$). The
descent map $\pi:\mathfrak h_{\mathrm{poly}}\to\bar A$ kills $1$,
which is precisely where $\eta$ takes its non-zero value. **Descent
breaks the primitive.**

**Why no reduced primitive exists.** Every $\bar\eta:\bar A\to\C$
satisfies $\bar\eta(0)=0$. The cocycle identity demands
$\bar\eta(\{z_1,z_2\}_{\bar A})=\omega(z_1,z_2)=1$. But
$\{z_1,z_2\}_{\bar A}=\pi(\{z_1,z_2\}_{\mathfrak h_{\mathrm{poly}}})=
\pi(1)=0$. So $0=\bar\eta(0)=1$, contradiction. **No reduced
primitive can exist as a linear functional.**

**Generalization to non-linear $\bar\eta$.** Allowing $\bar\eta$ to
be a higher-derivative or pairing functional does not change the
conclusion: every $\bar\eta:\bar A\to\C$ that is $\C$-linear and
vanishes at $0\in\bar A$ has the same obstruction. Higher-derived
$\bar\eta$ (e.g., A$_\infty$-extended) merely postpones the
obstruction to higher-order Massey products, as analyzed in
`reconstitution/phase4-exec-unreduced-primitive-2026-04-28.md`:565–610
(P-A$_\infty$ prescription).

**Theorem G residue verdict.** **The Theorem G residue
$\hbar N[\bar c]\in H^1(\mathcal O_{\mathrm{loc}}(\mathcal E_w),
Q+\{I_0,-\})$ is genuinely cohomologically non-trivial.** No
chain-level primitive exists in any of the five natural candidate
forms. The residue is the class.

---

## §7. Implications for the conditional-theorem status of W3-W15-04 and Theorem G

### `P4-Exec-RedCat-IMP-01` — W3-W15-04 status update

**Severity 4. Status: confirms W3-W15-04 verdict. Confidence high.**

**W3-W15-04 statement** (`wave3-W15-conditional-theorems-2026-04-28.md`:679–773):
"Unreduced QME holds modulo the regulator with a definite, non-zero
residue equal to $[\bar c]$; the residue is **not** a regulator
artifact."

**This catalog confirms.** The five candidate primitives all
fail to discharge the residue on $\bar A$. The residue is therefore
not in the image of any natural primitive, hence is a genuine
cohomology class, hence is **not a regulator artifact**. W3-W15-04
is **confirmed at the chain-level primitive layer**.

**Strengthening.** The catalog goes beyond W3-W15-04: it shows
that not only does the *constant Taylor* primitive fail to descend
(the original argument of `prop:app-scalar-contact-qme-class`),
but **every natural primitive form** (higher derivatives, residues,
cohomology pairings, supertrace, Capelli) fails to discharge.
This closes the door on the "maybe a different chain-level primitive
works" hope.

**Phase-4 status of W3-W15-04.** **CERTIFIED CONVERGED.** No
chain-level primitive on $\bar A$ exists; the residue is the
class. (The status was already CERTIFIED in W15; this catalog
provides additional evidence.)

### `P4-Exec-RedCat-IMP-02` — Theorem G unconditional vs. F$'$ conditional

**Severity 4. Status: validates the manuscript's Phase-3 stance.
Confidence high.**

**Theorem G** (`main.tex`:318–352, `thm:u1-center-anomaly`): The
class $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$ is non-zero and
spans the one-dimensional scalar-axis sub-line. **Unconditional.**

**Theorem F$'$** (`thm:phi-hbar-all-order`, `main.tex`:5459–5485):
gated by `prob:weighted-rg-locality`, which asks whether the QME
residue on the matrix probe is in the trivial class of
$H^1(\mathcal O_{\mathrm{loc}}(\mathcal E_w), Q+\{I_0,-\})$. The
residue is $\hbar N[\bar c]$, which the catalog shows is **not in
the trivial class**.

**Implication.** Theorem F$'$ on the bosonic source $\mathfrak{gl}_N$
is **not unconditional**; it requires either (a) source change
(W22-T1+T2 super-balancing on $\mathfrak{gl}(N|N)$ replacing the
coefficient $N$ by $\Str(I)=0$); (b) 5d-M-theory free pass (G4);
(c) a different theorem statement (Theorem F$''$ on a different
source).

**Manuscript stance is correct.** The manuscript's Phase-3 stance
(F$'$ conditional on `prob:weighted-rg-locality`; G unconditional)
is *exactly* what this catalog confirms. No edit needed at the
manuscript level.

**Status of `prob:weighted-rg-locality` on the bosonic source.**
**CLOSED IN THE NEGATIVE** at the chain-level primitive layer:
no natural reduced-only primitive exists. Re-opening requires
fresh foundational technique (Phase-5).

### `P4-Exec-RedCat-IMP-03` — W22-T1+T2 super-balancing remains the open route

**Severity 3. Status: confirms route-tree. Confidence high.**

**W22-T1+T2 (covered):** on $\mathfrak{gl}(N|N)$ super-balanced
source, the residue coefficient $\Str_{\mathrm{gl}(N|N)}(I)=N-N=0$
kills the residue at the *coefficient level*. No primitive needed.
Closes `prob:weighted-rg-locality` on this source. Catalog
candidate (D) confirms: the Berezin pairing trivializes on the
super source, and the residue itself vanishes.

**Phase-4 G3 extension (P4-G3-T-A1):** Same mechanism on
$\mathfrak{osp}(2N|2N)$ ($\Str=0$ by even/odd dimension equality).
Catalog candidate (D) extends here; candidate (E) Sergeev central
element gives $\hbar\cdot 0=0$ on this source.

**Phase-4 G4 5d-M-theory:** A different mechanism — intrinsic
$\Z/2$-grading of M-theory replaces the bosonic dimension by zero
through the Donaldson-Witten / Kapustin-Witten reduction. Catalog
candidates do not directly apply; this is a different
factorization architecture.

**Phase-5:** Required if all of (W22-T1+T2 super-balanced, G3 osp,
G4 5d-M) are insufficient for the manuscript's goals. The catalog
does not bear on the Phase-5 fresh-technique question.

---

## §8. Residuals and deciding evidence

### `P4-Exec-RedCat-RES-01` — Residual list

**R-`P4-Exec-RedCat-01`.** **All natural reduced-only primitives
fail.** Catalog covered: derivatives at origin (A), meromorphic
residues (B), degree-2 cohomology pairings (C), Berezin/supertrace
on super-stack (D), Capelli/Sergeev central elements (E). No
$\bar\eta:\bar A\to\C$ exists with the required (C1)–(C3)
properties. **Confidence: high.**

**R-`P4-Exec-RedCat-02`.** **The dominant obstruction is universal.**
Every linear $\bar\eta:\bar A\to\C$ vanishes at $0\in\bar A$. Every
2-cocycle requires evaluation at $\{z_1,z_2\}_{\bar A}=\pi(1)=0$ to
give $\omega(z_1,z_2)=1\neq 0$. The two are incompatible. **This
is a structural fact about $\bar A$, not an artifact of any
particular primitive form.** **Confidence: high.**

**R-`P4-Exec-RedCat-03`.** **Composition / Mayer-Vietoris fails for
basepoint-dependent candidates.** Candidates (A), (B), (C) all
violate translation invariance on $\C^2$ and do not glue across
the cover. Candidate (D) trivializes on the bosonic restriction.
Candidate (E) reduces to the residue itself. **No factorization-
algebra-natural primitive exists on $\bar A$.** **Confidence: high.**

**R-`P4-Exec-RedCat-04`.** **Lurie HA connected-symmetric-algebra
requirement is independent confirmation.** A factorization algebra
on a connected symmetric algebra (HA Definition 3.1.1.18) has its
constant line as the unit; no separate primitive in degree 0 is
allowed. Adjoining $\eta$ formally violates this; restricting to
$\bar A$ gives connected, but then no primitive exists. **The two
horns of the dilemma.** **Confidence: high.**

**R-`P4-Exec-RedCat-05`.** **W22-T1+T2 super-balancing is the
correct route.** The discharge mechanism is *not* a primitive at
all — it is a *coefficient zero*. The supertrace coefficient
$\Str(I)=0$ kills the residue without requiring a primitive. This
is the **correct interpretation** of the conditional-theorem status:
Theorem F$'$ on the bosonic $\mathfrak{gl}_N$ source is conditional;
Theorem F$'$ on the super-balanced source is unconditional;
the difference is the source, not the primitive. **Confidence:
high.**

### `P4-Exec-RedCat-RES-02` — Deciding evidence

**The decisive computation.** $\{z_1,z_2\}_{\bar A}=0$ in $\bar A$,
because $\{z_1,z_2\}_{\mathfrak h_{\mathrm{poly}}}=1$ and
$\pi(1)=0$. The cocycle identity
$\bar\eta(\{z_1,z_2\}_{\bar A})=\omega(z_1,z_2)=1$ requires
$\bar\eta(0)=1$, which contradicts linearity. This is a
**one-line proof** that no reduced primitive exists.

**This computation appears in:**
- `appendix-unreduced-bv-qme.tex`:144–157 (proof of
  `prop:app-scalar-contact-qme-class`).
- `main.tex`:308–315 (proof of `lem:omega-cocycle`).
- `phase4-exec-unreduced-primitive-2026-04-28.md`:124–141 (T1
  closure).
- §6 `OBS-03` of this document.

**The catalog adds:** confirmation that the obstruction is
*universal*, not specific to the constant-Taylor primitive. Every
natural alternative form fails for the same reason.

---

## §9. Phase-5 escalation conditions

### `P4-Exec-RedCat-PHASE5-01` — When does this catalog escalate to Phase-5?

**Severity 3. Status: criterion. Confidence high.**

**Phase-5 escalation condition** (from W18 / G5 ledger):
F$'$ on the bosonic source escalates to Phase-5 if **all** of:
- **(P5-α)** Unreduced-primitive route closes negatively: **MET**
  (G5 RELAUNCH-2 / `phase4-exec-unreduced-primitive-2026-04-28.md`).
- **(P5-β)** Source-change route closes negatively (W22-T1+T2,
  G3 osp, related extensions all fail): **NOT MET** (W22-T1+T2
  rigorous on $\mathfrak{gl}(N|N)$; G3 P4-G3-T-A1 chain-level
  rigorous on $\mathfrak{osp}(2N|2N)$).
- **(P5-γ)** 5d-M-theory free-pass route closes negatively
  (G4 fails to provide intrinsic $\Z/2$): **NOT YET TESTED**
  (G4 work pending).

**Implication of this catalog (P4-G5-M2).** The catalog *strengthens*
(P5-α): not only does the unreduced primitive fail, but **no natural
reduced-only primitive** exists either. This makes (P5-α) more
robustly MET.

**Catalog does NOT trigger Phase-5 by itself.** As long as
(P5-β) is not met (W22-T1+T2 / G3 osp give source-change escapes),
F$'$ on the appropriate super-balanced source remains in Phase-4.
The catalog confirms the bosonic source is the wrong source for
F$'$, not that F$'$ is unprovable.

### `P4-Exec-RedCat-PHASE5-02` — Conditional Phase-5 trigger

**Trigger condition.** Phase-5 escalation triggers if a future
finding shows:
1. (P5-β) fails: W22-T1+T2 on $\mathfrak{gl}(N|N)$ is rigorous
   (already established), but the *source-change* itself is
   physically untenable (e.g., the manuscript requires a bosonic
   brane probe for some load-bearing application).
2. (P5-γ) fails: G4 5d-M-theory does not provide an intrinsic
   $\Z/2$-grading.

**If both fail:** F$'$ requires fresh foundational technique
(non-connected $\mathbb E_n$-algebras, derived-CY methods,
cross-volume CY-to-chiral techniques in `~/calabi-yau-quantum-groups`).

**Catalog stance.** The catalog **does not** force Phase-5; it
**strengthens (P5-α)** and **leaves (P5-β), (P5-γ)** open. As long
as G3 (osp) or G4 (5d-M) remains positive, F$'$ can be stated on
that source without Phase-5 escalation.

### `P4-Exec-RedCat-PHASE5-03` — Recommendation

**Recommendation.** **No manuscript edits required from this
catalog alone.** The manuscript's Phase-3 stance (F$'$ conditional;
G unconditional; W22-T1+T2 super-balanced source as escape) is
correct and unaltered. Optional ledger updates:

**`P4-Exec-RedCat-WP-1`.** Add to
`reconstitution/phase4-G5-bosonic-Fprime-2026-04-28.md`
(P4-G5-M2 milestone entry):

> "**Phase-4 status update (2026-04-28, P4-Exec-RedCat).** Catalog of
> five natural reduced-only chain-level primitives
> $\bar\eta:\bar A\to\C$ — derivative at origin (A), meromorphic
> residue (B), degree-2 cohomology pairing (C), Berezin/supertrace
> (D), Capelli/Sergeev central element (E) — confirms that **no
> candidate satisfies (C1)–(C3) simultaneously**. Dominant
> obstruction: every linear functional on $\bar A$ vanishes at $0$,
> but the cocycle identity at $(z_1,z_2)$ requires evaluation at
> $\{z_1,z_2\}_{\bar A}=\pi(1)=0$ to give $\omega(z_1,z_2)=1\neq 0$.
> **The Theorem G residue $\hbar N[\bar c]$ is genuinely
> cohomologically non-trivial.** (P5-α) is strengthened (already
> MET); (P5-β), (P5-γ) remain open."

**`P4-Exec-RedCat-WP-2`** (optional). Add to
`appendix-unreduced-bv-qme.tex` `rmk:app-scalar-contact-escape-routes`
a brief note:

> "**Catalog of reduced-only primitives (2026-04-28, P4-G5-M2).**
> Five natural candidate forms — higher derivatives at origin,
> meromorphic residues, degree-2 cohomology pairings, Berezin
> integrals on the super-stack, Capelli/Sergeev central elements —
> all fail to provide a chain-level primitive
> $\bar\eta:\bar A\to\C$ for the residue $\hbar N[\bar c]$. The
> universal obstruction is linearity at $0\in\bar A$ versus the
> cocycle identity at $\{z_1,z_2\}_{\bar A}=0$. See
> `reconstitution/phase4-exec-reduced-primitives-catalog-2026-04-28.md`."

---

## §10. Convergence verdict

**Phase-4 / Exec / Reduced-primitives catalog (P4-G5-M2): COMPLETE
with universal-negative verdict.**

The catalog of five natural reduced-only chain-level primitives
$\bar\eta:\bar A\to\C$ — (A) higher derivatives at origin, (B)
meromorphic residues, (C) degree-2 cohomology pairings, (D)
Berezin integrals on the super-stack, (E) Capelli/Sergeev central
elements — confirms that **no candidate** satisfies (C1)–(C3)
simultaneously. The dominant obstruction is the structural
incompatibility between linearity at $0\in\bar A$ and the cocycle
identity at $\{z_1,z_2\}_{\bar A}=0$. The class
$[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$ is **not in the image
of $\delta_{\mathrm{CE}}|_{C^1}$**; it is a genuine non-trivial
cohomology class.

**Theorem G residue verdict: GENUINELY COHOMOLOGICALLY NON-TRIVIAL.**

**Phase-4 escape routes for F$'$ remaining open.**
- **W22-T1+T2 super-balanced** $\mathfrak{gl}(N|N)$: rigorous on
  super-balanced source.
- **G3 osp(2N|2N)**: rigorous-in-reach (P4-G3-T-A1 chain-level
  closed under (A1)–(A5)).
- **G4 5d-M-theory free pass**: pending.

**Phase-5 escalation status.** (P5-α) **strengthened** to MET in
two layers (unreduced primitive AND reduced primitive both fail).
(P5-β), (P5-γ) **open**; F$'$ remains Phase-4 via super-balanced
source-change.

**Inscribed durables.**
- This catalog document.
- W3-W15-04 status: **CERTIFIED CONVERGED**, strengthened.
- Theorem G residue: **GENUINELY COHOMOLOGICALLY NON-TRIVIAL**.
- (P5-α) **MET** in two layers; route-tree unchanged.
- Three workpieces (P4-Exec-RedCat-WP-1/2) for optional ledger
  updates; manuscript needs no edits.

End of P4-Exec-RedCat ledger.
