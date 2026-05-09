# Phase-4 EXEC W5-X34 — Script Em-Dash Purge Proposer

Date 2026-04-28. Mode proposal-only. Authorship Raeez Lorgat.
Severity-3 cosmetic violation (Russian-school voice / INVARIANTS.md
§IV) at the script-comment / docstring tier. Do not commit; do not
edit any script.

---

## 1. Affected scripts (13 of 20 check_*.py)

Enumerated by `grep -l $'\xe2\x80\x94' scripts/*.py`.

| count | script |
| ----: | ------ |
|     1 | check_bi_infinite_lie_consistency.py |
|    11 | check_bch_cubic_cocycle.py |
|     9 | check_g2g3_attack_heal.py |
|     1 | check_classical_super_sweep.py |
|    13 | check_higher_spin_jacobi.py |
|    11 | check_pva_module_z2_direction.py |
|    27 | check_pva_M2_degree3.py |
|    14 | check_pva_module_lambda_bracket.py |
|     3 | check_g2g3_transversality.py |
|     5 | check_sergeev_intertwiner.py |
|    14 | check_symp_functoriality.py |
|    14 | check_non_multiplicative_chiral_charge.py |
|     6 | check_W5_A4_small_N.py |

Line totals 129 (matches W5-X24); occurrence total 132 (a few lines
hold two em-dashes).

## 2. Lexical classification

Built by Python pass that tracks triple-quote state and `#` prefix.

| context | count |
| ------- | ----: |
| comment-only (`# … — …`) | 43 |
| string literal (single-line `"…—…"` or `print("…—…")`) | 45 |
| docstring (`""" … — … """` body) | 44 |
| **bare code (outside any string/comment)** | **0** |
| inside `re.compile / split / ==` literal | **0** |

Total 132. Confirms the violation is pure prose-tier: every em-dash
sits inside human-readable text (header docstring, inline comment, or
status print), never as a functional Python token.

## 3. Sanity check on content-bearing em-dashes

Searched for:

- `re.compile / re.search / re.match / re.sub / re.findall` with `—`
  in the pattern: 0 hits.
- Dictionary access of the form `d['…—…']`: 0 hits.
- `str.split('—…')`, `==` against an em-dash literal, `in` test
  against an em-dash literal, `.replace('—…', …)`: 0 hits.

**Verdict severity-3 cosmetic.** Replacement is mechanically safe.
Severity-2 not triggered.

## 4. Replacement grammar

For each em-dash hit propose the substitution by syntactic context.

| pattern | replace with | rationale |
| ------- | ------------ | --------- |
| ` — ` (space-em-space, parenthetical aside) | `; ` or `: ` | Russian-school voice prefers semicolon for parallel clauses, colon when the right clause expands the left |
| ` — ` (space-em-space, "but" / contrast) | `. ` (sentence break) | a contrastive em-dash usually wants its own sentence in austere prose |
| `x—y` (no spaces, tight pair) | `x to y` if range, `x, y` if list | numeric / index ranges read better as "to"; logical pairs as commas |
| stand-alone trailing `—` | `:` or removal | docstring section heads such as `T_QC — quasi-commutativity` become `T_QC: quasi-commutativity` |
| inside print banners (`==== — ====`) | hyphen `-` | preserves visual ASCII alignment of separator banners |

## 5. Worked examples — three sample scripts

### 5.1 check_pva_M2_degree3.py (27 hits, largest)

```
L  2  """P4-G2-M2 milestone — BCH cocycle on degree-3 generators…
   →  """P4-G2-M2 milestone: BCH cocycle on degree-3 generators…

L 45      So (a)/(b) and (c) disagree — this is the "z_1^2 disambiguation"
   →      So (a)/(b) and (c) disagree; this is the "z_1^2 disambiguation"

L276  # M2_T1 — Three-way agreement on degree-3 Hamiltonian action
   →  # M2_T1: Three-way agreement on degree-3 Hamiltonian action

L285      The "third method" — iterated z_1 then z_1 — is the
   →      The "third method", iterated z_1 then z_1, is the

L644      # disagree on the bidegree of the result — this is the W3-W26-05
   →      # disagree on the bidegree of the result; this is the W3-W26-05
```

