# Wave-2 W5 — Polyakov + Invariants lens, cross-volume audit

**Author.** Raeez Lorgat.
**Date.** 2026-04-28.
**Lens.** Polyakov (scaling, renormalization, anomaly, physical
dimension, path-integral sanity) + Invariants (what quantity is
preserved, which step changes it). Mission: audit every cross-volume
correspondence in the local Hamiltonian BF / Dirac brane manuscript.

**Repos in scope.**
- `/Users/raeez/topological-strings/` (current paper).
- `/Users/raeez/calabi-yau-quantum-groups/` (Vol III CY-to-chiral).
- `/Users/raeez/igusa-cusp-form/` (Igusa $\Delta_5$ / BKM).
- `/Users/raeez/chiral-bar-cobar/` (Vol I).
- `/Users/raeez/chiral-bar-cobar-vol2/` (Vol II).

---

## 1. Verification of the no-cross-volume-claim claim

### Method
Searched `main.tex`, every `\input` file (`abstract.tex`,
`claim-strength-ledger.tex`, `local-dictionary.tex`,
`principles.tex`, `theorem-lanes.tex`,
`tate-{T1,T2,T3,T4,T5}-*.tex`, `tate-{P1,P3,P5}-*.tex`,
`appendix-*.tex`, `open-obligations.tex`), every `\bib{...}` entry,
and every `\cite{...}` invocation across the manuscript for any
load-bearing cross-volume reference.

### Result

The only published-volume citations that appear in the bibliography
are `costello-gwilliam` (Vol. I, 2017, CUP) and
`costello-gwilliam-vol2` (Vol. II, 2021, CUP). These are real
published books; they are not the in-progress sibling repos. They are
cited as convention and vocabulary sources for locally constant
factorization and brane data
(`main.tex:2030, 2198`; `tate-T3:421, 448, 467, 542, 553`).

There is exactly **zero** `\cite` to in-progress sibling work
(`calabi-yau-quantum-groups`, `igusa-cusp-form`, `chiral-bar-cobar`,
`chiral-bar-cobar-vol2`).

The string "Vol III" appears only inside firewall remarks declaring
the local theorem **does not** assert a Vol III statement
(`tate-P5-cross-volume.tex:25,43,58–61,94`;
`tate-T1-weighted-completion.tex:818`;
`tate-T4-bv-vanishing.tex:199`;
`tate-P3-universality.tex:155,164,198`;
`open-obligations.tex:191`;
`main.tex:5894,5911`).

The string "Igusa" appears only as a non-asserted item in the same
firewall remarks. Same for "BKM" and "Borcherds".

The single dangling artifact `frontier_mnop_framing_volume.tex`
(which does mention Vol III concretely, including `\path{...}`
references to Vol III chapter files) is a **standalone file** with no
`% !TEX root = main.tex` and no `\input{frontier_mnop_...}` anywhere
in `main.tex` or the `Makefile`. It is not built into the manuscript.
Recommended cleanup: move to `reconstitution/` or `archive/` so an
auditing reader cannot mistake it for bound material.

### Verdict
The claim "no cross-volume claim is used in this paper" is **true** as
stated, contingent on the firewall remarks remaining in the rendered
PDF and on the dangling frontier file not being silently linked. No
load-bearing import. The single in-text reference that gestures
beyond the local model — "BCOV gives the guiding worldsheet example"
(`main.tex:691, 795`) — cites the published BCOV 1993 paper by name,
not any sibling repo.

---

## 2. Convention-checking interface attack

The user's `CLAUDE.md` mandates that conventions
($d=\dim_\C X$, worldsheet $\Sigma$, framing on $S^3$) must agree
across topological-strings and Vol III when stated in both, and that
divergences are load-bearing. I evaluated each.

### 2.1 Holomorphic dimension $d$

**Topological-strings.** The local theorem is at $d=\dim_\C X = 2$,
where $X = \widehat{\C^2}_0 = \mathrm{Spf}\,\C[[z_1,z_2]]$ is the
formal symplectic disk. Stated explicitly in
`tate-P5-cross-volume.tex:14–16`:
"the statement is at $d=\dim_\C X = 2$ and uses the brane line $\R$
as its one-dimensional factorization direction."

