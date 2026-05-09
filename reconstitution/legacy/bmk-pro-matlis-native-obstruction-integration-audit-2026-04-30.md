# BMK Pro-Matlis Native Obstruction Integration Audit, 2026-04-30

Agent 307.  Report-only ownership.  No TeX edits.

## Verdict

Integration is incomplete.

The manuscript correctly records the finite BMK current data, the finite
support-local current obstruction
\(\operatorname{Ob}^{\mathrm{BMK\mbox{-}curr}}_N\), the boundary-mode
calculation
\[
  z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1},
\]
and the projected finite-window \(L_\infty\) Jacobiator
\[
  (N+1)(N+2)\rho_{0,1}.
\]
This part is integrated in `main.tex`, the factorization-current appendix,
the theorem lane, and the claim ledger.

The post-push pro-Matlis split is not fully integrated.  The live TeX still
states only a finite one-pair analytic quotient and a four-entry all-window
vector.  It does not yet state the positive one-pair analytic pro-Matlis
retract
\[
  \bar\partial H_\chi^0+H_\chi^0\bar\partial
    =
  \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}},
  \qquad
  P_{\Pi}^{\mathrm{an}}=\tau P_{\mathrm{an}}
  \colon C^\bullet(B_2,B_1)\to
  \mathcal P_{\mathrm{an}}(B_1)\subset
  \widehat{\mathcal P}_{\Pi},
\]
with compatible finite projections
\[
  \pi_NP_{\Pi}^{\mathrm{an}}=p_N.
\]
It also does not state the strict native all-window current \(E_2\) transfer
as obstructed by the full six-entry vector
\[
  \operatorname{Ob}^{\Pi}_{\mathrm{BM}}
  =
  \left(
    \operatorname{ob}_{\oplus},
    \operatorname{ob}_{I_\Pi},
    \operatorname{ob}_{\mathfrak h,\Pi},
    \operatorname{ob}_{\mathrm{collar},\Pi},
    \operatorname{ob}_{3,\Pi},
    \operatorname{ob}_{\mathrm{unif},\Pi}
  \right).
\]

## Evidence

Construction push target:

- `reconstitution/bmk-all-window-pro-matlis-transfer-construction-push-2026-04-30.md:14`
  states the positive one-pair retract identity.
- `reconstitution/bmk-all-window-pro-matlis-transfer-construction-push-2026-04-30.md:26`
  states the pro-analytic moment map into
  \(\widehat{\mathcal P}_{\Pi}\).
- `reconstitution/bmk-all-window-pro-matlis-transfer-construction-push-2026-04-30.md:56`
  states the theorem-grade split: positive one-pair analytic pro-Matlis
  retract; obstructed strict native all-window direct-sum transfer; obstructed
  pro-product transfer for the full formal Hamiltonian algebra.
- `reconstitution/bmk-all-window-pro-matlis-transfer-construction-push-2026-04-30.md:466`
  states the six-entry final vector and entry statuses.

Live manuscript:

- `main.tex:1400` records a one-pair derived analytic quotient only after
  quotienting to a finite window \(\mathcal P_{\le N}\).  It does not name
  \(\widehat{\mathcal P}_{\Pi}\), \(\mathcal P_{\mathrm{an}}(B_1)\),
  \(P_{\Pi}^{\mathrm{an}}\), or the all-window compatibility
  \(\pi_NP_{\Pi}^{\mathrm{an}}=p_N\).
- `main.tex:1473` records the strict all-window transfer as downstream of
  only
  \[
    \operatorname{Ob}^{\infty}_{\mathrm{BM}}
    =
    (\operatorname{ob}_{\mathrm{mom}},
     \operatorname{ob}_{\mathrm{collar}},
     \operatorname{ob}_{3},
     \operatorname{ob}_{\mathrm{unif}}).
  \]
  This misses \(\operatorname{ob}_{I_\Pi}\) and
  \(\operatorname{ob}_{\mathfrak h,\Pi}\), and it does not separate
  direct-sum all-window failure from pro-product current/action failure.
- `appendix-factorization-current-conventions.tex:526` records the finite
  one-pair analytic quotient, not the pro-analytic all-window retract.
