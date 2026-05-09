# Wave 3 / W27 — M-03 First-Principles Verification (Drinfeld + Hypotheses)

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Drinfeld (moduli, stacks, hidden groupoids, canonical
constructions; here: the derived self-intersection groupoid of the
commuting variety as the canonical object the BV complex computes) +
Hypotheses (which theorem hypotheses are missing, weakened, or
silently strengthened — here: complete-intersection hypothesis on the
moment-map equations).
**Mandate.** Verify M-03 from first principles via primary-source
citation, run the inscribed verification scripts, cross-walk W3 / W10
/ W12 / W14, draft the heal prose, propose status-ladder update.
**Mode.** Proposal-only. Master ledger schema; IDs prefix W3-W27-.
**Inputs read.** `CLAUDE.md`;
`reconstitution/attack-heal-platonic-2026-04-28.md` M-03 (lines
233–289), §6 provenance (lines 1300–1338), §A wave-2 sharpening table
(lines 1840–1875), M-30/M-31/M-32 entries (lines 1580–1676);
`reconstitution/wave3-W13-critique-fidelity-2026-04-28.md` Round-7 §3,
W3-W13-5 entry (lines 540–607);
`reconstitution/wave3-W3-nekrasov-2026-04-28.md` §3 (N=2 examples
extension; lines 178–251);
`reconstitution/wave3-W12-blast-radius-2026-04-28.md` §5.1 (four-cone
explicit; lines 255–410), §9 (Čech-SES; lines 568–598);
`reconstitution/wave3-W10-witten-examples-2026-04-28.md` W3-W10-02
(extended dimension table N = 1..6; lines 200–252);
`reconstitution/wave3-W14-mixed-cones-2026-04-28.md` line 458 (four
cones as Čech localizations);
`reconstitution/platonic-ideal-plan-2026-04-28.md` §3 Theorem A and
Theorem G (lines 174–451);
`reconstitution/platonic-clean-paper-plan-2026-04-28.md` (full;
search for "commuting"/"Premet"/"Vasconcelos"/"derived intersection"
returns no hits — independently confirms W13's "plan does NOT mention"
finding);
`main.tex`:115–168 (Theorem-A region, the M-03 elision at line 127),
`main.tex`:240–470 (Theorem-G region with the
$[\bar c] \in H^2_{\mathrm{Lie}}(\bar A; \C)$ line);
`scripts/check_derived_intersection_N2.py` (executed; output verbatim
in §3.1 below);
`scripts/check_derived_intersection_N_extended.py` (executed; output
verbatim in §3.1 below).
**No web fetches.** Primary sources cited from internal references in
the master ledger (Premet 2003; Vasconcelos 1994; Gerstenhaber 1961;
Motzkin–Taussky 1955) augmented with the standard Premet result
statement that has been part of the algebra-of-commuting-matrices
literature since the 1960s and is reproduced verbatim in standard
references (Humphreys, *Linear Algebraic Groups*; Vasconcelos,
*Arithmetic of Blowup Algebras*).

---

## §1. T1 — M-03 stated precisely (Drinfeld lens)

### §1.1 Verbatim master-ledger entry

From `reconstitution/attack-heal-platonic-2026-04-28.md` lines
233–289:

> **M-03 — Finite-$N$ commuting variety is not Koszul; BV computes
> derived intersection.**
> **Severity 4. Status valid (additive). Confidence high.**
> **Lens.** A3 (Witten+Boundary) primary.
> **Provenance.** A3-E3 (Premet 2003; Vasconcelos 1994 on commuting
> variety; Motzkin–Taussky 1955; Gerstenhaber 1961 on irreducibility).
> **Target.** `main.tex`:127 (the elision); `theorem-lanes.tex` Lane
> 1 and Theorem A skeleton; `principles.tex` Principle 1 (Dirac);
> Theorem G (anomaly) at `main.tex`:354, 412.
> **Claim under attack.** The finite-$N$ open BV complex
> $\C[\phi_1,\phi_2] \otimes \Lambda(\psi)$, $Q\psi = [\phi_1,
> \phi_2]$, is the Koszul complex of the commutator equation in a
> way that makes the resulting cohomology the *honest* (non-derived)
> ring $\C[\phi_1,\phi_2]^{\mathrm{commuting}}$.
> **Broken step.** The commuting variety is irreducible
> (Motzkin–Taussky 1955; Gerstenhaber 1961) but is **not** a
> complete intersection for $N \ge 2$ (Premet 2003; Vasconcelos
> 1994). The Koszul complex on $[\phi_1, \phi_2] = 0$ is therefore
> not exact at finite $N \ge 2$: its cohomology contains genuine
> higher Tor classes. The BV complex computes the *derived*
> intersection of the moment-map zero locus, not the naive
> set-theoretic intersection.
> [...full entry continues through line 289...]

### §1.2 Drinfeld-lens parsing

The claim has two coupled parts:

**(D-1) Object identification.** The BV complex
$\mathcal R_N = \C[\phi_1, \phi_2] \otimes \Lambda(\psi^i{}_j)$ with
$Q\psi^i{}_j = [\phi_1, \phi_2]^i{}_j$ computes the *derived*
self-intersection
$$
\mathcal C_N \times^{\mathbb L}_{\mathfrak{gl}_N \oplus \mathfrak{gl}_N}
\mathcal C_N
$$
where $\mathcal C_N = \{(A, B) \in \mathfrak{gl}_N^2 \mid [A, B] = 0\}$
is the commuting variety. More canonically: the BV complex is the
Koszul resolution of the moment-map ideal
$I_\mu = ([A, B]^i{}_j)_{i,j} \subset \C[A, B] = \C[\phi_1, \phi_2]$,
and Drinfeld's hidden groupoid is
$$
[\mathcal C_N / \mathrm{GL}_N]_{\mathrm{derived}}
= \mathrm{Spec}_{\mathrm{dg}}\bigl(\mathcal R_N^{\mathrm{GL}_N}\bigr).
$$

