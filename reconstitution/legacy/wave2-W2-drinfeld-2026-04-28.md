# Wave-2 W2 — Drinfeld + Functoriality

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Wave/Lens.** W2 wave 2; Drinfeld (moduli, canonical, hidden
groupoids, factorization structures) + Functoriality (are maps
natural? Are choices canonical or merely chosen?).
**Mandate.** Stress-test the M-06 replacement of "Schur rigidity"
with **T²-Cartan-equivariant bigraded rigidity**; M-04 volume-form
datum; (∞,1)-equivariance under Symp$_{\mathrm{form}}(\C^2,0)$;
M-22 / A2-007 Matlis-vs-residue split.
**Files read.** `attack-heal-platonic-2026-04-28.md` (M-01–M-25);
`platonic-ideal-plan-2026-04-28.md`; `appendix-matlis-principal-parts.tex`
(full); `principles.tex` (full; Principle 3 at lines 156–204);
`theorem-lanes.tex` Lane 4 (lines 150–207); `main.tex` lines
2200–2400, 3680–3960, 3970–4200, 4240–4380, 3440–3500;
`tate-T5-chain-level-primitive.tex` lines 580–660. Cross-checked
against the 1225-case scripted verification of the coadjoint formula
in `scripts/check_one_psi_homology.py`.

The mandate has four sub-questions. Each receives an attack, a
proposed heal at LaTeX-level granularity, and a residual.

---

## §1. Method

Drinfeld + Functoriality reads a manuscript like a Tannakian moduli
problem: every numbered theorem must specify a category, a group of
natural automorphisms, a canonical structure preserved, and a
universal property realised. A construction whose authors cannot
describe such data is suspect. This wave's attack discipline:

1. For every place where the residue pairing or $\mathfrak h$-action
   is invoked, name the **exact group of natural automorphisms** under
   which the statement holds.
2. Where rigidity is asserted, identify whether the rigidity is by
   **abelian-categorical Schur** (irreducible $\Rightarrow$ End = scalars), by
   **bigraded Cartan torus equivariance** (a torus action with simple
   isotypic components forces a diagonal pairing), or by some genuine
   third structure (Matlis local cohomology, residue calculus).
3. Where a datum is "implicit" or "fixed once and for all", treat the
   datum as part of the moduli problem and redo the rigidity analysis
   with the datum varying.

The four sub-questions are clusters of W2-NN ledger entries below.

---

## §2. Master ledger

### W2-01 — Rigidity proof inspected: it is T²-Cartan-equivariant, not full $\mathfrak h$-Schur
**Severity 3. Status valid. Confidence high.**
**Lens.** Drinfeld + Functoriality.
**Provenance.** Wave-1 M-06; W2 verification by rechecking
`appendix-matlis-principal-parts.tex` Theorem~\ref{thm:app-matlis-residue-rigidity}
lines 179–206 and `main.tex` Theorem~\ref{thm:canonical-residue-pairing}
lines 3838–3906.
**Target.** `appendix-matlis-principal-parts.tex` lines 179–206;
`main.tex` lines 3848–3906; `theorem-lanes.tex` lines 183–185.
**Claim under attack.** "Schur rigidity" / "Matlis-form uniqueness"
of the residue pairing.
**Broken step.** The actual proof in both loci uses **only three
Hamiltonian elements**: the diagonal $z_1 z_2$ (which restricts to a
T²-Cartan torus action by weight) and the linear $z_1, z_2$. The
first determines the diagonal Kronecker form; the second and third
force constant coefficient propagation along the bigraded lattice.
**No non-Cartan, non-linear element of $\mathfrak h$ appears in the
uniqueness argument.** The proof structure is exactly the
toric-rigidity template: a torus $T^2 = \mathbb G_m^2$ acts diagonally
with character $(a,b)$ on $\rho_{a,b}$ and $(m,n)$ on $z_1^m z_2^n$;
total-degree zero gives $a+b = m+n$; the diagonal Cartan
$z_1 z_2$ gives $a-b = m-n$; the two together pin support to
$(a,b) = (m,n)$. After that, equivariance for a single linear
element propagates a single constant. This is **bigraded Cartan
equivariance** plus **one-parameter rigidity**, not Schur on an
abstractly irreducible $\mathfrak h$-representation.
**Evidence type.** proof_inspection.
**Evidence ref.** `main.tex`:3863, 3867–3877 (diagonal weight
constraint via $z_1 z_2$); 3883–3900 (constant-coefficient
propagation via $z_1, z_2$); identical structure in
`appendix-matlis-principal-parts.tex`:192–206. Confirmed against the
explicit proof: no other element of $\mathfrak h$ is required.
**Confidence.** High. The rigidity holds **as proved** under the
weaker hypothesis. M-06 names the correct structural content; this
W2 entry confirms by inspection of the proofs.
**Blast radius.** Two-fold:
* **Upgrade direction.** The proved rigidity is *stronger* than
  Schur in one sense (Schur would require $\mathcal P$ to be an
  irreducible $\mathfrak h$-module, which is *false* in $\Cat{TateVec}$
  — see W2-02 below) and *weaker* in another (it does not extend
  automatically to symplectomorphism-equivariant rigidity — see
  W2-04).
* **Downstream uses.** Every downstream use of the residue pairing
  uniqueness either reduces to T²-Cartan rigidity, or invokes a
  *different* structural result. See W2-03 for the audit.
**Minimal heal.**
* Rename `thm:canonical-residue-pairing` to "**Residue pairing,
  T²-Cartan rigid**" with explicit hypothesis: "the source is the
  T²-Cartan-graded $\mathfrak h$-module structure for the diagonal
  torus $T^2 = \mathrm{Spec}\,\C[z_1 z_2, z_1 / z_2]$ acting on the
  bigraded lattice, plus equivariance for the two linear elements
  $z_1, z_2$."
