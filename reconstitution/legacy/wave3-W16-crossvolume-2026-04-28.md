# Wave-3 W16 — Polyakov + Functoriality, deeper cross-volume audit

**Author.** Raeez Lorgat.
**Date.** 2026-04-28.
**Wave.** 3, item W16.
**Lens.** Polyakov primary (scaling, renormalization, anomaly,
physical dimension, path-integral sanity) + Functoriality secondary
(naturality of identifications across volumes, canonical vs chosen
data, intertwiner conditions).
**Mission.** Independent fresh attack on the cross-volume firewall.
Find invariants that **must agree** across `topological-strings`,
`calabi-yau-quantum-groups` (Vol III), `igusa-cusp-form` that the
wave-2 W5 audit might have missed; verify functoriality of every
proposed cross-volume identification; sharpen the BKM bridge
precision; record new residuals.

**Repos in scope.**
- `/Users/raeez/topological-strings/`.
- `/Users/raeez/calabi-yau-quantum-groups/` (Vol III).
- `/Users/raeez/igusa-cusp-form/` (Igusa $\Delta_5$ / BKM).

**Mode.** Proposal-only. Master-ledger schema; IDs prefix `W3-W16-`.
No edits to manuscript files in any repo.

---

## §1. Method

I read the W5 catalog, audited what it covered, and then asked: which
**invariants under quantization, scaling, automorphism, or category
inclusion must respect a forced equality between volumes regardless of
whether the manuscript ever asserts a cross-volume claim**? An
invariant that *must* agree because the underlying mathematical object
is the same, but does not because the conventions choose different
normalizations, is a silent reconciliation hazard even when the
manuscript firewall is intact in prose.

I then ran the Polyakov check on each:
- *scaling.* Does dimensional analysis of $\hbar$, $z_i$, $\omega$,
  central charge $c$ match? Are weights additive in the same direction?
- *anomaly.* Is the U(1)/Capelli class on this side truly distinct from
  the conformal $c$ / level $k$ on the chiral side, or are they two
  realizations of the same Lie 2-cocycle on
  $\widehat{\mathfrak h}=\mathfrak{ham}(\widehat{\C^2}_0)$?
- *path-integral sanity.* If the formal disk's $P_0$ centre were the
  formal-completion specialization of Vol III's $\Phi_2(D^b\Coh(K3))$,
  what would that mean for the BV propagator and the locally constant
  factorization product?

The Functoriality check is symmetric: write down the candidate functor
$F$ from a topological-strings category to a Vol III / Igusa category,
verify it commutes with the obvious source automorphisms (formal
symplectomorphisms, lattice symmetries, $S^d$-framings), and report
whichever fail.

---

## §2. Wave-2 W5 catalog: what was already covered

W5 cataloged five flagged divergences (all firewalled):
1. Worldsheet ($\R$-line vs $\Sigma_1\subset K3$).
2. BV / Poisson degree ($P_0$ vs $P_1$ at $d=2$).
3. Trace pairing (none vs CY$_d$ negative-cyclic).
4. Scalar $U(1)$ anomaly $[\bar c]$ has no counterpart elsewhere.
5. Bar-cobar (Lie/Tate vs chiral/Ran).

Plus three editorial / confirmation items: $S^3$ framing not
applicable; $d=\dim_\C X=2$ uniformity; bibliography contains zero
in-progress sibling citations.

W16 below adds **eight** new candidate divergence sites that W5 did
not name explicitly, and then runs the functoriality and BKM-bridge
checks.

---

## §3. Extended divergence catalog (W3-W16-D series)

Below I cite both `topological-strings` (`TS:`) and the relevant
sibling-volume file:line where the convention is set.

### W3-W16-D1. Sign of the Poisson bracket convention vs Schouten degree
**Severity 2. Status valid. Confidence high.**
**Topological-strings.** `appendix-unreduced-bv-qme.tex:24`:
"the Poisson sign convention is $\{z_1,z_2\}=1$".
`principles.tex:78–82`: $\{f,g\} = \partial_{z_1}f\,\partial_{z_2}g
- \partial_{z_2}f\,\partial_{z_1}g$.
**Vol III.** `chapters/theory/cy_to_chiral.tex:379`: at $d=2$ the
Gerstenhaber bracket is "the degree-$(-1)$ Schouten--Nijenhuis
bracket" on $\HH^\bullet(\cC) \cong \PV^\bullet(S)$. Vol III
canonical convention from
`chapters/theory/hochschild_calculus.tex:692`:
$\{\partial_{z_3}, z_3\}_{\mathrm{SN}} = 1$ on $\C^3$, with the
Schouten--Nijenhuis bracket of degree $-1$.
**Issue (Polyakov scaling).** Vol III's Schouten bracket is in
*polyvector* degree, where $\theta^i = \partial_{z_i}$ has polyvector
degree $1$ and $z_i$ has polyvector degree $0$, giving an
$\{\theta^1, z_1\}_{\SN}$-bracket of polyvector degree $0$.
Topological-strings' Poisson bracket is in *function* degree where
both $z_1, z_2$ have degree $0$, giving $\{z_1, z_2\}=1$.
The two conventions agree numerically on linear coordinates ($+1$),
but the **scaling axis** they index is different: Schouten lowers
polyvector degree by $1$; Poisson preserves Lie filtration. If a
matched-conventions theorem ever identifies the topological-strings
$\{z_1, z_2\}=1$ on $\widehat{\C^2}_0$ with the Vol III
$\{\theta^1, z_1\}_{\SN}$ on the formal completion of K3 at a smooth
point, the **comparison morphism must specify on which polyvector slot
$\theta^i$ lives.** No such specification appears in any
matched-conventions template. The naked-eye numerical equality
$\{z_1,z_2\} = 1$ vs $\{\theta^1, z_1\}_{\SN}=1$ is **not** evidence
of a transfer.
**Recommended firewall sharpening.** Add to
`tate-P5-cross-volume.tex:108` (the Vol III template) one bullet:
"State which slot of the polyvector grading the local
$\{z_1, z_2\} = 1$ corresponds to under the proposed comparison;
specify the polyvector degree of each generator."