**Vol III.** Family parameter $d \in \{1,2,3,5,\ldots\}$. The
two-stage factorization is
$\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}\circ\Phi^{\mathrm{FA}}_d$
with $n_{\mathrm{native}}(d) = \infty,2,1$ at $d=1,2,d\geq 3$ (Vol III
`main.tex:517,1010,1045`). Vol III's "$d=2$" case is K3 / abelian
surface / CY$_2$, **compact**, with reference curve $C \subset X$ a
genuine algebraic curve (Vol III appendix
`conventions.tex:81,376`).

**Divergence (Polyakov scaling).** Both repos use $d=\dim_\C X$, so
the scaling axis agrees. But topological-strings' $X$ is a **formal
neighborhood of a point** (Spf of a complete local ring); Vol III's
$X$ at $d=2$ is a **compact CY surface** (K3). These are not the same
geometric object even though both are at "$d=2$". The local theorem
is the formal-disk specialization of what Vol III's $\PhiFA_2$ would
restrict to on the formal completion at a smooth point of K3. This
specialization is **not asserted** anywhere in topological-strings;
the firewall remark `lem:no-formal-disk-transfer` explicitly denies
it.

Status: convention compatible (same $d$, same complex-dimension
counting); local model is stricter than Vol III's $d=2$ case.
Disclaimer is already in place
(`tate-P5-cross-volume.tex:56–76`).

### 2.2 Worldsheet $\Sigma$

**Topological-strings.** Ambient space-time is $\R^2\times\C^2$
(`main.tex:74-75`), with a defect world-line $\R\times p$ inside.
The transverse data is one real line of "topological time"
(the $\R^2$ factor; only one of the two real directions plays the
factorization-axis role) and the formal holomorphic disk
$\widehat{\C^2}_0$. Effective worldsheet of the brane defect: the
brane-line $\R$ (one-dimensional, real). No closed Riemann-surface
worldsheet, no $S^3$, no $K3\times E$, no compact curve.

**Vol III.** At $d=2$ the specialization curve $\Sigma_1\subset X$ is
a **real $1$-cycle realized as a genuine curve in the CY$_2$ target**,
not a topological circle in configuration space (Vol III
`main.tex:526`). For K3 this is the Nakajima cycle
$\Sigma_1^{\mathrm{Nakajima}}$ realizing the K3 Hilbert scheme as
factorization homology. The reference curve $C$ is then a Riemann
surface inside K3.

**Divergence (Polyakov path-integral sanity).** Topological-strings'
brane line $\R$ and Vol III's $\Sigma_1\subset K3$ are **categorically
distinct**: one is a topological time line for a defect probe, the
other is an algebraic curve carrying a chiral algebra. They are not
candidates for the same "worldsheet" datum. The local theorem
deliberately omits the ambient Riemann surface story; Vol III is built
on it. This is the load-bearing divergence — and the manuscript
already records it.
`appendix-factorization-current-conventions.tex` (which I confirmed by
read) and `tate-T1-weighted-completion.tex:818–830` carry the
no-transfer guarantee.

Status: divergent worldsheet conventions, divergence already firewalled.

### 2.3 $S^3$ framing

**Topological-strings.** $S^3$ framing is **not used** as a hypothesis
or theorem ingredient anywhere in `main.tex`. The single mention is
`main.tex:1591` listing it among absent global data. The brane
$\R\times p$ is not $S^3$; there is nothing to frame.

**Vol III.** $S^d$-framing is central. At $d=2$ the
Kontsevich–Vlassopoulos $\bS^2$-framing rigidifies $\Phi_2$ (Vol III
`main.tex:545,1239`). At $d=3$ the $S^3$-framing question is the
$[m_3, B^{(2)}]$ obstruction (Vol III `cy_to_chiral.tex:400, 2830`).
For the quintic Lagrangian the relevant Hirzebruch
$\sigma$-invariant is in $\pi_3(SO(3))=\Z$
(see the dangling `frontier_mnop_framing_volume.tex:155–171`, **not in
the built manuscript**).

