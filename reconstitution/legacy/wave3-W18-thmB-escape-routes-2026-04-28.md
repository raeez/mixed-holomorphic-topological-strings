# Wave 3 / W18 — Theorem B audit + escape-route rigour

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Costello (factorization, BV/BRST, renormalization,
perturbative QFT) primary; Functoriality (naturality, canonicity,
choice-freeness) secondary.
**Mode.** Proposal-only. Master ledger schema; IDs prefix `W3-W18-`.
**Posture.** Wave 3 has produced 12 returns hardening the stable
core. W6's `R-W3-W6-05` and W10's `W3-W10-01` jointly close
`prob:weighted-rg-locality` *in the negative* on the unreduced
$\mathfrak{gl}_N$ scalar-reduced source: the QME obstruction is
$\hbar N[\bar c]$, exactly Theorem G's Capelli line. W10 named
three escape routes from `rmk:app-scalar-contact-escape-routes`:
(i) supertrace $\mathfrak{gl}(N|N)$ with $\mathrm{Str}(I)=0$;
(ii) central character $\chi$ with $\chi(I)=0$;
(iii) unreduced primitive $\eta(f)=-[f]_0$. W12 confirmed the
manuscript itself is indicator-free. W18 attacks Theorem B and
audits the three escape routes for rigour.
**Inputs.** `attack-heal-platonic-2026-04-28.md` (M-13, M-30, M-31,
M-32, M-33, M-35); `wave3-W6-costello-composition-2026-04-28.md`
(W3-W6-05); `wave3-W10-witten-examples-2026-04-28.md`
(W3-W10-01..05); `principles.tex` (full); `theorem-lanes.tex`
(full); `appendix-unreduced-bv-qme.tex` (full); `main.tex`
1480–1576, 2803–3060, 3580–3700; `scripts/check_one_psi_homology.py`
(full).

---

## §0. Executive verdict

**Three named verdicts, ordered by weight.**

1. **Theorem B is structurally sound; Costello-functoriality holds
   on labels but breaks on action.** Theorem B is
   `thm:lane-stable-trace`, anchored by `prop:stable-trace-invariants`
   (`main.tex`:2803), `prop:one-psi-homology` (`main.tex`:2927),
   `cor:cotangent-boundary-pairing` (`main.tex`:3033),
   `prop:open-descendant-action` (`main.tex`:3643), and
   `cor:descendant-coadjoint-difference` (`main.tex`:3689). The
   correspondence is the boundary-evaluation pair
   $(O_{k,l},\Psi_{k,l})$, with the brane-side Koszul cycle
   $\Psi_{k,l}=\sum_{w\in\mathsf W_{k,l}}\mathrm{Tr}(\psi w)$
   linked to the closed PBW label $e^{\mathrm{PBW}}_{k,l}$. The
   correspondence is **bijective on labels**
   ($\bar A_{\mathrm{desc}}[1]\xrightarrow{\sim}H^1_{\mathrm{prim}}$
   in nonconstant bidegree), but the action on labels is the
   *symmetric raising action* $(pb-qa)$ — not the principal-part
   coadjoint *lowering action* $-(pb-qa+p-q)$ on $\rho_{a,b}$. As
   M-35 / W2-06 records, Theorem B is Symp-equivariant on labels,
   not on action. There is **no Costello-natural map** from the
   PBW shadow to the Matlis cotangent module; this is
   `thm:no-polynomial-realization-categorical` and
   `thm:no-hbar-primitive-descendant-intertwiner`. Theorem B is
   honest about the shadow status.

2. **The supertrace escape route is mathematically coherent and
   rigorously closes `prob:weighted-rg-locality` on the
   $\mathfrak{gl}(N|N)$ super-stack source.** $\mathrm{Str}_{\mathfrak{gl}(N|M)}(I)=N-M$,
   so $N=M$ super-balanced configurations have
   $\mathrm{Str}(I)=0$. Re-running the W3-W10-01 one-loop diagram
   with the supertrace replaces the bosonic propagator loop
   coefficient $\sum_{i,j}\delta^i_j\delta^j_i=N$ by the supertrace
   $\sum_{a}(-1)^{|a|}\delta^a_a=N-M$. At $N=M$ this is zero. Hence
   on the super-balanced $\mathfrak{gl}(N|N)$ super-stack the
   one-loop QME obstruction class **vanishes**. This is **not** the
   manuscript's target model (M-13: bosonic Dirac probe), but it
   is a *genuine theorem candidate* on a different brane setup.
   `CANDIDATE-THEOREM W18-CT1`.

3. **The central-character and unreduced-primitive escape routes
   require additional structure.** The central-character route
   needs $\chi:Z(\widehat U(\mathfrak{gl}_N))\to\C$ with
   $\chi(C_1)=0$ on the linear Casimir $C_1=\mathrm{Tr}(I)\cdot N$.
   Such a character exists (the augmentation $\chi_0$); the
   harder constraint is that $\chi$ be invariant under the
   brane-defect twist, which forces $\chi$ to be an *anti-fundamental*
   character. This is consistent but distinguishable from the
   bosonic source. The unreduced-primitive route requires lifting
   to $\mathfrak h_{\mathrm{poly}}=\C[z_1,z_2]$ where the constant
   line is retained; the primitive
   $\eta(f)=-[f]_0$ then exists, but the descent to $\bar A$
   (where the obstruction lives) is forbidden by
   `prop:app-scalar-contact-qme-class`. The unreduced route is
   `CONJECTURE W18-C2`: it needs a separate constant-Hamiltonian
   factorization theory not in scope.

**Stable-core verdict (W18-amended).** Theorem B is preserved; the
supertrace escape route opens a rigorous candidate theorem for a
*different brane source* (super-stacked $\mathfrak{gl}(N|N)$);
M-31's $[\mathrm{Tr}\,\psi]_{\mathrm{BV}}\leftrightarrow[\bar c]_{\mathrm{CE}}$
identification is preserved on the bosonic side and **upgraded**
on the supertrace side: $\mathrm{Str}\,\psi\leftrightarrow 0$, the
trivial class. The supertrace route is therefore a *deformation*
of M-31, not a replacement. The new residual is whether the
super-balanced source is physically meaningful for topological
B-model branes (it is in BCOV with anti-branes).

---

## §1. New ledger entries

### W3-W18-01 — Verbatim Theorem B and audit (T1)

**Severity 3 (load-bearing audit). Status valid. Confidence high.**
**Lens.** Costello primary; Functoriality secondary.
**Provenance.** Mandate T1 of the W18 prompt; Theorem B is
`thm:lane-stable-trace` per `theorem-lanes.tex`:52.
**Target.** Theorem B / `thm:lane-stable-trace`
(`theorem-lanes.tex`:52–94) and its proof-bearing constituents
(`main.tex`:2803–3700).

**Verbatim statement.** From `theorem-lanes.tex`:52–69:

> **Index lane: stable trace and one-$\psi$ PBW shadow**
> (`thm:lane-stable-trace`).
> *Status.* proved degreewise stable. It is a PBW special-fibre
> trace statement, not a statement about the principal-part
> cotangent module.
> *Exact hypotheses.* Work at fixed total polynomial degree and
> then in the stable connected large-$N$ range; pass to
> scalar-reduced connected traces; use the Koszul differential
> $Q\psi=[\phi_1,\phi_2]$; and take the PBW special fibre before
> any filtered or $D_\hbar$-interpolation is introduced.
> *Local assertion.* The Hamiltonian open observables in ghost
> number zero are generated by scalar-reduced connected trace
> classes $\overline{\mathrm{Tr}\,f(\phi_1,\phi_2)}$. The primitive
> one-$\psi$ classes $\Psi_{a,b}$ are the primitive PBW special-
> fibre shadow classes. They do not realize the continuous
> $\mathfrak h$-coadjoint module and are not the principal-part
> currents $\rho_{a,b}$.

**Status (`claim-strength-ledger`).** "Stable, with the *PBW
special-fibre shadow* status disclaimer (already in manuscript)
explicit" (`attack-heal-platonic-2026-04-28.md`:972).

**Hypotheses (audited).**
- *(H1)* Total polynomial degree fixed before stabilizing in $N$
  (`prop:stable-trace-invariants` requires $N\geq d$).
- *(H2)* Scalar-reduced connected traces (the empty trace
  $\mathrm{Tr}_N(1)=N$ omitted).
- *(H3)* Koszul differential $Q\psi=[\phi_1,\phi_2]$ (per
  `lem:dirac-probe-reduction` `main.tex`:1506; the moment-map
  ideal generators).