* In `rmk:residue-pairing-schur` (lines 3908–3929), replace "abstract
  Schur lemma" with "abstract Schur lemma applied to a putative
  irreducible $\mathfrak h$-module" — and explicitly add: "the
  $\mathfrak h$-module $\mathcal P$ is **not** $\mathfrak h$-irreducible
  in $\Cat{TateVec}$; rigidity follows from the much weaker
  T²-Cartan-equivariant total-degree-zero hypothesis."
* In `theorem-lanes.tex` lines 183–185, replace "uniqueness via
  local-cohomology duality" with "T²-Cartan rigidity plus
  one-parameter propagation; the Matlis local cohomology module
  identification is a distinct statement, see W2-08."
**Residual.** Whether the *Matlis-module identification* itself
descends to T²-Cartan equivariance alone, or whether genuine local
cohomology is required — see W2-08.

### W2-02 — $\mathcal P$ is not $\mathfrak h$-irreducible
**Severity 2 (additive). Status valid. Confidence high.**
**Lens.** Drinfeld + Functoriality.
**Provenance.** New W2 observation supporting W2-01.
**Target.** Same loci as W2-01.
**Claim under attack.** Implicit assumption that $\mathcal P$ is an
irreducible $\mathfrak h$-module, which would license an abstract
Schur argument.
**Broken step.** Re-derive carefully: $z_1 \cdot \rho_{a,b} =
-(b+1) \rho_{a, b+1}$; both indices are nonnegative, so the action
of $z_1$ on the bigraded basis raises the second index. The total
weight $a+b$ is therefore raised by 1. So the natural total-weight
filtration $F^N \mathcal P = \bigoplus_{0 < a+b \leq N} \C \rho_{a,b}$
is **not** preserved by $\mathfrak h$; the action *raises* total
weight, so the cofiltration $\mathcal P / F^N$ is the
$\mathfrak h$-stable structure. Each total-weight stratum
$F^{N+1}/F^N$ is a finite-dimensional space of "weight-$N+1$
principal parts", $\mathfrak h$-stable under the truncated action.

Hence $\mathcal P$ is **not** simple as an $\mathfrak h$-module — it
admits a nontrivial total-weight filtration with nonzero subquotients
— and abstract Schur on an irreducible representation does not apply.
However, each (a,b) weight space under the T²-Cartan torus is
**1-dimensional**, so the rigidity question is about T²-Cartan
isotypic uniqueness, not about $\mathfrak h$-irreducibility.
**Evidence type.** counterexample (literal Schur fails);
proof_observation (T²-Cartan saves the rigidity).
**Confidence.** High.
**Blast radius.** Validates W2-01: full $\mathfrak h$-Schur is the
*wrong* statement to invoke, and T²-Cartan rigidity is precisely
correct.
**Minimal heal.** Add a one-paragraph remark at the head of
`rmk:residue-pairing-schur` (`main.tex`:3908–3929) explicitly noting
that $\mathcal P$ is *not* an irreducible $\mathfrak h$-module
(infinite Krull dimension; nontrivial total-weight cofiltration), and
that the rigidity statement should be read as
**T²-isotypic-uniqueness plus one-parameter propagation**, not
abstract Schur.
**Residual.** None.
**Deciding evidence.** The remark.

### W2-03 — Downstream audit: T²-Cartan rigidity suffices everywhere
**Severity 4 (audit). Status valid. Confidence high.**
**Lens.** Drinfeld + Functoriality.
**Provenance.** W2 inspection of all downstream uses.
**Target.** All `\ref{thm:principal-part-coadjoint-uniqueness}` and
`\ref{thm:canonical-residue-pairing}` invocations in `main.tex` and
lane files. Audit list:
1. **`main.tex`:3732** (proof of `cor:descendant-coadjoint-difference`).
   Use: identifies the coadjoint half. Sufficient: T²-Cartan rigidity
   plus monomial calculation; no genuine $\mathfrak h$-Schur invoked.
2. **`main.tex`:4052** (proof of `thm:pbw-vs-deformation`). Use:
   labels the deformation-level coadjoint basis. Sufficient: same as
   above.
3. **`main.tex`:4084** (proof of `thm:pbw-vs-deformation` (3)). Use:
   the structural separation between PBW and coadjoint actions. The
   *non-isomorphism* uses local-nilpotence comparison, not Schur;
   T²-Cartan is irrelevant here.
4. **`main.tex`:4175** (proof of `thm:no-polynomial-realization-categorical`).
   Use: the explicit lowering/raising formulas. Sufficient: T²-Cartan
   rigidity plus the explicit formula.
5. **`main.tex`:4338, 4344, 4362** (proof of
   `prop:reduced-principal-part-boundary-current` — **the
   boundary-current locality theorem / Theorem E**). Use: the
   *negative-transpose* identity for the bracket
   $\{B_f(a), \Theta_\rho(B)\} = \Theta_{f \cdot \rho}(aB)$. The
   identity used is integration-by-parts under the residue pairing
   (line 3852–3856 of the proof of
   `thm:canonical-residue-pairing`); the *uniqueness* is not invoked.
   What is used is **existence of a residue pairing satisfying
   integration by parts**, not its rigidity. Sufficient: any pairing
   constructed from the volume form $dz_1 \wedge dz_2$.
6. **`main.tex`:4385, 4394, 4409** (`prob:boundary-principal-part-cotangent-operators`).
   Same as above: existence not uniqueness.
