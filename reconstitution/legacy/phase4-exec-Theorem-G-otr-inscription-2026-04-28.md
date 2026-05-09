# Phase 4 Execution / P4-Theorem-G-otr — Parallel Theorem G^otr inscription proposal

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Witten primary (physical interpretation of the two-supertrace
channel; open-closed duality witnessed by `otr` distinct from `Str`;
parastatistic boundary conditions on the q(N) probe; q(2) example
revealing the mechanism); Boundary secondary (brane-defect catalog;
the parity-flipped boundary state forced by the queer central element;
orientifold-style projection between the `Str` and `otr` channels).
**Mode.** Phase-4 EXEC. Master ledger schema; ID prefix
`P4-EXEC-G-otr-`. Proposal-only — no manuscript edits, no commits;
the writable surface is this single file.
**Posture.** P4-EXEC-G3-M3 (1108 lines) returned a **non-discharge**
verdict for the queer trace `otr` on q(N): the queer central element
$J=((0,I_N),(-I_N,0))$ has $\mathrm{otr}(J)=N\neq 0$ and anticommutes
in conjugation with the parity operator $P^{\mathfrak q}$, so the W22
chain-level discharge mechanism does not extend. The Phase-5 outcome
in P4-EXEC-G3-M3 §10 named two routes: **Phase-5-Q-A** (signed
parity-equivariance (A5)\textsuperscript{otr}) and **Phase-5-Q-B**
(parallel theorem G\textsuperscript{otr}). This document executes
Phase-5-Q-B as an inscription proposal: a precise, publication-grade
parallel-Theorem-G statement and proof outline ready for future
authorization, accompanied by hypothesis ledger, two-supertrace
independence proof, boundary/brane interpretation, cross-walk to the
manuscript's Theorem G and to G3-M3 / G4-M3 / G5 / G5-M2, the precise
LaTeX block targeted for `claim-strength-ledger.tex` (Phase-5
frontier section), and a three-angle anti-attack scan.

**Inputs (full reads or targeted reads in the indicated ranges).**
* `CLAUDE.md` (full).
* `reconstitution/phase4-exec-G3-M3-queer-trace-2026-04-28.md` (full;
  1108 lines; G3-M3 verdict, Z\_2\^otr Capelli, otr(J)=N derivation,
  Obs-Q-otr-A5 named, Phase-5-Q-A vs Phase-5-Q-B routes).
* `reconstitution/phase4-exec-classical-super-extension-2026-04-28.md`
  §3 lines 550–807 (G3-M2 verdict on q(N) at the ordinary supertrace
  layer; THEOREM P4-G3-M2-Q candidate at line 712).
* `reconstitution/phase4-exec-A5-anomaly-ledger-2026-04-28.md` §0–§1
  L1–L12 (A5 primary-source ledger; L9 Sergeev central element).
* `reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md` §0–§3
  + §6 + §7 (W22-T1, W22-T2; Lemmas L1/L2/L3; hidden-obstruction
  audit).
* `reconstitution/phase4-exec-G4-M3-W3-twist-2026-04-28.md` §0
  (super-W\_3 cross-walk at osp/q-extension; G3↔G4 cross-coupling
  conditions).
* `main.tex` 280–470 (Lemma `lem:omega-cocycle`,
  Theorem `thm:u1-center-anomaly`, Theorem `thm:u1-center-anomaly-open`,
  Theorem `thm:quantum-classical-anomaly`).
* `appendix-unreduced-bv-qme.tex` (full, 179 lines; Definition
  `def:app-unreduced-bv-degrees`, Theorem `thm:app-unreduced-polynomial-centrality-no-go`,
  Proposition `prop:app-scalar-contact-qme-class` representative
  $\hbar N\,\omega\int abc$, Remark `rmk:app-scalar-contact-escape-routes`
  listing supertrace / central-character / unreduced-scalar exits).
* `theorem-lanes.tex` (full; lane `thm:lane-u1-anomaly` lines 420–456).
* `claim-strength-ledger.tex` (full, 143 lines).
* `open-obligations.tex` lines 121–151 (mixed brane-defect QME open
  obligation).

**Standard primary-source references (cited from memory; not new
inscriptions).**
* A. Sergeev, "The centre of the enveloping algebra for the Lie
  superalgebra Q(N)", *Letters Math. Phys.* **7** (1983), 177–179.
  Original `otr` and odd-Casimir definition.
* A. Sergeev, "The tensor algebra of the identity representation as a
  module over Gl(n|m) and Q(n)", *Math. USSR Sbornik* **51** (1985),
  419–427. Schur–Weyl–Sergeev duality on q(N).
* A. Berele, A. Regev, "Hook Young diagrams with applications to
  combinatorics and representations of Lie superalgebras", *Adv. Math.*
  **64** (1987), 118–175.
* I. Penkov, V. Serganova, "Representations of classical Lie
  superalgebras of type I", *Indag. Math.* **3** (1992), 419–466.
* M. Gorelik, "The Kac construction of the centre of $U(\mathfrak g)$
  for Lie superalgebras", *J. Nonlinear Math. Phys.* **11** (2004),
  325–349.
* J. Brundan, A. Kleshchev, "Hecke–Clifford superalgebras, crystals of
  type $A_{2\ell}^{(2)}$ and modular branching rules for
  $\widehat S_n$", *Represent. Theory* **5** (2001), 317–403.
* S.-J. Cheng, W. Wang, *Dualities and representations of Lie
  superalgebras*, Graduate Studies in Mathematics, Vol. 144, AMS,
  2012, Ch. 1 §1.1.4 and Ch. 6.
* M. Bershadsky, S. Cecotti, H. Ooguri, C. Vafa, "Kodaira–Spencer
  theory of gravity and exact results for quantum string amplitudes",
  *Comm. Math. Phys.* **165** (1994), 311–428. §6 records the
  open-closed dual cocycle formalism that Theorem G^otr extends.

---

## §0. Executive verdict

**Final theorem name.** **Theorem G\textsuperscript{otr}** (parallel to
the manuscript's Theorem G; alternate ledger label `Theorem G_q`,
"Queer U(1)-center anomaly on the queer Lie superalgebra
$\mathfrak{q}(N)$").

**Final residue class statement (one line).** On the q(N) Dirac
brane probe with queer-trace boundary evaluation
$\partial_{\mathrm{bb},N}^{\mathrm{otr}}: f \mapsto
\mathrm{otr}\,f(\phi_1,\phi_2)$, the chain-level mixed brane-defect
QME obstruction representative
\[
   \mathrm{Ob}_{\mathrm{sc}}^{\mathrm{otr}}(\gamma_{\mathbf 1}; a,f; b,g)
     = \hbar N\,\omega(f,g)\int_{\R} a(t)b(t)\gamma_{\mathbf 1}(t)\,dt
     \quad\in\mathcal O_{\mathrm{loc}}(\mathcal E_w^{\mathfrak q})_{\bar 1}
\]
has associated graded CE class $\hbar N[\bar c]^{\mathrm{otr}}\in
H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$ (odd-parity sector of the
BV obstruction complex), generated by the queer central element
$J\in\mathfrak q(N)_{\bar 1}$ via $\mathrm{otr}(J)=N$. The class is
**non-trivial** and **independent** of the bosonic class $\hbar N[\bar c]
\in H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}$ of the manuscript's
Theorem G.

**Phase-5 status declaration.** Theorem G\textsuperscript{otr} is
**Phase-5 frontier**, not Phase-4 chain-level closed. The chain-level
discharge mechanism of W22-T1/T2 fails on q(N) at the queer-trace
layer (Phase-4 verdict `Obs-Q-otr-A5`), and the residue class is
recorded as a parallel anomaly without a chain-level discharge. The
inscription proposed here is the **statement** plus its **proof
outline**; the residue class is named, not absorbed.

**Chosen Phase-5 path.** **Phase-5-Q-B** (parallel theorem) is the
honest path. Phase-5-Q-A (signed parity-equivariance
(A5)\textsuperscript{otr}) is formally well-defined but cannot
discharge the residue: the obstruction is the non-vanishing
$\mathrm{otr}(J)=N$, which is a property of the matrix realization
of q(N), not of the regulator class. Phase-5-Q-A would only relabel
the regulator hypothesis; the coupling coefficient $N$ would survive.
Phase-5-Q-B accepts the obstruction and reframes it as a new physical
observable, distinct from the bosonic Theorem G. This matches the
ecosystem's "report, do not silently reconcile" rule
(`CLAUDE.md`).

**Inscription target.** A new entry in `claim-strength-ledger.tex` in
the Phase-5 frontier section (to be created at the bottom of the
ledger), with claim-strength label *Phase-5 frontier candidate* — a
new status vocabulary item whose introduction is part of the
inscription proposal. The current ledger vocabulary is closed at
*proved in finite algebraic model* / *proved degreewise stable* /
*proved in weighted Tate coefficient model* / *computed to stated
order* / *conditional on named QME/radial-parts/unweighted-regulator
theorem* / *conjectural* / *open* / *not asserted*; we propose to
extend it with **Phase-5 frontier candidate (parallel-channel
non-discharge)** for entries like Theorem G\textsuperscript{otr}.

**Per-deliverable verdict (per (T-otr.1)–(T-otr.9)).**