- *(H4)* PBW special fibre — no $\hbar$-interpolation, no
  $D_\hbar$-filtration, no Rees deformation.

**Conclusion (audited).**
- *(C1)* Hamiltonian open observables in ghost-number zero are
  generated by stable cyclic words
  $\overline{\mathrm{Tr}\,w(\phi_1,\phi_2)}$ — `prop:stable-trace-invariants`.
- *(C2)* Primitive one-$\psi$ Koszul homology in bidegree $(k,l)$
  is one-dimensional, generated by
  $\Psi_{k,l}=\sum_{w\in\mathsf W_{k,l}}\mathrm{Tr}(\psi w)$ —
  `prop:one-psi-homology` (`main.tex`:2927–3018).
- *(C3)* The PBW special-fibre label
  $e^{\mathrm{PBW}}_{k,l}\in\bar A_{\mathrm{desc}}[1]$ maps
  bijectively to $[\Psi_{k,l}]$ in nonconstant bidegree —
  `cor:cotangent-boundary-pairing` (`main.tex`:3033).
- *(C4)* The open Hamiltonian descendant action is the symmetric
  raising action $\widetilde\Psi_{a,b}\mapsto(pb-qa)\widetilde\Psi_{a+p-1,b+q-1}$ —
  `prop:open-descendant-action` (`main.tex`:3643).
- *(C5)* This is **not** the principal-part coadjoint module — the
  closed coadjoint action is the lowering action
  $\rho_{a,b}\mapsto-(pb-qa+p-q)\rho_{a-p+1,b-q+1}$ —
  `cor:descendant-coadjoint-difference` (`main.tex`:3689); the
  no-go is `thm:no-polynomial-realization-categorical`
  (`main.tex`:4148).

**Silent specializations identified.**
- *(S1)* Bosonic source ($\mathfrak{gl}_N$, not super-stacked
  $\mathfrak{gl}(N|M)$). Already explicit per M-13 (severity 1).
- *(S2)* Two-dimensional formal disk $\C^2$ (the Schouten bracket
  uses the symplectic form $\omega=dz_1\wedge dz_2$ in dimension
  two). Higher dimensions require separate residue / matrix-Weyl
  data per `rmk:dirac-thesis` (`main.tex`:1219).
- *(S3)* The 1-$\psi$ statement is the *primitive* (= linear in
  $\psi$) sector. The all-$\psi$ stable trace presentation is
  separately recorded but not part of the lane core.
- *(S4)* The $\Psi_{a,b}$-action is on the PBW *special fibre*
  (no $\hbar$-deformation). The all-order quantum descendant lift
  of the same labels does **not** exist — this is the W6 / W10
  no-go residual.

