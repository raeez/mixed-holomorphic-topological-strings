# Post-286-293 Integration Consistency Audit

Date: 2026-04-30.

Scope: report-only control-surface audit after the BMK, theta3, LQT,
radial, and stratified Weiss/Omega upgrades.  No TeX was edited.  No
build was run.

Mandatory sources read: `CLAUDE.md`, `AGENTS.md`, `main.tex`,
`theorem-lanes.tex`, `open-obligations.tex`,
`claim-strength-ledger.tex`, and reports 286-293.  During the audit,
reports 294-297 appeared in the worktree; their top-level findings were
skimmed only to avoid stale conclusions, and they confirm rather than
remove the findings below.

## Findings

### 1. BMK finite-window transfer language is still too strong on control surfaces

Status: stale claim / false-strength risk.

Agent 286 proves the strict support-local finite-current quotient is
obstructed.  Agent 292 sharpens this: the projected finite-window binary
action has a nonzero escape-return Jacobiator, and a finite
\(L_\infty\) repair preserving \(\mathcal P_{\le N}\) as surviving
finite moments is obstructed.

The main proposition has the right theorem surface:

- `main.tex:1333-1388`: current-limit data do not define
  \(H_{\chi,N}\); the finite-current obstruction vector is introduced.
- `main.tex:1408-1414`: \(\ell_2^{\mathrm{BM},N}=p_N[ix,iy]\) is only
  an arity-two Hamiltonian/Matlis coefficient comparison, not a homotopy
  transfer consequence.
- `main.tex:1513-1530`: the strict finite support-local quotient is
  impossible by Hamiltonian invariance.
- `main.tex:1603-1622`: the Darboux package correctly records current
  data, finite Matlis moments, arity-two comparison, and the obstruction.

Stale anchors:

- `theorem-lanes.tex:381-384` still describes the BMK lane as an
  explicit transfer-kernel construction obligation, not as the already
  sharpened current-limit/obstruction theorem.
- `theorem-lanes.tex:472-514` still says the next proof must construct
  the BM homotopy and identify the transferred arity-two operation; it
  omits the proved boundary-mode obstruction
  \(z_1^{N+2}\rho_{N+1,0}=-(N+2)\rho_{0,1}\) and the projected Jacobi
  escape-return obstruction.
- `claim-strength-ledger.tex:319-325` says "finite-window arity-two
  transfer" is proved data.
- `claim-strength-ledger.tex:608-625` says "proved finite-window BM
  transfer at arity two" and that the transfer uses the BMK homotopy.
- `main.tex:2672-2676` still says the proof uses "the finite-window BMK
  transfer" of the BMK proposition.

Proposed fix:

Replace every "finite-window BMK/BM transfer" phrase above by:

> BMK current-limit data, finite Matlis moment maps, and the arity-two
> output projection \(p_N[ix,iy]\), with strict finite-current transfer
> obstructed by \(\operatorname{Ob}^{\mathrm{BMK-curr}}_N\).

In `theorem-lanes.tex:472-514` and `claim-strength-ledger.tex:608-625`,
add the two obstruction facts:

- boundary-mode obstruction:
  \(z_1^{N+2}\rho_{N+1,0}=-(N+2)\rho_{0,1}\);
- projected finite-window Jacobi obstruction:
  \((N+1)(N+2)\rho_{0,1}\) on
  \((z_1^{N+2},z_2,\rho_{N,0})\).

### 2. LQT control files still collide \(W\) with the separate \(K,L\) windows

Status: unresolved parameter collision / claim-ledger propagation gap.

Agent 288 requires separate Koszul-weight and CE-length bounds:
\(A_{\psi,K}\), \(\Theta_{N,K,L}\),
\(\lambda_{\mathrm{LQT},K,L}\), and
\(N\ge\max(K,L+2)\), with \(W\) only as the specialization
\(K,L\le W\).  The current `main.tex` theorem uses this form:

- `main.tex:1929-1937`: \(\Theta_{N,K,L}\) and
  \(\lambda_{\mathrm{LQT},K,L}\).

Stale anchors:

- `theorem-lanes.tex:2088-2113` defines \(A_{\psi,W}\),
  \(\lambda_{\mathrm{LQT},W}\), and \(\Theta_{N,W}\), but then uses
  \(L\) in the Hopf logarithm and \(K,L\) in the stable range.
- `open-obligations.tex:143-172` has the same mix:
  \(\Theta_{N,W}\) and \(\lambda_{\mathrm{LQT},W}\), followed by
  \(\sum_{m=1}^L\) and \(N\ge\max(K,L+2)\).
- `claim-strength-ledger.tex:392-408` has
  \(\operatorname{Prim}^{1\mathrm{cyc}}_{N,W}\),
  \(\Theta_{N,W}\), and \(\lambda_{\mathrm{LQT},W}\), followed by
  \(N\ge\max(K,L+2)\).

Proposed fix:

Make the base theorem in all three control files use \(K,L\):

- \(A_{\psi,K}=A_\psi/F^{>K}A_\psi\);
- \(CC_{\mathrm{red},\le L}(A_{\psi,K})[1]\);
- \(\Theta_{N,K,L}\);
- \(\lambda_{\mathrm{LQT},K,L}=\Theta_{N,K,L}^{-1}P_{1\mathrm{cyc}}\);
- \(P_{1\mathrm{cyc}}=\sum_{m=1}^L(-1)^{m-1}J^{*m}/m\);
- \(N\ge\max(K,L+2)\).

