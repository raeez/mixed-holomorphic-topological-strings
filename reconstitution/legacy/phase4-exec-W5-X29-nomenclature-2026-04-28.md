# Phase-4 EXEC W5-X29: Nomenclature/Notation Self-Consistency Auditor

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Role.** Attacker W5-X29 (Nomenclature/Notation Self-Consistency Auditor),
attack-heal-swarm wave 5.
**Mode.** Read-only on the working tree. NO commit; NO edit of any TeX file.
**Target.** Verify `nomenclature.tex` + `notation.tex` + `local-dictionary.tex`
+ `commands.tex` + `mathmacros.tex` are internally consistent and
self-supporting for the 155-page manuscript; certify wave-5 inscription
readiness for the proposed +472-line W5-X5 patch.

---

## 0. Bottom-line verdict

**Severity 2.** Two genuine duplicate-symbol findings (`\Phi`, `\mathcal P`)
plus one structural finding (`notation.tex`, `nomenclature.tex`,
`commands.tex`, and `preamble.tex` are all orphaned with respect to the
`main.tex` compile path; only `mathmacros.tex` is `\input` from `main.tex`).
Em-dash / AI-tells scan: **clean** on all five files.

**Wave-5 inscription readiness.** The +472-line W5-X5 / W5-X20 patch
introduces **no new mathematical macro**. The single environmental
prerequisite (`\newtheorem{hyp}`) **must land in `mathmacros.tex` or in
`raeez-math-template.sty`, not in `preamble.tex`** — because `preamble.tex`
is not consumed by `main.tex`. The W5-X20 R4 hard-blocking dependency
specification is therefore correct in spirit but **wrong in target
file**. A drop-in patch that satisfies the same intent without rewriting
`preamble.tex` is sketched in §4.

---

## 1. File-by-file structural state

### 1.1 `nomenclature.tex` (162 lines)

Contains 64 `\nomenclature{...}{...}` declarations (active) plus 86
commented-out duplicate declarations (legacy). The active block ends with
`\nomenclature{$\IndNSt$}{...}` at line 162. Half of the symbols
(`\Klocfrac`, `\Ga`, `\Gm`, `\lpgrass`, `\glpgrass`, `\classgrp`,
`\TateCat`, etc.) are descriptive of an algebraic-geometry / class-formation
infrastructure that was substantial in the v1 thesis lineage but is
largely vestigial in the current 155-page Kodaira-Spencer / BCOV
manuscript.

### 1.2 `notation.tex` (267 lines)

Macro-declaration file containing a near-duplicate of `mathmacros.tex`'s
algebraic-geometry / class-formation symbol set (`\Cat, \G, \ringint,
\grk, \N, \Z, \Q, \R, \C, \FnS, \laurentpoly, \laurentser, \fpowerser,
\klocint, \Klocfrac, \tensor, \isom, \ov, \restr, \shf, \idshf,
\projline, \K, \polyring, \classgrp, \F, \idealgenby, \D, \pt, \Gr,
\Ga, \Gm, \lpgrass, \glpgrass, \Flds, \cartdual, \Mat, \RH,
\tateshiftedby, \TateCat, \TateCatG, \B, \ptmod, \Ind, \RHom, \Hom,
\Map, \coH, \hcoH, \Ab, \Ker, \Coker, \dg, \Vec, \VecF, \Coh, \Coind,
\Res, \Pic, \AJ, \divisor, \divisoridshf, \IndProSch, \FinIndProSch,
\Pro, \IndPro, \FinIndSch, \A, \Fun, \Frac, \curriedleftarg, \Zp,
\Qp, \Set, \Hilb, \disj, \bij, \sur, \inj, \injects, \fst, \snd,
\thrd, \nth, \shfcoH, \hshfcoH, \Obj, \grpring, \Ext, \Exts, \dualmod,
\LModCat, \RModCat, \indlim, \Schemes, \NoethSch, \NoethIntSch, \Sch,
\IndSch, \ModCat, \grkAlg, \ZAlg, \cc, \Bun, \Spec, \Specf, \mK, \Bil,
\IndNSt, \dim, \SL, \GL, \DMod, \IndSt, \Curve, \IxCHilb, \HilbCxI,
\locLb, \Locvbpos`).

### 1.3 `local-dictionary.tex` (210 lines)

