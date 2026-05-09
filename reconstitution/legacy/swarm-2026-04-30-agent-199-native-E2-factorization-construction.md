# Agent 199 Report: Native E2 Factorization Construction

Date: 2026-04-30.
Owned files:

- `reconstitution/native-E2-factorization-construction-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-199-native-E2-factorization-construction.md`

No TeX file was edited.

## Claim Attacked

Construct or sharpen the native holomorphic \(E_2\)/factorization object
on \(\mathbb C^2\), and prevent false identification with a curve VOA or
Zhu algebra.

## Verdict

The native object is the two-complex-dimensional CE/factorization algebra
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \bigl(
    \Omega_c^{0,\bullet}(B)\widehat\otimes
    (\mathfrak h\ltimes\mathcal P[1])
  \bigr),
\]
where
\[
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1,\qquad
  \mathcal P=\operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)
  \cong\mathfrak h^\vee_{\mathrm{cont}}.
\]
It is proved as a CE/factorization object with semidirect collision
operations.  The explicit Bochner-Martinelli transfer proof is open.  A
curve VOA/Zhu package is admissible only after controlled
\(\mathbb C\times\mathbb R\) reduction retaining \(z_2\)-modes or the
full principal-part coefficient system.

## Object Map

Fields on a holomorphic polydisk \(B\):
\[
  \alpha\in \Omega^{0,\bullet}(B)\widehat\otimes\mathfrak h[1],
  \qquad
  \beta\in \Omega^{0,\bullet}(B)\widehat\otimes\mathcal P[2],
\]
with differential \(\bar\partial\) and Hamiltonian BF interaction
\[
  I_{\mathrm{Ham}}=\frac12\int_B
  \langle\beta,\{\alpha,\alpha\}\rangle_{\mathrm{res}}.
\]
Compactly supported observable input:
\[
  \mathfrak g_B
  =
  \Omega_c^{0,\bullet}(B)\widehat\otimes
  (\mathfrak h\ltimes\mathcal P[1]).
\]
The mixed enhancement over \(U\subset\mathbb R^2_{\mathrm{top}}\) is
\[
  \mathfrak g^{\mathrm{mix}}_{U,B}
  =
  \Omega_c^\bullet(U)\widehat\otimes
  \Omega_c^{0,\bullet}(B)\widehat\otimes
  (\mathfrak h\ltimes\mathcal P[1]).
\]

The Hamiltonian bracket is
\[
  \{f,g\}
  =
  \partial_{z_1}f\,\partial_{z_2}g
  -
  \partial_{z_2}f\,\partial_{z_1}g
  \pmod{\mathbb C}.
\]
Constants are quotiented because \(X_f=0\) exactly for constant \(f\).
The principal-part action is determined by
\[
  \operatorname{Res}_0((f\cdot\rho)g)
  =
  -\operatorname{Res}_0(\rho\,\{f,g\}),
\]
and in monomials by
\[
  z_1^pz_2^q\cdot\rho_{i,j}
  =
  -(pj-qi+p-q)\rho_{i-p+1,j-q+1}.
\]

Collision operations:
\[
  [\alpha\otimes f,\beta\otimes g]
  =
  (\alpha\wedge\beta)\otimes\{f,g\},
\]
\[
  [\alpha\otimes f,\beta\otimes\rho[1]]
  =
  (\alpha\wedge\beta)\otimes(f\cdot\rho)[1],
  \qquad
  [\alpha\otimes\rho[1],\beta\otimes\sigma[1]]=0.
\]
Disjoint-polydisk factorization products are extension by zero on
compact supports followed by completed graded-commutative multiplication.

## Controlled Reduction Theorem Surface

The admissible shadow uses
\[
  \pi:\mathbb R_t\times\mathbb R_s\times\mathbb C_{z_1}\times\mathbb C_{z_2}
  \to
  \mathbb R_t\times\mathbb C_{z_1},
  \qquad
  \pi(t,s;z_1,z_2)=(t;z_1).
\]
A reduction datum must contain
\[
  \mathcal R_{\mathbb C\times\mathbb R}
  =
  (\pi,\kappa_{\mathrm{top}},\kappa_{\mathrm{hol}},
   B_{z_2},\pi_!,L_{\mathrm{red}},
   \langle-,-\rangle_{\mathrm{red}},
   \{-,-\}_{\mathrm{red}},H_{\mathrm{anom}}).
\]
The stable reduced coefficient system is
\[
  \mathfrak h_{\mathrm{red}}
  =
  \mathbb C[[z_1]][[z_2]]/\mathbb C\cdot1,
  \qquad
  \mathcal P_{\mathrm{red}}
  =
  \operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1),