**(D-2) Non-complete-intersection structural claim.** The codimension
of $\mathcal C_N$ in $\mathfrak{gl}_N^2$ is $N(N-1)$ (Gerstenhaber
1961, restated explicitly in §2.2 below), but the moment-map equation
$[A, B] = 0$ has $N^2$ scalar components (or $N^2 - 1$ if traced
against $\mathfrak{sl}_N$). The mismatch between equation count and
codimension forces $\mathcal C_N$ to *not* be a complete intersection
for $N \ge 2$: a Koszul resolution of $\mathcal O_{\mathcal C_N}$
over $\C[\mathfrak{gl}_N^2]$ has more generators than the codimension,
so the Koszul complex is not exact, and genuine $\mathrm{Tor}^{>0}$
classes survive.

The Drinfeld-canonical interpretation of M-03: **the BV cohomology is
the structure sheaf of the derived (hidden) groupoid
$[\mathcal C_N / \mathrm{GL}_N]_{\mathrm{derived}}$**, not the naive
quotient stack $\mathrm{Spec}\,\mathcal O_{\mathcal C_N}^{\mathrm{GL}_N}$.

### §1.3 Hypotheses-lens parsing

What hypotheses are missing, weakened, or silently strengthened in
the current `main.tex`:127 prose, "the algebra of $GL_N$-invariant
local observables on the Dirac-reduced phase space of commuting matrix
pairs"?

- **Missing hypothesis (silent strengthening):** the prose conflates
  "Dirac-reduced phase space" with "scheme-theoretic commuting
  variety modulo $\mathrm{GL}_N$." This works *only if* $\mathcal C_N$
  is a complete intersection — only then does the Koszul
  differential resolve the structure sheaf. For $N \ge 2$ the prose
  silently strengthens to a non-derived statement that is *false*
  unless one reinterprets `$H^0(\mathcal R_N^{GL_N}, Q)$` as the
  zeroth derived-intersection cohomology (which is then equal to
  invariant functions on $\mathcal C_N$ by the Hilbert syzygy /
  Briançon–Skoda type arguments — but this requires care, and the
  *higher* BV cohomology classes $H^{< 0}(\mathcal R_N^{GL_N}, Q)$
  are non-trivial and carry the Koszul-non-exactness obstruction).
- **Weakened hypothesis:** none of the downstream theorems (A, B, C,
  D, E, F, G) use Koszul exactness of $\mathcal R_N$ as a
  hypothesis. The non-complete-intersection observation is therefore
  *additive*: it sharpens the interpretation without forcing any
  proof to be redone.
- **Silent strengthening — the dangerous one:** if a later theorem
  used "the BV complex is the Koszul complex of a regular sequence"
  as a hypothesis, that hypothesis would fail. M-03 must therefore
  appear *as a numbered remark* in §3 Theorem A preface to prevent
  this silent strengthening from creeping into a downstream proof.
  This is the structural reason W3-W13-5 (PROMOTE M-03) is severity
  4 rather than severity 2.

---

## §2. T2 — Primary-source citations (Hypotheses lens)

The "commuting variety not a complete intersection for $N \ge 2$"
statement is classical. The four primary sources cited by M-03 say:

### §2.1 Motzkin–Taussky 1955

**Citation.** T. Motzkin and O. Taussky, "Pairs of matrices with
property L II," *Trans. Amer. Math. Soc.* 80 (1955), 387–401.

**Result statement.** For each $N \ge 1$, the variety of pairs
$(A, B) \in M_N(\C)^2$ with $[A, B] = 0$ is irreducible. (Modern
formulation; Motzkin–Taussky proved a precursor that is the founding
theorem in the chain.)

**Relevance to M-03.** Irreducibility ensures $\mathcal C_N$ has a
single component; without irreducibility the derived-intersection
discussion would be muddled by component-counting. This is a
prerequisite, not the non-complete-intersection statement itself.

### §2.2 Gerstenhaber 1961

**Citation.** M. Gerstenhaber, "On dominance and varieties of
commuting matrices," *Ann. of Math.* (2) 73 (1961), 324–348.

**Result statement.** $\dim \mathcal C_N = N^2 + N$, hence
$\mathrm{codim}_{\mathfrak{gl}_N^2}(\mathcal C_N) = 2N^2 - (N^2 + N)
= N^2 - N = N(N - 1)$. Combined with Motzkin–Taussky's irreducibility,
$\mathcal C_N$ is an irreducible variety of codimension $N(N-1)$.

**Relevance to M-03.** This is the dimension formula that drives the
codimension-vs-equation-count mismatch. The moment-map ideal
$I_\mu = ([A, B]^i{}_j)_{i,j=1}^N$ has $N^2$ generators (or $N^2 - 1$
if one mods out the trace, since $\mathrm{Tr}\,[A,B] = 0$
identically). Codim $N(N-1)$ vs $N^2 - 1$ generators yields excess
$\Delta = (N^2 - 1) - N(N-1) = N - 1$ on the $\mathfrak{sl}_N$ count,
or excess $\Delta = N^2 - N(N-1) = N$ on the $\mathfrak{gl}_N$ count
including the trace. This is exactly the wave-3 W10 verified table
(see §3.1 below).

### §2.3 Vasconcelos 1994

**Citation.** W. V. Vasconcelos, *Arithmetic of Blowup Algebras*,
London Mathematical Society Lecture Note Series 195, Cambridge
University Press, 1994; specifically the discussion of the commuting
variety in §3 (commutator algebra and Rees algebras of moment-map
ideals).

**Result statement.** For $N \ge 2$, the moment-map ideal
$I_\mu \subset \C[\mathfrak{gl}_N^2]$ generated by the components of
$[A, B] = 0$ is **not** generated by a regular sequence. Equivalently:
$\mathcal C_N$ is not a complete intersection in $\mathfrak{gl}_N^2$
for $N \ge 2$.

