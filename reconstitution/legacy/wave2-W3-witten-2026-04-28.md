# Wave 2 / W3 — Witten + Boundary lens (Raeez Lorgat)

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Lens.** Witten (physical consistency, dualities, anomalies, examples
that reveal the theorem) + Boundary (zero / infinity / empty / singular
strata).
**Mandate.** Verify or refute wave-1 master claim **M-03**
(*Finite-N commuting variety is not a complete intersection; BV computes
the derived intersection*) by explicit low-N computation; sharpen the
U(1)$_{\mathrm{ghost}}$ heal at M-15 / E2; identify the chain-level
$\mathrm{Tr}\,\psi$ class with the closed $[\bar c]$ anomaly line of
Theorem G; reconfirm the N=1 boundary stratum.

---

## §0. Summary

W3 confirms M-03 by explicit linear-algebra computation at $N=2$,
together with the literature codimension/irreducibility results
(Gerstenhaber 1961, Motzkin–Taussky 1955, Premet 2003, Vasconcelos 1994).
The durable artefacts are this report and
`/Users/raeez/topological-strings/scripts/check_derived_intersection_N2.py`,
which implements 8-variable polynomial arithmetic and verifies all
chain-level claims.

W3 inscribes four ledger entries:

* **W3-01** (severity 4, additive heal): commuting-variety dimensions
  match Gerstenhaber's $\dim C_N = N^2 + N$ at $N \in \{1,2,3,4\}$.
  Koszul generator count $\#\psi = N^2$ exceeds codim $N(N-1)$ for
  every $N \ge 2$; the gap is the homological cause of nonzero higher
  Tor classes M-03 invokes. None of Premet, Vasconcelos, Gerstenhaber,
  Motzkin–Taussky currently cited in `main.tex` (verified by grep).

* **W3-02** (severity 3, sharpening): U(1)$_{\mathrm{ghost}}$ in 1d
  $\mathfrak{gl}_N$ matrix mechanics is **regularization-compatible,
  not anomaly-canceling**. The actual anomaly is the Capelli $\hbar N$
  class of Theorem G. Wave 1's heal phrasing should be tightened;
  references: Costello, *RenEFT* (AMS Math.\ Surveys 170, 2011) §5.3;
  Henneaux–Teitelboim, *QGS* (Princeton 1992) §18.3.

* **W3-03** (severity 3, identification): $[\mathrm{Tr}\,\psi]_{\mathrm{BV}}
  = [\bar c]_{\mathrm{CE}}$ under the CE/PV map of Theorem C, mediated
  by the constant-Hamiltonian generator removal. Bridge proof is the
  unproved Obligation I content; chain-level closedness is verified.

* **W3-04** (severity 1, boundary): N=1 collapse confirmed. At N=1,
  $[\phi_1,\phi_2]=0$ identically; BV differential is zero;
  $\mathrm{Tr}\,\psi = \psi$ is trivially Q-closed; derived = underived
  intersection at this abelian stratum.

---

## §1. W3 ledger entries

### W3-01 — N=2 derived-intersection narrative confirmed by direct computation
**Severity 4 (additive). Status valid. Confidence high.**
**Lens.** Witten + Boundary.
**Provenance.** Wave-1 M-03; this wave's explicit N=2 linear algebra and
dimension count.
**Target.** `main.tex`:127 (Dirac reduction elision); `principles.tex`
Principle 1 (line 53); `theorem-lanes.tex` Lane 1 (lines 12–50);
Theorem A preface.
**Claim under attack.** That the finite-$N$ open BV complex
$\C[\phi_1,\phi_2] \otimes \Lambda(\psi)$, $Q\psi = [\phi_1,\phi_2]$,
realizes the *honest* (non-derived) coordinate ring
$\C[\phi_1,\phi_2]^{\mathrm{commuting}}$ as $H^0(Q)$.
**Computation.** At $N=2$, the four entries of $[\phi_1,\phi_2]$ in
$R_2 = \C[\mathfrak{gl}_2 \oplus \mathfrak{gl}_2]$ are nonzero with
their trace zero (cyclicity), giving 3 independent moment-map equations
in $\mathfrak{sl}_2$ against codim 2. The Koszul complex on
$\Lambda(\psi^{ij})$ has 4 odd generators. The verified table:

| $N$ | $\dim \mathfrak{gl}_N^{\oplus 2}$ | $\dim C_N$ | codim | $\#\psi$ | $\#\mu$ ($\mathfrak{sl}_N$) |
|-----|-----------------------------------|-----------|-------|----------|------------------------------|
| 1   | 2                                 | 2         | 0     | 1        | 0                            |
| 2   | 8                                 | 6         | 2     | 4        | 3                            |
| 3   | 18                                | 12        | 6     | 9        | 8                            |
| 4   | 32                                | 20        | 12    | 16       | 15                           |