Then add one sentence: if one integer \(W\) bounds both \(K\) and \(L\),
write \(A_{\psi,W}\), \(\Theta_{N,W}\), and
\(\lambda_{\mathrm{LQT},W}\) as abbreviations and require \(N\ge W+2\).

If Agent 295 is accepted into this same lane, also add the separated-block
finite-rank bridge \(P^{\mathrm{sep}}_{M,K,L}\) and keep the same-rank
folding obstruction \(\Gamma_N\) as open.

### 3. Stratified Weiss Cech/Roos obstruction is only partially propagated

Status: missing claim-ledger/control-surface propagation.

Agents 290 and 293 require the internal Weiss component to be the
Cech/Roos obstruction, not a generic \(\delta_{\mathrm{Weiss}}\).  The
current `theorem-lanes.tex` and `claim-strength-ledger.tex` include the
Cech cone and Roos class in prose, but the vector entries still hide this
data behind \(\delta_{\mathrm{Weiss}}\).  `open-obligations.tex` has the
Cech cone but not the Roos compatibility class near the vector.

Anchors:

- `theorem-lanes.tex:3120-3132` uses
  \(\delta_{\mathrm{Weiss}}\) in the internal vector.
- `theorem-lanes.tex:3141-3156` then defines the Cech cone and
  \(\mathfrak w^{\check C/R}_{V,\Omega,N,M}\) separately.
- `open-obligations.tex:1047-1050` defines only the cone part as
  \(\delta_{\mathrm{Weiss}}(V,\mathcal U)\).
- `open-obligations.tex:1147-1158` uses
  \(\delta_{\mathrm{Weiss}}\) in the internal vector with no nearby Roos
  class.
- `claim-strength-ledger.tex:805-835` uses
  \(\delta_{\mathrm{Weiss}}\) in the vector and then explains the cone plus
  Roos compatibility in prose.

Proposed fix:

Rename the vector component everywhere to
\[
  \delta_{\mathrm{Weiss}}^{\check C/R}
\]
and define it as the pair
\[
  \left(
    \{H^\bullet(\Delta^{N,M}_{V,\mathcal U})\}_{V,\mathcal U,N,M},
    \mathfrak w^{\check C/R}_{V,\Omega,N,M}
  \right).
\]
In `open-obligations.tex:1039-1050`, add the cohomological cone
differential and the Roos class, then use the same symbol in
`open-obligations.tex:1147-1158`.

### 4. The radial open-obligation row demotes the all-edge theorem to finite evidence

Status: theorem demotion violating Supremum Discipline.

The main theorem and theorem lanes state the stronger true theorem: the
edge strips are proved for all \((2,b)\) and \((a,2)\), not merely
certified through \(b=12\).

Correct stronger anchors:

- `main.tex:7285-7287`: complete edge families vanish by
  Proposition~\ref{prop:app-edge-pbw-telescoping}.
- `main.tex:8147-8148`: the primitive is proved for every edge bidegree.
- `theorem-lanes.tex:2546-2548`: edge classes vanish by the PBW
  telescoping theorem.
- `claim-strength-ledger.tex:920-928`: the all-\(N\) edge theorem is part
  of the proved radial surface.

Demoted anchor:

- `open-obligations.tex:1319-1324` says the current finite certificates give
  zero obstruction for edge families only through \(b=12\).

Proposed fix:

Rewrite `open-obligations.tex:1319-1324` as:

> Proposition~\ref{prop:app-edge-pbw-telescoping} proves the edge
> families \((2,b)\) and \((b,2)\) for all \(b\).  The finite
> certificates additionally cover the balanced diagonal through \((6,6)\),
> all non-edge bidegrees of total degree at most \(12\), and the listed
> total-degree \(13\) interior cases.

## Cleared Checks

- The Omega/QME parameter collision reported by Agent 290 at the QME
  residual has been repaired in the current checkout:
  `theorem-lanes.tex:2971-2978` now uses
  \(\hbar_{\mathrm{QME}}\) in both the coefficient extraction and the
  bracket.
- The centrality \(P_0\) parameter gate is coherent in the current checkout:
  `theorem-lanes.tex:3134-3169` and `open-obligations.tex:1048-1093`
  use \(P_{0,\hbar_{\mathrm{QME}}}\) for QME centrality and reserve
  \(\hbar_{\mathrm{W}}\) for reduced Weyl/Moyal current brackets.
- The theta3 lane is consistent with the exact obstruction and controlled
  enlargement target in reports 287, 291, and 294:
  `main.tex:8625-8880`, `open-obligations.tex:731-878`, and
  `claim-strength-ledger.tex:480-514`, `claim-strength-ledger.tex:861-918`
  all keep \(B^2_{02,20}\) as a missing local-functional column, not a
  constructed counterterm.

## Files Changed

- Added this report.
- Added `reconstitution/swarm-2026-04-30-agent-298-post-286-293-integration-consistency-audit.md`.

No TeX, script, source fixture, or build artifact was edited.