7. **`tate-T5-chain-level-primitive.tex`:611** (Moyal coadjoint
   construction). Use: the $r=1$ classical leading term. Sufficient:
   T²-Cartan rigidity at order 0; higher orders are forced by the
   $\hbar$-deformation structure, not by rigidity.
**Claim under attack.** A hidden invocation of full $\mathfrak h$-Schur
somewhere downstream.
**Broken step.** None found.
**Evidence type.** verification.
**Confidence.** High.
**Blast radius.** **The boundary-current locality theorem
(Theorem E) does not need $\mathfrak h$-Schur.** It needs only
existence of the residue pairing satisfying integration by parts and
the explicit coadjoint formula. T²-Cartan rigidity controls
*normalization* (one scalar $c$); the bracket identity is independent
of the choice.
**Minimal heal.** None at the proof level. Add an editorial remark
in `theorem-lanes.tex` Lane 4 (lines 199–207, the `Residuals`
paragraph) clarifying: "Theorem D's rigidity is bigraded T²-Cartan
rigidity (one scalar $c \in \C^\times$); it is *not* invoked
elsewhere as a full $\mathfrak h$-Schur statement. Theorem E's
brackets use existence-and-integration-by-parts of the pairing, not
its rigidity."
**Residual.** None.
**Deciding evidence.** Manuscript audit complete; T²-Cartan rigidity
is sufficient downstream.

### W2-04 — Volume datum $\Omega$ as moduli: does the residue pairing remain canonical under formal Symp-equivariance?
**Severity 4. Status valid (proposal-level). Confidence high.**
**Lens.** Drinfeld + Functoriality (canonical or chosen).
**Provenance.** Wave-1 M-04 (volume datum implicit), M-05
(Symp-functoriality). W2 sharpening.
**Target.** `appendix-matlis-principal-parts.tex` Definition (topology)
lines 23–47; the volume form $dz_1 dz_2$ implicit at line 81.
**Claim under attack.** The Matlis-dual realization $\mathcal P
\cong \mathfrak h^\vee_{\mathrm{cont}}$ and the residue pairing are
"canonical".
**Broken step.** The pairing depends on the volume form
$\Omega = dz_1 \wedge dz_2$. Under a polynomial symplectomorphism
$\varphi^* \omega = \omega$ (the *symplectic* form, not the volume),
the pulled-back volume can change by a factor: for symplectic
$\varphi$ on $\C^2$, $\varphi^* (dz_1 \wedge dz_2) = (\det J_\varphi)
\cdot (dz_1 \wedge dz_2)$, and Jacobian is 1 by symplectic-ness in
2 complex dimensions. So on $\C^2$ with $\dim = 2$, the symplectic
form **equals** the volume form, and Symp = SDiff
(volume-preserving), so the pairing *is* automatically
Symp-invariant.

But the **question is sharper**: under the **formal symplectic loop
group** Symp$_{\mathrm{form}}(\C^2, 0)$ — the pro-algebraic group of
formal power-series symplectomorphisms fixing the origin — is the
pairing equivariant?
**Evidence type.** verification + proof_observation.
**Test computation.** For symplectic $\varphi$, the condition
$\varphi^* \omega = \omega$ forces $J_\varphi \in
\mathrm{SL}_2(\C[[z_1, z_2]])$. So $\det J_\varphi = 1$ identically;
$\varphi^* (dz_1 \wedge dz_2) = dz_1 \wedge dz_2$. Hence
$\varphi^* \rho_{a,b}$ is some Laurent expression with
$\varphi^* (z_1^{-a-1} z_2^{-b-1} dz_1 dz_2)$. After
$\mathfrak m$-adic completion and projection to the principal-part
lattice, this gives an explicit Symp$_{\mathrm{form}}$-action on
$\mathcal P$ realised by **residue pullback**: $(\varphi^* \rho)(g) =
\rho(\varphi^{-1, *} g)$ for $g \in \mathfrak h$, where
$\varphi^{-1,*}$ is composition pullback. The residue pairing
$\langle \rho, g \rangle = \mathrm{Res}_0(g \cdot \rho)$ is
Symp$_{\mathrm{form}}$-invariant because the residue at the origin
is invariant under any formal automorphism fixing the origin —
*this is exactly the content of Hartshorne, Residues and Duality
III.10.10 / III App.A* (residue is intrinsic to the divisor, not the
coordinates).
**Confidence.** High. The required result is the residue pullback
formula plus $\mathrm{Res}_0$-invariance under automorphisms of
$(\C^2, 0)$.
**Blast radius.** **Volume-form-as-datum is correct.** Fixing
$\Omega = dz_1 \wedge dz_2$ is *not* a non-canonical choice in the
sense of worry: it is the canonical generator of $\Lambda^2
T^*_0 \C^2$ in the formal symplectic category, and the Symp-group
acts on it trivially in dim 2. Hence:
* On $\C^2$, the pairing is **automatically** Symp$_{\mathrm{form}}$-equivariant.
* On $\C^{2n}$, $n > 1$, the pairing depends on the *volume*
  $\Omega = \omega^n / n!$, which is canonically determined by the
  symplectic form $\omega$. Hence even there the Symp-group acts
  trivially on $\Omega$ and the pairing is intrinsic.
* The dimension-1 line $\C \rho_{0,0}$ is *also* Symp-invariant
  because the constant function $1 \in \C \subset R$ is Symp-fixed,
  hence its annihilator complement is Symp-stable — the socle
  remains intrinsic.