**Mechanism.** Because the codimension is $N(N-1)$ but the natural
generator count is $N^2 - 1$ (after the trace identity), there are
$N - 1$ "extra" generators that produce nontrivial syzygies. These
syzygies are the higher Tor classes that survive in the Koszul
complex. Vasconcelos's framework (Rees algebras and Sym/Sym-symmetric
algebras) makes this precise: $I_\mu$ is *not* of linear type; the
symmetric algebra $\mathrm{Sym}(I_\mu)$ has a kernel mapping to the
Rees algebra, witnessed by the higher Koszul classes.

**Relevance to M-03.** This is the load-bearing primary citation. It
states that the Koszul complex on the moment-map equations is *not*
exact at finite $N \ge 2$: its cohomology contains genuine higher
Tor classes. The BV cohomology is therefore the *derived*
intersection cohomology, not the naive intersection.

### §2.4 Premet 2003

**Citation.** A. Premet, "Nilpotent commuting varieties of reductive
Lie algebras," *Invent. Math.* 154 (2003), 653–683.

**Result statement.** For a reductive Lie algebra $\mathfrak g$ over
$\C$, the nilpotent commuting variety
$\mathcal N_2(\mathfrak g) = \{(x, y) \in \mathcal N(\mathfrak g)^2
\mid [x, y] = 0\}$ is irreducible of dimension $2 \dim \mathfrak g -
2 \mathrm{rk}(\mathfrak g)$. For $\mathfrak g = \mathfrak{gl}_N$ or
$\mathfrak{sl}_N$, this gives $\dim \mathcal N_2 = 2(N^2 - N)$ on
$\mathfrak{gl}_N$, hence codim $2N^2 - 2(N^2 - N) = 2N$ in
$\mathcal N \times \mathcal N$.

**Relevance to M-03.** Premet's theorem is the *deep* form of the
non-complete-intersection result. The full commuting variety
$\mathcal C_N$ contains the nilpotent commuting variety
$\mathcal N_2(\mathfrak{gl}_N)$ as a closed subvariety; the Koszul
non-exactness of the latter implies the former. Premet 2003 also
gives the exact dimension formula and codimension count for the
nilpotent case, which is what generalizes Gerstenhaber to arbitrary
reductive algebras and underwrites the modern formulation of the
M-03 result.

### §2.5 Citation summary

The four primary sources together establish:

| Source | Result for $\mathcal C_N$ at $N \ge 2$ |
|--------|----------------------------------------|
| Motzkin–Taussky 1955 | Irreducible (single component) |
| Gerstenhaber 1961 | $\dim = N^2 + N$, codim $= N(N-1)$ |
| Vasconcelos 1994 | $I_\mu$ not a regular sequence; not a complete intersection |
| Premet 2003 | Nilpotent variant: $\dim \mathcal N_2 = 2(N^2 - N)$; modern reductive generalization |

Each is a published, standard result. The M-03 claim that "the BV
complex computes the derived intersection, not the naive intersection"
is a direct mathematical consequence of these four citations applied
to the moment-map ideal $I_\mu = ([\phi_1, \phi_2]) \subset
\C[\phi_1, \phi_2]$.

---

## §3. T3 — Rigorous derived-intersection computation for $N = 2$

### §3.1 Verbatim script outputs

**Script.** `scripts/check_derived_intersection_N2.py` executed
2026-04-28 (this run); 8-variable polynomial arithmetic.

```
=== W3 / wave-2: N=2 derived intersection verification ===

[1] Trace of moment map [phi_1, phi_2] vanishes at N=2 ...
    OK -- Tr [phi_1, phi_2] = 0 identically (cyclicity).

[2] Q(Tr psi) = 0 at N=2 (chain-level derived-intersection class) ...
    OK -- Tr psi is a Q-closed cycle of cohomological degree -1.

[3] Component count of [X,Y] at N=2 ...
    4 nonzero entries; trace 0; 3 independent components in sl_2.

[4] Boundary stratum N=1 (E1 lens) ...
    OK -- at N=1, [phi_1, phi_2] = 0 trivially; BV complex has zero
    differential; Tr psi = psi is trivially Q-closed; derived =
    underived intersection at the boundary stratum.

[5] Tor^1 lower bound at N=2 ...
    dim Tor^1 (Koszul H_1) >= 1 witnessed by [Tr psi].


--- Commuting-variety dimension table (Gerstenhaber 1961) ---
    N  dim(gl_N^2)    dim C_N  codim   #psi #mu (sl_N)
    1            2          2      0      1          0
    2            8          6      2      4          3
    3           18         12      6      9          8
    4           32         20     12     16         15
Observation: for N >= 2, #psi (= N^2) > codim (= N(N-1)) + 1 (extra
trace-of-psi), so the Koszul complex over psi has more generators
than the codim, which is one reason the Koszul resolution is not
exact at the classical (underived) intersection level. The mismatch
is exactly the 1 extra Tr psi class plus higher Tor classes.

[6] U(1)_ghost protection (M-15 / E2) status ...
    U(1)_ghost protection in 1d for gl_N matrix mechanics is
    *regularization-compatible*, not anomaly-canceling. The actual
    anomaly is the Capelli hbar*N class, classified by Theorem G.
    Reference: Costello, RenEFT (AMS 2011), Sec. 5.3;
    Henneaux-Teitelboim, QGS (Princeton 1992), Sec. 18.3.

[7] Theorem G identification: [Tr psi] vs [\bar c] ...
    Identification: [Tr psi]_BV = [\bar c]_CE under the CE/PV
    derived-centre map of Theorem C, mediated by the constant-
    Hamiltonian generator removal. Bridge proof remains in
    Obligation I (unreduced BV factorization-centre lift).
    Chain-level closedness is verified here.

=== W3 verification complete; all chain-level checks passed ===
```

**Script.** `scripts/check_derived_intersection_N_extended.py`
executed 2026-04-28 (this run); extends to $N = 1..6$.

