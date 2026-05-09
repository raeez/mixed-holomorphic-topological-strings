# Phase 4 EXEC W5-X27 — Cosmetic Label/Env Fix Proposer

**Wave.** Attack-heal-swarm wave 5, agent W5-X27.
**Mode.** Proposal-only. No TeX edits, no commits.
**Authorship.** Raeez Lorgat.
**Date.** 2026-04-28.
**Source of finding.** W5-X21 final-pass referee simulation.

---

## 1. Confirmation of W5-X21 findings

### Item 1 — `main.tex:4266`

Confirmed. Line 4266 reads

```
\begin{thm}[Reduced principal-part current $P_0$ factorization algebra]\label{prop:reduced-principal-part-boundary-current}
```

Label prefix `prop:` is attached to a `\begin{thm}` environment. Mismatch
present.

### Item 2 — `main.tex:4405`

Confirmed. Line 4405 reads

```
\begin{thm}[Reduced factorization realization of the boundary local dual]\label{prob:boundary-principal-part-cotangent-operators}
```

Label prefix `prob:` (problem) is attached to a `\begin{thm}` environment.
Mismatch present.

### Item 3 — `abstract.tex:33`

Confirmed in spirit, with location refinement. The "regulator-independence
understatement" lives on lines 33–35:

```
the principal-part defect model after de Rham-current contraction. The weighted Tate
construction is proved only in the weighted Tate coefficient model and
does not assert regulator independence.
```

The negation "does not assert regulator independence" is correct in
content but is borderline-passive at the strongest sentence. A
Russian-school voice prefers an active naming of the limitation rather
than a bare negation.

---

## 2. Cross-reference census

`grep -n` across all `.tex` files for the two suspect labels yields:

```
theorem-lanes.tex:307:  Theorem~\ref{prop:reduced-principal-part-boundary-current} ...
theorem-lanes.tex:308:  Theorem~\ref{prob:boundary-principal-part-cotangent-operators}
main.tex:1920:        Theorem~\ref{prop:reduced-principal-part-boundary-current}
main.tex:1982:        \ref{prop:reduced-principal-part-boundary-current}
main.tex:2641:        Theorem~\ref{prop:reduced-principal-part-boundary-current}
main.tex:2766:        \ref{prop:reduced-principal-part-boundary-current}
main.tex:4266:        \begin{thm}[...]\label{prop:reduced-principal-part-boundary-current}    [DECL]
main.tex:4396:        Theorem~\ref{prop:reduced-principal-part-boundary-current}
main.tex:4405:        \begin{thm}[...]\label{prob:boundary-principal-part-cotangent-operators}  [DECL]
main.tex:4411:        Theorem~\ref{prop:reduced-principal-part-boundary-current}
main.tex:4420:        Theorem~\ref{prop:reduced-principal-part-boundary-current}
main.tex:4435:        Theorem~\ref{prob:boundary-principal-part-cotangent-operators}
tate-T5-chain-level-primitive.tex:425:  Theorem~\ref{prop:reduced-principal-part-boundary-current}
```

Reference counts (excluding the declaration itself):

- `prop:reduced-principal-part-boundary-current`: **8 references**, every
  one cited as `Theorem~\ref{...}` or as the bare `\ref{...}` immediately
  preceded by "Theorem".
- `prob:boundary-principal-part-cotangent-operators`: **2 references**,
  both cited as `Theorem~\ref{...}`.

**Structural finding.** Every callsite addresses these labels as
**theorems**, not as propositions or problems. The semantic intent of the
cross-reference network is that both objects are theorems. The label
prefix is the part out of step with the rest of the manuscript.

---

## 3. Repair options for Item 1 (`main.tex:4266`)

### Option A — change the environment to match the label

Change

```
\begin{thm}[Reduced principal-part current $P_0$ factorization algebra]\label{prop:reduced-principal-part-boundary-current}
...
\end{thm}
```

to `\begin{prop}[...]\label{prop:...}` ... `\end{prop}`. Cost: every one
of the 8 callsites currently says `Theorem~\ref{...}` and would need to
be re-prosed to `Proposition~\ref{...}`. Cost = 8 prose edits + 1 env
edit = 9 sites.

### Option B — rename the label to match the environment (RECOMMENDED)

Change

```
\label{prop:reduced-principal-part-boundary-current}
```

to

```
\label{thm:reduced-principal-part-boundary-current}
```

and rename the 8 `\ref{prop:...}` callsites to `\ref{thm:...}`. The prose
"Theorem~\ref{...}" already matches; only the prefix string changes. Cost
= 9 single-token edits, all of the form `prop:reduced-principal-part-boundary-current → thm:reduced-principal-part-boundary-current`.

### Recommendation