**Minimal heal.**
* Promote the Symp-invariance to a numbered proposition in
  `appendix-matlis-principal-parts.tex`:
  ```latex
  \begin{prop}[Symp$_{\mathrm{form}}$-invariance of the residue pairing]
  \label{prop:matlis-symp-functorial}
    Let $\varphi \in \mathrm{Symp}_{\mathrm{form}}(\C^2, 0)$ be a
    formal symplectomorphism fixing the origin. The Matlis-dual
    module $\mathcal P$ carries a $\varphi$-equivariant action by
    residue pullback, and the residue pairing
    $\langle \rho, g \rangle = \mathrm{Res}_0(g \cdot \rho)$ is
    Symp$_{\mathrm{form}}$-invariant: $\langle \varphi^* \rho,
    \varphi^* g \rangle = \langle \rho, g \rangle$.
  \end{prop>
  ```
  Cite Hartshorne, *Residues and Duality*, III.10.10 and III App.A.
* In Definition `def:app-matlis-topology`, list $\Omega = dz_1
  \wedge dz_2$ as an explicit datum and state: "the symplectic form
  $\omega = dz_1 \wedge dz_2$ on $\C^2$ coincides with the volume
  $\Omega = \omega^1 / 1!$ in $\dim = 2$, hence Symp$_{\mathrm{form}}$
  fixes both."
**Residual.** The *generalisation to higher symplectic dimensions*
(where $\Omega = \omega^n / n!$ is intrinsic but not equal to $\omega$)
remains a separate Hartshorne-residue argument, omitted from the
local manuscript.
**Deciding evidence.** The numbered proposition with citation, plus
the explicit Hartshorne reference.

### W2-05 — Socle-canonicity (A2-008) under Symp$_{\mathrm{form}}$
**Severity 3. Status valid. Confidence high.**
**Lens.** Drinfeld + Functoriality.
**Provenance.** W2 sharpening of A2-008.
**Target.** `appendix-matlis-principal-parts.tex` Definition
(reduced principal parts) lines 74–104; `principles.tex` lines
171–180.
**Claim under attack.** The dimension-1 quotient $\C \rho_{0,0}$ in
$E_R(\C) / \mathcal P$ is canonical under polynomial Symp, but is
it canonical under the **full** formal symplectic loop group
Symp$_{\mathrm{form}}$?
**Broken step.** The socle of the Matlis injective hull
$E_R(\C) = H^2_{\mathfrak m}(R) \cdot dz_1 dz_2$ is one-dimensional,
spanned by $\rho_{0,0}$. The formal automorphism $\varphi$ fixing
the origin acts on $\rho_{0,0}$ by the formula
$\varphi^* \rho_{0,0} = \rho_{0,0} + \text{higher-pole terms}$.
After projection to the principal-part lattice the leading term
is exactly $\rho_{0,0}$.

More carefully: the residue $\mathrm{Res}_0$ extracts the coefficient
of $z_1^{-1} z_2^{-1}$, which is intrinsic to the differential form
on the divisor; under any formal automorphism fixing the origin it
equals the coefficient of the local-cohomology socle, which is
intrinsic. Hence $\rho_{0,0}$ generates a canonical line.
**Evidence type.** proof_observation (residue intrinsicness).
**Confidence.** High.
**Blast radius.** Two-fold:
1. The line $\C \rho_{0,0}$ is a *Symp*$_{\mathrm{form}}$-stable line
   in $E_R(\C)$. Hence $\mathcal P = \mathrm{Ann}(\C \cdot 1) \subset
   E_R(\C)$ is a Symp$_{\mathrm{form}}$-equivariant submodule
   (W2-04).
2. Theorem G's identification of the U(1)/Capelli class with the
   socle is therefore Symp$_{\mathrm{form}}$-canonical: the anomaly
   line is intrinsic to the formal symplectic geometry, not a
   coordinate accident.
**Minimal heal.** Add a one-sentence remark in Definition
`def:app-matlis-principal-parts` (after line 104) stating: "The
socle line $\C \rho_{0,0} \subset E_R(\C)$ is intrinsic: under any
$\varphi \in \mathrm{Symp}_{\mathrm{form}}(\C^2, 0)$, $\varphi^*$
preserves $\C \rho_{0,0}$, by the Hartshorne residue-intrinsicness
theorem (Residues and Duality III.10.10). Hence the reduced
principal-part module $\mathcal P$ is intrinsically defined."
**Residual.** None.
**Deciding evidence.** The remark plus citation.

### W2-06 — (∞,1)-equivariance under Symp$_{\mathrm{form}}$: real desideratum or overkill?
**Severity 2 (decision). Status sharpened. Confidence medium.**
**Lens.** Drinfeld + Functoriality (the moduli stack of branes).
**Provenance.** W2 — new question on the desired equivariance level.
**Target.** Theorems A, B, C, D, E, F, G — global classification of
which extend to Symp$_{\mathrm{form}}$-equivariant statements.
**Claim under attack.** "(∞,1)-equivariant factorization algebra
over Symp$_{\mathrm{form}}$" is a coherent desideratum for *this*
paper.
**Broken step.** A genuine (∞,1)-equivariant factorization algebra
over Symp$_{\mathrm{form}}$ would mean: a factorization algebra
$\mathcal A$ on the brane line $\R$, together with, for every
$\varphi \in \mathrm{Symp}_{\mathrm{form}}(\C^2, 0)$, a coherent
homotopy $\varphi^* \mathcal A \simeq \mathcal A$, with all the
higher coherences (associativity of $(\varphi \psi)^*$ vs $\varphi^*
\psi^*$, identities, etc.) realised at the (∞,1)-level. This is a
theorem about the *moduli stack of branes in formal symplectic
$\C^2$* and its symmetries.