**Divergence.** Topological-strings has no $S^3$ to frame; the
question is mute on the local side. Vol III's $S^3$-framing applies
at $d=3$, not at $d=2$. The user's CLAUDE.md raises this as a
convention to match — and the answer is: there is nothing to match
because the local model lives at $d=2$ on a formal disk where no
relevant $S^3$ exists. The firewall remark
(`tate-P5-cross-volume.tex:71`) lists "an $S^3$ framing" among the
absent global data.

Status: not applicable to the local theorem; firewall correctly
records absence.

### 2.4 Trace pairing / negative-cyclic CY class

**Topological-strings.** No CY trace pairing. The closed sector is
Hamiltonian BF on the formal disk; there is no compact CY pairing in
negative cyclic homology, no $\Omega_X$ trivialization of $K_X$, no
Mukai-style compact pairing.

**Vol III.** The CY$_d$ pairing in negative cyclic homology is a
foundational input to $\PhiFA_d$ at $d\geq 2$ (Vol III
`cy_to_chiral.tex:400`).

Status: divergent; firewall in place.

### 2.5 BV degree / Gerstenhaber bracket convention

**Topological-strings.** $P_0$-shifted Poisson centre target
(`principles.tex:65–66, 89–96`). The shifted cotangent Lie algebra is
$\mathfrak g = \mathfrak h \ltimes \mathfrak h^\vee_{\mathrm{cont}}[1]$
with the $[1]$ shift on the cotangent factor. The closed CE/PV
identification reads as a $P_0$-derived-centre statement.

**Vol III.** Gerstenhaber bracket on $\HH^\bullet(\cC)$ has degree
$1-d$ (Vol III `main.tex:970,989,1001` and
`cy_to_chiral.tex:379`). At $d=2$ the bracket has degree $-1$ — i.e.
the local model is in a $P_2$-Poisson world (one degree higher than
the topological-strings $P_0$ target on the same formal disk).

**Divergence (Polyakov scaling, BV degree).** Topological-strings
proves a $P_0$ derived-centre theorem. Vol III's $\Etwo$-chiral
output at $d=2$ has a $P_1$-Poisson Koszul-dual (degree-$-1$
bracket). They live in **different operadic-degree windows** because
they answer **different questions**: topological-strings asks for the
derived Poisson centre of the brane-line factorization algebra (a
mechanical shifted-cotangent centre, $P_0$); Vol III asks for the
$E_2$-chiral object on a curve specialization
(Schouten–Nijenhuis-bracketed Hochschild, $P_1$). Both are correct;
they just are not the same target.

Status: degree-shift divergence, load-bearing for any matched-conventions
theorem, not asserted in either repo; firewall correct.

### 2.6 Koszul direction

**Topological-strings.** Bar-cobar in `lem:continuous-bar-cobar`
(`main.tex:3323–3437`): Lie bar–cobar
$\Omega C^{\mathrm{CE}}_*(\mathfrak g)\to\widehat U(\mathfrak g)$ is
an admissible filtered quasi-isomorphism in $\Cat{TateVec}$, with
PBW filtration on $\widehat U(\mathfrak g)$ and conilpotency
hypothesis on $\mathfrak g$.

**Vol I/II (chiral bar-cobar).** Different mathematical object: the
geometric bar coalgebra $\barB_X(\cA) = \mathrm{Sym}^c(s^{-1}\bar\cA)$
on $\mathrm{Ran}(X)$, three-component differential
$d_{\mathrm{int}} + d_{\mathrm{res}} + d_{\mathrm{deRham}}$,
$\Omega\circ\barB \xrightarrow{\sim}\mathrm{id}$ on the Koszul locus
(Vol I `chapters/theory/bar_construction.tex:1–80`). Vol II adds
`thm:verdier-bar-cobar` (Verdier duality on Ran intertwining bar and
cobar).

**Divergence.** These are **different statements about different
objects**. Topological-strings' bar-cobar is a Lie / completed-PBW
statement at the level of Tate vector spaces. Vol I/II's chiral
bar-cobar is a chiral coalgebra / factorization statement on
$\mathrm{Ran}(X)$ with a specific three-piece differential. They are
**compatible in spirit** (both invert bar by cobar with appropriate
conilpotency / Koszul hypotheses), but the topological-strings statement
is **not** a special case of the chiral version, nor vice versa.
The shared notation is benign; the underlying categories differ.

Status: parallel statements in different categories; neither is
imported by the other. The topological-strings statement is
self-contained for the formal Hamiltonian disk.

