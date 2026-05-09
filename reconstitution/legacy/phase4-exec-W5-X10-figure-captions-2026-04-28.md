# Phase-4 EXEC W5-X10: Figure Caption Upgrade Drafter

**Author.** Raeez Lorgat.
**Date.** 2026-04-28.
**Mode.** Proposal-only. No edits to `main.tex`, no commits.
**Wave.** Attack-heal swarm wave 5, ticket W5-X10.
**Target.** Severity-2 escalation #15 from W5-X6 critical-analysis re-read
(`reconstitution/phase4-exec-W5-X6-critical-analysis-2026-04-28.md`, line 89-99,
lines 162, 170, 197), against the pre-Phase-3 referee complaint:

> 15. The figures weaken the paper. The schematic ovals on pages 41, 50, and 51
> do not communicate mathematical data: no labels, no propagator convention, no
> orientation, no automorphism factor, no boundary ordering, no kernel. The
> captions say they are not Feynman-integral proofs. That makes them look
> ornamental. Either remove them or replace them with real graph notation:
> $\Gamma_1$, $\Gamma_3$, $\mathrm{Aut}(\Gamma)$, $P_\partial$, ordered boundary
> inputs.
> (`materials/processed/2026-04-28-whitepaper-critical-analysis.txt` lines
> 496-504.)

---

## 1. Source-of-truth audit

### 1.1 Asset reality

The repo-local `CLAUDE.md` source layout asserts six legacy image assets:

```
firstorder.{png,svg}, thirdordera.{png,svg}, thirdorderb.{png,svg}
```

These files exist on disk
(`/Users/raeez/topological-strings/firstorder.png` etc.), but the manuscript
`main.tex` does **not** include any of them via `\includegraphics`,
`\image{...}`, or `\imageopt{...}`:

```
$ grep -n 'includegraphics\|firstorder\|thirdordera\|thirdorderb' main.tex
(no matches)
```

The two figure environments in the manuscript (lines 4588-4639 and 5720-5793)
inscribe the graphs in pure TikZ. The PNG/SVG assets are dead-weight legacy
artefacts from an earlier draft. They are not what a referee sees.

This is a structural finding: the W5-X6 escalation was diagnosed against a
pre-Phase-3 state of the manuscript. Phase 3 (commit `bc41359` and earlier)
already replaced the schematic ovals with TikZ graphs that carry vertex labels,
propagator labels $P_\partial$, automorphism notation $\mathrm{Aut}(\Gamma)$,
and symmetry factors. Severity-2 escalation #15 is therefore **already
substantively closed at the structural level**: the figures are no longer
schematic ovals.

What remains for referee-grade self-containment is **propagator-kernel
declaration** inside each caption. The current captions cite the bivector
$P_\partial$ but do not cite the underlying time-domain propagator
$G(t,s)=\tfrac12\,\mathrm{sgn}(t-s)$ from
Proposition~\ref{prop:conditional-boundary-product-normalization}
(`main.tex` lines 5572-5601). A referee interpretation the caption alone cannot
reproduce the boundary integral
$\int a(t)b(t')\,G(t,t')\,P_\partial\,dt\,dt'$. This is a self-containment
gap, not a structural mis-rendering.

**Severity reassessment.** The figures are clean (TikZ, fully labelled, all
auts, all weights, all multiplicities), not structurally mis-rendered. The
remaining gap is editorial caption self-containment. Downgrade severity-2
escalation #15 → **severity-3 editorial polish** at the caption level.

### 1.2 Manuscript page locations

The two figure environments in `main.tex`:

| TikZ block | Lines | Caption | Label | Approximate page |
|---|---|---|---|---|
| Γ_1 single-edge | 4588-4639 | "The first-order graph $\Gamma_1$ for the trace bracket $\{O_f,O_g\}$..." | `fig:gamma1` | p. 41 (W5-X6 baseline) |
| Γ_{3a} three same-orientation edges | 5720-5747 (sub-block) | shared with Γ_{3b} | n/a (no separate label) | p. 50 |
| Γ_{3b} two-forward-one-reversed edges | 5752-5775 (sub-block) | shared with Γ_{3a} | `fig:gamma3` | p. 51 |

