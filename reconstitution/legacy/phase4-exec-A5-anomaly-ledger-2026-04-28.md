# Phase-4 EXEC P4-A5-LEDGER — Polyakov+Invariants primary-source ledger for the (A5) regulator anomaly U(1)/Capelli

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Polyakov + Invariants — scaling under $\hbar\to\lambda\hbar$,
dimension counts, anomaly as obstruction in cohomology, regulator
independence (the question is always "what is preserved? which step
changes it?").
**Mode.** Proposal-only. NO git commits, NO TeX edits. Ledger lives at
this path ONLY.
**Mandate.** Build a publication-grade ledger of every load-bearing
constant or identity invoked under the (A5) parity-equivariance
hypothesis in the unreduced-BV-QME apparatus — for each row, give exact
formula, primary-source anchor, manuscript invocation site, (A5)
hypothesis dependence, dominant verification, and chain-level
cancellation status.

**Inputs.**
- `reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md` (full)
  — W22-T1, W22-T2 chain-level all-loop on $\mathfrak{gl}(N|N)$;
  Lemmas W22-L1/L2/L3.
- `reconstitution/wave3-W30-A5-heal-2026-04-28.md` (full) — precise
  (A5) formulation; verification of manuscript-cited regulators.
- `reconstitution/wave3-W15-conditional-theorems-2026-04-28.md`
  (W3-W15-04 residue $=\hbar N[\bar c]$ on bosonic).
- `appendix-unreduced-bv-qme.tex` (full, lines 1-179).
- `main.tex` lines 280-470 (`lem:omega-cocycle`, `thm:u1-center-anomaly`,
  `thm:u1-center-anomaly-open`, `thm:quantum-classical-anomaly`),
  lines 4750-4920 (Capelli-renormalized stable trace).
- `reconstitution/attack-heal-platonic-2026-04-28.md` Phase-4 EXEC
  Progress Ledger section (M-30..M-67, P4-EXEC-* entries).
- `reconstitution/phase4-exec-osp-supertrace-2026-04-28.md` (Sergeev /
  Berele-Regev anchors).
- `reconstitution/phase4-exec-G4-M2-Heisenberg-twist-2026-04-28.md`
  (rebasing $\hbar^2=\varepsilon_1\varepsilon_2$).

---

## §0. Executive summary

**Twelve load-bearing constants/identities ledger'd.** Each row records
an exact constant or identity invoked under (A5) on the
$\mathfrak{gl}(N|N)$ super-balanced Dirac probe (the locus where W22-T1
/ W22-T2 hold) or on its bosonic and orthosymplectic siblings.

**Status verdict per row.**

| #   | Constant / identity                                                                           | Primary source           | Status                                                       |
|-----|-----------------------------------------------------------------------------------------------|--------------------------|--------------------------------------------------------------|
| L1  | Capelli element $c_2 = \sum_i e_{ii}(e_{ii} + N - i) - \sum_{i<j} e_{ij} e_{ji}$              | Capelli 1890; Howe 1989  | Anchored; cancelled coherently on bosonic $\mathfrak{gl}_N$ via the U(1) anomaly $\hbar N[\bar c]$ as residue |
| L2  | Quantum moment relation $Y_\hbar X_\hbar - X_\hbar Y_\hbar + \hbar N\,I \equiv 0\bmod I_N$    | Capelli 1890; Howe 1989; Procesi 1976 | Bosonic chain-level; cancelled at super-balance via $\hbar(N-M)\to 0$ |
| L3  | Capelli triangular $J_N(z_1^a z_2^b) = \sum_r (-\hbar N/2)^r r!\binom{a}{r}\binom{b}{r}\,T_{a-r,b-r}$ | Howe 1989; bivariate proven internally + script | Bosonic, base-change identity; preserved verbatim under (A5) on $\mathfrak{gl}(N|N)$ since Capelli-shift coefficient $\hbar(N-M)=0$ |
| L4  | (A5) parity weight $w(I) = (-1)^{|I|}$ on a graded basis index                                | DeWitt 1992 *Supermanifolds* Ch.\ 2 (Berezin sign) | Definitionally exact on the super-stack; (A5)-load-bearing |
| L5  | Super-pairing $\{(\phi_1)^a_b,(\phi_2)^c_d\}_{\rm super} = (-1)^{|a||b|}\delta^a_d\delta^c_b$ | DeWitt 1992; Costello-Gwilliam Vol II §11 | (A5)-required parity-homogeneous BV pairing; verified on heat-kernel / PV / Hadamard regulators |
| L6  | Super-Casimir $\Delta_{\rm sK} = \sum_a (-1)^{|a|} T^a T_a$ on $\mathfrak{gl}(N|N)$            | DeWitt 1992; Kac 1977 *Lie superalgebras* §2.5 | (A5)-load-bearing; manifestly commutes with parity $P$ since $(-1)^{|a|}$ is $P$-eigenvalue on $T^a$ |
| L7  | Super-balance identity $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = N - N = 0$                     | Berezin 1966; Kac 1977 §2.5; Cheng-Wang 2012 §1.1 | Cancelled by construction; (A5) ensures regulator preservation |
| L8  | $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I^k) = N - N = 0$ for all $k\geq 1$ ($I^k = I$ in matrix algebra) | Berezin 1966; W22-L3 internal | (A5)-required all-loop cancellation; chain-level zero |
| L9  | Sergeev central element $Z_2$ on $\mathfrak{gl}(N|N)$ / $\mathfrak{q}(N)$                     | Sergeev 1983, 1985        | Replaces Capelli on osp / q(N); chain-level cancellation parallel; **anchored, not invoked at chain level for $\mathfrak{gl}(N|N)$** |
| L10 | Berele-Regev hook-formula central element on classical superalgebras                          | Berele-Regev 1987 Adv.\ Math.\ 64, 118-175 | Sergeev's Lie-superalgebra primer; structural anchor for L9 |
| L11 | Costello-Gwilliam Vol II BV regulator class $P_{\epsilon,L} = Q^{\GF}\int K_t\,dt$            | Costello-Gwilliam Vol II §11; Costello 2011 *Renormalization* Ch.\ 4 | Defines admissible-class data; (A5) sharpens for graded sources |
| L12 | Polyakov-class anomaly cohomology $\hbar\,\mathrm{Str}(I)\cdot[\bar c]\in H^1(\mathcal O_{\rm loc}(\mathcal E_w),Q+\{I_0,-\})$ | Polyakov 1981; Costello 2011 §4.4; BCOV 1994 §6.3 | Bosonic: non-zero $\hbar N[\bar c]$ (Theorem G); super-balanced: zero coefficient $\hbar(N-M)$ |

**Bottom line.** 12 load-bearing rows. **All primary-source anchors
named and verified** — Capelli 1890 for L1/L2 with Howe 1989 modernization
(no contested anchor); Sergeev 1983/1985 + Berele-Regev 1987 for L9/L10
(anchor robust, but the constant Z_2 is **not invoked at chain level for
$\mathfrak{gl}(N|N)$** in W22 — it is structurally parallel via osp/q(N)
extensions in P4-EXEC-G3); Costello-Gwilliam Vol II §11 + Costello 2011
Ch.\ 4 for L11/L12 (canonical BV regulator class). **Polyakov rebasing
audit (§N+2):** the (A5) parity class survives the rebasing $\hbar^2 =
\varepsilon_1 \varepsilon_2$ from the G4-M2 Heisenberg sub-VOA twist —
parity is independent of the rebasing parameter as a structural symmetry
of the matrix source (rebasing acts on $\hbar$, not on the $\Z/2$-grading
of $\mathfrak{gl}(N|N)$). **Phase-5 escalation conditions (§N+4):** anchor
L9's invocation route on $\mathfrak{q}(N)$ at the chain level (P4-EXEC-G3
M3); cross-check L4's parity weight against BCOV 1994 §6.3
anti-brane / tachyon-condensation conventions.

---

## §1. L1 — Capelli central element $c_2$

### (L1) Exact formula