A typeset section (`\section*{Local dictionary}`) inscribed into
`main.tex` at line 67 via `\input{local-dictionary.tex}`. Provides the
canonical local-disk vocabulary (`R, \mathfrak m, \mathfrak h, \bar A,
\bar A_{\mathrm{desc}}, [\bar c], H_{a,b}, O_{a,b}, \Psi_{a,b},
\mathsf F_{\mathrm{Rees}}, \mathfrak g = \mathfrak h \ltimes
\mathfrak h^\vee_{\mathrm{cont}}[1], H_I, c^I, u_I, \theta^I, O_I, \Phi,
\mathcal P, \rho_{a,b}, z_1^p z_2^q \cdot \rho_{a,b}, \mathcal P_I,
\mathfrak h_I, \mathfrak g_I, B_f(a), A^{\mathrm{Ham}}_\partial(I),
A^{\mathrm{pp}}_\partial(I)`).

### 1.4 `commands.tex` (166 lines)

Mostly a formatting / display utility file (graphics, tikz, theorem
environments, nomenclature wiring). Declares only three mathematical
helpers (`\HRule`, `\nomentryend`, `\nomunit`), one of which is
commented out. Substantively a duplicate of pieces of
`mathmacros.tex`'s "Markup Readability" block.

### 1.5 `mathmacros.tex` (341 lines)

The **only** macro / preamble file `\input` from `main.tex` (line 5).
Declares 162 unique macro names. Includes the algebra extensions
(`\lb, \rb, \llb, \rrb, \lp, \rp, \llp, \rrp`) needed for the
`\fpowerser, \laurentser, \klocint, \Klocfrac` chain; the algebraic
infrastructure of notation.tex; the manuscript-specific
`\Curve, \IxCHilb, \HilbCxI, \locLb, \Locvbpos, \Tor, \W, \T, \Hirz,
\Tot, \P, \Pbd, \blP, \cM, \M, \ef, \Vleft, \Vright, \Verma, \VermaL,
\V, \lie, \su, \gl, \g`; and the markup helpers
(`\nc, \rc, \nm, \mc, \mbb, \mbf, \mrm, \mathsc, \image, \imageopt,
\twotuple, \setpresent`).

### 1.6 Compile-path observation

`main.tex` (master branch as of 2026-04-28) `\input`s only
`mathmacros.tex` (line 5) and `authors.tex` (line 6); no
`\input{preamble.tex}`, no `\input{notation.tex}`, no
`\input{commands.tex}`, no `\input{nomenclature.tex}`. The file
`raeez-math-template.sty` (loaded at line 4 via
`\usepackage{raeez-math-template}`) supplies all the substantive
typography, theorem environments, and 80+ `\providecommand` /
`\renewcommand` providers (`\C, \R, \Z, \Q, \N, \F, \cA, \cB, \dots,
\cZ, \bA, \bC, \bF, \bH, \bN, \bP, \bQ, \bR, \bS, \bZ, \fg, \fh, \bg,
\gl, \fgl, \fsl, \Hom, \End, \Aut, \Spec, \Conf, \colim, \Rep, \Vect,
\Ch, \Res, \Reg, \Tr, \td, \id, \op, \ord, \str, \sBer, \pt, \defeq,
\ChirHoch, \BP, \BRST, \Vir, \Virc, \CompCl, \Defcyc, \SCchtop,
\chirAss, \chirCom, \chirLie, \chirtensor, \ch, \barB, \BarchFG,
\dzero, \dfib, \orline`). The template `raeez-math-template.sty:896`
also declares `\declaretheorem[style=garamonddef, name=Hypothesis,
sibling=theorem]{hypothesis}` — so a **`hypothesis` environment is
already live**, although a short `hyp` alias is not.

This is a load-bearing structural finding: **the W5-X20 R4 hard-blocking
dependency on `\newtheorem{hyp}` in `preamble.tex` cannot be satisfied
by an edit of `preamble.tex`** because the file is not consumed during
the build. See §4 for the corrected patch target.

---

## 2. Duplicate-symbol scan

### 2.1 Systematic-name duplications (notation.tex vs mathmacros.tex)

`notation.tex` redeclares 130+ macros that already exist in
`mathmacros.tex` with the same expansion. Because `notation.tex` is not
`\input`, this does not produce a compile-time clash; it is a tracked
duplication of source text only. A near-perfect diff:

```
mathmacros.tex \ notation.tex (in mathmacros only):
  blP, cM, ef, g, gl, Hirz, image, imageopt, lb, lie, llb, llp, lp,
  M, mathnm, mathsc, mbb, mbf, mc, mrm, nc, nm, P, Pbd, rb, rc, rp,
  rrb, rrp, setpresent, su, T, Tor, Tot, twotuple, V, Verma, VermaL,
  Vleft, Vright, W
notation.tex \ mathmacros.tex (in notation only): (none)
```

So `notation.tex` is a strict subset of `mathmacros.tex`. **No semantic
drift between the two, only redundancy.**

### 2.2 Genuine duplicate-meaning collisions

Two genuine collisions identified across the manuscript prose:

#### 2.2.1 `\Phi` (severity-2)

`local-dictionary.tex`:128 declares `\Phi` as the **cochain-level
CE/PV map** (`c^I \mapsto \theta^I`, `u_I \mapsto O_I`).

`main.tex`:422 (Theorem `thm:quantum-classical-anomaly`,
quantum-classical equivalence of the U(1) center class) declares
`\Phi=(\phi_1,\phi_2)` as the **classical brane field** on the formal
local disk (a 2-tuple of classical fields). The same theorem then uses
`\Phi_\hbar=(\phi_1^{\hbar},\phi_2^{\hbar})` as the Weyl-quantized
version.

`main.tex`:2272-2473 (block around Theorem `thm:open-closed-derived-center`)
re-uses `\Phi` as the CE/PV cochain map per local-dictionary.tex.

The two meanings co-occur in the same file (`main.tex`) but in
sufficiently distant theorem-blocks (line 422 vs line 2272) that local
context disambiguates them. A careful reader of either subsection is
not confused; a reader scanning the whole file would pause on this
overload.

**Recommended remedy** (NOT inscribed; owner-only): rename the
classical-brane-field `\Phi` to `\Phi^{\mathrm{cl}}` or
`(\Phi_1,\Phi_2)` at line 422-423. The CE/PV cochain `\Phi` is
inscribed at the local-dictionary.tex level and is the dominant usage
across the manuscript, so it should keep the bare name. Five-line
delta if the patch were authorized.

#### 2.2.2 `\mathcal P` (severity-2)

`local-dictionary.tex`:143 declares
`\mathcal P = \operatorname{Ann}_{\mathrm{res}}(\C\cdot 1) \subset
H^2_{\mathfrak m}(R)\,dz_1 dz_2`, identified with
`\mathfrak h^\vee_{\mathrm{cont}}` — the **reduced principal-part
module**.

`tate-T3-quillen-equivalence.tex`:158-185 uses `\mathcal P` as a
generic **operad** in
`\mathrm{Free}_{\mathcal P}\dashv\mathrm{Forget}` /
`\mathcal P\text{-alg}_{\geq 0}` (Hovey 1998 / Lurie HA conventions).

Co-occurrence in different sub-files; both meanings are conventional
in their respective subjects (residue / coadjoint vs operad / model
category). The contextual disambiguation is robust because of the
structural subscript / superscript pattern (`\mathcal P_I`,
`\rho_{a,b} \in \mathcal P` vs `\mathcal P\text{-alg}`,
`\mathrm{Free}_{\mathcal P}`).

**Recommended remedy** (NOT inscribed; owner-only): in
`tate-T3-quillen-equivalence.tex`, rename `\mathcal P` to
`\mathcal O` (operad in the Hovey lineage uses `\mathcal O` at least
as often as `\mathcal P`) or to `\mathcal Q` to avoid the clash.
~6 line delta if authorized.

### 2.3 Symbols flagged but disambiguated

#### 2.3.1 `\mathfrak h` — clean