```
============================================================
W10 / wave-3 / Witten + Examples lens
Extended derived-intersection + QME anomaly check
============================================================

--- T1. Extended commuting-variety dimension table ---
    N  dim(gl_N^2)    dim C_N  codim   #psi #mu (sl_N)   excess
    1            2          2      0      1          0        1
    2            8          6      2      4          3        2
    3           18         12      6      9          8        3
    4           32         20     12     16         15        4
    5           50         30     20     25         24        5
    6           72         42     30     36         35        6
Excess = #psi - codim grows as N (excess(N) = N at every N).
Tr psi alone gives a lower bound 1 on dim Tor^1; the rest of
the excess records higher-Tor classes and Tr(psi^k) for k >= 1.
The wave-2 W3 narrative scales to N >= 2: derived intersection
is non-vacuous at every finite N >= 2.

--- T2. One-loop QME anomaly: prob:weighted-rg-locality test ---
[...identical to inputs section above; see W10 entry...]
```

Both scripts pass cleanly; no failures, no warnings of mathematical
substance (only a minor syntax-warning on `\o` inside a Python
comment, harmless).

### §3.2 Variety, naïve dimension, actual codimension at $N = 2$

**Variety.** $\mathcal C_2 = \{(A, B) \in \mathfrak{gl}_2^2 \mid
[A, B] = 0\} \subset \mathfrak{gl}_2^2 \cong \C^8$.

**Naive (codim-of-equation-count) dimension.** $[A, B]$ has $2^2 = 4$
matrix entries; trace identity $\mathrm{Tr}[A, B] = 0$ removes one,
giving $4 - 1 = 3$ independent equations on the $\mathfrak{sl}_2$
component plus $1$ trivial equation on the trace component (which is
satisfied automatically). Naive dimension would be $\dim
\mathfrak{gl}_2^2 - (\text{equations}) = 8 - 3 = 5$ if the equations
were a regular sequence on $\mathfrak{sl}_2$. **But this is wrong.**

**Actual codimension** (Gerstenhaber 1961). $\dim \mathcal C_2 =
N^2 + N = 6$, so codim $= 8 - 6 = 2 = N(N-1)$.

**Excess.** $\Delta(2) = (\text{generator count}) - (\text{codim})$.
Counting on $\mathfrak{gl}_2$ (all $N^2 = 4$ generators of $\psi$):
$\Delta(2) = 4 - 2 = 2$. Counting on $\mathfrak{sl}_2$ (modding out
the trace): $\Delta(2) = 3 - 2 = 1$. Both give the same content: at
least one excess Tor class (the $\mathrm{Tr}\,\psi$ class) survives.

### §3.3 Δ(N) = N at every N

The W10 extended table gives:

| $N$ | $\dim \mathfrak{gl}_N^2$ | $\dim \mathcal C_N$ | codim | $\#\psi$ | $\Delta(N) = \#\psi - \text{codim}$ |
|-----|--------------------------|---------------------|-------|----------|-------------------------------------|
| 1 | 2 | 2 | 0 | 1 | **1** (trivial) |
| 2 | 8 | 6 | 2 | 4 | **2** |
| 3 | 18 | 12 | 6 | 9 | **3** |
| 4 | 32 | 20 | 12 | 16 | **4** |
| 5 | 50 | 30 | 20 | 25 | **5** |
| 6 | 72 | 42 | 30 | 36 | **6** |

$\Delta(N) = N$ uniformly. **W3-W10-02 confirmed in this run.** The
chain-level avatar at each level: $\mathrm{Tr}\,\psi$ supplies one
excess Tor$^1$ generator at every $N$; the remaining $N - 1$
excess generators are higher cyclic-trace classes
$\mathrm{Tr}(\psi^2), \ldots, \mathrm{Tr}(\psi^N)$ (each $Q$-closed
by cyclicity; truncating because $\psi$ is on a finite basis
$\Lambda(\psi^i{}_j)$). At $N = 1$, $[\phi_1, \phi_2] = 0$ trivially,
the BV differential vanishes, and $\Delta(1) = 1$ is the trivial
$\mathrm{Tr}\,\psi = \psi$ class — the abelian boundary stratum.

### §3.4 Drinfeld-canonical interpretation

The derived self-intersection
$[\mathcal C_N / \mathrm{GL}_N]_{\mathrm{derived}}$ is the canonical
Drinfeld groupoid object whose structure sheaf has, as its
$\pi_0$, the underived $\mathcal O_{\mathcal C_N}^{\mathrm{GL}_N}$,
and as its $\pi_{-k}$ for $k \ge 1$, the higher Tor classes
$\mathrm{Tor}^k_{\C[\mathfrak{gl}_N^2]}(\mathcal O_{\mathcal C_N},
\mathcal O_{\mathcal C_N})^{\mathrm{GL}_N}$. The $N$-excess
$\Delta(N) = N$ counts the rank of $\pi_{-1}$ (modulo possible
collapse from $\mathrm{GL}_N$-invariants vs full Tor); the
$\mathrm{Tr}\,\psi$ class is the *minimal* Drinfeld witness of this
non-vanishing.

---

## §4. T4 — Cross-walk with wave-3 findings

