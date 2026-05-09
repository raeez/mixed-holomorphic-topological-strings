# Agent 349 next-lane priority queue

Ownership: report-only in `reconstitution/`.  No TeX, script, figure, bibliography,
PDF, or build artifact edited.

Evidence boundary: Agent 340's progress audit is the ordering base.  Later
materialized reports 338-344 refine two entries: Agent 338 identifies the
non-scalar supremum route through the lower `theta_3` Bianchi column, and Agent
344 gives the patch-grade skeleton for that column.  Agent 339 removes a BMK
bibliography build risk.  Agent 341 confirms the radial surface is
`\Omega^{\mathrm{rad}}` / decorated PBW Stokes / signed row.  Agent 342 finds
no root manuscript compile blocker.  Agent 343 finds no compact-CY firewall
breach.

The next queue excludes compact/global comparison.  It also holds the protected
physical trace-state theorem behind the non-scalar QME and stratified descent
lanes; launching it now would mainly restate the same obstruction vector.

## Queue

| Rank | Lane | Principal target | Write scope |
|---:|---|---|---|
| 1 | `theta3-bianchi-column` | Build or obstruct the scalar-zero lower `theta_3` counterterm column. | `main.tex:8849-9121`; `theorem-lanes.tex:3472-3612`; `open-obligations.tex:795-957`; `claim-strength-ledger.tex:516-550`; new report only. |
| 2 | `nonscalar-marked-row-package` | Construct the finite marked row table and transition data needed for larger non-scalar QME. | `appendix-unreduced-bv-qme.tex:2077-2399`; `scripts/finite_window_graph_array.py`; new report only.  Do not write the rank-1 `theta_3` windows owned by lane 1. |
| 3 | `radial-decorated-stokes` | Close the total-degree 14 frontier or produce the signed obstruction row. | `scripts/quantum_shear_trace_diagram_normal_form.py:371-396,745-801`; `scripts/quantum_shear_primitive_search.py:347-419`; `appendix-radial-parts-moyal.tex:820-1027,1658-1713`; radial report only. |
| 4 | `bmk-native-all-window` | Turn `Ob^{Pi}_{BM}` into either a changed-habitat construction or a proved native no-go theorem. | `main.tex:1362-1546`; `theorem-lanes.tex:481-545`; `open-obligations.tex:274-309`; `claim-strength-ledger.tex:323-340`; `appendix-factorization-current-conventions.tex:680-820`. |
| 5 | `stratified-omega-descent` | Build internal stratified Cech/Roos descent with Omega-basic QME boundary data. | `main.tex:4672-4704`; `theorem-lanes.tex:2901-3250`; `open-obligations.tex:1000-1238`; `claim-strength-ledger.tex:846-940`; no LQT/BMK/radial writes. |
| 6 | `lqt-separated-block-finalization` | Finish the fixed-rank bridge theorem surface: separated-block proof plus raw same-rank obstruction. | `main.tex:1981-2100`; `theorem-lanes.tex:2096-2152`; `open-obligations.tex:143-212`; `claim-strength-ledger.tex:402-440`; LQT report only. |

## 1. `theta3-bianchi-column`

Attack: a name `C_{\theta_3}` does not kill the row unless it supplies an
actual degree-zero local functional.  The current row has
\[
  \mathcal Q^0_{\theta_3,M}=0,\qquad
  \mathcal Q^1_{\theta_3,M}=\mathbb C\mathsf E_{\theta_3,M},\qquad d_M=0,
\]
so the covector `ell_theta3` proves the current class nonzero.

Construction target:
\[
  B^M_{02,20}\in\mathcal K^0_{\mathrm{ns},M}(I),\qquad
  d_{\mathrm{ns},M}B^M_{02,20}=-\mathfrak b^M,\qquad
  \widehat\sigma_{\mathrm{sc},M}(B^M_{02,20})=0.
\]
At `N=2`, with basis
\((E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})\),
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T,\qquad
  A_B^2=(0,0,-1)^T.
\]
The accepted matrix is
\[
  A^2_{D,B}=
  \begin{pmatrix}-2&0\\2&0\\1&-1\end{pmatrix},\qquad
  A^2_{D,B}(1,1)^T=-r_2.
\]
Tower gate:
\[
  \Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N
  =
  d_{\mathrm{ns},N}H^{M,N}_{02,20},
\]
and
\[
  [\pi_{M,N}B^M_{02,20}-B^N_{02,20}-H^{M,N}_{02,20}]
  =
  0
  \quad\text{in}\quad
  \varprojlim\nolimits^1_N H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I)).
\]