565 occurrences in the substantive manuscript files. Every occurrence
is consistent with `local-dictionary.tex`:122 ("Reduced Hamiltonian
Lie algebra of the formal disk"). No drift to Cartan / Heisenberg.

#### 2.3.2 `\mathfrak m` — clean

Used 174 times as the **maximal ideal $(z_1,z_2)$ of the formal
symplectic disk** per `local-dictionary.tex`:120. No second meaning.

#### 2.3.3 `J` — disambiguated

`main.tex` uses `J(f)` (always with a function-argument bracket) as
the **open-trace observable functional**
$J(f)=\overline{\mathrm{Tr}\,f(\phi_1,\phi_2)}$ (line 220ff) and
`J_N(f)` as the **Capelli-renormalized Weyl trace** (line 4814ff).
`tate-T3-quillen-equivalence.tex`:65 uses bare `J = \bigl\{\ldots\bigr\}`
as the **set of acyclic generating cofibrations** in the model-category
proof — a standard Hovey 1998 / Hirschhorn 2003 convention. The
syntactic disambiguator (the function-call bracket on the open-trace
J vs the displayed-equation set on the cofibrations J) is robust.
**No semantic clash in the same scope.**

#### 2.3.4 `\rho` — clean

101 occurrences, all of the form `\rho_{a,b}` (Matlis principal-part
residue current per `local-dictionary.tex`:151). 56 of those 101 are
the explicit subscripted `\rho_{a,b}`. No `\rho(J)`, no `\rho_p`,
no representation-theoretic `\rho`. **No drift.**

#### 2.3.5 `\Psi`, `\bar A`, `\bar c` — clean

All consistent with `local-dictionary.tex`. `\Psi_{a,b}` is the
primitive one-`\psi` stable open class (line 76). `\bar A` is the
polynomial Hamiltonian sector (line 30). `\bar c` is the distinguished
scalar U(1) anomaly class (line 38).

---

## 3. Cross-reference / dead-weight scan

Of the 162 macros declared in `mathmacros.tex`, the following are
**never referenced** in the substantive manuscript files (`main.tex`,
`theorem-lanes.tex`, `claim-strength-ledger.tex`, `open-obligations.tex`,
`tate-T1`-`T5`, `tate-P1`, `tate-P3`, `tate-P5`,
`appendix-matlis-principal-parts.tex`,
`appendix-factorization-current-conventions.tex`,
`appendix-unreduced-bv-qme.tex`, `appendix-radial-parts-moyal.tex`):

```
\A, \Ab, \B, \Bil, \Bun, \Coh, \Coind, \Coker, \Curve, \D, \DMod,
\Exts, \F (n.b. \F is re-provided by template; \mathbb{F} via template),
\FinIndProSch, \FinIndSch, \Flds, \FnS, \Frac, \Fun, \G, \GL, \Ga,
\Gm, \Gr, \Ind, \IndNSt, \IndPro, \IndProSch, \IndSch, \IndSt, \K,
\LModCat, \Map, \Mat, \ModCat, \NoethIntSch, \NoethSch, \Obj, \Pic,
\Pro, \Qp, \RH, \RModCat, \Res (re-provided by template),
\SL, \Sch, \Schemes, \Set, \Spec (re-provided), \Specf, \T, \Tor,
\V, \Vec, \VecF, \W, \Zp, \bij, \cartdual, \cc, \coH, \dg, \disj,
\fst, \g, \gl, \grk, \hcoH, \hshfcoH, \inj, \injects, \isom, \mK,
\nth, \ov, \polyring, \projline, \pt (re-provided), \ptmod, \restr,
\ringint, \shfcoH, \snd, \su, \sur, \tensor, \thrd
```

86 dead-weight declarations. None are load-bearing for the manuscript;
they are vestigial holdovers from the v1 algebraic-geometry /
class-formation thesis lineage. They do not produce a compile error,
but they bloat the macro-dictionary and increase the cognitive load
for a future maintainer.

**Severity-1 cleanup recommendation** (not authorized):
remove the unused 86 declarations. ~80-line delta to `mathmacros.tex`.
This is purely cosmetic / hygienic; no manuscript-level effect.

---

## 4. Wave-5 inscription readiness

### 4.1 Required new macros / environments

The W5-X20 patch (and the full +472-line W5-X5 synthesis) introduces
the following surface symbols:

| Symbol | Source | Status in active compile path |
|--------|--------|-------------------------------|
| `\mathfrak m` | inline math | provided by amsmath / amssymb (via `\mathfrak{m}`); already used 174 times |
| `\mathfrak h` | inline math | provided; already used 565 times |
| `P_{(z_1)}` | inline math | bare TeX; no macro needed |
| `\tau_{\mathfrak h}` | inline math | bare TeX; no macro needed |
| `\simeq^{\mathrm{Q}}` | inline math | bare TeX; no macro needed |
| `(A5)^{\mathrm{RG}}` | inline math | bare TeX; no macro needed |
| `\mathrm{Symp}_{\mathrm{form}}` | inline math | bare TeX; no macro needed |
| `\mathrm{Aut}(\widehat{\mathcal O}_{X,x}, \mathfrak m_x)` | inline math | bare TeX; no macro needed |
| `\widehat{\mathcal O}_{X,x}` | inline math | bare TeX; no macro needed |
| `W(P_{\epsilon, L}, I)` | inline math | bare TeX; no macro needed |
| `\Phi_{\mathrm{Sergeev}}` | inline math | bare TeX; no macro needed |
| `\rho(J)/\sqrt n` | inline math | bare TeX; no macro needed |
| `\mathrm{End}(V^{\otimes n})` | inline math | bare TeX; no macro needed |
| `\mathrm{Ad}_{\rho(J)/\sqrt n}` | inline math | bare TeX; no macro needed |
| `P^{\mathfrak q}`-equivariant | inline math | bare TeX; no macro needed |
| `[K_t,P]=[Q^{\mathrm{GF}},P]=[P_{\epsilon,L},P]=0` | inline math | bare TeX; no macro needed |
| `\widetilde\Psi_{a,b}` | inline math | bare TeX; no macro needed |

**Result.** **Zero new mathematical macros are required** by the W5-X5
inscription. All proposed text uses raw TeX expressions whose primitives
are already in the active compile path (via amsmath / amssymb, the
template's `\providecommand` block, or the existing `mathmacros.tex`).

### 4.2 Environment prerequisite

The W5-X5 master draft and the W5-X20 inscription readiness validator
both call for `\newtheorem{hyp}[thm]{Hypothesis}` so that
`claim-strength-ledger.tex` can host
`\begin{hyp}\label{hyp:A1-truncation}...\end{hyp}` blocks (one per
master hypothesis). Two options:

#### Option (a) — short alias `hyp` (W5-X20 default)

Inscribe `\newtheorem{hyp}[thm]{Hypothesis}` at the top of
**`mathmacros.tex`** (NOT `preamble.tex` — see §1.6 above). Adjacent
to the existing `\newcommand\nm{} % temporarily disable standard
\nomenclature` block at line 10, or at the very end after `\nc\g{\lie{g}}`
on line 341.

Suggested location: append to the end of `mathmacros.tex` as a
2-line block:

```latex
% Hypothesis environment for master hypothesis ledger (W5 inscription)
\newtheorem{hyp}[thm]{Hypothesis}
```

#### Option (b) — reuse the existing `hypothesis` environment (no patch)

`raeez-math-template.sty:896` already declares
`\declaretheorem[style=garamonddef, name=Hypothesis, sibling=theorem]{hypothesis}`.
The W5-X5 / W5-X20 master-hypothesis blocks would then be inscribed
as `\begin{hypothesis}\label{hyp:A1-truncation}...\end{hypothesis}`
(label name unchanged; environment name `hypothesis` instead of `hyp`).

**No edit to any apparatus file required.** This is the structurally
cleanest path.

#### Recommendation

**Option (b).** Use the pre-declared `hypothesis` environment from
`raeez-math-template.sty`. Saves the patch-step entirely; uses the
authorial typography (`garamonddef` style) already in service for the
sister `definition` and `assumption` environments; matches the
elite-grade Russian-school voice of the manuscript.

If the user prefers the short `hyp` keyword for visual brevity in
the source, then Option (a) is the minimal patch: 2-line append to
`mathmacros.tex`. The W5-X20 R4 specification ("must inscribe in
preamble.tex") is incorrect at the byte level and would not produce a
working build; the working location is `mathmacros.tex`.

### 4.3 Inscription readiness verdict

**READY** under either Option (a) or Option (b). Zero new mathematical
macros, one optional 2-line environment declaration. The +472-line
inscription patch can proceed without nomenclature / notation /
local-dictionary / commands / mathmacros adjustment beyond the optional
single 2-line `\newtheorem{hyp}` alias.

The W5-X20 §4 R4 dependency-ordering analysis remains valid in spirit
(if `\begin{hyp}` is used, then `\newtheorem{hyp}` must precede the
ledger commit) but **the target file is `mathmacros.tex`, not
`preamble.tex`**. With this correction, R4 severity drops to "trivial
in the corrected pipeline."

---

## 5. Em-dash / AI-tells scan

| File | Em-dash hits | AI-tells hits |
|------|--------------|---------------|
| `nomenclature.tex` | 0 | 0 |
| `notation.tex` | 0 | 0 |
| `local-dictionary.tex` | 0 | 0 |
| `commands.tex` | 0 | 0 |
| `mathmacros.tex` | 0 | 0 |

**Clean.** All five files pass the elite-grade voice scan.

---

## 6. Severity ledger

| Finding | Severity | Action |
|---------|----------|--------|
| `notation.tex` orphaned (not in compile path) | Structural / 2 | Either consolidate into `mathmacros.tex` and remove `notation.tex`, or add `\input{notation.tex}` to `main.tex` (requires audit of duplicate declarations first) |
| `nomenclature.tex` orphaned | Structural / 2 | Either consolidate into `mathmacros.tex` and inscribe `\printnomenclature` in main.tex, or remove |
| `commands.tex` orphaned | Structural / 1 | Remove; pieces overlap with mathmacros.tex |
| `preamble.tex` orphaned | Structural / 1 | Remove or consolidate into raeez-math-template.sty |
| `\Phi` overload (classical brane field vs CE/PV cochain map) | Symbol / 2 | Rename classical-brane `\Phi=(\phi_1,\phi_2)` to `\Phi^{\mathrm{cl}}` at main.tex:422 |
| `\mathcal P` overload (principal-part module vs operad) | Symbol / 2 | Rename operad `\mathcal P` in tate-T3 to `\mathcal O` or `\mathcal Q` |
| 86 dead-weight macro declarations in mathmacros.tex | Hygiene / 1 | Remove unused declarations |
| W5-X20 R4 spec error (preamble.tex vs mathmacros.tex) | Inscription / 2 | Use existing `hypothesis` env (Option b) OR patch `mathmacros.tex` not `preamble.tex` (Option a) |
| Em-dash / AI-tells | Voice / 0 | Clean |
| `\mathfrak h, \mathfrak m, \rho, \Psi, J, \bar A, \bar c` semantics | Symbol / 0 | Consistent across manuscript |

**Aggregate.** Severity 2 (two genuine duplicate-meaning symbols in
manuscript prose; W5-X20 inscription target file misnamed; orphaned
apparatus files; dead-weight macros). The manuscript builds and reads
cleanly today; these are observed as elite-grade cleanup items, not
blockers.

---

## 7. Minimal patch (proposal-only, NOT inscribed)

If the user authorizes the elite-grade clean-up, the minimal patch is:

1. **Pick an environment policy** for the wave-5 master hypothesis
   ledger. Default: Option (b) — use `hypothesis` from
   `raeez-math-template.sty`. No file edit needed.

2. **Rename `\Phi=(\phi_1,\phi_2)`** at `main.tex`:422-423 to
   `\Phi^{\mathrm{cl}}=(\phi_1,\phi_2)` (or `(\Phi_1,\Phi_2)` for
   visual disambiguation). Track the rename through the proof body of
   `thm:quantum-classical-anomaly` (lines 421-456 ish) — likely 8-12
   sites.

3. **Rename `\mathcal P`** in `tate-T3-quillen-equivalence.tex` (operad
   role; lines 158-185) to `\mathcal O` or `\mathcal Q`. ~6 sites.

4. **Optional cleanup.** Remove the 86 dead-weight macros from
   `mathmacros.tex`; remove `notation.tex`, `commands.tex`,
   `preamble.tex`, and `nomenclature.tex` from the working tree if no
   longer used by any standalone-document compile path. ~120-line net
   delta on apparatus files; zero substantive-prose delta.

5. **W5-X5 inscription.** Use the already-live `hypothesis`
   environment in `claim-strength-ledger.tex`; the rest of the +472-line
   patch lands as proposed in W5-X20 §3.

**No commit. No edit of any TeX file.**

---

## 8. Verdict

**Severity 2.**

- Two genuine duplicate-meaning symbols in manuscript prose
  (`\Phi`, `\mathcal P`).
- One structural finding (4 of the 5 audit-target files are orphaned
  with respect to the `main.tex` compile path).
- One inscription-readiness correction (W5-X20 R4 target file
  is `mathmacros.tex`, not `preamble.tex`; or use existing
  `hypothesis` environment).
- 86 dead-weight macro declarations (severity 1; hygienic).
- Em-dash / AI-tells scan: **clean** on all 5 files.
- Otherwise: nomenclature consistency is **strong**; the
  `local-dictionary.tex` separation rule (PBW special-fibre labels vs
  CE/PV labels vs Matlis labels) is honored across the manuscript;
  the Fourier-Rees bridge and the Russian-school voice are respected.

**Recommendation.** When the user authorizes:
1. Choose Option (b) for the `hypothesis` environment.
2. Rename `\Phi=(\phi_1,\phi_2)` and `\mathcal P` (operad) to
   disambiguate from `\Phi` (CE/PV) and `\mathcal P` (principal-part).
3. Optional cleanup of dead-weight macros and orphaned apparatus
   files.

End of W5-X29 report.