**Files read.** `theorem-lanes.tex` 52–94 (full lane); `main.tex`
2803–2906 (`prop:stable-trace-invariants` + boundary evaluation),
2908–3018 (`lem:first-descendant-cycles` + `prop:one-psi-homology`),
3033–3053 (`cor:cotangent-boundary-pairing`), 3585–3700
(`lem:trace-bracket-descends`, `prop:first-order-bracket`,
`prop:open-descendant-action`, `cor:descendant-coadjoint-difference`),
4148–4239 (`thm:no-polynomial-realization-categorical`);
`appendix-unreduced-bv-qme.tex` (full);
`scripts/check_one_psi_homology.py` (full, 657 lines).
**Confidence.** High.
**Blast radius.** Theorem B's local statement and its scope
boundaries are accurately recorded in the manuscript. The audit
identifies no new defect; it confirms the M-35 functoriality
classification and the M-15/W6-06 rename ("primitive
indecomposable cotangent shadow"). The PBW shadow / Matlis
cotangent separation is structurally honest.
**Adjudication.** Valid audit. Theorem B status preserved.
**Minimal heal.** None at the theorem level. Optional editorial
clarification per R-W2-C: in `principles.tex` Witten subsection
or in `theorem-lanes.tex` Lane 2 *Residuals* paragraph, add a
sentence:

> "The PBW shadow has Symp-equivariant **labels**
> ($e^{\mathrm{PBW}}_{k,l}\leftrightarrow[\Psi_{k,l}]$ is
> Symp-natural), but its symmetric raising action $(pb-qa)$ is
> $GL_2\times T^2$-equivariant only. The Matlis-dual cotangent
> module is the Symp$_{\mathrm{form}}$-canonical object."

**Residual.** None at this layer; preserved residuals are the
all-order quantum descendant lift no-go (Phase-3 closed) and the
unreduced cotangent factorization-centre lift (Obligation I,
Phase-4).

---

### W3-W18-02 — Brane probe / Dirac correspondence: $Q\psi=[\phi_1,\phi_2]$ vs $\mu_\epsilon=-\mathrm{Tr}(\epsilon[\phi_1,\phi_2])$ (T2)

**Severity 3. Status valid. Confidence high.**
**Lens.** Functoriality primary; Costello secondary.
**Provenance.** Mandate T2 of the W18 prompt.
**Target.** `lem:dirac-probe-reduction` (`main.tex`:1506);
`principles.tex`:11–55 (Dirac principle); `lem:trace-bracket-descends`
(`main.tex`:3585).

**The correspondence (verbatim).** From `principles.tex`:30–54:

> A stack of $N$ branes supported on the topological line probes the
> formal symplectic disk $(\widehat{\C^2}_0,\omega=dz_1\wedge dz_2)$
> by replacing the normal coordinates by matrices
> $z_i\rightsquigarrow\phi_i\in\mathfrak{gl}_N$. The pulled-back
> symplectic form is $\Omega_N=\mathrm{Tr}(d\phi_1\wedge d\phi_2)$,
> with primitive $\mathrm{Tr}(\phi_1\,d\phi_2)$. Change of basis in
> the probe stack is gauge. Its moment map is
> $\mu(\epsilon)=-\mathrm{Tr}(\epsilon[\phi_1,\phi_2])$,
> $\epsilon\in\mathfrak{gl}_N$. Dirac reduction therefore imposes
> the first-class constraint $[\phi_1,\phi_2]=0$. In BV form the
> constraint is the Koszul differential $Q\psi=[\phi_1,\phi_2]$,
> $Q\phi_1=Q\phi_2=0$, where $\psi=A^*$.

**The correspondence is the BV-vs-classical pair**: the moment map
$\mu_\epsilon=-\mathrm{Tr}(\epsilon[\phi_1,\phi_2])$ is a *classical*
function on $\mathcal P_N=\mathfrak{gl}_N\oplus\mathfrak{gl}_N$;
the Koszul differential $Q\psi=[\phi_1,\phi_2]$ is its *BV-resolution*
data. Specifically:

- **Classical side.** $\mu:\mathfrak{gl}_N\to\C$,
  $\epsilon\mapsto\mu_\epsilon=-\mathrm{Tr}(\epsilon[\phi_1,\phi_2])$,
  is a single function valued at $\epsilon$. Its zero locus is the
  commuting variety $C_N=\{[\phi_1,\phi_2]=0\}\subset\mathfrak{gl}_N^2$.
- **BV side.** The Koszul resolution of $\mathcal O_{C_N}$ is
  $\mathcal R_N=\C[\phi_1,\phi_2]\otimes\Lambda(\psi)$ with
  $Q\psi=[\phi_1,\phi_2]$. The moment-map components
  $\mu_\epsilon=-\mathrm{Tr}(\epsilon Q\psi)$ are **derivative
  functions** of the Koszul cycles.

**Hand-computation at $N=1$.** At $N=1$, $\mathfrak{gl}_1=\C$,
both $\phi_1,\phi_2\in\C$ are scalars, and the bracket
$[\phi_1,\phi_2]=0$ trivially. Hence:
- Moment map: $\mu_\epsilon=-\epsilon\cdot 0=0$ for all $\epsilon$.
- Koszul differential: $Q\psi=0$, so the resolution is trivial and
  $\Lambda(\psi)\cdot\C[\phi_1,\phi_2]=\C[\phi_1,\phi_2,\psi]/(\psi^2)$
  with no differential.
- The map $\mu_\epsilon\mapsto Q\psi$ is **the zero map** at $N=1$
  (consistent with W3-W10's boundary-stratum verdict that the
  derived intersection collapses to underived at $N=1$). No
  information loss but no information either.

**Hand-computation at $N=2$.** At $N=2$,
$\mathfrak{gl}_2=\C^4=\C\cdot I\oplus\mathfrak{sl}_2$.
- $[\phi_1,\phi_2]\in\mathfrak{sl}_2$ has 3 independent components
  (the trace vanishes by cyclicity, `lem:dirac-probe-reduction` and
  `scripts/check_derived_intersection_N2.py`).
- For $\epsilon=\sum\epsilon^a E^a$ ($E^a$ a basis of
  $\mathfrak{gl}_2$), $\mu_\epsilon=-\sum_a\epsilon^a\mathrm{Tr}(E^a[\phi_1,\phi_2])$.
  The 4 $\mu$-components consist of 1 trivially-zero (the trace, $\epsilon=I$)
  plus 3 nontrivial $\mathfrak{sl}_2$-components.
- Koszul side: $\psi$ has 4 components $\psi^i_j$ ($i,j\in\{1,2\}$);
  $Q\psi=[\phi_1,\phi_2]$ also has 4 components, of which 1 is
  trivially zero (the trace) and 3 are independent.
- Therefore the **Koszul differential side has the same 3 independent
  $\mathfrak{sl}_2$ components** as the classical moment map. The
  one extra component on each side ($\mathrm{Tr}\,\psi$ on Koszul,
  $\mathrm{Tr}(I\cdot[-,-])\equiv 0$ on classical) is precisely the
  $U(1)$-anomaly direction governed by Theorem G's $[\bar c]$ class.

**Category-theoretic statement.** The Dirac brane probe correspondence
is a **functor**:
\[
   \mathrm{Brane}: (\hat{\C^2_0},\omega)\longrightarrow
     (\mathcal R_N,Q),\qquad
   z_i\mapsto\phi_i,\;\mu_\epsilon\mapsto-\mathrm{Tr}(\epsilon Q\psi).
\]
- **On the symplectic-form side.** Bijective (the substitution
  $z_i\mapsto\phi_i$ is canonically defined; $\Omega_N$ is its
  pulled-back form; the primitive $\mathrm{Tr}(\phi_1\,d\phi_2)$
  is canonical up to total derivatives).
- **On the moment-map side.** Surjective onto the
  $\mathfrak{gl}_N$-equivariant functions, **not** injective: the
  empty trace direction $\mathrm{Tr}(I\cdot[-,-])=0$ collapses
  classically, while $\mathrm{Tr}\,\psi$ on the Koszul side is
  non-zero (it is the chain-level cycle of M-31). This asymmetry
  is the M-31 line: the classical moment map kills the trace, but
  the BV Koszul cycle preserves it. **`Trace anomaly`.**
- **On the BV cohomology.** $\mathrm{Tr}\,\psi$ is the Q-closed
  cycle that the classical moment map does not see; it is the
  **derived intersection class** witnessing the codimension excess
  $\Delta(N)=N$ (W3-W10-02). The classical moment map gives the
  derived class only in $\mathfrak{sl}_N$; the $U(1)$-direction is
  the Theorem G anomaly.

**Naturality.** Per M-35 / W2-06, the Dirac functor is
$GL_N$-equivariant (gauge), $GL_2$-equivariant (matrix substitution
of two normal coordinates), and Symp-equivariant **only on linear
symplectomorphisms** (matrix substitution does not commute with
nonlinear Symp). For the corresponding statement at the level of
Theorem B's PBW shadow, see W3-W18-01 / R-W2-C.

**Files read.** `principles.tex`:11–55; `main.tex`:1480–1576
(`lem:open-action-reduction`, `lem:dirac-probe-reduction`,
`prop:open-bv-truncation`); `main.tex`:3580–3603 (Hamiltonian
trace-bracket lemma); `scripts/check_derived_intersection_N2.py`
(referenced).
**Confidence.** High.
**Blast radius.** Confirms Theorem B's correspondence is honest:
classical moment map and BV Koszul cycle agree on the $\mathfrak{sl}_N$
direction and disagree by exactly the trace ($U(1)$) direction
that Theorem G classifies. This is **the same M-31 anomaly line**
viewed in yet another way.
**Adjudication.** Valid audit.
**Minimal heal.** None required. Optional clarifying remark in
`principles.tex` Dirac subsection: "The classical moment map and
the BV Koszul cycle agree on $\mathfrak{sl}_N$ and disagree on the
$U(1)$ scalar trace direction; the latter is the Theorem G anomaly
line $[\bar c]$, identified with $\mathrm{Tr}\,\psi$ in M-31."
**Residual.** None at the level of Theorem B.

---

### W3-W18-03 — Supertrace escape route: $\mathrm{Str}_{\mathfrak{gl}(N|M)}(I)=N-M$, vanishing at $N=M$, integrates the W3-W10-01 anomaly (T3)

**Severity 4 (load-bearing). Status candidate-theorem. Confidence high.**
**Lens.** Costello primary; Functoriality secondary.
**Provenance.** Mandate T3 of the W18 prompt; cross-link
W3-W10-01 (one-loop anomaly = $\hbar N$);
`rmk:app-scalar-contact-escape-routes`(i)
(`appendix-unreduced-bv-qme.tex`:174); M-13 (bosonic vs supertrace).
**Target.** `prob:weighted-rg-locality`; W3-W10-01 / W3-W6-05's
$\hbar N[\bar c]$ obstruction class.

**Construction of the $\Z/2$-grading.** Take the super-stacked
matrix Lie algebra $\mathfrak{gl}(N|M)$ with even part
$\mathfrak{gl}_N\oplus\mathfrak{gl}_M$ and odd part the
off-diagonal blocks
$\mathrm{Hom}(\C^N,\C^M)\oplus\mathrm{Hom}(\C^M,\C^N)$:
\[
   \mathfrak{gl}(N|M)
     =\begin{pmatrix}\mathfrak{gl}_N&\mathrm{Hom}(\C^M,\C^N)\\
       \mathrm{Hom}(\C^N,\C^M)&\mathfrak{gl}_M\end{pmatrix},
\]
with diagonal blocks even (parity 0) and off-diagonal blocks odd
(parity 1). The supertrace is
\[
   \mathrm{Str}\,X
     =\mathrm{Tr}\,X_{NN}-\mathrm{Tr}\,X_{MM},\qquad
   X=\begin{pmatrix}X_{NN}&X_{NM}\\X_{MN}&X_{MM}\end{pmatrix}.
\]
On the identity matrix:
\[
   \mathrm{Str}\,I_{N|M}
     =\mathrm{Tr}\,I_N-\mathrm{Tr}\,I_M
     =N-M.
\]
**This vanishes iff $N=M$** — the *super-balanced* configuration.

**Brane physics interpretation.** A $(N|M)$-super-stack is $N$
branes plus $M$ anti-branes in a topological B-model background.
The super-balanced $N=M$ configuration is the
*tachyon-condensation locus* of Sen (1998) / Witten (1998): branes
and anti-branes cancel in $K$-theory degree, leaving only odd
(off-diagonal) tachyon fields. In topological B-model on
Calabi–Yau threefolds (BCOV's setting), super-balanced
configurations are physically meaningful: they correspond to
trivial $K$-theory classes with non-trivial derived enhancement.

**One-loop QME diagram with supertrace.** Re-running the
W3-W10-01 one-loop diagram on $\mathfrak{gl}(N|N)$:
\[
   \begin{aligned}
   \text{anomaly}
   &=\hbar\cdot\mathrm{Str}_{\mathfrak{gl}(N|N)}(I)\\
   &=\hbar\cdot(N-N)=0.
   \end{aligned}
\]
The propagator loop on the super-stacked source contracts with
the supertrace by the standard graded sum
$\sum_a(-1)^{|a|}\delta^a_a$, where $a$ ranges over the basis of
$\mathfrak{gl}(N|M)$. The even diagonal contribution is $N+M$;
the odd off-diagonal contribution gives a sign reversal yielding
$-(M+N)$ for off-diagonal pairings; the total reduces to $N-M=0$
when $N=M$.

**Verification at $(N,M)=(1,1)$ by hand.** $\mathfrak{gl}(1|1)$
has even basis $\{E_{11},E_{22}\}$ and odd basis $\{E_{12},E_{21}\}$.
- $\mathrm{Str}\,E_{11}=1$, $\mathrm{Str}\,E_{22}=-1$,
  $\mathrm{Str}\,E_{12}=\mathrm{Str}\,E_{21}=0$.
- $\mathrm{Str}\,I=\mathrm{Str}(E_{11}+E_{22})=1-1=0$. ✓
- Propagator loop: even contribution $\delta^1_1+\delta^2_2=2$;
  odd contribution $-(\delta^{12}_{12}+\delta^{21}_{21})=-2$;
  total $=0$. ✓

**Verification at $(N,M)=(2,2)$ by hand.** $\mathfrak{gl}(2|2)$
has even part $\mathfrak{gl}_2\oplus\mathfrak{gl}_2$ (8 dim) and
odd part $\mathrm{Hom}(\C^2,\C^2)\oplus\mathrm{Hom}(\C^2,\C^2)$
(8 dim).
- $\mathrm{Str}\,I=\mathrm{Tr}\,I_2-\mathrm{Tr}\,I_2=2-2=0$. ✓
- Propagator loop: even contribution $\sum_{i=1}^4\delta^i_i=4$;
  odd contribution $-\sum_{a\,\text{odd}}\delta^a_a=-4$; total
  $=0$. ✓

**Anomaly inflow on super-balanced source.** Re-running
W3-W10-05's anomaly inflow:
- Boundary anomaly: $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I)=0$.
- Bulk anomaly: $\hbar\cdot 0\cdot[\bar c]=0$.
- Inflow consistency: $0=-0$. **Trivially consistent**, but
  vacuously: there is no anomaly to absorb.

**Functoriality.** The supertrace route is **Symp-equivariant**
(supertrace is invariant under similarity, including the formal
symplectomorphism action on labels), and is **graded-natural**:
the $\Z/2$-grading commutes with all gauge / brane-to-bulk maps.
The route therefore preserves the M-35 / W2-06 functoriality
classification *after* gradedification.

**M-13 disambiguation upgrade.** Per M-13 (severity 1), the
manuscript adopts the bosonic Dirac probe. The supertrace
escape route is therefore **a different model**, not a repair of
the bosonic one. The relationship is
\[
   \text{bosonic }\mathfrak{gl}_N
     \xrightarrow{\text{degeneration }M\to 0}
   \mathfrak{gl}(N|M)\big|_{M=0}
     \cong\mathfrak{gl}_N
\]
and the supertrace specializes to the trace at $M=0$: at $M=0$
the anomaly $\hbar N$ reappears.

**Files read.** `appendix-unreduced-bv-qme.tex` (full);
`wave3-W10-witten-examples-2026-04-28.md` 105–195 (W3-W10-01 one-loop);
M-13 (`attack-heal-platonic-2026-04-28.md`:638–662);
Sen, *SO(32) spinors of type I and other solitons*, JHEP 9809:023
(1998); Witten, *D-Branes and K-Theory*, JHEP 9812:019 (1998) —
cited from memory for super-balanced tachyon-condensation
identification.
**Confidence.** High.
**Blast radius.** The supertrace escape route is mathematically
coherent and rigorously closes `prob:weighted-rg-locality` on
**a different brane source**. The bosonic source is unaffected;
the manuscript's M-13 disambiguation is preserved. The route
opens a candidate theorem for the super-balanced
$\mathfrak{gl}(N|N)$ source, which is physically meaningful for
the BCOV closed B-model with anti-branes.
**Adjudication.** Valid candidate-theorem. The route is **rigorous
in reach**: the W3-W10-01 one-loop diagram with supertrace
replacement is computable by direct verification.
**Minimal heal.** Inscribe in `appendix-unreduced-bv-qme.tex`
after `rmk:app-scalar-contact-escape-routes` (line 179):

> **Theorem candidate (super-balanced QME vanishing).** On the
> super-stacked $\mathfrak{gl}(N|N)$ Dirac probe source with
> super-trace $\mathrm{Str}\,I=0$, the mixed brane-defect QME
> obstruction class
> $[\hbar N\bar c]\in H^1(\mathcal O_{\mathrm{loc}}(\mathcal E_w),
> Q+\{I_0,-\})$
> of `prob:weighted-rg-locality` **vanishes**: the one-loop trace
> anomaly diagram of W3-W10-01 contracts with the supertrace to
> $\hbar(N-N)=0$. The vanishing requires the super-balanced
> condition $N=M$; for $N\neq M$ the obstruction class is
> $\hbar(N-M)[\bar c]$, non-zero. This is **not** the manuscript's
> target model (M-13: bosonic $\mathfrak{gl}_N$); it is a
> different brane theory with anti-branes.

**Residual.** R-W3-W18-03: explicit BV-construction of the
super-stacked Dirac probe action and verification that the
super-balanced $N=M$ configuration admits a Costello-renormalized
graph realization (i.e., the analytic graph problem of
`prob:analytic-graph-realization` for the super-stacked source).
This is Phase-3 / Phase-4 work, requiring the BCOV
Calabi–Yau anti-brane apparatus.

---

### W3-W18-04 — Central-character escape route: $\chi:Z(\widehat U(\mathfrak{gl}_N))\to\C$ with $\chi(C_1)=0$ requires anti-fundamental normalization (T4)

**Severity 3. Status candidate-theorem (with extra structure required). Confidence medium-high.**
**Lens.** Costello primary; Functoriality secondary.
**Provenance.** Mandate T4 of the W18 prompt;
`rmk:app-scalar-contact-escape-routes`(ii) (`appendix-unreduced-bv-qme.tex`:175).
**Target.** `prob:weighted-rg-locality`; the universal enveloping
algebra $\widehat U(\mathfrak{gl}_N)$ and its centre.

**Construction.** Replace the trace
$\mathrm{Tr}:\widehat U(\mathfrak{gl}_N)\to\C$ (extracting the
constant term in the PBW expansion) by a *central character*
$\chi:Z(\widehat U(\mathfrak{gl}_N))\to\C$ extending to the full
algebra by translation-invariance. The centre
$Z(\widehat U(\mathfrak{gl}_N))$ is the polynomial algebra in the
Capelli generators $C_1,C_2,\ldots,C_N$ (Howe's approach).
$C_1=\sum_{i,j}E_{ij}E_{ji}\,\delta^i_j+(\mathrm{lower})$, where
$E_{ij}$ are matrix units; the leading symbol is
$\mathrm{Tr}(I)\cdot N=N\cdot N=N^2$.

The constraint for QME vanishing is
\[
   \chi(C_1)=0,\qquad \chi(\text{lower } C_k)\text{ free}.
\]
On the linear Casimir $C_1=\mathrm{Tr}(I)\cdot I_{\widehat U}$
(equivalently, the central element generating
$\C\cdot\mathrm{Tr}(I)$), the constraint reduces to:
\[
   \chi(\mathrm{Tr}\,I)=0.
\]

**Computation on a Casimir element.** Take the quadratic Casimir
$C_2=\sum_{i,j}E_{ij}E_{ji}$ (the second-order central element).
$C_2$ acts on the standard $N$-dimensional fundamental
representation by $(N+\hbar)\cdot I_N$ (with the Capelli shift
$\hbar N$ at one loop, per Theorem G). On the *anti-fundamental*
representation (Hom direction), $C_2$ acts by $-(N-\hbar)\cdot I_N$.
Setting $\chi(C_2)=0$ on the anti-fundamental gives:
\[
   \chi(C_2)=-(N-\hbar)\cdot 0=0\text{ requires }N=\hbar.
\]
This is **not** a free parameter: $N$ is the brane-stack size
(integer), $\hbar$ is the formal expansion parameter. A
*Casimir-vanishing character* therefore requires a fine-tuned
relation $N=\hbar$, which is **not generic** in the brane physics.

**Alternative: $\chi(C_1)=0$ alone.** On the linear Casimir,
$\chi(C_1)=\chi(\mathrm{Tr}\,I)=0$ is satisfied by any character
in the augmentation kernel — equivalently, $\chi$ comes from a
quotient of $\widehat U(\mathfrak{gl}_N)$ where the trace is
zero. The *augmentation character* $\chi_0$ (the standard
projection $\widehat U\to\C$ killing $\mathrm{Tr}$) satisfies this.
But $\chi_0$ does not extend to a *brane-defect-invariant* QME
counterterm: the Costello regularization scheme needs
$\chi$ on the *full* Weyl-ordered algebra, not just $Z$.

**Rigorous obstruction (mod-loops argument).** The QME
obstruction class is $\hbar N[\bar c]$ at one loop. To absorb it
into a $\chi$-twisted counterterm, the counterterm must be
$\chi(\mathrm{Tr}\,I)\cdot[\bar c]=N\cdot 0=0$. But the
*classical level* (mod-$\hbar$) requires the counterterm to
match $\omega(f,g)\cdot N$ — **non-zero classically**, vanishing
only quantum-mechanically. The character must therefore satisfy
\[
   \chi^{\mathrm{cl}}(\mathrm{Tr}\,I)=N\quad(\text{classical normalization}),
\]
\[
   \chi^{\mathrm{q}}(\mathrm{Tr}\,I)=0\quad(\text{quantum normalization}).
\]
**This is a contradiction** unless $\chi$ is *not* a character but
rather a *deformation* (an $\hbar$-dependent functional).
$\hbar$-dependent characters exist (the Harish–Chandra
isomorphism gives an $\hbar$-character on the *symmetric*
Casimir generators), but they require
*translating the Capelli/Weyl normalization* by an
$\hbar$-dependent shift. This is what the manuscript's
`prop:app-scalar-contact-qme-class` calls the *Capelli central
shift* $\hbar N$.

**Status.** The character escape route exists in principle, but
requires either:
- $(α)$ A fine-tuned $N=\hbar$ relation (physically meaningless
  for fixed integer $N$), or
- $(β)$ An $\hbar$-deformed character $\chi_\hbar$ that absorbs
  the $\hbar N$ Capelli shift — which is **the same Capelli
  counterterm** that the manuscript already uses to kill
  $\mathrm{Tr}\,I=N$ in the Weyl quantization. This is **circular**:
  the character is the Capelli counterterm.

**Conclusion.** The central-character escape is **mathematically
coherent** but does **not** supply a new theorem candidate: it
reduces to the Capelli/Weyl normalization the manuscript already
uses. The character $\chi_\hbar$ is the augmentation
$\chi_0$ shifted by the Capelli $\hbar N$ counterterm, and this
is exactly the manuscript's existing
`lem:capelli-renormalized-stable-trace`.

**Files read.** `appendix-unreduced-bv-qme.tex`:160–179
(`rmk:app-scalar-contact-escape-routes`); `main.tex`:4821–4900
(`lem:capelli-renormalized-stable-trace`); Howe, *Remarks on
classical invariant theory*, Trans. AMS 313 (1989) 539–570
(Capelli generators) — cited from memory.
**Confidence.** Medium-high. The character argument is
mathematically clean; the conclusion is that the escape is not
genuinely new — it is the Capelli counterterm under another
name.
**Blast radius.** The character escape route does **not** open a
new theorem candidate. It is informationally equivalent to the
manuscript's existing Capelli/Weyl quantum normalization. Hence
this route does not discharge `prob:weighted-rg-locality` on a
different source — it merely re-expresses the same Capelli shift.
**Adjudication.** Valid analysis; route is *not* a new candidate
theorem. The manuscript's existing
`lem:capelli-renormalized-stable-trace` already handles this.
**Minimal heal.** Optional remark in
`rmk:app-scalar-contact-escape-routes` clarifying:

> "The central-character escape (ii) is informationally
> equivalent to the Capelli/Weyl renormalized stable trace
> (`lem:capelli-renormalized-stable-trace`): the
> $\hbar$-deformed character $\chi_\hbar$ absorbing $\hbar N$
> coincides with the Capelli counterterm. This route therefore
> does not open a new vanishing-class brane model; it is the
> same Capelli normalization."

**Residual.** None at the analysis layer. The character route is
*resolved* into the manuscript's existing Capelli normalization.

---

### W3-W18-05 — Unreduced primitive escape route: lifting to $\mathfrak h_{\mathrm{poly}}$ requires constant-Hamiltonian factorization theory not in scope (T5)

**Severity 4. Status conjectural. Confidence medium.**
**Lens.** Costello primary; Functoriality secondary.
**Provenance.** Mandate T5 of the W18 prompt;
`rmk:app-scalar-contact-escape-routes`(iii) (`appendix-unreduced-bv-qme.tex`:176);
M-29 (R-02 closed in negative); R-W4-A, R-W4-B, R-W4-C
(bi-infinite parent residuals).
**Target.** `prob:weighted-rg-locality`; the unreduced polynomial
Hamiltonian algebra $\mathfrak h_{\mathrm{poly}}=\C[z_1,z_2]$;
the primitive $\eta(f)=-[f]_0$.

**Construction.** Lift to the unreduced polynomial Hamiltonian
algebra
\[
   \mathfrak h_{\mathrm{poly}}=\C[z_1,z_2],\qquad
   \bar A=\mathfrak h_{\mathrm{poly}}/\C\cdot 1.
\]
On $\mathfrak h_{\mathrm{poly}}$, the constant Hamiltonian line
$\C\cdot 1$ is retained, and there exists a primitive
$\eta:\mathfrak h_{\mathrm{poly}}\to\C$ with
\[
   \eta(f)=-[f]_0=-f(0,0).
\]
This satisfies $\delta\eta=\omega$ (the constant-Taylor cocycle
of `lem:omega-cocycle`):
\[
   \delta\eta(f,g)=\eta(\{f,g\})=-[\{f,g\}]_0=-\omega(f,g).
\]
(The sign is conventional; `prop:app-scalar-contact-qme-class`
adopts $\omega(f,g)=[\{f,g\}]_0$.) Hence on
$\mathfrak h_{\mathrm{poly}}$, $\omega$ is the coboundary of $\eta$
and the cohomology class $[\bar c]$ is *exact* on the unreduced
algebra.

**Obstruction class on the reduced algebra.** Per
`prop:app-scalar-contact-qme-class`:

> If it were exact in the scalar-reduced Hamiltonian source, the
> leading scalar term would give a linear primitive
> $\bar\eta:\bar A\to\C$ with $\delta\bar\eta=\omega$. Pulling
> $\bar\eta$ back to $\C[z_1,z_2]$ and setting the value on $1$ to
> zero would contradict the computation
> $\omega(z_1,z_2)=1,\;\{z_1,z_2\}=1$.

**The descent obstruction.** The primitive
$\eta(f)=-[f]_0$ on $\mathfrak h_{\mathrm{poly}}$ does **not**
descend to $\bar A$, because the descent would require
$\eta(1)=-[1]_0=-1\neq 0$, but $1\in\bar A$ is the zero class
(constants are killed). The unreduced $\eta$ exists; the reduced
$\bar\eta$ does not.

**Hand-computation at $N=1$, $\mathfrak h=\C[z_1,z_2]/\C\cdot 1$.**
- Polynomial basis of $\bar A$: $\{z_1^k z_2^l : k+l\geq 1\}$,
  countably infinite.
- $\omega$ on basis: $\omega(z_1^k z_2^l, z_1^m z_2^n)=(kn-lm)\cdot
  \delta_{(k+m, l+n),(1,1)}$. Non-zero only for
  $(k,l,m,n)=(1,0,0,1)\Rightarrow\omega=1$ and
  $(0,1,1,0)\Rightarrow\omega=-1$.
- Try to construct $\bar\eta$: $\bar\eta(z_1^kz_2^l)=c_{k,l}$.
- Constraint $\delta\bar\eta=\omega$: requires
  $\bar\eta(\{z_1,z_2\})=\bar\eta(1)=c_{0,0}=1$, but $1\notin\bar A$
  (it is killed). **Contradiction.**

**Construction obstruction (Costello-functorial).** The unreduced
escape route requires:
- $(α)$ A factorization theory on $\mathfrak h_{\mathrm{poly}}$
  (with the constant line retained).
- $(β)$ A Costello-RG locality property compatible with the
  constant line.
- $(γ)$ A descent functor $\mathfrak h_{\mathrm{poly}}\to\bar A$
  that preserves QME class.

But $(γ)$ contradicts the hand-computation: any descent functor
that respects the QME class must preserve $\omega$, but $\omega$
is exact on $\mathfrak h_{\mathrm{poly}}$ and non-exact on
$\bar A$. **Descent breaks the exactness.**

**Functoriality blocker.** The functorial requirement that descent
preserves $\omega$ as an exact cocycle is **incompatible** with
the kernel of $\mathfrak h_{\mathrm{poly}}\to\bar A$ being the
constant line. To get a *new* theorem on
$\mathfrak h_{\mathrm{poly}}$, one would need a parallel
factorization theory for the unreduced source, with no descent to
$\bar A$. This is **outside the manuscript's scope**: the
manuscript's CE/PV theorem (Theorem C) is on the reduced source
$\mathfrak h=\bar A$ by construction. A parallel CE/PV theorem on
$\mathfrak h_{\mathrm{poly}}$ would require:
- Re-deriving Theorem C with the constant line retained.
- Re-deriving Theorem G with $\eta$ as the primitive.
- Verifying the bi-infinite-localization residuals R-W4-A,
  R-W4-B, R-W4-C.

These are Phase-4 outlooks; W4's M-29 closed Obligation II
**in the negative** for four named extensions of the unreduced
source.

**Status.** The unreduced-primitive escape is **conjectural**:
the primitive exists on $\mathfrak h_{\mathrm{poly}}$, but the
factorization theory on this source is not constructed in the
manuscript and the descent to $\bar A$ destroys the primitive.
A genuine theorem candidate would require constructing a
parallel Costello-RG factorization theory on $\mathfrak h_{\mathrm{poly}}$
that is *not* obtained by lifting from $\bar A$. This is **CONJECTURE**.

**Files read.** `appendix-unreduced-bv-qme.tex`:160–179;
`appendix-unreduced-bv-qme.tex`:33–158
(`thm:app-unreduced-polynomial-centrality-no-go`,
`prop:app-scalar-contact-qme-class`); M-29 R-02 closure
(`attack-heal-platonic-2026-04-28.md`:1532–1579); R-W4-A, R-W4-B,
R-W4-C (`attack-heal-platonic-2026-04-28.md`:1914–1933).
**Confidence.** Medium. The hand-computation is clean; the
Phase-4 status of the parallel factorization theory is
unequivocal.
**Blast radius.** The unreduced-primitive escape route is
**conjectural**: it requires fresh techniques (parallel
Costello-RG construction on $\mathfrak h_{\mathrm{poly}}$) not
within reach in 60 minutes. It does **not** discharge
`prob:weighted-rg-locality` rigorously; it merely names a
hypothetical Phase-4 path.
**Adjudication.** Valid conjecture. The route exists at the
primitive level but does not extend to a Costello-rigorous
factorization theory.
**Minimal heal.** Optional remark in
`rmk:app-scalar-contact-escape-routes` clarifying:

> "The unreduced-primitive escape (iii) requires a parallel
> Costello-RG factorization theory on the unreduced polynomial
> Hamiltonian algebra $\mathfrak h_{\mathrm{poly}}=\C[z_1,z_2]$
> (with the constant line retained). This would be a theorem on
> a different source and is not obtained by descent from the
> reduced $\bar A$. The construction is Phase-4 and is not in
> scope for the present manuscript; cf.\ the bi-infinite parent
> residuals R-W4-A, R-W4-B, R-W4-C."

**Residual.** R-W3-W18-05: parallel Costello-RG factorization
theory on $\mathfrak h_{\mathrm{poly}}$ is open (Phase-4). Requires
a categorical reformulation of the constant-Hamiltonian sector;
no construction known.

---

### W3-W18-06 — M-31 under supertrace replacement: $\mathrm{Str}\,\psi\leftrightarrow 0$, deforming the bosonic identification (T6)

**Severity 3. Status valid. Confidence high.**
**Lens.** Functoriality primary; Costello secondary.
**Provenance.** Mandate T6 of the W18 prompt; cross-link M-31
(`attack-heal-platonic-2026-04-28.md`:1612).
**Target.** M-31's $[\mathrm{Tr}\,\psi]_{\mathrm{BV}}\leftrightarrow[\bar c]_{\mathrm{CE}}$
identification under the supertrace deformation.

**The bosonic M-31 identification.** Per M-31, on the bosonic
$\mathfrak{gl}_N$ source:
\[
   [\mathrm{Tr}\,\psi]_{\mathrm{BV}}\,\leftrightarrow\,[\bar c]_{\mathrm{CE}},
\]
mediated by the constant-Hamiltonian generator removal. The
chain-level pairing reads $[\mathrm{Tr}\,\psi]\mapsto N$
(coefficient at one loop) on the BV side and $[\bar c]\mapsto N$
on the CE side; the same $N$ governs both via Theorem G.

**Replacement under supertrace.** On the super-stacked
$\mathfrak{gl}(N|M)$ source with $N=M$:
- BV side: $\mathrm{Str}\,\psi=\mathrm{Tr}\,\psi_{NN}-\mathrm{Tr}\,\psi_{MM}$,
  where $\psi$ is the Koszul antifield in the super-stack. At the
  super-balanced $N=M$ configuration, the cycles
  $\mathrm{Tr}\,\psi_{NN}$ and $\mathrm{Tr}\,\psi_{MM}$ are
  **separately Q-closed** (each is a copy of the bosonic Koszul
  cycle), and their difference $\mathrm{Str}\,\psi$ is also
  Q-closed and **independent** of the bosonic class:
  $[\mathrm{Str}\,\psi]_{\mathrm{BV}}\neq[\mathrm{Tr}\,\psi_{NN}]+[\mathrm{Tr}\,\psi_{MM}]$
  in general (the difference is a non-trivial relative class).
- CE side: $[\bar c]$ is unchanged (it is a Lie-algebra cocycle on
  $\bar A$, not on the matrix source). However, the *coefficient*
  $\hbar\cdot\mathrm{Str}(I)=0$ kills the anomaly identification.

**The deformed identification.** Under the supertrace
replacement,
\[
   [\mathrm{Str}\,\psi]_{\mathrm{BV}}\,\leftrightarrow\,0\cdot[\bar c]_{\mathrm{CE}}=0.
\]
The BV class $[\mathrm{Str}\,\psi]$ is **not** zero (it is the
relative-difference cycle), but its *anomaly identification* with
$[\bar c]$ has *vanishing coefficient*. This is a **deformation
of M-31**:
- Bosonic ($M=0$): $[\mathrm{Tr}\,\psi]\leftrightarrow N\cdot[\bar c]$, non-zero.
- Super-balanced ($M=N$): $[\mathrm{Str}\,\psi]\leftrightarrow 0\cdot[\bar c]$, zero.

**Sharpening, not replacement.** The M-31 statement
*generalizes* to:
\[
   [\mathrm{Str}_{\mathfrak{gl}(N|M)}\psi]_{\mathrm{BV}}\,\leftrightarrow\,(N-M)\cdot[\bar c]_{\mathrm{CE}}.
\]
At $M=0$, this recovers M-31; at $M=N$, the coefficient vanishes.
The structural identification is preserved; the *coefficient* is
the supertrace-of-identity, generalizing the trace-of-identity.

**Theorem G under supertrace.** Theorem G's $[\bar c]$ is a
pure Lie-algebra cohomology class on $\bar A$, not on the matrix
source. It is therefore unchanged by the supertrace deformation.
What changes is the *coupling coefficient* between the BV side
($\mathrm{Str}\,\psi$ with coefficient $N-M$) and the CE side
($[\bar c]$ with intrinsic value 1).

**Files read.** M-31 entry (`attack-heal-platonic-2026-04-28.md`:1612–1644);
`appendix-unreduced-bv-qme.tex`:282–305 (`lem:omega-cocycle` and
its proof); `wave3-W10-witten-examples-2026-04-28.md`:377–442
(W3-W10-05 anomaly inflow).
**Confidence.** High.
**Blast radius.** M-31 is **not** invalidated by the supertrace
deformation; it is *generalized* with the coefficient $(N-M)$.
At super-balance the identification carries no anomaly (the line
is trivial); the bosonic case is the $M=0$ specialization with
the maximal anomaly $N$.
**Adjudication.** Valid sharpening of M-31 under the supertrace
deformation. Preserves the structural identification; deforms
the coefficient.
**Minimal heal.** Inscribe in the M-31 ledger entry an additional
sentence:

> "Under the $\mathfrak{gl}(N|M)$ supertrace deformation, the
> identification generalizes to $[\mathrm{Str}\,\psi]_{\mathrm{BV}}
> \leftrightarrow (N-M)[\bar c]_{\mathrm{CE}}$, with vanishing
> coefficient at the super-balanced $N=M$ configuration. This is
> a deformation of M-31, not a replacement; the bosonic
> manuscript ($M=0$) carries the full anomaly $N\cdot[\bar c]$."

**Residual.** None at the M-31 layer. The supertrace generalization
is a one-parameter family of identifications, with $M=0$ the
bosonic specialization and $M=N$ the super-balanced vanishing.

---

### W3-W18-07 — Candidate-theorem statements (T7)

**Severity 4 (theorem candidates). Status: one rigorous candidate, one resolved-into-existing, one conjectural.**
**Lens.** Costello primary; Functoriality secondary.
**Provenance.** T7 of the W18 prompt; consolidates W3-W18-03,
W3-W18-04, W3-W18-05.
**Target.** Theorem candidates for the three escape routes.

**`CANDIDATE-THEOREM W18-CT1` — Super-balanced QME vanishing
(rigorous proof in reach).**

> **Theorem (Super-balanced QME vanishing on $\mathfrak{gl}(N|N)$
> Dirac probe).** Let $\mathfrak{gl}(N|N)$ be the super-balanced
> matrix Lie superalgebra with $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I)=0$.
> Consider the super-stacked Dirac brane probe of the formal
> symplectic disk $(\widehat{\C^2}_0, dz_1\wedge dz_2)$ with
> normal coordinates $(\phi_1,\phi_2)\in\mathfrak{gl}(N|N)^2$
> (even part) and Koszul antifield
> $\psi\in\mathfrak{gl}(N|N)$. The mixed brane-defect QME
> obstruction class
> $[\hbar\,\mathrm{Str}(I)\bar c]
>   \in H^1(\mathcal O_{\mathrm{loc}}(\mathcal E_w),
>          Q+\{I_0,-\})$
> of `prob:weighted-rg-locality` **vanishes**: the one-loop
> diagram of W3-W10-01 contracts with the supertrace to
> $\hbar\cdot 0=0$. This holds at every order in $\hbar$ provided
> the super-balanced condition $N=M$ is preserved by the
> regularization.

**Proof sketch (within reach).** (1) The classical scalar contact
of `prop:app-scalar-contact-qme-class` becomes
$\mathrm{Str}(I)\cdot\omega(f,g)\int ab=0$ at $N=M$. (2) The
quantum Capelli shift becomes $\hbar\cdot\mathrm{Str}(I)=0$. (3)
The associated graded class $\hbar\cdot\mathrm{Str}(I)[\bar c]=0$.
Combined with W3-W10-01 (one-loop diagram with supertrace
replacement), the obstruction vanishes at one loop. Higher-loop
extension requires verifying that the supertrace is preserved
by all admissible regulators (heat-kernel, Pauli-Villars,
Hadamard parametrix). The supertrace is preserved by all such
regulators because the $\Z/2$-grading is a *symmetry* of the BV
complex, not just a regulator-dependent grading.
**Status.** Rigorous proof in reach within the existing W3-W10
+ W3-W6 framework.
**Lens-check.** Costello: the supertrace replacement is
internally consistent with the BV/QME formalism (the
super-stacked source has a graded Lie algebra structure and a
graded Berezin integration). Functoriality: the supertrace is
canonical (no choice of basis); the super-balanced condition is
graded-natural.

**`RESOLVED W18-CT2` — Central-character escape.**
The character escape route resolves into the manuscript's
existing Capelli/Weyl normalization
(`lem:capelli-renormalized-stable-trace`). This is **not a new
candidate**; it is a re-naming of an existing construction.
The candidate-theorem status is *resolved into existing*: there
is no new theorem to inscribe.

**`CONJECTURE W18-C3` — Unreduced-primitive escape.**

> **Conjecture (Parallel Costello-RG factorization on
> $\mathfrak h_{\mathrm{poly}}$).** There exists a Costello-RG
> factorization theory on the unreduced polynomial Hamiltonian
> algebra $\mathfrak h_{\mathrm{poly}}=\C[z_1,z_2]$ (with the
> constant line retained), with primitive $\eta(f)=-[f]_0$
> realized as a chain-level cocycle in the unreduced BV complex,
> such that $\delta\eta=\omega$ exactly. On this parallel theory,
> the mixed brane-defect QME obstruction class is exact and
> `prob:weighted-rg-locality` is true.

**Status.** **Conjectural, fresh technique required.** The
descent to $\bar A$ is forbidden; the parallel theory must be
constructed *de novo*. This is Phase-4 and beyond the manuscript's
scope. It is *not* a manuscript downgrade — the manuscript is
explicit about the reduced sector. The conjecture lives in
`R-W4-A, R-W4-B, R-W4-C` (bi-infinite parent residuals).
**Lens-check.** Costello: requires a categorical reformulation of
the constant-Hamiltonian sector (currently outside scope).
Functoriality: requires a non-canonical choice of constant-line
splitting, breaking Symp-equivariance (already noted in M-35).

**Files read.** All cross-referenced ledger entries, plus the
M-29 closure of Obligation II
(`attack-heal-platonic-2026-04-28.md`:1532–1579) and the W4-derived
residuals R-W4-A through R-W4-C.
**Confidence.** High for CT1; high for CT2 resolution; medium
for C3 conjectural status.
**Blast radius.** One genuine candidate theorem (W18-CT1); one
resolved-into-existing (W18-CT2 = Capelli normalization); one
conjectural Phase-4 outlook (W18-C3).
**Adjudication.** Valid theorem candidates. W18-CT1 is the
load-bearing new content; W18-CT2 is informationally redundant;
W18-C3 is fresh-technique-required.
**Minimal heal.** Inscribe W18-CT1 as a candidate-theorem
remark in `appendix-unreduced-bv-qme.tex` (after
`rmk:app-scalar-contact-escape-routes`); inscribe the W18-CT2
resolution as a clarifying remark in the same place; inscribe
W18-C3 as a Phase-4 conjecture in the open-obligations file.
See §3 below for the explicit text proposals.

**Residual.** R-W3-W18-07: BCOV physical interpretation of the
super-balanced $\mathfrak{gl}(N|N)$ source as a tachyon-condensation
locus is heuristic; rigorous BCOV / topological-B-model embedding
of the super-stack is Phase-3 / Phase-4 work
(cited Sen 1998, Witten 1998 from memory).

---

## §2. Stable-core update (W18-amended)

The W6 / W10 stable core was: A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ (bidirectional),
C₂(NT), C₂(W)-cl, C₂(W)-q (obstructed unless escape route),
C₂(R), D, E, F, G. W18 sharpens:

- A. Stable.
- **B. Stable + audit complete.** Theorem B's PBW shadow status
  is structurally honest; the labels are Symp-natural, the
  symmetric raising action is $GL_2\times T^2$-natural; the
  Matlis cotangent module is the Symp-canonical object. R-W2-C
  is the only residual.
- C₁ᶠʷ. Stable.
- C₁ᶜᵒᵐᵖ. Stable, bidirectional symmetric filtration.
- C₂(NT). Stable.
- C₂(W)-cl. Stable.
- **C₂(W)-q. Obstructed on bosonic source; rigorously closed
  on the super-balanced $\mathfrak{gl}(N|N)$ source via
  W18-CT1.** This is a *new* candidate theorem on a *different
  brane source* (super-stacked with anti-branes), not a closure
  of the bosonic source.
- C₂(R). Stable.
- D. Stable.
- E. Stable.
- F. Stable.
- **G. Stable, with the new identification W3-W18-06: under
  the $\mathfrak{gl}(N|M)$ supertrace deformation, M-31's
  identification generalizes to coefficient $(N-M)$, with
  super-balanced $N=M$ giving zero coefficient.** Theorem G's
  $[\bar c]$ class is unchanged; the coupling coefficient is
  the supertrace-of-identity.

**Posture against W6 / W10.** W6 / W10 closed
`prob:weighted-rg-locality` *in the negative on bosonic*; W18
opens it *in the positive on super-balanced* (W18-CT1). The
manuscript's bosonic target is preserved; the super-balanced
candidate is a **new genuine theorem possibility on a different
source**.

---

## §3. Heal proposals (smallest first)

### Tier 1 — Statement-only edits

**WP3-W18-1 (W3-W18-03 = W18-CT1 candidate theorem).** In
`appendix-unreduced-bv-qme.tex` after
`rmk:app-scalar-contact-escape-routes` (line 179), inscribe:

> **Theorem candidate `cor:app-super-balanced-qme-vanishing` (super-balanced QME vanishing).**
> On the super-stacked $\mathfrak{gl}(N|N)$ Dirac probe source
> with $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I)=0$, the mixed
> brane-defect QME obstruction class
> $[\hbar\,\mathrm{Str}(I)\,\bar c]
>   \in H^1(\mathcal O_{\mathrm{loc}}(\mathcal E_w),Q+\{I_0,-\})$
> of `prob:weighted-rg-locality` vanishes at one loop, with
> coefficient $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I)=N-N=0$. The
> generalization to $\mathfrak{gl}(N|M)$ gives coefficient
> $\hbar(N-M)[\bar c]$, vanishing iff $N=M$. **This is not the
> manuscript's target source (M-13: bosonic $\mathfrak{gl}_N$
> Dirac probe);** it is a different brane theory with anti-branes,
> consistent with BCOV anti-brane / tachyon-condensation physics.

