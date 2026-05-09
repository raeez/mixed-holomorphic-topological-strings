# Agent 325: radial summary propagation final audit

Date: 2026-04-30.

Owned write paths:

- `reconstitution/radial-summary-propagation-final-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-325-radial-summary-propagation-final-audit.md`

No manuscript TeX or script file was edited.

## Claim attacked

Every summary mentioning the all-\(N\) radial/Weyl ordinary trace input must
state the accepted obstruction surface:
\[
  \Omega^{\mathrm{rad}}_{a,b}
  =
  [(T_{a,b},E^+_{a,b})]\in\operatorname{coker}B_{a,b},
  \qquad
  B_{a,b}(W)=(\partial W,C^+_{a,b}(W)).
\]
Positive closure is \(\Omega^{\mathrm{rad}}_{a,b}=0\), equivalently the
decorated PBW Stokes condition for
\[
  D^\square_{a,b}=C^+_{a,b}\partial_2.
\]
Failure is exactly a signed row
\[
  (\phi,-\lambda)\in\ker B_{a,b}^*,
  \qquad
  \lambda(E^+_{a,b})-\phi(T_{a,b})\ne0.
\]

## Result

Status: partial propagation after Agent 320.  Several of Agent 320's reported
defects are now healed in the current checkout, but summary-level stale
\(\mathcal C_{a,b}\)/left-cokernel language remains.

Correct surfaces now include:

- `main.tex:1055-1080`, `main.tex:2750-2779`,
  `main.tex:7414-7439`, `main.tex:7628-7642`,
  `main.tex:8294-8315`.
- `theorem-lanes.tex:2530-2555`, `theorem-lanes.tex:2670-2683`,
  `theorem-lanes.tex:2774-2783`, `theorem-lanes.tex:3646-3689`.
- `open-obligations.tex:512-529` and `open-obligations.tex:1350-1440`.
- `claim-strength-ledger.tex:987-1043`.
- `appendix-radial-parts-moyal.tex:965-1027`.

## Remaining TeX defects and patch targets

1. `main.tex:2434-2442`: early theorem narrative still names compatible
   \(K_{a,b}\) or left-cokernel vanishing for \(\mathfrak o_{a,b}\), without
   \(\Omega^{\mathrm{rad}}\), \(D^\square\), or signed rows.
2. `main.tex:7554-7563`: `cor:degree-zero-quantum-upgrade` still uses
   \(\mathfrak o_{a,b}=0\), functorial lifts, and left-cokernel language only.
3. `main.tex:8430-8435`: the \(T_{\mathrm{Ham},\hbar}\) factor is introduced
   with \(\mathfrak o_{a,b}\), homotopy, and left-cokernel language only.
4. `main.tex:8545-8548`: proof text names the radial-normalization
   obstruction but not the dual-potential/Stokes/signed-row form.
5. `theorem-lanes.tex:2718-2723`: componentwise coefficient-surface summary
   still says homotopy or left-cokernel theorem only.
6. `claim-strength-ledger.tex:103-109`: Stage A6a summary omits the exact
   obstruction surface.
7. `claim-strength-ledger.tex:207-215`: top claim table's radial/Weyl row is
   old \(\mathcal C_{a,b}\)-splitting language only.
8. `claim-strength-ledger.tex:300-308`: radial trace-diagram branch row is old
   cokernel/homotopy/left-cokernel language only.
9. `claim-strength-ledger.tex:577-585`: frontier item "Radial all-\(N\) image
   and all-bidegree homotopy" omits \(\Omega^{\mathrm{rad}}\), \(D^\square\),
   and signed rows.
10. `claim-strength-ledger.tex:1238-1270`: quantum Hamiltonian/Moyal item still
    closes at \(\operatorname{coker}\mathcal C_{a,b}\) and uniform contracting
    homotopy.
11. `claim-strength-ledger.tex:1288-1294`: componentwise quantum coefficient
    surface summary still says finite-certificate radial/Weyl gate and
    uniform-homotopy obstruction only.
12. `appendix-radial-parts-moyal.tex:888-939`: decorated Hodge obstruction
    theorem is still \(A_{a,b}=C^+|_{\ker\partial}\)-only; add the
    \(B_{a,b}\), \(\Omega^{\mathrm{rad}}\), and signed-row equivalence or an
    explicit forward pointer.
13. `appendix-radial-parts-moyal.tex:965-1027`: define the square-cell complex,
    prove \(\operatorname{im}\partial_2=\ker\partial\), and state
    \(\lambda D^\square=0\Rightarrow\lambda(R^{\mathrm{free}})=0\).
14. `appendix-radial-parts-moyal.tex:1061-1111`: distinguish the ordinary
    square-cell cycle mechanism from the decorated Stokes map
    \(D^\square=C^+\partial_2\).
15. `appendix-radial-parts-moyal.tex:1434-1440`: finite-\(N\) proof text still
    uses free corrections or left-cokernel obstruction only.
16. `appendix-radial-parts-moyal.tex:1820-1830`: final proof item should add
    `prop:app-radial-dual-potential-obstruction` and the \(D^\square\)
    criterion.

## Evidence

Read `main.tex`, `theorem-lanes.tex`, `open-obligations.tex`,
`claim-strength-ledger.tex`, `appendix-radial-parts-moyal.tex`, and Agent
303/314/320 reports.  The non-`swarm-*` report copies differ from their
`swarm-*` mirrors; the non-`swarm-*` Agent 303/314 files contain the fuller
post-Stokes theorem surface.  Current TeX line anchors were re-read after
detecting concurrent edits.

Commands run:

```text
rg
nl -ba
sed -n
wc -l
cmp -s
git status --short
```

No build was run.  This was a report-only audit.
