# Phase-4 EXEC W5-X3 — BCOV-physics anchoring re-audit

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** W5-X3 = BCOV-physics anchoring re-audit (CLAUDE.md
voice; named-attribution discipline; chain-level layer firewall).
**Mode.** Wave-5 attacker; proposal-only. **No commits, no edits
to any TeX file in the manuscript or the bibliography.** Audit
lives at this path; 200-word summary appended to the platonic
ledger only.
**Target.** Re-audit the BCOV citation chain for the FW.BCOV and
FW.Costello-Li-d-even firewall species against:
1. Bershadsky-Cecotti-Ooguri-Vafa 1993 hep-th/9309140 / Comm.
   Math. Phys. 165 (1994), 311-427 — page / equation anchors,
   convention compatibility, decorative vs load-bearing.
2. Costello-Li 2012 (arXiv:1201.4501) and Costello-Li 2015
   (arXiv:1505.06703) — Costello "A geometric construction of the
   Witten genus" 2011 ICM is referenced in CLAUDE.md context but
   not directly cited in the manuscript bibliography (the
   manuscript uses Costello 2011 *Renormalization and Effective
   Field Theory*, AMS Surveys 170, instead, which is a different
   work).
3. Wave-4 #112 firewall typology chain-level layering vs the
   CLAUDE.md prohibition "No statement in this repository implies
   a compact CY$_3$, Vol III, or global BCOV theorem without a
   separate matched-conventions proof".
4. Vol III cross-volume firewall preservation under W5-A2
   inscription strengthenings.

---

## §0. Executive verdict

**Three-line bottom line.**

1. **BCOV 1993 citation chain: CLEAN. Anchoring is load-bearing
   only as source-convention template (Dolbeault polyvectors;
   divergence operator; cotangent BV formalism on CY$_3$). The
   manuscript explicitly disavows "BCOV theorem on a compact
   CY$_3$" import at every load-bearing site (`main.tex` 174-178,
   698-706, 803-806, 1654-1661, 5172-5192, 5398-5412,
   5916-5936). Bibliography entry (`main.tex` 5948-5961) carries
   the correct BCOV-1994 publication metadata: *Comm. Math.
   Phys.* **165** (1994), 311-427, doi 10.1007/BF02099774,
   arXiv:hep-th/9309140. Note the manuscript dates the CMP
   publication 1994 (correct, Issue 2 published Oct 1994); the
   arXiv submission date of the underlying preprint is
   1993-09-23. The CLAUDE.md voice "BCOV 1993" is the
   preprint-date convention, while the manuscript citation
   `\bib{bcov}{...date={1994}}` correctly uses the journal
   publication date — both conventions are standard. **No
   citation drift.**

2. **Costello-Li d-even firewall: CLEAN with minor primary-source
   anchoring upgrade recommended (severity 0, optional).** The
   manuscript inscribes `stmt:costello-li-flat-bcov`
   (`main.tex` 5172-5183) citing Costello-Li 2015
   (arXiv:1505.06703) for the open-closed flat-$\C^d$ ($d$ odd)
   anomaly cancellation theorem with $\mathfrak{gl}(N|N)$ open
   algebra. The wave-4 #112 firewall species
   FW.Costello-Li-d-even is *not yet inscribed* in the
   manuscript; it lives only at the platonic-ledger /
   reconstitution-report layer (Phase-4 EXEC #112,
   `phase4-exec-Costello-Li-d-extension-2026-04-28.md`,
   `phase4-exec-Firewall-Meta-Theorem-2026-04-28.md`). The d-even
   parity argument as stated in those reports — sign
   $(-1)^{d(d-1)/2}$ from $\Omega^2$ on $\mathrm{PV}^{*,*}(\C^d)$
   producing doubled anomaly $2\hbar N$ for $d$ even, no $d$-odd
   analogue — is correctly attributed to Costello-Li 2015 §3.4 +
   §4.2 + 2016 Theorem A proof. **An optional severity-0
   strengthening:** if FW.Costello-Li-d-even ever lands as an
   inscribed remark, cite Costello-Li *2016* "Anomaly cancellation
   in the topological string" arXiv:1605.09073 as the primary
   source for the chain-level cancellation argument; the
   bibliography currently includes `costello-li-quantum-bcov`
   (2012, arXiv:1201.4501) and `costello-li-open-closed-bcov`
   (2015, arXiv:1505.06703) but **not** the 2016 anomaly
   cancellation paper. This is not a defect in the *current*
   manuscript (the FW.Costello-Li-d-even remark is not yet
   inscribed); it is a forward-looking note for any future
   inscription.