For $N \ge 2$, $\#\psi = N^2 > $ codim $= N(N-1)$. The Koszul complex
on the full $N^2$ moment-map components has more generators than the
codim, hence at least $N$ excess generators that cannot fit a regular
sequence. The first such excess is $\mathrm{Tr}\,\psi$, Q-closed by
$Q\,\mathrm{Tr}\,\psi = \mathrm{Tr}\,[\phi_1,\phi_2] = 0$ identically.
**Evidence type.** counterexample (literature: Premet 2003,
Vasconcelos 1994, Gerstenhaber 1961, Motzkin–Taussky 1955);
verification (W3 explicit script).
**Files read.** `main.tex` 100–300, 1500–1610, 2855–2935;
`principles.tex` all; `theorem-lanes.tex` Lane 1.
**Confidence.** High.
**Blast radius.** *Additive*: re-explains Theorems A, B, G, does not
falsify them. The honest narration is that BV cohomology in the
unreduced ring is the *derived* commuting-pair intersection, with
$\mathrm{Tr}\,\psi$ and higher Tor representatives recording the
non-complete-intersection structure.
**Minimal heal.** Phase 1: insert technical remark in `principles.tex`
Principle 1 and `main.tex` Theorem A area, noting that for $N \ge 2$
the commuting variety is not a complete intersection (Premet 2003;
Vasconcelos 1994; Gerstenhaber 1961; Motzkin–Taussky 1955). Add the
four citations to the bibliography. Announce $\mathrm{Tr}\,\psi$ as the
chain-level avatar. The exclusion stated at `main.tex`:1003 and 2904
is *preserved*: the constant-Hamiltonian removal corresponds, under
CE/PV, to the chain-level avatar exclusion.
**Residual.** Full Macaulay2 minimal-free-resolution computation of
$\mathrm{Tor}^{\bullet}_{R_N}(\mathcal O_{C_N}, \C)$ at $N=2,3$ not
performed; lower bound $\dim \mathrm{Tor}^1 \ge 1$ established via
$\mathrm{Tr}\,\psi$. Premet 2003 Theorem 1.2 and Vasconcelos 1994 §9
are pointers, not full Tor computations.
**Deciding evidence.** A Macaulay2 minimal-free-resolution would close
the residual; out of scope for the swarm.

### W3-02 — U(1)$_{\mathrm{ghost}}$: regularization-compatible, not anomaly-canceling
**Severity 3 (sharpening). Status valid. Confidence high.**
**Lens.** Witten + Boundary.
**Provenance.** Wave-1 M-03 / E2 heal claim; this wave's interpretation of
Costello *RenEFT* §5.3 and Henneaux–Teitelboim §18.3.
**Target.** Wave-1 master ledger M-03 / M-15 narrative;
`appendix-unreduced-bv-qme.tex`.
**Claim under attack.** Wave-1 phrasing: "quantum extension of
ghost-zero truncation requires U(1)$_{\mathrm{ghost}}$ anomaly-freeness".
**Broken step.** This conflates two distinct statements:

(a) The heat-kernel BV regularization in 1d (Costello *RenEFT* §5.3)
preserves the U(1)$_{\mathrm{ghost}}$ grading on the BV complex —
automatic in 1d topological theories because the heat kernel propagates
each field type to itself and ghost number is integer-valued. *Not an
anomaly-freeness theorem*; a compatibility statement.

(b) The actual quantum anomaly of the BV master equation in this
$\mathfrak{gl}_N$ Dirac-probe model is the Capelli $\hbar N$ class —
the same line as the classical $[\bar c] \in H^2_{\mathrm{Lie}}(\bar A; \C)$
of Theorem G. In Henneaux–Teitelboim §18.3 vocabulary the ghost
anomaly equals the trace anomaly of the gauge generators, which here
is $\mathrm{Tr}_{\mathfrak{gl}_N}(I) = N$. *One* anomaly classified by
Theorem G, *not* a separate U(1)$_{\mathrm{ghost}}$ obstruction.