**Option B.** Both options are nine-site edits, but Option B preserves
all prose verbatim and requires only a sed-style rename of one identifier.
Option A would force re-wording the 8 cross-references from "Theorem" to
"Proposition", a deeper semantic change that downgrades the result
without justification — the statement *is* a theorem in the manuscript's
internal grading.

---

## 4. Repair options for Item 2 (`main.tex:4405`)

### Option A — change the environment to match the label

Change `\begin{thm}[...]\label{prob:...}` ... `\end{thm}` to
`\begin{prob}[...]\label{prob:...}` ... `\end{prob}`. Cost: 2 callsites
currently say `Theorem~\ref{...}` and would need to be re-prosed to
`Problem~\ref{...}`. Cost = 2 prose edits + 1 env edit = 3 sites.

But the content is **not** a problem statement — it asserts a chain-level
realization, not an open question. Demoting it to a problem
mis-represents the proven content.

### Option B — rename the label to match the environment (RECOMMENDED)

Change

```
\label{prob:boundary-principal-part-cotangent-operators}
```

to

```
\label{thm:boundary-principal-part-cotangent-operators}
```

and rename the 2 `\ref{prob:...}` callsites to `\ref{thm:...}`. Cost = 3
single-token edits.

### Recommendation

**Option B.** The `prob:` prefix here is plainly a paste artefact —
nothing in the surrounding prose or the cross-references frames this as
an open problem. Renaming the label to `thm:...` is the least-invasive
and content-faithful repair.

---

## 5. Repair option for Item 3 (`abstract.tex:33–35`)

### Current text

```
The weighted Tate
construction is proved only in the weighted Tate coefficient model and
does not assert regulator independence.
```

### Russian-school-voice fix (1–2-word edit)

Replace the bare negation "does not assert regulator independence" with
an active naming of the regulator-dependence content. Two minimal
candidates:

**Candidate (i) — single-word strengthening:**

```
The weighted Tate
construction is proved only in the weighted Tate coefficient model;
regulator independence is not claimed.
```

(Comma → semicolon, "and does not assert regulator independence" → "; regulator
independence is not claimed". Net: the limitation is named as a separate
clause rather than passively appended.)

**Candidate (ii) — two-word strengthening (RECOMMENDED):**

```
The weighted Tate
construction is proved only in the weighted Tate coefficient model and
makes no regulator-independence claim.
```

(Replace `does not assert regulator independence` → `makes no
regulator-independence claim`. Same length, plain active voice, names the
absent claim as a positive object the reader can reach for.)

Either candidate sharpens the epistemic disclosure without overclaiming.
Neither asserts regulator independence; both refuse it more cleanly. The
recommendation is **(ii)** because it preserves the sentence's
parallel structure (`is proved only ... and makes no ... claim`) and
requires only a substring replacement.

---

## 6. Em-dash / AI-tells / agent-language scan on each proposed fix

Each proposed string was scanned for: em-dashes (`—`, `--` rendered as
em-dash), AI tells (`Let's`, `it's worth noting`, `comprehensive`,
`leverage`, `seamless`, `delve`), agent language (`agent`, `swarm`,
`ledger`, `LLM`, `wave`).

| Proposed fix | em-dash | AI tells | agent-language | Verdict |
|---|---|---|---|---|
| Item 1 Option B: `prop:` → `thm:` rename | none | none | none | clean |
| Item 2 Option B: `prob:` → `thm:` rename | none | none | none | clean |
| Item 3 Candidate (i): `; regulator independence is not claimed.` | none | none | none | clean |
| Item 3 Candidate (ii): `makes no regulator-independence claim.` | none | none | none | clean |

All four proposed fixes pass the scan.

---

## 7. Net line-delta estimate

- Item 1: 9 single-line in-place edits, **net 0 lines**.
- Item 2: 3 single-line in-place edits, **net 0 lines**.
- Item 3: 1 in-place substring replacement (Candidate ii), **net 0 lines**.

**Total net line-delta from W5-X27 fixes: 0.**

---

## 8. Summary recommendation block

| Item | File:Line | Recommended fix | Edit kind | Sites touched |
|---|---|---|---|---|
| 1 | `main.tex:4266` (decl) + 8 refs | Rename label `prop:reduced-principal-part-boundary-current` → `thm:reduced-principal-part-boundary-current` | identifier rename | 9 |
| 2 | `main.tex:4405` (decl) + 2 refs | Rename label `prob:boundary-principal-part-cotangent-operators` → `thm:boundary-principal-part-cotangent-operators` | identifier rename | 3 |
| 3 | `abstract.tex:35` (sentence end) | `does not assert regulator independence` → `makes no regulator-independence claim` | substring | 1 |

All three are mechanical, prose-preserving, content-faithful, and
em-dash / AI-tell free. No TeX file was edited under W5-X27; the edits
are queued for a successor EXEC agent.