- `appendix-factorization-current-conventions.tex:646` records the same
  four-entry vector.  It defines
  \(\widehat{\mc P}_{\Pi}\) and
  \(Q_{\mathrm{mom}}=\widehat{\mc P}_{\Pi}/\mc P\), but does not state the
  support-local pro-current section obstruction
  \(\operatorname{ob}_{I_\Pi}\) or the full formal Hamiltonian product-action
  obstruction \(\operatorname{ob}_{\mathfrak h,\Pi}\).
- `theorem-lanes.tex:513` says the strict all-window/pro-Matlis transfer is
  only the next construction target.  It does not record the positive
  pro-analytic one-pair theorem or the six-entry native obstruction vector.
- `claim-strength-ledger.tex:639` uses the four-entry
  \(\operatorname{Ob}^{\infty}_{\mathrm{BM}}\).  The later classification
  calls the all-window strict transfer an exact obstruction, but the listed
  obstruction is incomplete.
- `open-obligations.tex` has no BMK/all-window row.  The nearest local row is
  the Matlis/local-cohomology cotangent source at `open-obligations.tex:246`;
  no row records \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).

## Attack-Heal Check

Attack: perhaps the existing
\(\operatorname{ob}_{\mathrm{mom}}\) is already the same as
\(\operatorname{ob}_{\oplus}\), so the vector is materially complete.

Heal: \(\operatorname{ob}_{\mathrm{mom}}\) is the direct-sum moment failure.
It does not record two independent native failures of the product target:
the compatible finite derivative-delta sections have no limit as compactly
supported currents, and the full formal Hamiltonian algebra does not act on
\(\widehat{\mathcal P}_{\Pi}\).

Attack: perhaps the one-pair analytic quotient already proves the
pro-Matlis positive statement.

Heal: the live text only descends to finite
\(\mathcal P_{\le N}\).  The construction push adds the all-window
Taylor-coordinate map
\(\tau\colon\mathcal O(B_1)^\vee_{\mathrm{red}}\to
\widehat{\mathcal P}_{\Pi}\), the analytic subspace
\(\mathcal P_{\mathrm{an}}(B_1)\), and the compatible tower
\(\pi_NP_{\Pi}^{\mathrm{an}}=p_N\).  These are absent from the live TeX.

Attack: perhaps the uniformity obstruction covers the missing pro-current
and full-action failures.

Heal: it does not.  The pro-current obstruction is categorical: an arbitrary
product coefficient sequence does not define a finite-order distribution
supported at the collision point.  The full-action obstruction is algebraic:
for
\[
  f=\sum_{p\ge2}z_1^p,\qquad
  \lambda=\sum_{p\ge2}\rho_{p-1,0},
\]
the \(\rho_{0,1}\)-coefficient of \(f\cdot\lambda\) is
\(-\sum_{p\ge2}p\).  No current seminorm estimate repairs an undefined
coefficient.

## Exact Fixes Needed

### 1. Main proposition

In `main.tex`, after the finite one-pair analytic quotient block at
`main.tex:1400-1419`, insert the pro-analytic positive replacement:

```tex
  Keeping the whole Taylor tower gives a different, positive one-pair
  statement.  Let
  \[
    \widehat{\mathcal P}_{\Pi}
      =
      \prod_{a+b>0}\C\rho_{a,b},\qquad
    \mathcal P_{\mathrm{an}}(B_1)
      =
      \tau\bigl(\mathcal O(B_1)^\vee_{\mathrm{red}}\bigr)
      \subset\widehat{\mathcal P}_{\Pi},
  \]
  where \(\tau(\lambda)=(\lambda(z_1^az_2^b))_{a+b>0}\).
  If the full analytic BMK contraction
  \[
    \bar\partial H_\chi+H_\chi\bar\partial
      =
    \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}}+E_\chi
  \]
  is supplied on the single-pair relative/collar complex and the collar
  quotient kills \(E_\chi\), then
  \[
    H_\chi^0
      =
    (1-I_{\mathrm{an}}P_{\mathrm{an}})H_\chi
    (1-I_{\mathrm{an}}P_{\mathrm{an}})
  \]
  satisfies
  \[
    \bar\partial H_\chi^0+H_\chi^0\bar\partial
      =
    \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}} .
  \]
  The pro-analytic moment map
  \(P_{\Pi}^{\mathrm{an}}=\tau P_{\mathrm{an}}\) has compatible finite
  projections
  \[
    \pi_NP_{\Pi}^{\mathrm{an}}=p_N,\qquad
    \pi_{M,N}p_M=p_N .
  \]
  This is a one-pair analytic pro-Matlis retract.  It is not a native
  support-local factorization-current transfer.
```