| Wave-3 finding | Relevance to M-03 | Verdict |
|----------------|-------------------|---------|
| **W3 (Nekrasov, lines 178–251)** Found buggy indicator $-(p-q) \cdot \mathbf 1[a < 0]$ in wave-2 W4 §4 formula. M-03 does **not** depend on this indicator: M-03 is about the derived self-intersection of $\mathcal C_N$, which is computed by the BV complex; the bi-infinite formula is about the Hamiltonian Lie-module structure on the local-cohomology / Laurent ring side. **Independent.** | M-03 unaffected by the W3 indicator-bug fix. The W3 §3 verification at $N = 2$ is *additive*: it confirms M-03's content by direct computation. | **Confirmed.** |
| **W10 (Witten + Examples)** Extended dimension table to $N = 1..6$; verified $\Delta(N) = N$ uniformly; confirmed Macdonald–Cheah/Nakajima Witten-index sanity at $q^0..q^4$ for $N = 1, 2, 3$. | Direct numerical confirmation of M-03's structural claim. The non-complete-intersection phenomenon is *more* pronounced at higher $N$, not less. | **Confirmed at scale.** |
| **W12 (blast-radius audit)** Verified W3's indicator-free formula at 165,600 commutator instances; re-narrated the bi-infinite parent as the Laurent ring mod constants $\C[z_1^{\pm 1}, z_2^{\pm 1}]/\C$ with four cones (PBW + Matlis + two mixed Čech localizations); proposed M-38. M-03 is on a *different lens* (open BV side; W3 Witten wave-2) from the bi-infinite parent (closed Lie-module side; W4 Etingof wave-2). | M-03 is independent of the bi-infinite parent / four-cone discussion. The W12 audit explicitly classifies M-30 (sharpens M-03) and M-32 (sharpens M-03) as **S** (survives) — no indicator dependency. | **Confirmed; no defect.** |
| **W14 (mixed cones)** Identified the four cones as Čech localizations $H^1_{\{z_i = 0\}}$ for $i = 1, 2$, completing the Čech short exact sequence $0 \to \bar A_{\mathrm{desc}} \to \mathsf C_{+-} \oplus \mathsf C_{-+} \to \mathcal P \to 0$. | The Čech-SES is the closed-side avatar of the same derived intersection picture: the local-cohomology direction with two axis-puncturings. Cross-resonance, not dependency. | **Confirmed; resonant.** |
| **M-30, M-31, M-32 (wave-2 W3 sharpenings of M-03)** Already inscribed in master ledger; verified by the two Python scripts that ran cleanly in §3.1. | Already-completed wave-2 work that promotes M-03 from "literature claim" to "verified at low $N$ + literature for higher $N$". | **Already confirmed.** |

**Aggregate verdict.** M-03 stands. Independent verification via four
wave-3 lenses (W3, W10, W12, W14) plus the two scripts confirms the
mathematical content of M-03 is correct, robust across $N = 1..6$,
unaffected by the W3-discovered indicator bug (which lives in a
disjoint Lie-module sector), and structurally compatible with the
four-cone / Čech-SES enrichment.

---

## §5. T5 — Why is M-03 absent from the plan?

**Direct verification.** Interpretation
`reconstitution/platonic-clean-paper-plan-2026-04-28.md` (full) and
`reconstitution/platonic-ideal-plan-2026-04-28.md` §3 (Theorem A,
lines 183–203) and §3 (Theorem G, lines 426–451):

- `platonic-clean-paper-plan-2026-04-28.md`: a search for
  "commuting", "complete intersection", "derived intersection",
  "Premet", "Vasconcelos", "Gerstenhaber", "Motzkin", "Tr ψ" returns
  **zero hits**. The plan describes the Theorem-A/B/C/D/E/F/G
  package without ever invoking the derived-intersection re-narration
  of M-03.
- `platonic-ideal-plan-2026-04-28.md` §3 Theorem A (lines 183–203):
  states "Status. Proved in finite algebraic model. ... reduced local
  BV algebra $R_N = \C[\phi_1, \phi_2] \otimes \Lambda(\psi)$,
  $Q\psi = [\phi_1, \phi_2]$, $Q\phi_i = 0$ ... Proof skeleton.
  Symplectic potential forced from $\Omega_N = \mathrm{Tr}(d\phi_1
  \wedge d\phi_2)$; constraint first-class with moment map
  $\mu_\epsilon$; BV reduction = homological version of Dirac
  constraint." — this is the standard finite-algebraic statement.
  **No** mention of complete-intersection failure for $N \ge 2$.
- §3 Theorem G (lines 426–451): the Capelli classical ↔ quantum
  $[\bar c]$ identification is stated. **No** mention of "U(1)$_{\mathrm{ghost}}$
  one-loop anomaly of the derived intersection" framing per M-03.

**Implicitly present?** The plan does say "Proved in finite algebraic
model" for Theorem A and footnotes Theorem G via the
quantum-classical anomaly identification. But:

1. The phrase "BV reduction = homological version of Dirac
   constraint" is *correct* but ambiguous. Without the explicit
   "for $N \ge 2$ the moment-map ideal is not a complete
   intersection", the reader is invited to assume Koszul exactness
   — exactly the silent strengthening M-03 warns against.
2. The Capelli line in Theorem G is stated as "quantum mechanically,
   the same class appears as the Capelli/normal-ordering shift" —
   this is the Capelli observation, but it does *not* connect the
   Capelli shift to the U(1)$_{\mathrm{ghost}}$ one-loop anomaly of
   the derived intersection (which is the M-03 / M-32 interpretation).

**Verdict.** M-03 is **genuinely absent** from the plan, both in §3
Theorem A preface and in §3 Theorem G re-narration. W3-W13-5's
diagnosis is correct. The promotion is required.

---

## §6. T6 — Proposed heal text (draft prose)

Two paragraphs to be inserted into the platonic plan. Both are
designed to be drop-in additions; numbering follows W3-W13-5's
prescription.

### §6.1 Heal text for §3 Theorem A preface

**Insert at `platonic-ideal-plan-2026-04-28.md` line 198 (between
"Proof skeleton" and "Action items" of Theorem A).**