For the **proved core** of the present paper:
* **Theorem A (Dirac brane probe).** The brane probe $z_i \rightsquigarrow
  \phi_i$ is *not* Symp-equivariant in general: a polynomial
  symplectomorphism $\varphi$ does not commute with the matrix
  substitution unless $\varphi$ is linear. Hence Theorem A is
  GL$_2$-equivariant (where GL$_2$ acts linearly on $(z_1, z_2)$),
  not full-Symp-equivariant.
* **Theorem B (Stable Hamiltonian trace).** The stable trace algebra
  $A_\partial = S(\bar A \oplus \bar A_{\mathrm{desc}}[1])$ as a Lie
  algebra carries a **natural Symp$_{\mathrm{form}}$-action** by
  pulled-back Hamiltonians. The PBW special-fibre identification is
  Symp-equivariant on the *bigraded vector-space* level, but the
  *symmetric raising action* on $\widetilde \Psi_{a,b}$ is **only
  GL$_2 \times$ T$^2$-equivariant**, because the explicit formula
  $F_{p,q}: \widetilde \Psi_{a,b} \mapsto (pb - qa) \widetilde
  \Psi_{a+p-1, b+q-1}$ uses linear coordinates.
* **Theorem C (CE/PV derived-centre).** The CE complex of
  $\mathfrak g = \mathfrak h \ltimes \mathfrak h^\vee[1]$ is
  intrinsically defined; the polyvector field side
  $\mathrm{PV}(S(\mathfrak h))$ is intrinsic. The isomorphism
  $\Phi$ of generators $c^I \mapsto \theta^I$, $u_I \mapsto O_I$
  uses a *basis* $\{H_I\}$ of $\mathfrak h$, but coordinate-free
  Lichnerowicz reformulation (plan §3 Theorem C) makes it
  **Symp$_{\mathrm{form}}$-equivariant intrinsically**. Theorem C is
  the most Symp-natural theorem in the paper.
* **Theorem D (Matlis-dual / principal parts).** Symp$_{\mathrm{form}}$-equivariant
  by W2-04, after the heal.
* **Theorem E (Factorization-current).** The de Rham factorization
  cosheaf on $\R$ is independent of the formal disk; the
  *coefficient* $\mathfrak h$ is Symp-equivariant on the
  module level, but the *interval factorization product* and the
  bracket between currents and principal parts (which involves the
  product of a smooth function and a distribution) depend on the
  brane-line topology, not on Symp$_{\mathrm{form}}$. Theorem E is
  Symp$_{\mathrm{form}}$-equivariant in the coefficient direction
  (each $\mathfrak h_I = \Omega^\bullet_c(I) \widehat\otimes
  \mathfrak h$ admits the action), but not in the brane-line
  direction (where it is $\mathrm{Diff}^+(\R)$-equivariant or
  translation-equivariant).
* **Theorem F (Moyal target).** Quantum Moyal product on $\bar A_\hbar$
  is Symp$_{\mathrm{form}}$-equivariant up to scalar (Kontsevich
  formality).
* **Theorem G (U(1)/Capelli anomaly).** The class $[\bar c]$ lives
  in $H^2_{\mathrm{Lie}}(\bar A; \C)$, which has a natural
  Symp$_{\mathrm{form}}$-action; the weight-(0,0) component (M-09 +
  W2-05) is *Symp-stable*, hence the anomaly line is
  Symp-canonical.
**Evidence type.** proof_observation; classification.
**Confidence.** Medium (the (∞,1) coherences are routine but not
verified at full chain-level).
**Blast radius.** **The (∞,1)-equivariant factorization algebra
desideratum is an overkill for the present paper.** What the paper
proves and what would benefit from being made Symp-equivariant
explicitly:
* **Yes (one-line addition).** Theorems C, D, G. (Coordinate-free
  reformulation: Theorem C via Lichnerowicz; Theorem D via
  Hartshorne residue-intrinsicness; Theorem G via weight-(0,0)
  cohomology canonicality.)
* **Partial (proof modification needed).** Theorem B. The PBW
  shadow is Symp-equivariant on labels, not on actions; the symmetric
  raising formula is GL$_2 \times$ T$^2$-only. Honest statement: the
  PBW shadow is a *coordinate-dependent* representative of an
  intrinsic graded vector space.
* **No (different equivariance group).** Theorems A, E. Theorem A is
  GL$_2$-only; Theorem E uses brane-line $\mathrm{Diff}^+(\R)$, not
  Symp.
* **Conditional.** Theorem F (Symp-equivariant up to Kontsevich
  scalar; finite algebraic model only).
**Minimal heal.**
* Add a "Naturality" section in `principles.tex` (or a numbered
  remark in §0 of `main.tex`) cataloguing which theorems are
  Symp$_{\mathrm{form}}$-equivariant and which use a different
  equivariance group.
* **Do not** elevate the (∞,1)-equivariant factorization algebra to
  a theorem of this paper. Reserve it as a **future work** outlook
  paragraph: "A genuinely Symp$_{\mathrm{form}}$-equivariant
  (∞,1)-factorization algebra would require coherent
  $\varphi$-functoriality of the brane-line factorization sheaf at
  all higher orders; this is beyond the scope of the present
  formal-local theorem."
**Residual.** The (∞,1)-coherence question for the moduli stack of
branes in formal symplectic $\C^{2n}$ is a Phase-4 research problem,
parallel to N4 (unreduced BV centre).
**Deciding evidence.** The naturality table in `principles.tex` and
the future-work paragraph.