**WP3-W18-2 (W3-W18-06 = M-31 sharpening).** Sharpen the M-31
ledger entry with one additional sentence (after line 1641 of
`attack-heal-platonic-2026-04-28.md`):

> "Under the $\mathfrak{gl}(N|M)$ supertrace deformation,
> M-31's identification generalizes to
> $[\mathrm{Str}\,\psi]_{\mathrm{BV}}\leftrightarrow(N-M)[\bar c]_{\mathrm{CE}}$.
> The bosonic case ($M=0$) carries the full anomaly $N$; the
> super-balanced case ($M=N$) has zero coefficient. The structural
> identification is preserved; the coefficient is the
> supertrace-of-identity, generalizing the trace-of-identity."

**WP3-W18-3 (W3-W18-04 character escape resolution).** In
`rmk:app-scalar-contact-escape-routes` line 175 (after the
character mention), append a clarifying parenthetical:

> "The central-character escape (ii) is informationally
> equivalent to the Capelli/Weyl normalization
> (`lem:capelli-renormalized-stable-trace`): the
> $\hbar$-deformed character $\chi_\hbar$ absorbing $\hbar N$
> coincides with the Capelli counterterm. This route is
> therefore not a new vanishing-class brane model; it is a
> renaming of the existing Capelli normalization."