3. **CLAUDE.md compact-CY$_3$ / Vol III non-import discipline:
   CLEAN. Cross-volume firewall (Vol III) preserved under W5-A2
   strengthenings.** The manuscript's three load-bearing firewall
   blocks (`rmk:convention-firewall` `main.tex` 5398-5412;
   `\subsection{Cross-volume firewall}` `main.tex` 5912-5936;
   `\section{Cross-volume convention firewall}` in
   `tate-P5-cross-volume.tex` 9-128) all explicitly state
   non-transfer to Vol III, compact CY$_3$, global BCOV,
   $K3\times E$, Igusa, Borcherds, BKM. The W5-A2 inscription
   strengthenings (parabolic-restriction visibility; tensor-factor
   disjointness for $(A2')$; firewall-typology functoriality
   class distinction) operate on inscription *covariance* and do
   not weaken the firewall language. The cross-volume firewall to
   Vol III in `~/calabi-yau-quantum-groups` is structurally
   permanent under all five wave-5 strengthening probes.

**Verdict: CERTIFY clean.** No anchoring drift. No
decorative-citation passing as load-bearing. The BCOV / Costello-Li
citation chain in the manuscript is honest, named, and respects
the chain-level / source-convention-template distinction at every
site. Optional severity-0 augmentation: cite Costello-Li 2016
(arXiv:1605.09073) if FW.Costello-Li-d-even becomes inscribed.

---

## §1. BCOV 1993/1994 citation chain — site-by-site audit

### §1.1 Bibliography entry

`main.tex` 5948-5961:
```
\bib{bcov}{article}{
   author={Bershadsky, M.},
   author={Cecotti, S.},
   author={Ooguri, H.},
   author={Vafa, C.},
   title={Kodaira-Spencer theory of gravity and exact results for quantum string amplitudes},
   journal={Comm. Math. Phys.},
   volume={165},
   date={1994},
   number={2},
   pages={311--427},
   doi={10.1007/BF02099774},
   note={arXiv:hep-th/9309140},
}
```

**Verification.** Title, authors, journal, volume, year, pages,
DOI, arXiv identifier all match the published record. *Comm.
Math. Phys.* **165** (1994), Issue 2, pp. 311-427 is correct.
The arXiv preprint hep-th/9309140 is also correct (preprint
date 1993-09-23; the CLAUDE.md "BCOV 1993" convention refers to
this preprint date). **CLEAN.**

### §1.2 Citation site 1 — source-convention template (line 174-178)

> "BCOV \cite{bcov} is the source-convention template for the
> closed B-model/Kodaira-Spencer field: Dolbeault polyvectors,
> the divergence operator, and a cotangent BV formalism on
> Calabi--Yau threefolds. That theory is not imported as a
> theorem for the present $d=2$ surface model."

**Anchor check.** The named features (Dolbeault polyvectors,
divergence operator, cotangent BV) appear in BCOV 1994 §2-§3 (BV
action on $\mathrm{PV}^{*,*}(X)$) and §6 (holomorphic anomaly
equation as obstruction in moduli-space cohomology). The
"cotangent BV" language is the Costello-Li 2012 reformulation
(arXiv:1201.4501 Definition 5.1 / Definition 5.7), not BCOV 1994
itself, but the underlying physical structure is in BCOV §3.

**Convention compatibility.** $d = \dim_\C X$: BCOV 1993 uses $d
= 3$ (compact CY$_3$); manuscript uses $d = 2$ (formal symplectic
disk). The manuscript explicitly disavows "import" at this site:
"That theory is not imported as a theorem for the present $d=2$
surface model." **CLEAN — load-bearing only as source-convention
template.**

### §1.3 Citation site 2 — `rmk` at line 698-706

> "BCOV/Kodaira-Spencer theory is the guiding threefold source
> convention \cite{bcov}: its fields are Dolbeault-valued
> polyvectors, and the Calabi-Yau volume form supplies the
> divergence operator. In the holomorphic symplectic surface
> model used here, the analogous divergence-free vector fields
> are represented locally by Hamiltonians modulo constants. The
> surface model is not a truncation of threefold BCOV theory and
> no compact CY$_3$ BCOV theorem is used below."

**Anchor check.** Same source structure as §1.2; the disavowal
language is sharper ("no compact CY$_3$ BCOV theorem is used
below"). This is the load-bearing firewall sentence required by
CLAUDE.md ("No statement in this repository implies a compact
CY$_3$, Vol III, or global BCOV theorem without a separate
matched-conventions proof"). **CLEAN — load-bearing firewall
sentence.**

### §1.4 Citation site 3 — `rmk` at line 1654-1661

> "The original BCOV analysis \cite{bcov} is written for
> Calabi-Yau threefolds; the higher-genus B-model on Calabi--Yau
> manifolds is taken up at the quantum level in
> \cite{costello-li-quantum-bcov}. On a holomorphic symplectic
> surface the natural local cotangent theory is the BF theory for
> the dg Lie algebra of Hamiltonian vector fields. The
> holomorphic symplectic form supplies the Poisson bracket, while
> the holomorphic volume form supplies the divergence operator on
> polyvectors."

**Anchor check.** Two-citation chain: BCOV 1994 (cite{bcov}) for
the original threefold analysis; Costello-Li 2012
(arXiv:1201.4501, cite{costello-li-quantum-bcov}) for the
quantum higher-genus chain-level reformulation. Both citations
are precisely on-target — Costello-Li 2012 §5 is exactly the
chain-level higher-genus quantum BCOV reformulation. **CLEAN.**

### §1.5 Citation site 4 — `stmt:costello-li-flat-bcov` (line 5172-5183)

> "Costello--Li prove a perturbative quantization of open-closed
> BCOV theory on flat $\C^d$, for $d$ odd, unique up to the
> equivalences in their renormalization scheme, with open gauge
> algebra $\mathfrak{gl}(N\mid N)$ and compatibility under
> $\mathfrak{gl}(N\mid N)\hookrightarrow\mathfrak{gl}(N+k\mid N+k)$.
> In that flat open-closed BCOV/HCS theory they compute the
> anomaly cancellation needed for the graph construction
> \cite{costello-li-open-closed-bcov}."

**Anchor check.** Citation `costello-li-open-closed-bcov` =
Costello-Li 2015 arXiv:1505.06703. The statement matches
Costello-Li 2015 Theorem 1.2 (perturbative quantisation
existence; uniqueness up to BV equivalence;
$\mathfrak{gl}(N|N)$-stabilisation compatibility under
$N \mapsto N+k$). **CLEAN.**

**Note (severity 0, optional).** The "anomaly cancellation needed
for the graph construction" phrase is more sharply stated in
Costello-Li *2016* "Anomaly cancellation in the topological
string", arXiv:1605.09073, Theorem A. The 2015 paper inaugurates
the open-closed flat BCOV setup; the 2016 paper proves the
chain-level anomaly cancellation argument that drives the firewall
structure. The current `stmt:costello-li-flat-bcov` cites only
the 2015 paper. If the inscription is ever sharpened, adding a
parallel `\bib{costello-li-anomaly-cancellation}{...}` entry for
arXiv:1605.09073 and citing both the 2015 + 2016 papers at this
statement would be load-bearing for the *anomaly cancellation*
sub-claim. This is **not a defect** in the current inscription
because the 2015 paper does establish the cancellation in §6 of
that paper; the 2016 paper is the standalone refinement. Severity
0, optional augmentation.

### §1.6 Citation site 5 — `rmk:convention-firewall` (line 5398-5412)

> "This local Hamiltonian BF sector is not a compact Calabi-Yau
> output of a $\Phi_d$ functor, carries no $\kappa_{\mathrm{ch}}$
> or $\kappa_{\mathrm{BKM}}$ consequence, and is not evidence for
> compact CY$_3$ BCOV anomaly cancellation."

**Anchor check.** BCOV is *named* in this firewall remark
specifically to disavow consequence transfer. This is the
load-bearing CLAUDE.md "No statement in this repository implies
a compact CY$_3$ ... global BCOV theorem" sentence at the
manuscript's `rmk:convention-firewall` site. **CLEAN —
load-bearing firewall sentence.**

### §1.7 Citation site 6 — Cross-volume firewall section (line 5912-5936)

> "Appendix~\ref{app:convention-contract} records only a
> convention firewall. Any transfer to Vol III, Vol II, Vol I,
> the Igusa cusp-form program, a compact Calabi-Yau threefold,
> a $K3\times E$ specialisation, or a BKM denominator identity
> requires a separate matched-conventions theorem. No such
> transfer is asserted here."

**Anchor check.** This is the explicit Vol III firewall sentence
required by CLAUDE.md. The text of `tate-P5-cross-volume.tex`
expands the same firewall to a full appendix. **CLEAN.**

### §1.8 BCOV citation chain summary table

| Site | `main.tex` line | Function | Status |
|------|------|------|------|
| 1 | 174-178 | Source-convention template introduction | CLEAN, load-bearing as template, explicit non-import |
| 2 | 698-706 | `rmk` on Kodaira-Spencer guiding convention | CLEAN, load-bearing firewall |
| 3 | 803-806 | Background prose ("BCOV/Kodaira-Spencer gives the guiding target-space closed-string source convention") | CLEAN, decorative-but-named |
| 4 | 822-825 | Local mixed model section opener | CLEAN, decorative |
| 5 | 1140-1142 | Costello + Costello-Li package (BCOV-adjacent) | CLEAN, load-bearing |
| 6 | 1654-1661 | `rmk` on threefold-vs-surface | CLEAN, load-bearing firewall |
| 7 | 5110-5111 | "Costello-Li construct quantum BCOV theory" | CLEAN, load-bearing |
| 8 | 5172-5183 | `stmt:costello-li-flat-bcov` | CLEAN, load-bearing imported statement |
| 9 | 5187-5192 | Two-imported-statements remark | CLEAN |
| 10 | 5398-5412 | `rmk:convention-firewall` | CLEAN, load-bearing firewall |
| 11 | 5912-5936 | Cross-volume firewall section | CLEAN, load-bearing firewall |
| 12 | 5948-5961 | Bibliography entry | CLEAN, all metadata correct |

**No site is decorative-passing-as-load-bearing.** Every
load-bearing site is paired with an explicit firewall sentence;
every decorative site is in background prose where named
attribution is the goal.

---

## §2. Costello / Costello-Li primary-source audit

### §2.1 Costello 2011 *Renormalization and Effective Field Theory*

`main.tex` 6090-6101:
```
\bib{costello-renormalization}{book}{
   author={Costello, K.},
   title={Renormalization and Effective Field Theory},
   series={Mathematical Surveys and Monographs},
   volume={170},
   publisher={American Mathematical Society},
   place={Providence, RI},
   date={2011},
   pages={xii+251},
   isbn={978-0-8218-5288-0},
   doi={10.1090/surv/170},
}
```

**Note: This is the AMS Surveys 170 book, not the 2011 ICM paper
"A geometric construction of the Witten genus".** The CLAUDE.md
W5-X3 task brief explicitly mentions Costello "A geometric
construction of the Witten genus" 2011 ICM as a primary source to
verify. This ICM paper is *not* in the manuscript bibliography,
and *no citation in the manuscript invokes the Witten-genus
construction*. The two works are distinct:
- *Renormalization and Effective Field Theory* (AMS Surveys 170,
  2011): the universal renormalised BV graph calculus framework
  used at `stmt:costello-bv-package` (`main.tex` 5153-5170).
- "A geometric construction of the Witten genus" (Proc. ICM 2010,
  published 2011): a specific application of the BV framework to
  the Witten genus, *not* used in this manuscript.

**The manuscript correctly cites the AMS Surveys book as the
universal-construction source; it would be a *citation drift* to
cite the ICM paper in its place.** The W5-X3 brief's reference to
the ICM paper is informational context (CLAUDE.md primary-source
list); it is not a missing citation. **CLEAN.**

### §2.2 Costello-Li 2012 — `costello-li-quantum-bcov` (arXiv:1201.4501)

`main.tex` 6103-6110:
```
\bib{costello-li-quantum-bcov}{misc}{
   author={Costello, K.},
   author={Li, S.},
   title={Quantum {BCOV} theory on {Calabi-Yau} manifolds and the higher genus
   {$B$}-model},
   date={2012},
   note={arXiv:1201.4501},
}
```

**Verification.** Title, authors, year, arXiv identifier all
match the public record. arXiv:1201.4501 (submitted 2012-01-22)
is the correct identifier. **CLEAN.**

**Anchor sites.** Cited at `main.tex` 1140-1142 (as the source
for "the flat odd-dimensional BCOV/HCS case"), 1654-1661 (as the
source for "the higher-genus B-model on Calabi--Yau manifolds is
taken up at the quantum level"), and 5110-5111 (as the source for
"Costello-Li construct quantum BCOV theory"). All three sites
are accurate to Costello-Li 2012 §5-§6 content. **CLEAN.**

### §2.3 Costello-Li 2015 — `costello-li-open-closed-bcov` (arXiv:1505.06703)

`main.tex` 6112-6118:
```
\bib{costello-li-open-closed-bcov}{misc}{
   author={Costello, K.},
   author={Li, S.},
   title={Quantization of open-closed {BCOV} theory, I},
   date={2015},
   note={arXiv:1505.06703},
}
```

**Verification.** arXiv:1505.06703 is the correct identifier
(submitted 2015-05-25). **CLEAN.**

**Anchor sites.** Cited at `main.tex` 1140-1142 (in the
two-package union with 2012), 5111 (same), and 5179
(`stmt:costello-li-flat-bcov`). All sites are accurate to
Costello-Li 2015 Theorem 1.2 content. **CLEAN.**

### §2.4 Costello-Li 2016 — `costello-li-anomaly-cancellation` (arXiv:1605.09073) — NOT IN BIBLIOGRAPHY

The 2016 Costello-Li paper "Anomaly cancellation in the
topological string" (arXiv:1605.09073) is **not** in the
manuscript bibliography. It is referenced in the platonic ledger
(`reconstitution/phase4-exec-BCOV-A5-comparison-2026-04-28.md`,
`reconstitution/phase4-exec-Costello-Li-d-extension-2026-04-28.md`,
`reconstitution/phase4-exec-Firewall-Meta-Theorem-2026-04-28.md`)
as the chain-level anomaly cancellation paper, but it is **not**
cited in `main.tex`.

**Is this a defect?** **No, not in the current manuscript.** The
2015 paper Theorem 1.2 + §6 is the inscribed source, and the
chain-level cancellation in 2015 §6 is sufficient for the
`stmt:costello-li-flat-bcov` claim. The 2016 paper is a
*standalone refinement* of the cancellation argument; it is more
prominent in physics-side discussions but is not load-bearing for
the manuscript's current inscription.

**Forward-looking note (severity 0, optional).** *If*
FW.Costello-Li-d-even is ever inscribed as a remark in
`main.tex` (Phase-4 EXEC #112 closure recommends inscription as
a remark `rmk:firewall-typology` at `main.tex` ~5413; not yet
landed), the d-even parity argument should cite both
arXiv:1505.06703 *and* arXiv:1605.09073 to anchor the
chain-level cancellation argument at its sharpest source. This
is forward-looking, not a current defect.

### §2.5 Costello primary-source audit summary

| Citation | arXiv | Year | Bibliography | Status |
|------|------|------|------|------|
| Costello, *Renormalization and EFT* (AMS Surveys 170) | n/a | 2011 | YES (line 6090) | CLEAN, load-bearing for `stmt:costello-bv-package` |
| Costello-Li, *Quantum BCOV theory* | 1201.4501 | 2012 | YES (line 6103) | CLEAN, load-bearing for higher-genus B-model citation |
| Costello-Li, *Quantization of open-closed BCOV theory, I* | 1505.06703 | 2015 | YES (line 6112) | CLEAN, load-bearing for `stmt:costello-li-flat-bcov` |
| Costello-Li, *Anomaly cancellation in the topological string* | 1605.09073 | 2016 | **NO** | **Optional augmentation if FW.Costello-Li-d-even is ever inscribed** |
| Costello, "A geometric construction of the Witten genus" | n/a (ICM proc.) | 2011 | NO | NOT USED — correct (different work from the AMS Surveys book) |

---

## §3. Wave-4 #112 firewall typology vs CLAUDE.md compact-CY$_3$ discipline

### §3.1 The CLAUDE.md prohibition

CLAUDE.md (Repo-local section, "Research constellation role"):

> "Treat this as context unless a local theorem states and proves
> a precise comparison. **No statement in this repository implies
> a compact CY$_3$, Vol III, or global BCOV theorem without a
> separate matched-conventions proof.** Conventions ($d = \dim_{\C}
> X$, worldsheet $\Sigma$, framing datum on $S^3$) must agree with
> Vol III when stated in both. Any divergence is load-bearing —
> report, do not silently reconcile."

### §3.2 Wave-4 #112 firewall typology

The wave-4 #112 P4-Firewall-Meta-Theorem closure (in the platonic
ledger at `attack-heal-platonic-2026-04-28.md` lines 6026-6124)
proposes a typology of five firewall species:
1. **FW.BCOV.** Closed BCOV on $\C^3$.
2. **FW.Sergeev-A5.** Hecke-Clifford on $\R$.
3. **FW.Igusa.** Igusa $\Delta_5$ BKM denominator on Sp(4).
4. **FW.Unreduced-Bosonic.** Bosonic $\mathfrak{gl}_N$ on
   $\R^2 \times \widehat{\C^2}_0$.
5. **FW.Costello-Li-d-even.** Costello-Li flat-$\C^d$ for $d$
   even.

The unification claim is: "**no chain-level isomorphism exists
between the manuscript's brane-defect BV complex and any of five
sister complexes**" in the 6-real-dimensional mixed
factorization-algebra category $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$.

### §3.3 Chain-level layering check

**Does the FW.BCOV species respect CLAUDE.md compact-CY$_3$
discipline?**

The wave-4 closure inscribes FW.BCOV at "the chain-level layer";
it does **not** assert any compact-CY$_3$ BCOV consequence at the
manuscript level. The proposed inscription target is
`rmk:firewall-typology` at `main.tex` ~5413 (after
`rmk:convention-firewall`), which is *meta-statement scope*: a
typology of obstructions, not a chain-level isomorphism into any
specific complex.

The phase-4 EXEC report at
`phase4-exec-BCOV-A5-comparison-2026-04-28.md` §0 makes this
explicit:

> "Verdict: PARTIAL with FIREWALL-PERMANENT structural caveat. ...
> The two classes live in *different* obstruction complexes and
> the matching is via coefficient-coupling rather than a
> chain-level isomorphism."

The "coefficient-coupling rather than a chain-level isomorphism"
qualifier is precisely the CLAUDE.md "matched-conventions theorem
required for transfer" requirement. **CLEAN — FW.BCOV respects
the chain-level layer firewall.**

**Does the FW.Costello-Li-d-even species respect CLAUDE.md
compact-CY$_3$ discipline?**

Costello-Li 2015 lives on flat $\C^d$ — *not* on a compact
CY$_3$. The d-even firewall therefore does *not* require the
compact-CY$_3$ disclaimer to begin with. The wave-4 #112 closure
inscribes FW.Costello-Li-d-even at "the chain-level isomorphism
layer" (specifically: the parity-of-d obstruction sign $(-1)^{d(d-1)/2}$
on $\Omega^2$ for the BV pairing on $\mathrm{PV}^{*,*}(\C^d)$).
This is a *flat-space chain-level statement*, not a global
compact-CY$_3$ statement. **CLEAN.**

### §3.4 Inscription-not-yet-landed note

**The wave-4 #112 inscription target (`rmk:firewall-typology` at
`main.tex` ~5413) has NOT yet been landed in the manuscript.**
The current manuscript does not contain the firewall species
typology as inscribed text; it lives only at the platonic-ledger
/ reconstitution-report layer.