### 2.7 Matlis / residue convention

**Topological-strings.** Continuous cotangent module is the reduced
Matlis residue current module $\mathcal P =
\mathrm{Ann}(\C\cdot 1) \subset H^2_{\mathfrak m}(R)\,dz_1dz_2$
(`principles.tex:166–180`, `local-dictionary.tex:143–164`). Coadjoint
action lowers indices.

**Vol III / Igusa.** Neither repo uses Matlis residue currents on a
formal disk in this role. Vol III's continuous cotangent setup runs
through the holomorphic CY pairing in negative cyclic homology, not
through Grothendieck local cohomology of a complete local ring.

Status: convention native to the local model, no parallel claim
elsewhere.

### 2.8 Scalar reduction and U(1) anomaly

**Topological-strings.** The scalar U(1) anomaly is a one-dimensional
class $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$ (Lemma
`lem:omega-cocycle`, Theorems
`thm:u1-center-anomaly`, `thm:u1-center-anomaly-open`,
`thm:quantum-classical-anomaly`). The class is realized on the closed
side as the cocycle $\omega(f,g) = [\{f,g\}]_0$ and on the open side
as the U(1) center of $\mathfrak{gl}_N$ with character $\mathrm{Tr}$.
Quantum incarnation is the Capelli/Weyl shift $\hbar N$.

**Vol III.** Vol III does not state a one-dimensional U(1)/Capelli
scalar anomaly class in this form. It does discuss central scalar
terms in matrix-like settings
(`cy3_chain_level_bridge.tex:2023`, `e1_chiral_algebras.tex:2507`),
but these are different objects (Schur central scalars; Yangian
$\hbar/z$ central terms in $R$-matrices). Vol III's modular
characteristic $\kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}$
constants are **not** the topological-strings $[\bar c]$ class.

**Igusa.** Igusa repo has a `lem:b-cocycle-central-extension` and
discusses central extensions of abelian groups by 2-cocycles
(`main.tex:4170–4216`). This is a Borcherds-lattice central extension
controlling the Weyl-chamber pentagon, not a Hamiltonian Poisson
$U(1)$ anomaly. Different physics, different mathematics.

**Vol I/II.** `conformal_anomaly_rigidity_platonic.tex` exists in
Vol I; this is conformal/$c$-anomaly rigidity, not the Capelli U(1)
class.

Status: the topological-strings $[\bar c]$ class is **native to the
local model**. No analog in the other repos shares its precise
statement. The user's mission asked: "where does an analog of the
Theorem G anomaly class appear in the other repos?" Answer: nowhere
in the form proved here. The Igusa $B$-cocycle, Vol III Yangian
central scalars, and Vol I conformal anomaly are all different
classes, and no comparison morphism is asserted.

### 2.9 Large-N

**Topological-strings.** Stable large-$N$ limit:
$\lim_{N\to\infty}\mathcal A_N \simeq \mathcal B^!$
(`main.tex:493`); but the manuscript labels this as **conjectural**
(`main.tex:494, 498`). The all-$N$ radial-parts comparison is one of
the named open obligations. The Capelli shift $\hbar N$ depends on
$N$.

**Vol III.** Large-$N$ does not enter as a primary parameter; Vol III
parameterizes by the CY data and the operadic level $n(d)$.

Status: large-$N$ is a topological-strings-internal axis; not a
cross-volume convention.

### 2.10 Igusa $\Delta_5$ generating-function bridge

The user asked: is there a concrete generating function in
topological-strings that should match an Igusa denominator formula?

**Searched.** The Igusa repo's headline equation is
$\mathrm{den}(\mathfrak g_{\Delta_5}) = 64^{-1}\Delta_5(2Z)$
(Igusa `main.tex:90–91, 277, 346`), and the OP/DT amplitude on
$K3\times E$ is $-4096\,\Delta_5^{-2}$
(`main.tex:101, 297, 341`). Both are **compact-CY$_3$-on-$K3\times E$**
statements with a Borcherds product and a Hall orientation.

**Topological-strings concrete generating functions.** The local
manuscript computes:
- Capelli/Weyl Moyal coefficients $C^{a,b}_{(p,q),(r,s)}$ to stated
  order (e.g. `main.tex:2522` lists $C^{1,1}_{(2,0),(0,2)}=4$ and
  related).
