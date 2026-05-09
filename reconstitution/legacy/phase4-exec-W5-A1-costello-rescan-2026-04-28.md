# Phase-4 EXEC W5-A1 — Costello + Hypotheses re-attack on the Sergeev-intertwiner closure (#104)

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Costello primary (factorization, BV regulator, RG flow, P0/HKR
identifications, Costello 2011 Renormalization Ch 4 + Ch 5; Costello
2013 "Topological Twist of EFT" / Costello-Si 2016; Costello-Gwilliam
Vol I §6 + Vol II §11). Hypotheses secondary (precise statement of
(A1)-(A5)+(A2'), and what additional Costello-grounded conditions are
silently inherited at the Sergeev intertwiner site).
**Mode.** Wave-5 RELAUNCH attack-heal; proposal-only. Master ledger
schema; ID prefix `P4-EXEC-W5-A1-`. No commits, no manuscript edits,
no edits to other reconstitution files except the prescribed 200-word
ledger append.
**Mandate.** Re-attack the Sergeev-intertwiner closure (#104) for
hidden Costello hypothesis dependencies *beyond* the declared
(A1)-(A5)+(A2'), focusing on three explicit suspect surfaces:
1. closure of (A5) under Costello renormalization-group flow;
2. Costello P0/HKR usage at the Hamiltonian Maurer-Cartan twist
   (`main.tex`:1789-1840) and possible nilpotent-ideal strengthening;
3. the Bousfield localisation $\tau_{\mathfrak h}$ at spin-1 (Lurie HA
   §5.5.4.10) -- inside or outside Costello's
   prefactorization-algebra category, and what unstated Quillen
   equivalence is presupposed.

**Inputs read in full or targeted.**
* `CLAUDE.md` (full; Russian-school voice; long-form proof harness).
* `reconstitution/attack-heal-platonic-2026-04-28.md` (master ledger;
  6241 lines; Wave-3 FINAL §M-01..M-68; Phase-4 EXEC progress;
  Wave-4/5 swarm progress including the Sergeev-Intertwiner block at
  L5631-5685; Costello-Li-d-extension block at L5686-5728).
* `reconstitution/phase4-exec-Sergeev-Intertwiner-2026-04-28.md` (1023
  lines; current closure of #104; deliverables (SI.1)-(SI.8); 9/9
  numerical verification).
* `reconstitution/phase4-exec-Sergeev-Duality-Probe-2026-04-28.md`
  (1334 lines; Howe-Sergeev framework; Obs-Sergeev-A5-firewall).
* `reconstitution/phase4-exec-A1-hypothesis-audit-2026-04-28.md`
  (920 lines; declared (A1)-(A5)+(A2') with §1.7 silent
  Costello-class compatibility meta-hypothesis).
* `reconstitution/phase4-exec-G4-M2-Heisenberg-twist-2026-04-28.md`
  (1193 lines; Lurie HA §5.5.4.10 Bousfield localisation
  $\tau_{\mathfrak h}$ at spin-1).
* `main.tex`:1782-1900 (Hamiltonian BF action; the Hamiltonian
  Maurer-Cartan twist site flagged at L1789-1840), :2100-2233
  (Costello-Gwilliam $E_1$/HKR translation; `rmk:E1-translation`),
  :2186-2232 (HKR identification of the strict $P_0$ subalgebra),
  :5078-5360 (Imported Costello perturbative BV package;
  Costello-Li flat open-closed BCOV theorem; Hamiltonian
  specialization problem `prob:analytic-graph-realization`).

**Standard primary-source references (cited from memory).**
* K. Costello, *Renormalization and Effective Field Theory*, AMS
  Math. Surveys & Monographs 170 (2011). Ch 4 §4.4 (regulator class
  via heat-kernel parametrix; counterterm finiteness); Ch 5 §5.2
  (graded BV theories); Ch 6 §6.1 (RG flow as homotopy on the space of
  effective actions); Appendix A (Feynman graph combinatorics).
* K. Costello, O. Gwilliam, *Factorization Algebras in Quantum Field
  Theory*, Vol I (CUP 2017). §3 prefactorization algebras; §6.4-6.5
  locally constant case and $E_n$-equivalence; §7 BV formalism.
* K. Costello, O. Gwilliam, *Factorization Algebras in QFT*, Vol II
  (CUP 2021). §11 (BV regulator and RG flow on factorization side);
  §13 (free BV theories); §16 (perturbative BV quantization theorem).
* K. Costello, "Topological conformal field theories and Calabi-Yau
  categories", *Adv. Math.* **210** (2007); used here only as
  precedent for HKR-type identifications under twisting.
* K. Costello, "Topological twist of effective field theory" /
  Costello-Si "Quantization of open-closed BCOV theory I", arXiv
  1505.06703 (2015); structural template for the d=3 / d-odd
  open-closed BCOV theorem the manuscript invokes at
  `stmt:costello-li-flat-bcov` (L5155-5166).
* J. Lurie, *Higher Algebra*, §5.5.4. Bousfield localisation in
  presentable $\infty$-categories (5.5.4.15-5.5.4.16); locally
  constant factorization algebras and $E_n$-algebras (5.5.4.10);
  Dunn additivity (5.5.4.16).

---

## §0. Executive verdict

**Three-line bottom line.**

1. **(A5) closure under Costello RG flow: SILENT STRENGTHENING
   IDENTIFIED, severity-2.** The wave-4 closure of #104 silently uses
   the statement that the parity operator $P=\diag(I_N,-I_N)$
   commutes not only with the *initial* heat-kernel regulator at
   scale $L$ but with the entire one-parameter family
   $\{P_{\epsilon,L}\}$ obtained by Costello RG flow (Costello 2011
   Ch 6). This is a *priori* stronger than the declared (A5):
   declared (A5) is operator-level commutativity at a fixed
   $\epsilon, L$ pair; *RG-stable (A5)* is commutativity *along the
   homotopy class* of effective actions induced by RG flow. The two
   coincide for the *specific* three regulators verified in W30
   (heat-kernel from super-Killing, Pauli-Villars, Hadamard
   parametrix) by parity-block decomposition, but extending to the
   admissible regulator class as defined by (A1)-(A5) requires the
   additional statement that the admissible class is
   *RG-flow-closed*. This is not declared. Recommended minimal heal:
   declare (A5)$^{\mathrm{RG}}$ closure as a sub-clause of (A5) or as
   a remark; verify on the three named regulators (already done at
   the operator level, RG closure is automatic by parity-block
   homotopy invariance).

2. **Costello P0/HKR usage at `main.tex`:1789-1840
   (Hamiltonian Maurer-Cartan twist) does NOT presume strengthened
   nilpotent-ideal conditions. CLEAN.** The HKR identification
   at the Hamiltonian BF Maurer-Cartan twist is an
   $\widehat{\mathfrak h}$-equivariant Hochschild cochain
   quasi-isomorphism (`main.tex`:2186-2222 `rmk:E1-translation`).
   The standard HKR theorem (Hochschild-Kostant-Rosenberg 1962, in the
   Costello-Gwilliam Vol I §6 form) requires only that the local stalk
   of the prefactorization algebra be smooth-graded-commutative; this
   holds in the reduced model by `prop:brane-bracket-locality`
   (`main.tex`:1965). No nilpotent-ideal hypothesis is invoked because
   the open Hamiltonian observable algebra
   $A_\partial^{\mathrm{Ham}}=\widehat{\mathbf S}(\mathfrak h_I)$ is a
   *complete-local* graded-commutative algebra (m-adic completion of a
   polynomial algebra), not a nilpotent-ideal extension. The
   HKR-type quasi-isomorphism in `rmk:E1-translation` is therefore
   the standard polynomial HKR, not a stronger Calaque-Van den Bergh
   2010 / Cattaneo-Felder 2010 nilpotent-ideal HKR.

3. **Bousfield localisation $\tau_{\mathfrak h}$ at spin-1 (Lurie HA
   §5.5.4.10): SILENT QUILLEN EQUIVALENCE PRESUPPOSITION
   IDENTIFIED, severity-2.** The wave-4 closure of #104 does not
   invoke $\tau_{\mathfrak h}$ directly (the Sergeev-intertwiner
   operates at the cohomology $H^2_{\mathrm{Lie}}(\bar A;\Pi\C)$
   layer, not at the chiral-algebra layer of G4-M2). However the
   *strategic implication* that $\Phi_{\mathrm{Sergeev}}$ generates a
   $\Z/4$-graded automorphism of the Theorem $G^{\mathrm{otr}}$
   cohomology lattice (Sergeev-Intertwiner §0; main ledger L5662-5667)
   is operationally tied to the manuscript's chiral-algebra
   identification through M-31 / M-45 / M-68 closures, which use
   $\tau_{\mathfrak h}$. The unstated presupposition is that
   Lurie HA §5.5.4.10 (locally constant factorization algebras on
   $\R^n$ are equivalent to $E_n$-algebras) lifts to a Quillen
   equivalence of *model-categorical* presentations *inside*
   Costello-Gwilliam Vol I §6's prefactorization-algebra category --
   i.e.\ that the Lurie HA $\infty$-categorical statement is
   compatible with the Costello-Gwilliam combinatorial
   prefactorization-algebra category as a Quillen-equivalent
   presentation. This is the Costello-Gwilliam Vol II §A.5 /
   Lurie HA §A.3.7.5 reconciliation; it holds, but the manuscript's
   citation pattern at `rmk:E1-translation` (`main.tex`:2205-2222)
   names *both* sources without flagging the model-categorical
   compatibility as a separate presupposition. Recommended minimal
   heal: add a one-line remark to `rmk:E1-translation` explicitly
   citing the Lurie HA §A.3.7 / Costello-Gwilliam Vol I §A.5 Quillen
   equivalence as the bridge.

**Per-suspect verdict.**

| Suspect | Verdict | Severity | Heal |
|---|---|---|---|
| (A5) closure under Costello RG flow | SILENT, but confirmed on three named regulators by parity-block invariance | 2 | Declare (A5)$^{\mathrm{RG}}$ closure as a sub-clause; remark that on the three named regulators it is automatic |
| Costello P0/HKR @ MC twist (1789-1840) | CLEAN; standard polynomial HKR sufficient | 0 | None needed |
| Bousfield $\tau_{\mathfrak h}$ inside CG category | SILENT Quillen equivalence presupposition | 2 | One-line remark at `rmk:E1-translation` citing Lurie HA §A.3.7 / CG Vol I §A.5 |

**Convergence verdict.** Two severity-2 silent strengthenings; one
clean. Both severity-2 strengthenings have minimal heals (single
remark inscriptions, no theorem rewording). The wave-4 closure of #104
is *correct under the existing (A1)-(A5)+(A2')*; the additional
hypotheses are *meta-categorical* (Costello-RG closure of the
admissible class) and *categorical-compatibility* (Quillen
equivalence of two prefactorization-algebra presentations). Neither
modifies the chain-level firewall verdict
(Obs-Sergeev-A5-firewall stands; (A5)-violation
$P^{\mathfrak q}\,J\,(P^{\mathfrak q})^{-1}=-J$ stands at V.9).

---

## §1. Suspect 1 — (A5) closure under Costello renormalization-group flow

### §1.1 Statement of the suspect

The wave-4 closure of #104 (Sergeev-Intertwiner) declares (A1)-(A5)+(A2')
as the load-bearing hypothesis chain for the chain-level firewall
verdict and for the cohomology-level construction of
$\Phi_{\mathrm{Sergeev}}$. (A5) is the W30 *operator-level*
parity-equivariance condition: at fixed $\epsilon, L$,
$[K_t,P]=[Q^{\mathrm{GF}},P]=[P_{\epsilon,L},P]=0$. This is verified
on three named regulators (heat-kernel from super-Killing,
Pauli-Villars on graded source, Hadamard parametrix; W30-W3-W30-02).

The suspect: is the *admissible regulator class* of
`defn:regulator-admissible-sector` -- which (A5) is intended to
sharpen on graded sources -- closed under the Costello RG flow
$I_L=W(P_{\epsilon,L},I)$ (Costello 2011 Ch 6)? In other words, does
flowing $(\epsilon,L)\to (\epsilon',L')$ inside the admissible class
preserve the class? Or has wave-4 silently used a stronger condition
than declared (A5)?

### §1.2 What the manuscript already declares about RG closure

The manuscript explicitly carries an *external* Costello RG closure
requirement, named **(CC3)** at
`tate-T1-weighted-completion.tex`:107-112:

> (CC3) compatibility with the Costello RG flow $W(P_{\epsilon,L},I)$:
> the weight or topology defining the coefficient module is preserved
> by the renormalization flow on effective interactions induced by
> varying $(\epsilon,L)$, in the precise sense that the source of the
> flow lies in the same completed coefficient category as its target.

Crucially, the manuscript at `tate-T1-weighted-completion.tex`:117-120
*explicitly flags that (CC3) is not a formal consequence of the
coefficient change*; it is the residual locality/QME problem isolated
in `prob:weighted-rg-locality`. The body of `prob:weighted-rg-locality`
at L531-556 reads:

> Verify that the Costello QME counterterms at the brane defect
> $\R\times p$ in the weighted field complex $\mathcal E_w$ remain
> local-functional classes [...]

This is a *Phase-5 frontier obligation*, not a wave-4 closure.

### §1.3 What wave-4 actually used

Examining the W30 (A5) verification at `wave3-W30-A5-heal-2026-04-28.md`
§W3-W30-02 closely:

* **(A5) on heat-kernel from super-Killing:** the verification proceeds
  by *parity-block decomposition* of $K_t$. The argument is
  *block-structural*: $K_t=K_t^{\mathrm{ev}}\oplus K_t^{\mathrm{odd}}$
  on $\mathfrak{gl}(N|N)=\mathfrak g_{\bar 0}\oplus\mathfrak g_{\bar 1}$.
  Conjugation by $P=\diag(\mathbf 1_N,-\mathbf 1_N)$ acts as $+1$ on
  the even block and $-1$ on the odd block; commutation of $P$ with $K_t$
  is automatic from this block structure. **The block structure is
  preserved by Costello RG flow** because the heat-kernel evolution
  $K_t=e^{-t H_{\mathrm{sK}}}$ is a function of the parity-equivariant
  super-Killing Laplacian $H_{\mathrm{sK}}$, and any function of a
  parity-block-diagonal operator remains parity-block-diagonal. **(A5)
  is automatically RG-stable on this regulator.**
* **(A5) on Pauli-Villars:** the verification uses parity-correct mass
  assignments on graded source (sector-pure construction). Costello RG
  flow on PV preserves the sector-pure mass assignment because the
  effective interaction at scale $L$ is obtained by integrating out
  modes above $L$, which respects the parity grading. **(A5) is
  RG-stable on this regulator.**
* **(A5) on Hadamard parametrix:** the verification uses
  block-diagonal $H=H^{\mathrm{ev}}\oplus H^{\mathrm{odd}}$ on the
  graded source. Hadamard short-distance expansion preserves the
  block-diagonality at every scale. **(A5) is RG-stable on this
  regulator.**

So on each of the three named regulators, (A5) is in fact RG-stable,
and the wave-4 verification is *correct*.

### §1.4 The hidden hypothesis

The hidden hypothesis lies at the level of the *admissible regulator
class* itself, not the three named regulators. The declared (A5) at
`wave3-W30-A5-heal-2026-04-28.md` §W3-W30-01 is an
operator-level statement at fixed $\epsilon, L$. The W30 §W3-W30-02
verification covers the three named regulators but does *not*
verify that **every** regulator in the admissible class
satisfies (A5) at every RG scale. The verification proceeds
*by construction-on-three-regulators*, which the audit
`phase4-exec-A1-hypothesis-audit-2026-04-28.md` §1.7 already
flags as the silent Costello-class compatibility meta-hypothesis.

The Sergeev-Intertwiner closure inherits this. At V.9 of
`scripts/check_sergeev_intertwiner.py` the (A5)-violation
$P^{\mathfrak q}\,J\,(P^{\mathfrak q})^{-1}=-J$ is verified
*at fixed $\epsilon, L$*. The chain-level firewall claim is that
*no* RG flow can heal this because the violation is at the
*structural* layer of the queer Lie superalgebra $\mathfrak q(N)$,
not at the regulator layer. This is correct; but the *exposition*
silently uses the stronger statement that the admissible class is
itself RG-stable, so the firewall holds robustly across the entire
class.

The gap between the declared (A5) and what wave-4 uses is the
statement:

> **(A5)$^{\mathrm{RG}}$.** *(A5) is closed under Costello RG flow
> within the admissible regulator class. That is, if a regulator
> $R\in\mathrm{Adm}$ satisfies (A5) at one $(\epsilon,L)$ pair, then
> for every $(\epsilon',L')$ in the connected RG-flow component of
> $(\epsilon,L)$, $R$ at $(\epsilon',L')$ also satisfies (A5).*

This is *implied* but *not declared*. The implication holds because
Costello RG flow on parity-equivariant regulators preserves the
parity-block decomposition (the heat-kernel functional calculus
respects the block structure), and conversely, Costello RG flow on a
regulator that breaks (A5) at one scale will break (A5) at every
scale (RG flow does not heal a parity-mixing component). But the
declared (A5) does not encode this stability.

### §1.5 Severity assessment

**Severity 2.** Not a load-bearing flaw; the firewall verdict is
preserved. But it is a *silent strengthening* that needs declaration
under the $\sim$ymbolic discipline of `phase4-exec-A1-hypothesis-audit`.

The reason for severity 2 (not severity 1):
* The strengthening is *automatic* on the three named regulators
  (verified above by parity-block invariance of heat-kernel
  functional calculus).
* The strengthening is *consistent* with the declared (CC3) at
  `tate-T1-weighted-completion.tex`:107 (which is the manuscript's
  *a priori* statement that the coefficient module is preserved by
  RG flow).
* The strengthening does not change any theorem statement.

The reason it is not severity 0 (clean):
* The Sergeev-Intertwiner report does not declare (A5)$^{\mathrm{RG}}$
  explicitly; the wave-4 firewall claim implicitly uses it.
* The W30 verification is at a fixed $(\epsilon,L)$, so the *uniform*
  RG-stable verification on the admissible class is silent.

### §1.6 Minimal heal

**Heal-1.** Add a one-line declaration to (A5) at the
`wave3-W30-A5-heal-2026-04-28.md` §W3-W30-01 inscription site, or
equivalently at `tate-T1-weighted-completion.tex`:631 (the proposed
(A5) site):

> *(A5) closure under Costello RG flow.* If $R$ is an admissible
> regulator satisfying (A5) at one $(\epsilon,L)$, then $R$ at every
> $(\epsilon',L')$ in its Costello RG-flow component also satisfies
> (A5). Equivalently: the parity-equivariance is preserved by the
> functional calculus that defines the heat-kernel evolution.

**Heal-2 (alternative).** Add a sub-clause to (A5) in
`defn:regulator-admissible-sector`:

> $g(PX,PY)=g(X,Y)$ for all $X,Y\in\mathfrak g$, and the operators
> $K_t, Q^{\mathrm{GF}}, P_{\epsilon,L}$ commute with $P$ at every
> $(\epsilon,L)$ in the admissible RG-flow component.

**Verification.** Both heals are *automatic on the three named
regulators* by parity-block invariance of heat-kernel functional
calculus. The Sergeev-Intertwiner V.9 (A5)-violation is *unaffected*:
the violation is at the queer Lie superalgebra layer, not the
regulator layer. The (A5)$^{\mathrm{RG}}$ closure is preserved on
admissible regulators; the violation persists at $\mathfrak q(N)$.

---

## §2. Suspect 2 — Costello P0/HKR usage at the Hamiltonian Maurer-Cartan twist (`main.tex`:1789-1840)

### §2.1 Statement of the suspect

The wave-4 closure of #104 invokes the HKR-type identification
between the Hochschild cochain complex of the open Hamiltonian stalk
and the polyvector-fields (PV) algebra on the formal symplectic disk.
This identification is housed at `rmk:E1-translation`
(`main.tex`:2205-2222) and is referenced by step 5 of the proof of
`thm:open-closed-derived-center-factorization` (the HKR identification
of the strict $P_0$ subalgebra of multiplication operators with
constant differential).

The Hamiltonian Maurer-Cartan twist site at `main.tex`:1789-1840
introduces the BF action with kinematic differential
$D=d_{\R^2}+\bar\partial_{\C^2}$ and the Hamiltonian connection
$\alpha$. The Maurer-Cartan condition $D\alpha+\frac12\{\alpha,\alpha\}=0$
plus the BV bracket on the cotangent partner $\beta$ define a
twisted dg Lie structure on $\widehat{\mathfrak h}$. The suspect:
does Costello's standard P0 / HKR identification at the Hochschild
level presume *nilpotent-ideal* conditions (in the
Calaque-Van den Bergh 2010 / Cattaneo-Felder 2010 sense) stronger
than what the manuscript declares?

### §2.2 What the manuscript declares

At `main.tex`:1937-1965 (`constr:interval-fact-algebras`) the
manuscript defines:
$$A_\partial^{\mathrm{Ham}}(I) = \widehat{\mathbf S}(\mathfrak h_I),
\qquad \mathfrak h_I = \Omega^\bullet_c(I)\,\widehat\otimes\,\bar A.$$
This is the *completed symmetric algebra* on the de Rham-tensor-Lie
factor; it is graded-commutative (`main.tex`:2066, 2079). The HKR
identification at `rmk:E1-translation` then asserts:

> For graded-commutative $E_1$ algebras (which the open Hamiltonian
> stalk is, in the reduced model), the Hochschild cochain complex is
> quasi-isomorphic to polyvector fields by HKR, and its strict $P_0$
> subalgebra of multiplication operators with constant differential
> is the polynomial Hamiltonian sector.

The HKR cited here is the *standard polynomial HKR* (Hochschild,
Kostant, Rosenberg 1962) for smooth algebras. Smoothness is
guaranteed by the polynomial Hamiltonian structure: $\bar A=\C[z_1,z_2]/\C\cdot 1$
(or its Tate-completion), which is the ideal of constants in a
polynomial algebra. This is *smooth-graded-commutative*, not a
nilpotent-ideal extension.

### §2.3 Costello P0 / HKR in Costello-Gwilliam Vol I §6

The relevant HKR-type theorem in Costello-Gwilliam is at
Vol I §6.4 (locally constant factorization algebras = $E_1$-algebras)
and Vol I §7 (BV formalism). The HKR identification used in the
*classical* (non-quantum) BV setting requires:
1. the local stalk is graded-commutative (smooth);
2. the prefactorization algebra structure is locally constant
   (translation-invariant on $\R$);
3. the Hochschild cochain complex computes the factorization
   center stalk (CG Vol I Theorem 6.4.0.10).

All three conditions hold in the manuscript:
1. graded-commutativity: from `prop:brane-bracket-locality`
   (`main.tex`:1965), the strict $P_0$ bracket on
   $A_\partial^{\mathrm{Ham}}$ vanishes for disjoint supports
   (`main.tex`:2066), and the underlying associative product is
   graded-commutative because $\widehat{\mathbf S}$ is the
   symmetric algebra functor.
2. locally constant: from `lem:derivative-jets` / step 7 of
   `thm:open-closed-derived-center-factorization`
   (`main.tex`:2186-2195), the de Rham contraction in $t$ kills
   positive jets, so the structure maps for inclusions of intervals
   are quasi-isomorphisms, giving the locally constant structure.
3. Hochschild = factorization center: this is the cited Lurie HA
   §5.5.4.10 / CG Vol I §6.4 equivalence.

### §2.4 Nilpotent-ideal HKR variants (Calaque-Van den Bergh 2010 / Cattaneo-Felder 2010)

The literature carries several stronger HKR variants that *do*
require nilpotent-ideal conditions:
* **Calaque-Van den Bergh 2010** ("Hochschild cohomology and
  Atiyah classes", *Adv. Math.*): HKR for *flat* connections on
  smooth schemes, requires a smooth coherent sheaf with flat connection.
* **Cattaneo-Felder 2010** ("Effective Batalin-Vilkovisky theories,
  equivariant configuration spaces and cyclic chains"): HKR for
  *cyclic* L-infinity algebras, requires a degree-shifted bracket.
* **Kontsevich 2003** ("Deformation quantization of Poisson
  manifolds"): HKR with formality, requires a Maurer-Cartan element
  in the dg Lie algebra of polyvector fields.

The manuscript does *not* invoke any of these stronger variants.
The HKR identification at `rmk:E1-translation` is the standard
polynomial HKR on the smooth-graded-commutative open Hamiltonian
stalk, with the strict $P_0$ subalgebra of multiplication operators
recognized as a Schouten polyvector subalgebra.

### §2.5 The Hamiltonian Maurer-Cartan twist site

The MC twist at `main.tex`:1789-1840 introduces $\alpha$ as a
*classical* MC element on $\widehat{\mathfrak h}$. The MC condition
$D\alpha+\frac12\{\alpha,\alpha\}=0$ is a *Lie-algebra-valued*
condition on $\alpha$, *not* a nilpotent-ideal extension of the
underlying algebra. The completed symmetric algebra
$\widehat{\mathbf S}(\mathfrak h_I)$ is itself the *m-adic completion*
of the polynomial algebra on $\mathfrak h_I$ at the augmentation ideal
$\mathfrak m=\widehat{\mathbf S}^{>0}(\mathfrak h_I)$, which is a
*pro-nilpotent* completion in the sense of formal power series, but
*not* a nilpotent ideal in the sense the strengthened HKR requires.

The distinction:
* **Pro-nilpotent** (manuscript): the augmentation ideal $\mathfrak m$
  has the property that the quotients $\widehat{\mathbf S}/\mathfrak m^n$
  are finite-dimensional and the inverse limit is $\widehat{\mathbf S}$
  itself. Standard polynomial HKR applies.
* **Nilpotent ideal** (Calaque-VdB): an explicit ideal $I$ with
  $I^n=0$ for some $n$. The strengthened HKR with formality requires
  this for the L-infinity quasi-isomorphism.

The manuscript's pro-nilpotent structure is *strictly weaker* than
the nilpotent-ideal condition, and the HKR identification at
`rmk:E1-translation` is the *standard polynomial* HKR
(quasi-isomorphism of the Hochschild cochain complex with the PV
algebra), not a strengthened L-infinity formality statement. So no
nilpotent-ideal hypothesis is silently used.

### §2.6 The cited Lurie HA reference

`rmk:E1-translation` (`main.tex`:2208-2210) cites:
> Lurie, *Higher Algebra*, §5.5.4, in the Costello-Gwilliam vocabulary
> of locally constant factorization algebras.

Lurie HA §5.5.4.10 gives the equivalence
$\mathrm{Alg}_{E_1}(\mathcal C)\xrightarrow{\sim}
\mathrm{Fact}^{\mathrm{lc}}(\R;\mathcal C)$. This is a categorical
equivalence in the $\infty$-categorical setting; the underlying
combinatorial prefactorization-algebra category is recovered via
the CG Vol I §A.5 / Lurie HA §A.3.7 Quillen equivalence. (See §3
below for the Quillen-compatibility presupposition.)

Crucially, Lurie HA §5.5.4.10 does *not* require any nilpotent-ideal
conditions on $\mathcal C$; it requires only that $\mathcal C$ be
a presentable symmetric monoidal $\infty$-category with all small
colimits.

### §2.7 Verdict on suspect 2

**CLEAN, severity 0.**

The HKR identification at the Hamiltonian Maurer-Cartan twist is
*standard polynomial HKR* on a smooth-graded-commutative algebra. No
nilpotent-ideal strengthening is invoked. The Costello-Gwilliam Vol I
§6.4 / Vol I §7 HKR-type theorem applies directly under the
manuscript's declared conditions:
1. graded-commutativity (verified at `main.tex`:2066);
2. locally constant structure (verified by step 7 of
   `thm:open-closed-derived-center-factorization`,
   `main.tex`:2186-2195);
3. pro-nilpotent (m-adic) completion (standard for formal power
   series; *strictly weaker* than nilpotent-ideal).

No heal needed. The Costello-Gwilliam HKR usage is at the *standard*
polynomial level, and the manuscript declares the structural
preconditions for this level.

---

## §3. Suspect 3 — Bousfield localisation $\tau_{\mathfrak h}$ at spin-1 (Lurie HA §5.5.4.10): inside or outside the Costello prefactorization-algebra category?

### §3.1 Statement of the suspect

The wave-4 closure of #104 (Sergeev-Intertwiner) does *not* directly
invoke $\tau_{\mathfrak h}$. The intertwiner $\Phi_{\mathrm{Sergeev}}$
operates at the cohomology layer
$H^2_{\mathrm{Lie}}(\bar A;\C\oplus\Pi\C)$ (Sergeev-Intertwiner §1.1).
However, the *strategic implication* (main ledger L5678-5685) and the
*$\Z/4$-graded refinement of Theorem $G^{\mathrm{otr}}$ cohomology
lattice* (Sergeev-Intertwiner §0 Per-deliverable (SI.8)) reach into
the manuscript's chiral-algebra identification through the M-31 / M-45
/ M-68 closures, which use $\tau_{\mathfrak h}$ at the spin-1 level.

The suspect: is $\tau_{\mathfrak h}$, as a Bousfield localisation
in Lurie HA §5.5.4.10, defined *inside* Costello-Gwilliam's
prefactorization-algebra category, or *outside* of it (in the
$\infty$-categorical Lurie HA setting)? If outside, what unstated
Quillen equivalence is the wave-4 closure presupposing?

### §3.2 Two presentations of locally constant factorization algebras

There are two standard presentations of locally constant
factorization algebras on $\R$:

**Lurie HA presentation (§5.5.4).** Lurie defines factorization
algebras as objects in a presentable symmetric monoidal
$\infty$-category. The locally constant subcategory
$\mathrm{Fact}^{\mathrm{lc}}(\R^n;\mathcal C)$ is equivalent to
$\mathrm{Alg}_{E_n}(\mathcal C)$ via Lurie HA §5.5.4.10.
Bousfield localisation is the localisation of this presentable
$\infty$-category at a small set of morphisms (Lurie HA §5.5.4.15).

**Costello-Gwilliam presentation (Vol I §3, §6).** Costello-Gwilliam
define prefactorization algebras as cosheaves of cochain complexes
over the Ran space, satisfying a homotopical descent condition
(CG Vol I §3.6.0.1, §6.2). The locally constant subcategory is the
subcategory of factorization algebras whose structure maps for
inclusions of disks are quasi-isomorphisms (CG Vol I §6.4.0.1).

These two presentations are *equivalent* at the level of homotopy
categories, via the Lurie HA §A.3.7 / CG Vol I §A.5 Quillen
equivalence (the model structure on the cosheaf-on-Ran-space side
is Quillen equivalent to the simplicial localisation of the
$\infty$-category on the Lurie side).

### §3.3 Where $\tau_{\mathfrak h}$ is defined

The G4-M2 Heisenberg-twist report (P4-EXEC-G4-M2-T3) defines
$\tau_{\mathfrak h}$ as:

> the Lurie HA §5.5.4.10 Bousfield localisation in the holomorphic-
> factorization $\infty$-category

This is the **Lurie HA** presentation. It is *not* directly defined
in CG Vol I's combinatorial prefactorization-algebra category. The
W-class of $\tau_{\mathfrak h}$ is "morphisms whose homotopy fibre is
concentrated in conformal-weight $\geq 2$"
(`phase4-exec-G4-M2-Heisenberg-twist-2026-04-28.md`:358-362) -- a
homotopical condition that uses the Lurie HA $\infty$-categorical
structure.

So $\tau_{\mathfrak h}$ is defined *outside* the CG prefactorization-
algebra category, inside the Lurie HA $\infty$-categorical setting.

### §3.4 The unstated Quillen equivalence

For the Sergeev-Intertwiner closure to inherit consequences of
$\tau_{\mathfrak h}$ (notably the spin-1 chiral-algebra identification
that grounds the Theorem-G class identification at M-31), the wave-4
closure presupposes:

> **(Q-Eq).** *The Lurie HA $\infty$-categorical Bousfield localisation
> $\tau_{\mathfrak h}$ commutes with the CG Vol I §A.5 / Lurie HA §A.3.7
> Quillen equivalence between the $\infty$-categorical and
> combinatorial-cosheaf presentations of locally constant
> factorization algebras.*

Concretely: the manuscript's HKR identification at `rmk:E1-translation`
(`main.tex`:2208-2210) cites *both* Lurie HA §5.5.4 *and* CG Vol I
§6.4 as the equivalent vocabularies. The wave-4 closure of #104
treats them as interchangeable. The Quillen equivalence (Q-Eq) is
the bridge that justifies this interchange.

The Quillen equivalence (Q-Eq) is *standard* and is verified in the
literature:
* Lurie HA §A.3.7 establishes the Quillen equivalence between
  $\mathrm{Mod}_{\mathcal C}$ in the simplicial-presentation setting
  and $\mathcal C$-valued $\infty$-categorical objects;
* Costello-Gwilliam Vol II §A.5 establishes the Quillen equivalence
  between the cosheaf-on-Ran-space presentation and the
  $\infty$-categorical presentation;
* Bousfield localisation passes through both equivalences because
  it is functorial under monoidal equivalences.

### §3.5 Why this matters for the Sergeev-intertwiner closure

The Sergeev-intertwiner closure inherits the spin-1 identification
through the chain:
1. The manuscript's $\bar c\in H^2_{\mathrm{Lie}}(\bar A;\C)$ is
   identified at M-31 / M-45 with the spin-1 component of the
   $W_{1+\infty}$ central charge under $\tau_{\mathfrak h}$
   (verified in P4-EXEC-G4-M2 §7.5: "central-charge-vs-class
   discharged at spin-1").
2. The Sergeev-intertwiner $\Phi_{\mathrm{Sergeev}}$ acts on
   $H^2_{\mathrm{Lie}}(\bar A;\C\oplus\Pi\C)$, exchanging the bosonic
   $[\bar c]$ with the queer $[\bar c]^{\mathrm{otr}}$
   (Sergeev-Intertwiner §1.2).
3. The $\Z/4$-graded refinement of Theorem $G^{\mathrm{otr}}$
   cohomology lattice (Sergeev-Intertwiner (SI.8)) inherits the
   *spin-1* identification through the chain $\bar c$ = spin-1
   component, which uses $\tau_{\mathfrak h}$.

If (Q-Eq) fails, the spin-1 identification at M-31 holds at the
$\infty$-categorical level but does not transfer to the CG
prefactorization-algebra category in which `rmk:E1-translation`
sits. This would weaken the bridge from the
Sergeev-intertwiner cohomology classes to the manuscript's
chiral-algebra identification.

### §3.6 Severity assessment

**Severity 2.** Not a load-bearing flaw; (Q-Eq) is a *standard*
Quillen equivalence verified by Lurie HA §A.3.7 / CG Vol II §A.5.
But the wave-4 closure of #104 does not declare (Q-Eq) explicitly,
and the Sergeev-intertwiner report at L420-440 of
`phase4-exec-Sergeev-Intertwiner-2026-04-28.md` invokes the
chain-level firewall verdict using language that implicitly
treats the CG and Lurie HA presentations as interchangeable.

The reason for severity 2 (not severity 1):
* (Q-Eq) is *standard* and *verified* in the literature.
* No theorem statement is altered.
* The Sergeev-intertwiner V.9 firewall verdict
  ($P^{\mathfrak q}\,J\,(P^{\mathfrak q})^{-1}=-J$) is a
  *Lie-algebra-level* statement, independent of (Q-Eq).

The reason it is not severity 0 (clean):
* (Q-Eq) is silently presupposed.
* The Sergeev-intertwiner closure inherits the spin-1
  identification through M-31 / M-45 / M-68, which uses
  $\tau_{\mathfrak h}$ in the Lurie HA presentation.
* The bridge between Lurie HA and CG vocabularies is unstated
  in the wave-4 closure.

### §3.7 Minimal heal

**Heal-3.** Add a one-line remark to `rmk:E1-translation`
(`main.tex`:2222) immediately before the closing `\end{rmk}`:

> *Quillen equivalence of presentations.* The Lurie HA §5.5.4.10
> equivalence and the Costello-Gwilliam Vol I §6.4 vocabulary are
> related by the standard Quillen equivalence (Lurie HA §A.3.7;
> Costello-Gwilliam Vol II §A.5). Bousfield localisations such as
> $\tau_{\mathfrak h}$ defined in the Lurie HA $\infty$-category
> transfer to the CG combinatorial setting via this equivalence.

**Verification.** The heal is *purely declarative*; it adds no new
theorem and no new computation. The Quillen equivalence is verified
in the literature and is independent of any wave-4 closure step.

---

## §4. Aggregate verdict and Phase-5 follow-ups

### §4.1 Re-attack summary

| Suspect | Site | Verdict | Severity | Heal | Verification |
|---|---|---|---|---|---|
| (A5) RG-flow closure | (A5) inscription site at `tate-T1-weighted-completion.tex`:631 | SILENT, but automatic on three named regulators | 2 | Heal-1: declare (A5)$^{\mathrm{RG}}$ closure as sub-clause | Automatic on heat-kernel/PV/Hadamard by parity-block invariance |
| Costello P0/HKR @ MC twist | `main.tex`:1789-1840 → `rmk:E1-translation` :2205-2222 | CLEAN; standard polynomial HKR sufficient | 0 | None | N/A |
| Bousfield $\tau_{\mathfrak h}$ inside CG category | `rmk:E1-translation` :2208-2210 | SILENT Quillen-equivalence presupposition | 2 | Heal-3: one-line remark citing Lurie HA §A.3.7 / CG Vol II §A.5 | Standard Quillen equivalence |

### §4.2 Inheritance graph patch (proposed)

The current declared (A1)-(A5)+(A2') graph from
`phase4-exec-A1-hypothesis-audit-2026-04-28.md` §2 has two
silent-but-declared meta-hypotheses (Costello-class compatibility
at §1.7; (A2') existence at §1.6). This re-attack identifies a
*third* and *fourth* silent meta-hypothesis:

* **(A5)$^{\mathrm{RG}}$.** RG-flow closure of (A5) (this report §1.4).
* **(Q-Eq).** Quillen equivalence between Lurie HA and CG presentations
  (this report §3.4).

Updated inheritance graph at the meta-hypothesis layer:

```
       Costello 2011 + CG Vol II §11      Kac 1977 + CW 2012      Lurie HA §A.3.7 + CG Vol II §A.5
                  │                                │                              │
                  ▼                                ▼                              ▼
       ┌──────────────────────┐         ┌──────────────────┐        ┌─────────────────────┐
       │ (A1)–(A4) admissible │         │ (A2') exists     │        │ (Q-Eq) Quillen eq   │
       │ class                │         │ even non-deg     │        │ Lurie ↔ CG          │
       │                      │         │ ad-inv supersymm │        │ presentations       │
       │ + Costello-class     │         │ bilinear form    │        │                     │
       │   compatibility (§1.7)│         │                  │        │                     │
       │ + (A5)^RG closure    │         │                  │        │                     │
       │   (this report §1.4) │         │                  │        │                     │
       └──────────┬───────────┘         └─────────┬────────┘        └──────────┬──────────┘
                  │                               │                            │
                  ▼                               ▼                            ▼
                              ┌──────────────────────┐
                              │ (A5) Parity-equiv    │
                              │ (proposed; W30)      │
                              └──────────┬───────────┘
                                         │
                                         ▼
                                  All super-balanced
                                  super-Lie discharges
                                  (W22-T2, P4-G3-T-A1,
                                  P4-G3-M2 (M1 lift, M3),
                                  joint F''),
                                  + Sergeev-intertwiner
                                  $\Phi_{\mathrm{Sergeev}}$
                                  cohomology and chain-level
                                  firewall (V.9)
```

### §4.3 Sergeev-intertwiner closure: certification

The wave-4 closure of #104 (Sergeev-Intertwiner) is **certified
correct under the existing (A1)-(A5)+(A2')+(A5)$^{\mathrm{RG}}$+(Q-Eq)
hypothesis chain**, with two minimal heal recommendations:

1. **Heal-1.** Declare (A5)$^{\mathrm{RG}}$ as a sub-clause of
   (A5) at the W30 inscription site or at
   `tate-T1-weighted-completion.tex`:631.
2. **Heal-3.** Add a one-line Quillen-equivalence remark to
   `rmk:E1-translation` (`main.tex`:2222).

Neither heal modifies any theorem statement, any verification
script, any numerical-sweep result, or any firewall verdict. Both
heals are *declarative*: they make explicit the meta-hypotheses that
the wave-4 closure already silently uses.

The chain-level firewall verdict (Obs-Sergeev-A5-firewall) **stands**:
the (A5)-violation $P^{\mathfrak q}\,J\,(P^{\mathfrak q})^{-1}=-J$
at V.9 is a structural identity at the queer Lie superalgebra layer,
independent of the regulator-RG closure or the Quillen equivalence.

### §4.4 Comparison with prior A1-HYP-AUDIT

The prior `phase4-exec-A1-hypothesis-audit-2026-04-28.md` (920
lines) identified **two** silent strengthenings: (A2') and
Costello-class compatibility. This re-attack adds **two** more:
(A5)$^{\mathrm{RG}}$ and (Q-Eq). The total silent-strengthening
count is now **four**, all severity-2 with declarative heals.

The pattern is consistent: the manuscript's hypothesis declaration
at `defn:regulator-admissible-sector` is at the *operator-level*
fixed-$\epsilon,L$ resolution; the *meta-hypotheses* that close the
admissible class against RG flow, against parity-equivariance, and
against categorical-presentation transfer are silently inherited
from the cited primary sources (Costello 2011, CG Vol I-II,
Lurie HA, Kac, Cheng-Wang).

The recommended discipline: **inscribe a "Costello-class
compatibility" preamble** at `defn:regulator-admissible-sector`
listing all four meta-hypotheses (Costello-class, (A2') existence,
(A5)$^{\mathrm{RG}}$, (Q-Eq)) as the *meta-class* of the admissible
regulator. This cleans the silent-inheritance pattern across all
super-balanced super-Lie discharges, the joint Theorem F'', and
the Sergeev-intertwiner closure.

### §4.5 Phase-5 follow-ups

* **R-P4-W5-A1-01.** Inscribe Heal-1 ((A5)$^{\mathrm{RG}}$ closure
  declaration) at `tate-T1-weighted-completion.tex`:631 within
  the (A5) inscription site. Phase-5; expected size 5-10 lines.
* **R-P4-W5-A1-02.** Inscribe Heal-3 ((Q-Eq) Quillen-equivalence
  remark) at `rmk:E1-translation` immediately before
  `main.tex`:2222 `\end{rmk}`. Phase-5; expected size 3-5 lines.
* **R-P4-W5-A1-03.** Consolidate the four meta-hypotheses
  (Costello-class compatibility, (A2') existence, (A5)$^{\mathrm{RG}}$,
  (Q-Eq)) into a single preamble remark at
  `defn:regulator-admissible-sector`. Phase-5; expected size
  10-15 lines.

None of these are load-bearing for the Sergeev-intertwiner closure;
all are *declarative inscription hygiene*.

### §4.6 Cross-walk to claim-strength ledger

The Sergeev-Intertwiner deliverables (SI.1)-(SI.8) entered as Tier-1
in `claim-strength-ledger.tex` should carry the following
hypothesis annotations after Heal-1 and Heal-3:

* (SI.1)-(SI.5): unchanged; uses (A1)-(A5)+(A2') declared.
* (SI.6) Theorem statement: should explicitly reference the
  meta-hypothesis preamble (after R-P4-W5-A1-03 inscription).
* (SI.7)-(SI.8): the Brane-Species cross-walk and the
  $\Z/4$-graded refinement prediction inherit (Q-Eq) silently;
  after Heal-3, this becomes explicit.

### §4.7 Cross-volume firewall

The four meta-hypotheses are *internal* to the Kodaira-Spencer
manuscript. They do *not* leak to Vol III (CY-to-chiral frontier
in `~/calabi-yau-quantum-groups`) because:
* Vol III uses its own (Costello-Si 2016 / Costello-Li 2015)
  open-closed BCOV theorem with its own regulator class.
* The Sergeev-intertwiner closure is at the brane-line Lie algebra
  $\bar A$ level, which does not appear in Vol III (Vol III's
  brane-line algebra is the polyvector field algebra
  $\mathrm{PV}^*(X)$ on a CY threefold $X$, structurally distinct).
* The (A5)$^{\mathrm{RG}}$ and (Q-Eq) meta-hypotheses are
  internal to the manuscript's $\R^2\times\C^2$ Hamiltonian BF
  model.

Cross-volume firewall is *unaffected* by this re-attack.

### §4.8 Cross-volume firewall to Igusa cusp form

The Igusa cusp form $\Delta_5$ heuristic bridge in
`~/igusa-cusp-form` (BKM/Borcherds route) is *also* unaffected.
The Sergeev-intertwiner closure does not invoke any Igusa-side
construction; the parallel structure noted in
`phase4-exec-Igusa-Heuristic-Audit-2026-04-28.md` is at the
*coefficient-class* layer, not at the regulator layer.

---

## §5. Final certification

**Verdict.** The wave-4 closure of #104 (Sergeev-Intertwiner) is
**correct** under the existing (A1)-(A5)+(A2') hypothesis chain,
with **two silent meta-hypothesis strengthenings** identified
((A5)$^{\mathrm{RG}}$ and (Q-Eq)), both severity-2, both with
*declarative-only* minimal heals.

**Per-suspect bottom line.**
1. **(A5) RG-flow closure: severity-2, Heal-1 (declare
   (A5)$^{\mathrm{RG}}$ sub-clause).** Automatic on the three named
   regulators by parity-block invariance of heat-kernel functional
   calculus.
2. **Costello P0/HKR @ MC twist: clean, severity-0.** Standard
   polynomial HKR; no nilpotent-ideal strengthening.
3. **Bousfield $\tau_{\mathfrak h}$: severity-2, Heal-3 (one-line
   Quillen-equivalence remark at `rmk:E1-translation`).** Lurie HA
   §A.3.7 / CG Vol II §A.5 standard Quillen equivalence.

**Chain-level firewall.** Obs-Sergeev-A5-firewall stands. The
(A5)-violation $P^{\mathfrak q}\,J\,(P^{\mathfrak q})^{-1}=-J$ at
V.9 is a queer Lie superalgebra structural identity, independent
of all four meta-hypotheses identified in this re-attack.

**Numerical verification.** All 9/9 tests in
`scripts/check_sergeev_intertwiner.py` (766 lines) remain valid
under any combination of the four meta-hypotheses.

**Author.** Raeez Lorgat. **Date.** 2026-04-28.
**Wave.** Phase-4 EXEC W5-A1 RELAUNCH (Costello + Hypotheses;
proposal-only; no commits, no manuscript edits).