### W3-W16-D2. $\hbar$ as scaling parameter: dimensional vs dimensionless
**Severity 3. Status valid. Confidence high.**
**Topological-strings.** `main.tex:5398–5408` Weyl/Moyal: $\hbar$ is
the formal Rees deformation parameter; classical limit is $\hbar\to0$;
quantum Capelli shift is $\hbar N$
(`main.tex:419–425`). $\hbar$ is **adimensional** in the formal-disk
algebra: nothing in the local theorem relates it to physical
length/area on the worldsheet.
**Vol III.** `main.tex:679–688` rank-26 Fake-Monster R-matrix:
$R^{\mathrm{FM}}(u, Z) = (1 + \hbar\, \Omega_{\II_{25,1}}/u)\cdot
\theta^{\mathrm{FM}}(u, Z)$, where $u$ is a **spectral parameter**
of dimension inverse to the Yangian level. Also `main.tex:790–803`:
the Fake-Monster row enforces $\hbar^2 \cdot K = -1$ with
$K = 2c_+(L) = 50$ on $\II_{25,1}$, giving
$\hbar^2 = -1/50 = -1/8$ on the Bruinier branch (the text writes
$(K, \hbar^2) = (8, -1/8)$ on the Monster row).
**Igusa.** `main.tex:2092–2093`: $\nu_{\Delta_5}: \Sp_4(\Z) \to \C^\times$
with weight $5$; no $\hbar$ enters.
**Issue (Polyakov dimensional analysis).** Vol III's $\hbar$ on the
Fake-Monster row is **fixed numerically** by the lattice
($\hbar^2 = -1/8$ on Monster, $-1/50$ on Fake-Monster), determined by
the Cartan Casimir $K = 2c_+(L)$ and the Borcherds-product structure.
This is the **opposite direction** to topological-strings, where
$\hbar$ is a *free* formal Rees parameter and the Capelli shift
$\hbar N$ is a tunable normalization. If a matched-conventions
theorem ever claims a $\Phi_2$ specialization at a smooth point of K3
sends the local $\hbar$ to the Vol III Yangian $\hbar$, **the local
$\hbar$ would have to be fixed to the K3 Heisenberg level
$\kappa_{\ch}^{\Heis}(K3) = 2 = \chi(\cO_{K3})$ (Vol III
`main.tex:1349`), not free**. The local theorem proves a
$\C[[\hbar]]$-linear isomorphism (`main.tex:5459–5485`), valid for
**every** $\hbar$, and so cannot be the formal-disk specialization
of a fixed-$\hbar$ Vol III row.
**Conclusion.** The $\hbar$ used in this manuscript is not the
Vol III Yangian $\hbar$. They differ by both *role* (free vs fixed
by lattice) and *scaling axis* (deformation parameter vs spectral
parameter). The firewall correctly forbids transfer; the deeper
divergence is that even at "$d=2$" the two roles are incommensurate.
This refines W5-02 / W5-03 by adding a *parameter-space* divergence
on top of the worldsheet/BV-degree divergence.

### W3-W16-D3. $\mathfrak{gl}_N$ vs $\mathfrak{sl}_N$: scalar trace direction
**Severity 2. Status valid. Confidence high.**
**Topological-strings.** `main.tex:23, 162, 250, 359`: probes are
matrices in $\mathfrak{gl}_N$. The Capelli shift $\hbar N$ uses the
*identity* trace $\Tr(I) = N$. The center extension is the U(1) center
of $\mathfrak{gl}_N$ with character $\Tr$ (`main.tex:391`). The scalar
quotient passes from $\mathfrak{gl}_N$ to (informally) $\mathfrak{sl}_N$
via the Tr-ideal but the manuscript keeps $\mathfrak{gl}_N$ as the
ambient probe Lie algebra.
**Vol III.** `chapters/theory/cy_to_chiral.tex:7611–7616` and
`main.tex:706–712`: K3 Yangian Heisenberg generators $J_{i,n}$ with
**lattice index** $i \in \{1, \ldots, 24\}$. There is no "$N$"
cardinality of probes; the rank is fixed by the Mukai lattice rank
$24$. Vol III's natural Lie algebra of probes (when an $N$-probe
picture exists at all) is the **trace-zero** subalgebra inside the
positive-half Hall datum, not $\mathfrak{gl}$.
**Issue (Polyakov anomaly direction).** The local $[\bar c]$ class
is the U(1) center anomaly of $\mathfrak{gl}_N$. If a matched-conventions
theorem ever claims the local Capelli class is the formal-disk
specialization of a Vol III central scalar, **it must specify whether
Vol III is using the trace-full $\mathfrak{gl}$ or the trace-free
$\mathfrak{sl}$ ambient algebra of the BFN affine-Yangian
sub-quantization** (Vol III `main.tex:715`,
$Y_\hbar^\mu(\widehat{\fg})_{k=1}$). The BFN $\widehat{\fg}$ in the
ADE BFN affine-Yangian context is typically simply-laced
**simple** ($\mathfrak{sl}_N$ in the type-A case), not $\mathfrak{gl}_N$.
The Capelli class on the topological-strings side and any candidate
"BFN central scalar" on the Vol III side **live on different ambient
algebras** before any conventions are matched, and **carry different
center dimensions** ($\dim Z(\mathfrak{gl}_N) = 1$ vs
$\dim Z(\mathfrak{sl}_N) = 0$ semisimple-side).
**Recommended firewall sharpening.** Add one row to
`local-dictionary.tex` after the $[\bar c]$ row noting "the ambient
matrix Lie algebra is $\mathfrak{gl}_N$ throughout; no
$\mathfrak{sl}_N$ identification with any sister-volume central
scalar is asserted."