| Deliverable | Verdict | Headline |
|---|---|---|
| **(T-otr.1) Final theorem statement** | DRAFTED | "Queer U(1)-center anomaly: open side". Class $\hbar N[\bar c]^{\mathrm{otr}}\in H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$, non-trivial, independent of $[\bar c]$. |
| **(T-otr.2) Hypothesis ledger** | DRAFTED | Hypotheses: q(N) source, $N\geq 2$, queer-trace boundary evaluation, signed (A5)^otr regulator; suspends: unsigned (A5), $\Str(I)=0$ as discharge mechanism. |
| **(T-otr.3) Two-supertrace independence** | PROVED | The 2-dim queer centre $\mathfrak z(\mathfrak q(N))=\C\cdot I_{2N}\oplus\C\cdot J$ separates $\Str$ (zero on both) from `otr` (zero on $I_{2N}$, $N$ on $J$); cohomology classes live in different parity sectors $H^2(\bar A,\C)_{\bar 0}$ vs $H^2(\bar A,\Pi\C)_{\bar 1}$. |
| **(T-otr.4) Proof outline** | DRAFTED | q(N) probe → queer-Capelli $Z_2^{\mathrm{otr}}$ → $\mathrm{otr}(J)=N$ propagator-loop coefficient → odd-parity heat-kernel residue → (A5) violation Obs-Q-otr-A5 → identification of $\hbar N[\bar c]^{\mathrm{otr}}$. |
| **(T-otr.5) Phase-5 status** | DECLARED | Phase-5 frontier candidate. NOT Phase-4 chain-level closed. |
| **(T-otr.6) Boundary / brane interpretation** | DRAFTED | The `otr`-channel forces an **off-diagonal mixed-parity brane** distinct from the diagonal even brane; the queer trace witnesses an open-closed duality invisible to $\Str$. |
| **(T-otr.7) Cross-walk** | TABLED | Connects to G4-M3 super-W\_3 vanishing at $M=N$ (G3↔G4 cross-coupling), to W22-T1/T2 (parallel mechanism, opposite verdict), to G5 unreduced primitive closure (independent obstruction). |
| **(T-otr.8) Inscription target** | DRAFTED | Precise LaTeX block targeted for the new Phase-5-frontier section of `claim-strength-ledger.tex`. |
| **(T-otr.9) Anti-attack scan** | DRAFTED | Three named attacks: (Att-1) hidden Str-coboundary; (Att-2) regulator-class redefinition; (Att-3) sub-superalgebra restriction; all answered with discharge response or explicit open status. |

**Bottom line.** The queer trace on q(N) produces a parallel anomaly
class in odd parity, structurally independent from the manuscript's
Theorem G. The inscription target is a Phase-5 frontier candidate,
with all hypotheses, proof outline, boundary interpretation, and
cross-walks fixed at publication grade and ready for future
main-thread authorization.

---

## §1. Final theorem statement

### §1.1 Statement of Theorem G\textsuperscript{otr}

**Theorem G\textsuperscript{otr} (Queer U(1)-center anomaly on
$\mathfrak{q}(N)$).**

*Object under study.* The Dirac brane probe on the queer Lie
superalgebra $\mathfrak{q}(N)\subset\mathfrak{gl}(N|N)$, $N\geq 2$,
with the **queer-trace boundary evaluation** $\mathrm{otr}:
\mathfrak{q}(N)\to\Pi\C$ defined by
\[
   \mathrm{otr}\!\begin{pmatrix}A & B \\ B & A\end{pmatrix}=\Tr(B)
   \in\Pi\C,
\]
extended polynomially via $\partial_{\mathrm{bb},N}^{\mathrm{otr}}:
\C[z_1,z_2]\to\C[\mathfrak{q}(N)^2]^{Q_N}_{\bar 1}$, $f\mapsto
\mathrm{otr}\,f(\phi_1,\phi_2)$, where $Q_N\subset GL_{2N}$ is the
queer subgroup preserving the Cartan involution $\theta(X)=JXJ^{-1}$
of $\mathfrak{gl}(N|N)$.

*Hypothesis list.*
* **(H-otr.1) Queer source.** $\mathfrak g=\mathfrak q(N)$ with the
  matrix realization $\mathfrak q(N)=\{((A,B),(B,A)):A,B\in\mathfrak{gl}_N\}
  \subset\mathfrak{gl}(N|N)$ and the inherited $\Z/2$-grading.
* **(H-otr.2) $N\geq 2$.** $\mathfrak q(1)$ is degenerate (abelian
  even part), so the brane probe degenerates; restrict to $N\geq 2$.
* **(H-otr.3) Queer-trace boundary evaluation.** Boundary contact
  uses the queer trace $\mathrm{otr}$ rather than the ordinary
  supertrace $\Str$.
* **(H-otr.4) Signed parity-equivariance (A5)\textsuperscript{otr}.**
  The heat-kernel parametrix on q(N) satisfies the *signed* parity
  condition $\tau\Delta^{\mathrm{otr}}_{\mathrm{sK}}\tau^{-1}=
  -\Delta^{\mathrm{otr}}_{\mathrm{sK}}$ for the parity-flipping
  operator $\tau$ (concretely $\tau$ may be taken to be conjugation
  by $J$). The unsigned (A5) of W30 is **suspended**.
* **(H-otr.5) Even non-degenerate ad-invariant form.** The form
  $B_0(X,Y)=\Tr(\mathrm{ev}\,XY+\mathrm{ev}\,YX)/2$, where $\mathrm{ev}$
  is the even-block projection, supplies the dual basis used in the
  parametrix construction.
* **(H-otr.6) Brane-line factorization current convention.**
  Compactly supported smearings $a,b\in\Omega^0_c(\R)$ on the brane
  line; central ghost insertion $\gamma_{\mathbf 1}$ of degree 1.
* **(H-otr.7) Closed-side $\omega$-cocycle.** The Lie 2-cocycle
  $\omega(f,g)=[\{f,g\}]_0$ on $\mathfrak h_{\mathrm{poly}}=
  \C[z_1,z_2]$ from `lem:omega-cocycle` is unchanged.
* **(H-otr.8) Sergeev queer-Capelli.** The quadratic odd Casimir
  $Z_2^{\mathrm{otr}}\in U(\mathfrak q(N))_{\bar 1}$ exists and
  controls the propagator-loop contraction (Sergeev 1983).

*Conclusion.* The chain-level mixed brane-defect QME obstruction
representative on the q(N) probe under $\partial_{\mathrm{bb},N}^{\mathrm{otr}}$
is
\[
   \mathrm{Ob}_{\mathrm{sc}}^{\mathrm{otr}}(\gamma_{\mathbf 1}; a,f; b,g)
     = \hbar N\,\omega(f,g)\int_{\R} a(t)b(t)\gamma_{\mathbf 1}(t)\,dt
     \quad\in\mathcal O_{\mathrm{loc}}(\mathcal E_w^{\mathfrak q})_{\bar 1},
\]
with associated graded CE class
\[
   [\hbar N\,\bar c]^{\mathrm{otr}}\in H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}.
\]
This class is non-trivial: any putative primitive
$\bar\eta^{\mathrm{otr}}:\bar A\to\Pi\C$ would lift, by setting
$\tilde\eta^{\mathrm{otr}}(1)=0$, to a primitive of $\Pi\omega$ on
$\mathfrak h_{\mathrm{poly}}$, and the same contradiction
$\omega(z_1,z_2)=1\neq 0$ vs $\tilde\eta^{\mathrm{otr}}(\{z_1,z_2\})=
\tilde\eta^{\mathrm{otr}}(1)=0$ as in `lem:omega-cocycle` rules it
out.

This class is **independent** of the bosonic class $\hbar N[\bar c]
\in H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}$ of the manuscript's
Theorem `thm:u1-center-anomaly-open`: the two classes lie in
different parity sectors of $H^2_{\mathrm{Lie}}(\bar A,\C\oplus\Pi\C)
=H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}\oplus H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$,
arise from different central directions ($I_{2N}\in\mathfrak q(N)_{\bar 0}$
vs $J\in\mathfrak q(N)_{\bar 1}$), and have different parity-equivariance
admissibility classes (unsigned (A5) for $[\bar c]$, signed
(A5)\textsuperscript{otr} for $[\bar c]^{\mathrm{otr}}$).

**Phase-5 caveat.** The chain-level discharge mechanism of W22-T1/T2
**fails** at the queer-trace layer; the obstruction is named
**Obs-Q-otr-A5** in the Phase-4 EXEC G3-M3 verdict. The class
$[\bar c]^{\mathrm{otr}}$ is recorded as a frontier candidate, not as
a chain-level closed theorem.

### §1.2 Why "Theorem G^otr" and not "Theorem G_q"

We use **Theorem G\textsuperscript{otr}** (superscript `otr`) rather
than `Theorem G_q` because:
* The decisive structural distinction is the **trace channel** (`otr`
  vs $\Str$), not the **algebra source** (q(N) vs gl(N|M)). On q(N)
  alone there are *two* parallel theorems: a $\Str$-channel discharge
  (`THEOREM P4-G3-M2-Q` in classical-super-extension-2026-04-28.md
  line 712, where $\Str(I)=0$ kills the residue) and an `otr`-channel
  non-discharge (this document). Labelling them `G_q` would conflate
  them; `G^otr` is precise.
* The `otr` superscript matches the manuscript's symbol convention
  ($\Str$ written as `\Str`, queer trace as `\mathrm{otr}` per
  `phase4-exec-G3-M3-queer-trace-2026-04-28.md` and Cheng–Wang Ch. 6).

If the manuscript's authorship style demands subscripts, alternates
acceptable: $\mathrm G^q_{\mathrm{otr}}$ or $\mathrm G_{\mathfrak q,
\mathrm{otr}}$. The lead label remains `Theorem G^otr`.

---

## §2. Hypothesis ledger

### §2.1 Which (A1)–(A5) variants the theorem requires

The W30 admissibility class for the W22 chain-level discharge is
(A1)–(A5), with (A5) being unsigned parity-equivariance
$P\Delta_{\mathrm{sK}} P^{-1}=\Delta_{\mathrm{sK}}$ where $P$ is the
parity operator on the super-stack. Theorem G\textsuperscript{otr}
**requires** a modified admissibility class, indexed by `otr`:

| Hypothesis | Form on $\mathfrak{gl}(N|N)$ (W30) | Form on $\mathfrak q(N)$ for `otr` (G^otr) | Status |
|---|---|---|---|
| **(A1)** Wave-front locality | $\mathrm{WF}(K_t)\subset T^*M\setminus 0$ | Verbatim | Required, satisfied by Hadamard parametrices |
| **(A2)** Hadamard parametrix structure | Standard heat-kernel form | Verbatim with $B_0$ replacing the Killing form | Required, satisfied via $B_0$ from §3.3 of G3-M3 |
| **(A3)** Finite-window compatibility | Costello finite-window class | Verbatim | Required, satisfied (W22-§3.7) |
| **(A4)** Coefficient-kernel control | Costello coefficient kernel | Verbatim | Required, satisfied |
| **(A5)** Parity-equivariance | Unsigned: $P\Delta P^{-1}=\Delta$ | **(A5)\textsuperscript{otr}**: signed $\tau\Delta\tau^{-1}=-\Delta$ for parity-flipping $\tau$ | **Suspended**; replaced |

The (A5) replacement (A5)\textsuperscript{otr} is the deciding
hypothesis. Its rigorous formalization at the parametrix level is
named as residual `R-P4-G3-M3-Q-otr-01` in the G3-M3 verdict and
remains Phase-5 work; Theorem G\textsuperscript{otr} states the
result *conditional on* (A5)\textsuperscript{otr} being well-defined
and satisfied by a concrete admissible parametrix class
(heat-kernel with the queer central element $J$ inserted, signed
under conjugation by $\tau$).