**WP3-W18-4 (W3-W18-05 unreduced-primitive escape conjecture).**
In `open-obligations.tex` (or in
`rmk:app-scalar-contact-escape-routes` after line 176), inscribe:

> "**Conjecture `conj:unreduced-primitive-factorization-theory`
> (Phase-4).** There exists a parallel Costello-RG factorization
> theory on the unreduced polynomial Hamiltonian algebra
> $\mathfrak h_{\mathrm{poly}}=\C[z_1,z_2]$ (with the constant
> line retained), in which the primitive $\eta(f)=-[f]_0$
> realizes $\delta\eta=\omega$ at the chain level, and the mixed
> brane-defect QME obstruction class is exact. The construction
> is not obtained by descent from the reduced source $\bar A$
> (which would forbid $\eta(1)=-1\neq 0$); it requires a
> categorical reformulation outside the present manuscript's
> scope. The bi-infinite parent residuals R-W4-A, R-W4-B, R-W4-C
> are sub-pieces of this conjecture."

### Tier 2 — Cross-link with existing entries

**WP3-W18-5 (W3-W18-01 audit / R-W2-C closure).** In
`theorem-lanes.tex` Lane 2 (Stable trace and one-$\psi$ PBW
shadow), append to the *Residuals* paragraph:

> "The PBW shadow has Symp-equivariant **labels** (the bijection
> $e^{\mathrm{PBW}}_{k,l}\leftrightarrow[\Psi_{k,l}]$ is
> Symp-natural via M-35), but its symmetric raising action
> $(pb-qa)$ is $GL_2\times T^2$-equivariant only. The Matlis-
> dual cotangent module
> (`thm:principal-part-coadjoint-uniqueness`) is the
> Symp$_{\mathrm{form}}$-canonical realization of the same
> labels; the polynomial PBW representative is a *symmetric
> raising shadow*, not a coadjoint module. This asymmetry is
> the Symp-equivariance gap recorded in R-W2-C."