- The first and third Costello graph normalizations (computed to
  stated order).
- The PBW/Matlis Fourier-Rees bridge factor
  $(-1)^{a+b}\hbar^{a+b}a!b!$
  (`local-dictionary.tex:79–88`).

**Comparison.** None of these is a candidate generating function that
should match $\Delta_5$, $\Delta_5^{-2}$, $\chi_{10}$, or any
Borcherds denominator. They live in completely different settings:
the topological-strings coefficients are local-disk Moyal/graph
numbers; the Igusa generating functions are global automorphic forms
on the Siegel period. There is no concrete coefficient matching to
attempt.

**Verdict.** The plan §9 statement that "modular-form frontier
comparison with Igusa is heuristic" is correct. There is no
generating function in topological-strings that should match an Igusa
denominator at the present level of statement. The would-be bridge
requires the matched-conventions theorem template
(Igusa/BKM template, `tate-P5-cross-volume.tex:108–115`). That
theorem is not proved, not asserted, and not used.

Status: heuristic-only bridge; firewall correct.

---

## 3. Conventions ledger

| Convention | Topological-strings | Vol III (CY-to-chiral) | Vol I (chiral bar-cobar) | Vol II (chiral bar-cobar) | Igusa $\Delta_5$ |
|---|---|---|---|---|---|
| Holomorphic dim $d$ | $d=2$, $X=\widehat{\C^2}_0$ formal disk | $d\in\{1,2,3,5,\ldots\}$, compact CY$_d$ | curve-level (varies) | curve-level | $d=3$ on $K3\times E$ |
| Worldsheet | brane line $\R\times p$ in $\R^2\times\C^2$ | $\Sigma_{d-1}\subset X$ + ref. curve $C\subset X$ | $\mathrm{Ran}(X)$ on a curve $X$ | $\mathrm{Ran}(X)$ on a curve $X$ | period domain $\mathbb H_2$ |
| Framing | none used | $\bS^d$-framing canonical | none | none | none |
| Trace pairing | none | CY$_d$ negative-cyclic | none load-bearing | none load-bearing | Borcherds product |
| BV / bracket degree | $P_0$ centre, shifted-cotangent $[1]$ | Gerstenhaber degree $1-d$ | $E_n$-bar with internal/residue/dRham | Verdier-twisted | n/a |
| Koszul direction | Lie bar–cobar in $\Cat{TateVec}$ | $E_d$-bar–cobar adjunction | chiral coalgebra on $\mathrm{Ran}$ | Verdier bar–cobar | source bar of hybrid object |
| Matlis / residue | $\mathcal P\subset H^2_{\mathfrak m}$ | not used in this role | not used | not used | not used |
| Scalar / U(1) anomaly | $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A)$, Capelli $\hbar N$ | no parallel single-class statement | conformal $c$-anomaly | conformal $c$-anomaly | $B$-cocycle on Borcherds lattice |
| Large-$N$ | conjectural stable limit | not primary | n/a | n/a | n/a |

**Divergences flagged.**
1. Worldsheet (R-line vs algebraic curve in CY$_d$) — load-bearing,
   firewalled.
2. BV/Poisson degree ($P_0$ vs $P_{1}$ at $d=2$) — load-bearing,
   firewalled.
3. Trace pairing (none vs CY$_d$) — load-bearing, firewalled.
4. Scalar U(1) anomaly class — native to topological-strings, no
   counterpart elsewhere; not a convention divergence but a class
   that does not transfer.
5. Bar-cobar (Lie / Tate vs chiral / Ran) — different categories,
   parallel, neither imports the other.

**No silent reconciliations identified.** Every divergence is either
explicitly named in `tate-P5-cross-volume.tex`, the convention firewall
remarks, or the open-obligations list.

---

## 4. Recommended cross-volume disclaimers

The existing firewall material is sufficient to prevent
load-bearing cross-volume claims, but two cleanups would harden the
audit:

1. **Move or archive `frontier_mnop_framing_volume.tex`.** This file
   sits in the repo root and contains explicit `\path{...}` references
   to Vol III chapter files. It is not built into the manuscript, but
   a casual reader walking the repo could read it as bound material.
   Move to `reconstitution/dangling-frontier-2026-04-28-mnop-framing.tex`
   or to a marked-archive subdirectory.