### W3-W16-D4. Scaling weight on the residue current
**Severity 2. Status valid. Confidence high.**
**Topological-strings.** `principles.tex:178–195`,
`local-dictionary.tex:149–157`: principal-part current
$\rho_{a,b} = z_1^{-a-1}z_2^{-b-1}\,dz_1\,dz_2$, coadjoint action
$z_1^p z_2^q \cdot \rho_{a,b} = -(pb-qa+p-q)\rho_{a-p+1,b-q+1}$.
**Vol III.** No analog of $\rho_{a,b}$ exists in Vol III. The
Mukai-lattice basis $\Lambda_{K3}$ is finite-dimensional rank $24$;
the principal-part module $\mathcal P$ is infinite-dimensional with
generators indexed by $a+b \geq 1$.
**Issue (Polyakov scaling — bidegree).** The local
$\rho_{a,b}$ has **scaling weight** $a+b+2$ in the natural torus
action $z_i \mapsto t_i z_i$ (the volume form $dz_1\,dz_2$ is weight
$1+1$, the $z_1^{-a-1}z_2^{-b-1}$ part is weight $-(a+b+2)$, and the
combined object is contravariantly a weight-$+(a+b+2)$ functional
under the naive grading lift). The Vol III Mukai pairing on
$\Lambda_{K3}$ is **degree zero in any natural grading**: it is the
Euler / Mukai pairing on a finite-rank lattice. A formal-disk
matched-conventions theorem would have to prove that the
**bidegree-graded** principal-part Tate cotangent is the
**ungraded** Mukai pairing under formal completion at a smooth
point. This is a non-trivial functoriality statement: it would
require a specific Beilinson-style $\Z$-grading vs filtration
correspondence on K3.
**No-go heuristic.** A graded continuous cotangent module on a
formal disk and an ungraded finite-rank lattice on a compact CY are
**not naturally isomorphic** as $\mathfrak h$-modules (the former is
not even a finite-dimensional module). The local theorem cannot
specialize to a Vol III statement on $\Lambda_{K3}$ without a
Hilbert-scheme integration-style passage that **breaks the bidegree
grading** (Nakajima's $\Sigma_1^{\Nakajima}$ specialization in Vol III
`main.tex:1305–1306` is exactly such a passage). The firewall is
correct; the divergence is more structural than W5 named.

### W3-W16-D5. Worldsheet not closed, no genus, no Riemann moduli
**Severity 3. Status valid. Confidence high.**
**Topological-strings.** `main.tex:74–75, 619–630`: ambient is
$\R^2 \times \C^2$ with brane defect $\R \times p$. The "worldsheet
$\Sigma$" of any global topological-string sense is **absent**;
the manuscript explicitly defines a "local string-field-theoretic"
sense and disclaims all Riemann-surface moduli (`main.tex:619–630`).
There is no $\overline{\mathcal M}_{g,n}$, no Deligne-Mumford
compactification, no string measure, no integration of correlators
over moduli.
**Vol III.** Vol III at $d=2$ uses a reference curve $C \subset X$ for
the Stage-2 specialization (`chapters/theory/cy_to_chiral.tex:4392`).
This is a **smooth algebraic curve** in K3, hence carries a Riemann
genus, an algebraic moduli, and a Hodge bundle. Vol III does not
itself integrate over $\overline{\mathcal M}_{g,n}$, but the
specialization curve $C$ has genus, while the topological-strings
brane line $\R$ does not.
**Igusa.** Modular forms of $\Sp_4(\Z)$, with **two** modular
parameters $z_1, z_2$ realizing the Siegel period $\mathbb H_2$.
There is no genus-zero or genus-one specialization to compare with the
brane line.
**Issue (Polyakov path-integral sanity).** Any putative bridge from
the local theorem to a Vol III $\Phi_2$ output, or further to an
Igusa $\Delta_5$ output, **must change the genus axis**: from
$\R$-line to algebraic curve $C \subset K3$ in Vol III, then from
$C$ to the Siegel period $\mathbb H_2$ in Igusa. **Three** worldsheet
genera are involved (none, $g(C) \geq 0$, period of rank 2). The
firewall remarks (`tate-P5-cross-volume.tex:23–31`) deny the
transfer; W16 records the explicit genus-axis count needed for any
bridge — three steps, not one.

### W3-W16-D6. Functoriality: Symp(formal disk) action does not lift to Vol III's Aut(K3)
**Severity 3. Status valid. Confidence high.**
**Topological-strings.** `main.tex:840–875`: the local Hamiltonian
construction is invariant under the formal symplectomorphism group of
$\widehat{\C^2}_0$, with substitution map $z_i \mapsto \phi_i$
equivariant. This is a **pro-algebraic** group of formal Hamiltonian
flows, infinite-dimensional. The substitution map and the Capelli
shift respect the Symp$(\widehat{\C^2}_0)$ action.
**Vol III.** K3 has a *finite* automorphism group
$\Aut(K3, \omega_{K3})$ for generic $K3$, and a finite or torus
extension when special. The Mukai lattice $\Lambda_{K3}$ has
automorphism group inside $O(\Lambda_{\mathrm{Muk}}) = O(4, 20)$,
constrained by the global Torelli theorem.
**Functoriality issue.** The formal-disk $\Symp(\widehat{\C^2}_0)$
action on the topological-strings closed sector **does not extend** to
the global $\Aut(K3)$ action on the Vol III closed sector at a smooth
point: a generic formal symplectic flow on the formal completion at
$p \in K3$ is **not** the formal completion of a global K3
automorphism. Thus any candidate functor
$F: \mathcal C_{\mathrm{loc}} \to \mathcal C_{\mathrm{Vol III}}$
sending the local Hamiltonian BF formal-disk theorem to a $\Phi_2$
output **cannot be simultaneously** $\Symp(\widehat{\C^2}_0)$-
equivariant on the source and $\Aut(K3)$-equivariant on the target.
This is a **functoriality obstruction** that W5 named less explicitly:
even the would-be "specialization to a smooth K3 point" map breaks
naturality on infinitesimal symmetries.
**Polyakov interpretation.** The disagreement is between the
infinite-dimensional Hamiltonian group on a formal disk (continuous
symmetries of a path-integral over a formal neighborhood) and the
finite Aut group on K3 (discrete global symmetries). A
matched-conventions theorem must **either restrict** the local
$\Symp(\widehat{\C^2}_0)$ action to a finite subgroup compatible with
$\Aut(K3, p)$, **or extend** $\Aut(K3, p)$ to the formal flows,
neither of which is canonical.

