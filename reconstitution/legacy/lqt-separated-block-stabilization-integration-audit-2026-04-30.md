# LQT Separated-Block Stabilization Integration Audit

Date: 2026-04-30

Agent: 302

Scope: report-only audit of the LQT separated-block stabilization theorem
surface.  No TeX was edited.

## Verdict

No live manuscript contradiction remains between the stable block-sum Hopf
projection, the separated-block finite-rank zigzag, the failure of raw
same-rank deletion, and the collision coderivation \(\Gamma_N\).

The current manuscript correctly fences the theorem-grade projection as the
stable block-sum Hopf Eulerian idempotent
\[
  P_{1\mathrm{cyc}}=\log^*(\operatorname{id})
  =
  \sum_{m=1}^{L}\frac{(-1)^{m-1}}{m}
  (\operatorname{id}-u\epsilon)^{*m}.
\]
It also says explicitly that the fixed-rank operation which keeps one-cycle
tensors and deletes multicycles is not a chain map.

The remaining integration weakness is not a contradiction.  The manuscript
names the separated-block stabilization zigzag, but the explicit maps
\(\alpha_{M,K,L}\), \(\beta_{M,K,L}\), and the total separated rank
\[
  B(K,L)=\max(K,L+2),\qquad M=L\,B(K,L)
\]
remain only in
`reconstitution/lqt-fixed-rank-to-stable-hopf-bridge-construction-2026-04-30.md`.
If the manuscript is meant to contain the finite-rank bridge as a theorem, the
snippets below should be inscribed.  If the bridge may stay in the
reconstitution ledger, no TeX correction is mandatory.

## Anchors Checked

- `main.tex:1873-1885` separates Procesi--Razmyslov coordinate invariants from
  the LQT cyclic-homology template.
- `main.tex:1887-1902` states Loday--Quillen--Tsygan only as an external
  stable template.
- `main.tex:1903-1986` states and proves the stable Eulerian finite-window
  LQT projection in the stable block-sum Hopf CE window.
- `main.tex:1988-2017` fences same-rank deletion and records
  \(\Gamma_N=d_{\mathrm{same}}F_N-F_Nd_{\oplus}\).
- `theorem-lanes.tex:2079-2131` records the finite-window LQT acceptance datum,
  stable Hopf idempotent, same-rank failure, \(\Gamma_N\), and scalar-Koszul
  quotient.
- `open-obligations.tex:143-197` records the same repaired LQT comparison and
  the same same-rank obstruction.
- `claim-strength-ledger.tex:392-426` marks the LQT component theorem-grade
  only in the Koszul-window stable single-cycle image and false for same-rank
  multicycle deletion.
- `reconstitution/lqt-fixed-rank-to-stable-hopf-bridge-construction-2026-04-30.md:25-53`
  constructs \(B(K,L)\), \(M\), \(P^{\mathrm{sep}}_{M,K,L}\), \(\alpha\), and
  \(\beta\).
- `reconstitution/lqt-fixed-rank-to-stable-hopf-bridge-construction-2026-04-30.md:220-277`
  identifies the same-rank fold obstruction \(\Gamma_N\) and the missing
  all-window collision homotopy.
- `references/primary-sources/lqt-tsygan-source-anchors-2026-04-30.md:44-50`
  records LQ84 Theorems 6.2 and 6.9 as the stable source anchors.
- `references/primary-sources/lqt-tsygan-source-anchors-2026-04-30.md:91-105`
  records that LQ84 does not prove the manuscript's finite-window dg map,
  scalar quotient, or open \(A_\infty\) transfer.

## Attack-Heal Audit

### A1. Stable Hopf projection versus same-rank deletion

Status: healed.

The theorem in `main.tex:1916-1928` defines \(P_{1\mathrm{cyc}}\) inside the
stable block-sum Hopf CE window.  The proof at `main.tex:1967-1985` uses
block diagonal sum before the Hopf logarithm and kills decomposable multicycle
products by the Stirling-number Eulerian calculation.  This is the correct
stable cumulant projection.

