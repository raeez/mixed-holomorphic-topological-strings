# W13 Critique-Fidelity Audit (Wave 3) — 2026-04-28

**Agent:** W13 (relaunched after stall on 11366-line transcript)
**Lens:** Beilinson (descent of recommendations into plan items) + Standalone reader (cold-reader gaps)
**Sources:**
- Critique: `/Users/raeez/topological-strings/materials/processed/2026-04-28-whitepaper-critical-analysis.txt` (~11366 lines)
- Plan: `/Users/raeez/topological-strings/reconstitution/platonic-ideal-plan-2026-04-28.md`
- Master ledger: `/Users/raeez/topological-strings/reconstitution/attack-heal-platonic-2026-04-28.md`

**Status:** WORK-IN-PROGRESS. Chunked workflow per W13 RELAUNCH protocol — each critique chunk drives an immediate inventory append before moving on.

---

## Status checkpoint

[CHECKPOINT: ALL CHUNKS COMPLETE — 287 critique items inventoried from full 11366-line transcript; cross-map A/P/S/R complete; 27 W3-W13- recommendations issued.]

---

## T1. Critique Inventory

Severity scale: 1 = cosmetic; 2 = local prose; 3 = sharpening of theorem statement; 4 = a major proof obligation or convention error; 5 = strikes the central claim and forces structural rewrite.

### Round 1 — hostile-referee attack (lines 14-572)

| #   | Short name                                     | Sev | Critique lines |
|-----|------------------------------------------------|-----|----------------|
| C01 | Title vs body: "Koszul duality" overclaims; PBW special-fibre is what is proved | 5 | 21-69 |
| C02 | Closed-open map: source-convention error (boundary observable starts from $f \in \bar A$ not from a CE cochain; Prop 0.2.18 perfectness) | 5 | 70-124 |
| C03 | Cotangent/descendant module mismatch: $\Psi_{a,b}$ vs $\rho_{a,b}$ coadjoint; even direction wrong; $h^\vee[1]\cong\langle\Psi_{a,b}\rangle$ as graded vec only | 5 | 125-172 |
| C04 | Cor 0.2.51 false on $f=z_1, g=z_2$: $\{Tr\phi_1,Tr\phi_2\}=N$, not zero; must say "after projection to Hamiltonian quotient" | 4 | 173-247 |
| C05 | "Central operation" Theorem 0.2.17 is too tautological in graded-commutative reduced model (ordinary Hochschild centrality automatic); only Poisson part is non-trivial; demote rhetorically | 3 | 248-281 |
| C06 | "Sector" is selected by hand: scalar trace, $Tr(\psi)$, higher-$\psi$ homology, finite-$N$ identities, coadjoint mismatch all excluded; introduction language overstates | 4 | 282-305 |
| C07 | Large-$N$ is algebraic, not physical: must distinguish $\mathrm{Prim}_{\mathrm{st}}$, $\mathrm{Conn}_{N\to\infty}$, Hamiltonian scalar quotient — three different operations | 3 | 306-332 |
| C08 | Reduced gauge/BV model suppresses quotient-stack issue: linearly reductive invariants vs CE/BRST cohomology — which model is being used must be explicit | 3 | 333-356 |
| C09 | One-$\psi$ homology proof under-proved: chip-moving / Abel-map needs full sign lemma, cellular-chain identification, attaching cells, stabilizer quotient, $S^1$-cycle ID | 4 | 357-385 |
| C10 | Tate / Koszul-duality formalism under-specified: which category of Tate spaces, which bar/cobar adjunction, conilpotency, completed PBW, continuity in length and Taylor degree, coadjoint topology preservation | 4 | 386-405 |
| C11 | Closed sector is formal BF, not yet physical closed string: no parent 11D background, no derived dimension count, no constructed twist, no derived defect from worldvolume, no QME, no propagator/kernel, no quantum graph | 3 | 406-438 |
| C12 | BCOV / Kodaira-Spencer analogy is dangerous: invites wrong comparison; use "Hamiltonian BF for formal symplectic disk" as primary terminology | 3 | 439-450 |
| C13 | Quantum section is target, not result: Moyal/Weyl is a target; Prop 0.2.52 only BRST-descents traces; commutator identity under quantum reduction left as Problem 0.2.54; Capelli/normal-ordering shift can feed lower traces | 4 | 451-470 |
| C14 | Central extension $\{Tr\phi_1,Tr\phi_2\}=N$ is physically meaningful (center-of-mass canonical pair), not disposable bookkeeping; same shift returns quantum mechanically; must be a named obstruction | 4 | 471-494 |
| C15 | Figures (pp. 41, 50, 51) are ornamental ovals; either remove or replace with real graph notation ($\Gamma_1, \Gamma_3, \mathrm{Aut}(\Gamma), P_\partial$, ordered boundary inputs) | 2 | 495-503 |
| C16 | Reference / notation cleanup: malformed citation labels ([13]razmyslov, [2]tsygan); Loday–Vallette index off by one | 2 | 504-511 |
| C17 | Defensible safe fallback theorem statement (Round 1 close-out): explicit bullet-form theorem with PBW SF comparison + boundary-evaluation Lie map after scalar quotient + descendant-module disclaimer | 3 | 512-572 |

### Round 2 — constructive derived-center proposal (lines 573-1492)

| #   | Short name                                     | Sev | Critique lines |
|-----|------------------------------------------------|-----|----------------|
| C18 | Insert CE/PV derived-Poisson-center theorem $C^\bullet_{\mathrm{CE}}(h\ltimes h^\vee[1])\cong Z^{P_0}_{\mathrm{fact}}(S(h))\simeq \mathrm{PV}(S(h))$ as central new section; replace Problem 0.2.20 by this theorem | 5 | 583-728 |
| C19 | Generator-level identification: $c^I\mapsto\theta^I=\partial/\partial O_I$, $u_I\mapsto O_I$; verify $\Phi d_{\mathrm{CE}}=d_\pi\Phi$ and $\Phi$ preserves $P_0$-bracket | 5 | 729-994 |
| C20 | Resolution of CE-source obstruction: $O_I=\mathrm{Tr}\,H_I(\phi_1,\phi_2)$ is image of $u_I$ (cotangent CE coord), not of $c^I$ (Hamiltonian ghost) | 5 | 995-1075 |
| C21 | Recovery: ordinary boundary bracket theorem is moment-map shadow of $\Phi$ at degree zero | 3 | 1076-1118 |
| C22 | Factorization version on intervals using $C_c^\infty(I)\otimes h$: verify locally constant factorization, multiplicativity over disjoint intervals | 4 | 1119-1213 |
| C23 | One-$\psi$ descendants belong to PBW-special-fibre $S(h\oplus h^\vee[1])$; principal-part module $\mathcal P=\bigoplus C\rho_{a,b}/(C\rho_{0,0})$ realizes $h^\vee_{\mathrm{cont}}$ as $h$-module, with $f\cdot\rho=\pi_{\mathrm{pp}}\{f,\rho\}$ | 5 | 1214-1318 |
| C24 | Replacement theorem statement for the paper: $\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}=C^\bullet_{\mathrm{CE,cont}}(h\ltimes h^\vee_{\mathrm{cont}}[1])\cong Z^{P_0}_{\mathrm{fact}}(A_\partial)$, with $c^I,u_I$ assignments and interval lift | 5 | 1369-1481 |

### Round 3 — Diracian rewrite (lines 1493-2493)

| #   | Short name                                     | Sev | Critique lines |
|-----|------------------------------------------------|-----|----------------|
| C25 | Voice/structure: paper should be Diracian, beginning with observables, brackets, locality of measurement (not "is this really a string theory") | 3 | 1500-1535 |
| C26 | First-principle origin of factorization algebra: independent local experiments, $\mathrm{Obs}(U_1)\otimes\cdots\otimes\mathrm{Obs}(U_n)\to\mathrm{Obs}(V)$; $L_v=[Q,\iota_v]$ topological, $L_{\partial/\partial \bar z_i}=[Q,\iota_{\partial/\partial \bar z_i}]$ holomorphic | 4 | 1536-1593 |
| C27 | Forced first-order action from $\Omega_N$, moment-map $\mu_\epsilon$, and BV reduction $Q\psi=[\phi_1,\phi_2]$ as Dirac-constraint-in-homological-form | 4 | 1594-1690 |
| C28 | Three notions of locality must be derived: support locality on brane line ($\delta(t-s)$), topological locality ($L_v=[Q,\iota_v]$), formal-holomorphic / distributional locality transverse to brane | 4 | 2105-2150 |
| C29 | Cotangent boundary sector is distributionally local, not polynomially local: principal parts are residue functionals supported at brane (transverse delta-currents) | 4 | 2126-2150 |
| C30 | One-$\psi$ descendants role: PBW special-fibre, not deformation-level coadjoint; principal parts are true coadjoint; package as distributional boundary current sector $\Theta_\rho(a)$ with $\{O_f(a),\Theta_\rho(b)\}=\Theta_{f\cdot\rho}(ab)$, $\{\Theta_\rho,\Theta_\sigma\}=0$ | 4 | 2151-2244 |
| C31 | Unitarity: do not pretend the model is unitary; replacement is CME ($QI+\frac12\{I,I\}=0$) plus QME ($+\hbar\Delta I=0$) and factorization/OPE associativity; protected cohomological sector | 3 | 2245-2293 |
| C32 | Insertable Diracian opening (model passage): "Local measurements and constraints / The center / Locality / Unitarity / The actual thesis sentence" | 3 | 2294-2475 |
| C33 | Thesis sentence: "A stack of branes is a system of probes for the formal symplectic normal disk... closed observables are precisely the derived Poisson central operations on the stable open Hamiltonian brane algebra" | 3 | 2459-2474 |

### Round 4 — first-principles synthesis (lines 2480-...)

| #   | Short name                                     | Sev | Critique lines |
|-----|------------------------------------------------|-----|----------------|
| C34 | Paper is local BV/factorization, not global worldsheet string; downgrade global rhetoric | 3 | 2487-2530 |
| C35 | Reduce divergence-free polyvectors on $C^2$ to Hamiltonians via Poincare-lemma argument; justifies $\bar A=C[z_1,z_2]/C$ | 3 | 2812-2910 |
| C36 | Open brane sector first-principles construction from exact A-brane on $\mathbb R\subset T^*\mathbb R$ tensored with B-brane skyscraper $\mathcal O_0$ at origin; $\mathrm{Ext}^\bullet_R(k,k)\simeq\Lambda(\epsilon_1,\epsilon_2)$ via Koszul resolution | 3 | 2911-3050 |
| C37 | Dirac interpretation of open action: $\Omega_N=\mathrm{Tr}(d\phi_1\wedge d\phi_2)$, $A$ as multiplier, $\mu_\epsilon=-\mathrm{Tr}(\epsilon[\phi_1,\phi_2])$, BV antifield $\psi=A^*$ with $Q\psi=[\phi_1,\phi_2]$ | 4 | 3051-3157 |
| C38 | Local operators reduce to evaluation at insertion via $[d_R,\iota_{\partial_t}]=\partial_t$ jet-degree contraction (Euler argument) | 3 | 3158-3196 |
| C39 | Stable large-$N$ as Procesi–Razmyslov: $C[\mathfrak{gl}^{2\infty}]^{GL_\infty}_{\mathrm{st}}\cong S(\mathrm{Cyc}(F)_{\mathrm{nonempty}})$; $\mathrm{Tr}(1)=N$ not primitive stable; graded cyclicity for $\psi$ | 3 | 3197-3239 |
| C40 | Adjacent-swap exactness: $Q\mathrm{Tr}(\psi vu)=\mathrm{Tr}([\phi_1,\phi_2]vu)\Rightarrow\mathrm{Tr}(uxyv)-\mathrm{Tr}(uyxv)$ exact | 3 | 3240-3275 |
| C41 | One-$\psi$ descendants $\Psi_{k,l}$ definition + $Q$-closedness via cyclic transition counting; chip-moving / Abel-map proof of $H_1$ one-dimensional | 4 | 3276-3370 |
| C42 | Sector exclusion: $\mathrm{Tr}(\psi)=\Psi_{0,0}$ removed to match constant exclusion in $\bar A$; higher-$\psi$ primitive homology excluded | 3 | 3371-3384 |
| C43 | Closed Koszul dual / PBW-special-fibre comparison admits identification only as filtered graded-commutative product, not deformation-level coadjoint module — PRINCIPAL-PARTS CORRECTION REQUIRED | 4 | 3385-3450 |
| C44 | Degree-zero boundary map calculation: $\{Tr(\phi_1^k\phi_2^l),Tr(\phi_1^m\phi_2^n)\}=(kn-lm)Tr(\phi_1^{k+m-1}\phi_2^{l+n-1})$ after stable connected Hamiltonian quotient | 3 | 3451-3537 |
| C45 | Scalar central subtlety: $\{Tr\phi_1,Tr\phi_2\}=N$ pre-reduction; in reduced $\bar A$, $\{z_1,z_2\}=1\equiv 0\pmod C$; FORMULAS HOLD ONLY AFTER projection out of scalar trace class; reappears as Capelli/normal-ordering | 4 | 3538-3578 |
| C46 | CE-source obstruction is the root reason for derived-center: $\bar A$ perfect ($z_1^az_2^b=\{z_1,\frac{1}{b+1}z_1^az_2^{b+1}\}$); $d_{CE}\xi_{a,b}\ne 0$, no CE cocycle has linear Hamiltonian part | 4 | 3579-3653 |
| C47 | Corrected closed-open derived center theorem: with $\Phi(c^I)=\theta^I, \Phi(u_I)=O_I$, $\Phi d_{CE}=d_\pi\Phi$ is mechanical; bdy Hamiltonian = image of cotangent CE coord, not of $c^I$ | 5 | 3654-3895 |
| C48 | Why principal parts are necessary: continuous dual of $h$ realized by $\rho_{a,b}=z_1^{-a-1}z_2^{-b-1}dz_1\wedge dz_2$ via residue pairing $\langle\rho_{a,b},z_1^mz_2^n\rangle=\delta_{a,m}\delta_{b,n}$; exclusion $a+b>0$ matches removed constants | 4 | 3896-3976 |
| C49 | Principal-part coadjoint action: $z_1^pz_2^q\cdot\rho_{a,b}=-(pb-qa+p-q)\rho_{a-p+1,b-q+1}$; linear $z_1$ raises $b$ by one — not lowers — fix any sentence with the wrong direction | 4 | 3981-4044 |
| C50 | Polynomial descendants vs principal parts: $O_{1,0}: \Psi_{a,b}\mapsto b\Psi_{a,b-1}$ (lowers $b$) vs $z_1\cdot\rho_{a,b}=-(b+1)\rho_{a,b+1}$ (raises $b$) — direction opposite, hence not the same module | 5 | 4045-4112 |
| C51 | No-go theorem (no polynomial coadjoint realization): $O_{1,0},O_{0,1}$ act by constant derivations on polynomials hence locally nilpotent; principal-part action raises pole order indefinitely; local nilpotence preserved by module isomorphism | 5 | 4113-4159 |
| C52 | Local-dual boundary sector $M^{\mathrm{pp}}_\partial=H^2_{(z_1,z_2)}\otimes(dz_1dz_2)/C\rho_{0,0}$, $\Theta_{a,b}\leftrightarrow\rho_{a,b}$, $\{O_{p,q},\Theta_{a,b}\}=-(pb-qa+p-q)\Theta_{a-p+1,b-q+1}$, $\{\Theta,\Theta\}=0$, realizes $\bar A\ltimes \mathcal P[1]$ | 4 | 4160-4267 |
| C53 | Dirac interpretation of principal parts: position vs momentum analogy; Hamiltonian functions vs cotangent residue currents (transverse delta-currents at brane); brane is a defect, defect-localized duals are normal delta currents | 4 | 4269-4321 |
| C54 | Witten/open-closed interpretation: derived $P_0$-center contains functions, vector fields, higher polyvectors; closed BF fields = polyvector central operations on open brane phase space | 4 | 4322-4391 |
| C55 | Three notions of locality formalization: support locality / topological locality (locally constant) / formal-holomorphic-distributional locality | 4 | 4392-4445 |
| C56 | Unitarity replacement: CME $QI+\frac12\{I,I\}=0$ + QME $+\hbar\Delta I=0$ + factorization/OPE associativity + anomaly cancellation; protected twisted sector | 3 | 4446-4473 |
| C57 | Quantum Moyal target: $f\star g=m\circ\exp(\hbar P/2)(f\otimes g)$, $P=\partial_{z_1}\otimes\partial_{z_2}-\partial_{z_2}\otimes\partial_{z_1}$; coefficients $\hbar,\hbar^3/24,\hbar^5/1920,\hbar^7/322560$ for odd $r$ | 3 | 4474-4598 |
| C58 | Quantum matrix reduction Capelli obstruction: $YX-XY+\hbar NI=0$ in moment ideal $\Rightarrow Tr(AXY)-Tr(AYX)=\hbar N\,Tr(A)$; can feed lower-degree traces into connected sector; quantum part = target only, not theorem | 4 | 4599-4670 |
| C59 | Costello graph problem checklist: elliptic parent, defect conditions, gauge fix, propagator, anomaly, bulk-to-defect kernel, propagator/Weyl link, first-order graph normalization, third-order graph normalization to $1/24$, connected-trace extraction with Capelli treatment | 4 | 4671-4699 |
| C60 | Corrected global thesis: 3 main theorems (PBW stable trace + derived closed-open center + principal-parts cotangent realization), not one overloaded theorem | 5 | 4700-4805 |
| C61 | Errata 1 — principal-part linear action sign sentence ("$z_1$ lowers indices") is WRONG | 3 | 4806-4831 |
| C62 | Errata 2 — polynomial descendants do not simply "raise indices"; depends on $p+q$; the real point is action is not the coadjoint action | 3 | 4832-4850 |
| C63 | Errata 3 — paper's coadjoint formula $z_1^pz_2^q\cdot\rho_{a,b}=-(pb-qa+p-q)\rho_{a-p+1,b-q+1}$ is correct; treat as reference | 2 | 4851-4859 |
| C64 | Errata 4 — smeared bracket formula $\{I_\partial(a,f),I_\partial(b,g)\}=I_\partial(ab,\{f,g\}_{\bar A})$ requires connected Hamiltonian quotient by scalar trace; otherwise $f=z_1, g=z_2$ gives $N\int ab$ | 4 | 4860-4886 |
| C65 | Errata 5 — "removing constants" not literally "removing all $U(1)$ centre-of-mass": $Tr(1)=N$ removed, but $Tr\phi_1, Tr\phi_2$ remain | 2 | 4887-4910 |
| C66 | Errata 6 — full closed-open map can be sharpened: stalkwise CE/PV isomorphism is the abstract content; remaining work is implementing it inside unfrozen BV/factorization model with compact supports, de Rham/Dolbeault, defect kernels | 3 | 4911-4938 |
| C67 | Errata 7 — references and labels need cleanup ([13]razmyslov, [2]tsygan, PBW citation off-by-one) | 2 | 4939-4942 |
| C68 | Errata 8 — figures upgraded or demoted: schematic reminders only, label propagators / boundary vertices / aut factors / orientation, or keep explicitly informal | 2 | 4943-4948 |

