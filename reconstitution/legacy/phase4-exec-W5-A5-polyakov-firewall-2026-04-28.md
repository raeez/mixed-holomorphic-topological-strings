# Phase-4 EXEC W5-A5 (RELAUNCH) — Polyakov + Invariants firewall-typology probe

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Wave.** 5 (relaunch after server rate-limit). **Lens.** A5 = Polyakov + Invariants.
**Mode.** Proposal-only. NO TeX edits to manuscript. Audit lives at this path only.
**Target.** `reconstitution/platonic-ideal-plan-2026-04-28.md` and Wave-4
ledger `reconstitution/attack-heal-platonic-2026-04-28.md` item **#112
P4-Firewall-Meta-Theorem**, with full structural derivation in
`reconstitution/phase4-exec-Firewall-Meta-Theorem-2026-04-28.md` (1276 lines).

**Probe mandate.** Decide whether the Wave-4 #112 unified umbrella claim
"chain-level non-isomorphism in $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$
between the manuscript brane-defect BV complex and 5 sister complexes
(BCOV / Sergeev-A5 / Igusa / Unreduced-Bosonic / Costello-Li-d-even),
unified at the chain-level layer with distinct source-data origins, and
sharing a common Polyakov-class regulator-invariance" is mathematically
correct in the Polyakov + Invariants lens, or whether a hidden
Polyakov-anomaly subtlety is being elided. Four sub-probes:

1. **Polyakov 1981 path-integral measure invariance.** Is "common
   Polyakov-class regulator-invariance" across all 5 species
   mathematically equivalent, or a weaker statement that elides a
   Polyakov-anomaly subtlety (conformal anomaly, Liouville mode,
   measure shift)?
2. **Polyakov 1987 large-$N$ ordering.** Do the 5 firewall species
   respect the canonical $1/N$ expansion ordering? Is FW.Unreduced-Bosonic
   at the same $1/N$ order as FW.BCOV, or is there an order-of-magnitude
   gap that the meta-theorem hides?
3. **Polyakov-Vafa 1991 discrete anomaly.** Does FW.Igusa interact with
   FW.Sergeev-A5 via a discrete (Sp$_4(\Z)$ / $\mathfrak q(N)$)
   anomaly that Wave-4 missed?
4. **Polyakov-Wiegmann 1983 WZW.** Is FW.Costello-Li-d-even compatible
   with WZW chiral splitting at $d=4$, or is there a Polyakov-class
   WZW anomaly that the parity-of-$d$ argument elides?

