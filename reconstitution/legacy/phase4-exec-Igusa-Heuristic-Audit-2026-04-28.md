# Phase-4 EXEC P4-Igusa-Heuristic-Audit — Polyakov+Invariants audit of the Igusa $\Delta_5$ / BKM heuristic cross-volume bridge

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Polyakov + Invariants. The Polyakov question is "what
generating-function symmetry does the (A5) machinery actually realise?
What is the modular partition?" The Invariants question is "which
representation-theoretic invariant gets mapped on each side, and what
external choices (lattice basis, polarisation, regulator) does the
matching require?"
**Mode.** Proposal-only. NO git commits, NO TeX edits. Cross-volume
read of `~/igusa-cusp-form` is permitted (read-only). Audit lives at
this path ONLY.
**Mandate.** Audit the explicit CLAUDE.md framing — *"Modular-form
frontier: generating functions in topological-string theory motivate
comparison with the Igusa cusp form $\Delta_5$ construction in
`~/igusa-cusp-form` via the Borcherds / BKM route. **This is a
heuristic and convention-checking bridge here, not a BKM consequence
of the local Hamiltonian BF/Moyal calculation.**"* Decompose the
heuristic into structural conditions $X$, classify each $X$ as
*currently met / partially met / unmet*, and tag each unmet $X$ as
*Phase-5* or *firewall-permanent*.

**Inputs (loaded prior to mathematical reasoning).**
- `CLAUDE.md` (topological-strings, lines 22 + lines 7–24) — the
  bridge statement and the cross-volume firewall paragraph.
- `~/igusa-cusp-form/CLAUDE.md` (47 lines) — Igusa repository's
  research-constellation framing.
- `~/igusa-cusp-form/main.tex` (read in 200-line slices; see anchored
  line ranges below).
- `reconstitution/phase4-exec-A5-anomaly-ledger-2026-04-28.md` (1162
  lines) — twelve load-bearing constants L1–L12; the anomaly class
  $\hbar\,\mathrm{Str}(I)\,[\bar c]$ on $\bar A$.
- `reconstitution/phase4-exec-BCOV-A5-comparison-2026-04-28.md` (1093
  lines) — established firewall topology to BCOV; coefficient layer
  liftable, chain-level layer permanent.
- `reconstitution/phase4-exec-W30-M2-regulator-branches-2026-04-28.md`
  (830 lines) — four-regulator audit (R1) heat kernel, (R2)
  point-splitting, (R3) dim reg, (R4) Hadamard; all agree on $[\bar
  c]$.
- `reconstitution/phase4-exec-reduced-primitives-catalog-2026-04-28.md`
  — five candidate reduced-only primitives all fail; the residue
  $\hbar N[\bar c]$ is genuinely cohomologically non-trivial.
- `main.tex` 5380–5394 (`rmk:convention-firewall`) — explicit
  exclusion of Igusa / Borcherds / BKM transfer.
- `main.tex` 5894–5915 (`ssec:cross-volume-horizon`) — cross-volume
  firewall section; explicit Igusa cusp-form, $K3 \times E$, BKM
  exclusion.

**Primary external sources cited (and the role each plays).**
- J.-i. Igusa, "On Siegel modular forms of genus two", *Amer. J. Math.*
  **84** (1962), 175–200 — the genus-two Siegel modular form ring,
  $M^{\rm even}_*(\Sp_4(\Z)) = \C[E_4, E_6, \Delta_{10}, \Delta_{12}]$;
  the weight-$10$ form $\Delta_{10}$ and its square root $\Delta_5$
  with the Maass character $\nu_{\Delta_5}$.
- R. Borcherds, "Automorphic forms with singularities on
  Grassmannians", *Invent. Math.* **132** (1998), 491–562 — the
  Borcherds product machine; theta lifts of weak Jacobi / vector-valued
  modular forms produce automorphic infinite products on orthogonal
  Shimura varieties; the singular-theta correspondence.
- V. Gritsenko, V. Nikulin, "Siegel automorphic form corrections of
  some Lorentzian Kac–Moody Lie algebras", *Amer. J. Math.* **119**
  (1997), 181–224 — BKM reformulation of $\Delta_5$ as the
  denominator function of a generalised Kac–Moody algebra
  $\mathfrak g_{\Delta_5}$ with explicit Cartan matrix
  $\bigl(\begin{smallmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{smallmatrix}\bigr)$
  on three real simple roots.
- R. Dijkgraaf, E. Verlinde, H. Verlinde, "Counting dyons in $N=4$
  string theory", *Nucl. Phys.* **B484** (1997), 543–561 — the dyon
  partition function $1 / \chi_{10}$ on type-II / heterotic on $K3
  \times T^2$; the physics motivation linking $\Delta_{10} = \Delta_5^2$
  to BPS state counting.
- M. Bershadsky, S. Cecotti, H. Ooguri, C. Vafa, *Comm. Math. Phys.*
  **165** (1994), 311–427 — the closed B-model on a compact Calabi–Yau
  threefold; holomorphic anomaly equation §6, Eq. (6.10)–(6.12).
- K. Costello, S. Li, "Quantum BCOV theory" arXiv:1201.4501 (2012),
  "Quantization of open–closed BCOV theory I" arXiv:1505.06703
  (2015), "Anomaly cancellation in the topological string"
  arXiv:1605.09073 (2016) — chain-level rigorous BCOV.
- R. Borcherds, "Monstrous moonshine and monstrous Lie superalgebras",
  *Invent. Math.* **109** (1992), 405–444 — the original BKM /
  no-ghost theorem for the Monster.

---

## §0. Executive verdict

**Three-line bottom line.**

1. **The Igusa $\Delta_5$ / BKM heuristic firewall is structurally
   weaker than the BCOV / Vol III firewall, but it is currently
   FIREWALL-PERMANENT at every load-bearing layer.** No generating
   function in the manuscript, including the (a, b)-bigraded
   one-$\psi$ Koszul homology lattice, the column-Verma lattice, the
   $T_{a,b}$ trace lattice, and the active-support lattice of the
   Capelli triangular system, possesses an Sp$_4(\Z)$ modular
   action; the (A5) parity-equivariance is a $\Z/2$-symmetry, not a
   modular symmetry. The lattices on the two sides are dimensionally
   incompatible ($\Z^2$ on our side; the type-II hyperbolic lattice
   $\Lambda^{2,1}_{II} = \HypPlan \oplus [2]$ on the Igusa side).
   The CLAUDE.md framing is correct: the bridge is *heuristic and
   convention-checking only*, not a BKM consequence.

2. **The (A5) parity-equivariance hypothesis does NOT lift to
   Sp$_4(\Z)$ modular invariance.** (A5) is a $\Z/2$ structural
   symmetry of the matrix source $\mathfrak{gl}(N|N)$; Sp$_4(\Z)$ is
   the arithmetic symmetry of the genus-two Siegel upper half-space
   $\mathbb H_2$. The two symmetries act on different objects — (A5)
   on the parity grading of the colour algebra; Sp$_4(\Z)$ on the
   period vectors of an automorphic form. There is no induced action
   of Sp$_4(\Z)$ on $\mathfrak{gl}(N|N)$ from any structure currently
   inscribed in the manuscript. The Igusa heuristic firewall is
   permanent at the *modular-invariance layer*.

3. **There is no smallest computational test that necessarily
   matches.** Unlike BCOV, where the Costello–Li 2015 / 2016
   open-closed flat $\C^d$ formulation provides a partial firewall
   lift via the shared coefficient $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I)
   = N - M$, the Igusa side has no analogous chain-level partial
   lift on a smaller spacetime. The BKM denominator algebra
   $\mathfrak g_{\Delta_5}$ is an algebraic object whose structure
   constants are signed root multiplicities $\smult \mathfrak
   g_{\Delta_5,\alpha(n,l,m)} = f(nm,l)$; our model produces no
   generating function with these multiplicities and no embedding of
   a subset of the colour algebra into the BKM root system. The
   smallest hypothetically-matching test (§6 below) is an *external*
   check on the pair $(\Lambda^{2,1}_{II}, W^{(2)}(\Lambda^{2,1}_{II}))$
   — not any quantity computable from the local Hamiltonian BF /
   Moyal data.