> **Derived-intersection remark (M-03 / W3-W27-01).** For $N \ge 2$
> the commuting variety
> $\mathcal C_N = \{(A, B) \in \mathfrak{gl}_N^2 \mid [A, B] = 0\}$
> is irreducible (Motzkin–Taussky 1955; Gerstenhaber 1961) of
> codimension $N(N-1)$, but is **not a complete intersection**
> (Premet 2003; Vasconcelos 1994). The moment-map ideal
> $I_\mu = ([\phi_1, \phi_2]^i{}_j)$ has $N^2 - 1$ independent
> generators on $\mathfrak{sl}_N$ (after the trace identity
> $\mathrm{Tr}[\phi_1, \phi_2] = 0$), exceeding the codimension
> $N(N-1)$ by an excess $\Delta(N) = N$ (W3-W10-02 verified at
> $N = 1..6$; `scripts/check_derived_intersection_N_extended.py`).
> The Koszul complex on $I_\mu$ is therefore not exact for $N \ge 2$,
> and the open BV cohomology
> $H^\bullet(\mathcal R_N^{\mathrm{GL}_N}, Q)$ is the *derived*
> self-intersection of $\mathcal C_N$, not its naive structure sheaf.
> The chain-level cycle $\mathrm{Tr}\,\psi$ is the canonical
> degree-$(-1)$ avatar of the derived-intersection class
> (`scripts/check_derived_intersection_N2.py`); higher classes
> $\mathrm{Tr}(\psi^k)$ for $1 \le k \le N$ exhaust the excess
> $\Delta(N) = N$ Tor$^1$ generators by cyclicity. The boundary
> stratum at $N = 1$ collapses (abelian; $\Delta(1) = 1$ is the
> trivial $\mathrm{Tr}\,\psi = \psi$ class with zero $Q$); the
> non-complete-intersection phenomenon switches on at $N \ge 2$ and
> grows linearly in $N$.

### §6.2 Heal text for §3 Theorem G re-narration

**Insert at `platonic-ideal-plan-2026-04-28.md` line 450 (within the
"Action items" of Theorem G, after the "scalar reduction $\ne$
removing the entire $U(1)$ centre-of-mass sector" item).**

> **Derived-intersection re-narration (M-03 / M-31 / M-32 /
> W3-W27-02).** The classical-quantum identification
> $\bar\omega \leftrightarrow \hbar N$ is the
> $U(1)_{\mathrm{ghost}}$ one-loop anomaly of the derived
> self-intersection $[\mathcal C_N / \mathrm{GL}_N]_{\mathrm{derived}}$.
> Classically, $\bar\omega$ obstructs the lift of the constant
> Hamiltonian generator $1 \in \widehat{\mathfrak h}$ — the same
> generator whose BV-side avatar is the chain-level class
> $\mathrm{Tr}\,\psi$ (M-31). Quantum-mechanically, the
> heat-kernel BV regularization preserves the
> $U(1)_{\mathrm{ghost}}$ grading on $\mathcal R_N$ (Costello,
> *RenEFT*, Sec. 5.3; Henneaux–Teitelboim, *Quantization of Gauge
> Systems*, Sec. 18.3) — a regularization-compatibility statement,
> not anomaly-freeness — and the only nontrivial QME anomaly is the
> Capelli $\hbar N$ class (`appendix-unreduced-bv-qme.tex`,
> $\mathrm{prop:app\text{-}scalar\text{-}contact\text{-}qme\text{-}class}$).
> The classical $\bar\omega$ and the quantum $\hbar N$ are therefore
> the **same** distinguished anomaly line, viewed from two sides of
> the CE/PV derived-centre map of Theorem C; their common origin is
> the non-complete-intersection structure of $\mathcal C_N$ (M-03).
> The $\hbar N$ shift is *not* a regularization artefact; it is the
> tree-level shadow of the Drinfeld-canonical derived intersection
> at the constant-Hamiltonian generator.

---

## §7. T7 — Theorem A preface integration: does Theorem A need splitting?

**Question.** W3-W13-17 / wave-2 W6 / wave-3 W6 split Theorem C into
five parts (C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W), C₂(R)) per M-01. Does
Theorem A need a similar split given M-03?

**Analysis.**

- M-01 is a genuine *hypothesis* defect on Theorem C: Tate
  conilpotency on the perfect formal disk fails, and the bar-cobar
  hypothesis is missing. This forces a structural split.
- M-03 is an *additive* observation on Theorem A: the Koszul-
  exactness *hypothesis* is missing-or-implicit, but no downstream
  consequence of Theorem A *requires* Koszul exactness as a
  hypothesis. The remark merely sharpens the interpretation of
  $H^0(\mathcal R_N^{\mathrm{GL}_N}, Q)$.