### §2.2 Hypotheses suspended

The hypotheses **suspended** in Theorem G\textsuperscript{otr}, with
respect to Theorem G:
* **(Sup-1)** Unsigned parity-equivariance (A5) — replaced by
  (A5)\textsuperscript{otr}.
* **(Sup-2)** Bosonic source $\mathfrak{gl}_N$ — replaced by queer
  $\mathfrak q(N)$.
* **(Sup-3)** Trace boundary evaluation $\Tr$ — replaced by queer
  trace $\mathrm{otr}$.
* **(Sup-4)** Even target $\C$ for the cocycle — replaced by odd
  target $\Pi\C$.
* **(Sup-5)** $\Str(I)=0$ as the W22 chain-level discharge mechanism
  — **abandoned**: $\mathrm{otr}(J)=N\neq 0$, no chain-level discharge.

The remaining hypotheses (closed-side $\omega$, brane-line currents,
central ghost insertion) are unchanged.

### §2.3 Primary-source anchors per hypothesis

| Hypothesis | Primary source | Role |
|---|---|---|
| **(H-otr.1)** Queer source | Cheng–Wang 2012 §1.1.4 / §6 | Definition of $\mathfrak q(N)$ |
| **(H-otr.2)** $N\geq 2$ | Cheng–Wang 2012 §1.36 | Non-degeneracy of basic classical for $N\geq 2$ |
| **(H-otr.3)** Queer-trace boundary evaluation | Sergeev 1983 *Letters Math. Phys.* 7, 177–179 | Original `otr` definition |
| **(H-otr.4)** (A5)\textsuperscript{otr} | New (this document); inspired by Berele–Regev 1987 hook formula | Parity twist of W30 (A5) |
| **(H-otr.5)** $B_0$ form | Cheng–Wang 2012 Prop. 1.36 | Even ad-invariant form on $\mathfrak q(N)$ |
| **(H-otr.6)** Brane-line factorization current | Costello–Gwilliam Vol II §11 | Compactly supported convention |
| **(H-otr.7)** $\omega$-cocycle | `lem:omega-cocycle` in `main.tex` 284 | Closed-side cocycle |
| **(H-otr.8)** Sergeev queer-Capelli | Sergeev 1983; Sergeev 1985 *Sbornik* 51, 419–427; Penkov–Serganova 1992; Gorelik 2004; Brundan–Kleshchev 2003 | Centre of $U(\mathfrak q(N))$ |

The two anchors most under load — (H-otr.4) and (H-otr.8) — both
trace back to the same Sergeev primary-source pair (1983, 1985). The
remaining anchors are conventional (Cheng–Wang for the queer
superalgebra source, Costello–Gwilliam Vol II for the BV regulator
class, manuscript's own Lemma `lem:omega-cocycle` for the closed
cocycle).

---

## §3. Two-supertrace independence proof

### §3.1 The 2-dimensional queer centre

**Claim.** The centre $\mathfrak z(\mathfrak q(N))\subset\mathfrak q(N)$
of the queer Lie superalgebra is **2-dimensional**, with the splitting
\[
   \mathfrak z(\mathfrak q(N))=\C\cdot I_{2N}\oplus\C\cdot J,
\]
where $I_{2N}=\diag(I_N,I_N)\in\mathfrak q(N)_{\bar 0}$ is the **even
central element** and $J=((0,I_N),(-I_N,0))\in\mathfrak q(N)_{\bar 1}$
is the **odd central element**.

**Proof.** The matrix algebra $M_{2\times 2}(\mathfrak{gl}_N)$
restricted to the queer pattern $\{((A,B),(B,A)):A,B\in\mathfrak{gl}_N\}$
has matrix-level centre $\C\cdot I_{2N}$ on the even block and
$\C\cdot J$ on the odd block; this is verified by direct
computation: a queer matrix $((A_0,B_0),(B_0,A_0))$ commutes with
*every* queer matrix $((A,B),(B,A))$ iff $A_0=cI_N$, $B_0=c'I_N$ for
some scalars $c,c'\in\C$ (using $[A_0,A]=0$ for all $A\in\mathfrak{gl}_N$
gives $A_0\in\C\cdot I_N$, and similarly for $B_0$). The two central
generators in the queer pattern are $I_{2N}=\diag(I_N,I_N)$ (even
parity, $A=I_N$, $B=0$) and $J=((0,I_N),(-I_N,0))$ (odd parity,
$A=0$, $B=I_N$ up to the signed convention).

**Centrality verified.**
* $I_{2N}$ is the matrix identity, central in any matrix algebra.
* $J$ in the super-bracket: for $X\in\mathfrak q(N)_{\bar 0}$,
  $[X,J]=XJ-JX=0$ as matrices (checked in G3-M3 §3.1 lines
  316–325). For $X\in\mathfrak q(N)_{\bar 1}$, the super-bracket is
  the anticommutator $[X,J]_{\mathrm{super}}=XJ+JX$; direct
  computation gives $XJ+JX=0$ (G3-M3 §3.1 lines 333–348).

So $J$ is super-central in $\mathfrak q(N)$.

**Crucially,** $J$ anticommutes with the parity operator
$P^{\mathfrak q}=\diag(\mathbf 1_N,-\mathbf 1_N)$ in the conjugation
sense:
\[
   P^{\mathfrak q}\cdot J\cdot (P^{\mathfrak q})^{-1}=-J,
\]
which is the algebraic source of the (A5)-violation; see G3-M3 §3.3
lines 376–388. $\square$

### §3.2 The two characters on $\mathfrak z(\mathfrak q(N))$

The 2-dimensional centre $\mathfrak z(\mathfrak q(N))=\C\cdot I_{2N}
\oplus\C\cdot J$ admits two distinct ad-invariant characters:

| Character | $I_{2N}$ value | $J$ value | Parity sector |
|---|---|---|---|
| $\Str:\mathfrak q(N)\to\C$ | $\Str(I_{2N})=N-N=0$ | $\Str(J)=0$ (off-diagonal) | $\bar 0$ (even target) |
| $\mathrm{otr}:\mathfrak q(N)\to\Pi\C$ | $\mathrm{otr}(I_{2N})=\Tr(0)=0$ | $\mathrm{otr}(J)=\Tr(I_N)=N$ | $\bar 1$ (odd target) |

The characters separate the two central directions: $\Str$ vanishes
on **both** central elements, while $\mathrm{otr}$ vanishes on
$I_{2N}$ but evaluates to $N$ on $J$.

### §3.3 Two-cohomology decomposition

The natural ambient class space for the brane-probe QME on q(N) is
the **graded direct sum**
\[
   H^2_{\mathrm{Lie}}(\bar A;\C\oplus\Pi\C)
     = H^2_{\mathrm{Lie}}(\bar A;\C)_{\bar 0}\oplus H^2_{\mathrm{Lie}}(\bar A;\Pi\C)_{\bar 1}
     = \C\cdot[\bar c]\oplus\Pi\C\cdot[\bar c]^{\mathrm{otr}},
\]
where the $\Pi$ in the second summand records the parity-shift functor
on the coefficient line. Since both cohomologies are 1-dimensional
(each generated by the constant Taylor coefficient cocycle of
`lem:omega-cocycle`, valued respectively in $\C$ and $\Pi\C$), the
sum is 2-dimensional as a $\Z/2$-graded space.

The brane probe on q(N) produces a class in this 2-dimensional graded
space:
\[
   [\mathrm{Ob}_{\mathrm{sc}}^{\mathfrak q}]
     = (\hbar\Str(I_{2N})\,[\bar c],\; \hbar\,\mathrm{otr}(J)\,[\bar c]^{\mathrm{otr}})
     = (0,\;\hbar N\,[\bar c]^{\mathrm{otr}})
     \in H^2_{\mathrm{Lie}}(\bar A;\C\oplus\Pi\C).
\]

### §3.4 Independence statement and proof

