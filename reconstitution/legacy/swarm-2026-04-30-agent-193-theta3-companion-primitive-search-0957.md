# Agent 193 - Theta3 Companion Primitive Search, 09:57 Refresh

Status: report-only; owned files staged; no commits or pushes.

## Stable Core

Agent 187's obstruction is correct for the finite row complex actually
supplied:
\[
  K^0_{theta_3,M}=0,\qquad
  K^1_{theta_3,M}=C E_{theta_3,M},\qquad d=0.
\]
The residual is \(R_{theta_3,M}=E_{theta_3,M}\), the scalar gate is zero,
and the cokernel functional \(\ell(E_{theta_3,M})=1\) proves a nonzero
finite-row \(H^1\)-class in that displayed subcomplex.

This is not a proof that \(E_{theta_3,M}\) is non-exact in the larger
local-functional complex.  A heal would require a new degree-zero primitive
or a larger degree-one companion-face row presentation.

## Best Possible Heal

The sign is forced by the row definition
\[
  E_{theta_3,M}=-K^M_{Theta_3}(zeta_{M,nu_3}).
\]
A primitive must satisfy
\[
  d_{ns,M}C_{theta_3,M}=-E_{theta_3,M}
    =
  K^M_{Theta_3}(zeta_{M,nu_3}),
\]
so the finite primitive matrix has entry
\[
  A^M_{E,C}=-1.
\]

Two actual sources could supply such a row, but neither is present.

1. CE-ancestor primitive:
   \[
     C^{CE}_{theta_3,M}=K^M_{Theta_3}(eta_{theta_3,M}),
     \qquad d_{CE}eta_{theta_3,M}=zeta_{M,nu_3}.
   \]
   This works only if the Hom-valued Bianchi term on `eta_theta_3` is zero,
   or all extra target-differential and bracket faces are supplied and
   canceled.

2. Local counterterm primitive:
   a degree-zero local counterterm
   \(C^{ct}_{theta_3,M}\in K^0_{ns,M}(I)\) with explicit differential
   \(dC^{ct}_{theta_3,M}=-E_{theta_3,M}\).
   The counterterm must live in the full-equivariant marked habitat or have
   its scalar projection computed directly.

The source-face alternative is cancellation rather than a primitive: restore
all omitted faces in
\[
  d_{CE}zeta_M=+zeta_{M,nu_3}+other faces
\]
and prove their signed row sum is zero.  That changes the residual vector;
it does not produce \(C_{theta_3}\).

## Required Labels And Gates

Any valid primitive row must supply:

- label `C_theta_3`;
- order `|Theta_3|_hbar=3`;
- finite degree `d_max=3`;
- the theta-row external labels
  `u_{a dt tensor z_1^2}`, `u_{b dt tensor z_2}`,
  `c_{B_theta,rho_{2,1}}`;
- the theta-row finite edge labels
  `P^{w,M}_{epsilon,L}`, `Delta^{w,M}_{epsilon,L}`, and `E_Weyl`;
- the full `gl(N|N)`-equivariant Brauer marker with cyclic supertrace zero;
- scalar condition `sigma_sc(C_theta_3)=0`;
- differential entry `dC_theta_3=-E_theta_3`;
- primitive transport
  \(P^{M,N}_{C,C}=1\) for \(N\ge3\), zero below the degree-three window;
- the matrix identity \(T^{M,N}A^M=A^NP^{M,N}\).

With these data the windowwise solution is \(c_M=1\), and
\[
  P^{M,N}c_M-c_N=0.
\]
The Roos \(\varprojlim^1H^0\)-class is then zero.  If the primitive
truncates by \(pi_{M,N}C_M=C_N+h_{M,N}\), the fixed-window obstruction is
gone but the remaining obstruction is \([h_{M,N}]\in H^0\).

## Valid Attacks