**One-line invariant.** No invariant currently inscribed in the
manuscript transports across the Igusa heuristic firewall. The
Polyakov question — "what generating-function symmetry survives?" —
returns `null` on every candidate generating function tested. The
Invariants question — "which lattice gets mapped?" — returns "no
lattice morphism" on the (a, b)-bigrading vs. the type-II hyperbolic
lattice.

**Classification of the firewall lift conditions $X_1, \ldots, X_5$
(detailed in §3 / §4):**

| Condition | Status | Phase-5 vs Permanent |
|---|---|---|
| $X_1$ matched-conventions functor (Igusa BV / chiral $\leftrightarrow$ ours) | UNMET | FIREWALL-PERMANENT (no Igusa side BV exists) |
| $X_2$ regulator-class compatibility | UNMET | OPEN-LITERATURE (no chain-level Igusa regulator inscribed) |
| $X_3$ Sp$_4(\Z)$ modular-invariance hypothesis on (A5) | UNMET | FIREWALL-PERMANENT at current resolution |
| $X_4$ lattice morphism $(a, b)$-bigrading $\to \Lambda^{2,1}_{II}$ | UNMET | FIREWALL-PERMANENT (dimension mismatch, signature mismatch) |
| $X_5$ duality (T / S) inducing Sp$_4(\Z)$ from physical structure | UNMET | PHASE-5 (requires construction of N=4 / closed-B-model bridge) |

**Bottom line.** The manuscript is correct to inscribe the Igusa
firewall in `rmk:convention-firewall` (`main.tex`:5380–5394) and
`ssec:cross-volume-horizon` (`main.tex`:5894–5915). No load-bearing
revision is required.

---

## §1. $\Delta_5$ / BKM canonical statement

### 1.1. Igusa $\Delta_5$ as a Siegel modular form

The Igusa form $\Delta_5$ is the unique (up to scalar) cusp form of
weight 5 on $\Sp_4(\Z)$ with Maass character $\nu_{\Delta_5}$
(`~/igusa-cusp-form/main.tex`:2185–2225). Its square is the
weight-10 scalar Igusa cusp form $\Delta_{10}$ which generates the
even scalar subring
\[
M^{\rm even}_*(\Sp_4(\Z)) \;=\; \C[E_4, E_6, \Delta_{10}, \Delta_{12}],
\qquad \mathrm{wt}(\Delta_{10}) = 10.
\]
The transformation law on $\mathbb H_2 = \{Z = \binom{z_1\;z_2}{z_2\;z_3}
\mid \mathrm{Im}\,Z > 0\}$ reads
\[
\Delta_5(g \cdot Z) \;=\; \nu_{\Delta_5}(g)\,\det(CZ + D)^5\,\Delta_5(Z),
\qquad
g = \begin{pmatrix} A & B \\ C & D \end{pmatrix} \in \Sp_4(\Z),
\]
with $\nu_{\Delta_5}: \Sp_4(\Z) \to \C^\times$ the Maass multiplier
of finite order (`~/igusa-cusp-form/main.tex`:2202–2214). The product
of ten even theta constants gives the explicit form
$\Delta_5 = \prod_{(a,b)} \nu_{a,b}$ with the indicated theta
characteristics (`~/igusa-cusp-form/main.tex`:2194–2199).

### 1.2. Borcherds product expansion

In the type-II cusp polarisation $(q, r, s) = (e^{2\pi i z_1}, e^{2\pi
i z_2}, e^{2\pi i z_3})$, the Gritsenko–Nikulin specialisation of
Borcherds' product theorem (Borcherds 1998 + Gritsenko–Nikulin 1997)
gives
\[
D_5 \;=\; 64^{-1} \Delta_5 \;=\; \mathrm{Borch}(\phi_{0,1})
\;=\; q^{1/2} r^{1/2} s^{1/2} \!\!\prod_{(n,l,m) \in
\Gamma_{\rm eff}^+}\!\! (1 - q^n r^l s^m)^{f(nm,l)},
\]
where $\phi_{0,1}(\tau, z) = \sum_{n \geq 0, l \in \Z} f(n,l) q^n r^l$
is the unique (up to scalar) weight-zero index-one weak Jacobi form
on $\SL_2(\Z) \ltimes \Z^2$, with leading expansion
$\phi_{0,1} = r^{-1} + 10 + r + O(q)$
(`~/igusa-cusp-form/main.tex`:1769–1781, 712–713). The active
support $\Gamma_{\rm act} = \{(n,l,m) \in \Gamma_{\rm eff} \mid f(nm,l)
\neq 0\}$ injects into the type-II hyperbolic lattice
$\Lambda^{2,1}_{II} = \HypPlan \oplus [2]$ via
\[
\alpha(n,l,m) \;=\; 2n f_2 - l f_3 + 2m f_{-2}\;\in\;\Lambda^{2,1}_{II},
\qquad
(\alpha(\gamma), \alpha(\gamma)) \;=\; -2(4nm - l^2)
\]
(`~/igusa-cusp-form/main.tex`:5081–5096). The Lorentzian signature is
$(2,1)$.

### 1.3. Gritsenko–Nikulin BKM reformulation

Gritsenko–Nikulin (1997) construct a generalised Kac–Moody algebra
$\mathfrak g_{\Delta_5}$ whose denominator function is
\[
\mathrm{den}(\mathfrak g_{\Delta_5}) \;=\; 64^{-1} \Delta_5(2Z),
\qquad
\smult\,\mathfrak g_{\Delta_5,\alpha(n,l,m)} \;=\; f(nm, l)
\]
on the active support (`~/igusa-cusp-form/main.tex`:282–290). The
real simple roots are $\delta_1 = 2 f_2 - f_3$, $\delta_2 = 2 f_{-2}
- f_3$, $\delta_3 = f_3$ with Gram matrix
\[
((\delta_i, \delta_j)) \;=\; \begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 &
-2 \\ -2 & -2 & 2 \end{pmatrix}
\]
(`~/igusa-cusp-form/main.tex`:5066–5067). The Weyl group
$W^{(2)}(\Lambda^{2,1}_{II})$ is generated by reflections in the
three real simple roots; the Weyl vector is $\rho = \tfrac12(\delta_1
+ \delta_2 + \delta_3) = f_2 - \tfrac12 f_3 + f_{-2}$
(`~/igusa-cusp-form/main.tex`:5064–5068). The chamber decomposition
is $\Aut(\Poly_{II}) \simeq S_3$ generated by $s_{f_2 - f_3}$ and
$s_{f_{-2} - f_2}$ (`~/igusa-cusp-form/main.tex`:4994–4998).

### 1.4. Canonical-form identity

The canonical Igusa $\Delta_5$ / BKM identity invoked by the
heuristic is therefore
\[
\boxed{\;\;
\mathrm{den}(\mathfrak g_{\Delta_5})(Z) \;=\;
e^{-2\pi i (\rho, Z)}
\!\!\prod_{\alpha \in \Lambda^{2,1}_{II,+}}\!\! (1 - e^{-2\pi i (\alpha, Z)})^{\smult \alpha}
\;=\; q^{1/2} r^{1/2} s^{1/2}\!\!\prod_{(n,l,m) \in
\Gamma_{\rm eff}^+}\!\! (1 - q^n r^l s^m)^{f(nm, l)}
\;\;}
\]
with $\smult \alpha(n,l,m) = f(nm,l)$. This is simultaneously a
Borcherds product (Borcherds 1998) and a denominator identity for a
generalised Kac–Moody algebra (Gritsenko–Nikulin 1997).