### W3-W16-D7. Coefficient topology: Tate vs $\Z$-graded vs cohomological-grading
**Severity 2. Status valid. Confidence high.**
**Topological-strings.** `main.tex:5240–5245`,
`appendix-factorization-current-conventions.tex` (referenced):
the topology on $\mathfrak h = \prod_{d \geq 1} H_d$ is the
product/direct-sum Tate convention — **strict colimit on
$\mathfrak h$, product completion on $\mathfrak g$**. $\mathfrak h$ is
$\Z_{\geq 1}$-graded by polynomial degree, sitting in $\Cat{TateVec}$.
Cohomological grading: the BV degrees are $|\phi_i| = 0$,
$|\psi| = -1$, $|c_f| = 1$, $|u_\rho| = 0$
(`appendix-unreduced-bv-qme.tex:13–20`).
**Vol III.** Vol III's natural categorical setting is dg/$\infty$-
categories of CY data: stable $\infty$-categories, Hochschild
homology in degree $-d$ (`chapters/theory/cy_to_chiral.tex:385,
H3 hypothesis`). The coefficient topology is the **smooth/proper**
condition (Vol III `H1`); Tate-vector spaces with strict
colimit/product topology do not enter.
**Igusa.** Coefficients are `weight-$k$ Siegel modular forms` valued
in $\C$, no Tate structure.
**Functoriality issue.** A would-be functor from
$\Cat{TateVec}_{\mathrm{strict}}$ to $\dgCat^{\sm,\proper}$ (Vol III)
must specify **how** the Tate strict-colimit data on
$\mathfrak h$ is realized as a smooth-proper dg category. The natural
translation (taking finite truncations $\mathfrak h_{\leq N}$ and
viewing them as objects of $\dgCat$) **is not full**: it lands in
the finite-truncated locus, exactly where the M-01 conilpotency
hypothesis holds. The Tate-conilpotency / weighted regulator
machinery T1–T5 lives **outside** the Vol III smooth-proper
hypothesis. Hence any matched-conventions transfer at $d=2$ would
have to choose: either the Vol III statement on K3 specializes to the
nilpotent-truncated $\mathfrak h_{\leq N}$ (in which case the
unweighted regulator-independence is a separate axis Vol III does not
address), or the Tate-conilpotency repair lives outside Vol III's
hypothesis class altogether.
**Recommended firewall sharpening.** Add to the Vol III
template (`tate-P5-cross-volume.tex:94–100`) one bullet: "specify
whether the Vol III hypothesis admits Tate-strict colimits or only
smooth-proper dg objects; in the latter case, the topological-strings
input must be the truncation $\mathfrak h_{\leq N}$."