Expected proof object: a regular-density or graphwise wavefront-admissible
Costello local functional \(B^M_{02,20}\), its scalar-zero verification, the
fixed-window matrix proof, transition cochains \(H^{M,N}_{02,20}\), and a zero
secondary Roos class.  If the functional cannot be constructed, the deliverable
is a proved obstruction theorem naming the cokernel functional that detects
`A_B^2`.

## 2. `nonscalar-marked-row-package`

Attack: the minimal full-equivariant branch proves zero only in its named
minimal marked habitat.  It supplies no larger graph package, no row table, no
curved bulk-to-defect kernel, and no centrality homotopies.

Construction target: for each finite window \(M\), build a codimension-two
closed marked Costello list \(\mathcal G_M^{\mathrm{mk}}\) and row array
\[
  R^{\mathrm{ns}}_{n,M}=\sum_i r_i^M\rho_i^M,\qquad
  d_{\mathrm{ns},M}\eta_j^M=\sum_i A^M_{ij}\rho_i^M,\qquad
  A^M c=-r^M.
\]
The transition matrices must satisfy
\[
  T^{M,N}r^M=r^N,\qquad T^{M,N}A^M=A^NP^{M,N},\qquad
  [P^{M,N}c_M-c_N]=0\in H^0(\mathcal Q^\bullet_{w,N}(I)).
\]
Centrality rows require
\[
  R^{\mathrm{cent}}_{x,y,M}+d_MH^M_{x,y}=0,\qquad
  A^Mh^M=-r^M.
\]

Expected proof object: a finite table with every field-differential, BV-edge,
collision/contact, counterterm, and CE-source face, including output graph,
coefficient, marker transport, incidence sign, scalar gate, lower-window
truncation, and transition matrices.  The script output must reproduce the row
arrays and either solve \(A^Mc=-r^M\) or print a normalized left-null
certificate \(\ell A^M=0,\ell(r^M)\ne0\).  Do not advertise a full Costello
graph/QME theorem unless the curved kernel
\[
  \operatorname{Curv}(\kappa_{\hbar,w,I}+C_{\hbar,w})=0
\]
is also constructed with the Roos and centrality data.

## 3. `radial-decorated-stokes`

Attack: longer execution of the present shuffle-expanded solver is not a
mathematical proof.  The frontier cases
\[
  (6,8),\quad (8,6),\quad (7,7)
\]
are timeout/frontier cases, not obstruction rows.

Construction target:
\[
  \Omega^{\mathrm{rad}}_{a,b}
  =
  [(T_{a,b},E^+_{a,b})]\in\operatorname{coker}B_{a,b},
\]
equivalently the decorated PBW Stokes equation
\[
  D^\square_{a,b}H_{a,b}=R^{\mathrm{free}}_{a,b},\qquad
  D^\square_{a,b}=C^+_{a,b}\partial_2.
\]
Failure must be the signed row
\[
  (\phi,-\lambda)\in\ker B_{a,b}^*,\qquad
  \lambda(E^+_{a,b})-\phi(T_{a,b})\ne0.
\]

Expected proof object: target-normal-form compression by PBW matching orbits,
cycle-basis membership after the classical solve, modular sparse membership,
and signed-row extraction on inconsistency.  The theorem result is either
certificates closing `(6,8)`, `(8,6)`, `(7,7)` and a visible pattern toward all
bidegrees, or a normalized signed row in the dual-potential complex.

## 4. `bmk-native-all-window`

Attack: the one-pair analytic pro-Matlis retract is not a strict native
support-local all-window current transfer.

Construction target:
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
The finite-window obstruction remains
\[
  z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1},
\]
and the projected escape Jacobiator is
\[
  \operatorname{Jac}_{\mathrm{proj}}(z_1^{N+2},z_2,\rho_{N,0})
  =(N+1)(N+2)\rho_{0,1}.
\]

Expected proof object: first attempt a changed-habitat construction with a
direct-sum moment map, compact-current section of the pro-product tower,
Hamiltonian action, collar estimates, ternary homotopy, and inverse-limit
control.  If that cannot exist in the native topology, prove the obstruction
theorem: identify which entries of `Ob^{Pi}_{BM}` are nonzero, with explicit
test elements such as \(f=\sum_{p\ge2}z_1^p\) and
\(\lambda=\sum_{p\ge2}\rho_{p-1,0}\), and isolate the collar/ternary entries
as the remaining construction targets.

## 5. `stratified-omega-descent`

Attack: Darboux stalks, reduced current brackets, and normal Omega weights do
not give a stratified factorization theorem or brane-defect QME.

