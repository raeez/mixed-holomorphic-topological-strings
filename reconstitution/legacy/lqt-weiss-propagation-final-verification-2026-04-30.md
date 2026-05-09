# LQT/Weiss Propagation Verification

Date: 2026-04-30.

Agent: 310.

Scope: report-only verification after the current patches.  No TeX was
edited.  The current checkout, not earlier attack-ledger prose, is the
evidence.

## Verdict

The LQT \(K,L/W\) collision is fixed in the live manuscript-facing
surface.  The theorem-grade comparison consistently uses the two-window
notation \(K,L\), specializes to one bound \(W\) only as an abbreviation,
and records the separated-block finite-rank bridge rather than a
same-rank deletion map.

The Weiss \(\delta_{\mathrm{Weiss}}^{\check C/R}\) propagation is fixed
on the main stratified theorem lane, the open-obligations stratified
object, and the detailed stratified-factorization ledger row.  One
remaining ledger row still carries a bare \(\delta_{\mathrm{Weiss}}\).
That row should be updated to
\(\delta_{\mathrm{Weiss}}^{\check C/R}\), or expanded as a pointer to the
Cech-cone/Roos class defined later in the ledger.

## LQT Verification

Status: fixed.

Current anchors:

- `main.tex:1903-1944` states the stable Eulerian finite-window LQT
  theorem with \(A_{\psi,K}\), CE length \(\le L\),
  \(\lambda_{\mathrm{LQT},K,L}
  =\Theta_{N,K,L}^{-1}P_{1\mathrm{cyc}}\), and the one-bound
  specialization \(N\ge W+2\).
- `main.tex:1988-2039` separates \(P_{1\mathrm{cyc}}\) from same-rank
  deletion, defines \(B(K,L)=\max(K,L+2)\), \(M=L\,B(K,L)\), displays
  \(\alpha_{M,K,L}\), \(\beta_{M,K,L}\), and records
  \(\Gamma_N=d_{\mathrm{same}}F_N-F_Nd_{\oplus}\) with its first
  commutator component.
- `theorem-lanes.tex:2079-2143` propagates the same LQT datum, including
  the \(W\)-abbreviation, the separated-block idempotent
  \(P^{\mathrm{sep}}_{M,K,L}
  =\beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L}\), and the
  \(\Gamma_N\) obstruction.
- `open-obligations.tex:143-208` propagates the same finite-window dg
  comparison, stable range, scalar-Koszul quotient, separated-block
  idempotent, and same-rank obstruction.
- `claim-strength-ledger.tex:398-449` records the same theorem strength:
  theorem-grade only on \(A_{\psi,K}\), CE length \(\le L\), stable
  single-cycle image, \(W\) as abbreviation for \(K,L\le W\),
  separated-block idempotent, and \(\Gamma_N\).

No remaining live search hit asserts that same-rank multicycle deletion
is a chain map, a same-rank bridge, or a replacement for the stable
block-sum Hopf Eulerian idempotent.

## Weiss Verification

Status: one residual ledger propagation defect.

Fixed anchors:

- `theorem-lanes.tex:3130-3180` now states that
  \(\delta_{\mathrm{pref}}=\delta_{\mathrm{assoc}}=0\) only on the
  reduced product-basis datum, then defines the nine-component internal
  vector with \(\delta_{\mathrm{Weiss}}^{\check C/R}\), the coverwise
  Cech cone \(\Delta^{N,M}_{V,\mathcal U}\), and the Roos compatibility
  class \(\mathfrak w^{\check C/R}_{V,\Omega,N,M}\).
- `theorem-lanes.tex:3181-3195` keeps the centrality homotopies in the
  \(P_{0,\hbar_{\mathrm{QME}}}\) local-functional row, not in the
  reduced Weyl/Moyal current bracket.