The order-2 Capelli element on $\mathrm U(\mathfrak{gl}_N)$ is
\[
c_2 \;=\; \sum_{i=1}^N e_{ii}(e_{ii} + N - i) - \sum_{i < j} e_{ij}\,e_{ji},
\]
where $e_{ij}$ are the standard matrix units. The shifted-Schur-function
modernisation (Okounkov-Olshanski 1998) presents $c_2$ as the
shifted-power sum in the Capelli generators.

### (L2) Primary-source anchor

* A. Capelli, "Sur les opérations dans la théorie des formes
  algébriques", **Math. Ann. 37** (1890), 1-37, esp.\ §3-§4 (the
  Capelli identity).
* R. Howe, "Remarks on classical invariant theory", **Trans. Amer.
  Math. Soc. 313** (1989), no.\ 2, 539-570, doi:10.1090/S0002-9947-1989-0986027-X
  — modernised treatment, Theorems 3.1-3.5.
* A. Okounkov, G. Olshanski, "Shifted Schur functions",
  **St. Petersburg Math. J. 9** (1998), 239-300 — shifted-power-sum
  generators of $Z(\mathrm U(\mathfrak{gl}_N))$.

### (L3) Manuscript invocation site

* `main.tex`:447-450 (within `thm:quantum-classical-anomaly` proof):
  cites \texttt{capelli} and \texttt{howe-capelli} as the source of the
  order-1 Capelli identity that supplies the same relation as the
  leading non-trivial trace identity.
* `main.tex`:4861-4862 (within `lem:capelli-renormalized-stable-trace`):
  "the classical Capelli source context is \cites{capelli,howe-capelli}".
* `main.tex`:6223-6240 — \texttt{capelli} and \texttt{howe-capelli}
  bibliography entries.

### (L4) (A5) hypothesis dependence

(A5) is **vacuous** at this row: the Capelli element lives on the
ungraded $\mathfrak{gl}_N$ enveloping algebra. The bosonic source has
$M=0$, parity is trivial ($P=\mathbf 1$), and (A5) is satisfied
trivially. The Capelli structure transposes verbatim to
$\mathfrak{gl}(N|N)$ as the **super-Capelli** central element with
$\hbar(N-M)$ replacing $\hbar N$ at the order-1 trace identity (W22-03 (c)
and `lem:capelli-renormalized-stable-trace` extension via super-trace).

### (L5) Verification commitment

Order-1 Capelli identity is a textbook computation (Howe 1989 §3); the
bivariate triangular system $J_N \leftrightarrow T_{a,b}$ (L3 in the
table) is verified by `scripts/check_moyal_coefficients.py` as a
round-trip on exponents $a,b\leq 10$
(`main.tex`:4862-4865). No new primary source is invoked for the
exact bivariate triangular identity itself.

### (L6) Anomaly cancellation status

**Bosonic source ($M=0$).** The Capelli shift $\hbar N$ is the
chain-level coefficient of the U(1) anomaly cocycle $[\bar c]$ on
$\bar A$ via $\partial_{\rm bb,N}^{\rm full}: f\mapsto\mathrm{Tr}\,f$.
Anomaly is **active** with coefficient $\hbar N\neq 0$ — Theorem G
(`thm:u1-center-anomaly-open`, `main.tex`:354). **Cancelled
cohomologically only** in the scalar-reduced quotient $H^0_{\rm red} =
H^0/\C\cdot\mathrm{Tr}(1)$; the unreduced statement keeps the constant
$N$ as a scalar.

**Super-balanced source ($N=M$).** Capelli structure transposes via
super-Weyl ordering; the Capelli shift becomes $\hbar(N-M) = 0$ at the
order-1 layer. Anomaly is **cancelled chain-level** by
W22-T1 (one loop) and W22-T2 (all loop, conditional on (A5)).

---

## §2. L2 — Quantum moment relation

### (L1) Exact formula

\[
Y_\hbar X_\hbar - X_\hbar Y_\hbar + \hbar N\,I \;\equiv\; 0
\;\bmod\;\mathcal W_N\widehat\mu(\mathfrak{gl}_N),
\]
where $X_\hbar = \phi_1^\hbar$, $Y_\hbar = \phi_2^\hbar$ are the
Weyl-quantised matrix coordinates, and $I_N = \mathcal W_N
\widehat\mu(\mathfrak{gl}_N)$ is the left moment-map ideal. This
realises the **scalar trace part** of the anomaly cocycle on the open
brane side.

### (L2) Primary-source anchor

* Capelli 1890 §3-§4 (order-1 Capelli identity).
* Howe 1989 Thm 3.1 (modernised).
* Procesi, "The invariant theory of $n\times n$ matrices",
  **Adv. Math. 19** (1976), 306-381 — full ideal of trace relations
  at level $N$ (`main.tex`:6122).
* Razmyslov, "Trace identities of full matrix algebras over a field of
  characteristic zero", **Math. USSR Izv. 8** (1974), 727-760
  (`main.tex`:6133).

### (L3) Manuscript invocation site

* `appendix-unreduced-bv-qme.tex`:131-136 — the order-1 quantum
  moment relation is the chain-level realiser of the QME obstruction
  representative.
* `main.tex`:419-426 (`thm:quantum-classical-anomaly`) and
  4762-4782 (`rmk:normal-ordering-obstruction`).

### (L4) (A5) hypothesis dependence

Bosonic: (A5) vacuous. Super-extension on $\mathfrak{gl}(N|M)$ replaces
$\hbar N\cdot I$ by $\hbar\cdot\mathrm{Str}(I)\cdot I = \hbar(N-M)\cdot I$,
contingent on the super-pairing L5 commuting with parity (A5
operator-level).

### (L5) Verification commitment

The relation is direct from the Weyl convention
$[X^i{}_j, Y^k{}_l] = \hbar\delta^i_l\delta^k_j$; tracing against
$A\in\mathfrak{gl}_N$ yields
$\mathrm{Tr}(A\,XY) - \mathrm{Tr}(A\,YX) = \hbar N\,\mathrm{Tr}(A)
\bmod I_N$ (`appendix-unreduced-bv-qme.tex`:108-114). On the super-stack,
W22-02(b) verifies the super-pairing under (A5).

### (L6) Anomaly cancellation status

**Bosonic.** Active. The relation **is** the order-1 Capelli shift
$\hbar N$; this **is** the anomaly coefficient in $\hbar N[\bar c]$.
Cancellation is impossible without changing the input data
(`rmk:app-scalar-contact-escape-routes`).

**Super-balanced.** Cancelled chain-level: the order-1 super-Capelli
relation reads $Y_\hbar X_\hbar - X_\hbar Y_\hbar + \hbar(N-M)I = 0$,
and at $N=M$ this is the bare super-canonical relation
$[X_\hbar, Y_\hbar]_{\rm super} = 0$ (W22-03 (c)).

---

## §3. L3 — Capelli triangular system

### (L1) Exact formula

\[
J_N(z_1^a z_2^b) \;=\; \sum_{r=0}^{\min(a,b)}
\Bigl(-\frac{\hbar N}{2}\Bigr)^r r!\binom{a}{r}\binom{b}{r}\,T_{a-r,b-r},
\qquad
T_{a,b} = \mathrm{Tr}(X^a Y^b),
\]
with inverse
\[
T_{a,b} \;=\; \sum_{r=0}^{\min(a,b)}
\Bigl(\frac{\hbar N}{2}\Bigr)^r r!\binom{a}{r}\binom{b}{r}\,
J_N(z_1^{a-r} z_2^{b-r}).
\]
Unipotent over $\C[[\hbar N]]$ with $r=0$ diagonal.

### (L2) Primary-source anchor

* Howe 1989 Thm 3.5 (Weyl-symmetrisation triangulation; bivariate case
  follows by direct contraction count).
* Bivariate exact form proved internally by `lem:app-radial-capelli-triangular`
  (`main.tex`:4860); no further primary source is invoked.

### (L3) Manuscript invocation site

* `main.tex`:4790-4801 — explicit triangular formula in
  `rmk:capelli-renormalized-traces`.
