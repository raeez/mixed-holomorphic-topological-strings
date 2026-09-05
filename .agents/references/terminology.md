# Terminology and prose

Read when introducing terms or revising mathematical prose.
The repository writing standards govern the research register. Paths refer to the repository root.

## The four-part test for new terms

Before introducing any new term, run the four-part test of §III of the writing standards. **All four must hold.**

1. **Scope.** No accepted term in algebra, geometry, number theory, homotopy theory, or mathematical physics covers the construction, even when those fields are searched together. *Most coinings fail here.*
2. **Material.** The object is a precise mathematical object — category, complex, sheaf, operad, algebra, functor, morphism, class, characteristic, integral, structure constant. Not an attitude, methodology, or slogan.
3. **Subject.** Etymology and form match the mathematical register: Greek/Latin roots, named after discoverer or operative property, or composition with accepted prefixes (chiral-, derived-, factorization-, modular-, shifted-, twisted-, completed-, filtered-, perfect-, virtual-).
4. **Necessity.** The construction requires a distinct name. Use standard prose when it describes the object precisely.

A term failing any of (1)–(4) is **branding**, deleted on sight.

### Examples passing all four
- *factorization algebra* — forced by locality structure (Beilinson–Drinfeld).
- *Maurer–Cartan element* — named after discoverer; forced by integrability.
- *shifted symplectic structure* — accepted prefix; forced by degree shift.
- *Borcherds product* — named after discoverer; forced by multiplicative lift.
- *chiral Hochschild cochain* — accepted prefixes; forced by chiral OPE.
- *derived chiral centre* — accepted prefixes; forced by open-closed centre construction.

### Examples failing
- *matrix microscope, brane microscope, matrix probe* — fail (1): "trace measurement" suffices; fail (2): name a methodology, not an object; fail (3): evocative metaphor; fail (4): "trace measurement on the derived zero fibre" names the object precisely. Replace with "trace measurement" or "$J(f) = \mathrm{Tr}\,f(\phi_1, \phi_2)$" or "Dirac brane formal-stalk chart."
- *magic identity* — every identity has a name; cite WDVV, Bianchi, Jacobi, holomorphic anomaly, residue.
- *inner music, X spine, secret weapon* — fail all four; delete and state the structure.

When generating prose, theorem statements, or replacement abstracts, run the four-part test before any candidate term is inscribed.

---

## Standard terminology by subfield

The default; deviation requires the four-part test.

### Algebra and homological algebra

Lie / dg Lie / $L_\infty$-algebra. **Maurer–Cartan element**, MC equation, MC space, deformation functor. Hochschild cochain complex $C^\bullet(A, A)$ with **Gerstenhaber bracket** and **cup product**; Hochschild cohomology $HH^\bullet$; Hochschild homology $HH_\bullet$; **negative-cyclic** $HC^-_\bullet$; **periodic cyclic** $HP_\bullet$. **Chevalley–Eilenberg** complex $C^\bullet_{\mathrm{CE}}(\mathfrak{g}, M)$ — write out at first use. Koszul duality, complex, resolution. Bar construction $B$, cobar $\Omega$, twisting morphism. **Batalin–Vilkovisky (BV)**, classical / quantum master equation (CME / QME), BV bracket $\{-,-\}$, BV Laplacian $\Delta$. **Operad**, cooperad, $E_n$-operad, little $n$-disks, framed little disks, **Swiss-cheese operad** (Voronov; topological). **Factorization algebra** (Beilinson–Drinfeld, Costello–Gwilliam) — *not* a synonym for vertex algebra or chiral algebra. **Vertex algebra**, **vertex operator algebra (VOA)**, **chiral algebra** — distinguish: vertex algebra carries OPE on a formal disk; chiral algebra carries the right $\mathcal{D}$-module on a curve $C$. Drinfeld centre $Z(\mathcal{C})$, derived centre $Z^{\mathrm{der}}$, chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}$ — distinguish.

The bar complex is *not* a centre. Bar/cobar classifies twisting morphisms. The acting bulk is the derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(A) \simeq C^\bullet_{\mathrm{ch}}(A, A)$.

### Geometry

**Calabi–Yau** (always with diaeresis on the second i). Distinguish *$d$-Calabi–Yau category* (Kontsevich–Soibelman; non-degenerate negative-cyclic trace $HC^-_d(\mathcal{A}) \to k$) from *Calabi–Yau $d$-fold* ($K_X$ trivial). **Holomorphic symplectic** ($\omega \in \Omega^2$ closed, non-degenerate) versus **holomorphic volume form** (section of $K_X$) — not interchangeable. Hodge structure, mixed Hodge structure, variation of Hodge structure (VHS), period map. Moduli stack, derived moduli stack, derived intersection, derived zero locus $\mu^{-1}_{\mathrm{der}}(0)$. Kodaira–Spencer map, Tian–Todorov lemma, **BCOV theory** (Bershadsky–Cecotti–Ooguri–Vafa, 1993–94 — spell out at first use). Holomorphic anomaly equation: precise sign convention is binding. Threefold, fourfold, $n$-fold for complex dimension $n$. Perfect obstruction theory, virtual fundamental class $[X]^{\mathrm{vir}}$, virtual structure sheaf. **Donaldson–Thomas (DT)**, **Pandharipande–Thomas (PT)**, **Gromov–Witten (GW)**, **Maulik–Nekrasov–Okounkov–Pandharipande (MNOP)**.