### Tier 3 — Architectural cross-link

**WP3-W18-6 (W18-CT1 cross-volume cross-check).** Optional
remark in `principles.tex` Witten subsection or in Theorem G
area:

> "On a super-stacked Dirac probe with $N$ branes and $M$
> anti-branes, the U(1) anomaly coefficient generalizes from
> the bosonic $\hbar N$ to $\hbar(N-M)$. At super-balance ($M=N$),
> the anomaly vanishes — consistent with Sen tachyon
> condensation in BCOV / topological B-model on Calabi-Yau
> threefolds. This is a Phase-3 / Phase-4 outlook; the present
> manuscript's bosonic target is preserved by the
> $M=0$ specialization."

---

## §4. Residuals after W18

- **R-W3-W18-01 (from W3-W18-01).** Theorem B audit complete;
  no new residuals at the theorem level. R-W2-C from W2-06
  preserved (PBW shadow / Matlis cotangent symmetry asymmetry).
- **R-W3-W18-02 (from W3-W18-02).** Dirac brane probe
  correspondence audit complete; no new residuals. The M-31
  trace anomaly direction is the same line viewed from yet
  another side.
- **R-W3-W18-03 (from W3-W18-03).** W18-CT1 super-balanced
  QME vanishing rigorously proved at one loop on the super-stacked
  $\mathfrak{gl}(N|N)$ source; **higher-loop / all-order extension**
  requires verifying that the supertrace is preserved by all
  admissible regulators (heat-kernel, Pauli-Villars, Hadamard
  parametrix). Cross-link with W3-W6-04 (regulator-class-canonicity).
  Phase-3 / Phase-4 work.