**Evidence type.** missing_source (no Henneaux–Teitelboim citation in
manuscript); proof_gap (Costello *RenEFT* §5.3 sets up the scheme but
does not prove finite-dim $\mathfrak{gl}_N$ ghost-anomaly cancellation —
which is part of Obligation IV).
**Files read.** `main.tex` ghost-number passages (130, 1450–1470,
1542–1574); ledger M-03 narration (263–289).
**Confidence.** High.
**Blast radius.** Without sharpening, the manuscript would
double-count the anomaly: once as "U(1)$_{\mathrm{ghost}}$ obstruction"
and again as "Capelli $\hbar N$". W3 confirms both are the same line.
**Minimal heal.** Replace "U(1)$_{\mathrm{ghost}}$ anomaly-freeness"
by "U(1)$_{\mathrm{ghost}}$ preserved by the regularization (free
statement); the only nontrivial anomaly is the Capelli $\hbar N$ class
of Theorem G". Add Henneaux–Teitelboim §18.3 and Costello *RenEFT* §5.3
citations.
**Residual.** Full one-loop QME cancellation argument is Obligation IV.
**Deciding evidence.** A complete one-loop QME calculation in
`appendix-unreduced-bv-qme.tex` closes Obligation IV.

### W3-03 — Identification of $[\mathrm{Tr}\,\psi]_{\mathrm{BV}}$ with $[\bar c]_{\mathrm{CE}}$ under CE/PV
**Severity 3 (identification). Status valid. Confidence medium-high.**
**Lens.** Witten (open-closed correspondence) + Boundary
(constant-Hamiltonian stratum).
**Provenance.** Wave-1 M-03; Theorem G; Theorem C (CE/PV); this wave's
explicit construction.
**Target.** `main.tex` Theorem G area (247–393); `principles.tex`
Principle 1; constant-Hamiltonian removal at `main.tex`:1003, 2904.
**Claim.** The chain-level $\mathrm{Tr}\,\psi$ (BV side, cohomological
degree $-1$) and the CE-level $[\bar c]$ cocycle (closed side,
$H^2_{\mathrm{Lie}}(\bar A; \C)$) are the same distinguished anomaly
line, viewed from the two sides of CE/PV.
**Construction of the comparison map.**

1. **Closed side.** $\bar c \in Z^2_{\mathrm{Lie}}(\bar A; \C)$ is
   $\omega(z_1^k z_2^l, z_1^m z_2^n) = (kn-lm)\mathbf 1_{(k+m,l+n)=(1,1)}$.
   Generates the distinguished line of $H^2_{\mathrm{Lie}}(\bar A;\C)$
   corresponding to the abelian extension
   $0 \to \C\cdot 1 \to \mathfrak h_{\mathrm{poly}} \to \bar A \to 0$.

2. **Open side.** $\mathrm{Tr}\,\psi$ at finite $N$ is a Q-closed cycle
   in $H^{-1}(\C[\phi_1,\phi_2] \otimes \Lambda(\psi), Q)$ because
   $Q\,\mathrm{Tr}\,\psi = \mathrm{Tr}\,[\phi_1,\phi_2] = 0$ identically.
   Chain-level avatar of the derived intersection (M-03).

3. **Bridge via CE/PV.** Under Theorem C ($c^I \mapsto \theta^I$,
   $u_I \mapsto O_I$), the constant Hamiltonian generator
   $1 \in \mathfrak h_{\mathrm{poly}}$ — the line removed in $\bar A$ —
   corresponds on the open side to $\mathrm{Tr}_N(1) = N$, the empty
   trace removed in the connected stable limit. The cotangent CE
   coordinate $u_1$ dual to this constant generator is realized on the
   open BV side as $\mathrm{Tr}\,\psi$: the boundary value at $(k,l)=(0,0)$
   of the descendant family $\Psi_{k,l}$ — excluded from the Hamiltonian
   comparison precisely because the constant Hamiltonian was removed.

4. **Same line.** The closed obstruction $[\bar c]$ measures the
   failure of the lift $\bar A \to \mathfrak h_{\mathrm{poly}}$ along
   the constant-Hamiltonian line; the open obstruction
   $[\mathrm{Tr}\,\psi]$ measures the failure of the BV Koszul complex
   to be a (classical) free resolution along the same direction. Both
   are obstructions to the *same* lift, viewed from either side of CE/PV.