### W3-W16-D8. Sign convention on the cyclic / trace pairing
**Severity 1. Status valid. Confidence medium.**
**Topological-strings.** `main.tex:108`:
$S_\partial = \int_\R \Tr(\phi_1\,d\phi_2 + A[\phi_1,\phi_2])$.
The primitive sign is **$+\Tr(\phi_1\,d\phi_2)$**, not
$-\Tr(\phi_2\,d\phi_1)$. The moment map is
$\mu_\epsilon = -\Tr(\epsilon[\phi_1,\phi_2])$ (`main.tex:97`).
**Vol III.** The Mukai pairing
$\langle (r,c,s),(r',c',s')\rangle_{\Muk} = c\cdot c' - rs' - r's$
(Igusa `main.tex:3923–3925`) carries a *minus* sign on the
rank-stalk pairing.
**BCOV (Bershadsky-Cecotti-Ooguri-Vafa, cited at
`main.tex:170–174, 690–697`).** BCOV's natural negative-cyclic CY pairing
on $\PV^\bullet(X)$ is $\langle\alpha,\beta\rangle_{\CY} =
\int_X (\alpha \wedge \beta) \cdot \Omega_X$, with sign convention
fixed by the choice of holomorphic volume form $\Omega_X$.
**Issue (Polyakov path-integral sanity).** The topological-strings
primitive $\Tr(\phi_1\,d\phi_2)$ has sign opposite to a
"BCOV-symmetric" $\frac12(\Tr(\phi_1\,d\phi_2) - \Tr(\phi_2\,d\phi_1))$
choice. Either is consistent within the local theorem, but if a
matched-conventions theorem ever pulls the local symplectic primitive
through to a Vol III / BCOV CY pairing, **the sign normalization on
the volume form $\Omega$ must be tracked**. This is editorial only
within topological-strings; cross-volume it must be named.

---

## §4. Functoriality verification (T3)

For each candidate cross-volume identification I attempted to write
down the functor $F$ explicitly and check whether it commutes with
relevant automorphism actions. None of the identifications below are
*asserted* in the manuscript; the firewall denies them. The point is
that even as **templates** for a future matched-conventions theorem,
many proposed bridges fail naturality.

### F1. "Local $[\bar c]$ ↔ Vol III BFN central scalar"
**Source category.** Tate-Lie algebras with U(1) center anomaly
class $[\bar c] \in H^2_{\Lie}(\bar A, \C)$ (one-dimensional).
**Target category.** Vol III BFN affine-Yangian
$Y_\hbar^\mu(\widehat{\fg})_{k=1}$ ADE central scalars
(`main.tex:715`).
**Naturality test.** The local $[\bar c]$ is invariant under
$\Symp(\widehat{\C^2}_0)$ (a continuous infinite-dimensional group);
the BFN central scalars are invariant under the finite Weyl group of
$\widehat{\fg}$. A would-be intertwiner $F([\bar c]) = $ "BFN central
scalar" cannot be both $\Symp$-equivariant and $W(\widehat{\fg})$-
equivariant simultaneously.
**Verdict.** Functoriality fails on automorphism groups. The local
$[\bar c]$ is **not** the BFN central scalar under any natural
intertwining.

### F2. "Local Capelli $\hbar N$ ↔ Vol III Heisenberg level $k$ on K3"
**Source.** $\hbar N$ for $N \to \infty$ in topological-strings.
**Target.** $\kappa_{\ch}^{\Heis}(K3) = 2$ in Vol III
(`main.tex:1349`); or the Mukai-Heisenberg R-matrix
$R(u) = (u + \hbar P)/(u + \hbar)$ (`main.tex:709`).
**Naturality test.** $N \to \infty$ is the topological-strings
**stable** large-$N$ limit (conjectural;
`main.tex:493–498`). Vol III's $\kappa_{\ch}^{\Heis}(K3) = 2$ is a
**categorical Euler-characteristic supertrace**, fixed and finite.
A would-be functor sending the local stable limit to the Vol III
fixed value would have to **either fix $N = 2/\hbar$** (specifying a
preferred quantization) or **wash out the dependence on $N$** by a
universal renormalization. Neither is canonical.
**Polyakov check.** $\hbar N$ is a *quantization parameter*;
$\kappa_{\ch}^{\Heis}$ is a *categorical invariant* (Hodge supertrace).
They have **different scaling weights** under the would-be matching.
**Verdict.** Functoriality fails on scaling axis. The local
Capelli shift and Vol III's $\kappa_{\ch}^{\Heis}$ are not natural
correspondents.

### F3. "Local Moyal/Weyl quantization ↔ Vol III deformation
quantization on K3"
**Source.** $f * g = m \circ \exp(\frac{\hbar}{2} P)(f\otimes g)$ on
$\widehat{\C^2}_0$ (`main.tex:5398–5402`).
**Target.** Vol III at $d=2$: degree-$(-1)$ Schouten-Nijenhuis
bracket on $\HH^\bullet(D^b\Coh(K3)) \cong \PV^\bullet(K3)$
(`chapters/theory/cy_to_chiral.tex:4452–4464`).
**Naturality test.** Kontsevich's formality theorem provides an
$L_\infty$-quasi-isomorphism on each formal completion. The
**global** formality on K3 then assembles via
Costello-Gwilliam-Li locality. The local Moyal product is **the
formal-disk piece** of this assembly. As long as the formal-disk
sign and parameter normalizations agree
(W3-W16-D2: they do not; $\hbar$ is fixed in Vol III), the
underlying formal-disk algebra **is** the local theorem.
**Polyakov check.** Both sides are deformation quantizations of a
holomorphic symplectic surface. The scaling axis matches in the
formal-disk localization — provided the $\hbar$ normalization is
adjusted.
**Verdict.** Functoriality holds at the formal-disk level, **conditional
on $\hbar$ normalization matching**. This is the closest thing to a
genuine cross-volume identification. The matched-conventions
theorem template at `tate-P5-cross-volume.tex:108` would need to
specify the $\hbar$-normalization morphism explicitly. Currently
not asserted; this is the most promising bridge.

### F4. "Local $P_0$ derived centre ↔ Vol III $E_2$-chiral output"
**Source.** $Z^{P_0}_{\fact}(\Obs^{\cl}_{\open})$ with strict
$P_0$ bracket (`principles.tex:65–66`).
**Target.** $\Phi_2(D^b\Coh(K3)) \in E_2$-Hol-FA on K3
(`chapters/theory/cy_to_chiral.tex:4392`).
**Naturality test.** The $P_0$-Poisson centre and the $E_2$-chiral
factorization output are **Koszul-dual** in the standard
Lurie/Costello-Gwilliam dictionary, with degree shift $1-d = -1$ at
$d=2$. So $P_0 \mapsto P_1 = E_2$-Koszul-dual lives in degree $-1$
relative to $P_0$. Functoriality holds at the **operadic-degree**
level conditional on the Koszul-duality bookkeeping being uniform.
**Verdict.** This is W5-03 restated. The conventional firewall is
correct: the two answer **different categorical questions** (Poisson
centre vs $E_2$-Koszul dual). They are not natural correspondents
without a separate Koszul-dual functor inserted.

### F5. "Local Matlis principal-part $\mathcal P$ ↔ Vol III Mukai
lattice $\Lambda_{K3}$"
**Source.** $\mathcal P = \bigoplus_{a+b > 0} \C\rho_{a,b}$,
infinite-dimensional, $\Z_{\geq 1}^2$-graded.
**Target.** $\Lambda_{K3} = H^*(K3, \Z)$ with Mukai pairing,
finite-rank $24$, ungraded as a lattice.
**Naturality test.** No natural functor exists. The dimensions do
not match (infinite vs $24$). The grading axis (bidegree
$\Z^2_{\geq 1}$ on $\mathcal P$, no grading on $\Lambda_{K3}$ as a
lattice) does not match. The natural action ($\widehat{\mathfrak h}$
on $\mathcal P$ vs $W_{\Lambda_{K3}}$ on $\Lambda_{K3}$) does not
match.
**Verdict.** No candidate functor between these two objects.
Anyone proposing a transfer at this site has nothing to draft.

### F6. "Igusa $\Delta_5$ ↔ topological-strings generating function"
**Source.** Local Moyal coefficients
$C^{a,b}_{(p,q),(r,s)}$ (e.g. $C^{1,1}_{(2,0),(0,2)} = 4$,
`main.tex:2522`); first / third Costello graph normalizations.
**Target.** $\Delta_5(2Z) = 64 \cdot \den(\fg_{\Delta_5})$
(Igusa `main.tex:2287`); $\Delta_5 \in M_5(\Sp_4(\Z), \nu_{\Delta_5})$.
**Naturality test.** Both are in different categories of generating
functions (formal Moyal coefficient on a formal disk vs Siegel
modular form on $\mathbb H_2$). No candidate intertwiner exists at
the level of generating series. The Borcherds singular-theta lift
goes from a weak Jacobi form $\phi_{0,1}$ to $\Delta_5$ on the global
side; topological-strings has no Jacobi form input (no elliptic
curve, no Eisenstein series, no $\phi_{0,1}$).
**Verdict.** Heuristic-only bridge. Confirmed W5-07. To make this
proof-grade requires generating a Jacobi-form input from the local
theorem, which the local theorem does not contain. See §5 below.

---

## §5. BKM bridge to Igusa $\Delta_5$ — exact precision

The CLAUDE.md statement (W16's `repo-local`):
> "Modular-form frontier: generating functions in topological-string
> theory motivate comparison with the Igusa cusp form $\Delta_5$ in
> `~/igusa-cusp-form` via the Borcherds / BKM route. This is a
> heuristic and convention-checking bridge here, not a BKM consequence
> of the local Hamiltonian BF/Moyal calculation."

W16's audit confirms this is correct and identifies **what would
have to be supplied** to make the bridge proof-grade:

### 5.1 Required inputs to upgrade heuristic to theorem

To run a Borcherds singular-theta lift one needs:
1. **A weak Jacobi form $\phi$ of weight 0 and index $L$.**
   The Igusa $\Delta_5$ comes from $\phi_{0,1}^{K3}$, the K3 elliptic
   genus (Igusa `main.tex:2284, 2297`; Eichler-Zagier 1985). The
   local theorem **has no elliptic curve** anywhere in scope (no
   $E$ factor, no $\tau$ modular parameter, no Jacobi specialization
   axis). To produce a $\phi_{0,1}$-equivalent from the local theorem
   one would have to **fiber the local Hamiltonian BF over an elliptic
   curve** — exactly the move forbidden by `tate-P5-cross-volume.tex:71`
   (no global $E$ or $K3 \times E$ construction).
2. **An even lattice $L$ of signature $(n, 2)$ with $n \leq 25$.**
   The local theorem operates on the formal symplectic
   disk's Tate cotangent module; this is **not a finite-rank lattice**
   and has signature $(\infty, 0)$ in any natural completion. To
   produce a finite-rank lattice from the local theorem one would have
   to truncate the Tate module to a finite jet — but the obstruction
   M-09 / W3-W16-D7 says the conilpotent truncation
   $\mathfrak h_{\leq N}$ has different homology behavior than the
   unweighted limit.
3. **A reflective Weyl chamber.** Vol III
   `chapters/theory/cy_to_chiral.tex:7611–7616` requires
   the Borcherds-Kac-Moody Cartan matrix to be *reflective* and
   *symmetrizable*. The local theorem has neither a Cartan matrix
   nor a Weyl chamber.
4. **A super-Etingof-Kazhdan quantization.** Vol III
   `chapters/theory/cy_to_chiral.tex:7616` requires a
   $U_\hbar\mathfrak g$ quasi-Hopf super structure on the BKM. The
   local theorem produces a $\C[[\hbar]]$-linear Moyal/Weyl algebra
   on the formal disk; this is **not** a quasi-Hopf super-bialgebra.

### 5.2 Compatibility check

If, hypothetically, all four inputs were supplied (which they are
not), would the local Hamiltonian BF construction be **compatible**
with a BKM lift? The check has three subparts:

- **a) Lattice signature.** The local symplectic form
  $\omega = dz_1 \wedge dz_2$ on $\widehat{\C^2}_0$ is signature
  $(0, 2)$ when "complexified" naively, **wrong direction** for the
  Borcherds $(n, 2)$ requirement: BKM lifts go from signature
  $(n, 2)$ Jacobi forms; the formal disk side has the opposite-sign
  contribution. A BKM-compatible local theorem would need to be on a
  $(\C^2)^* \times \C^2$-style indefinite formal symplectic structure.
  This is **incompatible with the local symplectic disk as written**.

- **b) Modular weight.** The local Capelli shift $\hbar N$ has no
  natural modular weight. A BKM-compatible bridge would have to
  produce a modular weight from the local theorem. The natural
  candidate ($\hbar^k N^k$ in the Moyal expansion at order $k$) does
  **not** carry a modular transformation; it carries a Rees grading.
  These are **different gradings** (Rees $\Z_{\geq 0}$ vs modular
  weight under $\SL_2(\Z) \subset \Sp_4(\Z)$).