### Round 5 — second-pass critique on v3 draft (lines 4949-...)

| #   | Short name                                     | Sev | Critique lines |
|-----|------------------------------------------------|-----|----------------|
| C69 | Persistent inconsistency: interval-wise factorization theorem still maps $(a\otimes f)^\vee[-1]$ to $B_f(a)$; this is the OLD MISTAKE in factorization form; the source must be the cotangent CE coord (label $u_{a\otimes f}$), not the Hamiltonian CE coord | 5 | 5081-5175 |
| C70 | $\Psi\to\rho$ cannot be a strict $P_0$-morphism: explicit counterexample at $f=z_1$ ($b\rho_{a,b-1}$ vs $-(b+1)\rho_{a,b+1}$); chain-level primitive projection claim must NOT assert strict $P_0$-bracket compatibility | 5 | 5176-5311 |
| C71 | Distinguish PBW special-fibre open descendant sector ($\Psi_{a,b}$) from new distributional/principal-part boundary sector ($\Theta_\rho$); do not define principal-part sector as $P_0$-quotient of polynomial $\Psi$-sector unless an honest intertwiner is constructed | 5 | 5312-5346 |
| C72 | "Interpolation by $\hbar$" claim is not a theorem: $\Psi$ vs $\rho$ are not two bases of same $h$-module (no-go from local nilpotence); to make interpolation real, construct Rees / Fourier-Borel $D_\hbar$-module $M_\hbar$ with two specializations | 5 | 5347-5455 |
| C73 | Factorization algebra must use $\Omega^\bullet_c(I)$ de Rham compact supports, not $C_c^\infty(I)$; the latter has no differential, inclusions of intervals not quasi-isomorphisms | 4 | 5456-5514 |
| C74 | Quantum radial-parts theorem is potentially huge but UNDERPROVED: list seven specific challenges (which radial-parts theorem; applies to all Weyl-ordered mixed traces; Calogero-Moser/Dunkl correction terms; radial map injectivity; quotient order; connected single-trace projection; stable cumulant extraction) — author as Theorem F$'$ "Radial-Moyal theorem for Weyl traces" with appendix-level proof | 5 | 5515-5613 |
| C75 | Weighted Tate completion is regulator, not the original strict dual: state explicitly that hierarchy: strict algebraic / weighted analytic regulator / regulator-independence comparison statement; without comparison, weighted Tate is not a completion of the original object | 4 | 5614-5683 |
| C76 | Principal-part module needs $D$-module proof, not "Schur rigidity": prove via $H^2_{(z_1,z_2)}(\mathbb C[z_1,z_2])dz_1dz_2/\mathbb C\rho_{0,0}$ + uniqueness from continuous degree-preserving pairing satisfying coefficient extraction and Hamiltonian integration by parts | 4 | 5684-5736 |
| C77 | Scalar anomaly section: phrase as the distinguished one-dimensional anomaly line in $H^2_{\mathrm{Lie}}$, not as "the one-dimensional sub-line of $H^2$" (avoid overstating one-dimensionality of full $H^2$) | 2 | 5737-5779 |
| C78 | Chain-level primitive projection should be RENAMED: "primitive Lie/$P_0$ quotient projection" or "primitive indecomposable shadow" — NOT cotangent factorization-center lift / factorization algebra equivalence; if quotient kills products of positive primitives it is not the same factorization object | 4 | 5780-5822 |
| C79 | Three physical principles structure: Dirac constrained probes / Witten closed-open centrality / Cotangent fields are transverse currents — should be the first section, makes factorization algebra physically inevitable | 3 | 5823-5908 |
| C80 | Strongest theorem package: 5 main theorems (Dirac probe / Derived center / Defect current factorization / Principal-parts coadjoint / Quantum radial Moyal); separate purely algebraic Theorem B from analytic Theorem C from quantum Theorem | 4 | 5909-5999 |
| C81 | Theorem D detailed: $h^\vee_{\mathrm{cont}}\cong\mathcal P=H^2_{(z_1,z_2)}(\mathbb C[z_1,z_2])dz_1dz_2/\mathbb C\rho_{0,0}$, residue pairing, coadjoint action; do NOT rely on "Schur rigidity" unless actually proved | 4 | 6000-6035 |
| C82 | Theorem E detailed: $\mathcal A^{\mathrm{pp}}_\partial(I)=S(h_I)\otimes S(\mathcal P_I[1])$ with independent $\Theta_\rho$ generators; ${B_f,\Theta_\rho}=\Theta_{f\cdot\rho}$, ${\Theta,\Theta}=0$; not from ordinary polynomial open observables | 4 | 6003-6235 |
| C83 | Theorem F decomposed: unconditional algebraic Moyal/Weyl target / conditional Costello graph realization; explicit separation of degree-zero quantum sector (proved if radial-parts identity holds) from full descendant/cotangent quantum lift (conditional on Tate/QME) | 4 | 6497-6502 |
| C84 | Cross-volume horizon material should NOT be in the main paper: dilutes core theorem; move to private convention appendix or separate "programmatic outlook"; transfers are local-only and non-transferable without matched-convention proofs | 4 | 6066-6076 |
| C85 | Replacement abstract draft (round 5): physics paragraph (mixed brane line, Dirac probe, $Q\psi=[\phi_1,\phi_2]$, closed shifted cotangent BF) + theorem paragraph (CE/PV derived-center, $u_x\mapsto O_x$, $c_\lambda\mapsto\theta_\lambda$, $\mathcal P$ as principal-part residues, PBW shadow status, $U(1)$ anomaly, Weyl/Moyal Capelli, Costello isolated) | 4 | 6077-6131 |
| C86 | Concrete Errata for v3 (round 5): 10 specific replacements listed; same as C61-C68 plus: (1) interval source ($u_{a\otimes f}\mapsto B_f(a)$), (2) $C_c^\infty(I)\to\Omega^\bullet_c(I)$, (3) delete "Ψ and ρ different bases of same module", (4) delete strict $P_0$-compatibility of $\Psi\to\rho$, (5) make principal-part currents independent boundary generators, (6) rename primitive projection, (7) strengthen or condition radial-parts theorem, (8) treat weighted Tate as regulator, (9) replace Schur rigidity with $D$-module / residue uniqueness, (10) move cross-volume material out | 5 | 6132-6257 |

### Round 6 — exhaustive technical punch list (lines 6306-...)

The following items are taken from the 201-item technical punch list. Numbered to match (round-6 item N = critique item C(86+N)).

