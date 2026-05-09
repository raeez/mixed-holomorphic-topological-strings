# Agent 229 - Analytic Costello First/Third Graph Realization Frontier

Status: report-only attack-heal completed.  No manuscript or script files were
edited.

## Claim Attacked

The attacked claim was that the first and third Moyal coefficients
\[
  \hbar P(f,g),\qquad {\hbar^3\over24}P^3(f,g)
\]
are already realized by actual Costello brane-defect graphs.

They are not.  They are proved in the formal Weyl algebra and in the reduced
open-line Wick model with midpoint propagator.  The Costello graph theorem
still needs the analytic specialization datum.

## Failure Mode

The reduced open-line computation fixes:

- \(S_0=\int_{\mathbb R}\operatorname{Tr}(\phi_1\,d\phi_2)\);
- \(G(t,s)=\frac12\operatorname{sgn}(t-s)\);
- Weyl-ordered vertices;
- no self-contractions;
- \(r\)-fold cross-contractions only.

This gives
\[
  W_r^>(f,g)={1\over r!}\left({\hbar\over2}\right)^rP^r(f,g),
  \qquad
  W_r^<(f,g)={1\over r!}\left(-{\hbar\over2}\right)^rP^r(f,g),
\]
and hence odd commutator coefficient \(2/(2^r r!)\).  Thus \(r=1\) gives
\(1\), and \(r=3\) gives \(1/24\).

This is not a Costello heat-kernel graph integral.  It has no bulk-to-defect
kernel, no Costello configuration-space measure, no counterterm subtraction,
and no QME row calculation.

## Heal

The strongest true theorem surface is the obstruction target recorded in
`reconstitution/analytic-costello-first-third-graph-realization-frontier-2026-04-30.md`.
The required Costello data are:

1. An elliptic mixed HT parent theory or dimensional reduction whose restriction
   is the Hamiltonian BF sector.
2. A weighted Tate coefficient category in which the BV Casimir and
   \(P_{\epsilon,L}^w\) converge.
3. A brane-restricted propagator proving \(P_{\partial,L}|_{\rm Ham^0}=P/2\).
4. A continuous bulk-to-defect kernel
   \[
     \kappa_{\hbar,w,I}\colon
     C^\bullet_{\rm CE,cont}(\mathfrak g^{w,{\rm cur}}_{\hbar,I})
     \to \mathfrak Q^\bullet_{w,\partial,\hbar}(I).
   \]
5. Local counterterms \(C_{\Gamma,w}^{w_0}(\epsilon)\) with locality, RG,
   support, finite-window, and weight-transport compatibility.
6. Scalar anomaly cancellation or scalar-contact filtration lift:
   ordinary \(\mathfrak{gl}_N\) has scalar class \(\hbar N[\bar c]\).
7. Marked finite-window Costello row tables with \(d\)-faces, CE-source faces,
   bracket rows, collision rows, counterterm rows, signs, marker transport,
   and truncation matrices.
8. Connected single-trace extraction and principal-part current compatibility.
9. Vanishing of the first and third normalization defects
   \[
     \mathfrak n_1=P_{\partial,L}|_{\rm Ham^0}-{1\over2}P,
   \]
   \[
     \mathfrak n_3=
     \left[
       {\rm ObsProd}^{(3)}_{\rm Costello}(f,g)
       -{\hbar^3\over24}P^3(f,g)
     \right]_{\rm Ham^0,conn,red}.
   \]

## Obstruction Named

Current data block the Costello theorem by the tuple
\[
  \mathfrak O_{\rm Cost}^{1,3}
  =
  \bigl(
    \mathfrak o_{\rm Cas},
    \hbar N[\bar c]\ {\rm or}\ o_{\sigma,w}^{(r)},
    [\operatorname{Ob}^{\rm red}_{w,\partial,\hbar}],
    \mathfrak O_{\theta_3},
    \mathfrak n_1,
    \mathfrak n_3
  \bigr).
\]
The reduced open-line model kills \(\mathfrak n_1,\mathfrak n_3\) by its
chosen midpoint kernel.  The Costello model has not yet defined these defects
because the specialization data are not supplied.

The current \(\theta_3\) finite-row subcomplex has
\[
  \mathcal Q^0_{\theta_3,M}=0,\qquad
  \mathcal Q^1_{\theta_3,M}=\mathbb C E_{\theta_3,M},\qquad d=0,
\]
so \(\ell_{\theta_3}(E_{\theta_3,M})=1\) proves the displayed one-row class
nonzero.  It is healed only by a CE ancestor, a local counterterm with
\(dC=-E\), or a complete companion-face table with compatible \(v\)-transport
and zero residual.

## Evidence

Local anchors:

- `main.tex:7402-7566`: Hamiltonian Costello specialization data.
- `main.tex:7674-7731`: formal Moyal coefficients.
- `main.tex:8383-8509`: reduced open-line midpoint/Wick computation.
- `main.tex:8521-8771`: first/third Costello normalization target.
- `main.tex:8021-8346`: non-scalar QME and theta3 row obstruction.
- `appendix-radial-parts-moyal.tex:39-70`: exact formal coefficients.
- `appendix-radial-parts-moyal.tex:1343-1418`: reduced open-line graph
  expansion.
- `appendix-radial-parts-moyal.tex:1510-1588`: realization boundary.
- `open-obligations.tex:342-630`: finite-window QME row calculus.

Primary-source anchors:

- `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1549-1563`:
  heat kernel and \(Q^{\rm GF}K_t\) kernel.
- `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1746-1807`:
  counterterm and renormalized limit theorem.
- `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2121-2190`:
  propagator identity and renormalized QME.
- `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2376-2420`:
  local obstruction to solving the renormalized QME.
- `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:3540-3572`:
  graph/asymptotic locality theorem.

## Verification Commands

```bash
python3 scripts/check_moyal_coefficients.py
python3 scripts/finite_window_graph_array.py
rg -n "Moyal|first-order|third-order|1/24|Costello|graph|Wick|QME|anomaly|counterterm|propagator|finite-window|theta" main.tex appendix-radial-parts-moyal.tex open-obligations.tex scripts/*.py
nl -ba main.tex | sed -n '7200,8778p'
nl -ba appendix-radial-parts-moyal.tex | sed -n '1330,1635p'
nl -ba open-obligations.tex | sed -n '205,640p'
```

Results:

- `check_moyal_coefficients.py`: PASS.  It verified 14641 monomial pairs,
  orders through 11, Capelli round trips, low-rank radial restrictions, and
  open-line \(r=1,3\) graph weights.
- `finite_window_graph_array.py`: PASS.  It preserves the current theta3
  obstruction unless an actual \(dC=-E\) primitive, CE ancestor, or complete
  companion-face table is supplied.

## Files Changed

- `reconstitution/analytic-costello-first-third-graph-realization-frontier-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-229-analytic-costello-first-third-graph-realization-frontier.md`

No build was run.  This task produced reports only.
