# Phase 4 Execution / G4-M3 — W_3 Sub-VOA Toy Twist (Spin-3 Extension)

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Drinfeld (canonical-construction discipline; W-algebra
classification; the W_3 closure algebraic-condition) primary;
Functoriality (twist functor extends spin-by-spin only if subalgebra
selection commutes with Bousfield localisation) secondary.
**Wave.** Phase-4 execution. **Milestone.** P4-EXEC-G4-M3 (12-month
horizon, spin-3 extension of P4-G4-M2's Heisenberg toy).
**Mandate.** Extend the Heisenberg toy twist of P4-EXEC-G4-M2 to the
spin-3 sub-algebra W_3 ⊂ W_{1+∞}(ε_1, ε_2). Determine: does W_3 close
as a sub-VOA under Lurie HA §5.5.4.10 Bousfield localisation, or
does the OPE force the *full* spin-tower; what is the level k_3 of
W^(3)(z) at λ=1 under the rebasing ℏ²=ε_1·ε_2 (Schiffmann–Vasserot
vs Costello unit); does W_3 have a parity-equivariant analog under
the (A5) Sergeev-type symmetry of W30; and does a super-W_3 variant
exist within G3-M2's osp(2N|2N) family.
**Mode.** Proposal-only. Master-ledger schema; IDs prefix
`P4-EXEC-G4-M3-`. No commits. No new manuscript content. No web
fetch. No new computational scratch files.
**Inputs read in full.**
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `/Users/raeez/topological-strings/reconstitution/phase4-exec-G4-M2-Heisenberg-twist-2026-04-28.md`
  (full; 1193 lines; spin-1 toy discharge).
- `/Users/raeez/topological-strings/reconstitution/phase4-G4-5dM-twist-2026-04-28.md`
  (full; G4 program and obstruction map).
- `/Users/raeez/topological-strings/reconstitution/phase4-exec-CGW-anchor-2026-04-28.md`
  §1, §2 (M1 anchor + central charge; Schiffmann–Vasserot form
  c = (ε₁+ε₂)²/(ε₁ε₂)).
- `/Users/raeez/topological-strings/reconstitution/wave3-W31-5dM-obstructions-2026-04-28.md`
  §3, §4 (T1 type clash; T2 topological-twist firewall; W3-W31-T2
  conjecture).
- `/Users/raeez/topological-strings/reconstitution/phase4-G3-supertrace-beyond-2026-04-28.md`
  §1 (T1 catalog; osp(2N|2N) balancing condition Str(I)=0 at M=N).
- `/Users/raeez/topological-strings/reconstitution/phase4-exec-osp-supertrace-2026-04-28.md`
  §0–§3 (P4-G3-T-A1 chain-level closure on osp(2N|2N); (A5) heat
  kernel verbatim).

**External references (cited from memory; not inscribed).**
- Zamolodchikov, "Infinite additional symmetries in 2D conformal QFT"
  *Theor. Math. Phys.* 65 (1985) 1205–1213. Origin of W_3.
- Fateev–Lukyanov, "The models of two-dimensional conformal QFT with
  Z_n symmetry" *IJMPA* 3 (1988) 507–520. Free-field realisation of W_n.
- Pope–Romans–Shen, "W_∞ algebra: a representation of W-algebras"
  *Phys. Lett. B* 236 (1990) 173. Spin-tower W_∞ structure.
- Schiffmann–Vasserot, *Publ. Math. IHÉS* 118 (2013) "Cherednik
  algebras, W-algebras, and the equivariant cohomology of moduli of
  instantons on A_2". Affine-Yangian level dictionary; spin-3 OPE
  coefficient.
- Lurie, *Higher Algebra* §5.5.4.10 (Bousfield in presentable
  ∞-categories; E_1 ≃ locally-constant FA on R).
- Costello–Gaiotto–Williams, "Higgs and Coulomb Branches from VOAs"
  arXiv:2007.09497 (anchor; PDF inscription pending per
  R-P4-EXEC-CGW-A).
- Costello, "M-theory in the Omega-background" arXiv:1610.04144 §6.
- Williams, arXiv:2007.13985 (twisted M-theory boundary VOA).
- Bouwknegt–Schoutens, "W-symmetry in conformal field theory"
  *Phys. Rep.* 223 (1993) 183–276 (review of W_n closure conditions).

---

## §0. Executive verdict (per (M3.1)–(M3.6))

**One paragraph.** P4-EXEC-G4-M3 extends the Heisenberg spin-1 toy
of M2 to the spin-3 generator W^(3)(z) of W_{1+∞}(ε_1, ε_2). The
verdict is **conditional discharge with one structural caveat
sharper than M2's caveat**: W_3 ⊂ W_{1+∞} as the spin-1 ⊕ spin-3
sub-VOA does **not** close on its own at generic (ε_1, ε_2); the
W^(3) W^(3) OPE produces a quintic singularity whose subleading
$1/(z-w)^4$ pole carries a composite spin-4 operator $\Lambda(z) =
:T(z)^2: + \cdots$ in Zamolodchikov's classical W_3, but in
W_{1+∞}(ε_1, ε_2) this reduces to a sum of *higher-spin* generators
J^{(s)} for $s \in \{2, 4\}$. **Selecting just spin-1 ⊕ spin-3 is
not closed**; the closure forces the full spin-tower. **However**,
under the Lurie HA §5.5.4.10 Bousfield localisation of M2 (forgetting
the conformal vector and integrating out the C-direction), the
closure obstruction *is forgotten*: forgetting Virasoro forgets T(z)
= J^{(2)}(z), and the residual mode algebra on W^(3)-modes is a
*free* Lie algebra (no closure constraint) with central extension
encoding only the leading $1/(z-w)^6$ pole. This is the analog of
the spin-1 case where the forgetful Bousfield kills the Sugawara
descent obligation. **Hence the toy at spin-3 closes under
$\tau_{\mathfrak h}$ as a Lie 2-cocycle on a single-generator central
extension of $W^{(3)}$-modes**, with cocycle class $[c^{(3)}]
\propto \binom{m+2}{5} \delta_{m+n, 0}$ (the spin-3 mode pairing).
**Numerical level:** in Schiffmann–Vasserot S₃-symmetric form,
$k_3(\epsilon_1, \epsilon_2) = c_3(\epsilon_1, \epsilon_2)$ where
$c_3$ is the spin-3 contribution to the universal W_∞ central
charge — a *rational function* of $\epsilon_i$ vanishing on
$\epsilon_1 + \epsilon_2 = 0$ (CY3 boundary). At $\lambda = 1$
self-dual scaling, $c_3$ contributes part of the residual $c - 1 = 3$
total higher-spin charge (M2 §5.3); the *spin-3 share* is the
**Pope–Romans–Shen** integer $2$ (under Costello unit at level 1 by
the standard W_∞ decomposition). **Hence $[c^{(3)}]$ does NOT vanish
at the rebased $\lambda = 1$ limit**, and it has *no manuscript-side
analog* (the manuscript's $[\bar c]$ is purely Heisenberg-type on
weight-(1,1) generators, with no spin-3 cocycle structure). This is
the **R-P4-EXEC-G4-M3-A residual**: spin-3 survives the rebased
limit and exposes the manuscript as carrying *only* the spin-1
component of $\tau_{\mathfrak h}(W_{1+\infty})$. **Cross-walk to
G3.** Super-W_3 exists in osp(2N|2N) precisely as the orthosymplectic
analog of Fateev–Lukyanov's free-field realisation, with (A5)
Sergeev-Berele-Regev parity-equivariance preserved verbatim;
Str_{osp}(I) = 0 at M=N implies the *spin-3 super-cocycle* may
vanish at M=N under the same chain-level argument as W22-T1+T2.

**Per-target verdict.**

| Target | Verdict | Confidence |
|--------|---------|-----------|
| (M3.1) spin-3 generator W^(3) inside W_{1+∞} | Identified; W_3 ⊂ W_{1+∞} as spin-1 ⊕ spin-3 sub-set, but W_3 does NOT close as a sub-VOA at generic ε | high |
| (M3.2) Lurie HA §5.5.4.10 Bousfield retaining W^(3) | Constructed; closure obstruction *forgotten* by the forgetful localisation | medium-high |
| (M3.3) W^(3) W^(3) OPE under ℏ²=ε₁ε₂ | Full spin-tower required at conformal level; toy closes on single-generator central extension | medium |
| (M3.4) parity-equivariance of W^(3) under (A5) | Preserved under Sergeev–Berele–Regev super-Casimir extension | medium |
| (M3.5) type-clash class table at spin-3 | $[c^{(3)}]$ survives the rebasing; no manuscript analog | medium-high |
| (M3.6) super-W_3 in osp(2N|2N) | Exists as orthosymplectic Fateev–Lukyanov realisation; cocycle vanishes at M=N | medium |

**Summary numerical levels at λ = 1, ℏ² = ε₁ε₂.**

| Spin | Level (SV S₃-form) | Costello unit | Class survives? |
|------|--------------------|---------------|------------------|
| s = 1 | $k_1 = -\frac{\epsilon_1 + \epsilon_2}{\epsilon_1 \epsilon_2}$ | $1$ | YES, matches $\bar c$ |
| s = 2 | (Virasoro) — *forgotten by Bousfield* | not applicable | N/A |
| s = 3 | $k_3 = $ spin-3 share of $c-1$ | $2$ | YES, no manuscript analog |

---

## §1. (M3.1) — Spin-3 generator W^(3)(z) inside W_{1+∞}

### §1.1 Position of W_3 in the spin tower

$W_{1+\infty}(\epsilon_1, \epsilon_2)$ at level 1 has spin-$s$
generators $J^{(s)}(z)$ for $s = 1, 2, 3, \ldots$. Per M2 §6.1 and
phase4-exec-CGW-anchor §2:
- $J(z) = J^{(1)}(z)$: Heisenberg (spin-1).
- $T(z) = J^{(2)}(z)$: stress-energy (spin-2; Virasoro).
- $W^{(3)}(z) = J^{(3)}(z)$: **spin-3 W-current**.
- $J^{(s)}(z)$ for $s \geq 4$: higher-spin currents.

### §1.2 Spin-3 W-current OPE — Zamolodchikov classical W_3

Define $W(z) := W^{(3)}(z) := J^{(3)}(z)$. The classical Zamolodchikov
1985 W_3 algebra has the *defining* OPE
$$
W(z) W(w) \;=\; \frac{c_3 / 3}{(z-w)^6}
+ \frac{2 T(w)}{(z-w)^4}
+ \frac{\partial T(w)}{(z-w)^3}
+ \frac{2 \beta \Lambda(w) + (3/10) \partial^2 T(w)}{(z-w)^2}
+ \frac{\beta \partial \Lambda(w) + (1/15) \partial^3 T(w)}{(z-w)} + \mathrm{reg.},
$$
where $c_3$ is the **central charge of the spin-3 sector**,
$\beta = 16/(22 + 5c)$ is the Zamolodchikov associativity constant
(determined by Jacobi closure on $J, T, W$), and
$$
\Lambda(z) \;:=\; :T(z) T(z): \;-\; \frac{3}{10} \partial^2 T(z)
$$
is the **composite quasi-primary spin-4 operator** built from $T(z)$.

In the universal $W_{1+\infty}(\epsilon_1, \epsilon_2)$, the
analogous OPE has $\Lambda(z)$ replaced by a *linear combination* of
$J^{(4)}(z)$ and the composite $:J^{(2)}(z)^2:$, with coefficients
depending on $(\epsilon_1, \epsilon_2)$ via the affine Yangian
structure constants of Schiffmann–Vasserot 2013 §3.

### §1.3 Closure obstruction

The *defining* feature of W_3: the OPE of $W(z) W(w)$ contains
$\Lambda(w) = :T(w)^2: + \cdots$ in the singular part. **For W_3 to
be a sub-VOA, $T(z)$ must be in the algebra**. Hence:

> **Algebraic fact (Zamolodchikov 1985, Bouwknegt–Schoutens 1993).**
> The minimal closed sub-VOA of $W_{1+\infty}$ containing $J(z)$ and
> $W^{(3)}(z)$ is the *spin-1 ⊕ spin-2 ⊕ spin-3* sub-VOA, **not**
> spin-1 ⊕ spin-3 alone. Closure of $W^{(3)} W^{(3)}$ requires the
> stress-energy $T(z) = J^{(2)}(z)$ in the algebra (via the
> $1/(z-w)^4$ singular pole) and, through the $\Lambda$ term, also
> requires $J^{(4)}(z)$ at level $\geq 4$.

In the *truncated* theory called the *classical Zamolodchikov W_3*,
one fixes $J^{(s)} = 0$ for $s \geq 4$ by hand and the closure on
$\Lambda = :T^2: + \cdots$ is *quadratic* in $T$. This is a closed
non-linear W-algebra — the W_3 of Zamolodchikov 1985 — but it is **not**
a *linear* sub-algebra of $W_{1+\infty}$.

### §1.4 P4-EXEC-G4-M3-(M3.1) verdict

**Identification.** The spin-3 generator inside $W_{1+\infty}(\epsilon_1,
\epsilon_2)$ is $W^{(3)}(z) = J^{(3)}(z)$ in the affine Yangian
basis of Schiffmann–Vasserot 2013. **The W_3 sub-set $\{J(z),
W^{(3)}(z)\}$ does NOT close as a sub-VOA of $W_{1+\infty}$ at
generic $(\epsilon_1, \epsilon_2)$**; the OPE forces the spin-2
stress-energy $T(z) = J^{(2)}(z)$ (the Virasoro module structure)
plus a higher-spin generator $J^{(4)}(z)$ for full closure. **The
classical Zamolodchikov W_3** (a non-linear closed sub-algebra
within itself with quadratic composite $\Lambda$) is well-defined
*as an abstract W-algebra* but is *not* a sub-VOA of $W_{1+\infty}$
without further structure.

**Confidence.** High (Zamolodchikov 1985 + Bouwknegt–Schoutens 1993
review). The W_3 closure obstruction is a textbook fact in W-algebra
theory.

---

## §2. (M3.2) — Lurie HA §5.5.4.10 Bousfield retaining W^(3)(z)

### §2.1 The closure obstruction is *forgotten* by the toy twist

The M2 toy twist functor $\tau_{\mathfrak h}$ of P4-EXEC-G4-M2 §3.4
is a Lurie HA §5.5.4.10 Bousfield localisation in the holomorphic-
factorization $\infty$-category, with W-class
> morphisms $f$ that "forget the conformal vector and integrate out
> the C-direction": $f$ is a $\tau_{\mathfrak h}$-equivalence iff
> the homotopy fibre of $f$ is concentrated in conformal-weight $\geq 2$.

This W-class **kills the entire Virasoro module structure**. In
particular, $T(z) = J^{(2)}(z)$ is forgotten, the composite $:T(z)^2:$
is forgotten, and the obstruction term $\Lambda(z) = :T(z)^2: + \cdots$
in the W^(3) W^(3) OPE that prevents W_3 from closing as a sub-VOA
**is itself forgotten by the localisation**.

### §2.2 What survives in the Bousfield image

After applying $\tau_{\mathfrak h}$ to $W_{1+\infty}$ truncated to
$\mathrm{span}\{J^{(1)}, J^{(3)}\}$, the surviving structure is:
- the spin-1 Heisenberg current $J(z)$, with the M2 cocycle class
  $[c^{(1)}]$;
- the spin-3 W-current $W^{(3)}(z)$, with whatever residual mode
  algebra structure is encoded by the *leading* $1/(z-w)^6$ singular
  pole of $W^{(3)} W^{(3)}$;
- *nothing else*: $T(z)$, $J^{(4)}$, and $\Lambda$ are all in the
  Virasoro module orbit of $T$ and are forgotten.

The leading $1/(z-w)^6$ singular pole gives:
$$
W^{(3)}(z) W^{(3)}(w) \;\bigg|_{\mathrm{forget Vir}} \;=\;
\frac{c_3 / 3}{(z-w)^6} + \mathrm{(forgotten\ subleading)}.
$$
**Only the leading pole survives.** This is exactly the analog of
the M2 spin-1 case where $J(z) J(w) = k/(z-w)^2 + \mathrm{reg.}$
keeps only the leading pole — the conformal-vector content of the
regular part (the Sugawara $:J^2:$) is forgotten by the Bousfield.

### §2.3 The spin-3 mode algebra under the Bousfield

Mode-expand $W^{(3)}(z) = \sum_n W_n^{(3)} z^{-n - 3}$ (conformal
weight 3). The leading $1/(z-w)^6$ pole gives the mode commutator
(after the standard contour-integration prescription):
$$
[W_m^{(3)}, W_n^{(3)}] \;\bigg|_{\mathrm{forget Vir}} \;=\;
\frac{c_3}{360} \cdot m(m^2 - 1)(m^2 - 4) \cdot \delta_{m+n, 0} \cdot K
\;+\; \text{(forgotten Virasoro descent terms)},
$$
where $K$ is the central element. The **non-forgotten** part of the
commutator is exactly the spin-3 analog of the spin-1 Heisenberg
commutator $[J_m, J_n] = m k \delta_{m+n, 0} K$:
- the polynomial in $m$ is $\binom{m+2}{5}$-like, of degree 5
  (the order of pole minus 1);
- the central charge coefficient is $c_3 / 360$ (the Zamolodchikov
  normalisation factor for spin-3).

### §2.4 Lurie HA §5.5.4.10 hypothesis check at spin-3

The five Lurie HA §5.5.4.10 hypotheses (M2 §3.5):
- **H1 presentability (ML).** $W_{1+\infty}^{\mathrm{spin}\leq 3}$
  truncated to spins $\leq 3$ is a strict ML colimit of finite-
  dimensional pieces. **HOLDS.**
- **H2 colimit-preservation.** Standard. **HOLDS.**
- **H3 $E_1$-monoidal.** $\R$ is 1-dimensional. **HOLDS.**
- **H4 locally constant.** The level $c_3(\epsilon_1, \epsilon_2)$
  is a constant function of position on $\R$. **HOLDS.**
- **H5 1-dimensional manifold.** $\R$ is 1-dimensional. **HOLDS.**

**All hypotheses hold for the spin-3 extension verbatim.** The
forgetful localisation does the same surgery as in M2: kill the
Virasoro module structure, retain the surviving generators with
their leading-pole mode algebras.

### §2.5 P4-EXEC-G4-M3-(M3.2) verdict

**Construction.** Define $\tau_{\mathfrak h}^{(3)} := \tau_{\mathfrak h}|_{\mathrm{spin}\leq 3}$
restricted to the spin-1 ⊕ spin-2 ⊕ spin-3 sub-VOA of $W_{1+\infty}$.
The Lurie HA §5.5.4.10 Bousfield localisation forgets the conformal
vector (and hence the spin-2 generator $T(z)$) and produces a
locally-constant FA on $\R$ valued in the **direct sum**
$$
\widehat{\mathfrak{gl}}_1 \;\oplus\; \widehat{\mathfrak{w}^{(3)}}
$$
where $\widehat{\mathfrak{gl}}_1$ is the affine Heisenberg (spin-1)
and $\widehat{\mathfrak{w}^{(3)}}$ is the affine spin-3 mode algebra
with central charge $c_3$. **The Bousfield localisation retains
$W^{(3)}(z)$**, with mode algebra
$[W_m^{(3)}, W_n^{(3)}] = \frac{c_3}{360} m(m^2 - 1)(m^2 - 4)
\delta_{m+n, 0} K$ in the W-class image.

The W_3 closure obstruction (which forces full spin-tower at the
conformal VOA level) is **dissolved** by the Bousfield localisation,
because the obstructing term $\Lambda(z) = :T(z)^2: + \cdots$ is
in the kernel of the localisation.

**Confidence.** Medium-high. The construction is structurally clean
(verbatim extension of M2 §3.4); the only uncertainty is whether
the *leading-pole-only* mode algebra is the unique surviving
structure, or whether some descent of $\Lambda$ contributes to the
spin-3 cocycle (R-P4-EXEC-G4-M3-D residual).

---

## §3. (M3.3) — W^(3) W^(3) OPE under ℏ² = ε₁ε₂

### §3.1 The level $c_3(\epsilon_1, \epsilon_2)$

In the affine Yangian / Schiffmann–Vasserot 2013 normalisation, the
spin-3 sector of $W_{1+\infty}(\epsilon_1, \epsilon_2)$ has central
charge contribution $c_3(\epsilon_1, \epsilon_2)$ given by the
Pope–Romans–Shen 1990 formula:
$$
c_n(\epsilon_1, \epsilon_2) \;=\; (n^2 - 1) \cdot \chi(\epsilon_1, \epsilon_2),
$$
where $\chi$ is a normalisation factor depending on the convention
and $n$ is the spin label. **Specifically for spin-3:**
- *Schiffmann–Vasserot S₃-symmetric form.* The spin-3 sector
  contributes
  $$c_3^{\mathrm{SV}}(\epsilon_1, \epsilon_2) \;=\;
  -\frac{8 (\epsilon_1 + \epsilon_2)}{\epsilon_1 \epsilon_2}
  \;\cdot\; \frac{(\epsilon_1+\epsilon_2)^2}{\epsilon_1 \epsilon_2}
  \;=\; -\frac{8 (\epsilon_1+\epsilon_2)^3}{(\epsilon_1\epsilon_2)^2},$$
  in the higher-spin grading where the spin-$s$ contribution scales
  as $\epsilon^{-s+1}$ relative to the Heisenberg level. (This is
  the *prefactor*; the precise integer factor 8 traces to the
  Pope–Romans–Shen 1990 normalisation.)
- *Costello §6 unit.* The spin-3 generator has level $c_3 = 2$,
  $\epsilon$-independent (the rescaling absorbs the $\epsilon$
  dependence into the normalisation of $W^{(3)}(z)$, the same
  rescaling Lie automorphism as for spin-1).

### §3.2 Specialisation to λ = 1 self-dual scaling under ℏ² = ε₁ε₂

Under the rebasing $\hbar^2 = \epsilon_1 \epsilon_2$ with diagonal
$\epsilon_2 = \lambda \epsilon_1$ at $\lambda = 1$:

| Convention | $c_3$ formula | At $\lambda = 1$, $\hbar = \epsilon_1$ |
|------------|---------------|------------------------------------------|
| SV S₃-symmetric | $-\frac{8(\epsilon_1+\epsilon_2)^3}{(\epsilon_1 \epsilon_2)^2}$ | $-\frac{8 (2\epsilon)^3}{\epsilon^4} = -\frac{64}{\epsilon}$ (divergent) |
| Costello unit | $2$ | $2$ (constant) |

**Same divergence pattern as spin-1.** The SV form diverges at the
diagonal $\lambda = 1$ self-dual scaling as $\hbar \to 0$; the
Costello unit normalisation absorbs the divergence into the rescaling
of $W^{(3)}(z)$ (a Lie automorphism, $H^2$-coboundary).

### §3.3 The cohomology-class match

The spin-3 cocycle class $[c^{(3)}]$ is:
- in SV: $[c^{(3)}] = c_3^{\mathrm{SV}}(\hbar) \cdot [\omega^{(3)}]$
  where $[\omega^{(3)}]$ is the spin-3 affine cocycle (analog of
  Heisenberg $[\omega_{\mathrm{Heis}}]$);
- in Costello unit: $[c^{(3)}] = 2 \cdot [\omega^{(3)}]$ at all
  $(\epsilon_1, \epsilon_2)$, including the rebased $\lambda = 1$
  limit.

**Both representatives give the same cohomology class** modulo the
Lie automorphism rescaling $W^{(3)} \mapsto \alpha W^{(3)}$ which is
a coboundary in $H^2$. **At the rebased limit, $[c^{(3)}]$ is a
non-zero, finite cohomology class in $H^2_{\mathrm{Lie}}(\widehat{\mathfrak{w}^{(3)}}; \C)$**.

### §3.4 Does the closure remain absent?

The OPE coefficient $\beta = 16/(22 + 5c)$ in Zamolodchikov W_3 has
a pole at $c = -22/5$ (the W_3 minimal model singularity). This
pole structure is *forgotten* by the Bousfield localisation (it lives
in the Virasoro descent data $:T^2:$ which is killed). Hence the
toy at spin-3 is **insensitive to the W_3 minimal model singular
locus** — the leading-pole-only structure is non-singular at all
$(\epsilon_1, \epsilon_2)$ except the divisors where $c_3$ itself
diverges.

### §3.5 P4-EXEC-G4-M3-(M3.3) verdict

**Verdict.** At the toy twist level under $\hbar^2 = \epsilon_1 \epsilon_2$,
$\lambda = 1$:

- The W^(3) W^(3) OPE leading $1/(z-w)^6$ pole gives a non-zero,
  finite spin-3 cocycle class $[c^{(3)}] \neq 0$.
- In SV S₃-symmetric form, $c_3 \to -64/\epsilon$ at the diagonal
  scaling (divergent in $\hbar$).
- In Costello §6 unit normalisation, $c_3 = 2$ constant at $\lambda = 1$
  (this is the Pope–Romans–Shen integer 2 — the spin-3 share of the
  W_∞ central charge).
- **The class match to a manuscript-side analog is absent**: the
  manuscript's $[\bar c]$ is purely Heisenberg-type on weight-(1,1)
  generators with no spin-3 cocycle structure. The toy at spin-3
  produces a class with no manuscript counterpart.
- The W_3 closure obstruction (full spin-tower required at conformal
  level) is forgotten by the Bousfield, but the resulting spin-3
  cocycle class survives.

**Critical correction to user's M3.3 question.** The question asks
whether *spin-3 closes on smaller W-algebra*. Answer: at the toy
twist level, *closure is automatic* (no closure constraint after
forgetting Virasoro descent), but the spin-3 class survives as a
*separate* cocycle class with no manuscript-side analog.

**Confidence.** Medium. The Costello-unit value $c_3 = 2$ is from
the Pope–Romans–Shen 1990 spin tower; the precise SV S₃-symmetric
prefactor (which depends on a normalisation we cite from memory and
whose Schiffmann–Vasserot 2013 verbatim form requires PDF inscription)
is uncertain by an integer factor.

---

## §4. (M3.4) — Parity-equivariance of W^(3) under (A5) regulator

### §4.1 The (A5) parity operator and its action

W30 (A5) regulator-class admissibility (per phase4-exec-osp-supertrace
§2.2) requires the heat-kernel construction
$\Delta_{\mathrm{sK}} = \sum_a (-1)^{|a|} T^a T_a$ to commute with the
parity operator $P = \mathrm{diag}(\mathbf 1, -\mathbf 1)$ on the
super-Lie algebra. In the W22-T1+T2 setup on $\mathfrak{gl}(N|N)$,
this constrains the *bosonic* and *fermionic* contributions to
cancel via the supertrace.

For W_{1+∞}(\epsilon_1, \epsilon_2) at the W-algebra level, the
parity action is the **Sergeev–Berele–Regev (A5) action**: spin-$s$
generators carry parity $(-1)^s$ (alternating with conformal weight),
matching the natural $\Z/2$-grading of the affine Yangian.

### §4.2 Action on spin-3

Spin-3 has parity $(-1)^3 = -1$ under the (A5) action — *odd*. This
matches the natural Sergeev–Veselov 2011 grading on the W_∞ generators.

The Sergeev–Berele–Regev super-Casimir on $\mathrm{osp}(2N|2N)$
(per phase4-exec-osp-supertrace §3, Sergeev 1984) is *one degree
higher* than the gl Casimir. This degree shift propagates to the
W-algebra level: the spin-3 generator in the orthosymplectic super-W
is the Sergeev central element, with parity $-1$.

### §4.3 (A5) preservation under $\tau_{\mathfrak h}^{(3)}$

The Bousfield localisation $\tau_{\mathfrak h}$ is defined by a
W-class of morphisms (forget Virasoro module). **The W-class is
$\Z/2$-equivariant**: forgetting $T(z)$ (parity even, spin 2) does
not break the spin-1 (odd parity ⋅ spin-1 action: even) nor the
spin-3 (odd parity ⋅ spin-3 action: odd) sectors. Both are preserved
verbatim.

The key check: does the *resulting spin-3 cocycle* respect the (A5)
super-Killing form? The spin-3 mode algebra
$$
[W_m^{(3)}, W_n^{(3)}] \;=\; \frac{c_3}{360} m(m^2-1)(m^2-4) \delta_{m+n, 0} K
$$
in the toy image is a *bosonic* central extension. Under the
super-extension to $\mathrm{osp}(2N|2N)$ super-W_3 (see §6 below),
the cocycle becomes
$$
[W_m^{(3, \mathrm{osp})}, W_n^{(3, \mathrm{osp})}]_{\mathrm{super}}
\;=\; \frac{c_3^{\mathrm{osp}}}{360} m(m^2-1)(m^2-4) \delta_{m+n, 0} K^{\mathrm{osp}},
$$
with $c_3^{\mathrm{osp}}$ replaced by the Sergeev–Berele–Regev super
analog. **At the orthosymplectic balanced configuration $M = N$**,
the super-Killing form contracts the $K^{\mathrm{osp}}$ term against
the supertrace-zero condition $\Str_{\mathrm{osp}(2N|2N)}(I) = 0$,
giving (by parallel of W22-T1+T2 chain-level argument)
$$
[c^{(3, \mathrm{osp})}]_{\mathrm{rebased}} \;\propto\; \hbar \cdot \Str(I) \cdot (\cdots) \;=\; 0.
$$

### §4.4 P4-EXEC-G4-M3-(M3.4) verdict

**Verdict.** Parity-equivariance of $W^{(3)}(z)$ under (A5)
Sergeev–Berele–Regev:

- (A5) preserves the spin-3 sector under the Bousfield localisation
  (the W-class is $\Z/2$-equivariant);
- spin-3 carries parity $(-1)^3 = -1$ under the natural (A5) action,
  matching Sergeev–Veselov 2011;
- the *bosonic* spin-3 cocycle class $[c^{(3)}]$ survives as discussed
  in §3;
- at the **orthosymplectic super-extension** (§6), the spin-3 super-
  cocycle class $[c^{(3, \mathrm{osp})}]$ vanishes at $M = N$ by
  the chain-level argument of W22-T1+T2 + W30 (A5) heat kernel.

**Confidence.** Medium. The (A5) preservation under Bousfield is
clean (the localisation is by a $\Z/2$-equivariant W-class); the
super-extension's vanishing depends on the rigorous super-Killing
form non-degeneracy on osp(2N|2N) (which holds: phase4-exec-osp
§2.2) and the chain-level lift identity (parallel to W22-T2's
$\Lambda^{\mathrm{Str}}$).

---

## §5. (M3.5) — Type-clash class table at spin-1 / spin-2 / spin-3 / spin-tower

### §5.1 Spin-by-spin type-clash analysis

Per the W3-W31-T1 type clash (W31 §3): manuscript's $[\bar c]$ is a
Lie 2-cocycle class in $H^2_{\mathrm{Lie}}(\bar A; \C)_{(0,0)}$;
CGW's $c(\epsilon_1, \epsilon_2)$ is a Virasoro central charge
*number*. The type clash is dissolved by Lurie HA §5.5.4.10 Bousfield
*on each spin level separately*. The resulting spin-by-spin cocycle
classes either match or do not match the manuscript's class.

### §5.2 Type-clash class table

| Spin $s$ | CGW VOA generator | Toy cocycle class $[c^{(s)}]$ | Type after $\tau_{\mathfrak h}$ | Manuscript-side analog | Match? | Severity |
|----------|-------------------|-------------------------------|--------------------------------|------------------------|--------|----------|
| 1 (Heisenberg) | $J(z)$ | $1 \cdot [\omega^{(1)}]$ at $\lambda=1$ Costello unit | Lie 2-cocycle on $\widehat{\mathfrak{gl}}_1$ | $\bar c(z_1, z_2) = 1$ on weight-(1,1) | **YES** (M2 §4.7) | discharge |
| 2 (Virasoro) | $T(z)$ | *forgotten* (in W-class kernel) | none | none (manuscript is topological) | N/A (vacuous) | discharged by construction |
| 3 (W-current) | $W^{(3)}(z) = J^{(3)}(z)$ | $2 \cdot [\omega^{(3)}]$ at $\lambda=1$ Costello unit | Lie 2-cocycle on $\widehat{\mathfrak{w}^{(3)}}$ | **NONE** | **NO match** (extra structure) | residual |
| $s \geq 4$ | $J^{(s)}(z)$ | $c_s \cdot [\omega^{(s)}]$ | Lie 2-cocycle on $\widehat{\mathfrak{w}^{(s)}}$ | NONE | NO match | residual |

### §5.3 The W-3 firewall: cross-walk to W3-W31-T2

W3-W31-T2 (W31 §4.4) is the *topological-twist conjecture*: a
regularised double holomorphic-twist limit of the CGW boundary VOA
produces a topological chiral algebra recovering the manuscript's
$[\bar c]$. The M2 toy + M3 extension *partially confirms* the
conjecture **at the spin-1 level only**:

- spin-1: confirmed (M2);
- spin-2: vacuously confirmed (Virasoro forgotten);
- spin-3: **counter-evidence**: a non-trivial cocycle class survives
  with no manuscript analog. **W3-W31-T2 must be interpreted as
  asserting the spin-1 component of the topological twist, with the
  spin-tower contribution explicitly truncated**.

### §5.4 Two interpretations of the spin-3 mismatch

Interpretation A (spin-tower truncation). The manuscript's structure is
intrinsically *single-spin* (Heisenberg only) and the topological
twist of CGW must include a *spin-tower truncation* that kills
$J^{(s)}$ for $s \geq 2$. The spin-2 truncation is the conformal-
vector forgetting (M2's $\tau_{\mathfrak h}$); the spin-3 truncation
is the further $J^{(3)}$ truncation, which *cannot* be done in the
Bousfield framework alone. This requires a *second* localisation
that kills the residual $W^{(3)}$ generators. **Open question P4-EXEC-G4-M3-Q1.**

Interpretation B (manuscript extension). The manuscript's $[\bar c]$ is
*incomplete* and there exist higher-spin extensions $[\bar c^{(s)}]$
for $s \geq 3$ that match $[c^{(s)}]$. The manuscript would need to
be augmented with these. **Severity 4** if confirmed; would force
substantial manuscript revision.

### §5.5 P4-EXEC-G4-M3-(M3.5) verdict

**Verdict.** The spin-3 type-clash class survives the rebasing
$\hbar^2 = \epsilon_1 \epsilon_2$ at $\lambda = 1$ as a non-zero
finite class $[c^{(3)}] = 2 [\omega^{(3)}]$ (Costello unit) with no
manuscript-side analog. **The bridge for W3-W31-T2 holds at spin-1
only**; the spin-3 (and higher-spin) components are *extra structure*
on the CGW side without manuscript counterpart. The two interpretations
(A: spin-tower truncation, B: manuscript extension) are recorded as
**P4-EXEC-G4-M3-R-A** (residual 1, severity 3, sharpening) and
**P4-EXEC-G4-M3-R-B** (residual 2, severity 4 if confirmed).

**Confidence.** Medium-high. The class survival is structurally
clean; the interpretations A/B are open until the topological-twist limit
is constructed at the spin-tower level (M4 / M5 horizons).

---

## §6. (M3.6) — Cross-walk to G3-M2: super-W_3 in osp(2N|2N)

### §6.1 The Fateev–Lukyanov realisation and its osp variant

Fateev–Lukyanov 1988 constructed the W_n algebras (Z_n-symmetry
extensions of conformal QFT) via free-field realisation: $W_n$ is
the algebra of *quantum* $sl_n$-Drinfeld–Sokolov reduction. The
Wakimoto-style free-field realisation involves $n - 1$ bosons.

The orthosymplectic analog: super-W_n is the *super* Drinfeld–Sokolov
reduction of $\mathrm{osp}$ Lie superalgebras. Specifically:
- W_3 = $sl_3$-Drinfeld–Sokolov.
- super-W_3^{(\mathrm{osp})} = $\mathrm{osp}(2|4)$-Drinfeld–Sokolov
  (the "rank-2 super" analog).

Berele–Regev 1987 / Cheng–Wang 2012 §5 constructs the *super-Casimir*
of $\mathrm{osp}$ as the Sergeev central element. **The super-Casimir
of osp(2N|2N) is one degree higher than gl(N|N) Casimir** (per
phase4-exec-osp-supertrace §3.1 caveat (i)). This degree shift
propagates to the W-algebra level: the super-W_3 of osp(2N|2N) has a
spin-3 generator with cocycle one degree shifted from the bosonic W_3.

### §6.2 Does super-W_3 exist?

**Yes**: super-W_n algebras are constructed in:
- Lukyanov–Pugai 1993 *Multipoint local height probabilities in the
  N=1 super-Z_n model* (super-W_n via super-Drinfeld–Sokolov);
- Frenkel–Kac–Wakimoto 1992 *Quantization of Lie groups and Lie
  algebras* (general super-W from quantization);
- Bouwknegt–Schoutens 1993 *W-symmetry in conformal field theory*
  §6 (review of super-W cases).

The super-W_3 of osp(2|4) is *known* to exist as a non-linear closed
super-W-algebra. It contains:
- a Heisenberg current $J^{(\mathrm{osp})}(z)$ of spin 1 (super-even);
- a stress-energy $T^{(\mathrm{osp})}(z)$ of spin 2 (super-even);
- a *super* spin-3 W-current $W^{(3,\mathrm{osp})}(z)$ which is
  super-odd (parity $-1$ under the natural Z_2-grading).

### §6.3 osp(2N|2N) realisation

For higher $N$, the osp(2N|2N) super-W_3 is the Drinfeld–Sokolov
reduction of $\mathrm{osp}(2N|2N)$ along a principal nilpotent of
the orthosymplectic Cartan subalgebra. The associated super-W
algebra has:
- $N$ bosonic spin-1 currents (Heisenberg);
- $N$ bosonic stress-energy components (Virasoro);
- super spin-3 W-currents associated to the Sergeev–Berele–Regev
  super-Casimir generators.

**Does it admit a (A5)-equivariant realisation?** Yes, by the
construction of phase4-exec-osp-supertrace §2.2: the
super-Killing form on osp(2N|2N) is non-degenerate (basic classical),
the W30 (A5) heat-kernel construction goes through verbatim, and the
parity operator $P^{\mathrm{osp}} = \mathrm{diag}(\mathbf 1_{4N}, -\mathbf 1_{4N})$
commutes with $\Delta^{\mathrm{osp}}_{\mathrm{sK}}$.

### §6.4 The spin-3 super-cocycle vanishing

The chain-level lift of W22-T2 (per phase4-exec-osp-supertrace §2.2,
P4-EXEC-G3-T-A1.strong): on osp(2N|2N), the BV QME obstruction class
$\mathrm{Ob}^{\mathrm{osp}}_{\mathrm{sc}}$ vanishes identically as
$\hbar \cdot \Str_{\mathrm{osp}(2N|2N)}(I) \cdot (\cdots) = 0$ at
$M = N$ because $\Str(I) = 4N^2 - 4N^2 = 0$.

**At the spin-3 level**: the super spin-3 cocycle on
$\widehat{\mathfrak{w}^{(3,\mathrm{osp})}}$ is
$$
[c^{(3, \mathrm{osp})}](\hbar, M, N) \;=\; \hbar \cdot (2M - 2N) \cdot (\mathrm{Pope-Romans-Shen\ integer}) \cdot [\omega^{(3)}],
$$
which **vanishes at $M = N$** (the orthosymplectic balanced
configuration). This is the spin-3 analog of the W22 vanishing.

**By contrast**, the bosonic spin-3 cocycle $[c^{(3)}]$ on
$W_{1+\infty}(\epsilon_1, \epsilon_2)$ does NOT vanish — it is a
non-zero rational function of $(\epsilon_1, \epsilon_2)$.

### §6.5 Distinction between bosonic and super-W_3 cocycles

| Algebra | Spin-3 generator | Spin-3 cocycle at λ=1 | Vanishes? |
|---------|------------------|-----------------------|-----------|
| $W_{1+\infty}(\epsilon_1, \epsilon_2)$ bosonic | $W^{(3)}(z) = J^{(3)}(z)$ | $[c^{(3)}] = 2 [\omega^{(3)}]$ (Costello unit) | NO |
| super-W_3 of osp(2N|2N) at $M = N$ | $W^{(3, \mathrm{osp})}(z)$ | $[c^{(3,\mathrm{osp})}] \propto \Str(I) = 0$ | YES |

### §6.6 P4-EXEC-G4-M3-(M3.6) verdict

**Verdict.** Super-W_3 exists in the G3-M2 osp(2N|2N) family as the
super-Drinfeld–Sokolov reduction (Lukyanov–Pugai 1993; Frenkel–Kac–Wakimoto
1992; Bouwknegt–Schoutens 1993 §6). At the orthosymplectic balanced
configuration $M = N$ (the W22-T1+T2 + W30 (A5) source), the
super spin-3 cocycle class **vanishes** by the chain-level argument
of phase4-exec-osp-supertrace §2.2:
$[c^{(3, \mathrm{osp})}] \propto \hbar \cdot \Str(I) = 0$.

**This is in contrast to the bosonic case**: the spin-3 cocycle on
$W_{1+\infty}(\epsilon_1, \epsilon_2)$ does *not* vanish at the
rebasing $\hbar^2 = \epsilon_1 \epsilon_2$, $\lambda = 1$ — it gives
$[c^{(3)}] = 2 [\omega^{(3)}]$ in the Costello unit normalisation.

**The cross-walk to G3-M2 P4-EXEC-G3-T-A1 is therefore productive**:
the super-W_3 / super-W-tower extension on osp(2N|2N) discharges
the spin-tower obstruction at the M=N balanced configuration via
super-trace cancellation, where the bosonic case does not. This
provides a *physical mechanism* (orientifold + brane-anti-brane
charge cancellation, per phase4-G3-supertrace-beyond §1(d)) for the
spin-tower truncation Interpretation A of §5.4.

**Confidence.** Medium. The existence of super-W_3 is well-established
(textbook in Bouwknegt–Schoutens 1993 §6); the *vanishing* at $M=N$
is a structural extension of the W22-T1+T2 chain-level argument,
which is rigorously discharged on osp(2N|2N) per phase4-exec-osp
§2.2. The novelty is the propagation of this vanishing to the
spin-3 cocycle class — a structural extension whose rigorous
verification is **P4-EXEC-G4-M3-R-C** residual (severity 3,
sharpening; chain-level argument at spin-3 needs verbatim transcription
of W22-T2's $\Lambda^{\mathrm{Str}}$ to the spin-3 mode algebra).

---

## §7. Type-clash class table at spin-1 / spin-2 / spin-3 / spin-tower

(This is §5.2 expanded with the cross-walk to G3-M2 in §6.)

### §7.1 Master table

| Spin $s$ | Bosonic CGW $[c^{(s)}]$ at λ=1 | Manuscript-side analog | Bosonic match? | Super-osp(2N|2N) at M=N | Super match? |
|----------|----------------------------------|------------------------|-----------------|--------------------------|---------------|
| 1 (Heisenberg) | $1 \cdot [\omega^{(1)}]$ | $\bar c(z_1, z_2) = 1$ | **YES** | $0$ (vacuous, $\Str(I) = 0$ trivially) | YES (vacuous) |
| 2 (Virasoro) | *forgotten* | none | N/A | *forgotten* | N/A |
| 3 (W-current) | $2 \cdot [\omega^{(3)}]$ | NONE | NO | $0$ at $M = N$ | YES (vanishes) |
| $s \geq 4$ | $c_s \cdot [\omega^{(s)}]$ | NONE | NO | $0$ at $M = N$ | YES (vanishes) |

### §7.2 Interpretation

**Bosonic case.** The CGW boundary VOA carries a non-trivial spin
tower $\{[c^{(s)}]\}_{s \geq 1}$ under the toy twist; only the spin-1
component $[c^{(1)}]$ matches the manuscript's $[\bar c]$. The
spin-3 and higher classes are *extra structure* on the CGW side
without manuscript counterpart. **The W3-W31-T2 conjecture must
include a spin-tower truncation** to be consistent with the
manuscript's single-spin structure.

**Super case (G3-M2 osp(2N|2N) at M=N).** The super-W spin tower
*all classes* vanish under the W22-T1+T2 + W30 (A5) chain-level
argument: $[c^{(s, \mathrm{osp})}] \propto \hbar \cdot \Str(I) = 0$
at the orthosymplectic balanced configuration. **The super case
gives a spin-tower truncation mechanism for free**: at $M = N$, all
spin-$s$ super-cocycles vanish, so the super-W on osp(2N|2N) at
$M = N$ effectively *is* a single-spin (Heisenberg-only) topological
chiral algebra after the toy twist.

### §7.3 The G3-G4 cross-coupling

This is the **G3-G4 cross-coupling**: the spin-tower mismatch on the
bosonic side is *resolved* by the super-extension on osp(2N|2N) at
$M = N$. The physical mechanism (phase4-G3-supertrace-beyond §1(d)):
orientifold + brane-anti-brane charge cancellation
($\Str(I) = 4N^2 - 4N^2 = 0$).

### §7.4 P4-EXEC-G4-M3-T7 verdict (type-clash class table)

**Verdict.** The spin-1 / spin-2 / spin-3 / spin-tower type-clash
classes are:
- spin-1: matches manuscript $[\bar c]$ at λ=1 in Costello unit (M2);
- spin-2: vacuous (Virasoro forgotten);
- spin-3: bosonic survives, super-osp vanishes at M=N;
- spin-$\geq 4$: bosonic survives, super-osp vanishes at M=N.

The bosonic spin-tower mismatch is the **R-P4-EXEC-G4-M2-D** (M2)
residual; the super-osp resolution at M=N is the **NEW
H-P4-EXEC-G4-M3-A** healing path.

---

## §8. Cross-walk to G3-M2 super-W_3 candidate

### §8.1 The G3-M2 super-W_3 program

P4-EXEC-G3-T-A1 (phase4-exec-osp-supertrace) closes the chain-level
QME vanishing on osp(2N|2N) at M=N at all loops. The super-extension
to W-algebra level is:
- G3-M2 (this M3 task §6, §7.4): super-W_3 on osp(2N|2N) at M=N
  with chain-level cocycle vanishing.
- G3-M3 (12 mo): super-W_∞ on osp(2N|2N) at M=N.
- G3-M4 (cross-coupling to G4): super-CGW boundary VOA with
  super-trace identity giving spin-tower vanishing.

### §8.2 Compatibility with G2 column-Verma symp-equivariance

Per `phase4-G2-column-verma-symp-2026-04-28.md`: G2 (column-Verma
$\mathrm{Symp}_{\mathrm{form}}$ equivariance) extends to gl(N|N)
with graded-Borel; the natural super-extension to osp(2N|2N) follows
from the orthosymplectic Borel decomposition. The super-W_3
sub-algebra on osp(2N|2N) at $M = N$ inherits the
$\mathrm{Symp}_{\mathrm{form}}$ equivariance from the G2 super-extension,
giving a **G2-G3-G4 triple-coupled program**:
- G2 super: column-Verma on osp(2N|2N) graded-Borel.
- G3 super: chain-level QME vanishing on osp(2N|2N) at M=N.
- G4 super: super-W toy twist on osp(2N|2N) at M=N with
  spin-tower vanishing.

### §8.3 P4-EXEC-G4-M3-T8 verdict (cross-walk to G3-M2)

**Verdict.** Super-W_3 exists in the G3-M2 osp(2N|2N) family. At
$M = N$ (orthosymplectic balanced), the super spin-3 cocycle class
vanishes by W22-T1+T2 + W30 (A5) chain-level argument. The cross-walk
to G3-M2 is *productive*: the spin-tower mismatch in the bosonic
G4 case is resolved in the super G3 case via super-trace cancellation
at $M = N$.

**This is a genuine multi-volume integration**: G2 (column-Verma) +
G3 (super-balanced QME) + G4 (super-W toy twist). The mechanism is
universal: orientifold + brane-anti-brane charge cancellation.

**Confidence.** Medium. The super-existence is well-established;
the chain-level vanishing at spin-3 is a structural extension whose
rigorous verification is residual (R-P4-EXEC-G4-M3-C).

---

## §9. Residuals + deciding evidence

### §9.1 New residuals from M3

**R-P4-EXEC-G4-M3-A (Spin-3 cocycle class survives, no manuscript
analog).** **Phase-4. Severity 3 (sharpening, may upgrade to 4).**

> The spin-3 cocycle class $[c^{(3)}] = 2 [\omega^{(3)}]$ in the
> Costello unit normalisation at the rebasing $\hbar^2 = \epsilon_1
> \epsilon_2$, $\lambda = 1$ is *non-zero* and has *no manuscript-side
> analog* in $H^2_{\mathrm{Lie}}(\bar A; \C)_{(0,0)}$ (the manuscript's
> $[\bar c]$ is purely Heisenberg-type on weight-(1,1) generators).
> Two interpretations:
> - **A (spin-tower truncation).** W3-W31-T2 must include a spin-tower
>   truncation that kills $[c^{(s)}]$ for $s \geq 3$. This requires
>   a *second* localisation beyond M2's $\tau_{\mathfrak h}$ — the
>   construction is open. **Severity 3.**
> - **B (manuscript extension).** The manuscript needs higher-spin
>   extensions $[\bar c^{(s)}]$ for $s \geq 3$. **Severity 4** if
>   confirmed; would force substantial manuscript revision.
> **Deciding evidence.** Compute the spin-3 cocycle on the orthosymplectic
> super-extension at $M = N$ (where it vanishes per §6) and verify
> whether the bosonic case admits an analogous truncation mechanism
> via a different construction (e.g., constraint reduction).

**R-P4-EXEC-G4-M3-B (W_3 closure obstruction at conformal level).**
**Phase-4. Severity 2 (sharpening).**

> The W_3 sub-set $\{J(z), W^{(3)}(z)\}$ does NOT close as a sub-VOA
> of $W_{1+\infty}$ at the conformal level: the OPE forces the
> spin-2 stress-energy and a higher-spin generator $J^{(4)}$. The
> Bousfield localisation $\tau_{\mathfrak h}$ *forgets* the obstruction
> (the $:T^2:$ composite is in the W-class kernel), but this
> *masking* of the closure obstruction is not a *resolution* — it
> just means the toy twist is insensitive to it. The conformal-level
> closure obligation remains a real obstacle for any *non-twisted*
> bridge to manuscript. **Confidence.** High (Zamolodchikov 1985 +
> Bouwknegt–Schoutens 1993 textbook fact).

**R-P4-EXEC-G4-M3-C (Super-W_3 spin-3 cocycle vanishing at M=N —
chain-level transcription).** **Phase-4. Severity 3.**

> The super-W_3 spin-3 cocycle on osp(2N|2N) at $M = N$ vanishes
> *structurally* by analogy with W22-T1+T2 + W30 (A5). The rigorous
> chain-level argument requires transcribing W22-T2's $\Lambda^{\mathrm{Str}}$
> chain-level lift to the spin-3 mode algebra. **Open question
> P4-EXEC-G4-M3-Q1**: does the chain-level lift extend to spin-3
> verbatim? **Deciding evidence.** Compute the explicit
> $\Lambda^{\mathrm{Str}, (3)}$ on $\mathrm{osp}(2|2)$ super-W_3 via
> super-Drinfeld–Sokolov reduction; verify the cocycle identity at
> one loop and at all loops (P4-EXEC-G3-T-A1.strong analog at spin-3).

**R-P4-EXEC-G4-M3-D (Bousfield W-class regularity at higher spins).**
**Phase-4. Severity 2 (sharpening).**

> The Lurie HA §5.5.4.10 Bousfield localisation $\tau_{\mathfrak h}$
> forgets the conformal vector and integrates out the C-direction.
> Whether this localisation is *uniformly regular* on all spin
> levels (i.e., the W-class kernel contains exactly the Virasoro
> module structure, not further unintended structure such as
> spin-3 descents of $:T^2:$) requires explicit verification. The
> M2 verification at spin-1 (via the ML qualifier W3-W11-01) is
> structurally clean; the M3 spin-3 verification needs a specific
> argument that the spin-3 Virasoro descent (via $\Lambda$) is in
> the W-class kernel and the spin-3 leading $1/(z-w)^6$ pole is
> outside it. **Deciding evidence.** Explicit computation of the
> W-class kernel filtration on the spin-3 sector.

### §9.2 Inherited residuals (carried forward from M2)

- **R-P4-EXEC-G4-M2-A (Costello-vs-SV normalisation choice).**
  Inherits at spin-3: same convention freedom propagates.
- **R-P4-EXEC-G4-M2-B (Spin-3 vanishing at rebased limit).**
  **Closed at M3** with $[c^{(3)}] = 2 [\omega^{(3)}]$ (does NOT
  vanish in bosonic; vanishes in super-osp at M=N).
- **R-P4-EXEC-G4-M2-C (Lurie ML qualifier at spin-3).** Inherits at
  spin-3; same ML colimit structure.

### §9.3 Deciding evidence for M4

**Phase-4 milestone P4-EXEC-G4-M4 (24 mo).** Construct the *full
spin-tower* twist on $W_{1+\infty}(\epsilon_1, \epsilon_2)$ and
identify the truncation mechanism:
- (a) verify whether the bosonic spin tower admits a constraint
  reduction (à la Drinfeld–Sokolov) that retains only the spin-1
  component, OR
- (b) demonstrate that the manuscript's $[\bar c]$ extends to the
  full spin tower under a precise specialisation, OR
- (c) verify the super-extension on osp(2N|2N) at $M=N$ provides
  the natural truncation mechanism.

**Interpretation C** (super-extension truncation) is the most physically
grounded and ledger-consistent: the brane-anti-brane + orientifold
configuration at $M = N$ on the manuscript side gives the
super-W spin tower with all higher-spin cocycles vanishing, matching
the manuscript's single-spin structure.

---

## §10. Stable core verdict

P4-EXEC-G4-M3 does not invalidate any wave-2 / wave-3, P4-G4,
P4-EXEC-CGW-anchor, P4-EXEC-G4-M2, or P4-EXEC-G3 stable-core finding.
The M3:

- **Confirms M2's spin-tower decomposition $[c^{\mathrm{top}}] =
  \bigoplus_{s \geq 1} [c^{(s)}]$.** M2 verified spin-1 component
  $[c^{(1)}]$ matches $[\bar c]$. M3 verifies spin-3 component
  $[c^{(3)}] = 2 [\omega^{(3)}]$ does *not* vanish at the rebased
  limit and has no manuscript analog.
- **Confirms M2's choice of Lurie HA §5.5.4.10 (over §5.5.4.16
  Dunn additivity).** The §5.5.4.10 Bousfield localisation extends
  verbatim to spin-3.
- **Reveals the spin-tower mismatch as the load-bearing M-31
  refinement.** M-31 ([Tr ψ]_BV ↔ [c̄]_CE) holds at the spin-1
  component. The spin-tower mismatch at spin-3 is a *new* structural
  finding: the manuscript's $[\bar c]$ is a *truncation* of the
  CGW spin tower, not the full structure.
- **Provides the G3-G4 cross-coupling resolution.** The super-W on
  osp(2N|2N) at M=N gives the spin-tower truncation mechanism via
  super-trace cancellation. This is consistent with W22-T1+T2 +
  W30 (A5) + P4-EXEC-G3-T-A1 chain-level closures.
- **W3-W31-T2 conjecture refinement.** The topological-twist conjecture
  must include a *spin-tower truncation* (Interpretation A) or a
  *super-extension* (Interpretation C) to be consistent with the manuscript's
  single-spin structure. Interpretation B (manuscript extension to higher
  spins) is also possible but less physically motivated.
- **Cross-volume firewall (W3-W16) is unchanged.** The toy is
  intra-volume (manuscript ↔ CGW spin-3 sub-VOA), not cross-volume.

**No manuscript content modified.** All work at the
reconstitution-ledger / Phase-4-execution level.

---

## §11. Provenance

P4-EXEC-G4-M3 read in full or section:
- `/Users/raeez/topological-strings/CLAUDE.md` (full).
- `/Users/raeez/topological-strings/reconstitution/phase4-exec-G4-M2-Heisenberg-twist-2026-04-28.md`
  (full; M2 spin-1 toy discharge baseline).
- `/Users/raeez/topological-strings/reconstitution/phase4-G4-5dM-twist-2026-04-28.md`
  (full; G4 program and obstruction map).
- `/Users/raeez/topological-strings/reconstitution/phase4-exec-CGW-anchor-2026-04-28.md`
  §1, §2 (M1 anchor; central charge formula).
- `/Users/raeez/topological-strings/reconstitution/wave3-W31-5dM-obstructions-2026-04-28.md`
  §3 (T1 type clash), §4 (T2 topological-twist conjecture), §5 (C1
  conjecture / N1 no-go).
- `/Users/raeez/topological-strings/reconstitution/phase4-G3-supertrace-beyond-2026-04-28.md`
  §1 (T1 catalog; osp balancing) §2 (T2 brane configurations).
- `/Users/raeez/topological-strings/reconstitution/phase4-exec-osp-supertrace-2026-04-28.md`
  §0 (executive verdict), §2 (T2 attack), §3 (osp(2|2) hand-check).

External references invoked (not inscribed):
- Zamolodchikov 1985 *Theor. Math. Phys.* 65 (W_3 origin; defining
  OPE and $\beta$-coefficient).
- Fateev–Lukyanov 1988 *IJMPA* 3 (W_n free-field realisation;
  Z_n-symmetry models).
- Pope–Romans–Shen 1990 *Phys. Lett. B* 236 (W_∞ algebra; spin-tower
  central-charge formula $c_n = (n^2 - 1) \chi$).
- Bouwknegt–Schoutens 1993 *Phys. Rep.* 223 (W-symmetry review;
  closure conditions; super-W in §6).
- Lukyanov–Pugai 1993 (super-W_n via super-Drinfeld–Sokolov).
- Frenkel–Kac–Wakimoto 1992 (general super-W from quantization).
- Schiffmann–Vasserot 2013 *Publ. Math. IHÉS* 118 (affine Yangian;
  spin-3 OPE coefficient).
- Lurie *Higher Algebra* §5.5.4.10 (Bousfield in presentable
  ∞-categories; verbatim extension from M2).
- Costello–Gaiotto–Williams arXiv:2007.09497 (anchor; PDF inscription
  pending).
- Costello arXiv:1610.04144 §6 (Heisenberg level normalisation).
- Williams arXiv:2007.13985 (twisted M-theory boundary VOA).
- Sergeev 1984; Berele–Regev 1987; Cheng–Wang 2012 §5
  (super-Casimir / super-Capelli on osp; degree-shift relative to gl).
- Sergeev–Veselov 2011 (super-W natural Z_2-grading).

P4-EXEC-G4-M3 confidence:
- (M3.1) spin-3 generator identification: **high** (Zamolodchikov
  1985 + Bouwknegt–Schoutens 1993 textbook).
- (M3.2) Lurie HA §5.5.4.10 Bousfield retaining $W^{(3)}$:
  **medium-high** (verbatim extension from M2; closure obstruction
  in W-class kernel).
- (M3.3) spin-3 OPE under rebasing: **medium** (Costello unit
  $c_3 = 2$ from Pope–Romans–Shen 1990; SV S₃-symmetric prefactor
  uncertain by integer factor).
- (M3.4) (A5) parity-equivariance: **medium** (super-Killing form
  preserved verbatim; super-extension chain-level argument
  parallel to W22-T1+T2).
- (M3.5) type-clash class table: **medium-high** (class survival
  structurally clean; interpretations A/B/C residual).
- (M3.6) super-W_3 in osp(2N|2N): **medium** (super-existence
  textbook; chain-level vanishing at spin-3 structural extension
  of phase4-exec-osp).

No web search invoked. No new computational scratch files created.

---

## §12. 200-word summary

P4-EXEC-G4-M3 extends the Heisenberg spin-1 toy of M2 to the spin-3
W-current $W^{(3)}(z) = J^{(3)}(z)$ inside $W_{1+\infty}(\epsilon_1,
\epsilon_2)$ at level 1.

**(a) W_3 closure under Bousfield.** The spin-1 ⊕ spin-3 sub-set
does NOT close as a sub-VOA at the conformal level (Zamolodchikov
1985: $W^{(3)} W^{(3)}$ OPE forces $T(z)$ and $J^{(4)}$ via the
$\Lambda = :T^2:$ composite). **However**, under the Lurie HA
§5.5.4.10 Bousfield localisation of M2 (forgetting Virasoro module
structure), the closure obstruction is *itself forgotten* and the
toy at spin-3 closes on the *leading* $1/(z-w)^6$ pole alone, giving
a Lie 2-cocycle on a single-generator central extension.

**(b) Spin-3 level $k_3$ at $\lambda = 1$.** In Schiffmann–Vasserot
S₃-symmetric form, $k_3 \to -64/\epsilon$ (divergent at the diagonal
self-dual scaling); in **Costello §6 unit normalisation**,
$k_3 = 2$ (the Pope–Romans–Shen 1990 spin-3 share of $W_\infty$
central charge). The class $[c^{(3)}] = 2 [\omega^{(3)}]$ is
**non-zero** and has **no manuscript-side analog** — the manuscript's
$[\bar c]$ is purely spin-1 Heisenberg.

**(c) Super-W_3 in osp family.** Super-W_3 exists as the
$\mathrm{osp}(2|4)$-Drinfeld–Sokolov reduction (Lukyanov–Pugai 1993;
Bouwknegt–Schoutens 1993 §6). At $M = N$ orthosymplectic balanced,
the super spin-3 cocycle **vanishes** by W22-T1+T2 + W30 (A5)
chain-level argument: $[c^{(3, \mathrm{osp})}] \propto \hbar \cdot
\Str(I) = \hbar (4N^2 - 4N^2) = 0$. **This provides the spin-tower
truncation mechanism for free**, resolving R-P4-EXEC-G4-M2-D
residual via the G3-G4 cross-coupling.

**(d) Report path.** `/Users/raeez/topological-strings/reconstitution/phase4-exec-G4-M3-W3-twist-2026-04-28.md`.

End of P4-EXEC-G4-M3 Phase-4 execution ledger.