Replace the four-entry all-window vector at `main.tex:1473-1486` by the
six-entry vector:

```tex
  The strict native all-window current \(E_2\) transfer is therefore
  obstructed by
  \[
    \operatorname{Ob}^{\Pi}_{\mathrm{BM}}
    =
    \left(
      \operatorname{ob}_{\oplus},
      \operatorname{ob}_{I_\Pi},
      \operatorname{ob}_{\mathfrak h,\Pi},
      \operatorname{ob}_{\mathrm{collar},\Pi},
      \operatorname{ob}_{3,\Pi},
      \operatorname{ob}_{\mathrm{unif},\Pi}
    \right).
  \]
  Here \(\operatorname{ob}_{\oplus}=[\operatorname{mom}_\infty]\in
  \widehat{\mathcal P}_{\Pi}/\mathcal P\) is nonzero on the full
  compact-support current complex; \(\operatorname{ob}_{I_\Pi}\) is the
  nonexistence of a compact-current section
  \(i_\Pi:\widehat{\mathcal P}_{\Pi}\to\mathcal D'_0{}^{0,2}(B)\)
  extending all \(i_N\); \(\operatorname{ob}_{\mathfrak h,\Pi}\) is the
  failure of the full formal Hamiltonian action on
  \(\widehat{\mathcal P}_{\Pi}\), detected by the divergent
  \(\rho_{0,1}\)-coefficient for
  \(f=\sum_{p\ge2}z_1^p\) acting on
  \(\lambda=\sum_{p\ge2}\rho_{p-1,0}\).  The remaining entries are the
  compatible collar primitive class, the first ternary small-diagonal
  transfer class, and the all-window uniform estimate class.  The first,
  second, third, and sixth entries are nonzero in the native current
  topology; the collar and ternary entries are exact unconstructed primitive
  classes.
```

The proof paragraph at `main.tex:1545-1551` should be extended with the
same \(P_{\Pi}^{\mathrm{an}}\) compatibility.  The proof paragraph at
`main.tex:1566-1571` should be changed from four requirements to the six
requirements above.

### 2. Appendix theorem

In `appendix-factorization-current-conventions.tex`, after
`appendix-factorization-current-conventions.tex:526-543`, add the same
one-pair analytic pro-Matlis retract statement.  The appendix is the best
place to record the definitions of
\(\widehat{\mc P}_{\Pi}\), \(\mathcal P_{\mathrm{an}}(B_1)\), and
\(P_{\Pi}^{\mathrm{an}}\) before using the obstruction vector.

Replace the four-entry vector at
`appendix-factorization-current-conventions.tex:646-655` by
\(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\) with the six entries listed
above.  Also add the two product-target failures:

```tex
  There is no support-local current section
  \[
    i_\Pi:\widehat{\mc P}_{\Pi}\to\mathcal D'_0{}^{0,2}(B)
  \]
  extending the finite derivative-delta sections \(i_N\), because a
  distribution supported at one point has finite order.
```

```tex
  The full formal Hamiltonian action does not extend to
  \(\widehat{\mc P}_{\Pi}\).  For
  \(f=\sum_{p\ge2}z_1^p\) and
  \(\lambda=\sum_{p\ge2}\rho_{p-1,0}\), the
  \(\rho_{0,1}\)-coefficient would be \(-\sum_{p\ge2}p\).
```

The proof paragraph at
`appendix-factorization-current-conventions.tex:756-768` should say that
a strict native all-window transfer would need six data, not four:
direct-sum moment landing, pro-current section or changed current habitat,
full Hamiltonian action or changed bornology, compatible collar primitives,
ternary small-diagonal primitive, and uniform estimates.

### 3. Theorem lane

In `theorem-lanes.tex`, update the status at `theorem-lanes.tex:381-385`
to:

```tex
  \emph{Status.} \emph{proved CE/factorization object and proved
  semidirect collision algebra; BMK current-limit data, finite Matlis
  moment maps, arity-two output projection, and one-pair analytic
  pro-Matlis retract proved; strict native all-window current transfer
  recorded as an exact obstruction}.
```

Replace `theorem-lanes.tex:513-514` with a short statement of the split:
positive one-pair analytic pro-Matlis retract, but strict native
all-window/pro-product transfer obstructed by
\(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).

### 4. Claim ledger

In `claim-strength-ledger.tex`, update both BMK rows:

- `claim-strength-ledger.tex:319-331`: add the positive one-pair
  analytic pro-Matlis retract and replace
  \(\operatorname{Ob}^{\infty}_{\mathrm{BM}}\) by the six-entry
  \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).
- `claim-strength-ledger.tex:615-649`: replace the four-entry vector with
  the six-entry vector and record entry status:
  \(\operatorname{ob}_{\oplus}\), \(\operatorname{ob}_{I_\Pi}\),
  \(\operatorname{ob}_{\mathfrak h,\Pi}\), and
  \(\operatorname{ob}_{\mathrm{unif},\Pi}\) are nonzero in the native
  current/product topology; \(\operatorname{ob}_{\mathrm{collar},\Pi}\)
  and \(\operatorname{ob}_{3,\Pi}\) are unconstructed primitive classes.

### 5. Open obligations

Add a BMK all-window/pro-Matlis obligation row to `open-obligations.tex`,
near the Matlis/local-cohomology row.  The row should state:

```tex
  \item \emph{BMK all-window/pro-Matlis native obstruction.}
  The one-pair analytic pro-Matlis BMK retract is the positive analytic
  replacement
  \[
    \bar\partial H_\chi^0+H_\chi^0\bar\partial
      =
    \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}},\qquad
    P_{\Pi}^{\mathrm{an}}=\tau P_{\mathrm{an}}.
  \]
  It is not a native support-local factorization-current transfer.  A
  strict native all-window current \(E_2\) transfer is controlled by
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
  The first entry is the failure of full compact-support current moments to
  land in the direct-sum Matlis module; the second is the nonexistence of a
  product-Matlis compact-current section; the third is the failure of the
  full formal Hamiltonian action on the product target; the fourth and
  fifth are compatible primitive obligations; the sixth is nonzero in the
  unweighted current topology.
```

## Status Recommendation

Do not mark the BMK pro-Matlis native obstruction integration as complete.
The finite-current obstruction gate is integrated.  The pro-Matlis
positive analytic retract and the native strict all-window obstruction
vector still need TeX integration in the proposition, appendix theorem,
theorem lane, claim ledger, and open-obligations rows.

## Commands Run

```bash
pwd && git status --short
sed -n '1,220p' CLAUDE.md
sed -n '1,220p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '1,260p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
sed -n '1,220p' /Users/raeez/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,220p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,620p' reconstitution/bmk-all-window-pro-matlis-transfer-construction-push-2026-04-30.md
nl -ba reconstitution/bmk-all-window-pro-matlis-transfer-construction-push-2026-04-30.md | sed -n '1,520p'
rg -n -F -e 'BMK' -e 'Bochner' -e 'Martinelli' -e 'Matlis' -e 'Ob}^{\\infty}_{\\mathrm{BM}' -e 'ob}_{\\mathrm{mom}' -e 'pro-Matlis' -e 'widehat{\\mc P}_{\\Pi}' -e 'Q_{\\mathrm{mom}' theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex main.tex appendix-factorization-current-conventions.tex
nl -ba main.tex | sed -n '1180,1585p'
nl -ba main.tex | sed -n '1588,1632p'
nl -ba main.tex | sed -n '2380,2452p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '1,260p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '360,840p'
nl -ba theorem-lanes.tex | sed -n '360,545p'
nl -ba open-obligations.tex | sed -n '200,330p'
nl -ba open-obligations.tex | sed -n '880,1045p'
nl -ba claim-strength-ledger.tex | sed -n '300,665p'
nl -ba appendix-matlis-principal-parts.tex | sed -n '210,250p'
```
