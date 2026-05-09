# Phase-4 EXEC W5-X7: Convention-Firewall Sharpening Drafter

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Mode.** Proposal-only. No commit. No edit to `main.tex`.
**Wave.** 5, attacker X7.
**Target.** `rmk:convention-firewall` at `main.tex:5397-5411`.
**Provenance.** W5-X1 cross-volume audit identified the sharpening
as severity-0 / optional: "add one-sentence pointer in
topological-strings `rmk:convention-firewall` noting that each
sister volume likewise declares its own scope."

---

## 1. Verification of need

The current remark text (lines 5397-5411) reads, in compressed
form:

> This local Hamiltonian BF sector is not a compact Calabi-Yau
> output of a $\Phi_d$ functor, carries no $\kappa_{\mathrm{ch}}$
> or $\kappa_{\mathrm{BKM}}$ consequence, and is not evidence for
> compact CY$_3$ BCOV anomaly cancellation. The Moyal computation
> below is local deformation quantization of a formal symplectic
> disk. A closed-open factorization source is extra structure:
> descent, QME/anomaly cancellation, completion, and the
> specialization or defect map must be supplied before one may
> pass from a formal coefficient calculation to a Costello graph
> realization. The Weyl algebra fixes the target coefficients;
> it does not reconstruct the elliptic BV source. In particular
> the formal disk carries no compact Calabi-Yau datum, no $K3
> \times E$ specialization, no chosen $(\Sigma,C)$ specialization,
> no Igusa cusp form, no Borcherds input form, no BKM denominator
> identity, and no Stage-1 or Stage-2 $\Phi_d$ specialization.

The remark declares the local-side scope discipline. It does **not**
declare that the sister volumes (Calabi-Yau quantum-groups Vol III,
chiral bar-cobar Vols I/II, Igusa cusp-form program) declare their
own scope discipline along the same line. The W5-X1 audit observed
that this leaves the firewall asymmetric: the topological-strings
side renounces, but the reader is not told the sister volumes
renounce in the corresponding direction. The optional sharpening
restores the symmetry inside the remark itself, where a reader
naturally looks.

