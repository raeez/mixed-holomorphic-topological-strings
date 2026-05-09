# Agent 345 theorem-surface final consistency pass

Date: 2026-04-30.

Scope: `main.tex`, `theorem-lanes.tex`, `open-obligations.tex`,
`claim-strength-ledger.tex`.

## Verdict

One contradiction was found and patched.  No surviving contradiction was
found among the componentwise quantum coefficient surface, radial/Weyl
decorated-Stokes surface, \(\theta_3\) fixed-window obstruction, BMK
pro-Matlis lane, native \(E_2\) taxonomy, normal \(\Omega\)-control, and
larger non-scalar Costello/QME frontier.

The patched contradiction was a stale edge-strip range in
`open-obligations.tex`: the componentwise item still said the edge
families \((2,b),(b,2)\) were only certified through \(b=12\), while the
body and lanes now prove all edge strips.  The text now says the
all-edge PBW telescoping theorem holds for \((2,b)\) and \((a,2)\), and
that the remaining problem is all-interior.

Patch anchor: `open-obligations.tex:516`--`open-obligations.tex:520`.

## Consistency checks

### Native \(E_2\) and BMK

Consistent.  The native object is the \(\C^2\) holomorphic
factorization/CE object, not a curve VOA:
`main.tex:1129`--`main.tex:1190`,
`theorem-lanes.tex:381`--`theorem-lanes.tex:407`,
`open-obligations.tex:224`--`open-obligations.tex:254`,
`claim-strength-ledger.tex:650`--`claim-strength-ledger.tex:693`.

The BMK lane is also consistent: current-limit data, finite Matlis
moments, arity-two projection, and the one-pair analytic pro-Matlis
retract are proved; strict native finite/all-window support-local current
transfer is obstructed by
\(\operatorname{Ob}^{\mathrm{BMK\mbox{-}curr}}_N\) and then
\(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\):
`main.tex:1260`--`main.tex:1488`,
`main.tex:1710`--`main.tex:1721`,
`main.tex:2582`--`main.tex:2596`,
`theorem-lanes.tex:474`--`theorem-lanes.tex:545`,
`open-obligations.tex:274`--`open-obligations.tex:310`,
`claim-strength-ledger.tex:323`--`claim-strength-ledger.tex:340`.

### Componentwise quantum surface

Consistent after the patch.  The componentwise theorem is exactly the
product
\[
  \mathfrak S_{\hbar,w}(I)=
  \mathcal K_{\mathrm{BV}}^w\times\{0_{\mathrm{sc}}\}
  \times A^{\mathrm{pp},w}_{\partial,\hbar}(I)
  \times T_{\mathrm{Ham},\hbar},
\]
with weighted BV convergence, balanced scalar zero on its habitat,
reduced weighted Moyal principal-part currents, and radial-gated
degree-zero trace comparison.  It is not a full non-scalar Costello
graph/QME theorem:
`main.tex:8432`--`main.tex:8562`,
`theorem-lanes.tex:2721`--`theorem-lanes.tex:2857`,
`open-obligations.tex:498`--`open-obligations.tex:545`,
`claim-strength-ledger.tex:1270`--`claim-strength-ledger.tex:1292`.

The minimal full-equivariant finite-window branch remains a named
exception, not evidence for larger graph packages:
`theorem-lanes.tex:2887`--`theorem-lanes.tex:2898`,
`claim-strength-ledger.tex:1320`--`claim-strength-ledger.tex:1341`.

### Radial/Weyl decorated Stokes

Consistent after the patch.  The controlling surface is
\[
  \Omega^{\mathrm{rad}}_{a,b}
  =[(T_{a,b},E^+_{a,b})]\in\operatorname{coker}B_{a,b},
\]
equivalently decorated PBW Stokes
\(D^\square_{a,b}=C^+_{a,b}\partial_2\).  Failure is exactly a signed
row \((\phi,-\lambda)\in\ker B_{a,b}^*\) with
\(\lambda(E^+_{a,b})-\phi(T_{a,b})\ne0\):
`main.tex:2452`--`main.tex:2466`,
`main.tex:2781`--`main.tex:2800`,
`main.tex:7391`--`main.tex:7488`,
`main.tex:8318`--`main.tex:8399`,
`theorem-lanes.tex:2549`--`theorem-lanes.tex:2719`,
`theorem-lanes.tex:3673`--`theorem-lanes.tex:3724`,
`open-obligations.tex:1355`--`open-obligations.tex:1454`,
`claim-strength-ledger.tex:996`--`claim-strength-ledger.tex:1043`.

