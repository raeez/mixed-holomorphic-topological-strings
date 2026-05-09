# BMK Pro-Matlis Postintegration Verification, 2026-04-30

Agent 315. Report-only verification. No manuscript TeX was edited.

## Claim Attacked

The attacked integration claim is that the BMK post-push theorem surface now
shows both pieces consistently:

\[
  \bar\partial H_\chi^0+H_\chi^0\bar\partial
  =
  \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}},
  \qquad
  P_{\Pi}^{\mathrm{an}}=\tau P_{\mathrm{an}},
  \qquad
  \pi_NP_{\Pi}^{\mathrm{an}}=p_N ,
\]

as the positive one-pair analytic pro-Matlis retract, and

\[
  \operatorname{Ob}^{\Pi}_{\mathrm{BM}}
  =
  (\operatorname{ob}_{\oplus},
   \operatorname{ob}_{I_\Pi},
   \operatorname{ob}_{\mathfrak h,\Pi},
   \operatorname{ob}_{\mathrm{collar},\Pi},
   \operatorname{ob}_{3,\Pi},
   \operatorname{ob}_{\mathrm{unif},\Pi})
\]

as the native strict all-window obstruction vector.

## Verdict

Partial integration.

The main BMK proposition, the factorization-current appendix theorem, the
native \(E_2\) theorem lane, the local-theorem BMK summary, and both BMK rows
in `claim-strength-ledger.tex` now visibly contain the six-entry native
obstruction vector. The positive one-pair analytic pro-Matlis retract is
visible in the core proposition, appendix, theorem lane, and claim ledger. The
remaining integration defects are narrower: `open-obligations.tex` still has no
BMK pro-Matlis row, and several theorem-summary sentences still mention only
the finite BMK data without the positive pro-Matlis retract.

## Verified Present

- `main.tex:1421-1456` states
  \(\widehat{\mathcal P}_{\Pi}\), \(\mathcal P_{\mathrm{an}}(B_1)\),
  \(P_{\Pi}^{\mathrm{an}}=\tau P_{\mathrm{an}}\), and
  \(\pi_NP_{\Pi}^{\mathrm{an}}=p_N\). `main.tex:1599-1610` repeats the proof
  path.
- `main.tex:1510-1540` states the six-entry
  \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\), including
  \(\operatorname{ob}_{I_\Pi}\) and
  \(\operatorname{ob}_{\mathfrak h,\Pi}\), and names the first, second, third,
  and sixth entries as nonzero in the native current topology.
- `appendix-factorization-current-conventions.tex:545-580` states the positive
  one-pair pro-Matlis statement. `appendix-factorization-current-conventions.tex:642-713`
  states the product-current section obstruction, the full formal-action
  obstruction, and the six-entry \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).
- `appendix-factorization-current-conventions.tex:809-820` updates the proof
  tail to the six required data: direct-sum moment landing, pro-current
  section, formal Hamiltonian action, collar primitives, ternary primitives,
  and uniform estimates.
- `theorem-lanes.tex:382-386` updates the lane status to include the one-pair
  analytic pro-Matlis retract. `theorem-lanes.tex:514-528` states
  \(P_{\Pi}^{\mathrm{an}}=\tau P_{\mathrm{an}}\),
  \(\pi_NP_{\Pi}^{\mathrm{an}}=p_N\), and
  \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).
- `main.tex:2483-2493` now names the six-entry all-window obstruction problem
  \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\), and `main.tex:2520-2530` replaces
  the old finite-window remark by the one-pair/pro-product split language.
- `claim-strength-ledger.tex:319-336` and `claim-strength-ledger.tex:662-680`
  now name the positive one-pair pro-Matlis retract and the six-entry
  \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).

## Remaining TeX Defects

1. `main.tex:1675-1684` still summarizes the native Darboux package as only
   BMK current-limit data, finite Matlis moments, arity-two comparison,
   \(\operatorname{Ob}^{\mathrm{BMK\mbox{-}curr}}_N\), and then ternary
   cutoff/collar plus all-window uniformity. It should also state the positive
   one-pair pro-Matlis retract and replace the downstream obstruction language
   by the six-entry \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).

2. `main.tex:2483-2493` now has the correct six-entry
   \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\), but it still does not display the
   positive pro-Matlis formula in the local-theorem summary. Patch target: add
   the split
   \[
     P_{\Pi}^{\mathrm{an}}=\tau P_{\mathrm{an}},\qquad
     \pi_NP_{\Pi}^{\mathrm{an}}=p_N
   \]
   as the positive one-pair analytic retract before the strict native
   all-window current transfer controlled by
   \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).