- `open-obligations.tex:1047-1066` replaces the old descent slogan by
  the Cech totalization cone.  The notation
  \(\delta_{\mathrm{Weiss}}(V,\mathcal U)\) is acceptable there as the
  cover-level cone before Roos propagation.
- `open-obligations.tex:1158-1187` uses
  \(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\) with
  \(\delta_{\mathrm{Weiss}}^{\check C/R}\), defines it as
  \((\{H^\bullet(\Delta^{N,M}_{V,\mathcal U})\},
  \mathfrak w^{\check C/R}_{V,\Omega,N,M})\), and keeps
  \(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) external.
- `claim-strength-ledger.tex:183-190` already uses
  \(\delta_{\mathrm{Weiss}}^{\check C/R}\) in the top claim-status table.
- `claim-strength-ledger.tex:820-872` uses the nine-component internal
  vector, defines \(\delta_{\mathrm{Weiss}}^{\check C/R}\), records the
  Cech cone, and names the Roos compatibility class.

Remaining anchor:

- `claim-strength-ledger.tex:451-461` still records the full open BV
  factorization-center failure as
  \[
    (\operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}},
    \operatorname{ob}^{P_0}_{\mathrm{cent}},
    \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}},
    \delta_{\mathrm{Weiss}}).
  \]
  This should propagate the sharpened Cech/Roos notation.

Exact fix:

```tex
  Failure is
  \((\operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}},
  \operatorname{ob}^{P_0}_{\mathrm{cent}},
  \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}},
  \delta_{\mathrm{Weiss}}^{\check C/R})\).
```

Stronger self-contained fix:

```tex
  Failure is
  \((\operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}},
  \operatorname{ob}^{P_0}_{\mathrm{cent}},
  \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}},
  \delta_{\mathrm{Weiss}}^{\check C/R})\), where the Weiss term is the
  coverwise Cech cone together with the Roos compatibility class defined
  in the stratified factorization row below.
```

## Checks Run

```bash
sed -n '1,220p' CLAUDE.md
sed -n '1,260p' reconstitution/post-audit-cleanup-verification-2026-04-30.md
sed -n '129,170p' ~/ecosystem/INVARIANTS.md
sed -n '143,164p' ~/ecosystem/AGENTS-HARNESS.md
sed -n '1,220p' commands.tex
sed -n '1,220p' mathmacros.tex
sed -n '1,180p' notation.tex
sed -n '1,220p' preamble.tex
nl -ba main.tex | sed -n '1880,2050p'
nl -ba theorem-lanes.tex | sed -n '2068,2145p'
nl -ba open-obligations.tex | sed -n '132,210p'
nl -ba claim-strength-ledger.tex | sed -n '366,452p'
rg -n -F -e "A_{\\psi,W}" -e "Theta_{N,W}" -e "lambda_{\\mathrm{LQT},W}" -e "N\\geq W" -e "K,L\\le W" -e "K,L" main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
rg -n -F -e "same-rank" -e "P_{\\mathrm{del}}" -e "Gamma_N" -e "P^{\\mathrm{sep}}" -e "B(K,L)" -e "M=L" main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
nl -ba theorem-lanes.tex | sed -n '3000,3235p'
nl -ba open-obligations.tex | sed -n '960,1190p'
nl -ba claim-strength-ledger.tex | sed -n '170,195p'
nl -ba claim-strength-ledger.tex | sed -n '440,466p'
nl -ba claim-strength-ledger.tex | sed -n '820,874p'
rg -n -F -e "delta_{\\mathrm{Weiss}})" -e "delta_{\\mathrm{Weiss}}^{\\check C/R}" -e "ob}^{\\mathrm{src}}_{\\mathrm{CFG}}" theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex appendix-unreduced-bv-qme.tex main.tex
rg -n -F -e "holim" -e "Tot\\check C" -e "Delta^{N,M}_{V,\\mathcal U}" -e "\\mathfrak w^{\\check C/R}" theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex main.tex local-dictionary.tex
```

No build was run.  This was a report-only verification.