\]
with the same two-variable bracket.  The brane image is
\[
  L_{\mathrm{red}}=\mathbb R_t\times\{z_1=0\},
\]
but the second matrix survives:
\[
  \operatorname{ev}^{\mathrm{red}}_N(f)
  =
  \overline{\operatorname{Tr}f(X,Y)},
  \qquad X=\phi_1,\quad Y=\phi_2.
\]
The induced CE/factorization shadow is
\[
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \bigl(
    \Omega_c^\bullet(I)\widehat\otimes
    \Omega_c^{0,\bullet}(D_1)\widehat\otimes
    (\mathfrak h_{\mathrm{red}}\ltimes\mathcal P_{\mathrm{red}}[1])
  \bigr).
\]
This is a theorem surface until the \(z_2\)-Dolbeault or residue
pushforward has support control, factorization compatibility, BV-pairing
degree checks, and anomaly homotopy.

## Attacks And Heals

1. False native VOA.
   Attack: a vertex algebra lives on a complex curve with vacuum,
   translation, finite Laurent OPEs, and locality.  The native object lives
   on polydisks in \(\mathbb C^2\) and has CE/factorization collision
   operations.
   Heal: keep \(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\) native; require
   a separate tuple
   \((\iota_L,\mathcal B_\perp,\mathsf R_{L,\mathcal B_\perp},
   V_L,\mathbf1_L,T_L,Y_L,\zeta_{L,\hbar})\) before any VOA claim.

2. Naive \(z_2=0\) reduction.
   Attack: the one-variable quotient kills the Hamiltonian bracket and
   cannot match Moyal/Weyl.
   Heal: retain
   \(\mathfrak h_{\mathrm{red}}=\mathbb C[[z_1]][[z_2]]/\mathbb C\cdot1\)
   and the full two-index principal-part module.

3. Literal \(b=0\) residue line.
   Attack: it is not stable under the coadjoint action since
   \(z_1\cdot\rho_{a,0}=-\rho_{a,1}\).
   Heal: retain the full principal-part coefficient system.

4. Curve BRST/Zhu imported too early.
   Attack: the reduced Dirac BRST algebra needs OPE normalization,
   weights, \(Q_{\mathrm{BRST}}^2=0\), the Capelli shift, and anomaly
   matching.
   Heal: record it only after \(\mathcal R_{\mathbb C\times\mathbb R}\).
   The reduced Zhu relation is
   \[
     QB=YX-XY+\hbar N I+[B,C],
     \qquad
     YX-XY+\hbar N I=0.
   \]

## Anchors

- `main.tex:1099-1228`: constructed local Hamiltonian holomorphic
  factorization algebra.
- `main.tex:2703-2753`: Hamiltonian polyvector reduction and scalar
  quotient.
- `theorem-lanes.tex:381-511`: native holomorphic \(E_2\) collision lane
  and BM obligation.
- `theorem-lanes.tex:676-862`: controlled \(\mathbb C\times\mathbb R\)
  reduction.
- `theorem-lanes.tex:864-1002`: reduced Dirac BRST/Zhu surface.
- `local-dictionary.tex:170-370`: local taxonomy and vertex/OPE boundary.
- `claim-strength-ledger.tex:298-353`: claim status ledger.
- `reconstitution/native-E2-factorization-construction-2026-04-30.md`:
  full object map written by this agent.

## Files Changed

- Added `reconstitution/native-E2-factorization-construction-2026-04-30.md`.
- Added `reconstitution/swarm-2026-04-30-agent-199-native-E2-factorization-construction.md`.

## Verification Commands

```bash
shasum -a 256 materials/raw/2026-04-30-mixed-holomorphic-topological-strings-critique.pdf
rg -n "Dirac|BRST|Zhu|chiral algebra|native holomorphic|E_2|E2|factorization|obligation|reduction" theorem-lanes.tex local-dictionary.tex reconstitution materials main.tex
rg -n -F -e "curve vertex algebra" -e "Bochner-Martinelli" -e "mathcal R" -e "hbar N I" -e "rho_{a,0}" -e "mathcal F_{\\mathrm{Ham}}^{\\mathrm{hol}}" reconstitution/native-E2-factorization-construction-2026-04-30.md reconstitution/swarm-2026-04-30-agent-199-native-E2-factorization-construction.md
git diff --cached --check -- reconstitution/native-E2-factorization-construction-2026-04-30.md reconstitution/swarm-2026-04-30-agent-199-native-E2-factorization-construction.md
```

No PDF build was run because the changes are markdown-only reconstitution
artifacts.
