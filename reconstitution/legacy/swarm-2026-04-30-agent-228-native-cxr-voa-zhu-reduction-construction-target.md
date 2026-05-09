# Swarm Report: Agent 228, Native CxR/VOA/Zhu Reduction Target

Date: 2026-04-30.

Owned files:

- `reconstitution/native-cxr-voa-zhu-reduction-construction-target-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-228-native-cxr-voa-zhu-reduction-construction-target.md`

No manuscript or script files were edited.

## Claim Attacked

The remaining curve chiral/VOA/Zhu surface: construct the exact
\(\mathbb C\times\mathbb R\) reduction target from the native
\(\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}\) formal
local theory, or name the exact obstructions.

## Evidence Read

- `CLAUDE.md`, `AGENTS.md`.
- Attack-heal skill and protocol:
  `/Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md`
  and `references/protocol.md`.
- Vol II rectification harness:
  `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- Manuscript anchors:
  `main.tex:80-184`, `main.tex:588-635`, `main.tex:1111-1452`,
  `appendix-matlis-principal-parts.tex:27-244`,
  `appendix-factorization-current-conventions.tex:36-397`,
  `theorem-lanes.tex:227-1025`, `theorem-lanes.tex:2135-2425`,
  `theorem-lanes.tex:3346-3385`, `local-dictionary.tex:1-375`,
  `claim-strength-ledger.tex:318-386`, `open-obligations.tex:260-306`.
- Existing reduction threads:
  `reconstitution/controlled-CxR-reduction-thread-2026-04-30.md`,
  `reconstitution/reduced-dirac-brst-zhu-thread-2026-04-30.md`,
  `reconstitution/native-E2-factorization-construction-2026-04-30.md`,
  and reports for agents 181, 182, 199.
- Vol II anchors:
  `chapters/connections/concordance.tex:1-260`,
  `chapters/theory/sc_chtop_heptagon.tex:120-320`,
  `chapters/connections/hochschild.tex:360-470`,
  `chapters/connections/hochschild.tex:660-800`,
  `metadata/theorem_registry.md:1-46`.

## Stable Core

The exact target is
\[
  R_{\mathbb C\times\mathbb R}
  =
  (\pi,B_{z_2},\pi_!,K_{\mathrm{red}},
   L_{\mathrm{red}},\langle-,-\rangle_{\mathrm{red}},H_{\mathrm{anom}}).
\]

The algebraic core is fixed:
\[
  \pi(t,s;z_1,z_2)=(t;z_1),
  \qquad
  \mathfrak h_{\mathrm{red}}
  =
  \mathbb C[[z_1]][[z_2]]/\mathbb C\cdot1,
\]
\[
  \mathcal P_{\mathrm{red}}
  =
  \operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)
  \subset
  H^2_{(z_1,z_2)}(\mathbb C[[z_1,z_2]])\,dz_1dz_2.
\]
The bracket, pairing, and coadjoint action are the native two-variable
ones:
\[
  \{f,g\}_{\mathrm{red}}
  =
  \partial_{z_1}f\,\partial_{z_2}g
  -
  \partial_{z_2}f\,\partial_{z_1}g,
\]
\[
  \langle\rho_{a,b},z_1^mz_2^n\rangle_{\mathrm{red}}
  =
  \delta_{a,m}\delta_{b,n},
\]
\[
  z_1^pz_2^q\cdot\rho_{i,j}
  =
  -(pj-qi+p-q)\rho_{i-p+1,j-q+1}.
\]

The brane image is
\[
  L_{\mathrm{red}}=\mathbb R_t\times\{z_1=0\},
\]
with both finite-\(N\) matrices retained:
\[
  \operatorname{ev}^{\mathrm{red}}_N(f)
  =
  \overline{\operatorname{Tr}f(X,Y)},
  \qquad X=\phi_1,\quad Y=\phi_2.
\]

## Destroyed Claims

- A native curve VOA/Zhu algebra on the \(\mathbb C^2\) object is false.
  The native object is the two-complex-dimensional Hamiltonian
  CE/factorization algebra.
- The quotient \(\mathbb C[[z_1,z_2]]/\mathbb C\to
  \mathbb C[[z_1]]/\mathbb C\) is false for this theorem.  It kills the
  Hamiltonian bracket and Moyal bivector.
- Literal \(z_2\)-residue keeping only \(b=0\) principal parts is false:
  \(z_1\cdot\rho_{a,0}=-\rho_{a,1}\).
- Vol II \(\mathsf{SC}^{\mathrm{ch,top}}\) and Zhu technology do not
  construct \(\pi_!\), \(K_{\mathrm{red}}\), the reduced pairing, or
  \(H_{\mathrm{anom}}\).  They are target interfaces after reduction.

## Exact Obstructions

The open obstruction vector is
\[
  \operatorname{Ob}_{228}
  =
  (\operatorname{ob}_{K,\infty},
   \operatorname{ob}_{\mathrm{fac},2},
   \operatorname{ob}_{\mathrm{fac},3},
   \operatorname{ob}_{\mathrm{pair}},
   \operatorname{ob}_{\mathrm{anom}},
   \operatorname{ob}_{\mathrm{VOA}},
   \operatorname{ob}_{\mathrm{Zhu}}).
\]

- \(\operatorname{ob}_{K,\infty}\): failure to choose compatible
  finite-window \(s,z_2\) fiber homotopies with
  \(d_FK+Kd_F=\operatorname{id}-i\pi_!\).
- \(\operatorname{ob}_{\mathrm{fac},2}\),
  \(\operatorname{ob}_{\mathrm{fac},3}\): failure of \(\pi_!\) to commute
  with binary and ternary factorization products after collar subtraction.
- \(\operatorname{ob}_{\mathrm{pair}}\): degree/sign/orientation mismatch
  between the pushed-forward BV pairing and the reduced residue pairing.
- \(\operatorname{ob}_{\mathrm{anom}}\): anomaly transport class, with
  scalar projection \(\hbar N[\bar c]\).
- \(\operatorname{ob}_{\mathrm{VOA}}\): failure of the reduced curve
  factorization product to have finite Laurent OPEs, vacuum, translation,
  and locality.
- \(\operatorname{ob}_{\mathrm{Zhu}}\): multiplicativity defect
  \(\zeta_\hbar(f*g)-\zeta_\hbar(f)\zeta_\hbar(g)\).

## Reduced VOA/Zhu Target

After \(R_{\mathbb C\times\mathbb R}\), the candidate reduced Dirac
vertex algebra has fields \(Z_1,Z_2,b,c\) with
\[
  Z_1{}^i{}_j(z)Z_2{}^k{}_\ell(w)
  \sim
  \frac{\hbar\delta^i_\ell\delta^k_j}{z-w},
  \qquad
  b^i{}_j(z)c^k{}_\ell(w)
  \sim
  \frac{\delta^i_\ell\delta^k_j}{z-w}.
\]
The BRST current is
\[
  j_{\mathrm{BRST}}
  =
  \operatorname{Tr}(c[Z_1,Z_2])
  +\frac12\operatorname{Tr}(b[c,c]).
\]
The square-zero check is the moment-map equivariance/Jacobi computation,
subject to the selected anomaly branch.  The Zhu target requires weights
\[
  \operatorname{wt}(Z_1)=0,\quad
  \operatorname{wt}(Z_2)=1,\quad
  \operatorname{wt}(c)=0,\quad
  \operatorname{wt}(b)=1,
\]
and the Capelli-shifted relation
\[
  QB=YX-XY+\hbar N I+[B,C],
  \qquad
  YX-XY+\hbar N I=0.
\]

## Files Changed

- Added `reconstitution/native-cxr-voa-zhu-reduction-construction-target-2026-04-30.md`.
- Added `reconstitution/swarm-2026-04-30-agent-228-native-cxr-voa-zhu-reduction-construction-target.md`.

## Verification

Commands run:

```bash
rg -n -e 'chiral' -e 'VOA' -e 'vertex' -e 'Zhu' -e 'z_2' -e 'principal' -e 'factorization' main.tex theorem-lanes.tex local-dictionary.tex
nl -ba main.tex | sed -n '1110,1460p'
nl -ba theorem-lanes.tex | sed -n '227,1030p'
nl -ba appendix-matlis-principal-parts.tex | sed -n '1,260p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '1,460p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex | sed -n '660,800p'
```

Post-write checks:

```bash
git diff --check -- reconstitution/native-cxr-voa-zhu-reduction-construction-target-2026-04-30.md reconstitution/swarm-2026-04-30-agent-228-native-cxr-voa-zhu-reduction-construction-target.md
rg -n -F -e 'ob_K' -e 'ob_Zhu' -e 'z_1\\cdot\\rho_{a,0}' -e 'R_{\\mathbb C\\times\\mathbb R}' reconstitution/native-cxr-voa-zhu-reduction-construction-target-2026-04-30.md reconstitution/swarm-2026-04-30-agent-228-native-cxr-voa-zhu-reduction-construction-target.md
git add -- reconstitution/native-cxr-voa-zhu-reduction-construction-target-2026-04-30.md reconstitution/swarm-2026-04-30-agent-228-native-cxr-voa-zhu-reduction-construction-target.md
```

No TeX build was run; the changes are report-only Markdown artifacts.