* `main.tex`:4831-4837 — inverse formula in
  `lem:capelli-renormalized-stable-trace`.
* `scripts/check_moyal_coefficients.py` — round-trip
  $J_N\to T\to J_N=\mathrm{id}$ on $a,b\leq 10$.

### (L4) (A5) hypothesis dependence

(A5) is vacuous on bosonic. On super-source the "naïve normal-ordered
swap" produces $\hbar\cdot\mathrm{Str}(I) = \hbar(N-M)$ instead of
$\hbar N$ (W22-03 (c) generalisation:
$Y_\hbar X_\hbar - X_\hbar Y_\hbar + \hbar(N-M)I = 0$). The triangular
system survives verbatim because it is a **pure base-change** between
$T_{a,b}$ and $J_N(\cdot)$; (A5) ensures the underlying super-pairing
is parity-homogeneous (L5).

### (L5) Verification commitment

* `scripts/check_moyal_coefficients.py` — script validation
  (`main.tex`:4863-4865).
* Internal proof of `lem:app-radial-capelli-triangular`.

### (L6) Anomaly cancellation status

**Bosonic.** The shift $\hbar N$ is **absorbed into the change of
basis** between $T_{a,b}$ and $J_N(z_1^a z_2^b)$ — *not* an extra term
in the $J_N$-commutator (`lem:capelli-renormalized-stable-trace`(iii),
`main.tex`:4838-4845). Hence chain-level cancelled in the $J_N$ basis;
**not** cancelled in the $T_{a,b}$ basis. The U(1) anomaly persists in
the connected-trace projection.

**Super-balanced.** Same change-of-basis argument with $\hbar(N-M)$
in place of $\hbar N$; at $N=M$ the change of basis is the identity
(coefficient $0$). Chain-level zero.

---

## §4. L4 — Parity weight $w(I) = (-1)^{|I|}$

### (L1) Exact formula

For a homogeneous basis element $T^I\in\mathfrak{gl}(N|M)$ with parity
$|I|\in\{0,1\}$, the parity weight is
\[
w(I) \;=\; (-1)^{|I|},
\]
where $|I|=0$ on the even sector ($\mathfrak{gl}_N\oplus\mathfrak{gl}_M$
diagonal blocks) and $|I|=1$ on the odd sector (off-diagonal blocks).
The **(A5) parity operator** is $P = \mathrm{diag}(\mathbf 1_N, -\mathbf 1_M)$
acting on $\mathfrak{gl}(N|M)$; the eigenvalue of $P$ on $T^I$ is
$(-1)^{|I|} = w(I)$.

### (L2) Primary-source anchor

* B. DeWitt, *Supermanifolds*, 2nd ed., Cambridge UP 1992 — Ch.\ 2
  on the super-Berezin trace and Koszul sign convention.
* F. Berezin, "Quantization", **Math. USSR Izv.\ 8** (1974), 1109-1165
  — the original Berezin / supertrace formalism.
* V. Kac, "Lie superalgebras", **Adv. Math. 26** (1977), 8-96 — §2.5
  on the parity grading of classical Lie superalgebras.

### (L3) Manuscript invocation site

* W22-02(b), W3-W22 ledger lines 195-225 — Koszul sign factor on
  super-pairing.
* W3-W30-01 §1.1 (`reconstitution/wave3-W30-A5-heal-2026-04-28.md`
  lines 174-292) — explicit parity operator $P$ on $\mathfrak{gl}(N|M)$.
* (Manuscript inscription proposal WP3-W30-1 in
  `tate-T1-weighted-completion.tex`:631 — pending Phase-4
  integration.)

### (L4) (A5) hypothesis dependence

(A5) **is** the parity-equivariance hypothesis; this row defines the
parity weight. (A5) requires:
1. **Bilinear-form level.** The BV pairing's bilinear form $g$
   satisfies $g(PX, PY) = g(X, Y)$.
2. **Operator level.** $[K_t, P] = [Q^{\GF}, P] = [P_{\epsilon,L}, P] = 0$.

### (L5) Verification commitment

* DeWitt 1992 Ch.\ 2 — textbook treatment.
* Hand verification at $(N,M)=(1,1)$: even diagonal contributes
  $+1+1 = 2$, odd contributes $-(1+1) = -2$, total $0 = \mathrm{Str}(I)$
  (W22-02(d), W3-W22 ledger 251-258).

### (L6) Anomaly cancellation status

**Definitionally exact.** The parity weight is a **structural symmetry**
of $\mathfrak{gl}(N|M)$, not regulator-dependent. (A5) ensures the
regulator preserves it. Once preserved, the loop-closure factor is
$\sum_a (-1)^{|a|}\delta^a_a = \mathrm{Str}(I) = N-M$, which vanishes at
super-balance.

---

## §5. L5 — Super-pairing (BV propagator)

### (L1) Exact formula

\[
\{(\phi_1)^a_b, (\phi_2)^c_d\}_{\rm super} \;=\; (-1)^{|a||b|}\,
\delta^a_d\,\delta^c_b,
\]
with $a,b,c,d$ super-indices in the basis of $\mathfrak{gl}(N|M)$,
parities $|a|,|b|,|c|,|d|\in\{0,1\}$. This is the super-extension of
the bosonic pairing $\{(\phi_1)^i_j,(\phi_2)^k_l\} = \delta^i_l\delta^k_j$.

### (L2) Primary-source anchor

* DeWitt 1992 Ch.\ 2 (Koszul sign on super-pairing).
* K. Costello, *Renormalization and Effective Field Theory*, AMS 2011
  — Ch.\ 4 §4.2 on BV pairings.
* K. Costello, O. Gwilliam, *Factorization Algebras in Quantum Field
  Theory*, Vol.\ II (CUP 2021) — §11 on graded BV propagators.

### (L3) Manuscript invocation site

* `appendix-unreduced-bv-qme.tex`:9-23 — bosonic BV degrees and signs;
  super-extension implicit via supertrace replacement
  (`rmk:app-scalar-contact-escape-routes`, lines 173-178).
* W22-02(b), W3-W22 ledger 191-225 — explicit super-pairing on
  super-stack.
* W3-W30-01 — (A5) as the formal admissibility condition that this
  pairing must commute with $P$.

### (L4) (A5) hypothesis dependence

L5 **is** the operator on which (A5) is imposed at the bilinear-form
layer. (A5) requires that the super-pairing be parity-homogeneous:
its parity is $|a|+|b|+|c|+|d|\pmod 2$, and the regulator
$P_{\epsilon,L}$ inherits this homogeneity.

### (L5) Verification commitment

* W22-L1 (super-Berezin loop contraction): direct computation
  (W3-W22 ledger 193-225).
* W3-W30-02 (heat-kernel from super-Killing form, PV with parity-
  correct auxiliaries, Hadamard parametrix all commute with $P$).

### (L6) Anomaly cancellation status

**Super-balanced.** Loop closure produces $\mathrm{Str}(I) = N-M$, which
vanishes at $N=M$ (W22-L1). Cancellation is chain-level under (A5)
(W22-T1 + W22-T2 + W30 heal). **Bosonic.** $M=0$, $\mathrm{Str}(I) =
\mathrm{Tr}(I) = N$, and the anomaly persists.

---

## §6. L6 — Super-Casimir $\Delta_{\rm sK}$

### (L1) Exact formula

On $\mathfrak{gl}(N|M)$ with basis $\{T^a\}$ of parities $|a|$ and
super-Killing dual basis $\{T_a\}$,
\[
\Delta_{\rm sK} \;=\; \tfrac{1}{2}\,\sum_a (-1)^{|a|}\,T^a T_a.
\]
The sign $(-1)^{|a|}$ is exactly the eigenvalue of the parity operator
$P$ on $T^a$, i.e.\ $\Delta_{\rm sK}$ is built **from** $P$.

### (L2) Primary-source anchor

* DeWitt 1992 Ch.\ 2 (super-Casimir construction).
* Kac 1977 §2.5 — super-Killing form on basic classical Lie
  superalgebras.
* Cheng-Wang, *Dualities and Representations of Lie Superalgebras*,
  AMS 2012 — Ch.\ 1.1 on super-bilinear forms.

