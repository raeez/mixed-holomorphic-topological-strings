# Swarm 2026-04-30 Agent 315: BMK Pro-Matlis Postintegration Verification

Scope: report-only attack-heal verification after main-thread BMK integration.
No manuscript TeX was edited.

## Verdict

Partial integration.

The current checkout has healed the central Agent 307 failure in three places:

- `main.tex:1421-1456` and `main.tex:1510-1540`;
- `appendix-factorization-current-conventions.tex:545-580` and
  `appendix-factorization-current-conventions.tex:642-713`;
- `theorem-lanes.tex:382-386` and `theorem-lanes.tex:514-528`.

These passages now display the positive one-pair analytic pro-Matlis retract
\[
  \bar\partial H_\chi^0+H_\chi^0\bar\partial
  =
  \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}},
  \qquad
  P_{\Pi}^{\mathrm{an}}=\tau P_{\mathrm{an}},
  \qquad
  \pi_NP_{\Pi}^{\mathrm{an}}=p_N,
\]
and the six-entry native obstruction vector
\[
  \operatorname{Ob}^{\Pi}_{\mathrm{BM}}
  =
  (\operatorname{ob}_{\oplus},
   \operatorname{ob}_{I_\Pi},
   \operatorname{ob}_{\mathfrak h,\Pi},
   \operatorname{ob}_{\mathrm{collar},\Pi},
   \operatorname{ob}_{3,\Pi},
   \operatorname{ob}_{\mathrm{unif},\Pi}).
\]

The integration is not complete across all theorem surfaces, but the old
four-entry vector has been removed from the scanned TeX surface.

## Exact Remaining TeX Defects

1. `main.tex:1675-1684` still summarizes the native package without the
   one-pair analytic pro-Matlis retract and without the six-entry
   \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).

2. `main.tex:2483-2493` now names
   \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\), but it does not display
   \(P_{\Pi}^{\mathrm{an}}=\tau P_{\mathrm{an}}\) and
   \(\pi_NP_{\Pi}^{\mathrm{an}}=p_N\) in the local-theorem summary.

3. `main.tex:2520-2530` now has the one-pair/pro-product split and
   \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\), but the discharged-data sentence
   still omits the positive one-pair analytic pro-Matlis retract.

4. `main.tex:2669-2672` and `main.tex:2758-2761` still describe only finite
   BMK current data and arity-two Matlis comparison. Patch if the local theorem
   theorem-surface summary is meant to expose the postintegration BMK state.

5. `claim-strength-ledger.tex:326` has
   \(z_1^{N+2}\rho_{N+1,0}\) where the action formula should be
   \[
     z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1}.
   \]

6. `claim-strength-ledger.tex:662-680` now has the six-entry vector, but it
   should explicitly add the entry status sentence: first, second, third, and
   sixth entries are nonzero in the native current/product topology; collar and
   ternary entries are exact primitive construction targets.

7. `open-obligations.tex` has no BMK all-window/pro-Matlis row. Add it near
   `open-obligations.tex:253-269`, after the Matlis/local-cohomology row.

8. `appendix-factorization-current-conventions.tex:800-807` has a notation lag:
   the proof tail says \(\operatorname{ob}^{\chi}_{3,N}\), while the theorem
   vector uses \((\operatorname{ob}^{\chi}_{3,\Pi,N})_N\). Align the notation
   or state explicitly that it is the finite-window representative of the
   \(\Pi\)-tower class.

## Claim Status

Proved/visible: finite BMK current data, finite Matlis moment maps, residue
current sections, finite obstruction
\(\operatorname{Ob}^{\mathrm{BMK\mbox{-}curr}}_N\), boundary-mode obstruction
\[
  z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1},
\]
and projected finite-window Jacobiator
\[
  (N+1)(N+2)\rho_{0,1}.
\]

Constructed/visible: the one-pair analytic pro-Matlis retract, but only as a
changed analytic habitat.

Obstructed/visible in core proposition, appendix, and lane: strict native
all-window current transfer by the six-entry
\(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).

Not fully propagated: local theorem summaries, claim-ledger entry-status
language, and the open-obligations controller.

## Checks

Residual stale-vector scan currently returns no hits:

```text
```

The formal-action obstruction was rechecked by finite partial sums. For
\[
  f=\sum_{p\ge2}z_1^p,\qquad
  \lambda=\sum_{p\ge2}\rho_{p-1,0},
\]
the \(\rho_{0,1}\)-coefficient partial sums are \(-5\), \(-14\), and \(-54\)
at cutoffs \(3,5,10\), confirming the divergent
\(-\sum_{p\ge2}p\) coefficient.

## Files Changed

- `reconstitution/bmk-pro-matlis-postintegration-verification-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-315-bmk-pro-matlis-postintegration-verification.md`