3. `main.tex:2520-2530` now uses the one-pair/pro-product split and
   \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\), but it still lists the discharged
   data as only current-limit data, finite Matlis moments, and arity-two
   comparison. Patch target: add the positive one-pair analytic pro-Matlis
   retract to the discharged data.

4. `main.tex:2669-2672` and `main.tex:2758-2761` still use only the finite
   BMK description in the theorem body/proof summary. This is less dangerous
   than a wrong obstruction vector, but it leaves the positive pro-Matlis
   retract invisible from the local theorem's theorem-surface summary.

5. `claim-strength-ledger.tex:326` still writes the boundary-mode obstruction
   without the action dot:
   \[
     z_1^{N+2}\rho_{N+1,0}=-(N+2)\rho_{0,1}.
   \]
   Patch target:
   \[
     z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1}.
   \]

6. `claim-strength-ledger.tex:662-680` has the six-entry vector and data list,
   but it does not explicitly record the entry statuses. Patch target: add one
   sentence after the vector: the first, second, third, and sixth entries are
   nonzero in the native current/product topology; collar and ternary entries
   are exact primitive construction targets.

7. `open-obligations.tex` has no BMK all-window/pro-Matlis obligation row.
   The nearest anchor is the Matlis/local-cohomology row at
   `open-obligations.tex:253-269`. Add a row nearby:
   \[
     \bar\partial H_\chi^0+H_\chi^0\bar\partial
     =
     \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}},
     \qquad
     P_{\Pi}^{\mathrm{an}}=\tau P_{\mathrm{an}},
   \]
   followed by the six-entry
   \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\) and the entry statuses above.

8. `appendix-factorization-current-conventions.tex:800-807` still names the
   ternary proof-tail residue as
   \(\operatorname{ob}^{\chi}_{3,N}\), while the theorem vector now uses
   \((\operatorname{ob}^{\chi}_{3,\Pi,N})_N\) at
   `appendix-factorization-current-conventions.tex:669-704`. Patch target:
   replace the proof-tail occurrence by \(\operatorname{ob}^{\chi}_{3,\Pi,N}\)
   or explicitly say it is the finite-window representative of the
   \(\Pi\)-tower class.

## Attack-Heal Check

Attack: the remaining theorem-surface summaries might be sufficient because
the core proposition and theorem lane carry the formula.

Heal: not quite. The local theorem and native Darboux package are reader-facing
theorem surfaces. They should name the positive pro-Matlis retract when they
summarize BMK data; otherwise the construction looks only finite-window even
though the proposition now proves a one-pair all-window analytic retract.

Attack: the positive one-pair analytic quotient might already imply a native
all-window transfer.

Heal: it does not. The positive object is one-pair and analytic. It depends on
the analytic moment space, \(I_{\mathrm{an}}P_{\mathrm{an}}\), and a chosen
polydisk pair. It is not a support-local compact-current factorization
transfer.

## Computation Check

The formal-action obstruction was checked directly. For
\[
  f=\sum_{p\ge2}z_1^p,\qquad
  \lambda=\sum_{p\ge2}\rho_{p-1,0},
\]
the monomial action formula gives
\[
  z_1^p\cdot\rho_{p-1,0}=-p\,\rho_{0,1}.
\]
Partial sums for the \(\rho_{0,1}\)-coefficient are \(-5\), \(-14\), and
\(-54\) for cutoffs \(M=3,5,10\), confirming the divergent
\(-\sum_{p\ge2}p\) row.

## Files Changed

- Added `reconstitution/bmk-pro-matlis-postintegration-verification-2026-04-30.md`.
- Added `reconstitution/swarm-2026-04-30-agent-315-bmk-pro-matlis-postintegration-verification.md`.

## Checks Run

```bash
rg -n -F 'Ob}^{\infty}_{\mathrm{BM}' main.tex appendix-factorization-current-conventions.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
rg -n -F 'Ob}^{\Pi}_{\mathrm{BM}' main.tex appendix-factorization-current-conventions.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
rg -n -F 'P_{\Pi}^{\mathrm{an}}' main.tex appendix-factorization-current-conventions.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
python3 - <<'PY'
for M in [3, 5, 10]:
    coeff = 0
    terms = []
    for p in range(2, M + 1):
        i, j, q = p - 1, 0, 0
        target = (i - p + 1, j - q + 1)
        c = -(p*j - q*i + p - q)
        assert target == (0, 1)
        coeff += c
        terms.append(c)
    print(M, terms, coeff)
PY
```

The stale-vector scan returned no hits after the concurrent main-thread
integration completed.