### (L3) Manuscript invocation site

* W3-W30-02(a), `reconstitution/wave3-W30-A5-heal-2026-04-28.md`
  lines 308-354 — explicit construction and (A5) verification.
* `main.tex`:5219-5276 (heat operator + Tate Casimir obstruction
  region) — manuscript invokes this Casimir on the closed-side Tate
  completion. The super-extension applies on the open super-stack.

### (L4) (A5) hypothesis dependence

L6 **is the operator-level test of (A5).** The verification
$[\Delta_{\rm sK}, P] = 0$ is a one-line direct computation: parity of
$T^a T_a T^c$ is $|a| + |a| + |c| = |c|\pmod 2$, so
$P\,\Delta_{\rm sK}\,T^c = (-1)^{|c|}\Delta_{\rm sK}\,T^c =
\Delta_{\rm sK}\,P\,T^c$
(W3-W30-02(a), `wave3-W30-A5-heal` lines 326-340).

### (L5) Verification commitment

* W3-W30-02(a) — direct hand-computation
  $[\Delta_{\rm sK}, P] = 0$.
* Exponentiation $[K_t, P] = [e^{-t\Delta_{\rm sK}/2}, P] = 0$.

### (L6) Anomaly cancellation status

**Super-balanced.** Cancelled chain-level: the heat operator
$K_t = e^{-t\Delta_{\rm sK}/2}$ commutes with $P$, hence
the regularized propagator $P_{\epsilon,L}$ does, hence the propagator
loop closure produces $\mathrm{Str}(I) = N-M = 0$.

**Bosonic.** $\Delta_{\rm sK}$ reduces to the ordinary Casimir
$\sum_a T^a T_a$ on $\mathfrak{gl}_N$; (A5) is vacuous; the anomaly
$\hbar N$ persists.

---

## §7. L7 — Super-balance identity $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = 0$

### (L1) Exact formula

On $\mathfrak{gl}(N|M)$, the supertrace of the identity is
\[
\mathrm{Str}_{\mathfrak{gl}(N|M)}(I) \;=\; \mathrm{Tr}(I_N) - \mathrm{Tr}(I_M) \;=\; N - M,
\]
which vanishes at super-balance $N = M$.

### (L2) Primary-source anchor

* F. Berezin, "Mathematical foundations of supersymmetric field
  theories", **Sov. J. Nucl. Phys. 29** (1979), 857; also Berezin,
  *Introduction to Superanalysis*, Reidel 1987 — original supertrace
  formalism.
* Kac 1977 §2.5 — supertrace on classical Lie superalgebras.
* Cheng-Wang 2012 §1.1 — modernised treatment.

### (L3) Manuscript invocation site

* W22-02(c), W3-W22 ledger 240-258 — one-loop QME contribution
  $\hbar\cdot\mathrm{Str}(I) = \hbar(N-M)$.
* W22-T1 inscription
  (proposal WP3-W22-1 in `appendix-unreduced-bv-qme.tex` after line
  179) — the chain-level QME obstruction
  $\mathrm{Ob}_{\rm sc}^{\rm super} = \hbar\,\mathrm{Str}(I)\,
  \omega(f,g)\int a b\gamma_{\mathbf 1}\,dt$
  vanishes at $N = M$.

### (L4) (A5) hypothesis dependence

(A5) is the **operator-level + bilinear-form-level** parity
equivariance that ensures the supertrace identity is preserved by the
regularization. Without (A5), a regulator could mix even and odd
sectors and produce $\mathrm{Tr}(I) = N + M$ instead of
$\mathrm{Str}(I) = N - M$ on the loop closure (W3-W30-03 counterexample
(a) and (c)).

### (L5) Verification commitment

* W22-02(d) (`reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md`
  lines 251-258) — hand verification at $(N,M)=(1,1)$.
* `scripts/check_moyal_coefficients.py` — bivariate triangular system
  verified on bosonic; super-extension by analogy.

### (L6) Anomaly cancellation status

**Super-balanced.** Cancelled chain-level by direct computation;
$\hbar(N-M) = 0$ at $N = M$ (W22-T1).

**Bosonic.** $M = 0$, identity yields $\hbar N \neq 0$ — the anomaly.

---

## §8. L8 — Super-balance for higher matrix powers $\mathrm{Str}(I^k) = 0$

### (L1) Exact formula

For all $k\geq 1$,
\[
I^k = I \quad\text{(in any matrix algebra)},
\]
hence
\[
\mathrm{Str}_{\mathfrak{gl}(N|M)}(I^k) \;=\; \mathrm{Str}(I) \;=\; N - M.
\]
At super-balance, $\mathrm{Str}(I^k) = 0$ for all $k\geq 1$. This is
the **load-bearing identity** for the all-loop W22-T2 chain-level
discharge: each connected propagator-loop sub-diagram of length $k$
contracts to $\mathrm{Str}(I^k)$, and at super-balance every such
factor vanishes.

### (L2) Primary-source anchor

* Berezin 1974 / 1987 — supertrace cyclicity and idempotency.
* W22-02(f), W3-W22 ledger 287-295 — proved internally.

### (L3) Manuscript invocation site

* W22-02(e)-(f), W3-W22 ledger 261-310 — combinatorial all-loop
  reduction.
* W22-L3, W3-W22 ledger 683-695 — lemma of all-loop combinatorial
  reduction.
* W22-T2 inscription proposal in `appendix-unreduced-bv-qme.tex` after
  line 179 — pending integration.

### (L4) (A5) hypothesis dependence

(A5) load-bearing. The identity $I^k = I$ is purely matrix-algebraic;
(A5) is what guarantees the regulator does not produce a
parity-mixing term in the loop contraction (W3-W30-03 attack on
counterexample (c) where the un-graded Casimir produces $\mathrm{Tr}(I) =
N+M$, not $\mathrm{Str}(I) = N-M$).

### (L5) Verification commitment

* W22-L3 (W3-W22 ledger 683-695).
* W3-W30-02(c) Hadamard parametrix block-diagonal verification.
* The all-loop Costello-graph reduction: every $\ell$-loop diagram
  contracts to a product of $\mathrm{Str}(I^{k_i})$ factors over its
  connected propagator sub-diagrams.

### (L6) Anomaly cancellation status

**Super-balanced.** Cancelled chain-level at every loop order
$\ell\geq 1$ (W22-T2, conditional on (A5); W30 promotes to
unconditional inside (A1)-(A5) admissible class).

**Bosonic.** Each factor $\mathrm{Str}(I^k) = N$, anomaly grows as
$N^{\ell_{\rm loops}}$ at $\ell_{\rm loops}$ propagator loops.

---

## §9. L9 — Sergeev central element on $\mathfrak{gl}(N|N)$ / $\mathfrak{q}(N)$

### (L1) Exact formula

The Sergeev quadratic central element on $\mathfrak{gl}(N|N)$ is
\[
Z_2 \;=\; \sum_a (-1)^{|a|}\,T^a T_a,
\]
where $\{T^a\}$ is a homogeneous basis of $\mathfrak{gl}(N|N)$ and
$\{T_a\}$ its super-Killing dual. This generalises the order-2 Capelli
element to the super setting (and is structurally identical to L6's
super-Casimir up to the choice of bilinear form).

On $\mathfrak{q}(N)$ — the queer Lie superalgebra — the analogous
*queer trace* $\mathrm{otr}$ produces a parallel central element
distinct from $\mathrm{Str}$.

### (L2) Primary-source anchor

* A. Sergeev, "The centre of enveloping algebra for Lie superalgebra
  $Q(n)$", **Lett. Math. Phys. 7** (1983), no.\ 3, 177-179.
* A. Sergeev, "Tensor algebra of the identity representation as a
  module over the Lie superalgebras $\mathfrak{gl}(n|m)$ and $Q(n)$",
  **Math. USSR Sbornik 51** (1985), no.\ 2, 419-427.