The false projection is separately named as \(P_{\mathrm{del}}\) at
`main.tex:1988-2003`.  The displayed computation
\[
  P_{\mathrm{del}}d_{\mathrm{CE}}
  (\Theta_1(a)\wedge\Theta_1(b))
  =
  \pm\Theta_1(ab-(-1)^{|a||b|}ba),
  \qquad
  d_{\mathrm{CE}}P_{\mathrm{del}}
  (\Theta_1(a)\wedge\Theta_1(b))=0
\]
prevents the reader from identifying the Hopf logarithm with same-rank
cycle deletion.

### A2. Separated-block zigzag

Status: concept present; theorem data not fully inscribed.

The manuscript states that the theorem-grade finite-rank bridge is the
separated-block stabilization zigzag at `main.tex:2003-2006`,
`theorem-lanes.tex:2118-2120`, and `open-obligations.tex:189-190`.
The construction report gives the missing data:
\[
  P^{\mathrm{sep}}_{M,K,L}
  =
  \beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L},
  \qquad M=L\max(K,L+2).
\]
This is a strict chain idempotent on the separated-block subcomplex because
different diagonal blocks commute as Lie subalgebras.

No text currently asserts that the separated-block zigzag is the same as a
one-block fixed-rank endomorphism.  The gap is only that the manuscript does
not yet display \(\alpha\), \(\beta\), or \(M\).

### A3. Same-rank deletion failure

Status: healed.

The failure appears in all manuscript-facing LQT rows:

- `main.tex:1988-2003`;
- `theorem-lanes.tex:2114-2118`;
- `open-obligations.tex:185-189`;
- `claim-strength-ledger.tex:409-412`.

No remaining TeX search hit asserts that raw same-rank deletion is a chain map
or a chain-homotopy model for \(P_{1\mathrm{cyc}}\).

### A4. Collision coderivation \(\Gamma_N\)

Status: healed in theorem/proof rows; claim ledger should cite it if the ledger
is meant to be self-contained.

The formula
\[
  \Gamma_N=d_{\mathrm{same}}F_N-F_Nd_{\oplus},\qquad
  \Gamma_N(\Theta_1^N(a)\wedge\Theta_1^N(b))
  =
  \pm\Theta_1^N(ab-(-1)^{|a||b|}ba)
\]
is present at `main.tex:2006-2016`, `theorem-lanes.tex:2119-2127`, and
`open-obligations.tex:190-197`.  The claim ledger records the same-rank
failure but does not name \(\Gamma_N\).  That is not a contradiction, but it
leaves the ledger less precise than the theorem surface.

## Exact Proposed Edits

No contradiction requires a TeX edit.  The following exact edits promote the
separated-block theorem data from the reconstitution report into the manuscript
and remove the remaining notational ambiguity between a per-block stable rank
and the total separated rank.

### Main Text

Replace `main.tex:2003-2006`:

```tex
  The theorem uses the stable block-sum Hopf cumulant
  projection before returning to a stable finite window.  The
  theorem-grade finite-rank bridge is therefore the separated-block
  stabilization zigzag.
```

with:

```tex
  The theorem uses the stable block-sum Hopf cumulant projection before
  returning to any finite rank.  More precisely, set
  \(B(K,L)=\max(K,L+2)\) and \(M=L\,B(K,L)\).  Let
  \[
    \beta_{M,K,L}\colon
    \mathsf H^{\mathrm{st}}_{K,L}(A_\psi)
    \to
    C_*^{\mathrm{CE}}(\mathfrak{gl}_M(A_{\psi,K}))^{\mathrm{sep}}_{\leq L}
  \]
  place the connected Hopf factors in mutually disjoint diagonal
  \(B(K,L)\)-blocks, and let
  \[
    \alpha_{M,K,L}\colon
    C_*^{\mathrm{CE}}(\mathfrak{gl}_M(A_{\psi,K}))^{\mathrm{sep}}_{\leq L}
    \to
    \mathsf H^{\mathrm{st}}_{K,L}(A_\psi)
  \]
  forget the block labels and read back the stable block-sum Hopf word.
  Then
  \[
    P^{\mathrm{sep}}_{M,K,L}
    =
    \beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L}
  \]
  is the strict finite-rank chain idempotent on the separated-block
  subcomplex.  This zigzag, not a same-rank endomorphism of one exterior CE
  complex, is the theorem-grade finite-rank bridge.
```

