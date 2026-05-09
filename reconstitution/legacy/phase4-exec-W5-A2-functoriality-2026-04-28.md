# Phase-4 EXEC W5-A2 — Drinfeld+Functoriality inscription-covariance attack

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** A2 = Drinfeld + Functoriality (chiral / factorization
functoriality, BD §3.5; Lurie HA §5.5.4 covariance proofs; Drinfeld
1986/1989/1990 quasi-Hopf / quasi-triangular structure).
**Mode.** Wave-5 attack on the proposed Phase-4 inscription itself.
Proposal-only. **No commits, no manuscript edits, no edits to other
ledger files** beyond this report and the 200-word append to
`reconstitution/attack-heal-platonic-2026-04-28.md`.
**Target.** The +444-line (or +467-line with #105/#112 augmentations)
inscription proposal certified by W4 #110 P4-Symp-Functoriality
closure.

**Question.** The W4 #110 closure classifies Phase-4 discharges into
four functoriality classes (PARABOLIC / FULL / INDEPENDENT /
HOLOMORPHIC) and concludes that the +444-line inscription requires
**no** functoriality-related deltas. This audit asks whether the
proposed inscription text *itself* — the LaTeX that will be written
into `claim-strength-ledger.tex` and `main.tex` — preserves the
covariance structure W4 #110 certified at the closure-of-discharges
level, or whether it instead silently breaks the parabolic /
full / independent / holomorphic distinctions when read off the
page by a Drinfeld-functoriality-aware referee.

**Posture.** A Drinfeld-functoriality referee reads each inscribed
sentence and asks: under what subgroup of $\mathrm{Symp}_{\mathrm{form}}$
is this sentence covariant, and is that subgroup the one the W4
classification assigned to the underlying discharge? If a sentence
silently breaks parabolic-covariance (mentions $z_1$ in a
non-parabolic-equivariant way), if it silently inflates parabolic
to full (claims FULL where only PARABOLIC is supportable), or if it
silently merges functoriality classes (PARABOLIC and FULL handled by
the same prose), the inscription is not faithful to the W4 #110
classification regardless of how the underlying discharge passes.

---

## §0. Executive verdict

**Three structural attacks; two land; one borderline.** The proposed
inscription has the following functoriality-covariance defects:

1. **Attack F''-A1 (LANDS, severity 2 / minor — load-bearing remark
   recommended).** The F'' theorem statement at `claim-strength-ledger.tex`
   line-delta 56 (option-(c) theorem block) names the column-Verma
   $\widehat M_0$ as "m-adic-completed at $\mathfrak m = (z_1)$"
   without explicitly stating that the resulting BV complex is
   $P_{(z_1)}$-equivariant only (not full
   $\mathrm{Symp}_{\mathrm{form}}$-equivariant). A
   Drinfeld-functoriality referee cannot recover the parabolic
   restriction from the inscription alone; the parabolic classification
   from W4 #110 is invisible at the point where the F'' theorem is
   read. This is not a sign error or a wrong claim; it is an
   **under-specification** that breaks the BD §3.5 cross-walk.

2. **Attack MHB-A1 (LANDS, severity 2 / minor — load-bearing
   strengthening recommended).** The (A2$'$) hypothesis statement in
   the master hypothesis block at line-delta 267 uses
   "ad-invariant supersymmetric bilinear form" without specifying
   the Lie-source action under $\mathrm{Symp}_{\mathrm{form}}$. The
   ad-invariance condition is functorial only under the inner
   automorphism group $\mathrm{Inn}(\mathfrak g) \subset
   \mathrm{Aut}(\mathfrak g)$, not under outer automorphisms induced
   by $\mathrm{Symp}_{\mathrm{form}}$ acting on the second tensor
   factor of $\mathfrak g \otimes \widehat A$. The Drinfeld 1989 /
   1990 quasi-triangular setup distinguishes exactly this: the
   $r$-matrix ad-invariance is preserved by $\mathrm{Inn}$, but
   conjugation by an outer twist changes the $r$-matrix datum
   (Drinfeld twist). The inscription must specify that
   $\mathrm{Symp}_{\mathrm{form}}$ acts only on the $\widehat A$
   factor (not the $\mathfrak g$ factor), making the (A2$'$)
   condition $\mathrm{Symp}_{\mathrm{form}}$-trivially preserved
   regardless of inner / outer distinction. Without this
   specification, the (A2$'$) inscription leaves the door open to a
   referee asking "is (A2$'$) preserved under the
   $\mathrm{Symp}_{\mathrm{form}}$-action you are asserting in F''?",
   and the answer requires the tensor-factor disjointness statement
   that the inscription does not currently make explicit.

3. **Attack FT-A1 (BORDERLINE, severity 1 / cosmetic).** The
   firewall-typology remark (#112 augmentation, +12 lines) at
   `rmk:firewall-typology` lists five firewall species (FW.BCOV,
   FW.Sergeev-Howe, FW.Igusa, FW.Unreduced-Bosonic,
   FW.Costello-Li-d-even) without distinguishing their
   $\mathrm{Symp}_{\mathrm{form}}$-functoriality classes. The
   FW.BCOV and FW.Costello-Li firewalls are FULL-holomorphic
   functorial; the FW.Sergeev-Howe is FULL-trivial (matrix-factor
   only); the FW.Unreduced-Bosonic is PARABOLIC (m-adic completion);
   the FW.Igusa is $\mathrm{Symp}_{\mathrm{form}}$-INDEPENDENT
   (modular-form-theoretic). The remark prose makes no such
   distinction, **implicitly merging PARABOLIC and FULL** classes
   under the umbrella "structural permanence". This is the
   borderline case: the merger is not a logical error (the
   firewall-permanence claim holds in each functoriality class),
   but it loses the W4 #110 typology granularity at the point of
   inscription. **A one-line annotation** distinguishing the
   functoriality class per FW species would heal this.

**Verdict.** **Two minor strengthenings recommended; one cosmetic
clarification optional.** The base +444-line inscription target
**remains publication-grade**; the recommended strengthenings are
**load-bearing** in the sense that without them a
Drinfeld-functoriality-aware referee can ask covariance questions
that the inscription does not currently answer. The strengthenings
are **additive and small** (estimated +6 lines total, distributed
across the F'' theorem block, the (A2$'$) hypothesis block, and
optionally the firewall-typology remark).

---

## §1. Attack F''-A1: Theorem F'' at line-delta 56 — parabolic
restriction invisibility

### §1.1 The proposed inscription text

The F'' theorem block (option-(c), line-delta 47 of the 56-line
total) at `claim-strength-ledger.tex` reads in part:

> Let $\widehat L = \mathfrak g \otimes \widehat A$ be the
> m-adic-completed super-local Lie algebra on the formal symplectic
> 2-disk, with $\widehat A = \C[[z_1, z_2]]$ and $\bar A = \widehat A
> / \C \cdot 1$. Let $\widehat M_0 \subset \widehat L$ be the
> column-Verma at $a = 0$ m-adic-completed at $\mathfrak m = (z_1)
> \subset \widehat A$. Let $\mathrm{Symp}_{\mathrm{form}}(\C^2, 0)$
> act on the second tensor factor via the Hamiltonian-Lie algebra
> exponential...

The phrase "m-adic-completed at $\mathfrak m = (z_1)$" appears once;
the phrase "$\mathrm{Symp}_{\mathrm{form}}$ acts on the second tensor
factor" appears once. Nowhere does the inscription state explicitly
that the **action is $P_{(z_1)}$-restricted** rather than
full-$\mathrm{Symp}_{\mathrm{form}}$.

### §1.2 The Drinfeld-functoriality breakage

A Drinfeld-functoriality referee reads this as follows. The
$\mathrm{Symp}_{\mathrm{form}}$-action on the second tensor factor
is a group action on $\widehat A$. The m-adic completion at
$\mathfrak m = (z_1)$ is a separate datum: it is the
$\mathfrak m$-adic topology on $\widehat A$. **Group actions on
$\widehat A$ that do not preserve the topology do not extend to
the completion.** The natural diagram

\[
\begin{array}{ccc}
\mathfrak g \otimes \widehat A & \xrightarrow{\mathrm{id} \otimes \varphi^*} &
\mathfrak g \otimes \widehat A \\
\widehat{\phantom{X}} \downarrow & & \downarrow \widehat{\phantom{X}} \\
\widehat L & \xrightarrow{?} & \widehat L
\end{array}
\]

commutes if and only if $\varphi$ preserves $\mathfrak m$, i.e.,
$\varphi \in P_{(z_1)}$. For non-parabolic $\varphi$ (e.g.,
$\varphi: z_1 \mapsto z_1 + z_2$), the bottom arrow does not exist
because $\varphi^*$ maps m-adic-convergent series to non-m-adic-convergent
series.

The inscription asserts "$\mathrm{Symp}_{\mathrm{form}}$ acts on the
second tensor factor" without restricting to $P_{(z_1)}$; this is
**literally false** at the level of the m-adic-completed BV complex
$\widehat L$. The W4 #110 closure correctly identifies this as the
PARABOLIC class; the proposed inscription however does not transmit
this restriction to the reader.

### §1.3 Drinfeld 1986 / 1989 / 1990 covariance precedent

Drinfeld 1986 ("Quantum groups", *Proc. ICM Berkeley*) introduces
quantum groups as Hopf-algebra deformations functorial under the
group of base-changes preserving the deformation parameter. Drinfeld
1989 ("Quasi-Hopf algebras", *Leningrad Math. J.* 1) generalizes to
**quasi-Hopf algebras**, where functoriality is restricted to a
**twist groupoid**: the Drinfeld twist $F \in A \otimes A$
intertwines two quasi-Hopf structures via $F \cdot \Phi$ where
$\Phi$ is the associator. The functoriality class of a quasi-Hopf
algebra is **the stabiliser of $\Phi$**, not the full automorphism
group. Drinfeld 1990 ("Quasi-triangular quasi-Hopf algebras", in
*Algebraic Analysis*) extends to quasi-triangular, where the
$r$-matrix is **functorial under the same stabiliser** (preserving
both $\Phi$ and the universal $R$).

**Application to F''.** The m-adic completion datum
$(\mathfrak g \otimes \widehat A, \mathfrak m)$ is a quasi-Hopf-style
datum: the pair of underlying algebra plus distinguished structure
(the m-adic ideal). Its functoriality class is the **stabiliser of
$\mathfrak m$**, which is exactly $P_{(z_1)}$ in the
$\mathrm{Symp}_{\mathrm{form}}$ language. **Drinfeld's covariance
precedent therefore mandates that the inscription state the
parabolic restriction explicitly**, not assume the reader will
recover it from the m-adic-completion phrase.

### §1.4 BD §3.5 cross-walk failure

Beilinson-Drinfeld §3.5 (Chiral Algebras, AMS Colloq. 51) defines
chiral algebras as $\mathcal D$-modules on the Ran space functorial
under the **groupoid of formal-coordinate changes preserving the
chosen formal point**. When localized at a closed point $x \in X$,
the chiral algebra functoriality restricts to the **stabiliser**
$\mathrm{Aut}(\widehat{\mathcal O}_{X,x}, \mathfrak m_x) = P_{x}$
of the maximal ideal. Our $P_{(z_1)} \subset \mathrm{Symp}_{\mathrm{form}}$
is the symplectic version of this exact construction.

**The W4 #110 closure correctly cites this BD §3.5 cross-walk** as
the structural justification for the PARABOLIC class. **The proposed
inscription does not transmit this cross-walk to the reader**: the
phrase "BD §3.5 cross-walk" never appears in the F'' theorem block
or in its accompanying remark `rmk:joint-Fpp-status`. A
Drinfeld-functoriality referee can therefore correctly criticize:
"The W4 audit cites BD §3.5; the inscription does not. The
parabolic structure is invisible at the page where it is most
load-bearing."

### §1.5 Lurie HA §5.5.4 covariance audit

Lurie *Higher Algebra* §5.5.4 establishes that the symmetric
monoidal functor structure on $\mathrm{Pr}^L$ (presentable
$\infty$-categories) is functorial under symmetric monoidal
equivalences preserving the chosen tensor product. For our setting,
the $E_2$-tensor structure on the BV complex is functorial under
the **subgroup of $\mathrm{Symp}_{\mathrm{form}}$ preserving the
$E_2$-coherence data**, which is exactly $P_{(z_1)}$ at the
chain level (the $E_2$-coherence at the column-Verma uses the
m-adic filtration as its "small object" data; non-parabolic
automorphisms break this).

The Lurie covariance audit therefore **also mandates the parabolic
restriction in the inscription**. The proposed inscription does not
cite Lurie HA §5.5.4 in the F'' theorem block.

### §1.6 Recommended healing strengthening

**Recommended strengthening (severity 2 / minor — load-bearing
remark).** Add one sentence to the F'' theorem block, immediately
after the sentence "Let $\mathrm{Symp}_{\mathrm{form}}(\C^2, 0)$ act
on the second tensor factor via the Hamiltonian-Lie algebra
exponential..." interpretation:

> Concretely, the action restricts to the parabolic stabiliser
> $P_{(z_1)} = \{\varphi \in \mathrm{Symp}_{\mathrm{form}} :
> \varphi^* \mathfrak m \subset \mathfrak m\}$ of the m-adic ideal,
> in line with the BD §3.5 cross-walk for chiral algebras localized
> at a closed point and the Lurie HA §5.5.4 $E_2$-coherence
> structure on the column-Verma.

**Estimated line-delta.** **+3 lines** (one sentence in the
theorem statement + comment line).

**Alternative healing path.** Add an analogous one-sentence
clarification to the accompanying `rmk:joint-Fpp-status` remark
(line-delta currently 17 lines). This is also +3 lines.

**Either healing path** closes the F''-A1 attack; both is
redundant.

### §1.7 Severity classification

**Severity 2 / minor (load-bearing remark recommended).**
Justification: the W4 #110 closure correctly identifies the
PARABOLIC class as the natural symmetry, not a forced restriction.
The discharge **passes** in the parabolic class. The attack lands
not on the underlying mathematics but on the inscription's failure
to **transmit the parabolic structure to the reader**. A
Drinfeld-functoriality-aware referee can correctly raise this as a
clarity defect; the strengthening heals the defect with three
additive lines.

---

## §2. Attack MHB-A1: Master hypothesis block (A2$'$) at line-delta
267 — outer-automorphism gap

### §2.1 The proposed inscription text

The (A2$'$) hypothesis block at line-delta 267 of the master
hypothesis block (the 38-line `\hyp`-block subsidiary at
$\sim$ master line 56–94 if normalized) reads:

> When the open matrix source is a $\Z/2$-graded super-Lie algebra
> $\mathfrak g$, there exists an even non-degenerate **ad-invariant**
> supersymmetric bilinear form $g \colon \mathfrak g \otimes
> \mathfrak g \to \C$ used to construct the BV pairing. Concretely:
> $g$ has parity $0$, satisfies $g(X, Y) = (-1)^{|X||Y|} g(Y, X)$,
> and $g([Z, X], Y) + (-1)^{|Z||X|} g(X, [Z, Y]) = 0$.

The **ad-invariance** condition $g([Z, X], Y) + (-1)^{|Z||X|}
g(X, [Z, Y]) = 0$ is the standard infinitesimal invariance under
the **adjoint action** of $\mathfrak g$ on itself. This is functorial
under $\mathrm{Inn}(\mathfrak g) = $ inner automorphisms (group
generated by $\exp(\mathrm{ad}\, X)$ for $X \in \mathfrak g$).

### §2.2 The Drinfeld-functoriality breakage

For a generic Lie superalgebra $\mathfrak g$, the automorphism group
$\mathrm{Aut}(\mathfrak g)$ properly contains $\mathrm{Inn}(\mathfrak g)$.
The quotient $\mathrm{Out}(\mathfrak g) = \mathrm{Aut}(\mathfrak g)
/ \mathrm{Inn}(\mathfrak g)$ — the **outer automorphism group** — can
act non-trivially on bilinear forms even when ad-invariance is
preserved.

**Drinfeld 1989 quasi-Hopf example.** Drinfeld 1989 §1.7 shows that
inner / outer Hopf-twist conjugation **distinguishes**: an inner
twist by $F = \exp(\mathrm{ad}\, X) \otimes \mathrm{id}$ preserves
the $r$-matrix; an outer twist (e.g., the involution $X \mapsto -X^t$
on $\mathfrak{sl}_n$) sends $r \mapsto -r^{21}$, a different
$r$-matrix datum. The outer twist datum is **functorial in a
different group** than the inner twist datum.

**Application to (A2$'$).** The Sergeev form $B_0(X, Y) =
\frac{1}{2}\Tr(\ev XY + \ev YX)$ on $\mathfrak q(N)$ is
ad-invariant. But under the outer involution $\sigma: X \mapsto -X^*$
(supertranspose composed with sign), $B_0$ is sent to $-B_0$ (a
sign change). On $\mathfrak{psl}(N|N)$, the outer automorphism group
is $\Z/2 \times \Z/2$ (Kac 1977 §2.5.5); both Killing forms vanish,
but the bilinear forms induced by lifts to $\mathfrak{sl}(N|N)$ differ
by outer signs.

**The (A2$'$) hypothesis as currently inscribed is silent on this**:
it asserts the existence of an even non-degenerate ad-invariant form
without specifying functoriality under outer automorphisms.

### §2.3 The Drinfeld functoriality question for F''

**Question.** In F'', the open matrix source is
$\mathfrak{gl}(N|N)$. The $\mathrm{Symp}_{\mathrm{form}}$-action is
on the **second tensor factor** $\widehat A$, not on the matrix
factor $\mathfrak g$. **Therefore $\mathrm{Symp}_{\mathrm{form}}$
does not act on the (A2$'$) form directly** — the form is matrix-factor
data, the action is target-factor data. Tensor-factor disjointness
gives functoriality trivially.

**However**, the inscription does not state this tensor-factor
disjointness explicitly in the (A2$'$) block. The (A2$'$) block
introduces ad-invariance but does not state that the form is
**$\mathrm{Symp}_{\mathrm{form}}$-trivially preserved** by living
in the matrix factor.

A Drinfeld-functoriality referee can ask: "F'' asserts
$\mathrm{Symp}_{\mathrm{form}}$-equivariance on $\widehat L =
\mathfrak g \otimes \widehat A$. The (A2$'$) form $g$ is part of
the BV pairing on $\widehat L$. Is $g$
$\mathrm{Symp}_{\mathrm{form}}$-equivariant?" The answer is yes,
trivially, because $g$ acts on $\mathfrak g$ alone — but the
inscription does not say so.

### §2.4 BD §3.5 + Drinfeld covariance precedent

Beilinson-Drinfeld §3.5 cross-walk: chiral algebras factor through
the **product** of (matrix-factor automorphism group) $\times$
(target-factor coordinate-change group). Functoriality on each
factor is independent. Drinfeld 1989 / 1990: the $r$-matrix /
form data on the matrix factor is functorial under
$\mathrm{Aut}(\mathfrak g)$ alone; the symplectic-disk coordinate
change is functorial under $\mathrm{Symp}_{\mathrm{form}}$ alone.

**The two functorialities are independent.** The proposed (A2$'$)
inscription, by not stating tensor-factor disjointness, leaves the
joint functoriality structure ambiguous.

### §2.5 Recommended healing strengthening

**Recommended strengthening (severity 2 / minor — load-bearing
strengthening).** Add one comment-line at the end of the (A2$'$)
hypothesis block:

> %% Functoriality: $g$ acts on the matrix factor only; under
> %% $\mathrm{Symp}_{\mathrm{form}}$ on the target factor, $g$ is
> %% trivially preserved by tensor-factor disjointness. (A2$'$) is
> %% functorial under $\mathrm{Inn}(\mathfrak g)$ on the matrix
> %% factor (Drinfeld 1989, 1990 inner-twist precedent); outer
> %% automorphisms of $\mathfrak g$ may change $g$ by a sign and
> %% are not within the operative scope of W22-T1 / T2 / P4-G3-T-A1
> %% discharges.

**Estimated line-delta.** **+5 lines** (six comment lines including
% prefixes; one is empty).

**Why comment-form rather than visible prose.** The
tensor-factor disjointness is operative-but-trivial: the F''
discharge does not depend on it explicitly, only on the
**absence** of a coupling. Documenting it as a comment line
clarifies the audit trail without burdening the visible (A2$'$)
prose.

### §2.6 Severity classification

**Severity 2 / minor (load-bearing strengthening).**
Justification: the inner / outer distinction is real (Drinfeld
1989 quasi-Hopf precedent + Kac 1977 outer automorphism group on
$\mathfrak{psl}(N|N)$). The discharge **passes** because the
F'' setup tensors $\mathfrak g$ with $\widehat A$ and the
$\mathrm{Symp}_{\mathrm{form}}$ action is on $\widehat A$ only.
The attack lands on the inscription's failure to **document the
tensor-factor disjointness** that makes the functoriality
question moot. A six-comment-line annotation closes this.

---

## §3. Attack FT-A1: Firewall-typology remark — implicit
PARABOLIC / FULL merger

### §3.1 The proposed inscription text

The firewall-typology remark (#112 augmentation, +12 lines, at
`rmk:firewall-typology` after `rmk:convention-firewall` in
`main.tex`) contains five firewall species:

- **(FW1) BCOV chain-level firewall.**
- **(FW2) Sergeev-Howe open-line firewall.**
- **(FW3) Igusa modular firewall.**
- **(FW4) Bosonic discharge firewall.**
- **(FW5) Costello-Li $d$-odd parity firewall.**

The umbrella sentence reads:

> These five firewalls share a uniform structural property: they
> obstruct chain-level matched-conventions functors at the
> vertex-class layer of the 6-real-dim mixed
> topological-holomorphic factorization-algebra category
> $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$ on
> $\R^2 \times \widehat{\C^2}_0$.

### §3.2 The functoriality-class merger

Each of the five firewalls has a different
$\mathrm{Symp}_{\mathrm{form}}$-functoriality class per W4 #110:

| Firewall | W4 #110 functoriality class | Rationale |
|----------|------------------------------|-----------|
| FW1 BCOV | FULL holomorphic | flat $\C^d$, no m-adic completion |
| FW2 Sergeev-Howe | FULL trivial | matrix-factor only |
| FW3 Igusa | $\mathrm{Symp}_{\mathrm{form}}$-INDEPENDENT | modular-form data |
| FW4 Unreduced-Bosonic | PARABOLIC | m-adic completion at $\mathfrak m$ |
| FW5 Costello-Li $d$-even | FULL holomorphic | flat $\C^d$ |

The proposed remark, by stating "uniform structural property at the
vertex-class layer", **implicitly merges PARABOLIC (FW4) and FULL
(FW1, FW2, FW5) and INDEPENDENT (FW3) classes** under the umbrella
of "structural permanence". This is not a logical error: the
structural-permanence claim holds in each functoriality class.
**But it loses the W4 #110 typology granularity** at the inscription.

### §3.3 The Drinfeld-functoriality referee's interpretation

A Drinfeld-functoriality referee reads the firewall-typology remark
and asks: "These five firewalls all live in
$\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$. What is the
functoriality structure of this category? Is each firewall
functorial under the same group?" The remark gives no answer.

The W4 #110 audit gives the precise answer: each firewall has a
**different** functoriality class. The remark, by not transmitting
this, allows the referee to **wrongly assume** uniformity of
functoriality class. This is a borderline cosmetic vs. load-bearing
defect.

### §3.4 BD §3.5 cross-walk on the merger

Beilinson-Drinfeld §3.5 cross-walks: chiral-algebra functors are
classified by their **functoriality groupoid** (the group of
coordinate / formal-point changes for which the functor is
natural). Two chiral functors with **different functoriality
groupoids** are not the same datum, even if they share a
structural-permanence property at one layer.

The five firewalls have different functoriality groupoids; the
remark elides this. **This is the BD §3.5 cross-walk failure**: the
remark asserts a uniform structural permanence without acknowledging
that the structural-permanence theorem is internal to each
functoriality class separately.

### §3.5 Recommended healing strengthening (optional)

**Recommended strengthening (severity 1 / cosmetic — optional).**
Add one sentence to the firewall-typology remark, immediately
before the umbrella sentence:

> Each of the five firewalls is permanent within its own
> $\mathrm{Symp}_{\mathrm{form}}$-functoriality class:
> (FW1) and (FW5) within the FULL holomorphic class, (FW2) within
> the matrix-factor-trivial class, (FW3) within the
> $\mathrm{Symp}_{\mathrm{form}}$-independent modular class, and
> (FW4) within the PARABOLIC class. Permanence is internal to
> each class; cross-class lifting is not asserted.

**Estimated line-delta.** **+3 lines** (one sentence).

**Why optional rather than mandatory.** The firewall-typology remark
is structurally classification-grade prose; the missing distinction
is the granularity at which W4 #110 operates. A Drinfeld referee
can correctly criticize the merger, but the criticism is
cosmetic-grade: the underlying mathematics is correct. The
strengthening is therefore optional, not mandatory.

### §3.6 Severity classification

**Severity 1 / cosmetic (optional clarification).**
Justification: the merger is not a logical error; the
structural-permanence claim is correct in each functoriality class
separately. The attack lands on the remark's failure to **make the
classes visible**, which is a clarity defect, not a correctness
defect. The +3-line strengthening heals it cosmetically.

---

## §4. Aggregate verdict and proposed line-delta

**Total proposed line-delta from W5-A2 attack-heal:** **+11 lines**.

Distribution:
- **Mandatory (load-bearing) strengthenings (+8 lines).**
  - F''-A1 strengthening at line-delta 56 (one healing path):
    +3 lines.
  - MHB-A1 strengthening at line-delta 267 (comment block):
    +5 lines.
- **Optional (cosmetic) clarification (+3 lines).**
  - FT-A1 clarification at firewall-typology remark: +3 lines.

**Revised inscription target with W5-A2 strengthenings:**

| Component | Existing | Base delta | W5-A2 delta | Total |
|-----------|----------|------------|-------------|-------|
| F'' theorem block | 0 | +56 | **+3** | **+59** |
| Master hypothesis block | 0 | +267 | **+5** | **+272** |
| Firewall typology (#112) | 0 | +12 | **+3** (optional) | **+15** |
| All other blocks | (per W4 #110) | (no change) | 0 | (no change) |
| **Manuscript total** | — | **+444 base** | **+8 mandatory + 3 optional** | **+452 mandatory / +455 with optional** |

(With the #112 firewall-typology +12 augmentation:
**+456 base + 8 mandatory + 3 optional = +467 mandatory / +470 with
optional.**)

**Disruption class.** Each strengthening is **additive only**: an
inserted sentence or a comment block. **Zero rewrites of existing
lines.** Cross-references resolve trivially (no new labels
introduced).

**Verification anchor.** The strengthenings are LaTeX-only edits;
`make` PDF build verifies LaTeX correctness. No new chain-level
script required (the underlying discharges are unchanged).

---

## §5. The W5-A2 attack-heal-summary

**The W4 #110 closure was correct at the discharge level.** The
PARABOLIC / FULL / INDEPENDENT / HOLOMORPHIC classification is
sound, and the +444-line inscription target is publication-grade
**at the underlying discharge level**.

**The W5-A2 attack lands at the inscription level.** The proposed
LaTeX text **does not transmit** the W4 #110 functoriality
classification to the reader at three points: the F'' theorem block
(parabolic invisibility), the (A2$'$) hypothesis block (outer-twist
gap), and the firewall-typology remark (PARABOLIC / FULL merger).

**Heal.** Three additive strengthenings, totalling +8 mandatory + 3
optional = +11 lines. Each strengthening transmits the W4 #110
classification to the inscription. **No mathematical change**; the
strengthenings are clarifications of what is already true.

**Drinfeld-functoriality referee posture.** With the strengthenings,
a Drinfeld-functoriality-aware referee finds the inscription
faithful to the W4 #110 typology: parabolic restriction explicit at
F'', tensor-factor disjointness documented at (A2$'$), functoriality
classes distinguished at the firewall typology. Without the
strengthenings, the referee can correctly raise covariance questions
at each of the three points; the answers exist (they are the W4 #110
audit) but are not on the inscribed page.

**Strategic implication for inscription.** **Authorize the +444-line
target with the +8-line W5-A2 mandatory strengthenings**
(+452 total mandatory). The +3-line firewall-typology clarification
is recommended but optional; user discretion. With the #105 / #112
augmentations, the revised total is **+467 + 8 mandatory + 3 optional
= +475 / +478**.

**No commit. No manuscript edit.** This report is proposal-only,
per the W5 attack-heal mode. Authorship: Raeez Lorgat.

---

## §6. Citations

- **Beilinson-Drinfeld §3.5.** *Chiral Algebras*, AMS Colloquium
  Publications 51 (2004), §3.5 (functoriality of chiral algebras
  under formal coordinate changes; localization at a closed point
  restricts to the stabiliser subgroup).
- **Drinfeld 1986.** "Quantum groups", *Proc. ICM Berkeley* (1986),
  Vol. 1, 798–820 (functoriality of quantum-group deformations
  under base-change).
- **Drinfeld 1989.** "Quasi-Hopf algebras", *Leningrad Math. J.* 1
  (1990), 1419–1457 (Russian original 1989; functoriality classes
  of quasi-Hopf algebras under the twist groupoid; inner / outer
  twist distinction at §1.7).
- **Drinfeld 1990.** "Quasi-triangular quasi-Hopf algebras and a
  group closely connected with $\mathrm{Gal}(\bar{\Q}/\Q)$",
  *Leningrad Math. J.* 2 (1991), 829–860 (Russian original 1990;
  $r$-matrix functoriality under stabiliser of associator).
- **Lurie HA §5.5.4.** *Higher Algebra*, current preprint, §5.5.4
  (covariance proofs for $E_n$-algebras under symmetric monoidal
  equivalences in $\mathrm{Pr}^L$; small-object-argument
  functoriality).
- **Kac 1977.** V. Kac, "Lie superalgebras", *Adv. Math.* 26 (1977),
  8–96, §2.5.5 (outer automorphism group of $\mathfrak{psl}(N|N)$
  is $\Z/2 \times \Z/2$).
- **Sergeev 1984.** A. N. Sergeev, *Mat. Sb.* 124 (1984), 422–430
  (Sergeev form $B_0$ on $\mathfrak q(N)$ ad-invariance).

---

End of Phase-4 EXEC W5-A2 (Drinfeld+Functoriality) report.