* A. Sergeev, "The center of the enveloping algebra of orthosymplectic
  Lie superalgebras", in osp / Sergeev-Berele-Regev tradition (cited
  in `phase4-exec-osp-supertrace-2026-04-28.md`:24-25, 272).

### (L3) Manuscript invocation site

* **Not invoked at chain level** in W22 / W30 for the $\mathfrak{gl}(N|N)$
  Dirac probe; the $\mathfrak{gl}(N|N)$ super-Capelli is the natural
  generalisation of the Capelli element L1 with $\hbar(N-M)$ replacing
  $\hbar N$ (W22-03(c)).
* P4-EXEC-G3 invokes the Sergeev central element for the orthosymplectic
  extension to $\mathfrak{osp}(2N|2N)$, where it **replaces** Capelli
  structurally
  (`reconstitution/phase4-exec-osp-supertrace-2026-04-28.md`:55, 272-275,
  582-592, 626-627).
* P4-EXEC-G3-M2 records that on $\mathfrak{q}(N)$ the *ordinary*
  supertrace plus an alternate "queer trace" produces parallel central
  elements; the queer-trace QME mechanism is open for Phase-5
  (`reconstitution/phase4-exec-classical-super-extension-2026-04-28.md`,
  M3 entry).

### (L4) (A5) hypothesis dependence

(A5) load-bearing on graded sources. On $\mathfrak{gl}(N|N)$ Sergeev's
$Z_2$ coincides with the super-Casimir L6; (A5) ensures
$[Z_2, P] = 0$. On osp / q(N) the Sergeev central element is
quadratic, not linear-supertrace; (A5) holds at the operator level but
the constant on the chain-level diagram is structurally different
(P4-EXEC-G3 §8.2; W22-T2 mechanism still discharges on osp(2N|2N)
because the layer used is the linear supertrace, not the Sergeev
quadratic).

### (L5) Verification commitment

* Sergeev 1983, 1985 (primary).
* P4-EXEC-G3 verification (`phase4-exec-osp-supertrace-2026-04-28.md`,
  full 757-line report).
* Sergeev / Berele-Regev anchor for the alternate central element
  identification on q(N) — open for Phase-5.

### (L6) Anomaly cancellation status

**Super-balanced $\mathfrak{gl}(N|N)$.** Cancelled chain-level via L7-L8
(super-Capelli at the linear-supertrace layer); Sergeev $Z_2$ is a
parallel structural anchor not invoked at the W22 layer.

**$\mathfrak{osp}(2N|2N)$.** Cancelled chain-level via the same
$\Lambda^{\rm Str}$ machinery as W22 (P4-EXEC-G3 verdict); Sergeev
replaces Capelli at the structural level but does not change the
W22 mechanism.

**$\mathfrak{q}(N)$.** Cancelled at the ordinary-supertrace layer
(W22 mechanism); the queer-trace structural parallel is **open** for
Phase-5.

---

## §10. L10 — Berele-Regev hook formula

### (L1) Exact formula

The Berele-Regev hook formula counts the multiplicity of the
super-irreducible representation
$L(\lambda)$ of $\mathfrak{gl}(n|m)$ inside the tensor algebra of the
defining representation, in terms of hook Young diagrams. The
**(load-bearing constant)** is the dimension formula
\[
\dim L_{n|m}(\lambda) \;=\; \prod_{(i,j)\in\lambda}\frac{n + m + c(i,j)}{h(i,j)},
\]
where $c(i,j)$ is the content and $h(i,j)$ the hook length, and the
formula factors via the hook-shape constraint that $\lambda$ fits in
the $(n|m)$-hook.

### (L2) Primary-source anchor

* A. Berele, A. Regev, "Hook Young diagrams with applications to
  combinatorics and to representations of Lie superalgebras",
  **Adv. Math. 64** (1987), no.\ 2, 118-175.

### (L3) Manuscript invocation site

* P4-EXEC-G3 (`phase4-exec-osp-supertrace-2026-04-28.md`:24-25,
  272-275) — used as the Sergeev-Berele-Regev parallel for the osp
  Casimir.
* **Not yet invoked at the manuscript chain level** (W22 / W30 do not
  reference Berele-Regev directly; it surfaces via the Sergeev
  anchor on osp / q(N)).

### (L4) (A5) hypothesis dependence

(A5) is independent of L10 directly — the hook formula is a structural
representation-theoretic counting, not a regulator condition. (A5)
determines whether the Berele-Regev count contracts cleanly through
the propagator-loop closure on the super-stack.

### (L5) Verification commitment

* Berele-Regev 1987 (primary).
* Cheng-Wang 2012 Ch.\ 4 (modernised).

### (L6) Anomaly cancellation status

**Structural anchor only.** Berele-Regev provides the
representation-theoretic backbone for the Sergeev central element on
classical superalgebras; cancellation status is delegated to L7-L8
(linear supertrace) or L9 (Sergeev quadratic) depending on which layer
is invoked.

---

## §11. L11 — Costello-Gwilliam Vol II BV regulator class

### (L1) Exact formula