| #   | Short name                                     | Sev | Critique lines |
|-----|------------------------------------------------|-----|----------------|
| C87 | Punch1: Reorganize paper around six clean theorem layers (Dirac/Stable trace/CE-PV/Principal-part/Factorization-current/Quantum) — split the umbrella theorem | 4 | 6394-6502 |
| C88 | Punch2: Fix central source-convention error in factorization theorem 0.2.21: $u_{a\otimes f}\mapsto B_f(a)$, $c_\lambda\mapsto\theta_\lambda$; propagate through 0.1.14(iii), 0.2.21, 0.2.23, abstract, factorization compatibility proof | 5 | 6503-6574 |
| C89 | Punch3: Replace $C_c^\infty(I)$ by $\Omega^\bullet_c(I)$ in all locally-constant factorization statements; degree-zero current formula recovered as top-degree component | 4 | 6578-6650 |
| C90 | Punch4: Remove "Ψ and ρ different bases of the same g-module" — most dangerous mathematical sentence in the draft; replace with two distinct module realizations of same PBW label set + named problem for Rees/Fourier interpolation | 5 | 6651-6761 |
| C91 | Punch5: Correct "raising/lowering" terminology for principal parts; replace with "coadjoint principal-part action" or "negative-transpose residue action"; add small explicit table $f\to f\cdot\rho_{a,b}$ effect | 3 | 6762-6818 |
| C92 | Punch6: Re-prove principal-part uniqueness using local cohomology / residue calculus, NOT Schur rigidity; uniqueness statement: residue pairing is unique continuous degreewise pairing satisfying coefficient extraction and Hamiltonian integration by parts after fixing $\langle\rho_{a,b},z_1^az_2^b\rangle=1$ | 4 | 6819-6858 |
| C93 | Punch7: Separate the three cotangent objects $u_I,\Psi_{a,b},\Theta_\rho$ via explicit dictionary table; add warning $\Psi_{a,b}\mapsto\rho_{a,b}$ is not a $P_0$-morphism | 4 | 6859-6920 |
| C94 | Punch8: Rename "primitive projection" to "primitive indecomposable $P_0$-shadow" (NOT factorization algebra lift); state explicitly $\pi_{\mathrm{prim}}(XY)=0$ for positive primitive $X,Y$ | 4 | 6921-6970 |
| C95 | Punch9: Recast principal-part boundary sector as added enlarged reduced defect-current sector, NOT as derived from polynomial observables; explicit paragraph: "principal-part sector is not obtained from ordinary polynomial matrix observables; adjoined as reduced local-dual defect-current module forced by the coadjoint action" | 4 | 6971-7010 |
| C96 | Punch10: Strengthen the derived-center proof by adding a coordinate-free version: $\mathrm{PV}(S(h),\pi_h)\cong C^\bullet_{\mathrm{CE}}(h;S(h))\cong C^\bullet_{\mathrm{CE}}(h\ltimes h^\vee[1])$ via Lichnerowicz | 4 | 7011-7068 |
| C97 | Punch11: Sign-convention appendix: $V[1]^n$ convention, CE differentials, $d^2_{\mathrm{CE}}u_K=0$ verification, Schouten bracket convention $[\theta^I,O_J]=\delta^I_J$ (not negative), $d_\pi=[\pi,-]$ formulas, sign checklist $\Phi(d_{\mathrm{CE}}c^K)=d_\pi\Phi(c^K)$, $\Phi(d_{\mathrm{CE}}u_K)=d_\pi\Phi(u_K)$ | 4 | 7069-7140 |
| C98 | Punch12: Claim-strength ledger table near abstract (statement / status), unconditional vs conditional vs open vs proved-after-correction — exhibits exact mathematical claims that are proved | 4 | 7141-7167 |
| C99 | Punch13: Two-paragraph abstract rewrite (physics + theorem); explicitly state CE/PV isomorphism, principal-part residues, PBW shadow status, U(1) anomaly | 3 | 7168-7243 |
| C100 | Punch14: Rewrite "thesis" section as theorem-corollary "Dirac-Witten closed-open principle" — closed-open map is identity on polyvector operations under CE/PV identification; physics synthesis becomes inevitable | 3 | 7244-7272 |
| C101 | Punch15: Add Dirac first-principles derivation box: $\Omega_N$, $\mu_\epsilon$, $\iota_{X_{\mu_\epsilon}}\Omega_N=-d\mu_\epsilon$, $X_{\mu_\epsilon}(\phi_i)=[\epsilon,\phi_i]$, $S_\partial=\int Tr(\phi_1d\phi_2)-\mu_A=\int Tr(\phi_1d\phi_2+A[\phi_1,\phi_2])$ — appears before any string terminology | 3 | 7274-7314 |
| C102 | Punch16: Witten centrality derivation box after Dirac: $\mathrm{Obs}_{\mathrm{closed}}\to Z_{\mathrm{fact}}^{P_0}(\mathrm{Obs}_{\mathrm{open}})$; physical reason for factorization, front-loaded | 3 | 7315-7354 |
| C103 | Punch17: Fix the "closed Hamiltonian factor before adjoining cotangent generators" theorem (Theorem 0.2.21): split into Part 1 (Hamiltonian ghosts only $C^\bullet_{\mathrm{CE}}(h_I)\to \mathrm{PV}_{\mathrm{const}}(S(h_I))$) and Part 2 (shifted cotangent extension $C^\bullet_{\mathrm{CE}}(h_I\ltimes h_I^\vee[1])\cong\mathrm{PV}(S(h_I))$) | 4 | 7355-7430 |
| C104 | Punch18: Recast PBW/Koszul-dual theorem as separate "shadow" theorem: $(C^\bullet_{\mathrm{CE}}(g))^!\simeq U(g)$, $U_\hbar(g)/(\hbar)\simeq S(h\oplus h^\vee[1])$, $S(\bar A\oplus\bar A_{\mathrm{desc}}[1])$ as polynomial PBW SF shadow + warning that PBW SF does not encode coadjoint action | 4 | 7431-7470 |
| C105 | Punch19: Prove $h$ perfect in formal completed setting via continuity argument: $f=\sum f_{a,b}z_1^az_2^b\Rightarrow f=\{z_1,\sum (f_{a,b}/(b+1))z_1^az_2^{b+1}\}$ in completed topology; gives $[h,h]=h$ in topological Lie algebra used by main theorem | 3 | 7471-7517 |
| C106 | Punch20: Add local-cohomology explanation of $a+b>0$ cutoff: $\rho_{0,0}=z_1^{-1}z_2^{-1}dz_1dz_2$, $\langle\rho_{0,0},1\rangle=1$, $h=\mathbb C[[z_1,z_2]]/\mathbb C$ ⇒ $\mathcal P=H^2/(\mathbb C\rho_{0,0})$; tie to scalar anomaly $\rho_{0,0}\leftrightarrow 1\leftrightarrow Tr(1)=N$ | 3 | 7518-7559 |
| C107 | Punch21: Tighten U(1) anomaly statement; do NOT claim $[\bar c]$ spans all of $H^2_{\mathrm{Lie}}(\bar A;\mathbb C)$ unless full cohomology computed — say "distinguished scalar-extension line" | 3 | 7560-7605 |
| C108 | Punch22: Clarify "scalar reduction" vs "removing $U(1)$ centre-of-mass": linear traces $Tr\phi_1, Tr\phi_2$ remain; only $Tr(1)=N$ removed; explicit warning after every $\{z_1,z_2\}=0$ in $\bar A$ formula | 3 | 7606-7634 |
| C109 | Punch23: Three large-$N$ operations subsection: $\mathrm{Prim}_{\mathrm{st}}$ / $\mathrm{Conn}_{N\to\infty}$ / Hamiltonian scalar quotient — define each separately, do not conflate | 3 | 7635-7657 |
| C110 | Punch24: Strengthen one-$\psi$ homology proof with seven explicit lemmas: $C_2(k,l)\to C_1(k,l)\to C_0(k,l)$ formal definition, sign lemma for two-$\psi$ boundary, cellular-chain identification with two-skeleton, attaching cells lemma, Abel-map well-definedness under cyclic relabelling, stabilizer/affine-quotient contractibility, identification of $\Psi_{k,l}$ with $S^1$-cycle | 4 | 7658-7697 |
| C111 | Punch25: Reproducibility appendix for finite checks (script/checks/range table) — verifies finite instances, NOT proof except where stated as computational evidence | 2 | 7698-7711 |
| C112 | Punch26: Rework weighted Tate as regulator theorem; rename $(h^w,h^{\vee,w}_{\mathrm{cont}})$ as "weighted coefficient regulator"; state regulator-independence problem | 4 | 7714-7754 |
| C113 | Punch27: Remove overstrong claims in weighted quantum extension; split into unconditional weighted coefficient kernel / unconditional graphwise RG boundedness / conditional weighted quantum cotangent lift | 4 | 7756-7779 |
| C114 | Punch28: Add "Hadamard/Mittag-Leffler does not imply QME" boxed warning: controls wavefront and finite-window locality but not obstruction class | 3 | 7780-7795 |
| C115 | Punch29: Reassess all-$N$ radial-parts theorem (Theorem F$'$) with eight explicit questions in standalone Appendix C: which algebra is the quantum reduction; exact $J_N(f)$; Capelli-renormalized generator $\tilde J_N(f)$; which radial map; injectivity on relevant subspace; image as one-particle Weyl operator sums; Dunkl/Calogero corrections; connected single-trace projection commutes with bracket | 5 | 7796-7848 |
| C116 | Punch30: Clarify Moyal target vs Costello graph normalization: Moyal algebra theorem ≠ Costello graph theorem — make explicit theorem/problem boundary | 4 | 7849-7883 |
| C117 | Punch31: Source-target-status diagram showing $C^\bullet_{\mathrm{CE}}\xrightarrow{\Phi}\mathrm{PV}$, Koszul dual $\to U$, $\mathrm{gr}^{\mathrm{PBW}}\to S(h\oplus h^\vee[1])$, label identification $\to S(\bar A\oplus\bar A_{\mathrm{desc}}[1])$; annotated with $u_f\mapsto O_f$, $c_f\mapsto\partial_{O_f}$, $\delta_{a,b}[1]\mapsto\Psi_{a,b}$ only in PBW SF, $\delta_{a,b}\mapsto\rho_{a,b}$ as coadjoint module | 4 | 7884-7926 |
| C118 | Punch32: Replace "Hamiltonian factor" terminology with three-level notation (Hamiltonian Lie algebra $h$ / boundary Hamiltonian $O_f$ / CE Hamiltonian ghost $c_f$ / CE cotangent $u_f$); never write "$f\mapsto O_f$" without specifying level | 3 | 7927-7962 |
| C119 | Punch33: Rename $A_\partial=S(h)$ more carefully as $\mathcal O_{\mathrm{poly}}(h^\vee)$; $O_f$ is linear function on $h^\vee$ corresponding to $f\in h$ | 3 | 7963-7984 |
| C120 | Punch34: Define topology on $S(h)$ once and enforce it: $S(V)$, $\widehat S(V)$, $S_{\mathrm{Tate}}(V)$, weighted completion — notation table | 3 | 7985-7999 |
| C121 | Punch35: Finite-degree support lemmas for all infinite sums in $d_{\mathrm{CE}}u_K=\sum_J C^L_{KJ}u_Lc^J$ etc.; prove for each finite output degree only finitely many terms contribute | 3 | 8011-8042 |
| C122 | Punch36: Move cross-volume horizon out of main paper; private appendix only; keep one paragraph: "No compact CY3, Igusa, Borcherds, BKM claim is used; transfer requires separate matched-conventions proof" | 3 | 8043-8053 |
| C123 | Punch37: Remove "twisted M-theory universality" from main theorem path — make conditional outlook ("Conditional realization in admissible protected twisted-M sectors") not "universality" | 4 | 8056-8081 |
| C124 | Punch38: Rephrase "string" as Costello-Witten string-field-theoretic local-operator sense; disclaimer in first two pages; avoid "M-theory" in theorem titles; use "Hamiltonian BF brane model" | 3 | 8082-8092 |
| C125 | Punch39: Strengthen unitarity section: no reflection positivity, no Hilbert-space completion; if unitary parent exists, this is protected cohomological sector only | 3 | 8093-8110 |
| C126 | Punch40: "Physical dictionary" table after the theorem (8 rows: normal coords, symplectic form, gauge constraint, BV Koszul variable, closed canonical transformations, closed cotangent field, brane measurement, closed central operation, cotangent defect current) | 3 | 8112-8170 |
| C127 | Punch41: "Why principal parts are forced" subsection — Dirac/Witten explanation; principal parts are brane-localized currents, not functions; holomorphic analogue of momentum distributions | 3 | 8172-8191 |
| C128 | Punch42: Add explicit no-go theorem for $\Psi\to\rho$ as numbered theorem: "No polynomial descendant realization of the coadjoint module" — proof from local nilpotence | 4 | 8192-8213 |
| C129 | Punch43: Rephrase Rees interpolation as conjectural $D_\hbar$-module theorem: $\mathrm{gr}_\hbar M_\hbar\cong\bar A_{\mathrm{desc}}$, $M_\hbar[\hbar^{-1}]\cong\mathcal P$ | 4 | 8215-8252 |
| C130 | Punch44: Clarify CE/PV theorem's relationship to HKR: split into algebraic identity / center identification / HKR only for ordinary $E_1$ center | 3 | 8253-8295 |
| C131 | Punch45: Finite-dimensional approximation proof for Tate CE/PV via finite Taylor windows + Mittag-Leffler exact inverse limits | 4 | 8297-8317 |
| C132 | Punch46: Clean up Tate Quillen-equivalence section: move full model-category construction to appendix; main text keeps only strict cochain isomorphism in admissible filtered Tate envelope; firewall claim from raw category | 3 | 8319-8340 |
| C133 | Punch47: Make nilpotent truncation section less central — appendix as finite check/regulator, not part of main theorem | 3 | 8341-8357 |
| C134 | Punch48: Strengthen "naive truncation fails" proof: explicit $\{z_1^2,z_2^2\}=4z_1z_2$, $\{z_1z_2,z_1^2\}=-2z_1^2$, $\{z_1z_2,z_2^2\}=2z_2^2$ recovering $\mathfrak{sl}_2$ basis | 3 | 8358-8388 |
| C135 | Punch49: Quantum $\mathfrak{m}^3/\mathfrak{m}^{N+1}$ obstruction lemma: $P^3(z_1^4,z_2^4)=576z_1z_2\Rightarrow$ nilpotent classical truncation not Moyal-flat | 3 | 8389-8427 |
| C136 | Punch50: "Unreduced versus reduced" notation convention: $A^{\mathrm{red}}_\partial$, $A^{\mathrm{unred}}_\partial$, $A^{\mathrm{pp}}_\partial$, $A^{\mathrm{Ham}}_\partial$ | 3 | 8428-8469 |
| C137 | Punch51: Clean up theorem numbering with map of dependencies (CE/PV / principal parts / stable traces / quantum Moyal / weighted Tate / Costello graph) | 2 | 8471-8487 |
| C138 | Punch52: Notation index ($\bar A$, $h$, $\mathcal P$, $O_f$, $B_f(a)$, $c^I$, $u_I$, $\theta^I$, $\Psi_{a,b}$, $\Theta_\rho$, $[\bar c]$) | 2 | 8488-8526 |
| C139 | Punch53: Make $\mathcal P_I$ density-dual object, not arbitrary distributions: $h^\vee_I=(\Omega^\bullet_c(I))^\vee\otimes\mathcal P=\Omega^{-\bullet}(I)\otimes\mathcal D'(I)\otimes\mathcal P$; do not multiply two arbitrary distributions; only $aB$ for $a\in C_c^\infty, B\in \mathcal D'_c$ | 4 | 8527-8580 |
| C140 | Punch54: Distribution-locality subsection: $aB$ legal; $\{B_f(a),\Theta_\rho(B)\}=\Theta_{f\cdot\rho}(aB)$; $\{\Theta_\rho,\Theta_\sigma\}=0$ avoids distribution products | 4 | 8582-8588 |
| C141 | Punch55: Fix "strict $P_0$ structure follows from delta-function locality" — strictness depends on reduced post-contraction model; in unreduced BV, represented by homotopies and contact-term choices | 4 | 8589-8612 |
| C142 | Punch56: Strengthen global-local section: $0\to \mathbb C_X\to \mathcal O_X\to \mathcal O_X/\mathbb C_X\to 0\Rightarrow H^0\to H^1$ period obstruction; main theorem formal local; globalization requires descent | 3 | 8613-8636 |
| C143 | Punch57: Clarify relationship to BCOV/Kodaira-Spencer; use "Hamiltonian BF" as primary terminology; "Kodaira-Spencer analogue" only as motivation | 3 | 8637-8645 |
| C144 | Punch58: Clarify closed mixed Hamiltonian sector fields $\alpha,\beta$ with table of ghost-zero components and degrees | 3 | 8647-8663 |
| C145 | Punch59: Justify or fix BF pairing degree calculation $|\alpha|+|\beta|$ for top form $p+q=4$; spell out density degree or BV dual shift | 3 | 8664-8678 |
| C146 | Punch60: Open ghost-zero truncation proof: "classical truncation, not full BV quantum measure; quantum corrections may reintroduce discarded fields unless protected by symmetry" | 3 | 8680-8688 |
| C147 | Punch61: Finite-$N$ statement for commuting-pair quotient: BV complex is Koszul presentation of derived zero locus of moment map; $H^0$ is classical invariant ring; higher cohomology records derived intersection — avoid claiming Koszul exact beyond proven | 3 | 8689-8716 |
| C148 | Punch62: Clarify gauge BRST vs invariant reduction: "we compute invariant functions on derived moment-map zero locus, not the full BRST cohomology of infinitesimal gauge algebra"; group linearly reductive ⇒ invariants exact | 3 | 8718-8729 |
| C149 | Punch63: Reference/labels audit: $\backslash$cite cleanup for [13]razmyslov, [2]tsygan; align Loday-Vallette / Priddy / Hinich / Berger-Moerdijk / Lefèvre-Hasegawa numbers; insert bibliography entries | 2 | 8730-8754 |
| C150 | Punch64: Theorem-proof boundary for LQT: motivational template, not direct proof; explicit caveat "LQT is motivational here, not the proof of the Hamiltonian sector" | 3 | 8755-8764 |
| C151 | Punch65: "Sector exclusions" theorem stating exactly what is excluded ($Tr(1)$, $Tr(\psi)$, higher-$\psi$ primitive homology, finite-$N$ trace identities) and why | 3 | 8765-8771 |
| C152 | Punch66: Included/excluded table for open algebra (six rows: $Tr(\phi_1^k\phi_2^l)$, $Tr(1)$, $\Psi_{k,l}$, $Tr(\psi)$, two-$\psi$ primitives, $\Theta_\rho$) | 3 | 8772-8789 |
| C153 | Punch67: Strengthen scalar-central formula in every bracket theorem: explicit unreduced formula $\{B_f(a),B_g(b)\}=B_{\{f,g\}_{\bar A}}(ab)+N\bar\omega(f,g)\int ab\,dt$; never state reduced bracket without referencing this | 4 | 8790-8821 |
| C154 | Punch68: Low-degree sanity-check subsection: $\{z_1,z_2\}=1\equiv 0$ in $\bar A$, $\{Tr\phi_1,Tr\phi_2\}=N$; $\{z_1^2,z_2^2\}=4z_1z_2$, $\{Tr\phi_1^2,Tr\phi_2^2\}=4Tr(\phi_1\phi_2)$ | 2 | 8822-8847 |
| C155 | Punch69: "Finite rank warning" before every use of freely generated trace algebras: free trace generation is degreewise stable, not finite-$N$ | 3 | 8848-8862 |
| C156 | Punch70: Quantum theorem source notation: $\Phi^{(0)}_\hbar(u_f)=J_\infty(f)$, $\Phi^{(0)}_\hbar(c_f)=$quantum derivation; degree-zero quantum theorem treats $u_f$-coordinate part of derived center | 3 | 8863-8898 |
| C157 | Punch71: Define quantum $P_0,\hbar$-center carefully; $d_\hbar=[\pi_\hbar,-]$ for quantum Poisson cochains, OR $Z^{E_1}_{\mathrm{fact}}(\mathrm{Obs}^\hbar_{\mathrm{open}})\simeq HH^\bullet(\mathrm{Obs}^\hbar_{\mathrm{open}})$ for associative central operations; do not blur $P_0$ and quantum $E_1$ | 4 | 8901-8957 |
| C158 | Punch72: Separate Weyl/Moyal deformation of disk from Weyl algebra of matrices: $(\mathbb C[[z_1,z_2]][[\hbar]],\star)$ vs $W_N=D_\hbar(\mathfrak{gl}_N)$; trace map $J_N(f)$ connects them | 3 | 8958-8984 |
| C159 | Punch73: Capelli triangular renormalization explicit small-degree formulas: $\tilde J_N(z_1z_2)=Tr\,\mathrm{Sym}(XY)+c_1\hbar N$, $\tilde J_N(z_1^2z_2^2)=Tr\,\mathrm{Sym}(X^2Y^2)+c_1\hbar N\,Tr\,\mathrm{Sym}(XY)+c_2\hbar^2 N^2$ | 3 | 8985-9002 |
| C160 | Punch74: Radial-parts proof "finite $N$, then stable $N$" order: 4 lemmas (finite-$N$ Weyl trace descent / finite-$N$ radial-parts identity / finite-$N$ commutator identity mod scalar/Capelli / stable connected extraction) | 4 | 9007-9019 |
| C161 | Punch75: Quantum scalar anomaly theorem with Rees specialization: $U_\hbar(\bar A[\bar c])/(\hbar)\cong S(\bar A[\bar c])$, $[X,Y]=\hbar\bar c$, boundary $[Tr X,Tr Y]=\hbar N$ | 3 | 9020-9039 |
| C162 | Punch76: Replace "single nontrivial class" with "distinguished nontrivial scalar-extension class" unless full $H^2$ classified | 2 | 9040-9050 |
| C163 | Punch77: "No global unitarity" theorem-style statement: cohomological protected sector; CME/QME and factorization associativity; no positive Hilbert-space inner product constructed or required | 3 | 9051-9057 |
| C164 | Punch78: Examples of physical observables: $O_{1,0},O_{0,1}$ (centre-of-mass), $O_{2,0},O_{1,1},O_{0,2}$ (quadratic deformations / $\mathfrak{sl}_2$), $\rho_{1,0},\rho_{0,1}$ (first-derivative delta-currents), $u_{1,0}$ (CE cotangent) | 2 | 9058-9092 |
| C165 | Punch79: Make $\mathfrak{sl}_2$ quadratic sector physically explicit: $H_2\cong\mathfrak{sp}_2\cong\mathfrak{sl}_2$ generates linear symplectic transformations; not nilpotent | 3 | 9094-9115 |
| C166 | Punch80: "What would prove the full Costello theorem" formal checklist (13 items: elliptic mixed bulk BV / brane-defect boundary condition / gauge fixing / heat kernel / propagator / bulk-to-boundary kernel / renormalization scheme / counterterms solving QME / scalar anomaly renorm / connected trace normalization / first graph coeff 1 / third graph coeff 1/24 / all odd coefficients match Moyal) | 4 | 9117-9150 |
| C167 | Punch81: Treat figures as either real graph notation or remove; each graph displays $\Gamma$, $|\mathrm{Aut}\,\Gamma|$, $P_\partial$, boundary order, kernel orientation, coefficient | 2 | 9152-9158 |
| C168 | Punch82: Prove closed BF action satisfies CME explicitly via AKSZ calculation: $\{S,S\}=2\int\langle D\alpha+\frac12[\alpha,\alpha], D\alpha+\frac12[\alpha,\alpha]\rangle$ + Jacobi terms; invariant pairing and coadjoint action necessary | 3 | 9159-9183 |
| C169 | Punch83: Ensure semidirect bracket degree signs correct: $[f,\eta_\lambda]=\eta_{\mathrm{ad}^\vee_f\lambda}$ with shift signs; $[\eta_\lambda,\eta_\mu]=0$ shifted-cotangent abelian; graded Jacobi proof | 3 | 9184-9210 |
| C170 | Punch84: Explicit proof $d^2_{\mathrm{CE}}u_K=0$ via Jacobi/coadjoint representation property | 4 | 9212-9230 |
| C171 | Punch85: Fix "basis dependence" language: CE/PV map basis-independent (canonical identification function-polyvector on linear Poisson space), formula basis-dependent; residue basis $\rho_{a,b}$ coordinate-dependent under Darboux but residue pairing coordinate-invariant up to symplectic volume | 3 | 9231-9251 |
| C172 | Punch86: Formal symplectomorphism covariance: $f\mapsto f\circ\phi^{-1}$, $\rho\mapsto\phi_*\rho$, $O_f\mapsto O_{f\circ\phi^{-1}}$; CE/PV map commutes | 3 | 9253-9270 |
| C173 | Punch87: Clarify closed $\beta$-field as cotangent field, not antifield: BF cotangent participating in shifted symplectic pairing, not merely antifield of $\alpha$ | 2 | 9271-9277 |
| C174 | Punch88: Glossary of "Hamiltonian," "cotangent," "descendant," "principal part" — overloaded terms in one place | 2 | 9279-9289 |
| C175 | Punch89: Clean title — "Closed Hamiltonian BF Theory as the Derived Poisson Centre of a Dirac Brane Probe" with subtitle "A formal local mixed holomorphic-topological model on $\mathbb R^2\times\mathbb C^2$" | 3 | 9290-9302 |
| C176 | Punch90: "Main contributions" list after abstract (7 items: Dirac derivation / stable trace / CE/PV derived center / principal-part residue / U(1) anomaly / quantum Moyal target / weighted Tate regulator) | 3 | 9305-9315 |
| C177 | Punch91: Replace "groundbreaking" claims with theorem names; let theorem names carry the ambition (Derived center / Principal-part cotangent / Dirac probe / Scalar anomaly / Radial-Moyal) | 3 | 9319-9330 |
| C178 | Punch92: "Locality from first principles" derivation section (4 derivations: equal-time delta brackets / Q-exact translations / Dolbeault Q-exact antiholomorphic / principal parts as local cohomology) ⇒ factorization is algebra of local measurements | 3 | 9331-9362 |
| C179 | Punch93: "Lack of locality" where appropriate: formal holomorphic direction is jet direction; locality means holomorphic factorization, not causal propagation | 3 | 9363-9373 |
| C180 | Punch94: "What is not proved" section before conclusion (7 items: full global twisted-M-theory / unreduced BV principal-part / full quantum descendant lift / Costello graph / QME anomaly / regulator independence / Rees-Fourier interpolation) | 3 | 9374-9386 |
| C181 | Punch95: Conclusion stating synthesis: "closed fields are not merely functions evaluated on branes; they are derived central operations" + "cotangent closed field is not polynomial descendant; it is transverse residue current" | 3 | 9387-9395 |
| C182 | Punch96: Fix theorem status of "full closed CE/cotangent lift": abstract CE/PV cochain-level resolved / reduced post-contraction principal-part boundary resolved / unreduced BV/factorization principal-part lift open / quantum cotangent descendant lift conditional — globally consistent | 4 | 9396-9408 |
| C183 | Punch97: "Old problem resolved" notation; specify which part of Problem 0.2.46 is resolved and which remains open | 3 | 9410-9417 |
| C184 | Punch98: Replacement Theorem 0.1.20 with 7-part structure (derived center / generator dictionary / moment-map shadow / principal-part dual / stable PBW open shadow / scalar anomaly / quantum status) | 4 | 9419-9503 |
| C185 | Punch99: Precise language for "moment-map shadow" $J: h\to A_\partial$, $J(f)=O_f=\Phi(u_f)$ — composite $f\mapsto u_f\to C^\bullet_{\mathrm{CE}}\to A_\partial$, NOT $f\mapsto c_f$ | 3 | 9504-9531 |
| C186 | Punch100: "Ordinary center is not enough" proof: Hochschild centrality of $O_f$ tautological in graded-commutative reduced model; nontrivial statement is Lichnerowicz $d_\pi O_f=[\pi,O_f]=X_{O_f}$ = CE differential of $u_f$ | 4 | 9533-9578 |
| C187 | Punch101: Explicit formula for $d_\pi O_f$: $d_\pi O_K=C^L_{KJ}O_L\theta^J$ or $\sum O_{\{f,e_i\}}\theta^i$; $O_f$ not closed unless $f$ central; degree-zero function whose derived-center differential is its Hamiltonian vector field | 3 | 9579-9617 |
| C188 | Punch102: Physical interpretation of $d_\pi O_f$: boundary Hamiltonian function determines infinitesimal canonical transformation of all open observables; central operation produced by closed insertion through brane OPE | 3 | 9618-9639 |
| C189 | Punch103: Make $P_0$-center definition explicit: commutative dg algebra with appropriate-degree Poisson bracket; $Z^{P_0}(A)=(\mathrm{PV}(A),[\pi,-])$; bracket on center is Schouten | 3 | 9640-9660 |
| C190 | Punch104: "Why CE of $T^*[1]h$ equals functions on derived center" conceptual proof via shifted symplectic language: $\mathcal O(T^*[1]Bh)=C^\bullet_{\mathrm{CE}}(h\ltimes h^\vee[1])$; $T^*[1]h^\vee\sim h^\vee\oplus h[1]$ | 3 | 9661-9688 |
| C191 | Punch105: "Dirac bracket vs Poisson bracket" clarification: constraints first-class, Poisson bracket of gauge-invariant functions descends, do not call Dirac bracket; use "Dirac reduction" for constraints | 3 | 9689-9712 |
| C192 | Punch106: Make $Tr\,f(\phi_1,\phi_2)$ ordering conventions precise: classical = ordering-independent class in $H^0(Q)$; quantum = Weyl ordering $Tr\,\mathrm{Op}_W(f)(X,Y)$; keep separate | 3 | 9713-9735 |
| C193 | Punch107: Classical ordering independence theorem: for any two words $w,w'$ with same multidegree, $Tr\,w(\phi_1,\phi_2)-Tr\,w'(\phi_1,\phi_2)=Q(\cdots)$ via adjacent swaps; commutative $f\mapsto O_f$ well-defined | 3 | 9736-9750 |
| C194 | Punch108: Quantum ordering dependence not $Q$-exact automatically: classical $Q$-exact replaced by Weyl-ordering convention plus Capelli renormalization | 3 | 9751-9756 |
| C195 | Punch109: Finite-$N$ trace identities not killed by $Q$: $H^0(R_N^{GL_N},Q)$ still has finite-$N$ identities; only stable $N\to\infty$ frees primitives | 3 | 9757-9770 |
| C196 | Punch110: Treat $Tr(\psi)$ carefully: $Q\,Tr\,\psi=Tr[\phi_1,\phi_2]=0$, $Tr\,\psi\leftrightarrow\rho_{0,0}\leftrightarrow 1$, removed by scalar reduction | 2 | 9771-9786 |
| C197 | Punch111: "Full higher-$\psi$ problem" section as named research problem: complete primitive stable Koszul homology of $C\langle x,y,\psi\rangle_{\mathrm{cyc}}$ with $Q\psi=[x,y]$; current paper uses no-$\psi$ and one-$\psi$ Hamiltonian sectors only | 3 | 9787-9802 |
| C198 | Punch112: "Relation to cyclic homology" appendix: speculative/conjectural relation to LQT and derived commutative algebra; explain without overclaiming | 2 | 9803-9809 |
| C199 | Punch113: Fix notation $A,\bar A,A_\partial,A_\hbar$: define $A_{\mathrm{poly}}=\mathbb C[z_1,z_2]$, $\bar A=A_{\mathrm{poly}}/\mathbb C$, $h=\mathbb C[[z_1,z_2]]/\mathbb C$, $A_\partial=S(h)$, $A_{\partial,\mathrm{poly}}=S(\bar A)$ — use consistently | 3 | 9810-9849 |
| C200 | Punch114: "Continuous dual" defined in two cases (strict $(\prod H_d)^\vee_{\mathrm{cont}}=\bigoplus H_d^\vee$ vs weighted $h^{\vee,w}_{\mathrm{cont}}=\prod w(d)^{-1}H_d^\vee$); boxed note | 3 | 9850-9874 |
| C201 | Punch115: Proof unweighted Casimir $C_h=\sum e_{d,i}\otimes e^i_d$ does not converge: second factor in $\prod H_d^\vee$, not $\bigoplus H_d^\vee$, hence $C_h\notin h\otimes h^\vee_{\mathrm{cont}}$ | 3 | 9876-9914 |
| C202 | Punch116: Clarify CE/PV theorem does not require Casimir: cochain algebraic derived center independent of BV propagator; Costello graph realization requires coefficient kernel | 3 | 9915-9933 |
| C203 | Punch117: Reassess "universal bar-cobar/Koszul template": full Hamiltonian algebra with linear and $H_2$ modes is not lower-central conilpotent; ensure theorem does not imply full $h$ uses conilpotent template | 4 | 9934-9948 |
| C204 | Punch118: Recast Tate Quillen section as "optional categorical enhancement: admissible Tate bar-cobar envelope" | 2 | 9949-9955 |
| C205 | Punch119: Add exact external theorem citations for factorization center (Costello-Gwilliam / Lurie / Calaque-Pantev-Toën-Vaquié-Vezzosi / Cattaneo-Felder); insert precise reference for $P_0$-center of Poisson algebra as Poisson cochains; do not leave as folklore | 3 | 9956-9972 |
| C206 | Punch120: "Comparison with Gwilliam-Williams" compact paragraph: GW = holomorphic bosonic string on Riemann surface with critical dimension; this paper = local target-space Hamiltonian BF on $\mathbb R^2\times\mathbb C^2$; no imported critical dimension | 2 | 9973-9981 |
| C207 | Punch121: Remove apologetic phrasing: avoid "not a theorem", "only a shadow", "not yet"; use "the theorem is the reduced formal local theorem", "the analytic graph realization is a separate problem", "the PBW descendant sector is a special-fibre theorem" | 2 | 9982-9991 |
| C208 | Punch122: "Proof skeleton" before long proofs: identify generators / compute differential on generators / verify... | 2 | 9994-9999 |
| C209 | Punch123: Shorten introduction by moving technical machinery later (Quillen, weighted Tate, nilpotent truncation, Hadamard parametrix, cross-volume) | 3 | 10006-10020 |
| C210 | Punch124: "Minimal study path" in introduction; identify core theorem sections vs optional categorical Tate / weighted regulator appendices | 2 | 10022-10027 |
| C211 | Punch125: Exact replacement for problematic part (ii) of umbrella theorem: "two are not in conflict because they answer different questions; PBW SF symbols vs deformation-correct coadjoint modes; Rees/Fourier $D_\hbar$-module interpolation a further construction" | 4 | 10028-10056 |
| C212 | Punch126: Exact replacement for problematic part (iii) of umbrella theorem: $u_{a(t)dt\otimes f}\mapsto B_f(a)$, $c_\lambda\mapsto\theta_\lambda$ | 5 | 10058-10092 |
| C213 | Punch127: Exact replacement for cotangent reduced theorem: $A^{\mathrm{pp}}_\partial(I)=S(h_I)\otimes S(\mathcal P_I[1])$ enlarged reduced principal-part defect-current model; $\partial^{\mathrm{pp}}_{\mathrm{bb}}(f)=B_f, \partial^{\mathrm{pp}}_{\mathrm{bb}}(\rho[1])=\Theta_\rho$, $\{B_f,\Theta_\rho\}=\Theta_{f\cdot\rho}$ — REDUCED $P_0$-MODEL, unreduced BV realization not automatic | 4 | 10093-10133 |
| C214 | Punch128: Exact replacement for quantum theorem status: degree-zero quantum theorem treats $u_f$-function part of derived center; proves Moyal commutator for Capelli-renormalized stable Weyl traces; cotangent/principal-part descendant sector remains conditional on weighted Tate/QME | 4 | 10134-10145 |
| C215 | Punch129: Theorem about open-line Weyl product independent of Costello: $F\star G=m\circ\exp(\hbar P_\partial/2)(F\otimes G)$ internal to reduced first-order open-line Weyl model; NOT Costello graph realization | 4 | 10147-10166 |
| C216 | Punch130: "Normalization conventions" appendix for Moyal coefficients: $f\star g=m\circ e^{\hbar P/2}(f\otimes g)$, $[f,g]_\star=2\sum_{r\,\mathrm{odd}}\frac{\hbar^r}{2^r r!}P^r(f,g)$; first two coeffs $\hbar P, \hbar^3 P^3/24$ | 3 | 10167-10195 |
| C217 | Punch131: Exact formula for $P^r$ on monomials $P^r(z_1^kz_2^l,z_1^mz_2^n)=\sum_{a=0}^r(-1)^a\binom{r}{a}(k)_{r-a}(l)_a(m)_a(n)_{r-a}z_1^{k+m-r}z_2^{l+n-r}$; only odd $r$ enter commutator | 3 | 10196-10212 |
| C218 | Punch132: $P^3(z_1^4,z_2^4)$ coefficient consistency check: $(4)_3(4)_3=24\cdot 24=576$; in normalized bracket, $\hbar^2/24\cdot 576=24\hbar^2 z_1z_2$ | 2 | 10213-10268 |
| C219 | Punch133: "Finite $N$ vs $N$ in $\mathfrak m^N$" notation warning: avoid using $N$ both for matrix size and truncation order; use $R$ (rank) and $D$ (truncation degree) | 2 | 10269-10289 |
| C220 | Punch134: "Rank $N$ and truncation $D$" global convention | 2 | 10290-10295 |
| C221 | Punch135: Fix "dimension 1+4" phrasing: $\mathbb R^2\times\mathbb C^2$ is $2+4=6$ real dimensions; better notation $\mathbb R_{\mathrm{brane}}\times\mathbb R_{\mathrm{top,normal}}\times\mathbb C^2_{\mathrm{hol}}$ | 2 | 10296-10314 |
| C222 | Punch136: Notation for $x_1,x_2$ topological coordinates; brane is $\mathbb R_{x_1}\times\{x_2=0\}\times\{p\}$ | 2 | 10315-10324 |
| C223 | Punch137: Avoid "boundary" when it is a defect; brane is line defect not boundary of spacetime; use "bulk-to-defect" or "bulk-to-brane" | 3 | 10325-10339 |
| C224 | Punch138: "Bulk-to-boundary" vs "bulk-to-defect" convention disclaimer | 2 | 10340-10345 |
| C225 | Punch139: Exact proof of Darboux equivariance of substitution: not literal for noncommuting matrices at finite $N$, but well-defined after $Q$-cohomology / stable commutative reduction | 3 | 10347-10363 |
| C226 | Punch140: Treat noncommutative formal symplectomorphisms carefully: ordering ambiguities exact in $H^0(Q)$, formal Darboux acts on commutative Hamiltonian labels | 3 | 10364-10372 |
| C227 | Punch141: "Index conventions for monomials" note: $H_{a,b}=z_1^az_2^b$, $a,b\ge 0$, $a+b>0$; $H_{m,n}=0$ for $m<0,n<0,m+n=0$ after scalar reduction | 2 | 10373-10389 |
| C228 | Punch142: Sign of Hamiltonian vector field $X_f=(\partial_{z_1}f)\partial_{z_2}-(\partial_{z_2}f)\partial_{z_1}$, $\iota_{X_f}\omega=-df$, $X_f(g)=\{f,g\}$; keep convention globally | 3 | 10390-10432 |
| C229 | Punch143: Sign sanity check $X_{z_1}=\partial_{z_2}, X_{z_2}=-\partial_{z_1}$, $\{z_1,z_2\}=1$ | 2 | 10433-10463 |
| C230 | Punch144: Verify principal-part action signs against convention: $\langle f\cdot\rho,g\rangle=-\langle\rho,\{f,g\}\rangle$, derive $f\cdot\rho_{a,b}=-(pb-qa+p-q)\rho_{a-p+1,b-q+1}$ explicitly | 4 | 10464-10512 |
| C231 | Punch145: Clarify "negative-index targets zero" rule for principal-part action | 2 | 10513-10516 |
| C232 | Punch146: Principal-part examples computed: $z_1\cdot\rho_{a,b}=-(b+1)\rho_{a,b+1}$, $z_2\cdot\rho_{a,b}=(a+1)\rho_{a+1,b}$ — clearer than "lowering" | 3 | 10517-10563 |
| C233 | Punch147: Fix any place saying $z_1$ lowers principal-part indices; raises $b$-pole order | 2 | 10564-10571 |
| C234 | Punch148: Compare polynomial descendant action $\Psi_{a,b}\mapsto b\Psi_{a,b-1}$ vs principal-part $\rho_{a,b}\mapsto -(b+1)\rho_{a,b+1}$ — opposite shift, different coefficient, different module | 4 | 10572-10609 |
| C235 | Punch149: Do not call polynomial action "raising" — use "symmetric PBW action" instead | 2 | 10610-10620 |
| C236 | Punch150: "Module mismatch lemma": $\Psi_{a,b}\mapsto\rho_{a,b}$ does not intertwine $z_1$; only label identification | 4 | 10621-10654 |
| C237 | Punch151: "Rees interpolation must change category": cannot live in ordinary polynomial modules; must pass through distributions or $D_\hbar$-modules | 4 | 10655-10661 |
| C238 | Punch152: Rework principal-parts note into paper section: bring in conceptual content, correct formulas | 3 | 10663-10668 |
| C239 | Punch153: Make "position vs momentum" analogy mathematically precise: functions↔coordinates on $h^\vee$, polyvector fields↔derivations, principal parts↔distributions supported at brane | 3 | 10669-10681 |
| C240 | Punch154: "Defect current" notation $\Theta_\rho(B)$ for $B\in\mathcal D'_c(I)$, smeared with $b(t)dt$; pair with $\Omega^\bullet_c(I)$ | 3 | 10683-10711 |
| C241 | Punch155: Clarify $\Theta_\rho$ parity: $\mathcal P[1]$ is shifted, state $|\Theta_\rho|=?$, verify $\{\Theta_\rho,\Theta_\sigma\}=0$ compatible with graded antisymmetry | 3 | 10712-10735 |
| C242 | Punch156: Finite-dimensional toy model BEFORE $\mathbb C[[z_1,z_2]]$: finite Lie $\mathfrak l$ with $C^\bullet_{\mathrm{CE}}(\mathfrak l\ltimes\mathfrak l^\vee[1])\cong\mathrm{PV}(S(\mathfrak l))$; intuition for infinite Tate case | 4 | 10736-10751 |
| C243 | Punch157: Exact toy proof: with basis $e_i$, $C^\bullet_{\mathrm{CE}}=S(u_i)\otimes\Lambda(c^i)$, $\mathrm{PV}(S(\mathfrak l))=S(O_i)\otimes\Lambda(\theta^i)$, $u_i\mapsto O_i, c^i\mapsto\theta^i$ becomes main theorem by completion | 4 | 10752-10782 |
| C244 | Punch158: "What is $Z^{P_0}_{\mathrm{fact}}$ on an interval?" — for locally constant factorization algebra from $A$, center stalk is Hochschild cochains; for Poisson compatibility, $P_0$-center is Poisson cochains; on intervals $Z^{P_0}_{\mathrm{fact}}(A_\partial)(I)\simeq\mathrm{PV}(A_\partial(I))$ | 3 | 10783-10814 |
| C245 | Punch159: Fix factorization product direction arrows; CE cochains contravariant unless using chains/cosheaves; recommendation: define every object as factorization algebra of compactly supported observables (covariant) | 4 | 10815-10843 |
| C246 | Punch160: Consider factorization coalgebras for CE cochains: $I\mapsto h_I$ cosheaf, CE chains naturally factorization coalgebra, CE cochains dual; compactly supported observables/density-duals so completed CE cochain assignment is covariant under extension by zero | 4 | 10846-10862 |
| C247 | Punch161: Exact treatment of compact support and distributions: source $h_I=\Omega^\bullet_c(I)\otimes h$ has compact support, dual involves distributions on $I$; $B_f(a)$ uses compactly supported density not a distribution; keep source and dual separate | 3 | 10863-10874 |
| C248 | Punch162: "Density vs function" convention: $a(t)$ in $\int a(t)dt$ is density $a(t)dt\in\Omega^1_c(I)$; avoid ambiguity | 3 | 10875-10887 |
| C249 | Punch163: Orientation convention for brane line; symplectic potential depends on orientation | 2 | 10889-10897 |
| C250 | Punch164: Clarify boundary terms in open action: reducing $\frac12\int Tr(\phi_1d\phi_2-\phi_2d\phi_1)$ to $\int Tr\phi_1d\phi_2$ discards boundary term — compactly supported variations / local operators in interior / fixed boundary values | 3 | 10898-10918 |
| C251 | Punch165: Prove gauge invariance of open action; move into Dirac theorem | 3 | 10920-10921 |
| C252 | Punch166: Clarify role of $A$ as 1-form gauge field: both Lagrange multiplier and connection; in 1D, no curvature, imposes moment map | 2 | 10923-10925 |
| C253 | Punch167: BRST/BV field table (4 columns: field / form-Ext degree / ghost number / role): $A$, $\phi_1$, $\phi_2$, $\psi=A^*$; consistent signs/degrees | 3 | 10927-10944 |
| C254 | Punch168: Define $\psi$ degree consistently: $Q\psi=[\phi_1,\phi_2]$ ⇒ $|Q|=1$ ⇒ $\psi$ degree $-1$ or $1$ depending on chain/cochain convention; state once | 3 | 10946-10954 |
| C255 | Punch169: Revisit "$S(V)$ means free graded-commutative algebra" with shifts: if $V[1]$ has parity reversed, $S(V[1])$ is exterior on even $V$; $S(\bar A_{\mathrm{desc}}[1])$ exterior if descendants odd | 3 | 10955-10970 |
| C256 | Punch170: "Odd ideal abelian" sign check: $[\rho[1],\sigma[1]]=0$ symmetric or antisymmetric depending on bracket degree; verify with $P_0$ convention | 3 | 10972-10977 |
| C257 | Punch171: Avoid calling $\mathcal P[1]$ "odd local-dual ideal" without degree convention; use "shifted local-dual ideal" with degree | 2 | 10982-10989 |
| C258 | Punch172: Insert proof of Jacobi for $A^{\mathrm{pp}}_\partial$: $[f,[g,\rho]]-[g,[f,\rho]]=[[f,g],\rho]$ by coadjoint representation; smearing $a(bB)-b(aB)=abB$ for smooth $a,b$ and distribution $B$ | 3 | 10990-11003 |
| C259 | Punch173: "Do not multiply distributions" note in Jacobi proof: bracket of two $\Theta$'s set to zero avoids distribution products | 4 | 11004-11006 |
| C260 | Punch174: Exact definition of $f\cdot\rho=\pi_{\mathrm{pp}}\{f,\rho\}$: define as Lie derivative $f\cdot\rho=-\mathcal L_{X_f}\rho$ (negative Lie derivative for coadjoint on densities); verify sign against formula | 4 | 11007-11032 |
| C261 | Punch175: Use "residue currents" instead of "Laurent forms" when emphasizing physics | 2 | 11033-11042 |
| C262 | Punch176: Add Grothendieck residue citation to standard source for local residues / local cohomology | 2 | 11043-11046 |
| C263 | Punch177: Re-evaluate "unique $h$-equivariant continuous pairing": equivariance follows for pairing between $\mathcal P$ and $h$, but uniqueness "of total degree zero" requires proof or replace with "canonical" | 3 | 11047-11051 |
| C264 | Punch178: Local cohomology exact sequence $H^2_\mathfrak{m}(R)\cong\mathbb C[z_1^{-1},z_2^{-1}]/(\mathbb C[z_1,z_1^{-1}]+\mathbb C[z_2,z_2^{-1}])$ or Čech model — grounds $\mathcal P$ | 3 | 11052-11066 |
| C265 | Punch179: Čech representative $H^2_\mathfrak{m}(R)=R[z_1^{-1},z_2^{-1}]/(R[z_1^{-1}]+R[z_2^{-1}])$, basis $z_1^{-a-1}z_2^{-b-1}$, multiply by $dz_1dz_2$ | 3 | 11067-11086 |
| C266 | Punch180: Tie principal parts to Verdier / local duality: $H^2_\mathfrak{m}(R)dz_1dz_2$ is Matlis dual of completed local ring $R^\wedge_\mathfrak{m}$ — exactly the continuous dual | 4 | 11087-11106 |
| C267 | Punch181: "Matlis dual" phrase: $\mathcal P\simeq\mathrm{Hom}_{\mathrm{cont}}(\mathbb C[[z_1,z_2]]/\mathbb C,\mathbb C)$ is the reduced Matlis dual | 4 | 11107-11115 |
| C268 | Punch182: Recast principal-part theorem in Matlis dual language: "reduced Matlis dual of $h$ is $\mathcal P$, Hamiltonian Lie derivative realizes coadjoint action" — much more standard than "principal-part residue module" alone | 4 | 11116-11119 |
| C269 | Punch183: Continuity of residue pairing: continuous functional on $\mathbb C[[z_1,z_2]]$ with $\mathfrak m$-adic topology depends on finitely many coefficients; $\mathcal P$ as direct sum of $\rho_{a,b}$ exactly gives finite coefficient-extraction sums; weighted product $\mathcal P^w$ different completion | 3 | 11120-11135 |
| C270 | Punch184: Clarify completed $h^\vee$ in closed BF action: direct sum (finite Taylor-dual support for $\beta$) vs weighted product (infinite dual support for $\beta$); state which model each theorem uses | 4 | 11136-11150 |
| C271 | Punch185: "Strict model" vs "weighted model" notation: $g_{\mathrm{str}}=h\ltimes\mathcal P[1]$ vs $g^w=h^w\ltimes\mathcal P^w[1]$; do not use same $g$ for both | 4 | 11151-11168 |
| C272 | Punch186: "Dense inclusion" theorem $\mathcal P\hookrightarrow\mathcal P^w$ for finite-support principal parts; strict polynomial sector embeds into weighted regulator | 3 | 11169-11178 |
| C273 | Punch187: Exact statement of graphwise RG limitation: each fixed graph controlled, but not convergence of sum over graphs; "graphwise boundedness is not perturbative renormalizability by itself" | 4 | 11179-11186 |
| C274 | Punch188: Move Costello-Li failure analysis to appendix or keep concise; main text summarizes (noncompact, mixed top-hol, brane defect, $\mathfrak{gl}_N$ not $\mathfrak{gl}(N|N)$, coefficient Tate direction) | 3 | 11187-11197 |
| C275 | Punch189: Avoid sounding like you refute Costello-Li; say "Costello-Li theorem is not applicable to this local mixed defect model without additional work" | 3 | 11198-11210 |
| C276 | Punch190: "Why ordinary $\mathfrak{gl}_N$ retains $U(1)$ anomaly" paragraph: Costello-Li supertrace cancellation uses $\mathfrak{gl}(N|N)$; ordinary $\mathfrak{gl}_N$ has trace $N$; tie to $[\bar c]$ | 3 | 11211-11220 |
| C277 | Punch191: Clarify "Capelli shift as $U(1)$ charge": $\hbar N$ is charge of central direction; $Tr(I)=N$ ⇒ central moment relation has scalar $N$ | 3 | 11221-11230 |
| C278 | Punch192: "Background independence" caveat: formal local model depends only on formal Darboux disk; global backgrounds require choices | 3 | 11231-11234 |
| C279 | Punch193: "Minimal theorem-only version" appendix: 3 pure math theorems extractable (CE cochains of $T^*[1]h$ = Poisson cochains of $S(h)$ / $h^\vee_{\mathrm{cont}}=\mathcal P$ for $h=\mathbb C[[z_1,z_2]]/\mathbb C$ / stable trace yields $S(\bar A\oplus\bar A_{\mathrm{desc}}[1])$) | 3 | 11235-11253 |
| C280 | Punch194: "Physics-only summary" appendix (2 pages); helps interdisciplinary readership | 2 | 11254-11257 |
| C281 | Punch195: Theorem name consistency check: avoid "Koszul duality" for CE/PV center / "factorization equivalence" when reduced post-contraction / "universal" when conditional / "closed string" when formal local closed sector | 3 | 11258-11270 |
| C282 | Punch196: Replacement table of contents (12 sections: Dirac probes / local mixed BV model / open brane reduction stable traces / closed Hamiltonian BF / CE/PV derived-center / principal parts / factorization on brane line / PBW SF descendants / scalar anomaly / quantum Weyl/Moyal / weighted Tate regulator / appendices) | 4 | 11271-11288 |
| C283 | Punch197: Move Tate Quillen equivalence after CE/PV theorem; do not introduce model category before central theorem | 3 | 11289-11293 |
| C284 | Punch198: Move "Cross-volume convention contract" out of paper entirely; keep as private doc | 4 | 11294-11296 |
| C285 | Punch199: Final "research program" list (7 items): Rees/Fourier interpolation / unreduced BV principal-part currents / regulator independence weighted Tate / full quantum descendant lift / Costello graph realization / global descent over hol-symplectic surfaces / full higher-$\psi$ primitive Koszul homology | 4 | 11297-11307 |
| C286 | Punch200: Highest-priority edits "do these first" (10 items: $u$-source, $\Omega^\bullet_c$, delete same-module sentence, no-go lemma, Schur ⇒ local-cohomology, rename pp sector, split umbrella theorem, claim-strength ledger, cross-volume out, sign-convention appendix) | 5 | 11309-11346 |
| C287 | Punch201: One-paragraph strongest-version vision: theorem-driven Dirac-Witten local model; brane stack as constrained matrix probe of formal symplectic disk; closed CE observables as derived Poisson central operations on open algebra; polynomial $\Psi_{a,b}$ as PBW SF shadow; principal parts as transverse residue currents; $U(1)$ anomaly same class classically and quantum; $W/M$ deformation governs degree-zero quantum sector; Costello graph realization isolated as analytic theorem | 5 | 11347-11366 |

**Inventory total.** 287 distinct items (C01–C287) across six rounds.

**[CHECKPOINT: critique inventory complete; all 287 items written to file.]**

---

## T2/T3. Cross-Map to Plan and Master Ledger

Legend: **A** = addressed (plan section explicit); **P** = partially addressed (acknowledged but watered down or deferred); **S** = silently dropped; **R** = refuted. Plan refs are line numbers in `platonic-ideal-plan-2026-04-28.md`. Master refs are `M-XX` IDs in `attack-heal-platonic-2026-04-28.md`.

### Round 1 — hostile-referee attack (C01–C17)

| # | Class | Plan ref | Master ref | Notes |
|---|---|---|---|---|
| C01 (Title overclaim) | A | §6 item 5, §5 title (lines 581-593) | — | Plan promotes to deformation-level CE/PV theorem with new title "Closed Hamiltonian BF Theory as the Derived Poisson Centre…" |
| C02 (CE-source error) | A | §0 D2 (lines 50-57); §3 Theorem C (lines 236-291); §6 item 1 | M-16 | Plan installs $u_I\mapsto O_I$ globally; M-16 verifies |
| C03 (Module mismatch) | A | §0 D3 (lines 58-69); §3 Thm D embedded no-go (lines 321-331); §6 item 3-4 | M-02 | Plan installs no-go lemma; M-02 sharpens to structural impossibility |
| C04 (Cor 0.2.51 false) | A | §3 Thm G action items (lines 446-449), §6 item 4 implicit | M-12 | Scalar reduction made explicit; M-12 differentiates index-pair vs trace-pair Capelli |
| C05 (Tautological centrality) | A | §7 N11 (lines 781-792) | — | Plan calls out: "ordinary Hochschild centrality of $O_f$ is tautological in graded-commutative reduced models, but the non-trivial statement is Poisson centrality" |
| C06 (Sector selected by hand) | A | §3 Thm B critical disclaimer (lines 220-225); §6 item 3 | — | Sector exclusions remain explicit |
| C07 (Three large-$N$) | A | §7 N10 (lines 770-779) | M-10 | Plan dedicates one-page subsection; M-10 already named distinguishing operations on empty trace |
| C08 (Quotient stack issue) | P | §3 Thm A (lines 184-201) | — | Plan does not explicitly distinguish algebraic invariants vs CE/BRST cohomology of full gauge algebra; partial coverage in Theorem A statement |
| C09 (One-$\psi$ proof) | A | §3 Thm B action items (lines 226-234); §7 N2 (lines 705-713) | — | Plan dedicates appendix with seven specific lemmas |
| C10 (Tate / Koszul foundations) | A | §7 N1 (lines 695-703); appendix path | M-01, M-25 | M-01 gives the structural diagnosis (Tate-conilpotency fails for perfect $\mathfrak h$); plan invokes nilpotent truncation + weighted regulator + Mittag-Leffler |
| C11 (Closed sector formal BF) | A | §0 (lines 26-35); §1 thesis (lines 80-105); §5 reorganization (lines 583-594) | — | Plan adopts "Hamiltonian BF for formal symplectic disk" as primary terminology |
| C12 (BCOV analogy danger) | A | §6 item 10 (lines 660-667); §5 demote BCOV (lines 562-567) | M-22 | Plan tightens BCOV to one paragraph; M-22 calls for one-sentence disclaimer |
| C13 (Quantum target only) | A | §3 Thm F (lines 391-425); §4 Obligations IV-V; §0 D-status conditional | M-03 | Theorem F$'$ explicitly conditional; Obligation V the analytic theorem |
| C14 (Central extension U(1)) | A | §3 Thm G (lines 426-449); §6 item 7 | M-09, M-12, M-32 | Plan promotes scalar anomaly; M-09 weight-bidegree decomp; M-12 trace vs index pair |
| C15 (Figures ornamental) | S | — | — | No explicit plan section addresses figures; plan's appendix list does not include "upgrade or remove figures" |
| C16 (Citation cleanup) | A | §6 item 11 (lines 668-675) | — | Citation audit; precise factor $P_0$-centre citation requested |
| C17 (Defensible safe theorem) | A | §3 Thm B + Thm C; §6 item 5 | — | Plan's explicit decomposition into A-G blocks subsumes the safe-fallback |

### Round 2 — constructive derived-center proposal (C18–C24)

| # | Class | Plan ref | Master ref | Notes |
|---|---|---|---|---|
| C18 (CE/PV center theorem) | A | §1 (lines 80-105); §3 Thm C (lines 236-291); §7 N1 | M-01 | Central platonic theorem; M-01 splits into C₁/C₂ |
| C19 (Generator-level $\Phi$) | A | §3 Thm C proof skeleton (lines 263-275); §6 item 8 sign appendix | M-01 (C₁) | Generator-level identity is C₁ |
| C20 (Resolution of CE-source) | A | §0 D2; §3 Thm C; §6 item 1 | M-16 | Plan inscribes $u_I\mapsto O_I$ |
| C21 (Boundary bracket recovery) | A | §3 Thm C statement (lines 252-261); §7 N1 ends with moment-map shadow | — | Moment-map shadow is the degree-zero corollary |
| C22 (Factorization $C_c^\infty\otimes h$) | A | §3 Thm E (lines 342-389); §6 item 2 | M-17 | Plan replaces $C_c^\infty$ by $\Omega^\bullet_c$; this fixes C22's instance, but C22's "$C_c^\infty(I)$ is fine" was actually a Round-2 STARTING-POINT, so really resolved by C73/C89/M-17 |
| C23 (One-$\psi$ + principal-part) | A | §3 Thm D (lines 292-340); §6 items 3-7 | M-02 | Plan installs principal-part module + no-go |
| C24 (Replacement theorem) | A | §3 Thm C; §6 item 1; §5 replacement abstract | M-16, M-01 | Plan's central theorem statement |

### Round 3 — Diracian rewrite (C25–C33)

| # | Class | Plan ref | Master ref | Notes |
|---|---|---|---|---|
| C25 (Diracian voice) | A | §1, §2 (Three Diracian principles) (lines 110-170); §5 voice & prose (lines 595-602) | — | Plan adopts Russian-school + Diracian-physical voice |
| C26 (Factorization first-principle origin) | A | §2 (locality from three principles) (lines 156-170) | M-20 | Plan derives factorization from Diracian principle |
| C27 (Forced first-order action) | A | §2 Principle 1 (lines 119-127); §3 Theorem A (lines 183-203) | — | Plan installs Dirac-reduction-in-homological-form |
| C28 (Three notions of locality) | A | §2 (lines 156-170) | M-20 | Plan lists three notions; M-20 calls for explicit derivation in `principles.tex` |
| C29 (Distributional locality) | A | §2 (lines 165-167); §7 N9 (lines 763-769) | M-23, M-36 | Plan installs distribution-locality subsection |
| C30 (Distributional boundary current $\Theta_\rho$) | A | §3 Thm D (lines 292-340); §6 item 7; Notation index $\Theta_\rho$ row (lines 686) | — | Plan installs $\Theta_\rho$ as enlarged reduced defect-current generator |
| C31 (Unitarity replacement) | A | §2 (lines 168-171); §6 voice (line 599) | M-21 | Plan articulates CME/QME + factorization associativity; M-21 calls for unitarity table |
| C32 (Diracian opening passage) | A | §1 thesis paragraph (lines 80-105); §5 replacement abstract (lines 569-580) | — | Plan installs verbatim opening |
| C33 (Thesis sentence) | A | §1 (lines 80-105) | — | Plan installs verbatim |

### Round 4 — first-principles synthesis (C34–C68)

| # | Class | Plan ref | Master ref | Notes |
|---|---|---|---|---|
| C34 (Local BV not global string) | A | §0; §6 voice (line 599); §9 cross-volume isolation | — | Plan downgrades global rhetoric |
| C35 (Divergence-free reduction) | P | §2 Principle 1 (lines 119-127) | — | Plan installs Hamiltonian Lie algebra $\mathfrak h$ but does not include explicit Poincaré-lemma divergence-free derivation; deferred |
| C36 (Open brane sector first-principles) | P | §3 Thm A (lines 183-203) | — | Plan asserts but does not derive A-brane $\otimes$ B-brane $\otimes$ Koszul-resolution origin |
| C37 (Dirac interpretation of action) | A | §2 Principle 1; §3 Theorem A | — | Plan installs |
| C38 (Jet contraction / Euler) | S | — | — | Plan does NOT explicitly derive local-operator reduction from $[d_R,\iota_{\partial_t}]=\partial_t$; presumed in Theorem A but argument elided |
| C39 (Procesi-Razmyslov stability) | A | §3 Theorem B proof skeleton (lines 215-219) | — | Plan invokes Procesi-Razmyslov stable invariants |
| C40 (Adjacent-swap exactness) | A | §3 Theorem B proof skeleton (lines 216) | — | Plan installs |
| C41 ($\Psi_{a,b}$ + chip-moving) | A | §3 Thm B action items; §7 N2 (lines 705-713) | — | Plan dedicates appendix |
| C42 (Sector exclusion $Tr(\psi)$) | A | §6 item 3; §0 D3 | — | Plan installs sector-exclusion narrative |
| C43 (PBW-SF disclaimer) | A | §0 D1; §3 Thm B (lines 220-225); §6 item 3 | — | Plan installs critical disclaimer |
| C44 (Degree-zero bracket calc) | A | §3 Thm C; §3 Thm G | — | Plan installs |
| C45 (Scalar central subtlety) | A | §3 Thm G (lines 426-449); §6 item 7 explicit warning | M-09, M-12 | Plan installs scalar anomaly thread |
| C46 (CE-source obstruction root) | A | §0 D2; §3 Thm C statement | — | Plan installs |
| C47 (Corrected derived center theorem) | A | §3 Thm C central position; §6 item 1; §7 N1 | M-01, M-16 | Plan installs |
| C48 (Why principal parts) | A | §2 Principle 3 (lines 141-155); §3 Thm D | — | Plan installs |
| C49 (PP coadjoint action signs) | A | §6 item 8 sign appendix (lines 644-654); §3 Thm D action items (lines 332-340) | — | Plan installs explicit derivation $z_1\cdot\rho_{a,b}=-(b+1)\rho_{a,b+1}$, etc. |
| C50 ($\Psi$ vs $\rho$ direction opposite) | A | §3 Thm D embedded no-go (lines 321-331); §6 item 3 | M-02 | Plan installs |
| C51 (No-go from local nilpotence) | A | §3 Thm D embedded no-go (lines 321-331) | M-02 | Plan elevates as numbered theorem |
| C52 (Local-dual boundary sector) | A | §3 Thm D + §4 Obligation I; §6 item 7 (lines 642-647) | — | Plan installs $A^{\mathrm{pp}}_\partial$ as enlarged reduced defect-current model |
| C53 (Dirac interpretation principal parts) | A | §2 Principle 3; §3 Thm D | — | Plan installs |
| C54 (Witten centrality) | A | §2 Principle 2 (lines 129-138); §7 N11 | — | Plan installs |
| C55 (Three notions of locality) | A | §2 (lines 156-170) | M-20 | Plan installs |
| C56 (Unitarity replacement) | A | §2 (lines 168-171) | M-21 | Plan installs |
| C57 (Quantum Moyal target $\hbar P/2$) | A | §3 Thm F (lines 391-425); §6 voice; §7 N3 | — | Plan installs |
| C58 (Quantum Capelli) | A | §3 Thm G; §3 Thm F$'$; §4 Obligation IV | M-12, M-32 | Plan installs explicitly conditional |
| C59 (Costello graph problem checklist) | A | §4 Obligation V (lines 504-513); §7 N8 (lines 754-762) | — | Plan installs as boxed problem |
| C60 (Three-theorem global thesis) | A | §3 Thm A-G architecture (lines 174-450); §5 reorganization | — | Plan installs six (+G) blocks |
| C61 (Errata 1 PP linear sign) | A | §3 Thm D action items (lines 332-340); §6 item 8 | — | Plan reverses any wrong-direction prose |
| C62 (Errata 2 polynomial direction) | A | §3 Thm D embedded no-go; §6 item 3-4 | — | Plan disambiguates |
| C63 (Errata 3 reference formula) | A | §3 Thm D | — | Plan adopts as reference formula |
| C64 (Errata 4 smeared bracket scalar quotient) | A | §3 Thm G; §6 item 4 (implicit) | M-09 | Plan installs scalar-quotient discipline |
| C65 (Errata 5 removing constants vs U(1)) | A | §3 Thm G action items (lines 446-449) | — | Plan disambiguates |
| C66 (Errata 6 closed-open sharpening) | A | §1, §3 Thm C, §4 Obligation I | M-16 | Plan installs |
| C67 (Errata 7 references) | A | §6 item 11 | — | Plan installs |
| C68 (Errata 8 figures) | S | — | — | Same gap as C15: figures not addressed |

### Round 5 — second-pass critique (C69–C86)

| # | Class | Plan ref | Master ref | Notes |
|---|---|---|---|---|
| C69 (Persistent factorization source error) | A | §6 item 1 (lines 612-616); §3 Thm E correction (lines 369-381) | M-16 | Plan installs HIGHEST-PRIORITY edit |
| C70 ($\Psi\to\rho$ not strict $P_0$) | A | §3 Thm E "Critical correction"; §6 item 6 (rename); §3 Thm D no-go | M-02, M-15 | Plan installs |
| C71 (Distinguish PBW vs distributional sectors) | A | §3 Thm B critical disclaimer; §3 Thm D enlarged sector; §6 item 3 | — | Plan installs |
| C72 (Interpolation only via Rees $D_\hbar$) | A | §4 Obligation II (lines 469-478); §7 N5 (lines 731-739) | M-02 | Plan reformulates as Obligation II / construction N5; M-02 sharpens |
| C73 ($\Omega^\bullet_c$ not $C_c^\infty$) | A | §6 item 2 | M-17 | Plan installs |
| C74 (Radial-parts theorem armoring) | A | §3 Thm F$'$ (lines 405-425); §7 N3 (lines 716-722); §4 Obligation status | — | Plan installs Theorem F$'$ + N3 standalone proof obligations |
| C75 (Weighted Tate as regulator) | A | §4 Obligation III (lines 481-490); §7 N6 | M-11 | Plan installs admissible-only regulator-independence |
| C76 (Schur rigidity → local cohomology) | A | §3 Thm D action items (lines 332-340); §6 item 5 | M-06 | Plan installs Matlis local-cohomology uniqueness |
| C77 (Distinguished anomaly line) | A | §3 Thm G action items (lines 444-449) | M-09 | Plan installs sharpening |
| C78 (Primitive projection rename) | A | §6 item 6 (lines 632-634) | M-15 | Plan installs |
| C79 (Three principles structure first) | A | §2 (lines 110-170); §5 replacement TOC | — | Plan installs |
| C80 (Strongest theorem package) | A | §3 Theorem blocks A-G (lines 174-450) | — | Plan installs |
| C81 (Theorem D detailed) | A | §3 Thm D (lines 292-340) | M-05, M-06 | Plan installs with M-05/M-06 sharpenings |
| C82 (Theorem E detailed) | A | §3 Thm E (lines 342-389) | M-17, M-23, M-24 | Plan installs |
| C83 (Theorem F decomposed) | A | §3 Thm F vs Thm F$'$ split; §4 Obligation V | — | Plan installs |
| C84 (Cross-volume out) | A | §6 item 10; §9 (lines 851-884); §5 reorganization | — | Plan installs |
| C85 (Replacement abstract draft) | A | §5 replacement abstract (lines 569-580) | — | Plan installs |
| C86 (10-item errata list) | A | §6 surgical correction list (lines 605-687); appendix to §10 (lines 937-960) | — | Plan installs |

### Round 6 — exhaustive technical punch list (C87–C287)

For brevity, I summarize this large round in groups; detailed mapping in the audit section below.

**Architectural / structural items (C87, C88, C89, C90, C99, C100, C101, C102, C103, C104, C111, C123, C175, C176, C181, C184, C196, C282, C286).** Class **A** in plan via §3 (theorem blocks), §5 (reorganization), §6 (surgical list), §7 (constructions N1-N11), §8 (sequencing). These are the main edits the plan converts into actionable phases.

**Sign / convention / topology items (C97, C107, C115, C120, C133, C134, C137, C138, C144, C145, C146, C147, C148, C168, C169, C170, C171, C172, C228, C229, C230, C231, C232, C233, C249, C250, C254, C262, C264, C265).** Class **A or P** mostly via §6 item 8 sign appendix and §3 Thm D action items. M-04, M-07, M-25 in master ledger. C133 ($N$ vs truncation $D$ notation collision) is **S** — plan does not warn against this collision.

**Notation / glossary / dictionary items (C118, C119, C138, C174, C199, C220, C221, C222, C223, C224).** Class **A** via §6 item 12 notation index (lines 676-687) and §10 success criteria. Some specifics like C138 "physical dictionary table" appear in spirit but not as an explicit row table.

**Errata / formula / sign-correctness items (C61-C68 echoed in C217, C218, C232, C234, C235, C236, C237).** Class **A** uniformly.

**Distributional locality / cosheaf / factorization-foundations items (C140, C141, C153, C158, C159, C160, C161, C162, C167, C173, C246, C247, C248, C257, C258, C259, C260, C261).** Class **A or P** via §3 Thm E + §7 N9 + §6 item 2; M-23, M-24, M-36 sharpen. C173 (Costello-Li failure / refutation tone) is **S** in the plan body since it advises moving to appendix without specifying.

**Cross-volume / outlook items (C111, C123, C124, C137, C176, C284).** Class **A** via §9.

**Specific punch items not addressed by plan (silent drops, S):**

| # | Title | Why dropped / suggested reincorp |
|---|-------|-----------------------------------|
| C15, C68, C167 | Figures upgrade or removal — explicit graph notation requirements | **S**. Plan does not call for figure surgery. **Reincorp:** add §6 item 13 "Figure discipline: every diagram must show $\Gamma$, $\mathrm{Aut}\,\Gamma$, $P_\partial$, boundary order, kernel orientation, coefficient — or be labeled schematic-only." |
| C38 | Jet-contraction Euler argument $[d_R,\iota_{\partial_t}]=\partial_t$ derivation | **S**. Plan invokes locally-constant factorization but not the explicit jet-contraction reduction. **Reincorp:** add proof step to Theorem A's action items. |
| C133, C219, C220 | Notation collision: $N$ for matrix size vs $\mathfrak m^{N+1}$ truncation | **S**. Plan does not warn. **Reincorp:** add to §6 item 12 notation index a "rank vs truncation" disambiguation row. |
| C145 | BF pairing degree justification ($|\alpha|+|\beta|$ for top form $p+q=4$) | **S**. Plan signs convention appendix is silent on BF pairing degrees per se. **Reincorp:** add to §6 item 8 sign appendix. |
| C147 | Finite-$N$ commuting variety not complete intersection | **A** via M-03 in master ledger; **but plan does NOT mention this** in §2-§7. Plan's finite-algebraic-model is silent on derived intersection re-narration. **Critical reincorp:** add §3 Theorem A action item invoking M-03's BV-computes-derived-intersection narrative. |
| C171 (basis-dependence language) | Basis-independent structure of CE/PV map | **P**. Plan's coord-free Lichnerowicz proof addresses this; not made explicit. **Reincorp:** §7 N1 should call out coordinate-free covariance separately. |
| C207 | "Apologetic phrasing" replaced with theorem-driven language | **A** via §5 voice (line 599-602); but specific phrases ("not a theorem", "only a shadow") not flagged. **Reincorp:** §5 voice should add explicit phrase blacklist. |
| C227 | Index conventions for monomials (negative-index targets zero) | **P**. Plan's sign appendix (item 8) is silent on negative-index conventions. **Reincorp:** add to §6 item 8 sign appendix. |
| C239, C240, C241 | $\Theta_\rho$ pairing/parity precision; "defect current" notation $\Theta_\rho(B)$ | **P**. Plan installs $\Theta_\rho$ but parity/pairing rules not made explicit. **Reincorp:** add to §6 item 12 notation index or §7 N9. |
| C243 | Toy proof at finite Lie $\mathfrak l$: $C^\bullet_{\mathrm{CE}}(\mathfrak l\ltimes\mathfrak l^\vee[1])\cong\mathrm{PV}(S(\mathfrak l))$ | **P**. Plan's §7 N1 mentions this toy warm-up but does not number it as a theorem; only "includes the toy finite-dimensional warm-up". **Reincorp:** elevate to a numbered Lemma in N1. |
| C273 | Graphwise RG limitation: graphwise-bounded ≠ perturbatively renormalizable | **S**. Plan's Costello checklist (Obligation V, N8) does not flag this distinction explicitly. **Reincorp:** add to §4 Obligation V. |
| C274, C275 | Costello-Li failure analysis location and tone | **P**. Plan moves cross-volume to private appendix; Costello-Li-failure analysis is not addressed by name. **Reincorp:** add §4 Obligation V or Phase 4 outlook clarification. |
| C254 | $\psi$ degree consistency ($-1$ vs $+1$) | **P**. Plan's sign appendix (item 8) covers $V[1]^n$ convention; $\psi$-degree thread not flagged. **Reincorp:** add to §6 item 8 sign appendix. |

**Already-addressed items via M-XX entries (typical mapping):**

| Critique | Plan + Master |
|---|---|
| C09, C41 (one-$\psi$ proof strengthening) | §3 Thm B action items + §7 N2 |
| C61, C232, C233 (PP sign direction) | §6 item 8 + §3 Thm D action |
| C70 ($\Psi\to\rho$ not strict $P_0$) | M-02 + §6 item 6 / Thm D no-go |
| C72 (Rees / $D_\hbar$ interpolation) | M-02 (reformulated) + §4 Obl II + §7 N5 |
| C76 (Schur → local cohomology) | M-06 + §6 item 5 + §3 Thm D action |
| C77, C107, C162 (anomaly line) | M-09 + §3 Thm G action |
| C78, C95 (primitive projection rename / enlarged reduced sector) | M-15 + §6 item 6 / item 7 |
| C107, C162 (full $H^2$ classification) | M-09 |
| C109 (three large-$N$) | M-10 + §7 N10 |
| C112 (regulator independence admissible-only) | M-11 + §4 Obl III |
| C103 (Theorem 0.2.21 split) | M-16 + §6 item 1 + §3 Thm E correction |
| C115 (radial-parts armoring) | §3 Thm F$'$ + §7 N3 |
| C159, C160 (factorization arrows / coalgebra direction) | M-04 + M-24 |
| C204 (Tate Quillen as enhancement) | M-01 (split into C₁/C₂) + §3 Thm C |
| C266, C267, C268 (Matlis dual language) | §3 Thm D + appendix-matlis |
| C277 (Capelli shift trace pair) | M-12 + §3 Thm G |
| C284 (cross-volume out entirely) | §9 + §6 item 10 |
| C286 (highest-priority edits) | §6 + appendix to §10 |

---

## T4. Silent-drop and Dilution Audit

### Silent drops requiring reincorporation (S items)

| Critique | Severity | Reincorporation proposal |
|---|---|---|
| **C15, C68, C167** (Figures discipline) | 2 | **W3-W13-1: §6 item 13 (new) — Figure discipline.** Every diagram must display $\Gamma$, $\|\mathrm{Aut}\,\Gamma\|$, $P_\partial$, boundary order, kernel orientation, coefficient — OR be explicitly labeled "schematic only; not used in proof." |
| **C38** (Euler jet contraction explicit) | 3 | **W3-W13-2: §3 Theorem A action item.** Add "Derive local-operator reduction explicitly from $[d_R,\iota_{\partial_t}]=\partial_t$ Euler-type contraction, showing each local cohomology class has a representative depending only on field values at the insertion point, not derivatives." |
| **C133, C219, C220** (rank-$N$ vs truncation-$N$ notation collision) | 2 | **W3-W13-3: §6 item 12 notation index — add disambiguation row.** Use $N$ for brane rank and $D$ for Taylor truncation; existing $\mathfrak m^{N+1}$ notation in `tate-T2` should be recast as $\mathfrak m^{D+1}$. |
| **C145** (BF pairing degree justification) | 3 | **W3-W13-4: §6 item 8 sign-convention appendix — add subsection.** Compute $\|\alpha\|+\|\beta\|=p+q-3$ for top form $p+q=4$, and reconcile with claimed BV pairing degree $-1$. Ensure no mismatch between $\alpha$-shift ($[1]$) and $\beta$-shift ($[2]$) is silently absorbed. |
| **C147** (Finite-$N$ commuting variety not Koszul; BV computes derived intersection) | 4 | **W3-W13-5: PROMOTE M-03 to §3 Theorem A preface AND §3 Theorem G re-narration.** Master ledger M-03 already names this; plan does not propagate. Add Theorem-A action item: "for $N\ge 2$ the commuting variety is not a complete intersection (Premet 2003; Vasconcelos 1994); the open BV complex computes the derived intersection, $Tr\,\psi$ is a chain-level avatar of the derived intersection class." Add Theorem-G action item: "the $\hbar N$ Capelli shift is the U(1)$_{\mathrm{ghost}}$ one-loop anomaly of the derived intersection." |
| **C273** (graphwise-bounded ≠ renormalizable) | 4 | **W3-W13-6: §4 Obligation V — clarification.** Add: "graphwise-boundedness is not perturbative renormalizability by itself. The full effective interaction is a formal sum over graphs and loop order; locality and QME are separate from graphwise control. The weighted Tate argument controls each fixed graph; convergence over graphs is open." |
| **C274, C275** (Costello-Li failure analysis tone and location) | 3 | **W3-W13-7: §4 Obligation V — Costello-Li addendum.** Add: "Costello-Li's theorem is not applicable to this local mixed defect model without additional work — the model is noncompact, mixed topological-holomorphic, brane-defect at codimension 5, uses ordinary $\mathfrak{gl}_N$ (not $\mathfrak{gl}(N\|N)$), and has the coefficient Tate direction. Each non-applicability is a separate reduction step." |

### Dilution items where critique severity > plan response priority (P items)

| Critique | Severity | Plan response | Sharpening proposal |
|---|---|---|---|
| **C08** (Quotient stack vs invariant reduction) | 3 | §3 Theorem A statement is silent on the distinction algebraic-invariants-vs-CE/BRST | **W3-W13-8: §3 Theorem A action item.** Add explicit statement: "We compute invariant functions on the derived moment-map zero locus, not the full BRST cohomology of infinitesimal gauge algebra. The group $\mathrm{GL}_N$ is linearly reductive in characteristic zero, hence invariants are exact." |
| **C35** (Divergence-free $\Rightarrow$ Hamiltonian via Poincaré lemma) | 3 | §2 Principle 1 asserts but does not derive | **W3-W13-9: §2 Principle 1 expansion.** Add explicit derivation: $\partial_\Omega X=0\Leftrightarrow d(\iota_X\omega)=0$; on formal disk Poincaré lemma kills closed 1-forms ⇒ $\iota_X\omega=-df\Rightarrow X=X_f$. Justifies $\bar A=\mathbb C[z_1,z_2]/\mathbb C$. |
| **C36** (Open brane sector first-principles A-brane $\otimes$ B-brane $\otimes$ Koszul resolution) | 3 | §3 Theorem A asserts BV reduction but does not derive Ext-algebra origin | **W3-W13-10: §3 Theorem A proof skeleton expansion.** Add: "Open string states $= \Omega^\bullet(\mathbb R)\otimes\mathrm{Ext}^\bullet_{\mathbb C[z_1,z_2]}(\mathcal O_0,\mathcal O_0)\otimes\mathfrak{gl}_N[1]$; via Koszul resolution $\mathrm{Ext}^\bullet_R(k,k)\simeq\Lambda(\epsilon_1,\epsilon_2)$, the ghost-zero open field is $A+\phi_1\epsilon_1+\phi_2\epsilon_2$, recovering the first-order action." |
| **C171** (Basis-independence of CE/PV) | 3 | §7 N1 mentions Lichnerowicz coordinate-free proof; does not separately call out covariance under formal symplectomorphism | **W3-W13-11: §7 N1 expansion.** Add explicit covariance statement and link to M-05 (Symp$(\mathbb C^2,0)$ functoriality). The CE/PV map is canonical on the linear Poisson space $\mathfrak h^\vee$; the formula is basis-dependent but the map is not. |
| **C207** (Apologetic phrasing blacklist) | 2 | §5 voice (lines 599-602) generic | **W3-W13-12: §5 voice — explicit blacklist.** Add: avoid "not a theorem", "only a shadow", "not yet"; replace by "the theorem is the reduced formal local theorem", "the analytic graph realization is a separate problem", "the PBW descendant sector is a special-fibre theorem." |
| **C227** (Negative-index targets zero rule) | 2 | §6 item 8 sign appendix is silent | **W3-W13-13: §6 item 8 sign appendix expansion.** State: "if $a-p+1<0$ or $b-q+1<0$, the target $\rho_{a-p+1,b-q+1}$ is absent and the action is zero. This is the convention behind the $a+b>0$ exclusion in $\mathcal P$." |
| **C239–C241** ($\Theta_\rho$ pairing/parity precision) | 3 | §3 Thm D installs $\Theta_\rho$ but parity/pairing/density-vs-distribution rules elided | **W3-W13-14: §6 item 12 notation index expansion.** Add: $\|\Theta_\rho\|=$ explicit shift; $\Theta_\rho(B)$ for $B\in\mathcal D'_c(I)$; pairing with $\Omega^\bullet_c(I)$. |
| **C243** (Finite Lie toy proof numbered) | 4 | §7 N1 mentions; not numbered | **W3-W13-15: §7 N1 — promote toy.** Make the finite-dimensional warm-up a numbered Lemma: "For finite Lie $\mathfrak l$, $C^\bullet_{\mathrm{CE}}(\mathfrak l\ltimes\mathfrak l^\vee[1])\cong\mathrm{PV}(S(\mathfrak l))$; the map $u_i\mapsto O_i, c^i\mapsto\theta^i$ becomes the main theorem by completion." |
| **C254** ($\psi$ degree consistency) | 3 | §6 item 8 covers $V[1]^n$; $\psi$-degree thread not flagged | **W3-W13-16: §6 item 8 sign appendix expansion.** Add subsection: $Q\psi=[\phi_1,\phi_2]$ ⇒ $\|Q\|=1$ ⇒ $\|\psi\|=-1$ in cohomological / $+1$ in chain convention; state once. |
| **C92** (Local-cohomology proof for principal-part uniqueness — already addressed by M-06 but mid-tier dilution) | 4 | §3 Thm D action items + §6 item 5 + M-06 (rename + split) | OK — convergent. |

### Items where master ledger has entries but plan does not propagate

These are cases where M-XX exists in `attack-heal-platonic-2026-04-28.md` but the plan does not (yet) reflect the heal.

| Master ID | Plan status | Action |
|---|---|---|
| **M-01** (Theorem C split into C₁ / C₂) | Plan does NOT split Theorem C; plan §3 Theorem C is still monolithic | **W3-W13-17: §3 Theorem C update.** Split into C₁ (generator-level identity, hypothesis-free) and C₂ (bar-cobar / PBW consequence on admissible Tate-conilpotent windows). Plan must absorb M-01's structural reformulation. |
| **M-02** (Obligation II structural impossibility) | Plan §4 Obligation II says "must change category — Rees / holonomic $D_\hbar$-modules"; M-02 sharpens to "no $\mathfrak h$-equivariant solution; categorical reformulation open" | **W3-W13-18: §4 Obligation II reformulation.** Reword: "The maximal honest comparison is the Fourier-Rees bridge of `\thm:app-matlis-rees-fourier-bridge` (graded-vector-space identification only on the labelled basis; no $\mathfrak h$-equivariance). No $\mathfrak h$-equivariant Rees-flat $D_\hbar$-module candidate realizes both fibres simultaneously (verified against 21-case sweep). The open question is whether any category-changing construction (derived $D_\hbar$-modules, perverse sheaves at the conormal, factorization $D_\hbar$-bimodules) can carry both fibres equivariantly." |
| **M-03** (Derived intersection re-narration) | Plan does NOT mention finite-$N$ commuting variety not being Koszul | **W3-W13-5** above |
| **M-07** (Shift inconsistency $[-1]$ vs $[+1]$) | Plan §6 item 8 calls for sign appendix but does not specifically resolve shift inconsistency | **W3-W13-19: §6 item 8 sign appendix.** Add: "Pick the manuscript's standard $[1]$ convention; align all references to $[1]$. Resolve `main.tex`:2206 vs 3449 contradiction." |
| **M-09** (Weight-bidegree decomposition lemma) | Plan §3 Thm G action items mention but do not prove the weight-bidegree decomposition | **W3-W13-20: §3 Theorem G action item.** Add: "Author $\mathrm{lem:weight-bidegree-anomaly}$ in Theorem G area: $H^2_{\mathrm{Lie}}(\bar A;\mathbb C)$ is bigraded by weight $(p,q)$; weight-$(0,0)$ component is one-dimensional, spanned by $\bar\omega$." |
| **M-11** ($q\to 1^+$ forbidden, admissible-only) | Plan §4 Obligation III says "stabilises as $q\to 1^+$" — DIRECTLY VIOLATED | **W3-W13-21: §4 Obligation III rewording.** "For any two admissible weights $q,q'>1$, the weighted constructions give canonically equivalent finite-degree local observables. Stabilisation as $q\to 1^+$ is NOT asserted: forbidden by `\thm:strict-unweighted-no-go`. Admissible-window finite-degree observable computation is what stabilises, not the strict-weight limit." |
| **M-13** (bosonic vs $\mathfrak{gl}(N\|N)$ supertrace) | Plan does not mention | **W3-W13-22: §3 Theorem A or §1 thesis statement.** Add one-sentence remark: "The brane stack is the bosonic $\mathfrak{gl}_N$ Dirac probe; a $\mathfrak{gl}(N\|N)$ supertrace alternative would be a different super-stacked model with anti-branes, and is not studied here." |
| **M-14** (Weiss-cosheaf descent) | Plan §4 Obligation VII (global descent) covers in spirit; not explicit | **W3-W13-23: §4 Obligation VII expansion.** Make Weiss-cosheaf descent on $\mathbb R^2\times\mathbb C^2$ explicit residual (currently buried in "global descent"); preserve as named open obligation per M-14. |
| **M-32** (U(1)$_{\mathrm{ghost}}$ regularization-compatible) | Plan §3 Thm G or §4 Obligation IV does not engage with M-32's distinction "regularization-compatible vs anomaly-canceling" | **W3-W13-24: §4 Obligation IV expansion.** Add the M-32 distinction: "The mechanism (a) closed exchange-graph contributions, (b) supertrace, (c) central-character / normal-ordering counterterm — is a regularization-compatible question. Do not conflate regularization-compatibility with anomaly cancellation." |
| **M-35** (Symp$_{\mathrm{form}}$-equivariance per-theorem, not (∞,1)-uniform) | Plan does not engage with this distinction | **W3-W13-25: §6 voice or §7 N1 expansion.** Add: "Symp$_{\mathrm{form}}(\mathbb C^2,0)$-equivariance is verified per-theorem; we do not claim (∞,1)-uniform Symp-equivariance across all theorem blocks." |
| **M-36** (Distribution-product avoidance structural, not by fiat) | Plan §6 item 7 + §7 N9 install distribution-locality but with "by fiat" wording per M-23 | **W3-W13-26: §7 N9 expansion.** Make the avoidance structural (i.e., proven from coadjoint Jacobi + smearing $a(bB)-b(aB)=abB$ for smooth $a,b$ and distribution $B$), not declared by fiat. |
| **M-37** (Sharpened R-03 four-ingredient closure plan) | Plan §4 Obligation VII is high-level | **W3-W13-27: §4 Obligation VII expansion.** Adopt M-37's four ingredients: (1) Weiss descent for the brane-line factorization construction; (2) global Hamiltonian sheaf $\mathcal H$ with period choice; (3) holomorphic-symplectic anomaly bookkeeping; (4) global U(1)/Capelli class transfer. |

---

## T5. Recommendations — M-XX entries to add or sharpen

The following 27 W3-W13-prefixed entries should be added to the master ledger. Numbering is contiguous in the W3-W13 namespace; severities mirror the underlying critique.

| ID | Title | Severity | Origin |
|---|---|---|---|
| W3-W13-1 | Figure discipline (every diagram labels $\Gamma,\mathrm{Aut}\Gamma,P_\partial$, boundary order, kernel orientation, coefficient — or explicit "schematic only") | 2 | C15, C68, C167 |
| W3-W13-2 | Euler jet-contraction $[d_R,\iota_{\partial_t}]=\partial_t$ as Theorem A action item | 3 | C38 |
| W3-W13-3 | Rank-$N$ vs truncation-$D$ notation disambiguation | 2 | C133, C219, C220 |
| W3-W13-4 | BF pairing-degree appendix subsection ($|\alpha|+|\beta|$ accounting) | 3 | C145 |
| W3-W13-5 | PROMOTE M-03 (BV computes derived intersection) into §3 Theorem A preface and §3 Theorem G re-narration; plan currently silent | 4 | C147, M-03 |
| W3-W13-6 | Graphwise-bounded ≠ perturbatively renormalizable disclaimer in §4 Obligation V | 4 | C273 |
| W3-W13-7 | Costello-Li addendum in §4 Obligation V (explicit non-applicability reduction list) | 3 | C274, C275 |
| W3-W13-8 | Quotient-stack vs invariant-reduction explicit statement in §3 Theorem A | 3 | C08 |
| W3-W13-9 | Divergence-free ⇒ Hamiltonian Poincaré-lemma derivation in §2 Principle 1 | 3 | C35 |
| W3-W13-10 | A-brane $\otimes$ B-brane $\otimes$ Koszul-resolution origin of open BV in §3 Theorem A | 3 | C36 |
| W3-W13-11 | Symplectomorphism-covariance call-out in §7 N1 | 3 | C171 |
| W3-W13-12 | Apologetic-phrasing blacklist in §5 voice | 2 | C207 |
| W3-W13-13 | Negative-index zero-target convention in §6 item 8 | 2 | C227 |
| W3-W13-14 | $\Theta_\rho$ parity/pairing/density precision in §6 item 12 | 3 | C239–C241 |
| W3-W13-15 | Numbered finite-Lie toy lemma in §7 N1 | 4 | C243 |
| W3-W13-16 | $\psi$-degree convention statement in §6 item 8 | 3 | C254 |
| W3-W13-17 | §3 Theorem C explicit split into C₁ / C₂ matching M-01 | 5 | M-01 |
| W3-W13-18 | §4 Obligation II reformulation matching M-02 | 5 | M-02 |
| W3-W13-19 | §6 item 8 specific shift convention resolution per M-07 | 4 | M-07 |
| W3-W13-20 | §3 Theorem G weight-bidegree decomposition lemma per M-09 | 2 | M-09 |
| W3-W13-21 | §4 Obligation III re-wording (admissible-only, no $q\to 1^+$) per M-11 | 3 | M-11 |
| W3-W13-22 | Bosonic vs $\mathfrak{gl}(N\|N)$ supertrace remark in §3 Theorem A or §1 per M-13 | 1 | M-13 |
| W3-W13-23 | §4 Obligation VII Weiss-cosheaf-descent residual explicit per M-14 | 3 | M-14 |
| W3-W13-24 | §4 Obligation IV regularization-compatible vs anomaly-cancellation distinction per M-32 | 4 | M-32 |
| W3-W13-25 | Symp$_{\mathrm{form}}$ equivariance per-theorem, not (∞,1)-uniform per M-35 | 2 | M-35 |
| W3-W13-26 | §7 N9 distribution-product-avoidance made structural (Jacobi+smearing proof) per M-36 | 3 | M-36 |
| W3-W13-27 | §4 Obligation VII four-ingredient closure plan per M-37 | 3 | M-37 |

**Critical drops (severity ≥4 not addressed by plan).** Five drops require highest-priority sharpening: **W3-W13-5** (M-03 derived intersection), **W3-W13-6** (graphwise vs renormalizable), **W3-W13-15** (toy-lemma), **W3-W13-17** (Theorem C split per M-01), **W3-W13-18** (Obligation II per M-02), **W3-W13-24** (M-32). The Theorem C split (W3-W13-17) is the load-bearing one — without it the plan's central theorem statement holds an implicit hypothesis (Tate-conilpotency) that fails for the perfect formal disk, exactly as M-01 diagnoses.

**Plan sections requiring direct edits:** §2 (Principle 1 derivation, Symp covariance), §3 (Theorem A finite-$N$ commuting variety remark + jet contraction; Theorem C split into C₁/C₂; Theorem G weight-bidegree lemma), §4 (Obligations II, III, IV, V, VII reformulation), §5 (voice phrase blacklist), §6 (notation index disambiguations + sign appendix expansions), §7 (N1 numbered toy lemma + Symp covariance call-out + N9 structural distribution-product avoidance).

---

## Summary (200 words)

This audit catalogs 287 distinct critique items (C01-C287) extracted in chunks from the 11366-line whitepaper-critical-analysis transcript covering six rounds: hostile-referee attack (C01-C17), constructive derived-center proposal (C18-C24), Diracian rewrite (C25-C33), first-principles synthesis (C34-C68), v3 second-pass (C69-C86), and exhaustive 201-item technical punch list (C87-C287). Cross-mapped against the 979-line `platonic-ideal-plan-2026-04-28.md` and the 37-entry master ledger `attack-heal-platonic-2026-04-28.md`, most items are classified A (addressed). Substantively, the platonic plan is faithful to the critique on the central theorem (CE/PV derived center, principal-part Matlis dual, no-go for $\Psi\to\rho$ as $\mathfrak h$-module, scalar U(1)/Capelli line, Costello as conditional analytic obligation, regulator status of weighted Tate). The audit identifies 13 silent drops or dilutions (S/P) and 11 master-ledger heals (M-01, M-02, M-03, M-07, M-09, M-11, M-13, M-14, M-32, M-35, M-36, M-37) that the plan does not yet propagate. The recommended 27 W3-W13- entries cover all gaps. Five (W3-W13-5/-6/-15/-17/-18/-24) are severity 4-5 and should be added first; the load-bearing one is W3-W13-17 (Theorem C explicit C₁/C₂ split per M-01).

**File location:** `/Users/raeez/topological-strings/reconstitution/wave3-W13-critique-fidelity-2026-04-28.md`

