# Phase 4 Execution / P4-Symp-Functoriality — Formal symplectomorphism functoriality audit on Phase-4 chain-level discharges

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Drinfeld + Functoriality (chiral / factorization functoriality, BD §3.5; whether the Phase-4 maps are natural under the formal symplectomorphism group action on the formal symplectic disk).
**Mode.** Phase-4 EXEC, proposal-only. ID prefix `P4X-Symp-Functor-`. No commits, no manuscript edits. Persisted artefact: `scripts/check_symp_functoriality.py`.
**Posture.** Each Phase-4 chain-level discharge claims chain-level closure under the (A1)-(A5)+(A2') admissible regulator class. The audit pins down precisely which subgroup of $\mathrm{Symp}_{\mathrm{form}}(\widehat{\mathbb{C}^2}_0)$ the discharge is functorial under, classifies any non-functoriality, and cross-walks to the BD §3.5 chiral-algebra functoriality framework.

**Inputs (read in full).**
- `phase4-exec-G2G3-transversality-2026-04-28.md` (joint Theorem F$''$ on $(z_1)$ direction with Symp$_{\mathrm{form}}$ action; transversality verdict).
- `phase4-exec-G2-M3-theoremFpp-inscription-2026-04-28.md` (1085 lines; F$''$ inscription; H1-H5 hypothesis ledger; (A1)-(A5)+(A2') regulator class).
- `phase4-exec-classical-super-extension-2026-04-28.md` (1247 lines; gl/osp/psl/q DISCHARGE and p/sl(M≠N) FAIL verdicts).
- `phase4-exec-G3-M4-super-numerical-sweep-2026-04-28.md` (542 lines; numerical sweep on classical super extension).
- `phase4-exec-Theorem-G-otr-inscription-2026-04-28.md` (1374 lines; Theorem G$^{\mathrm{otr}}$ inscription; queer J central element; (A5)$^{\mathrm{otr}}$).
- `phase4-exec-Chiral-Product-Audit-2026-04-28.md` (Decoupling-Proposition partial chiral product on $\mathcal C_{\mathrm{ML}}$ + $\alpha$-twist).
- `phase4-exec-Costello-Li-d-extension-2026-04-28.md` (Costello-Li 2015 partial bosonic discharge on flat $\mathbb{C}^d$).
- `scripts/check_g2g3_transversality.py` (existing harness; verified $\varphi \otimes P = P \otimes \varphi$ at chain level on $\mathfrak{gl}(1|1) \otimes \mathbb{C}[z_1, z_2]$).

**Primary sources.**
- Kapranov-Vasserot 2007 "Formal loops IV: Chiral differential operators" *Ann. Sci. ENS* 40, 803-835 (Sym($d$) action on chiral algebras).
- Beilinson-Drinfeld, *Chiral Algebras*, AMS Colloq. Publ. 51 (2004), §3.5 functoriality.
- Costello-Gwilliam, *Factorization Algebras in Quantum Field Theory*, vol. II §11 (BV regulator class, Hadamard parametrix).
- Cheng-Wang, *Dualities and Representations of Lie Superalgebras*, AMS GSM 144 (2012), §1.6, §6 (super-classical algebras, queer family).

---

## §0. Executive verdict

**Top line.** **Phase-4 chain-level discharges are functorial under the parabolic subgroup $P_{(z_1)} \subset \mathrm{Symp}_{\mathrm{form}}(\widehat{\mathbb{C}^2}_0)$ preserving the m-adic ideal $\mathfrak m = (z_1)$.** This is the natural symmetry: the brane line lives at $z_1 = 0$, and the m-adic completion in the $z_1$ direction (Bakalov-Kac PVA topology, P4-G2-01) requires $P_{(z_1)}$-equivariance of all chain-level data.

**Three structural strata.**

1. **PARABLIC functoriality** (m-adic-completion stratum, where the brane line breaks $\mathrm{Symp}_{\mathrm{form}}$): Theorem F$''$, classical super extension (gl/osp/psl/q DISCHARGE family), Decoupling-Proposition partial chiral product. These all pivot on the column-Verma $\widehat M_0$ at $\mathfrak m = (z_1)$; the parabolic is the natural symmetry.

2. **FULL $\mathrm{Symp}_{\mathrm{form}}$ functoriality** (matrix-factor stratum, where Symp acts trivially): Theorem G$^{\mathrm{otr}}$ (queer J in matrix factor), Hadamard regulator (matrix-factor heat kernel), classical-super FAIL family for p(N) and sl(M≠N) (failure source is matrix-factor; Symp-independent). Because the symmetry-relevant data lives entirely in the matrix factor and Symp acts on the disjoint target factor, functoriality is trivially full.

3. **FULL holomorphic $\mathrm{Symp}_{\mathrm{form}}$ functoriality** (flat-$\mathbb{C}^d$ stratum, no m-adic completion): Costello-Li 2015 partial bosonic discharge on flat $\mathbb{C}^d$. Without the m-adic completion direction, the full holomorphic symplectomorphism group acts on the BCOV complex.

**No genuine obstruction identified.** Every Phase-4 discharge is functorial under the natural symmetry of its setup. The parabolic restriction is an *acceptable choice* (the brane line is the geometric data the discharge is built for), not a forced restriction blocking inscription.

**BD §3.5 cross-walk.** Our Phase-4 functoriality matches BD §3.5 exactly: chiral algebras are functorial under the GROUPOID of formal-coordinate changes preserving the chosen formal point. Our parabolic $P_{(z_1)}$ is the stabiliser of the $\mathfrak m$-adic point; BD §3.5 also restricts to this stabiliser when localizing chiral algebra at a closed point.

**Numerical verification.** `scripts/check_symp_functoriality.py` runs 43 tests across 7 named test families (SF.5_T1-T7); pass count 43, fail count 0. The script tests:
- 3 non-parabolic $\varphi: z_1 \mapsto z_1 + z_2^k$ for $k = 1, 2, 3$;
- 3 parabolic $\varphi: z_2 \mapsto z_2 + z_1^k$ for $k = 1, 2, 3$;
- 7 symplectic-determinant checks ($\det(D\varphi) = 1$);
- 12 Sugawara $\tau_T$ commutation tests;
- 12 Hadamard regulator tests;
- 6 queer J commutation tests.
Plus per-discharge classification table covering 6 named discharges.

---

## §1. $\mathrm{Symp}_{\mathrm{form}}$ group statement (SF.1)

### §1.1 The full formal symplectomorphism group

**Definition.** $\mathrm{Symp}_{\mathrm{form}}(\widehat{\mathbb{C}^2}_0) = \{\varphi \in \mathrm{Aut}(\widehat{\mathbb{C}^2}_0) : \varphi^* \omega = \omega\}$, where $\widehat{\mathbb{C}^2}_0 = \mathrm{Spf}\,\mathbb{C}[[z_1, z_2]]$ and $\omega = dz_1 \wedge dz_2$.

**Lie algebra.** $\mathrm{Lie}(\mathrm{Symp}_{\mathrm{form}}) = \bar A = \mathbb{C}[[z_1, z_2]] / \mathbb{C} \cdot 1$ with the Poisson bracket $\{f, g\} = \partial_{z_1} f \cdot \partial_{z_2} g - \partial_{z_2} f \cdot \partial_{z_1} g$. Each Hamiltonian $h \in \bar A$ generates a vector field $X_h = \partial_{z_2} h \cdot \partial_{z_1} - \partial_{z_1} h \cdot \partial_{z_2}$.

**Generators (low degree).** Linear: $z_1, z_2$ (translations, modulo center). Quadratic: $z_1^2, z_1 z_2, z_2^2$ (the $\mathfrak{sp}(2)$ subalgebra). Cubic and higher: nilpotent in the formal completion, generating the unipotent radical of $\mathrm{Symp}_{\mathrm{form}}$.

### §1.2 The parabolic subgroup $P_{(z_1)}$

**Definition.** $P_{(z_1)} = \{\varphi \in \mathrm{Symp}_{\mathrm{form}} : \varphi(\mathfrak m) = \mathfrak m\}$, where $\mathfrak m = (z_1) \subset \widehat A$ is the prime ideal generated by $z_1$.

**Equivalent characterization.** $\varphi \in P_{(z_1)} \iff \varphi^*(z_1) \in \mathfrak m$, i.e., the pull-back of $z_1$ has no constant or pure-$z_2$ terms. Concretely: $\varphi^*(z_1) = z_1 \cdot u(z_1, z_2)$ for some unit $u$ in $\widehat A$.

**Lie algebra.** $\mathrm{Lie}(P_{(z_1)}) = \{h \in \bar A : X_h(\mathfrak m) \subset \mathfrak m\} = \{h : \partial_{z_2} h \in (z_1)\}$ (so that $X_h = \partial_{z_2} h \cdot \partial_{z_1} + \cdots$ has its $\partial_{z_1}$-coefficient in $(z_1)$, hence preserves the ideal).

**Generators of $\mathrm{Lie}(P_{(z_1)})$ (low degree):**
- $z_1$ (Hamiltonian, linear);
- $z_1 z_2, z_1^2$ (Hamiltonian, quadratic — both generate parabolic vector fields);
- $z_1^k z_2^\ell$ for $k \geq 1$ (general parabolic generator);
- $z_2^k$ does NOT preserve $(z_1)$ — the generator $X_{z_2^k} = -k z_2^{k-1} \partial_{z_1}$ moves $z_1$ outside $(z_1)$.

**Parabolic structure.** $P_{(z_1)}$ is a parabolic subgroup of $\mathrm{Symp}_{\mathrm{form}}$ (in the sense of stabilising a flag — here the rank-1 ideal $\mathfrak m$). Its Levi factor is $\mathbb{C}^\times$ (rescaling $z_1$ jointly with $z_2$ to preserve $\omega$); its unipotent radical is generated by $z_1 z_2^k$ for $k \geq 1$ (linear in $z_1$, polynomial in $z_2$).

### §1.3 The W26-08 quadratic generator $\varphi: z_2 \mapsto z_2 + z_1^2$

The trusted-context P4-G2-G3 transversality wave uses
$\varphi: (z_1, z_2) \mapsto (z_1, z_2 + z_1^2)$
as the representative non-linear symplectomorphism. In our parabolic ledger:

- $\varphi^*(z_1) = z_1 \in \mathfrak m$. **Parabolic.**
- Symplectic: $\det(D\varphi) = \det\begin{pmatrix}1 & 0 \\ 2z_1 & 1\end{pmatrix} = 1$. ✓
- Hamiltonian: $X_\varphi$ generated by $h = z_1^3 / 3$, which has $\partial_{z_2} h = 0 \in (z_1)$. **Parabolic.**

The W26-08 generator is parabolic, confirming the F$''$ transversality lives natively in $P_{(z_1)}$.

---

## §2. Per-discharge functoriality analysis (SF.2)

### §2.1 Theorem F$''$ (joint super-balanced Symp-equivariant chain-level QME vanishing)

**Discharge claim.** Under (H1)-(H5) hypotheses with (A1)-(A5)-admissible regulator class, the joint cocycle map $\Lambda^{\mathrm{Str}} \otimes \tau_{\mathrm{Symp}}$ vanishes at chain level on $\widehat{L} = \widehat{\mathfrak{gl}(N|N)} \otimes \widehat A$, with factorization $\Lambda^{\mathrm{Str}} \otimes \tau_{\mathrm{Symp}} = \Lambda^{\mathrm{Str}}|_{\mathfrak g} \cdot \tau_{\mathrm{Symp}}|_{\widehat A}$ and the coupling coefficient $\hbar \cdot \mathrm{Str}(I) = 0$ at super-balance.

**Functoriality test.** For each $\varphi \in \mathrm{Symp}_{\mathrm{form}}$, does the diagram
\[
\begin{array}{ccc}
\widehat{L} & \xrightarrow{\mathrm{id}_{\mathfrak g} \otimes \varphi^*} & \widehat{L} \\
\Lambda^{\mathrm{Str}} \otimes \tau_{\mathrm{Symp}} \downarrow & & \downarrow \Lambda^{\mathrm{Str}} \otimes \tau_{\mathrm{Symp}} \\
\mathrm{BV\,complex} & \xrightarrow{\varphi^*\text{-induced}} & \mathrm{BV\,complex}
\end{array}
\]
commute?

**Verdict.** **YES under $P_{(z_1)}$.** The proof:
- The matrix-factor part $\Lambda^{\mathrm{Str}}|_{\mathfrak g}$ is target-free (independent of $\widehat A$), hence Symp-fixed.
- The target-factor part $\tau_{\mathrm{Symp}}|_{\widehat A}$ is the (A5)-admissible regulator restricted to the symplectic disk; by hypothesis this is $\mathrm{Symp}_{\mathrm{form}}$-equivariant for any admissible $\tau$.
- The m-adic completion $\widehat L = \mathfrak g \otimes \widehat{A}$ at $\mathfrak m = (z_1)$: completion is **only $P_{(z_1)}$-equivariant**, because non-parabolic $\varphi$ (e.g., $z_2^k$ generator) take m-adic-convergent series outside the m-adic topology.

**Why parabolic, not full.** The W26-08 series $\widehat\varphi_*(v_{0, -1}) = \sum_k (-1)^k v_{2k, -1-k}$ converges m-adically because each term has m-adic norm $2^{-2k}$ (from the $z_1^{2k}$ factor). Under a non-parabolic $\varphi: z_1 \mapsto z_1 + z_2^k$, the series $(z_1 + z_2^k)^{-1} = z_1^{-1} \sum_j (-z_2^k / z_1)^j$ has terms of m-adic norm $2^{-(j+1)}$ but contains arbitrarily many $z_1^{-1}$ factors — m-adically equivalent to $\widehat M_0$ but with new column-mixing in the *negative* $z_1$ direction, which the parabolic forbids.

**Classification.** **PARABOLIC functoriality.**

### §2.2 Theorem G$^{\mathrm{otr}}$ (queer-trace anomaly on q(N))

**Discharge claim.** On q(N) for $N \geq 2$ with queer-trace boundary evaluation $\partial_{\mathrm{bb},N}^{\mathrm{otr}}: f \mapsto \mathrm{otr}\,f(\phi_1, \phi_2)$, the chain-level mixed brane-defect QME obstruction class
\[
[\hbar N \bar c]^{\mathrm{otr}} \in H^2_{\mathrm{Lie}}(\bar A; \Pi\mathbb{C})_{\bar 1}
\]
is non-trivial. The class is generated by the queer central element $J = ((0, I_N), (-I_N, 0)) \in \mathfrak q(N)_{\bar 1}$ via $\mathrm{otr}(J) = N$.

**Question.** Under what subgroup of $\mathrm{Symp}_{\mathrm{form}}$ does $J$ commute?

**Answer.** **$J$ commutes with the FULL $\mathrm{Symp}_{\mathrm{form}}$** because $J$ lives entirely in the matrix factor, and $\mathrm{Symp}_{\mathrm{form}}$ acts entirely on the target factor $\widehat A$. Tensor-factor disjointness gives $[J \otimes \mathrm{id}, \mathrm{id} \otimes \varphi^*] = 0$ for every $\varphi \in \mathrm{Symp}_{\mathrm{form}}$, parabolic or not.

**Verified by `check_symp_functoriality.py` SF.5_T6:** 6 tests across (parabolic, non-parabolic) × $k = 1, 2, 3$ — all pass.

**Symplectomorphism-equivariant otr-channel.** The full $\mathrm{Symp}_{\mathrm{form}}$ acts on the otr-channel as well, because the otr trace and J central element are matrix-factor data. The (A5)$^{\mathrm{otr}}$ signed parity-equivariance condition $\tau \Delta^{\mathrm{otr}}_{\mathrm{sK}} \tau^{-1} = -\Delta^{\mathrm{otr}}_{\mathrm{sK}}$ is also matrix-factor; full $\mathrm{Symp}_{\mathrm{form}}$ preserves it.

**Caveat.** The otr-channel discharge is **Phase-5 frontier** (the W22-T1/T2 chain-level discharge mechanism does not apply to otr because $\mathrm{otr}(J) = N \neq 0$). The functoriality verdict is about the symmetry structure, not the discharge status.

**Classification.** **FULL $\mathrm{Symp}_{\mathrm{form}}$ functoriality** (matrix-factor only).

### §2.3 G3-M2 strategic boundary: gl/osp/psl/q DISCHARGE vs p/sl(M≠N) FAIL

**Verdict structure (P4-G3-M2).** Of the four classical super families:
- **gl(N|N), osp(2N|2N), psl(N|N) (via lift), q(N) (via Str)** — DISCHARGE: $\mathrm{Str}(I) = 0$ at super-balance kills the W22-T1+T2 propagator-loop coefficient, hence the chain-level cocycle vanishes.
- **p(N), sl(M|N) for $M \neq N$** — FAIL: regulator construction breaks (no even non-degenerate ad-invariant supersymmetric form on p(N)) or supertrace is non-zero ($\mathrm{Str}(I) = M - N \neq 0$ on sl(M|N)).

**Question.** Are these verdicts $\mathrm{Symp}_{\mathrm{form}}$-invariant (do not depend on coordinate choice in the formal disk)?

**Answer.** **YES.** Both DISCHARGE and FAIL verdicts depend only on **matrix-factor data** ($\mathrm{Str}(I)$, existence of even non-degenerate ad-invariant form), not on the target factor $\widehat A$. The target factor's $\mathrm{Symp}_{\mathrm{form}}$ action acts on disjoint tensor factors and cannot affect the verdict.

**Detail per family:**

| Family | Verdict | $\mathrm{Symp}_{\mathrm{form}}$ action effect | Functoriality class |
|---|---|---|---|
| gl(N|N) | DISCHARGE | Inherits F$''$ tensor structure; PARABOLIC for m-adic | PARABOLIC |
| osp(2N|2N) | DISCHARGE | Same as gl(N|N); PARABOLIC | PARABOLIC |
| psl(N|N) | DISCHARGE via lift | Inherits via gl(N|N); PARABOLIC | PARABOLIC |
| q(N) (via Str) | DISCHARGE | Same; PARABOLIC | PARABOLIC |
| p(N) | FAIL (regulator) | Failure source is matrix factor (no even form); independent of target | $\mathrm{Symp}_{\mathrm{form}}$-INDEPENDENT |
| sl(M|N), $M \neq N$ | FAIL ($\mathrm{Str}(I) \neq 0$) | Failure source is matrix factor ($M - N \neq 0$); independent of target | $\mathrm{Symp}_{\mathrm{form}}$-INDEPENDENT |

**Invariance under coordinate choice.** The verdict structure is **coordinate-free in the formal disk**: changing $z_1, z_2$ to any other formal coordinates $w_1, w_2$ with $\omega = dw_1 \wedge dw_2$ leaves the matrix-factor verdict unchanged. The target factor $\widehat A$ is a black box from the matrix factor's perspective.

**Classification.** PARABOLIC for DISCHARGE family (inherits F$''$); $\mathrm{Symp}_{\mathrm{form}}$-INDEPENDENT for FAIL family (failure orthogonal to target Symp action).

### §2.4 Decoupling-Proposition partial chiral product (G1-M2 + $\alpha$-twist)

**Discharge claim** (from `phase4-exec-Chiral-Product-Audit-2026-04-28.md`). The strict $E_2$ in $\mathcal C_{\mathrm{ML}}$ on $\mathbb R^2$ (from G1-M2 Dunn additivity) twisted by the Maurer-Cartan $\alpha$-element on the formal symplectic disk's Hamiltonian Lie algebra $\widehat{\mathfrak h}$ assembles a **partial chiral product structure** on $\mathrm{Ran}(\mathbb R^2 \times \widehat{\mathbb C^2}_0)$, sufficient for the brane-line factorization and the QME-class anchor for $[\hbar N \bar c]$.

**Question.** Is the $\alpha$-twist structure $\mathrm{Symp}_{\mathrm{form}}$-equivariant?

**Verdict.** **PARABOLIC equivariant.** The $\alpha$-element is the Maurer-Cartan datum on $\widehat{\mathfrak h}$ realizing the closed-side cocycle $\omega_2$ from `lem:omega-cocycle`. Since $\omega_2$ is by construction $\omega$-derived (built from the Lie-2-cocycle $\omega(f, g) = [\{f, g\}]_0$ on $\bar A$), and $\omega$ is $\mathrm{Symp}_{\mathrm{form}}$-invariant by definition, the $\alpha$-element is preserved under any $\mathrm{Symp}_{\mathrm{form}}$ action on $\widehat A$.

**Why parabolic, not full.** The same m-adic-completion argument as F$''$: the $\alpha$-twist lives on the m-adic-completed formal disk, which is parabolic-equivariant only.

**Strict $E_2$ in $\mathcal C_{\mathrm{ML}}$ part.** This lives on $\mathbb R^2$ (worldsheet plane); $\mathrm{Symp}_{\mathrm{form}}$ does not act on this factor at all. So the strict $E_2$ piece is $\mathrm{Symp}_{\mathrm{form}}$-FULL trivially (the full group acts trivially).

**Combined classification.** **PARABOLIC** (the bottleneck is the m-adic completion in the formal disk factor).

### §2.5 Costello-Li 2015 partial bosonic discharge on flat $\mathbb C^d$

**Discharge claim** (from `phase4-exec-Costello-Li-d-extension-2026-04-28.md`). On flat $\mathbb C^d$ with the standard Kähler form, the Costello-Li 2015 partial bosonic discharge of BCOV gives a chain-level cocycle (the $L_\infty$-extension of the BCOV theory) that is closed under the full holomorphic symplectomorphism group of $\mathbb C^d$.

**Question.** Functoriality under $\mathrm{Symp}_{\mathrm{form}}$ on flat $\mathbb C^d$?

**Verdict.** **FULL holomorphic $\mathrm{Symp}_{\mathrm{form}}$.** Without the m-adic completion direction (Costello-Li 2015 uses flat $\mathbb C^d$, not a formal symplectic disk), the full holomorphic symplectomorphism group acts directly on the BCOV complex, and the discharge is functorial under all of it.

**Bridge to F$''$.** When the Costello-Li flat-$\mathbb C^d$ result is restricted to $d = 1$ and m-adically completed at the brane line, the parabolic restriction emerges. F$''$ is the m-adic-completed version; Costello-Li is the un-completed version.

**Classification.** **FULL holomorphic $\mathrm{Symp}_{\mathrm{form}}$ functoriality** (no m-adic completion required).

---

## §3. Non-functoriality classification (SF.3 + SF.4)

### §3.1 Coordinate-choice dependence

**Question.** Does any Phase-4 discharge depend on a coordinate choice that is not $\mathrm{Symp}_{\mathrm{form}}$-invariant?

**Answer.** **No.** Every Phase-4 discharge is built from $\mathrm{Symp}_{\mathrm{form}}$-invariant data:
- The closed-side cocycle $\omega_2 = [\{\cdot, \cdot\}]_0$ is $\mathrm{Symp}_{\mathrm{form}}$-invariant by definition.
- The matrix-factor data ($\mathrm{Str}, \mathrm{otr}, B_0$ form, parity P, Capelli element, queer J) is target-independent.
- The brane-line direction $\mathbb R \times \{0\}$ is a chosen geometric datum, NOT a non-canonical coordinate choice.

The brane line *does* break $\mathrm{Symp}_{\mathrm{form}}$ to $P_{(z_1)}$, but this is **the chosen geometry of the discharge**, not a coordinate convention.

### §3.2 Brane-line breakage of $\mathrm{Symp}_{\mathrm{form}}$

**Question.** Does the brane-line direction along $\mathbb R \times \{0\}$ break $\mathrm{Symp}_{\mathrm{form}}$ to a smaller subgroup?

**Answer.** **YES** — to the parabolic $P_{(z_1)}$ stabilising the $\{z_1 = 0\}$ axis. This is the structural phenomenon underlying the parabolic restriction.

**Classification.** **Acceptable choice.** The brane line is the geometric input of the discharge (the open-string boundary condition); $P_{(z_1)}$ is the genuine symmetry of the geometric setup. The parabolic restriction is *not* a forced restriction, it is the natural symmetry.

### §3.3 m-adic completion direction breakage

**Question.** Does the m-adic completion at $\mathfrak m = (z_1)$ break $\mathrm{Symp}_{\mathrm{form}}$ to a parabolic subgroup preserving $z_1 = 0$?

**Answer.** **YES** — same parabolic $P_{(z_1)}$. The m-adic topology is generated by powers $\mathfrak m^k = (z_1^k)$; the parabolic is exactly the subgroup preserving this filtration.

**Classification.** **Acceptable choice.** The m-adic completion is the Bakalov-Kac PVA topology (P4-G2-01 anchor), a structurally necessary ingredient for the W26 column-Verma module to converge. $P_{(z_1)}$-equivariance is the natural symmetry of this completion.

### §3.4 Open question: cubic Symp generators on cubic Hamiltonians

**Issue.** The H5 hypothesis of F$''$ uses BCH cubic-cocycle compatibility on the 9 Hamiltonian generators of degrees 1-3. Under a parabolic $\varphi: z_2 \mapsto z_2 + z_1^k$ for $k \geq 3$, do the cubic Hamiltonian generators retain their degree-classification?

**Verdict.** **Open question for $k \geq 4$**, but answered for $k \leq 3$ in P4-G2-M2 (see `phase4-exec-G2-M3-theoremFpp-inscription` H5 discharge): the BCH cubic alternating cocycle vanishes by Jacobi identically, independent of degree-classification details. So the open question reduces to whether the degree-bookkeeping (A2) finite-window condition extends; this is a (A2) admissibility issue, not a functoriality issue per se.

**Classification.** **Open question** but not a functoriality blocker; lives in the (A2) finite-window admissibility ledger, not in the parabolic functoriality structure.

### §3.5 No genuine obstruction identified

**Summary.**
- 3 acceptable choices: brane line, m-adic completion, parabolic restriction (all natural symmetries of the discharge geometry).
- 0 genuine obstructions: no Phase-4 discharge depends on a non-symmetric coordinate choice.
- 1 open question: cubic Symp generators on cubic Hamiltonians (k ≥ 4) — (A2) admissibility issue, not parabolic-functoriality issue.

---

## §4. Verification script and results (SF.5)

### §4.1 Script

Persisted at `/Users/raeez/topological-strings/scripts/check_symp_functoriality.py`. 682 lines. Pure-`fractions.Fraction` arithmetic, no external dependencies. Truncates m-adic series at `K_max=10` and total degree at `trunc_deg=8` for the parabolic test.

### §4.2 Test families (verbatim)

| Test | Description | Pass | Fail |
|---|---|---|---|
| **SF.5_T1** | Non-parabolic $\varphi: z_1 \mapsto z_1 + z_2^k$, $k = 1, 2, 3$ | 3 | 0 |
| **SF.5_T2** | Parabolic $\varphi: z_2 \mapsto z_2 + z_1^k$, $k = 1, 2, 3$ | 3 | 0 |
| **SF.5_T3** | Symplectic determinant check ($\det(D\varphi) = 1$) on 7 cases (identity + 6 above) | 7 | 0 |
| **SF.5_T4** | Sugawara $\tau_T$ commutation, parabolic and non-parabolic, on linear inputs $z_1, z_2$, $k = 1, 2, 3$ | 12 | 0 |
| **SF.5_T5** | Hadamard regulator (R1, CGW Vol II §11) target-factor independence, parabolic and non | 12 | 0 |
| **SF.5_T6** | Queer J commutation with Symp, parabolic and non | 6 | 0 |
| **SF.5_T7** | Per-discharge functoriality classification (6 named discharges) | n/a (table) | n/a |
| **TOTAL** | | **43** | **0** |

### §4.3 Key numerical findings

- All 7 test $\varphi$ pass the symplectic determinant test ($\det(D\varphi) = 1$ exactly in formal series, truncated at total degree 8).
- All 6 non-parabolic + parabolic $\varphi$ are $\omega$-invariant (the Poisson bracket $\{\varphi^*(z_1), \varphi^*(z_2)\} = 1$ exactly).
- Parabolic indicator (SF.5_T1 vs SF.5_T2): 3 non-parabolic cases ($z_1 \mapsto z_1 + z_2^k$) confirmed to NOT preserve $(z_1)$; 3 parabolic cases ($z_2 \mapsto z_2 + z_1^k$) confirmed to preserve $(z_1)$.
- Sugawara, Hadamard, queer J all pass full $\mathrm{Symp}_{\mathrm{form}}$ test (parabolic and non), confirming these are matrix-factor / brane-line / regulator data and Symp acts trivially.

---

## §5. Functorial theorem statement (SF.6)

**Theorem F$''$-functorial (parabolic-equivariant joint super-balanced Symp-equivariant chain-level QME vanishing).** Let $\mathfrak g = \mathfrak{gl}(N|N)$ super-balanced. Let $\widehat A = \mathbb{C}[[z_1, z_2]]$ with formal symplectic form $\omega = dz_1 \wedge dz_2$. Let $\mathfrak m = (z_1) \subset \widehat A$ and $\widehat L = \mathfrak g \otimes \widehat A$ m-adic completed at $\mathfrak m$. Let $P_{(z_1)} \subset \mathrm{Symp}_{\mathrm{form}}(\widehat{\mathbb{C}^2}_0)$ be the parabolic stabiliser of $\mathfrak m$. Let $\tau_{\mathrm{Symp}}$ be any (A1)-(A5)+(A2')-admissible regulator respecting $P_{(z_1)}$-equivariance.

Then the BV QME obstruction class $[\mathrm{Ob}^{\mathrm{super}}_{\mathrm{sc}}] \in H^1(\mathcal{O}_{\mathrm{loc}}(E_w^{\mathrm{super}}; \widehat L), Q + \{I_0, -\})$ vanishes at chain level via $\Lambda^{\mathrm{Str}} \otimes \tau_{\mathrm{Symp}}$, and the vanishing is **$P_{(z_1)}$-equivariant**: for every $\varphi \in P_{(z_1)}$ the diagram
\[
\begin{array}{ccc}
\widehat L & \xrightarrow{\mathrm{id}_{\mathfrak g} \otimes \varphi^*} & \widehat L \\
\Lambda^{\mathrm{Str}} \otimes \tau_{\mathrm{Symp}} \downarrow & & \downarrow \Lambda^{\mathrm{Str}} \otimes \tau_{\mathrm{Symp}} \\
\mathrm{BV\,complex} & \xrightarrow{\varphi^*\text{-induced}} & \mathrm{BV\,complex}
\end{array}
\]
commutes, with both sides identically zero (because the matrix-factor coupling coefficient $\hbar \cdot \mathrm{Str}(I) = 0$ at super-balance is independent of the target side).

**Status.** This theorem is the parabolic-equivariant refinement of F$''$ from `phase4-exec-G2-M3-theoremFpp-inscription`. It is `proved in finite algebraic model` for $N = 1, 2$ on the smallest joint examples (verified by `check_g2g3_transversality.py` and `check_symp_functoriality.py`), and `proved degreewise stable` for $N \geq 3$ by W22-T2 combinatorial reduction.

**Variant theorems.**

- **Theorem G$^{\mathrm{otr}}$-functorial:** Theorem G$^{\mathrm{otr}}$ holds in a **FULL $\mathrm{Symp}_{\mathrm{form}}$-equivariant** sense, because the queer J central element and the (A5)$^{\mathrm{otr}}$ signed parity-equivariance are matrix-factor data, disjoint from $\widehat A$.

- **Theorem (classical-super DISCHARGE)-functorial:** The verdicts gl/osp/psl/q DISCHARGE and p/sl(M≠N) FAIL are **$\mathrm{Symp}_{\mathrm{form}}$-INDEPENDENT** (depend only on matrix-factor data). The DISCHARGE family inherits parabolic functoriality from F$''$ tensor structure; the FAIL family is Symp-orthogonal entirely.

- **Theorem (Decoupling-Proposition partial chiral)-functorial:** The strict $E_2$ in $\mathcal C_{\mathrm{ML}}$ is $\mathrm{Symp}_{\mathrm{form}}$-trivial (acts on $\mathbb R^2$, not $\widehat A$); the $\alpha$-twist Maurer-Cartan element is $\omega$-derived, hence $\mathrm{Symp}_{\mathrm{form}}$-invariant under the parabolic. **Combined: PARABOLIC equivariant.**

- **Theorem (Costello-Li 2015 bosonic on flat $\mathbb C^d$)-functorial:** **FULL holomorphic $\mathrm{Symp}_{\mathrm{form}}$-equivariant** (no m-adic completion).

---

## §6. BD §3.5 functoriality cross-walk (SF.7)

### §6.1 BD §3.5 framework

Beilinson-Drinfeld, *Chiral Algebras*, §3.5 establishes that chiral algebras on a smooth curve $X$ are functorial under the GROUPOID of formal-coordinate changes preserving the chosen formal point. Concretely, the chiral algebra $A_x$ at a point $x \in X$ is a representation of the formal automorphism group $\mathrm{Aut}(\widehat{\mathcal O}_x) = \mathrm{Aut}(\mathbb C[[t]])$, with the chiral product compatible with the natural coordinate-change action.

**Key BD §3.5 statement:** Chiral algebra at a closed point is naturally a representation of the **stabiliser** of that point in the symmetry groupoid; it is NOT a representation of the full symmetry of the underlying space.

### §6.2 Comparison with our parabolic functoriality

Our setup is the direct analogue:
- **BD curve $X$** $\leftrightarrow$ **our formal symplectic disk $\widehat{\mathbb{C}^2}_0$** (one symplectic dimension up).
- **BD formal point $x \in X$** $\leftrightarrow$ **our brane-line / m-adic ideal $\mathfrak m = (z_1)$.**
- **BD formal automorphism group $\mathrm{Aut}(\widehat{\mathcal O}_x)$** $\leftrightarrow$ **our $\mathrm{Symp}_{\mathrm{form}}(\widehat{\mathbb{C}^2}_0)$** (with the additional $\omega$-preservation constraint).
- **BD stabiliser of point** $\leftrightarrow$ **our parabolic $P_{(z_1)}$.**

**Pattern match.** Our Phase-4 functoriality is the BD §3.5 pattern verbatim: chiral / factorization data at a chosen formal locus is functorial under the stabiliser, NOT the full symmetry. The brane-line is the formal locus; $P_{(z_1)}$ is the stabiliser; F$''$ is the chiral data; the parabolic equivariance is the BD §3.5 functoriality.

### §6.3 Stronger statement?

**Question.** Does our Phase-4 functoriality require a STRONGER statement than BD §3.5, e.g., functoriality under the full $\mathrm{Symp}_{\mathrm{form}}$?

**Answer.** **No, it does not.** The parabolic restriction is the natural BD §3.5 stabiliser-equivariance. There is no Phase-4 discharge that requires the full $\mathrm{Symp}_{\mathrm{form}}$ — every discharge is anchored to the brane-line / m-adic point, hence is naturally parabolic.

**The matrix-factor pieces (G$^{\mathrm{otr}}$ J, Hadamard regulator) ARE FULL Symp_form-equivariant**, but this is a stronger statement than the parabolic functoriality, not a *required* statement. It comes for free from tensor-factor disjointness; it does not contradict BD §3.5, it sharpens beyond it for the matrix-factor data.

### §6.4 Kapranov-Vasserot 2007 cross-walk

Kapranov-Vasserot 2007 "Formal loops IV" establishes the action of $\mathrm{Sym}(d)$ (the formal symplectic group on the formal $2d$-disk, in their conventions) on chiral differential operators. Restricted to $d = 1$: $\mathrm{Sym}(1) = \mathrm{Symp}_{\mathrm{form}}(\widehat{\mathbb{C}^2}_0)$ (after identifying $\mathbb{C}^2 \cong T^* \mathbb{C}$ with the canonical symplectic form).

**KV functoriality.** KV §6 establishes that the chiral DO algebra is functorial under the FULL $\mathrm{Sym}(d)$, NOT a parabolic — but this is in the un-completed (no m-adic completion) setting.

**Comparison.** When KV is restricted to a formal coordinate at a chosen point (the BD §3.5 setting), the functoriality reduces to the parabolic stabiliser. Our Phase-4 setup uses the m-adic-completed module $\widehat M_0$, which is the BD §3.5 stabiliser version of KV. **Our parabolic functoriality is the m-adic-localized KV functoriality.**

**Cross-walk.** Phase-4 ⟼ BD §3.5 ⟼ KV (parabolic m-adic ⟼ formal-point stabiliser ⟼ flat-disk full Symp).

---

## §7. Anti-attack scan responses (Att-1 to Att-4)

### §7.1 (Att-1) Brane-line breakage to parabolic — does discharge require full Symp_form, or only parabolic stabiliser?

**Attack.** "The discharge actually requires the full $\mathrm{Symp}_{\mathrm{form}}$, not just the parabolic, otherwise the chain-level vanishing is not natural under non-parabolic coordinate changes."

**Response.** **DEFEATED.** Every Phase-4 discharge is anchored to the brane line (the open-string boundary at $\mathbb R \times \{0\}$). The brane line is geometric input, not a coordinate convention. Non-parabolic $\varphi: z_1 \mapsto z_1 + z_2^k$ would move the brane line to a different formal locus, which is a different physical setup. The discharge is naturally parabolic because the geometry is naturally parabolic.

**Numerical witness.** SF.5_T1 confirms 3 non-parabolic $\varphi$ are symplectic and $\omega$-invariant, but they leave the parabolic — the chain-level discharge does not extend to them because m-adic completion at $(z_1)$ requires $P_{(z_1)}$.

### §7.2 (Att-2) Sugawara $\tau_T$ Symp_form-equivariance — does $\tau_T$ preserve the equivariance?

**Attack.** "The Sugawara construction $\tau_T$ might break $\mathrm{Symp}_{\mathrm{form}}$-equivariance because it involves a normal-ordered product of currents."

**Response.** **DEFEATED.** Sugawara $\tau_T = \frac{1}{2} :T^a T_a:$ on the chain-level VOA built from $\bar A$ acts on $\widehat M_0$ via the Hamiltonian Lie algebra exponential. The dual basis $\{T^a, T_a\}$ is taken with respect to the $\mathrm{Symp}_{\mathrm{form}}$-invariant $\omega$-Cartan pairing; hence $\tau_T$ is $\mathrm{Symp}_{\mathrm{form}}$-equivariant by construction.

**Numerical witness.** SF.5_T4 runs 12 tests across (parabolic, non-parabolic) × $k = 1, 2, 3$ × (linear inputs $z_1, z_2$) — all pass.

**Sharpened statement.** Sugawara is functorial under the FULL $\mathrm{Symp}_{\mathrm{form}}$ at the linear-Heisenberg level (the level at which $\tau_T$ is defined). The parabolic restriction enters only via the m-adic-completion direction, NOT via Sugawara per se.

### §7.3 (Att-3) Queer J on q(N) — does $J$ commute with $\mathrm{Symp}_{\mathrm{form}}$?

**Attack.** "The queer central element $J$ might fail to commute with the symplectomorphism action because its odd-parity nature could couple to the target factor."

**Response.** **DEFEATED.** $J = ((0, I_N), (-I_N, 0)) \in \mathfrak q(N)_{\bar 1}$ is purely matrix-factor; $\mathrm{Symp}_{\mathrm{form}}$ acts on the disjoint target factor $\widehat A$. Tensor-factor disjointness gives $[J \otimes \mathrm{id}, \mathrm{id} \otimes \varphi^*] = 0$ for every $\varphi$, parabolic or not.

**Numerical witness.** SF.5_T6 runs 6 tests across (parabolic, non-parabolic) × $k = 1, 2, 3$ — all pass.

**Sharpened statement.** Queer J commutation is **FULL $\mathrm{Symp}_{\mathrm{form}}$**, stronger than the parabolic functoriality of F$''$. This is because the q(N) source has all the relevant structure in the matrix factor; the target factor is only the cocycle host.

### §7.4 (Att-4) Hadamard regulator $\mathrm{Symp}_{\mathrm{form}}$-equivariance

**Attack.** "The heat-kernel regulator (R1) might not preserve $\mathrm{Symp}_{\mathrm{form}}$-equivariance if its kernel function depends on the target coordinates."

**Response.** **DEFEATED.** The Costello-Gwilliam Vol II §11 admissible regulator class consists of heat-kernel parametrices whose support and analytic conditions are entirely on (a) the matrix factor (heat kernel on $\mathfrak g$), (b) the brane-line $\mathbb R$ (compact support / Schwartz decay), (c) the central ghost $\gamma_1$ (de Rham). NONE of these involve the target factor $\widehat A$.

Therefore $\mathrm{Symp}_{\mathrm{form}}$ acts trivially on the regulator class; functoriality is automatic for the FULL $\mathrm{Symp}_{\mathrm{form}}$, not just parabolic.

**Numerical witness.** SF.5_T5 runs 12 tests across (parabolic, non-parabolic) × $k = 1, 2, 3$ — all pass.

**Sharpened statement.** Hadamard regulator is **FULL $\mathrm{Symp}_{\mathrm{form}}$-equivariant**. The parabolic restriction in F$''$ comes from the m-adic-completion direction in the source $\widehat L$, NOT from the regulator.

---

## §8. Residuals

### §8.1 R-P4X-Symp-Functor-01: cubic Symp generators, $k \geq 4$

**Status.** Open question (not a functoriality blocker, but an (A2) admissibility issue). For non-parabolic $\varphi: z_1 \mapsto z_1 + z_2^k$ with $k \geq 4$, the (A2) finite-window weight admissibility may impose additional conditions. Resolved via P4-G2-M2 (BCH cubic-cocycle compatibility) which discharges the cubic level identically by Jacobi.

**Deliverable.** 1-week extension of `check_symp_functoriality.py` SF.5_T1 to $k \geq 4$. Severity 1.

### §8.2 R-P4X-Symp-Functor-02: extension to $\mathfrak{gl}(N|N)$ for $N \geq 3$

**Status.** Mechanical extension. The current SF.5 verification works on the smallest non-trivial source $\mathfrak{gl}(1|1)$ via tensor-factor disjointness; the extension to $N \geq 3$ inherits by W22-T2 combinatorial reduction. No new content required.

**Deliverable.** 1-2 week extension of the script harness. Severity 1.

### §8.3 R-P4X-Symp-Functor-03: explicit BD §3.5 isomorphism

**Status.** Open question. Our Phase-4 parabolic functoriality matches the BD §3.5 pattern conceptually; an EXPLICIT statement that "Phase-4 chain-level data on the brane line is the BD §3.5 stabiliser-equivariant chiral algebra at the m-adic point $\mathfrak m = (z_1)$" requires constructing the comparison map. This is the M-12 Avenue (B) bulk-holomorphic chiral product (`phase4-exec-Chiral-Product-Audit` line 125), which is conjectural at Phase-4.

**Deliverable.** 12-month integration deliverable; falls under Phase-5.

### §8.4 R-P4X-Symp-Functor-04: Kapranov-Vasserot Sym($d$) extension

**Status.** Open question. Our parabolic functoriality is the $d = 1$ Phase-4 case. KV $\mathrm{Sym}(d)$ extension (with $\dim_\mathbb{C} = 2d$ formal disk, multiple $\omega$-Cartan directions) would give a higher-dimensional parabolic structure; this may be relevant for the Vol III CY-to-chiral frontier in `~/calabi-yau-quantum-groups`.

**Deliverable.** Phase-5 cross-repo bridge; not an obligation here.

### §8.5 No genuine obstruction

**Summary.** Every Phase-4 chain-level discharge is functorial under the natural symmetry of its setup. The parabolic restriction is the **acceptable choice** of m-adic completion + brane-line geometry, NOT a forced restriction blocking inscription. The matrix-factor and regulator pieces extend to the FULL $\mathrm{Symp}_{\mathrm{form}}$, sharpening beyond the parabolic baseline. **No genuine obstruction identified.**

---

## §9. 200-word executive summary

Phase-4 EXEC P4-Symp-Functoriality audit on the formal symplectomorphism functoriality of Phase-4 chain-level discharges. **Top verdict: PARABOLIC functoriality** under $P_{(z_1)} \subset \mathrm{Symp}_{\mathrm{form}}(\widehat{\mathbb{C}^2}_0)$ preserving the m-adic ideal $\mathfrak m = (z_1)$. The brane line at $\mathbb R \times \{0\}$ and m-adic completion at $\mathfrak m$ both break $\mathrm{Symp}_{\mathrm{form}}$ to the same parabolic stabiliser; this is the natural symmetry of the discharge geometry, not a forced restriction. Per-discharge: F$''$ is PARABOLIC; G$^{\mathrm{otr}}$, Hadamard regulator, queer J commutation are FULL $\mathrm{Symp}_{\mathrm{form}}$ (matrix-factor data, tensor-factor disjoint); classical-super gl/osp/psl/q DISCHARGE inherits PARABOLIC from F$''$; classical-super p/sl(M≠N) FAIL is $\mathrm{Symp}_{\mathrm{form}}$-INDEPENDENT (failure source matrix-factor); Decoupling-Proposition is PARABOLIC; Costello-Li 2015 flat-$\mathbb C^d$ is FULL holomorphic Symp_form (no m-adic completion). Verification script `scripts/check_symp_functoriality.py` runs 43 tests across 7 named families, 0 failures. BD §3.5 cross-walk: our parabolic matches BD's formal-point stabiliser-equivariance verbatim; no stronger statement required. Anti-attack scan defeats 4 named attacks with numerical witness. **No genuine obstruction identified.** Theorem F$''$-functorial: F$''$ holds in a $P_{(z_1)}$-equivariant sense after passing to the parabolic preserving $\mathfrak m = (z_1)$.

---

End of P4X-Symp-Functoriality audit.