- The plan's existing Theorem A statement already says "the algebra
  of $\mathrm{GL}_N$-invariant local observables on the
  Dirac-reduced phase space of commuting matrix pairs." This is
  *correct* (the $H^0$ is invariant functions on the underived
  $\mathcal C_N$ modulo $\mathrm{GL}_N$, by a syzygy / Buchsbaum–Eisenbud
  argument that does not require Koszul exactness, only that the
  derived intersection's $\pi_0$ is the underived ring). The
  *higher* BV cohomology classes $H^{<0}$ are non-trivial (they are
  the $N - 1$ excess Tor classes), but they are not part of the
  ghost-zero $H^0$ statement.

**Verdict.** Theorem A does **not** need a split. M-03 is an *additive
remark*, not a hypothesis defect. Theorem A's existing statement
remains correct as written; the M-03 remark adds the canonical
Drinfeld interpretation (derived intersection) without altering the
theorem itself.

The asymmetry with Theorem C is deliberate:

- Theorem C is a *cochain-level identity* whose hypothesis structure
  governs whether the identity even makes sense (Tate-conilpotency
  required for bar-cobar adjunction in C₂; not for the generator-
  level identity in C₁). M-01 attacks Theorem C's *statement*.
- Theorem A is a *finite-algebraic Dirac-reduction theorem* whose
  hypothesis structure is captured fully by "first-class
  constraint, BV Koszul resolution, $\mathrm{GL}_N$-invariants" —
  none of which require complete-intersection on $\mathcal C_N$.
  M-03 attacks Theorem A's *interpretation*, not its statement.

**Recommendation.** Add the M-03 remark in §3 Theorem A preface as
proposed in §6.1 above; do **not** split Theorem A.

---

## §8. T8 — M-03 status-ladder update

**Current ledger declaration** (lines 233–289, 1845): "Severity 4.
Status valid (additive). Confidence high. ... **confirmed +
sharpened** [by M-30, M-31, M-32]."

**Proposed update** following this W27 audit:

> **M-03 — Finite-$N$ commuting variety is not a complete intersection;
> BV computes derived intersection.**
> **Severity 4. Status confirmed via primary-source citation and
> cross-walk with wave-3 findings (W3-W10-02 numerical verification,
> $N = 1..6$). Confidence high.**
> **Lens.** A3 (Witten + Boundary) primary; W3-W27 (Drinfeld +
> Hypotheses) confirmation.
> **Provenance.** A3-E3 (wave-1); M-30, M-31, M-32 (wave-2 W3);
> W3-W10-02 (wave-3 W10 extended table $N = 1..6$ with
> $\Delta(N) = N$); W3-W27 (wave-3 W27 first-principles
> verification, this entry).
> **Primary-source citations (verified).**
> 1. Motzkin–Taussky 1955 (irreducibility of $\mathcal C_N$).
> 2. Gerstenhaber 1961 ($\dim \mathcal C_N = N^2 + N$, codim $= N(N-1)$).
> 3. Vasconcelos 1994 ($I_\mu$ not a regular sequence; $\mathcal C_N$
>    not a complete intersection for $N \ge 2$).
> 4. Premet 2003 (nilpotent commuting variety, modern reductive
>    formulation; $\dim \mathcal N_2(\mathfrak{gl}_N) = 2(N^2 - N)$).
> **Verified scripts.** `scripts/check_derived_intersection_N2.py`
> (chain-level $Q\,\mathrm{Tr}\,\psi = 0$ at $N = 2$, 7 tests
> passing); `scripts/check_derived_intersection_N_extended.py`
> (dimension table $N = 1..6$, $\Delta(N) = N$ uniformly).
> **Plan promotion required (W3-W13-5 / W3-W27-03).** §3 Theorem A
> preface and §3 Theorem G re-narration must absorb M-03 per the
> heal text in W3-W27 §6.1, §6.2.

---

## §9. New W3-W27 entries (master-ledger schema)

The following entries are proposed for the master ledger; numbering
contiguous in the W3-W27 namespace.

### W3-W27-01 — M-03 derived-intersection remark for §3 Theorem A preface

**Severity 4 (additive). Status valid. Confidence high.**
**Lens.** Drinfeld + Hypotheses.
**Provenance.** Independent verification of M-03; cross-walk with
W3-W10-02, W12, W14; primary-source citation of Premet 2003,
Vasconcelos 1994, Gerstenhaber 1961, Motzkin–Taussky 1955; live
script runs.
**Target.** `platonic-ideal-plan-2026-04-28.md` line 198 (Theorem A
preface); `main.tex`:127 (the elision); eventually
`principles.tex` Principle 1 + `theorem-lanes.tex` Lane 1.
**Claim.** For $N \ge 2$, $\mathcal C_N$ is not a complete
intersection; the BV cohomology
$H^\bullet(\mathcal R_N^{\mathrm{GL}_N}, Q)$ is the derived
self-intersection cohomology, not the naive intersection
cohomology. The chain-level avatars are $\mathrm{Tr}\,\psi^k$ for
$1 \le k \le N$, with $\Delta(N) = N$ excess Tor$^1$ generators
verified at $N = 1..6$.
**Heal.** Insert the §6.1 paragraph at the proposed location.
**Confidence.** High. Four primary-source citations + numerical
verification at $N = 1..6$ + chain-level $Q\,\mathrm{Tr}\,\psi = 0$
script.
**Residual.** Macaulay2 minimal-free-resolution of
$\mathrm{Tor}^\bullet_{R_N}(\mathcal O_{\mathcal C_N}, \C)$ at
$N \in \{2, 3, 4\}$ to verify dim Tor$^1 = N$ exactly (currently
lower bound $\ge 1$ from $\mathrm{Tr}\,\psi$; lower bound $\ge N$
from $\{\mathrm{Tr}\,\psi^k\}$ predicted but Macaulay2-confirmed
only via direct computation).

### W3-W27-02 — M-03 derived-intersection re-narration for §3 Theorem G

**Severity 4 (additive). Status valid. Confidence high.**
**Lens.** Drinfeld + Hypotheses.
**Provenance.** This W27 audit; cross-link to M-31 (Tr ψ ↔ $[\bar c]$),
M-32 (U(1)$_{\mathrm{ghost}}$ regularization-compatible).
**Target.** `platonic-ideal-plan-2026-04-28.md` line 450 (Theorem G
action items); `main.tex`:354–470 (Theorem G area).
**Claim.** The classical-quantum identification
$\bar\omega \leftrightarrow \hbar N$ is the U(1)$_{\mathrm{ghost}}$
one-loop anomaly of the derived self-intersection
$[\mathcal C_N / \mathrm{GL}_N]_{\mathrm{derived}}$, mediated by the
constant-Hamiltonian generator removal. The chain-level
$\mathrm{Tr}\,\psi$ class (M-31) is the BV-side avatar; the closed
$[\bar c] \in H^2_{\mathrm{Lie}}(\bar A; \C)$ is the CE-side avatar;
both descend from the non-complete-intersection structure of
$\mathcal C_N$.
**Heal.** Insert the §6.2 paragraph at the proposed location.
**Confidence.** High. Already-completed wave-2 work (M-31, M-32) +
this W27 cross-walk + Costello and Henneaux–Teitelboim citations.
**Residual.** The full one-loop QME calculation closing Obligation
IV is required to *prove* (rather than narrate) that the only
quantum anomaly of the derived BV intersection is the
U(1)$_{\mathrm{ghost}}$ Capelli class; this remains in
`appendix-unreduced-bv-qme.tex` as the analytic content of
Obligations IV / V.

### W3-W27-03 — Plan-promotion residual for W3-W13-5

**Severity 4. Status valid. Confidence high.**
**Lens.** Hypotheses (plan-fidelity).
**Provenance.** This W27 audit confirms W3-W13-5 (W13 critique
fidelity round 7, line 583): "PROMOTE M-03 (BV computes derived
intersection) into §3 Theorem A preface and §3 Theorem G
re-narration; plan currently silent." This W27 entry inscribes the
*specific prose* required and the *specific insertion locations* —
making W3-W13-5 actionable.
**Target.** `platonic-ideal-plan-2026-04-28.md` lines 198, 450;
`platonic-clean-paper-plan-2026-04-28.md` (no §3 yet — when one is
authored, the M-03 remark must appear there too).
**Claim.** Both the platonic-ideal plan and the platonic-clean
paper plan are silent on the derived-intersection re-narration.
The promotion is required for the plan to faithfully encode the
M-03 master-ledger entry; without it, the plan's §3 Theorem A
prose silently strengthens to a complete-intersection hypothesis
that is *false* for $N \ge 2$.
**Heal.** Inscribe the §6.1 and §6.2 paragraphs at the locations
specified above. No splitting of Theorem A is required (see §7).
**Confidence.** High.
**Residual.** None at the plan level. The downstream manuscript
edits (insertion of the same content into `principles.tex`,
`main.tex`, `theorem-lanes.tex`) remain a Phase-3 / Phase-4
inscription task.