Construction target:
\[
  \mathcal F^{\mathrm{str}}_{\Omega,N}\colon
  \operatorname{Disk}^{\mathrm{str}}_{X,L}\to
  \operatorname{Ch}_{R_\Omega^{N,M}[[\hbar_{\mathrm{QME}}]]},
\]
with descent defect
\[
  \Delta^{N,M}_{V,\mathcal U}
  =
  \operatorname{Cone}\!\left(
    \mathcal F^{\mathrm{str}}_{\Omega,N,M}(V)
    \to
    \operatorname{Tot}\check C^\bullet
    (\mathcal U;\mathcal F^{\mathrm{str}}_{\Omega,N,M})
  \right)
\]
and
\[
  \delta_{\mathrm{Weiss}}^{\check C/R}
  =
  (\{H^\bullet(\Delta^{N,M}_{V,\mathcal U})\}_{V,\mathcal U,N,M},
   \mathfrak w^{\check C/R}_{V,\Omega,N,M}).
\]
The Omega QME boundary is
\[
  Q_\Omega=Q+\iota_{V_\Omega},\qquad Q_\Omega^2=L_{V_\Omega},
\]
\[
  \operatorname{Curv}(K_{\Omega,N})
  =
  d_{\mathrm{QME}}K_{\Omega,N}
  +\frac12[K_{\Omega,N},K_{\Omega,N}]_{\hbar_{\mathrm{QME}}}=0.
\]

Expected proof object: a collared stratified prefactorization datum, collar
module, products, Cech descent contraction, Roos refinement/window/transport
compatibility, and basic centrality homotopies
\[
  R^{\mathrm{cent}}_{x,y,\Omega,M}+d_{M,\Omega}H^\Omega_{x,y,M}=0,\qquad
  L_{V_\Omega}H^\Omega_{x,y,M}=0.
\]
Failure must name the surviving entry of
\(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\), not appeal to
external Costello-Gwilliam or Weiss/Ran slogans.

## 6. `lqt-separated-block-finalization`

Attack: the raw same-rank deletion of multicycles is not a chain map.  The
admissible bridge is separated-block stabilization, and the theorem surface
must not slide back into the false fixed-rank endomorphism.

Construction target:
\[
  P_{1\mathrm{cyc}}
  =
  \log^*(\operatorname{id})
  =
  \sum_{m=1}^{L}\frac{(-1)^{m-1}}{m}(\operatorname{id}-u\epsilon)^{*m},
\]
\[
  \lambda_{\mathrm{LQT},K,L}
  =
  \Theta_{N,K,L}^{-1}P_{1\mathrm{cyc}}
  \colon
  \mathsf H^{\mathrm{st}}_{K,L}(A_\psi)
  \to
  CC_{\mathrm{red},\le L}(A_{\psi,K})[1],
\]
in the range \(N\ge\max(K,L+2)\).  The finite-rank separated bridge is
\[
  P^{\mathrm{sep}}_{M,K,L}
  =
  \beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L},\qquad
  M=L\max(K,L+2),
\]
with
\[
  \alpha_{M,K,L}\beta_{M,K,L}=\operatorname{id}.
\]
The raw same-rank defect is
\[
  \Gamma_N=d_{\mathrm{same}}F_N-F_Nd_{\oplus},\qquad
  \Gamma_N(\Theta_1^N(a)\wedge\Theta_1^N(b))
  =
  \pm\Theta_1^N(ab-(-1)^{|a||b|}ba).
\]

Expected proof object: a final theorem-lane audit that the stable Eulerian
projection, separated-block zigzag, scalar-Koszul quotient, and same-rank
obstruction are all typed in the same dg finite-window habitat.  If new TeX is
needed, it should only repair local typing around the displayed maps; it must
not touch BMK, theta3, radial, non-scalar QME, or Omega scopes.

## Dispatch order

Launch lanes 1, 3, 4, 5, and 6 independently.  Lane 2 may run immediately on
appendix/script data, but its main-theorem insertion should wait for lane 1's
`B^M_{02,20}` decision.  A protected physical Omega trace-state lane should
wait for lane 2 and lane 5, because its Ward identities require the
brane-defect QME, non-scalar class, and centrality homotopies.

## Verification run for this report

Command run after writing:

```bash
git diff --check -- reconstitution/swarm-2026-04-30-agent-349-next-lane-priority-queue.md
```

Result: passed with empty output.

Because the report was a newly added file, I also checked the file content with:

```bash
git diff --no-index --check -- /dev/null reconstitution/swarm-2026-04-30-agent-349-next-lane-priority-queue.md
```

Result: passed with empty output; exit status `1` is the normal no-index
diff-exists status for a new file.

After staging the report, run:

```bash
git diff --cached --check -- reconstitution/swarm-2026-04-30-agent-349-next-lane-priority-queue.md
```

Result: passed with empty output.