A closely related pointer appears later in the manuscript at line
5933 ("Any transfer to Vol III, Vol II, Vol I, the Igusa cusp-form
program ... requires a separate matched-conventions theorem"), but
that pointer lives in `ssec:cross-volume-horizon`, far from the
remark. The remark itself remains one-sided.

**Verdict.** The pointer is needed inside the remark.

---

## 2. Drafted pointer

```latex
  Each sister volume declares its own scope discipline along the same
  line: Vol III of the Calabi-Yau quantum-groups program, Vols I and II
  of the chiral bar-cobar program, and the Igusa cusp-form program each
  state separately what they assert and what they do not, and a transfer
  between volumes is a separate matched-conventions theorem rather than
  an implication of any one volume.
```

This is one prose sentence wrapped to manuscript column-width
(80 columns by inspection of surrounding lines). Total +6 lines of
TeX, within the +2 to +4 sentence-equivalent budget the W5-X7
charter allowed.

### Voice alignment

The drafted sentence uses the same voice as the existing remark:
declarative third-person nominal, no first-person plural, no
hedging modal. It mirrors the existing remark's terminating
anaphoric structure ("no X, no Y, no Z") with a parallel
volume-list ("Vol III ..., Vols I and II ..., Igusa cusp-form
program ..."). The final clause ("a transfer ... is a separate
matched-conventions theorem rather than an implication of any one
volume") echoes the manuscript's existing line at 5933 without
duplicating it.

### Naming convention

Volumes are cited by mathematical-program name:

* "Vol III of the Calabi-Yau quantum-groups program" — not
  `~/calabi-yau-quantum-groups`.
* "Vols I and II of the chiral bar-cobar program" — not
  `~/chiral-bar-cobar`.
* "the Igusa cusp-form program" — not `~/igusa-cusp-form`.

This matches the existing house style at line 5933 ("Vol III,
Vol II, Vol I, the Igusa cusp-form program").

---

## 3. Scans

### 3.1 Em-dash / en-dash scan

Inspected character-by-character for `--`, `---`,
`\textemdash`, `\textendash`, U+2014, U+2013, and any compound
glyph that would render as an em-dash. The draft contains only:

* commas: 4
* one colon (after "along the same line:")
* hyphens inside compound nouns: "bar-cobar", "cusp-form",
  "matched-conventions", "Calabi-Yau", "quantum-groups"

No em-dashes. No en-dashes. **PASS.**

### 3.2 AI-tells / draft-language scan

Checked the draft against the standard AI-tell list:

| Tell | Present? |
|------|----------|
| "delve" | no |
| "leverage" | no |
| "robust" | no |
| "comprehensive" | no |
| "seamless" | no |
| "moreover" / "furthermore" | no |
| "in conclusion" | no |
| "this paper presents" | no |
| "let us" / "we shall" | no |
| "rich tapestry" | no |
| "elucidate" | no |
| "underscore" | no |
| "as we have seen" | no |
| any first-person plural marketing voice | no |

No AI tells. **PASS.**

### 3.3 Agent / swarm / ledger / draft-process scan

Checked for: "agent", "swarm", "ledger", "wave", "phase",
"attack", "heal", "audit", "sharpening", "drafter", "exec",
"reconstitution", "task", "GPT", "Claude", "Codex", "harness",
"chunked-workflow", "subagent". None present.

**PASS.**

---

## 4. Re-attack

### 4.1 Drinfeld functoriality

Does the pointer create or break parabolic-restriction structure?

The pointer makes no claim about a functor between categories, no
claim about Drinfeld center, no claim about chamber-wall structure,
no claim about $\Phi_d$ functoriality, and no claim about parabolic
restriction. It declares only a meta-discipline on cross-volume
claim transfer. The pointer does not assert any functor; it
therefore cannot break parabolic-restriction.

**Verdict.** Drinfeld-clean. **PASS.**

### 4.2 Witten boundary visibility

Does the pointer expose internal scaffolding (worktree paths,
directory names, agent tooling, slug-form labels)?

* Directory paths: none. The draft uses only mathematical-program
  names.
* Slug-form labels: none.
* Agent tooling: none.
* Filesystem boundary leak: none.

The reader of the manuscript sees only mathematical objects.

**Verdict.** Witten-clean. **PASS.**

### 4.3 Polyakov-class invariance

Does the pointer claim cross-volume Polyakov-class identity (a
single Polyakov class shared between volumes, or conformal-anomaly
cancellation in one volume implying it in another)?

The pointer's mathematical content is precisely the negation:
"each state separately what they assert and what they do not, and
a transfer between volumes is a separate matched-conventions
theorem rather than an implication of any one volume". The pointer
explicitly **denies** unmediated cross-volume Polyakov-class
identity. It does not implicitly assert one through any other
channel: there is no shared Polyakov class invoked, no anomaly
parameter named, no central charge identity asserted.

**Verdict.** Polyakov-firewall preserving. **PASS.**

---

## 5. Insertion proposal

**Site.** `main.tex:5411`, immediately before `\end{rmk}` of
`rmk:convention-firewall`.

**Mode.** Strict-additive. No deletion. No reordering.

**Diff sketch.**

```latex
  Igusa cusp form, no Borcherds input form, no BKM denominator identity, and no
  Stage-1 or Stage-2 $\Phi_d$ specialization.
+ Each sister volume declares its own scope discipline along the same
+ line: Vol III of the Calabi-Yau quantum-groups program, Vols I and II
+ of the chiral bar-cobar program, and the Igusa cusp-form program each
+ state separately what they assert and what they do not, and a transfer
+ between volumes is a separate matched-conventions theorem rather than
+ an implication of any one volume.
\end{rmk}
```

**Lines added.** +6.
**Within W5-X7 charter budget.** Yes (+2 to +4 sentence-equivalent;
delivered: 1 sentence wrapped to 6 lines).

---

## 6. Decision

The drafted pointer passes all three scans (em-dash, AI-tells,
agent/swarm/ledger) and all three re-attacks (Drinfeld
functoriality, Witten boundary, Polyakov-class invariance). The
proposal is ready for the maintainer to merge into `main.tex` if
the manuscript line of attack endorses the symmetric interpretation of
the firewall. The proposal is strict-additive and does not
disturb any existing claim.

**Status.** Proposed, not committed, not edited into `main.tex`.

---

## 7. Provenance and obligations

* W5-X1 audit `phase4-exec-W5-X1-cross-volume-2026-04-28.md`
  identified the optional sharpening at severity-0.
* This report fulfills the W5-X7 charter: verify, draft, scan,
  re-attack, propose strict-additive insertion at
  `main.tex:5411`.
* No commit performed.
* No `main.tex` edit performed.
* No new TeX-side label introduced.
* No other manuscript file modified.

---

**End of W5-X7 report.**