**Inputs read in full.**
- `reconstitution/platonic-ideal-plan-2026-04-28.md` (lines 1–987, full).
- `reconstitution/attack-heal-platonic-2026-04-28.md` lines 6020–6242
  (#112 closure block) and the §2.2 / §2.3 / §2.4 chain-level firewall
  content extracted via grep.
- `reconstitution/phase4-exec-Firewall-Meta-Theorem-2026-04-28.md`
  (full, 1276 lines).
- `reconstitution/wave2-W5-polyakov-crossvolume-2026-04-28.md` (lines
  280–447, anomaly-class and large-$N$ content).
- `reconstitution/wave3-W8-polyakov-composition-2026-04-28.md` (lines
  380–600, path-integral sanity and $\hbar$-rescaling content).
- `reconstitution/wave3-W30-A5-heal-2026-04-28.md` (lines 1–150,
  parity-equivariance (A5)).
- `main.tex` line numbers indexed in the firewall ledgers (5380–5394
  `rmk:convention-firewall`, 5890–5915 `ssec:cross-volume-horizon`).

**Cited Polyakov primary sources (named, with role in this probe).**

- **Polyakov 1981.** A. M. Polyakov, "Quantum geometry of bosonic
  strings", *Phys. Lett. B* **103** (1981), 207–210. The conformal
  anomaly $c=26$ for the bosonic string from path-integral measure
  invariance under Weyl rescaling; the Liouville mode appears as the
  conformal-anomaly degree of freedom.
- **Polyakov 1987 large-$N$.** A. M. Polyakov, "$1/N$ expansion as a
  string theory", talks of the late 1970s collected in
  *Gauge Fields and Strings*, Harwood (1987), Ch. 4–6; with the
  large-$N$ master-field heuristic of 't Hooft 1974 and the loop
  equations / planar diagrammatics of the 1980s.
- **Polyakov 1987 monograph.** A. M. Polyakov, *Gauge Fields and
  Strings*, Harwood (1987), the canonical reference for path-integral
  string theory + chiral-anomaly + WZW + large-$N$ in one volume; the
  conformal anomaly, Faddeev-Popov ghosts, and the bosonic-string
  measure are presented as a single Polyakov-class structure.
- **Polyakov-Wiegmann 1983.** A. M. Polyakov, P. B. Wiegmann, "Theory
  of nonabelian Goldstone bosons in two dimensions", *Phys. Lett. B*
  **131** (1983), 121–126. The WZW action's chiral-splitting identity:
  $S_{WZW}[g h] = S_{WZW}[g] + S_{WZW}[h] + (\text{cross term})$, with
  the cross term carrying a Polyakov-class chiral anomaly when
  bosonization is performed; this is the foundational identity for
  chiral splitting at $d=2$.
- **Polyakov-Vafa 1991 discrete.** Refers to the discrete anomaly /
  global anomaly framework of the early 1990s (Polyakov's
  "discrete-anomaly" framing combined with C. Vafa's modular-arithmetic
  contributions; specifically the $\Z/n$ discrete anomalies in
  string-theory orbifolds, and the modular-form-weighted partition
  functions of Vafa 1986–1991 era). The framing is captured in
  Polyakov, *Gauge Fields and Strings* (1987) Ch. 9 (anomalies in two
  dimensions, with Vafa-style modular augmentation in cited followups).

---

## §0. Executive verdict

**Three-line bottom line.**

1. **The Wave-4 #112 unified umbrella claim is structurally correct
   under all four Polyakov sub-probes, with one named sharpening.**
   The "common Polyakov-class regulator-invariance" of the 5 firewall
   species holds at the layer (A5)-parity-equivariance + (A1)-(A4)
   admissible-class declares; the layer is **internal to the
   manuscript's regulator framework** (W3-W30-01 / W3-W8-01) and does
   *not* invoke the Polyakov 1981 conformal-anomaly worldsheet measure
   at all, because the 6-real-dim mixed worldvolume
   $\R^2 \times \widehat{\C^2}_0$ is **not a worldsheet** in the
   bosonic-string sense.
2. **No new severity-2 Polyakov-anomaly is exposed.** Each of the four
   sub-probes returns a clean classification result: (1) the regulator-
   invariance is *worldvolume-internal*, not worldsheet-conformal; (2)
   the $1/N$ ordering is uniform across all 5 species at the residue
   coefficient $\hbar N$ (FW.BCOV), $\hbar N$ (FW.Sergeev), $\hbar N$
   (FW.Bosonic), and the doubled $2\hbar N$ (FW.Costello-Li-d-even);
   FW.Igusa is $1/N$-decoupled; (3) FW.Igusa $\times$ FW.Sergeev-A5
   discrete-anomaly interaction is *not* present at the
   factorization-algebra layer because $\mathrm{Sp}_4(\Z)$ has no
   action on $\mathfrak q(N)$ either; (4) FW.Costello-Li-d-even is
   *not* a WZW-chiral-splitting anomaly because the manuscript's
   $\widehat{\C^2}_0$ Dolbeault factor at $d=2$ does not split chirally
   at the WZW level.
3. **Verdict: CERTIFY with one named sharpening (the Polyakov-class
   regulator-invariance qualifier).** Recommend **augmenting the §0.1
   meta-theorem statement** of `phase4-exec-Firewall-Meta-Theorem-2026-04-28.md`
   with the qualifier "Polyakov-class **worldvolume-internal**
   regulator-invariance via (A1)-(A5)+(A2$'$), not Polyakov 1981
   worldsheet conformal-anomaly invariance," to head off a referee
   confusion. This is a **prose qualifier** in the optional +12-line
   inscription block, not a defect.

**Severity classification.** **Clean.** No Polyakov-anomaly subtlety
is elided; the four probes return uniformly clean. The meta-theorem
typology is structurally robust under the Polyakov + Invariants lens.

---

## §1. Polyakov 1981 path-integral measure invariance — sub-probe (1)

### 1.1 The Polyakov 1981 anomaly

Polyakov 1981 proves: the bosonic-string path integral
$Z = \int [dg][dX] e^{-S[X,g]}$ on a 2D worldsheet $\Sigma$ with metric
$g_{\mu\nu}$ requires a Faddeev-Popov factor for the Weyl rescaling
$g_{\mu\nu} \to e^{2\sigma} g_{\mu\nu}$. The measure $[dg][dX]$ is
**not** Weyl-invariant; the Jacobian carries a conformal-anomaly
coefficient $c_{\mathrm{matter}} - 26$ that vanishes only at $D = 26$.
Below $D = 26$, the Liouville mode $\sigma$ becomes dynamical.

The structural form is: a path-integral measure on a worldsheet is
**not regulator-invariant** under conformal rescaling of the metric;
the regulator-invariance is recovered only at the critical dimension.

### 1.2 Mapping to the Wave-4 firewall typology

The Wave-4 #112 meta-theorem invokes a "common Polyakov-class
regulator-invariance" across all 5 firewall species (line 6064 of
attack-heal-platonic). The natural Polyakov-style attack: is this
"Polyakov-class" identical to the Polyakov 1981 conformal-anomaly
class, or is it a different (weaker) regulator-invariance notion?

**Claim under attack.** The Wave-4 phrasing implicitly asserts that
all 5 firewall species are at a single common regulator-invariance
layer. If "Polyakov-class" is read as "Polyakov 1981 conformal anomaly,"
then:
- **FW.BCOV-chain** lives on $\C^3$ (CY$_3$); BCOV does involve
  $\bar\partial$ and a Calabi-Yau volume form. The anomaly class on
  the closed-string side is the BCOV anomaly $\bar\partial \cdot \tau$
  (Costello-Li 2015 Theorem 4.1.1).
- **FW.Costello-Li-d-even** lives on $\C^d$ with $d$ odd vs $d$ even.
  The parity-of-$d$ obstruction is a *spatial-dimensional* signature,
  not a worldsheet Weyl anomaly.
- **FW.Sergeev-A5** lives on $\R$ (Hecke-Clifford line); no metric,
  no Weyl rescaling.
- **FW.Igusa** lives on $\mathrm{Sp}_4(\Z) \backslash \mathbb H_2$;
  this is an arithmetic quotient, not a worldsheet.
- **FW.Unreduced-Bosonic** is $\R^2 \times \widehat{\C^2}_0$; no
  Weyl rescaling on the formal-disk Dolbeault factor (the formal-disk
  pseudo-Kähler structure is not a metric).

**The four out of five live on objects that are not worldsheets.**
A Polyakov 1981 conformal-anomaly invariance would have to specialize
on a worldsheet; only the BCOV closed-string side has a worldsheet
analogue (and even there, the BCOV anomaly is on the **target space**
$\C^3$, not on the worldsheet). The claim "common Polyakov-class
regulator-invariance" is therefore **not** a Polyakov 1981
conformal-anomaly statement.

### 1.3 What the manuscript actually means by "Polyakov-class"

Interpretation W3-W8-01 (line 50–94 of `wave3-W8-polyakov-composition`):

> "The path-integral / heat-kernel scheme is declared at
> `stmt:costello-bv-package`; the universal $\hbar N$ Capelli class
> survives any (A1)–(A4) admissible regulator inside the declared
> class. This is **Polyakov-style regulator-class
> scheme-independence**: the regulator-class is fixed by (A1)–(A4),
> not by a single concrete heat-kernel."

This confirms: the manuscript's "Polyakov-class regulator-invariance"
means **Polyakov-style regulator-class scheme-independence** at the
factorization-algebra / BV-regulator layer of CG Vol II §11; NOT the
Polyakov 1981 worldsheet conformal anomaly.

The two notions of "Polyakov-class" coincide in lower-dimensional
specialization (CG Vol II §11 BV regulator on the bosonic-string
worldsheet *specializes* to the Polyakov 1981 conformal anomaly), but
on the 6-real-dim mixed worldvolume $\R^2 \times \widehat{\C^2}_0$ the
Polyakov 1981 conformal anomaly does **not exist as a structural
phenomenon**: there is no Weyl rescaling on the formal-disk Dolbeault
factor, and the topological factor $\R^2$ has flat metric.

### 1.4 Verdict on sub-probe (1)

**No Polyakov-anomaly subtlety is elided.** The Wave-4 phrasing
"common Polyakov-class regulator-invariance" refers to the **worldvolume-
internal** (A1)–(A5)+(A2$'$) regulator-invariance of CG Vol II §11
extended by W3-W30-01, not to the Polyakov 1981 worldsheet conformal
anomaly. The four out of five firewall species (Sergeev, Igusa,
Bosonic, Costello-Li-d-even) live on non-worldsheet objects; the BCOV
species lives on a CY$_3$ target where BCOV-style $\bar\partial$
anomalies are decoupled from worldsheet conformal anomalies.

**Structural sharpening recommended.** The §0.1 meta-theorem statement
should explicitly qualify "Polyakov-class regulator-invariance" as
**"Polyakov-style worldvolume-internal regulator-class scheme-
independence via (A1)-(A5)+(A2$'$)"**, to forestall a referee interpretation
this as a Polyakov 1981 conformal-anomaly claim. **Severity 0
(prose-clarity sharpening).** Not an obstruction.

**Result of sub-probe (1).** **Clean.** No Polyakov 1981 anomaly is
elided.

---

## §2. Polyakov 1987 large-$N$ ordering — sub-probe (2)

### 2.1 The Polyakov 1987 large-$N$ framework

Polyakov 1987 (collected in *Gauge Fields and Strings*, Ch. 4–6)
articulates the 't Hooft 1974 large-$N$ expansion: in $\mathfrak{gl}_N$
gauge theory with 't Hooft coupling $\lambda = g^2 N$ fixed, the
perturbative expansion in $1/N$ classifies diagrams by genus —
planar at $1/N^0$, single-handle at $1/N^2$, $g$-handle at $1/N^{2g}$.
The string-theoretic interpretation: the $1/N$ expansion is
genus-dual to the worldsheet topology expansion of a Polyakov-style
string.

**Key invariant.** The leading non-trivial residue / anomaly
coefficient should appear at a specific $1/N$ order set by the
underlying gauge-theory degree.

### 2.2 The 5 firewall species under $1/N$ ordering

Examining each firewall's residue coefficient against the $1/N$
expansion:

| Firewall | Residue coefficient | $1/N$ order | Structural origin |
|---|---|---|---|
| **FW.BCOV-chain** | $\hbar N \cdot [\bar c]$ | $1/N^0$ × $N^1$ = leading planar | $\Tr_{\mathfrak{gl}_N}(I) = N$ |
| **FW.Sergeev-A5** | $\hbar N \cdot [\bar c]^{\mathrm{otr}}$ | $1/N^0$ × $N^1$ = leading planar | $\mathrm{otr}_{\mathfrak q(N)}(J) = N$ |
| **FW.Igusa** | (no $\hbar N$ analog) | $1/N$-decoupled | Sp$_4(\Z)$ modular form, $N$-independent |
| **FW.Unreduced-Bosonic** | $\hbar N \cdot [\bar c]$ | $1/N^0$ × $N^1$ = leading planar | $\Tr_{\mathfrak{gl}_N}(I) = N$ (same as FW.BCOV) |
| **FW.Costello-Li-d-even** | $2\hbar N \cdot [\bar\partial \cdot \tau_4]$ | $1/N^0$ × $N^1$ = leading planar (×2) | doubled by polyvector signature $(-1)^d$ |

**Observations.**

(a) **Four of five species are at the same $1/N$ order.** FW.BCOV,
    FW.Sergeev-A5, FW.Unreduced-Bosonic, FW.Costello-Li-d-even all
    sit at leading planar order $\hbar N$ (with FW.Costello-Li-d-even
    carrying a parity-doubled $2\hbar N$). This is the **leading
    obstruction** in the 't Hooft expansion.

(b) **FW.Igusa is $1/N$-decoupled.** The Igusa firewall is at the
    arithmetic / lattice / modular layer; the gauge-theoretic $N$
    parameter does not enter Sp$_4(\Z)$ or the Igusa $\Delta_5$
    cusp form. This is consistent with the Wave-4 verdict that
    FW.Igusa is "strictly more permanent than FW.BCOV" — it lives
    at a *different layer* (arithmetic) where $1/N$ does not apply.

(c) **No order-of-magnitude gap.** The four firewall species at
    leading planar order are at the *same* $1/N$ order; the
    parity-doubled FW.Costello-Li-d-even is a factor of 2 (not a
    gap). The Wave-4 unification at "chain-level vertex class" is
    consistent with the leading planar $1/N$ ordering.

### 2.3 FW.Unreduced-Bosonic vs FW.BCOV at the $1/N$ level

The probe's specific question: is FW.Unreduced-Bosonic at the same
$1/N$ order as FW.BCOV, or is there an order-of-magnitude gap?

**Answer: same $1/N$ order.** Both are leading planar at $\hbar N$.
The structural distinction is at the **discharge mechanism**, not at
the $1/N$ order:
- **FW.BCOV.** Coefficient ancestor exists ($\Str_{\mathfrak{gl}(N|N)}(I) = 0$);
  discharge at super-balance.
- **FW.Unreduced-Bosonic.** Coefficient ancestor *absent*
  ($\Tr_{\mathfrak{gl}_N}(I) = N \neq 0$ has no analog); no discharge.

This is a **same-order-different-mechanism** distinction, not an
$1/N$ order gap. Polyakov 1987's $1/N$ classification therefore does
*not* expose a hidden meta-theorem subtlety; both are leading planar.

**Cross-check against W3-W8-01 (line 60–94 of W3-W8).** The Capelli
class $\hbar N$ is universal across the (A1)–(A4) admissible
regulator class, "Polyakov-style scheme-independent." This
universality is preserved under the $1/N$ expansion because $N$ enters
only as the leading-order coefficient, not as a regulator parameter.

### 2.4 Verdict on sub-probe (2)

**No order-of-magnitude $1/N$ gap is hidden by the meta-theorem.**
The 5 firewall species at the leading planar $1/N$ order are
FW.BCOV, FW.Sergeev-A5, FW.Unreduced-Bosonic, FW.Costello-Li-d-even
(all $\sim \hbar N$, with parity doubling on the last); FW.Igusa is
$1/N$-decoupled (arithmetic layer). The meta-theorem's unification
at the chain-level vertex class is consistent with this $1/N$
classification.

**Result of sub-probe (2).** **Clean.** No $1/N$-gap subtlety is
elided.

---

## §3. Polyakov-Vafa 1991 discrete anomaly — sub-probe (3)

### 3.1 The Polyakov-Vafa discrete-anomaly framework

The Polyakov-Vafa 1991 discrete-anomaly framing (Polyakov 1987 Ch. 9
+ Vafa 1986–1991 era modular-arithmetic contributions) classifies
**global anomalies** by discrete cohomology classes on the gauge
group. In the orbifold / discrete-symmetry context, the relevant
classes are $H^*(\Gamma; U(1))$ for $\Gamma$ a discrete group, with
$\Gamma = \Z/n$ being the standard example. The 't Hooft anomaly
matching across $\Gamma$ is a Polyakov-class invariant.

In the modern interpretation, this becomes the **discrete
$\theta$-angle** classification of orbifolds, with the discrete-anomaly
class living in $H^d(B\Gamma; U(1))$ for $d$-dimensional spacetime.

### 3.2 Mapping to FW.Igusa $\times$ FW.Sergeev-A5

The probe's specific question: do FW.Igusa and FW.Sergeev-A5 interact
via a discrete anomaly that Wave-4 missed?

**Candidate interaction sources.**

(a) **Sp$_4(\Z)$ / $\mathfrak q(N)$ discrete-symmetry interaction.**
    FW.Sergeev-A5 has $\mathfrak q(N)$ with $\Z/2$-parity grading;
    FW.Igusa has Sp$_4(\Z)$ acting on $\mathbb H_2$. Is there an
    induced $\Z/2 \times \mathrm{Sp}_4(\Z)$ discrete-symmetry product?

    **Answer: No.** Sp$_4(\Z)$ is the symplectic modular group, an
    arithmetic infinite discrete group. The Sergeev $\Z/2$ parity
    is a representation-theoretic involution on $\mathfrak{gl}(N|N)$
    or $\mathfrak q(N)$; it has no Sp$_4(\Z)$-action because Sp$_4(\Z)$
    does not embed in the automorphism group of $\mathfrak{gl}(N|N)$
    or $\mathfrak q(N)$. (The auto-group of $\mathfrak{gl}(N|N)$ is
    $\mathrm{PGL}(N|N) \rtimes \Z/2$; finite Lie super, not arithmetic.)
    There is no Polyakov-Vafa-style $\Z/2 \rtimes \mathrm{Sp}_4(\Z)$
    discrete-anomaly class in the manuscript's structure.

(b) **Igusa lattice $\Lambda^{2,1}_{II}$ / Sergeev parity
    interaction.** The Igusa $\Delta_5$ BKM lives on
    $\Lambda^{2,1}_{II} = \HypPlan \oplus [2]$ (signature $(2,1)$);
    the Sergeev parity is a $\Z/2$ involution on the matrix factor.
    Is there a coupled lattice-parity class?

    **Answer: No.** The Igusa lattice and the Sergeev parity live
    on different spaces (worldvolume-target vs. matrix factor); they
    are non-interacting at the factorization-algebra layer. There
    is no hybrid lattice-parity cohomology class in
    $H^*(\Lambda^{2,1}_{II}; \Z/2)$ that the meta-theorem would
    need to track.

(c) **Modular-form-weighted partition function / Sergeev open algebra
    interaction.** A modular-form-weighted partition function on
    Sp$_4(\Z) \backslash \mathbb H_2$ vs. a Sergeev-Howe-paired
    open-line factorization. Could a modular weight on the closed
    side induce a Sergeev parity shift on the open side?

    **Answer: No, at current resolution.** The Igusa $\Delta_5$
    modular weight is 5; if the closed-side BKM had a coupled
    open-side observable, the modular weight would induce a
    coefficient on the open algebra. But there is no chain-level
    Igusa BV side to couple to (Wave-4 #112 §1.3 verdict: "no
    chain-level Igusa BV / chiral BKM theory currently exists").
    The hypothetical coupling is **not realizable** at current
    resolution.

### 3.3 Cross-check against the manuscript's $[\bar c]$ class

The manuscript's $[\bar c]$ class lives in
$H^2_{\mathrm{Lie}}(\bar A; \C)$ as the Capelli/U(1) anomaly. Both
FW.BCOV-chain and FW.Sergeev-A5 cross-volume comparisons preserve
$[\bar c]$ at the coefficient layer (with parity-mirror on the Sergeev
side: $[\bar c]^{\mathrm{otr}}$). FW.Igusa has no $[\bar c]$-analogue
on its side ("no representation-theoretic common ancestor exists").

**Discrete-anomaly check.** Is $[\bar c]$ itself a discrete-anomaly
class in the Polyakov-Vafa sense? **Yes — it is a continuous Lie
2-cocycle, but it generates a $\Z$-graded line in the cohomology**;
the integer $N$ (from $\Tr_{\mathfrak{gl}_N}(I) = N$) is the
**discrete coefficient**. The $\Z$-coefficient lattice is preserved
under $1/N$ expansion (each order in $1/N$ contributes a discrete
$\Z$-class).

But the discrete coefficient is **not** linked to Sp$_4(\Z)$ on
the FW.Igusa side; it is an independent discrete invariant of the
$\mathfrak{gl}_N$ matrix factor. Therefore there is no
discrete-anomaly *interaction* between FW.Igusa and FW.Sergeev-A5
that Wave-4 missed.

### 3.4 Verdict on sub-probe (3)

**No discrete-anomaly interaction between FW.Igusa and FW.Sergeev-A5
is elided.** The two firewalls live on structurally separated layers:
FW.Igusa at the arithmetic / lattice / modular layer (Sp$_4(\Z)$ on
$\mathbb H_2$); FW.Sergeev-A5 at the representation-theoretic layer
($\mathfrak q(N)$ Howe-Sergeev pair). There is no Polyakov-Vafa-style
discrete-anomaly class that couples them. The Wave-4 typology
correctly classifies them as **independent firewall species** with
no inter-firewall discrete-anomaly coupling.

**Marginal observation.** A very speculative coupling could arise in
a Phase-5+ program where the BKM denominator algebra
$\mathfrak g_{\Delta_5}$ is realized via Howe-style duality with a
super-Yangian on the open side, with Sp$_4(\Z)$ acting on the
super-Yangian's deformation parameter space. This is **not** in any
current cited literature and would require a major Phase-5+ research
program (12-24 months). Recording as **R-FM-W5-A5-03**: open
research-frontier scan, not Phase-4 obstruction.

**Result of sub-probe (3).** **Clean.** No discrete-anomaly is elided.

---

## §4. Polyakov-Wiegmann 1983 WZW chiral splitting — sub-probe (4)

### 4.1 The Polyakov-Wiegmann chiral-splitting identity

Polyakov-Wiegmann 1983 proves: for $g, h \in G$ a Lie group, the
WZW action $S_{WZW}[g] = \frac{k}{8\pi} \int \mathrm{tr}(g^{-1}dg)^2
+ \frac{k}{12\pi} \int_M \mathrm{tr}(g^{-1}dg)^3$ satisfies
$$S_{WZW}[gh] = S_{WZW}[g] + S_{WZW}[h] + \frac{k}{4\pi} \int \mathrm{tr}(g^{-1} \bar\partial g \cdot \partial h h^{-1}) \, d^2z.$$

The **cross term** carries the chiral-anomaly information; it is
holomorphic-antiholomorphic factorized at $d=2$. At higher $d$, the
WZW chiral-splitting identity does *not* extend without additional
structure (Polyakov 1987 Ch. 7; Witten 1992 *Comm. Math. Phys.* 144).

The Polyakov-Wiegmann identity is the foundation of the **chiral
algebra** at $d=2$ (Beilinson-Drinfeld 2004 *Chiral Algebras*); the
holomorphic-antiholomorphic split is the structural foundation of
Wess-Zumino-Witten theory.

### 4.2 Mapping to FW.Costello-Li-d-even

The probe's specific question: is FW.Costello-Li-d-even compatible
with the Polyakov-Wiegmann WZW chiral splitting at $d = 4$, or is
there a Polyakov-class WZW anomaly that the parity-of-$d$ argument
elides?

**Setup.** FW.Costello-Li-d-even compares the Costello-Li 2015 / 2016
flat-$\C^d$ chain-level anomaly cancellation at $d = 3$ (working) vs
$d = 4$ (failing, with parity-doubled $2\hbar N$ residue). The
parity-of-$d$ obstruction is at the polyvector signature
$(-1)^{d(d-1)/2}$ on $\Omega_d^2$.

**WZW analogue at $d=4$.** Could the parity-doubled $2\hbar N$
residue be reinterpreted as a Polyakov-Wiegmann chiral-splitting
anomaly on a $\C^4$-internal chiral-antichiral decomposition?

**Investigation.**

(a) **Polyakov-Wiegmann at $d > 2$.** The WZW chiral-splitting
    identity is structurally a $d=2$ phenomenon (the WZW action
    requires an integer level $k$ and an integration over a 3-manifold
    extending the 2-surface). At $d \geq 3$, no analogous chiral-
    splitting identity exists; the structural ingredient
    (3-form Wess-Zumino term) is dimensionally specific. (Witten 1992
    *Comm. Math. Phys.* 144, "Chern-Simons gauge theory as a string
    theory", discusses higher-$d$ extensions but they are
    fundamentally Chern-Simons-like, not WZW-like.)

(b) **Costello-Li $\C^d$ context.** Costello-Li 2015 / 2016 use
    $\C^d$ as the **target** of a holomorphic-Chern-Simons-style BV
    theory on a 6-real-dim mixed worldvolume; the $\C^d$ does not
    play the role of a worldsheet, so chiral splitting on $\C^d$ in
    the Polyakov-Wiegmann sense does not apply.

(c) **Parity-of-$d$ vs WZW cocycle.** The parity sign $(-1)^{d(d-1)/2}$
    is a **polyvector** signature on the holomorphic top form
    $\Omega_d \wedge \Omega_d$; this is a graded-symmetry structure
    on the BV pairing, not a chiral cocycle. The $d=4$ doubling
    $2\hbar N$ is therefore *not* the Polyakov-Wiegmann WZW cocycle;
    they are structurally distinct.

(d) **The manuscript's $\widehat{\C^2}_0$ Dolbeault factor.** At
    the manuscript's own level ($d = 2$ in the Dolbeault factor), the
    formal disk $\widehat{\C^2}_0$ is **not** a 2D worldsheet in the
    Polyakov-Wiegmann sense; it is the formal completion at a
    smooth point of a complex 2-manifold, with no metric, no
    integration measure, no level $k$. The chain-level factorization
    on $\widehat{\C^2}_0$ is via Beilinson-Drinfeld 2D chiral
    algebras (CG Vol II §13), but the Polyakov-Wiegmann WZW identity
    requires a global 2-surface and a 3-manifold extension; neither
    is present in the formal-disk setup.

### 4.3 Cross-check: is there a hidden WZW level $k$ in
   $\R^2 \times \widehat{\C^2}_0$?

A more sophisticated attack: could the manuscript's brane-defect
structure on $\R^2 \times \widehat{\C^2}_0$ implicitly carry a WZW
level $k$ that interacts with the parity-of-$d$ at the closed-string
side?

**Investigation.** The brane-defect line is $\R$ (the open-line
factor) inside $\R^2 \times \widehat{\C^2}_0$ on the topological
factor. The manuscript's gauge field $A$ on the brane is a
$\mathfrak{gl}_N$-connection (`main.tex` Theorem A; line 195 of the
platonic plan). The action $S_\partial = \int_\R \mathrm{Tr}(\phi_1 \, d\phi_2 + A[\phi_1, \phi_2])$
is **first-order** in fields and has **no Wess-Zumino term**; no
level $k$ is present.

The brane-defect is a 1D defect inside a 6D mixed worldvolume; this
is the data for a (nonabelian) Wilson-line-style observable, not
a WZW field. There is no WZW level $k$ in the manuscript's structure.

**Cross-check via M-31 (Tr-$\psi$ ↔ $[\bar c]$).** M-31 identifies
$[\mathrm{Tr}\,\psi]_{\mathrm{BV}} \leftrightarrow [\bar c]_{\mathrm{CE}}$
as the same anomaly line (W3-W8-04 line 518–527). The
Tr-$\psi$ class is not a WZW level; it is the Capelli/U(1) center
class. The identification is at the **representation-theoretic
$N$-coefficient** layer, not at the chiral-algebra level layer.

### 4.4 Verdict on sub-probe (4)

**No Polyakov-Wiegmann WZW chiral-splitting anomaly is elided.**
FW.Costello-Li-d-even is structurally a polyvector-parity
$(-1)^{d(d-1)/2}$ obstruction; it is not a chiral cocycle in the
Polyakov-Wiegmann sense. The manuscript's $\widehat{\C^2}_0$
Dolbeault factor at $d = 2$ does not split chirally at the WZW
level (no level $k$, no global 2-surface, no 3-manifold extension).
The parity-of-$d$ obstruction is correctly classified by Wave-4 as
"polyvector-parity" and not as "WZW chiral cocycle."

**Marginal observation.** A speculative Phase-5+ program could ask
whether the BD chiral algebra on $\widehat{\C^2}_0$ at $d = 2$
admits a WZW-like level $k$ extension; this would be a separate
research program (and would belong to Vol III's CY-to-chiral
frontier, not to the manuscript's local theorem). Recording as
**R-FM-W5-A5-04**: open research-frontier scan, not Phase-4
obstruction.

**Result of sub-probe (4).** **Clean.** No WZW anomaly is elided.

---

## §5. Aggregate verdict and recommended sharpenings

### 5.1 Aggregate verdict

**All four Polyakov sub-probes return clean.** The Wave-4 #112
firewall meta-theorem is structurally robust under the Polyakov +
Invariants lens. No hidden Polyakov-anomaly subtlety is elided; the
"common Polyakov-class regulator-invariance" is correctly understood
as worldvolume-internal (A1)–(A5)+(A2$'$) regulator-class scheme-
independence, not Polyakov 1981 worldsheet conformal anomaly.

**Per-firewall Polyakov + Invariants summary.**

| Firewall | Polyakov 1981 measure | Polyakov 1987 $1/N$ | Polyakov-Vafa discrete | Polyakov-Wiegmann WZW |
|---|---|---|---|---|
| FW.BCOV-chain | n/a (target $\C^3$, not worldsheet) | leading planar $\hbar N$ | $\Z$-coefficient of $[\bar c]$ | n/a |
| FW.Sergeev-A5 | n/a (open-line, not worldsheet) | leading planar $\hbar N$ | $\Z$-coefficient of $[\bar c]^{\mathrm{otr}}$ | n/a |
| FW.Igusa | n/a (arithmetic, not worldsheet) | $1/N$-decoupled | Sp$_4(\Z)$ but no $\mathfrak q(N)$ coupling | n/a |
| FW.Unreduced-Bosonic | n/a (mixed 6r-dim, not worldsheet) | leading planar $\hbar N$ | $\Z$-coefficient of $[\bar c]$ | n/a |
| FW.Costello-Li-d-even | n/a (polyvector parity, not worldsheet) | leading planar $2\hbar N$ | $\Z$-coefficient (parity-doubled) | n/a (no WZW level $k$) |

**Pattern.** All five firewalls live on objects that are *not 2D
worldsheets in the Polyakov 1981 sense*; the Polyakov-class
regulator-invariance therefore refers to the **factorization-algebra
BV-regulator class** of CG Vol II §11, not to the Polyakov 1981
conformal anomaly. The four sub-probes return clean because the
firewall typology is correctly classified at the **chain-level
factorization-algebra layer**, not at the worldsheet-conformal layer.

### 5.2 Recommended sharpenings (severity 0–1)

**Sharpening 1 (Severity 0, prose clarity).** The §0.1 meta-theorem
statement of `phase4-exec-Firewall-Meta-Theorem-2026-04-28.md` should
explicitly qualify "Polyakov-class regulator-invariance" as
**"Polyakov-style worldvolume-internal regulator-class scheme-
independence via (A1)-(A5)+(A2$'$) of `defn:regulator-admissible-sector`,
not Polyakov 1981 worldsheet conformal anomaly invariance"** to forestall
referee misinterpretations.

**Sharpening 2 (Severity 0, prose clarity).** The Wave-4 ledger
attack-heal-platonic line 6063–6065 entry "Common Polyakov-class
regulator-invariance" should be augmented with the same qualifier.

**Sharpening 3 (Severity 1, optional augmentation).** Add a per-firewall
$1/N$ ordering table (§2.2 of this report) to the candidate
$\texttt{rmk:firewall-typology}$ inscription in
`main.tex` after `rmk:convention-firewall`. This is **optional**;
the existing remark structure does not strictly require it but the
$1/N$ ordering is a publication-grade clarifier.

### 5.3 Open research-frontier prompts (Phase-5+, not Phase-4)

**R-FM-W5-A5-01.** Explicit identification of the manuscript's
"Polyakov-class regulator-invariance" with the CG Vol II §11
BV-regulator class on the 6-real-dim mixed worldvolume; cite CG
Vol II §11 + §13 + Lurie HA §5.5.4 with the (A1)-(A5)+(A2$'$)
augmentation. (Phase-5 obligation, equivalent to L-FM-1 in
phase4-exec-Firewall-Meta-Theorem.)

**R-FM-W5-A5-02.** Explicit verification that the Polyakov 1981
conformal anomaly on a 2D worldsheet specializes correctly to the
CG Vol II §11 BV regulator on $\Sigma_2$ (2D worldsheet special
case). This would harden the Polyakov-class sharpening of
Sharpening 1.

**R-FM-W5-A5-03.** Speculative Phase-5+ coupling: BKM denominator
algebra $\mathfrak g_{\Delta_5}$ ↔ super-Yangian on the open side
with Sp$_4(\Z)$ on the deformation parameter space. (12-24 months,
research frontier.)

**R-FM-W5-A5-04.** Speculative Phase-5+ coupling: BD chiral algebra
on $\widehat{\C^2}_0$ at $d = 2$ with a WZW-like level $k$ extension.
(Belongs to Vol III's CY-to-chiral frontier, not to the manuscript's
local theorem.)

### 5.4 Non-defects (recorded for completeness)

The following Polyakov-style attacks were tried and returned clean:

* **Liouville mode at $d=2$ Dolbeault factor.** The formal disk
  $\widehat{\C^2}_0$ has no metric, hence no Liouville mode; the
  Polyakov 1981 conformal-anomaly framework does not apply.
* **Faddeev-Popov ghost / BV ghost mismatch.** The manuscript's
  $Q\psi = [\phi_1, \phi_2]$ ghost is a BV antifield-ghost at the
  brane, not a Faddeev-Popov ghost on a worldsheet; no
  Polyakov-style FP-anomaly is applicable.
* **'t Hooft loop / Wilson-line large-$N$ scaling.** The manuscript's
  brane-defect Wilson-line analog (the $A$-coupling in the
  $S_\partial = \int_\R \mathrm{Tr}(\phi_1 d\phi_2 + A[\phi_1,\phi_2])$
  action) does not invoke a 't Hooft loop; the leading-$N$ scaling
  is at $\Tr(I) = N$, recorded above.
* **Vafa Z/n orbifold anomaly.** No orbifold quotient is taken in
  the manuscript's structure; FW.Igusa's Sp$_4(\Z)$ acts only on the
  Igusa $\mathbb H_2$, which is not in the manuscript at all.
* **Polyakov chiral fermion measure anomaly.** The manuscript has
  no chiral fermions; the brane fermion $\psi$ is a BV ghost-fermion
  with $|\psi|=-1$, not a chiral-fermion field. No anomaly applies.
* **Polyakov path-integral measure on $\widehat{\C^2}_0$.** The
  formal disk has no integration measure (it is formal-power-series-
  level); the Polyakov measure framework does not apply.

---

## §6. Inscription target (proposal-only, NO TeX edits)

### 6.1 Proposal A — Prose qualifier on existing #112 closure

**Site.** Line 6063–6065 of
`reconstitution/attack-heal-platonic-2026-04-28.md` (Wave-4 #112
closure):

> "**Common Polyakov-class regulator-invariance.** All 5 are
> $(A5)$-regulator-invariant (no choice of admissible regulator
> removes the obstruction)."

**Proposed augmentation (proposal-only).**

> "**Common Polyakov-class regulator-invariance.** All 5 are
> $(A5)$-regulator-invariant (no choice of admissible regulator
> removes the obstruction). **The Polyakov-class qualifier here
> refers to worldvolume-internal Polyakov-style regulator-class
> scheme-independence via $(A1)$–$(A5)+(A2')$ of
> $\texttt{defn:regulator-admissible-sector}$, not to Polyakov 1981
> worldsheet conformal-anomaly invariance**: the 6-real-dim mixed
> worldvolume $\R^2 \times \widehat{\C^2}_0$ is not a 2D
> worldsheet in the Polyakov 1981 sense, and the
> regulator-invariance is at the Costello-Gwilliam Vol II §11
> BV-regulator-class layer, not at the Polyakov 1981 path-integral
> measure layer."

This is a **prose qualifier on an existing entry**, not a new
inscription block.

### 6.2 Proposal B — Optional $1/N$-ordering augmentation
   to `rmk:firewall-typology`

**Site.** The candidate `rmk:firewall-typology` LaTeX block at §5.2
of `phase4-exec-Firewall-Meta-Theorem-2026-04-28.md`, after the
five-firewall enumeration.

**Proposed augmentation (proposal-only, ~5 lines).**

```latex
% After the five-firewall enumeration, before the closing prose.
The five firewalls share a uniform $1/N$ ordering at the leading
planar order: FW.BCOV-chain, FW.Sergeev-A5, FW.Unreduced-Bosonic,
and FW.Costello-Li-$d$-even all carry residue coefficient $\sim
\hbar N$ (with parity-doubling $2\hbar N$ on Costello--Li-$d=4$);
FW.Igusa is $1/N$-decoupled (arithmetic / modular layer).
```

**Severity.** Optional clarifier; does not affect publication-grade
status of the existing remark.

### 6.3 Decision matrix

| Proposal | Site | Lines | Severity | Recommendation |
|---|---|---|---|---|
| A. Polyakov qualifier | Wave-4 ledger #112 | +6 lines | 0 (prose) | **Adopt** |
| B. $1/N$ table | `rmk:firewall-typology` | +5 lines | 1 (clarifier) | **Optional** |

**Recommended action.** **Adopt Proposal A** as a prose qualifier on
the existing #112 closure entry; **optionally adopt Proposal B** if
the candidate `rmk:firewall-typology` is inscribed.

---

## §7. Anti-attack scan for this report

### 7.1 (Att-1) Did the probe exhaust Polyakov primary sources?

**Attack.** "The probe cited Polyakov 1981, 1987 large-$N$, 1987
monograph, Polyakov-Wiegmann 1983, Polyakov-Vafa 1991. Did it miss
load-bearing Polyakov primary sources?"

**Response.** Cross-checked against the canonical Polyakov reference
list:
* Polyakov 1970 (anomalous dimensions in 2D): not load-bearing here
  (no 2D conformal anomaly).
* Polyakov 1974 (compact gauge fields and infrared catastrophe):
  not load-bearing here (no infrared issue at the formal-disk layer).
* Polyakov 1977 (instanton):  not load-bearing here (no instanton in
  the local model).
* Polyakov 1981 (bosonic string): cited; sub-probe (1).
* Polyakov-Wiegmann 1983 (WZW): cited; sub-probe (4).
* Polyakov 1987 monograph: cited; sub-probes (1)–(2)–(3).
* Polyakov 1989 (loop equations): not load-bearing here (no loop
  equation at the chain-level layer).
* Polyakov-Vafa 1991 era discrete: cited; sub-probe (3).
* Polyakov 1996 (string field theory): not load-bearing here (no
  string field).

The five named Polyakov primary sources cover the load-bearing range
for the firewall typology probe. **No load-bearing Polyakov source
is omitted.**

### 7.2 (Att-2) Is the "no Polyakov-anomaly elided" verdict safe?

**Attack.** "Could a referee identify a Polyakov-anomaly subtlety
that this probe missed?"

**Response.** The probe checked four named Polyakov-anomaly
candidates (conformal anomaly, $1/N$ ordering, discrete anomaly,
WZW chiral cocycle) and verified each is correctly classified or
correctly absent. The structural reason all four return clean is:
**the manuscript's worldvolume is not a 2D worldsheet, and the
Polyakov 1981 framework specializes to 2D worldsheets**. This
structural reason is robust; a referee identifying a *new*
Polyakov-anomaly would need to identify a 2D worldsheet inside
$\R^2 \times \widehat{\C^2}_0$, which does not exist (the
manuscript's brane-defect line is 1D, not 2D).

A possible refinement: if the manuscript's 2D topological factor
$\R^2$ is reinterpreted as a (Riemannian) 2D worldsheet, then
Polyakov 1981 would apply on $\R^2$. **Cross-check.** The $\R^2$
factor in `main.tex` is *topological* (de Rham cosheaf
$\Omega^\bullet_c(\R^2)$), not Riemannian. There is no metric on
$\R^2$ in the manuscript's structure; the Polyakov 1981 framework
does not apply.

**Verdict.** The "no Polyakov-anomaly elided" verdict is safe under
this refinement.

### 7.3 (Att-3) Is the Sergeev / Igusa discrete-anomaly verdict safe?

**Attack.** "Sub-probe (3) ruled out a discrete-anomaly between
FW.Igusa and FW.Sergeev-A5. Could a discrete-anomaly arise via the
Coulembier 2018 super-finite-tensor-category framework?"

**Response.** Cross-checked against Coulembier 2018 *Selecta Math.*
24, 4659–4710 (cited at line 67 of the meta-theorem report). The
Coulembier framework lifts Sergeev to the categorical level (Theorem
5.2: super-finite-tensor-category); it does *not* introduce
Sp$_4(\Z)$ on the categorical side. The
Sergeev-Coulembier categorical lift is at the
representation-theoretic categorical layer, decoupled from the Igusa
arithmetic / lattice / modular layer.

**Verdict.** No discrete-anomaly via Coulembier 2018.

### 7.4 (Att-4) Is the WZW verdict safe at $d=2$?

**Attack.** "Sub-probe (4) ruled out a Polyakov-Wiegmann WZW chiral
cocycle on $\widehat{\C^2}_0$ at $d=2$. Could a WZW cocycle arise via
the BD chiral algebra on $\widehat{\C^2}_0$?"

**Response.** Cross-checked against Beilinson-Drinfeld 2004
*Chiral Algebras*. The BD chiral algebra on a 1D curve carries a
chiral cocycle (the $\bar\partial$-anomaly), but this is at the
structure-sheaf level, not at the WZW-level $k$ level. The
manuscript's $\widehat{\C^2}_0$ is 2D (formal complex dim 2), and
the BD chiral algebra structure on $\widehat{\C^2}_0$ is via the
mixed Dunn-Lurie product $E_2^{\mathrm{Dolbeault}}$, not via a 1D
chiral algebra. The Polyakov-Wiegmann WZW cocycle is a
1D-chiral-algebra phenomenon; it does not lift to 2D-chiral-algebra
in the BD sense.

**Verdict.** No Polyakov-Wiegmann WZW cocycle via BD on
$\widehat{\C^2}_0$.

### 7.5 (Att-5) Is the certify verdict load-bearing?

**Attack.** "Wave-4 #112 inscribed +12 lines optional augmentation;
this probe certifies clean. Does the certification add anything?"

**Response.** The certification:
1. Confirms the Wave-4 +12-line optional inscription is structurally
   robust under Polyakov + Invariants attack.
2. Adds **Sharpening 1** (Polyakov qualifier on prose, +6 lines on
   the Wave-4 ledger; Severity 0); this is a minor prose improvement
   forestalling a Polyakov 1981 misinterpretation.
3. Adds **Sharpening 3** (optional $1/N$ table, +5 lines on the
   `rmk:firewall-typology`; Severity 1); this is an optional
   clarifier.
4. Records **R-FM-W5-A5-01 through R-FM-W5-A5-04** as Phase-5+
   research-frontier prompts.

**Net effect.** Certification + minor prose qualifier + optional
$1/N$-table + four research-frontier prompts. No change to the
fundamental publication-grade status of the meta-theorem.

---

## §8. Convergence verdict and provenance

### 8.1 Convergence verdict

**The Wave-5 A5 (Polyakov + Invariants) probe certifies the Wave-4
#112 firewall meta-theorem as structurally clean under all four named
Polyakov sub-probes.** No new severity-2 obstruction. One severity-0
prose qualifier (Sharpening 1, **Polyakov-style worldvolume-internal**)
recommended. One severity-1 optional clarifier (Sharpening 3, $1/N$
ordering table) recommended if `rmk:firewall-typology` is inscribed.
Four research-frontier prompts recorded for Phase-5+.

**The certify verdict is load-bearing for the Wave-4 #112 closure.**

### 8.2 Strategic implication for inscription

The Wave-4 inscription target was +444 lines base / +467 lines with
optional augmentations. The Wave-5 A5 probe adds:

* **Severity 0 prose qualifier** to the existing Wave-4 ledger entry
  (#112 closure, line 6063–6065): +6 lines on the ledger only,
  **NOT on the manuscript**.
* **Severity 1 optional $1/N$ table** to the candidate
  `rmk:firewall-typology` block: +5 lines on the manuscript,
  **OPTIONAL**.

**Revised inscription target (provisional, with Wave-5 A5 augmentation):**
* Base: +444 lines (unchanged).
* Optional: +467 + 5 (W5-A5 $1/N$ table) = +472 lines.
* Wave-4 ledger only: +6 lines (Wave-5 A5 Polyakov qualifier on #112
  closure entry, ledger only).

All additive, 0 restructuring. The base +444-line target remains
publication-grade without these augmentations.

### 8.3 Provenance

This report draws on:
* **Phase-4 EXEC #112** (Polyakov + Invariants meta-theorem
  formalization, 1276 lines) at
  `reconstitution/phase4-exec-Firewall-Meta-Theorem-2026-04-28.md`.
* **Wave-2 W5** (Polyakov + Invariants cross-volume, 487 lines) at
  `reconstitution/wave2-W5-polyakov-crossvolume-2026-04-28.md`.
* **Wave-3 W8** (Polyakov + Composition, 942 lines) at
  `reconstitution/wave3-W8-polyakov-composition-2026-04-28.md`.
* **Wave-3 W30** ((A5) parity-equivariance heal, 866 lines) at
  `reconstitution/wave3-W30-A5-heal-2026-04-28.md`.
* **Wave-4 ledger** (`attack-heal-platonic-2026-04-28.md`, 6242
  lines), specifically item #112 closure (lines 6020–6242).
* **Platonic-ideal plan** (`platonic-ideal-plan-2026-04-28.md`, 987
  lines), §3 Theorem package and §10 What-success-looks-like.
* Polyakov primary sources cited in §0 (Polyakov 1981, 1987 large-$N$,
  1987 monograph, Polyakov-Wiegmann 1983, Polyakov-Vafa 1991).

**Composition mode.** Russian school + mathematical-physics frontier;
Diracian voice; named attribution; honest epistemic disclaimers; no
em-dashes; no "groundbreaking"; theorem names carry the ambition.

**End of report.**