```yaml
- id: A1-193-01
  severity: 1
  status: valid
  lens: primitive existence
  target: theta_3 one-row package
  claim: The theta_3 obstruction can be healed by the currently supplied data.
  broken_step: No degree-zero candidate row is present in the supplied finite row complex.
  evidence_type: line_reference
  evidence_ref: tate-P1-hadamard-mittag-leffler.tex:2031 and Agent 187 report
  minimal_heal: Add C_theta_3 with dC=-E, or add companion faces changing the residual.
  residual: Larger local-functional exactness remains open.

- id: A1-193-02
  severity: 1
  status: undecided
  lens: CE ancestor
  target: possible C_theta_3 = K_Theta_3(eta_theta_3)
  claim: A source primitive eta_theta_3 exists with d_CE eta=zeta_nu3.
  broken_step: The current row table supplies zeta_nu3 as a face, not as a CE boundary with an ancestor eta.
  evidence_type: missing_data
  evidence_ref: tate-P1-hadamard-mittag-leffler.tex:1945 and scripts/finite_window_graph_array.py:795
  minimal_heal: Supply eta_theta_3, its CE differential, and all Bianchi companion faces.
  residual: If no eta exists, this route is blocked by source cohomology.

- id: A1-193-03
  severity: 1
  status: undecided
  lens: counterterm primitive
  target: possible local counterterm C_theta_3^ct
  claim: A Costello local counterterm has dC=-E_theta_3.
  broken_step: No actual local functional or d_M-expansion is supplied.
  evidence_type: missing_data
  evidence_ref: tate-P1-hadamard-mittag-leffler.tex:2017 and 2057
  minimal_heal: Supply C^M_{Theta_3,nu_3,w} with scalar projection, d_M boundary, and truncation.
  residual: The counterterm may not exist in the chosen local subcomplex.

- id: A1-193-04
  severity: 2
  status: valid
  lens: Roos compatibility
  target: future primitive tower
  claim: Fixed-window primitive existence is enough.
  broken_step: A primitive must also commute with finite-window truncation up to a zero Roos class.
  evidence_type: line_reference
  evidence_ref: tate-P1-hadamard-mittag-leffler.tex:1855 and 2061
  minimal_heal: Provide P^{M,N}, verify T A = A P, and compute [P c_M-c_N].
  residual: None for the identity/zero transport; open for any nonidentity primitive.
```

## Script Next Step

Do not change the current obstruction case.  Add future guarded cases:

- `theta_3_with_ce_ancestor_eta`, enabled only after
  `source_ancestor_verified`, `extra_faces_closed`, `scalar_zero`, and
  `truncation_verified` are true.
- `theta_3_with_counterterm_primitive`, enabled only after the payload
  includes `d_ns C_theta_3_ct = -E_theta_3`.
- `theta_3_with_complete_ce_companion_faces`, enabled only after all
  omitted CE faces and their signs are supplied and their residual vector
  sums to zero.

Each case should run the existing finite linear system \(Ac=-r\), then the
transport identities \(T r=r\), \(T A=A P\), and finally the Roos test
\([P c_M-c_N]\).

## Verification

Commands used were read-only inspections: `sed`, `rg`, `ls`, and
`git status`.  I did not run or edit `scripts/finite_window_graph_array.py`;
the user instructed that `tate-P1` and scripts were Agent 187 read-only
surfaces for this pass.  No build was run because this is report-only.

## Files Changed

- `reconstitution/finite-window-theta3-companion-primitive-search-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-193-theta3-companion-primitive-search-0957.md`

## Remaining Obligation

The exact missing datum is one of:

1. a CE ancestor `eta_theta_3` plus its Hom-valued Bianchi companion rows;
2. a local counterterm primitive with explicit `d_M` boundary and scalar
   projection;
3. the complete CE-source face table proving residual cancellation.

Until one is supplied, the one-row theta obstruction remains a finite-row
obstruction, not a solved order-three QME branch.