- **c) Imaginary-root multiplicities.** Vol III
  `chapters/theory/cy_to_chiral.tex:1593`:
  $\mathrm{mult}(\alpha) = c_{\phi_{0,1}}(-\frac12(\alpha,\alpha),\ell_\alpha)$.
  These are *integer multiplicities* read from a Jacobi-form
  Fourier expansion. The local theorem produces *Moyal coefficients*
  $C^{a,b}_{(p,q),(r,s)}$ which are rational numbers, not integer
  Fourier coefficients of a weak Jacobi form.
  **Incompatible without a non-trivial integer-summing operation
  (e.g. graded Euler characteristic on a virtual derived
  intersection).**

### 5.3 Verdict on the BKM bridge

**The local Hamiltonian BF / Moyal construction is not BKM-compatible
as written.** Three independent compatibility failures:
- (a) lattice signature wrong direction;
- (b) Rees grading is not modular weight;
- (c) Moyal rationals are not Jacobi-form integer coefficients.

The bridge's heuristic value is in the *qualitative* observation that
both calculations exhibit infinite-product / generating-function
behavior. To make it proof-grade requires constructing the four
missing inputs (Jacobi form, lattice, Weyl chamber, EK
super-quantization) **from outside** the local theorem, then proving a
matched-conventions theorem. None of these exist; the firewall is
correctly tight.

**Recommended sharpening of the Igusa/BKM template
(`tate-P5-cross-volume.tex:108–115`).** Add three explicit
preconditions before "primitive recognition theorem":
- specify the Jacobi-form input and the elliptic curve $E$ on which it lives;
- specify the lattice, its signature, and the Weyl chamber;
- specify the EK super-quantization or equivalent Hopf structure.

Without these, the template is a list of names, not a falsifiable
matched-conventions hypothesis.

---

## §6. Invariants that must agree (T2)

The following invariants are **sub-volume invariants** of the
mathematical objects on each side. If a matched-conventions theorem
ever exists, they must agree under it. The manuscript firewall
denies the theorem; W16's job is to record what would have to match.

### MA-1. Schouten-Nijenhuis bracket sign on linear coordinates
Both sides agree numerically: $\{z_1, z_2\} = +1$
(topological-strings `appendix-unreduced-bv-qme.tex:24`;
Vol III `chapters/theory/hochschild_calculus.tex:692`).
**Verified:** sign convention compatible.
**Caveat:** see W3-W16-D1 — the polyvector grading on the
Vol III side carries an additional axis the topological-strings
side does not; sign is correct only at the linear level.

### MA-2. $\hbar$-expansion parity
Topological-strings: Moyal star commutator is **odd** in $\hbar$
(`main.tex:5409–5417`); even orders vanish.
Vol III: the BFN affine-Yangian uses the standard $\hbar$-expansion
where the R-matrix $R(u) = 1 + \hbar r(u) + O(\hbar^2)$ has nonzero
even-$\hbar$ contributions in general (Yangian normalization).
**Disagreement.** Star-commutator parity (odd $\hbar$ only) is a
*Weyl-Moyal-specific* convention; Yangian/BFN expansions have both
parities. A matched-conventions theorem would have to identify
which parity convention is used **and renormalize even orders**.
**This is a NEW divergence not in W5.**
Severity 2.