The Dirac brane stack at $N$ branes is the derived commuting variety $[\mu^{-1}_{\mathrm{der}}(0) / \mathrm{GL}_N]$.

### Number theory and modular forms

Modular form, Siegel modular form, Hilbert modular form, automorphic form, Maass form. Borcherds product, theta lift, Saito–Kurokawa, Ikeda, Yoshida, Gritsenko lifts. **Igusa cusp form** $\Phi_{10} = \chi_{10}$ — *not* "$\Delta_5$" without prior definition; "$\Delta_5$" is a working handle for $\Phi_{10}^{1/2}$ or the level-five BKM denominator depending on convention; specify. **Borcherds–Kac–Moody (BKM) algebra**, denominator formula, Weyl–Kac character formula. Eisenstein series $E_k$, cusp form, CM point, Hecke operator, L-function. **CHL (Chaudhuri–Hockney–Lykken) model**, CHL point, dyonic invariant.

### Homotopical and $\infty$-categorical

$\infty$-category — always with the $\infty$ symbol; never spelled "infinity-category" inconsistently. Stable $\infty$-category, dg category, $A_\infty$-category, cyclic $A_\infty$-category. Homotopy colimit / limit, derived functor, (co)fibration, mapping space, adjunction. $\infty$-operad, dendroidal $\infty$-category, coloured operad. **Factorization homology** $\int_M \mathcal{A}$ (Lurie; Ayala–Francis). Pro-object, ind-object, **pro-Matlis**.

### Physics

Topological string, A-model, B-model, mirror symmetry. **Worldsheet $\Sigma$** (always Greek $\Sigma$; never "WS"). Target $X$. Mapping space $\mathrm{Map}(\Sigma, X)$. Moduli of curves $\overline{\mathcal{M}}_{g, n}$. Brane, D-brane, boundary condition, boundary state, boundary vacuum. BPS state, BPS index, BPS spectrum. Genus expansion $\sum_{g \geq 0} g_s^{2g - 2} F_g$; string coupling $g_s$; $\hbar$ for the QFT loop expansion. **Distinguish $g_s$ and $\hbar$.** Large-$N$, 't Hooft expansion, 't Hooft coupling $\lambda = g_{\mathrm{YM}}^2 N$. Open–closed, bulk–boundary, open-closed map, bulk-boundary OPE. **Chern–Simons** (3d, 3d holomorphic, 6d holomorphic), Witten genus, elliptic genus. **OPE** (operator product expansion), stress tensor $T(z)$, central charge $c$ or $\kappa$. Anomaly: distinguish gauge / global / 't Hooft / mixed / parity; specify the anomaly polynomial. Holomorphic twist, topological twist, $\Omega$-background, Nekrasov partition function.

---

## Forbidden patterns (catalogue with replacements)

§V of the writing standards is authoritative. Common offenders to delete on sight:

| pattern | replacement |
|---|---|
| matrix microscope, brane microscope, matrix probe | trace measurement, Dirac brane formal-stalk chart |
| platonic ideal (in body prose) | state the structure directly |
| Theorem A / B / C labels in prose | refer by formula or theorem number |
| Wave $N$ / Phase $j$ / round $M$ / session $k$ | delete; state the mathematical content |
| we now turn to, having established, this section sharpens | state next mathematical content directly |
| is closely related to, corresponds to, is the analogue of (when exact) | $=$ or $\simeq$ with the morphism named |
| is wrong, would be, must not, fails to | positive construction; name objects + map |
| certificate, manifest, spec, schema | rational reduction, table, or field-standard term |
| we hope, perhaps, remarkably, crucially, notably | state the result |
| $A$ is the primitive open algebra | $\mathcal{C}^{\mathrm{op}}_\partial$ on $(X, D, \tau)$; chart $b$ gives $A_b = \mathrm{End}(b)$ |
| $\mathrm{Bar}(A)$ is the bulk | $\mathrm{Bar}(A)$ classifies twisting; bulk is $Z^{\mathrm{der}}_{\mathrm{ch}}(A) \simeq C^\bullet_{\mathrm{ch}}(A, A)$ |
| direct $\Phi : \mathrm{CY}_d \to \mathrm{ChirAlg}$ | $\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$ |
| $A$ is modular | $\mathcal{C}^{\mathrm{op}}_\partial$ carries cyclic trace $\mathrm{Tr}_\mathcal{C}$ compatible with clutching; closed shadow has modular consequences |
| $\Delta_5$ = compact BPS Hilbert space | degree-2 modular section of $\Omega_{\mathrm{central}}$; operator lift open |
| scalar $Z_{\mathrm{BPS}}$ = operator algebra | scalar = protected trace of still-to-be-constructed operator package |
| $W_\infty[\lambda] \Rightarrow E_\infty$ unconditional | conditional on the four hypotheses |
| formal Darboux $\Rightarrow$ compact target theorem | formal-Darboux + descent + QME + anomaly + locality $\Rightarrow$ candidate |

---

## Define-before-use, motivate-before-introduce

- Every symbol defined at or before first use.
- Every acronym written out at first occurrence: BCOV, BV, QME, VOA, OPE, CoHA, BKM, MNOP, DT, GW, PT, MC, CE, PV, KN.
- Every construction motivated by what came before. Definition forced by the structure preferred over definition by fiat.
- Example before abstract machine when the example carries the structural content.
- Section opens with the first mathematical object; closes by crystallizing what was proved and forcing what comes next.

---