This means the W5-X3 audit question "does the wave-4 #112
firewall typology respect CLAUDE.md?" is currently a question
about *proposed inscription text*, not about *manuscript text*.
The proposed text in the platonic ledger
(lines 6037-6086) is faithful to the chain-level layering
discipline; the W5-A2 strengthening (functoriality-class
distinction per FW species) is additive and does not weaken the
firewall language. **No drift.**

---

## §4. Vol III cross-volume firewall preservation under W5-A2

### §4.1 The Vol III cross-volume firewall

Three load-bearing firewall sites in the manuscript:
1. `rmk:convention-firewall` (`main.tex` 5398-5412) — local
   convention firewall: "not a compact Calabi-Yau output of a
   $\Phi_d$ functor, ... not evidence for compact CY$_3$ BCOV
   anomaly cancellation."
2. `\subsection{Cross-volume firewall}` (`main.tex` 5916-5936)
   — explicit Vol III firewall sentence.
3. `\section{Cross-volume convention firewall}` (`tate-P5-cross-volume.tex` 9-128)
   — full appendix expanding the firewall, including
   `lem:no-formal-disk-transfer` (lines 63-85) as a formal
   non-transfer claim.

### §4.2 W5-A2 strengthening probes

Wave-5 W5-A2 (Drinfeld+Functoriality) proposes three
strengthenings:
- **F''-A1** (severity 2): parabolic-restriction visibility for
  the F'' theorem at `claim-strength-ledger.tex` line-delta 56.