- **R-W3-W18-04 (from W3-W18-04).** Character escape resolved
  into Capelli normalization; no new residual.
- **R-W3-W18-05 (from W3-W18-05).** Conjecture W18-C3 (parallel
  Costello-RG factorization on $\mathfrak h_{\mathrm{poly}}$);
  Phase-4. Sub-pieces R-W4-A, R-W4-B, R-W4-C from W4.
- **R-W3-W18-06 (from W3-W18-06).** M-31 sharpening under
  supertrace deformation; no new residual at the structural
  level. Super-balanced specialization is the new candidate
  theorem.
- **R-W3-W18-07 (from W3-W18-07).** Physical embedding of the
  super-balanced $\mathfrak{gl}(N|N)$ source into BCOV /
  topological B-model on Calabi-Yau threefolds; cited Sen 1998 /
  Witten 1998 from memory; rigorous B-model anti-brane
  apparatus is Phase-3 / Phase-4.

---

## §5. Convergence verdict

**Theorem B (audit, T1+T2): VALID, structurally honest.** The
correspondence $Q\psi=[\phi_1,\phi_2]\leftrightarrow
\mu_\epsilon=-\mathrm{Tr}(\epsilon[\phi_1,\phi_2])$ is the
classical / BV pair; the M-31 trace anomaly direction is the
same anomaly line viewed yet again. PBW shadow / Matlis cotangent
asymmetry recorded in R-W2-C. **Verdict: VALID, audit complete.**