### W2-07 — Functoriality of the closed-open map under linear automorphisms
**Severity 2 (additive). Status valid. Confidence high.**
**Lens.** Drinfeld + Functoriality.
**Provenance.** W2 — new observation on the closed-open map's
covariance.
**Target.** Witten convention section in `principles.tex` lines
56–113; closed-open map of Theorem C.
**Claim under attack.** The closed-open map is "natural" without a
named equivariance group.
**Broken step.** The map $\Phi: c^I \mapsto \theta^I$, $u_I \mapsto
O_I$ depends on a basis $\{H_I\}$ of $\mathfrak h$. The
basis-independent reformulation: $\Phi$ is the canonical map
$C^\bullet_{\mathrm{CE}}(\mathfrak g) \to \mathrm{PV}(S(\mathfrak h))$
induced by the Lichnerowicz isomorphism. Under a Lie automorphism
$\varphi \in \mathrm{Aut}(\mathfrak h)$, both sides transform
covariantly: $\varphi$-twist on $\mathfrak g = \mathfrak h \ltimes
\mathfrak h^\vee[1]$ acts on $C^\bullet_{\mathrm{CE}}$ by inner
automorphism; on the PV side by pullback through
$\varphi: S(\mathfrak h) \to S(\mathfrak h)$. The map $\Phi$ is
$\mathrm{Aut}(\mathfrak h)$-equivariant. For $\mathfrak h$ the
formal Hamiltonian algebra of $\C^2$, $\mathrm{Aut}_{\mathrm{Lie}}(\mathfrak h)$
contains Symp$_{\mathrm{form}}(\C^2, 0)$ (acting by Hamiltonian
pullback) plus the abelian dilation group $\C^\times$ (rescaling
$\omega$). Hence Theorem C is naturally
**Symp$_{\mathrm{form}}(\C^2, 0)$-equivariant**.
**Evidence type.** proof_observation.
**Confidence.** High.
**Blast radius.** Theorem C is the central mathematical result;
making its naturality explicit is high-value.
**Minimal heal.** In `principles.tex` line 100 (Witten section),
after the generator dictionary, add: "The map $\Phi$ is
$\mathrm{Symp}_{\mathrm{form}}(\C^2, 0)$-equivariant: for any
formal symplectomorphism $\varphi$, $\varphi^* \Phi = \Phi
\varphi^*$ on generators, and the Lichnerowicz coordinate-free
reformulation extends this to a functor of dg $P_0$-algebras."
**Residual.** None.
**Deciding evidence.** The remark.

### W2-08 — Matlis vs residue split: two distinct theorems
**Severity 3. Status valid. Confidence high.**
**Lens.** Drinfeld + Functoriality.
**Provenance.** Wave-1 M-22 (Matlis-form uniqueness), A2-007 (split
identification + rigidity); W2 sharpening.
**Target.** `main.tex` `thm:canonical-residue-pairing` (lines
3838–3906); `thm:principal-part-coadjoint-uniqueness` (lines
3931–4017); `rmk:residue-pairing-schur` (lines 3908–3929);
`appendix-matlis-principal-parts.tex` Theorem
`thm:app-matlis-residue-rigidity` (lines 179–206); Proposition
`prop:app-matlis-realization` (lines 106–123).
**Claim under attack.** "Matlis-form uniqueness" — a single
statement.
**Broken step.** What is currently labelled
`thm:principal-part-coadjoint-uniqueness` (the "Matlis form")
conflates two genuinely separate facts:

1. **Matlis-module identification.** The continuous dual
   $\mathfrak h^\vee_{\mathrm{cont}}$ is canonically isomorphic to
   the reduced principal-part annihilator $\mathcal P =
   \mathrm{Ann}(\C \cdot 1) \subset E_R(\C) \cdot dz_1 dz_2$. This
   is Matlis duality + Grothendieck local cohomology + the residue
   trivialization of $\omega_R$. The identification is
   *categorical*: it follows from $E_R(\C) \cong H^2_{\mathfrak m}(R)
   \cdot dz_1 dz_2$ for the regular local 2-dim ring $R = \C[[z_1,
   z_2]]$, plus the dual filtration identification $F^N \mathcal P =
   \delta$-functionals vanishing on $\mathfrak m^{N+1}$. **Proof
   technique: Matlis duality theorem, Hartshorne LC.III, no residue
   calculation.**

2. **Residue-pairing rigidity.** Among all continuous, T²-Cartan-graded,
   total-degree-zero, $\mathfrak h$-equivariant pairings $\mathcal P
   \times \mathfrak h \to \C$, the residue pairing is unique up to
   scalar. **Proof technique: explicit T²-Cartan rigidity argument
   using $z_1, z_2, z_1 z_2$. Independent of Matlis.**

The current single theorem `thm:principal-part-coadjoint-uniqueness`
states (1) and (2) as a fused result. They are logically independent
— (1) gives the abstract isomorphism, (2) determines the unique
*formula* $\rho_{a,b} \mapsto \delta_{a,b}$ for the basis.

**Why the split matters.** (1) is **canonical** — fully natural
under Symp$_{\mathrm{form}}$; the isomorphism is intrinsic to the
formal disk. (2) is **canonical up to one scalar** — and the scalar
is the "residue normalization" choice. After the split:
* (1) is Symp-equivariant (W2-04).
* (2) determines that scalar uniquely under the additional choice
  of bigraded basis normalization $\langle \rho_{0,1}, z_2 \rangle =
  1$ (or whatever convention).

In the unified statement these get blurred and the "scalar" looks
unmotivated.

**Evidence type.** proof_inspection; structural.
**Confidence.** High.
**Blast radius.** Editorial clarity. Important for the platonic-ideal
manuscript.
**Minimal heal.** Replace `thm:principal-part-coadjoint-uniqueness`
in `main.tex` (lines 3931–3951) by a pair of theorems:

```latex
\begin{thm}[Matlis-module identification]\label{thm:matlis-module-identification}
  There is a canonical $\mathfrak h$-module isomorphism
  $$\mathcal P \xrightarrow{\sim} \mathfrak h^\vee_{\mathrm{cont}},$$
  natural under $\mathrm{Symp}_{\mathrm{form}}(\C^2, 0)$, induced by
  Matlis duality $E_R(\C) \cong H^2_{\mathfrak m}(R) \cdot dz_1 dz_2$
  for $R = \C[[z_1, z_2]]$, after the trivialization $\omega_R = R
  \cdot dz_1 dz_2$ and restriction to $\mathrm{Ann}(\C \cdot 1)$.
  The isomorphism is independent of the choice of basis or pairing
  normalization.
\end{thm}

\begin{proof}
  Matlis duality plus Hartshorne LC.III for the regular complete
  local ring $R$. Symp-naturality is
  Proposition~\ref{prop:matlis-symp-functorial}.
\end{proof}

\begin{thm}[Residue-pairing rigidity, T²-Cartan form]\label{thm:residue-pairing-cartan-rigidity}
  Among all continuous, T²-Cartan-graded, total-degree-zero,
  $\mathfrak h$-equivariant pairings
  $\mathcal P \times \mathfrak h \to \C$, the residue pairing
  $\langle \rho_{a,b}, z_1^m z_2^n \rangle = \delta_{a,m} \delta_{b,n}$
  is the unique nondegenerate one, up to a single scalar
  $c \in \C^\times$.
\end{thm}

\begin{proof}
  T²-Cartan rigidity argument using $z_1, z_2, z_1 z_2$ as in the
  current proof of Theorem~\ref{thm:canonical-residue-pairing}.
\end{proof}

\begin{cor}[Coadjoint isomorphism formula]\label{cor:coadjoint-isomorphism-formula}
  The Matlis-module identification of
  Theorem~\ref{thm:matlis-module-identification}, normalized by the
  residue-pairing scalar of Theorem~\ref{thm:residue-pairing-cartan-rigidity},
  is the explicit formula $\rho_{a,b} \mapsto \delta_{a,b}$.
\end{cor}
```

This **replaces the unified Theorem D rigidity statement** by an
**existence-and-identification + rigidity-of-formula** pair, with
the corollary supplying the explicit normalized isomorphism used
downstream.

**Residual.** Renaming downstream `\ref` labels in `main.tex`:3732,
4052, 4084, 4175, 4344, 4362; lane file 192; tate-T5:611. Each
reference picks up the appropriate replacement
(`cor:coadjoint-isomorphism-formula` for explicit formula uses;
`thm:matlis-module-identification` for module-isomorphism uses;
`thm:residue-pairing-cartan-rigidity` for normalization uses).
**Deciding evidence.** The split with explicit usage list.

---

## §3. Stable-core update: Theorem D's actual proven content

After the W2 inspection plus the M-06 / M-22 split, **Theorem D** of
the platonic-ideal plan resolves into **three independent theorems**:

* **Theorem D₁ (Matlis-module identification).** $\mathcal P \cong
  \mathfrak h^\vee_{\mathrm{cont}}$, canonical and
  Symp$_{\mathrm{form}}$-equivariant, by Matlis duality. Uses no
  residue calculation; uses regular-local-ring duality theory.

* **Theorem D₂ (Residue-pairing T²-Cartan rigidity).** The residue
  pairing is the unique nondegenerate continuous total-degree-zero
  T²-Cartan-equivariant pairing, up to a single scalar. Uses
  T²-Cartan torus rigidity plus one-parameter propagation along the
  bigraded lattice. **Does not need Schur**; **does not need full
  $\mathfrak h$-irreducibility** (which fails); **does not need
  symplectomorphism equivariance** (which is automatic in
  $\dim_\C = 2$).

* **Theorem D₃ (No-go for polynomial $\mathfrak h$-module realization).**
  Already correctly stated in the manuscript
  (`thm:no-polynomial-realization-categorical`). Uses local
  nilpotence on the polynomial side, raising-action on the
  principal-part side.

The wave-1 M-06 correction is verified: every downstream use of D₂
is either a normalization fact (one scalar $c$) or a formula use
(explicit lowering action), and **none requires $\mathfrak h$-Schur**.
The boundary-current locality theorem (Theorem E /
`prop:reduced-principal-part-boundary-current` at `main.tex`:4240)
uses **existence-with-integration-by-parts** of the residue pairing
(not its rigidity), so it is unaffected by the rigidity-rename.

---

## §4. Heal proposals as concrete LaTeX-level patches

(See ledger entries above for full statements; here, the patch list
in priority order.)

* **W2-P1 (W2-08).** Split `thm:principal-part-coadjoint-uniqueness`
  in `main.tex`:3931–3951 into D₁/D₂/Cor as displayed in §2 above.
  Renumber downstream `\ref`s.
* **W2-P2 (W2-01 + W2-02).** Edit `thm:canonical-residue-pairing`
  title to "Residue pairing, T²-Cartan rigid". Edit
  `rmk:residue-pairing-schur` to make the non-irreducibility of
  $\mathcal P$ explicit; replace "abstract Schur lemma" with "abstract
  Schur lemma applied to a putative irreducible $\mathfrak h$-module
  (which $\mathcal P$ is not; rigidity is T²-Cartan-isotypic)".
* **W2-P3 (W2-04, W2-05).** Add `prop:matlis-symp-functorial` in
  `appendix-matlis-principal-parts.tex` after line 104, citing
  Hartshorne III.10.10. Make the volume datum $\Omega = dz_1
  \wedge dz_2$ explicit in `def:app-matlis-topology`.