### 1.5. Dijkgraaf–Verlinde–Verlinde 1997 dyon-counting interpretation

In type-II string theory on $K3 \times T^2$, the BPS dyon counting
function is
\[
Z_{\rm dyon}(Z) \;=\; \frac{1}{\Delta_{10}(Z)} \;=\;
\frac{1}{\Delta_5(Z)^2}
\]
(Dijkgraaf–Verlinde–Verlinde 1997, abstract and §3). The Igusa cusp
form $\Delta_{10}$ is the partition function of the generating index
on a $1/4$-BPS dyon Hilbert space. On the topological-string side,
this emerges as the second-quantised partition function on $K3 \times
T^2$ via the DMVV formula (Dijkgraaf–Moore–Verlinde–Verlinde 1997).
This is the physics origin of the heuristic and the source of the
interpretive bridge in BCOV-style topological strings.

---

## §2. Heuristic correspondence as currently used in CLAUDE.md

### 2.1. The bridge text

CLAUDE.md (`/Users/raeez/topological-strings/CLAUDE.md`:22):

> "Modular-form frontier: generating functions in topological-string
> theory motivate comparison with the Igusa cusp form $\Delta_5$
> construction in `~/igusa-cusp-form` via the Borcherds / BKM route.
> This is a heuristic and convention-checking bridge here, not a BKM
> consequence of the local Hamiltonian BF/Moyal calculation."

### 2.2. Generating-function symmetries on the topological-strings side

The local Hamiltonian BF / Moyal calculation produces several
generating functions, none of which is explicitly modular in the
Sp$_4(\Z)$ sense. Catalogue:

(GF-1) **The Capelli triangular eigenvalues / $T_{a,b}$ basis change.**
The Capelli element $c_2 = \sum_i e_{ii}(e_{ii} + N - i) - \sum_{i<j}
e_{ij} e_{ji}$ has triangular action on the $T_{a,b} = \mathrm{Tr}(X^a
Y^b)$ basis with shift $\hbar N / 2$ (`main.tex`:4790–4801,
`lem:capelli-renormalized-stable-trace`). The generating function is
\[
F^{\rm Cap}(z_1, z_2; \hbar) \;=\; \sum_{a, b \geq 0} T_{a, b}\,z_1^a
z_2^b,
\]
on the bigrading $(a, b) \in \Z_{\geq 0}^2$. *Symmetry:* shift
covariance under the Capelli endomorphism. **No modular symmetry.**

(GF-2) **The one-$\psi$ Koszul homology generating function.**
Proposition `prop:one-psi-homology` (`main.tex`:2927) computes the
primitive one-$\psi$ Koszul homology on the bigraded basis
$\{\widetilde\Psi_{a,b} : a, b \geq 0\}$. The generating function is
\[
F^{\psi}(z_1, z_2) \;=\; \sum_{a, b \geq 0}
\dim_{\C} H^{\rm psi}_{a,b}\,z_1^a z_2^b
\;=\; \sum_{a, b \geq 0} 1 \cdot z_1^a z_2^b
\;=\; \frac{1}{(1 - z_1)(1 - z_2)},
\]
since the homology is one-dimensional in each bidegree
(`main.tex`:3016). *Symmetry:* the $\Z/2$ swap $(a, b)
\leftrightarrow (b, a)$ from $z_1 \leftrightarrow z_2$ exchange and
the (A5) parity-equivariance on the super-stack.

(GF-3) **The column-Verma generating function.** The polynomial
Hamiltonian Lie algebra $\mathfrak h_{\rm poly} = \C[z_1, z_2]$ is
graded by total degree and bidegree. Column-Verma constructions
(reconstitution `phase4-G2-column-verma-symp-2026-04-28.md`) produce
a bigraded vector space whose Hilbert series factors as $\prod_k (1 -
z_1^a z_2^b)^{-1}$ in some normalisation. *Symmetry:* the symplectic
$\SL_2(\C)$ rotating the bidegree axes (this rotates $(a, b)$ on a
hyperbola of constant $a + b$, not modularly).

(GF-4) **The active-support partition function of the
$T_{a, b}$-basis.** Tracing $T_{a, b}$ produces
$\mathrm{Tr}(\phi_1^a \phi_2^b)$ on $\mathfrak{gl}_N$; the generating
function $F^{\rm Tr}(z_1, z_2) = \sum_{a, b} \mathrm{Tr}(\phi_1^a
\phi_2^b)\,z_1^a z_2^b$ is the closed observable trace of the
two-particle BF Wilson loop. *Symmetry:* $S_2$ on the spectral
parameters of $\phi_1, \phi_2$.

(GF-5) **U(1) anomaly indexing.** The U(1) anomaly cocycle $[\bar c]
\in H^2_{\rm Lie}(\bar A, \C)$ has coefficient $\hbar N$ in the
bosonic chamber, $\hbar(N - M)$ in the super extension. The U(1)
indexing is the central-charge labelling on $\bar A = \C[z_1, z_2]
/ \C \cdot 1$. *Symmetry:* (A5) parity-equivariance ($\Z/2$); rebasing
covariance under $\hbar^2 = \varepsilon_1 \varepsilon_2$.

### 2.3. What the heuristic claims to mirror

The heuristic correspondence — *as currently invoked in CLAUDE.md* —
identifies the relevant generating-function symmetry on our side
with one of:

* **(GF-2 ↔ Borcherds product structure).** The bigraded
  $(a, b)$-pattern of one-$\psi$ Koszul homology generates a partition
  / Fock-character-like product structure
  $\prod (1 - z_1^a z_2^b)^{-1}$, which is *formally* the same shape
  as the Borcherds product of $\Delta_5$, modulo the lattice
  identification $(a, b) \mapsto \alpha(a, b, m)$ for some choice of
  $m$ and signed multiplicity $f(nm, l)$.

* **(GF-3 ↔ BKM root supermultiplicities).** The column-Verma Hilbert
  series, when interpreted as signed dimensions of a $\Z/2$-graded
  representation, would in principle assign supermultiplicities to
  bidegrees $(a, b)$ matching $\smult \mathfrak g_{\Delta_5}$ on
  some sub-lattice of $\Lambda^{2,1}_{II}$.

* **(GF-5 ↔ Maass-character / orientation-character matching).** The
  (A5) $\Z/2$-symmetry would in principle map to the orientation
  character $\nu_{\Delta_5}: W^{(2)}(\Lambda^{2,1}_{II}) \to \{\pm
  1\}$ via a sub-extension.

### 2.4. The literal claim of the bridge

The bridge as inscribed claims **none of these matchings** as a
consequence of the manuscript. The CLAUDE.md sentence is precise:
the comparison is *motivated* by both sides being "generating
functions in topological-string theory"; the bridge is *heuristic
and convention-checking*; it is *not a BKM consequence of the local
Hamiltonian BF/Moyal calculation*. The function of the bridge is to
provide a structural sibling against which the manuscript's
conventions ($\hbar$ normalisation, $T_{a, b}$ vs. $J_N$ basis,
parity / orientation / sign data) can be cross-checked but never
*proved*.

---

## §3. $X$-conditions for chain-level lift

The heuristic *would* become a chain-level rigorous BKM consequence
if-and-only-if the following five conditions are simultaneously met.
The conditions are organised in dependency order: $X_1$ is the
formal conditional ("if a matched-conventions functor exists then…");
$X_2, X_3, X_4, X_5$ are the structural sub-hypotheses any such
functor must satisfy.

### 3.1. $X_1$ — Matched-conventions functor

**Statement.** A chain-level functor
\[
\mathcal F_{\rm Igusa} : (\text{Igusa BV / chiral category})
\;\longrightarrow\; (\text{our brane-defect BV category on}\
\R^2 \times \widehat{\C^2}_0)
\]
preserving the BV degree, the regulator class, and the anomaly
cohomology class.