**Evidence type.** verification (chain-level closedness verified at N=2);
proof_gap (full bridge map is Obligation I content).
**Files read.** `main.tex` 247–393, 996–1010, 2858–2906; `principles.tex`
all.
**Confidence.** Medium-high. The chain-level identification is direct;
the full bridge proof requires Obligation I (Phase 4). The
weight-bidegree decomposition lemma `lem:weight-bidegree-anomaly`
proposed at master P-06 (M-09) gives independent confirmation: the
closed cocycle is concentrated in bidegree $(0,0)$, exactly compatible
with the open-side constant-Hamiltonian removal.
**Blast radius.** This is the *unifying* consequence of M-03:
Theorems A, B, C, G all say the same thing about the same one-dimensional
anomaly line. The narration becomes: *the U(1)/Capelli class is the
unique anomaly of the derived intersection of the moment-map zero
locus, classically the $[\bar c]$-extension obstruction,
quantum-mechanically the $\hbar N$ Capelli shift, chain-level on the BV
side the $[\mathrm{Tr}\,\psi]$ avatar.*
**Minimal heal.** Phase 2: numbered remark in Theorem G area citing M-03
chain-level avatar status; parallel remark in `principles.tex`
Principle 1.
**Residual.** Obligation I (unreduced BV factorization-centre lift) is
the bridge; without it the identification is line-level not
quasi-isomorphism-level.
**Deciding evidence.** A construction realizing the bridge map at
factorization-centre level closes Obligation I and the identification
becomes a numbered theorem.

### W3-04 — N=1 boundary stratum collapse confirmed
**Severity 1. Status valid. Confidence high.**
**Lens.** Boundary (E1: abelian limit).
**Provenance.** Mandate item 5; standard $\mathfrak{gl}_1 = \C$ fact.
**Computation.** At $N=1$, $\phi_1, \phi_2 \in \C$ commute trivially:
$[\phi_1,\phi_2] = 0$ identically. $Q\psi = 0$, BV complex
$\C[\phi_1,\phi_2] \otimes \Lambda(\psi)$ has zero differential.
Moment-map zero locus is all of $\C^2$; $C_1 = \C^2$ *is* a complete
intersection trivially. $\mathrm{Tr}\,\psi = \psi$ is trivially Q-closed.
$\dim C_1 = 1^2 + 1 = 2$, codim $0$, $\#\psi = 1$, $\#\mu = 0$.
**Confidence.** High.
**Blast radius.** Confirms the derived-intersection narrative
degenerates correctly to the abelian limit. The non-complete-intersection
obstruction is a non-abelian phenomenon switching on at $N \ge 2$ when
$\mathfrak{sl}_N \ne 0$.
**Minimal heal.** Optional: parenthetical remark in M-03 inscription
that the derived-intersection claim is non-vacuous only for $N \ge 2$.
**Residual.** None.

---

## §2. Verdict on M-03

**Verified.** The wave-1 master claim that the BV Koszul complex
computes the *derived* intersection (not the underived classical ring)
and that $\mathrm{Tr}\,\psi$ is the chain-level avatar of the
derived-intersection class is correct.

**Heal proposals.**

* **H1.** Inscribe in `principles.tex` Principle 1 and `main.tex`
  Theorem A area: "For $N \ge 2$ the commuting variety
  $C_N \subset (\mathfrak{gl}_N)^2$ is not a complete intersection
  (Premet 2003; Vasconcelos 1994; Gerstenhaber 1961;
  Motzkin–Taussky 1955); the Koszul complex computes the *derived*
  intersection of the moment-map zero locus. The class
  $\mathrm{Tr}\,\psi$ is a chain-level avatar of this structure;
  under CE/PV (Theorem~\ref{thm:open-closed-derived-center}) it
  identifies with the closed $[\bar c]$ anomaly line of
  Theorem~\ref{thm:u1-center-anomaly} via the constant-Hamiltonian
  generator removal."
* **H2.** Add Premet 2003, Vasconcelos 1994, Gerstenhaber 1961,
  Motzkin–Taussky 1955 to the bibliography (none currently present).
* **H3.** Numbered remark in Theorem G area (around line 393)
  identifying $[\mathrm{Tr}\,\psi]_{\mathrm{BV}}$ with
  $[\bar c]_{\mathrm{CE}}$ via CE/PV; flag bridge as Obligation I.
* **H4.** Tighten wave-1's M-03 / E2 phrasing in
  `attack-heal-platonic-2026-04-28.md`:
  "U(1)$_{\mathrm{ghost}}$ anomaly-freeness" →
  "U(1)$_{\mathrm{ghost}}$ preserved by the regularization scheme;
  the only nontrivial anomaly is the Capelli $\hbar N$ class of
  Theorem G". Add Henneaux–Teitelboim §18.3 and Costello *RenEFT* §5.3.

**Residuals.**

1. Macaulay2 minimal-free-resolution of
   $\mathrm{Tor}^{\bullet}_{R_N}(\mathcal O_{C_N}, \C)$ at $N=2,3$ not
   performed; lower bound $\dim \mathrm{Tor}^1 \ge 1$ established via
   $\mathrm{Tr}\,\psi$.