### Theorem Lane

Replace `theorem-lanes.tex:2118-2120`:

```tex
      differential gives zero.  The finite-rank bridge is the
      separated-block stabilization zigzag; a same-rank chain-homotopy
      bridge is blocked by the collision coderivation
```

with:

```tex
      differential gives zero.  The finite-rank bridge is the
      separated-block stabilization zigzag: with
      \(B(K,L)=\max(K,L+2)\) and \(M=L\,B(K,L)\), place each connected
      Hopf factor in a distinct \(B(K,L)\)-block by
      \(\beta_{M,K,L}\), read separated blocks back by
      \(\alpha_{M,K,L}\), and use
      \[
        P^{\mathrm{sep}}_{M,K,L}
        =
        \beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L}.
      \]
      A same-rank chain-homotopy bridge is blocked by the collision
      coderivation
```

### Open Obligations

Replace `open-obligations.tex:189-190`:

```tex
  zero.  The finite-rank bridge must use separated-block stabilization;
  the same-rank bridge is obstructed by
```

with:

```tex
  zero.  The finite-rank bridge must use separated-block stabilization:
  for \(B(K,L)=\max(K,L+2)\) and \(M=L\,B(K,L)\), the chain idempotent on
  the separated-block subcomplex is
  \[
    P^{\mathrm{sep}}_{M,K,L}
    =
    \beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L},
  \]
  where \(\beta\) places connected Hopf factors in disjoint diagonal
  blocks and \(\alpha\) reads them back as a stable block-sum Hopf word.
  The same-rank bridge is obstructed by
```

### Claim Ledger

Insert after `claim-strength-ledger.tex:412`:

```tex
  The finite-rank bridge is therefore the separated-block idempotent
  \(P^{\mathrm{sep}}_{M,K,L}
  =\beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L}\) with
  \(B(K,L)=\max(K,L+2)\) per occupied block and \(M=L\,B(K,L)\).  Folding
  separated blocks back into one same-rank block is obstructed by
  \[
    \Gamma_N=d_{\mathrm{same}}F_N-F_Nd_{\oplus},\qquad
    \Gamma_N(\Theta_1^N(a)\wedge\Theta_1^N(b))
    =
    \pm\Theta_1^N(ab-(-1)^{|a||b|}ba).
  \]
```

## Residual Theorem Surface

The separated-block theorem is closed at the finite-window level once the
maps \(\alpha\), \(\beta\), and the rank \(M\) are inscribed.  The same-rank
problem remains open as an explicit obstruction theorem: a positive same-rank
bridge would need a full partition-lattice collision homotopy
\[
  d_{\mathrm{same}}H+Hd_{\oplus}=-\Gamma_N
\]
with Koszul signs, stabilizers, scalar-Koszul quotient compatibility, and
Roos compatibility over the finite-window tower.  No current manuscript line
asserts that such a homotopy exists.

## Checks Run

```bash
sed -n '1,260p' CLAUDE.md
sed -n '1,320p' AGENTS.md
sed -n '1,260p' ~/ecosystem/INVARIANTS.md
sed -n '1,260p' ~/ecosystem/AGENTS-HARNESS.md
sed -n '1,220p' .agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,260p' ~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,320p' reconstitution/lqt-fixed-rank-to-stable-hopf-bridge-construction-2026-04-30.md
rg -n -F -e "LQT" -e "Loday--Quillen" -e "lambda_{\\mathrm{LQT" -e "P_{1\\mathrm{cyc}" -e "same-rank deletion" -e "separated-block" -e "Gamma_N" *.tex
nl -ba main.tex | sed -n '1840,2025p'
nl -ba theorem-lanes.tex | sed -n '2060,2140p'
nl -ba open-obligations.tex | sed -n '135,205p'
nl -ba claim-strength-ledger.tex | sed -n '360,455p'
nl -ba reconstitution/lqt-fixed-rank-to-stable-hopf-bridge-construction-2026-04-30.md | sed -n '1,330p'
nl -ba references/primary-sources/lqt-tsygan-source-anchors-2026-04-30.md | sed -n '35,115p'
```

No PDF build was run.  This was a report-only integration audit.