**Required input on the Igusa side.** A chain-level BV / chiral
formulation of the BKM denominator algebra $\mathfrak g_{\Delta_5}$.
This does not currently exist in the literature: the
`~/igusa-cusp-form/main.tex` repository explicitly inscribes
construction of the BKM as *imported* (`~/igusa-cusp-form/main.tex`:
352–355: "BKM denominator: imported theorem; Gritsenko–Nikulin give
$\mathfrak g_{\Delta_5}$ and $\mathrm{den}(\mathfrak g_{\Delta_5}) =
64^{-1} \Delta_5(2Z)$") and the Hall-side compact realization as
*conditional / open* (`~/igusa-cusp-form/main.tex`:355–361).

**Required output on our side.** Whatever exists is the brane-defect
BV theory of `appendix-unreduced-bv-qme.tex` and the local Hamiltonian
BF formulation of `main.tex` `tate-T1-weighted-completion.tex`.

**Verdict.** UNMET. There is no chain-level Igusa BV / chiral
category currently in the literature. The Igusa repository names
construction of such a category as the *open Dirac–Igusa
realization certificate* (`~/igusa-cusp-form/main.tex`:411–418) and
flags it as open. **Firewall-permanent at current resolution.**

### 3.2. $X_2$ — Regulator-class compatibility

**Statement.** The regulator class on our side ((A5) admissible:
heat-kernel, point-splitting, dim-reg, Hadamard parametrix; W30-M2
audit) is compatible with whatever chain-level regulator the
Borcherds product / BKM denominator structure invokes.

**Required input on the Igusa side.** A regulator class that
preserves the Borcherds product structure at the chain level. The
Borcherds product expansion converges in the cusp-completed
semigroup algebra $0 < |s| \ll |q| \ll |r|^{-1} \ll 1$
(`~/igusa-cusp-form/main.tex`:739–742) — this is a *combinatorial*
convergence (every coefficient receives finitely many contributions),
not a chain-level regulator. To upgrade to a chain-level regulator
would require constructing a heat-kernel regulator on a
hypothetical Igusa BV theory (which does not exist; see $X_1$).

**Verdict.** UNMET. **Open-literature** rather than firewall-permanent
at this layer: were a chain-level Igusa BV theory constructed in
Phase-5, the Costello–Gwilliam Vol II §11 / Costello 2011 Ch. 4
regulator framework would (in principle) provide a
parity-preserving regulator scheme aligned with the (A5) admissible
class. The obstruction is upstream ($X_1$).

### 3.3. $X_3$ — Sp$_4(\Z)$ modular-invariance hypothesis on (A5)

**Statement.** The (A5) parity-equivariance hypothesis lifts to a
Sp$_4(\Z)$ modular-invariance hypothesis on the brane-defect
regulator class. Concretely, the parity operator $P =
\mathrm{diag}(\mathbf 1_N, -\mathbf 1_M)$ extends to a representation
of Sp$_4(\Z)$ on the matrix source / regulator data, with the (A5)
condition $[K_t, P] = 0$ generalising to $[K_t, \rho(g)] = 0$ for
all $g \in \Sp_4(\Z)$.

**Required input.** A construction of an Sp$_4(\Z)$-action on
$\mathfrak{gl}(N|N)$ (or on the regulator data
$\{K_t, Q^{\rm GF}, P_{\epsilon, L}\}$) that reduces to the (A5) $\Z
/ 2$-action on the centre $\Z / 2 \hookrightarrow \Sp_4(\Z)$ via
$\pm \mathbf 1_4$. **No such construction exists in the manuscript or
in the literature on $\mathfrak{gl}(N|N)$ super-Lie algebras.**

**Verdict.** UNMET. **Firewall-permanent at the modular-invariance
layer.** Sp$_4(\Z)$ has no natural action on $\mathfrak{gl}(N|N)$;
there is no representation-theoretic mechanism inscribed in the
manuscript or in the structural framework that would induce one.
The (A5) is a $\Z / 2$ structural symmetry of the parity grading;
Sp$_4(\Z)$ is a non-abelian arithmetic symmetry of period vectors
on $\mathbb H_2$. The two algebras have no shared finite-dimensional
representation in the manuscript's framework.

### 3.4. $X_4$ — Lattice morphism

**Statement.** A morphism $\Lambda_{(a, b)} \to \Lambda^{2, 1}_{II}$
of lattices, with the (a, b)-bigrading on column-Verma /
$T_{a, b}$ / one-$\psi$ Koszul homology mapping to the type-II
hyperbolic lattice in a way that preserves the relevant invariants
(signature, root structure, Weyl-group action).

**Required input.** A lattice $\Lambda_{(a, b)}$ on our side. The
candidate is the bigrading lattice $\Z^2$ generated by the $(a, b)$
indices on $T_{a, b}$, $\widetilde\Psi_{a, b}$, etc. Its natural
quadratic form is the *positive-definite* form
\[
((a, b), (a, b))_{\rm bigrade} \;=\; a + b
\]
(the total degree on the bigrading; a Hilbert-series-type quadratic
form), or alternatively $(a, b) \cdot (a', b') = a a' + b b'$ on
$\Z^2$ as an abelian group.

**Required output.** The type-II hyperbolic lattice $\Lambda^{2, 1}_{II}
= \HypPlan \oplus [2]$ with signature $(2, 1)$ has a hyperbolic /
Lorentzian quadratic form with the explicit Gram matrix
$\bigl(\begin{smallmatrix} 0 & -1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 2 \end{smallmatrix}\bigr)$
on the basis $(f_2, f_{-2}, f_3)$ (`~/igusa-cusp-form/main.tex`:4772).

**Verdict.** UNMET. **Firewall-permanent.**

* **Dimensional mismatch.** $\Z^2$ on our side has rank 2; the
  type-II hyperbolic lattice has rank 3. There is no rank-preserving
  map.

* **Signature mismatch.** $\Z^2$ with $a + b$ or $aa' + bb'$ is
  positive-definite (signature $(2, 0)$); $\Lambda^{2, 1}_{II}$ has
  Lorentzian signature $(2, 1)$. There is no signature-preserving
  embedding.

* **Root-system absence.** The $(a, b)$-bigrading carries no
  reflective wall structure: there are no positive-norm vectors
  $\delta$ with $(\delta, \cdot) \cdot 2 / (\delta, \delta)$ landing
  in $\Z$ on the bigrading (the form is too weak). The
  Gritsenko–Nikulin Cartan matrix
  $\bigl(\begin{smallmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{smallmatrix}\bigr)$
  has no analogue on $\Z^2$.

* **Weyl-group absence.** $W^{(2)}(\Lambda^{2, 1}_{II})$ is a Coxeter
  group of infinite order with three real simple reflections; the
  $(a, b)$-bigrading has only the $\Z / 2$ swap $(a, b)
  \leftrightarrow (b, a)$.

The lattice morphism does not exist at any rank, signature, or root
data layer. **Firewall-permanent.**

### 3.5. $X_5$ — Duality (T / S) inducing Sp$_4(\Z)$

**Statement.** A T-duality, S-duality, or other physical duality
inducing the Sp$_4(\Z)$ action on the manuscript's local Hamiltonian
BF data through a *physical bridge*: e.g., type-II / heterotic on
$K3 \times T^2$ where Sp$_4(\Z)$ acts on the dyon charge lattice.

**Required input.** A construction of a *physical* compactification
that bridges the closed B-model on a Calabi–Yau threefold (the BCOV
parent) to the type-II / heterotic on $K3 \times T^2$ where Sp$_4(\Z)$
is the U-duality group. The literature on this bridge (Harvey–Moore
1996; Dijkgraaf–Verlinde–Verlinde 1997; Sen 2005, 2008; Cardoso–de
Wit–Mohaupt 2002) is non-trivial and requires identifying:

* Calabi–Yau threefold $X = K3 \times E$ as the geometric setting.
* The closed B-model on $X$ *via* a topological reduction.
* The dyon charge lattice $\Gamma_X^{\rm form}$ (Definition
  `def:dyonic-mukai-lattice`,
  `~/igusa-cusp-form/main.tex`:4047–4070) as the source of Sp$_4(\Z)$.
* A pull-back to our local Hamiltonian BF model via the Costello–Li
  $d = 3$ flat $\C^d$ formulation.

**Verdict.** UNMET. **Phase-5 (long horizon).** The bridge from
type-II on $K3 \times T^2$ (where Sp$_4(\Z)$ is natural) to the
closed B-model on a Calabi–Yau threefold (BCOV) to our local model
on $\R^2 \times \widehat{\C^2}_0$ is structurally non-trivial in
multiple steps. The Igusa repository explicitly lists these steps
in `~/igusa-cusp-form/main.tex`:218–246 as the
"projection-finite local factorization, rigidified wrapped
prequotients, local-local, ordered local/wrapped, and wrapped-wrapped
extension correspondences, the eight-word two-step binary flag
atlas, quotient-after-correspondence descent, and protected
integration with trace degree $s^{b_R}$." None of this is in our
manuscript. The DVV physics interpretation (`~/igusa-cusp-form/main.tex`:
4209–4211) is cited as input only.

---

## §4. Per-X status summary

| $X$ | Statement | Met? | Firewall classification |
|---|---|---|---|
| $X_1$ | Matched-conventions functor Igusa BV / chiral $\to$ ours | UNMET | FIREWALL-PERMANENT (no Igusa BV side exists) |
| $X_2$ | Regulator-class compatibility | UNMET | OPEN-LITERATURE (downstream of $X_1$) |
| $X_3$ | (A5) lifts to Sp$_4(\Z)$ modular invariance | UNMET | FIREWALL-PERMANENT (no Sp$_4(\Z)$ action on $\mathfrak{gl}(N|N)$) |
| $X_4$ | Lattice morphism $\Z^2 \to \Lambda^{2,1}_{II}$ | UNMET | FIREWALL-PERMANENT (rank, signature, root data all incompatible) |
| $X_5$ | Physical duality (T / S) bridge | UNMET | PHASE-5 (constructible if BCOV / Vol III / Igusa convergence is proved) |

**Interpretation.** Three of five conditions are firewall-permanent at the
*structural* layer: $X_1$ (no Igusa BV), $X_3$ (no Sp$_4(\Z)$ on
$\mathfrak{gl}(N|N)$), $X_4$ (lattice incompatibility). $X_2$ is
open-literature but downstream of $X_1$. $X_5$ is a Phase-5
conditional, requiring a separate trans-volume convergence theorem
that the manuscript explicitly excludes
(`rmk:convention-firewall`, `main.tex`:5380–5394).

**Net classification.** The Igusa heuristic firewall is
**FIREWALL-PERMANENT at three independent structural layers**.
Lifting any one would not lift the firewall; lifting all three
simultaneously would be a major Phase-5 program, possibly never.
This is qualitatively different from the BCOV firewall analysed in
`reconstitution/phase4-exec-BCOV-A5-comparison-2026-04-28.md`,
which had a single permanent layer (chain-level vertex-class) and a
liftable layer (coefficient).

---

## §5. Cross-walk to BCOV-A5 firewall

### 5.1. BCOV firewall topology (recap)

The BCOV-A5 audit established (`phase4-exec-BCOV-A5-comparison-2026-04-28.md`:
68–125):

* **Coefficient layer:** liftable. Both BCOV (Costello–Li 2015 / 2016)
  and our W22-T1 / W22-T2 share the coefficient
  $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = N - M$. The match is via a
  representation-theoretic common ancestor independent of spacetime,
  regulator, and vertex cocycle.

* **Chain-level vertex layer:** permanent. The two BV complexes are
  structurally distinct (HCS on a CY$_3$ vs brane-defect on $\R^2
  \times \widehat{\C^2}_0$).

* **Smallest matching example:** the open-closed BCOV theory on flat
  $\C^3$ (Costello–Li 2015) probed by an open brane on a Lagrangian
  with open algebra $\mathfrak{gl}(N|N)$. One-loop chain-level
  anomaly cancellation by exactly $\hbar \cdot \mathrm{Str}(I) = 0$.

### 5.2. Igusa firewall topology (this audit)

The Igusa firewall is **structurally tighter** than BCOV at every
layer:

* **No coefficient layer to lift.** The BCOV coefficient
  $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = N - M$ has no analogue on
  the Igusa side. The relevant Igusa-side quantity is the signed
  root multiplicity $\smult \mathfrak g_{\Delta_5, \alpha} = f(nm, l)$,
  which depends on the lattice point $\alpha = (n, l, m) \in
  \Lambda^{2, 1}_{II}$ and the weak Jacobi form $\phi_{0, 1}$. There
  is no representation-theoretic common ancestor on which both sides
  agree.

* **Chain-level vertex layer permanent (as on BCOV).** The Igusa BV
  / chiral side does not even exist as a chain-level theory in the
  literature.

* **Modular-invariance layer permanent (NEW, not present on BCOV).**
  BCOV does not require Sp$_4(\Z)$ modular invariance; the BCOV
  anomaly is a $\bar\partial$-cohomology class on a complex
  manifold's moduli space. The Igusa side, by contrast, requires
  Sp$_4(\Z)$ modular invariance as the *defining* property of
  $\Delta_5$. (A5) gives at most $\Z / 2$; the gap is structural.

* **Lattice layer permanent (NEW).** BCOV uses no Lorentzian lattice
  structure. The Igusa / BKM side has the type-II hyperbolic lattice
  $\Lambda^{2, 1}_{II}$ as a load-bearing object. There is no
  $\Z^2 \to \Lambda^{2, 1}_{II}$ embedding.

### 5.3. The inverse-Polyakov question

**Polyakov:** "What modular property does our (A5) machinery
realise?" Answer: a $\Z / 2$ structural symmetry of the parity
grading, a $\Z / 2$ swap of the $(a, b)$ bigrading. Neither lifts to
Sp$_4(\Z)$.

**Invariants:** "Which invariant gets mapped on each side?" Answer:
**no invariant maps**. The Igusa side's fundamental invariants are
the signed root multiplicities $f(nm, l)$ on a Lorentzian lattice; our
side's fundamental invariants are the U(1) anomaly coefficient $\hbar
N$ on $H^2_{\rm Lie}(\bar A, \C)$ and the bigrading $(a, b)$ on
$\Z^2$. Neither admits a morphism to the other.

### 5.4. Verdict on the cross-walk

The Igusa firewall is **strictly more permanent** than the BCOV
firewall:

| Firewall layer | BCOV-A5 verdict | Igusa-A5 verdict |
|---|---|---|
| Coefficient | LIFTABLE via rep-theoretic ancestor | NO ANCESTOR; permanent |
| Chain-level vertex | PERMANENT | PERMANENT (and Igusa BV side does not exist) |
| Modular invariance | (not load-bearing on BCOV) | PERMANENT (Sp$_4(\Z)$ has no action on our data) |
| Lattice | (not load-bearing on BCOV) | PERMANENT (signature / rank mismatch) |

The CLAUDE.md framing is therefore correct: the Igusa bridge is
heuristic / convention-checking only, with no Phase-4 path to a
chain-level lift. **A Phase-5 path requires lifting four
independent firewall layers simultaneously, three of which are
firewall-permanent at the current resolution.**

---

## §6. Smallest matching test

### 6.1. Hypothesis: is there a smallest example where matching is forced?

**Question.** Is there a smallest computational test where our
model's generating function would *necessarily* match $\Delta_5$?
On the BCOV side, the open-closed flat $\C^3$ Costello–Li theory
provides such a test: both sides compute one-loop $\hbar
\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = 0$ on the super-balanced probe.

### 6.2. Test attempt 1: leading coefficient match

The Igusa $\Delta_5$ has leading expansion
\[
\Delta_5(Z) \;=\; 64\,q^{1/2} r^{1/2} s^{1/2} - 64 \cdot 9\,q^{3/2}
r^{1/2} s^{1/2} + \ldots
\]
(from `~/igusa-cusp-form/main.tex`:2225, $c_\Delta(1, 1, 1) = 64$;
recursion `~/igusa-cusp-form/main.tex`:2249–2250). The leading
coefficient $64 = 2^6$ is the theta-leading constant. Our model
produces no such number: the closest analogue is the bigrading
coefficient on $T_{0, 0} = \mathrm{Tr}(I) = N$, which is
$N$-dependent and has no $N$-independent leading coefficient match
to $64$.

**Test verdict.** No match. The "leading coefficient" comparison is
trivially incompatible because our model has no fixed scalar on the
left-hand side.

### 6.3. Test attempt 2: bigrading-to-active-support map

**Hypothetical map.** Consider the proposal $(a, b) \mapsto
\alpha(a, b, 0) = 2a f_2 - b f_3 \in \Lambda^{2, 1}_{II}$. The image
of $\Z_{\geq 0}^2$ under this map is the slice $\{m = 0\}$ of
$\Gamma_{\rm eff}$.

**Active-support image.** The active support requires $f(nm, l) \neq
0$. At $m = 0$, the active support condition becomes $f(0, l) \neq
0$, which holds only at $l = 0, \pm 1$ (with $f(0, 0) = 10$, $f(0,
\pm 1) = 1$); see `~/igusa-cusp-form/main.tex`:1681. Hence the
hypothetical map sends only finitely many bigrades $(a, b) \in \{(0,
-1), (0, 0), (0, 1)\}$ to the active support; for $a \geq 1$, the
image lies outside the active support.

**Verdict.** The hypothetical bigrading map sends almost all of our
generating-function support to the *inactive* slice of $\Gamma_{\rm
eff}$, where the multiplicities $f(nm, l)$ are zero. The matching
fails at the support level.

### 6.4. Test attempt 3: Maass-character / orientation-character matching

The Maass character $\nu_{\Delta_5}: W^{(2)}(\Lambda^{2, 1}_{II}) \to
\{\pm 1\}$ takes value $-1$ on the three type-II simple reflections
$s_{\delta_1}, s_{\delta_2}, s_{\delta_3}$ and $+1$ on the three
chamber-permuting reflections $s_{f_{-2} - f_2}, s_{f_2 - f_3}, s_{f_2
+ f_3}$ (`~/igusa-cusp-form/main.tex`:5010–5017). The (A5)
parity-equivariance gives a $\Z / 2$-character on
$\mathfrak{gl}(N|N)$ via the parity operator $P = \mathrm{diag}(\mathbf
1_N, -\mathbf 1_M)$.

**Hypothetical match.** Could the (A5) $\Z / 2$ map to a $\Z /
2$-quotient of $W^{(2)}(\Lambda^{2, 1}_{II})$? Maass's character is
a $\Z / 2$-character, so this is a candidate.

**Obstruction.** The map would require an embedding $\Z / 2
\hookrightarrow W^{(2)}(\Lambda^{2, 1}_{II})$ via $P \mapsto$ some
reflection. The parity operator $P$ acts on $\mathfrak{gl}(N | N)$;
the reflections $s_{\delta_i}$ act on $\Lambda^{2, 1}_{II}$. There is
no algebra homomorphism $U(\mathfrak{gl}(N | N)) \to \C[W^{(2)}(\Lambda^{2,
1}_{II})]$ that intertwines the two $\Z / 2$ structures. The (A5)
$\Z / 2$ is *parity*; the Maass $\Z / 2$ is *reflection sign*. They
have no shared finite-dimensional module.

**Verdict.** No matching at the character layer. The two $\Z / 2$
structures have no constructive intertwiner.

### 6.5. Conclusion: no smallest matching test exists

There is **no smallest computational test where our model's
generating function necessarily matches $\Delta_5$**. The named
obstructions, in order:

1. **Leading-coefficient incompatibility.** Our model has no
   $N$-independent fixed scalar to match $64 = 2^6$.

2. **Active-support incompatibility.** The bigrading $(a, b)$ of
   our model maps under any natural projection to a slice of
   $\Gamma_{\rm eff}$ where multiplicities are almost everywhere zero
   (only the points $(0, 0, 0), (0, \pm 1, 0)$ are active).

3. **Character incompatibility.** The (A5) $\Z / 2$-parity has no
   intertwiner with the Maass $\Z / 2$-character on
   $W^{(2)}(\Lambda^{2, 1}_{II})$.

4. **Lattice incompatibility ($X_4$).** The bigrading lattice $\Z^2$
   has no morphism to the type-II hyperbolic lattice
   $\Lambda^{2, 1}_{II}$.

5. **Modular incompatibility ($X_3$).** Our model has no Sp$_4(\Z)$
   action; no candidate generating function transforms modularly.

The closest available comparison is **internal-consistency**: both
sides record a $\Z/2$ sign datum (parity / Maass character) whose
agreement on isolated low-degree generators could be recorded. This
is a *convention-checking* exercise, exactly as CLAUDE.md
specifies. It is not a chain-level rigorous match.

---

## §7. Anti-attack scan responses

### 7.1. (Att-1) Sp$_4(\Z)$ via duality?

**Attack.** $\Delta_5$ is a Siegel modular form on Sp$_4(\Z)$; our
model has no Sp$_4(\Z)$ action visible. *Could a duality (T-duality,
S-duality, mirror) induce one?*

**Response.** Three candidate dualities:

* **T-duality on a $T^2$ factor.** If our spacetime $\R^2 \times
  \widehat{\C^2}_0$ admits a $T^2 \subset \widehat{\C^2}_0$ T-duality,
  the duality group is $\SO(2, 2; \Z) \simeq \SL(2, \Z) \times
  \SL(2, \Z)$, not Sp$_4(\Z)$. The 5d M-theory frame discussed in
  reconstitution `phase4-exec-G4-T22-virasoro-twist-2026-04-28.md`
  has $T^2$ factor but the duality group is not Sp$_4(\Z)$.

* **S-duality on the $\mathfrak{gl}(N | N)$ open algebra.** The
  S-duality $\hbar \to 1 / \hbar$ on the matrix Weyl algebra has a
  group-theoretic image in $\SL(2, \Z)$, not Sp$_4(\Z)$.

* **U-duality of the type-II $K3 \times T^2$ compactification.** This
  is the natural setting for Sp$_4(\Z)$ as $\SO(6, 22; \Z)$
  intersected with the Siegel domain; cf. Dijkgraaf–Verlinde–Verlinde
  1997. **However, this duality is on the type-II / heterotic on
  $K3 \times T^2$ side, not on our local Hamiltonian BF on $\R^2 \times
  \widehat{\C^2}_0$.** The bridge from one to the other passes
  through the BCOV / Costello–Li open-closed framework on $\C^3$, the
  Vol III $\kappa$-stratification, and the compact $K3 \times T^2$
  partition function. None of these bridges is currently inscribed in
  the manuscript.

**Verdict.** No duality currently induces Sp$_4(\Z)$ on the
manuscript's data. The U-duality candidate is the natural physical
target but lies on the far side of the cross-volume firewall.

### 7.2. (Att-2) BKM root system intersection?

**Attack.** The BKM Lie algebra $\mathfrak g_{\Delta_5}$ has explicit
root data (Cartan matrix
$\bigl(\begin{smallmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{smallmatrix}\bigr)$
on three real simple roots). *Does any subset of $\mathcal W_{1+\infty}
(\varepsilon_1, \varepsilon_2)$ generators match a subset of these
roots?*

**Response.** $\mathcal W_{1+\infty}(\varepsilon_1, \varepsilon_2)$
is the Heisenberg-rebased $\mathcal W_{1+\infty}$ algebra appearing
in the G4-M2 Heisenberg twist (reconstitution
`phase4-exec-G4-M2-Heisenberg-twist-2026-04-28.md`). Its
generators $\{W_n^{(s)}\}_{n \in \Z, s \geq 1}$ index by mode
$n$ and spin $s$, with central charge $c = c(\varepsilon_1,
\varepsilon_2)$. The structure is an **affine current algebra**
(or its quantum deformation), not a BKM.

**No match.** The BKM $\mathfrak g_{\Delta_5}$ has *imaginary*
simple roots in addition to the three real simple roots
($\delta_1, \delta_2, \delta_3$); the imaginary simple roots have
multiplicities determined by $f(0, l)$, in particular the
$(0, 0)$-multiplicity is 10. The $\mathcal W_{1+\infty}$-affine
current algebra has no imaginary simple roots in this sense; its
positive roots index by integers $n \in \Z_{\geq 0}$, not by lattice
points in a Lorentzian sublattice of $\Lambda^{2, 1}_{II}$.

**No subalgebra inclusion.** A subset of $\mathcal W_{1+\infty}$
generators ($\{W_n^{(1)}, W_n^{(2)}\}$, the Heisenberg + Virasoro
sector) is the affine $\widehat{\mathfrak{gl}}_1 \oplus \mathrm{Vir}$
algebra; this is a *finite-dimensional Cartan* sub-data of the BKM
in the abstract sense, but the structure constants do not match.
**No homomorphism inscribed at any layer of the manuscript.**

**Verdict.** No BKM root-system match. The colour algebra in our
model is fundamentally affine / vertex-operator-algebra in nature;
the BKM is fundamentally generalised-Kac–Moody.

### 7.3. (Att-3) Bigrading vs BKM root lattice?

**Attack.** The Borcherds product expansion uses a specific lattice
of weights ($\Lambda^{2, 1}_{II}$, type-II hyperbolic lattice with
explicit basis $f_2, f_3, f_{-2}$). *Does the (a, b)-bigrading on
column-Verma generate a compatible lattice, or is it orthogonal to
the BKM root lattice?*

**Response.** The (a, b)-bigrading is on $\Z^2$ with positive-definite
$(2, 0)$ signature (or $(2, 0)$ in $\R^2$ totally positive cone).
The type-II hyperbolic lattice is $(2, 1)$ Lorentzian.

* **Rank mismatch.** $\Z^2$ has rank 2; $\Lambda^{2, 1}_{II}$ has
  rank 3.

* **Signature mismatch.** Positive-definite vs Lorentzian.

* **Active-support obstruction.** Even if one ignores rank /
  signature and simply maps $(a, b) \mapsto \alpha(a, b, m)$ for a
  fixed third coordinate $m$, the active-support condition
  $f(nm, l) \neq 0$ is satisfied only on a lower-dimensional sublattice
  of $\Gamma_{\rm eff}$ (mostly $4nm - l^2 \in \{-1, 0, 1, \ldots\}$).
  The bigrading lattice maps into the *kernel* of the active-support
  function for almost all $(a, b)$.

**Verdict.** The bigrading lattice is **structurally orthogonal**
to the BKM root lattice. There is no morphism, embedding, or
projection that respects the relevant invariants (rank, signature,
positivity).

### 7.4. (Att-4) DVV N=4 / closed B-model bridge?

**Attack.** The Dijkgraaf–Verlinde–Verlinde 1997 dyon-counting
interpretation links $\Delta_5$ to N=4 string theory. Our manuscript
is Hamiltonian BF (closed B-model). *The bridge from N=4 to closed
B-model is well-known to be subtle; is this our actual obstruction?*

**Response.** Yes — this is the deepest obstruction. The DVV
interpretation places $\Delta_{10} = \Delta_5^2$ as the partition
function of $1/4$-BPS dyons in type-II on $K3 \times T^2$ with
N=4 supersymmetry. The closed B-model on a Calabi–Yau threefold
$X$ (BCOV) is a topological subsector of N=2 type-II on $X$.
Bridging these requires:

1. A topological reduction of N=4 on $K3 \times T^2$ to N=2 on
   $K3 \times T^2$ via partial topological twisting.

2. A deformation from $K3 \times T^2$ as a Calabi–Yau twofold $\times$
   torus to a Calabi–Yau threefold $X$.

3. A reduction from BCOV on $X$ to our local model on $\R^2 \times
   \widehat{\C^2}_0$ via the Costello–Li flat $\C^d$ formulation
   ($d$ odd; $d = 3$).

Each of these steps is a substantial open program in the literature.
Sen's program (Sen 2005, 2008, 2010 series) addresses (1) and partial
(2); the BCOV / Costello–Li program addresses (3); a full chain (1)
$\to$ (2) $\to$ (3) is not currently inscribed.

**The actual obstruction.** Yes. The N=4 / closed-B-model gap is
the load-bearing obstruction. It is the same obstruction that the
manuscript's `rmk:convention-firewall` (`main.tex`:5380–5394) and
`ssec:cross-volume-horizon` (`main.tex`:5894–5915) inscribe as the
cross-volume firewall.

**Verdict.** This is the dominant Phase-5 obligation underlying all
five $X_i$ and the entire heuristic firewall. The DVV / Sen / BCOV /
Costello–Li bridge is structurally non-trivial and requires
matching-conventions theorems at each step.

---

## §8. Residuals + Phase-5 / open-literature classification

### 8.1. Residuals (open at Phase-4)

**(Res-1) Internal-consistency check on character match.** The (A5)
$\Z / 2$-parity character on $\mathfrak{gl}(N|N)$ has values $\pm 1$
on the parity-graded basis. The Maass character $\nu_{\Delta_5}$ on
$W^{(2)}(\Lambda^{2, 1}_{II})$ has values $\pm 1$ on the six wall
generators (`~/igusa-cusp-form/main.tex`:5010–5017, 1822–1826).

**Internal cross-check.** Both characters are $\Z / 2$-valued. On
*low-degree* generators a numerical agreement is possible
(e.g., the parity of $\widetilde\Psi_{1, 0}$ vs $\nu_{\Delta_5}(s_{f_3})
= -1$ at $\delta_3 = f_3$). This is the convention-checking content
of the heuristic.

**Phase-5 escalation.** A precise low-degree match between (A5)
parity sign data and Maass character values on the three type-II
simple reflections is a Phase-5 conditional. It does not constitute
a chain-level lift but does serve as a convention-stability test.
**Open at Phase-4; not load-bearing.**

**(Res-2) Cross-volume convergence theorem.** A matched-conventions
theorem comparing our local Hamiltonian BF data to the Costello–Li
2015 flat-$\C^3$ open-closed BCOV theory, and from there to a
hypothetical chain-level Igusa BV theory. This is the *Phase-5
master integration program* that the BCOV-A5 audit identified
(`phase4-exec-BCOV-A5-comparison-2026-04-28.md`:451–462) and that
the present audit confirms is the dominant residual.

**Phase-5 escalation.** The bridge requires: (a) the Costello–Li
2015 / 2016 cross-walk (BCOV firewall liftable layer); (b) a
deformation from $\C^d$ to $K3 \times T^2$ (Calabi–Yau threefold);
(c) the DVV-interpretation insertion (N=4 / closed-B bridge); (d)
an Igusa BV side construction. **Open-literature in (a)+(b);
Phase-5 in (c); structurally permanent in (d) at current
resolution.**

**(Res-3) Inverse-DVV check.** Whether the dyon partition function
$1 / \Delta_{10}$ admits a Hamiltonian-BF-style truncation that
recovers a $T_{a, b}$-type generating function at low order. This is
purely heuristic.

**Open-literature classification.** This is a literature exploration
task, not a manuscript Phase-4 obligation.

### 8.2. Phase-5 / open-literature classification

| Item | Classification | Phase-5 path |
|---|---|---|
| $X_1$ matched-conventions functor | FIREWALL-PERMANENT (no Igusa BV side) | Construct chain-level Igusa BV; cite open Dirac–Igusa certificate |
| $X_2$ regulator-class compatibility | OPEN-LITERATURE | Apply Costello–Gwilliam Vol II §11 to hypothetical Igusa BV |
| $X_3$ Sp$_4(\Z)$ on (A5) | FIREWALL-PERMANENT | Requires construction of an Sp$_4(\Z)$ representation on $\mathfrak{gl}(N|N)$ — no candidate inscribed |
| $X_4$ lattice morphism | FIREWALL-PERMANENT | Rank, signature, root data all incompatible — no path |
| $X_5$ duality bridge | PHASE-5 (long horizon) | DVV / Sen / BCOV / Costello–Li chain; open program |
| Res-1 character cross-check | PHASE-5 (short horizon) | Low-degree numerical match; convention-checking |
| Res-2 cross-volume convergence | PHASE-5 (master) | Coordinated with Vol III $\kappa$-stratification |
| Res-3 inverse-DVV check | OPEN-LITERATURE | Literature exploration |

**Master classification.** Three of five $X$-conditions are
firewall-permanent at the current structural layer. Lifting any one
firewall-permanent layer (say $X_3$ via construction of an Sp$_4(\Z)$
action) would not lift the firewall; lifting all three would
constitute a major Phase-5 program.

**The CLAUDE.md framing is structurally correct.** The Igusa /
$\Delta_5$ / BKM bridge is heuristic and convention-checking only,
*not a BKM consequence*. The manuscript's
`rmk:convention-firewall` (`main.tex`:5380–5394) and
`ssec:cross-volume-horizon` (`main.tex`:5894–5915) inscribe this
correctly. **No Phase-4 manuscript revision is required.**

### 8.3. Recommendations

**(Rec-1)** Preserve the explicit Igusa firewall in
`main.tex`:5380–5394 and 5894–5915 verbatim. The five-$X$ analysis
of this audit confirms that no claim weaker than "convention-checking
heuristic" is currently supportable.

**(Rec-2)** When future Phase-5 work attempts to lift the Igusa
firewall, do so layer-by-layer following the $X$-classification:
$X_2, X_5$ first (open-literature / Phase-5), then $X_1$ (requires
chain-level Igusa BV construction), then $X_3, X_4$
(structural — would require new algebra).

**(Rec-3)** The DVV / Sen / BCOV / Costello–Li bridge (Att-4) is
the single most informative Phase-5 program for this firewall.
Future audits should track the literature on the chain (1)
topological twist of $K3 \times T^2$, (2) deformation to threefold,
(3) BCOV / Costello–Li reduction.

**(Rec-4)** The Igusa-side primary anchors are clean: the
Gritsenko–Nikulin 1997 BKM construction and the Borcherds 1998
product theorem are both well-established. The bottleneck is on
*our side*: no chain-level structure on our model produces a
generating function in $\Sp_4(\Z)$-modular variables.

---

## §N+1. Anchor verification

* **Igusa 1962.** *Amer. J. Math.* **84**, 175–200. Anchor for the
  ring $M_*^{\rm even}(\Sp_4(\Z))$ structure. Verified in
  `~/igusa-cusp-form/main.tex`:2188–2189.
* **Borcherds 1998.** "Automorphic forms with singularities on
  Grassmannians", *Invent. Math.* **132**, 491–562. Anchor for the
  product expansion. Verified in `~/igusa-cusp-form/main.tex`:1769–1781
  (citation `Borcherds95` is to the 1995 *Invent. Math.* paper which
  is the primary singular-theta correspondence; the 1998 paper
  extends).
* **Gritsenko–Nikulin 1997.** *Amer. J. Math.* **119**, 181–224.
  Anchor for the BKM denominator formula and Cartan matrix. Verified
  in `~/igusa-cusp-form/main.tex`:5066–5067 (Gram matrix of the
  three real simple roots), 5024–5028 (chamber decomposition).
* **Dijkgraaf–Verlinde–Verlinde 1997.** *Nucl. Phys.* **B484**,
  543–561. Anchor for the dyon-counting interpretation. Verified in
  `~/igusa-cusp-form/main.tex`:4209–4211 (cited as `DVV` in proj.bib).
* **BCOV 1994.** *Comm. Math. Phys.* **165**, 311–427. Anchor for
  the closed B-model. Already audited in
  `phase4-exec-BCOV-A5-comparison-2026-04-28.md`.
* **Costello–Li 2012, 2015, 2016.** Already audited in
  `phase4-exec-BCOV-A5-comparison-2026-04-28.md`.

All anchors verified. No primary-source contestation.

---

## §N+2. Polyakov rebasing audit

The Polyakov rebasing audit applied to (A5) on the BCOV side
(`phase4-exec-A5-anomaly-ledger-2026-04-28.md`:§N+2) established
that (A5) is preserved under the rebasing $\hbar^2 = \varepsilon_1
\varepsilon_2$ from the G4-M2 Heisenberg sub-VOA twist. Parity is
independent of the rebasing parameter.

**Igusa-side analogue.** The Igusa $\Delta_5$ has its own
rebasing structure: the chamber decomposition $W^{(2)}(\Lambda^{2,
1}_{II}) \rtimes \Aut(\Poly_{II}) \simeq W^{(2)}(\Lambda^{2, 1}_{II})
\rtimes S_3$ permutes the three type-II simple roots
($\delta_1, \delta_2, \delta_3$). Under the chamber permutation
$S_3$, the form $\Delta_5$ transforms by $\det(a)$ on $\Aut(\Poly_{II})
= S_3$ (Maass restriction lemma,
`~/igusa-cusp-form/main.tex`:5005–5007).

**Cross-walk.** The (A5) $\Z / 2$ has no natural map to $S_3$ on the
Igusa side. The chamber automorphism $\Aut(\Poly_{II}) \simeq S_3$
contains $\Z / 2$ as a subgroup (any single transposition), but the
choice is arbitrary. **No canonical $(A5) \Z / 2 \hookrightarrow S_3$
exists in the manuscript.**

**Verdict.** The Polyakov rebasing on the Igusa side gives chamber
permutation $S_3$, not Sp$_4(\Z)$. (A5) survives our-side rebasing
but does not lift to Igusa-side rebasing. This is consistent with
the firewall classification of $X_3$.

---

## §N+3. (Final) consolidated verdict

**The Igusa $\Delta_5$ / BKM heuristic firewall is FIREWALL-PERMANENT
at three independent structural layers ($X_1, X_3, X_4$), with
$X_2$ open-literature and $X_5$ Phase-5 long-horizon. The CLAUDE.md
framing is structurally correct: heuristic and convention-checking
only, not a BKM consequence. No Phase-4 manuscript revision is
required.**

**Single sentence.** Without an Sp$_4(\Z)$ action induced from our
local Hamiltonian BF data (currently absent), without a lattice
morphism $\Z^2 \to \Lambda^{2, 1}_{II}$ (currently structurally
incompatible), and without a chain-level Igusa BV / chiral category
(currently absent in the literature), the bridge from our local
$T_{a, b}$ / $\widetilde\Psi_{a, b}$ generating functions to the
Igusa $\Delta_5$ Borcherds product cannot be lifted to a chain-level
match.