2. Obligation I (unreduced BV factorization-centre lift) bridging
   $[\mathrm{Tr}\,\psi]_{\mathrm{BV}}$ chain-level to $[\bar c]_{\mathrm{CE}}$
   complex-level remains Phase 4.
3. Obligation IV (mixed brane-defect QME cancellation) closes the
   U(1)$_{\mathrm{ghost}}$ / Capelli protection at one-loop. W3
   sharpens the residual phrasing; the cancellation difficulty is
   unchanged.

---

## §3. New ledger items proposed for inscription

| ID    | Severity     | Lens               | Action                                                                                                                                |
|-------|--------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| W3-01 | 4 (additive) | Witten + Boundary  | inscribe technical remark in `principles.tex` Principle 1; add Premet/Vasconcelos/Gerstenhaber/Motzkin–Taussky citations                |
| W3-02 | 3 (sharpen)  | Witten + Boundary  | tighten M-03 / E2 phrasing in master ledger; add Costello *RenEFT* §5.3 + Henneaux–Teitelboim §18.3 citations                          |
| W3-03 | 3 (identify) | Witten + Boundary  | numbered remark in Theorem G area identifying $[\mathrm{Tr}\,\psi]_{\mathrm{BV}} \leftrightarrow [\bar c]_{\mathrm{CE}}$ under CE/PV   |
| W3-04 | 1 (boundary) | Boundary           | optional: $N=1$ abelian-limit remark; derived-intersection claim non-vacuous only for $N \ge 2$                                       |

W3-01 strengthens M-03 with explicit computation; W3-02 sharpens the
M-03 "U(1)$_{\mathrm{ghost}}$ protection" heal phrasing; W3-03 is *new*
and links M-03 (derived intersection) with Theorem G (Capelli) as the
same line viewed from open and closed; W3-04 is a sanity check.

---

## §4. Inscriptions

**Durably inscribed.**
* This document
  (`reconstitution/wave2-W3-witten-2026-04-28.md`).
* Verification script
  (`scripts/check_derived_intersection_N2.py`), which implements
  8-variable polynomial arithmetic over $\mathbb Q$, computes $[X,Y]$
  symbolically at $N=2$, verifies the trace identity and Q-closedness
  of $\mathrm{Tr}\,\psi$, and tabulates commuting-variety dimensions
  at $N \in \{1,2,3,4\}$ against Gerstenhaber's formula.

**Not inscribed.** No edits to `main.tex`, `principles.tex`,
`theorem-lanes.tex`, or apparatus files. Proposals are scheduled.

**Recommended next steps.**

1. (Editorial.) Inscribe H1, H3 in `principles.tex` and `main.tex`;
   add four citations to the bibliography.
2. (Editorial.) Inscribe H2 / H4 in master ledger.
3. (Phase 4 research.) Obligation I bridge proof closes W3-03.
4. (Phase 4 research.) Obligation IV one-loop QME cancellation closes
   W3-02 residual.

---

## §5. Provenance

W3 read wave-1 master ledger M-01 through M-21, the platonic-ideal plan
§0–§10, the Dirac-probe sections of `main.tex` (lines 100–300,
1500–1610), the Theorem G area (247–393), the descendant area
(2855–2935), `principles.tex` in full, Lane 1 of `theorem-lanes.tex`,
and `scripts/check_one_psi_homology.py`.

External references consulted:

* Premet, A. "Nilpotent commuting varieties of reductive Lie algebras."
  *Invent. Math.* 154 (2003), 653–683.
* Vasconcelos, W.\ V. *Arithmetic of Blowup Algebras.* LMS Lecture Note
  Series 195 (1994), §9.
* Gerstenhaber, M. "On dominance and varieties of commuting matrices."
  *Ann. Math.* 73 (1961), 324–348.
* Motzkin, T.\ S., and Taussky, O. "Pairs of matrices with property L."
  *Trans. AMS* 80 (1955), 387–401.
* Costello, K. *Renormalization and Effective Field Theory.* AMS
  Math.\ Surveys and Monographs 170 (2011), §5.3.
* Henneaux, M., and Teitelboim, C. *Quantization of Gauge Systems.*
  Princeton University Press (1992), §18.3.

W3 confidence: every chain-level claim is verified by direct
computation (script runs; all assertions pass). Bridge claims
(W3-03 complex-level identification, W3-02 one-loop cancellation) are
conjectural with the same status they hold in the wave-1 ledger. The
dimension table at $N \le 4$ matches Gerstenhaber's formula exactly.

End of W3 ledger.