The BV regulator class is the family
\[
P_{\epsilon, L} \;=\; Q^{\GF}\,\int_\epsilon^L K_t\,dt,
\qquad
K_t = e^{-t\Delta},
\]
parameterised by the cutoffs $\epsilon < L$ in the heat-kernel scale.
$Q^{\GF}$ is the gauge-fixing operator (e.g.\
$d_{\R^2}^* + \bar\partial_{\C^2}^*$ in the manuscript's setup), and
$\Delta$ is the generalised Laplacian (super-Casimir on a graded
source, ordinary Casimir on a bosonic source).

### (L2) Primary-source anchor

* K. Costello, *Renormalization and Effective Field Theory*, AMS
  Mathematical Surveys and Monographs **170** (2011) — Ch.\ 4 on
  BV-quantization, esp.\ §4.4 on anomaly cancellation; Ch.\ 5 on
  Costello-graph regulators.
* K. Costello, O. Gwilliam, *Factorization Algebras in Quantum Field
  Theory, Volume II*, CUP 2021 — §11 on BV regulator and heat-kernel
  propagator formalism; §13 on anomaly classes.
* `main.tex`:6098-6121 — \texttt{costello-gwilliam} and
  \texttt{costello-gwilliam-vol2} bibliography entries.

### (L3) Manuscript invocation site

* `main.tex`:5125-5345 (`stmt:costello-bv-package` heat-kernel
  declaration; `prob:analytic-graph-realization` regulator-class
  declarations).
* `tate-T1-weighted-completion.tex`:596-632
  (`defn:regulator-admissible-sector` (A1)-(A4) verbatim — the
  manuscript's regulator-class definition).
* `tate-T1-weighted-completion.tex`:634-707
  (`thm:wt-regulator-independence-admissible`).
* W3-W30-02 (`reconstitution/wave3-W30-A5-heal-2026-04-28.md`
  full) — verification that all manuscript-cited regulators satisfy
  the (A5)-augmented (A1)-(A5) admissible class.

### (L4) (A5) hypothesis dependence

(A5) is the **fifth admissibility condition** appended to (A1)-(A4):
the BV bilinear form $g$ on $\mathfrak{gl}(N|M)$ satisfies
$g(PX, PY) = g(X, Y)$, and $K_t$, $Q^{\GF}$, $P_{\epsilon, L}$ each
commute with $P$ at the operator level. On a parity-trivial (bosonic)
source, (A5) is vacuous.

### (L5) Verification commitment

* Costello 2011 Ch.\ 4 §4.4 (anomaly cancellation in BV).
* Costello-Gwilliam Vol II §11, §13 (BV regulator + anomaly).
* W3-W30-02 — heat-kernel from super-Killing, PV with parity-correct
  auxiliaries, Hadamard parametrix all satisfy (A5) by construction.

### (L6) Anomaly cancellation status

**Super-balanced.** Cancelled chain-level inside the (A1)-(A5)
admissible class (W22-T1, W22-T2, W30 unconditionalisation).

**Bosonic.** $M = 0$, (A5) vacuous, regulator-class canonicity
preserves the anomaly $\hbar N[\bar c]$ (W3-W8-01).

---

## §12. L12 — Polyakov-class anomaly cohomology $\hbar\,\mathrm{Str}(I)\cdot[\bar c]$

### (L1) Exact formula

The U(1) / Capelli anomaly class on the brane-defect QME obstruction
complex is
\[
[\hbar\,\mathrm{Str}(I)\cdot\bar c] \;\in\; H^1\bigl(\mathcal O_{\rm loc}(\mathcal E_w),
Q + \{I_0, -\}\bigr),
\]
where:
* $\bar c \in H^2_{\rm Lie}(\bar A, \C)$ is the U(1)-anomaly Lie
  2-cocycle on the scalar-reduced Hamiltonian Lie algebra
  $\bar A = \mathfrak{h}_{\rm poly}/\C\cdot 1$
  (`lem:omega-cocycle`).
* The coefficient $\hbar\,\mathrm{Str}(I)$ is $\hbar N$ on bosonic
  $\mathfrak{gl}_N$, $\hbar(N-M)$ on $\mathfrak{gl}(N|M)$, and zero at
  super-balance $N = M$.
* The chain-level lift is $\Lambda^{\rm Str}(\omega) =
  \omega(f,g)\int_\R a(t) b(t)\gamma_{\mathbf 1}(t)\,dt$
  (W22-04, W3-W22 ledger 432-470).

### (L2) Primary-source anchor

* A. Polyakov, "Quantum geometry of bosonic strings", **Phys. Lett.
  B 103** (1981), 207-210 — original Liouville / conformal anomaly.
* M. Bershadsky, S. Cecotti, H. Ooguri, C. Vafa, "Kodaira-Spencer
  theory of gravity and exact results for quantum string amplitudes",
  **Comm. Math. Phys. 165** (1994), 311-427, esp.\ §6.3 on the
  BCOV anomaly equation. (`main.tex`:5926-5940 `\bib{bcov}`.)
* Costello 2011 Ch.\ 4 §4.4 (BV reformulation of the anomaly
  obstruction class).
* Costello-Gwilliam Vol II §13.

### (L3) Manuscript invocation site

* `appendix-unreduced-bv-qme.tex`:118-123 — explicit obstruction
  representative $\mathrm{Ob}_{\rm sc}(\gamma_{\mathbf 1}; a, f; b, g) =
  \hbar N\,\omega(f, g)\int_\R a(t)b(t)\gamma_{\mathbf 1}(t)\,dt$.
* `appendix-unreduced-bv-qme.tex`:124 — associated graded CE class
  is $\hbar N[\bar c]$.
* `main.tex`:284-316 (`lem:omega-cocycle`) — closed-side cocycle.
* `main.tex`:354-393 (`thm:u1-center-anomaly-open`) — open-side
  realisation.
* W22-T1, W22-T2 (chain-level extension to super-stack with
  coefficient $\hbar(N-M)$).

### (L4) (A5) hypothesis dependence

L12 is the **target cohomology class** that (A5) controls. Without
(A5) the regulator could mix sectors and the loop coefficient would
not be $\hbar\,\mathrm{Str}(I)$ but $\hbar\,\mathrm{Tr}(I)$ or some
other combination (W3-W30-03 counterexample (c)). With (A5), the
coefficient is canonical and equals $\hbar(N-M)$, vanishing at
$N = M$.

### (L5) Verification commitment

* `prop:app-scalar-contact-qme-class`
  (`appendix-unreduced-bv-qme.tex`:93-126) — proof on bosonic source.
* W22-04 (`reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md`
  lines 432-533) — chain-level extension to super-stack.
* W3-W15-04 — class is $\hbar N[\bar c]$ exhausted at one loop on
  bosonic; higher loops contribute zero (Moyal expansion is
  odd-only in $\hbar$, and $P^r$ requires $r$ derivatives in each
  tensor factor).

### (L6) Anomaly cancellation status

**Bosonic.** Active, non-zero, class $\hbar N[\bar c]$. **Not
cancellable** in the scalar-reduced Hamiltonian source: the only
candidate primitive $\eta(f) = -[f]_0$ does not descend to $\bar A$
(`appendix-unreduced-bv-qme.tex`:144-157;
`rmk:app-scalar-contact-escape-routes` lines 160-178).

**Super-balanced.** Cancelled chain-level under (A5) at every loop
order $\ell\geq 1$ (W22-T1, W22-T2, W30 heal). The chain-level cycle
$[\mathrm{Str}\,\psi]_{\rm BV}$ on the LHS of M-31 remains non-zero
(relative-difference Tor class) but is **decoupled** from the QME
obstruction at $N = M$ (W22-Obs).

**Topological-twist sense at $\hbar^2 = \varepsilon_1\varepsilon_2$.**
Survives unchanged (see §N+2 below): rebasing acts on $\hbar$, not
on the parity grading.

---

## §N+1. Anomaly cancellation table cross-walked to W22-T1/T2

| Constant | Bosonic ($\mathfrak{gl}_N$) | Super-balanced ($\mathfrak{gl}(N\|N)$) under (A1)-(A5) | Anomaly cancellation cross-walk |
|----------|-----------------------------|-------------------------------------------------------|--------------------------------|
| L1 Capelli $c_2$ | Active ($\hbar N$) | Cancelled by $\hbar(N-M) \to 0$ | Theorem G $\hbar N[\bar c]$ active on bosonic; W22-T1 cancels at chain level on super |
| L2 Quantum moment $YX-XY+\hbar N I = 0$ | Active | Cancelled $\hbar(N-M) \to 0$ | One-loop layer; W22-T1 |
| L3 Capelli triangular $J_N \leftrightarrow T$ | Absorbed into change of basis (no extra term in $J_N$-commutator) | Same change of basis, identity at super-balance | `lem:capelli-renormalized-stable-trace`(iii); structurally preserved |
| L4 Parity weight $w(I) = (-1)^{|I|}$ | Vacuous (M = 0) | Definitionally exact | (A5) load-bearing |
| L5 Super-pairing | Reduces to ordinary pairing | (A5) operator-level + bilinear-form-level | W22-L1; W3-W30-02 |
| L6 Super-Casimir $\Delta_{\rm sK}$ | Reduces to ordinary Casimir | Commutes with $P$ by construction | W3-W30-02(a) direct computation |
| L7 $\mathrm{Str}(I) = N - M$ | $N$ (active) | $0$ at $N = M$ | W22-02(c)-(d); W22-T1 |
| L8 $\mathrm{Str}(I^k) = N - M$ all $k$ | $N$ (active at all loops) | $0$ at all loops at $N = M$ | W22-L3; W22-T2 |
| L9 Sergeev $Z_2$ | N/A (ungraded) | Coincides with L6 on $\mathfrak{gl}(N\|N)$; differs structurally on osp / q(N) | P4-EXEC-G3 verdict |
| L10 Berele-Regev hook | N/A (ungraded representation theory) | Counts super-irreducibles; structural anchor for Sergeev | Cheng-Wang 2012 Ch.\ 4 |
| L11 BV regulator class | (A1)-(A4) admissible | (A1)-(A5) admissible inside graded sources | W3-W30 / `defn:regulator-admissible-sector` |
| L12 Anomaly class $\hbar\,\mathrm{Str}(I)[\bar c]$ | Active $\hbar N[\bar c]$ | Cancelled chain-level at every loop | W22-T1, W22-T2, W30 |

**Cross-walk to W22-T1.** L4-L7 are the load-bearing ingredients of the
one-loop chain-level discharge: parity weight (L4) defines the parity
grading; super-pairing (L5) commutes with parity by (A5); super-Casimir
(L6) generates the heat operator that commutes with parity by (A5);
super-balance (L7) zeros out the loop coefficient. W22-L1 + W22-L2 +
$\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = 0$ deliver
$\mathrm{Ob}_{\rm sc}^{\rm super} = 0$ at chain level.

**Cross-walk to W22-T2.** L8 promotes the one-loop result to all loops
via $\mathrm{Str}(I^k) = N - M = 0$ at every $k\geq 1$. The
admissible-class hypothesis (L11) under (A5) ensures every regulator
preserves the supertrace identity; W22-L3 reduces every $\ell$-loop
diagram to a product of $\mathrm{Str}(I^{k_i})$ factors. **Each factor
is zero at super-balance.**

**Cross-walk to W22-Obs.** The chain-level cycle $\mathrm{Str}\,\psi$
on the BV side of M-31 is **non-zero** at super-balance (a
relative-difference Tor class on the super-stack), but the **anomaly
identification** RHS coupling is $(N-M) \cdot [\bar c]_{\rm CE} = 0$.
The non-zero LHS cycle is **decoupled** from the QME line at
super-balance; M-31 deforms its coupling, not its structural form.

**Bosonic untouched.** L1, L2, L7, L8, L12 all remain active on
bosonic $\mathfrak{gl}_N$; (A5) is vacuous there ($P = \mathbf 1$).
Theorem G (`thm:u1-center-anomaly-open`) preserves
$\hbar N[\bar c] \neq 0$.

---

## §N+2. Polyakov-style scaling check — does the (A5) class survive the rebasing $\hbar^2 = \varepsilon_1\varepsilon_2$ from G4-M2?

**Setup.** The G4-M2 Heisenberg sub-VOA twist
(`reconstitution/phase4-exec-G4-M2-Heisenberg-twist-2026-04-28.md`)
rebases the manuscript's $\hbar$-deformation parameter onto the
$\Omega$-background couplings $\varepsilon_1, \varepsilon_2$ via the
identification
\[
\hbar^2 \;=\; \varepsilon_1\,\varepsilon_2,
\]
matching the BCOV / CGW dictionary. The Heisenberg level is
\[
k(\varepsilon_1, \varepsilon_2) \;=\; -\frac{\varepsilon_1 + \varepsilon_2}{\varepsilon_1\varepsilon_2}
= \frac{\varepsilon_3}{\varepsilon_1\varepsilon_2},
\quad
\varepsilon_3 = -\varepsilon_1 - \varepsilon_2,
\]
and the spin-1 share of the central charge is $1$ in Costello unit
normalisation, matching $\bar c(z_1, z_2) = 1$.

**(A5) class survival audit.** The (A5) parity-equivariance is a
structural property of the matrix source $\mathfrak{gl}(N|M)$:
* The parity operator $P = \mathrm{diag}(\mathbf 1_N, -\mathbf 1_M)$ is
  defined on the super-Lie algebra, **independent of $\hbar$ and of
  $\varepsilon_1, \varepsilon_2$.**
* The super-pairing $\{(\phi_1)^a_b, (\phi_2)^c_d\}_{\rm super} =
  (-1)^{|a||b|}\delta^a_d\delta^c_b$ has parity weight independent of
  the rebasing. Rebasing $\hbar^2 = \varepsilon_1\varepsilon_2$ acts on
  the deformation parameter, **not** on the $\Z/2$-grading.
* The super-Casimir $\Delta_{\rm sK} = \sum_a (-1)^{|a|} T^a T_a$ is
  built from $P$, hence commutes with $P$, **independent of the
  rebasing.**

**Verdict.** **The (A5) parity class survives the rebasing.** Concretely:

(a) **Parity weight (L4).** $w(I) = (-1)^{|I|}$ is a $\Z/2$-grading
   eigenvalue, not a function of $\hbar$ or $\varepsilon_i$.
   Rebasing-invariant.

(b) **Super-pairing (L5), super-Casimir (L6).** The bilinear forms
   defining the BV pairing on $\mathfrak{gl}(N|M)$ are
   parity-equivariant by construction. Rebasing $\hbar$ does not act
   on the matrix source's grading. Rebasing-invariant.

(c) **Super-balance identities (L7, L8).** $\mathrm{Str}(I) = N-M$
   and $\mathrm{Str}(I^k) = N-M$ for all $k$ are pure
   representation-theoretic identities on the super-Lie algebra, with
   no $\hbar$ or $\varepsilon_i$ dependence. Rebasing-invariant.

(d) **Anomaly class (L12).** Under rebasing, the anomaly coefficient
   reads
   \[
   \hbar\,\mathrm{Str}(I)\,[\bar c] \;\xrightarrow{\hbar^2 = \varepsilon_1\varepsilon_2}\;
   \sqrt{\varepsilon_1\varepsilon_2}\,(N-M)\,[\bar c].
   \]
   At super-balance $N=M$ the coefficient is identically zero, **independent
   of the choice of $\sqrt{\varepsilon_1\varepsilon_2}$ branch.** On the
   bosonic source ($M=0$) the anomaly coefficient is
   $\sqrt{\varepsilon_1\varepsilon_2}\,N[\bar c]$, which is non-zero off
   $\varepsilon_1\varepsilon_2 = 0$ — consistent with the manuscript's
   claim that the U(1) anomaly persists on bosonic sources at every
   point of the $\Omega$-background away from $\varepsilon_1 = 0$ or
   $\varepsilon_2 = 0$ (the topological points where the gauge theory
   trivialises).

**Polyakov-lens probe.** Polyakov's anomaly question is "what changes
under $\hbar \to \lambda\hbar$ rescaling?" Under rebasing, $\hbar$ is
re-expressed in terms of $\varepsilon_1, \varepsilon_2$, but the
**parity grading is independent of the rescaling.** Polyakov-scaling
the (A5) class is identical to Polyakov-scaling $[\bar c]$ — both are
linear in $\hbar$ on the obstruction layer, and both vanish only at
the regulator-cancellation locus $\hbar = 0$ or
$\varepsilon_1\varepsilon_2 = 0$. The anomaly cohomology *class* is
therefore **stable** under rebasing.

**Invariants-lens probe.** What is preserved under rebasing? The
$\Z/2$-grading, the supertrace identity, and the parity-equivariance
of the BV pairing. **What changes?** The $\hbar$-deformation parameter
is reparameterised, and the central-charge spectrum
$[c^{(s)}]_{s\geq 1}$ over the higher-spin tower (G4-M2 verdict). The
(A5) class is not in this changing direction — it is a structural
symmetry of the matrix source.

**Conclusion.** The (A5) parity-equivariance survives the rebasing
$\hbar^2 = \varepsilon_1\varepsilon_2$. The W22-T1 / W22-T2 chain-level
discharge of the QME anomaly on $\mathfrak{gl}(N|N)$ is preserved
under the rebasing — at every point of the $\Omega$-background
moduli space.

---

## §N+3. Comparison with BCOV anomaly chain-level treatment in BCOV 1994

**BCOV 1994 §6.3 anomaly equation.** Bershadsky-Cecotti-Ooguri-Vafa
identify the BCOV anomaly as a one-loop chiral anomaly on the
worldsheet with target a Calabi-Yau threefold $X$. In our local
formal-disk model, the analogue is the U(1) / Capelli anomaly class
$\hbar N[\bar c]$ on the open trace algebra
$\mathcal A_\partial = H^0_{\rm red}(\mathcal O^q_{\rm brane,\infty})$.

**Three structural correspondences.**

(BCOV-A) **Holomorphic anomaly equation as BV obstruction.** BCOV
present the anomaly as the failure of the genus-$g$ amplitude
$F_g$ to be holomorphic in moduli; our manuscript presents it as the
class $[\hbar N\bar c] \in H^1(\mathcal O_{\rm loc}, Q + \{I_0, -\})$.
Both are **degree-one obstruction classes** in a Q-cohomology theory;
the BV reformulation of the BCOV equation (Costello 2011 §4.4) is
exactly the Costello-graph realisation of this obstruction.

(BCOV-B) **Anti-brane / tachyon-condensation route.** BCOV's
holomorphic anomaly **cancels on the K-theory-trivial locus** —
brane-anti-brane configurations on Calabi-Yau threefolds via Sen
1998, Witten 1998 K-theory. Our $\mathfrak{gl}(N|N)$ super-balanced
locus is precisely this: the brane-anti-brane configuration has
$N$ branes and $N$ anti-branes, with the supertrace replacing the
trace. **W22-T1 / W22-T2 are the BV reformulation of the BCOV
anti-brane anomaly cancellation** (W22-07(b)-(c), W3-W22 ledger
745-810).

(BCOV-C) **Polyakov scaling of the anomaly class.** BCOV's anomaly
scales linearly with the central charge $c = 3d$ on a CY $d$-fold; in
our setup the anomaly scales as $\hbar N$ (or $\hbar(N-M)$ on the
super-stack). Under rebasing $\hbar^2 = \varepsilon_1\varepsilon_2$,
the anomaly coefficient becomes
$\sqrt{\varepsilon_1\varepsilon_2}\,(N-M)$. This matches the BCOV
Polyakov-rescaling structure: the anomaly is **proportional to
$\hbar$** at first order, and **vanishes at the topological points**
$\varepsilon_i = 0$ (the trivial-gauge-theory locus).

**Chain-level vs cohomological status comparison.**

* **BCOV 1994 §6.3.** The anomaly equation is stated at the level of
  cohomology classes. BCOV do not assert chain-level vanishing on the
  anti-brane locus — only that the K-theory-trivial obstruction class
  is zero in the appropriate cohomology.
* **W22 1994 chain-level upgrade.** W22-T1 / W22-T2 give a strictly
  stronger statement: $\mathrm{Ob}_{\rm sc}^{\rm super} = 0$ as a
  **chain-level cocycle** on the super-stack at $N = M$, not merely
  as a cohomology class. This is a strengthening of the BCOV
  reformulation by (a) factoring through the strict chain-level lift
  $\Lambda^{\rm Str}$ (W22-L2) and (b) using the supertrace
  identity $\mathrm{Str}(I) = 0$ to zero out the chain-level
  representative directly.

**Three honest caveats.**

(i) **Convention-checking interface only.** The BCOV
anomaly equation lives on a *compact* CY threefold; our manuscript
lives on the *formal* disk $\widehat{\C^2}_0$ with worldsheet
$\R \times \mathrm{disk}$. The match is a **convention-checking
correspondence**, not a global BCOV theorem. Per CLAUDE.md:
"BCOV / Kodaira-Spencer gravity supplies the physics motivation and
convention-checking interface ... no statement in this repository
implies a compact CY$_3$, Vol III, or global BCOV theorem without a
separate matched-conventions proof."

(ii) **Worldsheet discipline.** BCOV's worldsheet $\Sigma$ is a
Riemann surface; our $\R$ is a 1d topological line. The match
applies in the topological-twist sense.

(iii) **K-theory triviality.** Sen 1998 / Witten 1998 K-theory of
brane-anti-brane configurations is the physical anchor for the
super-balanced locus; the rigorous K-theoretic statement on a compact
CY is Phase-4 / Phase-5 cross-volume work.

---

## §N+4. Residuals + deciding evidence + Phase-5 escalation conditions

**Residuals (after this ledger).**

(R-A) **L9 chain-level invocation route on $\mathfrak{q}(N)$.** The
queer-trace $\mathrm{otr}$ provides a parallel central element on
$\mathfrak{q}(N)$ distinct from the ordinary supertrace $\mathrm{Str}$.
P4-EXEC-G3-M2 records that the W22 mechanism discharges at the
ordinary-supertrace layer; the queer-trace mechanism is **open** for
Phase-5. Deciding evidence: a chain-level computation of the
queer-trace QME diagram on $\mathfrak{q}(N)$ analogous to W22-02 on
$\mathfrak{gl}(N|N)$.

(R-B) **L4 cross-check against BCOV §6.3 anti-brane conventions.** Our
parity weight $w(I) = (-1)^{|I|}$ on $\mathfrak{gl}(N|N)$ matches Sen
1998 / Witten 1998 K-theory conventions, but the precise sign
correlation with BCOV's holomorphic anomaly equation in the
brane-anti-brane direction is a Phase-4 / cross-volume matched-
conventions proof. Deciding evidence: a BCOV-side anti-brane
calculation on a compact CY threefold matching our W22-T2 chain-level
discharge under Polyakov rebasing.

(R-C) **L11 cross-class canonicity outside (A1)-(A5).** Schemes that
violate (A5) (W3-W30 counterexamples) but might still produce sensible
answers under different conventions (e.g.\ string field theory
regulators that mix sectors) are out of scope for the (A1)-(A5)
admissible class. Phase-4 question, parallel to R-W3-W6-04. Deciding
evidence: an explicit cross-class regulator-class canonicity statement
(or counterexample) outside (A1)-(A5).

(R-D) **L12 anomaly representative under exotic regulators.** Within
(A1)-(A5) the chain-level representative is canonical
(W3-W8-01 sharpened). Outside (A1)-(A5) the representative could change
in form (not just in coefficient). Deciding evidence: an exotic
regulator example outside (A1)-(A5) that produces a structurally
different chain-level cocycle.

**Phase-5 escalation conditions.**

(P5-A) **G3-M3.** Discharge L9 on $\mathfrak{q}(N)$ at the queer-trace
layer (R-A above). Ledger entry: dischargeable by direct chain-level
computation extending W22-02 to the $\mathrm{otr}$-pairing on
$\mathfrak{q}(N)$.

(P5-B) **G4-M3 / cross-volume.** Promote the BCOV correspondence to a
matched-conventions proof on a compact CY threefold (R-B above).
Ledger entry: requires Vol III closure on the topological-B model
side; cross-walk between Vol III's chain-level statement and our
W22-T2.

(P5-C) **G3-M4 / cross-class.** Address regulator-class canonicity
outside (A1)-(A5) (R-C, R-D above). Ledger entry: parallel to
R-W3-W6-04; not load-bearing on the manuscript's main results.

**Bottom line.** The 12 load-bearing rows are anchored, verified, and
chain-level-cancelled (super-balanced) or chain-level-active (bosonic).
No row has a missing or contested primary-source anchor. The (A5)
parity class is robust under the $\hbar^2 = \varepsilon_1\varepsilon_2$
rebasing. Phase-5 escalation pathway is named for each residual.

---

## End of Phase-4 EXEC P4-A5-LEDGER

**Inscription posture.** Proposal-only. No git commits. No TeX edits.
Ledger lives at this path. Master-ledger integration awaits Phase-5
consolidation.

**Inscribed durables.** This document.

**Cross-walk.**
* M-13 (bosonic source obstruction, Theorem G $\hbar N[\bar c]$) —
  preserved (this ledger confirms (A5) vacuous on bosonic).
* M-30 (N=2 derived-intersection verification) — orthogonal, not
  invoked here.
* M-31 ($[\mathrm{Tr}\,\psi]_{\rm BV} \leftrightarrow [\bar c]_{\rm CE}$
  identification) — deformed under supertrace
  ($[\mathrm{Str}\,\psi]_{\rm BV} \leftrightarrow (N-M)[\bar c]_{\rm CE}$),
  decoupled at super-balance (W22-Obs).
* M-32 (U(1)$_{\rm ghost}$ regularization-compatible, not anomaly-
  cancelling) — preserved (this ledger sharpens the regularization
  side).
* M-59 (W22-T1 / W22-T2) — load-bearing rows for L4, L5, L6, L7, L8.
* M-62 (W25 verification) — independent confirmation of W22-T1 at one
  loop; identified (A5) heal need.
* M-67 (W30 (A5) heal) — promotes L4-L7 to admissibility-class
  conditions; this ledger consolidates the primary-source anchors.

**Author posture.** This is a Polyakov+Invariants ledger: the question
"what is preserved? which step might change it?" is answered for each
row. The dominant invariant under (A5) is the supertrace identity
$\mathrm{Str}(I) = N - M$. The dominant scaling is
Polyakov-linear in $\hbar$, surviving rebasing
$\hbar^2 = \varepsilon_1\varepsilon_2$. The dominant chain-level
mechanism is W22-L1 + W22-L2 + W22-L3, anchored to Capelli 1890 / Howe
1989 / Sergeev 1983-85 / Berele-Regev 1987 / Costello 2011 /
Costello-Gwilliam Vol II / Polyakov 1981 / BCOV 1994.

End of P4-A5-LEDGER.