Residual propagation note: `main.tex:2452`--`main.tex:2456` and
`main.tex:2781`--`main.tex:2785` still summarize the finite non-edge
certificate range only through total degree \(12\), while
`open-obligations.tex:1394`--`open-obligations.tex:1408` records later
total-degree \(13\) and partial total-degree \(14\) closures.  This is an
under-propagated summary, not a contradiction, because the main text does
not assert that the \(12\)-range is exclusive.

### \(\theta_3\) fixed-window obstruction

Consistent.  The first named larger-row test is a nonzero fixed-window
class in the supplied one-row scalar-zero complex
\(\mathcal Q^0_{\theta_3,M}=0\),
\(\mathcal Q^1_{\theta_3,M}=\C\mathsf E_{\theta_3,M}\), \(d_M=0\).
It is killed only by a CE ancestor, a scalar-zero local counterterm, or a
complete companion-face table, with finite-window/Roos compatibility:
`main.tex:8849`--`main.tex:8924`,
`open-obligations.tex:795`--`open-obligations.tex:838`,
`claim-strength-ledger.tex:941`--`claim-strength-ledger.tex:957`.

The tested finite routes are correctly obstructed rather than silently
accepted.  The lower source-coordinate candidate supplies source
exactness only; the Hom-valued Bianchi defect
\(\mathfrak b^2_{02,20}\), the matrix equation
\(A_D^2c=-r_2\), and the transport cocycle
\(\Delta^1_{M,N}=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N\) remain the
control surface:
`main.tex:8926`--`main.tex:9055`,
`theorem-lanes.tex:3444`--`theorem-lanes.tex:3611`,
`open-obligations.tex:839`--`open-obligations.tex:957`,
`claim-strength-ledger.tex:958`--`claim-strength-ledger.tex:994`.

### Non-scalar QME frontier

Consistent.  The larger theorem is not asserted.  Its exact gate is:
construct the scalar-contact filtration and filtered scalar projection,
kill \(o_{\sigma,w}^{(r)}\), build the curved bulk-to-defect kernel, kill
\([\operatorname{Ob}^{\mathrm{red}}_{w,\partial,\hbar}]\in
H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})\), and solve the
finite-window \(A^Mc=-r^M\) and Roos compatibility equations:
`main.tex:8613`--`main.tex:8847`,
`theorem-lanes.tex:2760`--`theorem-lanes.tex:2898`,
`theorem-lanes.tex:3373`--`theorem-lanes.tex:3765`,
`open-obligations.tex:546`--`open-obligations.tex:792`,
`claim-strength-ledger.tex:924`--`claim-strength-ledger.tex:940`,
`claim-strength-ledger.tex:1294`--`claim-strength-ledger.tex:1341`,
`claim-strength-ledger.tex:1365`--`claim-strength-ledger.tex:1406`.

### Normal \(\Omega\) and stratified trace

Consistent.  The \(\Omega\)-background is normal scaling on
\(N_LX=\R_s\oplus\C_{z_1}\oplus\C_{z_2}\) with \(t\) fixed, using
\(Q_\Omega=Q+\iota_{V_\Omega}\) and
\(Q_\Omega^2=L_{V_\Omega}\).  Localization supplies weights,
denominators, and candidate contractions; it does not itself supply the
Costello QME kernel, centrality homotopies, or a physical trace state:
`theorem-lanes.tex:2901`--`theorem-lanes.tex:3113`,
`theorem-lanes.tex:3115`--`theorem-lanes.tex:3370`,
`open-obligations.tex:1001`--`open-obligations.tex:1235`,
`open-obligations.tex:1258`--`open-obligations.tex:1334`,
`claim-strength-ledger.tex:755`--`claim-strength-ledger.tex:844`,
`claim-strength-ledger.tex:846`--`claim-strength-ledger.tex:922`.

The three parameters are separated consistently:
\(\hbar_{\mathrm{QME}}\), \(\hbar_{\mathrm{W}}\), and \(\hbar_\omega\).
A Weyl branch may set \(\hbar_{\mathrm{W}}=\hbar_\omega\); no branch
identifies either with \(\hbar_{\mathrm{QME}}\) without an explicit QME
calculation:
`open-obligations.tex:1060`--`open-obligations.tex:1082`,
`claim-strength-ledger.tex:831`--`claim-strength-ledger.tex:844`.

## Files changed

- `open-obligations.tex`: corrected the stale edge-strip certificate
  range in the componentwise quantum item.
- `reconstitution/swarm-2026-04-30-agent-345-theorem-surface-final-consistency.md`:
  this report.

## Claim-status recommendation

Current status should be kept as theorem-surface consistent after the
patch.  The next propagation target, if desired, is non-logical: update
the short `main.tex` finite-certificate summaries to mention the later
total-degree \(13\) and partial total-degree \(14\) radial certificates
already recorded in `open-obligations.tex`.