### MA-3. Capelli central charge
Topological-strings: Capelli $\hbar N$, normal-ordering shift
$Y_\hbar X_\hbar - X_\hbar Y_\hbar = \hbar N + O(\hbar^3)$
(`main.tex:441`).
Vol III at K3: $\kappa_{\ch}^{\Heis}(K3) = 2$ (`main.tex:1349`),
which is a Hodge-supertrace categorical invariant.
Igusa: $\kappa_{\BKM}(\Delta_5) = 5$ (Vol III `main.tex:1311`).
**These are three different objects.** $\hbar N$ is a **quantization
parameter**, $\kappa_{\ch}^{\Heis}$ is a **Hodge supertrace**,
$\kappa_{\BKM}$ is a **modular-form weight identity**. They are not
candidates for the same invariant despite all being "central
charges" in some loose sense.
**Verified divergent.** No matched theorem could equate them
without separate constructions. This is W5-05 restated.

### MA-4. Hodge supertrace vs reduced-disk Euler characteristic
Topological-strings: the formal disk has no Hodge structure (no
compact CY). The natural "Euler characteristic" of the Tate
cotangent module $\mathcal P$ is **divergent** (infinite rank).
Vol III: $\kappa_{\ch}(K3) = \chi(\cO_{K3}) = 2$ via Hodge supertrace
(`main.tex:1303`). $\kappa_{\cat}(K3 \times E) = 0$
(`main.tex:1411`).
**No identification.** The Tate cotangent's divergent rank is **not**
the Vol III Hodge supertrace. A formal-disk specialization of K3 at
a smooth point has Hodge structure 1 (only $H^0$ contributes
locally); the Tate cotangent is genuinely infinite-rank.
**This is a NEW divergence not in W5.**
Severity 2. Cross-walk: refines W5-04.

### MA-5. Cyclic CY pairing degree
Topological-strings: no CY pairing.
Vol III at $d=2$: cyclic CY pairing in degree $-2$
(`chapters/theory/cy_to_chiral.tex:385` H3 hypothesis).
BCOV: cyclic pairing on $\PV^\bullet(X)$ in degree $-d$ via
$\Omega_X$ (`main.tex:170–174` cites BCOV).
**Verified:** divergent; W5-04 covers this. W16 records that the
**degree** of the pairing ($-d$) on the Vol III side has no
counterpart in the topological-strings side (the local theorem
operates in degrees driven by BV: $|\psi| = -1$, $|c_f| = 1$,
$|u_\rho| = 0$).

---

## §7. New residuals (T5)

W16 identifies eight new candidate cross-volume divergences and three
new "must-agree-under-future-bridge" invariants. The complete W16
residual list, cross-walked against existing R-W5 residuals and
master ledger entries:

### R-W3-W16-A (cross-walks W5-02, W5-03, W5-04)
**Statement.** The Polyakov dimensional analysis of $\hbar$
(W3-W16-D2), the $\mathfrak{gl}_N$ vs $\mathfrak{sl}_N$ ambient
(W3-W16-D3), and the bidegree-graded principal-part vs ungraded
Mukai (W3-W16-D4) are **structural divergences not silently
reconciled**. They strengthen the firewall in
`tate-P5-cross-volume.tex` by adding three **explicit** convention
items that any matched-conventions theorem must specify.
**Severity.** 2 (editorial sharpening).
**Recommended action.** Add three bullets to the Vol III template
(`tate-P5-cross-volume.tex:94–100`):
- "specify the polyvector slot of each generator under the proposed
  $\theta^i \leftrightarrow z_i$ correspondence";
- "specify whether the local $\hbar$ is the free Rees parameter or
  fixed by a Cartan invariant (e.g.\ Vol III's
  $\hbar^2 = -1/(2c_+(L))$ on Fake-Monster);"
- "specify whether the ambient matrix Lie algebra is
  $\mathfrak{gl}$ or $\mathfrak{sl}$, and whether the U(1) center is
  carried."
**Status.** Proposal-only.

### R-W3-W16-B (cross-walks W5-05)
**Statement.** Functoriality of all six candidate cross-volume
identifications (F1–F6 in §4) was checked. Only F3 (formal-disk
deformation quantization $\leftrightarrow$ Vol III formal-disk
$\PV$ structure) survives, and only **conditional on the
$\hbar$-normalization**. F1, F2, F4, F5, F6 fail naturality at
either the automorphism-group level (F1, F6), scaling axis
(F2, F4), or dimension-counting (F5).
**Severity.** 2 (deepens W5-05 by giving explicit functoriality
counterexamples for each candidate identification).
**Recommended action.** Document in `tate-P5-cross-volume.tex` an
additional remark stating: "every cross-volume identification
template above must verify naturality under
$\Symp(\widehat{\C^2}_0)$ on the local side and the corresponding
sister-volume automorphism action; this manuscript verifies no
such naturality."
**Status.** Proposal-only.

### R-W3-W16-C (extends W5-07)
**Statement.** The BKM bridge to Igusa $\Delta_5$ has **three
specific compatibility failures** (§5.2): wrong-direction lattice
signature, Rees grading not modular weight, Moyal rationals not
Jacobi integers. These are **not editorial**; they are structural
incompatibilities that no matched-conventions theorem can paper
over without changing the local theorem itself (e.g.\ replacing
$\widehat{\C^2}_0$ with an indefinite-signature formal CY).
**Severity.** 3 (structural). The bridge is heuristic in a
**stronger sense** than W5 named: not just unproved but
**incompatible** with the local construction as written.
**Recommended action.** Sharpen the Igusa/BKM template
(`tate-P5-cross-volume.tex:108–115`) by adding the three failure
modes as explicit preconditions; alternatively, demote the
"BKM/Igusa frontier" mention in CLAUDE.md from "convention-
checking bridge" to "structural-incompatibility advisory".
**Status.** Proposal-only.

### R-W3-W16-D (NEW — not in W5)
**Statement.** The $\Symp(\widehat{\C^2}_0)$ formal symplectomorphism
group action on the topological-strings closed sector
(`main.tex:840–875`) **does not extend** to the global $\Aut(K3)$
action on the Vol III closed sector. This is a functoriality
obstruction at the level of infinitesimal symmetries: a generic
formal Hamiltonian flow at $p \in K3$ is not the formal completion
of a global K3 automorphism. Hence even the would-be
"local-to-K3-at-a-smooth-point" specialization breaks naturality.
**Severity.** 3 (genuine functoriality obstruction).
**Recommended action.** Add to
`lem:no-formal-disk-transfer` (`tate-P5-cross-volume.tex:56–76`)
one sentence: "Furthermore, any candidate specialization of the
local theorem to a smooth-point completion of K3 cannot be
simultaneously $\Symp(\widehat{\C^2}_0)$-equivariant and
$\Aut(K3)$-equivariant: generic formal symplectic flows at
$p \in K3$ are not formal completions of global automorphisms."
**Status.** Proposal-only.