The wave-3 referee cited pp. 41, 50, 51, mapping to: Γ_1 on p. 41, Γ_{3a} on
p. 50, Γ_{3b} on p. 51 (with the third-order figure environment spanning a
page break, with both Γ_{3a} and Γ_{3b} living in a single `\begin{figure}` block
that crosses the 50/51 boundary, sharing one `\caption` and one `\label`).

---

## 2. Referee-grade gap analysis

I scan each TikZ inscription against the referee's literal demand
("$\Gamma_1$, $\Gamma_3$, $\mathrm{Aut}(\Gamma)$, $P_\partial$, ordered
boundary inputs", plus "labels, propagator convention, orientation,
automorphism factor, boundary ordering, kernel"), and against the
self-containment standard "a referee should be able to reproduce the
propagator integral from the caption alone, knowing the manuscript
conventions".

### 2.1 First-order figure (Γ_1, lines 4588-4639)

| Requirement | Present? | Gap |
|---|---|---|
| Graph name $\Gamma_1$ | YES (caption + TikZ + body refs) | none |
| Vertex labels | YES (`O_f(t)`, `O_g(t')` boundary insertions) | none |
| Edge labels | YES (single edge labelled `P_\partial`) | none |
| Propagator bivector formula | YES (`P_\partial = \partial_{z_1}\otimes\partial_{z_2} - \partial_{z_2}\otimes\partial_{z_1}`) | none |
| **Propagator-kernel declaration** $G(t,s)$ | **NO** | The bivector $P_\partial$ is the cross-contraction tensor on the target Weyl algebra, not the time-domain propagator. The kernel $G(t,s)=\tfrac12\,\mathrm{sgn}(t-s)$ from Proposition~\ref{prop:conditional-boundary-product-normalization} (lines 5572-5584) is not cited in the caption. |
| Boundary ordering | YES (caption: "ordered boundary insertions sit on $\R$ at distinct times $t,t'$") | none |
| Automorphism factor | YES (`|\mathrm{Aut}(\Gamma_1)|=1`, `1/|\mathrm{Aut}|=1`) | none |
| Weight (order in $\hbar$) | YES ("weight $=\hbar^1$") | none |
| Ordered vs commutator weight | YES ("ordered one-edge weight is $\hbar P_\partial/2$; commutator weight is $\hbar P_\partial$") | none |
| BV cohomological degree | NO (implicit; never stated in caption) | All legs are degree-zero Hamiltonians; reader infers from context. |
| Cross-references | YES (Prop.~`prop:first-order-bracket`, Prop.~`prop:moyal-monomial`, Lem.~`lem:omega-cocycle`) | none |
| "Schematic; not a separate Feynman-integral proof" disclaimer | PARTIAL: appears in body text after `\end{figure}` (line 4640-4643), not in the caption itself | Referee interpretation caption alone may not see the disclaimer. |

### 2.2 Third-order figure (Γ_{3a}, Γ_{3b}, lines 5720-5793)

| Requirement | Present? | Gap |
|---|---|---|
| Graph names $\Gamma_{3a}$, $\Gamma_{3b}$ | YES | none |
| Vertex labels | YES (`O_f(t)`, `O_g(t')`) | none |
| Edge labels | YES (`P_\partial^{(1,2,3)}` for Γ_{3a}; `P_\partial^{(1,2)}` and `-P_\partial^{(3)}` for Γ_{3b}) | none |
| Edge orientations | YES (Stealth arrows for each propagator; reverse-orientation explicitly drawn for Γ_{3b}) | none |
| **Propagator-kernel declaration** $G(t,s)$ | **NO** | Same gap as Γ_1: the time-domain kernel is not cited in the caption. |
| Boundary ordering | YES (`O_f(t)` left, `O_g(t')` right) | none |
| Automorphism groups | YES (`\mathrm{Aut}(\Gamma_{3a})=S_3`, $|\cdot|=6$; `\mathrm{Aut}(\Gamma_{3b})=S_2`, $|\cdot|=2$) | none |
| Symmetry factors | YES ($1/6$, $1/2$) | none |
| Orientation multiplicities | YES (binomial coefficients $\binom{3}{a}$ for $a\in\{0,1,2,3\}$) | none |
| Weight (order in $\hbar$) | YES (caption: "the third-order Moyal weight is $\hbar^3/24$") | none |
| Closed Moyal-coefficient formula | YES (full sum $P^3(f,g)=\sum_{a=0}^3(-1)^a\binom{3}{a}(k)_{3-a}(l)_a(m)_a(n)_{3-a}\,z_1^{k+m-3}z_2^{l+n-3}$) | none |
| Cross-references | YES (Prop.~`prop:moyal-monomial`, Prop.~`prop:open-line-midpoint-graph-weights`, Prob.~`prob:first-third-graph-normalizations`) | none |
| "Schematic; not a separate Feynman-integral proof" disclaimer | NO: neither caption nor immediately surrounding body text carries this disclaimer for Γ_{3} | A referee interpretation p. 50-51 alone will not see the disclaimer. |
| BV cohomological degree | NO (implicit; never stated in caption) | All legs degree-zero. |

---

## 3. Upgraded captions (proposal-only)

The following are stand-alone LaTeX patches. Each replaces the existing
`\caption{...}` block with a self-contained version. After application a
referee interpretation the caption alone, together with the manuscript's standing
conventions on the brane line $\R$ and the reduced first-order open model
$S_0=\int_\R\mathrm{Tr}(\phi_1\,d\phi_2)$, can reconstruct the propagator
integral that the graph encodes.

### 3.1 Upgrade for Γ_1 (replaces lines 4624-4637)

```latex
  \caption{First-order boundary graph $\Gamma_1$ for the reduced open-line
    trace bracket $\{O_f,O_g\}$ in the first-order open model
    $S_0=\int_\R\mathrm{Tr}(\phi_1\,d\phi_2)$. Graph data: two ordered
    degree-zero boundary insertions $O_f(t),O_g(t')$ on the brane line $\R$
    with $t\neq t'$ (vertices, valence one each); one cross-contraction
    propagator (one edge); no internal vertices, no closed loops; planar
    boundary embedding. The time-domain propagator is the zero-mode-removed
    midpoint kernel
    $G(t,s)=\tfrac12\,\mathrm{sgn}(t-s)$ of
    Proposition~\ref{prop:conditional-boundary-product-normalization}, whose
    midpoint value $G(+,-)=\tfrac12$ assigns one copy of the constant
    Poisson bivector
    $P_\partial=\partial_{z_1}\!\otimes\!\partial_{z_2}-\partial_{z_2}\!\otimes\!\partial_{z_1}$
    to the cross-contraction. Automorphism group $\mathrm{Aut}(\Gamma_1)=1$
    (no nontrivial edge or vertex symmetry that fixes the labelled
    insertions). Ordered one-edge weight $\hbar P_\partial/2$; commutator
    weight $\hbar P_\partial$ after subtracting the reverse ordering.
    Interpretation the bivector contraction on monomials $f=z_1^kz_2^l$, $g=z_1^mz_2^n$
    reproduces the cocycle coefficient $(kn-lm)$ of
    Proposition~\ref{prop:first-order-bracket}, the order-$\hbar$ Moyal
    coefficient of Proposition~\ref{prop:moyal-monomial}, and the U(1) centre
    cocycle $\omega(f,g)$ of Lemma~\ref{lem:omega-cocycle} realised at
    multidegree $(k+m,l+n)=(1,1)$. Schematic; not a separate Feynman-integral
    proof. The full Costello brane-defect graph realisation requires the
    additional analytic data of
    Problem~\ref{prob:first-third-graph-normalizations}.}
```

**Line-delta estimate.** Existing caption: 14 lines (4624-4637). Upgraded
caption: 28 lines. Net +14 lines. No TikZ-body change; the caption itself
absorbs the propagator-kernel datum, the BV-degree datum, and the schematic
disclaimer.

### 3.2 Upgrade for Γ_3 (replaces lines 5776-5791)

```latex
  \caption{Third-order boundary graphs $\Gamma_{3a}$ (top) and $\Gamma_{3b}$
    (bottom) for the order-$\hbar^3$ cross-contractions whose tensor target
    is $P^3(f,g)$, in the reduced first-order open model
    $S_0=\int_\R\mathrm{Tr}(\phi_1\,d\phi_2)$. Graph data: two ordered
    degree-zero boundary insertions $O_f(t),O_g(t')$ on the brane line $\R$
    (vertices, valence three each), three cross-contraction propagators
    between them (three edges), no internal vertices, no closed loops,
    planar boundary embedding. Each propagator is the zero-mode-removed
    midpoint kernel $G(t,s)=\tfrac12\,\mathrm{sgn}(t-s)$ of
    Proposition~\ref{prop:conditional-boundary-product-normalization}; each
    cross-contraction at $t\neq t'$ contributes one copy of the constant
    Poisson bivector
    $P_\partial=\partial_{z_1}\!\otimes\!\partial_{z_2}-\partial_{z_2}\!\otimes\!\partial_{z_1}$,
    and reversing the orientation of an edge contributes a relative sign.
    The orientation multiplicities are the binomial coefficients
    $\binom{3}{a}$ of Proposition~\ref{prop:moyal-monomial}: $\Gamma_{3a}$
    realises $a\in\{0,3\}$ (all three propagators in a common orientation)
    with automorphism group $\mathrm{Aut}(\Gamma_{3a})=S_3$ permuting the
    three identical edges (symmetry factor $1/|S_3|=1/6$); $\Gamma_{3b}$
    realises $a\in\{1,2\}$ (two same-orientation propagators and one
    reversed) with automorphism group $\mathrm{Aut}(\Gamma_{3b})=S_2$
    permuting the two identical same-orientation edges (symmetry factor
    $1/|S_2|=1/2$). Summing all four orientation classes,
    $P^3(f,g)=\sum_{a=0}^{3}(-1)^a\binom{3}{a}(k)_{3-a}(l)_a(m)_a(n)_{3-a}\,
      z_1^{k+m-3}z_2^{l+n-3}$,
    and the third-order Moyal commutator weight is $\hbar^3/24$ (ordered
    weight $\hbar^3/48$, doubled by reverse-order subtraction). The reduced
    open-line weights are computed in
    Proposition~\ref{prop:open-line-midpoint-graph-weights}; the Costello
    counterterm and anomaly checks remain the analytic obligations of
    Problem~\ref{prob:first-third-graph-normalizations}. Schematic; not a
    separate Feynman-integral proof.}
```

**Line-delta estimate.** Existing caption: 16 lines (5776-5791). Upgraded
caption: 30 lines. Net +14 lines.

### 3.3 Cumulative line-delta

| Patch | Lines added | Lines removed | Net |
|---|---|---|---|
| Γ_1 caption | 28 | 14 | +14 |
| Γ_3 caption | 30 | 16 | +14 |
| **Total** | **58** | **30** | **+28** |

No edits to TikZ bodies; no edits to image assets; no commits.

---

## 4. AI-tells / em-dash / agent-language scan on draft text

I scan the proposed caption text for em-dashes (—), AI tells, and
agent/swarm/ledger references per `~/ecosystem/INVARIANTS.md §IV`
and the project's ELITE-grade voice discipline.

| Token | Γ_1 | Γ_3 | Action |
|---|---|---|---|
| Em-dash `—` | 0 | 0 | clean |
| `let me`, `here is`, `here are` | 0 | 0 | clean |
| `simply`, `just`, `clearly`, `obviously` | 0 | 0 | clean |
| `delve`, `tapestry`, `realm`, `landscape`, `journey` | 0 | 0 | clean |
| `agent`, `swarm`, `ledger` | 0 | 0 | clean |
| `the user`, `we will`, `we should`, `let's` | 0 | 0 | clean |
| `important to note`, `it should be noted` | 0 | 0 | clean |
| AI-style enumeration ("Firstly... secondly... finally...") | 0 | 0 | clean |
| Russian-school voice (declarative, named-attribution, theorem-bracketed) | YES | YES | clean |

The captions read as: "graph data: ...; propagator: ...; automorphism: ...;
weight: ...; closed formula: ...; cross-refs: ...; schematic disclaimer."
Stand-alone-document discipline: each caption is self-contained against the
manuscript's standing convention $S_0=\int_\R\mathrm{Tr}(\phi_1\,d\phi_2)$
and the propagator $G(t,s)=\tfrac12\,\mathrm{sgn}(t-s)$. A referee can
reconstruct the integral $\int a(t)b(t')\,G(t,t')\,P_\partial\,dt\,dt'$
from the caption alone.

---

## 5. Ledger entries

### 5.1 Was the figure structurally mis-rendered?

**No.** The figures are TikZ inscriptions with vertex labels, edge labels,
propagator bivector formulas, automorphism groups, symmetry factors,
orientation multiplicities, and binomial multiplicities. The image assets
`firstorder.{png,svg}`, `thirdordera.{png,svg}`, `thirdorderb.{png,svg}` are
unused legacy artefacts and should ideally be removed in a subsequent commit
(out of scope for this proposal-only ticket; not blocking).

**Severity downgrade.** W5-X6 severity-2 escalation #15 → severity-3
editorial polish. Structural complaint is closed.

### 5.2 What remains to certify "all original critical-analysis objections
addressed"?

The captions, as upgraded in §3, achieve referee-grade self-containment by
importing the propagator-kernel datum, the BV-degree datum, and the
schematic disclaimer into the figure captions themselves.

### 5.3 Author certification

I certify that the upgraded captions in §3:

1. cite the time-domain propagator $G(t,s)=\tfrac12\,\mathrm{sgn}(t-s)$
   exactly as inscribed at
   Proposition~\ref{prop:conditional-boundary-product-normalization} and
   Proposition~\ref{prop:open-line-midpoint-graph-weights};
2. use the manuscript's standing notation
   $P_\partial=\partial_{z_1}\!\otimes\!\partial_{z_2}-\partial_{z_2}\!\otimes\!\partial_{z_1}$
   exactly as inscribed at line 5583-5584;
3. state automorphism groups $\mathrm{Aut}(\Gamma_1)=1$,
   $\mathrm{Aut}(\Gamma_{3a})=S_3$, $\mathrm{Aut}(\Gamma_{3b})=S_2$ exactly
   as inscribed at lines 4616, 5742, 5770;
4. state the closed Moyal-coefficient formula exactly as inscribed at
   lines 5681-5685;
5. introduce no new mathematical claim; the upgrade is purely caption-level
   self-containment.

### 5.4 Open-obligation status

This proposal is editorial polish, not a load-bearing mathematical heal. It
does not interact with:

- the open-obligation ledger of `open-obligations.tex`,
- the claim-strength ledger of `claim-strength-ledger.tex`,
- the Costello brane-defect graph realisation (still
  Problem~\ref{prob:first-third-graph-normalizations}),
- the cross-repo firewall against
  `~/calabi-yau-quantum-groups`/`~/igusa-cusp-form`.

The "Schematic; not a separate Feynman-integral proof" disclaimer in both
upgraded captions is the editorial-discipline anchor that prevents the
caption from over-claiming a Costello graph theorem.

---

## 6. Decision

**Severity downgrade.** W5-X6 escalation #15 (severity-2) → severity-3
editorial polish. Structural complaint is closed; figures already carry full
graph-theoretic data. Remaining gap is caption self-containment, addressed
by the proposed upgrades in §3.

**Action recommended.** A subsequent EXEC ticket may apply the §3 patches as
a single editorial commit (line-delta $+28$ in `main.tex`). This ticket is
proposal-only.

**No commit. No edits to `main.tex` or any TeX file or image asset.**

End of W5-X10 report.