2. **Pin the local-disk vs Vol III $d=2$ distinction.** The current
   firewall says "no Vol III theorem is asserted here." Strengthen to
   note: the local theorem is proved on the formal completion at a
   smooth point of a $d=2$ CY, while Vol III's $d=2$ statement
   $\Phi_2(D^b\Coh(K3))$ is a compact-K3 statement; the local
   manuscript gives the formal-disk normalization that any Vol III
   matched-conventions theorem at $d=2$ must restrict to, but does not
   claim to be a $\PhiFA_2$ specialization without that matched
   theorem. This is a one-sentence sharpening of
   `lem:no-formal-disk-transfer`.

Both are editorial improvements; neither is a defect.

---

## 5. Verdict

**Cross-volume claims used in the manuscript:** **None**, in the
load-bearing sense. Confirmed by exhaustive search.
**Allowed-use claims:** the BCOV 1993 published paper is cited as
source convention; Costello–Gwilliam Vol. I and Vol. II (2017, 2021)
are cited for vocabulary and locally constant factorization; these are
real published references and are not the in-progress sibling repos.
**Firewall integrity:** intact. `tate-P5-cross-volume.tex`
(`app:convention-contract`) discharges every cross-volume obligation
by explicit non-assertion plus the matched-conventions theorem
template.
**Convention divergences:** five distinct divergences identified
(worldsheet, BV degree, trace pairing, anomaly class type, bar-cobar
category), every one of them already firewalled and none silently
reconciled.
**Recommended actions:** (a) move the dangling frontier file out of
the repo root; (b) sharpen `lem:no-formal-disk-transfer` by one
sentence to pin the local-disk vs compact-K3 distinction at $d=2$.

The Polyakov + Invariants lens finds no path-integral pathology, no
hidden scaling violation, and no preserved-quantity collision between
the local theorem and any sibling-volume statement. The manuscript
is, by every test I applied, free of cross-volume overreach.

---

## Ledger entries (W5)

- **W5-01.** Verified bibliography contains zero in-progress-sibling
  citations; only published Costello–Gwilliam Vol. I/II appear.
  Severity: confirmation, not a defect.
- **W5-02.** Worldsheet divergence (R-line vs $\Sigma_1\subset K3$):
  load-bearing, firewalled. Severity: structural divergence,
  correctly recorded.
- **W5-03.** BV / Poisson-degree divergence ($P_0$ vs $P_1$ at $d=2$):
  load-bearing, firewalled. Severity: operadic-level divergence,
  correctly recorded.
- **W5-04.** Trace-pairing divergence (none vs CY$_d$ negative-cyclic):
  load-bearing, firewalled.
- **W5-05.** Scalar U(1) anomaly $[\bar c]$ has no counterpart in Vol
  III, Vol I/II, or Igusa with the same statement; not a convention
  divergence but a class that does not transfer. Severity: identifies
  a genuine open transfer obligation if a sibling volume ever wants
  to import it.
- **W5-06.** Bar-cobar in different categories (Tate-Lie vs
  chiral-Ran). Severity: low; both are correct in their respective
  categories; topological-strings does not import the chiral version.
- **W5-07.** Igusa $\Delta_5$ generating functions and topological-strings
  Moyal/Capelli coefficients are in different settings; no concrete
  matching to attempt without the Igusa/BKM matched-conventions
  template. Severity: confirms the heuristic-only nature of the
  bridge.
- **W5-08.** $S^3$ framing not used in topological-strings; firewall
  correctly lists it as absent global data. Severity: confirmation.
- **W5-09.** `frontier_mnop_framing_volume.tex` is a dangling
  artifact in the repo root containing explicit Vol III references;
  not built into the manuscript. Severity: editorial; recommend
  archive move.
- **W5-10.** $d=\dim_\C X = 2$ is uniformly used in both repos for the
  complex-dimension counting, but the geometric object behind $d=2$
  differs (formal disk vs compact K3). The firewall records this;
  recommend a one-sentence sharpening of
  `lem:no-formal-disk-transfer`. Severity: editorial.

End W5 ledger.
