# Agent 211 Report: BM Transfer / Native E2 Main Integration

Date: 2026-04-30.
Lane: BM transfer/native \(E_2\) manuscript integration.

## Claim Integrated

Agent 206's Bochner--Martinelli transfer is now integrated into
`main.tex` at the native holomorphic factorization discussion.  The
inscribed claim is finite-window and support-at-collision:
arity-two comparison is proved; a strict all-window \(E_2\) transfer is
not claimed until the ternary/collar obstruction and uniformity
obstruction vanish.

## Main Anchors

- `main.tex:1235`: `prop:finite-window-bm-native-e2-transfer`.
- `main.tex:1267`: full Bochner--Martinelli--Koppelman kernel with
  \(d\bar\eta_j=d\bar\zeta_j-d\bar z_j\).
- `main.tex:1303`: support-at-zero current
  \(\Delta_{a,b}\) and Matlis residue normalization.
- `main.tex:1318`: finite principal-part projection \(p_N\).
- `main.tex:1338`: normalized finite-window
  \(\bar\partial H_{\mathrm{BM},N}+H_{\mathrm{BM},N}\bar\partial
  =\operatorname{id}-i_Np_N\).
- `main.tex:1352`: Hamiltonian arity-two bracket.
- `main.tex:1362`: Matlis coadjoint arity-two action.
- `main.tex:1376`: first ternary cutoff/collar obstruction
  \(\operatorname{Ob}_3^\chi\).
- `main.tex:1388`: all-window obstruction vector
  \(\operatorname{Ob}^{\infty}_{\mathrm{BM}}\).
- `main.tex:1400`: two-variable Cauchy/principal-part face and
  VOA/Zhu firewall.
- `main.tex:1487`: native Darboux package now includes the finite-window
  BMK arity-two transfer.
- `main.tex:2154`: theorem-lane status remark reading the older BM lane
  together with the new finite-window proposition.
- `main.tex:2301`: main local theorem package includes the BMK arity-two
  transfer and ternary obstruction.
- `main.tex:8111`: concurrent
  `prop:theta-three-finite-window-acceptance-gate` preserved.

## Formulas Inscribed

Full Koppelman kernel:
\[
  K_{\mathrm{BM}}(\zeta,z)
  =
  \frac{1}{(2\pi i)^2}
  \frac{
    \overline{\eta_1}\,d\bar\eta_2
    -
    \overline{\eta_2}\,d\bar\eta_1
  }{r^4}
  \wedge d\zeta_1\wedge d\zeta_2,
  \qquad d\bar\eta_j=d\bar\zeta_j-d\bar z_j .
\]

Finite-window transfer:
\[
  \bar\partial H_{\mathrm{BM},N}
  +H_{\mathrm{BM},N}\bar\partial
  =
  \operatorname{id}-i_Np_N .
\]

Arity-two comparison:
\[
  \ell_2^{\mathrm{BM}}(f,g)
  =
  \partial_{z_1}f\,\partial_{z_2}g
  -
  \partial_{z_2}f\,\partial_{z_1}g
  \pmod{\C},
\]
\[
  \ell_2^{\mathrm{BM}}(z_1^pz_2^q,\rho_{i,j})
  =
  -(pj-qi+p-q)\rho_{i-p+1,j-q+1}.
\]

First obstruction:
\[
  \operatorname{Ob}_3^\chi(x,y,z)
  =
  p[H_{\mathrm{BM}}([ix,iy]-i\ell_2^{\mathrm{BM}}(x,y)),iz]
  +\text{cyclic Koszul terms}.
\]

## Claim Status

- Proved in manuscript: finite-window support-at-collision BMK transfer
  and arity-two Hamiltonian/Matlis coadjoint comparison.
- Not claimed: strict all-window \(E_2\) transfer.
- Remaining obstruction:
  \[
    \operatorname{Ob}^{\infty}_{\mathrm{BM}}
      =
      (\operatorname{ob}_{\mathrm{mom}},
       \operatorname{ob}_{\mathrm{collar}},
       \operatorname{ob}_3,
       \operatorname{ob}_{\mathrm{unif}}).
  \]
- Firewall preserved: no curve VOA, Zhu algebra, one-variable reduction,
  or \(b=0\) principal-part truncation.  The \(z_2\)-principal parts stay
  in the native \(\C^2\) system.

## Files Changed

- `main.tex`
- `reconstitution/swarm-2026-04-30-agent-211-bm-transfer-main-integration.md`

No edits were made to `theorem-lanes.tex` or to other reports.

## Commands

```bash
git status --short --branch
git diff -- main.tex
git diff --staged -- main.tex
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-206-bm-transfer-native-e2-construction.md
sed -n '1,260p' reconstitution/bm-transfer-native-e2-construction-2026-04-30.md
sed -n '1040,1335p' main.tex
rg -n -F -e "prop:finite-window-bm-native-e2-transfer" -e "Bochner--Martinelli--Koppelman" -e "d\\bar\\eta_j=d\\bar\\zeta_j-d\\bar z_j" -e "\\bar\\partial H_{\\mathrm{BM},N}" -e "\\operatorname{Ob}^{\\infty}_{\\mathrm{BM}}" -e "z_1\\cdot\\rho_{a,0}=-\\rho_{a,1}" -e "prop:theta-three-finite-window-acceptance-gate" main.tex
rg -n -F -e "curve VOA" -e "Zhu" -e "one-dimensional VOA" -e "principal-part line" -e "strict all-arity" -e "finite-window BMK" main.tex
rg -n -F -e "theta-three-finite-window-acceptance-gate" -e "mathsf E_{\\theta_3,M}" -e "d_MC^{\\mathrm{ct}}_{\\theta_3,M}" main.tex
git diff --check -- main.tex
git diff --cached --check -- main.tex
```

`git diff --check -- main.tex` and
`git diff --cached --check -- main.tex` passed.  No PDF build was run.