**Supertrace escape route (T3 + T6 + T7-CT1): RIGOROUS CANDIDATE
THEOREM.** The W18-CT1 super-balanced QME vanishing is rigorous
in reach at one loop; higher-loop / all-order is Phase-3/4. M-31
generalizes with coefficient $(N-M)$; super-balanced $N=M$ gives
zero coefficient, consistent with BCOV anti-brane physics.
**Verdict: CANDIDATE-THEOREM W18-CT1, rigorous proof in reach.**

**Central-character escape route (T4): RESOLVED INTO EXISTING.**
The character $\chi_\hbar$ coincides with the Capelli counterterm
(`lem:capelli-renormalized-stable-trace`); the route is
informationally redundant. **Verdict: NO NEW CANDIDATE; resolved
into existing.**

**Unreduced-primitive escape route (T5): CONJECTURAL, PHASE-4.**
The primitive $\eta$ exists on $\mathfrak h_{\mathrm{poly}}$ but
does not descend to $\bar A$. A parallel Costello-RG factorization
theory on $\mathfrak h_{\mathrm{poly}}$ is required; this is
fresh technique, not in scope. **Verdict: CONJECTURE W18-C3,
Phase-4.**

**M-31 (T6): SHARPENED.** Generalizes to coefficient $(N-M)$ under
the supertrace deformation; the bosonic case ($M=0$) carries the
full $N$ anomaly. **Verdict: SHARPENED, structural identification
preserved.**

**Stable core (Wave 2 + W6 + W10 + W18).** A, B (audited), C₁ᶠʷ,
C₁ᶜᵒᵐᵖ (bidirectional), C₂(NT), C₂(W)-cl, **C₂(W)-q [obstructed
on bosonic; rigorously closed on super-balanced via W18-CT1]**,
C₂(R), D, E, F, G. The W18 contribution: one genuine new
candidate theorem (W18-CT1) on a different brane source; one
informational redundancy (W18-CT2); one Phase-4 conjecture
(W18-C3); M-31 sharpened with coefficient $(N-M)$.

**Inscribed durables.**
- This document.
- W18-CT1 candidate-theorem remark proposed for
  `appendix-unreduced-bv-qme.tex`.
- M-31 sharpening proposed for
  `attack-heal-platonic-2026-04-28.md`:1612.
- R-W2-C closure remark proposed for `theorem-lanes.tex` Lane 2.
- W18-C3 Phase-4 conjecture proposed for `open-obligations.tex`.

End of W3-W18 ledger.