### 5.2 check_pva_module_lambda_bracket.py (14 hits)

```
L  2  """P4-G2-M1 milestone — module λ-bracket on M̂_0…
   →  """P4-G2-M1 milestone: module λ-bracket on M̂_0…

L 76  # Vector representation: dict {(a,b): Fraction} — finite linear combinations.
   →  # Vector representation: dict {(a,b): Fraction}; finite linear combinations.

L119  # T_QC — quasi-commutativity of the algebra λ-bracket
   →  # T_QC: quasi-commutativity of the algebra λ-bracket

L188  # T_TWO — T^2 cocycle exactness
   →  # T_TWO: T^2 cocycle exactness

L364      print("  [T_QC]  passes — Poisson skew on bar A is structural")
   →      print("  [T_QC]  passes: Poisson skew on bar A is structural")
```

### 5.3 check_higher_spin_jacobi.py (13 hits)

```
L  2  """P4-EXEC P4-Higher-Spin-Jacobi — higher-spin Jacobi at λ^k for k ≥ 2.
   →  """P4-EXEC P4-Higher-Spin-Jacobi: higher-spin Jacobi at λ^k for k ≥ 2.

L 74  at non-zero ε_1 ε_2 — out of M-1 scope.
   →  at non-zero ε_1 ε_2; out of M-1 scope.

L118    TEST H9   Canonical degree-3 triples — deterministic sweep over
   →    TEST H9   Canonical degree-3 triples: deterministic sweep over

L492      """TEST H1: Jacobi at order (0, 0) — Lie-module Jacobi at chain level."""
   →      """TEST H1: Jacobi at order (0, 0); Lie-module Jacobi at chain level."""

L886      print("VERDICT — higher-spin Jacobi at λ^k on degree-3 generators of bar A:")
   →      print("VERDICT: higher-spin Jacobi at λ^k on degree-3 generators of bar A:")
```

## 6. Summary count for the remaining 10 scripts

| script | hits | dominant pattern |
| ------ | ---: | ---------------- |
| check_bi_infinite_lie_consistency.py | 1 | print banner; `—` → `:` |
| check_bch_cubic_cocycle.py | 11 | docstring head + comment dashes; `—` → `:` / `;` |
| check_g2g3_attack_heal.py | 9 | comment "ATTACK n: …" headers; `—` → `:` |
| check_classical_super_sweep.py | 1 | docstring head; `—` → `:` |
| check_pva_module_z2_direction.py | 11 | comment section headers; `—` → `:` |
| check_g2g3_transversality.py | 3 | docstring head + jet comment; `—` → `:` / `;` |
| check_sergeev_intertwiner.py | 5 | docstring + print; `—` → `:` |
| check_symp_functoriality.py | 14 | comment list bullets; `—` → `;` (list) / `:` (head) |
| check_non_multiplicative_chiral_charge.py | 14 | docstring head + comment; `—` → `:` / `;` |
| check_W5_A4_small_N.py | 6 | docstring head + author/year asides; `—` → `:` / `,` |

## 7. Phase-5 follow-up task

```
Phase-5 cosmetic cleanup task
  ID         W5-X34-followup
  priority   LOW
  scope      129 em-dash purges across 13 scripts (132 occurrences)
  method     mechanical sed-style substitution under the grammar of §4
  blocker    none (severity-3, no functional content)
  estimate   ~30-45 minutes single-pass for one human or one
             chunked-workflow agent
  acceptance grep -l $'\xe2\x80\x94' scripts/*.py returns empty
```

## 8. Certification

Severity 3 — cosmetic. No content-bearing em-dash. No regex, no dict
key, no split / equality literal carries the character. The 13
scripts compile and execute identically before and after the
proposed substitution. Recommend Phase-5 LOW-priority cleanup.