* **W2-P4 (W2-06).** Add a Naturality section in `principles.tex`
  cataloguing per-theorem equivariance group; do **not** elevate
  the (∞,1)-equivariant factorization algebra to a theorem.
* **W2-P5 (W2-07).** Add a one-sentence remark in `principles.tex`
  line 100 (Witten convention) noting Symp$_{\mathrm{form}}$-equivariance
  of the closed-open map $\Phi$.
* **W2-P6 (W2-03).** Add a clarifying paragraph in
  `theorem-lanes.tex` Lane 4 (after line 207) noting that Theorem D's
  rigidity is bigraded T²-Cartan and is **not used as Schur**
  downstream; Theorem E uses existence-with-integration-by-parts of
  the pairing.

---

## §5. Residuals

1. **Higher-symplectic-dimension Symp-equivariance.** Hartshorne's
   residue-intrinsicness theorem extends to $\C^{2n}$, $n \geq 2$,
   but the manuscript is local at $\C^2$; an explicit higher-dim
   extension is omitted. Phase-4 research.
2. **(∞,1)-coherence of Symp$_{\mathrm{form}}$-equivariant
   factorization algebras.** Reserved as outlook; not a desideratum
   for the present paper.
3. **Theorem B's PBW shadow Symp-equivariance.** Only the *labels*
   $\Psi_{a,b}$ are Symp-canonical; the *symmetric raising action*
   is GL$_2 \times$ T$^2$-only. The manuscript should acknowledge
   this asymmetry between the PBW (symmetry-breaking) shadow and the
   Matlis-dual (symmetry-canonical) cotangent.
4. **The "natural" ambiguity.** Drinfeld-style: without a named
   moduli stack and a named natural transformation group, "natural"
   is a slogan. The manuscript should either name the stack (formal
   symplectic disk + brane line) and the group
   (Symp$_{\mathrm{form}}(\C^2, 0)$ for the closed sector;
   $\mathrm{Diff}^+(\R)$ for the brane-line) explicitly, or
   abandon the naturality language. The W2-P4 catalogue is the
   cheap solution.

---

## §6. Summary

The wave-1 M-06 replacement of "Schur rigidity" with
**T²-Cartan-equivariant bigraded rigidity** is verified on inspection
of the proofs in `main.tex`:3848–3906 and
`appendix-matlis-principal-parts.tex`:179–206. The downstream audit
of `\ref{thm:principal-part-coadjoint-uniqueness}` and
`\ref{thm:canonical-residue-pairing}` (W2-03) confirms that **no
downstream theorem silently invokes full $\mathfrak h$-Schur**, in
particular the boundary-current locality theorem (Theorem E) uses
only existence-with-integration-by-parts of the pairing, not its
rigidity. Hence M-06 is a *correct* refinement, not a downgrade.

The volume-form-as-datum issue (M-04) is benign in $\dim_\C = 2$:
Symp = SDiff (volume-preserving) automatically, so $\Omega = dz_1
\wedge dz_2$ is intrinsically Symp$_{\mathrm{form}}$-fixed, and the
residue pairing is automatically Symp$_{\mathrm{form}}$-equivariant
by the residue-intrinsicness theorem (Hartshorne III.10.10). The
socle-canonicity (W2-05) follows. **Volume-datum-as-fixed is the
correct discipline**; it is canonical, not chosen.

The (∞,1)-equivariance question (W2-06) resolves to: Theorems C, D,
G are Symp$_{\mathrm{form}}$-equivariant; Theorem A is GL$_2$-only;
Theorem E is brane-line-$\mathrm{Diff}^+(\R)$-equivariant; Theorem
B's PBW shadow is GL$_2 \times$ T$^2$-only on actions. The full
(∞,1)-equivariant factorization algebra is a Phase-4 outlook, not a
present-paper desideratum.

The Matlis-vs-residue split (W2-08) is real: two genuinely separate
theorems (D₁ existence-and-identification; D₂ rigidity-of-formula)
are currently fused. The proposed split into D₁ + D₂ + Cor (the
explicit formula corollary) makes the manuscript's claim structure
honest, with each statement having its own proof technique (D₁ via
Matlis duality; D₂ via T²-Cartan rigidity).

**Net effect on the platonic-ideal plan.** Theorem D becomes three
theorems with explicit hypothesis annotations; the "Schur rigidity"
language is excised in favor of "T²-Cartan rigidity"; the
volume-form datum is named; Symp$_{\mathrm{form}}$-equivariance is
catalogued per-theorem; the closed-open map's covariance is
acknowledged. Downstream theorems are unaffected at the proof
level; only labels and references change. The total LaTeX patch
budget is approximately 8 numbered insertions (3 theorems, 2
remarks, 1 corollary, 1 catalogue table, 1 outlook paragraph) plus
a label-renumbering pass.

---

## Provenance

W2 wave-2 attack-heal entry, lensed by Drinfeld (moduli, canonical,
hidden groupoids, factorization structures) and Functoriality. Built
on wave-1 master ledger entries M-04, M-05, M-06, M-22 with W2-NN
sharpening. The downstream audit is by direct inspection of all
`\ref{thm:principal-part-coadjoint-uniqueness}` and
`\ref{thm:canonical-residue-pairing}` in `main.tex` (8 occurrences),
`tate-T5-chain-level-primitive.tex` (1 occurrence), and
`theorem-lanes.tex` (2 occurrences). Volume-datum analysis uses the
residue-intrinsicness theorem (Hartshorne, *Residues and Duality*,
III.10.10 + III App.A). Naturality classification is per-theorem on
the basis of explicit equivariance check.