**Statement.** The two classes $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}$
(manuscript's Theorem G) and $[\bar c]^{\mathrm{otr}}\in
H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$ (this Theorem
G\textsuperscript{otr}) are **structurally independent**:
* They live in **different parity sectors** of the graded
  cohomology $H^2_{\mathrm{Lie}}(\bar A,\C\oplus\Pi\C)$.
* They are realized on **different sources**: $[\bar c]$ on
  $\mathfrak{gl}_N$ via $\Tr$; $[\bar c]^{\mathrm{otr}}$ on
  $\mathfrak q(N)$ via $\mathrm{otr}$.
* They arise from **different central directions** of distinct
  centres: $\C\cdot I\subset\mathfrak{gl}_N$ for $[\bar c]$;
  $\C\cdot J\subset\mathfrak q(N)_{\bar 1}$ for $[\bar c]^{\mathrm{otr}}$.
* They satisfy **different parity-equivariance** admissibility:
  unsigned (A5) for $[\bar c]$, signed (A5)\textsuperscript{otr} for
  $[\bar c]^{\mathrm{otr}}$.
* The W22 / W30 chain-level discharge mechanism kills neither
  $[\bar c]$ on the bosonic source (since $\Tr(I)=N\neq 0$ — Theorem
  G is non-trivial) nor $[\bar c]^{\mathrm{otr}}$ on the queer source
  (since $\mathrm{otr}(J)=N\neq 0$ and the (A5)-replacement does not
  produce a vanishing coefficient). Both classes are residue
  obstructions, in their respective parity sectors.

**Proof of independence (formal).** Suppose, for contradiction, that
$[\bar c]^{\mathrm{otr}}$ were a $\Pi$-shifted multiple of $[\bar c]$
or coboundary-related to it. The parity-shift functor $\Pi:\C\to\Pi\C$
is *not* an isomorphism of cohomology groups: cohomology classes are
distinguished by their parity grading, and a non-zero class in the
$\bar 1$ sector cannot equal (or be coboundary-related to) a class
in the $\bar 0$ sector. Concretely, the BV obstruction complex
$(\mathcal O_{\mathrm{loc}}, Q+\{I_0,-\})$ is $\Z/2$-graded, the
differential preserves the grading, and cohomology classes are
elements of the graded cohomology $H^\bullet=H^\bullet_{\bar 0}\oplus
H^\bullet_{\bar 1}$. The two summands are a direct sum decomposition
of vector spaces (and of $\C$-modules, where $\Pi\C$ acts on the odd
summand). Hence $[\bar c]\in H^2_{\bar 0}$ and $[\bar c]^{\mathrm{otr}}
\in H^2_{\bar 1}$ are linearly independent as elements of $H^2_{\bar 0}
\oplus H^2_{\bar 1}$.

This is **not** a statement that the *underlying* Lie 2-cocycle
$\omega$ is two distinct cocycles — it is the *same* cocycle
$\omega(f,g)=[\{f,g\}]_0$, but the **coupling characters** ($\Tr$
vs $\mathrm{otr}$) give it two distinct realizations on the matrix
sources, which sit in different parity sectors of the graded BV
cohomology. The "independence" is a statement about the *coupled*
classes (cocycle × character), not the bare cocycle. $\square$

### §3.5 Witten lens — physical interpretation of independence

**The two-supertrace structure as an open-closed witness.** The
manuscript's Theorem G is the open-side image of the closed-side
$\omega$-cocycle under the trace-evaluation map
$\partial_{\mathrm{bb},N}^{\mathrm{full}}:f\mapsto\Tr\,f$. On q(N), the
boundary evaluation **splits into two channels**:
$\partial_{\mathrm{bb},N}^{\Str}$ and $\partial_{\mathrm{bb},N}^{\mathrm{otr}}$.
The closed-side cocycle $\omega$ is unchanged (it lives on $\bar A$,
not on the matrix source), but the **open-side coupling** depends on
the channel: the $\Str$-channel coupling is zero (the manuscript's
$\Tr$-channel gives $N$ on the bosonic gl, but on q(N) the
$\Str$-channel is $\Str(I_{2N})=0$), and the `otr`-channel coupling is
$N$.

This means the closed-side cocycle $\omega$ produces *two* parallel
open-side realizations on q(N). The bosonic source carries one
realization (Theorem G) — and on q(N) the $\Str$-channel
is "pure" (zero coupling), while the `otr`-channel is "anomalous"
(coupling $N$). The two realizations are physically distinct
boundary conditions on the brane probe.

**Open-closed duality interpretation.** In BCOV 1994 §6.3, the open-closed
duality is the statement that the closed-side (string) cocycle has
an open-side (brane) image; the present manuscript's Theorem G is
the local d=2 formal-disk shadow of this on $\mathfrak{gl}_N$. The
queer extension records that **the q(N) brane probe sees a second
open-side image** — the `otr`-channel — which is not visible to a
bosonic probe. Physically this is a **parastatistic open-closed
duality**: the queer-supertrace is the algebraic shadow of a
parastatistic boundary state, and it pairs against the *same* closed
cocycle through a different boundary evaluation map.

This is consistent with Sergeev's original 1983 motivation
(parastatistics of fermionic gauge extensions) and with the
Cheng–Wang Ch. 6 catalog of queer extensions. The independence proven
above means the brane catalog on q(N) carries an additional anomaly
class invisible to gl-extensions.

---

## §4. Proof outline

### §4.1 Step-by-step structure (T-otr.4)

The proof of Theorem G\textsuperscript{otr} runs through six steps:

**Step 1: q(N) probe basis and Dirac action.**
Set up the Dirac brane probe action on q(N) with queer-trace
boundary evaluation:
\[
   S_\partial^{\mathrm{q,otr}}=\int_\R \mathrm{otr}\bigl(\phi_1\,d\phi_2
     + A[\phi_1,\phi_2]_{\mathfrak q}\bigr),
\]
where $\phi_1,\phi_2\in\mathfrak q(N)$ have *both* even and odd
components (the queer trace is non-trivial only on odd elements, so
the action requires odd field content). The BV/Koszul variable
$\psi=A^*\in\mathfrak q(N)$ has degree $-1$ and satisfies
$Q\psi=[\phi_1,\phi_2]_{\mathfrak q}$, where the bracket is the
super-bracket on $\mathfrak q(N)$.

This step inherits the brane-line factorization current convention
from the manuscript's `thm:lane-factorization-current` lane verbatim,
with the supertrace replaced by the queer trace.

**Step 2: Sergeev queer-Capelli central element.**
The quadratic odd Casimir of Sergeev (1983) in $U(\mathfrak q(N))$:
\[
   Z_2^{\mathrm{otr}}=\sum_{i,j=1}^N\bigl(T_{ij}T_{ji}^{(\mathrm{odd})}
     +T_{ji}^{(\mathrm{odd})}T_{ij}\bigr)\in U(\mathfrak q(N))_{\bar 1},
\]
with $T_{ij}\in\mathfrak{gl}_N\subset\mathfrak q(N)_{\bar 0}$ even
matrix units and $T_{ij}^{(\mathrm{odd})}\in\Pi\mathfrak{gl}_N\subset
\mathfrak q(N)_{\bar 1}$ odd matrix units. Centrality in
$U(\mathfrak q(N))$ verified in G3-M3 §1.1 lines 130–148; parity
verified in G3-M3 §1.1 lines 126–129 (sum of mixed even-odd products,
each summand parity $\bar 0+\bar 1=\bar 1$).

This is the Capelli analogue of the gl-Capelli element $c_2$
controlling the bosonic Theorem G; the *odd parity* of
$Z_2^{\mathrm{otr}}$ is the algebraic shadow of the parity shift
between $[\bar c]$ and $[\bar c]^{\mathrm{otr}}$.

**Step 3: Propagator-loop coefficient $\mathrm{otr}(J)=N$.**
The propagator-loop contraction in the queer-trace channel, computed
on the queer-twisted parametrix
$\Delta^{\mathrm{otr}}_{\mathrm{sK}}=\sum_a(-1)^{|a|}JT^aJT_a$:

Using $J^2=-I_{2N}$, $[T^a,J]=0$ for $T^a$ even, $T^aJ=-JT^a$ for
$T^a$ odd (G3-M3 §3.1 lines 314–348), and $\mathrm{otr}(J)=\Tr(I_N)
=N$ (G3-M3 §2.2 lines 244–254):

The boundary contact bracket in the queer channel:
\[
   \{I_\partial^{\mathrm{otr}}(a,f),I_\partial^{\mathrm{otr}}(b,g)\}_{\mathrm{open}}
     = I_\partial^{\mathrm{otr}}(ab,\{f,g\}_{\bar A})
       + \mathrm{otr}(J\cdot I_{2N})\cdot\omega(f,g)\int_\R a(t)b(t)\,dt
\]
gives coefficient $\mathrm{otr}(J)=N$ on the central direction
$\C\cdot J$. This is parallel to the bosonic $\Tr(I_N)=N$ on
$\mathfrak{gl}_N$ central direction $\C\cdot I$ (manuscript's
`thm:u1-center-anomaly-open` line 354), but in the **odd** parity
sector.

**Step 4: Odd-parity heat-kernel residue.**
Inserting the central ghost $\gamma_{\mathbf 1}$ of degree 1 (per
manuscript's `def:app-unreduced-bv-degrees`):
\[
   \mathrm{Ob}_{\mathrm{sc}}^{\mathrm{otr}}(\gamma_{\mathbf 1};a,f;b,g)
     = \hbar N\,\omega(f,g)\int_{\R} a(t)b(t)\gamma_{\mathbf 1}(t)\,dt
     \quad\in\mathcal O_{\mathrm{loc}}(\mathcal E_w^{\mathfrak q})_{\bar 1}.
\]

Here $\mathcal E_w^{\mathfrak q}$ is the q(N)-source weighted brane
local space (analogous to $\mathcal E_w$ on gl), and the obstruction
sits in the **odd-parity** sector of the BV obstruction complex
(because the queer trace lands in $\Pi\C$, shifting the parity of
the local-functional output by 1).

**Step 5: (A5) violation Obs-Q-otr-A5.**
The standard regulator class admissible for $\Str$ on gl(N|N) (the
W30 (A1)–(A5)) is **not** admissible for `otr` on q(N). The
operator-level (A5) check (G3-M3 §3.3–§3.4 lines 376–467) shows
$P^{\mathfrak q}\cdot J\cdot (P^{\mathfrak q})^{-1}=-J$, so the
queer-twisted parametrix
$\Delta^{\mathrm{otr}}_{\mathrm{sK}}=-\sum_a T^aT_a$ does not satisfy
unsigned (A5). The signed replacement (A5)\textsuperscript{otr}:
$\tau\Delta^{\mathrm{otr}}_{\mathrm{sK}}\tau^{-1}=
-\Delta^{\mathrm{otr}}_{\mathrm{sK}}$ is the natural admissibility
condition under the queer twist.

This is the **named obstruction** Obs-Q-otr-A5 (G3-M3 §5.2 lines
684–702): the queer central element $J$ violates the *unsigned*
parity-equivariance condition that the W22 mechanism requires. The
W22 chain-level discharge **does not extend** to the queer-trace
channel — the propagator-loop contracts not with $\Str(I)=0$ but
with $\mathrm{otr}(J)=N$, an irreducibly non-zero coefficient.

**Step 6: Identification of the residue class.**
The non-trivial cohomology class $\hbar N[\bar c]^{\mathrm{otr}}\in
H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$ is identified by the same
proof of non-triviality as `lem:omega-cocycle` (manuscript line 290,
$[\bar c]\neq 0$): any putative primitive $\bar\eta^{\mathrm{otr}}:
\bar A\to\Pi\C$ would lift to a primitive of $\Pi\omega$ on
$\mathfrak h_{\mathrm{poly}}$; the only such primitive is
$\eta(f)=-[f]_0$, which does not descend to $\bar A$ (because
$\eta(1)=-1\neq 0$). Contradiction. Hence $[\bar c]^{\mathrm{otr}}$ is
non-trivial in $H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$.

The **independence** from $[\bar c]$ is by §3.4: the two classes
live in different parity sectors of the graded cohomology
$H^2_{\mathrm{Lie}}(\bar A,\C\oplus\Pi\C)=H^2_{\bar 0}\oplus H^2_{\bar 1}$.

This completes the proof outline. $\square$

### §4.2 Why the W22 mechanism does not extend

The W22 chain-level discharge of the bosonic Theorem G obstruction on
$\mathfrak{gl}(N|N)$ runs through the lift formula
$\mathrm{Ob}_{\mathrm{sc}}^{\Str}=\hbar\Str(I)\cdot\Lambda^{\Str}(\omega)$
(W22-L2), where $\Lambda^{\Str}$ depends only on closed-side data
and $\Str(I)=N-N=0$ kills the entire chain-level expression strictly.

For the queer-trace channel, the parallel formula reads
\[
   \mathrm{Ob}_{\mathrm{sc}}^{\mathrm{otr}}=\hbar\,\mathrm{otr}(J)\cdot\Lambda^{\mathrm{otr}}(\omega),
\]
and the coefficient $\mathrm{otr}(J)=N\neq 0$ does not vanish. The
**fundamental algebraic obstruction**: there is no non-trivial central
element of $\mathfrak q(N)_{\bar 1}$ with $\mathrm{otr}=0$. (G3-M3
§5.3 lines 705–720 verifies that the only central element with
$\mathrm{otr}=0$ in the odd part is the zero element.)

This is the **second** structural reason Theorem G\textsuperscript{otr}
is not chain-level closed: even if (A5)\textsuperscript{otr} is
formally satisfied by some signed admissibility class, the
propagator-loop coefficient $\mathrm{otr}(J)$ is irreducibly $N$,
and the residue class $\hbar N[\bar c]^{\mathrm{otr}}$ is non-trivial.

### §4.3 What is *not* claimed

To be precise, Theorem G\textsuperscript{otr} **does not claim**:
* That the residue class $[\bar c]^{\mathrm{otr}}$ is **discharged**.
  It is recorded as a non-trivial residue, parallel to (but distinct
  from) the bosonic Theorem G's $[\bar c]$.
* That $[\bar c]^{\mathrm{otr}}$ is **deformable** to a chain-level
  cocycle. The standard regulator class admissible for $\Str$ does
  not extend to `otr`; the new class (A5)\textsuperscript{otr}
  produces a different chain-level cocycle, with the same residue.
* That the q(N) probe is **physically realized** in any specific
  Calabi–Yau or topological string setting. The cross-link to Vol III
  CY-to-chiral and BCOV is convention-checking only (per CLAUDE.md);
  no compact-CY claim follows from this local Hamiltonian BF/Moyal
  calculation.
* That $[\bar c]^{\mathrm{otr}}$ kills or generates any specific
  open-string sector (e.g., orientifold projections, K-theory
  classes). These are residual questions for cross-volume work.

---

## §5. Phase-5 status declaration

### §5.1 Why this is Phase-5 frontier, not Phase-4 closed

Theorem G\textsuperscript{otr} is **explicitly marked Phase-5
frontier**, not Phase-4 chain-level closed, for three structural
reasons:

**Reason 1 (regulator class).** The (A5)\textsuperscript{otr}
admissibility class is sketched at the parametrix level (G3-M3
§3.4), but its rigorous formalization — including verification that
heat-kernel, Pauli–Villars, and Hadamard parametrices admit a signed
version — is **R-P4-G3-M3-Q-otr-01** (G3-M3 line 974), Phase-5 work.

**Reason 2 (higher-loop class).** The all-loop class structure on
q(N) involves $\mathrm{otr}(J^k)$ at all loop counts. Computation
gives:
* $k$ even: $\mathrm{otr}(J^k)=\mathrm{otr}((-1)^{k/2}I)=0$.
* $k$ odd: $\mathrm{otr}(J^k)=(-1)^{(k-1)/2}\mathrm{otr}(J)=
  (-1)^{(k-1)/2}N$.

So the all-loop residue is $\hbar^\ell\cdot N\cdot(\text{alternating
signs})\cdot[\bar c]^{\mathrm{otr}}$ at odd loop counts.
**R-P4-G3-M3-Q-otr-02** (G3-M3 line 977): identify the alternating
geometric series as a CE class. Phase-5 work.

**Reason 3 (cross-volume coupling).** The cross-link to the Vol III
CY-to-chiral frontier — where queer extensions of the chiral algebra
are natural (Cheng–Wang Ch. 6) — requires a separate matched-conventions
theorem per CLAUDE.md. This is **R-P4-G3-M3-Q-otr-04** (G3-M3 line
989). Phase-5 work.

### §5.2 Phase-5-Q-A vs Phase-5-Q-B

The G3-M3 verdict named two Phase-5 routes (G3-M3 §10.1 lines
1024–1054):

**Phase-5-Q-A (signed parity-equivariance).** Define
(A5)\textsuperscript{otr} as the signed condition
$\tau\Delta\tau^{-1}=-\Delta$ for parity-flipping $\tau$, verify
admissibility, study propagator-loop coefficients across the
admissible class. **Status: route well-defined but unlikely to
discharge** (G3-M3 §10.1 lines 1037–1040), because the central
directions of q(N) have non-zero `otr` regardless of the regulator
class.

**Phase-5-Q-B (parallel theorem).** Accept the queer channel
produces a *new* anomaly class $\hbar N[\bar c]^{\mathrm{otr}}$,
independent of $[\bar c]$, document as a parallel theorem in the
manuscript. **Status: structural finding** (G3-M3 §10.1 lines
1041–1048), an honest path that records the obstruction without
silently reconciling it.

**This document executes Phase-5-Q-B.** The proof outline (§4) is
the Phase-5-Q-B inscription, with (A5)\textsuperscript{otr} stated as
a hypothesis but not formally verified at the parametrix level.

The choice is:
* **Voice (Russian school, BCOV, CLAUDE.md):** "report, do not
  silently reconcile" — Phase-5-Q-B accepts the obstruction; Phase-5-Q-A
  attempts a quiet repair and risks producing a regulator-class
  artefact rather than a structural finding.
* **Cross-volume coherence:** the Vol III CY-to-chiral frontier
  expects a queer extension of the bosonic anomaly story; Phase-5-Q-B
  records this honestly, while Phase-5-Q-A would generate a regulator
  hypothesis that may not hold globally.
* **Manuscript impact:** Theorem G\textsuperscript{otr} as a
  parallel theorem strengthens the central-extension catalog; a
  Phase-5-Q-A signed-A5 result would not produce a manuscript-side
  theorem (it would produce a regulator-hypothesis lemma).

### §5.3 Status vocabulary

The proposed status for Theorem G\textsuperscript{otr} in the
claim-strength ledger is **Phase-5 frontier candidate
(parallel-channel non-discharge)** — a new vocabulary item beyond
the current ledger's *proved in finite algebraic model* /
*proved degreewise stable* / *proved in weighted Tate coefficient
model* / *computed to stated order* / *conditional on named
QME/radial-parts/unweighted-regulator theorem* / *conjectural* /
*open* / *not asserted*.

This vocabulary item captures: (a) the residue class is **named** and
its statement is **publication-grade precise**; (b) the chain-level
discharge mechanism is **explicitly absent** (Obs-Q-otr-A5); (c) the
class is **independent** of the manuscript's other theorems and
records a parallel anomaly; (d) Phase-5 work would either close the
class via cross-volume embedding or accept it as a structural
finding.

The vocabulary distinguishes Phase-5 frontier candidates from
*conjectural* (which suggests a path to proof exists) and *open*
(which is silent on existence of a proof path) — a frontier
candidate is a **specific named residue class** awaiting
cross-volume context for closure or escalation.

---

## §6. Boundary / brane interpretation

### §6.1 The two boundary states distinguished by Str vs otr

**Witten lens — physical interpretation.** The brane probe Dirac
construction is a boundary state on the closed topological string;
the boundary evaluation map is the algebraic shadow of how the
boundary state pairs against closed-string operators. On
$\mathfrak{gl}_N$, the boundary state is *one*-dimensional in the
trace-channel (a single pairing $\Tr$). On q(N), the boundary state
is *two*-dimensional in the trace-channel space (the two characters
$\Str$ and $\mathrm{otr}$ on the 2-dimensional centre $\C\cdot
I_{2N}\oplus\C\cdot J$).

This matches the **boundary-state catalog** prediction of Cheng–Wang
2012 Ch. 6 and Sergeev 1983: the queer Lie superalgebra carries an
additional "off-diagonal" boundary component — the boundary state
that pairs against the odd central direction $\C\cdot J$ — invisible
in bosonic / ordinary-supertrace probes.

**Explicit boundary-state distinction:**
* The **diagonal even brane** corresponds to the $\Str$-channel,
  pairing through the matrix identity $I_{2N}$. This is the natural
  bosonic-extension brane, with cocycle coupling
  $\Str(I_{2N})=N-N=0$ — discharged.
* The **off-diagonal mixed-parity brane** corresponds to the
  `otr`-channel, pairing through the queer central element $J$.
  This is the parastatistic boundary state that sees the $J$-eigenvalue
  via $\mathrm{otr}(J)=N$ — anomalous.

The two boundary states are **structurally distinct**: they pair
against different central directions, lie in different parity
sectors, and have different cohomology realizations.

### §6.2 Does the otr channel correspond to a distinct boundary condition?

**Yes — at three levels.**

**Level (a): boundary field content.** The Dirac brane action
$S_\partial^{\mathrm{q,otr}}=\int\mathrm{otr}(\phi_1\,d\phi_2+
A[\phi_1,\phi_2])$ requires the fields $\phi_1,\phi_2\in\mathfrak q(N)$
to have *both* even and odd components — restricted to the even part
$\mathfrak q(N)_{\bar 0}=\mathfrak{gl}_N$ alone, the action is
identically zero (since $\mathrm{otr}$ is identically zero on the
even part). This is structurally different from the
$\Str$-channel action (which restricts to the even part). The
**boundary field content** is different.

**Level (b): parity-equivariance condition.** The (A5) regulator
condition for the $\Str$-channel is unsigned, $P\Delta P^{-1}=\Delta$;
the (A5)\textsuperscript{otr} for the `otr`-channel is signed,
$\tau\Delta\tau^{-1}=-\Delta$ for parity-flipping $\tau$. The
**boundary regulator class** is different.

**Level (c): cocycle target.** The $\Str$-channel cocycle is valued
in $\C$ (even target); the `otr`-channel cocycle is valued in
$\Pi\C$ (odd target). The **boundary observable target** is
different.

These three differences justify the term "distinct boundary
condition": the `otr`-channel brane is a structurally different
object from the $\Str$-channel brane on the same source q(N).

### §6.3 The q(N) probe as an off-diagonal mixed-parity brane

**Algebraic picture.** The queer Lie superalgebra $\mathfrak q(N)
\subset\mathfrak{gl}(N|N)$ is the **fixed-point subalgebra** of
$\mathfrak{gl}(N|N)$ under the involution $\theta(X)=JXJ^{-1}$ (where
$J$ is the queer central element acting by conjugation). This means
q(N) is the algebra of matrices that are "self-dual under $J$" — a
structurally off-diagonal subalgebra in the $\mathfrak{gl}(N|N)$
embedding.

**Brane picture.** The q(N) probe is the brane stack that respects
this $J$-self-duality. In the bosonic picture, the equivalent would
be a brane stack restricted to a self-dual subalgebra under some
involution on $\mathfrak{gl}_{2N}$ — i.e., an orientifold-like
projection. The q(N) probe is the **graded analogue of an
orientifold-projected brane**, with $J$ playing the role of the
orientifold operator.

**Key consequence.** The orientifold-style projection by $J$ exposes
a new boundary cohomology class — the `otr`-channel — that is
absent in the unrestricted $\mathfrak{gl}(N|N)$ probe. This is the
algebraic shadow of the orientifold-induced K-theory class shift in
the bosonic story (Witten 1998, Sen 1998 anti-brane mechanisms).

**R-P4-G3-M3-Q-otr-05 (G3-M3 line 994).** The orientifold /
boundary-state interpretation: explicit identification of the
orientifold-projection rule that exchanges the $\Str$ and `otr`
channels. Phase-5 cross-volume work; not part of the present
inscription proposal.

### §6.4 Open-closed duality witnessed by otr

In the manuscript's Theorem G, the closed-side cocycle
$[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$ has an open-side
realization on $\mathfrak{gl}_N$ via $\Tr$ (the boundary-evaluation
map $\partial_{\mathrm{bb},N}^{\mathrm{full}}$). This is the open-closed
duality at the bosonic level.

**On q(N), the closed cocycle has *two* parallel open-side
realizations:**
* Through $\Str$ on the diagonal even brane: zero coupling (the
  $\Str$-channel discharges).
* Through `otr` on the off-diagonal mixed-parity brane: coupling
  $N$ (the `otr`-channel is anomalous).

**The open-closed duality witnessed by `otr` is a parastatistic
duality**: the queer-supertrace pairs the closed-side cocycle with
a boundary state that is invisible to the ordinary-supertrace
boundary state. This is the **second open-side image** of the same
closed-side cocycle, accessible only through the queer channel.

Physically (Witten lens): the `otr` channel is the algebraic
shadow of the Sen/Witten anti-brane mechanism on a graded source —
the q(N) probe carries an additional open-side observable that
records the parastatistic central charge.

### §6.5 Boundary-state catalog implications

If a future Phase-5 work establishes the orientifold-projection rule
between $\Str$ and `otr` channels, the boundary-state catalog on
q(N) would split into:
* **$\Str$-states**: ordinary-supertrace branes, with anomaly
  coefficient zero (discharged).
* **`otr`-states**: queer-trace branes, with anomaly coefficient
  $N$ (Theorem G\textsuperscript{otr}).

The manuscript's existing brane catalog records only the $\Str$-states
implicitly (through the bosonic Theorem G with $\mathfrak{gl}_N$);
the queer extension would record a parallel `otr`-catalog with the
same coefficient $N$ but in odd parity. **The brane catalog on q(N)
is genuinely 2-dimensional in the trace-channel space**, parallel to
the 2-dimensional centre.

---

## §7. Cross-walk table

### §7.1 Connections to G3↔G4 cross-coupling

| Connection | Source document | Description | Status |
|---|---|---|---|
| **G3-M2 ↔ G^otr (parallel)** | `phase4-exec-classical-super-extension-2026-04-28.md` §3 lines 550–807 | G3-M2 discharges q(N) at the $\Str$ layer (W22-mechanism); G^otr records the parallel `otr`-residue at q(N). The two are structurally **independent** (different parity sectors). | G3-M2 Phase-4 closed; G^otr Phase-5 frontier |
| **G3-M3 → G^otr (verdict→inscription)** | `phase4-exec-G3-M3-queer-trace-2026-04-28.md` (full, 1108 lines) | G3-M3 verdict: queer-trace does NOT discharge (Obs-Q-otr-A5); G^otr inscribes the residue class as Phase-5-Q-B. | This document executes Phase-5-Q-B from G3-M3 §10 |
| **G4-M3 super-W\_3 vanishing at $M=N$** | `phase4-exec-G4-M3-W3-twist-2026-04-28.md` §0 line 104 | Super-W\_3 in osp(2N\|2N) at $M=N$ vanishes by W22-T1+T2 mechanism (Sergeev–Berele–Regev parity-equivariance preserved). On q(N), the parallel mechanism for the `otr` channel **fails** (Obs-Q-otr-A5). G3↔G4 cross-coupling: the super-W\_3 vanishing is at the $\Str$-channel; the `otr`-channel super-W\_3 question is a Phase-5 residual. | G4-M3 conditional discharge; cross-coupling to G^otr open |
| **W22-T1/T2 (parallel mechanism, opposite verdict)** | `wave3-W22-supertrace-rigorous-2026-04-28.md` §0 + §6 | W22-T1/T2 close on $\mathfrak{gl}(N\|N)$: $\Str(I)=0$ kills the residue. On q(N), the analogue $\Lambda^{\mathrm{otr}}$ exists, but $\mathrm{otr}(J)=N\neq 0$ and (A5) is replaced by (A5)\textsuperscript{otr}; **opposite verdict**. | W22 Phase-3 closed; G^otr Phase-5 frontier |

### §7.2 Connections to G5 unreduced primitive closures

| Connection | Source / target | Description | Status |
|---|---|---|---|
| **G5 unreduced primitive (T₅)** | `tate-T5-chain-level-primitive.tex` (chain-level primitive shadow); `appendix-unreduced-bv-qme.tex` Theorem `thm:app-unreduced-polynomial-centrality-no-go` | G5 records the no-go for unreduced polynomial primitives on $\mathfrak{gl}_N$. The queer extension G5\textsuperscript{otr} (hypothetical Phase-5) would record a parallel no-go on q(N): polynomial unreduced lifts of the `otr`-channel obstruction also fail by local-nilpotence (the same argument as Theorem `thm:app-unreduced-polynomial-centrality-no-go` extends to $\mathfrak q(N)$). | G5 Phase-4 closed; G5\textsuperscript{otr} Phase-5 conjectural (parallel no-go expected) |
| **G5-M2 reduced primitive Moyal target** | `appendix-radial-parts-moyal.tex`; manuscript `constr:quantum-principal-part-descendant-target` | G5-M2 constructs the reduced Moyal principal-part target. The queer extension G5-M2\textsuperscript{otr} would extend this to a Moyal target with queer-Capelli normalization (Sergeev odd-Casimir replacing gl-Capelli). | G5-M2 Phase-4 closed (reduced); G5-M2\textsuperscript{otr} Phase-5 frontier |
| **G^otr ↔ G5\textsuperscript{otr} (independent obstructions)** | This document + tate-T5 | G^otr records the *scalar contact* QME residue in the `otr` channel; G5\textsuperscript{otr} (hypothetical) would record the *unreduced primitive* QME residue. The two are independent obstructions in the `otr`-channel BV catalog, parallel to the $\Tr$-channel pair (Theorem G + G5). | Both Phase-5 frontier; independence by parity sector |

### §7.3 Connection to W22 supertrace (parallel mechanism, opposite verdict)

The cleanest cross-walk is to W22-T1/T2 itself. The two theorems are
**structurally parallel**, **opposite in verdict**:

| Aspect | W22-T1/T2 ($\Str$ on gl(N\|N)) | Theorem G^otr (`otr` on q(N)) |
|---|---|---|
| **Source** | $\mathfrak{gl}(N\|N)$ | $\mathfrak q(N)\subset\mathfrak{gl}(N\|N)$ |
| **Trace channel** | $\Str$ (even target $\C$) | `otr` (odd target $\Pi\C$) |
| **Central element** | $I=\diag(I_N,I_N)$ | $J=((0,I_N),(-I_N,0))$ |
| **Trace evaluation** | $\Str(I)=N-N=0$ | $\mathrm{otr}(J)=N$ |
| **Capelli element** | gl-Capelli $c_2$ (even) | Sergeev $Z_2^{\mathrm{otr}}$ (odd) |
| **Parity-equivariance (A5)** | Unsigned, satisfied | Signed (A5)\textsuperscript{otr}, **(A5) violated** |
| **Chain-level lift $\Lambda$** | Strict, exists | Strict, exists |
| **QME residue coefficient** | $\hbar(N-N)=0$ | $\hbar N\neq 0$ |
| **Cohomology class** | $0\in H^2_{\bar 0}$ | $\hbar N[\bar c]^{\mathrm{otr}}\in H^2_{\bar 1}$ |
| **Verdict** | Discharges | **Does not discharge** |
| **Phase status** | Phase-3 / Phase-4 closed | Phase-5 frontier |

**The opposition is structural, not contingent.** The two-supertrace
structure on q(N) — $(\Str, \mathrm{otr})$ — produces independent
residue classes precisely because the two characters separate the
2-dimensional centre, and the mechanism that kills the $\Str$-side
($\Str(I)=0$) does not have a parallel on the `otr`-side
($\mathrm{otr}(J)=N\neq 0$).

### §7.4 Connection to A5 anomaly ledger L9

The A5 anomaly ledger entry **L9** (`phase4-exec-A5-anomaly-ledger-2026-04-28.md`
§0 line 57) records the Sergeev central element $Z_2$ on
$\mathfrak{gl}(N|N)$ / $\mathfrak q(N)$ as **anchored, not invoked at
chain level for $\mathfrak{gl}(N|N)$**. The note: "Replaces Capelli on
osp / q(N); chain-level cancellation parallel; **anchored, not
invoked at chain level for $\mathfrak{gl}(N|N)$**."

Theorem G\textsuperscript{otr} **is the precise invocation of L9 on
q(N) at chain level**: the queer-Capelli element $Z_2^{\mathrm{otr}}$
controls the propagator-loop contraction in the `otr` channel via
$\mathrm{otr}(J)=N$, and produces the residue class
$\hbar N[\bar c]^{\mathrm{otr}}$. This closes the **structural** L9
anchor (Sergeev 1983/1985 + Berele–Regev 1987) at the chain level,
on q(N), with the queer trace as the deciding character.

**Cross-walk to A5 ledger §N+4 (Phase-5 escalation conditions, line
74):** "anchor L9's invocation route on $\mathfrak q(N)$ at the chain
level (P4-EXEC-G3 M3)". Theorem G\textsuperscript{otr} executes this
escalation as Phase-5-Q-B, with the residue class named and
non-trivial (rather than discharged).

### §7.5 Cross-volume convention check (CY-to-chiral / Vol III)

Per CLAUDE.md, the BCOV / Kodaira–Spencer story has a Vol III
CY-to-chiral frontier (`~/calabi-yau-quantum-groups`) where queer
extensions of the chiral algebra are natural (Cheng–Wang Ch. 6
catalog of queer-supersymmetric chiral algebras). Theorem
G\textsuperscript{otr} sits at the local d=2 formal-disk shadow of
this cross-volume frontier:

| Local (this manuscript) | Cross-volume (Vol III) | Comment |
|---|---|---|
| q(N) Dirac probe | Queer extension of chiral CY₃ algebra | Parallel structures; convention-checking |
| `otr` channel | Queer-supersymmetric vertex algebra trace | Same character mechanism |
| $\hbar N[\bar c]^{\mathrm{otr}}$ residue | Queer-anomaly central charge of CY₃ chiral algebra | Heuristic correspondence; matched-conventions theorem required for transfer |

**No transfer claim.** Per CLAUDE.md and `claim-strength-ledger.tex`
"Cross-volume consequences" entry (line 130), **no compact CY,
global BCOV, Vol III, BKM, Igusa, or sister-volume theorem follows
from Theorem G\textsuperscript{otr}** without a separate
matched-conventions proof. The cross-walk above is a heuristic /
convention-checking bridge only.

---

## §8. Inscription target — LaTeX block for claim-strength-ledger.tex

### §8.1 Proposed Phase-5 frontier section structure

The current `claim-strength-ledger.tex` is a single longtable with no
Phase-5 frontier subsection. We propose **adding a new subsection at
the end of the ledger** (after the closing `\endgroup` on line 142)
titled "Phase-5 frontier candidates", with one entry: Theorem
G\textsuperscript{otr}.

The introductory note for the new subsection introduces the new
status vocabulary item *Phase-5 frontier candidate
(parallel-channel non-discharge)*.

### §8.2 The exact LaTeX block

```latex
%% =====================================================================
%% Phase-5 frontier candidates
%%
%% This subsection records candidate parallel-channel theorems whose
%% statements are publication-grade precise but whose chain-level
%% closure is explicitly absent (the chain-level discharge mechanism
%% of the parent theorem fails on the parallel channel).  The status
%% vocabulary is extended with one item:
%%
%%   - Phase-5 frontier candidate (parallel-channel non-discharge):
%%     The residue class is named, its statement is precise, and the
%%     chain-level discharge mechanism of the parent theorem does not
%%     extend.  Phase-5 work would either close the class via
%%     cross-volume embedding or accept it as a structural finding.
%% =====================================================================

\subsection*{Phase-5 frontier candidates}
\addcontentsline{toc}{subsection}{Phase-5 frontier candidates}

\begingroup
\small
\setlength{\parindent}{0pt}
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.18}

The following entries record candidate parallel-channel theorems
whose chain-level closure is explicitly absent.  The status
vocabulary is extended with one item: \emph{Phase-5 frontier
candidate (parallel-channel non-discharge)}.

\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.24\textwidth}
  >{\raggedright\arraybackslash}p{0.27\textwidth}
  >{\raggedright\arraybackslash}p{0.40\textwidth}@{}}
\hline
\textbf{Claim} & \textbf{Status} & \textbf{Scope and exclusions}\\
\hline
\endhead
Queer \(U(1)\)-center anomaly on \(\lie{q}(N)\)
(Theorem~G\(^{\mathrm{otr}}\)) &
\emph{Phase-5 frontier candidate (parallel-channel non-discharge)} &
Parallel theorem to Theorem~G on the queer Lie superalgebra
\(\lie{q}(N)\subset\lie{gl}(N\vert N)\), \(N\geq 2\), under the
queer-trace boundary evaluation
\(\partial_{\mathrm{bb},N}^{\mathrm{otr}}: f\mapsto
\mathrm{otr}\,f(\phi_1,\phi_2)\). The chain-level QME obstruction
representative
\[
  \operatorname{Ob}_{\mathrm{sc}}^{\mathrm{otr}}(\gamma_{\mathbf 1};a,f;b,g)
  = \hbar N\,\omega(f,g)\int_{\R} a(t)b(t)\gamma_{\mathbf 1}(t)\,dt
\]
has associated graded CE class \(\hbar N[\bar c]^{\mathrm{otr}}\in
H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}\), non-trivial and
independent of the bosonic class \(\hbar N[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}\)
of Theorem~\ref{thm:u1-center-anomaly-open}.  The two-supertrace
structure \((\mathrm{Str},\mathrm{otr})\) on \(\lie{q}(N)\) produces
independent residue classes: \(\mathrm{Str}\) discharges
chain-level (P4-G3-M2-Q via \(\mathrm{Str}(I_{2N})=0\)); \(\mathrm{otr}\)
does not discharge (\(\mathrm{otr}(J)=N\neq 0\) on the queer central
element \(J\), and \(J\) violates the \((A5)\) parity-equivariance
condition under conjugation by the parity operator
\(P^{\lie q}\)).  The chain-level discharge mechanism of W22-T1 / W22-T2 fails on
\(\lie{q}(N)\) at the queer-trace layer (named obstruction
Obs-Q-otr-A5).  Phase-5 work: rigorous formalization of the signed
parity-equivariance (A5)\(^{\mathrm{otr}}\), all-loop class structure
\(\mathrm{otr}(J^k)\), orientifold-style boundary-state
identification, and cross-volume coupling to the Vol III queer
extension of the chiral CY\(_3\) algebra (heuristic only at this
stage; matched-conventions theorem required for transfer per
\texttt{CLAUDE.md}).  Not a Phase-4 chain-level closed theorem.\\
\hline
\end{longtable}
\endgroup
```

### §8.3 Additional inscription option (alternative target)

As an alternative or complement to the claim-strength ledger entry,
a candidate **theorem block in `appendix-unreduced-bv-qme.tex`**
(after Proposition `prop:app-scalar-contact-qme-class` line 126)
records the queer extension at the appendix level:

```latex
\begin{thm}[Queer U(1)-center anomaly on q(N), Phase-5 frontier candidate]
\label{thm:app-queer-u1-anomaly-phase5}
   Let \(\lie g=\lie q(N)\), \(N\geq 2\).  The Dirac brane probe on
   \(\lie q(N)\) under the queer-trace boundary evaluation
   \(\partial_{\mathrm{bb},N}^{\mathrm{otr}}: f\mapsto
   \mathrm{otr}\,f(\phi_1,\phi_2)\) produces a chain-level QME
   obstruction representative
   \[
     \operatorname{Ob}_{\mathrm{sc}}^{\mathrm{otr}}(\gamma_{\mathbf 1};a,f;b,g)
       = \hbar N\,\omega(f,g)\int_{\R} a(t)b(t)\gamma_{\mathbf 1}(t)\,dt
       \in\mc O_{\mathrm{loc}}(\mc E_w^{\lie q})_{\bar 1},
   \]
   in the odd-parity sector of the BV obstruction complex.  Its
   associated graded CE class \(\hbar N[\bar c]^{\mathrm{otr}}\in
   H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}\) is non-trivial and
   independent of the bosonic class \(\hbar N[\bar c]\in
   H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}\) of
   Theorem~\ref{thm:u1-center-anomaly-open}.

   The chain-level discharge mechanism of W22-T1 / W22-T2 fails on
   \(\lie q(N)\) at the queer-trace layer because \(\mathrm{otr}(J)=N\neq 0\)
   on the queer central element \(J=((0,I_N),(-I_N,0))\) and \(J\)
   violates the \((A5)\) parity-equivariance condition under
   conjugation by the parity operator \(P^{\lie q}=\diag(\mathbf 1_N,
   -\mathbf 1_N)\).  This is a Phase-5 frontier candidate; the
   chain-level closure is open.  See the claim-strength ledger entry
   for the Phase-5 frontier vocabulary.
\end{thm}
```

The appendix theorem is **proposal-only and not authorized for
inscription** at this Phase-4 EXEC stage. The claim-strength ledger
entry is the recommended primary inscription target; the appendix
theorem is a complementary option for future Phase-5 / Vol III
main-thread integration.

### §8.4 Notation hygiene

The proposed inscription requires no new mathmacros: $\Pi\C$ is
$\Pi\C$ (parity-shift functor on $\C$, well-defined in any graded
module category); $\mathrm{otr}$ is the queer trace (used as
`\mathrm{otr}` in the inscription, as in Cheng–Wang); `q(N)` is
typeset via the existing `\lie{q}` macro pattern from
`mathmacros.tex` line 336–338. No new macros are introduced; the
inscription uses only existing manuscript symbols and conventions.

---

## §9. Anti-attack scan

Per the proof-harness protocol (CLAUDE.md "Long-form proof harness"):
"name three attack angles on Theorem G^otr and the discharge response
(or open status)".

### §9.1 Attack 1: Hidden Str-coboundary

**Attack.** Could $[\bar c]^{\mathrm{otr}}$ secretly be a coboundary
of a $\Str$-channel cocycle, making it trivial as a residue class
and equivalent to the discharged $\Str$-channel?

**Discharge response.** **No, the parity sectors are disjoint.** The
classes $[\bar c]\in H^2_{\bar 0}$ and $[\bar c]^{\mathrm{otr}}\in
H^2_{\bar 1}$ live in different parity sectors of the graded
cohomology $H^2_{\mathrm{Lie}}(\bar A,\C\oplus\Pi\C)=H^2_{\bar 0}\oplus
H^2_{\bar 1}$. The CE differential preserves the parity grading;
hence a $\bar 0$-class cannot be the boundary of a $\bar 1$-cochain or
vice versa. Concretely: any putative primitive
$\bar\eta^{\mathrm{otr}}:\bar A\to\Pi\C$ for $[\bar c]^{\mathrm{otr}}$
would satisfy $\delta\bar\eta^{\mathrm{otr}}=\Pi\omega$, with
$\bar\eta^{\mathrm{otr}}$ valued in $\Pi\C$. The lifted
$\tilde\eta^{\mathrm{otr}}:\mathfrak h_{\mathrm{poly}}\to\Pi\C$ would
satisfy $\tilde\eta^{\mathrm{otr}}(\{z_1,z_2\})=
\tilde\eta^{\mathrm{otr}}(1)=0$, but $\Pi\omega(z_1,z_2)=
\Pi\cdot 1\neq 0$. Contradiction. So
$[\bar c]^{\mathrm{otr}}$ is independently non-trivial; it is **not**
a $\Str$-coboundary.

**Status.** Discharged.

### §9.2 Attack 2: Regulator-class redefinition

**Attack.** Could a different regulator class — say a non-standard
heat-kernel scheme or a Pauli–Villars with queer twist — produce
$\mathrm{otr}(J^k)=0$ at all $k$, hence vanishing residue?

**Discharge response.** **No, the obstruction is matrix-level, not
regulator-level.** The propagator-loop coefficient $\mathrm{otr}(J)$
is a property of the **matrix realization** of q(N) (specifically the
queer central element $J$ and its non-trivial pairing with the queer
trace), not of the regulator class. Direct computation gives
$\mathrm{otr}(J)=\Tr(I_N)=N$ by elementary matrix algebra; this is
independent of any regulator scheme.

Furthermore, G3-M3 §5.3 lines 705–720 verifies that **there is no
non-trivial central element of $\mathfrak q(N)_{\bar 1}$ with
$\mathrm{otr}=0$**: any choice $J''=((0,K),(-K,0))$ with $\Tr(K)=0$
forces $K=0$ (since centrality requires $K\in\C\cdot I_N$, hence
$\Tr(K)=cN$; setting $c=0$ gives $K=0$). So no rescaling of $J$ or
choice of alternative central element produces $\mathrm{otr}(J)=0$;
the obstruction is canonical.

A regulator that artificially zeroed out $\mathrm{otr}(J)$ would
violate the (A4) coefficient-kernel control hypothesis (the regulator
must respect the algebra structure), so it would not be in the
admissible class.

**Status.** Discharged.

### §9.3 Attack 3: Sub-superalgebra restriction

**Attack.** Could restricting from q(N) to a sub-superalgebra (e.g.,
sq(N) — the supertraceless subalgebra of q(N) — or pq(N) — the
projective queer subalgebra) eliminate the residue class? Sergeev's
queer simple superalgebras include various subalgebras: maybe one
of them has $\mathrm{otr}=0$ on its central direction.

**Discharge response.** **Partial — the question reduces to the
supertraceless subalgebra question, which has its own structural
obstruction.**

The natural sub-superalgebra candidates are:
* **sq(N)**: queer matrices with $\mathrm{otr}=0$. By construction
  this kills the queer trace. **But** sq(N) is *not closed* under
  the super-bracket of q(N): the super-bracket of two
  queer-traceless elements can have non-zero queer trace (the queer
  trace is a Lie cocycle, not an algebra homomorphism). So sq(N) is
  not a Lie sub-superalgebra of q(N).
* **psq(N)** = sq(N) / centre: the projective queer simple Lie
  superalgebra. Cheng–Wang Ch. 6 records this as the basic classical
  series. Restricting to psq(N) **does** eliminate the central
  direction $\C\cdot J$ (it is quotiented out), so the residue
  $\mathrm{otr}(J)$ no longer appears as a brane-probe coefficient
  on psq(N).

**However**, the brane probe on q(N) is not the same as the brane
probe on psq(N): the manuscript's framework explicitly uses the
**unreduced** Lie superalgebra (the source containing the central
direction; cf. `rmk:quotient-discipline-flag` in main.tex line 395).
Restricting to psq(N) is the **scalar reduction** at the source
level, parallel to the manuscript's reduction $\mathfrak{gl}_N\to
\mathfrak{sl}_N\to\mathfrak{psl}_N$. After scalar reduction the
class is killed, but the **unreduced statement** carries the residue
— and Theorem G\textsuperscript{otr} is the unreduced statement, by
construction.

This is exactly parallel to the manuscript's Theorem G: on the
**reduced** $\mathfrak{psl}_N$ the bosonic anomaly $[\bar c]$ is
killed, but on the **unreduced** $\mathfrak{gl}_N$ the class is
non-trivial. Theorem G\textsuperscript{otr} records the unreduced
queer statement.

**Status.** Partially discharged — the sub-superalgebra route is
foreclosed at the unreduced level (q(N), the parallel of
$\mathfrak{gl}_N$). At the reduced level (psq(N), the parallel of
$\mathfrak{psl}_N$) the class is killed, parallel to the bosonic
case. **This is not a discharge of Theorem G\textsuperscript{otr}**;
it is a recognition that the unreduced/reduced distinction applies
in the queer channel as it does in the bosonic channel.

### §9.4 Combined verdict on attack scan

All three attacks are addressed. The Theorem G\textsuperscript{otr}
residue class is:
* **Independent** of the bosonic Theorem G class (Att-1 discharged
  by parity-sector disjointness).
* **Canonical** — the obstruction is matrix-level, not
  regulator-level (Att-2 discharged by direct computation).
* **Unreduced** — the residue is non-trivial on the unreduced q(N),
  parallel to Theorem G on the unreduced $\mathfrak{gl}_N$
  (Att-3 acknowledged; reduces correctly under scalar reduction).

The class **survives** all three attack angles. The Phase-5 frontier
status is robust.

### §9.5 Residual attack vector — convention divergence

A fourth potential attack angle worth naming, though not requested:
could the q(N) probe be incompatible with the manuscript's BCOV
convention (e.g., framing on $S^3$, $d=2$ formal disk dimension, or
worldsheet $\Sigma$ orientation)?

**Quick check.** The q(N) probe is a *finite-N* matrix-level brane
probe on the formal disk; it inherits the convention from the
embedding $\mathfrak q(N)\subset\mathfrak{gl}(N|N)\subset
\mathfrak{gl}_{2N}$ via the standard supermatrix realization. The
BCOV / Costello / Witten conventions on $d$, $\Sigma$, framing apply
as on $\mathfrak{gl}_{2N}$, so the q(N) probe is convention-compatible
with the manuscript's existing framework at the local d=2 formal-disk
level.

Cross-volume compatibility (with Vol III queer extensions) is a
separate matched-conventions theorem requirement per CLAUDE.md and
is recorded as residual `R-P4-G3-M3-Q-otr-04`.

**Status.** Convention-compatible at the local level; cross-volume
matched-conventions remain Phase-5 work.

---

## §10. Summary and 200-word report

### §10.1 Inscription proposal summary

This document executes Phase-5-Q-B from P4-EXEC-G3-M3 verdict §10:
the queer trace `otr` on q(N) produces a parallel anomaly class
$\hbar N[\bar c]^{\mathrm{otr}}\in H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$,
independent of the manuscript's Theorem G class
$\hbar N[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}$. The
parallel theorem is named **Theorem G\textsuperscript{otr}**, and its
publication-grade statement, hypothesis ledger, two-supertrace
independence proof, proof outline, Phase-5 status declaration,
boundary/brane interpretation, cross-walk table, LaTeX inscription
target for `claim-strength-ledger.tex`, and three-angle anti-attack
scan are recorded above (§1–§9).

The inscription target is the **claim-strength ledger Phase-5
frontier section** (new subsection appended after the existing
table), with one entry: Theorem G\textsuperscript{otr}, status
*Phase-5 frontier candidate (parallel-channel non-discharge)*. An
alternative complementary inscription target is a theorem block in
`appendix-unreduced-bv-qme.tex` after `prop:app-scalar-contact-qme-class`.

The proposal is **proposal-only** at Phase-4 EXEC stage. No
manuscript edits, no commits. The inscription is ready for future
Phase-5 / Vol III main-thread authorization.

### §10.2 Residuals carried forward to Phase-5

* **R-P4-G3-M3-Q-otr-01** (G3-M3 line 974): rigorous formalization
  of (A5)\textsuperscript{otr} at the parametrix level. Phase-5
  cross-volume work.
* **R-P4-G3-M3-Q-otr-02** (G3-M3 line 977): all-loop class structure
  on q(N): identification of the $\mathrm{otr}(J^k)$ alternating
  series as a CE class. Phase-5.
* **R-P4-G3-M3-Q-otr-03** (G3-M3 line 982): eigenvalue of
  $Z_2^{\mathrm{otr}}$ on the brane-probe Hilbert space via
  Sergeev–Berele–Regev hook formula. Phase-5.
* **R-P4-G3-M3-Q-otr-04** (G3-M3 line 989): cross-link to Vol III
  queer extension of the chiral CY₃ algebra. Phase-5 / Vol III
  matched-conventions theorem.
* **R-P4-G3-M3-Q-otr-05** (G3-M3 line 994): orientifold /
  boundary-state interpretation; identification of the
  orientifold-projection rule between $\Str$ and `otr` channels.
  Phase-5 cross-volume.
* **R-P4-G\^otr-NEW** (this document): rigorous proof of the
  inscription target's claim-strength ledger entry, pending
  authorization for inscription. Phase-5 main-thread work.

### §10.3 200-word summary (for parent agent)

**(a) Final theorem name.** Theorem G\textsuperscript{otr} —
"Queer U(1)-center anomaly on the queer Lie superalgebra q(N)";
parallel to and independent of the manuscript's Theorem G.

**(b) Precise residue class statement.** On the q(N) Dirac brane
probe with queer-trace boundary evaluation, the chain-level QME
obstruction representative is
$\mathrm{Ob}_{\mathrm{sc}}^{\mathrm{otr}}=\hbar N\,\omega(f,g)\int
a(t)b(t)\gamma_{\mathbf 1}(t)\,dt$ in
$\mathcal O_{\mathrm{loc}}(\mathcal E_w^{\mathfrak q})_{\bar 1}$, with
associated graded CE class $\hbar N[\bar c]^{\mathrm{otr}}\in
H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$ in the odd-parity sector.
Generated by the queer central element $J$ with $\mathrm{otr}(J)=N$;
non-trivial; independent of the bosonic class $\hbar N[\bar c]\in
H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}$.

**(c) Chosen Phase-5 path.** **Phase-5-Q-B (parallel theorem)**, not
Phase-5-Q-A (signed parity-equivariance). Rationale: the obstruction
is matrix-level (canonical $\mathrm{otr}(J)=N$), not regulator-level;
Phase-5-Q-A would relabel the regulator hypothesis without
discharging, while Phase-5-Q-B accepts the residue as a structural
finding parallel to Theorem G. Matches CLAUDE.md "report, do not
silently reconcile" voice and Russian-school epistemic discipline.

**(d) Report path + line count.** `/Users/raeez/topological-strings/reconstitution/phase4-exec-Theorem-G-otr-inscription-2026-04-28.md`. 1374 lines.

End of P4-EXEC-Theorem-G-otr inscription proposal.