### R-W3-W16-E (NEW — not in W5)
**Statement.** $\hbar$-expansion parity disagreement (MA-2).
Topological-strings Moyal star commutator is **odd** in $\hbar$
(even orders identically zero). Vol III BFN affine-Yangian and
Mukai-diagonal R-matrices generally have **both** parities. A
matched-conventions theorem at $d=2$ at the formal disk would have
to specify which parity convention is operative and how the
even-$\hbar$ terms are renormalized.
**Severity.** 2.
**Recommended action.** Optional firewall-sharpening note in
`tate-P5-cross-volume.tex` Vol III template: "specify the
$\hbar$-parity convention; topological-strings uses Moyal-Weyl
odd-$\hbar$, Vol III generally uses both."
**Status.** Proposal-only.

### R-W3-W16-F (NEW — not in W5)
**Statement.** Hodge-supertrace direction (MA-4).
The Tate cotangent module $\mathcal P$ has divergent rank; Vol III's
$\kappa_{\ch} = \chi(\cO_X)$ (Hodge supertrace) is finite. A
formal-disk specialization at a smooth point has Hodge supertrace
$1$ (only $H^0$ contributes locally), not the global K3 supertrace
$2$. Hence no matching of the local theorem's Tate cotangent rank
to Vol III's $\kappa_{\ch}^{\Heis}(K3)$ is possible, even as a
"specialization at a smooth point": the local rank is divergent,
the smooth-point Hodge value is $1$, and the global K3 value is
$2$.
**Severity.** 2 (refines W5-04 by giving the explicit count
mismatch: $\infty$ vs $1$ vs $2$).
**Recommended action.** Add to `tate-P5-cross-volume.tex:94–100`
one bullet: "specify the categorical invariant being matched
($\kappa_{\ch}, \kappa_{\cat}, \chi(\cO_{p}), \mathrm{rank}\,\mathcal P$);
the topological-strings side has no global Hodge supertrace, only
the local Tate cotangent rank, which is divergent."
**Status.** Proposal-only.

---

## §8. Summary verdict

The wave-2 W5 catalog is **complete in spirit**: every cross-volume
overreach is firewalled, no silent reconciliation is identified, and
every named divergence is correctly disclaimed. W16 confirms this by
running an independent attack along Polyakov + Functoriality.

W16 adds **eight** new candidate divergence sites
(W3-W16-D1 through D8), three of which are **structural**
(D2, D5, D6) and five of which are **conventional sharpenings**
(D1, D3, D4, D7, D8). These do not falsify the W5 verdict; they
**deepen** the firewall by naming additional dimensions on which a
matched-conventions theorem must specify data.

W16 verifies the BKM bridge to Igusa $\Delta_5$ is **structurally
incompatible** with the local Hamiltonian BF / Moyal construction as
written: three independent compatibility failures
(lattice signature, Rees vs modular weight, Moyal rationals vs Jacobi
integers). The bridge is heuristic in the strong sense that no
single matched-conventions theorem could close it without altering
the local theorem itself.

W16 verifies functoriality of all six candidate cross-volume
identifications (F1–F6 in §4). Only one (F3, formal-disk
deformation quantization) survives even as a candidate, and only
conditional on $\hbar$-normalization matching. The other five fail
naturality at the level of automorphism actions, scaling axis, or
dimension counting.

The Polyakov + Functoriality lens finds **no path-integral
pathology** in the local theorem, **no hidden scaling violation**,
and **no preserved-quantity collision** with Vol III or Igusa. The
manuscript is, by every test W16 applied, free of cross-volume
overreach. The deeper divergences identified are all structural
features of the *would-be* matched-conventions theorem, not defects
of the local construction.

The recommended editorial sharpenings (R-W3-W16-A, B, C, D, E, F)
add precision to the firewall but do not change the verdict that
the firewall is intact.

---

## §9. Ledger entries (W16)

| ID | Severity | Lens | Status | Provenance |
|---|---|---|---|---|
| W3-W16-D1 | 2 | Polyakov | new | `appendix-unreduced-bv-qme.tex:24`; Vol III `chapters/theory/hochschild_calculus.tex:692` |
| W3-W16-D2 | 3 | Polyakov | new | `main.tex:5398–5408, 5459–5485`; Vol III `main.tex:679–688, 790–803` |
| W3-W16-D3 | 2 | Polyakov | new | `main.tex:23, 162, 250, 359, 391`; Vol III `main.tex:706–712, 715` |
| W3-W16-D4 | 2 | Polyakov | new | `principles.tex:178–195`; Vol III `main.tex:1349, 1411` |
| W3-W16-D5 | 3 | Polyakov | new | `main.tex:74–75, 619–630`; Vol III `chapters/theory/cy_to_chiral.tex:4392`; Igusa `main.tex:2092–2093` |
| W3-W16-D6 | 3 | Functoriality | new | `main.tex:840–875`; Vol III `main.tex:706–712` (Aut(K3) implicit in Mukai-rank-24 statement) |
| W3-W16-D7 | 2 | Functoriality | new | `main.tex:5240–5245`; Vol III `chapters/theory/cy_to_chiral.tex:385` H1–H3 |
| W3-W16-D8 | 1 | Polyakov | new | `main.tex:108, 97`; Igusa `main.tex:3923–3925`; BCOV cited at `main.tex:170–174, 690–697` |
| R-W3-W16-A | 2 | both | proposal | cross-walk W5-02, W5-03, W5-04 |
| R-W3-W16-B | 2 | Functoriality | proposal | cross-walk W5-05; new functoriality verdicts F1–F6 |
| R-W3-W16-C | 3 | Polyakov | proposal | extends W5-07 with three structural compatibility failures |
| R-W3-W16-D | 3 | Functoriality | new | not in W5 |
| R-W3-W16-E | 2 | Polyakov | new | not in W5 |
| R-W3-W16-F | 2 | Polyakov | new | not in W5 |

End W16 ledger.