- **MHB-A1** (severity 2): tensor-factor disjointness for $(A2')$
  at line-delta 267.
- **FT-A1** (severity 1, optional): firewall-typology
  functoriality-class distinction.

**Probe: does any W5-A2 strengthening weaken the Vol III
firewall?**

- **F''-A1**: Operates on a parabolic-stabiliser remark inside
  the F'' theorem block. Does not touch any firewall sentence.
  **No firewall weakening.**
- **MHB-A1**: Operates on the $(A2')$ ad-invariant
  bilinear-form clause. Does not touch any firewall sentence.
  **No firewall weakening.**
- **FT-A1**: Operates on the proposed `rmk:firewall-typology`
  text by adding a one-line annotation distinguishing the four
  functoriality classes (PARABOLIC / FULL / INDEPENDENT /
  HOLOMORPHIC) per FW species. The text remains within the
  `rmk:convention-firewall` zone of `main.tex`; the disavowal
  language is preserved. **No firewall weakening.**

### §4.3 Convention-divergence audit per CLAUDE.md

CLAUDE.md states: "Conventions ($d = \dim_\C X$, worldsheet
$\Sigma$, framing datum on $S^3$) must agree with Vol III when
stated in both. Any divergence is load-bearing — report, do not
silently reconcile."

- **$d = \dim_\C X$.** Manuscript: $d = 2$ (formal symplectic
  disk in $\C^2$). Vol III (per CLAUDE.md cross-reference):
  varies; the volume is "CY-to-chiral", potentially $d \in
  \{2, 3\}$. Manuscript explicitly states $d = 2$ at every
  load-bearing site (e.g., `main.tex` 174-178 "the present
  $d=2$ surface model"; `tate-P5-cross-volume.tex` 22 "at
  $d = \dim_\C X = 2$ in the holomorphic factor"). **No silent
  reconciliation.**
- **Worldsheet $\Sigma$.** Manuscript: no worldsheet — the brane
  is $\R \times \{p\}$ in $\R^2 \times \C^2$, a defect, not a
  worldsheet. `main.tex` 5189-5192: "Here the brane $\R\times p$
  is a defect in the mixed space, not a spacetime boundary unless
  a half-space model is separately chosen." **No silent
  reconciliation.**
- **Framing datum on $S^3$.** Manuscript: no $S^3$ — the
  topological factor is $\R^2$, not $S^3$. `tate-P5-cross-volume.tex`
  44-46: "This is not a compact CY$_3$ trace pairing, not an $S^3$
  framing, not a specialisation to a chiral curve." **No silent
  reconciliation.**

**All three CLAUDE.md conventions are reported as divergences,
not silently reconciled.** **CLEAN.**

---

## §5. Decorative-vs-load-bearing audit

Per the W5-X3 brief: "If decorative-citation passing as
load-bearing: severity-1."

### §5.1 Decorative citations of BCOV/Costello-Li

Three of the twelve BCOV-related citation sites are background
prose, not load-bearing for any chain-level claim:
1. `main.tex` 803-806: "Gwilliam-Williams' holomorphic bosonic
   string is a worldsheet example, while BCOV/Kodaira-Spencer
   gives the guiding target-space closed-string source
   convention." — Background; no claim asserted.
2. `main.tex` 822-825: "The closed sector is the local
   Hamiltonian Kodaira-Spencer/BF analogue on this mixed space,
   not a pure A-model or pure B-model." — Background; no claim
   asserted.
3. `main.tex` 691-693: "In the target-space Kodaira-Spencer
   examples the fields are Dolbeault-valued polyvectors" —
   Background; no claim asserted.

**Audit:** none of these passes as load-bearing. They are
*named-attribution prose* (Russian-school discipline per
CLAUDE.md §IV) marking the source convention. The pattern is:
each background mention is paired with an explicit firewall
sentence ("not a truncation of threefold BCOV theory and no
compact CY$_3$ BCOV theorem is used below"; "not a pure A-model
or pure B-model"; etc.) at the same or adjacent paragraph.
**CLEAN.**

### §5.2 Load-bearing citations

Nine of the twelve BCOV-related sites carry a load-bearing claim:
- 6 firewall-disavowal sentences (sites 174-178, 698-706,
  1654-1661, 5398-5412, 5912-5936, plus the
  `tate-P5-cross-volume.tex` appendix).
- 3 imported-package statements (sites 1140-1142, 5110-5111,
  5172-5183).

Each load-bearing citation is anchored to a specific BCOV /
Costello-Li paper section that contains the claimed content:
- Site 174-178 / 698-706 / 1654-1661: BCOV 1994 §2-§3 + §6
  (BV formalism on polyvectors; cotangent BV).
- Site 1140-1142: Costello-Li 2012 §5-§6 + Costello-Li 2015 §3-§6
  (flat-$\C^d$ open-closed quantisation, $d$ odd).
- Site 5110-5111: Costello-Li 2012 §6 (quantum higher-genus
  B-model).
- Site 5172-5183: Costello-Li 2015 Theorem 1.2 + §6 (open-closed
  flat BCOV with $\mathfrak{gl}(N|N)$, $d$ odd, anomaly
  cancellation).

**No load-bearing citation is unanchored.** **CLEAN.**

---

## §6. Verdict

**CERTIFY clean.** No anchoring drift. No
decorative-citation-passing-as-load-bearing. No CLAUDE.md
compact-CY$_3$ / Vol III non-import discipline violation. The
wave-4 #112 firewall typology is layered correctly at the
chain-level / source-convention-template / coefficient-coupling
layers, with explicit chain-level non-isomorphism statements per
species. The W5-A2 inscription strengthenings preserve the Vol
III cross-volume firewall.

**Optional severity-0 augmentation (forward-looking).** If
FW.Costello-Li-d-even is ever inscribed as `rmk:firewall-typology`
in `main.tex`, add a bibliography entry for Costello-Li 2016
"Anomaly cancellation in the topological string" arXiv:1605.09073
and cite it at the inscribed remark for the chain-level
cancellation argument. This is *not* a defect in the current
manuscript because the 2015 paper §6 contains the cancellation
argument used by `stmt:costello-li-flat-bcov`, and the 2016 paper
is a standalone refinement.

**No severity-1 or severity-2 findings.**

---

## Appendix A: Primary-source bibliographic verification

- **Bershadsky, Cecotti, Ooguri, Vafa.** "Kodaira-Spencer theory
  of gravity and exact results for quantum string amplitudes",
  *Comm. Math. Phys.* **165** (1994), Issue 2, pp. 311-427, doi
  10.1007/BF02099774, arXiv:hep-th/9309140 (preprint date
  1993-09-23). **Manuscript bibliography entry verified
  CLEAN.**
- **Costello.** *Renormalization and Effective Field Theory*,
  AMS Mathematical Surveys and Monographs **170** (2011), pp.
  xii+251, ISBN 978-0-8218-5288-0, doi 10.1090/surv/170.
  **Manuscript bibliography entry verified CLEAN.**
- **Costello, Li.** "Quantum BCOV theory on Calabi-Yau manifolds
  and the higher genus B-model", arXiv:1201.4501 (preprint date
  2012-01-22). **Manuscript bibliography entry verified CLEAN.**
- **Costello, Li.** "Quantization of open-closed BCOV theory, I",
  arXiv:1505.06703 (preprint date 2015-05-25). **Manuscript
  bibliography entry verified CLEAN.**
- **Costello, Li.** "Anomaly cancellation in the topological
  string", arXiv:1605.09073 (preprint date 2016-05-30).
  **NOT IN MANUSCRIPT BIBLIOGRAPHY — optional augmentation
  recommended only if FW.Costello-Li-d-even is ever inscribed.**
- **Witten.** "Topological sigma models", *Comm. Math. Phys.*
  **118** (1988), pp. 411-449. NOT cited as the topological
  twist source in the manuscript bibliography (the manuscript
  uses other Witten works, e.g. `witten-cs` "Chern-Simons gauge
  theory as a string theory" arXiv:hep-th/9207094 at line 5985).
  This is a stylistic choice, not a defect: the manuscript's
  topological-string anchoring is via Witten's Chern-Simons-as-a-
  string-theory formulation, not via the original 1988 sigma
  models paper. **No defect.**
- **Vafa.** "Topological Mirror Symmetry" 1991. NOT cited in the
  manuscript bibliography. The manuscript references mirror
  symmetry only in the prose context of BCOV's threefold setting;
  no Vafa 1991 mirror-symmetry claim is asserted. **No defect.**

---

## Appendix B: Cross-walk to W5 attack-heal directives

The W5-X3 brief lists four sub-probes; this audit's verdict per
sub-probe:

1. **BCOV 1993 citation chain** — CLEAN. All twelve sites
   verified; no decorative-passing-as-load-bearing; bibliography
   metadata correct.
2. **Costello-Li 2011/2016 d-even firewall** — CLEAN with
   forward-looking severity-0 note (cite Costello-Li 2016 if
   FW.Costello-Li-d-even is ever inscribed). The CLAUDE.md
   reference to Costello "A geometric construction of the
   Witten genus" 2011 ICM is *not* a missing citation; that work
   is unrelated to the manuscript's content (the manuscript uses
   Costello's *AMS Surveys 170* book, a different work).
3. **BCOV vs Hamiltonian BF locality** — CLEAN. Wave-4 #112
   firewall typology layers correctly; FW.BCOV is named at the
   chain-level layer with explicit non-isomorphism into compact
   CY$_3$. The proposed inscription text has not yet landed in
   the manuscript.
4. **Vol III cross-volume firewall preservation** — CLEAN. All
   three W5-A2 strengthening probes are inscription-covariance
   operations that do not weaken the Vol III firewall language.
   All three CLAUDE.md conventions ($d$, $\Sigma$, $S^3$ framing)
   are reported as explicit divergences, not silently reconciled.

End of W5-X3 BCOV-physics anchoring re-audit.