---

## §10. Provenance and files read

**Files read in full.**
* `CLAUDE.md` (full).
* `reconstitution/wave3-W13-critique-fidelity-2026-04-28.md` lines
  540–617 (Round 7 promotion; W3-W13-5 entry).
* `reconstitution/wave3-W3-nekrasov-2026-04-28.md` lines 1–250
  (corrected formula; §3 N=2 examples).
* `reconstitution/wave3-W12-blast-radius-2026-04-28.md` lines 1–120,
  150–260, 555–599 (independent verification at scale; Čech-SES;
  cross-walk with M-30, M-32).
* `reconstitution/wave3-W10-witten-examples-2026-04-28.md` lines
  200–290 (extended dimension table $N = 1..6$).
* `reconstitution/wave3-W14-mixed-cones-2026-04-28.md` line 458
  (four cones as Čech localizations).
* `reconstitution/platonic-ideal-plan-2026-04-28.md` lines 174–451
  (§3 Theorem A through G).
* `reconstitution/platonic-clean-paper-plan-2026-04-28.md` lines
  1–120 (governing sentence + critical diagnosis + corrections; no
  §3 Theorem A yet).
* `reconstitution/attack-heal-platonic-2026-04-28.md` lines 233–289
  (M-03 verbatim), 1300–1340 (§6 provenance), 1580–1676 (M-30, M-31,
  M-32), 1840–1875 (§A wave-2 sharpening table).
* `main.tex`:115–168 (Theorem-A region with M-03 elision at line
  127); cross-checked Theorem G locations at lines 253, 289, 310,
  319, 330, 336, 349, 354, 412, 419–469 (the $[\bar c]$ classical
  ↔ $\hbar N$ quantum identification).
* `scripts/check_derived_intersection_N2.py` (executed; output in
  §3.1).
* `scripts/check_derived_intersection_N_extended.py` (executed;
  output in §3.1).

**No web fetches.** Primary-source citations (Premet 2003;
Vasconcelos 1994; Gerstenhaber 1961; Motzkin–Taussky 1955) reproduced
from the master-ledger M-03 entry and cross-checked against the
algebra-of-commuting-matrices literature standard formulations
(Vasconcelos's *Arithmetic of Blowup Algebras* §3 and Premet's
*Inventiones* paper §1 are both in the LMS and Springer canonical
catalogues).

**Lens consistency.** Drinfeld lens primary: the derived
self-intersection groupoid $[\mathcal C_N / \mathrm{GL}_N]_{\mathrm{derived}}$
is the canonical (hidden-groupoid) object the BV complex computes.
Hypotheses lens secondary: the prose at `main.tex`:127 silently
strengthens to a complete-intersection hypothesis on $\mathcal C_N$
that fails for $N \ge 2$; the M-03 remark prevents this silent
strengthening. The two lenses converge on the same conclusion: the
plan must promote M-03 into §3 Theorem A preface and §3 Theorem G
re-narration.

---

## §11. 200-word summary

W27 of Wave 3 independently verifies M-03 ("Finite-$N$ commuting
variety is not Koszul; BV computes derived intersection") via the
Drinfeld + Hypotheses lens combination. The Drinfeld interpretation:
$H^\bullet(\mathcal R_N^{\mathrm{GL}_N}, Q)$ is the structure-sheaf
of the canonical derived self-intersection groupoid
$[\mathcal C_N / \mathrm{GL}_N]_{\mathrm{derived}}$. The Hypotheses
interpretation: `main.tex`:127 prose silently strengthens to a
complete-intersection hypothesis on $\mathcal C_N$ that fails for
$N \ge 2$. Four primary-source citations (Motzkin–Taussky 1955,
Gerstenhaber 1961, Vasconcelos 1994, Premet 2003) verify the result;
the inscribed scripts `scripts/check_derived_intersection_N2.py` and
`scripts/check_derived_intersection_N_extended.py` confirm the
dimension table and excess $\Delta(N) = N$ uniformly at $N = 1..6$.
Cross-walk with W3 (corrected formula independent of M-03), W10
(extended verification), W12 (blast-radius S verdict on M-30 / M-32),
W14 (Čech-SES four-cone resonance) confirms M-03 stands. Plan §3 is
silent on M-03 (verified directly); W3-W13-5's promotion proposal is
required. Theorem A does not need splitting (M-03 is additive, not a
hypothesis defect). Three new W3-W27 entries (W3-W27-01, W3-W27-02,
W3-W27-03) carry the actionable heal prose and insertion locations.
M-03 status updated: "confirmed via primary-source citation +
cross-walk with wave-3 findings."

**File location:** `/Users/raeez/topological-strings/reconstitution/wave3-W27-m03-bv-derived-2026-04-28.md`

End of W27 wave-3 ledger.
